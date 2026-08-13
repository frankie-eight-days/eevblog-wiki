---
video_id: 3sSu-N1zkqQ
title: EEVblog #875 - NI VirtualBench Teardown
url: https://www.youtube.com/watch?v=3sSu-N1zkqQ
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 16, "2": 31, "3": 49, "4": 65, "5": 81, "6": 100, "7": 117, "8": 133, "9": 158, "10": 176, "11": 195, "12": 209, "13": 229, "14": 243, "15": 260, "16": 281, "17": 299, "18": 319, "19": 334, "20": 353, "21": 371, "22": 388, "23": 402, "24": 421, "25": 443, "26": 458, "27": 476, "28": 496, "29": 511, "30": 526, "31": 546, "32": 563, "33": 580, "34": 594, "35": 613, "36": 629, "37": 642, "38": 657, "39": 672, "40": 689, "41": 708, "42": 723, "43": 739, "44": 750, "45": 772, "46": 788, "47": 808, "48": 823, "49": 838, "50": 855, "51": 875, "52": 892, "53": 910, "54": 928, "55": 946, "56": 962, "57": 982, "58": 996, "59": 1011, "60": 1029, "61": 1043, "62": 1059, "63": 1077, "64": 1097, "65": 1115, "66": 1135, "67": 1152, "68": 1172, "69": 1188, "70": 1206, "71": 1222, "72": 1238, "73": 1255, "74": 1272, "75": 1291, "76": 1307, "77": 1328, "78": 1348, "79": 1370, "80": 1383, "81": 1400, "82": 1413, "83": 1431, "84": 1450, "85": 1474, "86": 1493, "87": 1515, "88": 1532, "89": 1549, "90": 1563, "91": 1600, "92": 1621, "93": 1642, "94": 1663, "95": 1678, "96": 1703, "97": 1721, "98": 1741, "99": 1757, "100": 1781, "101": 1803, "102": 1825, "103": 1842, "104": 1861, "105": 1877, "106": 1897, "107": 1914, "108": 1930, "109": 1946, "110": 1970, "111": 1984, "112": 2005, "113": 2020, "114": 2036, "115": 2051, "116": 2065, "117": 2082, "118": 2097, "119": 2112, "120": 2134, "121": 2156, "122": 2176, "123": 2193, "124": 2209, "125": 2227, "126": 2245, "127": 2271, "128": 2290, "129": 2306, "130": 2320, "131": 2337, "132": 2357, "133": 2372, "134": 2387, "135": 2405, "136": 2426, "137": 2444, "138": 2465, "139": 2483, "140": 2504, "141": 2519, "142": 2537, "143": 2555}
---

**Dave Jones:** Hi, it's Product Teardown and Playaround Time. Today we've got a nice bit of kit. Oh, this is National Instruments, their Virtual Bench. So thank you very much, National Instruments, for sending this one in. This is the top-of-the-line model, comes in two different models.

**Dave Jones:** This is the... well, they don't have the model number written on the front, strange. Anyway, it's the VB8034. This is the 300 MHz 4-channel model. It's also available in the VB8012 unit, which is the 100 MHz 2-channel model. And guess what it is?

**Dave Jones:** Take a look at all the different functions here. We've got a 4-channel scope. This one is 300 MHz, as I said. Built-in function generator. It's got external trigger, which is nice. So we've got the 4 channels plus the external trigger. It is a mixed-signal oscilloscope, as it said.

**Dave Jones:** So we've got a 16-channel mixed-signal scope. We've got a power supply. Look at this beautiful binding post here. The lesser model, the 100 MHz 2-channel, does not have these binding posts. It still has the DC power supply, but it has little Phoenix contact connectors,

**Dave Jones:** which are fiddly and annoying. I like the binding post on here. So it's got a plus-minus 25 volt 1-amp power supply, perfect for op-amps and things like that. It's got a 6 volt 3-amp supply, adjustable up to that. And it's got the mains earth grounding point.

**Dave Jones:** It's got a 5.5-digit multimeter built-in as well. And it's got digital I.O. as well, 8-channel digital I.O. So it's basically a complete workbench in one kit. And I'll give you one guess what market it's designed for. Yes, the educational market, where they buy this thing and the students have everything they need

**Dave Jones:** in one box like this. Beautiful. And it's designed with connectivity in mind. So it's got the Ethernet LAN standard, of course. It's got USB as well, but it's also got Wi-Fi built-in. It comes with the antenna, so you can connect through to your PC or your tablet.

**Dave Jones:** So you can control this thing either way, and just mains input. And it's got one of those Kensington lock things, valuable for the classroom, where, yeah, students can wander off with these things. So, hmm, gotta lock it down. So what am I expecting from this thing?

**Dave Jones:** Well, the same thing from every National Instruments product. It's going to be well-designed, well-manufactured, super high-quality. The software is going to be competent and complete. And it's going to be high-priced. How high-priced? This one is the 300 MHz 4-channel unit. We've got here is $6,000 US.

**Dave Jones:** Woo! Hang on, I'm feeling a bit light-headed. But the 100 MHz 2-channel model is a more reasonable $2,000. But, you know, if you compare that to a scope, for example, you know, modern scopes have, you know, they'll have 4 channels, they'll have the function generator built in, they'll have mixed signal, everything else.

**Dave Jones:** And that's, you know, it's getting towards on par with a regular bench scope. And certainly it's well above the price of, you know, other USB scopes on the market. But it's designed for a more niche market, designed for the educational market. The educational institutions wouldn't be paying that.

**Dave Jones:** They'd be paying a lot less. They'd order, you know, hundreds of things, getting a real good deal. But it's all in one unit. All of the functionality. It's very, very nice. And I'm sure the software's going to work pretty well. It's got nice feet on it, lovely.

**Dave Jones:** And it feels real, like a real top-quality instrument. And smells like a quality instrument too. And yeah, the build quality of the case and everything else is just beautiful. It really is absolutely stunning. What's that? There you go, we've got some compliance rubbish.

**Dave Jones:** And there it is, the VB8034. And they've got fuse access on the bottom for the multimeter, of course. So you know what we say here on the EEVblog, don't turn it on, take it apart. First up, we've got proper HRC fuses in here.

**Dave Jones:** See the brand, no worries. Got a small little M205 in there for the low current one. But hey, that's fine and dandy, no worries. One thing to note, no autoprobe interface, so it can't auto-detect times 10 probes. Alright, let's pop the hood on this thing.

**Dave Jones:** This feels like die-cast alloy. This feels very nice, but ta-da! We're in like Flynn. We don't have much on the bottom there. I like that plastic cover. That's really quite nice, around the whole multimeter section, which is fantastic. So they're using that as like, is that like a, you know,

**Dave Jones:** a blast shield in case anything, you know, blows up in the meter. Because, you know, that's common. People, you know, students are using the probes, a probe and everything, willy-nilly. And yeah, if anything's going to blow, it's probably going to be the multimeter inputs.

**Dave Jones:** So yeah, that's really quite nice. There's no shielding reason. It's not conductive at all, so that's just really neat. I like it. Hmm. And yep, it looks like we've got a, is that a die-cast alloy bottom? That just feels beautiful. But look at the RF contact that they've got stuck on here,

**Dave Jones:** and that mates up with the exposed pad here. But check out the ground plane separation on here. Look, via stitched all the way around there. Yeah, they're really serious. They really know how to lay out boards at National Instruments. That's what you'd expect.

**Dave Jones:** So yeah, that's just, that's excellent. So it looks like we have mostly power supply type stuff on the bottom here. These look like MOSFETs down here. We've got the inductors, of course, all dead giveaways. So yeah, it's, you know, we've got some current sense resistors up there, have we?

**Dave Jones:** So it's pretty much all power supplies. Yep, there we go. We've got some optocouplers there happening, I think. But yeah, just miscellaneous bypass and power supply business. And of course, each section's going to have its own, like, local regulation. So this is going to be local regulation over here.

**Dave Jones:** This will have some more regulation here. This little section up the front for your digital I.O. has its own little, you know, 1117 regulator up there, most likely. So it's all separate. Very nice. By the way, it's a fairly decent wattage power supply as well.

**Dave Jones:** Plus minus 25 volts at an amp. There's 50 watts right there. Thank you very much. And here we go, the top cover's coming off. I just love the feel of this thing. And it comes apart beautifully. It's beautifully designed. Oh, look at that.

**Dave Jones:** Once again, die-cast alloy top on it with the RF shield in there. Absolutely brilliant. And, well, there's not much on this. Well, we've been mooned. We're looking at the bottom side of the top board. So yeah, they've actually, it looks like they've flipped this upside down.

**Dave Jones:** But here's your individual channels. They're not shielded. That's rather interesting to see for 350 megahertz. Maybe they are on the top side, but the bottom side here doesn't have any shielding. So that is rather nice. So obviously the 100, I would guess that the 350 megahertz model

**Dave Jones:** is going to be different to the 100 megahertz model because it's two channels. So right there off the bat. And I think that's a different physical configuration for the BNCs and stuff like that. So they probably have an entirely different board. Yeah, it's marked VB8034.

**Dave Jones:** So yeah, it's not like a generic thing. How can you not be impressed with this? It just oozes quality. It really does. Look at the nice bundling of the power cables down here coming out of the switch mode power supply. Massive ferrite bead on there.

**Dave Jones:** Each bundle is individually heat shrunk. Or is that... Yeah, it looks like they might have individual... Oh no, is that... No, that's taping. No, they're actually taped. Wow. Oh my goodness. They're actually taped. Wow. Old school. But yeah, nice switch mode power supply.

**Dave Jones:** You need that in here, of course. We're not going to get a linear power supply for our main output. You know, for our 50 watt plus power supply output. So definitely not going to get that. This board down here is interesting. Look at this.

**Dave Jones:** At first I thought, oh, it must have something on the front panel, something like that. But there's nothing on the front panel here. There's absolutely nothing. I wonder what these slots are doing here. It looks like it's just an interconnect board to connect this top board here,

**Dave Jones:** the top acquisition board, through to the bottom board down there. It's quite strange. Hmm. And that's our mixed signal digital input. We've got extensive diode protection on there. Check that out. Whoa, yep. Positive and negative protection per input. Liking the way this case goes together.

**Dave Jones:** I tell you what, I think this front panel is just going to pull off here. Yeah, look at that. And there's a connector down in there, which I can just front panel connector. Aha! There's the trick. That's what it is. It looks like we've got some voltage.

**Dave Jones:** This is used as a voltage sense line coming back by the looks of it. Or is it maybe output on-off control? I can see some extra stuff down there, because you might be noting, well, where's the diode protection on the power supply? You know, the reverse diode protection.

**Dave Jones:** Well, I believe it's on the other side there. So I'm assuming that that's what this does, is this is a sense line, which connects through to there. I have to undo them all to have a look. And if you were concerned about the potential lack

**Dave Jones:** of shake-proof washers on there, don't be. I had a real hard time getting those nuts off. They've obviously got some sort of clear Loctite-type stuff on them, so yeah, serious business. And if you want to see where gilding the lily is, well, take a look at this.

**Dave Jones:** They could have, they had one screw here to hold this board in, in addition to all the binding posts across there. And look, they've gone to the effort to put a threaded insert into that. Very nice. Anyway, turns out this board has a lot more on it,

**Dave Jones:** and I would have realised if I actually turned the thing on before I took it apart. Oops! Look, we've got some LEDs in here, and they actually go through the front panel. So the front panel must have, like, a semi-transparent thing on it.

**Dave Jones:** So yeah, they're like status LEDs and things like that. But they're not marked on the front, so they just light up and flash and do things. So we've got a bit of drivery action happening there. There's a diode I told you about for protection there.

**Dave Jones:** We've got a couple of ceramic bypass caps on the output. Got ourselves a nice resettable fuse in there by the looks of it. And we've got some fuse protection here on the output. I don't... They don't look like resettable fuses. They look like, you know,

**Dave Jones:** one-time SMD fuses that blow. So I hope they've done their homework on that, because you wouldn't want the students to short the outputs and blow these things. But I'm sure they have. This is National Instruments, right? They know what they're doing. So probably for extreme gross overloads and things like that,

**Dave Jones:** if the constant current output, you know, circuitry limit failed or something like that. And for the main event, we will now attempt to lift this board off. There's a... looks like a PCI Express connector up here, which is very common in board-to-board stuff these days.

**Dave Jones:** So I need to lift that. But that should come out. They've got a nice slot there for the little micro coax coming from the antenna connector on the back. That's very nice. Attention to detail to keep it in place. Doesn't flap around in the breeze.

**Dave Jones:** So, you know, somebody was thinking, the person who laid out the board must have been instructed or was, you know, like, they worked together with the mechanical people. OK, we need a coax on the back here for the antenna. And, well, you know,

**Dave Jones:** you didn't have to put that slot in there. You have to know that that slot, when it went together as a system, that slot had to go in there. So they would have probably, you know, 3D modeled all this and everything else, but that's very nice.

**Dave Jones:** Anyway, here is the main event. I don't think there's any other cables. Ta-da! And, well, that's the bottom side, but oh, hello, sailor! Hello, sailor! Look at that! Woo! Wow, is that a gorgeous heatsink or what? Whoa! So this gets rather interesting now.

**Dave Jones:** This heatsink here is for the oscilloscope section. As you can see, here's our scope inputs here and our arbitrary waveform generator and everything else. Yeah, it's 350 megahertz, so, you know, it's going to get reasonably warm, but that seems a disproportionate size heatsink,

**Dave Jones:** but they're really going to town thermally on that, so that's absolutely brilliant. But have a look up here, you'll notice, well, where's all our, you know, our big 50 watt power supply coming from? All that, you know, usually you see, you know, some decent heatsink

**Dave Jones:** in for a reasonable size bench supply, which this one has. It's obviously all happening in this switch mode can here. This is not only the main stuff, but remember, this is the output going directly to that front panel binding post for the power supply,

**Dave Jones:** so it's all coming from up here like this. So obviously, look, we've only got some tiny little surface mount heatsinks in here like this on these surface mount parts. Nothing fancy at all. You remember you saw some power stuff on the other side of this board

**Dave Jones:** when we first opened the thing as well, but there were no heatsinks on that. So that's the entirety of the heatsinks for all the power supply. It's absolutely incredible. So you've got plus minus 25 volts at an amp and also 6 volts at 3 amps as well,

**Dave Jones:** so they're obviously controlling the switch mode output, you know, feeding back to the switch mode output to minimize the drop across the output voltage regulators so that they can get away with such a small heatsink like this. So for, say, a 25 plus minus 25 volt maximum output,

**Dave Jones:** this thing isn't going to be outputting, say, you know, 28 volts or something like that and then dropping the whole lot across there. You wouldn't have enough heatsinking at all. You would need, you know, something serious like this going on. So obviously they're using a tracking switch mode regulator in here

**Dave Jones:** which is also providing power for the main board as well. You can see we've got some isolation transformers here. These are Halo brand TG21s. They've got, they're like a compatible one for like a more traditional Pulse brand transformers. They've got another little baby one of that.

**Dave Jones:** Oh, sorry for the glare. Little baby one of that inside here as well for the multimeter section. So that's doing some isolation. Actually, I got a bit sidetracked there. It's more obvious when I think about it for a second. What we've got here is rather than control the main switch mode output here

**Dave Jones:** and use that as like a tracking pre-regulator kind of thing, because I thought like originally these might have been low dropout linear regulators on the output. And I believe they are. But what's going on here is actually this section here with our three isolation transformers

**Dave Jones:** is the switch mode converter. You'll notice that we've got our diode outputs there and we've got our bulk ceramic decoupling on the input. And if we flip it over, we've actually got, there we go, these look like our primary side drive transistors right here.

**Dave Jones:** And we've got some extra output filter in there. We've got everything hunky-dory. So what it is is they're using this as a switching pre-regulator and then I believe it looks like that they're using the outputs. These are low dropout linear regulators on the outputs,

**Dave Jones:** which is why they might only be dissipating like a watt each regardless of the output voltage. Just to clean it up. Because you could have a direct switch mode output but then it's not all that clean and well, I don't think national instruments would do that.

**Dave Jones:** Most likely, I don't know, you'd have to check the specs and things like that. It'd be obvious whether or not they've got a linear low dropout regulator on the output just based on the switching noise figures and things like that. So yeah, these are low dropout linear regulators

**Dave Jones:** probably dissipating like a watt each maximum or something like that. Which is why they can get away with such small heat sinks here. It looks like we've got some, are they our current sense resistors there? They're most likely tapping those off. But yep, and you can see it actually coming out here.

**Dave Jones:** Here we go, here we go. Follow the traces, follow the money, follow the money as Deep Throat said. Here we go, all the way over and that goes over to our, they're our two traces. So these would be our plus minus 25 volt regulators

**Dave Jones:** and this poor little lonesome guy over here will be the 6 volt output job. And I just love the board-to-board interconnect. I love, you know, PCI Express, I've used them myself for various board-to-board interconnects and test instrument interfaces and all sorts of things.

**Dave Jones:** They're cheap, they're reliable, high number of insertions and just, you know, great stuff. And they're cheap, you know, standardized and they're going to be around forever. And they're just brilliant board-to-board interconnects and then you just design a little riser board like that to join the two boards, some nice big standoffs.

**Dave Jones:** This is beautiful engineering. And it gets even better as we saw on the bottom side we've also got this custom injection molded plastic blast shield as well on the entire multimeter section. They're really going to town, gilding the lily. Like, I'm surprised the inside of this ain't gold-plated.

**Dave Jones:** Now this board is interesting. One of the things I noticed is, look, heat sink detect number 4 up here. So I, that makes me think that they're, and it wouldn't surprise me actually, that they're temperate, what detect means is that they're likely temperature sensing that heat sink.

**Dave Jones:** So it's probably there, maybe they've got some circuitry under there at that point. I don't see anything on the bottom side there really, any detection stuff, but I suspect that's what's happening. I don't see the other ones marked, 1, 2, 3 and 4, but there's definitely number 4 there.

**Dave Jones:** And down there for the digital I.O., nothing much happening. That little chippy there is actually a TI CC384. It's marked, I believe, that's a little TI microcontroller. Not surprising at all to see that there, that would be doing its own thing, controlling the I.O.

**Dave Jones:** here, and then you can have the software talk to that. So that makes complete sense. As for the multimeter section here, clearly these two cans here are the analog to digital converters. Why they've got two? Maybe they're using a... Oh, can you measure voltage and current at the same time perhaps?

**Dave Jones:** Hmm, that'd be nice. I haven't checked the functionality of the thing, but that'd make sense with the two ADCs. We can see the nice little surface mount current shunt down there. That'd be, I think, is it 10 amps capable? I don't know, it's several amps anyway.

**Dave Jones:** And there's a lattice CPLD happening in there just to control the conversion and things like that. So let's go all the way with LBJ here and take off its plastic blast shield on the top and the metal cans here. Pop those off and bingo!

**Dave Jones:** What have we got? All our circuitry's under here. Under here we've got a bunch of resistors. Now they're most likely, because they're near, this is actually the positive input jack where the current stuff is over here. You can see all the current shunts and big, huge, beefy traces.

**Dave Jones:** So this is an input high voltage divider here. And there's the other side right there. I'll crack out the microscope and have a look at some part numbers. And here's another angle of those input high voltage networking. See all these resistors here? Here we go.

**Dave Jones:** They're serial chaining all of those. That gives you a high voltage because each one only, you know, might have like a 150, 200 volts compliance. So you put them all in series in a string like that and bingo! You've got yourself a high voltage input resistor.

**Dave Jones:** No worries whatsoever. You can see some guard traces, guard rings going around there. Very nice. They know what they're doing at National Instruments, that's for sure, because they do lots, a ton of high-end instruments and things like that. You know, measurement instruments, you know, 24-bit ADCs,

**Dave Jones:** you know, plug-in acquisition cards that have ridiculous performance and things like that. So yep, they know exactly what they're doing. And the chippies, let's have a look. And we've got ourselves an ADG 1308 and a 1309 there. They're just some half-reasonable muxes, fast switching stuff,

**Dave Jones:** primarily designed for video type use. So I don't know how fast the switching is on this thing. I don't know if that's a requirement. But anyway, they've decided to use those. Just a few other miscellaneous jobbies around here. I'm not going to bother decoding.

**Dave Jones:** I don't think there's anything too interesting there. There's another ADG 1309 mux in there. Let's have a look at these others. It might be hard to see, but down in there we've got some analog devices, AD4610s, and they're very, very schmick. There's another one down there.

**Dave Jones:** Very, very schmick. Oh, that one's upside down. All the electrons are going to fall out. Oops. Very schmick. JFET, low noise, op amps, low, everything, super-duper, whiz-bang, Bob's your uncle, op amps. Oh, nice. And there's our voltage reference right there. Analog devices, AD586, precision 5-volt reference.

**Dave Jones:** No worries whatsoever. Got to have some 4000 series, or in this case 74HCT series, 4052 mux. No worries whatsoever. And we've got another one. We've got one up there, if it's ever going to focus. Yeah, 4053. Nice. Still use them, like, 40 years later.

**Dave Jones:** Brilliant. But I certainly came a gutser on that prediction, didn't I? I thought they were possibly dual ADCs under there. I didn't think about the muxes and the high-voltage input and all that sort of stuff. Duh. It's probably obvious if I gave it some more thought.

**Dave Jones:** So obviously they must be implementing an ADC inside this lattice CPLD here, because there's nothing else. This is going to be one of these digital isolators. You can actually see the ground through the board there. You can see the lack of copper in there.

**Dave Jones:** So they've got all the ground plane over here. They've got the ground plane here, obviously separated going under the chip there. So that's going to be a digital isolator. Don't even have to read the part number on that puppy. Not that I can on the screen here, you can probably read that in HD.

**Dave Jones:** But yeah, that lattice SEMI, they must be rolling their own ADC with that. So that's obviously going to be some sort of dual slopey type integrator converter, something like that. As for the rest of it, the power supply side of things, I won't go into a huge amount of detail.

**Dave Jones:** Suffice it to say, there you go, we've got some surface mount packages under there. But that's about all she wrote. Lots of bulk decoupling there with your ceramics and things like that. But yeah, got some isolation transformers, as I said. Ooh, doing a flyover.

**Dave Jones:** Ooh. Using Dave's Steadicam. Well, you probably know what I'm going to say about that. Isn't that gorgeous? Wow. Beautifully laid out. It just oozes quality. Nice shielding strap there on the transformer. Coil craft inductor over here. We've got our common mode choke on the input.

**Dave Jones:** Got our protection and our various class caps. They're all silasticed down. There's our diode bridge there. They're silasticed that down to the cap in here. Obviously it's not doing a huge amount. Our main DC cap we'll take a look at. But the main output primary transformer there looks absolutely fantastic.

**Dave Jones:** Those caps look super classy. There's a couple of texture marks on here, so that'd be some sort of production operator testing, something like that. They've just marked them off that it's fully passed. But that layout is just, ooh, just oozes quality. And if you're wondering about the earth pin

**Dave Jones:** flapping around in the breeze over here, you needn't be concerned, of course, because ta-da! There is the earth pin there, soldered onto the bottom, and that is connected directly to the ground plane on the whole Blinken lot. So yes, of course, everything is mains earth referenced,

**Dave Jones:** except the multimeter, of course. That'll be completely floating. And yes, they have a rubber-compliant mount on the fan here. I don't know what brand fan is. I'd have to take it out. Couldn't be bothered. And of course, the main caps are Nichicon. No worries.

**Dave Jones:** And the output caps, no worries at all. We've got the big M there. That stands for Matsushita, i.e. Panasonic. Beauty. And you don't think we're going to finish this teardown without taking a look under here, do ya? Nah, I don't either. Let's go!

**Dave Jones:** And for the main event. Arr! Arr! Arr! The main event is me failing to get that off. I've got all the screws out. Um, this thing ain't budging. I can only presume that I'm going to have to wiggle it because the surface, possibly the surface tension

**Dave Jones:** of the thermal compound on there is causing it to stick. I can give it a little wiggle, but... Jeez, don't want to bust it. Ah, trap for young players. Look at that. Bloody double-sided sponge tape under there by the looks of it. What a pain in the butt.

**Dave Jones:** Well that's actually likely to be thermal sponge, I believe. Adhesive thermal sponge. It's definitely, something's got to be adhesive because I'm putting a lot of force on this thing either trying to lever it up or trying to wiggle it side to side. I'm putting a lot of force on it

**Dave Jones:** and that's barely, barely budging. Wow. Anyway, I'm actually quite surprised that they've got the Wi-Fi chipset. There's the little micro coax output for the cable going to the antenna on the back. I'm surprised they've actually got that on the same board as the acquisition board.

**Dave Jones:** I mean, granted, this is, I believe this is the external trigger. This is your AWG output and your four scope channels are here. But still, you know, like on the same board in the same area but they know what they're doing. They've separated the ground planes, power supplies,

**Dave Jones:** everything's hunky-dory. Nothing you can't fix with a bit of levered screwdriver force. Here we go. Yep, we're going to be in like Flynn. In a second, hang on, hold onto your hats. Da-da-da! Wow, look at that. Awesome. And there's our evil thermal adhesive stuff.

**Dave Jones:** Really great stuff. You can see the imprints of the chips, which are probably the analog to digital converters. We'll check out. So they're actually using that to transfer the heat straight through. But obviously they've got, you know, die cutouts here that directly mate with like this big application processor here.

**Dave Jones:** Look at that beast. Oh, there we go. There's a Xilinx Zinc there. Oh, beautiful. Yeah, you need some serious FPGA combo arm horsepower and that zinc's going to deliver in spades. So, yep, there we go. Actually, they might be thermal, dedicated thermal pads on there anyway.

**Dave Jones:** They have to get, this is, this sponge stuff is going to be higher thermal resistance than either the direct contact or having a dedicated, you know, thermal pad, thermal grease, something like that. So, but it's still, you know, they do a reasonable job of getting the heat out.

**Dave Jones:** And there's our main beast. Look at that. Oh, that massive dye in there is, I see Xilinx, and we'll give that a bit of a wipe-a-dip with our isopropyl alcohol. Get that off there. We should be able to, hopefully, get a nice, shiny part number.

**Dave Jones:** And there she is, a Xilinx Kintex 7 XC7K160T. That is going to be a beast. If you want to ask the price on that puppy, you probably can't afford it. Wonder if it's on Digi-Key. Sure enough, $496 US, of course, Yankee money. One-off price.

**Dave Jones:** None of this quantity discount rubbish. But Digi-Key have 128 in stock. No worries. Well, it turns out that heat sink detect thing is not actually detecting temperature, because you'll see a little trace running off there. It's obviously detecting that it's physically there, like it's connected down to a ground point or something.

**Dave Jones:** So it's like checking that the heat sink is like a shorting strap. So yeah, why they're that keen to know that the heat sink's in place? I mean, what is it, just suddenly going to work loose and vanish, grow legs and vanish? I don't know.

**Dave Jones:** Now the interesting thing about this is not only do we have this beast of an FPGA here, this Kinects device here, a couple hundred bucks, sorry, $500 worth, in one-off quantity, we've also got another Xilinx Zinc here. And it's basically a similar, you know, kind of family.

**Dave Jones:** And this one, of course, has the ARM processor built in, plus the FPGA fabric, whereas this one is just a big-ass FPGA. But this Zinc on its own, we're looking at a $150 to $200 part here as well. And we've seen this in other scopes,

**Dave Jones:** just this on its own is enough to implement this scope. So what they're doing here, why they've got a combination of both of those, I'm not entirely sure. Like this scope, I believe, although I haven't powered it up yet, I believe it doesn't even have like intensity-graded display,

**Dave Jones:** and you know, like it doesn't do any real-time FFT or anything like that, as far as I'm aware. So really, this Zinc on its own is more than capable enough of doing this. We've seen lots of other low- to mid-range scopes with just this in teardown.

**Dave Jones:** So why they got to it, interestingly, look. I mean, if you follow the, once again, follow the money here, from this USB connector down here, the traces from the USB are going all the way over to here. Here's our USB transceiver here, and it's obviously tied into the Zinc, you can tell,

**Dave Jones:** but it's the physical location. There's no reason why you'd put it there, and then have it go into here, you know, like into this PCI and go somewhere else. It just doesn't make any sense at all. So clearly this is, they're using this ARM processor here

**Dave Jones:** to implement all of the USB, like the communications interface, with the software and things like that. And, of course, the main connects FPGA here is doing all of the oscilloscope processing itself. So, and the other interesting part is, I can't see any high-speed interface between the two.

**Dave Jones:** Look, we've got a, we've got a different, no, it's not even a, barely, not even a differential pair. I don't know, there's some traces running over there. There's nothing on the bottom side here between the two chips. So there's a ton of decoupling and everything else.

**Dave Jones:** But they could be running them on inner layers. This is at least a four-layer board. But basically, there's, you know, no huge big parallel communications between these two that we can at least see on the top. So I'm not exactly sure why. Now not only would this do all the system stuff,

**Dave Jones:** it's probably like running, who knows what little, it could be running an OS, or it could be running some custom thing in the ARM processor there. It's more than capable of running anything you can imagine. I figure maybe they're using the FPGA fabric in this as well

**Dave Jones:** to also run the arbitrary waveform gen. But it's all the way over here. Here's the ARB gen circuitry over here. This is the trigger out. This is the ARB gen output here. You can see the output resistors here. And there's probably, that's, I don't know,

**Dave Jones:** maybe a DAC or a reference or something under there. But yeah, that's all the way over there. But yeah, it could be getting the data right across the board. It just doesn't seem to make sense from a layout point of view anyway. So, hmm, I don't know.

**Dave Jones:** But hey, maybe the Kinects has enough grunt in it to drive the arbitrary waveform generator as well. That's, I wouldn't put it past it. Because the good thing about FPGA is that you can dedicate just a part of the chip, part of the fabric,

**Dave Jones:** to doing that individual task. It doesn't take away from the other task of running and doing the sampling system for the oscilloscope here. Now this particular model of the Kintex 7 here has 160k logic elements, which is one of the lower parts in the family.

**Dave Jones:** It's only 500 bucks, one-off cost. Go figure. Anyway, it's got 2 megabits of distributor RAM, and it's got 11 megabits of block RAM. So if you divide that by 8, that's more than a meg. And this thing, the spec for this thing is 1 meg.

**Dave Jones:** Not sure if it's 1, I think it's 1 meg per channel. So this actually has enough block RAM in it to do all the storage locally in there. But hey, look, we've got some extra memory here and here, and on the bottom as well.

**Dave Jones:** Are they DDR3s? Yep, these are DDR3. But hold on to your hats, these are 1 gig bit. That's 128 megabytes, meg samples, per chip. There's 4 chips, that makes sense, we've got 4 channels, dedicating 1 per channel. But they got 64, they can have 64 meg samples on this thing.

**Dave Jones:** And the spec, I'm pretty sure, only says 1. And the ADC, for you ADC aficionados, I know you're out there, this is the ADC-08D1520, a family that we've seen in oscilloscopes before, very common, basically purpose-designed for this sort of task. This is an 8-bit converter, 1.5 gig samples per second,

**Dave Jones:** dual channel. So that's why we've got two of these puppies on here. So, none of this multiplexing rubbish, you get the full 1.5 gig samples per channel. Nice. But these are actually capable of being interleaved or multiplexed, so you can get double sample rate on a single input channel.

**Dave Jones:** If you configure it that way, 3 gig samples per second, but the spec doesn't do that. So once again, just like the memory up here, they seem to be gilding the lily. It's, you know, this hardware is capable of much more than what I think

**Dave Jones:** they're actually making use of in this thing. I'm not sure if you can see the part number on that, but even if you could, it may not make much sense. I believe it's actually a TI LMX2581E. And no surprises for guessing, given where it is,

**Dave Jones:** right between the two ADCs, it's the PLL. We need to generate our clock. It's the frequency synthesizer, VCO, PLL, whatever you want to call it. And yeah, it's a bit of a beast. And it's generating the sample clock for the ADC. Now let's take a look at the front end here.

**Dave Jones:** Here's the BNC. And take a look at this little ceramic package here. Isn't that a bobby dazzler? Look at that, it's a CRF05. Have a look at the data sheet here, and it is a it's a ripper! It's a 7 gig high frequency read relay.

**Dave Jones:** So they're obviously using, once again, gilded the lily here, using this RF read relay to switch in extra input dividers down in here. That's spared no expense, really. That's just absolutely crazy. So, whew, anyway, check out what we have here. Ta-da! National Instruments part.

**Dave Jones:** Hmm, maybe we can decode that part number. I don't know, they're probably, it's most likely maybe an off-the-shelf thing that they've got rebranded National Instruments. Not sure why they'd do that, they haven't done it on any others, but I don't know. Could it be their own sort of custom front-end ASIC?

**Dave Jones:** I don't know, they're probably big enough to you know, expense to wear the expense on doing that, but anyway. Yeah, this will probably be our output differential driver here, I haven't looked at the part number on that, but that's probably driving the ADC

**Dave Jones:** or something like that. But yeah, it's got all the requisite bits for a scope front-end, pretty much. And this is a 350 gig one. So let's flip this over, have a look at the bottom. Is there much to do in here? What is that thing?

**Dave Jones:** 33078. What's that? I don't know, nothing special. But like I said earlier before, I'm a bit surprised that they didn't shield the bottom of this thing, but they don't need to, like it's right up against that, you know, that die-cast case and everything else.

**Dave Jones:** Like, you know, but they've gilded the lily everywhere else, so yeah, just a little, tad surprising there, but no problems. They've spared no expense on that front-end. I'm sure it works spectacularly. So that is some of the most expensive and gruntiest stuff we've seen in a, you know, any, even

**Dave Jones:** you know, some quite high-end scope teardown. So it's more than capable of doing the job, and you can see where the, in this case, the six grand retail cost goes. You know, these chips aren't particularly cheap, they wouldn't be making these in the millions,

**Dave Jones:** so you know, they'd be making them in the thousands or something like that, so not really huge volume. Let's take a look at our arbitrary waveform generator circuitry. Pop the hood on the can here, and look, we've just got some caps, some inductors, some resistors, we've just got an

**Dave Jones:** LC filter in there. That's it. That's all she wrote under that can. They are really going to town once again just to shield that filter and those inductors. Nice. And there's our DAC. Yep, analog devices of course, what else were you expecting there?

**Dave Jones:** One of the TX DAC parts, and that's a 14-bit 125 meg sample per second, so yep, it's doing the business. And then, yep, we've just got buffers, amplifiers, filters, and everything else after that. And on the output here we've got two THS3091s, high-speed

**Dave Jones:** output driver, exactly what you'd expect. We've got our output termination resistors there, we've got ourselves a poly switch fuse, and a little bit more filtering, and Bob's your uncle. Now this is interesting, this connector here does not poke out the back of the

**Dave Jones:** box. So only the Ethernet and the USB here, so what that puppy's doing? I don't know, some sort of test connector? Something like that, doesn't seem to be going. Internal layers, probably, half of them are ground, and so yeah, I would assume some sort of production

**Dave Jones:** test connector type thing, maybe. And here's our mixed signal logic analyzer part, we've got ourselves some comparators there, I won't even bother looking up, I know they're programmable comparators, and I believe they've got thresholds, allow you to set thresholds on each one. Extensive RC filtering

**Dave Jones:** here, or you know, compensation, the capacitors would be compensating the input divider. And you're going to need that, this is a reasonable 100 MHz maximum frequency input, one gig sample per second for timing mode, of course state, not even sure it might, I think there is an external clock on this, so it could do

**Dave Jones:** state analysis as well. What that means is that it uses an external clock to actually do the sampling, I think that one, the external clock, is 100 MHz maximum. So there you have it, that's the National Instruments VirtualBench torn down, and it is a bobby

**Dave Jones:** dazzler, is it not? And it's, well you pay $6000 for it, but you're getting quality in here, that's for sure. And yes, it is an expensive beast, but it all comes down to how well it works in the software. So I'm, this video's been too long,

**Dave Jones:** what is it, 35, 40 minutes or something? So I'll leave that to another one. So click here somewhere if you want to watch the video of actually having a play around with this thing. And as always I've got high-res teardown photos over on EEVblog.com, so

**Dave Jones:** yeah, I'll probably link that in somewhere down below. Catch you next time. EEVBlog.com
