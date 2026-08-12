---
video_id: czv_8d66IQU
title: EEVblog #628 - Tektronix 213 Vintage Portable Oscilloscope Teardown
url: https://www.youtube.com/watch?v=czv_8d66IQU
source: youtube-asr
timestamps: {"0": 4, "1": 19, "2": 32, "3": 42, "4": 61, "5": 77, "6": 97, "7": 112, "8": 132, "9": 147, "10": 160, "11": 180, "12": 193, "13": 205, "14": 222, "15": 236, "16": 256, "17": 274, "18": 289, "19": 303, "20": 313, "21": 332, "22": 345, "23": 359, "24": 372, "25": 385, "26": 403, "27": 416, "28": 429, "29": 442, "30": 457, "31": 470, "32": 484, "33": 497, "34": 510, "35": 523, "36": 541, "37": 554, "38": 565, "39": 580, "40": 592, "41": 606, "42": 621, "43": 639, "44": 652, "45": 668, "46": 684, "47": 697, "48": 711, "49": 724, "50": 739, "51": 754, "52": 766, "53": 781, "54": 792, "55": 808, "56": 824, "57": 835, "58": 851, "59": 872, "60": 888, "61": 902, "62": 917, "63": 931, "64": 944, "65": 954, "66": 969, "67": 983, "68": 997, "69": 1009, "70": 1021, "71": 1033, "72": 1041, "73": 1055, "74": 1068, "75": 1083, "76": 1099, "77": 1114, "78": 1129, "79": 1143, "80": 1158, "81": 1169, "82": 1180, "83": 1198, "84": 1213, "85": 1227, "86": 1245, "87": 1260, "88": 1277, "89": 1288, "90": 1301, "91": 1318, "92": 1332, "93": 1344, "94": 1361, "95": 1374, "96": 1390, "97": 1402, "98": 1416, "99": 1430, "100": 1445, "101": 1461, "102": 1477, "103": 1493, "104": 1506, "105": 1521, "106": 1534, "107": 1547, "108": 1559, "109": 1575, "110": 1589, "111": 1607, "112": 1617, "113": 1631, "114": 1647, "115": 1659, "116": 1671, "117": 1689, "118": 1699}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Quick announcement before we get into it. For those who have been asking where can I get one of these warranty void if not removed t-shirts? Well, you obviously missed my previous Teespring crowdfunding campaign for it. So, I've

**Dave Jones:** started again. For those who have asked, the link is down below. If you want one, they're pretty cheap. They're only 15 bucks and pretty cheap postage within the US. Other countries a bit more expensive, but hey, it's not bad at all. Certainly

**Dave Jones:** cheaper than my Zazzle store originally was. So, if you want to nab one, the campaign only runs for a short time. So, the link is down below. Go and nab one if you want it. They're available in women's

**Dave Jones:** styles and hoodies and winter jumpers and all sorts of things. So, excellent warranty void if not removed. I love it. Anyway, we're going to take a look at this Tektronix. Look at this. This Tektronix 213 handheld um not quite a pocket oscilloscope. If

**Dave Jones:** you had a really big pocket, you could call it a pocket oscilloscope. But, vintage handheld portable scope from 1975. Fantastic vintage technology. Had this hanging around for a while. Got it in the mailbag. So, let's check it out. And

**Dave Jones:** here it is. Isn't it just gorgeous? Look at this. State-of-the-art technology in 1975. And not only is it an oscilloscope as you'd expect. It's a 1 MHz oscilloscope by the way. 1 MHz bandwidth. Look at that nice crisp trace on that. It's just

**Dave Jones:** beautiful. But, yeah, not not a huge bandwidth, but good enough for a portable scope, especially for 1975. But, it's also a multimeter as well and a pretty decent multimeter at that. It's a 3 and 1/2 digit, but it's 0.1%

**Dave Jones:** plus one count motor meter. It does milliamps and ohms and also true RMS AC as well. So, pretty impressive stuff. Look at that. Generating the characters with the CRT. There's a specific custom CRT character generator chip inside this thing which

**Dave Jones:** we'll see. And yes, we do have the full schematics for this baby. But look at this. Isn't it just a thing of beauty? Really. And these are the input controls here. Here's your multimeter input jacks. They didn't use the BNC. The BNC is on the

**Dave Jones:** back. By the way, there's nothing else there on the back. But we can change the intensity and we can change the calibration of the horizontal and the vertical as well. And we can change the trigger. And it's got auto trigger mode

**Dave Jones:** and AC DC input coupling. No, it is not an isolated scope. But hey, you know. For a portable scope, ah, fantastic. I don't think anything else ever matched this thing. Really. And to have a CRT inside that, that is

**Dave Jones:** terrific. I mean, granted it is a really small screen. But hey, very useful back in its day, I'm sure. 1975. Not sure exactly when this one was manufactured. We'll find out when we open it up and take a look at the date code. So, let's

**Dave Jones:** go. So, a big thanks to Derek White who sent this in to the mail bag some time ago. Sorry it's taken me a while to get around to it. Look at that. That's really quite nice. I think there's only

**Dave Jones:** four screws on the bottom. Here, there's two on the front which hold this uh Oh, yeah. There we go. Can't get that one out. But anyway, and there's looks like there's two on the back here. And 1975. Well, it's all going to be

**Dave Jones:** it's all going to be dip uh componentry, that's for sure. Dip ICs, the custom character generator on there's some 4000 series CMOS. And yes, we do have the full schematics, which I'll show you later, and which I'll link in down

**Dave Jones:** below. And there's actually a wiki uh page on the tech wiki. Looks like the lid does come off here. Hey, hello. Whoa. Hey. Whoa, look at that. There's a bit of uh 40-year-old crustiness. I mean, you got to remember,

**Dave Jones:** this is 40 years old, 1975. Goodness. I mean, you know, that's just incredible. And look at this. It looks like it's a uh very nice little That's obviously for the uh internal battery, cuz this thing did have a battery, and that's probably

**Dave Jones:** where all that gunk uh came from. So, there's a cutout in there for that. But apart from that, look at this. It's a nice little uh sort of cube construction. Oh, well, yeah, there's a board on the bottom as well. So, there's

**Dave Jones:** board on all Well, no, not on this end, and not on that end, but all four sides are wrapped around like that. So, that's really quite neat. Actually, I hope they can pull apart. I hope they're not so

**Dave Jones:** Oh, no, yes, they are. I think they're plug-on boards. I can just lift that I should be able to just lift those boards out. So, there you go. Look at that. That is a thing of beauty. Look at the

**Dave Jones:** tiny little electrostatic CRT in there. I love it. Ah. Well, it's even earlier than that. Look at this. Copyright 1973 Tektronix Corp. So, it's more than 40 years old. Ah, can you believe it? Unbelievable. This is like, you know,

**Dave Jones:** just after the Apollo uh program finished. It's just incredible. But look, we have a date code here of '81. I don't know whether or not it was manufactured in '81, or there was some other mod, or something else happened. That could have been

**Dave Jones:** like, you know, tested by KW, I guess, um, in '81, perhaps. Anyway, we'll find out that once we get to the, uh, date code of the ICs. That'll be dead giveaway. There's a few adjustments on here, too. We've got plus 15 V adjust. I

**Dave Jones:** assume that's, uh, some sort of power rail. We've got charge adjust. We've got high voltage adjust. There we go. Character spacing adjust over here. This is like a link, I believe. I've had a quick look at the schematics and I think

**Dave Jones:** there was like a a jumper link in there that actually, uh, set how much, uh, spacing you have between the characters on the, uh, CRT. I'm not sure why you'd adjust that, but anyway, uh, DC calibration jumper. So, there's a jumper

**Dave Jones:** link. Um, DC cal, as well. Ohms adjust. Times 10 gain and, uh, DC zero and AC zero and AC gain. Oh, man. More adjustments you can poke an adjustment screwdriver at. So, what I'm going to do is try and lever this

**Dave Jones:** board out here and, uh, I'll show you in a, uh, no, hang on. I might have to take those. Looks like those nuts come out. All right. No, I'm stuck. These things, they do have, uh, board-to-board headers on

**Dave Jones:** here, but, yeah, it looks like those nuts have to come out. And check out also the classic black silk screen on the reverse side of these boards. Look at that. Terrific stuff. The other ones are actually, um, uh,

**Dave Jones:** etched into the copper on there, but, yeah, we do actually have, um, some, uh, silk screen overlay on bottom. And thoughtfully, these are the dip packages here. Thoughtfully, they've put them, you know, in exactly the right space on

**Dave Jones:** the back for servicing. I mean, that's terrific. Somebody was thinking. All right, she's just going to pop right out now. Ta-da! There we go. There's our first board. That's probably going to have our, uh, character generator ROM on there. These look like

**Dave Jones:** your custom, uh, Tektronix chips. So, we'll take a closer look at those, but, oh, look at that big ass cap. And there's the money shot, two custom tech chips. This is uh U270. We'll have a look at the schematic in a second. This

**Dave Jones:** is the uh character generator ROM. So, it basically gives the uh X, Y, and Z axis outputs and decimal uh point blanking and all that sort of stuff. And that's fed from this uh four-digit decade counter here, and you'll see that

**Dave Jones:** on the schematic. That's also a a custom uh tech chip of some description. So, look at that. And this is So, this is the combined analog Well, it tells you over here the analog to digital board, but also the character generators. So,

**Dave Jones:** basically, we're looking at some uh trim pot adjustments up there. They were the um ohms and DC uh volts adjust. Got some couple of discrete uh transistors. I'm not sure if that's a a input uh coupling cap or the sampling cap. We'll have a

**Dave Jones:** look at it in a minute. Um there's a funky-looking diode package. We'll check that out. Look at that. It's got a diode symbol on there. I've never never seen something like that before. That is bizarre. Then we've got

**Dave Jones:** ourselves an MC1456 op amp, and then going into a 74L double O. Oh, classic low-power TTL 74L series. I haven't seen those in a long time, but that's just doing some uh latching uh stuff. They're using four uh NAND gates

**Dave Jones:** there to do some latching. Um and that's pretty much it. Look at those funky capacitors, would you? They don't make them like they used to. There you go, decode the color code. Awesome. And yep, it turns out that's just a dual diode

**Dave Jones:** package. There's actually two pins on the other side. You can barely see them there. So, just two diodes in one package. I'm not sure if they're designed to be uh thermally bonded and matched. And you can see pretty much

**Dave Jones:** what's happening here. Here's our uh Zener reference here. So, our 6.2 V uh Zener reference. There's the CR217 I was talking about there. And where is it? They've got it down here as well. So, they've got that coupling over to

**Dave Jones:** the input to our counter over here. So, we've got a slope converter happening here. You'll see that in the rest of it. And yeah, there we go. Here's our integrator C227. And that is certainly that one there. So,

**Dave Jones:** that's our integrator capacitor. That's why it's so schmick. And pretty much yeah, voltage reference and then the ohms adjust here, which is one of these trim pots up here. And then that's all just going into a couple of latches and

**Dave Jones:** into our four-digit decade counter, which as I said is this one over here. And our NAND gates is our two NAND gates is two latches there. Nice little wave forms on these schematics here. I love it. They got voltage test points.

**Dave Jones:** Brilliant. They don't make schematics like this anymore. But yeah, that's pretty much all it is. This is a custom four-digit decade counter or four-decade counter here. And that here's the binary. Here's the decade, you know, the digit outputs

**Dave Jones:** here. And the digit outputs are fed into the character generator ROM down here. And the character generator ROM, unfortunately, we don't have any info on that. But it does all the magic and then outputs the XY and Z axis. And that goes

**Dave Jones:** off to the CRT only when you've switched it in, of course, in multimeter mode. It's disabled in scope mode. And then as I said, they've got the decimal point spacing enable pin here. So, this was that strapping we saw on the back of the

**Dave Jones:** PCB there. But yeah, there's not a huge amount to this. I mean, this is the analog to digital converter portion. It's all old school. There's no ADC chip as such in this thing. It does it using slope conversion. Terrific stuff.

**Dave Jones:** So, basically what this is doing here, the decade counter, that actually does the counting direct from the ADC. It starts at zero, counts it up and gives you your value, and then it multiplexes the output here and actually then that

**Dave Jones:** goes through the character generator ROM. So, it'll cycle through each one of the digits, and there's the digit transistors up here, and you can see that it would pass each digit directly through to the character generator ROM. So, all the character generator ROM has

**Dave Jones:** to do is convert that digit into a specific waveform data, but there'd be a lot of magic happening in there. I'd love to get some info on that. If anyone's got anything on that character generator ROM, please leave it in the

**Dave Jones:** comments. Now, you can see how they do the board-to-board interconnect here. They've got like those sort of like surface-mount crimp type pins that are designed to go into the normally like a you know a Molex mating block connector, something like that.

**Dave Jones:** Well, they soldered those pins directly onto the board, essentially surface-mount soldered them. I don't think that there's any that they're through-hole pins protruding through the and these things wouldn't be easy to solder as well. You wouldn't just solder

**Dave Jones:** them freehand one by one. You'd have either the original board in place like this or more likely some sort of soldering alignment jig where you'd plug the pins into the sockets and then solder them in so they're all nicely

**Dave Jones:** lined and then you'd pull the board out. And although this thing is a marvel of sort of you know systems engineering and integration to get it into this, sort of they couldn't really go the whole hog and have a proper PCB mounted

**Dave Jones:** BNC on here. So, they had to have a coax going down there, stuff it in, and insulate the back of this BNC connector down in here. It's a bit of a shame that they couldn't you know do that a bit

**Dave Jones:** better, but well, you know, what's a bit of wire in back in 1975? Now, is that my imagination or is that BNC not factory original? I think it could be a modern replacement, I suspect. And look at this.

**Dave Jones:** This is the mating BNC hole for that. It doesn't look like it's been factory done. It looks like somebody has hacked that thing out. Hmm. And check out the mains wiring. I mean, it's all pretty how-you-doing. And like there's no

**Dave Jones:** proper cable clamping or anything here. It just sort of comes out there. It's sort of wrapped It's not even wrapped around the post for a bit of strain relief or something like that. It's just got a bend in there right at the back

**Dave Jones:** neck of the CRT here and then soldered directly onto the PCB. Hey, at least it's fused. Danger. AC voltage and CRT. Approximately 1,200 V potentials are present under this area. Here's the main board. I popped it out. Battery charger

**Dave Jones:** test point. There you go. And ground plus 75 V, plus 15 V, and plus 6. plus minus 6.5 V in this CRT grid bias there. And that is our board. Ta-da! That's our CRT drive That's our main power supply that

**Dave Jones:** takes the 240 V in and converts it down. So is it Looks like some sort of uh uh switching converter or something to that effect. And then uh uh bit of CRT driver business happening there. And And here's a schematic for

**Dave Jones:** our main power supply and battery charging board. We've got some Here's our AC input here. We've got some uh filtering happening there. There you go. Common mode choke. Got a bridge rectifier straight on the mains coming across. Uh that's the battery charger

**Dave Jones:** converter circuitry. That says uh Those diodes and inductors and cap there are on a substrate. So I'm not sure Oh, inner shield, outer shield. Oh, okay. So this is all underneath the main shielding on the board there. I think

**Dave Jones:** that's what they're talking about. And uh then Oh, look. We've got ourselves a multi-vibrator there. Absolutely classic. You can tell that building block a mile away. And then here's our inverter over here and now that's all part of the regulation circuitry. And

**Dave Jones:** the inverter, by the way, is hanging If you're wondering where it is, where's the transformer? Well, here it is up here. And they've got it so they've got it in a separate can there and that's what this wire comes

**Dave Jones:** over and then attaches to this board over here like that. So, yeah, they've mounted that completely off board. So, once again, you know, not enough room in there cuz you've got to fit your CRT and everything else. Oh, we've got a little

**Dave Jones:** bit of volume left there. Let's whack our big ass transformer in there and just wire it over. Not a problem. Bob's your uncle. And check out this. Little modification notes. Somebody has done this. Look at 4th of the 11th,

**Dave Jones:** 2011. I downloaded this schematic. So, wherever they got it from, I don't know. They scanned it in from somewhere, but somebody's done this hand mod in there. So, there you go. That's a really aftermarket mod, that one, I think.

**Dave Jones:** There we go. We can really see those little board-to-board contact like Molex type pins there. And yeah, they do have a little tab which goes into the hole in the board there. That's how they hold them in place during

**Dave Jones:** soldering there. But yeah, they don't actually pins don't protrude through the other side. So, there you go. They could be purpose designed for that rather than just bodged from some some connector. And the other part of the CRT driver

**Dave Jones:** board down the bottom. This is a big board which goes basically the full base of the unit. It's got a big cutout in the middle for the battery and a couple of more trimmers down in there which don't have an external hole on the side.

**Dave Jones:** So, these would have have to have been trimmed on the bench before they installed all of this stuff. But once you put that board in there, you can't Oh, no. No, there we go. Sorry. They've got the trimmer holes through the board.

**Dave Jones:** There you go. So, yeah, you can actually install the board first and then trim them afterwards. But you wouldn't be able to do it once it's in the case. So, this whole thing has to lift out as an

**Dave Jones:** assembly. Huh, speak of the devil. There we go. Yeah, it all just popped out of the case very nicely. And you could, once you put all this in, um you know, pretty nicely adjust and trim this thing on the bench before you whack

**Dave Jones:** it in the case. It really is quite a lovely assembly. It's almost a work of art. And here we go. We can see the bottom of this thing. And uh we've got a so some red silkscreen. Now, doesn't that look

**Dave Jones:** lovely? Red and green. Ah, beautiful. And uh danger 1,200 V. Look at this. The PCB designer really knew this stuff. They're marking out the dangerous uh voltage side of the thing. All these contacts right around there. Terrific stuff. Oh, yeah. I forgot to mention the

**Dave Jones:** date code, by the way. Uh 37th week 1980. So, there you go. We're talking late 88 1980s for the chips. So, yeah. Certainly this thing looks like it was manufactured in uh '81 as it uh says in various locations around here. There we

**Dave Jones:** go. 51 50 Is that 51st week '81? I think it might be. Got ourselves a nice little uh shield in plate in there from this CRT. This is an electrostatic uh CRT, of course, as I mentioned. So, you get no

**Dave Jones:** uh deflection uh magnetic deflection coil uh yoke system as you'd get in like a uh TV or um uh you know, some of the older um instruments we've seen on the uh blog before which use magnetic deflection. This has electrostatic uh plates and

**Dave Jones:** there's no wiring coming in from the side at all. All comes straight out of the uh neck end here. There's a bit of uh system dodgy-ness going here. Look, they've got Instead of coming across the main PCB, it's coming from uh the back

**Dave Jones:** side of the unit over here. They've got this cable over here with a two-pin header connector that's you know, it plugs into a a right-angle header on this board over here. Here it is there. So, that's a bit rude. Um I don't like

**Dave Jones:** that at all. So, yeah, a bit of an afterthought. Oops, we forgot that pair. We have to run it all the way over the board. Ah, well, let's just run a cable over. Or maybe there's some electrical reason why they didn't do it, but I

**Dave Jones:** don't know. Seems more like an afterthought to me. And if you take a look at the schematics, because this is a multi-board design, it's interesting to note this is a very common technique. If you have a look at some of the

**Dave Jones:** numbers in here, you'll see like this is the ADC and character generator board. Like U260, Q247, R246, right? All of the Ns and Cs and all the Rs there labeled in the 200s. And that is specifically designed so that you

**Dave Jones:** don't duplicate designators over the entire design. Because, you know, they didn't have like CAD and checking back then and you know, automated stuff like that. So, they go, "Okay, everything on this schematic will just number 200, whether it's a transistor, a you know,

**Dave Jones:** an IC, an inductor, a capacitor, whatever. It'll get the 200 number series." And then you go over here and have a look at this high-voltage board, for example. No, sorry, this is the RMS converter board. Then everything's in the 100 series. There you go. There's

**Dave Jones:** a matched transistor thermally matched transistor pair there. Q194, 188. All the capacitors of the 100, you know, 167. All the resistors, everything else numbered in the 100 series. And I took that shield off our high-voltage board down in here. And haha, what do we

**Dave Jones:** find? There's our voltage multiplier. There you go. There's our diodes in there and our caps for our voltage multiplier. We can have a look at the schematic over here. Here it is. Classic topology. And we've got some handwritten notes up

**Dave Jones:** here. There we go. It should never exceed 450 volts. This voltage is highly dependent upon the battery the the condition of the battery. So there you go. Should not exceed 450 volts. Somebody's handwritten quite a few things on this schematic here. So

**Dave Jones:** that's rather neat. But there you go. There's our high voltage multiplier right under there. Well, hey, look at that. We have ourselves a high voltage ceramic resistor in there by the looks of it and with its own little insulator

**Dave Jones:** wire going all the way back over there. That one was most likely I can't see the silkscreen on the back. But most likely that 100 meg resistor in there. There you go. Unfortunately, it looks like we're missing the schematic for this

**Dave Jones:** baseboard here cuz it's got part numbers in the 300 range and none of the schematic sheets I've got here actually have the 300 range on them. And it's a shame cuz there's a very interesting little packaged IC part around here. I'll try

**Dave Jones:** and get at it. I might have to take the CRT out for that. And there you go. I popped out the CRT there and well, we've got a socketed strangely RCA chip. I don't know why it's socketed, but yeah, it's got a

**Dave Jones:** weird-ass part number on it. And check out this puppy down here. Another tech custom part in one of those weird-ass packages. And of course, I'm going to show you a close-up of that. Why wouldn't I? Look at that. Beautiful. Now

**Dave Jones:** here's the main function board. Nice classic gang switch arrangement here. Just beautiful. A couple of you know, bodgy mods on there. Look, I got some resistors all seriesed up. Some caps going from there to there. That's obviously some sort of afterthought.

**Dave Jones:** They've decided to whack that on there. You know, even some wiring here. Why they haven't got that on the board? I don't know. Did they run out of space? Meh, who knows? But anyway, yeah, quite a dense little arrangement here. Once

**Dave Jones:** again, more board-to-board interconnects top and bottom. So imagine trying to design this system from a cube arrangement. I've designed these actually full cubes where there's boards on all six sides. And trust me, it ain't easy. Even doing a four-board

**Dave Jones:** wrap-around like this and grounds can be a real big problem and things like that. So, yeah, real pain in the ass. But anyway, that's a quite dense little board there. That's obviously the front end is on the other

**Dave Jones:** side of it over here. And unfortunately, I may not be able to get to that board cuz I can't figure out how to get all this plastic off. I don't seem to see how it's all held in there. So, yeah, I may not go to

**Dave Jones:** the effort to actually do that. But anyway, yeah, if you want to it's just more of you know, more similar construction. Although we do have our rotary switches on there. And you can actually see the mechanism. There's part of the

**Dave Jones:** mechanism there, part of the contacts there. And other parts would be that metal right in there with that those through-hole terminals in there. That would they'd have contacts in there. And that'd be all part of the that switch. That's the

**Dave Jones:** volts per division and also the ohms and range selection and things like that. So, that's a multi-purpose switch. Real complex custom arrangement in that. Nasty business. And as for the scope front end here, well, it is a basic

**Dave Jones:** analog scope front end as you'd find in any scope. Here's the probe here. We've got our selectable AC DC input coupling here. We've got our input resistances with our frequency compensation as well as a 10 meg input resistor. And pretty

**Dave Jones:** much that's coupling into a matched JFET input pair. So, yeah, pretty odd, you know, just run-of-the-mill stuff. It's only got a bandwidth of 1 megahertz. Nothing fancy going on here at all. Basically, the only thing you're not going to find in a classic analog scope

**Dave Jones:** is the switch in the switch through to the meter. You can see how it switches the probe through here or it switches it through to some of the multimeter input circuitry here. Here's the milliamp ohms. Here's the ohms current source

**Dave Jones:** right down here. And then likewise on the output of the input buffer the JFET input buffer here. Then we've got some switching that goes through to the analog DMM circuitry all the vertical circuitry here. So it just switches that

**Dave Jones:** through whichever mode you're in and it's got all the range switching uh stuff up here. It's showing all that. Unfortunately, we can't see the rest of it here cuz somebody has included some sort of modern circuit here and um yeah,

**Dave Jones:** I'm not sure what relevance that actually has. Haven't looked into it, but yeah, there's obviously some more vital stuff missing there cuz we've got these switching lines going up here. So they're going up to some sort of switching diagram up there or something

**Dave Jones:** like that perhaps. So yeah, I don't think there's a whole lot of insight to be gained by ripping apart all this module and seeing that uh top side of the input board there that actually has the multimeter input terminals there

**Dave Jones:** soldered directly onto the board in there. There we go. It looks like that might be some sort of ceramic um uh resistor divider module that you'd find in any multimeter uh front end of the day. So, you know,

**Dave Jones:** yeah, pretty ordinary type stuff. The pots are mounted directly on the board down in there and the switches down in there and there's some shielding on top of that as well, I believe, coming from the other side. So, yeah, that's about all she

**Dave Jones:** wrote for the input circuitry on that thing, but there you go. That's pretty much the teardown in a nutshell. Look at that. Ah, that CRT is just so cute. Look at it. Ah, thing of beauty and a joy forever.

**Dave Jones:** So there you go. I hope you found that teardown of the classic 1975 vintage even though it was built in the '81. So, it had a bit of a life there. Although, I don't think it had much of a

**Dave Jones:** life after '81, probably. I don't know, but if anyone's got a final um you know, build or uh sell date on this thing, then please let us know. How long was the product lifetime? Anyway, that was Tektronix 213.

**Dave Jones:** Uh portable, not really pocket, but portable multimeter {slash} DMM. And this thing would have been killer in its day. And you got to remember this is practically 40 years ago, and it still works. Unbelievable. Still a marvel of

**Dave Jones:** technology, really. I mean, you know, there's not much more you can you could like if you had to do it with a CRT this day these days, the CRT is not going to be any smaller pretty much, and

**Dave Jones:** pretty much you can shrink some of the other circuitry, but it's not going to be a hell of a lot smaller. So, there you go. My hat's off to the Tektronix designers back then. This absolutely fantastic design to package

**Dave Jones:** all this, and you know, systems engineering that goes into creating that uh cube arrangement, that four-sided board arrangement, all interacting and board-to-board interconnects. That ain't easy, folks. I can tell you. So, very very impressed. I hope you enjoyed that, and if you did,

**Dave Jones:** please give it a big thumbs up. And if you want to discuss it, please jump on over to the EEVblog forum, or leave a comment on YouTube, or in the blog comments. I do read all of the comments.

**Dave Jones:** I try I do, and I try to reply to as many as possible, even though it takes me a lot lot of hours to do that. Ah, well, it's good fun. I love reading the comments. Catch you next time.
