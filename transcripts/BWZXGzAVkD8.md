---
video_id: BWZXGzAVkD8
title: EEVblog #360 - Rigol DS2000 Oscilloscope Teardown
url: https://www.youtube.com/watch?v=BWZXGzAVkD8
source: youtube-asr
timestamps: {"0": 0, "1": 19, "2": 31, "3": 42, "4": 55, "5": 69, "6": 84, "7": 108, "8": 128, "9": 136, "10": 159, "11": 175, "12": 194, "13": 219, "14": 232, "15": 244, "16": 262, "17": 280, "18": 294, "19": 312, "20": 338, "21": 355, "22": 374, "23": 392, "24": 407, "25": 426, "26": 442, "27": 458, "28": 466, "29": 482, "30": 493, "31": 509, "32": 528, "33": 545, "34": 559, "35": 570, "36": 584, "37": 599, "38": 618, "39": 628, "40": 639, "41": 651, "42": 665, "43": 681, "44": 694, "45": 713, "46": 731, "47": 742, "48": 751, "49": 762, "50": 778, "51": 789, "52": 801, "53": 820, "54": 841, "55": 854, "56": 867, "57": 888, "58": 896, "59": 910, "60": 940, "61": 953, "62": 971, "63": 983, "64": 1015, "65": 1033, "66": 1045, "67": 1056, "68": 1070, "69": 1083, "70": 1099, "71": 1121, "72": 1137, "73": 1165, "74": 1177, "75": 1207, "76": 1217, "77": 1236, "78": 1248, "79": 1262, "80": 1279, "81": 1299, "82": 1312, "83": 1340, "84": 1360, "85": 1376, "86": 1391, "87": 1408, "88": 1421, "89": 1439, "90": 1458, "91": 1468, "92": 1486, "93": 1504, "94": 1522, "95": 1536, "96": 1549, "97": 1558, "98": 1578, "99": 1595, "100": 1612, "101": 1623, "102": 1635, "103": 1651, "104": 1671, "105": 1695, "106": 1715, "107": 1726, "108": 1746, "109": 1763, "110": 1777, "111": 1791, "112": 1801, "113": 1818, "114": 1832, "115": 1854, "116": 1868, "117": 1906, "118": 1917, "119": 1933, "120": 1951, "121": 1964, "122": 1976, "123": 1998, "124": 2017, "125": 2026, "126": 2041, "127": 2054, "128": 2070, "129": 2084, "130": 2098, "131": 2108, "132": 2128, "133": 2142, "134": 2153, "135": 2168, "136": 2229, "137": 2243, "138": 2260, "139": 2275, "140": 2285, "141": 2301, "142": 2310, "143": 2323}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Yes, I'm excited. It's another oscilloscope. It's a new Rigol DS2000 series. And we haven't torn down a Rigol oscilloscope since the DS1052E, and that was years ago.

**Dave Jones:** Pretty excited to see what's inside this one. See if the build quality's any good. See if they've improved since the DS1052E. So you know what we say here on the EEVblog, don't turn it on, take it apart.

**Dave Jones:** And for those of you who haven't seen the two scopes side by side, the new 2000 series has a much bigger screen. It's absolutely huge. And of course it's bigger, wider.

**Dave Jones:** It's about the same depth, but it's a a fair bit heavier. So there's going to be lots of metal and shielding and stuff inside this puppy compared to the older 1000 series scope.

**Dave Jones:** So let's crack it open. And I do expect this thing to be pretty easy to take apart. There's no power button on the top, which when I took my original Rigol 1000 series apart, I actually broke off the knob.

**Dave Jones:** So we've got a a few screws down the bottom here. That's about I think. Well, that's probably it under there. There we go. Couple under the handle and they should pop right out.

**Dave Jones:** They're a little bit tricky, those top ones. Ta-da! And exactly what I expected, full metal shielding. Check it out. It's got the fan on the side. And to get this off, it looks like we're probably going to have to take off this BNC nut here and a few screws on the top and the side there, but that should just lift off easily.

**Dave Jones:** And check out even the shielding they've put around the IEC mains input connector there. I like that. That's terrific. That is well done. They've uh got of course metal threaded inserts down in the case here, but let's take the rest of it apart and check out these two pin headers penetrating the metal shield here.

**Dave Jones:** Oh, it's got hack written all over them. If I look at the silk screen through there, that says SPI boot. Oh, that could be a hacker's delight that one.

**Dave Jones:** And this one here is uh look at the silk screen, it's got ground, VCC, reset, and uh what is BRGD? Whatever that means. Go figure, but yeah, interesting. And here we go.

**Dave Jones:** I think I've got most of the screws out. Let's hey. Hello. Yeah, looks like it just lifts out. The fan is probably going to be attached over here, but that shouldn't be a a drama.

**Dave Jones:** Ah, fan and and well, power. Here we go. Tada. We're in. Ah, beautiful. Look, it's all laid out for us. Wonderful. This is really looking quite nice. I'll just disconnect the main power.

**Dave Jones:** Rather tight. There we go. The fan, bang, and that's it. Ah, that's just beautiful. I love it when products are so easy to take apart like that. Wonderful. And at first glance, this board just looks beautifully laid out and uh there's the input shielding can there, couple of main uh heat sink devices.

**Dave Jones:** We'll go into detail of all the parts, but it's just beautiful and accessible. I love that. And it looks like this board is going to pop out pretty easy, too, with these main screws here with these gold uh pads on them.

**Dave Jones:** And uh if we just undo that flat flex cable there, I think the rest of the board should just lift out. Probably have to do maybe undo the buttons on the front uh the knobs on the front or something like that, but that's the main board.

**Dave Jones:** And here is the rest of the chassis. And check it out. They've got another beautifully shielded power supply here. They've uh I don't see any uh RFI uh bead on there at all.

**Dave Jones:** And it's probably not easy to see down in the IEC connector down in there, but uh they're nice, properly heat shrunk mains rated cabling coming down. Beautiful little earth bonding point there with two separate wires, one coming directly from the IEC connector, the other one going off into the power supply.

**Dave Jones:** They're heat shrunk. They're properly crimped. There's a shake-proof washer on there by the looks of it. It's all really tight. Beautiful. Well designed. And look at that, they haven't skimped at the cable retention mechanism either.

**Dave Jones:** Beautiful. That's a double-sided uh adhesive tape one stuck down. It's all neat and tidy. It's just the correct length for the cable harness, just to just as long as it needs to be to get access to it and assemble and uh service it by pulling it back apart as well.

**Dave Jones:** All righty, probably not designed by Rigol. Um probably uh subcontracted out to a power supply specialist company. Most companies do that. So, I'd expect to see a quality and safe well designed power supply, probably not using prime spec you know, Panasonic caps or or something like that, but I certainly wouldn't expect one hung lows.

**Dave Jones:** Well, I may have been a little bit wrong on the uh third-party thing, cuz that's clearly got Rigol on it, and I can't see any other third party markings on this power supply board, but uh wow, this is really good, folks.

**Dave Jones:** This is very well designed. Check out the silastic everywhere for starters. They've silastic everything down. They're doing everything right. Let's have a look here. They've heat shrunk their inductors, their chokes on the input here.

**Dave Jones:** They've heat shrunk those, they're using proper mains-rated caps, of course, as you'd expect. Um the uh inductors and transformers look first-class quality. Hard to tell, but yeah uh you know, it's just the vibe of it.

**Dave Jones:** Australians will know what I mean. And uh the capacitors here, output all the output capacitors, they're um Epcos brand. There we go. They're not bad. They're not uh Capxon or anything uh horribly bad like that.

**Dave Jones:** They're all 105° C rated. Epcos. I like it. Lots of uh chokes on the output, as well. So, they're really doing really doing the business there. Not sure what uh those output devices are.

**Dave Jones:** Not that fussed, really, but uh they're, you know, they're all nicely uh insulated. They're doing all the right stuff. I see shake-proof washers on there, I believe. And uh that, folks, looks like a very nice power supply.

**Dave Jones:** You can see the split. I haven't taken the board out yet, but you can see the isolation, the high-voltage isolation slot underneath those optocouplers there, feeding back uh to the primary from the isolated secondary side.

**Dave Jones:** So, they're certainly doing the right stuff there. There doesn't seem to be a matching slot under there, although there could be. I'd have to take the board out to see that.

**Dave Jones:** But, uh they certainly spared no expense on the silicon. Stuff just blobbing all this stuff down. There's your input bridge rectifier. By the looks of it, that's not uh heat sunk at all.

**Dave Jones:** Doesn't really need to be, but check this out. I like this. Bit of attention to detail. Look at that diode there. It's got a little ferrite bead on the cathode there of that diode.

**Dave Jones:** Go figure. They've determined, "Well, we need to slightly take the edge off that thing, so I slightly take the edge off the waveform there. So, we're going to whack in a uh an RF bead onto that thing.

**Dave Jones:** Brilliant. I love it. Huge thumbs up. More uh isolation slots down here. There we go, to separate the earth from the uh active and neutral side of it. More slots down in there and up the top there.

**Dave Jones:** Whoop. There we go. I don't think I can find a single thing wrong with that power supply, folks. I'd expect that one to last quite some time. I assume that the main uh 450-V um rectified DC uh cap there is also an Epcos.

**Dave Jones:** It looks uh very similar. So, I'd expect that one to last at you know, a reasonable length of time. They've certainly done all the right engineering in that. Small attention to detail stuff.

**Dave Jones:** They've cable tied down that main cap. They've gone, "Well, the silicon is not good enough. We're going to do both." Really belt and braces kind of engineering. I really love it.

**Dave Jones:** And uh we've got our input surge protection, of course, input filtering stuff. So, it's certainly designed uh to meet all of the international requirements for such switching power supplies.

**Dave Jones:** I'm sure they'd have no problem at all getting that type approved in any country. Now, we'll take a look at the main board in more detail here, but beautifully laid out, nice and modular.

**Dave Jones:** Input can over here, your input triggering circuitry over here. Some power supply stuff up here. A Rigol branded chip which we'll take a look at here. And we've got clip retained heat sinks here, but I'll just mention somebody on the forum.

**Dave Jones:** Their DS2000 series scope actually, these retaining clips weren't soldered on and they actually popped off. And his scope failed, it probably shorted out something else and it went ping.

**Dave Jones:** And apparently, so it's something to watch out for. It'll be interesting to see once we get this board out if mine is soldered correctly, but the soldering looks first class on this by the way.

**Dave Jones:** Anyway, we've got processing up the top here, Blackfin processor we'll take a look at. More memory stuff. Um we've got all the power supply nicely modular, just in the individual little modules.

**Dave Jones:** You can see the individual ground planes surrounding those. Beautiful. Now, the only flux residue I can find on the board is around this presumably hand soldered front panel BNC connector here.

**Dave Jones:** You can see some of the residue left on there. Not a huge deal, really. This looks like these the soldering points over here. That would be for the front panel test point, test signal.

**Dave Jones:** But apart from that, the soldering really is first class on this thing, and I cannot fault it at all. And this is the external input trigger It's got it even written down on the board there, external input.

**Dave Jones:** There's an input uh series resistor there. Goes into a few large 1206 passives there. Couple of sot a bunch of sot 23 devices around there. That's a Texas Instrument branded chip, probably some sort of uh op amp or something.

**Dave Jones:** I'm not sure. And another device down there, a little Look, little MLF package. Not sure what's happening there. Another TI part. But quite a few TI parts there. P274 22KAV31.

**Dave Jones:** Don't know it offhand. Uh there's a voltage reference test point. A couple of more devices around there. It's all pretty bog standard stuff. And a 4051. You got to have a 4051.

**Dave Jones:** And check out the via stitching all the way around this external input circuitry. They've got going, "Oh, man, I don't want anything to get in or out of this sucker.

**Dave Jones:** Let's just stitch the hell out of it." There's a couple of switching power supplies up in the top corner here. Beautifully laid out. Look at the heavy via stitching on this stuff.

**Dave Jones:** Beautiful, nice tight compact layout. They've got them um uh separately isolated in terms of the grounds. I'm not sure what voltages they are. They're probably, you know, core voltages for uh some of the main chips like 1.2 V core or something like that.

**Dave Jones:** Perhaps we've got a TDK buzzer on there. Spared no expense. There's a 25 MHz uh oscillator there. It's not the main one. There's a couple of them on this board.

**Dave Jones:** So uh that one's powering a chip. But look at this. Look at this puppy here. There's something on top of that chip. There's something on top of that. It's really rather weird.

**Dave Jones:** So that oscillator is clearly going into this little puppy here and and then maybe that's sort of some sort of clock driver or something like that for the main Rigol device up here, which is a UZ0141.

**Dave Jones:** Who knows what that is? It could be a custom ASIC device. It could be just a you know, a re-badged off-the-shelf thingamajigger. We don't really know, but clearly they've tried to disguise this chip down here to fora for this main Rigol chip, which is driving presumably the clock in that thing.

**Dave Jones:** I can only presume by the location of this oscillator here next to this and then the Rigol chip all the way over here. Can only presume that goes into here and that goes off to the main Rigol ASIC.

**Dave Jones:** And check it out. It's almost as if like it's a bit of tape or something. You can see the laser markings on the chip underneath there. I'm going to try and scrape this off.

**Dave Jones:** It's only a tiny little tiny little thing. So, it looks like it's on top. It's really It's rather No, that's It's sort of almost like it's you know, it's sort of baked on there or something weird.

**Dave Jones:** I've I've never seen anything like that before. Seems to be some sort of new method to sort of cover up the identity of what that chip is. Go figure.

**Dave Jones:** And they've got SOT223 3117 low dropout voltage regulators. It's quite a few of them scattered around this board. And as you can see, they've got a tiny little heat sink attached to them.

**Dave Jones:** Really nice little layout, nice via stitching. And if we have a look at the main Rigol device here, whatever it is, we can uh see all of the differential pair serpentine traces leading up to this main BGA device up here with the heatsink on it and you can see how they're not only adding the serpentine parts into each pair to match say this pair here with the one next to it and match

**Dave Jones:** the length of the pair but they're also adding the little single-sided wiggle in there to tweak and match um the individual pair it's each line in the individual pair.

**Dave Jones:** So that trace there with the wiggle in it is designed so that it exactly matches the length of its companion differential trace next to it. Classic you know high-speed signal integrity layout.

**Dave Jones:** They've done it perfectly and of course this board would be multi-layer probably six or something like that. They might have even got away with a four-layer on here and that would be controlled impedance.

**Dave Jones:** And we've found ourselves the main sampling SDRAM. It is 512 megabit Hynix H5PS5162GFA DDR2 SRAM and that's cut my SDRAM and that's coupled into this main heatsink device here and there's a companion one over there as well and they've also got another one here tied into just the one by the way not two tied into the secondary device over here.

**Dave Jones:** Now I think we can figure out what this right gold chip here is by deduction. Let's lift off the front end here and we'll find that there's probably no ADCs under here so Aha.

**Dave Jones:** And to To this can off we're just going to have to bend up some little tabs we've got here and that should allow us to ta-da pop the lid on it.

**Dave Jones:** There you go. Now, we'll take a look at the front end later because it looks very similar to the DS1052E, but as you can see, there's no ADC in there.

**Dave Jones:** This is just a differential driver. So, where are the ADCs, you ask? The data has to come out of the front end here and it's got to go via differential pair, which will be on the inner layers in there.

**Dave Jones:** That's why you can't see any traces going from the input RF front end can over to here or anywhere else because there's no surrounding These aren't the ADCs here, right?

**Dave Jones:** Not sure what they are, but they're clearly not the ADCs. So, clearly, this custom device is the ADC. Now, whether or not it's an off-the-shelf one and they've just re-badged it Rigol at the You can do that with the manufacturer.

**Dave Jones:** You can get them to You know, if you order enough, say, "I don't want your part number on it. I want my part number on it." But, that has got to be, for all money, at least the analog both analog-to-digital converters, multiple analog-to-digital converters, or something like that, controlled via this this oscillator here will be like the master clock for it and all that sort of stuff.

**Dave Jones:** And here are the outputs. All these differential pairs going from presumably a ADC up to the main uh FP Presumably, this is an FPGA under here, which contains all the sampling, you know, logic and all that sort of stuff.

**Dave Jones:** And it's got the two sample memory buffers next to it. Bingo, that's it. And then, you've got the output from this flowing down over here into another FPGA or PLD which we'll have a look at uh with some more memory next to it um and then eventually flows over into the main um processor DSP processor over here.

**Dave Jones:** So, that's clearly what is happening there. And then if you're curious to know what this bunch of circuitry is here next to it, that's like a probably another FPGA under there.

**Dave Jones:** We've got some memory next to it, another DDR2 SDRAM, but that's clearly the display processor. Look, it's just got a couple of lines going uh maybe just a serial bus or something going from one side, you know, going from the main acquisition ASIC uh well, ASIC FPGA probably over to this display processor here because it's going it's a dead giveaway, of course, it's going down to the LCD display flat

**Dave Jones:** flex cable. So, clearly that is the role of this device here. And then they've got some traces coming out of it by the looks of it, once again, coupled into here.

**Dave Jones:** This FPGA sort of glues the uh the data coming from the acquisition engine sort of into the display processor and also takes commands from the DSP, which of course the DSP's not going to be doing a huge amount.

**Dave Jones:** It's just going to be doing like the user interface stuff and uh things like that. It's not, you know, busily um you know, updating the display. That's all offloaded to that display processor there.

**Dave Jones:** And if you remember the sampling memory here, 512 megabit each, divide that by eight, that's 64 megabytes and there's two of them. This is a two-channel scope, so that they'd probably be dedicating one of those per channel, of course.

**Dave Jones:** So, these this thing um well, in theory, has 64 megabytes of, uh, sample memory per channel. And on the display device here, we have two Cypress, uh, SRAMs, a CY73 1380C.

**Dave Jones:** And that's an Each one of those is an 18 megabit pipelined SRAM. So, that's how they're going to get really super fast display updating on this thing. And for what I probably call like the, uh, glue FPGA here, they haven't gone for one of the big two, uh, Xilinx or Altera.

**Dave Jones:** They've gone for an Actel ProASIC 3. And it's got its own local oscillator there as well. And we've got some Spansion, uh, flash memory here. And also the JTAG header down here.

**Dave Jones:** So, this thing, uh, pretty much a hacker's delight, really. And then linking these two, we've got, uh, some LVDS, uh, bus drivers there. And then we've got an ISI, uh, That's a, uh, IS42S16160D, which is, uh, clearly the main memory for, ta-da, the Analog Devices Blackfin processor.

**Dave Jones:** And that's an ADSP-BF526. I'm not sure if it's that's the same one used in the Rigol DS1052E. I forget. But, uh, there you go. That's the main processor. This is probably a flat flex cable going over to the, uh, keyboard, or the keypad, front panel keypad.

**Dave Jones:** And there's, uh, presumably the USB, uh, host interface. Haven't looked that one up, but that looks like a Cypress USB host. And we've got our Ethernet interface as well, all tied into the Blackfin processor there with its own dedicated, um, SDRAM memory.

**Dave Jones:** And then we've got the, uh, the flash as well. That's all the program flash. And then, of course, we go over into this glue FPGA or whatever it is and back again into our display processor.

**Dave Jones:** And there's that tantalizing SPI boot header. And then, this mysterious one over here, ground, VCC, reset, and BKGD. And this circuitry here is coupled around the front panel USB connector here.

**Dave Jones:** So, they've got their own local regulator here. And these devices, these two chips here would be associated with power, you know, providing power, current limited 500 milliamp power to the front panel USB port.

**Dave Jones:** And here's the date code, DS2000 main board version 1.00, 19th of March 2012. And you'll note that the real-time clock crystal there, a little bit bodgily soldered down, but at least it is soldered down held in place.

**Dave Jones:** Bit of solder residue, flux residue left on there, but yeah, not a big deal. So, although I can see the thermal grease under there, I am actually going to try and take this sucker off and see if we can get access to see what that device is under there.

**Dave Jones:** My guess is an FPGA of some sort. Should be able to clear that off and see what we've got under there. This is the display processor. And surprise, surprise, it's a Xilinx Spartan 6.

**Dave Jones:** Pretty new technology there, XC6SLX25. And that contrasts with the Actel FPGA we found elsewhere. So, what's the bet that this one up under here is also a Spartan 6.

**Dave Jones:** So, unless they had drastically different system requirements for these two devices, then they probably would have made sense to consolidate and you know into the one part and choose a Spartan-6 under here as well, but it could be something else.

**Dave Jones:** We'll see. There you go. I was bang on. Spartan-6 as well, XC6SLX25. So, hey, they got those at a discount. And it's most likely that both of these will be sharing that same JTAG interface up there because I can't see another JTAG interface for this one over here.

**Dave Jones:** So, all up there we've got three JTAG interfaces. One up here for these two Spartan-6 FPGAs, one over here for the Actel FP the smaller Actel FPGA, and one over here for the Analog Devices Blackfin DSP processor.

**Dave Jones:** And here's the front end analog input. And it is quite reminiscent of the DS1052E. Although there seems to be a bit less in here I think, or maybe it's just spread out a bit more.

**Dave Jones:** Now, both channel one and channel two look to be absolutely identical. So, we're only looking at channel two here. As you can see, we've got a couple of couple of relays in here.

**Dave Jones:** We've got a couple of trimmer caps in here for this switchable attenuator part of it for the higher-end voltages. We've probably got our this I haven't looked at the part number yet, but that probably will be a programmable gain amplifier driving the ADC.

**Dave Jones:** That'll be a differential output programmable gain amp. There'll be a JFET and a couple of transistors in there to drive that thing. High-speed op amp over here and that's it's I think it's operation is going to be pretty very similar to the DS1052E.

**Dave Jones:** Of course, these scopes have a upper bandwidth limit of 200 MHz as opposed to 100 MHz in the DS1052E. So, it's basically just that more of the same. They've just upped it to 200 MHz.

**Dave Jones:** They've chosen specific parts and you know, tweaked it to be able to do that. And I'm having a hard time reading that presumably programmable gain amp chip there and the one next to it.

**Dave Jones:** So, I'm going to have to get out the digital magnifier. And woohoo, what do you know? It's I'm not sure if that's easy to read there, but that is Rigol.

**Dave Jones:** They've got a custom Rigol branded chip there. But once again, it you know, it may not be a custom device. I probably doubt it. They're probably just maybe to prevent reverse engineering or something like that.

**Dave Jones:** They've just asked some manufacturer to relabel it and rebrand it as Rigol for them. But you know, I don't know. It could be custom, but I doubt it. And if we have a look through our mantis scope here, there's the corporate Rigol VM 13A B.

**Dave Jones:** Whatever on earth that is. But yeah, my guess is it's a programmable gain amp differential output. And I'm not sure if you're going to be able to see that, but the other device inside this uh front end has got like that magic tape on it or something that we saw on the other chip on the main board earlier.

**Dave Jones:** So, they're they're clearly trying to you know, stop reverse engineering or hacking of this thing by masking a couple of the chips in there. Bastards. So, is it hackable like the DS1052E to get the increased bandwidth?

**Dave Jones:** I don't know. Your guess is as good as mine. Is there a varactor in there like the other one and they just switch it in digitally controlled under the software to limit that bandwidth in the amplifier?

**Dave Jones:** Perhaps it could very well be in there, but I'll leave that up to somebody else can hack. They've probably fixed the software thing, so I'd be very surprised if you could just do it easily through software as easy as it was last time anyway cuz they're showing that they've fixed those things with the firmware upgrades.

**Dave Jones:** So, you know, but it's the easiest way to bandwidth limit these things is in the analog front end. They wouldn't be doing in software. I think they're still got to be a line coming in here with some sort of hardware filtering of that analog bandwidth.

**Dave Jones:** Now, this section here is interesting right next to the channel one input here and there's four devices here. There's a regular presumably a local regulator power and then there's some other little sock 23 device down here and another device up here.

**Dave Jones:** And if we zoom in on it, then I'm not quite sure what that device is. It's got 21 AD 38 78 on it. There's a couple of voltage points next to it.

**Dave Jones:** One is uh 5 V. I presume that's not 0.5 V. I think that's a little plus 5 V and a plus 6.3 V over here. Geez, what is it?

**Dave Jones:** A valve heater or something like that for an old valve? 6.3 V wasn't it for the heater for the old valves? I could be wrong. I'm sure I'll be corrected by one of the old graybeards, but there are four of these like that.

**Dave Jones:** Identical layout. There we go. Local low dropout reg 1117 again. And then we've got another TI device a HA595. And there it is. Channel one sec, channel one third, channel two third, channel two sec.

**Dave Jones:** And that's pretty much all she wrote on the main board there. I mean, you know, there's a a couple of uh stuff here for the uh back light inverter and other uh um couple of uh core voltage uh switching voltage regulators around there for core voltages for various uh FPGAs and things, but yeah, that's about it.

**Dave Jones:** I'd say we uh let's try and take this board out, flip it out, and uh see what's on the you know, the underside. There's going to be some bypass caps on there clearly cuz there's no bypass caps anywhere around any of these devices at all.

**Dave Jones:** And of course, these uh uh FPGAs uh here fairly dense um Spartan-6s, they need bypassing on the bottom and everything else. So, there'll be a bunch of passives on the bottom, and that's probably it, but there'll be another board on there for the front panel as well.

**Dave Jones:** So, here we go. It's not easy to get this board out. You've got to take out the metal frame first, take all the knobs off the front, of course, and these are all uh uh metal uh threaded inserts on here.

**Dave Jones:** Beautiful molded, there's the buttons, no problems whatsoever, and we'll have to take, no doubt, the BNC off here, but here's the front. Here we go. This is rather interesting, and check this out.

**Dave Jones:** Look what it says. Secretary Bird SMKey O2. Secretary Bird, I What is that the code name for this thing? Curiously, I think it has something to do with that symbol there, which is probably the secretary secretary.

**Dave Jones:** Australians will get that joke. Uh Secretary Bird, perhaps. Is it the name of an actual bird? Or is it I don't know. And what do you know, there is such a thing as the Secretary Bird.

**Dave Jones:** It's from Africa. Go figure. There's not a huge amount on this board, just the rotary encoders. These are all pushable, of course, and we have the nice spring-loaded zoom knob here.

**Dave Jones:** Rather like that. It's really sexy. And there you go. There's not a huge amount doing on the back here. The two channels have actually removed the bottom ground plane out of that for signal integrity performance reasons.

**Dave Jones:** But apart from that, yeah, we've just got some basic passives, and there's some resistor terminators on there. There's the bottom of the BGA down in there. If you you know, if you want to zoom in on that, you can see the classic bypass capacitor layout for an FPGA.

**Dave Jones:** Sort of, you know, done that dozens and dozens of times. That star arrangement like that. That's just the way they generally fit in in terms of the power pins under the BGA.

**Dave Jones:** There's some resistor terminators. Nothing terribly exciting. The main processor, I think that's the main No, that's the That's the other FPGA up the top there. They're the two memories.

**Dave Jones:** Yeah, and DDR termination resistors. And that is about all she wrote on this board. There's a soft power button down there. Of course, this thing is operational all the time.

**Dave Jones:** It gives that heartbeat type LED on the front power button. And you can see some residue on there as well. All these hand-soldered connectors certainly have a bunch of uh residue left.

**Dave Jones:** They haven't used a no-clean flux on there, but uh not a huge deal, really. What's that device in there? And it's another TI chip. Not sure what that one is or what it's doing, but there you go.

**Dave Jones:** There's the bottom of the uh uh that custom Rigol chip on the front end there, and it's identical between channel 1 and channel 2. And here's the back of the keypad board.

**Dave Jones:** My guess would have been a little micro or something like that, but it's a Lattice Mark IO POD. And what they've done is completely gunked up this flat flex cable.

**Dave Jones:** I don't know if there's a connector under there or not or whether or not it's maybe soldered directly on or something like that, but uh that runs under the LCD over to the other board over here, which uh then goes off to the main board down the bottom there.

**Dave Jones:** And the other thing to note, too, is there's a cutout in the metal panel here, and there's also a molding in the front panel for some sort of small connector interface.

**Dave Jones:** I don't know. A uh potential digital section? I don't know. Your guess is as good as mine. Check out this soldered tab going over the top from the keyboard board here to the main chassis.

**Dave Jones:** They've decided that they've got to ground that for some EMI, you know, reason. And it's time to reassemble this thing. It was a pain in the butt getting the uh buttons through the front panel, by the way.

**Dave Jones:** If anyone's looking at taking these apart, getting it back together is not necessarily easy. Beauty. So, there you have it. This is the new Rigol DS2000 series. This is the DS2200, but they're all the same.

**Dave Jones:** Uh wrong knob. Oops. Interestingly, the uh uh silk screen on that front panel is all the way under the knob there. There you go. Go figure. And uh that is a beautifully engineered scope.

**Dave Jones:** I really like it. I mean, this is an 800 $700 class scope, of course, for the entry-level uh one. I mean, the analog bandwidth, you're just paying for, you know, software options uh basically.

**Dave Jones:** Oops. Uh wrong knob. D'oh. There we go. There's our scale knob, which should be bigger. Bit disappointed that the horizontal is the same. Uh that's a trend with all scopes these days.

**Dave Jones:** I long for the day when they have a nice big horizontal. You know, you think this would be the horizontal. It's not. It's the zoom. Oh, man. Very Tektronix-like.

**Dave Jones:** There, but there you go. That is the new Rigol DS2000 series scope. And that is an absolute winner. It really is. That is beautifully engineered for, you know, the sub $1000 price category.

**Dave Jones:** I think it's awesome. I really couldn't fault the engineering in this thing at all, and I think it'll be a pretty darn reliable scope and probably pretty hackable as well, I would suspect.

**Dave Jones:** And I'm sure there'll be no shortage of people working on that just for fun, you know? Play a game of pong on it. Go figure. Anyway, if you want to discuss it, jump on over to the EEVblog forum.

**Dave Jones:** And if you like teardown Tuesday, please give it a big thumbs up. Catch you next time.
