---
video_id: 73AWJSugx3o
title: EEVblog #757 - HP4263A LCR Meter Teardown
url: https://www.youtube.com/watch?v=73AWJSugx3o
source: youtube-asr
timestamps: {"0": 1, "1": 20, "2": 34, "3": 52, "4": 68, "5": 81, "6": 96, "7": 111, "8": 127, "9": 142, "10": 155, "11": 168, "12": 179, "13": 198, "14": 215, "15": 233, "16": 246, "17": 260, "18": 273, "19": 289, "20": 306, "21": 323, "22": 340, "23": 361, "24": 376, "25": 390, "26": 406, "27": 422, "28": 438, "29": 455, "30": 469, "31": 483, "32": 504, "33": 522, "34": 532, "35": 544, "36": 559, "37": 574, "38": 594, "39": 609, "40": 621, "41": 635, "42": 652, "43": 667, "44": 680, "45": 692, "46": 703, "47": 716, "48": 733, "49": 746, "50": 760, "51": 771, "52": 788, "53": 800, "54": 810, "55": 824, "56": 836, "57": 853, "58": 865, "59": 880, "60": 893, "61": 907, "62": 923, "63": 937, "64": 952, "65": 967, "66": 981, "67": 994, "68": 1009, "69": 1024, "70": 1036, "71": 1052, "72": 1067, "73": 1080, "74": 1092, "75": 1103, "76": 1119, "77": 1133, "78": 1146, "79": 1162, "80": 1177, "81": 1192, "82": 1204, "83": 1217, "84": 1232, "85": 1245, "86": 1263, "87": 1276, "88": 1294, "89": 1306, "90": 1324, "91": 1336, "92": 1351, "93": 1364, "94": 1378, "95": 1396, "96": 1408, "97": 1425, "98": 1438, "99": 1459, "100": 1476, "101": 1491, "102": 1506, "103": 1522, "104": 1535, "105": 1547, "106": 1558, "107": 1573, "108": 1585, "109": 1598, "110": 1611, "111": 1623}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. It's another eBay score that I've got. This is a HP, yes, none of this Agilent or Keysight rubbish, 4263A LCR meter. And it's an oldie but a goodie, dates from about 1990 or thereabouts. So, jeez, it's amazing

**Dave Jones:** to think 1990 is like 25 years old, but anyway, it's an oldie but a goodie bench LCR meter. And I rather like these things. The user interface is a little bit clunky as we will see later, but I

**Dave Jones:** like the fact that they're nice and small and compact. It is not as wide as a big, you know, 19-in rack mount unit. It's not that deep. It only weighs 4.4 kilos. So, it's relatively cheap to get one of these shipped. And I picked up

**Dave Jones:** this for I saw it on there for 200 US buy it now, and I offered lower than that, and it was accepted. And postage was reasonable, and so it came in pretty good. So, for a It's a 0.1% class

**Dave Jones:** LCR meter. It can do more than LC and R. It can like measure transformer parameters, open short compensation, do all sorts of fantastic stuff. So, I thought we'd take a look inside. I don't think I've ever taken the hood off one

**Dave Jones:** of these puppies before. So, let's check it out. Now, don't confuse this with the 4263B model. This is the A model, which is the older one with the single-line LCD. If you can pick up the newer B model for a

**Dave Jones:** decent price, even better, but I think they go for a lot more cuz they're, you know, they were Keysight, sorry, Agilent bloody branded, and they went for a lot longer. This one was discontinued. Oh, I'm not actually sure. Wait.

**Dave Jones:** Let's have a look. But, yeah, they're they're basically equivalent. The B has a new dual-line LCD. Oh, got a bit of dust inside this puppy, which is, uh, quite unusual, cuz these things don't have a fan. Another thing I

**Dave Jones:** like about them, they're, uh, completely passive. Look at that, a nice linear transformer in the thing, and beautiful. Let's check it out.

**Dave Jones:** Uh, and wouldn't you know it, I'm out of air duster spray to clean this thing up, damn it. Um, so sorry, you get the, uh, you get the grotty unit. So, yeah, I'm rather surprised at the amount of dust

**Dave Jones:** in here that there's no, um, fan in it. So, you know, how does it, uh, I mean, you know, it's got vent holes, maybe it was, um, sitting in a rack, something like that, and yeah, you can get, uh, rack extensions for these

**Dave Jones:** that plug in the side, so you can plug them into 19-in racks, and maybe it was getting air flow from the rest of the system, or something like that, coming through the vent holes on the, uh, side over here.

**Dave Jones:** Anyway, um, it looks very neat and tidy. I like it. As I said, we've got a big thumping, uh, linear transformer here. We've got, interestingly, there's our diode bridge, okay, but we've got this little hybrid board with surface mount on the bottom, and two,

**Dave Jones:** uh, probably linear regulators on the top there with little piece and heat sinks on them. So, that's rather, rather interesting. Got a big, big bridge rectifier there, and we've got, uh, two big, uh, filter caps there, Nippon Chemicons, no worries whatsoever.

**Dave Jones:** Um, 105° C rated, thank you very much. And there's our, uh, our front panel terminals. They got little, uh, common mode toroids on them, just to, uh, keep the crap out, and nice, uh, board-to-board, uh, BNCs for those. Very

**Dave Jones:** nice and looks like we've got some input protection with the diodes there. And uh, cuz these things you don't want to go applying DC voltage and it probably tells you that. There it is. Discharge test device before connecting. If you

**Dave Jones:** hook up a big thumping electrolytic capacitor charged up to it, uh, it can ruin your day. Interestingly, they've got a DC to DC converter in here. They've gone to all the trouble for this nice linear uh, power supply

**Dave Jones:** arrangement and then they've got this little DC to DC converter brick and that's powering something over here. So, I'm not sure Oh, it Yeah, in down in there. So, I'm not sure what the deal is there. Hmm. This top board here,

**Dave Jones:** obviously the uh, processor interface. This puppy looks interesting. Oh, this dust is horrible. Take a good look at that in a minute. Um, it's the GPIB. Uh, it's driving the GPIB, so that'll be our GPIB chipset up there and uh, that's

**Dave Jones:** probably our processor. We'll take a look at that and there's the money shot for you, 68,000 fan boys. Obviously the main processor there and it's the HC version. Awesome. And we've got ourselves an NEC supercap 0.22 farads there, 5.5 volts. Uh, no rechargeable or

**Dave Jones:** uh, primary lithium battery to leak in this thing by the looks of it. Excellent. I love supercaps and none of this modern flash rubbish. We're going old school, Zilog X28C64E2 PROM. So, that uh, hold your uh, non-volatile settings and then we've got

**Dave Jones:** ourselves a um, AMD uh, EPROM here for the main program. One meg, it's a decent size uh, EPROM, let me tell you. And there we go, 1992 vintage. But, the main processor here is 52nd week '94. So, uh, this thing was

**Dave Jones:** built in 1995. And check this out, very interesting package. Look at this. I've rarely seen something like that. It's obviously some sort of National Semiconductor custom ASIC or a gate array or something like that. So, if anyone's got any info

**Dave Jones:** on that, please leave it in the comments. That is fascinating. And of course, it's all tied in to the process. You can see all the traces and uh everything else. So, wow, some sort of I It's almost like some sort of system

**Dave Jones:** glue logic, you know, trying that Look, it's tied up here, maybe into maybe it's doing some It's doing some memory as well and things like that. So, some It's almost like some sort of, you know, glue logic that you could have done in

**Dave Jones:** you know, a CPLD or a little FPGA or something. But yeah, so that makes me suspect that's some sort of custom gate array from National Semiconductor. And it wouldn't surprise me in the least if they upgraded this when they went to the B model with the

**Dave Jones:** dual line display cuz this thing probably went obsolete by, you know, like the end of the '90s. I'll show you the rear panel as well. Mains selection here. So, you you know, no worries with buying these internationally at all. And

**Dave Jones:** we've got external DC bias voltage, external trigger the handler handler interface. These things are important cuz LCR meters like this are designed for like, you know, automated system production testing and stuff like that. So, you'd have this digital handler

**Dave Jones:** interface which can control, you know, limit switches and you know, all sorts of, you know, bed of nails type stuff for your product under test. And all controlled via GPIB, of course. And made in Japan. All the best stuff's made in

**Dave Jones:** Japan. And for those wondering why it's made in Japan, cuz that's a bit unusual for HP gear, isn't it? Well, not so much, because this explains everything. Why HP? Yokogawa. HP, it's This is actually uh designed and probably

**Dave Jones:** manufactured by Yokogawa for HP. They had a partnership for lots of um high-end test instruments and things like that. Serious dust under here, that's for sure. Really need to clean this sucker out. I might have to head to

**Dave Jones:** Jaycar and get an emergency can of uh compressed air to clean this out. Anyway, interesting. We've got ourselves a little uh shield there that's uh uh trying to do some RF shielding for this vertical board here, which by the looks of

**Dave Jones:** the big capacitors on there and the resistors and there's some surface mount stuff on the other side, I reckon that is the um device under test uh range resistor select board. Because if you don't know how these LCR meters

**Dave Jones:** work, well, I've done a video on that way back in the day, which I'll link in here. Check it out if you haven't seen it. And the way these things work is that they put a resistor in series with

**Dave Jones:** the device under test, and that's the range resistor, which we'll see later. We can actually select that on the front panel. And with that resistor in series, of course, you measure You can measure the voltage and the current um and hence

**Dave Jones:** the current going through the resistor, and you can also measure the voltage of the device under test. And from those from the voltage and current uh through the device under test and the phase, you can actually calculate every parameter

**Dave Jones:** of the device under test, inductance, capacitance, uh reactance, series resistance, dissipation factor, quality factor, you name it. You can calculate all this stuff. And in the video here, I've gone through um and showed you the formulas that actually makes that

**Dave Jones:** happen. Now, unfortunately, I can't bend that board back cuz I'll break it, but aha, look at all these precisiony-looking resistors on here, plus a couple of little SO chips, which are probably muxes to choose the range on there. So, yeah, I

**Dave Jones:** reckon that's got to be the range resistor select board. Now, I couldn't find a service manual for this 4263A model, but I did find the service manual for the B model, which by the way looks like it came out in about 2000. So,

**Dave Jones:** about 10 years after they originally did the A model. And by the way, looking at the block diagram, it looks like it may sort of have the main chip over here, but like a similar layout, but it could have

**Dave Jones:** changed. Anyway, we have the overall theory of operation. And it's exactly as I explained before I was showing it in the other video, but yeah, we've got a the device under test and a range resistor, and it just measures the

**Dave Jones:** voltage and the currents going through the device. And from that voltage-current ratio measurement principle, you get the impedance. And from that, there we go. It only focuses on the impedance. The other parameters, LCR and every quality factor, dissipation, everything else is derived

**Dave Jones:** mathematically from the measured impedance values. So, it's rather quite simple. We've got a signal source here, selectable test frequency, 100 Hz, 120, 1K, 10K, and 100K. In this case, we've got our device under test. So, they're measuring the differential voltage

**Dave Jones:** across that here, and then they're measuring the current through the device with a range resistor here, which they can select in. It's anywhere from like 1 ohm up to 10 meg or something like that, as we'll see later in the software. And

**Dave Jones:** they just feed that, multiplex that into an ADC, and Bob's your uncle. You can calculate anything. Very simple technique, but there's a bit of math and filtering everything else which uh goes behind it. And here is more of the

**Dave Jones:** practical implementation how they do it. Here we've got the uh four terminals on the front here. So, they do uh Kelvin connection right at the device under test for compensate for your test leads. We've got our signal source here which

**Dave Jones:** uh uh generates from our current terminal and then we can read that off and then they can just multiplex that and whack it into an ADC and there's your range resistor on the low end side there. Too easy. And we've got ourselves

**Dave Jones:** a a Shay Kazi. If I'm pronouncing that correctly. Sure or not. Once again, Jap- Japan because it's a Yocto product. So, you know, no surprises uh for guessing that they're using Japanese chips in it. It's rather obscure AK9201A-VP.

**Dave Jones:** Can't really find a data sheet for it. It's you know, you get all the false leads on the on the uh merchant websites and stuff like that. But, of course, based on uh you know it's an analog part because

**Dave Jones:** A, you've got these electrolytic caps around it. There's no like big digital stuff going into it. And look, they've got some resistors around here and you know, look it it just looks like an analog analogy type chip. And what's it

**Dave Jones:** going to be in this thing? Well, we need that analog to digital converter, don't we? So, I'm pretty darn sure that is our analog to digital converter. So, I'm not sure what uh type it is. It's probably some sort of,

**Dave Jones:** you know, um maybe a dual slope uh converter or something. Not entirely sure. But, anyway, definitely analog to digital converter. And we've got ourselves a rather crude DAC in here as well, the 0802. And that is for setting your output uh signal

**Dave Jones:** level because tada, here's your output uh block diagram. We have our reference oscillator here. That's our DAC there that we just saw. Then we've got ourselves a low pass filter. And then the uh DC bias uh source. You can turn

**Dave Jones:** that off and on. They just sum that in. And as we saw before, you got an external uh connector on the back if you want to feed in your own uh DC bias and a buffer and then the source resistor.

**Dave Jones:** That's not to be confused with the uh range resistor. So, that's the source resistor driving your device under test. Because as you can see, not only can you set the uh frequency here from 100 Hz up to 100 K, but uh you can also set the uh

**Dave Jones:** voltage level as well. And for voltage uh dependent uh devices, that can be a big deal. So, you know, this has uh fixed steps built in or you can actually feed in your own externally. And we've got ourselves an

**Dave Jones:** Intersil uh 82C54 there. That's a uh programmable uh timer counter chip. And that puppy next to us just a very small uh pile there. So, they've just got some uh glue logic associated with that uh timer counter. Not sure why they bothered because the

**Dave Jones:** board is, you know, chock-a-block with all this other uh discrete logic stuff. And down on the front end here, no surprises for finding uh precision op-amps in this uh case uh Burr-Brown there. They were the ducks' guts back in

**Dave Jones:** the day. Um OPA627, they're uh precision die FET. Oh, not this bi FET rubbish, die FET uh op-amps. And we've got ourselves another regulator board down in there by the looks of it, but uh yeah, it is actually

**Dave Jones:** a different SMD layout on the back to this one we saw over here. So, I'm not sure what the deal is there. Now, I'm actually doubting that it's a regulator board. I think it could be something else. Actually, if you give it a

**Dave Jones:** moment's thought, you can probably figure out what this board does. There, power transistors. And I'll tell you why. We've got ourselves the DAC here, right? That DAC, as we saw on the modular block diagram, the DAC of course

**Dave Jones:** drives the signal level. We've got some filtering around here, probably. And then we've got the output buffer, which has to drive, tada, this wire here, which is our positive high current output there. There it is. So, that is

**Dave Jones:** obviously our output driver board with a couple of power transistors on there. So, some things like that actually become very obvious when you just, you know, follow the path and just put on your thinking cap for a few seconds and try and figure it out.

**Dave Jones:** So, yeah, I'd bet my bottom dollar that's a buffer amplifier board. And as I said, I'm willing to bet that's our range resistor board there or what they call the transducer there. So, I reckon that's probably it. They're doing some muxing

**Dave Jones:** in there and of course would contain the range resistors. It's just curiously placed because it's on the system diagram, of course, it's on the low side. So, here's our low side over here. And well, that's going in over here. So,

**Dave Jones:** hmm, having a few doubts, but it just seems to match just like the physical, you know, physical arrangement of what's on there and stuff like that, but interesting. So, yeah, we do not have the schematics for this thing that I

**Dave Jones:** could immediately find, but if you do have them, please link them in and then I will put always always put the link in down the bottom for those who want to play along at home with the service manual. Always fun. And on the

**Dave Jones:** mains side of things here, it's all very neat and tidy. It's got the requisite input protection and all the jazz. I like it apart from the fact that what wouldn't cut the mustard these days all the exposed mains wiring on the back of the voltage

**Dave Jones:** selection switch down in there. So, that's not too great, but still very neat and tidy. So, that's a look inside. So, we might now just power it up and have a little play around with it. Now, the 4263B

**Dave Jones:** service manual that I got, sadly it doesn't have any schematics in it. It's got the block diagrams, theory of operation, parts list, all that sort of jazz, but as is quite common, yeah, no schematics. You only got that in like

**Dave Jones:** gen the uh printed out version possibly and nobody's scanned it in so bummer. So, let's power this puppy up and uh it was it like it was just sold as kind of like as is. Um so, I like the uh 14 segment uh

**Dave Jones:** display on these things. Fantastic. There we go. 4263A. Oh, what what was that? Hang on. Whoop. Let's put it up. Yeah, they got the uh 14 segment uh starburst uh display and rev 2.00 option 001. Not sure what

**Dave Jones:** option 001 is. It might be like external DC uh bias or something like that which um in a lot of uh gear like this you might uh pay extra for especially in like the old um Fluke Philips um LCR meters. I

**Dave Jones:** think the DC bias was like an optional extra. Now, the only issue uh with this thing it seems to be you know seems to be doing the business. Of course, we're going to get overflow and you know every thing else because uh

**Dave Jones:** we've got nothing uh hooked up or the sense is not hooked up. So, basically what we do these are the current uh drive lines which actually drive the current through the device and then of course you got your sense terminal. So,

**Dave Jones:** it's a four terminal uh Kelvin uh measurement system. Now, of course, you can get really expensive um add-on pods which actually plug directly onto the front and then they've got the uh traditional two terminals for your uh device under test. I don't have one of

**Dave Jones:** those. I might actually make one up but uh in the meantime I've just made up a nice little adapter with uh four BNCs and um I've just got the uh sense terminal joined inside there. So, now we can just measure two terminal devices

**Dave Jones:** easy. And as you can see the BNCs are a bit crusty on this thing. Could actually replace them or you could try and clean them up. I might do that later but yeah, they've they've seen better days but the

**Dave Jones:** actual um internal uh contact is still okay. So, here we go. We're just measuring a mic cap here in uh s- series mode. And here's the thing I don't like about this series of LCR meters is that the

**Dave Jones:** user interface is a It's a bit dicky. It's a bit difficult to use. It's not the easiest thing to drive. You really have to get used to it. But anyway, we've got all the different measurement parameters. And the way you do it is a

**Dave Jones:** bit weird. You go into measurement parameters and you'd think that you'd be able to select those with your up down arrows, but that actually changes your main meant like your main menu options. See six of eight here. So,

**Dave Jones:** on the first, we can measure impedance. So, Z is impedance. So, you can get impedance and that is like phase angle. So, if we actually chose that, we could actually measure the impedance of our capacitor plus the phase angle. So, we'd

**Dave Jones:** actually go in there and you see it's changed from series capacitance to displaying the impedance at that particular frequency. We've got 100 hertz. We can just choose the different frequencies we want here. So, let's just leave it at 100 hertz and our drive

**Dave Jones:** level 50 millivolts. That's going to be fine. That's not going to the signal the voltage dependency of this cap is not going to be a it's not going to matter much if at all. No, it's changing bugger all there at 1 volt. There we go. It's

**Dave Jones:** changing a little bit down there, but we'll just leave it on 50 millivolts. And of course, you can see that we've got -90 degrees there cuz it's almost an ideal capacitor. Well, it's it's not a bad cap. It's doing all

**Dave Jones:** right. -90 degrees as your basic theory would suggest. And of course, if we put an inductor in there, tada, the voltage is going to lead instead of lag like we got on the capacitor. Yay! Just like the theory. It works. So, yes, rather

**Dave Jones:** unusual interface. So, So go your measurement parameter like this and then we can and of course we can get the resistance as well and then for all you admittance fan boys out there, yes you can measure the admittance with your

**Dave Jones:** phase angle and then you can measure your conductance with your susceptance. And then you've got your parallel capacitance with your dissipation factor as your secondary measurement. So basically what we're seeing is primary measurement secondary display and then you can get your parallel capacitance

**Dave Jones:** with your quality factor if you want or whatever and then you can get series capacitance just like you will will see in a minute on the Agilent handheld meter and once again so series parallel with quality or dissipation

**Dave Jones:** factor and then inductance parallel of course with our quality or dissipation factor and then series inductance and then we can get with the DC resistance as well and then we can get into transformer type stuff and the impedance as we saw.

**Dave Jones:** So lots of measurement functions on this thing. It's really quite nice. So there we go. If we measure the series capacitance of that very small dissipation factor half a bee's dick there or well, I don't know four bee's

**Dave Jones:** dicks is it? And we can set like we can do averages and things like that. That is actually 10 averages at the moment. This is actually a very fast a very fast meter. I shouldn't like the update speed is actually quite quick cuz

**Dave Jones:** it's a a system meter. So it's designed for quick uh production measurement and things like that. And then you've got comparator stuff we can you can set up so so you know component binning and things like that. And you've got your

**Dave Jones:** bias set up. You can do a reference offset if you want so like a delta you can yeah there it is. They've got like a delta reference and you can actually choose which parameter you want a delta. So you can choose CS. So we can actually

**Dave Jones:** delta out that one that we just did. So it's a rather convoluted system to actually do this, but we can go in there and then we can go on. Whoop. No, I gifted it, did I? Yep. Screwed the pooch.

**Dave Jones:** Ah. It's a really annoying user interface. You got to, you know, like if you don't use it for a while, you will certainly forget how to use the damn thing. So, let's see if I got it this time.

**Dave Jones:** Reference, go in there, and then we can choose, there we go, from off delta. So, we got to press mode again to go over to delta, and then we press enter, and ta-da! There we go. We've now got delta

**Dave Jones:** series capacitance. So, actually, why it didn't cancel that out and is now showing zero, I'm not sure. It should have. Huh. So, it looks like it can't take the delta from the component under test, or maybe it can,

**Dave Jones:** but anyway, in this case, it looks like I've got to actually uh delta out. Let's say we can delta out 10 in there. So, let's do that. And no. Doesn't like that at all. Oops. Oh, maybe I got the units wrong. I don't

**Dave Jones:** know. Anyway, these I think you get the idea. These things are a pain in the ass to drive if you haven't RTFM'd. Okay, so we're getting 100.26 nF at 100 Hz. So, let's try that on our handheld meter. There we go. That's not

**Dave Jones:** too shabby, 100.22 here. Once again, we're in series mode there at 100 Hz. So, all the same measurement parameters, the the actual signal test level isn't going to really make a difference here. So, there we go. It's pretty darn close

**Dave Jones:** to spot on. This is a This is one of the best handheld um meters you can get uh in my opinion the U uh 1733C it's a bit pricey. I know you can get like those cheap um ones on eBay for like you know 80 bucks

**Dave Jones:** these days and they're pretty good but uh yeah if you can afford it this one's a pretty decent uh meter but this one as I said like 0.1% uh class uh instrument and they're actually the uh the accuracy specs of these are actually

**Dave Jones:** quite complicated. Um it's it's not just you know a simple 0.1% they got like a whole chart and everything for it but as you can see it's um pretty much bang on after 20 years. Awesome. And you can set

**Dave Jones:** up other things like uh cable compensation you can do open short. I don't think don't know if this does open short load compensation. I think the B model uh does I won't go into what uh those is I might have done that in a

**Dave Jones:** previous video but yeah you know and you can set up triggering all that sort of stuff for all the automated handling interface uh as we saw on the back. And you can do all sorts of weird and wonderful things. There's lots of uh

**Dave Jones:** stuff in there that I haven't um in the setup which I haven't actually shown so but it's a very powerful versatile bench LCR meter. So there you go that's the HP 4263A and I think it still pretty much holds

**Dave Jones:** its own today you know 0.1% uh class with all the capability. Yeah the user interface is a little bit annoying but you know if you can pick up one of these like I did for under uh 200 US bucks and

**Dave Jones:** I think you know it's pretty much a bargain especially if you can get the new uh B model it's just got the nicer uh dual line dot matrix screen and things like that but I believe it's almost identical uh functionality but

**Dave Jones:** even for a 20-year-old instrument it's really quite nice and I like the form factor too it's you know it doesn't take up a huge amount of space on your bench it might be a bit bigger than some modern um LCR meters might be a bit

**Dave Jones:** deeper or something like that, but you know, I think it it does pretty well. It's a nice compact instrument and check them out on eBay if you can score one. So, there you go. There's another quick teardown of another eBay score. Hope you

**Dave Jones:** liked it. If you did, please give it a big thumbs up and as always I'll link to data sheets and things down below and forum comments. Catch you next time.
