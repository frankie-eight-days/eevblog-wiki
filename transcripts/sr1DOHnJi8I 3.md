---
video_id: sr1DOHnJi8I
title: EEVacademy | Digital Design Series Part 4 - Digital Logic Datasheets Explained
url: https://www.youtube.com/watch?v=sr1DOHnJi8I
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 25, "3": 38, "4": 55, "5": 69, "6": 86, "7": 101, "8": 118, "9": 132, "10": 145, "11": 160, "12": 176, "13": 191, "14": 208, "15": 225, "16": 240, "17": 257, "18": 273, "19": 286, "20": 297, "21": 310, "22": 322, "23": 336, "24": 359, "25": 375, "26": 391, "27": 409, "28": 424, "29": 438, "30": 456, "31": 476, "32": 489, "33": 507, "34": 524, "35": 540, "36": 556, "37": 571, "38": 592, "39": 609, "40": 625, "41": 645, "42": 666, "43": 682, "44": 700, "45": 717, "46": 730, "47": 743, "48": 757, "49": 771, "50": 792, "51": 810, "52": 824, "53": 841, "54": 861, "55": 879, "56": 896, "57": 912, "58": 927, "59": 940, "60": 956, "61": 978, "62": 993, "63": 1011, "64": 1029, "65": 1052, "66": 1068, "67": 1088, "68": 1102, "69": 1120, "70": 1135, "71": 1148, "72": 1163, "73": 1181, "74": 1195, "75": 1214, "76": 1232, "77": 1249, "78": 1269, "79": 1286, "80": 1300, "81": 1314, "82": 1335, "83": 1358, "84": 1373, "85": 1387, "86": 1405, "87": 1419, "88": 1433, "89": 1448, "90": 1468, "91": 1489, "92": 1504, "93": 1520, "94": 1534, "95": 1552, "96": 1568, "97": 1584, "98": 1597, "99": 1611, "100": 1626, "101": 1645, "102": 1664, "103": 1678, "104": 1697, "105": 1708, "106": 1720, "107": 1732, "108": 1747, "109": 1761, "110": 1777, "111": 1794, "112": 1812, "113": 1827, "114": 1841, "115": 1853, "116": 1869, "117": 1886, "118": 1906, "119": 1923, "120": 1942, "121": 1957, "122": 1968, "123": 1983, "124": 1999, "125": 2017, "126": 2032, "127": 2047, "128": 2064, "129": 2079, "130": 2094, "131": 2111, "132": 2130, "133": 2144, "134": 2163, "135": 2177, "136": 2191, "137": 2206, "138": 2221, "139": 2231, "140": 2243, "141": 2258, "142": 2272, "143": 2289, "144": 2302, "145": 2316, "146": 2330, "147": 2343, "148": 2361, "149": 2375, "150": 2389, "151": 2406, "152": 2424, "153": 2443, "154": 2457, "155": 2472, "156": 2493, "157": 2513, "158": 2525, "159": 2544, "160": 2558, "161": 2580, "162": 2598, "163": 2610, "164": 2623, "165": 2639, "166": 2654, "167": 2670, "168": 2686, "169": 2699, "170": 2711, "171": 2725, "172": 2740, "173": 2771, "174": 2787, "175": 2803, "176": 2819, "177": 2839, "178": 2855, "179": 2869, "180": 2885, "181": 2897, "182": 2912, "183": 2929, "184": 2943, "185": 2956, "186": 2968}
---

**Dave Jones:** Hi, we're going to take a look at, uh, digital logic data sheets today. We're going to start out with your classic 7400, uh, series logic. In this case, the 74HC00, which is a quad at two input NAND gate.

**Dave Jones:** We're going to go through the data sheet step-by-step, and we're going to take a look at what all this stuff here means, and we're going to go down into the specs and look at all of what this stuff

**Dave Jones:** means. Now, we're going to take a look at the Texas Instruments data sheet here, and different data sheets will be, uh, slightly different in various ways. We might take a look at some others for the, uh, same gate, but your data sheet

**Dave Jones:** start out very typical. They've got the features here, the top-level features. Now, one of the golden rules of, uh, reading data sheets is to not take the banner headline specs here at face value because they could actually not just be

**Dave Jones:** wrong, but not wrong, but misleading. So, they don't tell the full story. You really have to go down to the main specifications further on in the data sheet. Look at all the little astrixes and the little numbers and everything

**Dave Jones:** else to really get a feel for it, but at a general level, it's not too bad, you know? It can tell you the typical operating voltage from 2 volts to 6 volts, uh, for example, the typical, uh, propagation delay, which is TPD there,

**Dave Jones:** uh, the output drive capability, but there's a trap in that one, which we'll uh, take a look at potentially. And classic applications here in data sheets. These are engineers typically get a little bit of a laugh out of these things. They're

**Dave Jones:** really there just for a marketing warm fuzzy. It's like, "Ooh, I'm developing an enterprise tablet. So, oh, look at that. It just so happens that this is the perfect part for that." It's like, "No." Like, it's just ridiculous. I'm

**Dave Jones:** developing a PDA. Wow, it says that this is fantastic. No, we just get a little giggle out of those. Anyway, and often you'll find on the front page here, you'll find what packages they're available in. In this case, they're

**Dave Jones:** available in your regular PDIP, which is plastic jewel in line package. That's the one you used to that plugs into your breadboard. And then it has the associated part number here with it. So, you've got to have the N on the end.

**Dave Jones:** You'll notice that the numbers make a difference. And if you add the NS on the end here, then it's the SO package. So, that's the surface mount package. So, it's very different. So, when you go to order these parts, just be careful that

**Dave Jones:** you do get exactly the right number from Digikey or Mouser or whoever you're actually buying these from. Otherwise, you'll come a cropper and order the wrong package. So, we're looking at the 74HC00, which contains four independent two input gates there. They perform the

**Dave Jones:** Boolean function. And we've gone through Sorry, NAND. We've gone through that in a previous video. Now, we've got our table of contents. Nothing fancy here. Look out for the revision history by the way of these because often they might change

**Dave Jones:** some important stuff from revision either F. What have they added? They've changed the ESD. They've added the ESD ratings table. Have they? Yes, maybe the old data sheet didn't have that, for example. Uh added a military disclaimer and things like But, they can often be

**Dave Jones:** really important changes, especially in complex modern devices like microcontrollers, for example, can have really important differences in the revision history. They can have all sorts of silicon bugs. And then we've got our typical pin outs here. These are

**Dave Jones:** for pretty much all of the packages. So, for the SSOP, the SOIC surface mount ones for the uh DIP uh plastic DIP, the ceramic DIP packages. Oh, by the way, we didn't show up the top here that uh the

**Dave Jones:** 54HC, this is the military uh version, the 5400 series, and that has a ceramic uh DIP package version. It's just a more robust version, you know, than your regular uh plastic DIP package here cuz the military like the ceramic

**Dave Jones:** DIP. So, anyway, let's not get mixed up in that. So, you've got your typical pinouts. Um you've got your pin one identifier up here, and unless they say uh well, yes, they do say here, top view and top view. So, looking down from the

**Dave Jones:** top of the chip. Don't make the mistake of getting that back to front like you often do on these uh like surface-mount leadless chip carriers. You might think, "Ooh, these pins, because they're hidden on the bottom of the chip here like

**Dave Jones:** this, then I've got to flip the chip over in order to look at the uh pins and see which is pin one." Uh-uh, this is top view. So, don't fall for that one, and there's the pin one identifier,

**Dave Jones:** which will typically be a uh silkscreen or a laser-marked uh circle on top of the package. But, not all packages will have that. You've often got to go right down to the bottom of the datasheet, which we'll take a look at later, to get

**Dave Jones:** the physical identifiers. Then you can have a look at the uh pin functions here. The pin function table, as it's called, is often uh very handy. It just it gives you a an overview of what the actual pin is. Like, this is the gate

**Dave Jones:** three input, for example. By gate, uh we're not talking about a MOSFET uh gate, for example. We're talking about a logic gate. So, we're talking about one of the NANDs, remember? This contains four different NAND gates, and they're

**Dave Jones:** actually numbered. Uh this one this first number down here like this. So, one, two, three, and four. So, uh input A, so this is gate number one, input A, gate number one, input B, and gate number one, output Y. And then on your larger

**Dave Jones:** packages here, there's a bunch of NCs or not connected, and it tells you that there's no internal connection there. And of course, ground is ground pin, and VCC is your positive power pin. If you didn't know what VCC means, and well,

**Dave Jones:** where that actual term comes from, we won't get into, but you look in your functional description table. It's the power pin. Thank you very much. Now, here comes probably one of the most important ones here, the absolute maximum ratings. Now, do not exceed

**Dave Jones:** these under almost any circumstances, okay? Because you will basically ruin your device. It'll blow up, the magic smoke will escape, whenever, okay? So, let's take a look at our supply voltage VCC here. A minimum of not.5 because it's a reverse diode protected. Anyway,

**Dave Jones:** we won't go there. It's got a maximum of 7 V. So, do not exceed 7 V, but you might remember from way back up the top here, it said wide operating voltage range of 2 to 6 V. And that is the operating

**Dave Jones:** voltage range. This is the absolute maximum specs. Just because it's on there doesn't mean you can operate this chip at 7 V. No, that's just where you won't do major damage. Okay, let's have a look at this input

**Dave Jones:** clamp current here, and it's plus minus 20 milliamps like this. Now, if you have a look at the conditions under which it's valid, the VI, which is input, is less than zero or VI is greater than VCC. That means the input is less than

**Dave Jones:** is less than the supply rail or greater than the supply rail. And that's important because inside the Let's have a look what's inside the This data sheet actually doesn't have it. Otherwise, I'd show you the diagram, but basically this is uh

**Dave Jones:** the VCC pin. This is the input pin like this. Okay? So, that's our input pin, and then that buggers off to our internal circuitry. They've got these internal clamp diodes here, and that's what they're talking about, the clamping

**Dave Jones:** current. So, when this input here goes, say, plus, you know, 6 V or whatever, that's bigger than VCC up here, which might be 5 V. So, therefore current is going to conduct through the diode here, and that's what they're

**Dave Jones:** saying. You want an absolute maximum there of absolute maximum of plus-minus 20 mA. So, anything over 20 mA, and you risk actually blowing your input clamp diodes. So, don't exceed that. So, how do you avoid exceeding that? Well,

**Dave Jones:** I've erased my little diagram here, but you If you know it's going to clamp, you have an input limit current limiting resistor like that. So, depends on the maximum voltage V max here that you have on the input,

**Dave Jones:** you choose that resistor value to limit the absolute current through that clamping diode to plus-minus 20 mA. If you're looking to protect your device from overloads via this clamping mechanism, which you might if it's hooked up to any

**Dave Jones:** sort of like external circuit, for example. Next up, we've got continuous output current here, or IO. O stands for output, of course. It's plus-minus 25 mA. So, if you've got your NAND gate like this, and you're powering this from,

**Dave Jones:** say, a 2.5 V rail to make it nice, then you basically don't want your load to exceed 100 ohms. If you do, then that's going to exceed the maximum value here of plus minus 25 milliamps. Um the continuous output current. So, the

**Dave Jones:** instantaneous could be higher, but they're not going to tell you that. It's the continuous output current. So, anything lower than 100 ohms, you've exceeded your absolute maximum ratings, and the magic smoke could escape. Don't do that. So, you might think, "Aha, plus

**Dave Jones:** minus 25 milliamps, that sounds pretty grunty. I've got four of these gates. Therefore, I can have a maximum of a 100 4 * 25 or 100 milliamps coming out of this chip." Well, no, you can't. Look at the continuous current through VCC or

**Dave Jones:** ground is only plus minus 50 milliamps here. So, you can only take a maximum of plus minus 50 milliamps continuous from the actual chip. So, if you've got your chip like this, and there's your 5-V rail or whatever it is, and you've

**Dave Jones:** got your four outputs here, the total current on all these four outputs is not to exceed 50 milliamps. Even though you've got that wonderful plus minus 25 milliamps there for each output, the total is not to exceed 50. Otherwise, you'll just

**Dave Jones:** blow up something internal. They'll also tell you what ESD rating this chip is for cuz these most modern chips have ESD protection on the inputs, and they can survive the human body model. It's a We won't go into details, but basically

**Dave Jones:** plus minus 2,000 V can clamp the input, no problems whatsoever. It can survive that electrostatic discharge. But, as always, if you're really looking to protect your devices from external static shock, then you might have an external static clamp that can dissipate

**Dave Jones:** more energy than this particular chip can. But, still, it does have ESD protection built in. Now, up here we saw our absolute maximum ratings. As I said, you are not to use these as a design, you know, specification. You are not to

**Dave Jones:** design for those. They're just absolute You're going to break the damn thing. If you go down here, whoop, here it is. Recommended operating conditions. This is the one you want to design around. So, you saw saw before how we had a

**Dave Jones:** maximum supply rail of 7 V there. No, do not operate at 7 V. It's actually 6 V is the safe recommended operating condition for this chip. So, don't exceed 6 V. Now, Now, of course, we'll have a minimum

**Dave Jones:** operating volts voltage here of 2 V. And, of course, you can go under that if you want. And you're I'm certainly not going to damage your chip, but it's not guaranteed to work. The logic in there is just not going to

**Dave Jones:** function properly unless you've got that 2 V minimum. Now, a very important parameter is VIH and VIL. You'll see this for all sorts of digital logic. It's you know, it's universal across the board. And V stands for voltage, of

**Dave Jones:** course. And then, IH is not IH. It's I and then H. So, I means input, just like O will mean output, and H means high, and L means low in the digital logic scheme. So, VIH here is voltage input high. So, the high level

**Dave Jones:** input voltage. It tells you there. Fantastic. Now, this is actually split into three different specifications here for three different values of your supply voltage, for example. So, the value is actually going to change with the supply voltage. It's a ratiometric,

**Dave Jones:** as it's called. So, unfortunately, if you operate at the normal 5 V, well, it sits somewhere in there, slightly above that. So, they actually don't give you it for the nominal 5 V figure. So, you've got to go,

**Dave Jones:** "Yeah, it's somewhere between 3.15 V and 4.2 V." Now, what VIH actually is, let's have a look at this. We've got our NAND gate here, okay? Let's have a look. We've got our two inputs here. So, we've got our threshold, we've got our 5 V

**Dave Jones:** power supply up here, and our 0 V ground, okay? So, we're looking at the input pin here. So, what VIH is is going to be a level up here somewhere. So, let's say we're working VCC 4.5 V up here, okay? 3.15 V

**Dave Jones:** minimum. So, if we have a look down here, this is going to actually going to be 3.15 V, and then our low level threshold VIL here, once again at 4.5 V is going to be 1.35 V maximum. So, it's going to be

**Dave Jones:** 1.35 V. So, this is the threshold level of our digital logic. So, if our input signal goes up like this, let's say it shoots up like that and comes back down, oops, it never got to a point where it

**Dave Jones:** actually reached this threshold here. So, let let's say we had an input which goes, "Whoa, just like that for a split second." Then our input here is actually going to register as a logic high, and one and likewise, if our signal just

**Dave Jones:** went down like that, as long as it goes through that threshold level there, it it is recognized as a logic low. But, if the signal is inside this dead band here, then well, it's undefined basically and you don't know what the

**Dave Jones:** digital logic gate's going to do. It It can't be guaranteed at all. But you have to actually be careful with these because look, these are max and minimum values. So this is what they guarantee, but you'll notice that they don't give a

**Dave Jones:** nominal figure in here for these. So you know, you just have to design design around the min and the max. Sometimes they'll give a nominal sometimes they won't depending on the uh specification. But that's These figures are what they

**Dave Jones:** absolutely guarantee at that voltage. And over the operating free air temperature range. So that's over the full uh operating temperature range of this thing, which is down here. For the uh regular 74HC non-military stuff, it's minus 40 to

**Dave Jones:** plus 85° C or your typical uh commercial temperature operating range. The military ones, your 7400 series uh just basically they're the same, but they're rated for a much higher uh temperature range. Now, let's have a look at the

**Dave Jones:** DTDV or delta T versus delta V and that sounds complicated, but look at the label here. It's the input transition rise and fall time. So basically, if we're looking at our input signal, it's how fast our input signal ramps up like

**Dave Jones:** this. So let's actually have a squeeze here. Okay, this is our Let's say this is our input and it ramps up like that, okay? So you're going to have a time there between there and there and that might be say 1 ms

**Dave Jones:** to get from 0 up to VCC or it's actually in this particular case, it's the transition time between these threshold voltages here, essentially. Because that's what we really care about. We care about how much time the signal is actually spending

**Dave Jones:** in inside this dead zone here. Now, in this case of 1 ms here, what we're going to fail. Look at the specs here. They're 1,000 ns at 2 V or at say at 5 V there, it's going to be,

**Dave Jones:** you know, let's well, just call it 500 ns for example. That is the maximum, cuz we're talking about maximum here, transition time. So, it has to be faster than that. It's got to ramp up at least in that 500 ns for a 5 V rail for

**Dave Jones:** example. If it doesn't, then the gate is not guaranteed to work. It could go metastable. It could do anything. I mean, I talked about metastability in a previous video. It's just not guaranteed to work at all. So, you don't want slow

**Dave Jones:** rising inputs. That's what Schmitt trigger gates are good for. These are not Schmitt trigger gates. So, you need to have fast transition rise and fall times on your input for this particular type of CMOS logic. Or pretty much any CMOS logic will have a maximum

**Dave Jones:** transition rise and fall time unless it's a specific Schmitt trigger type. Next up, pretty much any device will have thermal information or the thermal resistance of the package. Now, because these aren't power devices, they're just simple logic gates, they're not designed

**Dave Jones:** for power dissipation. But if they were, it's still all relevant. I won't go into the various details. I've done a comprehensive video on thermal information that I can link in at the end of this. But basically, uh it's the

**Dave Jones:** junction to ambient thermal resistance here which matters. Or let's say you wanted to put a heat sink on top of this one, you'd be looking at junction, which is the semiconductor junction inside the thing, to the case, the top of the case

**Dave Jones:** where you want to put your heat sink onto. So, if you had a plastic DIP package, here's the value. It's 45° C per watt. So, if your chip was dissipating 1 W of power, then it would increase that there would be a

**Dave Jones:** temperature differential between the internal junction and the top of the case of 45°. So, let's just say the top of your chip happened to be measuring 45° C. Well, that's not what the temperature of your silicon die inside

**Dave Jones:** is at. It's at 45° plus 45.1 or 90.1 °C inside your chip due to that very high thermal resistance. But, we won't go into details. That's more relevant for power packages. Okay, let's have a look at VOH here, or V O stands

**Dave Jones:** for voltage, O stands for output, H stands for high. So, the voltage output high. Now, it's once again, it's got these at three different test conditions for three different output uh high currents when you're actually uh sourcing 4 mA,

**Dave Jones:** 5.2, or a very low 20 µA as you would if you're just driving some other gates or something like that. And then, for each one of these currents, you get three different specifications for the different uh voltage supply

**Dave Jones:** values. Now, let's take this example here of VCC equals, well, VCC equals 6 V here. Now, you'll notice that typical like minimum, it's going to output not 6 V, it's going to output 5.5, for for or normally typical, say at am this could change

**Dave Jones:** with temperature for example. Um so the typical value could be 5.8. So, once again, if you're going to if you're going to design if you're serious about your design specifications and your margins and you're building a probe that was going to Pluto, then, you know,

**Dave Jones:** you're really you'd be designing around these uh these minimum values here. You wouldn't be designing around the typical ones. You would go, "Well, this is going to be my worst case, so I'm going to design around that." But typi- But

**Dave Jones:** general design use, where it doesn't, you know, it's neither here nor there, then typical values are just fine. But what it shows is that our supply pin is 6 volts, but we're only getting 5.8 volts output. So, let's

**Dave Jones:** actually uh draw our gate here. Okay? So, we've got our NAND gate now. This is our 6-V supply pin inside here. We have ourselves a little transistor like this, which is going to the output pin. And then if we have a resistor,

**Dave Jones:** which is then going down to ground, this here is is not 0 ohms output, okay? It has a resistance, and you can calculate that output resistance based on the drop there. So, we're getting a 0.2-V drop at 5.2 milliamps output

**Dave Jones:** current. So, use Ohm's law. That's homework for you. Use Ohm's law. Oh, yes. There's the temperature I told you about at ambient temperature. I forgot to mention that. So, anyway, you can essentially work out the output resistance of the effective output

**Dave Jones:** resistance in quote marks of the MOSFET inside there. It's not I've drawn a JFET, but it's actually a MOSFET. And the output resistance of that at various currents. That's why the uh difference in this voltage here is going to get

**Dave Jones:** higher and higher the higher your output current gets. Up to that maximum, you remember where it said 25 milliamps before was our maximum current output current on the pin. Well, you can imagine how far the output voltage is going to drop based on 25

**Dave Jones:** milliamps output current. If you're driving a LED, for example, at 20 milliamps or even 10 milliamps, it's going to have significant voltage drop and that may not matter. But if you're driving something else where the output level is actually going to

**Dave Jones:** be an issue, then well, you could come a cropper and you've got to take all that into account. But normally, it's you know, it's not a problem. But that's all part of reading the data sheet. This is what it all means. And VOL here is

**Dave Jones:** exactly the same thing except we've got another transistor. Well, actually, I'll show you we've got another transistor down in here like this which goes down to ground and that would be if we had a resistor going up to VCC like that. And

**Dave Jones:** then we've got current flowing through like that. Once again, you've got a certain dynamic resistance there of your output driver MOSFET and that will be, once again, determined by these figures here. It won't be zero. It'll be 0.26 volts there, for example,

**Dave Jones:** at 25° C. And you might notice that the 74HC, the military version, actually is worse than the commercial one. What's going on there? Well, you saw before the operating temperature range. The 74, the military 54 series logic is designed for a much wider

**Dave Jones:** temperature range, so the specification is actually going to be worse for that. It It just comes with the territory. All right, let's look at II here. Once again, I is current and the little I there is input. So, the current on the

**Dave Jones:** input, i.e. effectively the input resistance. And once again, they give you a range over that's valid. They're basically saying just over the full operating voltage range there. Once again, at a typical ambient temperature. And once again, we have a typical value

**Dave Jones:** here. You'll see it's typical and you can use that. But once again, if you were doing worst-case design analysis, you'd go with the maximum. Okay? And there's a hell of a difference. Look at how many orders of magnitude difference there,

**Dave Jones:** right? Three orders of magnitude difference between your typical value and your maximum. So, that's a hell of a lot of order. All right. So, our typical value plus minus 0.1 nanoamps, that's 100 picoamps. So, obviously, this is a CMOS gate, right?

**Dave Jones:** There's hardly any input current whatsoever. You can, you know, do simple Ohm's law to figure out what the effective input resistance is at that particular voltage. But it's basically bugger all. But once again, that's going to change with temperature.

**Dave Jones:** So, if you were relying upon that for some super-duper ultra whiz-bang low-power design, that could matter. Watch out for it and you could come a cropper there cuz these typical values, basically, the typical values here are not They might even say

**Dave Jones:** it here in the data sheet. I'll have to check. Um but the typical values are not actually parametrically tested at the factory. They're just typical ones. They might batch test them occasionally or something like that to make sure that

**Dave Jones:** they're still meeting those typical values. But the chip you buy, you can't go to them and say, "I measured 1 nanoamp at 25° C." They're going to come back to you and say, "Well, tough titties. It's plus minus

**Dave Jones:** 100 nanoamps. That's all we guarantee. Your problem, not ours. And now we have our ICC, which is basically our power consumption of the device. I think it had that at the top level spec, didn't it? Low input current, low power

**Dave Jones:** consumption, there it is. 20 microamps maximum. So, let's have a look if that matches down here. I haven't checked this yet. 20 microamps, will it? ICC, 20 microamps for a 74HC? Yes, it does. There you go. There's the maximum figure

**Dave Jones:** at VCC 6 volts. So, they've done the full they've done the maximum voltage there. So, it doesn't matter. You'll notice how they've got different input conditions here. It doesn't matter whether the inputs are at VCC or zero. And And it's also at zero output

**Dave Jones:** current, of course. You can't be drawing any output current because then that will contribute to the chip power consumption on the ICC pin. So, this is with the output pins floating. And of course, this is a maximum value here.

**Dave Jones:** So, there you go. 20 microamps for those playing along at home for 74HC double O. That's fly halfway to the moon on 20 microamps. Geez. Anyway, let's continue. But, that 20 microamps is actually over the full temperature range at the ambient

**Dave Jones:** temperature range of 25°. You'll notice that it's only 2. So, you know, it's it's an order of magnitude better than the banner spec right up the top. So, if you just took that banner spec, yeah, that's worst case over the temperature

**Dave Jones:** range, but you're not going to generally you're not going to be using your product at minus 40° for example or right up at plus 85. So, and generally the chip, the die itself is not going to be an elevated temperature because

**Dave Jones:** you're not dissipating any power or anything like that. So, you know, really like 2 microamps is you know, you're designing a low power widget, yeah, you know, you you might say a five or something like that, perhaps. Of course,

**Dave Jones:** you can characterize it yourself, but they don't provide any further characteristic uh graphs on these things, and they don't provide any typical figure as well. They only give you a maximum figure. Now, C I, C is for capacitance, and I is for the input, of

**Dave Jones:** course, and from any over the full operational voltage range, and because it's capacitance, the units are picofarads or puff. Um if you want to uh like an industry uh veteran, then typical value of about three puff on the

**Dave Jones:** input. So, if you're using if you've got your gate, I'll just draw an inverter, but, you know, if you've got you're driving several gates like this, say, you know, there could be reasons why you're doing this. Um then, you

**Dave Jones:** know, system design, just basic system design, means you often driving more than one gate, then your total load, C L, load on the output here, is actually, you know, three of those typical capacitances, and that could matter for

**Dave Jones:** your slew rate up here. Where was it? Here you go. That could be a big deal for your input transition rise and fall times, because you're driving a capacitive load. So, just be aware of that. That can be a big deal, and maximum fan out

**Dave Jones:** was a big deal back in the day when they designed computers with you know, 74 series logic, because you'd have one chip driving 20, 30, you know, other chips, and it was a big deal, and capacitance of the input pins really

**Dave Jones:** mattered. But, that's not the end of the story there with the capacitance. In fact, it's just the start of the story. That C I is effectively the uh static capacitance, but what we've got here is a much more complex thing called CPD,

**Dave Jones:** and I could probably do a separate video on this, and this is the dynamic power dissipation. They don't say it's dynamic here, but it is the dynamic power dissipation capacitance per gate. And even though they're talking in terms of

**Dave Jones:** power capacitance and power dissipation, the units are still in picofarads, uh puff. So, it's much higher. It's actually 20 picofarads. Once again, that's a typical figure. They don't actually specify a maximum figure for that, but that's for a switching device.

**Dave Jones:** So, in a complex system, this one here, port one, and not just the static value here for an individual input. So, anyway, I won't go into details there. We don't have the uh time to do that here, but yeah, there are two different

**Dave Jones:** figures there for capacitance. One CI and one CPD. It's dynamic power dissipation. Now, let's look at TPD, or uh T is time. So, our units are going to be seconds, nanoseconds in this particular case, and P is uh stands for

**Dave Jones:** propagation, D is for delay. So, this is the propagation delay time. They give you exactly what it's for, from A or B input to the Y output. So, let's assume that your input just goes high like that. There is no uh rise

**Dave Jones:** time. Let's just say it's infinitely fast like that, and then your output will have the TPD is how long your output takes to change like that. So, your time in there is your TPD, or how long it takes the

**Dave Jones:** internal logic to propagate from the input through to the output. And there's a typical figure here. You might work from that, but once again, if you're doing worst-case system design, maximum's where it's at. So, you know, you don't want to come a gutser because

**Dave Jones:** your your fight your design around these figures and then your computer works fine at 25° C, but when you stick it in a box and it's working at 40° or in the middle of winter it's working at, you

**Dave Jones:** know, 0°, then you can completely come a cropper and your digital logic system just starts having a fit. Weird errors start happening and you're not sure why. It's because you aren't taking into account the propagation delay. So, let's

**Dave Jones:** say this is your input here, but this also buggers off to another input over here. You know, let's let's let's say you have another gate over here, it's connected and then the output of this one here is also connected down to here.

**Dave Jones:** The output here is only going to be valid after this propagation delay time here, like this. Because like during but during that time, the output here is undetermined, for example. So, you just got to make sure you don't come there in

**Dave Jones:** terms of your digital logic system design. And this can apply equally well to FPGAs, for example, PLDs, complex system design. It doesn't have to be discrete chips like this. You're going to get the same the same parameters like

**Dave Jones:** these for you know, in internal gates inside FPGAs and other devices like that. Next we'll look at TT here, which is the transition time. It doesn't tell you that in this particular data sheet. a bit cryptic here. Other ones

**Dave Jones:** might be better, might be more descriptive in that aspect. So, what it is is how long it takes for your output to transition from low to high, like that. And that's your time in nanoseconds. Once again, typical and

**Dave Jones:** maximum figures. So, this TI data sheet actually doesn't give a huge amount of detail here, cuz this could also be affected by uh the output capacitance. It doesn't say anything. Let's actually go over to a Nexperia data sheet, shall

**Dave Jones:** we? This is the uh once again it's for the exact same chip. It's for the 74HC uh 00. And if we go down here, let's have a look at the exact same parameter. There it is. Yeah, this one actually

**Dave Jones:** tells you its transition time. Take a look at that. And this one actually has C 6. And look, this one gets quite intricate. Look at this, TPHL there. What on earth is that? Well, T time, P propagation, H high, L low. So, it's the

**Dave Jones:** uh propagation delay time when it transitions from high to low output. So, that's a combinatorial parameter that includes the transition propagation delay time plus the uh output transition delay time. See, we didn't get that nice little informative uh waveform. You can

**Dave Jones:** go into more details on that. Oh, measurement points given in table nine. Let's have a look at table nine. Thank you very much. Ah, look it's all happening here. Table nine input, once again, aha, see, this one specifies a

**Dave Jones:** load capacitance. So, when you uh your test circuit, you'll notice that it actually has a load capacitance on there when they actually measure these parameters which they put in the data sheet up here. And check this out. Look at this. Whoa, CPD is used to

**Dave Jones:** determine the dynamic power dissipation. There you go, this one has much more detail. I don't think we got that in the TI data sheet. And you know, there's the like the formula is actually quite complex where all these things are taken

**Dave Jones:** into account to give you your dynamic power dissipation capacitance. And you know, make a big difference. Oh, I just made an absolute fool out of myself, didn't I? Here we go. Parameter measurement information. They've got it here. Sorry,

**Dave Jones:** TI. Shouldn't have doubted you. I still got my TI TTL data book, which is like 4 in thick. Anyway, so yeah, there you go. There's the I think we've gone through all of the specs, have we? Yes, we have

**Dave Jones:** in the data sheet. Fantastic. Still more to go, though. So, we've got all that fancy pantsy stuff here. Once again, with a test capacitance of 50 puff. There, note A. See, that includes the probe and fixture capacitance as well.

**Dave Jones:** Um trap for young players if you're not taking your probe capacitance into account because they're going to be viewing waveforms on the scope and stuff like that. So, you got to take into a you need a low capacity of a probe to be

**Dave Jones:** doing that or at least have it characterized and measured. Anyway, we're getting way out of the um bounds of what we need to talk about for the data sheet. So, we're done with all the specs and there's our functional block

**Dave Jones:** diagram. Whoop-de-doo. They're They're still updating this data sheet in 2016, which is pretty amazing. TTL's like 50 years old now. Uh 74HC is not quite that old, but it's really getting up there. Um and there's our functional truth

**Dave Jones:** table, which we've done a previous video on that will match your truth table You should know your truth table for your AND gate or you should be able to derive it. And a typical application. There's an SR flip-flop. Um that's just a

**Dave Jones:** How do I know it's a flip-flop? It's just the cross configuration like that and set and reset and your Q and not Q outputs. So, that would be equivalent to an SR to a 7400 series SR flip-flop. You can build

**Dave Jones:** it with two NAND gates if you really want to. And we've just got some nice little warnings here. Thank you very much, TI. Um take care to avoid bus contention because it drives currents that would exceed maximum limits. The high drive

**Dave Jones:** also creates fast edges into light loads. Routing and load conditions must be considered to prevent ringing, and that's all to do with the PCB layout routing and stuff like that. And here you go. They actually explicitly tell you

**Dave Jones:** what we talked about before. Load currents must not exceed 25 milliamps per output and 50 milliamps total for the part, and outputs must not be pulled above VCC. Thank you very much. Just don't Don't hurt your little gate.

**Dave Jones:** And we do have a parametric curve here. You don't often get parametric curves in just digital data sheets, but they decided to do the transition time versus voltage here. So, you'll notice that the higher up voltage you go, once you reach

**Dave Jones:** 5 volts here, it's pretty much a fixed 5 nanoseconds transition time there. So, it's just faster. The lower voltage If you're working down at 2 volts off a single coin cell, for example, CR2032 coin cell, then you're working in this

**Dave Jones:** region Whoop. You're working in this region here, which where you have much faster transition times, but not that is going to matter cuz if you're working off coin cell, well, you're going to be ultra-low frequency anyway, like working off a

**Dave Jones:** watch crystal. So, forget I said it. Then they're going to give you some handy recommendations on bypassing in case you didn't know. I've done a whole tutorial on bypassing, so I'm running into the limit of what I can

**Dave Jones:** link in at the end of the video, really. Um, so they recommend your typical 0.1 mic, 100n, and recommend multiple ones for each power pin, commonly used in parallel, etc., etc. And then we've got some nice layout guidelines and unused

**Dave Jones:** inputs. Thank you very much. Tie unused inputs to VCC or ground like this. And they actually tell you this up here, which I maybe forgot to mention, um because if you're talking about uh you know, power and package power

**Dave Jones:** dissipation and stuff like that, that's going to be dependent upon uh we recommend uh I'll find it. I'll find it. I'll find it. Don't you worry. Haha. All unused inputs of the device must be held at VCC or ground to ensure proper

**Dave Jones:** device operation. You know, if you leave one gate floating, uh like the inputs to one gate floating, it's not really going to affect the other gates. It could on a more complex chip. For example, that's why they tell you. Um but also, the fact

**Dave Jones:** that these are CMOS devices, if you leave your uh input pin just flapping around in the breeze open like that, then you're going to um potentially get interference on that pin, and it's going to start switching, and then you're going to get Where is

**Dave Jones:** it? Your dynamic capacitance. See? Whoop. Come on. CPD. You're going to be dissipating power, pissing away power, because you left You're getting um uh coupling on switching, especially and it could be due to routing right next to it. It could easily couple a signal into

**Dave Jones:** that uh floating input pin, which could cause the input to oscillate, and oscillation equals more power dissipation. So, do not leave your inputs floating. Tie them. Got it? Look at this. They even have a document, Implications of Slow Off-Loading CMOS Inputs. And one of

**Dave Jones:** those, I don't even have to read the document, I can tell you, will be that excess power dissipation. So, yeah, just don't do it. Anyway, related links. Now we're getting into the uh community resources, blah blah blah. Technical

**Dave Jones:** they link directly to their sample uh page. I wonder if you can get a sample for a 74HC00 these days? Probably. You know, I mean Anyway, now we get into the package option addendum. Um, and this is where you actually get

**Dave Jones:** the orderable part number over here. So, that was for the ceramic dip package. So, if you're looking for your plastic dip package, where is it? Your P dip over here, that's the one you want. Now, let's actually have a look. There's

**Dave Jones:** actually two plastic dip packages here. One's got N there, and one's got NE4. Let's have a look at the difference. Both are lead-free. Uh, lead ball finish. Aha, one of them has a different finish on the pins. There you go. So, if that mattered, like

**Dave Jones:** a different metal finish on the, uh, pin. So, if that mattered to you, uh, for, uh, really, um, RoHS compliant, but they're both, uh, RoHS compliant, so they're both lead-free. But, if that mattered to you from a soldering perspective or anything

**Dave Jones:** like that, you know, a critical if you Once again, if you design the probe flying to Pluto, you've got one shot at this. You know, you're you're going to have a dedicated engineer in the group just looking at the soldering and the

**Dave Jones:** metallurgy and all that sort of stuff involved in this sort of thing. So, you know, that could So, if your purchasing department ordered, uh, one instead of the other, that could ruin your space probe. And it looks like we've got more

**Dave Jones:** corporate waffle about, uh, lifetime buys and things like that if we make it obsolete, blah, blah, blah. Blah, blah, blah, nothing else happening. Oh. Ah, now, now we get it off, you package aficionados. Here we go. Here's the tape and reel information. This

**Dave Jones:** matters when you're getting your device manufactured. Uh, your, um, assembly house really want to know this. They want to know, well, it's okay. It's a standard SO type package. They're probably not going to, you know, they're just going to be able to handle it. But

**Dave Jones:** this you know, this can be important for our specialized devices and you can have them pin one. It tells you exactly where the pin one orientation is inside the quadrant of the pocket like this and it's important information.

**Dave Jones:** Your assembler needs to know this sort of stuff. So, you know, manufacturers might be different. One manufacturer might have pin one orientation on the tape completely different to another manufacturer. Don't take it for granted. And in this particular case, they're all

**Dave Jones:** in quadrant one here of your tape like that. But as I said, different manufacturers could be different and how comes in the box. So, for you box aficionados, there there you go, you know. How much shelf space it

**Dave Jones:** takes up. The That could be important for a huge manufacturer. You know, if you're Apple and you've got all these tapes and reels of components and stuff like that. All this stuff takes up shelf space when you've ordered, you know, 20 million of

**Dave Jones:** these parts. Anyway, let's get on down here. And now we have our physical package requirements. These are the min max. These are of all your mechanical engineers are all getting a bit moist now about the package. And there's the

**Dave Jones:** leadless chip carrier. So, how that's designed if you were doing a you know, designing a pad. You know, that just went For example, you know, your pad went around there like that. Then this sort of droid matters, right? So, let's go

**Dave Jones:** down here. There's our SO package. Once again, if you're designing a pad packages like Altium, for example, other packages might have a PCB layout packages might have a IPC footprint wizard, for example, and you need all of the

**Dave Jones:** information contained in here. It'll It'll have like a common format and stuff like that. It'll ask you for all these particular, you know, these particular widths here. It'll ask you for your package width and, you know, stuff like that. So, if you've got an SO

**Dave Jones:** package wizard generator that generates a footprint automatically, you just need to know this information and you can get that from the data sheet. Oh, look at that. Wow, ceramic dual flat pack for those military efficient autos. You could even cut out

**Dave Jones:** your board like this. You could even have like a cutout in your PCB like that where your chip actually sits flat and is then soldered on top of the pads like that. Seen that in various teardowns over the

**Dave Jones:** years. Oh, look, we get actual photos. This is the ceramic dip. Nobody uses ceramic Well, military still use ceramic dip. There it is. Um yep. Yeah. No. And recommended footprints. Now, here's the thing. Um some people are all for

**Dave Jones:** using the recommended footprints inside the data sheet for a particular chip. People will take that as gospel. Others will not. Nope, never ever touch a footprint inside a a data sheet. Never use it. You'll come a gotsy. Your

**Dave Jones:** assembler will hate you. Use the recommended ones from your assembler or or you're an IPC standards aficionado. You only use footprints from the IPC. I won't get into the flame war of, you know, all this. It's just not worth it.

**Dave Jones:** Anyway, there you go. So, there's all your details for your package. Once you There's your recommended SO footprint. You know, some people will not like it, others might. And your PCB package might actually have that particular um thing up there for the small outline

**Dave Jones:** package. It may label it in that particular way, but yeah. Important notice, yeah, don't probably don't use it in medical devices and stuff like that. And they're very serious about that, by the way. Um you know, if you're

**Dave Jones:** designing your chip into a medical device and it kills someone, they their army of lawyers will totally wash their hands of it. Does it even mention medical in there? I don't know. Anyway, important notice. Whatever. So, there you go. I hope you enjoyed that. I know

**Dave Jones:** it's been a long video, but there's really no way to avoid that when you go through every single page of a data sheet and every single parameter. And this is pretty simple 74HC 00 quad NAND gate. Imagine if we did it

**Dave Jones:** like a microcontroller data sheet or an FPGA data sheet or something like that. It I could do it like the video would literally be 24 hours long to do like an FPGA data sheet with all its parameters and everything else. But anyway, if you

**Dave Jones:** found that useful, please give it a big thumbs up. And as always, discuss down below if you like this sort of screen capture data sheet type thing. I can do more of them. Please leave a comment down below if you

**Dave Jones:** want to me to go through other types of data sheets. This one follows on nicely from the digital logic tutorials I've been doing recently, but if you've got suggestions for other data sheets you want to go through, then by all means,

**Dave Jones:** we can do that. Hope you enjoyed it. Catch you next time.
