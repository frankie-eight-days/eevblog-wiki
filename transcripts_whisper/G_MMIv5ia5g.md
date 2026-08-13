---
video_id: G_MMIv5ia5g
title: EEVblog #814 - Keysight N8762A 600V 5100W PSU Teardown
url: https://www.youtube.com/watch?v=G_MMIv5ia5g
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 20, "2": 45, "3": 61, "4": 76, "5": 94, "6": 112, "7": 130, "8": 156, "9": 172, "10": 191, "11": 209, "12": 236, "13": 260, "14": 275, "15": 290, "16": 311, "17": 330, "18": 344, "19": 362, "20": 379, "21": 398, "22": 421, "23": 432, "24": 448, "25": 464, "26": 486, "27": 505, "28": 521, "29": 537, "30": 559, "31": 580, "32": 594, "33": 610, "34": 622, "35": 638, "36": 656, "37": 670, "38": 684, "39": 698, "40": 712, "41": 726, "42": 746, "43": 762, "44": 778, "45": 794, "46": 808, "47": 824, "48": 838, "49": 854, "50": 870, "51": 886, "52": 902, "53": 920, "54": 938, "55": 954, "56": 974, "57": 992, "58": 1006, "59": 1020, "60": 1034, "61": 1046, "62": 1060, "63": 1074, "64": 1088, "65": 1108, "66": 1124, "67": 1140, "68": 1158, "69": 1178, "70": 1198, "71": 1218, "72": 1238, "73": 1254, "74": 1266, "75": 1286, "76": 1306, "77": 1320, "78": 1342, "79": 1356, "80": 1374, "81": 1392, "82": 1408, "83": 1430, "84": 1448, "85": 1462, "86": 1478, "87": 1490, "88": 1512, "89": 1530, "90": 1544, "91": 1560, "92": 1576, "93": 1594, "94": 1610, "95": 1630, "96": 1650, "97": 1664, "98": 1682, "99": 1698, "100": 1710, "101": 1722, "102": 1736, "103": 1752, "104": 1770, "105": 1788, "106": 1806, "107": 1830, "108": 1848, "109": 1860, "110": 1880, "111": 1898, "112": 1912, "113": 1928, "114": 1940, "115": 1956, "116": 1972}
---

**Dave Jones:** Hi, welcome to a teardown and potentially a, well, maybe the first part of a repair video. Check out what we've got. We've got an Agilent, sorry, it has actually Agilent on the front, N8762A system DC power supply, and this thing is a beast!

**Dave Jones:** Check it out! Look! Look at the specs! Woooo! Baby! 600 volts, 8.5 amps, 5100 watts. Wow! In a two rack unit high thing. This thing is an absolute beast. I got it courtesy of Charles at Trio Test and Measure, and he got this from a customer.

**Dave Jones:** They blew the arse out of it. They released the magic smoke and they were going to toss it in the dumpster, I believe. So Charles saved it and he said, here, we can have a look at it, have a teardown and maybe have a repair of this thing, if we can anyway.

**Dave Jones:** So, let's take a look inside. Oh, it's a bobby dazzler! Look at it! I mean, voltage and current, like a lot of these system power supplies are just that. They're designed to go into racks into systems which are under PC control and things like that.

**Dave Jones:** But this puppy has the rotor encoders on the front for the voltage and current control as well, and limiting and all sorts of stuff on the front. Very handy for control. I hate the system power supplies that don't have any front panel indicators at all.

**Dave Jones:** It's just annoying. Grrr. And this particular series of system DC supplies comes in many different models, of course, as is common for these type of things. Anywhere from an 8 volt unit with 400 amps capability up to the highest voltage model we've got here,

**Dave Jones:** 600 volts at 8.5 amps, 5100 watts. And yes, 5100 watts is more than your average PowerPoint can supply. So 240 volt or 110 volt, you know, 2400 watts here in Australia is the maximum. This one's 5100, so yes, it is three-phase. And the specs are incredible too.

**Dave Jones:** This is a 0.025% basic DC voltage class instrument, 0.1% on current. Absolutely incredible for such a high-voltage, high-current unit. Tell us the price, son. Well, this particular model, 7700 Australian dollars ticket price. Crikey! And on the back here, we've got good old, old-school GPIB, we've got 10100 Ethernet LAN,

**Dave Jones:** we've got USB host, we've got inactive, whatever that is, out in, I don't know, some sort of control thing, maybe. We've got a cap on here, that's the remote programming interface. We've got some dip switches to set some various things, we've got the sense lines.

**Dave Jones:** Yes, you've got to, at these sort of currents, you've got to have four terminal remote sensing. And here's our voltage output. There's a big-ass terminal block there, and there's actually two connections for the positive and two connections for the negative. So if you want the sense line, if you want to sense it at the load, then you've got to take it from here.

**Dave Jones:** But as you can see, as is quite common, if you're just using it basic without any sense, then you just put in loopback pins in there to do local sense feedback. And here's the trick and why it released the magic smoke. Here's the three-phase inputs, right?

**Dave Jones:** So you've got L1, L2, L3, plus your earth terminal, OK, no problem. Standard three-phase input, 190 to 240 volts. OK, yep, it's designed for the Australian market. Look, up here, 190, 240 volts AC, 3 kilowatts plus, no worries. Right? Wah, wrong! This one's actually a 120 volt US model, because we're talking three-phase,

**Dave Jones:** and in a Y arrangement, that can be 208 volts, or it can be 240 volts, depending on the particular configuration, per phase, for a 120 volt, you know, nominal country. Like in the US, there are various standards, and I won't go into them, you know,

**Dave Jones:** it depends on what type of factory and installation and what type of three-phase system, how it's wired, et cetera, et cetera. We won't go into it, but basically, no, you could be fooled into thinking this is a 240 volt unit, and you can hook it up in a country like Australia,

**Dave Jones:** which is a 240 volt country, and you can hook it up to our three-phase system here, but wah, you can't. Here, it's actually 400 volts for a three-phase system, typically. So that's exactly what they did here. I don't know where they got this thing from, I don't know the history,

**Dave Jones:** but Charles tells me that, sure enough, they actually hooked this puppy up to a local three-phase system here, and the magic smoke escaped. Awesome! Let's take a look inside. So, let that be a lesson to you on three-phase systems. Know exactly what you're doing, don't be fooled by labels like this.

**Dave Jones:** But yes, even though I don't have three-phase here in the lab, I could actually technically hook this up to a regular 240 volt outlet. I could, you know, there's no reason why I can't feed my single-phase 240 volts into and parallel it on all three inputs like that.

**Dave Jones:** It's just that I wouldn't get the available power, of course, I wouldn't get the full 5800 watts that this puppy is capable of, but, you know, hey, it still allows me to troubleshoot and do everything else. Actually, technically, I would not do that here in the lab,

**Dave Jones:** because my lab voltage here is actually 245 volts at the power point. And, actually, I'll prove that. And there you go, I'm actually pretty close to 247, so that's really quite almost the extreme limit of what they're allowed to actually give us here.

**Dave Jones:** So, yeah, not necessarily such a good thing. So, even though it's only 7 volts over the nominal upper rate of limited 240 volts here, and it'd probably work, you know, I'd be incredibly surprised if it was an issue. Still, just as a matter of course, you wouldn't do it.

**Dave Jones:** So I would use my, in troubleshooting this thing, I would use my adjustable mains power supply. So here we go, let's pop the lid on this puppy, and this thing is going to be first class. I can guarantee it. They will have spared no expense on the parts,

**Dave Jones:** and the construction will likely be absolutely drop-dead gorgeous. Let's hope Agilent don't let us down. Sorry, Keysight does have Agilent badge on the front, though, sorry. Ta-da! Oh, yeah, baby, look at that. That is gorgeous. Wow. And even though this puppy has been powered off for a long time,

**Dave Jones:** and I'm sure it's got bleeder resistors in there, not to store any residual charge on the caps, you know, when you're mucking around with something like this, you just want to check first. So I'll get in here to this lovely looking bus bar,

**Dave Jones:** and I'll give that a probe, and yeah, bugger all. And then you can go probe the main side. But it's all discharged. You just want to make sure this whole thing is discharged, both the secondary high voltage DC side, and the primary side over here,

**Dave Jones:** all discharged before you go poking around in here. And just remember, if you want to discharge some things, if you've got a multimeter with, ta-da, one of those low Z things, then, well, that'll do the business. It'll put a resistor in series, in parallel with the,

**Dave Jones:** series, double, parallel with the cap, and it will discharge it. So, and it'll display the voltage as it discharges. Beauty. Now, first thing I'm going to do is give it an old sniff test. No, I can't smell anything really burnt. So, yeah, and visually, at first glance,

**Dave Jones:** I don't see anything wrong with this thing. Oh, I can see, yep, down here, well, it's not actually something wrong that's blowing up, but two of the fuses for, two of the phases here are missing. These are, well, these are, two of the phases here are missing.

**Dave Jones:** These are, look, 30 amp, whoa, big beast, HRC ones too, 30 amps, 250 volt rated fuse, they're missing. So, I don't know whether or not somebody's, you know, had a go at this thing, or whether or not the fuses just blew out. I mean, look, there's something,

**Dave Jones:** something happened there, perhaps. That's, yes, actually. You see, on the side of these caps here, look at all that. Look at this crud, I mean, this is a very clean unit. This crud is not anywhere else, it's not dust or anything like that.

**Dave Jones:** So, it looks like, you know, this fuse here is likely, like, totally exploded, and, yeah, all the crap, and it's just, yeah. It's not charred everywhere, but it's, yeah, I don't know, has the ceramic exploded? I don't know, but, I mean, HRC fuses are supposed to take

**Dave Jones:** huge surge currents like that. So, I'm surprised I can't immediately see anything else visually blowing in this thing. That's funny looking. Check out that. They've got some, um, silicon stuff on one side of this, um, of this cap here. Are you kidding me?

**Dave Jones:** Like, why? No, it hasn't, like, oozed out of the bottom of something. I'm actually, can see this, actually, quite a few places around in here, actually gluing components together. But why they've just stuck it on the side of there, I've got no idea.

**Dave Jones:** Because they haven't done that to these ones down here, so, go figure. And just look inside this thing, isn't it gorgeous? All separate ball construction. Here's the mains input here, it's gonna have, um, it's actually got, there's a big clunking switch on the front,

**Dave Jones:** but it's just going down to there, so it looks like we might have some relay switching to actually, uh, turn that off and on, even though it's got a big clunking switch. It doesn't seem to be, um, it's certainly not switching the three-phase, uh,

**Dave Jones:** the actual mains input, so it's doing that electronically. Um, and we've got, I'll show you inside in a minute, we've got three big-ass bridge rectifiers here, so see, three separate fuses. Uh, we've got some caps, we've got our common-mode chokes here, so we've got a three-phase common-mode

**Dave Jones:** choke arrangement. We've got our three bridge rectifiers here, and I assume, are these big-ass relays? That looks like a little transformer, but we'll have to, uh, get some numbers off those puppies. Anyway, um, it's got, uh, power factor correction as well, so it's going to be doing some power factor correction.

**Dave Jones:** Is that down on this board here? Um, and then these are our two big output boards. Even though this is only a single output, it's obviously getting, like, there's, this is like the highest power model available. So they're obviously paralleling two of them.

**Dave Jones:** And you can see that on the busbar arrangement here. These are the two outputs here of the supply, these two here. See, I can touch that because I've already measured it. Um, the two outputs here and the two outputs here, these are identical

**Dave Jones:** power supplies, they just put them in parallel with these huge busbars. And then these busbars, it's quite nice, they come up into this top board here. You'll notice they've removed some of the solder mask to increase the current handling capability of the copper on there, but that's

**Dave Jones:** probably, you know, a two-ounce copper board anyway. Um, and just go into the output terminals here. Ooh, nice little spark gap in there. Let me show you. There we go, it's always nice to see a little spark gap arrangement like that. I've done a video

**Dave Jones:** actually arcing these across and it's really cool, I'll link it in if I remember. And no wonder this thing is gorgeous. Well, it'd be gorgeous anyway because Agilent slash Keysight know how to design products and they design really good ones but the best in the business

**Dave Jones:** has done this, TDK Lambda. Well, one of the best, if not potentially the best power supply manufacturer in the world. So it looks like Keysight have subcontracted TDK Lambda. No surprise. I mean, you know, leave it up to the experts to do these sort of things and they

**Dave Jones:** would have charged a pretty penny too, let me tell you. So it looks like every power supply board in here is TDK Lambda. This one is, this one, this one, and your two main power supply outputs as well. So it looks like Keysight have subcontracted

**Dave Jones:** out. That probably, maybe this output board here might be you know, custom Keysight and maybe, you know, the digital side of things. I mean, you know, that wouldn't be TDK Lambda, that would be all Agilent. So they've got GPIB board here and processor

**Dave Jones:** and it looks like a control board down the bottom. And it looks like someone in production has written some stuff on here after testing. What is that, P200 5k? So is that maybe 5 kilowatts they tested this puppy at, at 200 volts maybe?

**Dave Jones:** So yeah, they've written those on top of the heat sinks after they've done some production stress testing on this. Sorry for the handheld footage, but it's the easiest way to get this. Yeah, here's one of the relays on the main power supply input, Tyco

**Dave Jones:** relay. I'm not going to look up that number, but it certainly is. And there's two of those relays in there. That one and that one. And as I thought, this one is a transformer, so that's doing some, you know, tapping off a signal for

**Dave Jones:** cents or something like that. Now one thing I'm a bit disappointed at, just from a service and teardown troubleshooting point of view, is that you know, yeah, they've labelled all the connectors, you know CM1 and everything else, but like why can't they just label them, like

**Dave Jones:** with their system function? Like, you know 5 volt rail, 15 volt rail, whatever. You know, like actually be more descriptive on the connector outputs. But you know, there's nothing like that on here. There's no test point voltages or anything like that. So you know, it's not exactly service

**Dave Jones:** friendly, and I can't I had a quick look, but I cannot find the service or service manual or schematic for this thing. So if anyone has it, please leave it in the comments because that would be absolutely fascinating. We'd be able to tell a lot more without

**Dave Jones:** having to reverse engineer all this jazz. But yeah, what I think, yeah, we've got our input mains input switch in here. This looks like our, as I said the power factor correction. That's important when you're talking about these sort of loads, or your professional

**Dave Jones:** power supply's going to have PFC in it. It looks like we've got another power supply board over here, which looks like it does the low voltage rails for your digital and stuff like that, and our secondaries. Actually this PFC board here has the older NEMIC lander

**Dave Jones:** name on it. And that's the same as the mains input as well, but the low voltage DC supply has TDK lambda as do the two main power output ones as well. They're also TDK lambda. So yeah, maybe a different group within lambda. Lambda, lambda, lambda?

**Dave Jones:** The tri-lambs. Yeah, 80's aficionados will get that one. And of course you expect nothing less than Nippon Chemicon. There you go, the real deal. 105 degrees C of course. So of course these are all Nippon Chemicon, all the major ones in the DC power supply and the

**Dave Jones:** input, the output side and the input side as well. And they've put that grey celastic in between those to stop them flapping around in the breeze. Don't want them vibrating. Nothing worse than vibrating capacitors. Really annoying. So those caps are the output side of course.

**Dave Jones:** They are of course 450 volts. So this is a 600 volt capable supply, so they're going to have those puppies in series. So they'd be two in series and then two in parallel like that. So two groups in parallel. The output diodes here, they've got eight of those on

**Dave Jones:** this directly tied to the busbar output. See, because they've got no insulating washer, no sill pad on the back of that, so they've got, yeah, four on one side, four on the other, feeding the direct rail which goes right out there, right to the busbar.

**Dave Jones:** Very nice. And then there's our primary side switching transistors. We've got four of them down in there, they'd be big ass MOSFETs, big sill pad on the back of that. Don't need too much heat sinking on there. This is a pretty efficient design, but as you can see

**Dave Jones:** they've got the fans right here, so they drive in the air directly over these, the heat sinks are oriented in the correct orientation, except it sort of would have been nice to put this in the path of the fan here instead of like just slightly

**Dave Jones:** outside the path of it there. Would have been nice to get that air going over the fins, but eh, you know, they've done their homework, they've done their testing, and that's adequate. So that's a small, so yeah, air being sucked in the front and pushed right out the back

**Dave Jones:** directly across all of these. It would have been a real faux pas if they mounted the heat sink like that orientation, and then just blocking all the air. That's a trap for young players, that one. And you can see that they've done this

**Dave Jones:** absolutely perfectly designed up on the power factor correction board up here. They've got the fan here, it's sucking the air in from the front, blowing straight over the capacitors first, so it's keeping those really cool, and then the two heat sinks are aligned

**Dave Jones:** in the correct orientation so that the air can flow over the fins and straight out. So all, so it's you know, if you had it the other way so that these capacitors were on you know, over here like this, then you'd be blowing

**Dave Jones:** the hot air onto the capacitors and that's not good for their lives. So you want these caps on the cool side of the heat sink and your airflow like that. Nicely designed. And they've got themselves a little temperature sensor there right on the heat sink.

**Dave Jones:** That's very nice, that's a token brand NEC owned those I think, or vice versa, I don't know. Anyway, it's a little NEC token temperature sensor. Very nice, directly sensing the primary side output heat sink. And you can see here that the secondary side

**Dave Jones:** in addition to the four other diodes on the other side of the busbar here, there's addition for another four in there. So that'd be for a higher current model. And I think you can see down there, there's a jumper in one position there.

**Dave Jones:** And that would be to configure these output capacitors in series or parallel combination for, once again, for the different voltage current models. So lower voltage model they might whack all these, and higher current, they would whack all of these four capacitors in parallel.

**Dave Jones:** Whereas the higher voltage one like this is 600 volt one, they would actually whack them well, as I believe, I think they are two in parallel, two in parallel and then that group in series with that group to get your higher voltage. And they probably have

**Dave Jones:** a ballast resistor on there, I'd be guessing, just to equalize the voltage across the two of those. Well, looky what we have here. There we go. There's where our magic smoke escaped from. Looks like we have is that a MOF? We've had the arse blown out of that one.

**Dave Jones:** Only one of them. Only one, so yeah. That's interesting. That looks like the only visible visibly damaged component in this thing. You can see where it's just blasted. Look, it's blasted right out here and just spewed all its guts right against this heatsink.

**Dave Jones:** So yeah, that's the first thing you need to fix. And that puppy is actually a Nippon Chemicon MOF. That's 470 volt nominal rating, hence the 471k there. That's a dead giveaway. And this one's a 30 joule job, so it's a bit beefy, but yeah.

**Dave Jones:** Obviously, because you plugged in 400 volts AC in here, when you rectify that, oopsie! Now just looking at the failure mode here, we know where you put 400 volts per phase onto this puppy, so when you full wave bridge rectify that, of course, you're going to convert it to

**Dave Jones:** DC, multiply that by 1.41 times, and it's going to jump over here via these big jumper cables I didn't show. It's going to jump over to this power factor correction circuit, and, you know, so like we've got a little MOF down here which is blown on this side, but

**Dave Jones:** it's only for the low energy stuff going over to this secondary one. So yeah, so that's not like a main MOF. I don't think it looks like it. Might have to get the board out to check the wiring, but it doesn't look like it.

**Dave Jones:** That doesn't look like it's, you know, huge directly in the path, but it's still there and a blue. But anyway, you know, you would suspect something on here. I mean your DC filter caps, we've only got 400 volt caps, 420 volt rated caps there on our

**Dave Jones:** main DC rectified output of this thing, so because we're basically full wave rectifying the mains input. So that is not high enough rating to cater for the 400 volts per phase that we got here, but there looks to be no stress damage to those caps, but, you know,

**Dave Jones:** like, yeah, I wouldn't probably fix this thing without replacing those and putting it back into our production environment or something like that perhaps. But anyway, there's no physical stress on those. It doesn't look to be any physical stress on any other parts in here.

**Dave Jones:** None of the four transistors in here have any blowholes or signs of physical stress, but yeah, we don't necessarily know that. But visually, the only thing I can find is that MOV. Now in theory because the main output of these DC caps, if it stressed these ones

**Dave Jones:** then it's going to stress these ones up here as well on the input. Because there, we've got our wires coming here they go straight over to the input. They've got the same caps here over here. So they're effectively in parallel but they're like doing some local

**Dave Jones:** bulk storage down here for the channel. So, you know, these ones could have been stressed as well, but yeah, I can't see anything at all. But after that, I mean, I wouldn't expect anything on the secondary side over here to be blown. So if anything's going to be

**Dave Jones:** blown, it's the primary side over here and all this power factor correction stuff in here. So who knows, we might have got lucky and the fuses here and the MOVs actually protected, or MOV singular, well the others would have kicked in as well, but they didn't have their arse blown out of them so

**Dave Jones:** all the energy was directed to that middle one by the looks of it. But yeah, they could have taken out the fuses quick smart before before the energy could build up in these caps here and damage anything else. That's what you'd be hoping anyway.

**Dave Jones:** This puppy's interesting, check it out, little transformer there that's got this big arse, like secondary winding here with like a coiled, well a wrapped, like sense wire around that, just going on the secondary side there. It's got four pins, but it doesn't look like there's any coil

**Dave Jones:** on the second side there, only on the primary side here. And they've got a similar sort of thing happening there on the output board. Look at that. That puppy is just flapping around in the breeze there. Not sure why they've done that. And they've popped the main

**Dave Jones:** output board here, you can have a look at it, look at these big arse. Once again, the same Nippon Chemicon, the same series. These are big 450 volt caps, and they've whacked these in series, because this is a 600 volt power supply. You can see they've actually circled

**Dave Jones:** 600 volt model here, and these four resistors here, these would be the balancer resistors that ensure that the voltage is shared equally between these two caps here. I mean, you know, you can actually rely on the caps to self-balance, but, you know, using the internal ESR,

**Dave Jones:** but, you know, that's a bit how you're doing. So, you know, you can see that they've done it properly and put in the proper balancer resistors, and they've even got them, look, stood off from the board there. Lots of air spacing under there, no wuckers.

**Dave Jones:** Got ourselves four sets of suppression caps here, and they're elastic together, no worries whatsoever. And that's it. That looks like a common mode choke, it's not very impressive, it's only got a single turn on each side there. But anyway, that common mode choke is actually

**Dave Jones:** here. So that's what they've got, the spark gaps across the common mode choke there. Now this is really interesting, check this out. There's a big-ass bridge rectifier here on the output board. Now is it actually doing any bridge rectification? Well, let's follow the money

**Dave Jones:** and see what we're doing. This is the positive pin here, okay, the two middle ones you can see, they're the AC input, and the negative pin is over here. Let's take a look at this positive pin. The positive pin here is connected to this terminal here, which

**Dave Jones:** is, I've actually traced out, this is actually the negative output terminal, okay? So the negative output terminal to the positive pin of the bridge rectifier, look at these two AC input pins, they're going nowhere! They're flapping around in the breeze and I've actually confirmed, on the

**Dave Jones:** top you may not be able to see that, but I've confirmed that those pins actually go nowhere, okay? So they're completely isolated, and then the negative terminal of the bridge rectifier is going to, over to here, to our negative output, right over here

**Dave Jones:** to our negative output terminal here. What's going on? Let's go to Davecad. So what they're doing here, here's the negative output terminal on the back, and they're actually basically putting two series diodes like this in, and then two of those in parallel, because these AC terminals here are

**Dave Jones:** just floating, okay? They're not connected to anything, so you've basically got two diodes in series, two in series, and then those in parallel going down to the negative terminal of your power supply output. So, yeah! All of the output current is flowing through this diode bridge.

**Dave Jones:** Why are they doing that? In the negative line like that? I don't know, some sort of sense thing? Reverse protection somehow? And it doesn't actually make sense until you have a look at the second part here, which looks like another 4-terminal bridge rectifier, but it's not.

**Dave Jones:** It's actually a high-value 4-terminal current shunt resistor. Aha! Let's go back to Davecad. And bingo! Our sense resistor is in parallel with the diode bridge here. So this is our output current sense resistor they're doing low-side current sensing. It's 4-terminal, of course, to get the accuracy, because this thing's

**Dave Jones:** like 0.1% accurate on the current over the full range, I believe. So yeah, so that's going these two, this sense terminal's going off to a connector, which is then going back down to the board, and they're measuring that with a diff amp. It's not on this output board, it's

**Dave Jones:** actually back on the main board, so that's a bit how you do it, almost. I don't like that. I like having my differential sensor, my diff amp, right there. You know, you don't want to go through cables. Anyway, they've done their homework, they know what they're doing.

**Dave Jones:** So this big-ass bridge rectifier is basically protecting the current sense resistor here. And you can see that they are actually sensing the output voltage right on the output connectors here. This goes back to a connector here, which is wired back to the main board.

**Dave Jones:** So yeah, you know, they're doing it right at the connector. So they're doing it properly, but of course if you want to sense out the load, because this is, well, this is not a huge current. I mean, it's 8, you know, what is it?

**Dave Jones:** 8 amps or something? Which, you know, a decent amount, but the ones that are like, you know, 400 amps, absolutely crazy. You know, you want to sense at the load. You don't want to drop it across your wires. So you can still do that with this, but at least

**Dave Jones:** they're sensing right on the output terminals. So you know, your voltage on your output terminals is exactly what you're getting. And of course, this is the, as I said, high-voltage 8 amp model for the low-voltage 400 amp model. I mean, they've probably got

**Dave Jones:** different interconnection output board here, different output terminals, the whole work. So, you know, they've still got the busbar arrangement here, but yeah, they're going to have much higher current capability. I mean, this, you know, 8 amps is blah! You know, in the scheme of like, you know,

**Dave Jones:** high-current power suppliers, you know, nothing. It's down in the noise. You know, so you know, there's an output board like this is adequate, but I suspect the other models could be significantly different in their output configuration. And as for this GPIB Ethernet and USB board, well

**Dave Jones:** it looks like a complete kludge here on the top with the, look at this copper shielding, adhesive copper shielding tape here all over the damn thing. So you know, like, did it oopsie, not pass the requirements, and they did that as an afterthought.

**Dave Jones:** And nice cutouts, by the way, on the tantalums there, but yeah. Don't like that at all. And yep, that'd be our GPIB drivers on the back probably. I'm not going to bother looking at the number, but yeah, this'd be an adjuvant job no doubt.

**Dave Jones:** We're not talking TDK anymore. And as for the main processor board under here, well looky what we have here. Old school. We're talking Philips slash NXP 8951! 8051! Woohoo! In a PLCC socket. I'm a bit of a PLCC socket fanboy. Always loved them.

**Dave Jones:** So you've got to think, you know, how old is this design? What does it date back to? I don't know the previous generations of this system power supply, but yeah, it's probably not fairly recent. Probably not even this century. You'll notice there you go, the little model number

**Dave Jones:** ID, 600 volts circled, as I said, from 8-volt models up to 600. So that's not just a matter of a firmware change, otherwise they probably wouldn't bother having that on the board. They'd just whack a sticker on the chip or something like that.

**Dave Jones:** By the way, that micro is 64k of flash. Fancy-pantsy 8051, let me tell you. But yeah, so they've obviously got some hardware changes in terms of voltage dividers and ADC ranges and stuff like that. Voltage sensing stuff. So it's going to be significantly

**Dave Jones:** different between the different models. So there you go. I hope you enjoyed a look inside this Keysight 5100 watt system DC power supply. And well, I know what everyone's thinking. Oh, but you haven't fixed it, Dave. I know I haven't. Sorry, I've already got 40

**Dave Jones:** minutes worth of shot footage on this thing. And it's... what is it? It's now 5.17 on a Friday afternoon. And yeah, I gotta go. So that's it. So I want to get a video out this week because I've been extremely busy. But I'll have to do

**Dave Jones:** a follow-up video with this. Actually I have to take this board out. Have to replace the model or take it out. Don't necessarily have to have to replace it to get it actually working. It's just there in there for protection. So when you're actually...

**Dave Jones:** if you power this thing up under controlled conditions and you know exactly what you're doing, it's fine to actually do it without that. So we don't need a replacement MOV. I'll whack in two lower current fuses down here to protect it. I'll power it up,

**Dave Jones:** feed the same phase into all three channels down here, and look for other visual stuff once I get the board out. Maybe there's some track charring on the bottom of the board perhaps, where there's been overcurrent. But can't see anything on the top, so I don't necessarily expect

**Dave Jones:** anything on the bottom. So yeah, I can't see any other visual signs. Probably need to give it. Maybe somebody's screaming at me, they're watching in HD and they saw something that's blown that I didn't catch by looking at the camcorder screen here. But anyway,

**Dave Jones:** so yeah, maybe we can repair this puppy. Once again, if anyone's got schematics or service manual for this thing, please link it in. So I hope you liked that. If you did, please give it a big thumbs up. Catch you next time. Bye!
