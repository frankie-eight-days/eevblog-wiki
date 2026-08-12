---
video_id: mdOauVzY9OU
title: EEVblog #828 - Siglent SPD3303X Precision Lab PSU Teardown
url: https://www.youtube.com/watch?v=mdOauVzY9OU
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 29, "3": 43, "4": 53, "5": 71, "6": 83, "7": 92, "8": 104, "9": 124, "10": 147, "11": 165, "12": 176, "13": 187, "14": 199, "15": 217, "16": 235, "17": 244, "18": 254, "19": 268, "20": 279, "21": 290, "22": 300, "23": 314, "24": 323, "25": 347, "26": 363, "27": 373, "28": 384, "29": 396, "30": 409, "31": 426, "32": 439, "33": 449, "34": 461, "35": 471, "36": 489, "37": 505, "38": 515, "39": 523, "40": 536, "41": 555, "42": 567, "43": 586, "44": 596, "45": 620, "46": 629, "47": 642, "48": 653, "49": 667, "50": 681, "51": 697, "52": 710, "53": 733, "54": 747, "55": 757, "56": 788, "57": 795, "58": 804, "59": 820, "60": 829, "61": 837, "62": 848, "63": 860, "64": 872, "65": 885, "66": 902, "67": 912, "68": 927, "69": 938, "70": 946, "71": 962, "72": 973, "73": 986, "74": 1003, "75": 1012, "76": 1023, "77": 1036, "78": 1045, "79": 1061, "80": 1076, "81": 1094, "82": 1111, "83": 1125, "84": 1136, "85": 1152, "86": 1167, "87": 1185, "88": 1199, "89": 1207, "90": 1220, "91": 1234, "92": 1245, "93": 1259, "94": 1278, "95": 1288, "96": 1300, "97": 1310, "98": 1323, "99": 1338, "100": 1349, "101": 1361, "102": 1373, "103": 1392, "104": 1403, "105": 1412, "106": 1422, "107": 1430, "108": 1441, "109": 1456, "110": 1467, "111": 1481, "112": 1494, "113": 1503, "114": 1516, "115": 1524, "116": 1543, "117": 1565, "118": 1581, "119": 1591, "120": 1611, "121": 1632, "122": 1650, "123": 1659, "124": 1678, "125": 1690, "126": 1704, "127": 1736, "128": 1749, "129": 1760, "130": 1780, "131": 1795, "132": 1808, "133": 1825, "134": 1842, "135": 1856, "136": 1869, "137": 1881, "138": 1891}
---

**Dave Jones:** Hi, it's Teardown Time. We've got another linear bench power supply. It's the new Siglent SPD3303X series programmable power supply. As all new Siglent gear is, it's all the new X series.

**Dave Jones:** They're designed to work together and I don't know, have a similar look and feel or something like that. But anyway, this is a $539 US street price triple output 220 watts or thereabouts power supply.

**Dave Jones:** As the model number gives it away, we're looking at 30 volts 3 amps per channel, slightly over that actually, and a fixed voltage output here. So yes, it's a real big thumping linear power supply.

**Dave Jones:** None of this switch mode rubbish. It's got universal voltage input on the well, switchable voltage input on the back here. So it doesn't matter what region you're in, you can switch it to your voltage.

**Dave Jones:** It's ethernet enabled of course or programmable functionality. And it's a precision power supply. We're looking at 1 millivolt 1 milliamp resolution on the thing, which is order of magnitude 10 times better than the Rigol DP832 power supply.

**Dave Jones:** Cuz you have to buy with the Rigol, you've got to buy the software option to get this the resolution that this one has. So we'll worry about how it works and all that sort of jazz later.

**Dave Jones:** What we want to see now is what's inside. You know what we say on here on the EV log, don't turn it on. Take it apart. Now it looks and feels fairly decent quality.

**Dave Jones:** It's got a decent carry handle on the top. And I got no major issues with it except the binding posts could have been a bit higher quality. I don't know, they just feel a little bit cheapish.

**Dave Jones:** I sort of maybe would have liked a bit better. And the holes on them for the wires are pretty darn small. Look at that. I would have preferred big beefier holes so that you can get, you know, decent cable into these things because this thing, you know, a 3 amps and you can parallel the thing for even higher current.

**Dave Jones:** So, yeah, I think those holes are a bit small. I hate it when the hole's too small to poke your stuff into. Uh-oh. Not a standard width. And I'll tell you what, the binding posts don't even um take 4 mm banana plugs nicely.

**Dave Jones:** I mean, that's uh that's actually quite a loosey-goosey fit in there and so is this one. Like this, you know, I I know this is a BNC, okay? But, you know, like that that is real try like this is not feel a vision, but that is really loose.

**Dave Jones:** This one that doesn't have the uh the, you know, the flared things on it, that's just that just does not fit at all. I mean, whereas on the Rigol, for example, it fits just fine.

**Dave Jones:** So, yeah, don't like the binding posts at all. They have a nice big clunking power switch, beauty. No that's soft power rubbish. All right, so let's lift the hood on this thing.

**Dave Jones:** Had to take the handle off the top. I like that the handle is actually screwed into the metal work on the top there. That's very nice. It's not just like into the like the folded sheet metal case and then it's only held down here.

**Dave Jones:** So, that's you know, it gives you a lot of confidence that it's not just going to break on you. So, the quality in a power supply is all about the mains uh transformer, the uh quality and brand of capacitor used, the thermals, the internal wiring, you know, construction that's nicely loomed and things like that.

**Dave Jones:** So, let's give it a whirl. Ta-da! We're in like Flynn and got a nice big toroid here. Look at that. That's a monster. I like that that's mounted vertically, but is that a shorter turn?

**Dave Jones:** Uh-oh, I hope not, but anyway, we'll get to that. Nice cable looming here. It's all, you know, it's all cable tied held together. I don't know where that one's going.

**Dave Jones:** That's That's flapping around in the breeze there. But, uh they've got Silastic down here. We'll take a look at the quality of the caps, but they've gone to the effort to put some Silastic down there.

**Dave Jones:** So, here's this nice uh crossbar I was uh talking about with the um anchor holes in there. So, that's quite nice. And the thermals look and in fact, it's very, very similar to the to another one we've looked at.

**Dave Jones:** I'm sure it is very similar anyway. The uh the fan, of course, here uh it's blowing out the back, so it's sucking the air through the uh heat sinks here.

**Dave Jones:** So, our uh power transistors are on the side here. So, that's quite nice. Um that's all hunky-dory. There's our mains board down there. We've got our mains wiring going over.

**Dave Jones:** That looks very nice. Looks like it's doing the business. We'll check out the mains, but that looks okay. It's going down to a uh a screw terminal down there.

**Dave Jones:** Um got a shake-proof washer on it? I'm not sure, but anyway, let's have a look at this transformer. Now, with toroidal transformers like this that have they're a toroid shape, hence their uh name, they've got a big hole in the middle.

**Dave Jones:** They're a big donut, and you always mount them down with a big screw going right through the middle. And what they've got is two bits of sheet metal work, which are connected down to the chassis down here, okay?

**Dave Jones:** So, they're not isolated. They're electrically connected. So, this plate and this place is is at both at earth uh potential. And if you actually connect a bolt from one side to the other here to hold it in place, you actually create a shorter turn, which goes through the middle of the toroid, around through the chassis, and around through the other side.

**Dave Jones:** And that's a real trap for young players and incredibly bad design practice, but I think I might seen insulating washer right down in there. So, I think they know all about that and they're doing the right thing.

**Dave Jones:** So, it's hard to tell about the quality of the toroidal transform, but all looks okay. The wrapping all looks you know, hunky-dory. So, I'm going to give that a pass.

**Dave Jones:** No problems whatsoever. Shouldn't be any of course hum problems and things like that because there's no it's not like a C-core laminate transformer which you have to be careful of.

**Dave Jones:** If you don't laminate them properly, then they can actually vibrate and that's where you get that typical you know, sometimes you can hear that hum in instruments. That actually comes from the mains transformer.

**Dave Jones:** You won't get that in a toroid. So, it's very nice to see a toroid there instead of toroids generally you know, a higher quality solution than a you know, your traditional C-core transformer.

**Dave Jones:** And they've also got a rubber insulating mat in there which is very nice. Just so you know, no sharp bits from the metalwork or anything can actually protrude through the wrapping and pierce the windings and things like that and also lowering its electrical isolation.

**Dave Jones:** So, yeah, they've done it fairly well. And there's a bit of attention to detail there. They put some Loctite on the screws holding down the only component on this thing that moves which is the fan and causes vibration.

**Dave Jones:** So, excellent, but I don't see any rubber you know, isolating vibration isolating washers in there. So, I don't know. I have I haven't never haven't turned this thing on.

**Dave Jones:** So, I don't know if it's like a you know, temperature controlled fan. I assume it is. And I'm sorry to say LELON brand caps don't cut the mustard. Really?

**Dave Jones:** Come on. I mean, you know, a quality power supply that costs 500 bucks has one job, and that's to use high-quality caps and provide, you know, a long-life linear power supply.

**Dave Jones:** Lelon, they're not the worst out there, but they're not a Panasonic. They're not a Nippon Chemi-Con. They're not a Nichicon, you know, like Uh, come on. They could have spent, you know, I don't a dollar or two more for, you know, really top-quality caps.

**Dave Jones:** So, that's pretty disappointing. But, they are 105°C rated, so that's okay. LSM, I presume that's the model. I'm not going to look up the data sheet for them. And, they do have the separate mains earth wire going off to the earth terminal on the front panel.

**Dave Jones:** That goes over to the PCB. Yes, they've got a split washer on there, so that goes over pretty much provides a very low impedance path through the earth terminal, and that's what you want.

**Dave Jones:** So, they've done that decently. They haven't skimped. And, if you can see down in there, they are doing temperature sensing on the heat sink. Geez, they've gobbled that up, but there we go.

**Dave Jones:** There's a little thermistor right down there, bang on the heat sink. So, they've got thermal overload protection. Nice. But, you'd expect that. Now, I'm actually not that impressed with the mains wiring here.

**Dave Jones:** Why? Like, they've cable tied it together. And, you might think, "Okay, that's all okay. They've put some you know, Loctite type thing on the connector, so they can't wear loose and stuff like that." But, the fact is, you're It's right up against the laser-cut edge on this metal chassis.

**Dave Jones:** And, that's I can feel that. That's a little bit burry. Tiny burrs, but nonetheless, you can probably see, actually, some of the scrape marks on the edge of the wire there.

**Dave Jones:** You can you see that? You should be able to see that. So, that's what's caused by, you know, the laser-cut edge. So, that's the, you know, like I would have put a big uh you know, insulating sleeve right over the whole bundle there, but they haven't done that and that's just tucked down in the side like that.

**Dave Jones:** So, it's just not safe practice. I don't like it. It's you know, it it's they're probably going to get away with it, but you know, in a quality supply, you don't want to get away with it.

**Dave Jones:** You want to do it properly and that really should have a big insulating sleeve over it. Bummer. And behold the famous Siglent rust. Look on there uh lay I I presume it's like laser cut edge here and we've seen issues with rust in Siglent gear uh before, so yeah, not doesn't instill a lot of confidence, does it?

**Dave Jones:** If you've been watching my teardowns for a long time, you would know I'm not a big fan of just TO220s flapping around in the breeze there and that's what they've got.

**Dave Jones:** Look, it's just you know, stand free standing off the board like that. I don't like it from a vibrational uh point of view, especially um in this orientation when it's not uh vertical, when it's horizontal like that.

**Dave Jones:** If this thing's mounted on a you know, mounted on a trolley out in uh some production environment or something, I've seen TO220s like that actually snap off just through vibration in a couple of months.

**Dave Jones:** I you know, once again, they're probably going to get away with it, but it just shows a lack of attention to detail in that. They probably, you know, maybe they ran out of space on the board, but it it's not I don't I just don't like it.

**Dave Jones:** It gives me the heebie-jeebies. One interesting thing here is the uh ethernet and USB board. Uh here's the ethernet connector down here and you'll notice that the receiver is not, you know, the driver's not on that board.

**Dave Jones:** They're actually going through this uh unshielded uh cable here, this multiway cable and yeah, they've got a nice sleeve on it and everything and And goes all the way over all the way with LBJ, all the way over to the front panel, where our transceive our ethernet transceiver is down there.

**Dave Jones:** So, yeah, see, there's our output transformers. So, once again, you know, they're getting away with that. I mean, you know, like these are not proper twisted pairs either like you'd get on a proper ethernet cable.

**Dave Jones:** So, if you wanted to do that really professionally, you'd actually put an ethernet connector on the back here, and then you'd actually have a proper ethernet cable running over to another a matching ethernet connector on the back here, then you plug it in, and then, you know, you'd have another one coming out, and you know, I don't know, maybe I'm being a bit nitpicky.

**Dave Jones:** You notice that on this heatsink here we've actually got There's our bridge rectifier, okay, input bridge rectifier, but we've got two power transistors on this one, whereas the one on the other side we've only got a single power transistor.

**Dave Jones:** There it is, down in there. Why is that the case? Well, this is a triple output power supply. So, clearly they're running the 5-V output here or this switchable.

**Dave Jones:** It's not adjustable, it's switchable, so that's has its positive and negative points. Anyway, they're running that one from this secondary heatsink over this side. So, in theory, in theory, this the power output from here is coupled into the heatsink, for example, I'm going to assume it's channel one here, so that in theory you'll get less maximum power output from channel one than you would from channel two, but the

**Dave Jones:** specs are the same, but that heatsink will actually heat up more than the other one for this one. But, as long as you design that in, there's no problem with that.

**Dave Jones:** I'm just pointing it out. And sorry that I'm not going to take this whole thing apart. I don't really want to go to that sort of effort, so it's a bit bit dodgy on some of the camera angles here.

**Dave Jones:** Anyway, this tap on the transformer, the yellow wires, that's clearly the tap for the third channel output and there's our full wave bridge rectifier for the uses individual diodes for that third channel.

**Dave Jones:** So, they're not putting those on the heat sink cuz that doesn't have the same power output requirement as channels one and two. So, no problems there. They can get away with that fine and dandy.

**Dave Jones:** By the way, our mains input board, no real problems there. There's no fusing on this board cuz that's a part of the IEC input connector on the back panel where it's fused.

**Dave Jones:** They've got the isolation slots in there. You know, there's no You don't need common mode chokes and things like that for such a linear power supply. So, yeah, that's all part of the course.

**Dave Jones:** No problems at at all. And I said a big thumping power switch. Nice. And they've got some PTCs in there. Very nice. Just for this looks like an auxiliary winding coming from the transformer.

**Dave Jones:** You can see a tiny little bridge discrete bridge rectifier there. So, you know, that's not too shabby at all. All right, if you're a bit disappointed about the input capacitors, well, check out the output capacitors.

**Dave Jones:** These are Rubycons. There you go. So, that's a Rubycon are a decent brand capacitor. So, they're at least done Why they've, you know, used Rubycons on the output and they can't use Rubycons or, you know, some better brand on the input?

**Dave Jones:** I don't know. But then they've mixed those up with Lelons here. Once again, you know, these Taiwanese brand and Lelon are okay. Um kind of sort of, but yeah, it's just like why are they mixing those in?

**Dave Jones:** You know, like they're using Rubycon output caps. Well, why not make everything else Rubycon? Don't get it. And for those processor aficionados playing along at home, I know you're out there.

**Dave Jones:** We've got an STM processor. So, fairly grunty. So, this is probably running some, you know, light Linux OS or something in a power supply. Yeah, it's like But okay, whatever.

**Dave Jones:** But you know, they've got Ethernet or PC control, blah blah networking, the whole jazz. It's got a graphical, you know, display and interface and graphing and all that sort of stuff.

**Dave Jones:** So, you know, you kind of sort of have to go a bit, you know, a high-level OS there. There's not not much not a huge amount of choice really.

**Dave Jones:** So, that's fine. And they do have PC mini mount fuses directly soldered on, you know, lead axial leaded ones soldered onto the board down there. So, they're actually doing that a few times Well, they've got one for each channel basically and they've got some on the front, too.

**Dave Jones:** And they're doing that on the front panel as well right there. So, once again, another resettable fuse there, PTC there, and a couple of more TO220s just flapping around in the breeze.

**Dave Jones:** Actually, sorry, silly me. I stand corrected. These Rubicon caps here aren't actually for the output. These are These look like filtering for the main power supply for all the electronics and stuff like that.

**Dave Jones:** Of course, the minimum output capacitors because, you know, in an adjust like a adjustable current power supply, you want the output capacitors to be absolutely minimum possible. So, there's the third channel, for example, which is the fixed voltage output.

**Dave Jones:** Well, that one doesn't Yeah, that one would have a current limit, I think. I don't know. I haven't actually tried it. Anyway, um small amount of output but once again, that one is a Rubicon.

**Dave Jones:** But there's an output for channel two and these are not Rubicon caps. So, these are Lelons. So, yeah, there you go. They've actually got a fair bit of output capacitance there.

**Dave Jones:** You'll notice that the the reverse protection diode there is straight across the output, pretty beefy. They've got that also down here on the third channel as well. So, that's common as mud.

**Dave Jones:** And there you go, you can just see our output current shunt resistors there. I don't know whether they're high side or low side, but yeah, they got two of them.

**Dave Jones:** Have they whacked those in parallel? Not entirely sure, but yeah, this is a precision power supply as I said 1 mV 1 mA resolution, which is quite, you know, very impressive on a 30 V 3 A output capable supply.

**Dave Jones:** So, there's going to be a reasonably high-end ADC in there somewhere. Is it one of those puppies? I don't think the arm STM processor has a high enough resolution ADC even if it has one.

**Dave Jones:** And this is where the magic and the performance comes from an analog devices ADR 7792. This is actually pretty decent little beast. It's a three-channel 16-bit sigma-delta converter. It's got a built-in 4 ppm voltage reference.

**Dave Jones:** It's got built-in differential amplifiers and all sorts of jazz. And they've also got a ADR03. That's a pretty reasonably schmick 3 ppm 2.5 V voltage reference as well. So, they've got some decent hardware in here.

**Dave Jones:** So, I don't doubt that it actually meets its specs and performance targets and accuracy and stuff like that. So, yeah, thumbs up there. And they've got a whole bunch of sharp PC817 opto couplers there.

**Dave Jones:** That's to isolate all the data required. Nice. There's one thing I don't see around the processor here, and that's a JTAG header. Is that the puppy up there populated?

**Dave Jones:** Perhaps. And there's all our relays in there to do the switching for our series and parallel functionality on the front where you can join the outputs and get, you know, double the uh so you don't have to physically wire them.

**Dave Jones:** You can And then the uh voltage will track and things like that. So, that's nice, but they Yeah, they're not exactly name brand relays. They use the same ones over here and well, I Yeah, offhand I don't know who makes those, but eh, whatever.

**Dave Jones:** And in case you don't know how linear uh power supplies work, when you've got a 30-V uh 3-A output uh range, okay, that's a lot of power. And if you're got your voltage output set to uh 1 V for example, and you've got a 30-V input, you know, you've got to drop 30 V at 3 A.

**Dave Jones:** That's a huge amount of power, you know, uh dissipated in your uh output uh power transistor here and your heatsink. So, if you've Depends on the voltage range, they're actually going to switch in uh different taps on the transformer.

**Dave Jones:** So, you know, they might have like a you know, a 8-V tap for your low voltage. So, if you set your output voltage to 5 V, it might switch it to say the 8-V uh AC tap.

**Dave Jones:** And you don't nearly dissipate as much power in your uh output power transistor or your and your uh heatsink there. So, you know, when you go up to 12-V output, they might choose a you know, a 17-V tap or something like that.

**Dave Jones:** And when you go to full 30-V output, when you set that, uh they might switch in 30-V AC uh tap or something like that. And for those playing along at home, the switching transistor is an IRFP150N MOSFET.

**Dave Jones:** And now I remember where I've seen very similar construction here with the uh heatsinks. It's a Yeah, almost uh identical arrangement except for the toroid uh transformer here had a linear supply.

**Dave Jones:** I'll link in uh my ATEN power supply teardown. That was a horrible Oh, that was awful power supply both in terms of functionality. It was awful to use and the construction quality was pretty terrible as well.

**Dave Jones:** This Siglent's actually, you know, it's it's quite reasonable. Um it's definitely streets ahead of the um ATEN uh supply, which was absolutely horrible. It it used a linear transformer, but curiously the ATN uh one had actually it it was a precision power supply as well, but had lots of horrible problems.

**Dave Jones:** But it it actually had on the heat sinks some thermal cutouts. It actually had thermal mechanical cutouts on there. I mean, you know, Siglent you don't have to have those.

**Dave Jones:** I guess it's just a cheaper and simpler way of doing it. Siglent are doing it electronically here. They've got you know, a temperature sensor directly on there and then they can electronically uh shut the thing down.

**Dave Jones:** So that's, you know, technically that's actually better. But you know, if your sensing element fails or whatever, you know, uh so those mechanical thermal cutouts, you know, really old school kind of thing.

**Dave Jones:** But the ATN one actually used Nippon Chemi-Con capacitors. Go figure. And that one was really built down to a price and really shoddily uh constructed. So the Siglent is uh much better in that respect.

**Dave Jones:** So overall, I've got to give it a pass. It's not too bad. Like, you know, but there's just a few little niggly things in there. And you know, as I said, I would have preferred some better quality uh parts in there, but it is reasonably neat construction.

**Dave Jones:** It's I do believe it's going to meet uh its performance. It's got the ADC and the reference in there. It's doing the business. And all of the sensing everything's on the uh front panel PCB down here.

**Dave Jones:** So we don't have to dick around with that. If you've I'll have to link in the Rigol uh DP832 uh power supply tear down and it actually had many quite a few design issues in terms of uh sensing the voltage and things like that.

**Dave Jones:** So uh it it actually used discrete wiring through to the front panel. Whereas this actually is, you know, been quite neat. They've actually put a bit of thought into uh you know, mounting it all on the one uh front panel board like that.

**Dave Jones:** So that's not too shabby. And they've soldered plastic things down. And you know, it it it's certainly certainly a pass. So you know, decent quality uh toroidal uh transformer in the thing and just let down by a few smaller touches, but uh generally I'm I guess I'm fairly happy with that.

**Dave Jones:** All right, so let's power this puppy up and uh maybe we can put a load on it and uh check out its uh thermal uh performance perhaps. So, here we go.

**Dave Jones:** Uh booting straight into it. Look at that. Nice display on it. Love it. And that fan is actually going, but I'll tell you what, uh with no load on this thing, it is practically silent.

**Dave Jones:** So, it's got to have uh temperature control. I expect the the fan to really uh increase when we uh fully load this thing down. And there's some annoying user interface things like this.

**Dave Jones:** I have to do a separate video on using this thing, but look, you turn the voltage up. Voltage setting over range. Why tell me that? Why flash that up?

**Dave Jones:** It's just stupid. Just stop at 32 V. Like just stop there. I know it's not going to get you. I don't need to be warned. Give me a break.

**Dave Jones:** Oh, I'll tell you what, I'm switching this voltage all the way through the range. I cannot hear these relays switch. I cannot hear the range switching. At all. I swear I've put my uh ear right up to it.

**Dave Jones:** Can't hear a thing. And as I said, go to plug these uh banana plugs in here, it they really feel loosey-goosey. Doesn't instill a lot of confidence in me at all.

**Dave Jones:** I mean, look, I've just got, you know, my resistor load on there and you'll notice that the current's flapping around in the breeze. If I actually look, put force on those beans those banana plugs so that they're doing that.

**Dave Jones:** Look, I get a you know, perfectly nice stable current. I leave them loosey-goosey and it's not making good contact. Anyway, you'll notice that when I change this I I actually had that set to 4 V there.

**Dave Jones:** If I have it set to 5, you'll notice that it actually Oh, well, it doesn't do it there. Let's go to four. It'll actually change between So, when you're turning the knob, it'll be the set voltage, okay?

**Dave Jones:** But then, once you're a second later after you release it, it'll be actually the physical output voltage, which is fine. That's I like that. But the thing is like they've got this huge display, right?

**Dave Jones:** All of this display to their advantage, but they waste all this space with this stupid timer thing. Most of the time you're not going to use the timer, okay?

**Dave Jones:** So, get rid of it until you need it, and then have, you know, set voltage, set current, and then display, you know, maybe even a tiny a tiny font up here, you know, set voltage, set current, and then have your big displayed, you know, your actual output voltage and your actual output current and your actual output power.

**Dave Jones:** You know, like I It's a power supply. You want to know this information. You want to know what you set it to. Now, in terms of thermals on this thing, I'm actually shorting the outputs uh just running the thing at uh full pelt at the moment, but I'm having a look at the front panel here, and uh this is as I said, these two big filter caps, there's a bridge rectifier tucked

**Dave Jones:** away in there. It's got its own fuse. That's for the electronics, I believe, and that bridge rectifier in there, check it out, 90-odd I'm getting a peak of like over 90° for that bridge rectifier.

**Dave Jones:** Sorry about the glare there. Wow. That's not That's not terrific at all. That doesn't instill a lot of confidence in me. And what I'm doing is I'm running uh both outputs here.

**Dave Jones:** I'm sort of like uh shorting them out, and uh I ran them up to 32 volts, but I Once again, I still don't know. Without actually getting in there and start measuring stuff, probing around and around, I don't know where the actual voltage taps are, because usually you'd put it like at at worst possible tap.

**Dave Jones:** So, I could actually put it down to say 1 V on uh uh both channels here and then uh that, you know, that might be near enough to sort of worst case um worst case power dissipation cuz it's got to drop almost the full uh whatever transformer tap voltage um down to our 1 V output and then we shorten the thing on the output.

**Dave Jones:** So, yeah, um let's give it a whirl. So, this is actually really kind of hard to get, but uh if you have a look in there, like um sorry about the uh like the transformer is uh not um black anodized, so it's not going to be an accurate uh temperature.

**Dave Jones:** So, it's going to show up cool, but let's look at our silicon down there. That's our output uh transistor. That's the hottest and I was getting a peak of just over 100.

**Dave Jones:** Yeah, there we go, 100. 100° on the uh power transistor. So, that's that's pushing it, but that is worst case. It's still within margin, but yeah, uh and yes, by the way, at uh full tilt, yes, the fan does uh come on.

**Dave Jones:** It's yeah, it's noticeably loud, but hey, that's par for the course on these types of power supplies. Okay, I'm finally able to get the transformer taps on this thing.

**Dave Jones:** It you know, the output has to be on before it will switch the transformer taps. So, let's go down here and clunk. Once you get to 8 V, it and it switched back down from 7.

**Dave Jones:** There we go. So, that's the first tap. And then 16 down to 15 24 22. So, 23 24 and that's it. There you go, three taps. Okay, so what I'm going to do now is use my famous power supply killer here, the BK Precision 8500 electronic load that I have managed to kill a production power supply with before.

**Dave Jones:** When you set it to constant resistance, you can actually get this thing to oscillate between constant voltage and constant current mode. So, I've got it set to 8 volts, which is like the minimum of the tap.

**Dave Jones:** Okay, so of the next tap, so it's actually um Uh so, we switch to the next tap. So, this will be dissipating the most about amount of voltage across the output power transistor.

**Dave Jones:** I've got my resistance set to 1 ohm here, and we'll give it a whirl. Listen to that. There we go. It's pretty horrific. It's pretty horrific. I don't see any magic smoke escaping.

**Dave Jones:** And it's switching the input range current as well the transformer tap as well. I wouldn't like to leave that going all day, every day. I think it will eventually die, but yeah, let's turn that off, and it's started working again.

**Dave Jones:** And we can go back to say 1 amp constant constant current, for example. And switch that on. Ah, sorry. Yeah, our Yeah, sorry. I had already adjusted the current here.

**Dave Jones:** So, I've got to go in here and up the current. There we go. 1 amp. Yep. It's working a treat. And I switched it to like the 19-V range, and it's even more violent now.

**Dave Jones:** Wow, it's really not liking that. But, hey, it's surviving. Nothing's dying, so beauty. And I went out for a bit, came back. Look at this. By default, it looks like it has a bloody screen saver.

**Dave Jones:** Why? This is just insanity. It's a bloody power I assume I push that to get it back. It's a bloody power supply. Just leave the display there. Unbelievable. So, there you have it.

**Dave Jones:** I hope you enjoyed the uh little quick look inside the Siglent SPD3300X series uh precision programmable DC power supply. And I'll have to do a follow-up video of this, of course, actually playing around with it.

**Dave Jones:** Maybe a uh shoot-out comparison with the uh Rigol DP832, perhaps. So, yeah. Well, stick around for that, even though I haven't planned to shoot it yet, but maybe I will.

**Dave Jones:** Anyway, if you liked it, uh please comment on the video, give it a thumbs up, and all that sort of jazz. Discuss it on the forum, you know, follow me on Twitter, and buy my merch, and all that.

**Dave Jones:** Subscribe, and all that stuff I've got to say as a YouTuber to, you know, stay in business. Catch you next time.
