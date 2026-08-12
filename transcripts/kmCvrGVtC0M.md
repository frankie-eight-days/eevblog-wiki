---
video_id: kmCvrGVtC0M
title: EEVblog #296 - AIM-TTi I-Prober 520 Current Probe Review
url: https://www.youtube.com/watch?v=kmCvrGVtC0M
source: youtube-asr
timestamps: {"0": 0, "1": 10, "2": 20, "3": 38, "4": 54, "5": 63, "6": 75, "7": 95, "8": 109, "9": 121, "10": 131, "11": 150, "12": 161, "13": 172, "14": 183, "15": 203, "16": 215, "17": 227, "18": 256, "19": 281, "20": 305, "21": 314, "22": 333, "23": 359, "24": 376, "25": 392, "26": 419, "27": 427, "28": 440, "29": 452, "30": 465, "31": 479, "32": 497, "33": 504, "34": 530, "35": 552, "36": 568, "37": 581, "38": 610, "39": 629, "40": 643, "41": 653, "42": 665, "43": 676, "44": 684, "45": 695, "46": 711, "47": 721, "48": 731, "49": 742, "50": 755, "51": 765, "52": 776, "53": 789, "54": 800, "55": 824, "56": 849, "57": 862, "58": 886, "59": 899, "60": 911, "61": 920, "62": 928, "63": 942, "64": 954, "65": 968, "66": 985, "67": 1013, "68": 1024, "69": 1042, "70": 1052, "71": 1066, "72": 1078, "73": 1093, "74": 1108, "75": 1120, "76": 1132, "77": 1147, "78": 1161, "79": 1182, "80": 1195, "81": 1208, "82": 1229, "83": 1239, "84": 1253, "85": 1268, "86": 1277, "87": 1291, "88": 1303, "89": 1322, "90": 1335, "91": 1349, "92": 1366, "93": 1392, "94": 1410, "95": 1428, "96": 1443, "97": 1452, "98": 1467, "99": 1481, "100": 1500, "101": 1512, "102": 1530, "103": 1547, "104": 1570, "105": 1582, "106": 1597, "107": 1607, "108": 1627, "109": 1641, "110": 1651, "111": 1659, "112": 1669, "113": 1684, "114": 1697, "115": 1714, "116": 1730, "117": 1749, "118": 1764, "119": 1780, "120": 1796, "121": 1814, "122": 1829, "123": 1837, "124": 1854, "125": 1869, "126": 1887, "127": 1903, "128": 1917, "129": 1927, "130": 1938, "131": 1956, "132": 1973, "133": 1993, "134": 2006, "135": 2021, "136": 2033, "137": 2044, "138": 2059, "139": 2070, "140": 2088, "141": 2102, "142": 2124, "143": 2132, "144": 2144, "145": 2154, "146": 2164, "147": 2179, "148": 2192, "149": 2207, "150": 2219, "151": 2233, "152": 2256, "153": 2265, "154": 2282, "155": 2296, "156": 2304, "157": 2318, "158": 2329, "159": 2352, "160": 2364, "161": 2377, "162": 2395, "163": 2403, "164": 2416, "165": 2421, "166": 2444, "167": 2452, "168": 2463, "169": 2476, "170": 2488, "171": 2503, "172": 2513, "173": 2524, "174": 2540, "175": 2551, "176": 2566, "177": 2574, "178": 2598, "179": 2613, "180": 2622, "181": 2631, "182": 2642, "183": 2657, "184": 2671, "185": 2680, "186": 2699, "187": 2708, "188": 2721, "189": 2735, "190": 2749, "191": 2762}
---

**Dave Jones:** Hi, it's product review time. Bit excited about this one. Been wanting to get one of these little puppies for quite some time and thanks to Dan Evans at sayalig.com, he gave me one of these.

**Dave Jones:** So, thank you very much, Dan. Fantastic. Um, I had to wait quite some time to get one because apparently they're in high demand. So, go figure. We'll talk about that.

**Dave Jones:** What is it? It's the Aim TTI positional current probe. It's pretty much a world first in uh test instrumentation. It's well, it's a current probe, right? It measures current, but allows you to do it um by just probing over the PCB track.

**Dave Jones:** You don't have to actually break into it with a loop of wire and and put your little clamp around it and things like that. You've been able to buy uh current probes for oscilloscopes for well, as long as I've been alive anyway.

**Dave Jones:** So, um but they've all had that one limitation of having a little magnetic clamp you got to put over, put the wire through the clamp in there in order to measure the current.

**Dave Jones:** But these ones, you don't. You just probe the PCB track, you get the waveform on your scope. Brilliant. Does it work? Well, let's find out. Why haven't they done this before?

**Dave Jones:** Why haven't these been on the market, these current probes? It's because it uses a new patented uh technology from I believe at Cambridge University uh in the UK and they're the ones who developed the fluxgate magnetometer in in this thing, which allows um this positional current probing technology.

**Dave Jones:** And I believe the reason these things have been hard to get is because the fluxgate magnetometer used in here is the special patented sensor um is still made by Cambridge or some arm or division or something of Cambridge University.

**Dave Jones:** I could be corrected on that, but apparently um yeah, the supply is limited by how many of these little sensors, patented sensors I can manufacture. Had no luck in finding the patent number or the patent.

**Dave Jones:** So, if you can, please post it in the comments or on the forum and we'll take a look at it. But, what is a fluxgate magnetometer? It's a very simple and very old technology.

**Dave Jones:** It dates back to before the war, I believe. And war, that's not the war on terrorism, kiddies. That's WWII, okay? So, really old technology and it's traditionally used in things like electronic compasses back in the day before they were replaced by more modern technology.

**Dave Jones:** I've worked on a military sonobuoy design which had a fluxgate magnetometer in it. And there's very various ways to physically construct them, but they all work on the same basic principle.

**Dave Jones:** So, let's take a look at it. It's really easy. Basically, what it relies on is a magnetic core like this with a drive winding wound around it like that.

**Dave Jones:** And it's going to be a low saturation material so that the magnetic field generated by the drive signal can saturate this core really easy cuz the core must saturate.

**Dave Jones:** That's a key part of it. And pretty much, what you want to when you design a fluxgate magnetometer, they're designed to detect magnetic fields. That's how they work. So, this black arrow here, this up direction, we'll take that as the reference direction of the magnetic field that we want to measure.

**Dave Jones:** Okay? So, it's just a simple coil of wire around a low saturation core like this. And it basically they the drive signal just goes positive, negative. It'll be a square wave like this.

**Dave Jones:** So, it drives the core into saturation and you can effectively split it down the middle into two halves like this. So, there'll be flowing through that way and there'll be one flowing down like that.

**Dave Jones:** So, you get you put it into two halves and it basically saturates it one way and then the other. And based on your drive signal, so you'll get a saturation waveform, which looks like this for one direction, and if we have our black So that'll be our blue side here and our black side here, will saturate in the opposite direction like that.

**Dave Jones:** Simple. And what use is that? Well, we can use this and a another a secondary sense winding to detect changes, minute changes, in the an external magnetic field. So what you can do, once you've got a core like this being driven, you can actually put a sense winding all the way around the outside of it like that.

**Dave Jones:** There's many different ways you can physically construct these things for the maximum sensitivity, and there's multi-core types, all sorts of things. But this is basically how it's done. We're going to put an external field external sense coil around that, and this will generate a voltage on it based on the flux induced from this drive voltage down here.

**Dave Jones:** But as you can see, they're complementary waveforms. So if this thing is sitting in the middle of space, outer space, and it's got There's no external magnetic field at all.

**Dave Jones:** It's well away from the sun. It's in the interstellar medium or whatever. There's no magnetic field No external magnetic fields around here, then this alternating waveform will precisely, or if you construct it right, should precisely cancel it out, and you'll get no voltage induced in this sense winding.

**Dave Jones:** But as soon as an external magnetic field As soon as this whole coil system, this whole fluxgate magnetometer system is in the presence of an external magnetic field, it will actually adjust the bias point the saturation point slightly of one half or the other and you will get a waveform out of this.

**Dave Jones:** You'll get a voltage out and if it's high, you know, it's a high as constructed properly, it'll be high bandwidth and you'll actually get a signal out of this thing that you can hook up to your oscilloscope and that's basically all there is to a fluxgate magnetometer.

**Dave Jones:** They're actually quite simple but very do quite tricky to actually manufacture and perfect and get them precise absolutely precise and get them and get a high bandwidth like we have in the AIM-TTI I-prober.

**Dave Jones:** So, why hasn't somebody developed one of these before with a fluxgate magnetometer sensor head and you can put it and put it right against the track? Well, if you've got your PCB, it's got to be small enough to actually and close enough to be right within the magnetic field because the magnetic field surrounding a trace on a PCB will roughly drop with a square of the distance.

**Dave Jones:** So, it's not like you can have some big coil up here, you know, an inch away from the board or something like that. It's not going to work. It's got to be right on there.

**Dave Jones:** So, the real innovation here is not that they're using a fluxgate magnetometer to measure a magnetic field on a PCB trace. You've technically been able to do that for you know, forever.

**Dave Jones:** It's to make it small enough and tiny enough to fit right at the tip there. That sensor head, that tiny little sensor head, it's going to have a little toroid or something like that and it's going to have the coils in there.

**Dave Jones:** Probably I don't know if it's just a single drive and a single sense winding. It could be multiple ones. I'm not sure but it's got to be small enough to fit into there And that is the patent, and that's the innovation which has enabled this thing.

**Dave Jones:** Because you've been able to you could use other technologies like a Hall effect sensors to do something like this in theory, but in practice their you know their bandwidth is going to be poor and all sorts of other issues.

**Dave Jones:** So a fluxgate magnetometer is the ideal thing to measure current through a PCB trace without having to break it. It comes in a nice zip bag like this because it's not a really an often used instrument.

**Dave Jones:** So really you want to and it's a bit fragile. So you with you know wires and leads and things. So you want to really probably keep it in a case.

**Dave Jones:** So it's a really nice idea for them to supply it in a case like this. It's got a nice foam padded insert. You could put cutouts in here for other stuff if you wanted to and a a certificate of conformity and we've got ourselves which we'll see later a laminate a nicely laminated reference chart which you're going to need to get an absolute value out of this thing cuz

**Dave Jones:** as you'll see these are great for seeing a waveform but for actually measuring it it's going to be a bit tricky. And you get the instruction manual which is all which is in different languages and it tells you about the practical aspects of quantitative measurements, all that fun stuff, measurement in PCB traces, etc.

**Dave Jones:** etc. Looks like it's good enough. The probe itself of course and it's you know it's got a cable which is about a meter long or thereabouts which goes to the main unit over here which is the calibration box.

**Dave Jones:** It's got a calibrator built in. It's got various modes which we'll take a look at and bandwidth and some knobby adjustments here. And uh, that has a thin BNC output, which goes into your oscilloscope.

**Dave Jones:** There's a, uh, there's a plug pack here with, uh, multiple, um, different, uh, you know, uh, mains adapters for around the world. And we also get ourselves a, um, one of these, uh, traditional, more traditional current clamps, where you can just put it on the end and it, bingo, instead of having the positional thing, it turns it into your traditional, um, uh, current, you know, oscilloscope current probe

**Dave Jones:** system, where you put the wire through. And that will be a lot less sensitive to the position of the probe. So, if you want some, you know, some real easy, uh, absolute measurements, um, and you have a wire available to put through, you're much better off using this SamacSys 300-V CAT II rated.

**Dave Jones:** It's got some really nice finger guards here. I really like these. So, because one of the, uh, uses, one of the primary uses of this is, uh, probing the, uh, traces in, uh, high-voltage, uh, high-energy, high-current switch-mode power supplies.

**Dave Jones:** So, you don't have to break into the trace. You know, you can get through all the circuitry and probe in there. And it's a good distance back, so your fingers aren't going to touch live heat sinks and things like that.

**Dave Jones:** And really, it's going to be hard for your fingers to slip past those probe guards. So, I really like that. And it does, uh, feel really rugged. Um, it's, you know, I've got no problems with it at all.

**Dave Jones:** It's got got good strain relief on the end here. And, uh, the probe itself, um, because it's going to be touching things all the time, hopefully, um, it should wear fairly well.

**Dave Jones:** But it feels really like a solid bit of kit. The first try time I tried to put this on, I was, you know, I thought I'd break it or something like that.

**Dave Jones:** But you got to just use a little bit of force and it just locks in place like that. And there's a little bit of play in there, but, uh, I think that really affects the accuracy much at all.

**Dave Jones:** That sort of locks on there really nice and you just give it a bit of a twist and it comes off. I like it. Good design. And the electronics box here which contains the I I presume the driver or the you know the amplifiers and things like that or the driver might actually be in the head itself.

**Dave Jones:** I'm not sure. By the way, Mike at Mike's Electric Stuff has done a teardown of the probe and the box as well. So I'm not going to do one.

**Dave Jones:** He's already done a good job with that. So I'll link that in here. So if you want to see what's inside these, please check out Mike's video. He's done a good job because it's a bit destructive.

**Dave Jones:** You know, there's lots of there's lots of shielded cans inside this thing and stuff like that. So I don't really want to go you know desoldering hacking mine apart and Mike's already done it.

**Dave Jones:** Anyway, the control box here is it feels quite rugged good quality plastics and uh it's got a 5-V to 5.2 V DC input comes from the plug pack to power the thing.

**Dave Jones:** Why it's 5.2 V instead of 5 V? I've no idea. It's got a calibrator output here which allows you to put the probe down in there and we'll try that out later.

**Dave Jones:** It's got AC DC mode and you can switch it off because if you're doing absolute measurements, very important to calibrate this thing and that's why we have that chart in the box.

**Dave Jones:** Now, it's got three bandwidths. It's got a very low frequency practically DC down here 2-Hz measurement. If you're measuring very low frequency or DC magnetic field, you might want to put on the 2-Hz bandwidth filter.

**Dave Jones:** If you're measuring you know low lowish frequency switch mode power supplies or systems for example working at 10 kHz then you know a 500 kHz bandwidth might do it.

**Dave Jones:** Or it's got the full 5 MHz bandwidth which is quite remarkable for one of these positional current probes. Now, now the frequency of that drive signal to drive the fluxgate magnetometer in the head is probably going to be about an order of magnitude or you're going to want an order of magnitude greater than the bandwidth, the full 5 MHz bandwidth.

**Dave Jones:** So, it's probably driving that coil at, you know, 40, 50 MHz or something like that to get the 5 MHz performance out of this thing and it's that you could say that 5 MHz is probably bandwidth is probably one of the limitations of this thing because it's, you know, if you're if you've got a 1 MHz switch mode power supply, for example, that you're trying to probe,

**Dave Jones:** well, of course it's going to have harmonics which are greater than 5 MHz easily. So, it's a little bit limiting there. But now, there's three modes here. One is wire where you use the clip like this in that wire mode.

**Dave Jones:** So, you put it over there and it's going to be absolutely calibrated should be absolutely calibrated in that mode. And then you've got PCB trace mode which is the really neat mode we're interested in where you put it next to the probe on the printed the trace on the printed circuit board and then it can measure just magnetic fields in the air like it can measure the the Earth's magnetic field or a

**Dave Jones:** magnetic field of a product which is, you know, which which is generating an external magnetic field. And of course, it can detect whether or not you're overloading your amplifier and you're going to be clipping.

**Dave Jones:** So, there you go. That's all there is to the box and look at this beauty made in England. Made in the old dart. You ripper. I love it. Well done Aim-TTi and Thurlby Thandar.

**Dave Jones:** What a weird name that is. And it's got four rubber feet on the bottom. So, it really, you know, it sits on the bench really well and doesn't slide around too much.

**Dave Jones:** Let's give it a go. We'll use it in the PCB trace mode here. So, you're going to set the mode switch to the center there, and then we've got our three controls.

**Dave Jones:** The PCB sensitivity control is effectively the calibration pot because this thing will not be calibrated unless you put this knob to the right position, and you'll do a calibration step first, and that's what we're going to do.

**Dave Jones:** And this is where you now need your calibration uh chart which comes with the unit, and it shows you the characteristic response of this probe system. It's got two different probe responses.

**Dave Jones:** One is 2 amps per volt, and the other is 1 amp per volt, and it shows you the trace the the calibrator output voltage that you want to get versus the trace width which you're trying to measure.

**Dave Jones:** So, the one we're going to measure here first up is 1.6 mm wide trace. So, we will take that 1.6 mm wide up here, and it looks like we need a value of approximately 2.25 V out of our calibrator.

**Dave Jones:** And you'll notice that it's non-linear as the trace width gets smaller. So, right up here, you know, 6 and 1/2 7 mm big fat chunky trace. That trace width is very large compared to the size of the tiny fluxgate magnetometer we've got inside here, but once the size of the the probe in here, the fluxgate magnetometer, becomes a very very significant compared to the size of the trace.

**Dave Jones:** As your trace gets smaller, under about 2 mm there, which is roughly the width of that tip there, then it starts to become non-linear. So, this can't work down to arbitrarily small traces.

**Dave Jones:** So, what I'm going to use first up is one of these this big thick outer trace here, which is 1.6 mm wide on this strip of Veroboard, and that uh should allow us to uh you know, uh see if this thing is um you know, how far it's out in absolute values.

**Dave Jones:** I've got the unit here. I've put it into its calibrator. I've set it to AC over here. And basically um we've got two controllers. You can see our trace rotation.

**Dave Jones:** If I move that, it moves the trace up and down. Uh it effectively doesn't uh matter at the moment cuz all we care about is the peak-to-peak value, in this case the amplitude, not the peak-to-peak cuz you got that little that little overshoot there.

**Dave Jones:** So, just be careful not to include that overshoot. So, you'll see that the peak-to-peak value is actually higher than the amplitude value, which takes the value from the flat part of the waveform.

**Dave Jones:** So, just make sure you don't include that overshoot there. Now, um as I said, we've got a 1.6 mm wide trace. That's what we want to do. So, that from that chart um it said we need a calibration value of 2.25.

**Dave Jones:** So, we need this amplitude to be 2.25. It's quite touchy. And of course, if you wiggle and if you move this thing, if you twist it side to side, it's it's going to be all over the shop because there's effectively a calibration trace in there.

**Dave Jones:** And depending on the amount of pressure you put on it, you only I only have to move that out a fraction, like you know, half a millimeter, and that amplitude begins to drop.

**Dave Jones:** So, it is actually very very very very touchy, if you can see that. So, but the good thing about that is is so you can only undershoot your calibration value.

**Dave Jones:** You can't overshoot. So, you need to just wiggle it around, put pressure on it until it's the absolute max you can get. And we're down to 2.15 there. Can we get it up to 2.25?

**Dave Jones:** Yet, 2.27. There we go. So, I'm going to call that as our calibration value. Bingo. Don't touch this pot anymore. This thing is now calibrated for to give us an absolute value on a 1.6 mm wide PCB trace.

**Dave Jones:** Now, if we have a look at the basic specs in the manual here, you can see it's DC to 5 MHz. That's its basic bandwidth. And one really important one here is the noise or the equivalent in the toroid attachment there is 6 mA RMS for the full bandwidth or 1.5 mA RMS at the minimum 2 Hz bandwidth setting.

**Dave Jones:** So, really, you know, the absolute lowest you can measure with this thing is, you know, 5 mA or above, basically. Only a couple of mA. So, if you're looking to measure microamps with this thing, forget it.

**Dave Jones:** It's just not going to be do it. You're going to be down in the noise. Now, the magnetic field measurement just in free air, it can do 250 microteslas per volt output with plus minus 3% accuracy.

**Dave Jones:** And the maximum field it can measure is plus minus 2.5 mT, which is equivalent to 2,000 A per meter. And using it as a traditional current probe with the toroid attachment there, we're talking plus minus 10 mA to plus minus 10 A with plus minus 5% accuracy.

**Dave Jones:** So, it's not a hugely accurate device with a 1 A nominal 1 A per volt output. Now, what we're going to try and do here is the current measurement in the PCB track.

**Dave Jones:** And it doesn't give you any absolute accuracy figure here because it's going to to be dependent upon your calibration. But because the best case would be in terms of this toroid attachment, you know, you're looking at plus minus 5%.

**Dave Jones:** You see, you can expect the absolute best when you calibrate this thing to be roughly, you know, that 5% figure as well, I would expect. And here you go, it can measure from 0.2 mm to 3.5 mm 1 V per output.

**Dave Jones:** And there are those dual uh characteristic curves we saw on the supplied graph there. All right. Now, what I've got here is I've got my 1.6 mm PCB trace here.

**Dave Jones:** It's the one right down the bottom. Show you a close-up in a minute. And I've got it hooked up to a function generator, 50 ohm output function generator. And my Fluke 87 is showing the AC current here.

**Dave Jones:** And I've got it set to 100.0 mA at 1 kHz is the rough frequency here. And I'll be able to put different waveforms into this thing and see if we can probe it.

**Dave Jones:** Let's give it a go. If we've got 0.1 amps current, then we can expect 0.1 V output from our probe. And in this case, because we're using a Fluke 87 true RMS multimeter, that will be the RMS value, not the peak-to-peak value.

**Dave Jones:** So, we expect to see 100 mV RMS waveform out of this thing as we probe this 1.6 mm trace. Let's see if we Let's see if we get it here.

**Dave Jones:** Now, let's And you can either hold it I've found you can either hold it vertically like that. If I move it side to side like that, you can see the trace once again get smaller or bigger as I move it across the trace.

**Dave Jones:** Now, as I mentioned before, you can get away with You You can't You can only underead with this thing. You can't overread the calibration value. So, you tweak it around until you get to a point where you're getting your maximum amplitude there.

**Dave Jones:** And where the maximum we're able to get there is only It's barely 90 mV really. I I find it doesn't matter too much if I put it vertical or have it down like that, we're only talking There you go, you know, 90 millivolts is sort of the absolute best we can do.

**Dave Jones:** And you'll notice when I rotate it, it will eventually disappear completely because it's got to be the correct orientation. The magnetic field has to go through the um uh fluxgate magnetometer in a certain direction.

**Dave Jones:** So, the rotational aspect of this is just as important as the side-to-side position of the trace like that, which is also just as important as the height. If I lift that just a little bit off, you can see it change dramatically.

**Dave Jones:** But anyway, the best we're getting uh almost 92 there. 92 millivolts, so we're like 10% out. And we calibrated this thing, and I've rechecked, and the calibration is still fine.

**Dave Jones:** So, on that 1.6 mm trace, we're about 10% out. I don't know where the error is, whether or not it's in the unit uh itself, maybe um a slight measurement uh error on the trace.

**Dave Jones:** I just used my uh calipers there. It's probably not exact, be a little bit off, and the chart as well. All that sort of stuff combines to give us roughly a 10% error there.

**Dave Jones:** So, you know, it it's not too bad though. I mean, considering that you can probe a board, a trace with no uh without actually breaking it, then you know, if you can get within a 10% ballpark, it's not too bad.

**Dave Jones:** It's not as good as I expected though. I expected to be able to get maybe 5% or so. Here's a rather interesting uh waveform. I'm picking up the 50 hertz switching from the uh from the Hico here.

**Dave Jones:** And you can see it if I rotate it like that. Look at that, almost goes away to zip if I put it in that flat orientation, but I rotate it 90°.

**Dave Jones:** And move it around the unit. There seems to be a sweet spot, and I still have that on PCB track mode, but we can of course put that over to field mode, and we can actually get an absolute that as an absolute value from that Hico transformer.

**Dave Jones:** And if remember the spec sheet for this thing in the magnetic field measurement mode, it has a output scaling of basically 200 amps per meter per output volt, and we're getting about 10 volts peak-to-peak there.

**Dave Jones:** So, we're talking 2,000 amps per meter magnetic field on the side of that Hico transformer. And that's actually about half of the maximum usable range of this thing. The spec sheet says it can go up to plus minus 2.5 mT or 2,500 microteslas.

**Dave Jones:** Let me change this. I've got that's 10 kHz. Let's jump up to 100 kHz. There we go. So, let's take it up to 1 MHz, and let's have a look at it here.

**Dave Jones:** I've got my sine wave. We've got some averaging eight averages on just to clean up the waveform. Let's switch it to square wave. It's not going to be a perfect square wave, of course, and let's switch it to our triangle wave.

**Dave Jones:** There you go. And we can take that uh take that frequency up, of course. That's actually 10 MHz now. So, it's a well beyond its well beyond its rated bandwidth.

**Dave Jones:** And of course, this thing is uh sensitive to the DC offset as well. That's why we have the um offset trace position. If I adjust the DC offset control on my function gen, I can move this waveform up and down, and you can see it clip there.

**Dave Jones:** So, we can adjust for with the uh trace position control on the unit, we can adjust for any particular um DC offset on our current waveform. Okay, now we'll try it uh in wire mode.

**Dave Jones:** So, we switch the mode switch here all the way over to wire position there, and we snap on our toroid here, and we put our wire through as you would on a traditional current probe.

**Dave Jones:** And as you can see, we're getting uh pretty much uh spot on 100 milliamps uh RMS through this wire. So, we should be able to read 100 millivolts RMS.

**Dave Jones:** There's a bit of noise on that. So, um that's a 1 kHz waveform. So, I'm going to just knock the bandwidth back there, bit of triggering in there we go.

**Dave Jones:** It's cleaned it up a bit. We've got our bandwidth filter on. Now, as you can see, the position of the wire in here does matter. If If you go up and down, there's basically no difference there, pretty much.

**Dave Jones:** But, as it clearly should be close to the head there, you can move it around the outer thing, but you're supposed to put it against the head itself in there.

**Dave Jones:** And once you do that, bingo, we're spot-on to almost spot-on, practically spot-on to what we're measuring with the Fluke. So, that's within Well, it's easily within a percent or so there, and uh it's That's a lot better than the specification.

**Dave Jones:** The specifications are in plus minus 5%. So, it's doing a lot better on that traditional wire measurement. Works really well. And of course, the uh sensitivity control has no effect now because there is no calibration.

**Dave Jones:** It's It doesn't need calibration because the toroid keeps the field in there. So, it it makes no difference whatsoever. I thought it'd be interesting to see how much effect that massive magnetic field from the Heyday transformer has on this current measurement.

**Dave Jones:** When it's out here, it's about, you know, 8 in away or something like that, we're spot-on. We're measuring now 100 mA RMS. Bring it closer. Oh, hey, there's our 50 Hz kicking in.

**Dave Jones:** Now, the specs claim that the adding the toroid attachment actually reduces the effect on external magnetic fields by a factor of five or thereabouts, but obviously when you swamp it with a huge field like that, you're going to pick up something.

**Dave Jones:** Let's switch it off. Bop. Finally, that's perfect. And just a quick DC check at a larger current here. We're getting just under a fraction under 3 amps, and that's exactly what we're measuring with our toroid here.

**Dave Jones:** Spot-on. Pretty much well within the 5% claimed. And can we get that same thing without the toroid with the probe? So, we're looking for around about 3 volts. Once again, you probe around until you get it to its maximum value.

**Dave Jones:** There we go. We've got 2.87, 2.86. Once again, it's reading a little bit low as we got before, but there we go. If we tweak it, we can get reasonably close to our 3 amps anyway.

**Dave Jones:** Now, if you've got a battery supply for this thing, and you've got a multimeter, and you're stuck in the middle of the Outback somewhere, and the sun's not out, and you want to know where north is, not a problem.

**Dave Jones:** All you've got to do is turn this thing around until you find the zero and where which is around about around about there and that is north. Go figure and I can verify that actually is north.

**Dave Jones:** And playing around with this thing, you can really get a gist for just how sensitive it is to the Earth's magnetic field. If I hold it vertical there, we'll see that the face if we rotate it around will be at the zero point pointing north when it gives zero volts.

**Dave Jones:** So, um really this thing is is capable of measuring much lower magnetic fields than the Earth. So, when you're using this thing, you have to be extremely careful to not only you know ensure the thing is like clamped in place next to the thing that you're measuring.

**Dave Jones:** You got to zero it out and then switch it on. And with the small tip, it really is quite capable of measuring very narrow magnetic fields like the distance between windings in a you know a big wire wound inductor or something like that.

**Dave Jones:** And you could also use it to measure magnetic fields escaping from holes and things inside equipment cases and stuff like that. So, it really is quite flexible, but you got to be very careful on how you use it.

**Dave Jones:** You got to know exactly what you're doing. You can't just take a reading at face value because that's just crazy. So, can we actually measure the absolute value of the Earth's magnetic field?

**Dave Jones:** Well, yes, we can if we use this thing correctly. Now, according to an online calculator I used the Earth's magnetic field here in Sydney at the moment should be around about 57 microteslas.

**Dave Jones:** And of course this thing has an output sensitivity of 250 microteslas per volt. So, for 57 microteslas we'd expect around about 228 millivolts on here or point 228 volts.

**Dave Jones:** Let's see if we can get it. We're only going to get that when it's pointing north. Aha, we almost had it by accident there. Let's We won't get it by doing that orientation, but if we shift it like that, 90° directly down like that, we move it around, we can't get that 228 yet.

**Dave Jones:** We're off, but if we point it at the correct angle, the We're going to take the maximum peak value there. There we go. 225, 226, 227, 228, 230. Oh, there we go.

**Dave Jones:** We're pretty darn close, pretty darn spot-on to exactly what we should be getting for the Earth's magnetic field. Awesome. And of course, once again, the calibration control has no effect whatsoever.

**Dave Jones:** I can turn that because we're in an absolute measurement mode. The absolute measurement modes are the field and the wire. It's only when you go into the PCB trace mode, do you need to use the calibrator.

**Dave Jones:** Now, one obvious use for this probe is for tracing currents through ground planes and tracing out shorts and stuff like that. And a little very crude example of that here.

**Dave Jones:** I've got this wire on the back of this board here, which snakes around like that. Straight through to there, and it's actually shielded by all the other traces on there.

**Dave Jones:** But, because this doesn't is looking for a magnetic field in the wire, there's no current flowing through these traces on the top. We'll be able to detect the the signal through this board down here.

**Dave Jones:** So, let's give it a go. You'll notice that as I move it, it I can follow that signal around. If I keep going straight, we're We're to lose it.

**Dave Jones:** Once again, you've got to get the probe on the correct orientation. It's got to be perpendicular to the trace you're actually measuring, but we can see that wire going up there, and we can trace Oh, there we go.

**Dave Jones:** Can trace this thing around. And if you're careful enough, you can actually trace out if you got a texture out, you could actually trace out that exact path. And if you're careful all the way, so I can find shorts, current paths.

**Dave Jones:** You know, if you've got a short going through a chip, through a power rail, internally shorted on a power plane, in inside a multi-layer PCB or something like that, um you should be able to trace it out with this thing because it can find that signal anywhere because it's using the magnetic field of the trace.

**Dave Jones:** Now, what I'm going to do is try and attempt to trace out a real ground current on a PCB like this. And as you can see, there's a split PCB plane in there.

**Dave Jones:** So, I've got my current going in over here, coming out over here, and it's got to go through that tiny little trace down in there. That's the only way that it gets from there through to there.

**Dave Jones:** There's the split ground plane there, so we shouldn't get any current flow around in here. We shouldn't get any current flow in the ground fill down in there. We shouldn't get any current flow down in here.

**Dave Jones:** We should just get the current flowing through there, through that tiny little trace there if you can see it, and down around through to here. All right. Now, let's try and do this.

**Dave Jones:** Now, I'm using a 1 kHz signal here, but it would work as for DC as well, but just remember you've got the Earth's magnetic field as well. So, when you move this thing around, you know, we you we you're going to get an offset shift like that.

**Dave Jones:** So, just be careful, but here we go. There's our reference waveform, and we don't have to worry about the calibration on this pot at all. We can because we we don't care about the magnitude.

**Dave Jones:** We're just tracing currents here on this board. So, you can just, you know, immediately start to use this thing and not worry about it. Now, let's move it over this part of the ground plane, and you'll see we've got absolutely nothing there at all.

**Dave Jones:** We can change the orientation, and we get that offset, but there's no 1 kHz signal. There's nothing flowing through that part the ground plane, but here there most certainly is.

**Dave Jones:** Once again, if we get the wrong orientation, it's going to vanish like that if we hold it vertical, but if we keep the correct orientation according to the magnetic field of how it should flow, then bingo, we still get the waveform.

**Dave Jones:** So, we can see this see the currents going both sides of that hole there. No problems at all. Okay, and it flows through here like this. And once again, it does some of it does flow down around there like that, but the majority of it's going to flow through this top part here.

**Dave Jones:** And it's going to flow up here, and you'll notice that it won't flow down into that little fill, that little void down in there. There is no current flow there at all.

**Dave Jones:** So, there's nothing. So, you can see the current flowing through here, and likewise, there's going to be nothing flowing down here into these parts down here. They're electrically shorted together, but there's no current flow.

**Dave Jones:** And this is a great visualization uh learning tool as well as a real practical uh thing for determining tool for deter practical tool for determining where your currents are flowing in your ground planes.

**Dave Jones:** And there it is flowing down there, and it's look, it's not going down this little bit down here. It's not go you know, there's not much very little down there at all.

**Dave Jones:** Tiny little bit flowing through those two pads there. But, as you can see, it's all going to flow through that trace there, that one tiny little trace which connects the two split ground planes.

**Dave Jones:** And it's going to flow up here and all the way over to there. And look, down here, there's nothing in this little void down here because there's no where for it to flow.

**Dave Jones:** And likewise, all the way over here, down here, there's nothing. There's absolutely nothing. We're getting that offset, of course. And if we zero that out, there's no current flow through any of this stuff down here because that's where it flows, through that bottleneck there, around here, and down into there.

**Dave Jones:** Bingo. And if you watch out Mike's video, he actually attaches a visual aid, like an LED, to the output thing, so the brightness of the LED changes with the amplitude of the waveform.

**Dave Jones:** That's pretty easy to do, and then you'd be able to You wouldn't have to use an oscilloscope, you'd be able to actually visually see it. Or, he hooked it up to a tone generator as well, based on the amplitude of the waveform.

**Dave Jones:** So, you'd be able to get an audible tone as it went across. That's one feature, I guess, this thing is Would guess it would have been nice to have as like an internal buzzer inside here, so you could use the thing as a tone tracer, basically, to trace currents across a PCB.

**Dave Jones:** But, you know, it's designed as a measurement tool, so I guess you could deem that to be a bit crude to have that sort of thing, but it might have been handy.

**Dave Jones:** And you also see in Mike's video how he got a used a long camera exposure with the LED to get a visual map of where the current flows. I I I think I'll bother uh, setting that up.

**Dave Jones:** I haven't got time to do that, but I might experiment with that in the future. But, if you want to check that out, have a look at Mike's video.

**Dave Jones:** But, as you can see, this is a really useful tool for showing where currents flow in a board. It's fantastic. And, like I said, if you've got a a short inside a via or inside a pad in, you know, a multi-layer, like an eight or 10-layer board or something, and they're notoriously difficult to track down.

**Dave Jones:** But, with one of these puppies, you can feed a, you know, you can feed some, uh, you know, a reasonable amount of current through there and trace the thing down.

**Dave Jones:** Beautiful. Love it. And, of course, one of the big uses for this thing is, uh, probing switch-mode power supplies. So, you can, uh, have a look at the switching, uh, waveforms.

**Dave Jones:** So, let's take a look inside this switch-mode power supply here, and we can see the output of the inductor there, and we can measure the switching frequency. There it is.

**Dave Jones:** 40 kHz between those peaks there, and it allows you just to take a look at, without, uh, these waveforms, without having to break into the circuit, which is the traditional method to do it with these current probes.

**Dave Jones:** And, that's often very valuable. And, a lot of the time, you don't need to know the absolute calibrated value. It's just good enough to look at the waveform, and from the shape of the waveform, you can see if your transformer is saturated or something like that.

**Dave Jones:** So, you can figure out what your circuits are doing as you, uh, change things. So, it's really quite neat. You can probe around, and it's quite safe as long as you keep your, you know, your hands away.

**Dave Jones:** You've got your finger guard here, and, uh, you can trace, of course, it's better if you have access to the bottom side of the board with the traces, but we've got a wire actually coming out of here from the transformer.

**Dave Jones:** So, we're able to probe that. No problems at all. So, the iProbe 520 in summary, well, it's a novel bit of kit. I love it. I think it's a really great innovation.

**Dave Jones:** It's got some limitations though. Um, but it pretty much does exactly what it claims. You can now measure current uh without having to break into the circuit cuz that's always been a really annoying.

**Dave Jones:** You have to, you know, break your ground plane or whatever or break your trace, break into it either with a current shunt resistor or with a loop of wire and then you've got to get the oscilloscope current probe in there, one of those clamp ones, really kind of tricky business.

**Dave Jones:** And if you want to measure it at different points in your circuit, it's a pain in the ass. Now, if you just want to look at the waveform, just turn this thing on and probe it.

**Dave Jones:** That's it. Works a treat. But, of course, you saw the limitations on this thing. Uh one, of course, is it's so sensitive that the Earth's magnetic field, depends on the orientation, can cause a an offset, in this case a DC uh offset of, you know, like 250 mV or something like that to which is equivalent to 250 mA.

**Dave Jones:** So, you know, you've got to be really careful with this thing. It's not designed for microamps, it's only designed for milliamps, but it does have a pretty big dynamic range, anywhere from 10 milliamps up to uh a few tens of amps.

**Dave Jones:** So, that's not bad at all. And of course, you can use it as a H field uh probe on its own. It's got the PCB trace mode. It's got the wire mode with the toroid.

**Dave Jones:** It's got various bandwidths. Does everything you want. But, of course, in wire mode, you've got to calibrate the thing and that is a pain in the butt. It's not that accurate.

**Dave Jones:** I was able to get 10% for a quick test. You can probably get a bit better than that, maybe, you know, if you get get a tongue at the right angle on it.

**Dave Jones:** Tweak it a bit. But, for absolute measurements, uh not that great with just the PCB trace mode, but at least you can do it. You haven't been able to do it before, and that's uh, it's um, worth its money just in that respect.

**Dave Jones:** So, few limitations, but a really great bit of kit. And um, if you I I think it's probably one of those things that if you if you have it lying around, you'll probably find more uses for it than what you originally intended.

**Dave Jones:** I can think of lots of instances over the years where I would have loved to have one of these. It would have saved a lot of grief, a lot of time and effort and hacking up my prototype and making it look ugly.

**Dave Jones:** So, yeah, it's really quite nice. The bandwidth isn't huge. It's only 5 MHz, not as good as a proper wide bandwidth current probe. Bit limiting if you're working on, you know, 1 or 2 MHz switching regulators or something like that, but at least you can see waveforms.

**Dave Jones:** Um, it'll be useful for tracing shorts, stuff like that. So, I don't it it does the job. I think it's great. Excellent bit of kit. Thumbs up. I really like it.

**Dave Jones:** Um, within its limitations, if you want to use it. Now, price-wise, um, Saelig have got it for $798 US. Um, so, under 800 bucks US, pick you up one of these.

**Dave Jones:** Not exactly a hobbyist grade thing, but for any well-equipped lab, it's probably worth having cuz there's no other tool on the market like it. So, looks like Aim TTi / Thurlby Thandar, whatever they call themselves, got the whole market to themselves.

**Dave Jones:** It's brilliant. I I recommend if you can afford it, I think every well-heeled lab should have one of these things. They're really cool. It'd be interesting to see if any other manufacturers can uh, come out with a similar type one.

**Dave Jones:** I don't know. It might be locked up in that uh, patent with the special fluxgate magnet miniature fluxgate magnetometer in there. Who knows? But, certainly does the job. Recommended.

**Dave Jones:** Hope you enjoyed it. Catch you next time.
