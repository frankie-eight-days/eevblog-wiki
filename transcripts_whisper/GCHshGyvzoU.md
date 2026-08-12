---
video_id: GCHshGyvzoU
title: EEVblog #1090 - Sony Mystery Teardown
url: https://www.youtube.com/watch?v=GCHshGyvzoU
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 18, "2": 38, "3": 61, "4": 80, "5": 97, "6": 117, "7": 134, "8": 154, "9": 170, "10": 186, "11": 199, "12": 221, "13": 239, "14": 252, "15": 270, "16": 286, "17": 307, "18": 322, "19": 338, "20": 358, "21": 377, "22": 393, "23": 411, "24": 429, "25": 445, "26": 461, "27": 479, "28": 492, "29": 510, "30": 526, "31": 542, "32": 559, "33": 575, "34": 591, "35": 606, "36": 627, "37": 646, "38": 661, "39": 678, "40": 696, "41": 714, "42": 729, "43": 746, "44": 768, "45": 786, "46": 799, "47": 814, "48": 836, "49": 860, "50": 882, "51": 902, "52": 918, "53": 936, "54": 950, "55": 971, "56": 989, "57": 1006, "58": 1021, "59": 1040, "60": 1058, "61": 1071, "62": 1090, "63": 1106, "64": 1123, "65": 1145, "66": 1175, "67": 1199, "68": 1219, "69": 1243, "70": 1261, "71": 1277, "72": 1293, "73": 1309, "74": 1324, "75": 1341, "76": 1355, "77": 1373, "78": 1390, "79": 1403, "80": 1418, "81": 1438, "82": 1460, "83": 1478, "84": 1493, "85": 1509, "86": 1528, "87": 1547, "88": 1568, "89": 1586, "90": 1601, "91": 1617, "92": 1631, "93": 1647}
---

**Dave Jones:** Hi, it's mystery teardown time. Answers on the back of a postcard, please, what you think this might be. It's a bit of kit which I used many, many times back in the day for companies that I've worked for. What do you think it is?

**Dave Jones:** Look at all these output B and Cs. Hmm, lots of little trimmer caps. Nice. Get in there if you're tongue at the right angle. And it's got some inputs with some LEDs at 2, 4, 8 and 16. Ooh, look, it's had some ground bounce.

**Dave Jones:** I'm here all week. So what is it? Well, it's the PC216AX and it's a Sony. Check this out. It's what's called an instrumentation data recorder. And this is one of the more obscure bits of equipment that Sony manufactured. For a specific market in this case,

**Dave Jones:** this was like the industry standard instrumentation data recorder for use in the field that I was in, which was the seismic underwater industry, which is all low frequency type stuff, but like, you know, hundreds of channels, multiple channels, and also the vibration test industry as well.

**Dave Jones:** You would actually hook all of your sensors up to these, be they vibration sensors, let's say you're testing a motor or an engine or something like that, you might put, you know, dozens of different little vibration sensors all around it, and you'd hook them up to all these input channels here,

**Dave Jones:** and then you would record those onto digital audio tape. And it was state of the art for the day. It had a 16-bit converter on each individual channel, none of that multiplexing rubbish, but unfortunately the bandwidth did scale down based on how many channels you enabled.

**Dave Jones:** That's why we have the LEDs here for 16 channels, 8 channels, 4 channels, and 2 channels. In 2-channel mode, it had a bandwidth, an analog bandwidth of 20 kHz, and if you had all 16 channels enabled, all sampling at once, then it'd only have a 5 kHz bandwidth.

**Dave Jones:** But hey, that's plenty for lots of vibration work, and especially seismic and underwater, you know, sonar-type stuff. It was the duck's guts. Cost a fortune. If anyone knows the original price, I completely forget how much this thing cost, but if you had to ask the price, you probably couldn't afford it.

**Dave Jones:** And also there was a smaller model of this one, an 8-channel I believe, but you could also get like expansion units to hook onto. It was a complete, like, you know, system thing. There were all sorts of digital interfaces and everything else. Fantastic, very niche bit of kit,

**Dave Jones:** but, you know, it became the industry standard in any sort of, like, analog recording. And I always wanted to tear one of these things down at work, but you couldn't because they, you know, like, you just, this was like the holy grail bit of recording gear.

**Dave Jones:** You just didn't go taking apart something like this willy-nilly. And I think we even, did we get it calibrated? I can't remember, but, you know, you don't want to break the seals and everything else. If you got caught, you'd be in deep trouble.

**Dave Jones:** And this is actually manufactured by Sony Precision Technology Inc. This is a subsidiary of Sony that specifically make niche high-end gear for, you know, instrumentation and industry measurement and stuff like that. And the Sony Precision Technology Group actually started in 1969, so it's a very old group.

**Dave Jones:** And they make some of the best niche stuff you've probably never heard of. All the best stuff's made in Japan. Stop! Before returning this equipment, it's your oil accessories, blah, blah, blah, $50 replacement cost. Apparently this actually comes from a rental company, and you could actually rent this gear

**Dave Jones:** because they were very expensive. So if you're a company that, like, needed to do some testing, like a, you know, engineering company, and you want to do some vibration or other types of, you know, testing for a couple of weeks at a test house,

**Dave Jones:** you usually wouldn't buy one of these. You'd just rent one. So as you saw, it's got 16 analog inputs here. There's no trimmers on those. Normal 100k input impedance up to plus minus 26 volts peak there. We've got a Sony digital audio tape here.

**Dave Jones:** We've got a large screen. I'll power it up and show you. And, you know, you can set, like, multiple tape speed, times one, times two data rate, stuff like that. And you can put ID in there and tag and things like that. You can generate test signals and, you know,

**Dave Jones:** like, it's really purposely designed. This is not a consumer bit of kit. Purposely designed for this sort of, you know, data measurement, vibration, and analog type storage and replay. Because you've got 16 outputs here. You've got individual trimmers on each one. You can trim the output level and stuff like that.

**Dave Jones:** There's a monitor. You could microphone to do some annotation and stuff like that. And on the back here, because this was actually designed as a portable bit of kit, and we use it in the field very often, you know, like, yeah, you maybe could have done this

**Dave Jones:** with, like, a big multi-channel DAC card in a PC, like an ISA bus PC back in the day, or something like that. But having a PC do this sort of stuff, especially in a portable environment, we would actually take this out to a, like, a lake,

**Dave Jones:** where we'd actually test underwater sonar gear. And you don't want to, you know, drag around a PC. Having a portable bit of kit like this was much better. Anyway, it did have a battery, or you could, from an external battery pack here. But also, this one actually has a battery eliminator here.

**Dave Jones:** This is just the mains input, so universal mains input. You could power it from mains, but I don't know if the specifications, like, noise specifications still held with the mains. I don't probably. You know, they designed this thing well. Earthing, of course, system grounding, very important.

**Dave Jones:** So that's why they're strapping this earth over to here like this. And it had various expansion controls. As I said, like, you'd get multiple expansion chassis to put that on there. Digital I.O., external control, and all that sort of jazz. Now, it's actually got a dip switch here

**Dave Jones:** for 16 or 15-bit sampling mode. Normally, if you're just recording the signal, you put it in 16-bit acquisition mode, so a 16-bit ADC. But you could also put it in 15-bit mode. Of course, you sacrifice, you know, a whole bit. But that bit, what you can do with that

**Dave Jones:** is actually you can feed in an external digital signal. So let's say you had some sort of sensor that, you know, checked the rotational direction of some motor that you're testing or something like that. Then you could actually record, use that as a digital,

**Dave Jones:** like just a one-channel logic analyzer, so to speak, that actually recorded along with your analog data. And there's all the sample rates and things like that, durability of the battery pack. They tell you everything. The test signals, how you could actually search for stuff and things like that.

**Dave Jones:** And, of course, we've got the window down in here so you can actually see the digital audio tape doing its business in there, see if there's any jams and stuff like that. So this was much better than, like, analog recorders. So you could store all your analog stuff on error-corrected,

**Dave Jones:** they use double Reed-Solomon error correction on the digital audio tape. So it restores it digitally. And you can also, of course, output, re-output it analog-wise. But, of course, you'd get maybe some loss there. Or you could extract the data out digitally via a PC.

**Dave Jones:** And they had Windows 95 software that went along with this that allowed you to analyze everything. Very cool bit of kit. So I'm going to violate my rule and turn it on before I take it apart, because who knows what state this is going to be

**Dave Jones:** after a teardown. And it's going through a calibration routine now, and you'll actually see it. The LEDs will light up. It'll go 16 channels, 8, 4, and then 2 here. There's a bar graph. And then it's actually got, like, a bar graph indicator on here as well

**Dave Jones:** for monitoring the inputs and stuff like that, like each individual channel. You can see, there we go, 8. And it'll drop down to 4. It's doing a calibration check on all those channels. So, you know, pretty advanced bit of kit. So we're actually in 8-channel mode at the moment,

**Dave Jones:** hence why we've just got the 8 indicators there. And these would go up and down to match the input. It's like an analog audio spectrum analyzer, so to speak, except they're not frequencies, they're individual channels. You know, tape time and stuff like that,

**Dave Jones:** source, how many hours, how long it's been going for, your input voltage range, which channel you're monitoring on the output, tape ID, and all sorts of advanced stuff. It's very cool, whether or not you've got any overloads, test signals, everything else. And as far as ranges went,

**Dave Jones:** I'm in manual ranging mode at the moment. 0.5 was the lowest range, but with a 16-bit converter, that was pretty sweet. 1, 2, 5, up to 20-volt range. The screen actually does look a lot better than what it did before. I just had it at a very low angle

**Dave Jones:** compared to my overhead studio lights here. But yeah, it has a nice, funky, retro-green background on it. Actually, this is interesting. Forgot all about this. It's actually got, it was in power-save mode before, so it switches off the backlight to conserve battery power.

**Dave Jones:** But hey, that's important. You're out in the field and you're doing hours worth of measurements. You know, you can come a gutter. And of course, for system flexibility, you can set the input range individually on all of the 16 channels. Okay, let's void this warranty.

**Dave Jones:** Looks like this lid is going to pop off, and we're in like Flynn. Oh, check it out. Look at the shielding mesh. So that's really interesting. Look at that particular mesh they've got on top. It reminds me like of a rather larger Aputure microwave oven.

**Dave Jones:** And there's just two screws holding that. Why you need that with the metal top on the thing, I don't know. It's lower impedance. Wow, that could be one of the reasons why they're serious about the dust collection. They're serious about that DC to DC converter.

**Dave Jones:** Look at that. Made in Japan, of course, by Sony. And not only is that completely shielded in there, does it have a... I think it's got a temp sensor on the outside as well. Look at that. Oh, wow, they're really doing the business.

**Dave Jones:** So it's obvious they want to keep the crap out of the instrumentation, which is what you'd expect, because this is a 16-bit precision instrumentation recorder. And of course, you know, you need, because of the dynamic range of this thing, the large voltage ranges, the 20-volt ranges that we saw before,

**Dave Jones:** you know, it's all powered from a single battery, much lower voltage. You need the DC to DC converters to generate the required rails. But jeez, they've got a town there. And looks like a whole bunch of plastic package. Tranny's under there. Look at that.

**Dave Jones:** So are they linear regulators on the output? Probably. And you start to see the modular construction of this. We've got our digital audio tape, our DAT tape recorder up here. Of course, Sony invented the digital audio tape in 1987. It's their thing. And then we've got the DAT controller down here.

**Dave Jones:** And as is typical, as seen in many Sony teardowns, they like a roll in their own silicon. So there you go. That's whatever, like that's the, like is that like motor drive and all that sort of jazz going directly into the digital audio tape.

**Dave Jones:** But they would have, like, used that across multiple products. It wasn't just designed for this. And our wiring down in here looks neat and tidy. You can see the attention to detail. They've got the bypass caps there on the external DC supply. It's all nicely crimp-plugged and all that sort of jazz.

**Dave Jones:** Cable tied back. Neat. For those who love seeing inside their digital audio tape, oh, look at the little spinny cleaner there. Look at that. Very nice. Anyway, it's, yeah, we've got ourselves, oh, there you go. They're probably positioned, the reason that they've got the metal spokes

**Dave Jones:** on there is that they're getting positional information on that as it spins around so they know the exact location of the tape and whatnot. Oh, for those who like heads, there you go. Oh, spinny, spinny. And of course you've got all the requisite pinch rollers

**Dave Jones:** that are going to move in and out, hence all those. You can see the shafts in there. I wish, I do have a digital audio tape. Haven't I done another teardown of a dat thing? Anyway, I do have a tape somewhere, but I can't find it.

**Dave Jones:** So anyway, we're not going to be able to get that puppy working. It's actually a very nice combination of, look, we've got a flat flex connector board up here going to various motors and sensors and drivers and whatnot. And looks like we've got a drive motor down here

**Dave Jones:** and all the requisite cogs and everything else. Beautiful. It's a Sony. There's our front panel board. We've just got some keypad encoder stuff there. There's our LCD driver board, Hitachi driving chipset, all fairly standard. Once again, they're taking grounding and decoupling to ground so serious.

**Dave Jones:** These are the battery contacts here, and they're decoupling all of those directly to the chassis ground. Nice. Okay, let's have a look at the bottom. Ah, been mooned. Shielding, again. And look at that, just some sort of insulating sheet perhaps. Hmm. So it clearly wasn't good enough to just use the back metal case for the shielding.

**Dave Jones:** They wanted a more localized lower impedance ground. Now let's have a look at the bottom. Ta-da! Now we're talking. Check that out. Wow. Double-sided load, of course. And here's all the analog channels. Actually, well, that's only eight of them. Where's the rest? Where's Wally?

**Dave Jones:** Must be on the other side. Are they double-sided? Maybe there's two channels per thing. Now unfortunately I can't remove that shield for you. I don't, I believe this is in working condition, so I don't want to go desoldering that whole can. But yeah, you know, you can expect analog-y type stuff under there.

**Dave Jones:** Just like here, got a whole bunch of passives and everything else. You can see all the red stuff under the components here, each individual one. That's all the glue that holds down the components when they wave solder the bottom half of this board,

**Dave Jones:** because yes, this is a wave solder board. You can tell from the solder feeding pads, the large ones on the end that sort of leach away the solder as it flows over the solder bath and prevents shorts. But each one of those components glued down.

**Dave Jones:** And I can't get a good shot at the front panel PCB yet, because you have to take much more of it away to actually get that, but you can see the input here, it's got RFI, that's the BNC, that's the back of the BNC connector.

**Dave Jones:** You can see the RFI bead there, going down. Looks like they have another inductor up there by the looks of it. And it's all then individually coax wired over to the board up here, which we saw which then has the metal can, and that's obviously the front end amplifiers on the thing.

**Dave Jones:** We've got two coaxes going into each connector there, so obviously this is a pair of channels. Hang on, hang on, it's going to flip! Yes, Sony the masters of the PCB flip. Oh, not quite mastering, more shielding. Once we get all the coaxes off, we're going to be in like Flynn

**Dave Jones:** on the top side of that dart acquisition board, which is the thing I'm really interested in. Well this is interesting, we can flip it out, and one of the, I think probably the only board-to-board interconnect they've got in here is this, I can't remember,

**Dave Jones:** is that the digital I.O., digital I.O. connector at the back, actually goes into the back of that board. So someone went, oh yeah, I don't like this wiring, bugger that, I want a board-to-board interconnect, and got away with that. But there's the main board.

**Dave Jones:** Ooh, looksy. I think they're our ADCs. Check it out, that metal can did actually lift off there, and now we can see we've got, here's our input starting over here, and we've got a couple of relays, one per channel, got a couple of op-amps in there, I'll get the part numbers on those,

**Dave Jones:** or obviously this looks like, this is probably the ADC, I'll have to look it up. This is probably the DAC on the other side. We've got a couple of trimmers in there, two per channel, and these output coaxes here go down to the analog output,

**Dave Jones:** that's why it tells, like the B and Cs on the side, they're 16 channels, so that's why that one is probably the DAC there. And there's a couple of trimmers up the top there, 0.5 volts, probably setting, are they setting like range levels,

**Dave Jones:** or, oh no, voltage ref, there we go, 5 volts. So that's some sort of voltage ref for the ADC or something, perhaps? And that company, Asashi Kasai, I've heard of it somewhere, but my memory completely fails me, it's actually Asashi Microsystems, which is part of a much bigger group,

**Dave Jones:** which has been going on for like, I don't know, 50 year old company or so, actually 1922 I think they started, absolutely crazy. Anyway, don't know if they're still in business, taken over, merged, done whatever, but they had a semiconductor thing, and maybe they were contracted by Sony

**Dave Jones:** to custom make this thing, maybe they already had it and they based it around this obviously 16-bit ADC, we don't know. Well as it turns out, Asashi Kasai, or however you want to pronounce it, they're huge, no wonder I had like, rung a bell.

**Dave Jones:** They're like an $18 billion a year company, and they're into chemicals, home healthcare, fibers, electronics, construction materials, services, engineering, they actually commercialized the first lithium ion battery in cooperation with Sony actually. They still do LSIs, Hall Effect ICs, and all that sort of stuff,

**Dave Jones:** and they've even still got their microelectronics division still exists, and still make premium audio DACs. So the one we're looking at here, the AK4328 has been discontinued, but Cirrus Logic, well, Crystal Semiconductor slash Cirrus Logic make the CS4328. So it's like, I don't know whether it's under license or what the deal is with that,

**Dave Jones:** but anyway, yeah, they're still around, they're still a thing. Look it up, you can't get anything for the original company, but the Cirrus Logic CS4328, that is certainly available, and that's a dual stereo audio DAC. Exactly what you'd suspect. And aha, those chips are actually good old 74HC,

**Dave Jones:** they're 74HC4352s, they're like dual multiplexers or whatever. So there you go, they've got another 8-pin jobby in there. Is that an op-amp? Yeah, that's got 812 on it, and if you look up, say, an analog devices AD812, that's actually like a matched pair of trannies,

**Dave Jones:** like for amplification, like front-end. Something like that, is that how they're doing it? So all this stuff in here is support stuff for the data acquisition front-end, all 74HC series stuff, but hello, all you TI TMS320 fanboys! There's our DSP. Looks like they've coupled that onto some memory there.

**Dave Jones:** What's that? Mitsubishi job? SRAM? Not actually particularly fussed with the rest of it, especially that main logic board down in the bottom down there, that's just going to be like, you know, the main processor for like the digital interface stuff and driving the LCD

**Dave Jones:** and all that sort of stuff. It requires a significant effort to take apart the rest of this, I'm afraid, so I don't think I'd bother. I just wanted to see basically the front-end stuff, the construction and the shielding and all the other goodness

**Dave Jones:** which goes into the systems engineering of this thing. So as I mentioned, you can imagine like what your options were in the mid-90s, what are your options these days, if you've got a whole bunch of sensors, you know, a dozen or two sensors from people are still doing shock

**Dave Jones:** and vibration testing, acoustic testing and all that sort of stuff, it's still big business, still a very big need for that, if not more these days. And there, what do you do? How do you record all these sensors? Yeah, you could get like data acquisition cards for the PCs,

**Dave Jones:** but do they have nice BNC interfaces? Do they have the, they've probably got the dynamic range, probably got the electrical specs and things to do it, but do they have the nice interfaces and everything else? And how do you do it? There weren't too many options back then,

**Dave Jones:** and this was one of the obvious and best and state-of-the-art options to measure multi-channel, low-frequency sensor data, and to not only record it, but then play it back or suck it into a PC and then analyze it further. It was like fantastic stuff.

**Dave Jones:** I mean, there were models before this one, but this one sort of like became the de facto industry standard. Everyone used it. And the good thing about tearing down something like this is you can see that they haven't cut corners. This is not a consumer bidder kit.

**Dave Jones:** Price really didn't matter. The market paid for what it was, you know, for the product and what it was worth. It basically was like little if nothing else that could really do the job. So yeah, it didn't really matter. And they spared no expense on this thing, and it shows.

**Dave Jones:** And you can bet your bottom dollar, as we saw with like a lot of the grounds and things like that in here, they, you know, really very careful attention to detail in terms of, you know, signal fidelity, noise, grounding, dynamic range, all that sort of stuff.

**Dave Jones:** There would have been lots of little small touches that went into the design of this thing to ensure it had the best possible performance. So I think I'll leave that tear down there. I want to put it back together. It requires a lot of effort to get further

**Dave Jones:** with minimal sort of value add there in terms of that. Oop, all the electrons are going to fall out. It's upside down. But there you go, I hope you enjoyed that look at a very specialized bit of kit from a division of Sony,

**Dave Jones:** which you probably have no idea existed, probably had no idea there were specialist instrumentation data recorders like this. And you can still buy these sort of things. You might even be able to buy tape-based ones, and there's still a good second-hand market for these old Sony instrumentation recorders,

**Dave Jones:** from like the early to mid-90s. As I said, these were the industry standard for anything involving, you know, low-frequency audio, acoustics, vibration, shock, you know, all that sort of transducer, underwater sonar-type stuff, which is down in the low-frequency ranges. Because the industry I spent a lot of years in

**Dave Jones:** was like 2 kHz, was like RF, right? So, you know, everything was like really low-frequency stuff, you know, DC to 2 kHz type stuff. And we use these. These were the industry standard data recorders. They were fantastic little beasts, and a lot of engineering goes into there.

**Dave Jones:** And as I said, if you know what these things originally were priced at, I'll see if I can Google maybe some prices, but I doubt if we'll find anything. But if you know, please leave it down below. So what's actually available to do this today?

**Dave Jones:** Well, I just went to a random Daclog systems in the UK. They're like a supplier of these types of data acquisition systems. And if you go into obsolete systems down here, we can have a look. Here we go. Ta-da! Recognize anything? The PC200 series Sony.

**Dave Jones:** By the way, they did follow up the 200 series with the Sur 1000, which is just basically the same, well, a similar thing. It's just upgraded. They have a new version of the software, the PCScan3 or whatever it was called. But anyway, what do they have these days?

**Dave Jones:** Let's have a look at stand-alone portable data loggers. You probably saw one there. Ah, look at this jobby. TEAC. Who would have thought TEAC, right? Look at this beast. Look at this. There you go, a 16-channel instrumentation wideband data recorder. Is that like, is that record to hard drive?

**Dave Jones:** Surely they don't still use that. Yeah, one terabyte of data. Flexible memory system. Yep, flash, memory card, all that sort of stuff. There you go. Recording time, 38 hours, still battery-powered. Look at the size of these things. Absolutely enormous. And they most probably come with interfaces

**Dave Jones:** for direct vibration and shock sensors using the ICP interface or something. Does it say that down here? I'm sure they would if you looked them up. Probably some of them do. So that wouldn't surprise me at all. There's other companies. TEAC, they produce a smaller version.

**Dave Jones:** These other little portable, rugged, sort of with rubber baby buggy bumpers on the side of them. There you go. Look at that. They got ICP interfaces. Anyway, it wouldn't surprise me because the problem with, if you wanted to hook them up with vibration

**Dave Jones:** or shock, you know, accelerometers, then you had to have like a 16-channel accelerometer ICP amplifier kind of thing. It depends on the sensor you had. You had to have that in series with the coaxes, but a lot of these have that built in.

**Dave Jones:** They're just like a voltage, you know, driving down the line, and then it just taps off the AC signal kind of thing. So a lot of them will have that sort of stuff built in these days. But there you go. You can still buy these badass,

**Dave Jones:** look at these badass-looking systems. They're great. Look at that. Who knew? So I hope you enjoyed that look at a bit of an unusual bit of like state-of-the-art instrumentation. If you did, please give it a big thumbs up. As always, discuss down below

**Dave Jones:** on the EEVblog forum. Subscribe, support on Patreon, all that sort of stuff. Catch you next time. www.eevblog.com www.eevblog.com
