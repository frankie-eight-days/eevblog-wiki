---
video_id: KXbz2KUr8HQ
title: EEVblog #619 - Dumpster Dive PABX Teardown
url: https://www.youtube.com/watch?v=KXbz2KUr8HQ
source: youtube-asr
timestamps: {"0": 1, "1": 19, "2": 41, "3": 54, "4": 69, "5": 92, "6": 108, "7": 121, "8": 134, "9": 147, "10": 162, "11": 173, "12": 189, "13": 202, "14": 216, "15": 232, "16": 251, "17": 267, "18": 279, "19": 293, "20": 305, "21": 324, "22": 337, "23": 358, "24": 380, "25": 400, "26": 412, "27": 428, "28": 449, "29": 468, "30": 478, "31": 493, "32": 510, "33": 525, "34": 542, "35": 558, "36": 577, "37": 589, "38": 604, "39": 623, "40": 637, "41": 649, "42": 666, "43": 677, "44": 691, "45": 704, "46": 718, "47": 733, "48": 748, "49": 760, "50": 773, "51": 789, "52": 806, "53": 822, "54": 841, "55": 856, "56": 872, "57": 885, "58": 898, "59": 910, "60": 928, "61": 944, "62": 959, "63": 973, "64": 989, "65": 1006, "66": 1018, "67": 1033, "68": 1049, "69": 1063, "70": 1079, "71": 1093, "72": 1108, "73": 1126, "74": 1147, "75": 1159, "76": 1173, "77": 1187, "78": 1203, "79": 1219, "80": 1234, "81": 1249, "82": 1262, "83": 1275, "84": 1292, "85": 1303, "86": 1316, "87": 1333, "88": 1349, "89": 1367, "90": 1381, "91": 1397, "92": 1414, "93": 1426, "94": 1439, "95": 1451, "96": 1462, "97": 1483, "98": 1497, "99": 1510, "100": 1523, "101": 1537, "102": 1551, "103": 1570, "104": 1587, "105": 1605, "106": 1618, "107": 1630, "108": 1646, "109": 1666, "110": 1685, "111": 1702, "112": 1722, "113": 1737, "114": 1750, "115": 1769, "116": 1784, "117": 1799, "118": 1816, "119": 1833, "120": 1848, "121": 1861, "122": 1875, "123": 1888, "124": 1902, "125": 1914, "126": 1929, "127": 1941}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. And yes, I'm actually letting some people watch this well live, not through my live cam setup yet, but through my new Dropcam. There it is. Up there. So, hi to everyone watching at the moment. Now, I've got one of these

**Dave Jones:** new high-definition Dropcams cams. It's a Wi-Fi webcam that hooks up to and streams live to the net. So, the link is down below eevblog.com/live if you want to well, watch me 24/7 when I'm here anyway. So, I've turned the mic on.

**Dave Jones:** Ordinarily, the mic's not on, but anyway, that's an aside. So, I'm not sure how many people are watching me at the moment, but anyway, here we go. Teardown. I scored these just the other day from the dumpster room. If you're following on

**Dave Jones:** Twitter, I posted a photo of these. And what they are is a digital PABX system. Obviously, someone in the building here has decided to move out or replace it or shut down or whatever, and they've dumped all these gear, Panasonic and NEC

**Dave Jones:** stuff. So, we what we have here is a digital super hybrid system. It's a KX TD816AL, and this is a TVP 100 voice processing system. And so, this voice processing system has inboxes and things like that. So, it's got 64 voicemail inboxes. So, I

**Dave Jones:** expect some digital recording stuff inside this. And and this is the actual and I believe this NEC unit down here is the actual line interface unit. It supports two lines with six digital extensions or something like that. I'm

**Dave Jones:** not really big on my PABX system. So, someone with more knowledge might know how all these things work and go together. I'll post links down below anyway. So, this digital super hybrid system here, it's designed to hook up to

**Dave Jones:** these digital super hybrid phones. You may have seen this before. I got this from the dumpster a long time ago. I think I may have even now included it in a teardown or something. I'm not entirely sure. Anyway,

**Dave Jones:** so they're obviously throwing these away back then. That was a long time ago. That was like 9 months ago or something like that. But, this is one of the units which hooks up to one of these systems designed for, you know, sort of

**Dave Jones:** a medium size office, maybe with, you know, because it's a 64 voicemail inbox, this one. So, up to 64 users with their own voicemail inbox. There were multiple versions of these NEC line interface units down there. So, they could have

**Dave Jones:** had many lines with different switching. In fact, they probably would have. There were about four or five of these down here, but I only nabbed one of them because, well, a some of them were like had their guts just spewed out all over

**Dave Jones:** the all over the garbage room floor. Anyway, let's crack these open and have a look what's inside. I suspect lots of combination of DIP. And I'm not sure what vintage these are, but probably DIP with some surface mount technology.

**Dave Jones:** Lots of digital recording. I mean, this one's a voice processing system with a 64 inboxes. I expect there to be, you know, digital recording. What's it going to store it in? Some SRAM, SDRAM, something like that, I suspect. So,

**Dave Jones:** that'll have some decent processing in it. This will be like a line interface type unit. And this one here, digital the actual phone system itself. I'm not sure. It looks like it's got some sort of module things on the top. I don't

**Dave Jones:** know. Anyway, let's crack them open. So, the first one is this digital hybrid system KX-TD816AL. This is like the main controller, made in Japan. Beautiful. And yeah, as I said, it looks like they got like some modules on the top or something like

**Dave Jones:** And along the bottom they've got RS232 old school RS232 interface. They've got a paging output. So that'd be an an audio output. External music. So you can feed in your music for your on hold crap and stuff like that. Normal clear.

**Dave Jones:** Actually clear the system, the firmware and stuff like that. And to reset system make sure clear switch is on. That's just like a four pin molex connector or something like that. And 240 volt in. And that's it. And clearly this port

**Dave Jones:** here is designed These are like the interface modules. So this port here looks like just covers all the cables coming out here. So they will looks like they wire into here in the two modules and then all the pairs come out.

**Dave Jones:** Actually I expected more uh IO than this, but it's just got uh things that says uh two CO and PFT ports over here. Um so yeah, not much at all. And then this one over here will be exactly the

**Dave Jones:** same. So I mean they've you know for a big system you probably need multiple units of these. So they've got some screws on here. And I expect these modules to just pop off the top. And it looks like everything just um you know

**Dave Jones:** these things are designed for servicing and access and stuff like that because it's just got screws in here and these just pop open like that. Uh these ones aren't held captive. But the other ones were and uh they've got nice little springs on those

**Dave Jones:** too. Nice. I like that. Um and yeah and there's a hinge on the back here. So this whole cover Well, there we go. Whole cover will just lift off. So it looks like I don't even Although there's boards in there. Let's let's

**Dave Jones:** start out with these ones on the top. So here we go. Let's pop the hood on these. And oh ah No. Fail. I undid the screw and Oh, there we go. Oh, duh. Look at that. Nice. Okay. That's beautiful.

**Dave Jones:** Huge multiway ribbon cable coming out of there. Check out the ferrite. Check out the size of that bloody ferrite. That is enormous. Absolutely enormous. Trying to uh uh do some EMC there. And uh this is What is this? It's a 4CO line unit.

**Dave Jones:** There you go. So, hence we had those uh two ports each. So, I presume we can just No, it looks like we have to pop this cord on here. All right, here we go. Okay, now we're talking. Okay, this is interesting.

**Dave Jones:** Check out all the uh all the uh plastic is that yellowed, by the way. Uh the old plastic like this turns yellow. So, this could be substantially older. It could be cuz it heats up uh which would do it even

**Dave Jones:** sooner, I believe. Ooh, I can see some uh gas discharge tubes down in there. Anyway, um yeah, look. Here's our Here's our lines. So, yeah, uh CO 1 and 2 3 4 external line 1 external line 2 4

**Dave Jones:** uh up to eight. Hence, we had the four two four-port units. So, this supports eight CO lines. And uh There we go. So, we can should be able to whip those out now. Nice and modular. Really like that. That is That is

**Dave Jones:** terrific. But, yeah, look at that. Look at that big-ass ferrite. I'll keep that, that's for sure. It's a 0.1-in header there for the door phone. And check it out. Caution, do not remove uh this cover except qualified personnel. Well, I'm

**Dave Jones:** Ah, broke off. Look at that. Hey, the ROMs. There we go. You can change the ROMs on the sucker, obviously, but you know, you've got to update the uh firmware in these things. And here's just a little module I pulled out next

**Dave Jones:** to those uh ROMs there. Check it out. Looks like we have ourselves a uh 16.384 MHz uh oscillator here. Looks like a, you know, a fairly schmick one. And parts that you've uh never heard of. Mitel Networks, unless you're in the trade. MT

**Dave Jones:** uh 89 uh 41 BP. And I looked that up, and it is a T1 trunk uh PLL chip. So, there you go. That's all the stuff, and there'll be a whole bunch of telecoms-related uh chips in here, which you wouldn't recognize the part

**Dave Jones:** number. Bet your bottom dollar on it. Okay, let's pop the hood on this four-line CO unit. I still don't know what CO uh stands for. Uh I don't know. You'd have to probably read the manual or be in the know, in the trade, to

**Dave Jones:** know what that sort of stuff meant. But, it's a lot of engineering which goes into these suckers. This whole thing, I mean, you know, how big is the design group at uh Panasonic that manufactures this? There we go.

**Dave Jones:** There's our line. That's what you'd expect. Uh you expect all the line interface stuff. We've got relays, got uh gas discharge tubes. Look at that. Yeah. Now we're talking. There we go. Looks like we've got ourselves a neon lamp, too.

**Dave Jones:** They're uh uh quite common for um on uh phone uh side of things for protection. So, uh and gas discharge tubes, L. They're little inductors there. Um got some MOVs, by the looks of it. So, a whole bunch of protection stuff with for

**Dave Jones:** all that lightning, you know, because uh when you've got these sorts of phone systems, even though they're not they're usually only all internal. Oh, no, this would be the one No, this is These would be the ones These would be the Yeah, the

**Dave Jones:** line interface units going to the exchange. So, yes, they do leave the building. So, these ones you know, lightning could strike them, whatever surges, all sorts of stuff. So, you know, faulting other equipment down the line. So, you got to make sure that

**Dave Jones:** all this is protected. And you'll notice these neat little custom hybrids there with something on the other side. They're probably like uh uh no, relay, it says. It's marked with relay there. So, these are little maybe little solid state relays or something.

**Dave Jones:** Weird. Yeah, try and buy those or get a data sheet on them. Well, it's actually a Murata part, so your odds might be a bit better than usual. Anyway, I had a quick Google of that, couldn't really find anything, but yeah, that's

**Dave Jones:** interesting, especially the big bulge on the other side. Look at that. You can get a whole bunch of useful parts out of these things. And if you can ever salvage something like this, I think we're going to find lots of useful

**Dave Jones:** stuff. Look at these, you know, top quality Omron relays. We've got some NAIS brand solid state relays here. You know, you the inductors you can rip out of these things. And you know, little telecoms transformers, you know, very nice stuff.

**Dave Jones:** There's a big ass filter cap on here just sitting out there on its lonesome. 2200 microfarads 16 volts. So, it's not a super cap, but is a big beast of a cap you wouldn't ordinarily expect to see on

**Dave Jones:** here. So, could be for you know, momentary line outages or something like that or really just some heavy duty filtering for the relay switching and stuff like that, just so it doesn't interfere with all the line and audio

**Dave Jones:** stuff. And here's the back of the board. Check it out. We got a whole bunch of surface mount stuff on the bottom. So, they've gone wave soldering, of course, on the bottom. You can You can tell they're wave soldered and not reflow

**Dave Jones:** solder those pads. It just looks entirely different. Got a lot more solder on there. So, these are gone These have been glued down and then gone through the wave solder process. Of course, they're serious about shielding these things. There we go. A big

**Dave Jones:** shielding plate on the bottom. And then this big That's sort of It's not mylar. It's some really tough insulating film on there just to make sure nothing arcs over. Nothing's going to arc through that through to the grounded shield. All right. Now, let's

**Dave Jones:** pop the hood on this thing. Couple of fuses here. A line fuses. They got line and neutral line fuses. Double fuse there. Really going to town. And I find it's always interesting to note things like screws, for example. You know,

**Dave Jones:** people don't think about those. But think about the designer of this thing. Somebody Whoever designed this had to, you know, hold this case together with a certain kind of screw. And then what screws are you going to use in this one?

**Dave Jones:** Well, you've already specified these in your bill of materials. So, exactly the same ones are used to hold these modules together. I just find it's interesting to note that sort of stuff. Okay, let's lift this thing up. Ta-da!

**Dave Jones:** We're in like Flynn. Look at that. Yeah, once again, more line interface stuff around here. Big ass mains transformer there. And looks like we've got a big super cap under there. And anyway, let's have a look. Now, the first thing

**Dave Jones:** I notice here is all this grounding system. Look at this. They got a big central plate or a couple of central plates here. All tied together. All crimped All crimped properly. Shake-proof washers. Everything. The transformer down here. This one goes down to this

**Dave Jones:** transformer and also up to here and this is a uh This has got like little fingers in there. So, they obviously like something like a grounding stake or something plugs into the outside of this Oh, no. Sorry. No, no. That goes through. I'll

**Dave Jones:** show you. No, no. Check this out. There we go. There we go. There's the matching There's the case on top and there we go. It's got a matching tab. So, this slots directly down into that. Very nice. When this lid goes on like that,

**Dave Jones:** uh that's that's just beautiful. That is beautiful design. I really like that. And they're serious about their ferrites, too. They got more there and there. There's another one up there. There we go. So, you know, they're not mucking around. And more ferrites on the

**Dave Jones:** ribbon cables. Look at those. There and there. Whoa, belt and braces. And they've got good quality Rubicon caps in there. Only 85°C although I'm not sure, you know, these are designed for office environments, things like that to be installed inside

**Dave Jones:** typically. So, you know, not a huge deal and probably at the end of the day not a huge power consumption on these things. So, we got ourselves our switch mode down here. Big heat sink. All largely spread out. Looks

**Dave Jones:** really good. Here's these two watt line fuses on the top. They've got one in the active and the neutral lines. They've gone to the effort to make their own plastic body to hold those in place and bring them up. And they've gone to the

**Dave Jones:** effort to uh do a big plastic uh standoff here for this. It's not even a power button. It's just a power LED and they've molded that into the case and brought it out and screwed it in and molded that plastic

**Dave Jones:** cover and uh goodness. And there's the main micro you probably haven't seen before. Toshiba TMP68301 and it's a 16-bit micro. Couldn't get a full data sheet. just a basic pinout and block diagram and stuff like that. Uh, the job maybe it's big in Japan, who

**Dave Jones:** knows. You'll notice though that the board layout, this is actually quite common to uh get the get these 0.1-in headers around here. So, this is for development and debugging. They can uh plug the emulator directly in there and

**Dave Jones:** debug all the code and everything else. So, you know, this isn't most likely not like a flash microcontroller with your serial that you're used to. So, they did you know, really old-school um sort of you know, emulator and development system for

**Dave Jones:** this. And we got our first glimpse of a date code to '01, so 2001. So, you know, about 13 years old. There's another one in here, '02. So, maybe 12 years old, something like that. But the design probably even dates back further than

**Dave Jones:** that. And that front door interface over here we talked about before, well that's got a Mitel chip you've never heard of. It's the MT8981. It's a digital switch specifically designed for PCM-encoded data streams. And in this case it's a

**Dave Jones:** multi-channel up to 128 64K bits per second channels it can handle split up into several parts. So, 32 of those, there's four of them and 32 of those channels combined to form a 2 megabit ST bus. So, I'll link in the data sheet for

**Dave Jones:** that one for those interested. And once again, the back of this daughterboard got surface mount stuff on it, you know, fair amount and it's all wave soldered as well. So, let's have a look at these inputs here. As we saw before, these are

**Dave Jones:** the extension lines. So, there's eight extension lines here. These go to the digital phone that we looked at. So, these are all the internal wiring. So, you'd expect less protection on these internal ones cuz you know, it's not

**Dave Jones:** it's not like you're going to get a lightning strike inside the building or something like that. Whereas the outside lines, these CO lines, there's four of those. So, let's have a look at how that translates to eight and four over here on the

**Dave Jones:** daughter board. Well, two, four, six, eight. Oh, no, sorry. Two, four, six, eight. So, there are eight line inputs and you'll notice that all that circuitry around there for those, there's really no major protection around those. So, there's no

**Dave Jones:** gas discharge tubes, there's no MOVs or anything like that. You know, there's not that huge requirement. Whereas these four down these ones down here which handle the four incoming lines which go to the which actually, you know, go outside the

**Dave Jones:** building to the exchange and well, here's your four channels here. I like two on each two on each connector there. So, once again, you got your big gas discharge tubes here and you've got your MOVs as well. So, you know, decent

**Dave Jones:** protection on there and you've got your line isolation transformers, too. And then these here are your individual channels. Once again, we've got eight of those for those eight internal lines which go to the phone. So, yeah, a couple of nice little tiny pitch surface

**Dave Jones:** mount parts down in there. Have to get in there, take a look, but obviously, is that like another line isolation transformer, perhaps? And then maybe some line drivers, something like that. So, there's a Japan Radio Corp NJN 319 is just a dual comparator. But, the

**Dave Jones:** interesting one is over here on this side. Ta-da! We have ourselves an MC14LC5480. Let's go to the data sheet. So, this is a real interesting part and as always, I'll link in the data sheet. And what is this PCM codec? So, it's basically got a

**Dave Jones:** DAC and an ADC in there and it's also doing uh some filtering as well. Like it does sine x on x stuff and like you know, companding and all sorts of stuff uh to convert. There's the There's the

**Dave Jones:** receive uh well, the receive line and well, it's the DAC, it's the output line, but I guess they've got uh receive because that's the That's the labeling on the other end. Anyway, transmit here, the T, which comes in and

**Dave Jones:** this comes to the ADC. So, I guess they're named based on the phone end and then we've got some filtering ADC and uh the transmit shift register, all this sort of digital side all goes off to your microcontroller. So, there you go. Very

**Dave Jones:** nice little chip. Does some pretty advanced uh filtering DAC, ADC all-in-one custom design for these um uh you know, PCM type uh phone applications. And they've got some really nice descriptions here that are worth reading and here we go, to

**Dave Jones:** digitize intelligible voice requires signal-to-distortion ratios of 30 dB over a dynamic range of about 40. This may be accomplished using a linear 13-bit ADC and DAC. Well, you know, that's a pretty hefty uh DAC. So, uh what they do, excess performance per

**Dave Jones:** data sample. Two methods of data reduction are implemented by compressing the 13-bit linear scheme to compress pseudo-logarithmic 8-bit schemes. So, there you go, the two companding schemes are uh mu-law uh 255, primarily that's North American uh standard and A-law

**Dave Jones:** used in Europe. So, all those into your phone systems will know exactly what I'm talking about, but yeah, and it goes on and on. So, this is rather interesting reading. And this big beast that uh all these codecs feed into here, I mean, you

**Dave Jones:** know, good luck getting data on that. I suspect had a very quick look, uh nothing popped up. So, yeah, like there's no manufacturer, probably some sort of uh custom uh cell device, custom ASIC, something like that, uh combining

**Dave Jones:** all the individual uh voice streams into um you you is that the uh main processor and everything else can actually manage. And the rest of it, there's another custom ASIC chip here. It's got a different number on it. There's another

**Dave Jones:** ROM, so that's probably another some sort of processor something like that. We've got some system memory over here. Um curiously, we've got a big super cap here plus we've got a battery backup. So, real-time clock, so the super cap maybe I don't know designed to

**Dave Jones:** keep the processor running so it can shut down gracefully. Who knows? And there's the wave soldering arrow for all the dip parts. They put them through the wave soldering. I'm not going to bother to take this board out. There could be some

**Dave Jones:** surface mount stuff on the bottom. Don't know, but anyway, yeah, the as always, the direction of arrow shows which way this board should travel through the wave solder machine. So, there you go. That's what's inside a main PBX

**Dave Jones:** controller that controls four sorry, eight different phones with four incoming lines by the looks of it. So, let's now go have a look at that voice processor which presumably attaches to this system as all part of one big system optional, of

**Dave Jones:** course. You don't have to get the voicemail service, but let's take a look at that. There's going to be some digital recording in that sucker. Now for the TVP 100 voice processing system KX-TVP 100. Oh, exciting. So, let's lift the hood on

**Dave Jones:** this sucker. And uh once again uh cabling on here. Exactly. Dead spider. There we go. Yes, like all products, this one has bugs. There's not much in the way of cable access. We've got two ports here on each of these

**Dave Jones:** cards in here an empty module slot here. Not sure what's supposed to go in there. There's no cable gland holes for the cables to come up or anything like that. So, maybe that's just some sort of other management or some board maybe that sits

**Dave Jones:** in between those or something like that, but really are nice. These come out as little two-card modules. Look at that. Really quite neat. Um got some surface mount stuff, double-sided load, and we've got all our usual uh line

**Dave Jones:** interface stuff there. I don't see any um uh huge protection devices in there, so presumably they're not uh going to outside lines. They're just connected to the other device internal, and this is all just held together by our uh

**Dave Jones:** headers. So, let's whip that apart. There we go. So, we've got a line interface board. Uh oh, yeah, there's a couple of uh couple of little uh neon lamps in there, so a bit of protection there, but like

**Dave Jones:** nothing, no big gas discharge tubes for lightning strikes and things like that. So, obviously only internal connection uh through to the other unit. We've got some sort of custom processor up here. It's got some Well, it may not be a

**Dave Jones:** processor. May just be uh something. It's got some memory attached to it, but yeah, don't even bother looking for the part number for that. So, some sort of uh interface board which takes the uh data stream and uh encodes it and uh

**Dave Jones:** decodes it. Um because you've got to uh not only uh not only record the voice coming in, you've got to play it back as well on on command. So, all of the uh voice and uh data and uh and all the

**Dave Jones:** control data goes through here. Hello, that looks for all the world like a hard drive. Uh have they forgotten to erase their stuff? Who knows? We may have all their company's phone calls. Oops. Classic. Check it out. Uh Toshiba 5-V IDE

**Dave Jones:** interface uh notebook hard drive. Hmm, could still read that. Although, you've got to expect it to be a proprietary uh encoding scheme. It's not like they're, you know, running Windows, and And is going to be like a FAT uh file system or

**Dave Jones:** something like that. Probably. I don't know, but it would be worth uh hooking up just to see if it was actually uh readable. And I guess with hindsight, well, the hard drive is the only thing that made sense. I was hoping that uh

**Dave Jones:** you know, we'd be able to get um you know, some really big ass uh digital recording hardware in here, but you can't beat uh you know, a consumer hard drive for uh you know, bang for buck in terms of

**Dave Jones:** that uh storage. So, really not surprising. So, there's not going to be anything too huge in here. No. In fact, uh it's boring as. Well, sorry to disappoint, but that's all she wrote, really. Yeah, it's all the magic's in

**Dave Jones:** the hard drive. We've got this Looks like that same uh 16-bit uh Toshiba processor again, and we've got the ROMs for that. Another custom chip up here, which once again has the uh Oh, there's a live spider. Live spider.

**Dave Jones:** He's He's over there. He just ran. Here we go. I'll provoke him. He just ran under there, but yeah, there are all these cobwebs. So, he's in there somewhere. Look at that. And the only thing interesting here is this uh MT8952.

**Dave Jones:** It's a HDLC uh protocol controller. And it's basically um formatting data in the X.25 uh format. Nothing fancy. Look, '96 vintage, 38th week. So, nothing uh you know, that's pretty much it. Not a huge amount of stuff. And you'll notice that

**Dave Jones:** uh this um uh micro custom uh ASIC or cell device over here also has that uh debugging emulator interface over here. So, obviously, you know, designed for uh they would solder on on the development boards during our prototyping and development and uh

**Dave Jones:** debugging. They would solder headers on there, and then they'd be able to uh tap in there and emulate that chip. And you'd leave it off, and then you can tap right into it. Excellent stuff. You got to design that stuff in. Otherwise, you

**Dave Jones:** know, it's a real dog to to do this. It's an essential requirement back in the day before well, everything's got an in-circuit serial programming header of these days. But hey, for these types of things, no way, Jose. That's the only

**Dave Jones:** way to do it. And last and maybe least, we have ourselves an NEC Zen Alpha. So, this one's a very curious, you know, there's like a mains cord uh going into it and basically uh you know, Jack all has one cable port

**Dave Jones:** and that's it. It's an empty box and something rattles inside. Oh. Got ourselves some uh SLA batteries there. Uh they would have seen better days, no doubt. But anyway, out they come. And uh what else is in here?

**Dave Jones:** Phone cord and some sort of interface board. No idea what that's doing. And metal plates. Yeah, this thing's just been hacked. There's a serial sort of uh port and a couple of plug-in boards and well, yeah, there's a whole bunch of

**Dave Jones:** line stuff down here. This is an interesting hotchpotch actually. There's, you know, not as well sort of designed or thought out as the other ones, really. But anyway, we've got some line stuff happening over here. Presumably, yeah, there's the CO again. So, we've

**Dave Jones:** got the uh the Yeah, we've got CO1, CO2 and then six ST ST1 through ST6 external speaker. Uh maybe that's for a PA thing or something like that. Yeah, or this could be an entirely separate uh unit perhaps, nothing to do with the

**Dave Jones:** Panasonic system maybe. Oh, yeah, So, to get like the uh spec sheet for this thing. And yeah, this seems to be like a complete PA back solution. Nothing to do with the Panasonic. And the manual is just as hotchpotch as the

**Dave Jones:** uh as as the design in here. Look, you know, they've sort of non-symmetrical and everything's just sort of, you know, random connectors placed all over the place. And I don't know. It's just these vertical riser boards. It uh it's all a

**Dave Jones:** bit how you doing. Not that impressed. Anyway, yeah, it's like got a couple of uh uh main line inputs. No gas discharge tubes there that I can see anyway. So, uh not nearly as much uh filtering not nearly as much uh line protection as we

**Dave Jones:** saw on the uh Panasonic anyway. But, uh yeah, I don't know. This one's just a bit crusty. These boards are all over the shop. But, this is something uh fa- familiar. There you go, Hitachi H8S. So, you know, um

**Dave Jones:** you know, that's uh pretty familiar IDT uh 507201s. And you know, we've got some serious flash happening there. And uh you know, that's yeah, who knows what that board does. And then there's a whole bunch of other boards. Look at these. I mean,

**Dave Jones:** yeah, what? This one's got battery backup. Oh, yeah, we could go to town. But, nothing hugely interesting happening here. So, that's a Oh, that's a um that's a CO uh expansion one. Uh what was that? This one? No, here we go.

**Dave Jones:** This is a CO expansion one. So, it gives you a couple of extra uh lines. So, you know, meh. Nothing exciting. I don't know. We've seen it all before in the Panasonic. Is that a Tamura? What is that? I don't know. Google that

**Dave Jones:** part number. I doubt you'll find anything. But, obviously uh some sort of main system uh processor, something like that. And here's what I'm talking about uh salvaging parts. There's an excellent 3 W isolated DC-to-DC converter, 24 V in,

**Dave Jones:** plus minus 12 V out. Uh 3 W, you'd definitely nab that. And that's the thing with these boards. If you've got the room, you would just keep all these boards in a box. So, if you're desperately short of a part on a

**Dave Jones:** weekend, you know, when the electronic shop's closed or you're working at midnight or something, you definitely need a uh you know, a 200 V 33 mic electrolytic cap. Yeah, it's old, but you could rip that out and reuse it. So,

**Dave Jones:** there you go. I won't go into any more detail on this uh NEC unit. Video's probably gone long enough, but there's a a look inside a couple of typical uh PABX uh systems that you'll find in a business, you know, quite old ones, sort

**Dave Jones:** of, you know, 10-15 year-old sort of uh voice systems, but typically these stay in place for a long time. So, they probably bought these 10 years ago and uh installed them and they've been using them for a decade um ever since. So, you

**Dave Jones:** know, only now that they've moved or maybe they have upgraded, maybe they you know, moving to all uh VoIP uh based systems or something like that. Uh who knows? But, yeah, old-school PABX's, not too old-old school, but you know,

**Dave Jones:** relatively that um sort of, you know, mid-to-late uh '90s uh 2000 type vintage technology. Anyway, I hope I you like you like that teardown. There are some uh high-res photos of this They're always linked in on the eevblog.com

**Dave Jones:** uh website. And my little uh drop cam camera has been recording this, so maybe I'll actually uh try and extract the uh data from that and uh uh you know, you can have a look at that. I'll post that on my old zone

**Dave Jones:** channel if I do that. Certainly won't go on this uh main channel, but hope you enjoyed it. Catch you next time.
