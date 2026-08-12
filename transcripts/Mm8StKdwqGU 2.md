---
video_id: Mm8StKdwqGU
title: EEVblog #1294 - LLC Resonant Mode Converter Design
url: https://www.youtube.com/watch?v=Mm8StKdwqGU
source: youtube-asr
timestamps: {"0": 7, "1": 24, "2": 41, "3": 56, "4": 67, "5": 82, "6": 93, "7": 119, "8": 128, "9": 143, "10": 151, "11": 164, "12": 176, "13": 191, "14": 205, "15": 216, "16": 227, "17": 239, "18": 252, "19": 262, "20": 282, "21": 294, "22": 306, "23": 314, "24": 324, "25": 335, "26": 355, "27": 364, "28": 383, "29": 404, "30": 422, "31": 429, "32": 444, "33": 470, "34": 478, "35": 489, "36": 508, "37": 528, "38": 541, "39": 559, "40": 569, "41": 581, "42": 592, "43": 604, "44": 612, "45": 628, "46": 641, "47": 655, "48": 670, "49": 684, "50": 705, "51": 717, "52": 726, "53": 736, "54": 758, "55": 767, "56": 781, "57": 791, "58": 802, "59": 815, "60": 826, "61": 836, "62": 848, "63": 863, "64": 874, "65": 890, "66": 907, "67": 917, "68": 929, "69": 947, "70": 965, "71": 977, "72": 988, "73": 1004, "74": 1020, "75": 1033, "76": 1046, "77": 1062, "78": 1078, "79": 1089, "80": 1105}
---

**Dave Jones:** Now this is actually starting to look an awful lot like a resonant mode controller. It just makes sense. Well, it's a basic generic resonant mode topology, but I think we're going to see that line up here.

**Dave Jones:** We've got ourselves our four diodes down here. We've got ourselves four MOSFETs under here, down on their own heat sink down there. There are four 60R360s. So yeah, I'm pretty sure this is a resonant mode power supply and that makes sense.

**Dave Jones:** Now I won't go into a full tutorial on resonant mode power supplies well cuz that'd be an hour video in its own right. And it can be quite a complicated subject if you're, you know, go into the deep dive into the maths of it.

**Dave Jones:** So what we had up here is our four MOSFETs. I'm going to show you the data sheet for those in a minute cuz that's the tail. And under here we have our four diodes as well.

**Dave Jones:** And we've got some transformers here and a big ass inductor like this. So that with the four MOSFETs and the four diodes, that is a classic configuration for what's called a full bridge resonant converter.

**Dave Jones:** So I'll show you the topology in a minute, but the data sheet for these will pretty much prove it. And those MOSFETs that we saw under there, surprise surprise, look at this.

**Dave Jones:** 600 V CoolMOS CFD7 for those playing along at home. SJ MOSFET. Infineon's answer to resonant high power topologies. Bingo, we got it. The Infineon's latest high voltage super junction MOSFET technology with integrated fast body diode complementing the CoolMOS 7 is the ideal choice for resonant topologies in high power switch mode power supply applications such as server, telecom, EV charging stations, and all that sort of stuff.

**Dave Jones:** And you can go into the technical details about why this is the best in the business and stuff like that. Anyway, yeah, they compare it to all their competitors.

**Dave Jones:** Blah, blah, blah, blah, blah. But, anyway, yeah, that's the jobby that's used in here. So, yeah, this is a resonant mode controller and it makes complete sense because they're trying to put an 800 W power supply into a two rack unit case here.

**Dave Jones:** So, the efficiency is very important. You can't piss away any power in your heat sinks cuz then thermally you've just got to get all that out in the air flow and everything else.

**Dave Jones:** It's just It's horrible. So, you want to make this thing as efficient as possible. And that's what resonant mode converters do. They are higher quiescent current supplies, but when they're actually switching at full power, they are actually more efficient.

**Dave Jones:** And I'll explain why. I found this application note from Infineon. I'll link it in down below. Resonant LLC converter operation and design. And it has a good uh generic application um circuit here.

**Dave Jones:** And I believe this is pretty much what we're saying here. This is why it's a full bridge. Now, you can actually get a half bridge a resonant converter as well and they're very common, which of course will only have if you're aware of your full bridge, you know, your H bridge.

**Dave Jones:** Uh You can get a half bridge would only have the two MOSFETs and would only have the two output diodes. But, in this case, we do have physically four MOSFETs and four uh diodes on those heat sinks.

**Dave Jones:** is what's going on here. Now, how a resonant mode controller works is that it's basically a switch in series with an LC tank circuit, a capacitor and inductor tank circuit here.

**Dave Jones:** And that forms That's where the name comes from. Hence, a resonance. It's resonant mode. So, it actually switches on the resonant point of the L and the C here.

**Dave Jones:** And then you've got a transformer, which then couples that and that's where they're getting their isolation from, of course, uh for each uh channel. And then the output is just a regular full wave uh bridge like this.

**Dave Jones:** But, um it's the switching in here at the resonant point of the LC tank circuit that reduces the switching losses in the converter, and hence the heat dissipated uh during switching.

**Dave Jones:** And there you go, you can go into the uh mass of it for that and it gets more complicated than that uh too. That's the equivalent resonant circuit. Uh and the quality factor and blah blah blah, all that sort of stuff.

**Dave Jones:** And then you can get into the regions and things like that, and we won't go into that cuz it gets quite complex. So, the thing with a regular switch mode uh topology that you're used to with your regular switching uh transistor is that uh it's switching it basically like digitally, like high low high low high low like that.

**Dave Jones:** And the switching losses can be quite high, particularly the higher frequency you go, cuz you want to make it more efficient, so you go to a higher frequency, but at the higher frequency you get greater switching losses with that sort of thing.

**Dave Jones:** Whereas with a resonant mode uh converter like this, it actually changes the wave shape the switching wave shape so that there's effectively less losses. I'll I'll try and Dave cat it.

**Dave Jones:** Oh, and you can see the various uh switching wave forms. So, if you want to go through step by step how it works, this uh application note is uh pretty good.

**Dave Jones:** And it just goes through and it explains each cycle, etc. etc. And it shows some of the wave forms, too. But, uh let me try and explain something here.

**Dave Jones:** Please excuse the crudity of this model. I certainly didn't have time to build at the scale or to paint it. Now, this one on the left here is uh let's say the switching I'm simplifying this.

**Dave Jones:** Let's say this is the switching wave form for your typical uh converter, which is switching hard like this, okay? Now, this area in here and under here, these are you can consider those the power dissipation, the losses in your switching elements, which is heat that you have to get rid of, right?

**Dave Jones:** So, that's the efficiency of your converter. But, a resonant mode controller is going to change instead of like a hard switching like I've exaggerated the slew on that, by the way.

**Dave Jones:** Anyway, the resonant mode controller actually changes the wave shape, so it's like this. And I it's your switching losses are going to be smaller, but basically, what that does is it reduces the amount of switching losses in here, so it's smaller.

**Dave Jones:** And you can get a dramatic difference in the switching losses in your converter from a just a regular switch mode topology, whichever one you want to choose, which is hard switching versus a resonant mode switching, which is using the LNC to change the wave shape there, and you just get basically area under the curve you losses is less.

**Dave Jones:** But, as I said, it's not some magic bullet, that's why not everyone uses switch mode converters because the losses will actually in low power state like in effect quiescent power dissipation is going to be potentially higher for resonant mode stuff.

**Dave Jones:** So, you know, but for large output power supplies like this in a small amount of space where you want to make them as efficient as possible, resonant mode is a decent choice.

**Dave Jones:** And by the way, in this particular case, if you are actually using only half of the sinusoid the resonant LC sinusoid like this, then it's what's called a quasi resonant converter, and you might have heard that.

**Dave Jones:** And the other thing with resonant mode controllers, if you haven't already gathered, is that they're more expensive and more difficult to actually design and tweak and get right. So, hence they're only used in like really top shelf power supplies like this one, and you know, like you can just have a look at like all of the all of the analysis required, the equivalent resonant circuit, and this is just a

**Dave Jones:** first harmonic analysis, I believe, of it. But that's, you know, pretty much all you need to do, but you can go further down the rabbit hole, as I said.

**Dave Jones:** But yeah, actually getting just the tank circuit right and the the ratio, the turns ratio of the transformer and the various inductors and various modes and things like that.

**Dave Jones:** And the parasitics of the transformer, and and in some cases the transformer over here is is going to not be as like as well determined as specific inductors over in the LC tank part and things like this and matching all this and getting it all right and figuring out all this sort of stuff.

**Dave Jones:** Look, I mean, this is just right. Right, yeah, we're we're getting really serious in modes of operation and getting all right. So, it's pretty much vastly more difficult to actually design and engineer one of these than it is for your more traditional PWM you know, boost bucky sepic type converter that you're used to doing.

**Dave Jones:** So, yeah, you really only see these on like really pretty much top shelf power supplies. They've even got a flowchart design step here. What are the Qmax values? Find FX minimum is Kmax required required gain.

**Dave Jones:** All this sort of stuff and like choose your resonant component values. It's just It's it's seriously like selecting the M value for example. So, you've got to understand the formula up here and figure out what your M value is doing.

**Dave Jones:** Of course, you can just like kludge it all and kind of sort of make it work, but that kind of defeats the point. So, here you've got to know the ratio of the total primary inductance to the resonant inductance.

**Dave Jones:** So, you you've effectively got your resonance inductance here and then your primary inductance here transformer. You've got to match all that and all the parasitics involved in that, and it gets complicated.

**Dave Jones:** Any resonant mode smidge mode design experts, let us know in the comments down below if this is your day job designing that resonant mode controllers because yeah, a lot of effort went into doing this.

**Dave Jones:** Let's just put it that way. So, here it is. Like, this is for different values of M, for example, like M3, M6, for example, and how this like it flattens out the peaks here.

**Dave Jones:** So, lower M values are going to give you higher boost gain, narrow frequency range, more flexible regulation. But, if you want higher efficiency, you've got to go for the higher M values.

**Dave Jones:** But, then you got to get higher magnetizing inductance, and it's just yeah. No. So, yeah, like knock yourself out on resonant mode power supply design voltage gain verification. Look at this.

**Dave Jones:** As I said, I'll link this down below. And then you finally, once you've done all that engineering, you calculate resonant mode values, and then bridge and rectifier selection, for example.

**Dave Jones:** This is why they use MOSFETs in here. There's basically two you really can't do this with bipolar transistors cuz their drive requirements are too much. So, really you need a very specific, in this case, highly optimized MOSFET.

**Dave Jones:** One that's carefully tailored for this kind of specific resonant mode operation. And this is what they design these specific MOSFETs for. And if you want to know the difference between a full bridge and a half bridge one, how and why, here you go.

**Dave Jones:** The Although a half bridge requires half the primary turns for the same voltage gain and magnetic flux swing, thus half the primary winding resistance, the primary copper losses are, of course, double compared to the full bridge because the squared RMS and that pesky I squared R thing.

**Dave Jones:** The squared RMS current in the half bridge is four times. So, it might be cheaper and simpler to design a half bridge resonant uh, converter. And, as I said, uh, they're relatively common, um, but yeah, for the best performance in, like, a top-shelf product like this, you're going to want to implement the full-bridge, uh, converter, definitely.

**Dave Jones:** And here's where they talk about the output rectification as well. As I said, you can actually do a full, uh, bridge rectifier for a common transformer like this, but then again, you've got to have like a center-tapped transformer if you want to do that.

**Dave Jones:** Whereas, this one is, uh, not center-tapped. So, you probably larger transformer, maybe there's some, you know, design extra design losses and things like that. So, you might be better off for the full-bridge.

**Dave Jones:** So, there you go. There's a summary of the full-wave, uh, output rectifier compared to the full-bridge. And this has got, like, essentially nothing to do with the, resonant converter side.

**Dave Jones:** That's over on the, uh, primary side. This is just the secondary, uh, side. So, diode voltage rating's got to be times two, number of diodes, but you can save cost on your number of diodes, the conduction losses are divided by two, the number of, uh, secondary windings, but you've got to go up by two, as I said, uh, the resistance per winding goes up by two, and the IMS

**Dave Jones:** current, uh, is a square times square root of a half, and transformer secondary copper losses times two. Blah, blah, blah, blah, blah. So, you know, there's a big trade-off there.

**Dave Jones:** And by the way, you'll see, uh, these resonant mode, uh, controllers often like a half, uh, bridge type actually implemented in something like a, you know, a backlight for, uh, TV backlight, uh, power supplies and and things like that.

**Dave Jones:** Um, they're just trying to basically, uh, get the losses down. And, you know, these do a pretty good job at it. So, they actually give you a design example here.

**Dave Jones:** Once again, I'll link this down below, and you can actually go through the steps of actually designing, uh, a resonant mode, uh, converter step by step, calculating the resonant mode component values and all this sort of stuff.

**Dave Jones:** Look, we need like one mic, uh, for For for the capacitance, we need 11, uh, microhenries, uh, for the inductance, and all that sort of jazz. Experimental waveforms and efficiency, and he's actually measured waveforms and stuff like that.

**Dave Jones:** And you can see typical waveforms here, and you can check out the efficiencies here. You know, 97 and 1/2% it's pretty schmick. And it doesn't drop a huge amount with, uh, input uh, voltage variation.

**Dave Jones:** I mean, even like worst case here, we're still looking at 94%. Not too shabby. Oh, look at that. They've even got a reference design there. And the schematics and the bill of materials and everything.

**Dave Jones:** Great application note. Thumbs up. By the way, I forgot to mention that these are also called a resonant LLC, uh, converters. The reason that they're called LLC is because it's pretty obvious.

**Dave Jones:** Let's have a look down here. There's a capacitor, that's the C, and there's essentially two inductors here because that is, like, the transformer primary has to be, by definition, part it's an inductor, too.

**Dave Jones:** So, it's part of the, uh, LLC tank circuit. You have to take that into consideration in your calculations and stuff like that. So, they flip it even though the C is first physically in the circuit, it's LLC.

**Dave Jones:** Anyway, so if you see that term, they're talking about resonant mode converters. And basically, all it's doing is, uh, taking your DC input here, and it's converting that into a square wave, which then gets pulse shaped by this LC tank circuit.

**Dave Jones:** So, instead of having nice, hard, fast, uh, switching currents, you have nice, more gentle currents. Or, hence, hard switching versus smooth switching, effectively. So, LC circuits are just known as like smooth switches, really.

**Dave Jones:** And another advantage of resonant mode, uh, converters compared to your typical, uh, pulse width modulation ones, which as you know, can change the pulse width and actually freak change frequency, as well.

**Dave Jones:** I'm sure I've done, uh, videos on like, uh, different modes of operation. You know, they'll go into some pulse skipping mode and then they'll go they'll switch down frequencies or up frequencies depending upon the output current and things like that.

**Dave Jones:** They'll dynamically change. And they're actually when you've got like really broadly changing switching frequencies like that, it's really hard to filter out those sort of frequencies. So in terms of your EMI or electromagnetic interference and your compliance for that sort of stuff, resonant modes are actually much better.

**Dave Jones:** It's It's in the name. It resonates at one frequency. So you've pretty much got a really narrow range of frequencies that you have to filter out here. And it's it's just much easier to filter out to put in an EMC filter for your resonant mode LLC controller.

**Dave Jones:** And that especially comes into play at large output currents and large output powers cuz when you're switching huge amounts of current, if you're doing that over a huge variable frequency range, you know, you can really come a gutser come EMC testing time.

**Dave Jones:** So yeah, resonant mode has definite advantages there. So you can actually see these capacitors under here like this and they've got the same ones up under here. You just can't see it at this angle.

**Dave Jones:** So they would be our series capacitance in our topology. And maybe the inductor is actually this baby, but the part number of these two is identical. So we need an inductor plus a transformer.

**Dave Jones:** So maybe they're reusing one side. I'm not sure. Now you you might think that this one here, that's the resonant mode inductor, but I don't think so cuz it's not these little fiddly surface mount jobbies here.

**Dave Jones:** So yeah, and its location is further like is looks like it's on the isolate you know, it's on this isolated side of the converter. So that that really doesn't make sense.

**Dave Jones:** So that's probably just part of an output filter I'd say, but yeah, I'd say yeah, it's coming in here. This is our full wave bridge. These are our caps.

**Dave Jones:** Stick with me. And we've got an inductor, we've got a the now isolation transformer, we've got our four output rectifier diodes down here, and then there's as I said, there's another MOSFET under here, so I'm not quite sure what they're doing there.

**Dave Jones:** And then we've just got some output filter in. So, yeah, I think that's how it works. Sure the power supply aficionados will all be commenting down below about what's going on here, but anyway, it looks to be some variation of a resonant mode controller.

**Dave Jones:** Exactly how they're doing it, I don't know. We'd have to reverse engineer it, and that would require ripping the whole guts out. So, I hope you found that brief overview of LLC or resonant mode converters useful.

**Dave Jones:** If you did, please give it a big thumbs up. As always, you can discuss in the YouTube comments down below or over on the EV blog forum, or even in my library comment videos, even though the comment system's still not that terrific on library, but anyway, I'm getting right up there on subs.

**Dave Jones:** Fantastic. Anyway, catch you next time.
