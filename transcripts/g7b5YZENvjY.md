---
video_id: g7b5YZENvjY
title: EEVblog #72 - Let's Design a Product
url: https://www.youtube.com/watch?v=g7b5YZENvjY
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 29, "3": 41, "4": 53, "5": 71, "6": 80, "7": 86, "8": 97, "9": 112, "10": 123, "11": 132, "12": 142, "13": 155, "14": 172, "15": 179, "16": 190, "17": 198, "18": 213, "19": 236, "20": 254, "21": 266, "22": 285, "23": 296, "24": 310, "25": 336, "26": 344, "27": 355, "28": 368, "29": 377, "30": 389, "31": 402, "32": 415, "33": 430, "34": 441, "35": 458, "36": 473, "37": 488, "38": 507, "39": 516, "40": 532, "41": 546, "42": 556, "43": 573, "44": 594, "45": 611, "46": 626, "47": 635, "48": 651, "49": 670, "50": 685, "51": 706, "52": 722, "53": 738, "54": 755, "55": 777, "56": 789, "57": 801, "58": 818, "59": 832, "60": 843, "61": 860, "62": 873, "63": 892, "64": 915, "65": 927, "66": 938, "67": 953, "68": 964, "69": 973, "70": 987, "71": 997, "72": 1010, "73": 1024, "74": 1032, "75": 1043, "76": 1060, "77": 1071, "78": 1085, "79": 1100, "80": 1116, "81": 1131, "82": 1152, "83": 1161, "84": 1177, "85": 1186, "86": 1208, "87": 1219, "88": 1237, "89": 1250, "90": 1271, "91": 1287, "92": 1298, "93": 1310, "94": 1327, "95": 1338, "96": 1351, "97": 1363, "98": 1384, "99": 1402, "100": 1414, "101": 1432, "102": 1439, "103": 1451, "104": 1459, "105": 1480, "106": 1495, "107": 1509, "108": 1528, "109": 1543, "110": 1558, "111": 1572, "112": 1583, "113": 1598, "114": 1612, "115": 1626, "116": 1639, "117": 1652, "118": 1662, "119": 1679, "120": 1693, "121": 1709, "122": 1725, "123": 1741, "124": 1749, "125": 1760, "126": 1781, "127": 1798, "128": 1810, "129": 1823, "130": 1829, "131": 1848, "132": 1866, "133": 1876, "134": 1893, "135": 1903, "136": 1916, "137": 1929, "138": 1940, "139": 1960, "140": 1974, "141": 1981, "142": 1991, "143": 2006, "144": 2018, "145": 2034, "146": 2056, "147": 2067, "148": 2083, "149": 2091, "150": 2104, "151": 2116, "152": 2124, "153": 2143, "154": 2153, "155": 2170, "156": 2182, "157": 2189, "158": 2200, "159": 2211, "160": 2226, "161": 2237, "162": 2260, "163": 2271, "164": 2280, "165": 2297, "166": 2309, "167": 2321, "168": 2336, "169": 2344, "170": 2358, "171": 2370, "172": 2380, "173": 2391, "174": 2405, "175": 2418, "176": 2437, "177": 2458, "178": 2474, "179": 2489, "180": 2502, "181": 2517, "182": 2544, "183": 2559, "184": 2568, "185": 2579, "186": 2601, "187": 2618, "188": 2633, "189": 2647, "190": 2663, "191": 2674, "192": 2683, "193": 2704, "194": 2724, "195": 2733, "196": 2754, "197": 2772, "198": 2788, "199": 2812, "200": 2827, "201": 2843, "202": 2859, "203": 2873, "204": 2889, "205": 2901, "206": 2911, "207": 2922, "208": 2937, "209": 2955, "210": 2966, "211": 2993, "212": 3018, "213": 3043}
---

**Dave Jones:** Hi, welcome to the EEVblog an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, a viewer suggested sometime back if I could do a blog about designing a product from scratch, from start to finish.

**Dave Jones:** And well, it sounds like a good idea, but it's actually incredibly difficult cuz there's a lot of issues and concepts which go into a designing an entire product. But, I'm willing to give it a go.

**Dave Jones:** So, here we go. I'm going to show you how I designed a product from start from concept to finish. So, the best example I could come up with for this, I think, is my microcurrent adapter.

**Dave Jones:** You've seen it before and it was published in Silicon Chip magazine April 2009. And I think this is a really good example of how to design a simple product from start to finish cuz there's not much in the circuit.

**Dave Jones:** It's a very, very simplistic circuit, but as you'll see there's a lot more to designing a nice little product than just the circuit. So, what's the first step? Well, the first step is to define the problem and define what product you're going to design to solve that problem.

**Dave Jones:** In this case, it's burden voltage on multimeters. Now, I won't go into why burden voltage is a problem. You can see my previous one of my previous blogs for that.

**Dave Jones:** So, I won't go into why I'm actually going to design this. But, let's just say it's a problem and we're going to fix it. So, what do we have here?

**Dave Jones:** Let's take a look at the problem. The problem is you've got a power supply unit. You've got a multimeter which has a shunt resistor in there to measure the current when you're powering your particular circuit.

**Dave Jones:** Now, the voltage across here, the shunt resistor, is too high in a lot of cases and that causes all sorts of problems. So, we want to lower that value of shunt resistor and still use our multimeter.

**Dave Jones:** Okay, so what we want to do is design a little doohickey box that that works with our multimeter, that plugs in in series with it, and it lowers this value of shunt resistor here.

**Dave Jones:** It lowers the burden voltage. So, here it is. We need a box. Let's put dash. We need and we still need a current shunt resistor cuz that's how you measure current.

**Dave Jones:** You have a shunt resistor, and and you measure the voltage drop. Nothing's going to change there. There's no secret to it. So, it's very simple, but we just need to make it much lower than the one inside a typical multimeter.

**Dave Jones:** How much lower? Well, as always in electronics, you talk, you know, an order of magnitude or 10 times is always a good thing. So, 10 times less in value, that's not bad, but we'll go into that later.

**Dave Jones:** Maybe a hundred times. But, so the value will be lower, and because the value is lower, there's a kookaburra. Tell we're in Australia. Now, because the value the shunt resistor is lower, the multimeter's not going to be able to measure that value.

**Dave Jones:** So, you need an amplifier of gain that we haven't determined yet. So, that's it. That's all we're going to have in our box is a shunt resistor and an amplifier.

**Dave Jones:** Too simple. And there'll be a battery to power it as well. But, that's our entire product. But, let's look at the detail which goes into actually designing the final product.

**Dave Jones:** Next up, let's look at the basic specs we want to do. Now, the main problem I wanted to overcome is basically on the typically on the microamps and the milliamps ranges.

**Dave Jones:** I didn't really care much about the amps range. So, what we want to do is have multiple ranges. Obviously, one range isn't going to do the whole thing. It's just not going to work as we'll probably deduce later.

**Dave Jones:** So, we need something with different ranges. We basically need three different value current shunt resistors. Now, there's two basic ways to to do this. Either you have one set of input sockets like we do here, okay, and you switch in you you have a three-way Well, let's say a three-way switch and you switch in different current shunt resistor values.

**Dave Jones:** Or, you can have one ground terminal and then a different a different 4-mm banana terminal for each current range. But, these banana terminals are quite expensive and it's just it's it takes up front panel board space and I wanted to make this thing as small as possible.

**Dave Jones:** So, really I think I thought it was better just to um do the range switching based on a switch. Okay, so we've decided that we're actually going to switch the inputs for the different ranges.

**Dave Jones:** So, we get rid of this idea down here and now we need to figure out what value these resistors need to be for our different ranges. Now, because what we're basically trying to do here is use a multimeter to measure current, we can't use the existing current range on the multimeter because it has its own current shunt resistor.

**Dave Jones:** So, what we do is we use the voltage range of the multimeter, which just so happens to be the most accurate range, as we'll come into. That's actually an an important advantage.

**Dave Jones:** Now, as it turns out, usually the millivolt range on a digital multimeter is the most accurate and it's the easiest to use. So, that makes sense to use the 200-mV range on a 2,000-count multimeter.

**Dave Jones:** So, what we want is different current ranges. We want Let's say we want a direct convert current into voltage. So, we want 1 mV per milliamp for the milliamp range, 1 mV per microamp for the microamp range, and 1 mV per nanoamp cuz I think it might be handy if we include some nanoamps as well.

**Dave Jones:** Now, let's not limit our options here. We might actually want to measure amps as well just for good measure if it's easy to add to the design. But, we'll find that out later.

**Dave Jones:** So, you might have 1 mV per Now, let's look at what value current shunt resistors we need to do that directly. 1 mV per amp, um using Ohm's law is 1 m ohm.

**Dave Jones:** 1 mV per mA is 1 ohm. 1 mV per microamp is 1 k. 1 mV per nanoamp is 1 meg. They're what we need for the current shunt resistors, but really, that's the same as what's in a regular multimeter.

**Dave Jones:** We don't want that. We want to decrease it at least an order of magnitude or several orders of magnitude. So, um you know, we have to sort of make a decision there.

**Dave Jones:** One order of magnitude, 10 times, is pretty good, but I'd prefer 100 times. So, I'm just going to pick that as an arbitrary figure. I'd like my design to be 100 times lower.

**Dave Jones:** So, in this case, um 1 ohm equals 10 milli uh milliohms because we want it uh the value to be 1 100th of that value. So, it's 10 milliohms.

**Dave Jones:** Likewise, 1 k is 10 ohms, and 1 meg is actually 10 k ohms. So, they're the values for our three current shunt resistors if we use a times 100 amplifier.

**Dave Jones:** Now, we have to take a cursory look at the amps range to see if if it's easy to add to our design. Now, um a standard um for 1 mV per amp on a standard multimeter, it's a 1 m ohm shunt resistor.

**Dave Jones:** That's already very low. 1 mV per amp, and our typical multimeter has a 10 amp uh current range. So, it's going to be only a 10 mV drop. So, it's not really a big deal.

**Dave Jones:** So, I don't really think that there's a problem to be solved there by having amps. And when you go up um in very high currents like this, you have real problems with your connection resistances, um as we'll actually see later, even on the milliamp range.

**Dave Jones:** So, uh really, we, you know, amps is is quite hard to add. I mean, we could change that instead of 1 mV per amp, we could change it to 100 mV per amp and gain a you know, a 10 times advantage or something like that.

**Dave Jones:** But, you know, I I don't think there's a problem to be solved there. So, let's not bother. I think we'll scrap that amps range cuz we don't want to use a 10 microohm resistor to get the same to get the same ratio ranges as our other ones.

**Dave Jones:** So, it's a it's a bad idea. No amps. It's gone. All right. So, our basic design is taking shape. We have three different current ranges: milliamps, microamps, nanoamps. We have three different current shunt resistors, which are 100 times lower than a standard multimeter, basically.

**Dave Jones:** And to compensate for that, we've got a times 100 amplifier in there as well. And the good thing is is that there's a direct relationship between 1 mV and 1 mA, 1 mV 1 µA, and so on.

**Dave Jones:** So, that our multimeter is going to read directly in amps per millivolt. So, if you're on the 200 mV range and it's reading 200, you're actually reading 200 milliamps.

**Dave Jones:** That's really nice. You don't need any The user doesn't have to do any conversions or anything like that. So, that's a really nice design criteria, which we meet easily by having by not having oddball value resistors.

**Dave Jones:** We're going to choose them to give us a matching relationship between millivolts and milliamps. So, the design's pretty simple. We've got three current shunt resistors and a times 100 amplifier.

**Dave Jones:** It sounds pretty simple. But now, here's where the practical considerations come in. Now, if you know your basic op-amp theory, no op-amp is perfect, okay? That's going to have an input offset voltage, which is called VOS, okay?

**Dave Jones:** The input offset voltage can be, you know, in a typical general purpose op amp it might be millivolts, okay? But, that value is going to be because we've got a times 100 gain, if we've got a 1 millivolt offset on our op amp, we're going to get 100 millivolts offset we're going to get 100 millivolts offset.

**Dave Jones:** So, even when we're not feeding in any current at all, our output could read up to 100 millivolts. Now, if we're using the millivolt range, we're all you know, if it's going to read if we want 1 millivolt per milliamp, that means our output's going to read 100 millivolts.

**Dave Jones:** The user will think, "Oh, we're feeding in 100 milliamps." We're feeding in nothing like it. So, with the times 100 gain, we also need a basically a 100-fold uh reduction or so in that um V in that input offset voltage.

**Dave Jones:** So, we need to find a very schmick op amp that can actually do that. Now, we should look at how we're actually going to use this doodad with the multimeter.

**Dave Jones:** Let's take a bottom-of-the-range 3 and 1/2 digit 2,000-count multimeter, okay? We know we're using it on the millivolt range, okay? So, that's going to have a value of 200.0 millivolts, okay?

**Dave Jones:** So, its resolution is 0.1 millivolts. Now, when we feed in no current into here, we want it to measure nothing on the output. So, we need the offset voltage cuz we have a gain of 100 we need the offset voltage to be 100 times lower than this resolution, the least significant digit.

**Dave Jones:** So, 0.1 millivolts divided by 100 is 1 microvolt, and that's what we need for our V for our input offset voltage of this op amp. So, we need to look search for an op amp that can do um typically 1 microvolt offset.

**Dave Jones:** So, when we feed in no current into here, we basically read zero on our multimeter. Now, from my industry knowledge, I know one microvolt input offset voltage is incredibly low, and you're going to need a very, very schmick op amp to do it, and there's not many on the market that are actually going to meet that spec that we have here.

**Dave Jones:** So, but um I've done a blog on this before, as it so happens, and if you do your basic uh electronics theory, you'll do different types of um uh op amps, and one of them is called a chopper or an auto zero uh op amp.

**Dave Jones:** And these have the characteristic of having incredibly low input offset voltages. It's almost zero, cuz they automatically There's an automatic process inside the amplifier that um that nulls out the input offset voltage.

**Dave Jones:** Now, even if you didn't know about chopper amplifiers or auto zero amplifiers, what you would do in this case, if you want a one microvolt offset voltage, you would go on the web, and you would search either Digi-Key or Mouser or one of the other component suppliers that gives you a parametric search for for a particular op amp.

**Dave Jones:** So, you might type in op amp, and then you go into the op amp categories, you go into precision op amps or whatever, and then it's it'll have a whole list of tables of all the parameters, and one of them will be the offset voltage, and they'll be listed from .1 microvolts down all the way to, you know, a horrible one at, you know, 10 20 millivolts or something like that.

**Dave Jones:** So, what you want to do is you want to select the ones that are in the range, you know, .1 microvolts to to 1 microvolt or something like that, and then you want to narrow your search down to that.

**Dave Jones:** Now, you can also do the same thing on the individual manufacturer's website. So, you might know, if you're in the industry, you might know that Maxim do op amps, National Semiconductor, Linear Technology, companies like that.

**Dave Jones:** So, you'll go to their individual websites, but that can typically and do the same parametric search, but that can take longer. So, I often use Digikey or Mouser or uh you know, Newark or one of the other component supplies and search all the different brands parametrically.

**Dave Jones:** So, your parametric search spits out numbers like LMP2015 or LMV2011 or or the MAX4238 4239. So, what you do is you open up the data sheets for all these different chips and you start comparing them.

**Dave Jones:** In this case, our main requirement really is that input offset voltage. Now, what are the things you've got to um uh take into account with practical designs is uh temperature range.

**Dave Jones:** Things like input offset voltage and all sorts of other parameters vary over temperature. So, we don't want our product just working at room temperature. We want it to work over a decent um you know, industrial temperature range cuz that's good design practice.

**Dave Jones:** So, you will search the data sheets and you will look for the um typical input offset voltage over the entire temperature range, not just at not just at 20° C at room temperature.

**Dave Jones:** No, you want it over the whole range and and you compare these different chips and I compare them and it turned out that the um 38/4239 was was pretty much the best with um a typical offset voltage of 2.5 microvolts over the entire temperature range and it was a reasonable price.

**Dave Jones:** It's only a couple of dollars. So, I decided to base my design around that. And there are other things to look for as well like overload recovery with chopper amps and and uh and gain bandwidth product and stuff like that because but because this is a little current adapter and your average multimeter only has a couple of kilohertz bandwidth anyway, then pretty much any of these um chopper amps is

**Dave Jones:** going to meet the bandwidth requirements. So, the MAX4239 looked looked you know, fairly ideal And because Maxim have a nice free chip sample service, that's that's an extra sweetener.

**Dave Jones:** Even though I have issues with Maxim chips, um, I put that aside and I decided to go with the Maxim device this time. So, we've chosen our Max4239 chip.

**Dave Jones:** Now, if you look at the data sheet, it has a, um, VOS, a typical VOS of 0.1 microvolts. Beauty. At all, but the main thing is is that it's, um, offset voltage still microvolts over the entire temperature range.

**Dave Jones:** So, even absolute worst case, if we feed no current into here, um, times 100, we're only going to get, um, 2.5, it's only going to read plus minus 2.5 on the meter.

**Dave Jones:** And well, it's, you know, in practice it's going to be better than that. It's going to be, you know, 0.1 or something like that. So, I can live with that.

**Dave Jones:** That's fine. So, let's give it a go. Okay, so we now have our basic circuit. We've got three different current range resistors, 10K, 10 ohms, and 10 milliohms via an input switch, which switches the range.

**Dave Jones:** And we're also going to need a switch as well, which is a dual ganged switch to actually, um, tap off the, uh, voltage from one of the resistors into the amplifier.

**Dave Jones:** So, we need a three, we need a double pole, uh, three-way, uh, ganged switch there. Now, we've got our Max4239 as configured as a times 100 amplifier here, and that's it.

**Dave Jones:** That should give us our basic functionality that we're after. But there's one other thing to consider as well. Now, um, do we use a standard single-ended amplifier, or do we implement a differential amplifier?

**Dave Jones:** Well, bit because we're not, um, dealing with long lines or anything like that, our current shunt resistor is going to be on the same board, right next to the chip.

**Dave Jones:** We don't really need a, uh, differential amplifier. And because the whole thing is going to be battery powered in a box, there's no problems with you know, mains reference or any other system reference like that.

**Dave Jones:** So really, we can get away with just a single-ended amplifier. So all we need is a positive times 100 gain so that we configure the op amp in a standard non-inverting configuration of times 100.

**Dave Jones:** So what values do we choose for the non-inverting values? Well, because we don't want to use too much current, it's going to be battery powered, we'll make that one say 1K and this one has to be it has to have a gain of times 100.

**Dave Jones:** So your basic formula for your non-inverting op amp is R1 on R2 plus one. So if this is 1K to give you a gain of 100, this needs to be 99K.

**Dave Jones:** So 99K divided by 1K is a gain of 99 plus one gives you a gain of 100. Easy. And because we're only dealing with you know, a bandwidth of only several kilohertz, um these values can be reasonably high and you don't have to worry about stray capacitances and all that sort of stuff.

**Dave Jones:** Now there's one other thing I mentioned before about the large current ranges, the amps range. Um the contact resistances on the components and the connectors and things like that can make it can swamp the value of your low value shunt resistor.

**Dave Jones:** Well, even on our milliamp range here, this is our milliamp range. We've got a value of 10 milliohms. Now, that's very that's that's actually very low. Um and your contact resistance of a typical switch might be in the order of milliohms.

**Dave Jones:** So it's going to be it's you know, it's going to swamp that. It's it's going to swamp that in terms of accuracy. So when you're measuring something, you don't want to measure between ground here and this and the input connector because then you're actually measuring effectively a resistor in series with that that might be say, you know, or it might be 1 milliamp.

**Dave Jones:** So, what? 1 milliamp? So, you're 1 milliamp in series with 10 milliohms, you've got 11 milliohms. Your accuracy has just gone out the window. So, you don't want that.

**Dave Jones:** So, what you need is to tap it straight off the actual resistor like that. So, you want to actually connect it right onto the junction. I'll show it like this, but it's actually the junction right on the actual resistor.

**Dave Jones:** Now, you can actually get special current shunt resistors that do exactly this. They've actually got four terminals on them. Um your regular resistor and then two sense terminals like that.

**Dave Jones:** So, that's what you actually want to tap off into the amplifier, so it doesn't matter what the switch um the value of the the resistance of your switches. Now, your switch is going to affect your bur- the um total burden voltage on the milliamp range, but that's not a big deal cuz we're still an order more than order magnitude lower than a regular multimeter.

**Dave Jones:** So, it's just fine. And of course, when we're talking 10 ohms and 10k on the other ranges, well, you know, the contact resistance of the switch doesn't matter. There's yet another thing you have to think about.

**Dave Jones:** There's always something to think about in even basic designs like this. In this case, it's the operation of it. We want to measure current um positive and negative. So, if the current actually is flowing in like that, it's going to generate a positive voltage across there and it's going to generate a positive um output there.

**Dave Jones:** But, what if we've accidentally used this hooked it up backwards or the current is um AC? Then, it's going to be flowing in that direction. In this case, we're going to get out a negative voltage with respect to our output ground terminal.

**Dave Jones:** So, what we need we can't power this off from a single supply. We're going to need a dual supply. So, we're going to need a positive supply and a negative supply so that um if this is your input ground here, okay, this input terminal is effectively ground because it's battery.

**Dave Jones:** It's just an internal ground. It's not mains earth reference or anything like that. If we power this from positive and negative supplies, then our op amp can actually get out can generate positive and negative output voltages and that's what we want.

**Dave Jones:** Okay, so that's no big deal. You need a positive and negative supply. What's so hard about that? Well, there's actually a bit of thought which needs to go into this as well and it's about the practicality of your whole design and things like that.

**Dave Jones:** There's three different methods you can use to get a positive and negative supply from some from batteries from a little device. The first one is to put two batteries in series like that.

**Dave Jones:** In this case two double A's or triple A's, 1.5 volts each and the center tap becomes the ground and then the either side becomes the positive 1.5 and the negative 1.5 or positive positive three if you put two in series and negative three if you put two in series etc.

**Dave Jones:** Now look, that seems like an easy way to do it. But the problem with that is that the is that the current drain is actually going to be the current drain could be different for your different cells.

**Dave Jones:** So that means a good design I wanted to have a low battery voltage detecting this. So how do you detect when your battery is low? You've got two separate batteries drawing drawing different currents.

**Dave Jones:** So really there's there's practical considerations there which pretty much ruled that one out if you wanted an easy to design low voltage battery detection circuit. So you think about the second one.

**Dave Jones:** And the second one is to generate is to have two batteries in series the same. So you have three volts say or a single coin cell lithium or whatever and then you use a switch capacitor voltage inverter like the classic um uh 7660 voltage inverter and that actually just inverts your voltage from +3 to -3.

**Dave Jones:** So, this point's ground here, and it's you've got +3 here, and it generates -3. Now, the problem with that is that um these can generate noise. They generate switching noise, so you've actually got to filter that and take that into consideration as well.

**Dave Jones:** And in a very low uh noise design like this one, we're talking about, you know, we're talking about microvolts. So, really it's a bad idea to introduce a switching element into your design.

**Dave Jones:** And it also costs money as well. It's an extra bill of materials part. You need a couple of capacitors. And well, it's it's just not the preferred method. So, um number three is to get your same batteries, a 3-V battery, and then you split it in half with two series resistors here.

**Dave Jones:** Now, these need to be very high value, so you might make them 100k or something like that, so you're not draining your battery voltage, and you tap off that the same value.

**Dave Jones:** So, you tap off, you're effectively tapping off 1.5 V, and then you need to buffer that with a with a um a voltage follower op-amp so that it's low impedance, and that becomes your ground.

**Dave Jones:** Now, you're not actually shorting the output of there because it's not actually referenced to anything. This becomes the ground. The output of the op-amp becomes the ground of your circuit.

**Dave Jones:** And then um by that nature, you've got +1.5 V and -1.5 V, and bingo. There's um you've got a single low-cost um cheap op-amp, no switching noise, and you've generated your plus minus rails, and then you've only got a single battery to worry about for your low-voltage battery detection circuit.

**Dave Jones:** So, I choose number three. With this third option, you can actually buy a chip which actually just does this. It's a it's a specific voltage um supply splitter chip, and it essentially integrates the the the two resistors and the op-amp in there for you.

**Dave Jones:** But, they're fairly exotic and they actually they're not that cheap. They might be like a dollar each. Whereas a a you know, a jelly bean op-amp with you know, doesn't matter what the input offset voltage is in this case, can be you know, 10 or 20 cents.

**Dave Jones:** So, and and the resistors cost virtually nothing. So, we'll go with this option. Now, because we actually have ranges based on milliamp, microamp, and nanoamp I in order of a thousand, that means I'm to switch up to the next range, you have to go to a thousand millivolts output voltage on the device.

**Dave Jones:** Now, that's within the plus minus 1.5 volt range of the device. So, that's perfect. And a typical meter is going to be either it's going to be either 10,000 count or lower.

**Dave Jones:** If it's 20,000 count, it just means you get an extra digit of resolution. It doesn't mean that it goes to two volts or something like that. So, everything everything seemed to fit it and we can easily power the device from 1.

**Dave Jones:** plus minus 1.5 volts. Not a problem. Now, there's a choice of two parts with the max and max 4238 or the max 4239. Chose the max 4239 because it's a higher bandwidth version, but its only limitation is that it needs a gain of 10.

**Dave Jones:** But, we're going to use a gain of a hundred. So, there's no problem at all. So, we'll go with the higher bandwidth part. Okay, this is terrific. Our circuit's really coming together.

**Dave Jones:** Here it is. We have our three range resistors. We have a dual ganged switch. We have our times 100 gain precision max 439 op-amp. Let's whack in a series resistor there just to provide some overload protection for the op-amp so the internal diodes can clamp.

**Dave Jones:** Let's add a hundred ohm series resistor on the output so that it ensures stability the op-amp if it's driving a capacitive load. We don't want it to do something silly or if you short it out, we don't want to ruin the op amp.

**Dave Jones:** So, um we choose 100 ohm and 100 ohm, nice round values, no reason for them, they're just nice and round. They do the job and you want to try and keep values similar in a design to lower your bill of materials parts count as well.

**Dave Jones:** Even though they're the same cost, you don't want to use 100 ohms here and and 220 ohms here because, well, you know, that's just silly. But, you've got to be careful with this output resistor because, you remember, we're driving a multimeter and it's got an input impedance.

**Dave Jones:** So, you don't want to get extra induced error there, but most digital multimeters are going to be 10 megaohms. Now, if you put 10 megaohms, if you do the math, 100 ohm in series with 10 megaohms, the error is negligible.

**Dave Jones:** In fact, you have to get down to about 100 K input impedance of the meter before the 100 ohms starts being a problem at about 0.1 uh percent error.

**Dave Jones:** So, really, it's, you know, it's 100 ohm is a good value to protect it and not provide excess error when you're driving a meter. One of the big things to take into account is the type of battery, the battery voltage, and also your compatibility with the main device you're using.

**Dave Jones:** Now, the MAX4239 can work anywhere single supply from 2.7 volts to 5.5 volts. So, um we don't want though we're powering it from a split supply, the op amp doesn't really realize that, it just thinks it's a single supply.

**Dave Jones:** So, if you're powering it from a 3-volt battery, plus minus 1.5 volts, that's fine, that's within the range, but the battery voltage is going to drop. So, in this case, you don't want it to go um essentially below that 2.7 uh volt minimum uh operational range for the chip.

**Dave Jones:** So, if we decide to power things from 3 volts, then we need a low voltage battery detection circuit which cuts out at about 2.7 volts. Now, there's many ways to do low voltage battery detection circuits, but they're all very essentially the same thing.

**Dave Jones:** They have a voltage ref- a a precision voltage reference and a comparator. Once it drops below a certain level, it switches on an output and you can turn on an LED saying, "Low voltage." Now, um I didn't want to muck around with things like that.

**Dave Jones:** It turns out that you can get a whole slew, if you go on Digi-Key or Mouser, you can get a whole slew of these dedicated low-voltage battery detection chips.

**Dave Jones:** They're a tiny little uh tiny little um three-pin device and they just um give you an output once they get a below a predetermined level and you can buy them in different voltages.

**Dave Jones:** In this case, I bought the TPS um 3809L30, which is actually a 2.65 V um reference device. So, when the input voltage from the battery drops below 2.65 V, which is close enough to operational range of 2.7, it um we well, in this case, it's got a negative output, so it switches the LED off.

**Dave Jones:** So, I'm going to have a feature on the the LED is on when it's above 2.65 V and the LED turns off when it's below. So, if the LED's off, that's determines that it's you know, you've got low battery.

**Dave Jones:** Woo! There you have it. That's essentially our circuit and this is what essentially the final design of my MicroCar, what was published in Silicon Chip and the product I actually sold.

**Dave Jones:** So, um but that's not the end of the story. No, because a design a product design is much more than just the circuit. Sure, you can build this up on a bit of a vero board or on a breadboard and you know, it's it's it's going to work.

**Dave Jones:** It's going to do the job. Well, apart from the low-noise stuff, but let's not go into that. Um you can build it up and it's going to work. But that doesn't make a good product.

**Dave Jones:** Um there's lots of choices which will also um back interact with this circuit. So, you might have to change the circuit uh later based on the physical construction and the price constraints and other constraints in your to actually get your practical product.

**Dave Jones:** So, let's take a look at that. Now, although I designed the circuit first in this video, that's not necessarily the order that I'm going to do it when I design a a practical project like this because um functionality and the form factor can make or break your product as well as can the price.

**Dave Jones:** Price point is very important. So, I wanted this design to be small and low cost. Like um I could put it in a standard large size Jiffy box like this.

**Dave Jones:** I mean, in in Australia, we've got these Jiffy boxes and they're sold by Jaycar and and Dick Smith and Altronics and and others and they're pretty much a standard box and you drill holes for your switches and you drill holes for your terminals and you there's things to mount your board inside there.

**Dave Jones:** There's little standoffs to mount your board and you screw them screw in your board and then you wire things to the switches and well, that's that's pretty amateurish. Um and it can actually add to the cost and the complexity.

**Dave Jones:** So, I wanted something smaller and low cost. So, I put a got a fair bit of effort into actually minimizing the parts cost at the circuit design stage as well as the um assembly stage, too.

**Dave Jones:** So, I pretty much decided that I didn't really want to put in one of these large size Jiffy boxes although there's plenty of room to make it fit. So, I decided the to get the smallest Jiffy box which also happens to be the lowest cost.

**Dave Jones:** It's the UB5 Jiffy box and that's what I actually turned into the product because these Jiffy boxes you can get for like, you know, a dollar 20 or something like that in in reasonably small uh volume.

**Dave Jones:** So, they're very cheap and simple to design around. The next decision you're going to make is how you're going to do your front panel. Now, it it comes with a it comes with a lid like this which you can have uh professionally silk screen, but that's an extra step and it costs money.

**Dave Jones:** And then you got to have it punched or drilled for your switches and your terminals and your LED and stuff like that. And it's just it's really annoying and it just adds to the cost and complexity of of doing a small project run for something like this.

**Dave Jones:** In this case, you might want to make 50 or 100 of them. Going to the effort to silk screen and punch a panel can be a pain in the ass.

**Dave Jones:** So, I want to avoid that. So, what I did is I reverted to one of my standard techniques to make use of the PCB. I've got to design a PCB anyway, right?

**Dave Jones:** So, why not make it duplicate it as the front panel and mount all your components on the board. So, that's exactly what I did. Here is the micro current and it's everything's mounted and self-contained on that one board.

**Dave Jones:** There's no wiring at all. And I made it fit the standoffs in here and it just so happens the standoffs sit below the surface by 1.6 mm. You stick the board in there and it becomes the front panel.

**Dave Jones:** And it and it looks very professional. Now, side effect of using your PCB as your front panel and your entire for your entire design is that well, unless you want to see the circuitry on the top, which you don't, you've got to put it all underneath.

**Dave Jones:** And you don't want to see the solder joints on the top. So, that means you're forced to use surface mount components. So, it was pretty obvious early on in my design decision that everything every chip I chose, every part had to be a surface mount part to meet this design criteria.

**Dave Jones:** All right. So, I've made the decision to put in a small UV5 Jiffy boxes. Just enough room for your two output terminals. In which case, these output terminals have to be these banana 4 mm banana posts.

**Dave Jones:** They have to be the standard 19 mm industry standard spacing and you got to use these binding posts that double as banana jacks, so you can use um standard uh multimeter banana plug probes, or you can actually screw wires into them as well.

**Dave Jones:** Now, these are reasonably expensive, so but you know, pretty much I didn't have a choice. Um I had to use those, or I wanted to use those, for the input.

**Dave Jones:** But, for the output, I don't need that, because it's just going to the multimeter. So, although it's always a good idea to uh to use common parts in your design to lower your bill of materials, not at the expense of overall project cost.

**Dave Jones:** In this case In this case, the input banana um binding post terminals, they're expensive. So, I didn't want to use them on the output, because really, the output's just permanently connected to a multimeter.

**Dave Jones:** You don't want to wire it up. You want to just use banana plugs that plug in like that, which then goes into your multimeter. Simple. So, I used the low-cost, super-cheap ones.

**Dave Jones:** They're about a quarter of the price. Um these little tiny 4-mm um mounting posts. So, that lowered my project cost considerably. Next up was wiring. I didn't want to wire the damn things, cuz that's an extra assembly step, and that adds cost and complexity.

**Dave Jones:** So, what I did is I just put large pads on the on the back on the designed them into the board, and then I just used the existing screws to mount them on there.

**Dave Jones:** Same for the Same for the banana terminals as well. Now, in in case of the banana/binding terminals, they they can come loose, so you got to put two screws on there to hold it in place, and and a bit of Loctite sometimes, but that works, and I can There's no wiring at all in this entire design.

**Dave Jones:** It's nice. Next up was your battery consideration. Do I use double A's, triple A's? We've determined that I 3 V is a good voltage to actually choose for that, but well, what do you use?

**Dave Jones:** Double A's, triple A's, or lithium coin cell? Well, in this case, I didn't want extra wiring and have the batteries rattling around in the box and things like that.

**Dave Jones:** So, I decided to go for a lithium coin cell battery, which goes straight on the board like that. I got a surface mount one, and you plug in a standard CR2032 battery.

**Dave Jones:** So, um I made that choice pretty early on. So, when I chose the parts for my design, the Max um 4239, the uh the current um draw of that chip was important.

**Dave Jones:** Same with the op-amp for the uh voltage splitter the low voltage battery detection circuit. Uh one of my requirements for choosing those devices was low power consumption, so that it chose the lowest power consumption possible when it was switched on.

**Dave Jones:** And the other thing is, when you got a board as your front panel, how do you mount an LED on there? Well, you can solder it on the top, but then that's an extra assembly process, because you got to put it on the top instead of the bottom with all of the other parts.

**Dave Jones:** So, what I did is you got you can get these reverse LEDs, which actually surface mount ones that actually instead of emitting Here's Here's the actual LED here. So, instead of actually emitting from the top, like and coming out like that, which would actually come out the bottom of my board, I just drilled a hole in the board as as part of the PCB, file, put a hole in there, and it emits

**Dave Jones:** from the bottom of the device, and comes out the front panel. And it works really well. So, the design's really starting to fall into place. I've got ways to mount my connectors, do a cheap front panel, which is integrated into the board.

**Dave Jones:** It looks good. Get a red solder mask. It's red, looks sexy. I've got a way to mount my LED. Now, I've got a way to mount my battery with no wiring.

**Dave Jones:** It's all looking quite good. What's the last thing left? Well, the switches. Now, because I'm using the PCB as the front panel, I can't use one of those traditional toggle switches, cuz they would have stuck up about that far from the board, and they'd look really ugly if I got like a through-hole version.

**Dave Jones:** Um and I I really mount it through the board, cuz then it would have on the bottom, and that I didn't want to do wiring. It defeated the whole nice purpose of, you know, having everything surface mount, really.

**Dave Jones:** So, I once again, I did a parametric search for a double pole three throw switches PCB mount, and a slide switch is what I was looking for. So, I found a I found this C&K.

**Dave Jones:** As it turns out, there weren't too many actually that were actually available. So, I found this C&K nice C&K size slide switch. It was available in a vertical one and a right angle.

**Dave Jones:** And the right angle's good because I can put the silk screen on the board like that and just have the lever right next to it, which points to the silk screen.

**Dave Jones:** Really quite nice. And it's only about 20 cents or something. Beauty. So, I decided to base my design around those. Now, because I needed an on-off switch as well, I had to buy this special C&K switch.

**Dave Jones:** Well, it makes use to once again use common parts. So, I decided to use the same switch for the on-off switch. Now, because it's three pole double throw, I thought, "Aha, I don't just want to go on-off.

**Dave Jones:** Maybe I can have different modes." So, it has different modes. You switch it off, and then you switch it on with battery detect, and the LED comes on. Now, the LED actually draws excess current.

**Dave Jones:** And if you're using this for a long time, you don't want to drain your battery. So, you can add a third mode where it stays on, but it switches the LED off.

**Dave Jones:** And that's exactly what I did. There was one limitation with the switch, and that it could only handle a limited current up to several hundred milliamps, and it had a fairly high on resistance, which would contribute to the burden voltage, but it wasn't too much of a big deal.

**Dave Jones:** So, especially considering the price and the suitability, and it looks nice, then I, you know, I there weren't too many other choices, and this was a clear winner. And it was quite fortuitous that I only wanted to be at a couple hundred milliamps max anyway.

**Dave Jones:** So, really it was a great choice. Now, I find that often when I'm designing a product and designing a circuit or whatever, the there are often these fortuitous circumstances that conspire to sort of move your project in a certain direction based on these certain lovely parts you can get.

**Dave Jones:** You find they're an exact fit, and it's lovely. Things like getting the switch I wanted for cheaply, and it just met the current range I wanted. Things like my Maxim chip I wanted to use happened to just cut out at the 2.7 volts right at the cut out voltage of a lithium coin cell battery.

**Dave Jones:** Things like that. Really nice fortuitous design aspects, which really help make a good product. And a good designer will look for those things and take advantage of them. And as you can see, that's what I've got down here in the circuit.

**Dave Jones:** By fortuitous use of the same range switch up here, using it for the battery detect, I was able to switch between either by part turning off or on the low voltage battery detect chip to save and the LED to save power.

**Dave Jones:** And that was a really neat little nice touch to make it a bit more professional product. Now, to choose my op amp for the voltage divider zero volt reference, once again I used the parametric searcher.

**Dave Jones:** I go in and choose a generic op amp. I didn't care about the offset voltage or anything like that or the bandwidth cuz it's just a voltage follower, and it doesn't matter if I was millivolts, you know, 10, 20, 50 millivolts off on the center voltage.

**Dave Jones:** It's not really going to care that much. So, really my main requirement for this was low power to to minimize the draw from the battery. So, in this case I did a parametric search by price and power consumption and pretty much the LMV321 popped out and that's just a low power version low power low voltage version of the classic LM351.

**Dave Jones:** Now the other thing you've got to consider as well is the accuracy of the device. Now a typical cheapo multimeter might be 0.5% basic DC volts accuracy and a good meter might be 0.1% or 0.05%.

**Dave Jones:** So um but the current ranges, this is the other thing why I wanted to do this project. The current ranges on most mid to low multimeters aren't very accurate at all.

**Dave Jones:** They might be 1%, 1 and 1/2, 2%. So they're pretty horrible. So I wanted this thing to be pretty good. You know, I didn't want it to be 1% or 1/2 a percent.

**Dave Jones:** So I decided to use point I decided on a basic spec of roughly 0.1% cuz you can buy 0.1% resistors very cheaply. So the two current the microamp microamp and the nanoamp ranges, you just simply buy 0.1% resistors and that sets the tolerance there.

**Dave Jones:** The gain of the op amp, these two resistors are important so you use 0.1% resistors there. But the milliamp current shunt, the 10 milliohm current shunt, it's it's not impossible but it's very difficult and expensive to get a 0.1% 10 milliohm shunt resistor.

**Dave Jones:** So once again, I did parametric search in Mouser and Digi-Key to see what I can get off the shelf and it turns out it popped out was a 0.5% 10 milliohm current shunt resistor in the four terminal arrangement which we needed.

**Dave Jones:** So I used that and that's the only limitation so the milliamp range is roughly 0.5% ignoring that and the others are roughly 0.1 plus 0.1, you know, 0.2% uh over the temperature range.

**Dave Jones:** So, they're pretty good specs and that means that the microcurrent design is also going to improve the accuracy of your measurements, not just due to the burden voltage, but because it uses your DC millivolt range instead of your current range.

**Dave Jones:** So, I've decided all this sort of stuff, the circuit, how it's going to be constructed, everything, before I even prototyped the circuit to see if it worked cuz I pretty much knew the circuit was going to work.

**Dave Jones:** It's so simplistic, the chip chips are going to meet their specs and and you're putting some bypass caps and they're not going to oscillate and it it should work just fine.

**Dave Jones:** So, I jumped straight into doing the actual design of the board and I pretty much got it first go. I actually had to do another spin of the board because the old one um actually I didn't get the fonts right and they were too small and stuff like that, but um yeah, pretty much it went first go and bingo, out the end popped the full one product.

**Dave Jones:** And it was low cost, it was only about $17 in parts all up for everything in this. So, it's it it easily met the uh price. I didn't really know what my price target was, but I know I didn't want to spend 50 bucks in parts cuz then when you try and sell it, well, you got to sell it for 100 plus dollars and you know, that's

**Dave Jones:** just crazy. No one's going to pay that. But um yeah, even even in very small quantities, the price was only, you know, 15, 17, sort of under that $20 mark, which was beautiful.

**Dave Jones:** Which means it can be sold for 40 or 50 dollars. Once you build up your prototype, the only thing left is to measure the performance of it. Now, I just so happen to have a uh Keithley picoamp current source, so I can generate uh precision uh currents down to the picoamp range, so I could easily measure the nanoamp uh range of this device.

**Dave Jones:** Now, I added the nanoamp range on here cuz I thought it'd be real handy, but I knew it would be extremely sensitive. So, um a standard test for just testing input sensitivity to external fields is to get your mobile phone and put it near it and dial a number.

**Dave Jones:** Actually, you know, actually make it transmit and put it near the input terminals. In this case, it still worked pretty well cuz it's a nice tight layout and it just seemed to tolerate external electromagnetic fields pretty well.

**Dave Jones:** So, it worked. It worked a treat really. And I also at the time had access to a audio precision very expensive audio precision audio analyzer. So, I was able to measure the the bandwidth of this thing and the noise and the total harmonic distortion and the noise noise floor and the bandwidth over the entire range.

**Dave Jones:** And if you take a look at my article for it, you can actually see those plots. So, out the other end of all that design processes, probably more things which go into it and I've probably missed a couple of quite a few little subtle things which I put in there as well.

**Dave Jones:** Extra effort went into certain aspects and decisions and stuff like that, but I couldn't do them all. BUT WHAT POPPED OUT the other end was a really cool little product which is reasonably reasonably low cost and there's nothing else on the market like it.

**Dave Jones:** So, very often in a lot of my product designs, I will the circuits are you know, the circuit is almost totally irrelevant. It's all about form factor, meeting a price point, usability, things like that.

**Dave Jones:** They're what's going to appearance of the design. They are what's going to they could make or break your product. So, really, you know, you can't just slap something in a in a jiffy box and whack some switches on it and stuff like that and expect it to be a winning product.

**Dave Jones:** That's not necessarily the case. So, um I hope that next time you design something, you'll actually put a lot of thought into a lot of little subtle aspects of it and it's electronic design is more than just circuit design.

**Dave Jones:** Now, the other major thing you've got to think about during the whole design, not just up front, and I should have probably mentioned this right at the start as well, is that you've got to think about what the target what your target market or your target audience is.

**Dave Jones:** Now, in this case, it wasn't just for me. Otherwise, I would have just, you know, slapped it in a box and and put some Letraset lettering on it or something like that, real simple stuff.

**Dave Jones:** Um but no, I wanted cuz I knew friends and colleagues would want one as well, and I also thought, "Hey, it'd be great project to share with share with the community as well."

**Dave Jones:** So, I thought, "It would make a real interesting construction article in a magazine like Silicon Chip." So, I knew that I would have to my target market was the the you know, a small run of kits or something like that.

**Dave Jones:** I knew people would want kits or ready-made ones. You know, we're only talking about, you know, a couple hundred. We're not talking 10,000 or something like that. So, really those sort of choices that that market will determine a lot of your component choices which go into your design, component and other aspects of the design as well.

**Dave Jones:** Whether you're going to assemble it yourself, whether you're going to test it yourself, whether you're going to get somebody else to do it, or whatever. There's lots of factors there which can go into it as well.

**Dave Jones:** You have to take into account from the start of the project. Now, if you do a breakdown on how much time and effort actually goes into designing the actual circuit as opposed to the actual product, you'll find you'll probably spend most time searching for suitable parts to find to meet some design criteria or circuit design criteria and/or a visual usability functionality design criteria as well.

**Dave Jones:** So, uh, a lot of electronics design is not just grabbing, you know, parts from your junk bin and slapping something together. It's It's It's really making a lot, you know, sometimes hundreds of little individual choices, and each one of those can involve hours, sometimes hours of searching for each one of those decisions to come up with the best choice to go into your final product.

**Dave Jones:** Woo! So, there you go. That's how I designed a product from concept through the final design. And as you can see, there's more than just designing circuits. There's all sorts of things, even a simple design like this, which is basically a shunt resistor and an op-amp in a box with an LED and a switch and a couple of switches, there's there's more subtleties that go into designing a a

**Dave Jones:** decent quality product like this. So, I hope that's been useful for you, and you can make use of those techniques in your next design. See you.
