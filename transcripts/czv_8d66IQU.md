---
video_id: czv_8d66IQU
title: EEVblog #628 - Tektronix 213 Vintage Portable Oscilloscope Teardown
url: https://www.youtube.com/watch?v=czv_8d66IQU
source: youtube-asr
timestamps: {"0": 4, "1": 12, "2": 23, "3": 35, "4": 45, "5": 59, "6": 73, "7": 88, "8": 101, "9": 119, "10": 135, "11": 147, "12": 156, "13": 169, "14": 185, "15": 199, "16": 211, "17": 225, "18": 236, "19": 254, "20": 274, "21": 287, "22": 297, "23": 308, "24": 318, "25": 334, "26": 344, "27": 353, "28": 361, "29": 378, "30": 391, "31": 405, "32": 418, "33": 433, "34": 444, "35": 455, "36": 465, "37": 478, "38": 490, "39": 499, "40": 508, "41": 521, "42": 538, "43": 547, "44": 557, "45": 567, "46": 582, "47": 589, "48": 601, "49": 613, "50": 626, "51": 643, "52": 657, "53": 668, "54": 678, "55": 698, "56": 709, "57": 717, "58": 739, "59": 751, "60": 768, "61": 781, "62": 795, "63": 808, "64": 821, "65": 831, "66": 844, "67": 853, "68": 875, "69": 891, "70": 900, "71": 911, "72": 921, "73": 937, "74": 946, "75": 954, "76": 967, "77": 978, "78": 994, "79": 1007, "80": 1021, "81": 1029, "82": 1036, "83": 1044, "84": 1055, "85": 1065, "86": 1077, "87": 1088, "88": 1100, "89": 1111, "90": 1127, "91": 1136, "92": 1152, "93": 1163, "94": 1170, "95": 1183, "96": 1201, "97": 1215, "98": 1224, "99": 1237, "100": 1251, "101": 1262, "102": 1275, "103": 1290, "104": 1309, "105": 1320, "106": 1332, "107": 1341, "108": 1355, "109": 1365, "110": 1381, "111": 1394, "112": 1402, "113": 1413, "114": 1426, "115": 1437, "116": 1450, "117": 1464, "118": 1474, "119": 1490, "120": 1502, "121": 1518, "122": 1535, "123": 1547, "124": 1561, "125": 1572, "126": 1587, "127": 1600, "128": 1613, "129": 1623, "130": 1640, "131": 1662, "132": 1682, "133": 1697, "134": 1703}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Quick announcement before we get into it. For those who have been asking where can I get one of these warranty void if not removed t-shirts?

**Dave Jones:** Well, you obviously missed my previous Teespring crowdfunding campaign for it. So, I've started again. For those who have asked, the link is down below. If you want one, they're pretty cheap.

**Dave Jones:** They're only 15 bucks and pretty cheap postage within the US. Other countries a bit more expensive, but hey, it's not bad at all. Certainly cheaper than my Zazzle store originally was.

**Dave Jones:** So, if you want to nab one, the campaign only runs for a short time. So, the link is down below. Go and nab one if you want it. They're available in women's styles and hoodies and winter jumpers and all sorts of things.

**Dave Jones:** So, excellent warranty void if not removed. I love it. Anyway, we're going to take a look at this Tektronix. Look at this. This Tektronix 213 handheld um not quite a pocket oscilloscope.

**Dave Jones:** If you had a really big pocket, you could call it a pocket oscilloscope. But, vintage handheld portable scope from 1975. Fantastic vintage technology. Had this hanging around for a while.

**Dave Jones:** Got it in the mailbag. So, let's check it out. And here it is. Isn't it just gorgeous? Look at this. State-of-the-art technology in 1975. And not only is it an oscilloscope as you'd expect.

**Dave Jones:** It's a 1 MHz oscilloscope by the way. 1 MHz bandwidth. Look at that nice crisp trace on that. It's just beautiful. But, yeah, not not a huge bandwidth, but good enough for a portable scope, especially for 1975.

**Dave Jones:** But, it's also a multimeter as well and a pretty decent multimeter at that. It's a 3 and 1/2 digit, but it's 0.1% plus one count motor meter. It does milliamps and ohms and also true RMS AC as well.

**Dave Jones:** So, pretty impressive stuff. Look at that. Generating the characters with the CRT. There's a specific custom CRT character generator chip inside this thing which we'll see. And yes, we do have the full schematics for this baby.

**Dave Jones:** But look at this. Isn't it just a thing of beauty? Really. And these are the input controls here. Here's your multimeter input jacks. They didn't use the BNC. The BNC is on the back.

**Dave Jones:** By the way, there's nothing else there on the back. But we can change the intensity and we can change the calibration of the horizontal and the vertical as well.

**Dave Jones:** And we can change the trigger. And it's got auto trigger mode and AC DC input coupling. No, it is not an isolated scope. But hey, you know. For a portable scope, ah, fantastic.

**Dave Jones:** I don't think anything else ever matched this thing. Really. And to have a CRT inside that, that is terrific. I mean, granted it is a really small screen. But hey, very useful back in its day, I'm sure.

**Dave Jones:** 1975. Not sure exactly when this one was manufactured. We'll find out when we open it up and take a look at the date code. So, let's go. So, a big thanks to Derek White who sent this in to the mail bag some time ago.

**Dave Jones:** Sorry it's taken me a while to get around to it. Look at that. That's really quite nice. I think there's only four screws on the bottom. Here, there's two on the front which hold this uh Oh, yeah.

**Dave Jones:** There we go. Can't get that one out. But anyway, and there's looks like there's two on the back here. And 1975. Well, it's all going to be it's all going to be dip uh componentry, that's for sure.

**Dave Jones:** Dip ICs, the custom character generator on there's some 4000 series CMOS. And yes, we do have the full schematics, which I'll show you later, and which I'll link in down below.

**Dave Jones:** And there's actually a wiki uh page on the tech wiki. Looks like the lid does come off here. Hey, hello. Whoa. Hey. Whoa, look at that. There's a bit of uh 40-year-old crustiness.

**Dave Jones:** I mean, you got to remember, this is 40 years old, 1975. Goodness. I mean, you know, that's just incredible. And look at this. It looks like it's a uh very nice little That's obviously for the uh internal battery, cuz this thing did have a battery, and that's probably where all that gunk uh came from.

**Dave Jones:** So, there's a cutout in there for that. But apart from that, look at this. It's a nice little uh sort of cube construction. Oh, well, yeah, there's a board on the bottom as well.

**Dave Jones:** So, there's board on all Well, no, not on this end, and not on that end, but all four sides are wrapped around like that. So, that's really quite neat.

**Dave Jones:** Actually, I hope they can pull apart. I hope they're not so Oh, no, yes, they are. I think they're plug-on boards. I can just lift that I should be able to just lift those boards out.

**Dave Jones:** So, there you go. Look at that. That is a thing of beauty. Look at the tiny little electrostatic CRT in there. I love it. Ah. Well, it's even earlier than that.

**Dave Jones:** Look at this. Copyright 1973 Tektronix Corp. So, it's more than 40 years old. Ah, can you believe it? Unbelievable. This is like, you know, just after the Apollo uh program finished.

**Dave Jones:** It's just incredible. But look, we have a date code here of '81. I don't know whether or not it was manufactured in '81, or there was some other mod, or something else happened.

**Dave Jones:** That could have been like, you know, tested by KW, I guess, um, in '81, perhaps. Anyway, we'll find out that once we get to the, uh, date code of the ICs.

**Dave Jones:** That'll be dead giveaway. There's a few adjustments on here, too. We've got plus 15 V adjust. I assume that's, uh, some sort of power rail. We've got charge adjust.

**Dave Jones:** We've got high voltage adjust. There we go. Character spacing adjust over here. This is like a link, I believe. I've had a quick look at the schematics and I think there was like a a jumper link in there that actually, uh, set how much, uh, spacing you have between the characters on the, uh, CRT.

**Dave Jones:** I'm not sure why you'd adjust that, but anyway, uh, DC calibration jumper. So, there's a jumper link. Um, DC cal, as well. Ohms adjust. Times 10 gain and, uh, DC zero and AC zero and AC gain.

**Dave Jones:** Oh, man. More adjustments you can poke an adjustment screwdriver at. So, what I'm going to do is try and lever this board out here and, uh, I'll show you in a, uh, no, hang on.

**Dave Jones:** I might have to take those. Looks like those nuts come out. All right. No, I'm stuck. These things, they do have, uh, board-to-board headers on here, but, yeah, it looks like those nuts have to come out.

**Dave Jones:** And check out also the classic black silk screen on the reverse side of these boards. Look at that. Terrific stuff. The other ones are actually, um, uh, etched into the copper on there, but, yeah, we do actually have, um, some, uh, silk screen overlay on bottom.

**Dave Jones:** And thoughtfully, these are the dip packages here. Thoughtfully, they've put them, you know, in exactly the right space on the back for servicing. I mean, that's terrific. Somebody was thinking.

**Dave Jones:** All right, she's just going to pop right out now. Ta-da! There we go. There's our first board. That's probably going to have our, uh, character generator ROM on there.

**Dave Jones:** These look like your custom, uh, Tektronix chips. So, we'll take a closer look at those, but, oh, look at that big ass cap. And there's the money shot, two custom tech chips.

**Dave Jones:** This is uh U270. We'll have a look at the schematic in a second. This is the uh character generator ROM. So, it basically gives the uh X, Y, and Z axis outputs and decimal uh point blanking and all that sort of stuff.

**Dave Jones:** And that's fed from this uh four-digit decade counter here, and you'll see that on the schematic. That's also a a custom uh tech chip of some description. So, look at that.

**Dave Jones:** And this is So, this is the combined analog Well, it tells you over here the analog to digital board, but also the character generators. So, basically, we're looking at some uh trim pot adjustments up there.

**Dave Jones:** They were the um ohms and DC uh volts adjust. Got some couple of discrete uh transistors. I'm not sure if that's a a input uh coupling cap or the sampling cap.

**Dave Jones:** We'll have a look at it in a minute. Um there's a funky-looking diode package. We'll check that out. Look at that. It's got a diode symbol on there. I've never never seen something like that before.

**Dave Jones:** That is bizarre. Then we've got ourselves an MC1456 op amp, and then going into a 74L double O. Oh, classic low-power TTL 74L series. I haven't seen those in a long time, but that's just doing some uh latching uh stuff.

**Dave Jones:** They're using four uh NAND gates there to do some latching. Um and that's pretty much it. Look at those funky capacitors, would you? They don't make them like they used to.

**Dave Jones:** There you go, decode the color code. Awesome. And yep, it turns out that's just a dual diode package. There's actually two pins on the other side. You can barely see them there.

**Dave Jones:** So, just two diodes in one package. I'm not sure if they're designed to be uh thermally bonded and matched. And you can see pretty much what's happening here. Here's our uh Zener reference here.

**Dave Jones:** So, our 6.2 V uh Zener reference. There's the CR217 I was talking about there. And where is it? They've got it down here as well. So, they've got that coupling over to the input to our counter over here.

**Dave Jones:** So, we've got a slope converter happening here. You'll see that in the rest of it. And yeah, there we go. Here's our integrator C227. And that is certainly that one there.

**Dave Jones:** So, that's our integrator capacitor. That's why it's so schmick. And pretty much yeah, voltage reference and then the ohms adjust here, which is one of these trim pots up here.

**Dave Jones:** And then that's all just going into a couple of latches and into our four-digit decade counter, which as I said is this one over here. And our NAND gates is our two NAND gates is two latches there.

**Dave Jones:** Nice little wave forms on these schematics here. I love it. They got voltage test points. Brilliant. They don't make schematics like this anymore. But yeah, that's pretty much all it is.

**Dave Jones:** This is a custom four-digit decade counter or four-decade counter here. And that here's the binary. Here's the decade, you know, the digit outputs here. And the digit outputs are fed into the character generator ROM down here.

**Dave Jones:** And the character generator ROM, unfortunately, we don't have any info on that. But it does all the magic and then outputs the XY and Z axis. And that goes off to the CRT only when you've switched it in, of course, in multimeter mode.

**Dave Jones:** It's disabled in scope mode. And then as I said, they've got the decimal point spacing enable pin here. So, this was that strapping we saw on the back of the PCB there.

**Dave Jones:** But yeah, there's not a huge amount to this. I mean, this is the analog to digital converter portion. It's all old school. There's no ADC chip as such in this thing.

**Dave Jones:** It does it using slope conversion. Terrific stuff. So, basically what this is doing here, the decade counter, that actually does the counting direct from the ADC. It starts at zero, counts it up and gives you your value, and then it multiplexes the output here and actually then that goes through the character generator ROM.

**Dave Jones:** So, it'll cycle through each one of the digits, and there's the digit transistors up here, and you can see that it would pass each digit directly through to the character generator ROM.

**Dave Jones:** So, all the character generator ROM has to do is convert that digit into a specific waveform data, but there'd be a lot of magic happening in there. I'd love to get some info on that.

**Dave Jones:** If anyone's got anything on that character generator ROM, please leave it in the comments. Now, you can see how they do the board-to-board interconnect here. They've got like those sort of like surface-mount crimp type pins that are designed to go into the normally like a you know a Molex mating block connector, something like that.

**Dave Jones:** Well, they soldered those pins directly onto the board, essentially surface-mount soldered them. I don't think that there's any that they're through-hole pins protruding through the and these things wouldn't be easy to solder as well.

**Dave Jones:** You wouldn't just solder them freehand one by one. You'd have either the original board in place like this or more likely some sort of soldering alignment jig where you'd plug the pins into the sockets and then solder them in so they're all nicely lined and then you'd pull the board out.

**Dave Jones:** And although this thing is a marvel of sort of you know systems engineering and integration to get it into this, sort of they couldn't really go the whole hog and have a proper PCB mounted BNC on here.

**Dave Jones:** So, they had to have a coax going down there, stuff it in, and insulate the back of this BNC connector down in here. It's a bit of a shame that they couldn't you know do that a bit better, but well, you know, what's a bit of wire in back in 1975?

**Dave Jones:** Now, is that my imagination or is that BNC not factory original? I think it could be a modern replacement, I suspect. And look at this. This is the mating BNC hole for that.

**Dave Jones:** It doesn't look like it's been factory done. It looks like somebody has hacked that thing out. Hmm. And check out the mains wiring. I mean, it's all pretty how-you-doing.

**Dave Jones:** And like there's no proper cable clamping or anything here. It just sort of comes out there. It's sort of wrapped It's not even wrapped around the post for a bit of strain relief or something like that.

**Dave Jones:** It's just got a bend in there right at the back neck of the CRT here and then soldered directly onto the PCB. Hey, at least it's fused. Danger. AC voltage and CRT.

**Dave Jones:** Approximately 1,200 V potentials are present under this area. Here's the main board. I popped it out. Battery charger test point. There you go. And ground plus 75 V, plus 15 V, and plus 6.

**Dave Jones:** plus minus 6.5 V in this CRT grid bias there. And that is our board. Ta-da! That's our CRT drive That's our main power supply that takes the 240 V in and converts it down.

**Dave Jones:** So is it Looks like some sort of uh uh switching converter or something to that effect. And then uh uh bit of CRT driver business happening there. And And here's a schematic for our main power supply and battery charging board.

**Dave Jones:** We've got some Here's our AC input here. We've got some uh filtering happening there. There you go. Common mode choke. Got a bridge rectifier straight on the mains coming across.

**Dave Jones:** Uh that's the battery charger converter circuitry. That says uh Those diodes and inductors and cap there are on a substrate. So I'm not sure Oh, inner shield, outer shield.

**Dave Jones:** Oh, okay. So this is all underneath the main shielding on the board there. I think that's what they're talking about. And uh then Oh, look. We've got ourselves a multi-vibrator there.

**Dave Jones:** Absolutely classic. You can tell that building block a mile away. And then here's our inverter over here and now that's all part of the regulation circuitry. And the inverter, by the way, is hanging If you're wondering where it is, where's the transformer?

**Dave Jones:** Well, here it is up here. And they've got it so they've got it in a separate can there and that's what this wire comes over and then attaches to this board over here like that.

**Dave Jones:** So, yeah, they've mounted that completely off board. So, once again, you know, not enough room in there cuz you've got to fit your CRT and everything else. Oh, we've got a little bit of volume left there.

**Dave Jones:** Let's whack our big ass transformer in there and just wire it over. Not a problem. Bob's your uncle. And check out this. Little modification notes. Somebody has done this.

**Dave Jones:** Look at 4th of the 11th, 2011. I downloaded this schematic. So, wherever they got it from, I don't know. They scanned it in from somewhere, but somebody's done this hand mod in there.

**Dave Jones:** So, there you go. That's a really aftermarket mod, that one, I think. There we go. We can really see those little board-to-board contact like Molex type pins there. And yeah, they do have a little tab which goes into the hole in the board there.

**Dave Jones:** That's how they hold them in place during soldering there. But yeah, they don't actually pins don't protrude through the other side. So, there you go. They could be purpose designed for that rather than just bodged from some some connector.

**Dave Jones:** And the other part of the CRT driver board down the bottom. This is a big board which goes basically the full base of the unit. It's got a big cutout in the middle for the battery and a couple of more trimmers down in there which don't have an external hole on the side.

**Dave Jones:** So, these would have have to have been trimmed on the bench before they installed all of this stuff. But once you put that board in there, you can't Oh, no.

**Dave Jones:** No, there we go. Sorry. They've got the trimmer holes through the board. There you go. So, yeah, you can actually install the board first and then trim them afterwards.

**Dave Jones:** But you wouldn't be able to do it once it's in the case. So, this whole thing has to lift out as an assembly. Huh, speak of the devil. There we go.

**Dave Jones:** Yeah, it all just popped out of the case very nicely. And you could, once you put all this in, um you know, pretty nicely adjust and trim this thing on the bench before you whack it in the case.

**Dave Jones:** It really is quite a lovely assembly. It's almost a work of art. And here we go. We can see the bottom of this thing. And uh we've got a so some red silkscreen.

**Dave Jones:** Now, doesn't that look lovely? Red and green. Ah, beautiful. And uh danger 1,200 V. Look at this. The PCB designer really knew this stuff. They're marking out the dangerous uh voltage side of the thing.

**Dave Jones:** All these contacts right around there. Terrific stuff. Oh, yeah. I forgot to mention the date code, by the way. Uh 37th week 1980. So, there you go. We're talking late 88 1980s for the chips.

**Dave Jones:** So, yeah. Certainly this thing looks like it was manufactured in uh '81 as it uh says in various locations around here. There we go. 51 50 Is that 51st week '81?

**Dave Jones:** I think it might be. Got ourselves a nice little uh shield in plate in there from this CRT. This is an electrostatic uh CRT, of course, as I mentioned.

**Dave Jones:** So, you get no uh deflection uh magnetic deflection coil uh yoke system as you'd get in like a uh TV or um uh you know, some of the older um instruments we've seen on the uh blog before which use magnetic deflection.

**Dave Jones:** This has electrostatic uh plates and there's no wiring coming in from the side at all. All comes straight out of the uh neck end here. There's a bit of uh system dodgy-ness going here.

**Dave Jones:** Look, they've got Instead of coming across the main PCB, it's coming from uh the back side of the unit over here. They've got this cable over here with a two-pin header connector that's you know, it plugs into a a right-angle header on this board over here.

**Dave Jones:** Here it is there. So, that's a bit rude. Um I don't like that at all. So, yeah, a bit of an afterthought. Oops, we forgot that pair. We have to run it all the way over the board.

**Dave Jones:** Ah, well, let's just run a cable over. Or maybe there's some electrical reason why they didn't do it, but I don't know. Seems more like an afterthought to me.

**Dave Jones:** And if you take a look at the schematics, because this is a multi-board design, it's interesting to note this is a very common technique. If you have a look at some of the numbers in here, you'll see like this is the ADC and character generator board.

**Dave Jones:** Like U260, Q247, R246, right? All of the Ns and Cs and all the Rs there labeled in the 200s. And that is specifically designed so that you don't duplicate designators over the entire design.

**Dave Jones:** Because, you know, they didn't have like CAD and checking back then and you know, automated stuff like that. So, they go, "Okay, everything on this schematic will just number 200, whether it's a transistor, a you know, an IC, an inductor, a capacitor, whatever.

**Dave Jones:** It'll get the 200 number series." And then you go over here and have a look at this high-voltage board, for example. No, sorry, this is the RMS converter board.

**Dave Jones:** Then everything's in the 100 series. There you go. There's a matched transistor thermally matched transistor pair there. Q194, 188. All the capacitors of the 100, you know, 167. All the resistors, everything else numbered in the 100 series.

**Dave Jones:** And I took that shield off our high-voltage board down in here. And haha, what do we find? There's our voltage multiplier. There you go. There's our diodes in there and our caps for our voltage multiplier.

**Dave Jones:** We can have a look at the schematic over here. Here it is. Classic topology. And we've got some handwritten notes up here. There we go. It should never exceed 450 volts.

**Dave Jones:** This voltage is highly dependent upon the battery the the condition of the battery. So there you go. Should not exceed 450 volts. Somebody's handwritten quite a few things on this schematic here.

**Dave Jones:** So that's rather neat. But there you go. There's our high voltage multiplier right under there. Well, hey, look at that. We have ourselves a high voltage ceramic resistor in there by the looks of it and with its own little insulator wire going all the way back over there.

**Dave Jones:** That one was most likely I can't see the silkscreen on the back. But most likely that 100 meg resistor in there. There you go. Unfortunately, it looks like we're missing the schematic for this baseboard here cuz it's got part numbers in the 300 range and none of the schematic sheets I've got here actually have the 300 range on them.

**Dave Jones:** And it's a shame cuz there's a very interesting little packaged IC part around here. I'll try and get at it. I might have to take the CRT out for that.

**Dave Jones:** And there you go. I popped out the CRT there and well, we've got a socketed strangely RCA chip. I don't know why it's socketed, but yeah, it's got a weird-ass part number on it.

**Dave Jones:** And check out this puppy down here. Another tech custom part in one of those weird-ass packages. And of course, I'm going to show you a close-up of that. Why wouldn't I?

**Dave Jones:** Look at that. Beautiful. Now here's the main function board. Nice classic gang switch arrangement here. Just beautiful. A couple of you know, bodgy mods on there. Look, I got some resistors all seriesed up.

**Dave Jones:** Some caps going from there to there. That's obviously some sort of afterthought. They've decided to whack that on there. You know, even some wiring here. Why they haven't got that on the board?

**Dave Jones:** I don't know. Did they run out of space? Meh, who knows? But anyway, yeah, quite a dense little arrangement here. Once again, more board-to-board interconnects top and bottom. So imagine trying to design this system from a cube arrangement.

**Dave Jones:** I've designed these actually full cubes where there's boards on all six sides. And trust me, it ain't easy. Even doing a four-board wrap-around like this and grounds can be a real big problem and things like that.

**Dave Jones:** So, yeah, real pain in the ass. But anyway, that's a quite dense little board there. That's obviously the front end is on the other side of it over here.

**Dave Jones:** And unfortunately, I may not be able to get to that board cuz I can't figure out how to get all this plastic off. I don't seem to see how it's all held in there.

**Dave Jones:** So, yeah, I may not go to the effort to actually do that. But anyway, yeah, if you want to it's just more of you know, more similar construction. Although we do have our rotary switches on there.

**Dave Jones:** And you can actually see the mechanism. There's part of the mechanism there, part of the contacts there. And other parts would be that metal right in there with that those through-hole terminals in there.

**Dave Jones:** That would they'd have contacts in there. And that'd be all part of the that switch. That's the volts per division and also the ohms and range selection and things like that.

**Dave Jones:** So, that's a multi-purpose switch. Real complex custom arrangement in that. Nasty business. And as for the scope front end here, well, it is a basic analog scope front end as you'd find in any scope.

**Dave Jones:** Here's the probe here. We've got our selectable AC DC input coupling here. We've got our input resistances with our frequency compensation as well as a 10 meg input resistor.

**Dave Jones:** And pretty much that's coupling into a matched JFET input pair. So, yeah, pretty odd, you know, just run-of-the-mill stuff. It's only got a bandwidth of 1 megahertz. Nothing fancy going on here at all.

**Dave Jones:** Basically, the only thing you're not going to find in a classic analog scope is the switch in the switch through to the meter. You can see how it switches the probe through here or it switches it through to some of the multimeter input circuitry here.

**Dave Jones:** Here's the milliamp ohms. Here's the ohms current source right down here. And then likewise on the output of the input buffer the JFET input buffer here. Then we've got some switching that goes through to the analog DMM circuitry all the vertical circuitry here.

**Dave Jones:** So it just switches that through whichever mode you're in and it's got all the range switching uh stuff up here. It's showing all that. Unfortunately, we can't see the rest of it here cuz somebody has included some sort of modern circuit here and um yeah, I'm not sure what relevance that actually has.

**Dave Jones:** Haven't looked into it, but yeah, there's obviously some more vital stuff missing there cuz we've got these switching lines going up here. So they're going up to some sort of switching diagram up there or something like that perhaps.

**Dave Jones:** So yeah, I don't think there's a whole lot of insight to be gained by ripping apart all this module and seeing that uh top side of the input board there that actually has the multimeter input terminals there soldered directly onto the board in there.

**Dave Jones:** There we go. It looks like that might be some sort of ceramic um uh resistor divider module that you'd find in any multimeter uh front end of the day.

**Dave Jones:** So, you know, yeah, pretty ordinary type stuff. The pots are mounted directly on the board down in there and the switches down in there and there's some shielding on top of that as well, I believe, coming from the other side.

**Dave Jones:** So, yeah, that's about all she wrote for the input circuitry on that thing, but there you go. That's pretty much the teardown in a nutshell. Look at that. Ah, that CRT is just so cute.

**Dave Jones:** Look at it. Ah, thing of beauty and a joy forever. So there you go. I hope you found that teardown of the classic 1975 vintage even though it was built in the '81.

**Dave Jones:** So, it had a bit of a life there. Although, I don't think it had much of a life after '81, probably. I don't know, but if anyone's got a final um you know, build or uh sell date on this thing, then please let us know.

**Dave Jones:** How long was the product lifetime? Anyway, that was Tektronix 213. Uh portable, not really pocket, but portable multimeter {slash} DMM. And this thing would have been killer in its day.

**Dave Jones:** And you got to remember this is practically 40 years ago, and it still works. Unbelievable. Still a marvel of technology, really. I mean, you know, there's not much more you can you could like if you had to do it with a CRT this day these days, the CRT is not going to be any smaller pretty much, and pretty much you can shrink some of the other circuitry, but it's not going to

**Dave Jones:** be a hell of a lot smaller. So, there you go. My hat's off to the Tektronix designers back then. This absolutely fantastic design to package all this, and you know, systems engineering that goes into creating that uh cube arrangement, that four-sided board arrangement, all interacting and board-to-board interconnects.

**Dave Jones:** That ain't easy, folks. I can tell you. So, very very impressed. I hope you enjoyed that, and if you did, please give it a big thumbs up. And if you want to discuss it, please jump on over to the EEVblog forum, or leave a comment on YouTube, or in the blog comments.

**Dave Jones:** I do read all of the comments. I try I do, and I try to reply to as many as possible, even though it takes me a lot lot of hours to do that.

**Dave Jones:** Ah, well, it's good fun. I love reading the comments. Catch you next time.
