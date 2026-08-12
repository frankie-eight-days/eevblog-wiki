---
video_id: XroH4X78qTY
title: EEVblog #259 - PSU Rev C Schematic - Part 12
url: https://www.youtube.com/watch?v=XroH4X78qTY
source: youtube-asr
timestamps: {"0": 5, "1": 21, "2": 36, "3": 52, "4": 68, "5": 87, "6": 104, "7": 120, "8": 141, "9": 158, "10": 171, "11": 186, "12": 201, "13": 221, "14": 235, "15": 250, "16": 266, "17": 281, "18": 292, "19": 309, "20": 326, "21": 341, "22": 360, "23": 373, "24": 389, "25": 404, "26": 422, "27": 442, "28": 459, "29": 474, "30": 487, "31": 500, "32": 518, "33": 532, "34": 548, "35": 560, "36": 572, "37": 590, "38": 607, "39": 625, "40": 640, "41": 655, "42": 666, "43": 680, "44": 694, "45": 711, "46": 725, "47": 740, "48": 756, "49": 774, "50": 788, "51": 803, "52": 815, "53": 828, "54": 844, "55": 859, "56": 874, "57": 889, "58": 905, "59": 921, "60": 935, "61": 947, "62": 960, "63": 976, "64": 992, "65": 1007, "66": 1021, "67": 1036, "68": 1053, "69": 1067, "70": 1080, "71": 1099, "72": 1112, "73": 1125, "74": 1144, "75": 1160, "76": 1176, "77": 1189, "78": 1204, "79": 1221, "80": 1232, "81": 1247, "82": 1262, "83": 1276, "84": 1295, "85": 1309, "86": 1329, "87": 1342, "88": 1358, "89": 1373, "90": 1386, "91": 1400, "92": 1412, "93": 1427, "94": 1444, "95": 1458, "96": 1471, "97": 1485, "98": 1497, "99": 1514, "100": 1530, "101": 1547, "102": 1561, "103": 1577, "104": 1595, "105": 1611, "106": 1625, "107": 1640, "108": 1653, "109": 1668, "110": 1687, "111": 1700, "112": 1713, "113": 1726, "114": 1740, "115": 1753, "116": 1770, "117": 1783, "118": 1799, "119": 1813, "120": 1831, "121": 1845, "122": 1861, "123": 1881, "124": 1895, "125": 1910, "126": 1927, "127": 1943, "128": 1958, "129": 1976, "130": 1992, "131": 2010, "132": 2029, "133": 2045, "134": 2063, "135": 2081, "136": 2096, "137": 2113, "138": 2131, "139": 2144, "140": 2158, "141": 2174, "142": 2191, "143": 2210, "144": 2232, "145": 2247, "146": 2260, "147": 2281, "148": 2299, "149": 2317, "150": 2336, "151": 2349, "152": 2362, "153": 2379, "154": 2394, "155": 2412, "156": 2431, "157": 2444, "158": 2465, "159": 2478, "160": 2498, "161": 2513, "162": 2534, "163": 2550, "164": 2566, "165": 2579, "166": 2598, "167": 2613, "168": 2630, "169": 2648, "170": 2668, "171": 2687, "172": 2704, "173": 2719, "174": 2735, "175": 2752, "176": 2769, "177": 2782, "178": 2800, "179": 2818, "180": 2834, "181": 2851, "182": 2868, "183": 2881, "184": 2895, "185": 2909, "186": 2923, "187": 2940, "188": 2958, "189": 2977, "190": 2994, "191": 3009, "192": 3024, "193": 3041, "194": 3058, "195": 3072, "196": 3094, "197": 3111, "198": 3130, "199": 3150, "200": 3166, "201": 3184, "202": 3199, "203": 3218, "204": 3232, "205": 3246, "206": 3261, "207": 3277, "208": 3294, "209": 3308, "210": 3323, "211": 3342, "212": 3359, "213": 3378, "214": 3391, "215": 3411, "216": 3427, "217": 3440, "218": 3455, "219": 3467, "220": 3484, "221": 3497, "222": 3511, "223": 3529, "224": 3549, "225": 3564, "226": 3578, "227": 3595, "228": 3614, "229": 3634, "230": 3646, "231": 3660, "232": 3673, "233": 3686, "234": 3699, "235": 3714}
---

**Dave Jones:** And here's my Rev C schematic, which we'll go through in quite some detail. Now, I started out by looking at this Rev C design. It was reason I did it is because cost was getting a little bit out of hand. Wanted

**Dave Jones:** to shave a few dollars off here and there. And one of the things was of course the battery charging in the battery and the separate battery PCB I was going to have. Well, an extra PCB of course that costs money. And the battery

**Dave Jones:** charger chip was actually the most expensive chip on my board because I originally had the concept that you'd be able to charge this from a 5-V USB input. So of course the battery voltage using three lithium ions at you know,

**Dave Jones:** 4.2 V each over 12 V was actually greater than the 5 V so you needed a step-up converter, but then I thought, well, it'd be great if you could not just use a step-up, but use what's called a SEPIC voltage converter, which

**Dave Jones:** basically is a DC-to-DC converter, but the input voltage instead of being a boost or a buck, it's both. It can actually accept any voltage above or below your battery charge voltage. And Linear Technology make a brilliant SEPIC constant current

**Dave Jones:** constant voltage battery charger chip the LT 1512, but unfortunately, it's even in volume at a 100 of quantity here, it's still 3 bucks 85 and that put it as the most expensive semiconductor in my entire design and that just didn't

**Dave Jones:** really make sense. So I start that's where the whole cascade of changes came from. I decided, well, if I eliminate the battery PCB, put the charger on the main board, I decided to go for SMD circuitry rather than the through-hole kit. Now, I've

**Dave Jones:** explained that before on the forum and several other places. And really, it's it just made sense to ditch the 5-V USB charging charging capability. And it'd be very slow, too, of course, because to charge a 12-V over 12-V battery from

**Dave Jones:** a 500-mA 5-V USB or any 2 and 1/2 W USB interface, it's not that good. And then it breaks the isolation as well if you're powering it from a 5-V source that's not isolated like a PC or something like that. Well,

**Dave Jones:** it's buggered. So, I decided to ditch the LT1512 as good as it is. And here it is, by the way, if you want to actually if you're interested in the circuitry of that, it's the wall adapter here. It's

**Dave Jones:** actually a SEPIC converter configuration. And the input can be the input from what they call the wall adapter here actually can be greater than or equal to supply voltage. So, I could have had the option of USB charging or 12-V charging or 15-V

**Dave Jones:** charging or something like that from an external plug pack or USB. Would've been really nice, but far too expensive. So, I went through all my parametric searches. I won't bore you with the details. And I ended up um

**Dave Jones:** well, it turns out that as I mentioned before, having three lithium ion batteries actually makes the choice of battery charging IC more difficult, more expensive, more complex, things like that. So, I started looking for another battery charging chip. And I won't bore

**Dave Jones:** you with the details, but as it turns out, the Microchip one, surprise, surprise, are some of the cheapest on the market. But if you go through the Microchip uh they only support, if you look at this column here, number of lithium ion

**Dave Jones:** cells, there, then they only support one and two cell devices. So, um it looks like I'm going to have to I told myself I'm going to have to choose a two cell device, and it just so happens that the MCP73213,

**Dave Jones:** it's only $1.29 in volume. It is a 10-pin DFN but package over here, but I am going for uh surface mount anyway. Um and the board will actually be pre-assembled, won't be hand soldered, so not really an issue. We're trying to

**Dave Jones:** save some cost here. So, I've already saved a couple of dollars on my bill of materials uh cost by choosing this, but it only supports two cells maximum. And uh really, that changes the whole ballgame because I was originally going

**Dave Jones:** to have a 0 to 10 V uh supply, which actually was going to be lower than 10 V as the battery voltage drops, and the software inside the unit would have been intelligent enough to actually measure that and know

**Dave Jones:** that it's no longer capable of outputting 10 V, so it would change the maximum range that you actually had available. So, now with only uh two cells at 4.2 V per cell absolute maximum, um really, we're only talking about like a 0 to 6 V

**Dave Jones:** supply at the, you know, outside. Um that's with a full uh voltage cuz we've got a couple of volts drop with our LT3080 linear regulator. So, really, um that changed the whole ballgame and started the cascade of changes like I've

**Dave Jones:** talked about, and uh I went right, well, now I've got two lithium ion cells, what can I do with that to get a bigger output range? Well, I can put in a um switching uh a switching pre-converter in there to

**Dave Jones:** boost the voltage up uh before the LT3080. So, that gave the capability to then actually give um the entire to give a much bigger output voltage range. In this case it'll be zero to 20 volts instead of zero to 10 volts. And

**Dave Jones:** we can do that by having a boosting pre-regulator down here. And this is my new rev C schematic and this is my boosting pre-regulator. It comes from the battery we'll go through the whole thing but it comes in from the battery and it boosts

**Dave Jones:** it up before it goes over so the battery the input battery comes here. Here's my MCP. In fact we'll go through it now. Here's my MCP 73213 battery charger. We've got our DC jack here which is 12 volt 1 amp minimum.

**Dave Jones:** We've got some diode protection there. The charge rate I've set to 550 milliamps half an amp and there's our battery connector there. That's our two cell battery. We've got some battery measurement here which goes to the ADC but basically

**Dave Jones:** the Vbat goes into the DC to DC converter which is actually software controllable. Go into that later. The it's got an E squared pot here. So it gives an output range here of 9 volts to 22 volts output range. 22 volts being 2 volts

**Dave Jones:** above our maximum desired range and that then goes into our existing circuitry which we've got here and the as you've seen before the LT3080 and we drive it linear. What that gives us is by only keeping under intelligent

**Dave Jones:** software control the input voltage to the LT3080 voltage regulator keeping that only 2 volts above the output we're only dissipating at a maximum of 1 amp output current we're only dissipating a maximum of 2 watts in that LT3080

**Dave Jones:** regulator instead of much higher than that before, using just a straight linear voltage regulator. So, now we're only dissipating 2 W in our linear voltage regulator. It was like five times that before. So, now we can get away from

**Dave Jones:** using that expensive heat sink. So, here come the cascade of cost savings. We changed out we've eliminated a PCB. So, that was, you know, a dollar or $2 a couple at least a couple of dollars that cost there even if you get it if you got

**Dave Jones:** it from China more than that, probably double if I get it from my New Zealand source. So, a big cost there for the extra PCB large battery PCB which we're looking at to mount the battery holders on. We're saving that cost. We're saving

**Dave Jones:** a couple of bucks on the LT 1512 charger by choosing a different charger. We've got one less battery in the design, and we're dissipating less power, so we don't need that huge $4 $4 plus heat sink in volume. So, we can use our back

**Dave Jones:** panel which will be an aluminum back panel because it it is still dissipating 2 W. So, you know, it it will actually dissipate will actually get to a fairly high temperature if we only have that on a modest say

**Dave Jones:** a heat sink which built onto the PCB. And we'll go into that. So, really we've already saved quite a significant amount of cost just there, but there's more to come. But, of course, some of our cost saving has actually been offset by the need to

**Dave Jones:** actually have this DC to DC boost converter and the e-squared pod as well. But, these devices are quite cheap as we'll go into and we'll go into the selection for these things. But, we're still saving even with the addition of

**Dave Jones:** these two devices plus a few passive components around there, the inductor and things like that, you know, 20 cents for the inductor or something. We're still saving many dollars on our overall cost. Now, there's one thing you might

**Dave Jones:** notice missing from the uh charger circuitry here, and that is battery protection. Well, uh it's not that we don't have any. We're actually going to use the uh 18650 cells that have built-in battery protection circuitry. I.E., they um have a little uh they're

**Dave Jones:** slightly longer than your standard 18650 uh cell, but there's a little PCB in there with battery protection circuitry, which uh stops it being overcharged over 4.2 V, and it also uh stops it from being over discharged, and it cuts out at uh 2.7 V.

**Dave Jones:** So, uh really, where um it's the using those batteries saves us uh cost, and it offloads the protection into the batteries where it probably should be anyway. And if we take a look at our MCP73213 uh dual cell lithium-ion/lithium-polymer

**Dave Jones:** battery charger management IC, um it does actually have different battery charge uh voltage options, cuz we're using uh 4.2 V per cell, we need the 8.4 V version. So, you got to be careful when you order this thing to actually

**Dave Jones:** order the right part number. You can't just order MCP73213, otherwise you could end up with anything. You got to order the exact part number. Now, it actually has uh uh um yeah, it's output uh charge fast charge capability is programmable from

**Dave Jones:** 130 mA to 1.1 A. That's great. Um I've got it set to a nominal half an amp, just over half an amp at the moment, but I might set it up to an amp or something like that. And uh

**Dave Jones:** these uh batteries are typically like a 2,700 mA uh hours or something like that. So, uh really, you know, at a charge current rate of uh 1 A, it they should charge in, say, 3 hours or something like that.

**Dave Jones:** And the other great thing about this device and the advantage over the original LT um 1512 that I actually used it, actually has um end of charge uh control and things like that where you can select the minimum current uh,

**Dave Jones:** ratio. It's got safety timer. It's got preconditioning for depleted cells in here and it's, you know, it's a really nice device. And another advantage is it also has a uh, status LED as well. So, um, I'm going to put that on the front

**Dave Jones:** panel where the 5-V USB connector is and that's a the um, that's a thing I needed before with the LT1512 solution. I needed some sort of a LED um, status solution to show you that whether it's charging or finished charging. This is

**Dave Jones:** all built in. It's got a single resistor programming. It's a great device. It's so easy to use. Practically foolproof. So, we're going to use that and uh, if we take a look at the um, circuit here, you'll notice that uh, basically where

**Dave Jones:** um, the switch to turn the power supply off and on um, is basically just uh, disables um, the power supply from the battery. I could have wired the other um, uh, uh, throw of that switch to the input

**Dave Jones:** here, but then the Vbat, then you're limited by the maximum voltage of the MIC 2253. So, it's not like you could use a 12-V plug pack and feed it straight through. Otherwise, you'd blow up your uh, MIC2253 here. So, basically the unfortunately

**Dave Jones:** the uh, power supply um, it it would have been nice to have it powered from the plug pack while the battery was charging, but we're going to have to live with um, powering the uh, power supply circuit while the battery is

**Dave Jones:** charging. Either that or actually disconnect it. So, really when the batteries are charging, if you want to use the power supply at the same time that it's charging, well, it's going to share some of the uh, current um, uh,

**Dave Jones:** charge current. So, it's going to charge uh, slower, but there shouldn't be any problem by having the load um in parallel with the battery while it's charging. So, our battery uh voltage range when it's fully charged is going

**Dave Jones:** to be 8.4 V, and uh that's going to drop down to an end of life of uh 5.4 V, or that's where the uh safety cutoff in the battery will typically uh cut in, but not that you really should let them go

**Dave Jones:** that low. So, um the But, because we're reading the battery voltage here with our microcontroller, the microcontroller can determine what the low uh battery uh cutoff voltage is, and unfortunately it can't like Well, it could actually disconnect the load um if it wants to uh

**Dave Jones:** do that automatically. It can It has the has the option to actually do that. But, uh really it can uh flash the low battery warning indicator at any voltage you desire. So, how long will the batteries last in this design? Well, you know how

**Dave Jones:** long's a piece of string? Let's say we have our maximum output current uh capability of an amp, and we uh we haven't got the DC-to-DC converter uh switched on here. So, we're powering our output voltage, say 3.3 V, directly from

**Dave Jones:** the battery uh source. Um it's going to work just like a linear uh voltage voltage regulator in that case. So, uh 1 A output will flow directly through the regulator. It'll flow directly through the diode and the inductor there, and

**Dave Jones:** it'll be um taking 1 A directly from the two-cell battery here. And at a nominal uh capacity, it varies, but a typical one might be, say, 3,000 mA uh hours. Depends on the load current, of course, but let's say it's uh it will

**Dave Jones:** basically last uh 3 hours uh actually providing 1 A uh full capability uh to the load. So, that's not too bad. And if your load is less than that, the efficiency of our switching uh switching uh voltage regulator down here, our

**Dave Jones:** preregulator, will actually improve that at higher uh output voltages that there's less wastage. It's still operating partially linear, so it's a combination of a switching and a linear voltage regulator, but it should be more efficient than just a standard

**Dave Jones:** regulator. So, if you're powering something small, it could last all day. It could last 8, 10 hours, or or even a lot more than that depending on on your load. If it's very low load, jeez, could last forever. Actually, my entire

**Dave Jones:** circuit draws about a a quiescent current with no load. I think it's about 15 or maybe even 20 milliamps tops or something like that. It's not a huge amount. That's with the LCD. It doesn't take much, and the micro

**Dave Jones:** doesn't take much either. So, really we're talking a couple of hundred hours from a fully charged set of batteries just having the power supply turned on and the LCD operating. So, pretty much it's going to vary from vary from a couple of hours at full load

**Dave Jones:** to a couple of hundred hours at no load or very low load. And when the device is switched off, you don't really have to worry about this charger chip actually drawing current from your battery because it's very minimal. If we actually take a look at

**Dave Jones:** it, we're talking, you know, only a couple of microamps in shutdown mode there. So, you know, it's it's really not a big deal. You can just leave it actually connected straight across your device. So, just on the thermal aspects of the

**Dave Jones:** LT3080, as I said, it's dissipating 2 W. If we jump to the data sheet here for our chosen package, the TO220, the as you can see, the thermal resistance of the junction to case, this is without a heat sink. Just the

**Dave Jones:** junction to the case is 3° C per watt. So, at 2 W power dissipation, the junction to case is actually going to get 6° C above the heat sink temperature. So, one of the first things you think about, of course, is actually

**Dave Jones:** mounting this regulator directly on the PCB and using the copper on the PCB as a heat sink. And once again, the TO the LT3080 data sheet actually gives you info on here. This is for the five-lead DD pack, but it gives you example values

**Dave Jones:** here of the board area. 2,500 sq mm is 50 by 50 mm area. And in this tiny case we've got, that's actually a significant amount of board area. And of course, that is for the device mount on the top

**Dave Jones:** side. And look at the thermal resistance of this thing of the junction to ambient for this heat sink. It's you know, we're talking about if you got a total on the top side and the back side, you're still

**Dave Jones:** talking about 25° C per watt for 50 mm by 50 mm copper area on both sides of your board. So, really, if we're if this thing's actually dissipating 2 W, then we're talking about it's going to get a 50° C rise in that copper. And

**Dave Jones:** that's inside your sealed case. That's not you know, that's really not a good way to do it because the air has to actually get out as well. There's got to be thermal convection and stuff like that. So, really, that's not really a

**Dave Jones:** solution. It might have been a solution for say half a watt dissipation or something like that. But I can't afford probably can't afford 50 by 50 mm square area on the top and bottom to begin with, let alone talking about you know,

**Dave Jones:** heating up internally inside the case over long-term loads at our maximum power dissipation of 1 amp with a 2 V drop across the voltage regulator. Not to mention also the drop inside the current shunt resistor as well. You know, we've got some power

**Dave Jones:** dissipation there. So, really, that forced me into mounting the TO 220 package on the aluminum backing panel so that at least I um it's got the heat can escape to the outside world via the back panel. So, that should be adequate. So,

**Dave Jones:** unfortunately, the PCB wasn't really a viable solution there. So, let's take a look at our uh DC-to-DC boosting uh pre-regulator here. It's a Micrel uh 2253. I love the Micrel parts. They're really nice. And if we go over

**Dave Jones:** to Digikey here, we'll find that they're not bad price. It's only a dollar in uh reasonable volume or even less than that in uh higher volume. And it's a pretty nice part. It's a 3.5 amp 1 MHz. So,

**Dave Jones:** it's a high frequency, therefore high efficiency uh boost regulator with overvoltage protection and soft start. And you know, it really is quite neat. And it's got a 2.5 V to 10 V input range, which is perfect for our two-cell

**Dave Jones:** lithium-ion solution cuz the lithium-ions uh charge at 4.2 V. So, that's going to be the maximum 8.4 V maximum. Um and its output voltage can be up to 30 V. So, bingo. Now we start thinking with our LT3080 also capable of these uh

**Dave Jones:** sorts of high voltages, we start thinking, well, our power supply, what can we make it? Well, let's make it say 0 to 20 V instead of 0 to 10 V that we had before. You don't want to go too

**Dave Jones:** high and go over the top. 20's reasonable and it worked out because then I've just got to double my uh gain in my uh DAC system and things like that. So, I decided 0 to 20 or 20.48 um actually if you're using the

**Dave Jones:** uh DAC steps would be a reasonable output voltage. So, it's more than capable of that. Um it's you know, it's it's a reasonably nice device. It's available in a uh three-lead um it's available in a um just a surface mount package like this.

**Dave Jones:** Bit of a pain, but once again, our board's been machine assembled anyway. Um there's the heat dissipation in this thing is taken out by a thermal pad on the bottom there, as you can see. And and also the other the input and output

**Dave Jones:** leads as well. And it's a rather nice device and it's pretty simple to use and I've basically copied this application straight into my circuit because it's a standard boost DC to DC converter and there's minimal amount of parts. There's a couple of

**Dave Jones:** compensation components down here, but apart from that, we're all only talking about our voltage set resistor. And the good thing about this is that the voltage set resistor on the bottom here, this 10K one, you can change that value under

**Dave Jones:** software control by having an external E squared pot, as we'll see, to then so the power supply can actually adjust the input voltage to the LT3080 to be just above 2 volts above the required the currently set output voltage. So, that's going to work

**Dave Jones:** brilliantly. And just a quick look at some of the efficiency curves of our Micrel DC to DC converter. Let's go for a high output voltage here of 15 volts. Let's take a look at that. That's in the bottom left

**Dave Jones:** hand corner here. We've got efficiency on the Y axis here versus output current over here. And really it's capable of you know, up to 700 odd milliamps. It's going to be like you know, 80 well over 80% for say 300 milliamps through to 700

**Dave Jones:** milliamps output current with a V in of 5 volts. There's that solid line there. It's going to change as the battery drops the efficiency input battery voltage drops, the efficiency of this converter isn't going to change a huge amount really.

**Dave Jones:** The output current capability this will drop off something like that, but the you know, the software can know about this sort of stuff. You can actually program these uh curves or typical figures into the software so that the

**Dave Jones:** software knows what the maximum output capability uh is based on your particular current battery voltage and the efficiency of the regulator or the measured efficiency of your total circuit cuz this efficiency is not just the chip, it depends on the inductor you

**Dave Jones:** select and and the diode and the capacitor and stuff like that. So, uh really but that's pretty good. And um if we go up here and have a look at say 12 um in the top right-hand corner, 12 V

**Dave Jones:** output uh efficiency, once again, we're talking well over 80% for a good um chunk of the output range from 300 odd milliamps up to um in this case, goes up to an amp. So, that matches this device really matches our design fairly well

**Dave Jones:** here because at an input voltage of uh 5 V, it's, you know, 85% efficient at 1 amp um output, which is our maximum uh capability. So, that is really uh quite nice. It's quite ideal for this application, I think. And it's a fairly

**Dave Jones:** cheap device. But, I've gone into uh selecting uh these sort of things before and as a whole, I could do a whole hour on just selecting the correct uh DC to DC converter for this thing. But, this one seems ideally matched.

**Dave Jones:** But, there's one more neat thing about this. Now, I originally wanted my design to actually be low noise. Um hence why I'm the LT38 is a very low noise device, but it's also battery powered. So, it'd be a really low noise device, but now

**Dave Jones:** we've added this uh nasty 1 MHz switching regulator in here. It's not low noise anymore, but hey, even but we do have a linear voltage regulator on the output still. So, we will actually filter out a fair bit of that noise. I

**Dave Jones:** might put it like an RF bead in there or something like that to maybe uh drop it a bit more, but um the good thing is is that there's an an enable pin here, which allows us to switch off the

**Dave Jones:** DC-to-DC converter if we're getting low output voltages. Say we want a 3.3 V output voltage from our power supply, well, we can run that directly from the batteries. There's no need for this DC-to-DC converter. So, the software will know that because the software is

**Dave Jones:** measuring the battery voltage here. So, it knows what the battery battery voltage is. It knows what output voltage you're setting and what output voltage you're measuring and therefore, it can intelligently decide whether or not it needs to switch on this DC-to-DC

**Dave Jones:** converter, whether or not you can power it directly from the batteries or you need this converter. And if it switches off the converter by pin 11 here, by pulling that low, I believe it's an active low pin, then sorry, active high. If you

**Dave Jones:** pull it low, it switches it off. And the good thing about boost converters is look what you've got here. When this chip turns off, there's an internal FET inside here. If you look at the cursor, it goes down to ground. That

**Dave Jones:** switch, you're basically just switching down to ground. That's how these boost converters work. But what happens if you switch it off? Well, that internal switch switches off. So, pins 7 and 8 effectively become open circuit. And what have you got? You've got an

**Dave Jones:** inductor. Here's your input voltage over here in the top left, Vbat. That will flow through the inductor there and then flow through your Schottky diode, D5, directly to your output. So, if you disable this voltage regulator, your output voltage still works. It just goes

**Dave Jones:** through the low impedance inductor here and it goes through a low voltage drop Schottky diode. And bingo, you switched off your converter. Now you've got no switching noise, but your circuit can still operate because it's getting the battery voltage minus a small drop, you

**Dave Jones:** know, 0.3, 0.4 volts in the Schottky diode maybe, half a volt at most say, and a small drop across the inductor here, which is, you know, 0.01 ohms or something like that. It's going to be very low cuz it's a 3.5 amp

**Dave Jones:** inductor. But that's the beautiful part these boost converters. You can just switch them off. It's not unique to the MIC92253. Any almost any boost converter when you in disable them like this will just allow the power to pass straight through

**Dave Jones:** unimpeded. So we get the best of both worlds. At low voltages, our supply is still low noise cuz the switch is turned off, and at higher voltages, well, you know, you've got to use your DC-to-DC converter. So your output noise might go

**Dave Jones:** up a bit, but not a huge deal. So I really like that versatile capability. Now, as for setting your output voltage, I said we've got an E-squared pot cuz we need software control of that output voltage. Well, here's here's your

**Dave Jones:** formula for your output voltage here, pretty standard stuff, exactly the same as for most boost regulators. And so therefore, this R1 resistor down here, we can modify that in our circuit via the E-squared pot here, and that's exactly what we're doing. Now, R38 here,

**Dave Jones:** this is a 2K2. And from that formula, you can calculate your minimum and maximum requirements. Let's say our minimum we want to be 9 volts. So it's either this thing's either switched off or it'll give 9 volts minimum, and we

**Dave Jones:** want 22 volts maximum. Well, you can calculate using that formula what the values need to be. In this case, it's going to be 600 ohms total to give you 9 volts, or if it's a 1.6K resistor here, that will give you

**Dave Jones:** 22 volts out. So you just want to design this part of the circuit with the pot, which is a 5K pot. It's going to have 5K, and it's going to be 5K, 128 taps. That's plenty for, you know, this sort

**Dave Jones:** of thing. We could have easily used a 64, but this one was uh fairly cheap. Even 32 would have been plenty of taps. Heck, even 16 would have been quite uh reasonable. So, we can get away with uh

**Dave Jones:** just doing that. If you do the um follow the formula, the value of 5K in series with 820 in parallel with 2K2 gives you um the 600 ohms uh output or close enough to it, which will give you the 9

**Dave Jones:** volts. And when this pot in the uh wiper pins five and six here are your 5K pot, zero to 5K adjustable. And when it's uh 5K plus 820 on 2K2, that gives you 1.6K total. Just gives you 22. So, really, even if this

**Dave Jones:** thing powers up and the software is doing something really stupid, then um it it doesn't matter. It's it's not going to like massively go over voltage or under voltage or something like that. So, really, that those values work out

**Dave Jones:** quite neat. Now, the other thing about the um MCP40 uh 4017 T is that it's an I²C interface. Now, um these Microchip uh E² pots come in many uh come in different types. Uh one of them's I²C interface, the other's

**Dave Jones:** your traditional up-down uh counter pin. So, you just toggle a pin, and there's an up-down pin, and you can move the wiper up and down, like actually like in a manual uh type manner. But, that requires extra pins. And here's another

**Dave Jones:** cascaded change we've got. If I chose the one with the up-down pins, I would have needed more output pins on my IO expansion device. Remember I had uh two IO expansion devices before? Now, I've saved cost, and I've only got one. And

**Dave Jones:** one of the reasons for that is because I've consolidated many of my parts in this Rev C to use the I²C bus instead of the SPI bus. So, I parallel them and I don't use any extra pins on my

**Dave Jones:** microcontroller. Brilliant. So, let's take a look at this change. I had two of these devices before, now I've only got one. How have I done it? Well, I've what I've done is I've Now I've got my RGB LEDs here on

**Dave Jones:** the output of this chip which drives the RGBs from for the LCD backlight. Originally had those coming from the pulse width modulated pins on the microcontroller, but I decided that wasn't a hugely valuable capability and I could sacrifice those

**Dave Jones:** pins and put them on the IO device over here. It might be more difficult to PWM them, you might not even have that capability at all, but who cares? It's only the freaking backlight, right? No one's going to care. If it means saving

**Dave Jones:** cost and freeing up pins for better functionality, then I'm willing to sacrifice that. So, I've now done five switches instead of four because I removed my 5-V output socket. So, I can add an extra IO switch there. So, I've

**Dave Jones:** got my five switches plus the three RGB LEDs. But, what happened to all of my extra ones I had on the second chip over here? Well, I've actually consolidated them on the microcontroller, but how did I do that? Because I didn't have any

**Dave Jones:** free pins last time. I was absolutely maxed out and you guessed it, I maxed out again, but I managed to gain a couple of pins by ditching the SPI interface. Remember that bit banging SPI interface I was using? Well, I got rid

**Dave Jones:** of that and I consolidated with I²C part. So, on this I²C bus here, SDA and SCL there, I've got two pins. And let's have a look at what we're driving here. We're driving not only our I squared uh

**Dave Jones:** pot here, um we're doing that. So, we've got that capability for no extra pins, but we're driving our LCD as well, just like we were last time. So, we've got our LCD, and I changed my DAC here from an SPI DAC to an I squared C

**Dave Jones:** DAC. And um I think it might even be a few cents uh cheaper as well, but I freed up those three pins on the um on the on the micro because I've gone for an I squared C device instead of SPI.

**Dave Jones:** So, really, that was a bit of a no-brainer. So, these things cascade down, and I freed up all these pins. Now, you're probably wondering, "Where is my analog-to-digital converter?" Well, here's another trade-off. Now, which we need to get into cuz it's

**Dave Jones:** an important uh major change from the previous version. As you know, my previous design had a 12-bit analog four-channel 12-bit analog-to-digital converter. Well, I've ditched that, once again, saving some more cost cuz that was also an expensive device. That was actually the second

**Dave Jones:** most expensive device um on my design, I think. It was like uh $2.50 or something, third most expensive apart from the voltage uh regulator. So, really, by ditching that, um that was a big decision because I basically had to decide that this was no

**Dave Jones:** longer going to be a really high-precision uh power supply. And the reason I wanted uh I was using that is because I wanted excellent resolution on my current uh ranges from my micro current capability. And you'll notice what's also missing from here that was

**Dave Jones:** on the previous version. I've ditched my I my micro current capability. Or have I? And here's my previous Rev B schematic. And as you can see, there's my analog-to-digital converter plus the buffer voltage followers here. And that microcurrent capability, which I thought

**Dave Jones:** was quite novel. And I really didn't want to give that up, but I thought, well, how can I keep that microcurrent capability or very close to it while actually ditching it completely? It sounds ridiculous, but I found a way to

**Dave Jones:** actually do that. I ditched all this circuitry and I've replaced it with I've replaced it with another device over here, which is an INA219. And we'll take a look at that. And what I've done is I basically decided, well,

**Dave Jones:** uh a power supply like this is not really I didn't really design it to be a precision current constant current generator. So, having that, uh you know, 10-bit uh DAC, that dual channel DAC, which I was using in here to drive the

**Dave Jones:** uh current capability, if you remember that. Here it is over here. I have my dual channel DAC driving both the voltage and the uh current as well. Well, I don't really need to drive the current with that higher precision. It's

**Dave Jones:** just overload protection pretty much or just fairly rough um you know, current output set constant current output capability. I didn't need 10 or 12 bits resolution on that. So, I decided, well, that was a bit silly. So, I could live

**Dave Jones:** with 8-bit resolution on that, really. It's not a big deal, but I wanted to still accurately measure the current using a 12-bit analog-to-digital converter. And that's what I did before. I had my current sense amplifier here, my MAX4080, going into my 12-bit ADC.

**Dave Jones:** And I still wanted to keep that measurement capability and that full range because this previous design could measure um up from anywhere from a microamp up to two amps. It was a huge measurement range that no other power

**Dave Jones:** supply I know of actually has that. And I was able to keep that by choosing the INA219 and going back to a rough and just so my actual capability of measuring the current is still very similar, but I've got a rough PWM DAC

**Dave Jones:** down here. So I decided the I set comes directly from a PWM output, the OC 1A output on my Arduino microcontroller over here to control just the just the constant current capability. Plus that allowed me to go to a single channel

**Dave Jones:** DAC, get an I squared C version, lower cost, and it all starts to flow together, and you start really getting that tingly feeling when it all starts to, you know, fit together and all these design decisions and changes actually

**Dave Jones:** seem to be going in your direction for the better. So let's start by taking a look at the constant current circuitry. It's exactly the same before, but except I'm using a PWM DAC, which I went through in an

**Dave Jones:** early video. It's exactly the same error current limit comparator down here. It's all exactly the same. No changes from the previous two versions. But up here, I decided I'd go back to the rough and ready LM358 differential amplifier, just the single

**Dave Jones:** op-amp differential amplifiers because I didn't really need, you know, a really precision low offset capability for this current. Like 2 milliamps minimum would have been fine. And if you know the LM358, it's got, you know, in the order of several millivolts offset

**Dave Jones:** voltage. So what I did is I upped the the current shunt resistor here. It's actually 1 amp, so I put 10 10-ohm resistors in parallel to give me a total shunt value resistance of 1 ohm here, and that gives me with a um

**Dave Jones:** a 0 to gives me a with a 2-amp output range with a 10-bit digital to analog converter, it gives me 2 milliamps per bit. So, if my if my PWM here is a 10-bit, I can set the current in steps of 2 milliamps. If it's

**Dave Jones:** only 8-bit, I can set it in steps of 4 milliamps per bit. And really, that ties in well with the offset voltage of the LM358. So, I'm only going to be a bit or two out, and you can correct for

**Dave Jones:** that in software. Perhaps that's not a big deal, but what it means is that you're also dropping 1 volt if you've got 1 amp maximum output current capability, which our LT380 is capable of, you're also dropping 1 volt maximum

**Dave Jones:** across the 1 ohm shunt resistor here, and you're dissipating some of the power in that, but it's not really a big deal. It all comes out in the wash, and also that 1 volt capability will be important when we look at the INA219

**Dave Jones:** later. But, let's just look at the this capability here a bit more. I've got a a low-pass filter here just to filter out any switching noise or transient noise from the loads or like that. So, you might be wondering what this voltage

**Dave Jones:** follower op-amp is doing here. Why don't I put just the end of R17 there directly across the shunt resistor? Because that's how I had it in the original when I talked about this single op-amp differential amplifier before. That's what I did. Well, there's

**Dave Jones:** a very good reason for that because Uh, you'll see later, the INA219 will allow us to measure down to 10 microamps uh per bit load capability. So, very low. So, let's assume that our load our our output load here is only drawing 10

**Dave Jones:** microamps, okay? It's very, you know, you got your microcontroller, it's in shutdown, or it's a very low-power design, and you want to measure that. Well, uh the LT3080, it's going to use some current of its own. It's got 10

**Dave Jones:** microamps down this set pin. It's going to be fairly constant. The LM334 is set to 677 microamps. It's got a temperature coefficient, but it's not going to change a huge amount. So, we have the capability to offset this current in the set pin and the

**Dave Jones:** current through the LM334 zero it out. So, I'm going to dedicate one of my front panel switches to a zero capability, and I thought I'd do this way back in my first revision of my design, have a switch dedicated to just

**Dave Jones:** zeroing out the current. That you disconnect your output load, and then you can zero out the current from the LT3080, the LM334, and anything else which is attached to this output line from the current shunt resistor. And the thing is,

**Dave Jones:** that because your output voltage is a fixed value, you're at a fixed output voltage, the current should not change in these two devices. It'll only change with temperature, which won't be much at all. But, aha, look at this circuit here.

**Dave Jones:** With R17 and R18 here, the output the current flowing through those two resistors is going to change depending on your load current. So, if your circuit's drawing different load currents, then the value you've zeroed out is no longer accurate because it's

**Dave Jones:** changing based on the amount of current flowing through R17 and R18 will be dependent not on the output voltage but dependent on the on the output current cuz you'll have a different output voltage here. So, the voltage drop across R17 and R18

**Dave Jones:** will actually differ and you will get current through there. So, there's an error term there which is dependent upon your the output current of your power supply. So, you can't zero that out. It's a really very small trap but very significant

**Dave Jones:** that could have ruined the capability of measuring small currents on this device. So, I had the spare LM380. It's a dual chip device. I just put that as a buffer in there. It's a long explanation but that's why the buffer is there so

**Dave Jones:** there's no current flowing or insignificant current flowing into the non-inverting input of that op amp. So, we now have the capability to zero out any current draw from the LT3080 and the LM334 and the output diode if it's got

**Dave Jones:** leakage in the output caps and anything else or even an output load as well, you can zero it out. And then we can use our INA219 to accurately measure anywhere from low to high values of current. Let's take a look at that one.

**Dave Jones:** So, the INA219 device it's not that cheap at you know 100 off quantity $1.85 but you got to remember it's actually replacing that LT uh 3080 that we had sorry what is it? Yes, the and sorry the max uh 4080 we

**Dave Jones:** had here. It's replacing that. Plus, it's replacing the very expensive analog to 12-bit analog to digital converter down here. So, it's replacing those two devices with one at probably less than half the cost. So, it's a win. So, let's take a look at this novel

**Dave Jones:** device. I love it. It's uh described as a zero drift bidirectional current power monitor with I²C interface. And bingo, I²C magic term, it means we don't need any extra uh pins like we did before. So, we can actually um share once again

**Dave Jones:** share our I²C bus. We don't need any extra pins on the microcontroller. Brilliant. So, we've got like four, I think. One uh two, three, yeah, four different devices. Uh five, actually, with our IO expansion. Five different devices hooked on to our I²C bus. I love

**Dave Jones:** it. We're really maximizing the capability of those IO pins on that microcontroller. And that's exactly what the I²C bus was designed to do, to free up pins on low pin count microcontrollers. So, anyway, let's look at this device. It's high accuracy, 0.5%

**Dave Jones:** over temperature. It's got a 16 programmable addresses for the I²C bus. It can actually measure current, voltage, and power anywhere from 0 to 26 volts. Brilliant. We're doing 0 to uh 20 odd. So, that's great. It's available in

**Dave Jones:** easy-to-use SOIC-23 or SO-8 package. It's great. It's got calibration registers, filtering options, but let's have a look at what's inside it. And it really is an excellent device. This VIN uh plus and VIN minus here in the top

**Dave Jones:** left, um that goes across your current shunt resistor. And then it's got a programmable gain amplifier, which is a bit of a misnomer because it's a more like a programmable attenuation uh uh stage, as we'll see. And it's got a

**Dave Jones:** 12-bit analog-to-digital converter built in. It's um it's powered from a 3.3-volt uh power supply. Plus, it can actually measure voltage and current and power and then actually calculate the power based on internal registers. We're not actually going to

**Dave Jones:** use um that capability cuz we don't need to measure the voltage. It takes It measures the voltage on the VIN plus pin over here. So, it can actually uh calculate um that with that value and and the known

**Dave Jones:** current and the ratio you program in for your current shunt resistor, it can actually output a direct value in power. But, we're using it for its 12-bit analog-to-digital converter and its programmable uh gain/attenuation capability. Now, let's take a closer look at the

**Dave Jones:** specs here. Let's take a look at the offset voltage here. And with the PGA set to a gain of one, okay? We're talking it's got plus minus 10 uh microvolts uh offset uh capability. So, let So, I'm going to use that as a

**Dave Jones:** bottom Well, that that is the bottom line system capability. Remember, we're using a 1-ohm current shunt current shunt resistor. So, really the best case we can get there is um it's plus minus uh 10 microvolts uh offset. So, out

**Dave Jones:** That's going to uh translate to plus minus 10 microamps uh measurement capability. So, um uh yeah, it's got a maximum of plus minus 100, but uh I don't know. Let's go for our typical value, shall we? Just for purposes of today's experiment. Now,

**Dave Jones:** the problem with that is with a 12-bit um if we look up here, full-scale current sense voltage range with the program programmable gain amp set to uh one, gain of one, we can only get a maximum of 40 millivolts input voltage from our

**Dave Jones:** current shunt resistor. And because our current shunt resistor is fixed at 1 ohm, that only allows us 40 milliamps maximum current. So, this device, if it didn't have this programmable gain amp, if it just had a gain of one, we could

**Dave Jones:** only measure from zero to 40 milliamps, which is great if you've only got a zero to 40 milliamp supply, but our supply is zero to 1 amp capability. So, we need a way to measure greater values, and we

**Dave Jones:** can't change our current shunt resistor. Or we could, but then we need extra circuitry to do that MOSFET switching and maxing, and oh, it gets all really quite ugly. So, what we want to try and do is use that fixed 1 ohm current shunt

**Dave Jones:** resistor and change this programmable gain amp here to give us, and if you take a look at it, if you put in a programmable gain amp, that's not plus eight there, that's actually divide by eight in there. So, it's actually an

**Dave Jones:** attenuator. So, it can give you a maximum it can tolerate or measure a maximum of 320 millivolts across that current shunt resistor input. And at 1 ohm, that's zero to 320 milliamps, and it's got a couple of ranges in between. So, we can

**Dave Jones:** keep So, the microcontroller, the our Arduino, can know what current is coming out of this thing. If it's over range, automatically switch the range of this programmable gain amp, and actually keep very high resolution regardless of what current it's

**Dave Jones:** measuring. So, it can actually measure any current accurately at 12-bits from 320 milliamps right down to a maximum resolution of 10 microamps. That's a massive range, great capability in this one device, which only costs like a dollar 50, and we've eliminated our two

**Dave Jones:** other devices and consolidated into one. So, we've still effectively got pretty close to our micro our microcurrent measuring capability, but it's all consolidated in one device. I love it. It's a really brilliant device and they've got other devices

**Dave Jones:** that similar in the series that have actually got uh DAC output currents and almost uh a device which is perfect that actually has a current sense comparator and a DAC as well, but unfortunately, it's not quite suitable. So, I won't go into

**Dave Jones:** that, but you can have a look at uh that device as well, but hey, we've only got 320 milliamps. Where's our 1 amp range? This chip can't do it. Back to the schematic. And that brings us back to our

**Dave Jones:** analog-to-digital converter. We had our 12-bit converter before, but now it's built into this device and we now no longer have 12-bit uh measurement capability of our output voltage, but because we've only got a 10-bit DAC here anyway, why do we need a 12-bit

**Dave Jones:** measurement on our output? We don't. We only need a 10-bit resolution analog-to-digital converter to match our DAC. So, this current sense uh value over here, we I need to feed that into a 10-bit ADC. And of course, the Arduino, the microcontroller has a

**Dave Jones:** 10-bit ADC built in. So, we're going to take that ADC Vout and we're going to feed it directly into a pin on the microcontroller here, one of the ADC zero pins. There it is, measuring the Vout. But it's also

**Dave Jones:** measuring the battery voltage. We're using a second channel there. This AVR microcontroller has uh multiple channel uh analog-to-digital converters. And we're also measuring a third channel here, which is our ADC Iout, which actually takes the output voltage from here directly from the output of

**Dave Jones:** this rough-and-ready differential uh amp which we're using for our constant current set capability, but because that will give a direct output voltage in volts from zero to 1 volt output of pin seven there on the LM358 will be 0 to 1

**Dave Jones:** volt output for a 0 to 1 amp across our 1 ohm current shunt resistor or 1 mV per milliamp current sense output as my little yellow note there says. So, that allows us to give us a fifth uh current measurement measurement range

**Dave Jones:** just by having that one extra pin on the microcontroller there. Fantastic. So, we've got now this huge five spanned current measuring capability for 1 amp down to 10 microamps resolution with just a um current uh 1 ohm current shunt resistor,

**Dave Jones:** an INA219, and a rough and ready uh differential amp here. Brilliant. And of course, we have to feed our voltage reference into our uh microcontroller as well. So, we do that in on pin 21. It comes directly from our

**Dave Jones:** 2.048 voltage reference here. That that hasn't changed since uh we first originally uh since our first design. So, that um reference powers the DAC and the analog-to-digital converter as well. Uh we're still got our 0.1 uh 0.1% uh

**Dave Jones:** precision resistors in our voltage set capability. So, we shouldn't have to trim any of that in software. Might have to do a little bit of current trimming in um uh sorry, we've got 0.1% in our uh rough and ready, I guess,

**Dave Jones:** uh differential amplifier over here. And uh the current sense over here. And we've got now got a gain of uh 10 instead of a gain of five. So, our 0 to 2.8048 volt output from our digital-to-analog converter get multiplied that by a gain of 10,

**Dave Jones:** we've got 0 to 20.48 volts uh output or it gives us uh 20 mV per bit with that 10-bit DAC. And really, you know, that's good enough for a power supply of this class if we can set our

**Dave Jones:** output voltage in steps of 20 mV. Not a problem. So, I'm pretty happy with that. I'm pretty happy with that we've only got 10-bits output measurement range. We were gilding the lily before, as I said, with 12-bit analog-to-digital converters

**Dave Jones:** and 12-bit DACs. Crazy stuff. But hey, it was fun at the time. But now we've consolidated that into this microcontroller using the internal ADCs. We've got five devices hanging off our I2C bus. And of course, the more devices

**Dave Jones:** you have hanging off your I2C bus, the lower values you've got to have in your pull-up I2C pull-up resistors here because every device you add to the bus adds capacitance to the bus, which changes the I2C slew rate, which means that you

**Dave Jones:** can miss data bits. So, you can't have like a 10k pull-up anymore with five devices on there. That might be a bit dodgy. So, we dropped it down to 2k2. And really, I've added a reset switch here. We've still got our SparkFun FTDI

**Dave Jones:** Arduino-compatible interface. So, that also frees up You remember how we're talking about removing the heat sink on the back? It allowed So, now on the back panel connector, we've actually got room to put the Arduino interface on the back

**Dave Jones:** panel of the PCB. So, you don't have to open the case anymore to get in there to hook on your programming cable to program your Arduino device in there. And that brings us to our Ethernet capability, which I

**Dave Jones:** wanted serial, but capability from the very early get-go. But sort of that sort of morphed into pretty much Ethernet only capability. Although, you could actually hook on because we're having expansion sockets. This is not a chip. This is actually a module. So, we've got

**Dave Jones:** a 12-pin dual inline interface there. And pretty much we've had to dedicate all a whole bunch of pins all these pins down here from 14 through to 19 there through to the for the Ethernet interface. But, it's worth it

**Dave Jones:** cuz we were able to consolidate all the other pins onto there. So, we were able to free up these pins to dedicate to one of these WIZnet a WIZ820IO Ethernet module. Let's take a look at it. It's really quite nice. It's a

**Dave Jones:** pretty new. It's only been out for a couple of months. And it's under $20 or something like that. So, it's pretty much one of the cheapest solutions on the market. Dual inline 0.1 inch header. It's all integrated. It uses one of the

**Dave Jones:** WIZnet the WIZnet W5200 actual device on it with a magjack and everything. And it's 3.3 V powered. Perfect. It's a SPI interface, of course. It's got a power down pin, which is excellent because this our design is a battery powered power supply. So, if

**Dave Jones:** you're not using the Ethernet, you want to power the thing down. And the maximum power consumption down here when it's doing 1000 Base-T maximum uh speed is 120 milliamps. Uh it's not too bad. It's 3.3 V. It still certainly allows us to

**Dave Jones:** battery power the thing. It will actually chew extra power when you got if you got the Ethernet capability, but it's still not crippling. So, the power supply is able to use one of these modules. And it's optional extra. If you don't want it, don't plug

**Dave Jones:** it in. If you want it, pay your extra 20 bucks and you plug it in and add some software and bingo, you've got Ethernet capability on your power supply. So, I I love that. It's It's I think it's well worth uh just slipping

**Dave Jones:** in that capability and it can go directly on the back panel now that we don't have that big heat sink on the back. Just a cut out on the back. Ethernet straight in. We've got room for our FTDI

**Dave Jones:** serial programming interface over here and we've got room for our DC input jack and anything else we want to add on there. It's great. I love it. So, really they're the major um changes to this rev C circuit and

**Dave Jones:** hopefully you like it. I'm not going to say this is the final one. I just love tweaking designs like this. That's half the fun. It's just mucking around and you know, optimizing stuff, changing your mind. There's nothing wrong with

**Dave Jones:** doing that, but I think this is a really quite a neat solution. I'm pretty done happy with this one and I don't think I've missed any extra capability in there. All the All this operates the same. All the

**Dave Jones:** voltage regulation and current regulation and stuff like that and but we've added We've not only increased our output voltage range from 0 to 20 volts. We're powering from two 18650 cells. We've got It's much more efficient now, so we can get a higher

**Dave Jones:** output current capability at lower voltages and and it we extract greater capacity out of the batteries and it's got and we can switch it off low or high noise output with our regulator. We can enable, disable and it's just really quite neat. It's not

**Dave Jones:** quite as precision as the previous version, I don't think, but I think it's a very good trade-off and it should be a very neat, handy and novel power supply. So, I haven't actually built this thing up yet and

**Dave Jones:** tried it out, but it should work a treat. I mean, the the battery charging should uh work first go. That's not rocket science and the DC to DC converter straight out of the app notes, that should work. The e squared pot

**Dave Jones:** changing of the feedback voltage there, I've done that in other other designs and it does actually work, not a problem, but I haven't actually done it with this particular chip. We'll see if that capability works and once again, I won't

**Dave Jones:** go through like choosing diodes up here. It's a It's an SK 33A. It's a 3.5 amp 3 amp Schottky diode there rated to 30 volts, so hence the number SK 33A, 30 volts 3 amps and our inductor has to

**Dave Jones:** be three you know, at least say three times our output current capability. The Micrel 2253 supports up to I think it well, it's a 3.5 amp 3 amp switch switching device, but that doesn't mean you can get 3 amps output

**Dave Jones:** capability from it, but we should be able to get 1 amp out of it. But that's probably the only major thing which really needs to be tried, but apart from that, I'm pretty confident it should work. I haven't used the INA 219 before,

**Dave Jones:** but it looks, you know, I squared C interface, you got to believe the data sheet can do what it can do and it should be sweet. So, I'm probably going to lash up a board for this one and go straight to PCB cuz a lot of

**Dave Jones:** these SMD devices real bit of a pain in the ass to cobble it together. I might take a risk and just go straight to the PCB for this one and give it a go. So, there you go. Can't

**Dave Jones:** guarantee it'll be the final one, but I like it and I had fun doing it, which is the main thing. So, I'll keep you uh posted on any uh further updates to the design and the PCB when I finally get it done.

**Dave Jones:** But, let me know your feedback. Um if you've got any comments whether or not this was a good change or a bad change, whether you preferred the previous one or whether this one's um awesome and you didn't like the last one, let me know.

**Dave Jones:** Or if I've missed something uh before I go to the PCB, please bit of a crowd sourcing uh engineering design real checking here. I may have missed something. If I've done something dumb on the schematic, uh let me know. I'll post the schematic uh

**Dave Jones:** it'll be uh linked on the website so you can download it as a PDF. So, until then, I hope you enjoyed it. Catch you next time.
