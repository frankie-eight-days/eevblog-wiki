---
video_id: q_FBwu2K7j0
title: EEVblog #842 - Rohde & Schwarz HMO1202 Oscilloscope Teardown
url: https://www.youtube.com/watch?v=q_FBwu2K7j0
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 33, "3": 57, "4": 73, "5": 101, "6": 117, "7": 133, "8": 149, "9": 165, "10": 181, "11": 197, "12": 217, "13": 241, "14": 257, "15": 277, "16": 297, "17": 317, "18": 333, "19": 349, "20": 365, "21": 381, "22": 397, "23": 417, "24": 437, "25": 457, "26": 477, "27": 489, "28": 505, "29": 525, "30": 541, "31": 557, "32": 577, "33": 597, "34": 625, "35": 649, "36": 665, "37": 681, "38": 701, "39": 721, "40": 737, "41": 757, "42": 777, "43": 797, "44": 813, "45": 833, "46": 849, "47": 865, "48": 881, "49": 897, "50": 917, "51": 937, "52": 953, "53": 969, "54": 989, "55": 1009, "56": 1029, "57": 1049, "58": 1065, "59": 1081, "60": 1093, "61": 1113, "62": 1133, "63": 1153, "64": 1173, "65": 1189, "66": 1213, "67": 1233, "68": 1257, "69": 1273, "70": 1293, "71": 1317, "72": 1337, "73": 1353, "74": 1369, "75": 1385, "76": 1401, "77": 1417, "78": 1441, "79": 1461, "80": 1485, "81": 1497, "82": 1513, "83": 1533, "84": 1553, "85": 1573, "86": 1597, "87": 1617, "88": 1633, "89": 1649, "90": 1673, "91": 1693, "92": 1709, "93": 1729, "94": 1749, "95": 1765, "96": 1781, "97": 1801, "98": 1821, "99": 1833, "100": 1849, "101": 1899, "102": 1931, "103": 1947, "104": 1963, "105": 1979, "106": 1995, "107": 2011, "108": 2027, "109": 2039, "110": 2059, "111": 2079, "112": 2095, "113": 2111, "114": 2127, "115": 2143, "116": 2159, "117": 2179, "118": 2195, "119": 2211, "120": 2227, "121": 2243, "122": 2259, "123": 2279, "124": 2295, "125": 2315, "126": 2331, "127": 2347, "128": 2367, "129": 2387, "130": 2403, "131": 2423, "132": 2439, "133": 2455, "134": 2471, "135": 2487, "136": 2507, "137": 2523, "138": 2539, "139": 2555, "140": 2571, "141": 2591, "142": 2611, "143": 2631, "144": 2651, "145": 2675, "146": 2695, "147": 2711, "148": 2731, "149": 2751, "150": 2771, "151": 2791, "152": 2819, "153": 2843, "154": 2855, "155": 2871, "156": 2887, "157": 2903, "158": 2919, "159": 2943, "160": 2959, "161": 2971, "162": 2987}
---

**Dave Jones:** Hi, welcome to another oscilloscope teardown. We haven't had one of these before, Roden Schwarz. Ha ha! If you thought, you know, the likes of Keysight, Tektronix and LeCroy are top shelf stuff, well this is just as top shelf, if not more top shelf.

**Dave Jones:** Roden Schwarz makes some of the best gear on the market. And I've actually had a little play with this at the electronics trade show some time back, so I'll link in the video here. If you haven't seen that one, check it out. But today, they've finally got me one of these.

**Dave Jones:** It's the new HMO 1202 series, 2 gig samples per second, 2 meg sample memory and super compact form factor. I'll show you some comparisons after, but it's so cute and tiny, this little thing. Completely silent, no fan in it. And curiously, you might notice that they actually haven't printed

**Dave Jones:** any bandwidth on this thing. That's because I believe this is software upgradable from 100 MHz all the way up to 300 MHz. So, hopefully in the teardown we'll see a 300 MHz front end on this puppy. But yeah, it's a really nice, well-built scope.

**Dave Jones:** And prices for this puppy, according to Roden Schwarz Europe, we're looking for the 300 MHz one here, so the full bandwidth one, 1798 euros, or 1960 US dollars about current exchange rate for the 100 MHz model, the lower unit, the 1212. One is 1098 euros, and

**Dave Jones:** which is about just under 1200 Yankee dollars. But it is like, you know, 2 or 3 times the price of like an entry-level Rigol or something like that. But this is a very polished little product. I really like it. But you know what we say on the

**Dave Jones:** EEVblog, don't turn it on, take it apart. Beauty. Just a little look at the outside here. Nice tilting feet on it. Nice rubber here for when you have it sitting on the bench. Doesn't slide around at all. Very nice. You know, you can push the buttons

**Dave Jones:** it doesn't tip over. And you can see, it is, you know, it's reasonably deep like this. It weighs a bugger all. I can't remember the exact figure, but jeez, what is that? You know, half of the weight of the Rigol one. There's no carry handle as such, they've just got this

**Dave Jones:** finger thing in the bottom, which is really quite nice. And it feels like a quality bit of kit. Unfortunately there's no the main buttons here are not pushable, so you can't center the position. The select button you can push, and the times per, the volts

**Dave Jones:** per division, and the horizontal as well, you can push those. But that's a bit of a shame that they haven't gilded the lily and be able to have those pushable for the position. Anyway, this is a mixed signal scope, and I'll show you, might show you that later.

**Dave Jones:** It's also got built-in waveform generators as well, and pattern generator. Really quite an interesting instrument. And check out these sexy gold-plated BNCs. And if we have a look on the back here, not much happening at all. IEC here, we've got a USB host, and we've got Ethernet as well.

**Dave Jones:** The external trigger is on the front, so I don't know why they've got to cut out for the BNC there at all. But anyway, check it out. Made in the Czech Republic, in Roden Schwarz's own factory in Vimperk. And I'll link here to

**Dave Jones:** actually an interactive, you know, like 3D camera thing. You can actually see inside the Vimperk factory, really cool. And so hi to all my Czech Republic viewers. Engineered in Germany, manufactured in the Czech Republic. Fantastic. The good thing about Roden Schwarz having their own factory is that

**Dave Jones:** they can keep complete and tight quality control over this thing. So I expect this thing to be manufactured really well. No corners cut at all. And there you go, they do actually have the bandwidth on the sticker there, 300 MHz, so this must have the option for that.

**Dave Jones:** Oh, and they've actually changed the model number. This one's actually the HMO 1232, so it's the 1202 series. And this is the 300 MHz, so 1232. Hang on, I was completely fooled. I was under the impression that this thing was completely fanless. But I can, we'll see it when we tear it down, but there is a fan in there

**Dave Jones:** and I'll plug it, I'll turn it on, plug it in, and it, you can't hear a damn thing. It is completely silent. I can just hear the bearings. If I hold my tongue at the right angle and hold my ear right up to it

**Dave Jones:** but jeez. Beauty. Warren-y seal. Ha! Can fix that. No whackers. Yes, this one is a demo device, it's a 1232. Look, curiously they've got screws on the bottom, vertically like that. Usually like, you know, you get them down like that, so that's interesting.

**Dave Jones:** So there's two screws there, and two screws there, and two up, oop, and two up the top here. So they've got it screwed together really nicely, but it should be easy. It should just pop off. And I rather like that. That just slides in there,

**Dave Jones:** hooks in the bottom like that, and then the screw keeps that in for that foot. That's really nice design. Thumbs up. Alright, here we go. Let's lift her up, and ta-da! We're in like Flynn! Oh, there's nothing in it! Look, we've got one

**Dave Jones:** main board on the bottom, easily accessible. We can access the top and the bottom sides. This is really nice. Ah, check it out. Tiny little mains power supply over here. Jeez, this is beautiful. Oh, Altera Cyclone 4 I can see already, but there's

**Dave Jones:** nothing else in it! Look at this! Ah, they could have made it thinner, but they're not, you know, they've got to have everything right angle mounted on the board. I can understand why, very reminiscent of the old, you know, Tektronix TDS210 series, which had the board at the bottom like that.

**Dave Jones:** But, yeah, look, there's nothing else in it. Tiny fan, we'll check that out, the silent fan. Oh, with the compliant proper rubber compliant mount. Thank you very much. Oh, yeah. And, looks like we've got shielding over the flat flex cable going down there.

**Dave Jones:** What is that for the... that'd be the screen, I'm guessing. No, that's the screen, that'd be the differential pairs going over to the screen. Check it all out, but very neat, tidy design. There's our analog front ends, the cans. Oh, they're soldered down!

**Dave Jones:** Oh, they might be soldered down at a point! I can see some clips, anyway, hopefully we can get the cans off for the analog front end. But that's neat and tidy, I like how they've got the little cable clamp there. They're a bit, oh, they're a bit flappin' in the breeze there, but they've got

**Dave Jones:** the spiral wrap around those wires. Just single board solution, very well engineered. I love the tiny power supply, it's just great. And of course it doesn't it obviously doesn't need a huge amount of airflow, in fact it's actually sucking in from the side here, so it's sucking in from here

**Dave Jones:** and then it's just blowing straight across here and out the other side, out from the power supply. Neat! Wow! Beautiful. Has it got three times the spit and polish of the Rigol? You know, it's three times the price or whatever, or nearly. Yeah!

**Dave Jones:** Looks great! One thing you'll notice though, is that it's not shielded. It doesn't have the massive amount of shielding, there's some shielding here for the front, but there's basically nothing over the bottom of the board because the plastic case just sits over that.

**Dave Jones:** Roden-Schwarz really know their stuff, so they obviously determined that wasn't required. Of course the analog front ends are all that matter, they've got special low noise ADCs in this thing, so they claim, we'll have a look at that. Oh, in fact nope. It's a national semiconductor.

**Dave Jones:** Ooh, we'll get to that. But yeah, it's, oh actually check out the vias. This is the interesting thing, check out all the vias around the edge here. So they're shielding, this will be a multi-layer board of course, it has to be for the big BGA in there to fan

**Dave Jones:** it out. So it's, you know, probably six or, you know, probably at least six layers maybe. Look at all the vias stitching around the outside, that's to stop any leakage, any RF leakage like out the side of the board, so that helps with the

**Dave Jones:** EMC performance of this thing. But yeah, that looks nice. Ooh, panty shot. Now check this out, this is very interesting. Inside the power supply of course, which we'll no doubt open and take a look at, they've got the traditional molex connector in there.

**Dave Jones:** Cable coming out, it's going to some connectors, you can see those black connectors down there, which plug into the back of this board here, which looks like it has no other purpose than just to have a PCB mounted fuse on, and a nice way to integrate, you know,

**Dave Jones:** to get the cable exiting from the power supply going into here. I don't know why they've done that, it's like over-engineered to the hilt, but I like it. Everything I like about this thing, it just looks very professional and well-engineered. As we say here in Australia, it's just the vibe.

**Dave Jones:** It's the constitution, it's Mabo, it's justice, it's law, it's the vibe, and no, that's it, it's the vibe. I rest my case. That was sensational. And there's the fan, for all you fan, fan boys, Pabst fan, oh, does it get any better? It's the 400 series,

**Dave Jones:** it's the 412-212V, and yep, it's 18 SPL, rated 18 dBA, it might even be running less than that, like no wonder you can't hear the damn thing unless you put your ear right up to it. Beautiful. It's like $13 in a thousand volume from Digi-Key, it's not a cheap

**Dave Jones:** ass fan, spared no expense. And as if the specs on the fan weren't good enough already, look, they've got a custom rubber mount for that thing, oh, and they've even, I don't, look, they've angled that bracket, whether or not that's to give it

**Dave Jones:** some, once again, some vibration to take out some sort of vibrational mode from the rest of the chassis, I don't know, or whether or not they needed to angle it due to airflow, but I can't see why, so that's rather interesting that they've done that

**Dave Jones:** cut out there, but it shows that they've, you know, somebody really gilded the lily on this thing, and it's brilliant, I love it. Oh, check out the power supply, oh, it brings a tear to the eye. Isn't this cute? It is absolutely tiny, and look how well designed

**Dave Jones:** and built this thing is, oh, gorgeous! I don't think I'm going to be able to fault this puppy. We've got ourselves the proper mains earth coming over, it's going to a proper spade lug, properly crimped, everything else beautiful. We've got our mains input here,

**Dave Jones:** has its own heat shrunk choke on there, just for to take the edge off the RFI, no worries at all, you can see that secondary board that we talked about on the bottom there, and you can see how they've just got these cables coming over, and they've even twisted them, and going down to that

**Dave Jones:** bottom board, it's just beautiful. And Nippon Chemicon, thank you very much, no one hung low garbage in here, no Siri Bob, I love the big heatsink plate here, they've got an insulating washer under there, so that's the main switching transistor in there, there's the input bridge rectifier, they've got

**Dave Jones:** the requisite filtering caps, they've got a common mode choke, it's all happening fantastic. The main side fusing is in the back here of the holder, nice looking transformer there, tiny little secondary side heatsink, I guess they don't need that very big at all, it's very efficient,

**Dave Jones:** I guess it's a, you know, very optimised design. I think it is only actually a 12 volt output. That's it, so, yeah, mmm, yeah so there's, I think, there's a fixed, because there's two colours there, so I think they're using two wires just to get some extra current carrying

**Dave Jones:** capacity there. I believe it's just a fixed 12 volt output, so when you design 12 volts only, you can really optimise the efficiency of this thing if you've got a single rail output. Now I think I know why they're doing this bottom board, look, if you have a look down there, there's a cap there, there's a

**Dave Jones:** I might actually take that off, but there's, looks like there's an opto, possibly an optocoupler down there. Why they've got, they're tapping off some mains going over to this board, that's got to be for the 50 hertz line, slash 60 hertz for you yanks, line triggering, that's why they've got a 3 pin

**Dave Jones:** cable going over, they've got the 12 volt coming out plus the line triggering signal as well, so that's why they've done that board there. That's just, that is beautiful. Oh, that is definitely 3 times the spit and polish of any other low end

**Dave Jones:** scope I've seen. And the secondary side caps down in there, they're Rubicons for all you Rubicon fanboys, don't want to leave you out, so yep, no worries there whatsoever, so yeah, top quality. And there's that little AC line coupling board, as you can see, they're just basically

**Dave Jones:** feeding in the mains voltage here with the big isolation slots, thank you very much, everywhere, even under the optocoupler, beautiful. So they're just taking that, feeding that into the lead side of the optocoupler, so they're just driving that, so you know, you'd get your 50

**Dave Jones:** hertz or your 100 hertz, yeah, yes, your 50 hertz out of that, and then you'd, then it's just tapped off the secondary side here, which then goes into the extra, I guess, is it pin 1 there? Looks like pin 1 of that connector, so that sends the 50 hertz signal for

**Dave Jones:** the line triggering over to the main board, and of course everything else is just single 12 volt output with a surface mount fuse just in case. Oh, check out the fluted shaft on the rotary encoders here, beautiful. And these just look like gorgeous and feel like gorgeous rotary encoders, not sure

**Dave Jones:** who makes them, but I like the metal over there that's got, you know, that's surface mounted right down onto the PCB. It's just beautiful, the indents. I could play with those indents all day. And by the way, that front panel came off real easy, there's just 4 clips

**Dave Jones:** on the side there, and it just came off. I love how they're actually not, they've got no nuts on the BNCs here, so there's nothing holding this board in except some screws through these holes, access holes here, that actually screw this main board into the chassis here.

**Dave Jones:** So I take those out, and the whole board complete with BNCs, everything will just pop out, no dicky nuts and washers. Just beautiful. So once I get the screws out of here, and all through there, then ta-da! The board just lifts out, we're in like Flynn.

**Dave Jones:** Look at that, that's just, it's just gorgeous engineering, that is the best design and built scope I've seen, I think. I, let me know if I'm wrong, I mean, I'm just so impressed by this. Beautiful. So as you can see, absolutely everything is on this

**Dave Jones:** one board, is fully self-contained, you can easily test that, and yeah, as a complete product. Absolutely brilliant, so let's get straight into some of the chippies. This one, for all you fanboys. And here's something we haven't seen in a scope before, for all you Atmel fanboys, it's a

**Dave Jones:** ARM Cortex-A5 SAM series processor. Operating at just over 500 MHz or, well, capable of that. You know, these aren't bad beasts at all, they're quite low-power parts. You'll find the SAM series used in things like some of the more modern Hewlett-Packard calculators, for example.

**Dave Jones:** You'll find them in there because they're incredibly low-power stuff. Nothing like this beast, but this is the ARM Cortex-A5 series. And, you know, it's got all the requisite, you know, LCD controller and all sorts of other bells and whistles built in, so I'll link in the data sheet down below for those who want to check it out.

**Dave Jones:** And rumor has it that Rode and Schwartz actually, in a few of their products at least, implement Damsmall Linux, it's called. So whether or not that's actually used in here, or whether it's a complete custom OS, I don't know. You'd have to maybe tap into a debug

**Dave Jones:** port or something like that. And there's the ST Flash for the firmware, no worries. Let's take a look at the memory. And we've got ourselves two Micron DDR2 RAMs here, and these are, you know, you've got to do the stupid, you know, part numbers

**Dave Jones:** decoded thing, I don't know, why can't they put a bloody real part number on there? Anyway, these are 512 megabits a pop. So there's our main beast, our Altera Cyclone 4, and it's an Altera 4C, I'll link in the data sheet if you're interested.

**Dave Jones:** It's sort of like a middling range Cyclone 4, I think it is, you know, 28k logic elements, 608k of block RAM, all the usual jazz. So that's doing all the acquisition waveform processing, all that sort of jazz. And here's our sample memory, it's an SRAM of course,

**Dave Jones:** ISSI, I'll link in the data sheet, it's a 9 megabit synchronous SRAM, 200 megahertz or thereabouts, it's good enough for the purpose. And so that's basically, well, it's just over 1 megabyte per chip, there's actually three of these. So there's an oddball number, so

**Dave Jones:** this is a nominal, this is a 2 meg sample memory oscilloscope, so obviously they're using one of these per channel, and of course sorry, two of these total to give the 2 megabytes or 2 meg sample memory, because it's 8 bits per sample of course, but they've got a third one

**Dave Jones:** because they're probably doing that for the variable intensity display and the segmented memory and all that sort of jazz. And there's our Ethernet controller, it's a micro KSZ blah blah blah, so yeah, it's nothing doing. Here's a national semiconductor part, and just by the looks

**Dave Jones:** of it with the amount of pins in that sort of package, you know it's some sort of transceiver, this is actually an LVDS driver for the LCD display. And for those curious about the logic analyzer functionality, well, there's not much there at all, we've just got some

**Dave Jones:** probably ESD protection would be my guess for that. And basically you flip that over and it's basically going straight into, there's no comparators, there's no level shifting or threshold detection or any, you know, threshold setting, anything like that, that just goes straight into our Cyclone

**Dave Jones:** 4. So yeah, pretty rudimentary. And the pattern generation and waveform generation on the front here, no surprises for guessing, that's basically just straight into the Altera Cyclone 4 there, it's pretty much doing everything there. There might be a couple of just some small stuff,

**Dave Jones:** but it's basically all the FPGA, which is exactly what you'd expect. We've got ourselves a 74HC4052 there, a few other parts, nothing special, just some op-amps, that's going to be for, presumably, the analog drive for the function generator. It's not a high-speed function generator, it's like up to 50 kHz

**Dave Jones:** or something, nothing special, that'd be generated by the FPGA again. And probably relay switching to switch that puppy off. Tell you what, one thing I really like is the labeling on all these little test points here, very nice. Look at this, CS, oh,

**Dave Jones:** FRAM. What? Anyway, look, SDI, S-Clock, they've got, you know, lots of nice little silkscreen labels, very nice. There's the JTAG for example. It's just, yeah, very nice. Got them all over the board. We've got ourselves a couple of DC to DC converters down here, we need those.

**Dave Jones:** There we go, 2.5 volts tells you we need those because we've got, oh, 1.9 volts? Look, 1.9, okay. It's usually 1.8, are they allowing for some drop going across the board or something like that perhaps? Interesting, there's our 5 volt. I expect a 3.3 volt one somewhere.

**Dave Jones:** Hmm, and they've got regulators all over the shop, there's lots of linear ones there, you can actually see those. They've got, oh, there's minus 11.5 plus 1.3, plus 1.9 again, local regulation. There's got plus 5 volts, they've got minus 10 volts, oh man.

**Dave Jones:** So that must be a switch, maybe that's a switch cap filter for the negative rail there. It's more power supply goodness. Once again, yeah, negative 10 volt rail plus 10, so yeah, I think that's a switched capacitor filter, because there's no, or is that an

**Dave Jones:** inductor? Anyway, it doesn't look, oh yeah, it could be. Small amount of magnetics there, they could be doing that, but usually I think that is an inductor actually, so it might not be a switch cap filter. No, I don't think it is. Check out all the bypass caps there,

**Dave Jones:** got on the back of the SRAM there, so this is the same chip they've got on the other side of the board here. And they're really gilding the lily. Probably, you know, like different values, you know, 1N, 10N, 100N, something like that, just to cover the

**Dave Jones:** different frequency ranges. And if you want to see what's typically required on the back of an FPGA, like this Cyclone 4 here, here's all the bypassing for all of the FPGA. It's typically in the middle, you'll find the power pins are around the middle like that with IR around the

**Dave Jones:** side, and it's a bit of an art to actually bypassing FPGAs like that. It's actually good fun, trust me. And along the bottom of the board here under the shielded cans, once again, you can tell by the silkscreen labels, very good, like trigger DC, so they've got some op amps here, what are they?

**Dave Jones:** Not quite sure, some on semi generic job probably, or you know, probably precision op amps or something, I haven't looked them up. Anyway, trigger AC, DC gain 2, something attenuation I assume, a low frequency, and what's CT? DC gain, there we go, things like that.

**Dave Jones:** It does actually have auto calibration on this thing, so it actually generates signals of certain amplitudes and then can actually, you know, do offset and gain calibration, stuff like that. So maybe that's what that has to do with. And of course everyone wants to see the ADC, and here it is.

**Dave Jones:** National Semi ADC 08D1000, actually datasheet says not recommended for new design, so maybe this is a throwback from previous Haymeg designs, because this comes from the Haymeg stable, Roden-Schwartz now own Haymeg, so you know, it probably stems from that design. Anyway, this is a dual 8-bit

**Dave Jones:** 1 gig sample per second ADC, exactly what you expect, because this is a 2 gig sample per second scope, so obviously they interleave those if you've got a single channel turned on. If you're using both channels, of course, that 2 gig halves down to

**Dave Jones:** 1 gig sample per second. But they actually promote this scope as using a low noise, you know, like some special low noise ADC, so I thought maybe they might have rolled their own or something, or using something special, but this isn't anything particularly special.

**Dave Jones:** And by the way, found out what the 1.9 volt rail is for, it's for this puppy. It's nominal voltage rail, 1.9 volts. Like, meh, why? And there's our PLL, or it's a clock generator. ICS, it's actually, I've got a datasheet, so it's actually an IDT part, but

**Dave Jones:** I don't know, whatever, 84S42 something or other, I'll link it in down below. It's a dual output RF frequency synthesizer generating the clock for the ADC. Yeah, where's the crystal? It's not there. Once again, half the parts aren't populated. This is very common in these type of designs for loop, you know,

**Dave Jones:** the loop stability and stuff like that, so yeah, they've just put the pads there and where's the crystal? Where's Wally? That's the bottom of it. Where's Wally? I am not finding a crystal anywhere around here. Like anywhere. There is no Wally. Wally does not exist.

**Dave Jones:** There's nothing, even all the way over there's just, nothing. Where is it? Grrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr! Crazy thing is, pins 8 and 9 here, like it's got a built-in oscillator, which requires an external crystal, of course, and 8 and 9 are the pins, and they go out to the pads here.

**Dave Jones:** There is no crystal fitted, which is all hunky-dory fine, okay, they've switched it to the external clock input but yeah, that clock's coming from somewhere which I still can't find. I don't know. I'll look on the high-res photos of the board later. I'll link in the high-res photos.

**Dave Jones:** It's probably, everyone's probably screaming at me. It's probably an obvious crystal somewhere I can't see. And there's the money shot. There's our 300 MHz analog front end, or the top side of the board anyway. There's not a huge amount on the bottom side, I'll show you in a minute.

**Dave Jones:** I lifted, or desoldered the CAN on this thing and not a huge amount, very typical of a front end. We've got two Japanese relays in here, very nice. And just a whole bunch of regular stuff. We'll check out what these are, get a bit of a closer look.

**Dave Jones:** And no surprises for finding the National Semiconductor LMH6518. We may have even seen this on several scopes in the past. It's a 900 MHz programmable gain amp, so a PGA, digitally programmable gain amp with a differential output, so you can see the output here.

**Dave Jones:** There's the differential output tracers going out there. And so single-ended in to differential out, programmable gain amp. They've got, you know, they'll have the serial input here to select your programmable gain. So yeah, very nice puppy, exactly what you'd expect. The rest of it's just going

**Dave Jones:** to be like, you know, discrete FET. You know, discrete transistor front end, things like that. The op amps are going to be, you know, just for offset and stuff like that. So that's, yeah, that's about all she wrote for a 300 MHz front end.

**Dave Jones:** Amazing. And I promised to show you the backside, and as I said, yeah, not a huge amount happening there, just some large passives and 1206 passives, and just some more miscellaneous, probably just little amps and things like that for setting some offset stuff.

**Dave Jones:** I really like these BNCs though, they're in big cutouts in the board, soldered directly on there, reflowed in. They ain't going nowhere. And I just half popped off the can for the external trigger input here because it was difficult to get to the bit over there that was soldered, would have had to get the other can off,

**Dave Jones:** blah blah blah. Couldn't be bothered. There you go, there's a solid state relay, there's some amps and other things in there. Nothing real special on the external trigger input. By the way, just on that crystal, the only one I could find is over here on the Atmel SAM chip, so what's going on

**Dave Jones:** there? Anyway, OxOut didn't really take a look at that. Interestingly, they've got an output fuse here, right in the output line, look at that, gilding the lily a bit, but nice. So there you go, that's all she wrote on that board, and I'm quite impressed by that.

**Dave Jones:** It's a beautiful piece of engineering, all on one board, I love the BNCs, gold-plated, gilding the lily, literally. And it's, yeah, very nice. It's not really folded, it's not a huge powerhouse. I mean, this thing's only like I think rated for 10,000 waveform updates per second.

**Dave Jones:** They're obviously able to do that in the Cyclone 4 and, well, the Atmel SAM Cortex-A5 there, but yeah, it's doing the business. Nice piece of work. Fairly simplistic front end for the 300 megahertz, but hey, this is Roden Schwarz, they know what they're doing, I'm sure it performs the business.

**Dave Jones:** It doesn't need to be any more complex, I mean, you can do it with discrete transistors and a programmable gain amp and, you know, a few level shifters and stuff like that. Bob's your uncle. So there you go. Neat. Efficient design, I like it.

**Dave Jones:** And as always, high-res photos of the board at EEVblog.com. And as usual, just really not worth the effort for the front panel board in here, for the knobs and the, you know, the rotary encoders and switches and things like that. Nothing doing there.

**Dave Jones:** And we've just got the LCD module in there, but this is what we wanted to see. ... ... Oh! Forgot to plug the wires back in there, didn't I? Ah, bloody hell. Murphy will get you every time. At least I didn't do all the screws in the top.

**Dave Jones:** ... ... ... ... D'oh! I didn't press record on the last part of the assembly there. Sorry! Alright, plug her in. And it does have a real clunking power switch on the back of it, but once it's on, it does actually have a soft power button

**Dave Jones:** and that is how fast it boots, folks. Bloody beauty. Now this certainly won't be a review, because this thing's gone for well over, like, I don't know, a 40 minute teardown or something like that. But yeah, I've covered some of this in my initial

**Dave Jones:** play with it at the trade show, but I'll have to do a separate review on this, because I just really like this. The user interface is just brilliant on this, and I heard that Rodin-Schwarz actually have an entire division devoted to user interface stuff.

**Dave Jones:** People who just work on this, not just, you know, the oscilloscopes that's a tiny part of their business, but you know, their whole suite of high-end products. And it really shows, there's lots of nice touches in the user interface. For example, like, when you expand the menu

**Dave Jones:** like this, okay, it chops off a couple of your divisions here, of course, but when you turn it off like that, it actually puts it back, and then it flips them around to vertical like this, so you can still see what they are, like 50 ohms for example, and

**Dave Jones:** then you can actually call that up like that, and it expands it out and shows you exactly what it is. That's just, it's very nice. And the annotations on the display are really nice. Shows you that it's currently in refresh mode. Let's go into the acquire mode, and

**Dave Jones:** it's got high resolution mode that boxcar averaging and stuff like that, so we can turn that on, and you'll notice that we've gone into 10-bit resolution mode there, so we can turn that off. There we go, high resolution, refresh mode, resolution 10 bits.

**Dave Jones:** But of course you can't see the 10 bits on the screen on ordinary scopes, right? Digital scopes, you can get that extra high resolution, and you only can really make use of that if you do, you know, FFT analysis, or you export the data, or something like that.

**Dave Jones:** But this one actually, if you go into display, I've shown this before, it has a virtual screen, so you'll notice that we've now got cursors there. You'll notice these cursors turn on, and then we can actually move our display like that, and we can see all of

**Dave Jones:** our bits in there. We can get much better detail on the data. It's just very nice. Very nice. And it's got inverse brightness, it's got false color mode, you know, color intensity graded display for those who like that sort of thing. Dots for you dot aficionados,

**Dave Jones:** but yeah, that virtual screen is pretty cute. And then we can change our interpolation here, we've got linear, and sample and hold as well, which is terrific. I haven't seen sample and hold on a scope in, oh man, since the 80s or something like that.

**Dave Jones:** Anyway, it might be useful to someone. I like the fact that you can acquire modes, you can get maximum waveform rate, you'll notice 5 samples a second in, or you can go maximum sample rate, or you can go automatic. So you'd probably just leave it on automatic

**Dave Jones:** mode most of the time, and the sample memory's dropped down to 480k points, it just chooses that. So, you know, if you want maximum update speed, what do you want, maximum sample rate, you know, so it's all there. It's got various arithmetic modes as well, it's got your regular envelope mode,

**Dave Jones:** your regular averaging, the smoothing mode as well, you add the smoothing mode on, you'll notice it went up to 12-bit resolution here. A beauty and something you rarely get, is an adjustable filter here, so we can, you know, based on, it'll change based on

**Dave Jones:** the current sample rate and memory and everything else. But yeah, we can actually set our filter rate on that, actually does that in digital, it's probably doing that, I don't know, is it doing it in the FPGA? I wonder? Or is it doing it in the ARM Cortex A5?

**Dave Jones:** Hmm, it doesn't matter, either way, this is a very super responsive scope, it's just, it is really really nice, I like it. But of course, one of the major limitations of course, just like any compact scope like this, even though it's only two channels, I hate the fact that the external trigger in here

**Dave Jones:** it's really confusing, the external trigger's usually over here, but they have colour code that it's just, you know, like, but you ignore that. Like, you know, so I, you know, force of habit just means I ignore that, you'd get used to it. Anyway, channel 1, channel 2, share the same vertical control here

**Dave Jones:** so you've got to switch between the two like that. And you'll notice that depending on the time-based sample rate, everything else, we can, with smoothie mode and high-res mode, we can get up to 16-bit resolution. Of course it's only got an 8-bit converter in there, but you know, these high-res modes

**Dave Jones:** on modern scopes do a reasonable job. And I'll tell you what, I'm impressed by the probe adjust here. I mean, it's in the setup, you just go in here and, whoop, there it is. Probe adjust, and look at that. I mean, it gives you the, like, the waveform display there

**Dave Jones:** live in a little window, plus exactly how to connect it to the input here. It's just lovely. Love it. And it actually tells you whether or not you need to align it. I've never seen this feature in a scope. That's brilliant, because, you know, you've already

**Dave Jones:** it's already been tweaked. Fantastic! And you can go full screen if you want on that. And if we tweak it, let's see if it requires adjustment. So it shows us that we have to adjust the low frequency one on the probe itself. These are switchable x10 probes.

**Dave Jones:** And then we can go to the next step, so we can adjust that. I mean, we can tweak that live. There we go. I'm tweaking that with my screwdriver. Tweak that live, and that's beautiful. And then next step, the high frequency compensation on the

**Dave Jones:** cable end, the connector end, down here. So we have to adjust those, and you can see, we've got some ringing in there. We can fix that. But of course, no matter what we do to the adjustment down in here like this, we're always going to get the

**Dave Jones:** ringing on here like this. Why is it so? Well, on the high frequency adjust? Because we've got this big antenna earth lead here. Ah, get rid of that! Trap for young players. What we've got is they've actually got a little hook here, we've got a little probe hook

**Dave Jones:** that allows you to, quite nice, look, it just sits in there like that to get a real, look, low inductance path on there, and you'll notice that our signal is now beautiful! Look at that! So now we can adjust it. There we go.

**Dave Jones:** Ah, that's what we want. Right, now I can adjust one of the pots in there, there's two pots, but you'll notice that, like, it tells you what you want is the shortest possible rise time, okay? So that's what it's telling you there. So we

**Dave Jones:** want, that's the shortest possible rise time, okay? So there, so you want, and let's go to the other pot. Let's go to the other pot, and we can just trim that. So it's kinda, it's a little bit touchy. A little bit touchy, there you go, that's probably

**Dave Jones:** getting close to ideal there. Eh, somewhere in there, somewhere in there. That's ideal, what we want. We don't want too rounded like that, we don't want any overshoot like that. So it's just very nice user interface touch here to explain to people how to actually adjust

**Dave Jones:** all of your three different adjustments. You've got two adjustments down in there for your high frequency stuff, that's why it's at the end of the cable here, and your low frequency adjust right up there. So that's just beautiful. Thumbs up. And check out the power consumption

**Dave Jones:** in standby mode. It's only half a watt, absolutely tiny, but of course the power factor's gonna be really poor, so that's gonna result in 6.3 VA there, but yeah, beauty in standby. And operating, only 18 watts, and power factor, actually not that great when it's operating, so

**Dave Jones:** it's not terrific, but it doesn't have, you know, active power factor correction in it, or anything like that. So there you go, a measly 18.5 watts. And if you're wondering why we didn't see a lack of logic analyzer, or typical logic analyzer input circuitry,

**Dave Jones:** well, it's in the pod here. This is the HO3508 logic probe. It is optional, I believe. But you don't, I don't think you have to pay for the software for it. I think it's built in, but you just need the probe. So technically

**Dave Jones:** if you, I think if you built your own probe, don't quote me on this, but I believe that's the case. It uses standard 0.1 inch headers, everything else, so you could probably make your own probes to do this. Anyway, this looks like, you know, a pretty ordinary, look, no

**Dave Jones:** shielded cable, no nothing. So I don't think it's, you know, particularly high performance. But if we have a look inside, ta-da! It wasn't easy to get open, they were really clipped together cases, a lot of force required, and ta-da! We do have quite a

**Dave Jones:** bit of stuff in here. And what we've got here looks like some ESD input protection here, and no surprises for finding high speed ECL comparators in here. So these are dual high speed PECLs, these are AD CMP562s, and here's the data sheet. And

**Dave Jones:** these puppies are basically exactly what you'd expect to find in a front end like this, because you need a comparator so you can set the threshold voltage. And of course it's adjustable threshold voltage on this, so you need to be able to adjust that and

**Dave Jones:** have a comparator for each individual channel. And these are real high performance high speed puppies, and they're of course ECL output. So you can see, you probably can see the, yeah, there's the differential pair output there on the backside here. Of course these are

**Dave Jones:** dual chips, so we need 4 of them, so there's our 8 channels. So yeah, they're actually not, so actually you can't I stand corrected, it looks like you can't easily make your own probes, because they're not just regular CMOS inputs, they're actually ECL inputs.

**Dave Jones:** So yeah, you've got to take that into account. Although, you know, you could design and build your own, but yeah, it's not a matter of just hooking up to some probes and whacking, you know, CMOS or TTL inputs in there. So we've got

**Dave Jones:** ourselves a little DC to DC converter here, that would be generating the negative rail required, because it can go down to negative I think, so they'd be doing that there, and I'm not sure what that thing's doing. N5311, that could be, you know, maybe if I had a

**Dave Jones:** bit more Google-fu, at the moment I might be able to find that, but yeah, it's not a DC to DC converter, because there's no magnetics around there. Well I'll tell you what, there's a surprise, Z8F0123. I thought this was a Zilog micro, and I was right,

**Dave Jones:** I looked up the part number, little 8-pin Zilog microcontroller. Wow, haven't seen one of them in donkey's years. God, are they even still around? Making their micros probably, anyone still using Zilog micros? They were pretty decent parts back in the day, I guess they still are,

**Dave Jones:** but you know, yeah, I think they're certainly not mainstream these days, but anyway, what that's doing in there is rather interesting, it doesn't have a built-in DAC, but of course it's got PWMs it's got an ADC in there as well, so maybe they could be using that, the PWM, to generate the

**Dave Jones:** DC threshold level for the comparators perhaps. Yeah, I don't know, are they using some sort of security feature perhaps? I don't know. And there it is compared to the Rigol DS1054Z, which is already a nice small compact scope, this thing is even smaller

**Dave Jones:** look, it's significantly shorter like that it's a little bit higher, but yeah, and I said, like, it's not quite half the weight, but it's just, love it! Doesn't take up any bench space at all, it's brilliant. And there they are side-by-side, and I

**Dave Jones:** you know, I didn't really think about it, but this, the Rigol actually does look a bit weird, how it's like just elongated like that with its big wide screen like that. When you actually put it next to this one, I much prefer the Rodin Schwartz, it just looks like a

**Dave Jones:** more traditional sort of, you know, scope. And you're getting the same number of divisions, we've got 12 divisions across, and we've got 12 divisions across on here, because the Rigol throws away a lot of space with the measurement menu down the side, with all these extra buttons down the side here, so

**Dave Jones:** you know, I, yeah, give me the Rodin Schwartz! But you know, not really a fair comparison between these two, because this is, you know, the entry level scope on the market, I mean, well the 50 MHz version of course is only $400, whereas this is $1200

**Dave Jones:** for the entry level 100 MHz version of this, but hey, you do get mixed signal capability, and the pattern generators, and the component tester, and all sorts of other jazz and I think a better user interface, and, but this thing's 4 channels, this thing's only 2 channels, but the 100 MHz version

**Dave Jones:** here, if you're talking equivalent bandwidth without hacking this thing, this is $800 compared to $1200, but yeah, the 4 channels is really useful, but, oh yeah, if you got the money and you just want a 2 channel, you know, a really nice compact 2 channel scope, oh, the Rodin Schwartz

**Dave Jones:** very tempting. And, of course, as I said, it boots up... boots up so quick, it's just ready to go. Fantastic! Bam! Straight in. The Rigol's still sleeping. Give me a break. And I actually prefer the screen on the Rodin Schwartz it's clearer, it's, actually, the window

**Dave Jones:** area, the waveform window area is actually bigger I believe. Yep, quite significantly bigger, that's like 135mm, we're talking about 150mm. 150! Ah, beauty. Just a quick note on the user interface side of the Rodin Schwartz here, as I said, I would have preferred the external input, external

**Dave Jones:** trigger input over here, and then the trigger, I like how they've used the colour coding here, it's got everything, look, it shows you slope, like real, you know, like old school slope, you know, like it reminds me of the old tech you know, ah, yeah, beautiful.

**Dave Jones:** I would have preferred like that over here like this, so go vertical, horizontal, and then trigger and then have you trigger BNC over here, but I guess it's too late, they're not going to redesign it, just because I had a whinge in a video.

**Dave Jones:** And as I've shown in a previous video, one of the cool features of this is this quick view analyse function, I love how they've separated that there, you whack quick view on, and look at this, it gives you everything you want to know about your waveform, absolutely brilliant.

**Dave Jones:** So look at that, it gives us our mean level, it gives us our rise time, fall time, exactly how you want it, we've got, it's got a hardware frequency counter as well, it gives you the time and the frequency, it's just great. But as

**Dave Jones:** I showed in a video, if you've got the second channel on, it will only quick view will only actually analyse the one channel at a time, it just gets rid of everything else. Which is a bit unusual, but eh, I guess it's a clarity, user interface clarity

**Dave Jones:** thing, but yeah, that's pretty jazzy. Anyhow, that's a rather lengthy teardown of the new Roden Schwartz HMO 1202 series, the 300 MHz model, and I love this little, I love small, compact tools with nice user interfaces, and this thing just really fits the bill, so no doubt you'll

**Dave Jones:** see this in future videos, because I like it, I'm going to use it a lot. Because the good thing about this is small and compact, for my purposes I want to get things in a shot, you know, so if I'm working on like, you know, a board down here and I want to get the scope

**Dave Jones:** in the same shot, having that little small compact scope actually is quite useful for me personally in terms of doing videos and stuff like that. But anyway, so I'm sure you'll see more of this puppy, thank you very much Roden Schwartz for sending in this unit.

**Dave Jones:** And if you liked the video, please give it a big thumbs up if you want to discuss it, EEVblog forum, or blog comments or YouTube, wherever you want to leave them, whichever is your flavour. And as with most of my teardowns, high res photos over on EEVblog.com

**Dave Jones:** as well. Catch you next time. EEVblog.com
