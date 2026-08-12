---
video_id: Lg6oYFerUlA
title: EEVblog #232 - Lab Power Supply Design Part 5
url: https://www.youtube.com/watch?v=Lg6oYFerUlA
source: youtube-asr
timestamps: {"0": 0, "1": 8, "2": 36, "3": 49, "4": 63, "5": 76, "6": 88, "7": 102, "8": 115, "9": 130, "10": 138, "11": 145, "12": 163, "13": 177, "14": 188, "15": 196, "16": 219, "17": 235, "18": 243, "19": 271, "20": 287, "21": 304, "22": 317, "23": 328, "24": 348, "25": 359, "26": 370, "27": 384, "28": 397, "29": 410, "30": 431, "31": 441, "32": 474, "33": 486, "34": 507, "35": 537, "36": 548, "37": 559, "38": 571, "39": 584, "40": 598, "41": 620, "42": 641, "43": 655, "44": 668, "45": 682, "46": 699, "47": 711, "48": 721, "49": 733, "50": 747, "51": 769, "52": 781, "53": 791, "54": 807, "55": 824, "56": 840, "57": 850, "58": 862, "59": 874, "60": 894, "61": 914, "62": 922, "63": 936, "64": 946, "65": 958, "66": 982, "67": 999, "68": 1010, "69": 1033, "70": 1048, "71": 1061, "72": 1074, "73": 1083, "74": 1097, "75": 1111, "76": 1121, "77": 1139, "78": 1153, "79": 1171, "80": 1184, "81": 1200, "82": 1216, "83": 1232, "84": 1245, "85": 1261, "86": 1275, "87": 1286, "88": 1301, "89": 1315, "90": 1333, "91": 1348, "92": 1363, "93": 1375, "94": 1386, "95": 1396, "96": 1406, "97": 1421, "98": 1433, "99": 1453, "100": 1467, "101": 1477, "102": 1491, "103": 1506, "104": 1519, "105": 1529, "106": 1546, "107": 1556, "108": 1571, "109": 1588, "110": 1603, "111": 1616, "112": 1629, "113": 1647, "114": 1661, "115": 1681, "116": 1699, "117": 1713, "118": 1726, "119": 1738, "120": 1751, "121": 1771, "122": 1784, "123": 1794, "124": 1805, "125": 1817, "126": 1826, "127": 1842, "128": 1852, "129": 1874, "130": 1887, "131": 1900, "132": 1912, "133": 1922, "134": 1936, "135": 1948, "136": 1959, "137": 1972, "138": 1985, "139": 2004, "140": 2021, "141": 2041, "142": 2056, "143": 2067, "144": 2082, "145": 2098, "146": 2118, "147": 2134, "148": 2154, "149": 2172, "150": 2189, "151": 2207, "152": 2226, "153": 2233, "154": 2248, "155": 2258, "156": 2274, "157": 2283, "158": 2304, "159": 2323, "160": 2336, "161": 2350, "162": 2362, "163": 2378, "164": 2391, "165": 2403, "166": 2416, "167": 2440, "168": 2456, "169": 2477, "170": 2507, "171": 2521, "172": 2532, "173": 2560, "174": 2574, "175": 2587, "176": 2597, "177": 2606, "178": 2619, "179": 2635, "180": 2648, "181": 2659, "182": 2669, "183": 2684, "184": 2695, "185": 2714, "186": 2742, "187": 2751, "188": 2773, "189": 2788, "190": 2797, "191": 2818, "192": 2827, "193": 2844, "194": 2866, "195": 2881, "196": 2893, "197": 2909, "198": 2921, "199": 2937, "200": 2953, "201": 2965, "202": 2983, "203": 2991, "204": 3010, "205": 3041, "206": 3058, "207": 3067}
---

**Dave Jones:** Hi, it's time for the next part in the power supply series. I've been designing this cute little power supply and I thought we'd take a look at the final schematic.

**Dave Jones:** Let's go. And if you remember the previous videos, here's the existing circuit we already had, which I breadboarded up. We pretty much developed this from scratch. Now, the the final schematic we're going to go through today is essentially exactly the same configuration as this, but I've gilded the lily again, added a few niceties and put some system engineering into it, I guess you could say, and tada, here it is.

**Dave Jones:** Here's the final schematic. Now, it might look a bit complicated. That's cuz I've put it all sort of crammed it all onto an A4 sheet here. It's not terribly modular, but stick with me.

**Dave Jones:** We'll go through it and you'll see that it's not that hard at all. It's very simple. First of all, if you take away all the other circuitry there, you'll find that this circuitry in here is pretty much identical to our existing circuit here.

**Dave Jones:** So, let's take a look at that part of it first and the current shunt that current shunt amplifier and resistor, which I've changed up here. But before we do that, let's just take a look at the thing from a block diagram level, shall we?

**Dave Jones:** This is exactly the same circuit we had before. I've added a microcontroller down here. It's an ATmega168. It could be an ATmega328 or whatever. Any of those are 28-pin ATmegas.

**Dave Jones:** It's going to be Arduino compatible because the software will be written in the Arduino software environment. I've added external ADC and external ADC here around here with some voltage followers and an external DAC as well.

**Dave Jones:** Now, you know how I did the video on the pulse width modulation output and how you can control the output voltage and current with PWM. I was originally going to do that cuz most microcontrollers are only 10-bit resolution 80Cs.

**Dave Jones:** So, I don't know. I decided to gild the lily a bit. I wanted a bit more resolution, so I'm using external 12-bit DAC and an external 12-bit ADC, which we'll go into later.

**Dave Jones:** Uh up here we've got the LCD cuz we've got to have an LCD display to display the voltage and current and all sorts of other stuff. It's a nice squared C one.

**Dave Jones:** We'll go into that. Some push button switches, rotary encoders down here, two of them, one for voltage, one for current. I decided not to use the more expensive uh 10-turn pots.

**Dave Jones:** Um up here I've added a 5-V USB um output connector on the front panel with some um iPod kind of compatible uh things in there so it can uh tell an iPod that it's a genuine charger just so that you can uh power 5-V USB devices directly.

**Dave Jones:** There's a couple of voltage regulators up here. And here I've added I've really gilded the lily here. I've added what is essentially one of my microcurrent devices into the design here.

**Dave Jones:** So, I think this is probably one of the first uh power supplies bench power supplies on the market that I'm aware of anyway that can measure down to microamp output current.

**Dave Jones:** So, I can do a massive range uh from anywhere from a couple of microamps all the way up to a couple of amps with full resolution and full accuracy.

**Dave Jones:** So, that's a little nicety I've uh gone to the trouble to add there. We'll take a look at that, but that's the basic block diagram. In the previous design, we used a a very uh crude uh differential amplifier here for the current shunt, and that's not very accurate at high resolution stuff, 10- or 12-bits, which we're trying to do here.

**Dave Jones:** It's It'd be okay for 8-bit or something like that, but so I've decided to add a uh Maxim uh uh current sense amplifier specifically current sense amplifier specifically designed for the task and it does a really nice job.

**Dave Jones:** It's only a dollar or a dollar fifty or something like that. So, it's you know, it's a reasonable price, but it's very accurate and does a really good job.

**Dave Jones:** The current shunt resistor here, I've actually made up. Um I've Well, when I've laid out my board, I've put in uh 10 half watt half watt resistor um footprints in there so that uh you can basically get better than your uh 1% uh typical tolerance because it's quite difficult to get an accurate precision current shunt resistor like half a percent or point one percent or point two or something.

**Dave Jones:** It's very difficult to actually get those. They're very difficult and expensive to source. So, I've put 10 resistors uh in parallel. So, hopefully, if you see my previous videos on the Gaussian resistor response, we should get better than the typical 1% resistors we're using the tolerance there.

**Dave Jones:** Now, because we've got an intelligent controller over here, we don't really need technically need um a high precision accurate resistors in all of this power supply design because we can all we can calibrate the thing and compensate for that in software, but I that's just not nice.

**Dave Jones:** I didn't want to have to do that. So, I've made this overall design fairly high precision. So, I've used a 0.1% um high side current sense amplifier here. I've used 0.1% resistors elsewhere in the circuit down here as we'll see.

**Dave Jones:** Um and the current sense resistor, well, we'll see what we can get when we actually build the thing up, but I'm going to try and get it as accurate as possible.

**Dave Jones:** Now, you notice on my schematics that I've added these uh notes in various uh places here and I love doing that sort of thing cuz it just uh put formulas and things like that in little uh boxes next to uh the next to the actual pin that you're actually uh talking about and it just helps explain the schematic and when you come and look at it later, all

**Dave Jones:** the formulas are there, and you don't have to do the calculations. It's all done, and little notes and things, you know, you might add a star ground over here, so you put little notes and current values and things like that.

**Dave Jones:** That's just a nice touch to add to any schematic that you're actually doing. So, we're using a maximum 4080F high-side current sense amplifier, and that's got a fixed gain of five.

**Dave Jones:** It's basically a differential amplifier, and so it measures the differential voltage across a high-side current shunt resistor we've got here, and it multiplies by five, and it gives you a direct voltage output referenced to ground, and that's all it is.

**Dave Jones:** Very simple device, and this is a quite a precise one, and it's 0.1%, so with a gain of five, we can do various calculations up here for various current shunt resistor values.

**Dave Jones:** Now, I'll just mention that I'm actually using a 2.048 voltage reference here. It happens to be an ISL2107 over, but it can be any one on the market, really.

**Dave Jones:** It's, you know, it's not too bad. It's 30 ppm plus minus 0.25 0.25%. Now, why I'm using 2.048 V instead of the more traditional 2.5 V voltage reference is because then the values that we're going to get out of our analog-to-digital converter are going to be spot on.

**Dave Jones:** We don't have to fudge them or do anything like that. Now, I'll give you an example of that. Let's say we use a 2.5 V voltage reference, okay? And we're using a 12-bit analog-to-digital converter.

**Dave Jones:** There's going to be 2 to the power of 12 or 4,096 different steps in that analog-to-digital converter. Now, if we divide our 2.5 V maximum input to our analog-to-digital converter, cuz we're using a 2.5 V voltage reference, divide that by 4,096 steps, you end up with some weird-ass value here of 610 or thereabouts microvolts per bit resolution on your analog-to-digital converter.

**Dave Jones:** And that's well, that's hopeless, you know, if you feed in 100, you know, if you're measuring 100 bits out of something that represents a voltage of, you know, 61.035 millivolts.

**Dave Jones:** It's not a nice round number. It sucks. So, uh and you have to compensate for that in software. You've got to actually do some math in software. It's not that bad, but there's a reason they make these voltage references which correspond to the like a power of two to match your analog-to-digital converter.

**Dave Jones:** In this case, 2.048 volts, but you can get 4.096 volt voltage reference. But, 2.04 volts is more common. So, we're going to use that. So, look what happens if you're using 2.048 volts, okay, on maximum ADC value and you divide that by your 4,096 bits, bingo, you've got a nice round number of 500 microvolts per bit.

**Dave Jones:** And if you have a look up here of when you translate this into your current shunt values, you end up with a very nice round 500 microamps per bit resolution.

**Dave Jones:** Or if you use different values, you can have 1 milliamp per bit resolution precisely from the output of your analog-to-digital converter. And that works out really nice in your software.

**Dave Jones:** I love it, and that's why I've used it. If we take a look at our current shunt resistor here, let's take a value of 2 ohms. If you put 10 in parallel, you're going to get 0.2 ohms current shunt resistor.

**Dave Jones:** Now, I put up here for a gain of five in this MAX4080. Remember, it's built-in gain of five. You can get different versions uh gain of 20 or I think a gain of 60, but we're going to use a gain of five and I'll tell you why in a minute.

**Dave Jones:** And uh that out for a that will give us because it's a gain of five, okay, 0.2 ohms. Let's say an amp uh through it is 0.2 volts multiplied by gain of five is 1 volt.

**Dave Jones:** So, you're going to get out of your uh current shunt your uh current sense amplifier right here, you're going to get out 1 volt per amp output. And of course, that will give you a range because you're using a reference voltage on your analog-to-digital converter, it's going to give you a range a usable measurable range of 0 to 2.048 amps.

**Dave Jones:** And that translates to 500 microamps per bit resolution. And you can go through Let's say you wanted to use a uh 3-amp version of this LT3080, the LT3083, then uh you could say set it for a 4-amp current range and you'd get what still get an excellent resolution of 1 mV per bit.

**Dave Jones:** Awesome. And because you've used 10 resistors in parallel like this, say at half of what each are, you might have a 1-W resistor in there, then you might have 5 W or 10 W dissipation capability in your current shunt resistor there, and that's plenty.

**Dave Jones:** So, this current shunt resistor isn't going to heat up at all, so you can use um you know, fairly low-grade ones and they're going to work quite well. They're not going to change much with temperature because they don't heat up much.

**Dave Jones:** Let's take the example of the 2-ohm resistor here. If we've got 2 amps flowing through it, I squared R, 2 squared is 4 and * 0.2 ohms, we're only going to dissipate 0.8 W in all of those resistors.

**Dave Jones:** And we've got if we've got 5 W total capability or 10 W, not a problem whatsoever. It's not going to heat up much at all. Now, of course, the value of your current shunt resistor is going to determine how much voltage drop you get across there, and depending on your input voltage over here, depending on what you power it from, that may be an issue.

**Dave Jones:** In this case, if we use a 0.1 ohms, then we're only Well, in either of these two cases up here, we're only talking about a 0.4 volts maximum drop, which really isn't that bad at all.

**Dave Jones:** And you don't want to make it too low and use like a gain of 20 here or a gain of 60, because then you can start getting right down into the noise, and you can get errors and issues like that.

**Dave Jones:** So, you really don't want to go there. You want to tolerate You want to get as maximum voltage drop across your current shunt resistor as you can tolerate and the lowest gain here, so you minimize your errors.

**Dave Jones:** So, how much error can you tolerate in this amplifier here? What's the minimum? Well, it depends on your specs and what you're willing to whether or not you're willing to compensate for it in software, which I don't really want to do.

**Dave Jones:** I want to try and get the maximum uh uh possible absolute accuracy out of this thing. So, the input offset error of this amplifier is going to matter. So, you can't make this resistor shunt resistor arbitrarily small, because then the voltage drop's going to be so small, it's going to be swamped by the input offset voltage of this op amp of this amplifier here.

**Dave Jones:** So, what's the minimum that we can tolerate? Well, it's a basic rule of thumb is that well, you don't want it to be any more than one bit resolution on your analog-to-digital converter.

**Dave Jones:** You want to be able to measure accurately down to your last bit. Why not? So, in this case, we've got a 500 microamps per bit. So, 500 microamps is the minimum we can measure.

**Dave Jones:** So, if we do 500 microamps here times our 0.2 ohm resistor there, we're basically going to get 100 microvolts drop across this resistor here. So, that's the minimum that we're going to get 100 uh microvolts.

**Dave Jones:** So, let's go over to our data sheet here for our MAX uh 4080 device. And what's its input offset voltage? Huh, what a coincidence. It's 100 microvolts. Typical, you could go into there.

**Dave Jones:** Uh but it's going to be 100 micro microvolts input offset voltage. So, as you can see, the MAX4080 is almost ideal for this. Its input offset voltage is exactly the same as uh our minimum voltage on our input here.

**Dave Jones:** That's pretty good. I mean, ideally, you know, if you're designing a really high precision thing, you'd want it to be uh maybe an order of magnitude lower, you know, uh order of magnitude lower or something like that.

**Dave Jones:** But in this case, perfect. Good enough. We're happy for a one-bit uh error there. And of course, the input offset voltage is just that. It's relative to the input.

**Dave Jones:** So, this amplifier has a gain. So, the actual um output uh uh the area going to get on the output is the input offset voltage times five, which is 500 microvolts um error on the output.

**Dave Jones:** But because um it scales up five, we're still only talking about one bit uh error there caused by our input offset voltage. Beautiful. And as I said, you just can't make that resistor arbitrarily low cuz not only is there input offset voltages, but then you get um uh noise and things like that causing issues.

**Dave Jones:** So, there you go. That's almost perfect, that device. And just to get rid of any noise, I've added just a little um RC low-pass filter there, which then goes down into our existing circuit, which we've seen before, our um our uh constant current um comparator down the bottom here.

**Dave Jones:** And not only that, if you look at the net name there, it also goes over to our uh analog-to-digital converter over here, one of the channels. There it is, ADC I out.

**Dave Jones:** Now, speaking of the ADC, we've used a four-channel one here, and so it's going to measure Not only does it measure the outputs current via here, it also measures the output current from this micro amp circuit over here.

**Dave Jones:** So, I can measure the current two different ways, either in series with the output like that. Well, they're both in series with the output. I'll explain this one later.

**Dave Jones:** But, it measures the output from the micro current, and it can also measure the output voltage, which we'll take a look at there, and also the ADC input, the voltage input as well, coming from your source.

**Dave Jones:** So, then your software is able to determine whether or not it's got adequate voltage and whether or not this regulator is going to actually drop out. So, our 2.048 voltage reference here goes into the DAC over here, the 12-bit DAC, and it also goes over to our 12-bit analog-to-digital converter here, and both of those are devices from Microchip.

**Dave Jones:** This is The DAC is an MCP4922, and the ADC is an MCP3204. So, why did I choose this specific analog-to-digital converter and DAC? Well, let's find out. Let's go and do a parametric search in Digi-Key here.

**Dave Jones:** Let's search for ADC, and we'll go down here to analog-to-digital converters, ADC. There we go, almost 12, 13,000 of them. Can you believe it? And here we go. Here's our parameters.

**Dave Jones:** We want a 12-bit converter only. There's no point searching for all the others, so let's drill that down. Bingo, we're still got 4,434 different converters. Well, because this is a kit, we only want through-hole, so we'll select through-hole over here, and we apply the filter, and bingo, we're down to 439 ADCs.

**Dave Jones:** So, from these particular manufacturers, Microchip, I like them, National, Texas, you know, all the biggies are there, Linear, Analog Devices. But, uh let's sort by price because, well, really, I uh I do care about uh I do care about price.

**Dave Jones:** So, let's search for that. Let's say we're going to make 100 kits. Let's sort by price based on 100. And uh bingo, what comes up first? Not terribly surprising, Microchip.

**Dave Jones:** They make pretty cheap uh analog parts. People think they People mostly know them for their uh uh PIC microcontrollers and stuff like that, but they make some uh pretty cheap analog stuff.

**Dave Jones:** I'm finding I'm using more and more of them uh lately. So, basically, uh let's have a look at the number of converters. It's only got one. Bang. Uh not too happy with that.

**Dave Jones:** We want uh Basically, we want something with at least four channels in there. So, let's select that. Hey, what's going on? No, I pretty sure there's a Microchip one in there.

**Dave Jones:** So, something's happened to that Digi-Key search. I don't know what's what's gone wrong there. Something horrible. But, uh here No, here we go. Uh look, they've Digi-Key's got it wrong.

**Dave Jones:** Here's my converter. It's a four-channel. It's only got one number of converters, one. Wow, fail. Okay, so much for that. But, there you go. The cheapest device is there.

**Dave Jones:** Um these are single-channel, dual-channel. And the cheapest uh device, four-channel ADC we can get, is a Microchip MCP3204. And bingo, that's the one I used purely because it was the cheapest in quantity.

**Dave Jones:** It's $2.40 in 100 of quantity, which is, you know, expensive, but it is a 12-bit uh converter. The next uh nearest brand is um Analog Device Sorry, Texas Instruments ADS7822.

**Dave Jones:** Um but, that that won't be a four-channel in an eight-pin package. So, really, you know, there's no competition. The prices start going up and up and up. So, that's why I chose the Microchip, and I did exactly the same thing for the DAC, and the matching Microchip DAC, unsurprisingly, I guess, came up as the cheapest again.

**Dave Jones:** So, that's why I used them. That's parametric search. And if you're wondering why I just didn't use a microcontroller with a 12-bit analog-to-digital converter and PWM in it, well, let's take a look.

**Dave Jones:** I've gone through and selected all the DIP devices here. You can't select through holes, so I've just one DIP microcontrollers. I'm searching through the 32,000 microcontrollers available from Digi-Key, any brand, any manufacturer.

**Dave Jones:** So, let's take a look over here, ADC at 12 bits. 12 bits, 12 bits. It's It's a bit tedious. You have to go through and select your 12-bit ones in here.

**Dave Jones:** But, if we do that, and then if we go through and select just the ones in here with 12-bit ADCs, let's not worry about the PWM at the moment, cuz that's harder to find, but let's just, as a first pass, find ones with 12-bit analog-to-digital converters.

**Dave Jones:** What have we got? We've got Freescale, and we've got Microchip. That's it. So, all you Atmel fanboys out there, don't come running why I didn't use some Atmel thing, or some or if you're a TI fanboy, why I didn't use those?

**Dave Jones:** Because they're not available with a 12-bit ADC in a DIP package. So, there you go. And if we go along here, and we probably search for, say, the uh best price over here, let's 100 of quantity.

**Dave Jones:** Let's have a look. It happens to be the Freescale, the HCS08. Time That's a going to be a tiny a tiny little device. That's only a 16-pin DIP. Not enough pins, 28-pin DIP.

**Dave Jones:** Um may or may not be enough. You know, it's just I don't know. And then you get into the PIC devices here, and there are quite a few PIC devices available with 12-bit analog-to-digital converters.

**Dave Jones:** But if you want one with a decent number of pins, and then you'd have to go through and look at the ones that actually have a 12-bit capable pulse-width modulation output, it just gets trickier and trickier.

**Dave Jones:** And well, it was just all too hard. So, I just decided, simply decided to use an external ADC and DAC. And generally, anyway, you're going to get better performance with an external ADC and DAC.

**Dave Jones:** The ones built into microcontrollers, they're great. So, when you start trying to push 12 bits inside a microcontroller, you know, you're probably better off going to external. 10, that's why most of them only have 10 bits cuz that's generally all they're good up to.

**Dave Jones:** Now, you see that I've got a couple of voltage buffers down here driving the ADC like this. Now, there's a reason I've actually got that is because when you got a successive-approximation ADC like this, you can't have an arbitrarily high input impedance.

**Dave Jones:** So, in this case, ADC V out is coming from over here. Look at these 10k resistors, okay? We've got a relatively high input impedance driving this um analog-to-digital converter.

**Dave Jones:** And this has sample and holds in here, and it can cause you all sorts of problems. So, it's good practice to actually buffer that so it provides a low-impedance drive to your analog-to-digital converter.

**Dave Jones:** These ones here don't need it because it's coming directly from the output of the op amp here through three a little low-pass filter of 330 ohms here. Not a problem, that's low enough not to cause an issue.

**Dave Jones:** And the other comes from the ADC I out, which is the current we looked at before. And once again, it's 330 ohms, low enough not to cause an issue.

**Dave Jones:** And as always, read the data sheet. Here's the ADC, the MCP3204, which is the four-channel version. Also available in eight-channel version. It actually warns you about high input impedances.

**Dave Jones:** And here's the equivalent circuit of the analog-to-digital converter. And as you can see, it's got an inbuilt sampling switch here with an internal series resistance of 1K. And then it's got a 20 pF sampling capacitor on here.

**Dave Jones:** And basically, your input impedance, which I just talked about over here, here's your input pin. So, this is all inside of the all inside of the analog-to-digital converter chip.

**Dave Jones:** So, your external impedance here will actually affect the time that this capacitor takes to charge up. So, that's charge up to the value. And if you've got a 12-bit converter, it's got to get very close to the nominal value not to introduce any additional errors into your analog-to-digital converter.

**Dave Jones:** And if you take a look down here, they actually provide you a graph here. So, that actually shows you the input resistance in ohms, 10K here, 1K here, down to 100 ohms down here.

**Dave Jones:** And the maximum clock rate in megahertz at different voltages. And as you can see, if you're operating in a low voltage, we're operating at 3.3 volts. So, it's going to be like in there somewhere.

**Dave Jones:** It's going to be another curve which goes in there and down like that. As you can see, if you've got a 10K input impedance, it's useless to you can't get a 0.1% least significant bit deviation on this thing.

**Dave Jones:** So, the input impedance matters. In practice, we may not um, need these op amps down here. And if we don't need them, well, we can just not insert it and then just short out pins two and three and five and six there.

**Dave Jones:** Not a problem. But good practice to put it in if you need it based on your input resistance cuz that can affect your maximum sampling rate. And by the way, it's not just specific to this analog-to-digital converter, either.

**Dave Jones:** If you use the one inside your microcontroller, you would have the same issue. Just be aware. Now, I've actually used a really cheap garden variety, uh, op amp here.

**Dave Jones:** It's an NMJ, uh, 14558. It's a variation on the, um, very common 4558 op amp. And this one has, um, five a nominal, uh, value, not a maximum value, but nominal of 500, uh, 500 microvolts, um, input offset voltage.

**Dave Jones:** So, that should be good enough for our circuit, but as always, it's a standard pinout. If we need to put, uh, really, um, better precision op amps in there, we just drop them in.

**Dave Jones:** And as for our 12-bit DAC over here, well, it's pretty darn boring. There's some digital input lines here. It's an SPI, so we've got a clock, a chip select, and, uh, data input, a voltage reference input, bypass cap, and it just outputs two different voltages.

**Dave Jones:** It's a dual channel 12-bit DAC, this one. It's quite nice. Uh, well, for the price, it's really cheap. And, uh, and so, that just generates our voltage Vset and Iset exactly as we would if we hooked a pot onto here like we've seen in the previous videos.

**Dave Jones:** Or we use a pulse width modulation output from our digital, uh, or from our microcontroller here. We could also drive it. Um, but a nice, good 12-bit resolution DAC, that gives us some great resolution on the output.

**Dave Jones:** And as for our current resolution, well, we've already looked at that. We can actually set, um, the current limit in steps of 500 microamps. Brilliant. Over the whole range of 500 microamps to 2 amps.

**Dave Jones:** Fantastic. That's the advantage you get with the 12-bit analog 12-bit DAC. If we used a 10-bit DAC, you'd be looking at 2 milliamps per bit. Not as good, but still, you know, might be certainly adequate.

**Dave Jones:** So, I've just gilded the lily here. You could have just used the microcontroller for sure. Depends on your requirements. Now, as for our voltage output, well, our DAC is going to give out 0 to 2.048 V cuz that's our voltage reference coming in here.

**Dave Jones:** So, 0 to 2.048 V. I've put in a gain of five here in this amplifier set by these two resistors here. Exactly the same circuit you've seen before. The tap actually comes from here, so it compensates for these series resistances here.

**Dave Jones:** But, that circuit has a gain of five. So, once again, I've put an engineering note in there, and there it is. Gain equals five, 0 to 2.048 V input, which gives a 0 to 10.24 V output with 2.5 mV resolution for our 12-bit analog-to-digital converter.

**Dave Jones:** So, we can set our output our voltage output up here on the supply in steps of 2.5 mV. Awesome. And of course, if you used a 10-bit DAC or a 10-bit PWM in your microcontroller, you would get a 10-mV resolution output.

**Dave Jones:** Once again, that's still adequate for most purposes. I'm just gilding the lily. Some of you might be asking, "Why have I put two resistors in parallel here and two resistors in series?" Well, if you'll note, they're both they're all 10 K.

**Dave Jones:** I've tried to basically optimize my design to reuse existing values on my sheets here. So, I've got you know, 10 K up there, 0.1% cuz these resistors are fairly, you know, fairly expensive cuz they're 0.1% tolerance.

**Dave Jones:** So, I've just used them. It's better I think it's better to use them and reduce more of them and reduce your bill of materials than it is to have all these different values.

**Dave Jones:** And over here, which we'll look at later, I've also used 10K there as well and 10K here. So, I bought, you know, you can buy a whole bunch of those, so you can consolidate your bill of materials and you only have to buy the one item.

**Dave Jones:** That's not bad. So, I've done that up here, like for this last time you'll notice that I set my current um fixed current output here, the LM 334, to 1 mA, but that required an oddball value resistor here I'm not using elsewhere on my circuit.

**Dave Jones:** So, I decided to use a 100 ohm I am using elsewhere in the circuit, and it's still good enough, 677 microamps, good enough for a minimum load on our LT3080.

**Dave Jones:** Component consolidation is one of those steps you should do in any good design. So, you'll see not only the resistors I've done that, but also elsewhere on the circuit I've done that for the capacitors as well.

**Dave Jones:** If I needed 4.7 microfarads, and I don't use it anywhere else, well, but I've used 10 microfarads somewhere else, well, I'm going to use a 10 microfarad in there instead of the 4.7.

**Dave Jones:** And for output protection, I've got a big nice 5 amp reverse Schottky diode there. Now, this is the output I'm going to have a load switch external to the board, it's not actually mounted on the board, and that's why it's not shown here.

**Dave Jones:** And you'll note that I'm this is my sense line that senses the output voltage goes back to the analog-to-digital converter down here. This net here goes down to the ADC.

**Dave Jones:** Now, the reason I'm doing that is because some people like to have the sense line directly on the output, so that it still reads the voltage when the switch the load switch is open.

**Dave Jones:** Others prefer it the other way around. They'd like to know what the output voltage is going to be before they or or what the output voltage actually is regardless of the load switch position.

**Dave Jones:** So, um this just having a separate sense line gives people the flexibility to wire it up anyway they like. And once again, I've just got some voltage divider resistors here, and that will give me a certain voltage into my analog-to-digital converter scaled down to meet my 2.04 V voltage reference.

**Dave Jones:** And more than that, it is precisely the voltage here is precisely 1/5 of the output voltage. And coincidentally, remember I had a * 5 gain over here. So, once again, my that scales perfectly.

**Dave Jones:** My If my max output voltage is 10.24 V / 5, the max input to my ADC is going to be 2.048 V or that the output voltage divided by 5.

**Dave Jones:** So, it's perfect. I'm using the full maximum range of my analog-to-digital converter to measure my output. And that's what you want. You don't want to piss away any bits.

**Dave Jones:** Now, as for the current limit LED indicator over here, you know how I used this convoluted op amp before. I just wanted to show you that you could actually do that as a spare op amp, but that's not the nicest way.

**Dave Jones:** It's better to actually use a second transistor here and drive it direct. And that's exactly what I've done on the circuit here. Here's my current my current limit comparator down here.

**Dave Jones:** And as well as driving the as well as driving the set pin as per normal, it also drives a separate second transistor here because we're already used them. Same type, very cheap, you already got them.

**Dave Jones:** And that current limit goes into your microcontroller over here. It doesn't go directly to a LED. I decided to put input pin, and then you can the software can do intelligent stuff with the LED.

**Dave Jones:** It can blink it and do all sorts of things depending on various modes. So, there you go. And you don't need a pull-up resistor on there because you can program a pull-up resistor directly on your microcontroller here.

**Dave Jones:** And you'll notice the same with the optical rotary encoders. They got two outputs here. They go directly into the microcontroller. Normally, they need pull-up resistors on there, but do it inside the micro.

**Dave Jones:** No problems. Save a couple of resistors, save some board space. Now, let's take a look at this effectively a microcurrent circuit here, which allows us to measure if your if this lab power supply is powering your little microcontroller circuit and goes into sleep mode, well, you don't have to use your multimeter.

**Dave Jones:** This sucker, this power supply will be able to actually measure low values. Not as good as the microcurrent. It only goes down to a maximum of 2.5 microamps per bit, as we'll go into, but still, I don't know any other power supply that can measure the output current down to 2.5 microamps.

**Dave Jones:** And the way it does that is it basically this circuit doesn't operate all the time. This circuit will only effectively be in use when you want to measure and you want to measure low values and your microcontroller knows that the values are very low, it can switch this circuit in.

**Dave Jones:** And it does that with this MOSFET here. I can switch on this and effectively insert another load because our output voltage is here's our output voltage here, but the ground, here's our output, our negative output terminal.

**Dave Jones:** Instead of going directly to ground, it goes through a current shunt resistor here, a what's called a low-side as opposed to the high-side current shunt resistor we have up here.

**Dave Jones:** We have an additional low-side one. And normally, I don't like doing that because then it introduces an offset voltage error here from ground and depending upon your output current.

**Dave Jones:** That's why at very high output currents, we don't want to go through this resistor here. We want to shunt that Excuse the pun. We want to shunt that through a much lower value MOSFET here so we don't get any errors introduced on our low side.

**Dave Jones:** It's going to be effectively ground. So, let's say we want to only tolerate one bit resolution error on this output. What value do we need? Well, our output voltage is maximum output voltage is 10.25 V, 2.4 V, sorry, divided by 4096.

**Dave Jones:** We've got a 12-bit converter. So, 2.5 mV. So, basically, our ADC down here can measure our output voltage to 2.5 mV resolution. So, it'd be nice if this circuit here only dropped 2.5 mV or one bit or less.

**Dave Jones:** So, pretty much, we want 2.5 mV maximum drop across this MOSFET here when it's switched on and all this circuit is disconnected on our high current range. Our maximum resistance there is going to be 2.5 mV divided by the 2 A maximum current there, 1.25 mΩ.

**Dave Jones:** So, our FET there needs one bit error is going to need 1.25 mΩ. So, that's actually a very low value for a MOSFET. If you actually want to meet that, you need a really, really beefy MOSFET.

**Dave Jones:** I've decided to use one of these. It's cheap, readily available, in a nice package. I like it. And it's going to be near enough. It's got a rated maximum RDS on or a maximum maximum resistance of 8.4 mΩ, but that's going to be at the maximum current.

**Dave Jones:** It's going to be better than that at the lower current and at higher VGSs as well or higher gate source voltages. So, in any case, that MOSFET should give us a a very insignificant error at our maximum range of 2 amps.

**Dave Jones:** So, as I said, the software is capable of switching this MOSFET on and to do that, I've actually to get a higher um gate source voltage, I've actually used, rather than drive it directly from the microcontroller, which would only be a 0 to 3.3 V output, that's not really good enough for this MOSFET.

**Dave Jones:** I really want it a nice high value. So, I'm going to tie it to V+ here and I'm going to use an external transistor to turn it off and on.

**Dave Jones:** So, the gate voltage is going to go between 0 and V+, which is our input all the way over here. So, we're getting a nice high gate source voltage because the higher the gate source voltage, the lower the turn-on resistance for this MOSFET.

**Dave Jones:** So, you want it as low as possible. And during that 2 amp range, this circuit isn't used at all. It's still measuring. It's trying to measure something, but we don't read it at all.

**Dave Jones:** The micro doesn't read it. We're doing our measurement based on this high side uh current shunt resistor. So, we've effectively got two different current measurement ranges. So, let's have a look at the low value current measurement when this circuit is active.

**Dave Jones:** Now, what we've got here is we've got four resistors here, 1 ohm, and they're in series parallel combination giving a total shunt resistor here, low side shunt resistor value of 1 ohm.

**Dave Jones:** Now, the reason I'm using four like that is, well, not only to get a little bit extra accuracy like we did with the high side current shunt resistor, but a bit of margin for error in case this software selects the wrong range when it's when there's actually a high output current.

**Dave Jones:** So, in this case, let's say it was 2 amps maximum like that. Then, in theory, if the software accidentally turned this transistor off instead of on, then all that current would try and flow through the would flow through these resistors here and we would get a power dissipation in those resistors of 4 watts.

**Dave Jones:** So, really, you know, if you put a tiny little resistor single resistor in there, you might burn it out accidentally. You don't want that to happen. So, a couple of extra resistors it's, you know, it's going to survive anyway.

**Dave Jones:** It's still not going to be great. It's going to be very, very hot, but at least survive and it won't blow those resistors. So, if we've got a 1 amp current shunt resistor here and 1 milliamp flows through there, we're going to have 1 millivolt across here.

**Dave Jones:** This op amp, the MAX4238 you've seen in my micro current, it's exactly the same. It's got a gain set by these two resistors here of 200. It's quite a high gain.

**Dave Jones:** And so, if we've got 1 millivolt drop across the shunt resistor, we'll get 0.2 volts output. So, my little engineering note here says it again, the 200 the Vout equals 0.2 volts per milliamp flowing through here.

**Dave Jones:** And that can from that we can determine our maximum range cuz our ADC down here, remember it's only 2.048 volts maximum. So, we can only tolerate that voltage or it can only read that voltage maximum.

**Dave Jones:** So, we can have 10 times that or roughly 10 milliamps or if you want to round it off, 10.24 milliamps maximum is what this circuit is capable of measuring.

**Dave Jones:** So, the microcontroller, when it when it measures over here on this shunt resistor that the current drops below 10 milliamps or you can do it under manual control with one of the switches here.

**Dave Jones:** It can automatically, if it wants, switch on, disconnect this MOSFET, and then start reading from this circuit over here. So, if you're Let's say your circuit's powering your microcontroller, but this power supply is powering your microcontroller circuit that's just gone into sleep mode, the software of this power supply can detect that, and it can switch on this circuit and measure that sleep current accurately.

**Dave Jones:** I think that's brilliant. Why can't all power supplies have a feature like that? So, just like the high-side current sense amplifier, what is the maximum input offset voltage we can tolerate here before we start getting errors?

**Dave Jones:** Well, if our maximum output is 2.048 V, okay, we divide that by our 4,096, we're getting 500 µV is our minimum on the output here. So, we're going to read a 500 µV per bit, one bit resolution here, but we've got a gain of 200.

**Dave Jones:** So, let's divide that by 200, okay? And it can tolerate and that translates to 2.5 µV is our minimum per bit value across here. And of course, the only way that you're going to get an input offset a voltage error pretty much of two point down in the order of 2.5 µV, as you've seen in my microcurrent, is to use a is to use a chopper amplifier and

**Dave Jones:** auto-zeroing amplifier, which is exactly what the MAX4238 is. And what is its value? An ultra-low 0.1 V µV offset voltage. More than an order of magnitude more than what we need, but that's typical.

**Dave Jones:** But its maximum at ambient temperature, or even over the full temperature range, is about 2.5 µV. So, over the full temperature range, we're only going to get one bit error.

**Dave Jones:** Fantastic. More than what we need. A little bit overkill, but hell, I already used that in the micro current, so we're going to use it here again. Now, because I wanted to make this design into a kit, I wanted all the components to be through hole, and I tried as hard as I could to make everything through hole, but unfortunately, the MAX 4238 is only in an SO8 package, and likewise,

**Dave Jones:** the MAX 480 is only in an SO8 package, and the voltage reference, although I can get ones in like a TO92 package, they're cheaper and more readily available, especially in the 2.848 V version, in a SO23.

**Dave Jones:** So, they're the only three surface mount parts on the entire design. Everything else is through hole, and I pretty much optimized I chose parts based on through hole availability.

**Dave Jones:** There were maybe one or two others on the market for the current sense amp, but they weren't quite right and didn't have the right gain, and it didn't work out the values, and it just wasn't nice.

**Dave Jones:** I was pretty much forced to use an SO8 there, and pretty much an SO8 over here, and because I've used the chip before, ah well, you can't have everything.

**Dave Jones:** You have to if you go on build this thing up, you're going to have to solder a couple of SO8 packages. Sorry. And I've got a little MAXIM MCP1700 3.3 V voltage regulator.

**Dave Jones:** They're they're quite nice devices. They're actually got very high very close output tolerance of a percent or less, or half a percent. They're really really quite nice neat. You can actually use those almost as a voltage reference at an ambient temperature.

**Dave Jones:** I think I've mentioned that before, but anyway, I've got a standard LM7805 to give our 5 V out from our US for our USB output connector over here. And because I've This is the heat sink.

**Dave Jones:** I'm actually using it's from Altronics here in Australia. I don't think you can buy it anywhere else. I think it is specific to them. It's a PCB mount one.

**Dave Jones:** It's got PCB pins. It's upside down there cuz it was in my breadboard before, but it's got an extra hole here so I can mount both devices on the same heat sink.

**Dave Jones:** But, uh-huh, just be careful. You don't want to put them directly on there like that because then you'll short out the tabs which are connected through to the center pin and in this case it'll be ground and output which you'd be shorting.

**Dave Jones:** So, if you put this um uh, package here on if you put both these packages on the same heat sink, you'd actually be shorting the output of your LT3080.

**Dave Jones:** So, oops, you don't want that. Make sure you put some mica washers or some seal pad in there to isolate them from the heat sink. Now, as you'll see down here with the micro, I've actually used every available pin, every single one of them.

**Dave Jones:** And I probably goofed up here. I think I'm actually going to change it because I thought I could get away with using the 8 MHz internal oscillator in here and it'd be good enough to do my external serial RS232 comms, but to do RS232 as a rule of thumb you need a 1% tolerance frequency error or better and the oscillator in this thing can be trimmed to 1% or better in that

**Dave Jones:** software. You can actually software trim it, but it's not as good as the PIC one. I've done this on the PIC before and they come factory trimmed to 1% or better.

**Dave Jones:** So, out of the factory over temperature you can actually fairly reliably do RS232, but I don't think that's the case for the Atmel. So, probably going to have to use I'm going to have to free up these two pins down the bottom and put a oscillator on there, the external 8 MHz oscillator on there or 16 or whatever you want to use, which is Arduino compatible.

**Dave Jones:** You can use either and change it, but I'll probably use a ceramic resonator. They're at 8 MHz. So, I've got to free up two extra lines here so I can get that precision RS-232 serial comms out of here, I think.

**Dave Jones:** It's just You know, it's good practice. One of those ceramic resonators, you'll get, you know, easily get to half a percent tolerance on those, so more than good enough for RS-232.

**Dave Jones:** Now, the reason I've added a separate serial port here, it'll be a separate board, because really I want it to be able to do a whole bunch of things, be it just a standard, you know, 9-pin RS-232, you know, have an RS-232 chip or a 9-pin serial interface, or you can have electrically isolated.

**Dave Jones:** Because of a power supply, you can get major problems if you if you your connectors on the back are referenced to the computer, which is referenced to mains earth.

**Dave Jones:** That can be a big problem. So, electrical isolation can be a big issue. So, you can build a separate board with a USB to an isolated USB interface to RS-232 if you wanted to, or you could use one of those XBee wireless boards or something like that.

**Dave Jones:** So, this could be a wireless controlled power supply. That'd be awesome. There's no reason why you can't do that at all. That'd be fantastic. So, to free up these pins, basically, my DAC up here and my ADC over here, they're both SPI input devices, and because I had enough pins available, I just drove them separately.

**Dave Jones:** But, what I'm going to have to do is actually combine the clock pin on both. So, instead of having a separate clock pin coming from the micro, I'll have the same clock pin and I'll have the same data input pin as well.

**Dave Jones:** They can be shared and I'll just have a separate chip select pin for each separate chip select for each for the ADC and DAC. And that should do it.

**Dave Jones:** Bingo, I free up two pins so I can put the ceramic resonator and we're all sweet for our RS232 and Arduino compatibility. And I've got the external AVR ISP interface here so you can program the chip in circuit and download your hex code to it.

**Dave Jones:** No problems. For the LCD display up here, I've chosen a Newhaven display. I rather like them and they're one of the LCD manufacturers that I like. Their displays are quite neat.

**Dave Jones:** And what it is is it's an I squared C interface. There it is, SCL and SDA. That requires less pins on your microcontroller so I freed up pins here rather than using the standard parallel or full bit interface one.

**Dave Jones:** I can get away with just well, three lines actually. There's an LCD reset line as well but that wasn't the only reason. Here it is. It just so happened that this LCD fits nicely into the case that I'm using.

**Dave Jones:** It was exactly the right dimensions and it's a 20 character by two line because I figured 16 by two probably wouldn't give be able to give the status displays that I actually wanted.

**Dave Jones:** So it's a 20 by two line display, I squared C compatible input. It's only about eight or 10 bucks or something. It is the most expensive component in the whole in this entire power supply project but you've got to have a decent display.

**Dave Jones:** This is actually an RGB backlight one. I didn't want that but that's the only one that they had in stock for a couple of months. So I'm I'm using the backlight.

**Dave Jones:** It'll just be standard, but there you go. I pretty much a lot of my design design decisions for this entire project were actually built around the case the actual case I'm going to build this in and another aspect I haven't talked about the project which you'll find about out about in another video.

**Dave Jones:** And so I'll talk about that next time I think how to actually how I engineered this thing to fit into this case cuz that's really a very important decision and that drove a lot of the design requirements in terms of how many switches I use to fit on my front panel whether or not I had room for a USB output connector, you know, the type of heatsink I used the maximum

**Dave Jones:** power dissipation all sorts of stuff the room I had for the LCD for the controls how big I could make those the knobs how big they could be whether or not I could use 10 turn pots and everything just sort of you know pretty much revolved around the case I'm using.

**Dave Jones:** So this video's been long enough. I'll have to make that a separate video and I've already designed the PCB for this thing. I've got some time lapse video of me doing that.

**Dave Jones:** So there'll be a couple of more videos coming up. In fact, probably more than two or three coming up to finish off this power supply project. So thanks. See you next time.
