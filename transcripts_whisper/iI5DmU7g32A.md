---
video_id: iI5DmU7g32A
title: EEVBlog #823 - Rigol DSG815 RF Signal Generator Teardown
url: https://www.youtube.com/watch?v=iI5DmU7g32A
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 18, "2": 37, "3": 55, "4": 73, "5": 88, "6": 104, "7": 119, "8": 134, "9": 150, "10": 163, "11": 177, "12": 189, "13": 210, "14": 230, "15": 245, "16": 265, "17": 285, "18": 305, "19": 325, "20": 340, "21": 355, "22": 370, "23": 390, "24": 405, "25": 425, "26": 440, "27": 460, "28": 475, "29": 500, "30": 515, "31": 545, "32": 565, "33": 580, "34": 595, "35": 615, "36": 625, "37": 650, "38": 665, "39": 680, "40": 700, "41": 720, "42": 735, "43": 775, "44": 800, "45": 815, "46": 835, "47": 850, "48": 865, "49": 890, "50": 900, "51": 925, "52": 945, "53": 965, "54": 975, "55": 995, "56": 1010, "57": 1025, "58": 1040, "59": 1060, "60": 1075, "61": 1090, "62": 1110, "63": 1130, "64": 1145, "65": 1160, "66": 1180, "67": 1200, "68": 1220, "69": 1235, "70": 1255, "71": 1270, "72": 1285, "73": 1300, "74": 1315, "75": 1340, "76": 1355, "77": 1375, "78": 1395, "79": 1415, "80": 1430, "81": 1445, "82": 1465, "83": 1475, "84": 1485, "85": 1505, "86": 1525, "87": 1540, "88": 1560, "89": 1575, "90": 1600, "91": 1620, "92": 1650, "93": 1665, "94": 1685, "95": 1705, "96": 1720, "97": 1735, "98": 1750, "99": 1765, "100": 1790, "101": 1810, "102": 1825, "103": 1840, "104": 1860, "105": 1875, "106": 1890, "107": 1905}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Today we're going to take a look at the Rigol DSG815 signal generator, as opposed to a function generator. And if you don't know the difference, a signal generator is like a proper analog, in this case RF signal generator,

**Dave Jones:** from 9 kHz to 1.5 GHz, whereas a function generator these days is typically, almost all of them, direct digital synthesis. They're a digital generator and actually generate the waveform with a digital-to-analog converter. This thing doesn't do it. It's a proper RF signal generator and has the specs to match.

**Dave Jones:** So, we'll take a look inside. It's going to be lots of analog-y RF-type goodness, beauty. And thanks to the local Australian distributor, John South Addimona, who you've seen on the blog before, loaned me this little puppy for Teardown. And possibly we'll have a play around with it too, but we're just doing a Teardown today.

**Dave Jones:** And this is the 1.5 gig model, the 815. There's also the 830, which is a 3 gig bandwidth model. That, I believe, is the only difference. This one is about $2,000 US street price, which is not too bad for an RF signal generator

**Dave Jones:** of these sort of specs, and the 3 gig version is about $3,600 US street price. So, it looks all kind of funky with these big rubber surrounds on them, and very nice if you have to, well, I was going to say, if you have to drop it,

**Dave Jones:** if you did accidentally drop it, because it'll stop. Look, none of the RF connector and the knobs and everything don't actually protrude from the rubber, but, you know, which is great if it falls on its face, but otherwise, like here you can see the shadowing of the light and stuff like that.

**Dave Jones:** Not a big deal, but mate, you know, that's just my studio lights here up on the roof behind me that are doing that, but yeah, they do protrude just a little bit too far, but you can take them off, you can unscrew them, no big deal.

**Dave Jones:** We've got ourselves a nice big-ass end connector, of course, there's the low frequency output as well for modulation, because you can do all sorts of modulation and stuff like that. The keys on it are angled, check those out, so I, you know, like you actually push them down,

**Dave Jones:** you don't push them in. I can't actually push that in, it's like down like that, which is rather interesting, a little bit disconcerting at first, but I guess I'll get used to it. And the function keys, I don't believe this is a touchscreen, they also like push out.

**Dave Jones:** I can't push those in, if I, I think, if I, I don't know, I haven't powered this thing up yet, but if I don't go in, if I try to go in there like that, I push it straight on. It's weird, because you're generally used to pushing buttons straight on,

**Dave Jones:** and your finger goes, whoop, off to one side. Why have they done that? I don't know. And this one up here is a normal button, so is that one, but they're trying to be fancy-pantsy and differentiate them. Hmm, not sure I like it.

**Dave Jones:** Well, I'll tell you what, they're not mucking around on the back, look at what you get, you get the 10 MHz reference out, more importantly the 10 MHz reference in. I'm not sure what oscillator they've got inside this thing, I don't think it's like an ovenized or anything like that,

**Dave Jones:** it's probably just a TCXO. And more importantly, 10 MHz reference in, because if you've got lab frequency reference standard, you can plug that in. We've got LXI Ethernet, we've got USB device, USB host, we've got pulse in and out external modulator, signal valid, which is rather interesting, and trigger in.

**Dave Jones:** I don't know what these options here are. And as you can see, it's quite small and compact compared to a kind of equivalent one, which is my Marconi Instruments Slash Aeroflex 2023, which you've seen a teardown of as well, so basically very similar performance,

**Dave Jones:** except this one, the Marconi goes a bit lower in amplitude, well, a fair bit lower in amplitude, but the Rigol can go higher in amplitude. I think phase noise, which is one of the big specs, is quite equivalent, so, you know, look, big difference.

**Dave Jones:** Anyway, enough talk, you know what we say here on the EEVblog, don't turn it on, take it apart, bloody ripper. And this is always the best part. So satisfying. Of course, we could have taken off that nicely, but nah, we're making a statement.

**Dave Jones:** Alright, here we go, we may not see much, except a, you know, big-ass processor board, because all the RF goodness is probably going to be inside, well, it should damn well be inside some shielding cans, and yeah, well, that's boring as bat poo, isn't it?

**Dave Jones:** Although I tell you what, I don't mind it, it's nice and neat and tidy, isn't it? What are all these? There's obviously some posts in here for some option boards or something else, but look, oh, heat shrink on the coaxes here, very very nice attention to detail, they've tied them down, they're not flapping around in the breeze,

**Dave Jones:** very nice. Here's our power supply, it's nice and shielded once again, they've, attention to detail, they've tied down the cable up here so that when you slide on the case the wires don't get pinched, just, you know, it really is quite nice. Fan, airflow-wise, we've got vents on the side here, the fan actually

**Dave Jones:** pushes out this way, so it's sucking all the air in through the vents on this side, over the block, because any of the RS stuff that gets hot is basically going to be radiated from the internal block, and you can see the big-ass block

**Dave Jones:** down there. So that's the fun stuff that we want to take a look at, and let's have a look on the bottom. Ooh! Ooh! Now, one of the first things I notice, we'll check out the rest of this in a minute, and of course we'll take off

**Dave Jones:** the die-cast metal can, but check it out, we have a little option module, there it is, OCXO, that's an oven-controlled crystal oscillator. So that's nice, look, they've got a, like a card edge directly onto the board here, going right into the RF shield, that is fantastic, I really like that.

**Dave Jones:** And that's what that option is in the back, just plug it in. Very nice design, thumbs up. And we've got ourselves some PCB mount coaxial connectors right on the board, coming right out of the shield. That is absolutely brilliant, obviously designed to go through this cut-out

**Dave Jones:** with folded metal there, very nice attention to detail so that you don't cut your wires on the potentially sharp edge there. What they're for, I don't know, some option board on the top, I should have actually researched this before I started tearing it down.

**Dave Jones:** Anyway, you can see the center line of the PCB in there, and they've got the gold plating on the edges of the board too, so very nice attention to detail, so nothing escapes from this metal can. Fantastic. And all this stuff outside here, obviously power

**Dave Jones:** supply, these are all going to be, I don't even have to look at them, they're probably low drop-out regulators, more regulators up here, everything's going to be linear, none of this switch mode rubbish. So it looks like we have our power coming over here,

**Dave Jones:** that would come from a switch mode power supply, it's how they get the size down of course. But you won't find any switch mode converters on the main analog board itself, either outside the can or inside the can, definitely. Okay, looking at the spec sheet, there seems to be a pulse modulation option, so I'm going to assume

**Dave Jones:** that that will fit in here, having the RF coaxes coming up here, so that'd be the modulation, pulse modulation output, and digital control cable probably coming up here to the board. And let's pop the front panel off here, took off the rubber baby buggy bumpers there, and 4 screws here.

**Dave Jones:** Oh! Another nice design, look at this! There you go, PCI card edge connector. Oh! Thumbs up! Look at that! Beautifully modular, and the RF coming straight out of the brick. Beauty. And I'm not even going to bother tearing that down, because that's not what we're here

**Dave Jones:** for today. We're here for the RF can magic. And the power supply looks very nice, they're doing everything right, look at that, it's beautifully laid out, they've got protection, they've got a decent amount of input filtering and stuff like that, very nicely spaced.

**Dave Jones:** Airflow, you know, some celastic to hold stuff down, everything looks hunky-dory until... wah wah wah wah, Capzone brand! Ugh! Why? Like, this is not a bottom of the... I know they're trying to make a cheap-ish RS Sig Gen, like, you know, performance for the price, but come on, you don't have to use Capzone bloody caps, at least they're consistent

**Dave Jones:** all the way through, I'll give them that. And eagle-eyed viewers may have gone hey Dave, what's going on here with this earth pin? It's just flapping around in the breeze! Well, no it's not. It's actually a right-angle PCB mount job like that, and yes it does actually go through the traces

**Dave Jones:** right down, so no problems. And one thing I noticed, these little red permanent marker marks here, noting that for all the screws and things like that, not only for all the screws, but have a look at the chassis. Somebody's marked it off there, and I see

**Dave Jones:** this all the way around this thing. You know, the production operators either, you know, conscientious or it's part of their procedure when they assemble it to actually mark off with red every screw and every cable tie and everything that they've put in. Even the connectors!

**Dave Jones:** I mean look, you get it on the connectors as well. Yep, I've plugged that in, I've made sure that's okay. Or is that somebody else as a separate step coming around and checking it? Either way, I'm impressed. Now we could go and take out all these screws willy-nilly, and we will eventually

**Dave Jones:** but to get the actual board and the module out, some of them are marked with triangles like this. And if my hunch is correct, they will be ones that actually go right through and actually hold the board in. So have a look at that one.

**Dave Jones:** Ta-da! Yep. And what those marks show is part of the system engineering approach to this thing. The CAD designer who had to do the 3D model for this RF shield in die-cast can, machined aluminium can, then, not die-cast, I think it's machined aluminium

**Dave Jones:** and they had to put these marks in. So that shows that at that stage they already knew, okay, exactly where they were, exactly where they'd go through, exactly how they'd go into the chassis and everything else. So very nice. I know, yeah, that's probably the way to do it.

**Dave Jones:** You know, these days, ah, your CAD tools, they would have designed the whole blinkin' lot with all their 3D models. They would have even, you know, used something like the Altium Designer or some other PCB package, had all the 3D model in, they would have, you know, done all that and yeah, it's par for the course these days.

**Dave Jones:** Okay, I'll shut up. And here we go. You get all the correct screws out and hopefully it comes out. Ta-da! Oh, the BNCs at the back are a bit tricky, but voila. So look at that. Completely modular, all the functionality of this thing, all on one board,

**Dave Jones:** all in one big brick. Ah, beautiful. That'd be some decent cost saving on that, you know. No multiple boards to assemble, less internal wiring, less assembly cost, everything else. So that is beautiful. And I'll tell you what, not too shabby for version 1.00.

**Dave Jones:** Maybe they reset it for the production version. It'd have to be. You know, you're gonna have to re-spin this for R&D, surely. And my cordless screwdriver is down in the bunker, isn't it? Ah, in the middle of a much, much infinitely bigger teardown than this.

**Dave Jones:** In fact it's as big as one of my benches. So yeah, here we go. Oh dear. Alright, we've got one more. Ah, come on! Come on! Ta-da! And it's gonna pop out on the bottom, I think. We got it. Here we go. Will it lift?

**Dave Jones:** There might be a gasket. No, it's gonna lift straight off. We're in like Flynn! Oh yeah, look at that. Spartan 6 FPGA, wow! And yes, we do have gaskets on the bottom. Now I'll have to show you some sections up close, but you can see it is completely

**Dave Jones:** similar as all of these things are. And at the complexity of it, you might think, well that's kind of like the complexity of a spectrum analyzer, for example. This is just a basic signal generator. Well, if you've seen my Moconi signal generator teardown,

**Dave Jones:** ta-da! Here is the block diagram for that. And you can see that there is a whole bunch of stuff. Reverse power protection, step attenuators, frequency oscillators, modulation harmonic filters, everything! And that's what all of these, it's gonna be sort of like similar. We don't exactly

**Dave Jones:** know how Rigol have implemented it, because unfortunately Rigol don't include a nice block diagram like this in their documentation. Shame on Rigol! Come on! At least give us some technical stuff. But let's have a look at a few, just point out a few

**Dave Jones:** interesting things. Now here's our RF output here, and you can see this would be, as per the block diagram, this would be our reverse power protection. And you can see the signal just jump in between the shield in the die-cast can on top.

**Dave Jones:** And this section here, you know, probably like the output attenuator, you know, a multi-step attenuator, because this thing goes from plus 20 dB right down to minus 110 or something like, 105 or something like that. So not as it doesn't go down nearly as low as the Marconi one does, but

**Dave Jones:** still pretty decent though. You might be wondering, how the hell does the signal get in or out of this block? Well, it gets out. You can see the break in the shield here, and there's AC coupled across there. But how does anything get in?

**Dave Jones:** Look! It's completely shielded right around here. Aha! That's when you gotta go in here and have a look at some finer detail. See these little microvias down here that go from there to there? No coincidence that they're there, they're not random. There's actually a trace inside there, controlled

**Dave Jones:** impedance trace going from this chip, which we'll have a close look at in a second, because there's something naughty with it. And yeah, it runs inside, so it's completely shielded between the two cans. Excellent. And what have naughty Rigol gone and done? Look, mongrels!

**Dave Jones:** They've lasered off the part numbers on the chips, and they've numb these to a whole bunch of chips inside these things. So they don't want us innocent engineers tearing down our products and trying to figure out how it works. Come on! If anyone wants to bloody well reverse engineer this

**Dave Jones:** thing, they can. I mean, you know, it might slow down people for a few hours or a few days, but it's not going to stop them. Give us a break. And they've done that with this thing up here, next to the Spartan 6 FPGA.

**Dave Jones:** And you might be wondering, what is the Spartan 6 FPGA doing in here? I thought this was like entirely analog. Well, this is the low frequency output connector here, so this is doing all the low frequency modulation and stuff like that. So they're, you know, doing that digitally.

**Dave Jones:** So there's going to be a DAC in there, and that's probably what that puppy there is. It's probably a DAC. They have a good old-fashioned TL074 in there. Bloody ripper. So you can see that here's the output, and then we've got our output protection, we've got our output attenuator, and then

**Dave Jones:** we've got these four sections here. And these are rather interesting. Looks like, you know, some sort of filtering. Maybe they're switching in different band filters or something like that perhaps. And then next to that check this out, we've got something really important in here.

**Dave Jones:** How do you know it's really important? Well, look at all the cutouts around it. Why have they done that? Well, they're trying to eliminate thermal expansion on whatever that puppy is there. Or there could be something on the other side. I haven't actually looked, haven't taken the die cast can off the other side.

**Dave Jones:** Maybe we should do that. But yes, that little puppy there is obviously some sort of reference or something like that that they're really taking care of the Temco with. So that's nice attention to detail. You don't want any thermal expansion because, well, you know, this whole thing's going to heat up.

**Dave Jones:** But then when the PCB heats up, even if it's a top quality one, you're paying for low thermal expansion, but it's still going to have some thermal expansion, so that can actually expand the pins as well on the chip, and then that can actually

**Dave Jones:** affect the... that can add stresses to the internal die, and that can affect its performance as well. So I'm a little bit surprised to actually see that in here though, but nice work. And there's the other side, and we can see something interesting

**Dave Jones:** down on our isolated cutout there. Got ourselves two big-ass 150 ohm resistors. They might be in parallel for 75 ohms, and of course it's not 75 ohms impedance. What they're doing is they're... look at the size of them. They've got to be heaters, which is heating

**Dave Jones:** up that particular board, so that would be controlled. So they're... that's like a little mini oven in there. Very nice. Is that our main... that's not our main oscillator, because they've labeled that U, and that is not a oscillator package. If somebody can decode the SMD markings on that, then please do, but

**Dave Jones:** you know, probably some voltage reference, but they go into a lot of trouble. Anyway, back into the action down here. I'm not going to guess at all these components. I'm sure somebody will go to the trouble to take the photo of this. By the way, I will have high-res photos of

**Dave Jones:** this teardown on the board and all the sections available on evblog.com, link down below. Someone usually goes along and then marks all the blocks up for us. So yeah, I'll just crowdsource that. Bloody laser marked off the numbers again, mongrels. And then our signal travels along.

**Dave Jones:** Sorry about the shaky image, I need a dolly, don't I? And it travels along, does some more magic, heads on up here, up here, up, up, up, up, up. And once again you can see that the signal actually goes through a shielded inner layer there

**Dave Jones:** with a controlled impedance trace. And back to our wider shot again, and that's our modulation input, that modulation board. And then bingo, we've got some, what a lot of people call RF voodoo, it's just a distributed element filter. That's its official name, you can go Google that

**Dave Jones:** I'm sure, and have a look. Now it might look like magic until you actually realize what's going on here. It's basically just a filter, it's probably just a multi-stage low-pass filter. And what we've got, these pads here, these are actually capacitors, okay? So that's effectively a capacitor going down to ground.

**Dave Jones:** And then these little squiggles in here, they're actually inductors, so you've got a capacitor going to ground, then an inductor in series, then a capacitor going to ground. So it's an LC filter like that, and then you would have a little bit of resistance in here

**Dave Jones:** due to your controlled impedance trace. And it's basically just an LC filter, that's pretty much all it is. And they're doing a similar thing down here, but there can actually be subtle differences in the geometry of these things. You'll notice this one has a capacitor going down to ground, but there's also an inductor in series, okay?

**Dave Jones:** And you'll see that they're different shapes, that means they're different values, and then just a tiny little bit, even that little trace in there connecting to that, you know, that could be a resistor in series. Tiny little bit of inductance, and there's actually

**Dave Jones:** many different types, and I should actually have to link in some examples of these things. And you can actually see, you know, there's little subtle differences between how you implement this, it depends on the dielectric material, the board, the type of material, the dielectric

**Dave Jones:** constant, and the width of the trace, and the distance, all sorts of things. And there can be subtle differences, you can implement all sorts of unusual filter, bandpass and other type of arrangements using these distributed element filters. And why do they do it?

**Dave Jones:** Because, hey, it's cheap and easy, and there's software programs to spit these things out. I mean, the board's not cheap, you've got to have a nice, you know, controlled impedance, controlled dielectric board, you know, not just your regular Joe Bloggs, you know, FR4 from, you know, one hung low manufacturer.

**Dave Jones:** They would have specifically chosen the board material exactly for their purposes, and there's advanced programs you can get to actually calculate and design all these filters for you. So there's a whole bunch of stuff going on there, and this looks like it's probably a mixer or something like that

**Dave Jones:** perhaps, package? It's not the oscillator, I think I can get a part number on that, hang on. And there you have it, that's a ZCOM 3640, the Crow series cathode ray oscilloscope, thank you very much. It's a voltage controlled oscillator, VCO. And right up here

**Dave Jones:** next to the oven-controlled oscillator card edge connector, bingo, there is our main oscillator. 2 ppm general accuracy, but of course you plug in the oven-controlled oscillator and it's, you know, parts per billion. And interestingly, in addition to the Spartan 6 FPGA, right near the low frequency

**Dave Jones:** output here, we've got a Actel Pro Asic 3 FPGA, so what the hell? You know, unusual mix there, that's really bizarre. Anyway, here's some of the output protection as well, that's chock-a-block in there, check it out, that's a laser, removed the markings yet again,

**Dave Jones:** the mongrels. But generally speaking, on the other side of the board here, pretty much just all passives, nothing much doing there, huge amounts. So I won't go into detail, once again, high-res photos of both sides of this board available on the website if you want to check it out, but there you go, that's what's inside

**Dave Jones:** an RF section, this is what you're paying for, it's all, you know, analog RF magic. These parts are very expensive, you can't skimp on, you know, a good lot of these parts, they have to come from specific manufacturers and they cost you know, 50 bucks a pop or something like that.

**Dave Jones:** And that's why you can't make one of these things for a couple of hundred dollars, you know, you just can't do it. You've got to get the reputable parts, you can't just get rip-off parts from somewhere, it doesn't work, you don't get the performance.

**Dave Jones:** But overall I'm quite impressed by that, because Rigol are not going for their RF stuff, but they're certainly getting into it, and this is a pretty decent implementation, a physical design implementation, in fact it's really very nice. Shame we don't have a block diagram

**Dave Jones:** for it, that would have been really nice. But yeah, if you sit down for, you know, an hour or two, you might be able to figure out what all the blocks and all the parts do and things like that. But yeah, they've really gone to town,

**Dave Jones:** a lot of design effort has gone into this thing, and it's got reasonable specs as well. They're not going to, you know, they're not lead, they're not industry-leading specs by any stretch of the imagination, but you know, you get reasonable performance for the price, that's for sure.

**Dave Jones:** And the design quality, build quality, it looks like they've got someone there who knows what they're doing. Now if you're going to buy one of these by the way, or you know, any similar sort of RF product like this, it's nice to do a teardown like this, but if you're after, especially if you're buying a really

**Dave Jones:** ultra-high-end spec product, you don't want to be going, generally taking off the RF cans, because it could actually affect, very minutely, but could actually affect the low-level performance of this thing. So it might be likely that Rigol might have to, or might, you know, just as a matter of course, actually resend

**Dave Jones:** this back out for calibration once I'm done with this, taking it off, because you know, the torque of the screws on there and the gaskets can affect the, you know, the shield in between sections and things like that. So yeah, you're probably, especially like, probably not on

**Dave Jones:** this one, but you know, some of the more ultra-high-end ones definitely can have a real impact. And all right, why not? Because well, we didn't see the main processor. I know there's lots of processor aficionados out there. There it is, Freescale IMX283, one of these whiz-bang, you know, what is it, 6-800 MHz,

**Dave Jones:** 400 MHz or something, application processors, you know, high-end ARM. It's got all sorts of stuff built in, it's got all the LCD drivers, it's got everything else. There's our LCD ribbon going out there, and there's our front panel touch as well. And not much else doing.

**Dave Jones:** And of course we have our JTAG interface there, and I don't see, I usually get like a serial debug port on these things as well, but I don't see that doesn't, neither of those look like a serial debug port. So you know, usually you boot, you can boot these things up, hook up a, you know, regular

**Dave Jones:** to a PC serial port and have a look at all the boot, you know, console information as the thing boots, whatever OS it's using. But eh, doesn't seem to be one here. And a sneaky little 805.1 in there doing something with our PCI interface,

**Dave Jones:** PCI connector interface, not actually PCI, you know, standard or anything. But yeah, they're using the PCI connector. Something going over to that main board. Alright, let's plug it in and see if it works. I haven't actually powered up the thing, I don't even know if it worked

**Dave Jones:** out of the box, I literally tore it down. Didn't turn it on, I took it apart. So let's plug it in. It takes about 50 watts, so it's a reasonably power-hungry little piece. So let's plug her in. Universal voltage of course. Don't know what it takes

**Dave Jones:** on standby, I should actually test it. Hey! Winner winner, chicken dinner. Here we go, how long does it take to boot? Local boot in. Yep. Anyway. Hey, we're in like Flynn. There it is. Works a treat. Beauty. Alright, let's plug it in and see if we can actually get something out of the puppy.

**Dave Jones:** This won't be a review or a comprehensive test at all, but look, I got a nice RF cable with it. This doesn't actually, this doesn't usually come with it, I don't believe, but yeah, comes with its own spec sheet and everything. Beauty. And speaking of which, for all you CalCERT

**Dave Jones:** aficionados, I know you're out there, there we go. Yes, it does come standard with a Cal certificate. Beauty. Tell you what, I don't mind the interface at all, you know, you've got your frequency what you want, your level what you want, by default it's 1 gig and mine is 20 dBm

**Dave Jones:** and the RF output we can just switch off or on here, and then we can just switch our modulation off or on, and our low frequency as well, and then we can set it up and we've got a numeric keypad and we've got a real fair dinkin' knob

**Dave Jones:** so if we go up to frequency here, oh, there we go. Where's the marker? Where's the marker? Yeah, there we go, we've got a dot above it. But it wasn't obvious at first glance, it should have been, you know, but it wasn't. Why is the dot not up there permanently?

**Dave Jones:** Hmm. And here it is and this will not be a performance test by any stretch of the imagination, but I'm just showing you I've got the frequency at, well, the level, actually I'm going to change to 0 dBm, it was minus 2, but there you go.

**Dave Jones:** It's off by about 0.92 dBm, 0.9 dBm or thereabouts. I think the spec's about 0.5 dBm on the SIGGEN, don't quote me on that, but then you've got the scope as well, eh, whatever. There's our carrier, we've got a 1 gig carrier and here, there's our 2 gig harmonica, that thing

**Dave Jones:** and 2.5 as well. That's 1 gig at minus 10 dBm and let's go down lower. And that's down at minus 50 dBm carrier. And there's a minus 10 dB 1 gig carrier with some basic sine wave amplitude modulation there at what have we got set up?

**Dave Jones:** 10 kHz, so easy peasy. And if I change the depth down to 1% there on our modulation, bingo. It all works. So I didn't break anything, that's the main thing. Might have whacked it out of a cow a little bit. Half a bee's dick.

**Dave Jones:** So yeah, you've got a whole bunch of modulation there, AM, FM pulse modulation and there's options for that. We can do sweeps as well, that's very nice. And well, we've got our level and our frequency, it's all very nice to use. Turn your modulation off and on, turn your RF off and on.

**Dave Jones:** Beauty! Bob's your uncle, what more do you want? So there you go, I hope you enjoyed a look inside this Rigol DSG815 and apart from the caps on caps, it's pretty decent design and build quality it looks like, so definitely a thumbs up to that, apart from the caps, which is a thumbs down.

**Dave Jones:** But yeah, you know, it's par for the course these days. But yeah, when you're paying 2 grand for you know, a SIGGEN like this, you know, you expect Nichicon or some other, you know, Panasonic some quality caps in there at least, come on, don't skimp.

**Dave Jones:** I know you probably bought them caps on 1's by the zillion, and people are going to say, why harp on about the caps? I don't know, this is the only thing I really found wrong with inside the thing. It really is quite nice.

**Dave Jones:** So I haven't actually compared the specs on this thing compared to others on the market, bang per buck, I don't know yet, I haven't investigated, this is not a review, this was just a teardown. And I hope you enjoyed it, if you did, please give it a big thumbs up and discuss it in the comments and links.

**Dave Jones:** And as I said before, high res teardown photos on EEVblog.com linked in down below, unless you're already watching this video on EEVblog.com, in which case you already know the links are there. Catch you next time.
