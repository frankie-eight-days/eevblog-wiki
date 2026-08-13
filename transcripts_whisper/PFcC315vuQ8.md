---
video_id: PFcC315vuQ8
title: EEVblog #533 - LED Fluoro Tube Teardown
url: https://www.youtube.com/watch?v=PFcC315vuQ8
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 26, "2": 36, "3": 51, "4": 71, "5": 86, "6": 96, "7": 111, "8": 131, "9": 141, "10": 161, "11": 176, "12": 196, "13": 221, "14": 236, "15": 256, "16": 271, "17": 291, "18": 306, "19": 321, "20": 341, "21": 356, "22": 381, "23": 396, "24": 416, "25": 436, "26": 456, "27": 471, "28": 496, "29": 516, "30": 531, "31": 551, "32": 571, "33": 591, "34": 611, "35": 626, "36": 651, "37": 666, "38": 691, "39": 711, "40": 731, "41": 746, "42": 766, "43": 786, "44": 801, "45": 816, "46": 831, "47": 851, "48": 871, "49": 891, "50": 911, "51": 926, "52": 946, "53": 971, "54": 986, "55": 1006, "56": 1026, "57": 1046, "58": 1071, "59": 1091, "60": 1111, "61": 1131, "62": 1146, "63": 1166, "64": 1181, "65": 1201, "66": 1221, "67": 1241, "68": 1261, "69": 1281, "70": 1296, "71": 1316, "72": 1331, "73": 1351, "74": 1371, "75": 1391, "76": 1406, "77": 1426, "78": 1441, "79": 1451}
---

**Dave Jones:** Hi. In a previous video, I installed a couple of these German brand Muller lights, made in China. They're a LED T8 fluoro replacement, 18 watts, as you can see, 230 volt, one nominal 1700 lumens at 97 milliamps. They're a 4000K color temperature. And, well, I thought I'd crack one of these things open to see

**Dave Jones:** what's inside. I did measure it, I did know it was the safe type, so it is designed right. If you haven't seen the previous video, I will link it in down below. But anyway, let's crack this sucker open and see what's in it.

**Dave Jones:** I don't think I'm going to be able to reuse it afterwards. I think it is a destructive teardown, I'm afraid. And it's got a diffused tube in it, so you can't actually see the LEDs inside there at all. I mean, there's obviously going to be a PCB in there.

**Dave Jones:** This is the translucent top part where the light comes out, the bottom part under here, no light comes out of there because they're just, there'll be one huge PCB in there, the whole length of this 1.2 meter thing. Anyway, let's crack this sucker open, see what's inside in terms

**Dave Jones:** of the DC to DC constant current drive to drive all these LEDs. Use my dodgy pair of side cutters. You've always got to have just a crap, cheap, one hung low brand pair of side cutters just for sort of mechanical cutting like that.

**Dave Jones:** Doesn't look like the end cap's glued down at all. So, you know, probably, you know, heat welded maybe at a couple of spots on the end or something. I'm not quite sure how they manufacture these things. So I guess we'll find out. You can just get a screwdriver in there and it does snap out.

**Dave Jones:** So it looks like they just snap these end caps on afterwards. Yeah, there we go. They've got the, you can see the ridge around there. And as it turns out, there's a Phillips screw embedded in there, and of course these are a German tube.

**Dave Jones:** They're not made in Germany, they're made in China, but it is a German company. So I thought I'd use my German-weir screwdriver to unscrew that. We're getting close, so it looks like that is totally separate to the LED board in the centre, but no, I thought, see, I thought that was the board going through there,

**Dave Jones:** but it's not. It's just part of the plastic, and it's just like a ridge inside the plastic tube. And I didn't even have to cut this thing at all, I just grabbed it and applied a bit of force and this end just popped off, so there you go.

**Dave Jones:** Eh, did all that medieval cutting for nothing. There is the short, of course, in one end, and that's the proper way to do it, so that it's safe. And I'll link in a previous video with Doug Ford explaining exactly why this is the safe method to do it, and why

**Dave Jones:** some other methods of wiring these things are dangerous, and now are banned in this country. I'm not sure about overseas. And we've got another board with circuitry in the other end as well, and you have a look down there, you can actually see

**Dave Jones:** there's the aluminium tubing that is obviously inside acting as a heat sink. It's not solid, of course, these things are very light, very thin outer wall tubers. Somehow all of this is going to slide out maybe with that entire, well it should be, with the entire heat sink assembly, so

**Dave Jones:** some percussive maintenance could be required. Looks like a little part of the aluminium wraps around the board, just down in there. So, I'm not sure, but anyway, this whole thing is I, you know, when they assemble this, they certainly slide the entire aluminium assembly with the board, so they've got the aluminium heat sink on the back of that board

**Dave Jones:** somehow, you know, thermal, you know, they use some thermal adhesive on the back of that probably to connect the board through to the heat sink there, you know, exposed pads on the bottom of the board of course, solder mask removed, and then they slide the entire thing in.

**Dave Jones:** Found a bit of silicon on the board at the other end, but that's not really holding it. But I've put a big screwdriver in there, tried to bang the whole thing out, and well, it's not budging, so when in doubt, Dremel. There it is, I had to prize it up, so maybe

**Dave Jones:** I might be able to slide it out now, but oh! Man, this is not pretty. We're going to get our board to slide out now, there we go. If I can grab that, ta-da! There it is. It does look like one giant PCB.

**Dave Jones:** So that's rather impressive, but I guess ultimately not hugely surprising given that, you know, this isn't some hack manufacturer making these things on any production line. They're really going to, you know, optimize their production line for this large size board, because normally you

**Dave Jones:** can't get PCB panels this big. So, you know, this is over a meter long PCB, so not every PCB manufacturer in the world is going to be able to A, manufacture that board for you, and then B, you have to find an assembler who can do a one meter

**Dave Jones:** long board. Now a one meter long, usually you can, board can be any length for a pick-and-place machine, and you can go through the pick-and-place machine either in one whole pass if your pick-and-place machine's big enough, or you can just, you know, do it in halves or something like that and move the

**Dave Jones:** board along and then realign it to assemble your, to machine assemble your parts on there, this thing. But yeah, this sucker is a one meter long, over a meter long, I mean this is a nominal 1.2 meter tube, and you can see we've got a couple of strings in there, we've got

**Dave Jones:** one ground trace, the top one there, running completely from one end to the other, and I'll endeavour to show you exactly how many leads, oops, I accidentally ripped off, dragging it through the tube there, accidentally ripped off the pad there for that ground wire.

**Dave Jones:** And here's our main PCB at the mains input end here, there's our X class cap on the input, 0.1 microfarads, looks good, they've got heat-shrunk inductors, it looks like we probably have a fuse in there, nicely heat-shrunk like that, they've got the isolation

**Dave Jones:** slot cut into that so we don't get arcing across the, well, when the fuse blows, presumably the fuse blows, then we don't get extra arcing across there, that's nice attention to detail. You know, it's obviously the subcontractor AD Power who's actually manufacturing this.

**Dave Jones:** Yeah, not much doing on there at all, pretty darn simple. Our cap's 105 degree C rated, no problems there, but I don't think they're quality brands, no, BH, you're not going to find a Panasonic in there or anything like that, so Nichicon or anything like that.

**Dave Jones:** Ah well. Four diodes there, they're probably a full-wave bridge rectifier, so we've got some input filtering, of course, input fuse, and then some extra filtering there, and then our two after the bridge rectifier, so that's generating our high voltage DC, nothing more on there, the control circuitry must be at the other end.

**Dave Jones:** There it is, there's our controller, so basically the board at the mains input end is just generating the high voltage DC, and that comes all the way along the positive in the ground, and the positive trace up there, that's the direct mains rectified DC voltage, coming

**Dave Jones:** to the main controller board at this end, which then controls the strings, and I'll draw a Davecad drawing in a minute of all that, you can still see some of the dremeled plastic on there, blah, horrible stuff. Yeah, once again, BH branded cap, not the best.

**Dave Jones:** And we've got ourselves a compatible NXP SSL 2109T, but this is the SL2109A, I don't know who the manufacturer is for this one, clearly it's a rip-off of the genuine NXP, one probably has, you know, identical pin-out, of course, identical functionality, but they've gone for a cheaper Chinese source one by the looks of it.

**Dave Jones:** This chip's capable of both buck and flyback configurations, and at first thought I thought that was a flyback transformer and that's what they were doing, but a closer examination of what they're doing there seems to be the buck configuration exactly, almost exactly as per the application note

**Dave Jones:** in the NXP data sheet, there's the external MOSFET there, and all the LEDs, the positive part of all the LEDs are all common to the positive part of the supply. So what you'd think is a flyback transformer there, I think they're just using that

**Dave Jones:** as the output inductor there for the buck configuration. This side tap, I'm not sure what that side over there's doing though. If you have a look at the application note circuit for the buck configuration there, it's the buck low ripple one, then as you can see

**Dave Jones:** the LED string over here is commoned up to the positive high voltage rail coming from your mains input, as I said that first board bridge rectifies with that input fuse we saw there, and then feeds the high voltage DC along the board to this board at the other end of it, and I've checked a few things and it does

**Dave Jones:** seem like we've got the exact configuration here with the output, with the main electrolytic output cap here, which is that one up there, and then we've got our inductor L2, which is this winding, this side winding of the core there, we've got our external MOSFET

**Dave Jones:** there we had a look at, and it seems to be exactly, almost exactly the same configuration, but they do have a secondary side, the transformer over there, and I'm not quite sure what they're doing with that. They've got a Zener diode there, some filtering, so that's probably the low voltage supply for

**Dave Jones:** the device, whereas I think the genuine NXP one has the built-in regulator, it can generate its own VCC built-in, it looks like they've just got some stuff in here to generate that externally for this, you know, cheap rip-off brand one, it may not

**Dave Jones:** have that built-in. So this sucker has, you know, pretty much purpose-designed for this sort of application here. 95% efficiency, high power factor, low bomb cost, always important for these consumer stuff, as I said, can do buck boost and flyback modes, single inductor for non-isolated configurations, this can be a non-isolated configuration of course,

**Dave Jones:** because the user can't touch anything inside this sucker, and 5% output current control accuracy, not bad at all. And of course, here it is, for driving strings of lead or high voltage lead modules from a rectified mains supply. Bingo, exactly what you want in these LED replacement fluoros.

**Dave Jones:** And of course, it's just not a dumbass converter, it's got zero current switch-in and valley switch-in as well So it is following the mains input, knows exactly what it's doing. PWM of course, and fast transient response, cycle-by-cycle control, very nice, and tons of internal protection, so really no shortage of

**Dave Jones:** stuff, under-voltage lockout, lead and edge glow, over-current protection, short winding protection, over-temperature protection, well check that, I don't think there's a thermistor on this thing to measure the temperature. Anyway, it's got internal over-temperature protection on the die, but also external output short-circuit protection, really, can't go wrong with these things,

**Dave Jones:** this is what you want. I see, lifetime, easily matches or surpasses the lead lamp lifetime. Of course. Now on the NXP one here, we've got pin 3 is our NTC thermistor there, there it is for measuring external over-temperature protection, but if you look at pin 3, you probably can't see it, but anyway, trust me, pin 3

**Dave Jones:** down on the chip down in here, is going off to this part of the circuitry with the Zener diode, the cap and the diode and the extra winding there, so yeah, once again, probably not because it's a, because it's not, doesn't look to be a genuine NXP

**Dave Jones:** part, it's very close pin compatible, looks like it doesn't have the external temperature, something else doing there. Now, as for the actual lead element used, I'm not sure, I mean, I'm no expert in the field of leads just by looking at them like this, I mean,

**Dave Jones:** you know, you would presume that it's either a Cree or a Lumi leads, they're sort of like the big two manufacturers of leads, just a little Davecad doodle of exactly what configuration they've got on the lead strip here. Basically, they've got four strings of 24 leads in series, so all these, there's

**Dave Jones:** a common one going up there, and then that just goes into twice, they get to the end of 24 there, you can see that, maybe you can see that, but it branches off down in there, and they've just got four of those strings in parallel like that, once again,

**Dave Jones:** like no current sharing resistors in there, so they're pretty much relying on the strings themselves to just equally share the current. May not be entirely equal, but you know, it's going to be good enough for the purpose, really. Roughly four equal currents down

**Dave Jones:** the different strings. As I said towards the start of the video, this board is doesn't look like an aluminium backboard, so it looks like they've just got the copper on the back, and they're probably just thermally bonding that to the extruded aluminium heatsink which goes all the way through this sucker.

**Dave Jones:** I guess it's a dead giveaway that there's no vias on the top to, you know, get a thermal transfer from the top pads down in there, but I guess they've deemed that they don't need it, but anyway, it's only a single-sided PCB, check that out, there's nothing

**Dave Jones:** in there at all, and that board is, it's, in fact I don't, it's not even, it's not even glued to the aluminium backing there, it's just sort of held in place by the tabs which go over the top of the board like that, so they've deemed that they don't need any

**Dave Jones:** heatsinking in this thing. We'd have to know the efficacy of these leads, of course, and exactly what they're going to dissipate and have to go through the thermal calculations. So as a first reaction, I'm quite surprised that they didn't at least have some thermal bonding through to the aluminium backing, so

**Dave Jones:** they're probably just using the aluminium backing as some stiffening, I mean, you're going to get some, you know, radiated heat through, but you're certainly not going to get any conducted thermal heat through to there, so supposedly at least not that bad a, you know, reputable manufacturer, so

**Dave Jones:** I guess they've done their homework on that. So that got me interested, and I did a bit of digging, and it looks like we do have a LumiLeds, I think, don't quote me on this, but everything seems to match up. This looks like it's a Philips

**Dave Jones:** LumiLeds Luxion, Luxion Low Power, they're called. It's the 4014 compact footprint, delivering high efficacy and just the right amount of light. Well, that's what we need, just the right amount. And it's a, once again, 4000K Bangon 80 CRI, exactly what, you know, the specs for this thing

**Dave Jones:** are. Looks identical, package under the macro lens here, looks like we've got exactly the same thing. And 4mm length, 138 lumens per watt at 30 milliamps. Superior heat dissipation enables cost-effective thermal design. Well, that's exactly what they've done with this board. It's a cost-effective design because they've got away with a single-sided

**Dave Jones:** PCB. They don't need a double-sided. Double-sided's going to cost more. You need, you know, copper on the other side. Copper costs money of course, copper's not cheap. And then you need all the via holes on there to get the heat through to the

**Dave Jones:** other side, and then it's got to be thermally bonded onto the aluminium heat sink on the back, and all that sort of stuff. So they've done, effectively done away with that. And they can just, you know, just that little pad on there looks like it's big enough, this low-cost, low-power thermal design.

**Dave Jones:** And it's all starting to add up. Take a look at this. Luminous flux at 60 milliamps at 25 degrees C, of course. Minimum lumens, 18 per LED. And you remember we've got 4 strips of 24, 96, well, what's 96 times 18? Bingo! 1728.

**Dave Jones:** What's this thing rated at? 1700 lumens. And it's probably conservatively rated too, because that's the minimum. I mean, the typical is about 22. So 22 times 96, what are we looking at? 2000, you know, 2100. About 2100 lumens typical, or about 1700 minimum.

**Dave Jones:** So this doesn't look like a manufacturer that is over-spec-ing their tubes. And incidentally, I stumbled across a cheap Chinese knock-off version of this, looks very similar. It's labelled the 3014 model, and I'll link in the data sheet down below. So, you know, I can't be exactly sure which one this uses, whether

**Dave Jones:** it's a genuine Philips Loony LED Luxion, or it's just a generic, you know, Chinese rebranded one. Eh. Alright, let's just power it up for some fun here and see what we get. 240 volts input, and I'm measuring the current there, and we're getting about 150 milliamps.

**Dave Jones:** So that's a bit lower than expected. Because if you divide 150 milliamps by those 4 strings that we've seen on the board, then you're only running about 37 milliamps per string. So really I was expecting it to be 60 based on the data sheet to give this 1700 lumens out total.

**Dave Jones:** But of course that's just the RMS average current based on the multimeter there. And if you're interested in seeing the current waveform on this thing, I've got my AIM TTI iProber 520 here, just measuring the current on the main LED string. So it's all 4 strings.

**Dave Jones:** And we'll take a look at it. Of course I've got the wire attachment here, I've got it in wire mode. And this is what we're getting. Here it is. You can see the that's the advantage of the deep memory of course, you can capture all that and then

**Dave Jones:** zoom in. And you can see the current ramp there. Of course we've got a whole bunch of ringing at the bottom of it. And then after that, it looks like we've got some main stuff happening in here mixed up with that. But it's basically switching there at 64 kilohertz.

**Dave Jones:** And you can see the main stuff there, we're at 2 milliseconds per division. And if we take that point there for example, and go from there to there, which is the repeating period, then we've got 2, 4, 6, 8, 10 milliseconds, 100 hertz, which is

**Dave Jones:** of course our full wave rectified 50 hertz mains. And this AIM TTI iProber gives us 1 volt per amp output. So I've got it set to times 1 here on the vertical scale, and we're looking at basically 200, 400, maybe 600 volts with the

**Dave Jones:** undershoot there, about 0.6 amps full scale there. And if we look at the RMS value, there it is, about 178 millivolts. So that's a little bit higher than the average value, than the RMS value we measured on the multimeter. But of course that value

**Dave Jones:** is going to vary depending on which part of the 100 hertz cycle you're actually measuring that in. So we can move from 192 milliamps, it's millivolts, so it converts directly into milliamps, on that part of the waveform, then when it dips down here, there we go, down to 160

**Dave Jones:** milliamps or something like that, RMS. Now I've had this going for a bit, I'll try and measure the temperature very crudely with my IR thermometer, and ambient of 25 in here roughly, and I'm getting pretty much a peak 42, 43, so we're looking at

**Dave Jones:** at least 17, 18 degrees above ambient temperature. And I'm attempting to get a thermocouple directly on one of the pins there of the lead, which is going to be, you know, pretty much match the heatsink, that little tiny, you know, 1 square centimetre heatsink they've got between the pins there.

**Dave Jones:** And you know, 37, it's going to be a bit tricky, but it's going to be at least that. You know, it could be as high as say 40 or something, but yeah, there we go. You know, it's not a bad ballpark anyway. Heatsink on the back, and as you can see, it's not as hot of course,

**Dave Jones:** because the thermal bonding is, well, basically not there. It's just radiating through the FR4 onto that, but you know, it is certainly well above ambient, and if you encase the whole thing in polycarb, I don't know, you know, to do proper temperature measurements you've really got to do it inside the actual

**Dave Jones:** tube itself. And of course if you do the math, it's very easy to explain why they can get away without direct bonding to the heatsink. It's because the individual leads don't dissipate much. It's 37 milliamps each, I mean, you know, it's bugger all, basically, times

**Dave Jones:** the nominal 3 volts on there, each lead is dissipating only, you know, or consuming only 0.11 watts. I mean, you know, it's bugger all, really. So when you include the efficacy and everything else, and you know, how much waste heat is coming out of this thing, it is not a huge amount.

**Dave Jones:** That's why these things don't need to be, really have any major heatsink. Although, as we saw, they did actually have that, you know, little one square centimetre worth of large pad on each pin there. So there you go, that's inside a typical reasonable quality German, not German manufactured, but German

**Dave Jones:** company, Muller Light, one of their lead replacement fluorotubes. And that's not too shabby at all, you know, they've cut corners a little bit, but it could certainly be a lot worse, that's for sure. And of course, you know, to really get an idea of how good it is, you've got to measure its thermal performance and

**Dave Jones:** stuff like that, but I'm sure, you know, the reputable manufacturers have done their homework on that, and the heatsink in there is, you know, adequate enough for the life, and it's probably going to meet its life expectations. I don't know, you know, would it be nice to have a

**Dave Jones:** top quality cap in there or something at least? But anyway, yeah, not too bad at all. Nothing terribly surprising inside this, it's exactly what I thought it would be, really, and that's all there is to it. And really, I think you probably won't be able to buy fluorotubes

**Dave Jones:** or, you know, compact fluorescent light bulbs for too much longer. These lead things are just dominating. I just changed over all the bulbs in my house to lead bulbs, just, oh, so much better. Anyway, if you like it, jump on over to the

**Dave Jones:** EEVblog forum to discuss it, that's the place to do it, or leave YouTube comments, but the YouTube comment system kind of sucks, not that good for conversations, not as good as the forum anyway, but if you like it, give it a thumbs up.

**Dave Jones:** Catch you next time.
