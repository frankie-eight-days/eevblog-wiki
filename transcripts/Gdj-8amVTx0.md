---
video_id: Gdj-8amVTx0
title: EEVblog 1755 - Tolicore Femtoammeter TEARDOWN + REVERSE ENGINEER
url: https://www.youtube.com/watch?v=Gdj-8amVTx0
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 25, "3": 38, "4": 57, "5": 75, "6": 86, "7": 102, "8": 117, "9": 131, "10": 141, "11": 153, "12": 163, "13": 176, "14": 187, "15": 202, "16": 218, "17": 233, "18": 249, "19": 259, "20": 277, "21": 291, "22": 303, "23": 315, "24": 331, "25": 345, "26": 355, "27": 367, "28": 381, "29": 397, "30": 410, "31": 423, "32": 440, "33": 457, "34": 469, "35": 482, "36": 496, "37": 508, "38": 521, "39": 535, "40": 546, "41": 568, "42": 585, "43": 596, "44": 608, "45": 616, "46": 629, "47": 643, "48": 662, "49": 676, "50": 688, "51": 700, "52": 726, "53": 742, "54": 753, "55": 767, "56": 780, "57": 796, "58": 806, "59": 821, "60": 836, "61": 845, "62": 859, "63": 874, "64": 886, "65": 896, "66": 912, "67": 929, "68": 943, "69": 954, "70": 966, "71": 976, "72": 988, "73": 1001, "74": 1015, "75": 1027, "76": 1038, "77": 1055, "78": 1074, "79": 1092, "80": 1107, "81": 1118, "82": 1132, "83": 1142, "84": 1153, "85": 1170, "86": 1181, "87": 1195, "88": 1213, "89": 1228, "90": 1245, "91": 1267, "92": 1279, "93": 1293, "94": 1306, "95": 1331, "96": 1342, "97": 1359, "98": 1369, "99": 1380, "100": 1395, "101": 1411, "102": 1422, "103": 1435, "104": 1457, "105": 1482, "106": 1500, "107": 1519, "108": 1535, "109": 1548, "110": 1559, "111": 1574, "112": 1589, "113": 1608, "114": 1637, "115": 1659, "116": 1692, "117": 1718, "118": 1736, "119": 1746, "120": 1761, "121": 1771, "122": 1789, "123": 1807, "124": 1827, "125": 1845, "126": 1858, "127": 1873, "128": 1890, "129": 1898, "130": 1913, "131": 1922, "132": 1936, "133": 1948, "134": 1965, "135": 1976, "136": 1991, "137": 2015, "138": 2033, "139": 2045, "140": 2059, "141": 2068, "142": 2078, "143": 2090, "144": 2103, "145": 2113, "146": 2124, "147": 2150, "148": 2161, "149": 2173, "150": 2187, "151": 2200, "152": 2212, "153": 2229, "154": 2241, "155": 2252, "156": 2265, "157": 2279, "158": 2289, "159": 2308, "160": 2320, "161": 2332, "162": 2350, "163": 2358, "164": 2366, "165": 2377, "166": 2386, "167": 2399, "168": 2406, "169": 2418, "170": 2432, "171": 2448, "172": 2462, "173": 2470, "174": 2478, "175": 2492, "176": 2505, "177": 2516, "178": 2530, "179": 2540, "180": 2552, "181": 2563, "182": 2575, "183": 2597, "184": 2615, "185": 2625, "186": 2637, "187": 2653, "188": 2664, "189": 2675, "190": 2690, "191": 2702, "192": 2715, "193": 2730, "194": 2745, "195": 2756, "196": 2767, "197": 2780, "198": 2796, "199": 2810, "200": 2818, "201": 2826, "202": 2838, "203": 2848, "204": 2856}
---

**Dave Jones:** Hi, back in video number 1070, which is actually 8 years ago. My god, has it been that long? >> [snorts] >> My god, has it been that long? >> I'll link in the video if you haven't seen it.

**Dave Jones:** It was very popular. The Keithley 617 programmable electrometer, where we entered the world of attoamps. Not picoamps, not femtoamps, but attoamps. And because 20 milliamp range there, okay, 20 milliamps.

**Dave Jones:** Keep going down. Keep going down. Keep going down. Nanoamps? That's for amateurs. Picoamps? No worries. Look at this. This is its lowest range. That's where it's got a two picoamp range.

**Dave Jones:** Move the decimal place three digits across and we've got ourselves femtoamps. So, that's one femtoamp. So, 0.1 femtoamps or 100 attoamps resolution. It's absolutely incredible. We're talking about dozens of electrons per second here, okay?

**Dave Jones:** You can count the damn things. It's ridiculous. But, I can go you one better. We're in for a treat today because TolaTech Corp saw that video and went, "We can do one better than that." Let's take a squeeze.

**Dave Jones:** So, who are TolaTech Corp analytical instrumentation? Well, I got to admit, I'd never heard of them. And basically, they produce this one product. They've also got an optical power meter as well.

**Dave Jones:** But, basically, they specialize in femto detection unmatched. TolaTech Corp. Yes, they make picoammeters, femtoammeters, and we should be able to get a little bit better than we've got on the classic Keithley 617 here.

**Dave Jones:** We can go right down there, but I think this bad boy can actually do better than what they're claiming. Look at the femtoamp sensor. 10 femtoamp steps. 2.5 samples per second.

**Dave Jones:** >> [laughter] >> That's just ridiculous. It can do 38,400 readings per second. It can do 32-bit native resolution. It can also do voltage up measurement as well and measure resistance to teraohms just like the Keithley.

**Dave Jones:** It can do volts, ohms, cool ohms, and amps. So, let's have a look at this bad boy. Thank you very much to TDK for sending this in. Look at it.

**Dave Jones:** We're not worthy. We're not worthy. It's the 3720. There's also the 3710. So, this is the high-end unit here. We've got a USB stick. We've got a little charger, a bloody Yankee thing.

**Dave Jones:** And we've got a USB cable. And that's it. Look at this extruded alloy case. It's beautiful. And we've got a voltage source here, plus minus 12 volts, plus minus 20 milliamps.

**Dave Jones:** We've got a voltmeter. And there's our ammeter input. Yes, it's triaxial. I'm not sure why they didn't provide at least some sort of triaxial cable with it. That would have been nice cuz I don't have one here in the lab.

**Dave Jones:** Because if you've seen the previous video, you'll know that the only way you can do these ridiculously low currents is by having not just a shield, but also the inner guard ring there.

**Dave Jones:** And trust me, if you get any of the big players when you buy their triaxial cables, I've personally paid four digits for triaxial low noise cables before. And it's just painful when you pay four digits for a cable.

**Dave Jones:** Anyway, [laughter] we've got a SD card here, USB, G little GPIO connector. There we go. Look at that. Just in case you want to externally trigger it. No, actually, that's an external trigger input there by the looks of it.

**Dave Jones:** And we've got a power button because this bad boy is battery powered and it's just going to power straight up. Sorry, couldn't focus on my screen there. TDK analytical instrumentation.

**Dave Jones:** Oh, our current is off at the moment. But let's make it read something. Gorgeous resolution screen here. Yes, we do have a login graph as well, and we can adjust the range, but we have to go in cuz by default it's got the current set off.

**Dave Jones:** So we need to go into system, connections here, current in is off. Current in is now on. So we're measuring input current going into the meter. Oh, look at that.

**Dave Jones:** Look at that. And we can run this and you'll see it's got the highest I think it's a 20 milliamp range here, but that noise has actually scaled to plus minus like that's 20 nanoamps there to minus 60 nanoamps.

**Dave Jones:** So yeah, that's ridiculous. Get your confuser out and you can figure out the resolutions. So 20 milliamp range, we've got 2 milliamps, 200 microamps, 20 microamps. Oh, I can hear the relays going.

**Dave Jones:** It's got lots of relays in it. Oh, see it all scale there for the noise and it'll go low and you'll watch that go across and that'll scale for that whoop auto scale again.

**Dave Jones:** You can probably change the auto scale. Haven't played with it that much, but 20 nanoamps, 2 nanoamps, 200 picoamps. Whoa, that would have been like a relay kicking in there.

**Dave Jones:** So, no worries. Whoa, look at that. Check out this bad boy. We've got a 20 picoamp range here. So move our decimal place across three places. This is one femtoamp the resolution that digit there.

**Dave Jones:** Go across to the next digit, that is 100 attoamps resolution like we saw on the Keithley 617, but this one goes an extra digit beyond that to 10 attoamps resolution.

**Dave Jones:** Attoamps. Most engineers do not, when they learn their engineering notation, do not learn what atto is in the prefix in the scale of prefixes cuz it's so rarely used.

**Dave Jones:** A lot of people will never ever deal with femto amps, let alone atto amps. 10 It looks like that's a thing Yeah, it can go up to I'm seeing all the digits there.

**Dave Jones:** So, it looks like 10 atto amps resolution. Unbelievable. And I've just got that input on turn Oh, I I just touched. You can see me just touching the outside ground of that.

**Dave Jones:** And if I apply a physical shock there, look at that. We're We're getting like like atto amps shocks into this thing. That's just crazy. And I can do that on the physical case as well.

**Dave Jones:** Watch this. Look at that. This is ridiculous. Come on. >> [gasps and laughter] >> Atto amps. And then our average there is going beyond atto amps like beyond one atto amp.

**Dave Jones:** This This is nuts. Come on. I swear this video is going to get demonetized for pornography. For reference, one atto amp is about six electrons per second. Six individual electrons per second.

**Dave Jones:** That's just It's crazy. So, what would you use a bit of kit like this for? Well, obviously not just for low power measurement like what what you could Maybe we can like try and measure the you know, power consumption of a little little Casio watch or something like that, right?

**Dave Jones:** An ultra low power device, but it's more for like uh physics research, semiconductor research, you know, radiation uh research, things like that. When you're doing, you know, hardcore physical sciences uh when you know, you might need to measure down in the femto and atto amp region.

**Dave Jones:** And there's only a couple of bits on the of kit on the planet that can do this, and this is one of them. Tell us the price, son. Well, I can't because they just have like a quote-based system.

**Dave Jones:** They might even make them to order. I don't know if they like just a warehouse full of these things sitting around. I doubt it. So, if you have to ask the price, you probably can't afford it, but hey, give them an email.

**Dave Jones:** They'll send you a quote. No worries. You know, so for things like those extreme physics experiments, you know, those photo multiplier tubes you know, using to to count electrons or count photons and stuff like that, right?

**Dave Jones:** Really ultra low, ridiculously low current stuff, then this is where something like this comes into it. Anyway, it's just amazing. Look at the update speed of this thing, and I love the update.

**Dave Jones:** It's a very well-implemented auto ranging bar graph there. Yeah, display zoom. We can actually Well, no. Full scale. Okay, so we zoom. We can go plus minus 200 picoamps full scale there.

**Dave Jones:** Speed is normal, fast, and really, really slow. Don't get an extra digit in there though. It'd be really nice if we could go like full screen on that. Why can't we go full screen on that?

**Dave Jones:** Give me, give me. So, I have not RTFM'd on this thing yet, um but look, so we can do source as well, and we can do looks like a trace point.

**Dave Jones:** Okay, we can do external trigger here, continuous operation, trigger counts 1,000, trigger polarity, level. Looks like we can do automated testing source sequencing here. That's pretty cool. Won't play with that today though, but the source mode, we can do we can do a sweep source mode.

**Dave Jones:** Beautiful. Change the sweep settings. Start, stop, number of points. Fantastic. So, we can click on that, we can choose our current, our voltage, and our resistance. This one won't measure coulombs though, by the looks of it.

**Dave Jones:** Millivolts, let's go down. No, we can only go 200 millivolts full scale range. This is not a nanovoltmeter. And of course, we can stop our sampling at any point, which is cool, stop and start.

**Dave Jones:** I like the user interface on this, I really do. And we can measure teraohms, but the resistance is too high at the moment. So, we've got a two teraohm range, 200 gig, 20 gig.

**Dave Jones:** This is what you can do when you can measure ultra low currents. Oh, 2K. Come on. And it can do the Bluetooths as well as serial and GPIO and memory.

**Dave Jones:** We can plug in memory initialize, so we can looks like we can save our log data to the SD card, presumably in like CSV format. Haven't read the manual.

**Dave Jones:** System errors, none. Details, there you go. Serial number 250,209. I don't think they've made that many. I think that might be 2025. Ooh, it's got self-calibration as well. Source meter self-calibration.

**Dave Jones:** I'm just going to run this. Proceed with meter disconnect all analog cables, place EMC cap on the ammeter. Oh, okay. Well, that's Oh, that is EMC. Not sure if they're talking about this cap or if there's a special shorting plug for the input, perhaps?

**Dave Jones:** I don't know. No, I won't do it. I'm I'm not going to muck around with that. There's something weird going on here though. I've got it plugged in and charging, but it's flashy flashing between like coms.

**Dave Jones:** Maybe I've got the coms turned on and the battery was flashing between 31% before and trust me, it was going between 31% and like 23%. Yeah, 27. There There go, 24.

**Dave Jones:** So, maybe I've got some coms USB coms turned on or something. I don't know. Ooh, look at this. We can have temperature measurement, humidity measurement, pressure. Has it got those built in?

**Dave Jones:** It does. 30.5° C, 33% it's got a humidity sensor in there cuz that is going to matter. Isn't that smart? Because if you've seen my teardown, the Keithley 617 uh or you've read the multi hundreds of pages of the uh Keithley low current measurement handbook, which I'll try and link down below.

**Dave Jones:** Um absolutely fantastic bedtime reading. Um yeah, humidity matters, especially on on your PCB. If you get excess humidity, you get moisture on your PCB, these things all your femtoamps gone right out the window.

**Dave Jones:** Check this out. This is crazy. I've got the USB here, okay? The readings are so crazy sensitive. Look at this. If I just touch this, I it's not connected in in any way.

**Dave Jones:** Watch this. Look at this. We're getting Is that 50 Hz coupling in as I move my hand closer to the unshielded jack. Look at that. Further away, it goes down.

**Dave Jones:** Goes down in amplitude right down to the noise floor. And I can bring my hand in again. That's just capacitive coupling on the input. From this is a 50 Hz crap picked up on here.

**Dave Jones:** That's come on. [laughter] So, what happens if I physically plug in our well No, yeah, there you go. You don't want to be charging at the same time as you're doing your measurement, but there might be some way we can system ground this or something like that.

**Dave Jones:** Or you want to charge it from an external battery pack to not pick up that 50 Hz. So, if I just power that from an external battery pack there you go.

**Dave Jones:** That's not nearly as bad as using that dodgy plug pack that I had. But still, we are picking up a little bit more noise than we were. But of course, when you're doing measurements like this, it's all about your system shielding and your guards and everything else.

**Dave Jones:** You're really going to know what you're doing when you're measuring this low. So, let's feed a current source in. I've got one, the humble LED. Light emitting diode, they don't just emit light when you actually put light into them, they can actually generate current.

**Dave Jones:** And I've done a whole excellent video on this, by the way, on photon counting. So, I'll link that in down below. If you haven't seen it, it's absolutely fantastic.

**Dave Jones:** So, I've just got a junk bin red LED here and we don't care about the specs. And look, look at it go. It's generating 0.2 nanoamps with just my basic overhead lights on here.

**Dave Jones:** If I switch on my light near it, there you go. We've jumped up to 1.1 nanoamps generating from that LED just stuck into the middle there. Didn't didn't want to damage the connector, of course, but it's just stuck in the middle.

**Dave Jones:** It's not expanding the pins and just the internal ground connection there. And if I go near it, we can actually, of course, get more pick up. So, this all comes into the shielding of it because we're down into the nanoamps.

**Dave Jones:** We're not going to muck around with that today, but that's pretty cool and groovy, isn't it? And I've got my torch here, none of that flashlight rubbish. And whoa, we've overloaded.

**Dave Jones:** So, let's go up and nope, 200 nanoamps. Look at that. Look at that. So, we can just go whoop. And this is a pretty powerful torch. So, with a red LED there, we can easily get like half a microamp out of that sucker.

**Dave Jones:** No worries. Ooh, look. I can [laughter] just Just by moving it off axis, I can actually create Look at that. Wow, that's fantastic, isn't it? Just moving it off axis even slower.

**Dave Jones:** And without a proper shielding setup with leads, um I've got my Keithley 2400 source measure unit here. Um I'm down at uh 26 nanoamps or something like that. You can see it's jumping around like a jackrabbit.

**Dave Jones:** And if I go even uh lower, let's go. Let's go down to 1 nanoamp, shall we? And you'll find that unfortunately, um yeah, like we we can get it.

**Dave Jones:** It's measuring it. >> [laughter] >> Maybe we can turn some averaging on or something, but I mean, I've got stuff here that can generate picoamps in the lab. Unfortunately, we're going to need like a proper triaxial cable um setup and everything for that.

**Dave Jones:** So, uh I can't demonstrate that, but trust me, it's going to work. But I've turned on some uh power line averaging and stuff, and we're able to get that down a bit.

**Dave Jones:** Yeah, but if you fart halfway across the room, um it's going to impact this, and we're not even down at like the uh picoamp level. But it's just crazy that we can be on the 2 nanoamp range.

**Dave Jones:** Look at the resolution we're getting on that. That's insane. And we [laughter] can't overload the sucker at 200 picoamps. 200 puff. We can go down to 20 picoamps, and oops, oops, we're overloaded, but yeah.

**Dave Jones:** And as far as the burden voltage goes, well, let's do 10 milliamps on its maximum range of 20 milliamps here. And you can see, it's pretty darn spot-on to me my uh Keithley source, and let's measure it.

**Dave Jones:** Hold my tongue at the right angle. About 270 millivolts or thereabouts. But that burden voltage only applies to the 20 milliamp range. On the 2 milliamp range, it's going to be lower.

**Dave Jones:** And then anything less than 2 milliamps, it's going to be like insanely low, like micro like tens of microvolts. So, let's measure the 2 milliamp range here with 1 mA going in, 27 mV.

**Dave Jones:** That's naff all. And let's go down a range, 200 microamps. Oops, something's gone wrong there. There you go. I'm now feeding in 100 microamps, and look at that, 2.7 mV.

**Dave Jones:** Um and but the spec says it's not a comprehensive spec for all ranges. Let me check. Yeah, that's interesting. The spec is 1 mV on the 20-mA range, and then 100 microvolts going down to the 2-mA range, and then like 20 mV on the lower ranges.

**Dave Jones:** So, I'm not quite sure what's going on there. Doesn't quite meet its spec there. But, it's still ridiculously low because it's going to use what's called an electrometer input instead of just a burden voltage resistor that you'd get on you know, in a typical multimeter.

**Dave Jones:** And say the microcurrent for example with an electrometer input circuit, it's an active servo input. So, it actually compensates for the burden voltage. That's why they can get it, you know, [clears throat] practically zero, really.

**Dave Jones:** You know, when you're talking about microvolts burden voltage, it's neither here nor there. So, I'm going to self-calibrate this sucker to see if that nulls out that burden voltage thing.

**Dave Jones:** So, I've got the shorting cap here. And yes, this is actually conductive. Look at that. So, yeah, [laughter] it's not hugely conductive, but it's conductive enough to form a shield on the triaxial input like that.

**Dave Jones:** Cool. And you want it no external power source, you want it powered from the internal battery. And proceed with meter disconnect all analog cables, place EMC cap on ammeter.

**Dave Jones:** Yeah, ammeter input. So, yep, it's definitely going to do that. Make sure the instrument is warmed up. Oh, and go okay. System calibration. Heard the relays go clickety-clack. Oh, yeah.

**Dave Jones:** There you go. ADC offset calibration gain one. It's really cool that it can self-calibrate like this and you want it to like if you like change environments and your humidity change for example, then you'll want it recalibrate this thing before you take a critical measurement.

**Dave Jones:** And that's why they go to the effort and expense to actually build in proper system self-calibration. Current meter offset calibration. There you go. Yeah, it's calibrating the bias current.

**Dave Jones:** Beautiful. Burden voltage again on 10 milliamps. Let's see what we get. Ah, this is tricky. Oh, look at that. 0.3 millivolts now burden voltage. So, yep, it was the calibration.

**Dave Jones:** So, it just hadn't been calibrated since the factory. You can see the huge variation there in like it just the drift and calibration of this thing. So, yeah, it's really important if you're doing critical measurements to calibrate this thing before you take them.

**Dave Jones:** Huge difference in burden voltage. All right, we'll do a quick teardown. Hopefully, I don't do any damage. Tektronix have told me it's a bit tricky, but if you want a more detailed breakdown as I mentioned, I've done a really comprehensive video on that Keithley unit.

**Dave Jones:** So, yeah, anyway let's go. Aha, I assumed this would be an extruded aluminum case. Well, it is, but it's it's two parts. So, let me it's going to be in the slot.

**Dave Jones:** Yeah, it's going to be Ah, there you go. And the battery is replaceable. Very nice. Well, that's not tricky at all. Excellent. Oh, it's a bit trickier if I want to slide the PCB out to see what's on the bottom, but it's a display PCB for you display aficionados, but yeah, nice.

**Dave Jones:** We've got an 18650 just socketed in there. Beautiful. So, you can easily replace that. And warranty void if removed sticker, I think we're going to have to avoid our warranty here.

**Dave Jones:** There's absolutely no chance I'm not going further. Is there any components on the bottom? I'm not sure. I might stick a torch up its clacker. And oh, yeah, yeah, there is.

**Dave Jones:** There's some double-sided load there. I'm not sure it's significant enough to worry about, but all the magic is happening under here and it looks like they do have it on the same PCB, I think.

**Dave Jones:** But Torloco have told me this is not standard FR4 grade PCB material. They definitely needed something special to get the performance out of this thing. Beautiful shielded can. And once I take that off though, no touchies anything in there because the oil from your fingerprints or from anything else, any sort of contamination.

**Dave Jones:** I'll try not to you know, talk to wildly and accidentally spit on the thing, which has happened by the way. I get a tad excited. Oh, we have to do it.

**Dave Jones:** We have to do it. I'm sorry. But one of the world's best what? Precision instruments. We're going to have to avoid the warranty. Oh, look at that. Oh, it's criminal.

**Dave Jones:** It's criminal. Okay, Dave, be careful. Don't spit on it. Get the plastic spudger here. There you go. It's not soldered on. It's just what? There you go. It's coming off.

**Dave Jones:** Don't spit on it, Dave. Don't spit on it. Don't spit on it. Oh, no. It's a separate board. There you go. That makes sense. Oh, look at that. Oh, I see a ceramic hybrid.

**Dave Jones:** I'm going to stand behind the screen here so I don't accidentally salivate all over it. There you go. Look at that. That does look like a special dielectric, doesn't it?

**Dave Jones:** Beautiful. Look, they've removed the old solder mask there. It's all gone. And here you're going to have your very high impedance resistors for your electrometer circuit feedback. And going to have to pull a couple of part numbers on there.

**Dave Jones:** Ooh, I haven't populated the little coax there. So, I assume that is a factory test jobbie. Isn't that wonderful? It's upside down. All the electrons are going to fall out.

**Dave Jones:** Just as an aside, hats off to the PCB engineer here. Look at all the test points labeled for the voltages. Very nice. I'm liking it. That can there is for the voltmeter input.

**Dave Jones:** So, that looks like it's going to be a uh high accurate high resolution high accuracy ADC under there. And this is your voltage source output up the top. And it looks like our biggest baddest high ohms-ki resistor is this beautiful ceramic hybrid there done by Ohmcraft.

**Dave Jones:** That's a very extremely high value resistor. We're talking, you know, maybe 100 gigohms or something. Actually, I'm a bit surprised to not see more Manhattan construction, which is basically off-board point-to-point construction that we saw in the uh Keithley, but um they've engineered this and it looks like that they you know, they've engineered it well enough to do on PCB and there's not even any like slots under the uh components.

**Dave Jones:** They've done well enough on the material that um I guess they've they've deemed that they don't um need any of that. So, yeah, that's interesting. I expected a bit uh a bit more floaty off board construction, but nope, straight on the PCB.

**Dave Jones:** But yeah, you're paying a lot for that PCB material, let me tell you. If I got serial number 22 there, it's reverse engineering time. Let's go. We'll start with of course the the star of the show, which is the electrometer amplifier here, and we've got our input over here.

**Dave Jones:** So you can see that that goes directly soldered down into here. This is our guard terminal, which goes down to this point here, which then goes through this resistor here over to our ADA45 30.

**Dave Jones:** It's hard for you to read, but trust me, we'll have a look at the data sheet in a minute. It's exactly the part I expected here because it is a like a femto amp level input electrometer chip with guard functionality.

**Dave Jones:** And you can see that there's actually two guard pins here, two and seven here, and you can see that the guard is running all the way around here like this.

**Dave Jones:** It's running all the way up here, all the way in the middle of those resistors, and well, it stops there, but it trust me, it actually does continue. They've just got essentially a break in there, and there's a guard all the way around.

**Dave Jones:** Oh. Oh. Oh, my capture's slowing down. What's happened with Drawboard? You can see it, right? There's a guard going. Oh, that's terrible, Muriel. There's a guard going all the way around there like that.

**Dave Jones:** And it's via what's called via fenced or via stitched. You can see that all the way around there. And that via fencing in there, that like all the way around like that, they haven't done it over here, but in the more critical high impedance parts, as we'll talk about in a minute, they have actually done that.

**Dave Jones:** And that's to provide any internal to prevent and help prevent any internal leakage paths through the PCB material itself just like a lateral you know thing going through the PCB material but of course as I mentioned the big problem with like a really cuz this is a ridiculously the input to this amplifier is a ridiculously high impedance as I said femto amps right input impedance this is a crazy high

**Dave Jones:** input circuit so any leakage at all is going to call any leakage on the PCB on the surface of PCB through the PCB as I said you can leave if you touch it with your fingers that leaves oils that can contaminate the board and that could ruin your day so the whole idea of the guard ring here is basically there's a buffer amplifier inside this chip as

**Dave Jones:** we'll look at in a minute and it basically actively drives this guard pin like this to essentially be the same voltage as the input here so that's why there's like almost zero burden voltage because it's actively driven so that and if there's no voltage difference between this between your input and your guard if there's no voltage difference there's no current flow Ohm's law that's how guard traces work so you're actively

**Dave Jones:** driving this guard wire to match the voltage of the input here and that's how you can get actually prevent any leakage effects in your circuit on your PCB you contamination or whatever moisture on your PCB or whatever so I do actually have a Dave CAD here please excuse the crude the model didn't have time to build it to scale or to paint it so this is the ADA4530

**Dave Jones:** we'll have a quick look at that in a minute and you can see like it's got a ridiculously high impedance FET input amplifier in here as I said like femto amps input bias current, but it's also got this guard amplifier in here, which actively just drives the non-inverting input here.

**Dave Jones:** You can use it in either configuration. They just happen to be using it in the inverting configuration here going into the inverting pin like this, but you can put it the other way as well.

**Dave Jones:** But in terms of how the guard works, it all comes out in the wash. The whole idea is to get no voltage difference between your ridiculously high impedance input here and all the way up here and your ground over here.

**Dave Jones:** So, this is our triaxial input here. This is our input. K, I've just mentioned like it's in the killer ohms range. I don't know what the value is, but it's extremely low compared to the feedback resistors over here.

**Dave Jones:** So, in this particular case, we in in the design, they could have actually used the guard terminal to drive it like this, but so this guard buffer here is driving just like these traces over here, which as I as I showed are all like via stitch.

**Dave Jones:** You can imagine those being individual vias like that. Okay, just to prevent any cross contamination in the PCB. And those guard traces go like this under the resistors and the capacitors there and just go around, hence is why it's called a guard ring.

**Dave Jones:** It goes around and isolates all those high impedance circuits. The whole idea is to protect the high impedance node here, which you don't want any leakage from that node going outside, whoop, like that to anywhere else because once you've got a resistor leakage in there, you've got that leakage current.

**Dave Jones:** But if you drive that guard ring at the same voltage as what this node is, you can't get leakage because there's no voltage differential. Basic Ohm's law. And then the actual coax earth here is just connected down to your system earth, you know, your case earth or whatever.

**Dave Jones:** And the reason I put 10k there, I don't know, I haven't measured it. It could be 100k, could be a mega, whatever. Just to show that it's like, you know, probably like like a less than an order of magnitude greater than the value here cuz these would be in the kiloohms region.

**Dave Jones:** So, that's how it basically works. But instead of just having your traditional one like this, they've actually added in an AD 8655 chip and that's just a low noise, you know, pretty schmicko CMOS op-amp, but nothing special.

**Dave Jones:** And then I haven't looked at what's going into the inverting input here, but they're probably driving that with a DAC so that they can do some calibration offset there for the burden voltage would be my guess, but I haven't actually tried that functionality yet.

**Dave Jones:** So, if you see that in the edited in the video, it means I shot that after this. Tricks of the trade. And then we've got crazy high impedance resistors here.

**Dave Jones:** We've got 10 gig, 1 gig, 100 meg, 10 meg, 1 meg, and probably more depending on the ranges or whatever. And if we actually go back to our PCB and we correlate that here, that big ceramic jobby we saw there, that'd be the 10 gig.

**Dave Jones:** How do I know this? Because well, we know this resistor here. A 100 with a four on the end, that means four zeros, that means it's going to be 1 meg.

**Dave Jones:** So, if that resistor's 1 meg, all your ranges go up in decades. So, if that's 1 meg, they'll get progressively higher. This will be 10 meg, this will be 100 meg, this will be 1 gig, and hence this one here, the big ceramic jobby, will be 10 gig.

**Dave Jones:** And it's a big ceramic jobby because it's going to be more stable once you go up in the higher values. They were able to get a 1 gig surface mount here, but you can see how it's much bigger than they they get progressively smaller like that.

**Dave Jones:** They have to physically get bigger like that to get the resistances in there and the actual clearance on the bottom of the device as well, cuz you don't want like a little 402 in there, cuz you you know, if it was a tiny little itty-bitty thing like that, then you'd easily get leakage under there.

**Dave Jones:** So, yeah, you don't want that. And there's nothing special about the relays here. They're a TE jobby, and um yeah, nothing special. And you can see the guard ring actually going through uh the relays like this.

**Dave Jones:** And you can see that uh they're included inside that high impedance uh part of the circuit there. And here's that AD86R-55, which is part of the feedback loop. So, here's our input.

**Dave Jones:** This is going through that K, you know, it's like in the order of kiloohms here, and then that goes into the input, the high impedance input. Then our output, I believe, is pin six here, and that just goes over to uh the non-inverting input of the amplifier, and then you can see that the output here goes through there and around there, and that goes to our They've even conveniently la- labeled it

**Dave Jones:** out. Um that is the output node, which you'll see here. This is the output node here. So, it's really simple. It's an electrometer amplifier with a massive big feedback resistor and practically no like femtoamp input current on the input here.

**Dave Jones:** And if you're curious how they're measuring the humidity in this thing, cuz as I said, the humidity matter if if you've got like a condensation on your PCB, you know, rapid temperature changes, whatever causing, you know, high humidity, you might get condensation, things like that.

**Dave Jones:** You want to be able to measure that. So, so they've got a little itty-bitty teeny-weeny yellow polka dot bikini uh humidity sensor there, U456. And they've got an STM processor doing this.

**Dave Jones:** Um there's nothing else exciting there, really. Oh, by the way, there is some circuitry um on the purple PCB under here, but it's not much, so I'm not sure what's doing there.

**Dave Jones:** I wasn't going to go uh take the board out and touch it and everything uh just so I could see. I don't think it's anything exciting. And as far as our voltage output here goes, they've got an LT 1970.

**Dave Jones:** I think we've looked at this uh part before in a previous video. I can't remember. But it's a basically a power op-amp designed for power supplies. You can actually drive up to 500 uh milliamps.

**Dave Jones:** Um in fact, I'll show you the data sheet. Here it is here. Plus minus 500 uh milliamps. That's right. Right, I just remember this was used in the power supply functionality in the that Australian designed uh Moku:Go um oscilloscope, I think.

**Dave Jones:** That's where we've uh seen this before. So yeah, it's basically a um a power supply. It's basically like an adjustable uh power supply with adjustable current limit and everything.

**Dave Jones:** So it's cool little chip. So if you only need like a small amount of, you know, five you know, half an amp or whatever, it's it's pretty groovy. So they're using that to drive the uh 10-V voltage output.

**Dave Jones:** And by the way, these bypass capacitors here, these are special. Haha. Um yeah, these would be extremely low leakage uh caps here. So um yeah, it looks like they've used like regular ones here cuz as I said, these are like uh your lower This is your you know, one one meg and 10 meg, you know, not a you know, you can get away with sort of, you know, a like a a decent

**Dave Jones:** regular ceramic there. But yeah, these these ones here, real low leakage jobbies. And of course, that output there um not only does it go into the uh feedback there, but that just goes out to the output.

**Dave Jones:** So there must be another way that they're uh contact on the bottom of the PCB board-to-board interconnect they're getting that out cuz there was no coax in mine. And I'm not sure what's um going on here with this um solid This is a solid state uh relay.

**Dave Jones:** I'm not sure why they decided to use one there, but but that's just like ancillary to the basic um electrometer uh measurement system that we've got here. As I said, I just could not get that off and I didn't want to like really force it.

**Dave Jones:** So, anyway, um this is uh the external uh voltage um input here. So, yeah, that's just going to have like a I don't know, a 24-bit ADC in there or something and they're just um shielding that.

**Dave Jones:** So, you know, eh, it's okay, but it's not the main star of the show. And have a look in there, sneaky pants. Look at those, too. Once again, they've got some guard rings here.

**Dave Jones:** So, they're they're doing a similar sort of guard ring functionality in there and these are little um solid-state uh relays here. So, they're like obviously doing us just a couple of range um switching inside uh there, but um yeah, that's just a real high-resolution ADC.

**Dave Jones:** So, here's the star of the show, the ADA4530 femtoamp input bias current electrometer amplifier. This is probably the best chip on the market that you could possibly use for this thing.

**Dave Jones:** The only way you could get better, maybe if you rolled your own with some hand-selected um FETs, input FETs, then um which I think the old Keithley one was doing um in that regard.

**Dave Jones:** But, uh yeah, these days um you wouldn't do that. These are these are pretty schmick. I mean, we're talking about, you know, plus minus 20 femtoamps input bias current and then you can calibrate offset that out and stuff.

**Dave Jones:** So, you know, low offset it's not ridiculously low offset voltage, 50 microamps 50 microvolts is, you know, it's low, but it's not it's it's low enough to have, you know, a crazy low uh burden voltage to enable a crazy low uh burden voltage.

**Dave Jones:** And it's got that integrated guard buffer with a 100-microvolt uh maximum offset. So, that's where your spec uh primarily for your burden voltage is going to come from. 14 nanovolts per root hertz.

**Dave Jones:** I actually specify that 10 kilohertz. That's interesting. Uh and a 2 meg uh gain bandwidth product. Laboratory and analytical instrumentation, spectrophotometers, uh chromatographs, mass spectrometers. This is all the scientific instrumentation words of the day.

**Dave Jones:** Potentiostatic and ampiostatic coulometry. Ooh, coulomb counting, basically, which we've looked at in that previous video that I linked in. So, ooh, you can use them in picoammeters and coulombmeters.

**Dave Jones:** Um yeah, so I don't think this one measures um coulombs, which is interesting. And you can use them as a transimpedance uh amplifier as well as an electrometer. You know, for ion chambers and working electrode measurements.

**Dave Jones:** Once again, all that scientific stuff. If you want to know what these things are used for, I don't know, ask the local ask Doc Brown. Now, because this is a crazy, really ultra-high-end chip, expect to see tons of uh sample uh models and things like that in here.

**Dave Jones:** We won't I won't bore you with the specs, but let's go down. Here we go. These are like, you know, and you can probably uh bin these as well if you wanted better performance.

**Dave Jones:** You can get them, measure them in your own custom test jig, and actually bin them. I'm not sure if Toller Core uh do that, but that's something you can uh certainly do.

**Dave Jones:** That's a thing you do in ultra-high-performance electronic design is you bin parts before you and you hand-select them to put into your uh product. But yeah, like look at all these distribution graphs, right?

**Dave Jones:** So, you know, there's just tons of them. There's There's like a distribution graph for almost every parameter on this thing. You don't get this with your normal op amps and whatnot.

**Dave Jones:** It's just yeah, it's just crazy, right? So, look at them. It's still going. It's still going. They're still going. Like half the data sheet is just It's [laughter] just all this statistical information.

**Dave Jones:** It's just yeah, it's it's crazy, but that's why you you know, you buy you pay a lot for these chips. I don't know the price. I'll try and find it.

**Dave Jones:** The guard amplifier statistical information for the guard amplifier. It's still going. It's still going. Oh, we finally get into the into the theory of operation. And there you have it.

**Dave Jones:** There is the actual input schematic, and it's basically all just FETs, and there's your buffer amplifier there. As I said, it was connected directly to the non-inverting input there, and they've just got the two guard pins.

**Dave Jones:** Just conveniently put them on both sides of the chip, so you can run the guard directly through the chip. That's a layout thing they did deliberately on the chip, and it's got a bunch of input protection, and they would just, you know, they'd be pretty special, too, so there's bugger all leakage in those.

**Dave Jones:** High voltage protection there, however they're doing that. But, yeah, um FETs, that's how you do it. And contrary to what it might look like here, they're actually got a MOSFET input stage.

**Dave Jones:** Don't want to use that JFET rubbish, but yeah. Anyway, extremely low input bias currents, blah blah blah blah blah. The guard amplifier. Anyway, I'll link it in down below.

**Dave Jones:** You can read it for yourself, but let's see if there's anything else in Interesting though, they'll probably have layout information here as well. Hey, you can use it with current sensors, for example.

**Dave Jones:** And of course, they mention the Keithley low low level measurement handbook. We're not worthy, we're not worthy. Yeah, it's it's the Bible of, you know, low measurement, you know, extremely low level measurement design.

**Dave Jones:** So, I'll link that in. It's fantastic bedtime reading. And they show the guard amplifier there that as like an offset voltage circuit, for example. The input resistance, 100 teraohms, is it?

**Dave Jones:** >> [laughter] >> Yeah, and they're showing it there as a guard like that, exactly how I showed it. Dielectric relaxation. You might know it as dielectric absorption, and they just like to use a fancier term.

**Dave Jones:** And of course, this doesn't just apply as it would regularly to capacitors, for example, you know, dielectric absorption, but it will apply to the PCB material as well. This is why you have to select the actual PCB material.

**Dave Jones:** So, let's keep going and see if they've got any more info. High impedance models, humidity effects. There you go, they're talking about humidity effects because that is a huge deal.

**Dave Jones:** Um and then high impedance measurements. Like it's like nice little reference um data sheet, really. This is great. And there's the contamination that we talked about. You don't you know, fingerprints, you know, oils from your fingers.

**Dave Jones:** There's no way you Oh, I just washed my hands. Uh-uh, sorry. No, if you've touched it, then no. All bets are off. And they're talking about the contamination forming like a weak battery and stuff like that.

**Dave Jones:** It can be a big deal. And cleaning and handling. Look at this. Um use uh propyl bromide. Ooh. So, when you get your PCB assembled at the assemblers, they might like put it through a washing uh phase.

**Dave Jones:** This particular board you can't just use your regular wash. You're going to be extremely careful about what what you wash it with or how you wash it that it doesn't uh leave a you know, some sort of residue behind cuz that's just going to ruin all that wonderful Rogers, you know, PCB material, low dielectric absorption PCB material that you've actually uh got.

**Dave Jones:** And so, it's got solder paste selection and what to clean them with and everything. You know, use this to clean it. Otherwise, you're going to come a cropper. So, if you've got it assembled by just some random assembly house in China or whatever and um yeah, they're just going to clean it with whatever regular cleaner that they use and it comes back and you wonder why all

**Dave Jones:** your boards have failed. Ooh, current noise consideration. Boltzmann's constant. All the good stuff. It's all there. So, yeah, you know, all the current noise and things like that. Um wow, they go to town on that.

**Dave Jones:** Oh, there you go. They've got uh recommended uh resistors here. You know, Ohm it ones. Aha, I knew they'd have a layout guideline um guarding um like the actual guard ring on this thing.

**Dave Jones:** So, yeah, like it depends on the implementation. So, they've got different layout recommendations for different um implementations here. And here you go. Um there there it is there it is they're recommending Rogers uh 4350B.

**Dave Jones:** Um from memory that's not the world's best um piece of but we're not, you know, doing like microwave frequencies here. But yeah, you can you want to be using that Rogers where you get your bare board manufactured.

**Dave Jones:** You don't want to get your five boards for 10 bucks at JRLC or whatever. No, you want to specify that I've got that particular Rogers material, the 4350B. Thank you very much.

**Dave Jones:** And there you go. That's showing the um via the guard vias down there like the um yes, there you go. Via fence via fencing. There you go. They mentioned uh that and cables and connectors and wow, like electrostatic interference photodiode interface.

**Dave Jones:** So another application for this would be a photodiode for example and that would that's your classic transimpedance amplifier configuration there just with your feedback resistor like that. Bob's your uncle.

**Dave Jones:** AC error analysis. Wow, this is like a a transimpedance noise gain versus frequency. Oh man, you can go to town here. You can go to Look, you know, that's a big thing as photodiode application.

**Dave Jones:** So yeah, they're really going to town on that. Wow, look at this. Um like in noise budgets and stuff like that. Then we've got power supply recommendations cuz you don't want to ruin your noise your excellent noise performance with a dodgy power supply on there.

**Dave Jones:** Yeah, and temperature hysteresis, long-term drift. Oh my goodness. Temperature hysteresis of your power supply. That could be a factor. And so there you go. So that's a very impressive chip for a very impressive product here.

**Dave Jones:** Thank you very much TIA Corp. This is hugely interesting, isn't it? But yeah, there's there's a lot of art that goes into getting this right. Not only the design, but also the manufacturing of it.

**Dave Jones:** And once again, yeah, you do not touch this board. It's not just the shielding, but it's also the guarding. It's the selection of the PCB materials. It's the via fencing around here.

**Dave Jones:** It's the selection of your feedback capacitors here and the stability and selection of your thing. You got to get a special, you know, 10 gig hybrid uh input resistor here and, you know, it it takes a lot of effort to get this right.

**Dave Jones:** And if you get your confuser out here and uh you go, we said this one is almost certainly a 10 gig and uh if you multiply 10 gig ohms by the 20 pico amps full scale range minimum full scale range of this thing, sure enough you get 0.2 volts.

**Dave Jones:** So, it's like, you know, a 200 millivolt um full scale thing. Unfortunately, this video is way longer than I expected it to be and I didn't even get to play with like half the stuff this thing can do it.

**Dave Jones:** Like it's got Bluetooth and connection and login software and all sorts of stuff and the voltage uh source which can drive at the ADC input and you can measure resistance uh with those.

**Dave Jones:** It doesn't You can't just hook a resistor on the input. You have to like uh configure it. But, you know, it can do um all that sort of stuff which we didn't even look at.

**Dave Jones:** So, very impressive bit of kit. So, thank you very much Tolladay Coffer is sending in that very cool bit of kit. And if you're interested in something, you know, leading edge like this, then yeah, um send them an email.

**Dave Jones:** I'm sure they'll send them a quote. I'm not sure how much stock they have. Maybe if five, 10 units or something like that. Um, but yeah, if you need something like this, you need it.

**Dave Jones:** Um, it's a very impressive bit of kit. Thank you very much Tolladay Coffer. If you liked that video, please give it a big thumbs up. As always, discuss down below.

**Dave Jones:** Catch you next time. Oh, and don't forget to visit the EE blog.store cuz that's what keeps me in business. It's not the YouTube money.
