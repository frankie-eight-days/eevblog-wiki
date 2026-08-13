---
video_id: WTK4CgYbXEQ
title: EEVblog #790 - Lecroy Wavejet 354 Touch Oscilloscope Teardown
url: https://www.youtube.com/watch?v=WTK4CgYbXEQ
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 25, "2": 41, "3": 65, "4": 93, "5": 113, "6": 133, "7": 157, "8": 177, "9": 189, "10": 209, "11": 229, "12": 249, "13": 261, "14": 281, "15": 301, "16": 321, "17": 337, "18": 357, "19": 373, "20": 393, "21": 413, "22": 437, "23": 457, "24": 473, "25": 497, "26": 509, "27": 529, "28": 549, "29": 565, "30": 585, "31": 601, "32": 617, "33": 637, "34": 649, "35": 669, "36": 685, "37": 705, "38": 717, "39": 733, "40": 749, "41": 765, "42": 781, "43": 797, "44": 813, "45": 829, "46": 849, "47": 865, "48": 885, "49": 905, "50": 925, "51": 941, "52": 965, "53": 989, "54": 1005, "55": 1025, "56": 1049, "57": 1073, "58": 1097, "59": 1117, "60": 1141, "61": 1169, "62": 1197, "63": 1217, "64": 1237, "65": 1261, "66": 1281, "67": 1301, "68": 1317, "69": 1333, "70": 1353, "71": 1373, "72": 1389, "73": 1409, "74": 1433, "75": 1449, "76": 1469, "77": 1485, "78": 1497, "79": 1517, "80": 1533, "81": 1549, "82": 1569, "83": 1589, "84": 1609, "85": 1625, "86": 1645, "87": 1661, "88": 1677, "89": 1689, "90": 1709, "91": 1725, "92": 1741, "93": 1757, "94": 1773, "95": 1797, "96": 1813, "97": 1829, "98": 1845, "99": 1861, "100": 1881, "101": 1897, "102": 1917, "103": 1929, "104": 1949, "105": 1969, "106": 1989, "107": 2009, "108": 2025, "109": 2053, "110": 2069, "111": 2093, "112": 2109, "113": 2133, "114": 2149, "115": 2165, "116": 2185, "117": 2201, "118": 2217, "119": 2237, "120": 2257, "121": 2273, "122": 2297, "123": 2313, "124": 2333, "125": 2349, "126": 2369, "127": 2381, "128": 2401, "129": 2417, "130": 2429, "131": 2445, "132": 2465, "133": 2477, "134": 2535, "135": 2555}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. We haven't had an oscilloscope teardown in quite some time, so we've got this Teledyne LaCroix. What is it? It's a Wavejet Touch 354 4-channel, 500 MHz goes for about $5,000 US. It's actually not a Teledyne LaCroix, it's a rebadger, it's an Iwotsu made

**Dave Jones:** in Japan. Iwotsu makes some pretty good stuff. So I'm expecting this to be quite decent build quality inside. So it's an Iwotsu DS5600 series. So let's check it out. You know what we say here on the EEVblog, don't turn it on, take it apart.

**Dave Jones:** And here it is, made in Japan, Iwotsu Test Instruments Corporation. Ha ha, calibration void is seal broken, you bet. Ah, there we go. Gonski. As I mentioned, I expect this thing to be decent build quality. You might not have heard of Iwotsu, but they make

**Dave Jones:** excellent test gear and other industrial stuff. Very reputable Japanese company. They make, you know, they don't make cheap stuff, they make Iwotsu generally make pretty decent stuff. Is there a... yeah, there's a screw right up under there. Oh, that's a bit annoying. What I know about this so far is that it uses

**Dave Jones:** one chip per two channels. So one, you know, acquisition ASIC, so to speak. Whether or not they actually use an ASIC in this, or whether or not they use a FPGA, that will be interesting to see. Because you know, the likes of Keysight and

**Dave Jones:** Agilent, the biggies, and LaCroix of course, they spin their own ASICs. Now whether or not Iwotsu have done that, whether or not Iwotsu have been able to spin their own ASIC, or whether or not it's just FPGA technology, we'll find out very very

**Dave Jones:** shortly. These screws under here are really rather annoying. But this should lift straight off. And we're in, like Flynn. Well, not really. We've got the, all the shielding. Very nice shielding, no problems whatsoever. It's quite thin because this thing's not hugely heavy like the, say the

**Dave Jones:** Rigol units for example, but ooh yeah, look. You can see the nice little RF fingers down there. Look at that. They've really gone to town. All the way along there, they're serious with their EMC. These guys know what they're doing. Now there's an additional spot

**Dave Jones:** for a BNC here on the back panel, but I don't believe I can find any option in the menus, like in the spec sheet to see what that is, so I don't know. Maybe it's a feature that they thought they would build in and then left it out later.

**Dave Jones:** As you can see it's not simply just the PCB depopulated with the connector. It's not that easy, because there's no room in there to put a connector and you can actually see a wire going over there. That's rather interesting. Is that a bodge wire?

**Dave Jones:** We'll find out. More excellent RFI shielding there on the ethernet and the USB connector. Very nice. But this one here, look at that. That is an unpopulated connector. I'm not sure what that one is. It seems a tad on the small side. It's not a

**Dave Jones:** VGA connector, so I'm not sure what it was. Some sort of mixed signal test connector maybe? And the only break in that case is this little ribbon cable coming out of here going to the front panel. That would be the touch controller, a 4-wire resistive touch interface.

**Dave Jones:** And this is interesting. Down on the bottom here, these are our input amplifiers and all these holes, they're not ventilation. You might be able to see on the... might not actually, be able to see, but inside there are the trimmer pots for the front end.

**Dave Jones:** So there you go, they trim them after they put the case on. Hmm. Now this is interesting in that, looks like the side panel comes off here. Oh, now we're in like Flynn, Errol that is. Lattice. I can already see FPGA PLD goodness.

**Dave Jones:** So there you go, that looks like the main logic board in that configuration. Isn't that beautiful for debugging and servicing? Actually you can leave the scope up, right? You can operate the damn thing on the front and then get in there and probe

**Dave Jones:** that by just taking off that panel! That's got a... I'm going to say that is a deliberate design choice because they wanted to, you know, make this thing easy to debug and service. That's just... well, maybe not service. I don't know. Anyway, maybe the designers go, I don't want to put the thing

**Dave Jones:** flat on its face like that and then trying to operate the thing and debug it. What a pain in the arse, I'm going to make my life easy and lay out the board like that! Ah! Beautiful! Brings a tear to the eye. So I think what they've done here, this is the main

**Dave Jones:** processing board. This is just running the user interface and everything else. Looks like there's another vertical board in here you can see some heatsinks under here. I reckon they're the heatsinks for the acquisition, ASICs, memory, you know, that kind of stuff. So the analog-to-digital converters and

**Dave Jones:** stuff like that. And, of course, they have that another board there on the bottom, that's the four vertical amplifiers. So it looks like they've got a sandwiched box arrangement like that. And what's in the middle? Well, is it just an empty fan path?

**Dave Jones:** I don't know, power supply's got to be over here somewhere. This is an interesting beast. It's different to other scopes we've seen. And absolutely no surprises, being a Japanese product to find a Renesas microcontroller in here, because they're like, you know, number one in Japan, number one in the automotive, Japanese automotive,

**Dave Jones:** everything else. So, yeah, very popular in Japan. The SuperH 32-bit RISC processor. It's the R5S 76700. I'll link in the data sheet for those playing along at home. And check out this puppy. It's a Lattice LFE 2-70E. That's the ECP 2 Series FPGAs.

**Dave Jones:** And this is $250 worth in 40 quantity from DigiKey. As the number on there says, the 672, that denotes the number of pins, so 672 pin BGA, 500 I.O. pins on this puppy. And it's got 8500 logic blocks, 68000 logic elements, a meg of block RAM

**Dave Jones:** and all sorts of whiz-bang stuff. And that is surrounded by the memory there, and that is doing the display processing. So clearly what's going on here is they're using the Renesas main processor here, it's got the operating system, doing all the user interface stuff, you know, talking to the comms, USB ports,

**Dave Jones:** all the usual, you know, operating system type functionality. And the Lattice FPGA over here, coupled with this memory around here, this is doing all of your display processing, hence this ribbon cable going off here, it's a dead giveaway, that's going off to your LCD down here.

**Dave Jones:** So that is mapping all of your data coming from your acquisition ASICs and your analog-to-digital converters. So that puppy's doing you know, equivalent functionality to part of say the Keysight Megazoom ASIC with the direct mapping of the screen. But even with all this horsepower here, and they're doing it

**Dave Jones:** they're doing it right, they're doing the right things here. You can only still only get, if you have a look at my review for this thing, first impressions review, only like 5,000, 6,000 waveform updates per second, so it's not a fast scope at all.

**Dave Jones:** So bit of a shame, and quite surprising considering the hardware they got to do it. And this connector up here, that goes to the outside there, or the optional connector. Yeah, I'm not sure what that's doing, maybe some sort of debug interface or something.

**Dave Jones:** Yeah, that's all I can think of. And also there was look, a relay there. What's that doing? And I'm just propping the scope up with this. Nothing to see here. And this Epson part, I actually couldn't get any data on that at first pass, so I'll have to try

**Dave Jones:** harder. I'm going to presume just by its location that maybe a GPIB controller? I didn't know Epson did GPIB controllers though. Hmm, I don't know, either that or some sort of maybe USB controller? But then again, if it's not, where is the GPIB controller?

**Dave Jones:** Then we've got another lattice part, that's a Mark XO family PLD, so it's not an FPGA, it's a programmable logic device, and we won't know really what that's doing until we figure out where this ribbon cable's going, because that's clearly tied into there.

**Dave Jones:** Some sort of glue interface logic, something like that. It's not doing anything really heavy duty. Now I'm going to try and get the rest of this off. It's got a weird mix of screws on here, and these the ones in here holding down this analog board, or maybe going through the

**Dave Jones:** heat sinks or something, they're quite long. And I was afraid, I don't know, some nut would fall off inside. Oh, there we go. It looks like I've done the right thing. I've done the right, ah, there we go, yep. Beautiful. Oh! Oh, look at that.

**Dave Jones:** Oh, look at this. This is just gorgeous. I love the access on this thing. It's fantastic. We're straight into the analog sections, we can do all the acquisition section as well, plus the processor on the other side. And clearly, the power supply is all in the center business.

**Dave Jones:** It'll have its own shield in there, of course, they wouldn't be that silly. We'll have to check that, we can probably just start peeking and see it. I don't know if I'll don't know how far I'll go with this thing, actually. We'll see.

**Dave Jones:** Anyway, so yeah, power in here, and then fan, and then it just sucks it straight through. So that's terrific. Although that means, though, that all the airflow is going over the power supply, so you don't get any airflow over these main acquisition little

**Dave Jones:** bodged-on, they're PCB. Well, they're not bodged-on, they're stuck-on with thermal adhesive, which is fine. But they've got PCB pins on them, so they've actually used PCB-mounted heatsinks there with the PCB solder pin and just whacked them on. There's nothing wrong with that, I just think it's funny.

**Dave Jones:** And it reminds me of the product I worked on, the Datalogger, at a former company. It's actually in that famous hand photo that I've got, or infamous hand photo that is kind of, sort of my logo these days. And that was a similar sort of, like,

**Dave Jones:** but the one I had was like four-sided construction, boards on all four sides. This one has a front panel board as well, so technically it does have one on the other side, and then it had a fifth board on the end. Well, actually it was like a complete

**Dave Jones:** cube, it had one on either side, so it was completely embedded like that. And I just love this sort of construction. The access is just brilliant. When you're designing this thing and debugging it, you can have the full scope here, and you can get access

**Dave Jones:** in there to probe absolutely everything at any angle. Oh! Yes! Thank you! So we'll have a look at our analog board here, there's so much to look at. I hate when you can't get in, you know, they've got shielded cans on the bloody things

**Dave Jones:** and you can't get in there. No, they've got the classic blocks here to separate the individual sections, and then those long screws which I showed, these ones here, just go all the way through. I don't, you know, I was hoping that there wasn't like a nut on the other side that fell off, but obviously they've got some sort of captive

**Dave Jones:** nut or something else, some sort of part of the metalwork or something matched up on the other side. So that's very, very nice. You can see the serpentine traces, the matched length, that's why they wiggle around there, because they want the same length, they want the same this

**Dave Jones:** length of this track. This would be the main analog output from the fourth analog channel here, this has to be exactly the same length as this one coming from the first channel here, that's why this first channel has this snaking all the way around,

**Dave Jones:** it's got to be exactly the same length. So we've got our four channels here going into, it looks like four buffers at the end of the transmission line here, because it's a differential signal out, so that'd be differential. They might even convert it to single-ended again, and then

**Dave Jones:** these are obviously differential drivers coming out, haven't even looked at the numbers yet, it's just obvious with the topology. So yeah, it looks like we've got, yeah, no? Four? Yeah, there's four pairs coming out there, so the four channels again. So I think what they're probably doing

**Dave Jones:** there is tapping off the triggering points for the four channels, and then just then we've got our output buffers here, which would be our ADC line drivers going down there, and then popping out somewhere on our ADCs down here, which we'll take a look at.

**Dave Jones:** Actually there you go, yep, it tells us that is part of the trigger circuitry down in there, so each channel, four different trigger channels. And there's our trigger input amp as well, you know, there's a decent amount of stuff in there, they're really going

**Dave Jones:** to town on their external trigger input. Oh by the way, that wire that we saw through there, it's not, it's a little micro coax, board to board, connecting those two boards together, so yeah, not sure what they're running there, it's not like, you know, the main output for the ADC or anything, it's

**Dave Jones:** some sort of auxiliary thing. Anyway, speaking of auxiliary, look, there's that connector, there's that extra BNC, so yeah, they actually did have the, they do have the footprint for the BNC on there, this is auxiliary IO 1, can we see that? Auxiliary IO 1 and

**Dave Jones:** auxiliary IO 2, they decided they didn't want the second auxiliary output. Why? Hmm. Actually come to think of it, that's probably for the auxiliary IO output here, because this would be like the output driver for that presumably, so I reckon yeah, that's coming over here

**Dave Jones:** from, well it's coming over from the acquisition board, I would have, oh you know because you have to get the trigger output, the trigger output is switch, you can switch into this thing under software control, so yeah that makes sense, all that stuff there's probably the driver for the aux out.

**Dave Jones:** Now if you had a keen eye Now if you had a keen eye you might have spotted this unusual looking beast, which links, looks like one of the, looks like the output of basically all this here jumps over, and then that goes directly to the output pin of the BNC

**Dave Jones:** What is it? It looks like one of those current, you know, SMD current shunt resistors, but it's not. There's no tapping coming off it, why would you need to, you know measure the output? It's not that, it measures zero, I've actually measured it, it's a surface mount

**Dave Jones:** link by the looks of it. I'm not sure why maybe to get a probe on there perhaps, but it's like it's not, you know, it's actually not deep enough to get a, like a high up enough the board to get a probe off

**Dave Jones:** so it's rather unusual Now if you actually have a look at the traces here, you can actually see that they're actually connected the two IO connectors on the layout itself look, there's this one actually, you can see the trace actually goes in there

**Dave Jones:** OK, we've got ourselves a, maybe is that a little inductor there perhaps, and it just jumps straight over, so they're actually shorted when this link is in place Weird! It's almost as if like this was a normal via, and so was this and they were, you know, it was doing something else and they reconfigured

**Dave Jones:** the circuit, didn't want to re-spin the board, so they've got some sort of custom you know, jumpery link which goes between the two via pads, it's, um, I don't know It's bizarre On second thought it can't be that, it looks like the pad

**Dave Jones:** is actually designed for it, like the surface mount pad, so it's not just a bodge on a via Now they haven't got the same thing happening here, but they do have this gigantic jumper going across here, from here to here across the analog input, there's the BNC, that's the front panel

**Dave Jones:** BNC going straight into the board, that's a nice solid connection by the way, that BNC ain't going to wiggle loose anytime soon Nice big solid connection, and look it's actually connected through to the ground plane here and over here, so I can only presume that they're using that

**Dave Jones:** as some sort of ground test clip test point, something like that And at this point you're probably wondering, hey what's going on here? These are the output drivers, the differential output drivers for the ADC, and they're going through here and these differential pairs are just dropping down to vias here

**Dave Jones:** how are they getting over to the ADC down here, which we'll take a look at. Well, clearly there's got to be a board-to-board interconnect down in there somewhere And if you take a close look I reckon, look at those suspicious vias there, and also over here on the underside

**Dave Jones:** of this board, which is the acquisition ADC board there is a surface mount high-speed board-to-board interconnect which mates with a similar one up on there, because you can see also the matching vias down in there. So I reckon we've got board-to-board interconnect there

**Dave Jones:** So you see that in a couple of locations there, and here and I reckon there's one under here too for the output drive And sure enough, there we go, if you have a look under there, those vias there's got to be another board-to-board, high-speed board-to-board

**Dave Jones:** because we're getting, you remember? We're getting, you know, 500MHz analog signals board-to-board across here it's one of these real expensive, you know, high-speed purpose-designed board-to-board interconnects. And that's how they're doing it. You don't want to run it over a ribbon like they're doing

**Dave Jones:** down here between the output from the acquisition engine and just going over to the display engine over here. This is all like lower bandwidth stuff to the screen updating than what's actually happening. You know, it doesn't have like the 500MHz analog signals and stuff like this board does

**Dave Jones:** And if you look very carefully up under there you can see it, there's the board-to-board interconnect. Now I won't get into a detailed analysis of the front end here but you can see it's all passives on the top there, so a lot of the active stuff I think is on the bottom

**Dave Jones:** so we've got our BNC input there, and a couple of relays, and all of our trimmer adjustments and everything else. Before we start getting down to our first transistor down here, check out all the annoying well, that's a diode, sorry, that'd be 2D2

**Dave Jones:** and you might be wondering about the silkscreen designators here, like this one for example 2R7, that's not a 2.7 ohm resistor. You see how they all start with 2, and this one's 2D2 over here which is a diode 2RL which is a relay, 2 obviously stands

**Dave Jones:** for the board. It's not that common, but a lot of companies actually do this as company policy. This will be like the second board in the design, so they'll put board 2 first, then they'll put C So this is actually R7, and this is relay 3

**Dave Jones:** up here, this is diode 2 down here, etc. But as you can see we're basically not getting anywhere on all the active stuff, so there must be more on the bottom. Let's check out that puppy. That LinearTek 1097 there, that's just a low power precision

**Dave Jones:** amplifier, not much doing there, probably just some sort of offset thing. And no surprises for finding the National Semiconductor, now Texas Instruments, LMH6518, they've only got the L in there, but it's actually the LMH, and that's a 900 megahertz variable gain amplifier, digitally programmable

**Dave Jones:** variable gain amplifier. We've seen this before, I think it might have even been in the Rigol, I think. Anyway, yeah, it's one of the common front-end programmable gain amps, digitally, so the micro can just come in and set any gain from like, you know, 1 dB up to

**Dave Jones:** 40 dB in 2 dB steps. And that's pretty much a companion device for National Semiconductor's ADC, which we'll see on the other side. Well hello sailor, no surprises for finding you here. Once again, the matching National Semiconductor, 1 gig sample per second analog-to-digital converter, this is the dual one.

**Dave Jones:** This is the ADC-08D1000, as it says there. And yeah, 1 gig sample per second, dual AD converter, and pretty decent performance at 500 megahertz analog bandwidth, it's actually got 7.4 effective number of bits, it's not as shabby an ADC at all. And I think

**Dave Jones:** once again, a similar one, or the same one used in the Rigol, the high-end Rigol as well. And once again you can see the matched length serpentine tracers going up to your main acquisition ASIC slash FPGA up here. So once again they have to be matched length.

**Dave Jones:** If they're a different length, then the propagation delay of the signal, remember, rough rule of thumb, 15 centimeters per nanosecond. So, you know, when you're talking about high-speed digital stuff, the length can really matter. You don't, you want all that all the data, the output data to

**Dave Jones:** get to the, and to be latched in to your main ASIC, sampling ASIC, at exactly the same time. So that's why they have to match the lengths. So I've got a total of 2 dual ADCs here so 4 ADCs total, but only 2 acquisition ASICs.

**Dave Jones:** And this is why the sample rate actually halves when you turn on both channels. Because, you know, it can actually, in single channel mode, it can actually multiplex these ADCs, the 2 ADCs on the one, so you can get twice the sample rate.

**Dave Jones:** So you can get your 2 gig samples per second. So they just feed the same analog signal into both channels of the ADC here when you're in single channel mode for the 2 gig samples per second, and they do the interleaved sampling, so there's a slight skew between the 2 samples

**Dave Jones:** for the ADCs, and you can get twice the clock rate. So bingo, that's why it halves. And it's almost certain that around here, and here, and here, and here, you can tell by all the vias. Check out all the vias there and there, they've got

**Dave Jones:** a, like an SO type package in there which is the memory. So memory, memory, memory, memory, memory. So there's going to be 4 memory chips there on the flip side. We've got our bypass caps, look, we've got some little termination resistor packages in there as well.

**Dave Jones:** So yeah, a dead giveaway. I wouldn't even have to flip this board over, you can bet your life that there's a memory chip there, there, and there, and there. And as for this acquisition ASIC, well, I've got no idea what that puppy is, so it could certainly be

**Dave Jones:** a custom ASIC device. I don't know. What really gives it away is, well, over here, ta-da! They've got an iWattsu branded chip, whether or not it's a custom ASIC or it's just, you know, branded, or it's some off-the-shelf thing branded iWattsu, but you know, it wouldn't surprise me, they're a big company, they can spin

**Dave Jones:** their own ASICs. Aha! I just noticed this on the actual, the bottom side of these acquisition ASICs here, look at that! Altera, busted! It's an FPGA, it's not a custom ASIC, there you go. Almost certainly, like, Altera aren't going to spin them a custom ASIC.

**Dave Jones:** So yeah, they're using an FPGA for the acquisition engine. Exactly what one it is doesn't really hugely matter, so I'm not going to go and try and prise off this heatsink, it's, you know, like, probably stuck on pretty darn well with thermal adhesive.

**Dave Jones:** I don't want to ruin it. So my guess here is this iWattsu custom chip here is the trigger ASIC. It makes sense, I mean we've got our two acquisition ASICs here. This scope, if you've watched the first impressions review, you'll see that it does, it can do, you know, I squared C triggering, serial triggering, all that

**Dave Jones:** sort of jazz. So, you know, that's not terribly easy to do, so I reckon they're implementing that in hardware inside this puppy. And by the way, that lattice CPLD we saw before, coupled onto this ribbon cable, that looks like that ribbon cable's going over to the front rotary

**Dave Jones:** encoder board, so that could just be some real simple PLD logic to decode all the rotor encoders, drive the switch matrix and drive the front panel LEDs and all that sort of jazz. Which does actually make sense because you don't want to couple all those rotor encoders onto your

**Dave Jones:** main processor, and your main processor's busy, you know, doing what processors do, and, you know, updating screen and GUI and all that sort of jazz. So, you know, you want to take that hardware load off and put it here, which is really nice.

**Dave Jones:** But if you've seen my first impressions review and notice, I actually noticed some lag on the thing, some non-responsiveness of the controls, depending on how much heavy-duty processing the thing was doing. So, yeah, I'm not sure. Once again, they got the hardware to talk to

**Dave Jones:** care of these things, but anyway, it's like some other mechanism, it's, you know, at play. I don't know what. Now, taking out the top processor board, and ta-da! There it is. I was actually thinking before for the GPIB, I mentioned where is the GPIB controller

**Dave Jones:** and also the drivers, driver chips for that, the receivers. They're here as well, they're all on the bottom side. We've got an Altera Max 2 doing the heavy lifting for the GPIB So there you go, they've rolled their own GPIB interface there. Nice.

**Dave Jones:** And it looks like we've got some flash on the bottom, and well, that's about it. Bob's your uncle. Nothing else really doing there on the board. And of course, no one was going to be happy, were they, until I took out the acquisition board, and bingo, there's those memories exactly where I said

**Dave Jones:** they would be. There's the two big acquisition ASICs, you can tell by bypass caps and all sorts of, well, they, it is a I can't even see them from here, like half a meter away, but you can tell by the component designators. Big ASICs there and there, and so

**Dave Jones:** full memory for each one, two for each channel, obviously. So what we've got here is ISSI brand synchronous DRAMs as you'd expect. These are 64 megabits total per chip, so they're actually a 512k by 32 configuration, which is 4 different banks, so that gives a total of 64 megabits

**Dave Jones:** per chip. There's 2 chips per channel. So with 64 megabits total, of course we've got an 8-bit ADC on this thing, so we're talking about 8 meg samples total per chip. Now we've got 2 chips per channel, so that's a total of 16 meg samples per channel.

**Dave Jones:** So that's actually more than this thing is specced. This thing is only specced to have 2.5 megabits per channel. Of course when you interleave them, they give you the banner spec of 5 meg samples per channel, but that's like a single channel only 2.5 meg samples.

**Dave Jones:** Why have we got all the extra? Well, it's because of the replay feature in this thing, the continuous replay feature if you watch my review of this thing, you can see the really nice replay feature, it's always on, it's always storing all the

**Dave Jones:** parameters, it's always storing all the data, it's always storing all the waveforms before the trigger event. So when you hit stop, then you can automatically go through and replay them, it's always doing that. So it needs much bigger memory to actually do all that replay mode.

**Dave Jones:** And it needs the multibank configuration DRAM like this to actually get the speed required to actually, and the data throughput to actually do all that stuff. So the 4 banks inside each of these chips really helps. And the 512k by 32 configuration, not exactly sure how they're all storing it in memory,

**Dave Jones:** but yeah, there's a specific architectural, memory architectural reason why they chose this particular configuration memory chip. And for those who actually had their thinking cap on instead of just talking gibberish like I am, you would have known that I was way off the mark there with these

**Dave Jones:** two chips on the acquisition, sorry, the ADC board actually being, sorry, the analog front-end board actually being the drivers, the ADC drivers. No, this is just the trigger circuitry. All these tracers actually coming out here, these serpentine tracers I talked about, that's just going over, just dedicated to the trigger circuitry.

**Dave Jones:** So I thought it might have been tapping off there. So that actually comes over on this connection here, and of course it's obvious that the two analog channels go straight into the connector here. You can't see the tracers, they're on the other side of the board.

**Dave Jones:** They go straight up to the connector up here, into our ADC. Here! Because if you flip it over, ta-da! There it is. There's our connector. And that goes straight into your ADC here, straight into your ADC here. Two channels a pop. And this connector over here is part of your trigger

**Dave Jones:** input here, so your external trigger input. So this is your external input trigger connector going over to the acquisition board. Well, external trigger on this board coming over to your acquisition board here, and then this one is actually your trigger circuitry for your four channels here.

**Dave Jones:** Through all that there, if that makes sense. Oh goodness, I think I needed some sleep. And on the acquisition board we've got a smaller lattice FPGA than what we saw before. And this one's dedicated to the trigger circuitry, so receiving all that trigger data it was getting

**Dave Jones:** from the four channels. And you can see a fair bit extra happening down there on the bottom of the ADC board as well. And you can see maybe right down in there, we've got an extra relay down in there at least. And there's our output

**Dave Jones:** driver chip right there. And it's going to be, might be a bit tricky to get into these. I've got to take the BNCs off on the front and all sorts of jazz. Hang on folks, hold onto your hat. Watch this. I undid some screws

**Dave Jones:** here, trying to get off the power supply frame, and what do you know? What do you know? Look at that! Ah! We're in! That is beautiful! I love that! Ah, hats off. Nice. I'll tell you something for nothing, this is a really good

**Dave Jones:** well-engineered power supply. A, look at the size of the damn thing. It's the full, almost the full width of the thing. As I said, fan over here, like vents on the other side sucking straight through. Man, the life of this thing is going to be fantastic.

**Dave Jones:** It's just beautifully designed. Big, beefy, I love it. Looks, oh, top quality components, which we'll take a look at in a sec. Silastic down of course. Yep. There you go. Hot snot everywhere. Terrific stuff. And look at those chokes, beautiful looking chokes there.

**Dave Jones:** And there is, I do see, I don't know, I thought that was a bodge wire, is that? No, I thought it might be a bodge wire or thermistor, not entirely sure. And anyway, we've got a board with some opto isolators down in there, that's quite common.

**Dave Jones:** But look at the size of the heat sink here for these puppies. No problems whatsoever. And they've oriented it so that the air flows directly across the surfaces for this heat sink here. Fantastic. Although this L bracket here sort of breaks your air flow a bit, but

**Dave Jones:** eh, I'll cut them a break on that. Very nice, look we've got a sill, it's not a sill pad, it's a complete isolated sill type, you know, sill's a brand name but you know, I just use it as a generic term that's quite common.

**Dave Jones:** And insulating heat shrink type tube but sill pads are thermally conductive. So it's not just heat shrink tubing, because that's not thermally conductive, it's actually sill pad tubing held in place by this bracket. That's just, that'd be the main primary side switching transistor.

**Dave Jones:** Terrific stuff. Once again, attention to detail on the EMC, look, little ferrite rings there. On the secondary side, that's just to take the edge off, just a little bit. To, you know, to reduce your emissions from this thing, just slightly. You know, that's a real nice touch, they know what they're doing.

**Dave Jones:** Spared no expense on the main filter cap of course, nip on chemicon, none of this one hung low rubbish. And all your output filter caps are down in there under the heatsink, and having your output filter caps near the heatsink, usually a no-no, but in this

**Dave Jones:** case, because of the way it's oriented and the way they've got the air flow going through this thing, not a problem. So there's transistors and power diodes we saw on the other side, they were for the main 5 volt rail. These ones on the other side here, plus 12, minus 12,

**Dave Jones:** and minus 5. Smaller rails, don't need as much current capability. And RF ferrite rings, look, on the main diode bridge on the AC input. Oh, beautiful! How many times do you see that? Not very often. This is a fantastic supply. And check out that mains input board there, that's just beautiful.

**Dave Jones:** Dual HRC fuses, look at that, we've got ourselves a MOV there by the looks of it, we've got ourselves the requisite suppression caps as well. Fantastic! Just all on a separate board, very nice earth mounting over to there, although they've got this separate earth strap going all the way from the

**Dave Jones:** pin, going all the way back down to that post there. Yes, it is has got a shake-proof washer, properly crimped and terminated. Oh man, they really take pride in this. So that, boys and girls, is an example of how you design a power supply

**Dave Jones:** into an oscilloscope. That is beautiful. From practically every aspect, the design, build quality, safety, thermals, airflow, just the physical size of the thing, using prime quality parts, taking care of EMC with the ferrite beads and stuff, and yeah, hats off. Best example I've seen in an oscilloscope

**Dave Jones:** I think, bar none. Oh by the way, we do have a soft mains power switch here, so I'm definitely going to have to check the standby power consumption of this thing. And sorry folks, I tried to get this analog board out to see the other side, I took the bars out and the other

**Dave Jones:** screws, but unfortunately it looks like they do final soldering down there on the BNC connectors to hold that board in. I can't seem to get the thing out and that kind of makes sense, I guess. You know, I would have preferred a better one where you could get it out without desoldering, but I don't

**Dave Jones:** think so. So I think we're going to have to cut our tour short here. So there you go, I hope you enjoyed the teardown of this Teledyne LeCroy Wavejet Touch, aka the iWattsu DS5600 series, because well, that's where the credit has to go to

**Dave Jones:** the designers at iWattsu. And this thing is brilliant as you can see. This is exactly what I expected from iWattsu. It's just fantastic. And it's a beautiful design just from an engineering debugging point of view when you're designing and building this thing, or if you want to

**Dave Jones:** repair it or something like that. And the power supply is the finest example I've seen in an oscilloscope, I think. And it's just, yeah, it's beautiful. My hat's off to them. So I hope you enjoyed that look at a real quality built oscilloscope.

**Dave Jones:** So you can see why LeCroy had no hesitation in putting their name to this puppy. It was, it's just fantastic design and build quality. First-rate. And if you want to see the first impression sort of, you know, review of me unboxing and using this thing, I'll

**Dave Jones:** link it in at the end of the video here. And yeah, it's actually a really bottom-of-the-range 500 MHz unit. No frills, no bells and whistles, it's not that fast, and doesn't have all the fancy stuff which some of the more feature-rich modern scopes have.

**Dave Jones:** But geez, the build quality's fantastic. Rock solid. This thing will last you a lifetime, I think. So thank you very much Teledyne LeCroy for sending this one in. And if you like it please give it a big thumbs up on YouTube, because that always helps a lot.

**Dave Jones:** And if you want to discuss it, EEVblog Forum, YouTube comments, all that sort of stuff, follow me on Twitter, rate, subscribe, I don't know, whatever. If you want to buy the 555 Tyber t-shirt that I wore at the start, I'll link that one in as well.

**Dave Jones:** What the hell. Catch you next time. Actually, by the way, I always forget to mention this, and I don't think I've really, if ever, measured it. Thanks to all my Patreon and other financial supporters as well, because that really helps a lot. Pay the bills around here, because this is my full-time gig.

**Dave Jones:** So if you want to support the EEVblog financially, I recommend Patreon. It's a really good way to do it. It's like a monthly subscription thing, but yeah, totally optional. Only if you want to feel kind and generous and all that sort of stuff.

**Dave Jones:** See ya! ... Winner! And just listen to all these relays click on when you switch it on, I love it! ... And how much power does it draw on standby? 1.6 watts? Meh, that's okay. Would have liked it to have been a bit lower.

**Dave Jones:** VA of about 7, yeah. Not terrific, but that's what you get with a power factor of, you know, 0.23. And if we turn it on, we'll see that power factor. Shoot! Right up. Here we go. 0.64, it's still actually a reasonably poor power factor.

**Dave Jones:** Anyway, this draws, doesn't take much. 42 watts and 68 VA. And it's 11.20pm. You think I'm going to finish this on time? For Teardown Tuesday? I don't think so, but Australia's ahead of the rest of the world. See ya! ...
