---
video_id: W2o8otvVML4
title: ZERO INPUT PROTECTION! Micsig MHO14 Oscilloscope/Multimeter
url: https://www.youtube.com/watch?v=W2o8otvVML4
source: youtube-asr
timestamps: {"0": 2, "1": 15, "2": 33, "3": 47, "4": 73, "5": 97, "6": 111, "7": 132, "8": 154, "9": 166, "10": 180, "11": 193, "12": 212, "13": 223, "14": 241, "15": 256, "16": 266, "17": 276, "18": 287, "19": 300, "20": 309, "21": 326, "22": 338, "23": 364, "24": 386, "25": 401, "26": 411, "27": 424, "28": 452, "29": 467, "30": 482, "31": 500, "32": 509}
---

**Dave Jones:** Hi, just a quick follow-up video on this MHO14 Mixig tablet oscilloscope / multimeter thingo. And I can't believe I completely forgot this. Somebody mentioned it in the comments. Thank you very much.

**Dave Jones:** I like brain fart. Um, cuz you know I like to talk about input protection in multimeters. And here is the teardown photo and I completely forgot to mention the input protection on the volts ohms amps jack here or lack of protection.

**Dave Jones:** I guess I was carried away by like the non-HRC fuse up here and this really ridiculously bizarre milliamp and amp terminals that are actually physically joined together. A totally redundant terminal.

**Dave Jones:** I And then they had MOSFET switching on the different ranges on the different current ranges. I guess I got carried away with that and I got carried away with talking about like how lovely all this insulation stuff is and the insulation sheets on the other side and it's otherwise very apart from the quirk that was happening here, like, you know, quite nicely designed and laid out if somewhat

**Dave Jones:** basic. I forgot to mention though, there is no zero zilch nada input protection on the volts ohms amps jack. Let's follow the money. It goes straight into this I don't even know if this is a ceramic resistor divider or whether or not they've just got the actual individual resistors in there like this, but it basically goes straight into that resistor divider network here.

**Dave Jones:** And there's nothing else. There's no PTC input protection, no positive temperature coefficient resistor. If you don't know what that is, usually it's a a series resistor in series with the input here.

**Dave Jones:** Usually you'll have a PTC in series here. Um, either a surface mount one, you know, or a little disc shaped through hole jobbie, you have a PTC resistor there that if excess current flows into the input terminals either here or here, then the PTC will heat up and increase its resistance, hence positive temperature coefficient.

**Dave Jones:** It'll increase quickly increase its resistance and protect the magic smoke from being from escaping from any of the components in your multimeter circuit. They've got nothing. Not a Even like one of those cheapy $2 or $5 multimeters, they have at least a single PTC in series with them.

**Dave Jones:** And there's no MOV protection at all either. No metal oxide varistors like a clamping device in here. There's no even diode clamp. There's a diode there, right? Little wimpy thing.

**Dave Jones:** There's nothing else. There's a That's That's a transistor. It's got Q. There's two transistors down here which you might think might look like a back-to-back Zener clamper, and I've done a dedicated video on that.

**Dave Jones:** I'll have to link it in, but it's not that because look, this pin is connected to this pin. It's not your typical and there's resistors in here. This is not your typical back-to-back Zener clamping arrangement and it's all the way over here in the corner.

**Dave Jones:** So, that's got nothing to do with clamping at all. So, there's no clamping. There's no PTC. There's no MOV. There's nothing. So, you've got two paths. You've got one which goes into the resistor divider here, and you've got another path which goes into the relay here, and then I'm not sure where that comes out.

**Dave Jones:** The traces have to be on the bottom side of the board. And like look, otherwise they've gone really well doing all these slots, everything, all these beautiful slot cutouts, right?

**Dave Jones:** Everything's fantastic and the insulation sheets, they've gone to town and then they've decided well like what? What's this input protection stuff? What the hell I'm mixing doing here? And this is I I checked the front panel of this thing, it is CAT II 1000 V rated.

**Dave Jones:** There is no way this is CAT It's got zero protection. As I said, even the cheapest sub $10 multimeters at least have some a modicum of input protection on the volts, ohms, amps, diode jack.

**Dave Jones:** It's just It's just ridiculous. And if we actually it's a uses the HY13131 chipset. If we actually go in and take a look at the uh let's let's see if we can find it here.

**Dave Jones:** They will give us an example circuit, although it's it's not really good cuz there's many different ways to configure all of um you know the input muxes and everything inside here.

**Dave Jones:** Like if I go and show you the internals of uh like a typical chipset, there's many different ways you can actually uh yeah, many different ways that you configure it, right?

**Dave Jones:** They're extremely complex, right? They're extremely complex things. There's many different ways that you configure all of this stuff down here. And you'll notice that here down here it says use a PTC plus a 100 ohm resistor.

**Dave Jones:** On a typical multimeter, you'll get a 1K resistor, often fusible type on the you know your Flukes and your high quality meters, you'll get a fusible 1K resistor plus a PTC um in series.

**Dave Jones:** But that's on the RLD pin and that that has to do with um that's the internal switching matrix here and that has to do with mainly your uh resistance range, diode range, capacitance uh range, and your millivolt range, uh stuff like that.

**Dave Jones:** So, I I can't even see. And and that is pin one. That is pin one on the chip. So, I can't actually see pin one actually connected unless it's actually in there somewhere dropping down through a via there.

**Dave Jones:** But anyway, um yeah, it's like they've gone oh okay. And and I don't think that they're using um this traditional arrangement here because they've just got the input terminal going straight into the resistor divider, which then goes in here, whereas usually it goes through a 10 meg resistor like this, in, and then they have the different resistors, whereas over here, look, there's only the one pin.

**Dave Jones:** So, it's going in. Okay, it might have a 10 meg, although it could be coming out here. Granted, the 10 or the 10 meg could be like in here or something, and coming out here, and then these aren't actually connected internally to this like I showed previously, so we don't know, um, unless I actually went to the bother to measure it or something like that.

**Dave Jones:** I couldn't be bothered, but anyway, it it doesn't matter. This is a really basic implementation with no input protection. Don't use this thing on the mains at all. >> [laughter] >> This is ridiculous.

**Dave Jones:** And how much does the extra like even if it's only 10 bucks extra, I'd expect a single PTC in there, please. Let alone MOVs, you know, a single PTC, you know, a single MOV.

**Dave Jones:** At least, you know, do a modicum of work there, but I guess what do you expect when they use a, uh, automotive blade fuse, which is not, you know, it's not even like 200 V rated, are they?

**Dave Jones:** These are like automotive voltage rated fuses, aren't they? Leave it in the comments down below, but, um, yeah. So, this is this is just nuts. This is nuts. This is literally the worst input protected multimeter, well, no, you can well, no, even your gla- even your M205 glass fuses that are inside your $5, uh, Elcheapo Harbor Freight multimeters, they're at least, you know, 250 V rated, right?

**Dave Jones:** Um, like, ah, this is just all the, you know, maybe this does a better job, but these are automotive voltage rated fuses, and it's just it's just ridiculous. And what the hell are they doing joining these two jacks together?

**Dave Jones:** It's the only multimeter I've ever seen that has the amps in the milliamps jack physically tied together on the PCB. Totally redundant. It's just It's It's nuts. I can't believe that I forgot to mention the lack of input protection on this thing.

**Dave Jones:** It's just a joke. It's just an absolute joke. Unbelievable. Anyway, >> [laughter] >> thoughts and comments down below. Oh, yeah, you you can actually buy this um oscilloscope. I haven't used it yet, but you can actually Don't know if it's any good or not, but you can actually buy it without the multimeter.

**Dave Jones:** And well, if you're going to buy it with the multimeter, I'd stick to measuring just um yeah, really basic low voltage low energy circuits because this thing's got nothing.

**Dave Jones:** Nada. Thoughts and comments down below. Catch you next time.
