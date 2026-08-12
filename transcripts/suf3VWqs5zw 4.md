---
video_id: suf3VWqs5zw
title: EEVblog 1413 - Oscilloscope Current Probe TEARDOWN + DEMO
url: https://www.youtube.com/watch?v=suf3VWqs5zw
source: youtube-asr
timestamps: {"0": 0, "1": 8, "2": 21, "3": 35, "4": 48, "5": 69, "6": 82, "7": 100, "8": 111, "9": 125, "10": 136, "11": 156, "12": 171, "13": 181, "14": 194, "15": 207, "16": 220, "17": 227, "18": 239, "19": 251, "20": 267, "21": 287, "22": 303, "23": 321, "24": 330, "25": 338, "26": 349, "27": 366, "28": 380, "29": 395, "30": 402, "31": 414, "32": 426, "33": 435, "34": 448, "35": 459, "36": 469, "37": 487, "38": 503, "39": 516, "40": 533, "41": 545, "42": 562, "43": 573, "44": 586, "45": 609, "46": 617, "47": 628, "48": 643, "49": 657, "50": 668, "51": 677, "52": 688, "53": 698, "54": 709, "55": 723, "56": 734, "57": 752, "58": 768, "59": 779, "60": 797, "61": 808, "62": 817, "63": 828, "64": 845, "65": 853, "66": 866, "67": 879, "68": 890, "69": 908, "70": 918, "71": 933, "72": 945, "73": 963, "74": 979, "75": 1006, "76": 1017, "77": 1036, "78": 1054, "79": 1064, "80": 1085, "81": 1112, "82": 1131, "83": 1139, "84": 1153, "85": 1181, "86": 1194, "87": 1205, "88": 1216, "89": 1228, "90": 1240, "91": 1258, "92": 1286, "93": 1311, "94": 1322, "95": 1344, "96": 1356, "97": 1371, "98": 1383, "99": 1404, "100": 1416, "101": 1425, "102": 1437, "103": 1452, "104": 1467, "105": 1481, "106": 1494, "107": 1504, "108": 1516, "109": 1530, "110": 1541, "111": 1554, "112": 1572, "113": 1579, "114": 1588, "115": 1603, "116": 1614, "117": 1628, "118": 1637, "119": 1648, "120": 1658, "121": 1665, "122": 1686, "123": 1698, "124": 1711, "125": 1722, "126": 1736, "127": 1750, "128": 1769, "129": 1781, "130": 1795, "131": 1817, "132": 1830, "133": 1843, "134": 1855, "135": 1870, "136": 1886, "137": 1893, "138": 1904, "139": 1912, "140": 1928, "141": 1939, "142": 1952, "143": 1969, "144": 1977, "145": 1986, "146": 1993, "147": 2007, "148": 2020, "149": 2032, "150": 2042, "151": 2056, "152": 2069, "153": 2082, "154": 2094, "155": 2107, "156": 2119, "157": 2128, "158": 2140, "159": 2155, "160": 2167, "161": 2181, "162": 2193, "163": 2203, "164": 2215, "165": 2229, "166": 2243, "167": 2250, "168": 2262, "169": 2270, "170": 2284, "171": 2291, "172": 2299}
---

**Dave Jones:** Hi, we're going to take a look at a very interesting bit of kit today and one that's very, very valuable for your lab. If you haven't got one, a lot of labs don't have one of these.

**Dave Jones:** Now, you've no doubt seen this in several fairly recent videos. It's a current probe, in particular the Mixig CP2100 and disclaimer, I actually sell this in the EEVblog store.

**Dave Jones:** It was so good, I bought the company for those who remember that slogan. Anyway, So impressed, I bought the company. Yeah, this is the CP2100B current probe that hooks into your oscilloscope.

**Dave Jones:** Here it is hooking into a portable oscilloscope, but of course, these things, the great thing about these is that you don't have to like break into your circuit with like a little current shunt or something like that.

**Dave Jones:** You can actually just put it over a wire and clamp like that. Obviously, you can't do that to a PCB trace. If you want that capability, I've actually done a video donkeys years ago on the positional or the AMTI I-Prober positional current probe, which is a different thing, but we might have a look and compare that to this one in this video.

**Dave Jones:** Anyway, the whole idea is you whack a wire through there and if it closes properly, there you go, pinky sized. Um, whack your wire through there and you can measure your current all completely isolated.

**Dave Jones:** So, what do we get in the kit? We get a warranty card. This is the 2100B model. This one is available in two different models. There's the A model, which has an 800 kHz bandwidth and the B model, which is the only model that I sell on the EEVblog store and that's got a 2.5 MHz bandwidth.

**Dave Jones:** I know this one says 2 MHz on the label here, but actually this is one of the original prototypes and they actually upped it to 2.5 MHz. So, all my stock actually has 2.5 MHz written on it.

**Dave Jones:** So, anyway, what we're going to do today is tear this puppy down. We're going to not only tear down the amplifier here, but we're also going to tear down the head as well, cuz I suspect there's some electronics in there.

**Dave Jones:** It It ain't just the Hall effect sensor in there. It's going to be a It's going to have like a head amplifier. Anyway, as you'll see, this is a very nice bit of kit.

**Dave Jones:** Tell us the price, son. Well, the 2100 A model that starts from about street price of around about 270 bucks and upwards. This is Yankee bucks, but I've got the 2100 B model for like if Check the links down below.

**Dave Jones:** You can actually get a coupon discount code that can get this puppy down to 360 Yankee bucks for the 2.5 higher bandwidth 2.5 MHz model. Anyway, it comes with a the USB A, cuz that's where it gets the power from.

**Dave Jones:** It doesn't do anything else. It just gets the power. Most of the scopes these days, like digital ones, have a USB port on the front, so no worries. And then the output into your 1 megaohm impedance scope.

**Dave Jones:** There it is. BNC straight in, and it's got two different current ranges, 10 amps and 100 amps. So, it's not designed for like really low current. There's not many probes on the market that can go down to like really low current.

**Dave Jones:** You got to have some like really old-school tech one or something like that from, you know, the 1970s or something like that. Anyway, 10 amp current range, very handy for most general purpose electronics uses, and 100 amps for your higher end stuff.

**Dave Jones:** I haven't personally gone over 10 amps on it myself, cuz I'm not into the high power stuff. Anyway, 2.5 MHz bandwidth, and it's got auto zero functionality and shift as well functionality.

**Dave Jones:** And it's actually pretty smart. It must have a micro in it, cuz it can do like auto zero and things like that. So, it's got to have some smarts.

**Dave Jones:** We'll find out when we take this bad boy apart. And here's the probe head itself. I assume it is slightly different internals for the 800 kHz model as opposed to the 2 and 1/2 MHz model we've got here.

**Dave Jones:** DC max 100 amps, but I don't I think if you went over that I like it's you're just going to saturate the sensor. It's just the operational range. I don't think it's actually going to blow up anything or 70 odd amps AC RMS.

**Dave Jones:** It's got a 600 V CAT II rating 300 V CAT III because like well, it's basically it's that's non-contact. Your probe just goes in there, but there's our magnetics down in there and of course this of course you'll find this goes right under here.

**Dave Jones:** This forms a complete core around there. So yeah, and like you can't just operate it open like that. It's actually got to be shut. So you get the magnetic fluxes going completely right around the core like that and there'll be a Hall effect current sensor in here somewhere or some form of current sensor in there that actually measures the fluxy.

**Dave Jones:** And that will measure the magnetic field induced in the magnetics around here. So cool. Let's There's no obvious Oh yeah, there's a couple of screws on there. Oh yeah, yeah, might come apart reasonably well, but anyway, it does feel like a nice high-quality bit of kit.

**Dave Jones:** Beautiful strain relief on the backside here. Just feels really good quality. There's the back of that for the those playing along at home and it does have a an output here so that you can actually you know, power stuff off here as well, but I don't believe it actually does anything else.

**Dave Jones:** It's just so that you can if you can you can use your USB port basically just a pass-through. And of course yes, it comes in this nice handy little carry case.

**Dave Jones:** Sweet because this isn't like an often used bit of test gear. This is the one you kind of keep on your shelf for when you need it, you need it.

**Dave Jones:** And we're in the screws were actually covered by the front decal. So yeah, you kind of have to dig those out, but, anyway, we take that off and metal threaded inserts.

**Dave Jones:** Thank you very much for playing and there we go. Is that any micro down in there? We will actually go through this in detail, but the first interesting thing to note is the Presumably, yeah, that looks like one of those isolated DC to DC converters there.

**Dave Jones:** So, even though they didn't really need to, I don't think, because well, the the probe itself is isolated. It's not making electrical contact anything, but just to be on the safe side, they used an isolated DC to DC converter there for the power.

**Dave Jones:** So, that's rather interesting. Let's go to the old Tektronix here and we can have a closer look here. And as I said, that is a 0505. That'll be plus minus 5 V.

**Dave Jones:** Numbers on these are pretty common. So, if we go over to the videotape over here, we can take a look at. Here it is. It's available on the Digikey's.

**Dave Jones:** 5 weeks lead time. Geez, that's pretty good these days. With the chip again. Anyway, yeah, there it is. We've got the 0505. So, we've got the plus minus 5 V job.

**Dave Jones:** It's an isolated little 1 W converter. I've used these countless times before. You get them in different sizes and yeah, there's a million and one different manufacturers. They've all got the same pin out.

**Dave Jones:** So, if you get one, they're you know, you can just get them from any manufacturer. That's a great thing about designing these in. Anyway, they've got a moren sign in there.

**Dave Jones:** So, let's have a look at the main processor and that is a BusyBee. It's an EFM8 and if we go to the videotape over here, it's a BusyBee family data sheet.

**Dave Jones:** Here it is. It's a multi-purpose line of 8-bit microcontrollers. It's an 8051 jobby. Of course, it is. Goes up to 50 MHz. Not that old school frequency stuff, but yeah, it's pretty good.

**Dave Jones:** It's got a 12-bit analog to digital converter. not too shabby. Although, of course, the building converters are, you know, not as good as usually not as good as dedicated ones, but for something like this, doesn't matter.

**Dave Jones:** Two latency analog comparators. So, actually, this is a fairly grunty little 8051 old-school micro. There you go, the busy bee. Medical equipment, lighting systems, high speed. Oh, it's got CR 16-bit CRC security as well.

**Dave Jones:** Really? That's That's not too shabby. Geez, the old-school 8051. Anyway, there you go. It's got that. That's just general housekeeping. So, obviously, someone at Mixig likes their 8051s. Old-school, but these are obviously regulators.

**Dave Jones:** You can tell by the pin outs and the big caps input and output. They're just regulators regulating the output of this to give us a nice clean output cuz these are switching isolated converters.

**Dave Jones:** They are pretty noisy. So, you do want to quieten those up a bit. And what is that? Is that some sort of another regulator? Maybe? It looks like cuz the configuration, maybe it looks like a maybe a lower noise regulator.

**Dave Jones:** Perhaps going into the can over here. So, we haven't got the can off. We'll have to desolder that if you want to get that bad boy off. But, yeah, look, there's not much else in here, really.

**Dave Jones:** What's going on there? Some op amp business. Not much. Got some discrete transistors. TI op amp over here. Yeah, like there's nothing much doing. That That's a buzzer. LS loudspeaker.

**Dave Jones:** Loudspeaker. There you go. Yeah, cuz this thing does beep when it finishes its auto zero and stuff like that. But, yeah, basically, that's it. I don't expect much to be on the bottom.

**Dave Jones:** Unfortunately, it doesn't look like it comes out easily, but I'll do my best. Ha! Even the cable clamps have metal threaded inserts. Spared no expense. Brilliant. All right, we're out.

**Dave Jones:** And of course, what we expect in here because the head is going to have an headphone at headphone a head amplifier on it. Obviously, you want to amplify the low-level stuff right at the head and then it's going to have a cable drive which drives this and it's going to have just have a level converter and it'll do some shifting as well cuz it's got that functionality that shifting

**Dave Jones:** functionality as well. So, that's going to add a DC offset to you shift the output and that will go into there like that. So, maybe that's what that's driving over there.

**Dave Jones:** Perhaps, I don't know. Anyway, let's take that off. There we go. And yep. As I I didn't expect to see any circuitry on the bottom actually at all, but we do.

**Dave Jones:** But yeah, that's all just filtering stuff for the all the converters. And once again, there we got a couple of other transistors as well. Like a six-pin jobby. Two six-pin jobbies.

**Dave Jones:** They're labeled Q. So, what are they? Dual transistor or something? That's interesting. Anyway, yeah, we've got some LEDs there cuz they're the backlight for the the buttons do actually light up and everything.

**Dave Jones:** So, oh, there we go. We can get that off. There we go. Tada! And oh, is that going to Yeah, yeah, it's going to pull through. There you go.

**Dave Jones:** Got a couple of little parts on the bottom there. Oh, sorry if you couldn't see that. Got a couple of little caps on the bottom. Well, we're already double-sided loading and you had to double-side load for the LEDs anyway.

**Dave Jones:** See, that's the thing. Once you decide that well, well, once you're all what once you're forced to like double-side load because you want the buttons are on the bottom, of course, the board has to be flipped over so the buttons are on the other side.

**Dave Jones:** The button pads are here and you want to backlight the uh then well, you've got to have your LEDs. Well, no, you could actually mount your LEDs on the top side and then then have bottom emitters through a hole.

**Dave Jones:** That's a um the thing, you know, I've done that on projects. Um and that's really handy. So, you can avoid double-sided load that way, but in this case they went, "Nah, she'll be right.

**Dave Jones:** Just do double-sided load." Once you decided to do double-sided load, you pay the penalty even if you have one lousy capacitor, one lousy LED, or whatever, you usually pay that penalty um in terms of manufacturing uh cost and extra handling and whatnot.

**Dave Jones:** So, you might as well put your extra parts on the bottom as well. So, yeah. No worries. So, let's let's take this off. Ta-da! Hey, there we go. There we go.

**Dave Jones:** Let's peel that back. And solder directly on, but of course it's coax, so no no worries. That's what you'd expect. So, there we go. Once again, is that the same op-amp that we had over here?

**Dave Jones:** Yeah, I think they're re-reusing that, whatever that one is. So, here's our input over here, sig in and sig out. So, this looks like there is this driving the No No No, hang on.

**Dave Jones:** No, this just does the shifting cuz here's our Here's our output from our head, and that goes basically straight through. There you go. It goes straight through. So, they're just doing the level shifting.

**Dave Jones:** Yep, that's all they're doing. Okay. So, the actual um coax driver is in the head itself. So, when we tear down that, we'll be able to see that. But, they've got a various So, you got plus minus 5 volts going over to the head as well, V offset, V H V high or something.

**Dave Jones:** I don't know. DW1, DW2, DW I know. Um can't think of anything at the moment. Sure if I sat down and thought about it, it'd be obvious, but anyway, there you go.

**Dave Jones:** It's It's basically just doing some DC offset plus some measurement as well, cuz they do the zero offset, the automatic zero offset, so they need to be able to measure that.

**Dave Jones:** They'll be using the ADC built into the micro, and and Bob's your uncle. So, there you go. That's rather nice. Revision 2019. Geez, it's pretty It's been around for a while.

**Dave Jones:** I thought it was newer than that, but anyway, 2100 AB. So, this is for the A and the B version. So, yeah, I I believe this wouldn't change. The only difference for the lower frequency A version would be the magnetics in the hall of and the actual sensor in the head itself.

**Dave Jones:** So, anyway, yep, let's go over to the head. Oh, by the way, yeah, there's the uh there's the US Does the USB do anything? No, no, it doesn't even send data.

**Dave Jones:** I don't think it Yeah, I don't think that's going to pass data through. That ain't going to pass. That ain't going to pass your data, is I'm afraid. I think it's just going to pass your power.

**Dave Jones:** So, here is your head. I have actually removed the screws, and it's just got some adjustments on the bottom and the shield, so these shields just pop off like this.

**Dave Jones:** And, tada, we're in. We've got a fair income relay. That'll be our range switch, cuz you can't can actually hear the relay switch. It goes ka-thump when you switch between the 10-amp and the 100-amp range.

**Dave Jones:** So, there you go. They've got good old fair no electronic switching rubbish, obviously. Um too many parasitics or whatnot, so they're uh doing that with old school relay, AD8421.

**Dave Jones:** And if we go to the videotape, that one's not too shabby. Check that out, 3 nV per root hertz, uh low power instrumentation amp. There you go. It's exactly what you'd expect in there.

**Dave Jones:** That's 200 femtoamps current noise, 10 meg bandwidth, 2 meg bandwidth again of 100. Uh yep, so but that's exactly what you'd expect inside the head of something like this.

**Dave Jones:** So, that's about all she wrote, isn't it? There's uh more more footprints for variable caps. That's what VC stands for there. So, that's interesting. Why they haven't put the variable caps in?

**Dave Jones:** That was maybe only during development and they went nah. She'll be right. No wackers. Don't need them. And uh up here there our Hall effect sensor. Can see them right down in there.

**Dave Jones:** There they are. Anyway, that's our magnetics for you magnetic fanboys. There you go. You can count the number of laminations there. So, it's 88 something. Why the top's taken out of that?

**Dave Jones:** I don't know. 8877. Is the other one the same? They mounted backwards. Definitely says 8877 on there. I think the other one's in the other orientation. So, the idea, of course, is that when you close the jaws, there is the exactly the same magnetics, these same laminations here forming a complete loop like that.

**Dave Jones:** And of course, the loop's only broken there, but of course, all the magnetic flux has to flow through these make two magnetic sensors here. So, yep, that's the whole idea.

**Dave Jones:** So, presumably, they would use a different part in there for the 800 kHz version. I'll try and dig up some data on that. Well, I can't find any data on those sensors, but a reasonable guess might be these multi-dimension sensors in the future.

**Dave Jones:** Um I see a Willow Technologies company. God, how many variations of the one bloody company can they get anyway? There's a good chance it's this. Don't quote me on this, but anyway, TMR 2503 utilizes a unique push-pull Wheatstone bridge composed of four unshielded TMR sensor elements.

**Dave Jones:** The unique bridge design provides a high sensitivity differential output linearly proportional to magnetic field applied perpendicular to surface of the sensor package and it provides superior compensation the output.

**Dave Jones:** Um, etc. Anyway, it looks to be this package. So, uh, there's there any code information 88 sensitive direction? No. Doesn't seem to be any packaging information at all. So, like in terms of like labeling information.

**Dave Jones:** So, 8877 I don't know. So, yeah, they don't give you that data. Unfortunately, but anyway, it's likely that it's this. Um, that'd be a guess. Anyway, they do have a sensitive direction like this, but if we go down in here, you can see that they're actually one is backwards or it's not labeled, but um, I don't know.

**Dave Jones:** 8877 definitely on there. The other we can't see any label whatsoever. So, they must have put one backwards for a reason. Maybe to I don't know, cancel out do cancellation or something, noise or something, you know, I I don't know.

**Dave Jones:** They're not They're not paralleling those up. They're actually Oh, are they? Hang on. No, cuz we've only got the one op amp. Right? We've only got the one instrumentation amp.

**Dave Jones:** So, I might leave that to those playing along at home. Follow the money on that and see if you can figure out if they're and both joined somewhere cuz we've only got the one instrumentation amp.

**Dave Jones:** So, I reckon that they're just Yeah, they're putting in those for doesn't It's not going to increase the bandwidth, is it? I I don't know what they're doing there, but anyway, the interesting thing about this data sheet is that they don't actually give you the bandwidth information, sensitivity, supply current, saturation field, nonlinearity, offset voltage, hysteresis, temperature coefficient of resistance, temperature coefficient of sensitivity and offset, blah blah blah

**Dave Jones:** blah blah. But, they're not going to give you the bandwidth of this bad boy. So, there you go. Um I don't know. Like, is there a different part for the different bandwidths on here, or do they bin them?

**Dave Jones:** Maybe They and you know, put the lower ones in the 800 kHz model, and these in the and the better ones in the 2 and 1/2 meg model? I don't know.

**Dave Jones:** If you've got any info or thoughts on that, please leave it in the comments down below, but there you go. Um we can probably check the gain of this thing.

**Dave Jones:** Let's have a look. See what gain that's got. So, if we have a look at the resistor here, and what pins are we looking at? Anyway, there's one resistor that sets the gain.

**Dave Jones:** And it'll usually be two and three. Yes, it is. Resistor Yep, two and three there. And the input's over there. So, oh, okay. Right. Yeah, that's what those two resistor trim pots do.

**Dave Jones:** They set the gain. Okay, so they trim in the gain. Why you wouldn't put I does each one have to be Maybe each May Maybe there's such variability in the output of these sensors that they have to tweak Yeah, they have to tweak the gain on each one.

**Dave Jones:** What is Like, it doesn't give you a nominal accuracy here, does it, on on data sheet? It doesn't Yeah, I I it looks like and maybe the physical orientation of each little uh one in that like the how it's soldered in and how it's, you know, cuz the angle can slightly change um how you solder the thing in there, that could affect it by I don't know, a

**Dave Jones:** double-digit percentages or something perhaps. It could it it could affect the gain or whatever. So, yeah, I mean, that's not going to be perfect even if you tried to put the uh you know, the drilled the holes exact, you know, the just tight as a nun's nasty going in there, and you're still going to get some offset variation and balance variation as well, wiggle wiggle wiggle um of of the packages and that that

**Dave Jones:** would matter, right? Anyway, they Oh, yeah, I looks like is there some silicon down there? It looks like they put some sort of potting. Yeah, there's potting around here, some sort of, you know, encapsulant or whatever.

**Dave Jones:** I'm surprised that they didn't fill up the whole thing though, I guess, but but yeah, that's what they have to do, I reckon. Each one has got to be trimmed by someone with a gray-bearded nude virgin with a uh tongue at the right angle, and each one's uh tweaked at the factory, and possibly they bend the sensors, and that's how they get the different bandwidths out of this.

**Dave Jones:** So, I don't know, maybe you could get a good 800 kHz jobby. Who knows? If anyone's uh measured one, please leave it in the comments down below. Anyway, um let's measure the resistance and see.

**Dave Jones:** This is where your auto hold comes in handy cuz I can't see that damn thing. So, there we go. What is that? 298 ohms. There you go. So, what does that work out to?

**Dave Jones:** 299 ohms, actually. Ooh, I love binning. Look at that. Beautiful. That's the op amp or instrumentation amp, sorry. Anyway, where's our gain uh formula? Can't remember offhand what it is.

**Dave Jones:** It's been too long. Aha, 9.9k over G minus one. I love this. Look. This is hilarious. Look, the gain can be calculated by referring to error reference source not found.

**Dave Jones:** Someone at AD screwed up. Or using the following gain equation. There you go. Standard ones 200 amps, so we're talking I don't know. It's in the order of somewhere between 20 and 50 there.

**Dave Jones:** So, it's like 30 or something. There you go. That's a gain of 34. So, let's just have a practical example like this where it's very useful. Measuring mains power consumption.

**Dave Jones:** Now, I'm going to use the 10 amp range here. Now, this is one issue I have with it and they really should change the decal for this. If you use the 10 amp range, it's 0.1 volts per amp.

**Dave Jones:** But, what they don't tell you, they do tell you this in the manual, which is not provided in the case by the way. You got to download it. But, they do tell you that you should use the times 10 setting on your oscilloscope for the 10 amp range and for the 100 amp range, you are to use the times 100 setting on your scope.

**Dave Jones:** So, or if it doesn't have that, you have to multiply yourself. So, yeah, that's kind of not obvious at first use. But, anyway, we've got this hooked up to the scope and we're powering from the USB output here.

**Dave Jones:** No wackers. We've got our 10 amp range selected and our probe here, you notice it does actually have a direction marker on it. And of course, for DC, if there's any DC component in your signal, then you of course have to have it in the right direction.

**Dave Jones:** Otherwise, all your outputs are going to be a negative. So, anyway, what I'm going to do is I'm going to measure this thing right up its own clacker. So, I'm going to measure Here's the mains input cord for this oscilloscope.

**Dave Jones:** We're going to measure the power consumption of this oscilloscope using the oscilloscope itself. And this is one of the beautiful things about this. So, I've peeled back the sheath here.

**Dave Jones:** There's the active wire, the brown one, different in other weirdo countries. So, we'll whack this on. I'll put it in the right direction. It's going into the instrument. Not that there should be any DC offset on here because we've got AC.

**Dave Jones:** Get in there, you sucker. There you go. Tada! We're now measuring the waveform of this oscilloscope. Brilliant. And I'm also measuring this through my Volteq power analyzer as well, so we can just confirm the results.

**Dave Jones:** But, let's have a look at the scope here, and you can see the waveform. We can actually tidy this up a bit. So, we'll go into acquire, and cuz it's a little bit, you can see a bit of noise on there, right?

**Dave Jones:** And that's the thing. If I take it off, right? There we go. That's just the noise floor of the scope. Whack that on. But, we can clean that up by going into acquire and acquisition mode, and we'll just select averaging down there.

**Dave Jones:** So, that'll give us more resolution on there. And you can see the peaks in the waveform here. Look at them. Because this is a switch-mode power supply inside here, it's got And it doesn't have any power factor correction circuitry, you get these huge current spikes.

**Dave Jones:** Now, of course, one of the first things you have to do before you even get your measurement is to set up your probe properly. So, I've got it set.

**Dave Jones:** It's amps mode. And not not all scopes will have this, but pretty much any modern one should. It'll have amps mode. So, it'll give us a readout directly in milliamps per division.

**Dave Jones:** So, 200 milliamps per division, and then we can set the probe ratio there, and I've got the probe set to 10 to 1, which curiously on the Keysight scope, it only gives you the ability to do the probe there when you're like the attenuation setting when you're in volts mode.

**Dave Jones:** So, you got to set that first. Little bit weird. Anyway, we are set up. We are good to go. 200 milliamps per division. So, you can see 200, 400, almost 600 milliamps plus minus peaks there.

**Dave Jones:** And like, yeah, that's not great, is it? And of course, the AC the you can see the AC waveform in there, and that's just the normal current that's whoop whoop happening.

**Dave Jones:** Well, it's been a little bit in trigger there. And that's the normal current that's happening, but it's because it's a switch mode with no power factor correction taking these big spikes.

**Dave Jones:** And this allows you to see this via product under development. And this is brilliant because it allows you to see what sort of peak current you're getting and any noise issues and stuff like that.

**Dave Jones:** We might have a look at the noise in a second. We might be able to see it. So, 50 hertz the mains, not that 60 hertz yankee rubbish, and peak to peak current is around about an amp.

**Dave Jones:** Look at that. Um that's actually quite a lot. And I I've got the AC RMS here. This is the standard deviation. I've done a video on that, by the way.

**Dave Jones:** Might have to link that in, which takes out any DC component in there. And we've got basically 174 175 milliamps AC RMS. And the DC RMS, which includes any DC component, it's it's a little bit higher because maybe well, I haven't done an auto zero on this to actually subtract out any component.

**Dave Jones:** So, let's actually do that. So, we'll just disconnect that. We'll hold that down. It's going through auto zero. The LED's on. And beep beep beep, it's done its auto zero business.

**Dave Jones:** Let's plug this probe back in and see if that's any different. Yep, there you go. We've taken out the little DC component offset that we actually had in there.

**Dave Jones:** Now, it's bang on. There's no additional DC component in the mains AC signal. But of course, we can actually change that DC offset there. We can shift that. Like, way.

**Dave Jones:** Whoop, it's gone cuz it's not triggering anymore. It's gone out of our trigger window. So, there you go. We can just shift that like that. So, that's beautiful. You can see the DC component change there.

**Dave Jones:** But, yeah, we can just manually adjust that or do it automagically. Now, if we actually zoom in all the way in here, you'll notice there's a bit of a wiggle, wiggle, wiggle yeah in that waveform.

**Dave Jones:** That will be the switch mode frequency conducted back out of the oscilloscope via the mains cord cuz it it doesn't it might have some input. I'm sure it has some sort of input main mains filtering with a common mode choke and stuff, but it's sneaking out.

**Dave Jones:** And we can get in there and measure that. So, I don't know, set it to a rough peak there and then we'll Well, X2. Another rough peak there. Good enough for Australia.

**Dave Jones:** We're talking Uh what do we got? Six Oh, 66.66666. Thank you very much, kilohertz. Fantastic. So, that would be the switching frequency of our uh converter in there, which is sneaking its way back out on the mains cable here.

**Dave Jones:** And this thing is able to measure it. Neat, huh? So, one of the benefits of being able to see a waveform like this in mains equipment is uh well, not only to uh see what sort of switching frequencies or noise coming out or anything conducted mode noise or anything like that, but uh it can also show you what uh like peak currents.

**Dave Jones:** And this will have an effect on uh say the design of the fusing for your product uh for example. And of course, because this is apparent power versus real power, it's going to the apparent power is going to be higher.

**Dave Jones:** These current spikes, these are real. So, they have to come from the mains. And then the entire mains distribution system right back to wherever your generator is. So, these uh spikes on here.

**Dave Jones:** I'm I'm getting into apparent power versus real power, and that's not the scope of this video, but anyway, it shows you that these huge like normally, if it was power factor corrected, you would just see this waveform in here.

**Dave Jones:** You wouldn't have these gigantic peaks. Yeah, if it was ideal power factor of one, you'd only see a small amount of current in there. But, we've got these huge current spikes in here, positive and negative, and this causes like losses I squared R losses in the cable.

**Dave Jones:** I've covered that in fundamentals videos. You can't escape those I squared R losses. They're going to come from the cable. They're going to flow through your fuse, so it affects the fusing design of the fusing of your product and other component ratings inside your product and your distribution system and all sorts of things.

**Dave Jones:** And And obviously, for a small product like this, it's only taking tens of watts, but when you're designing like huge industrial stuff, like it can be a real huge deal.

**Dave Jones:** But, you know, if you manufacture, you know, 100 million of these widgets, and you you know, people use them all around the world, that's a lot of extra power consumption.

**Dave Jones:** Anyway, so it's very cool to be able to see the mains current waveform like that. But, of course, it doesn't have to be mains current. This is just one example you can do in circuit.

**Dave Jones:** But, because you are you've got a clamp jaw like this, often on prototypes you might break into a PCB trace, have a big loop coming out as or whatever, or you might, you know, have some input power supply cable in or something like that to be able to clamp onto.

**Dave Jones:** So, yeah, with these clamp probes, often you may not have the wires available, and you may have to budget in to test the prototype or something like that. Anyway, let's go back to our measurements here and see if it matches over here.

**Dave Jones:** Let's see if the accuracy. So, our apparent power VA is V as what it says, voltage times current. So, our current is 170. Let's round it to 175 milliamps, yeah?

**Dave Jones:** So, 170, get the confuser out here. This will tell us our voltage over here, 241.5. Thank you very much. So, multiply by 245 uh 41. Duh. 241.5. Ta-da! 42.26.

**Dave Jones:** And what do we get here for VA? Was I measuring VA? 42.88. Well, it's fluctuating all the time. It's varying. And there's going to be a bit of error in there.

**Dave Jones:** But, jeez, that's that's not bad. I don't know I calculate the percentage error there. If we run the numbers again, it's always jumping around a little bit. There's going to be error in this.

**Dave Jones:** There's going to be error in the probe. There's going to be error in the uh oscilloscope and all sorts of stuff. But, there you go. It's pretty darn close.

**Dave Jones:** So, I'm happy with that. And if we hit um and well, our power factor. There we go. Our power factor It's not great, is it? .55 power factor. Because well, there's no power factor correction in the product.

**Dave Jones:** We're getting those large spikes. And the actual power which you're paying mostly depends on which country you're in. The power you're paying for is only 23.8 W there. So, that's what you're paying for in terms of power consumption.

**Dave Jones:** At least here in Australia, that's what you're paying for unless you're in an industrial setting. And then you'll be paying for the VA. Because that power has to be coming from somewhere.

**Dave Jones:** Somebody's got to pay for it. And you ultimately pay for it in the distribution system. But anyway, I've covered this in other videos. So, there you go. That's pretty cool, huh?

**Dave Jones:** And I've shown this with the TTI Aim I-Prober positional current probe. And when you're measuring at really low currents, I'm down to the minimum uh that my scope can go, 5 mA per division here, which is basically pretty much down in the noise.

**Dave Jones:** If I rotate that, you'll notice the DC offset will change. That, of course, is the Earth's magnetic field. Cool, huh? So, wait. Yeah, you've just got to be careful.

**Dave Jones:** And to, course, if you open the clamp probes, it's yeah, it's all going to come a guster. But yeah, just be aware of the pesky earth's magnetic field and orientation measuring very low DC currents.

**Dave Jones:** And noise-wise, there's the scope unconnected, and let's plug it in. I've got no signal here. And there you go. So, well, depends on what range you want to measure that over.

**Dave Jones:** But here you go. We're talking you know, 4 milliamps RMS noise. Something like that. And if we disconnect it, it's There you go. Like half a milliamp, 500 microamps.

**Dave Jones:** So, and here's the specs in the manual, and it doesn't actually give you a spec for RMS noise on this thing, but its measurement range is nominally 50 milliamps to whatever the maximum current is.

**Dave Jones:** So, 50 milliamps minimum, but can measure that it can measure under that. Let's give it a try. And let's just measure a low current. I've got my signal generator here.

**Dave Jones:** I've got it just generating 1 kilohertz, and I'm set setting I'm just shorting the output basically into my scope, the 50 ohm output. And you can see 25 milliamps here, almost bang on.

**Dave Jones:** And we're reading 25.7 milliamps there. Now, it looks incredibly clean, and it is like the waveforms actually there. But because well, A, you've got to put noise rejector trigger on cuz we are down in the noise here.

**Dave Jones:** So, if we you know, if we don't do that, the trigger doesn't happen uh properly. And we are in the uh averaging acquire mode as well. So, we can go into the high resolution mode that just does boxcar averaging.

**Dave Jones:** And if we actually look at the signal as it really looks like, it's a little bit it's a little bit hairy scary, but it's there, and you can clean that up, and you can get decent accuracy out of this thing.

**Dave Jones:** So, there you go. It's almost That's practically bang on almost. And I can wind the wick down on that and that's that's 10 milliamps now and of course we're going to have to There we go.

**Dave Jones:** We can really clean that up with averaging and that's that's a 10 milliamp signal. So, it can measure way below its nominal 50 milliamps spec. So, that's not too shabby at all.

**Dave Jones:** So, there you go. I hope you like the look at this Micsig CP2100B current probe and they're a very useful bit of kit. I highly recommend picking one up.

**Dave Jones:** You don't necessarily have to get one from my store. If you do, that helps out the blog, but if you can get it cheaper somewhere else or you prefer the 800 day kilohertz bandwidth one, which is going to be a cheaper than the 2.5 megahertz B model that we've got here, then by all means.

**Dave Jones:** Highly recommend it. So, I'll leave a link down below where there'll be a coupon code. If you do want to get it from the EVblog store and maybe I should like read get a like a custom EVblog branding decal for it.

**Dave Jones:** I think. What do you think? Leave your comments down below. Like I've done that for my meters and my high voltage probes. So, um it's just like yeah, I don't sell these in large volumes.

**Dave Jones:** It's just small volume. Anyway, the very cool part about this is it is available in a even the low 800 kilohertz one is actually quite a high bandwidth for a current probe.

**Dave Jones:** Shop around. Like some of them are only like, you know, like 100 kilohertz or a couple 100 kilohertz. So, even 800's quite high, but yeah, 2.5 megahertz is really high.

**Dave Jones:** To get any higher than that, you've got to go to like the $5,000 Tektronix jobby or something like that that'll do like 50 megahertz. So, yeah, this is really positioned well in the market in terms of bang for buck.

**Dave Jones:** It's probably the best bang for buck current meter out there, but of course I sell it, so you know, but I think it is. Leave your thoughts down below.

**Dave Jones:** So, anyway, if you enjoyed that video, please give it a big thumbs up. As always, comment down below and check out my Odyssey channel and you know what to do.

**Dave Jones:** Catch See next time.
