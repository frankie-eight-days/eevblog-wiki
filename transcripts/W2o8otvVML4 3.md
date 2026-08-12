---
video_id: W2o8otvVML4
title: ZERO INPUT PROTECTION! Micsig MHO14 Oscilloscope/Multimeter
url: https://www.youtube.com/watch?v=W2o8otvVML4
source: youtube-asr
timestamps: {"0": 2, "1": 20, "2": 38, "3": 57, "4": 71, "5": 89, "6": 105, "7": 122, "8": 141, "9": 158, "10": 173, "11": 186, "12": 202, "13": 214, "14": 230, "15": 245, "16": 261, "17": 273, "18": 287, "19": 300, "20": 315, "21": 332, "22": 346, "23": 362, "24": 375, "25": 389, "26": 407, "27": 419, "28": 434, "29": 452, "30": 467, "31": 482, "32": 496, "33": 509}
---

**Dave Jones:** Hi, just a quick follow-up video on this MHO14 Mixig tablet oscilloscope / multimeter thingo. And I can't believe I completely forgot this. Somebody mentioned it in the comments. Thank you very much. I like brain fart. Um, cuz you know I like to talk about input

**Dave Jones:** protection in multimeters. And here is the teardown photo and I completely forgot to mention the input protection on the volts ohms amps jack here or lack of protection. I guess I was carried away by like the non-HRC fuse up here

**Dave Jones:** and this really ridiculously bizarre milliamp and amp terminals that are actually physically joined together. A totally redundant terminal. I And then they had MOSFET switching on the different ranges on the different current ranges. I guess I got carried

**Dave Jones:** away with that and I got carried away with talking about like how lovely all this insulation stuff is and the insulation sheets on the other side and it's otherwise very apart from the quirk that was happening here, like, you know, quite

**Dave Jones:** nicely designed and laid out if somewhat basic. I forgot to mention though, there is no zero zilch nada input protection on the volts ohms amps jack. Let's follow the money. It goes straight into this I don't even know if this is a ceramic

**Dave Jones:** resistor divider or whether or not they've just got the actual individual resistors in there like this, but it basically goes straight into that resistor divider network here. And there's nothing else. There's no PTC input protection, no positive temperature coefficient resistor. If you

**Dave Jones:** don't know what that is, usually it's a a series resistor in series with the input here. Usually you'll have a PTC in series here. Um, either a surface mount one, you know, or a little disc shaped through hole jobbie, you have a PTC resistor

**Dave Jones:** there that if excess current flows into the input terminals either here or here, then the PTC will heat up and increase its resistance, hence positive temperature coefficient. It'll increase quickly increase its resistance and protect the magic smoke from being from escaping

**Dave Jones:** from any of the components in your multimeter circuit. They've got nothing. Not a Even like one of those cheapy $2 or $5 multimeters, they have at least a single PTC in series with them. And there's no MOV protection at all

**Dave Jones:** either. No metal oxide varistors like a clamping device in here. There's no even diode clamp. There's a diode there, right? Little wimpy thing. There's nothing else. There's a That's That's a transistor. It's got Q. There's two transistors down here which

**Dave Jones:** you might think might look like a back-to-back Zener clamper, and I've done a dedicated video on that. I'll have to link it in, but it's not that because look, this pin is connected to this pin. It's not your

**Dave Jones:** typical and there's resistors in here. This is not your typical back-to-back Zener clamping arrangement and it's all the way over here in the corner. So, that's got nothing to do with clamping at all. So, there's no clamping. There's no PTC. There's no

**Dave Jones:** MOV. There's nothing. So, you've got two paths. You've got one which goes into the resistor divider here, and you've got another path which goes into the relay here, and then I'm not sure where that comes out. The traces have to be on

**Dave Jones:** the bottom side of the board. And like look, otherwise they've gone really well doing all these slots, everything, all these beautiful slot cutouts, right? Everything's fantastic and the insulation sheets, they've gone to town and then they've decided well

**Dave Jones:** like what? What's this input protection stuff? What the hell I'm mixing doing here? And this is I I checked the front panel of this thing, it is CAT II 1000 V rated. There is no way this is CAT It's

**Dave Jones:** got zero protection. As I said, even the cheapest sub $10 multimeters at least have some a modicum of input protection on the volts, ohms, amps, diode jack. It's just It's just ridiculous. And if we actually it's a uses the HY13131

**Dave Jones:** chipset. If we actually go in and take a look at the uh let's let's see if we can find it here. They will give us an example circuit, although it's it's not really good cuz there's many different ways to

**Dave Jones:** configure all of um you know the input muxes and everything inside here. Like if I go and show you the internals of uh like a typical chipset, there's many different ways you can actually uh yeah, many different ways that you configure

**Dave Jones:** it, right? They're extremely complex, right? They're extremely complex things. There's many different ways that you configure all of this stuff down here. And you'll notice that here down here it says use a PTC plus a 100 ohm resistor.

**Dave Jones:** On a typical multimeter, you'll get a 1K resistor, often fusible type on the you know your Flukes and your high quality meters, you'll get a fusible 1K resistor plus a PTC um in series. But that's on the RLD pin and that that has to do with

**Dave Jones:** um that's the internal switching matrix here and that has to do with mainly your uh resistance range, diode range, capacitance uh range, and your millivolt range, uh stuff like that. So, I I can't even see. And and that is pin one. That is pin one

**Dave Jones:** on the chip. So, I can't actually see pin one actually connected unless it's actually in there somewhere dropping down through a via there. But anyway, um yeah, it's like they've gone oh okay. And and I don't think that they're using

**Dave Jones:** um this traditional arrangement here because they've just got the input terminal going straight into the resistor divider, which then goes in here, whereas usually it goes through a 10 meg resistor like this, in, and then they have the different resistors,

**Dave Jones:** whereas over here, look, there's only the one pin. So, it's going in. Okay, it might have a 10 meg, although it could be coming out here. Granted, the 10 or the 10 meg could be like in here or something, and coming

**Dave Jones:** out here, and then these aren't actually connected internally to this like I showed previously, so we don't know, um, unless I actually went to the bother to measure it or something like that. I couldn't be bothered, but anyway,

**Dave Jones:** it it doesn't matter. This is a really basic implementation with no input protection. Don't use this thing on the mains at all. >> [laughter] >> This is ridiculous. And how much does the extra like even if it's only 10 bucks extra, I'd expect a

**Dave Jones:** single PTC in there, please. Let alone MOVs, you know, a single PTC, you know, a single MOV. At least, you know, do a modicum of work there, but I guess what do you expect when they use a, uh,

**Dave Jones:** automotive blade fuse, which is not, you know, it's not even like 200 V rated, are they? These are like automotive voltage rated fuses, aren't they? Leave it in the comments down below, but, um, yeah. So, this is this is just nuts.

**Dave Jones:** This is nuts. This is literally the worst input protected multimeter, well, no, you can well, no, even your gla- even your M205 glass fuses that are inside your $5, uh, Elcheapo Harbor Freight multimeters, they're at least, you know, 250 V rated,

**Dave Jones:** right? Um, like, ah, this is just all the, you know, maybe this does a better job, but these are automotive voltage rated fuses, and it's just it's just ridiculous. And what the hell are they doing joining these two jacks

**Dave Jones:** together? It's the only multimeter I've ever seen that has the amps in the milliamps jack physically tied together on the PCB. Totally redundant. It's just It's It's nuts. I can't believe that I forgot to mention the lack of input protection on

**Dave Jones:** this thing. It's just a joke. It's just an absolute joke. Unbelievable. Anyway, >> [laughter] >> thoughts and comments down below. Oh, yeah, you you can actually buy this um oscilloscope. I haven't used it yet, but you can actually Don't know if it's

**Dave Jones:** any good or not, but you can actually buy it without the multimeter. And well, if you're going to buy it with the multimeter, I'd stick to measuring just um yeah, really basic low voltage low energy circuits because this thing's

**Dave Jones:** got nothing. Nada. Thoughts and comments down below. Catch you next time.
