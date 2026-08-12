---
video_id: -V_p1GBH4pk
title: EEVblog #139 - Let's Select a DC-DC Boost Converter
url: https://www.youtube.com/watch?v=-V_p1GBH4pk
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 29, "3": 36, "4": 57, "5": 71, "6": 83, "7": 110, "8": 123, "9": 138, "10": 150, "11": 170, "12": 182, "13": 190, "14": 206, "15": 224, "16": 246, "17": 259, "18": 270, "19": 290, "20": 309, "21": 320, "22": 331, "23": 340, "24": 358, "25": 372, "26": 386, "27": 397, "28": 409, "29": 420, "30": 437, "31": 449, "32": 458, "33": 473, "34": 493, "35": 504, "36": 517, "37": 534, "38": 545, "39": 558, "40": 578, "41": 588, "42": 600, "43": 613, "44": 632, "45": 641, "46": 654, "47": 669, "48": 683, "49": 695, "50": 708, "51": 727, "52": 755, "53": 768, "54": 778, "55": 790, "56": 814, "57": 825, "58": 837, "59": 847, "60": 857, "61": 872, "62": 882, "63": 896, "64": 910, "65": 932, "66": 946, "67": 958, "68": 970, "69": 980, "70": 996, "71": 1009, "72": 1025, "73": 1037, "74": 1049, "75": 1063, "76": 1077, "77": 1095, "78": 1114, "79": 1134, "80": 1152, "81": 1163, "82": 1174, "83": 1196, "84": 1216, "85": 1234, "86": 1243, "87": 1263, "88": 1275, "89": 1284, "90": 1306, "91": 1324, "92": 1340, "93": 1364, "94": 1374, "95": 1404, "96": 1421, "97": 1431, "98": 1445, "99": 1454, "100": 1473, "101": 1492, "102": 1506, "103": 1516, "104": 1531, "105": 1550, "106": 1562, "107": 1573, "108": 1603, "109": 1623, "110": 1637, "111": 1651, "112": 1662, "113": 1680, "114": 1697, "115": 1712, "116": 1725, "117": 1737, "118": 1758, "119": 1774, "120": 1800, "121": 1812, "122": 1829, "123": 1840, "124": 1861, "125": 1875, "126": 1890, "127": 1900, "128": 1914, "129": 1942, "130": 1955, "131": 1966, "132": 1995, "133": 2018, "134": 2035, "135": 2044, "136": 2066, "137": 2080, "138": 2098, "139": 2113, "140": 2126, "141": 2137, "142": 2150, "143": 2162, "144": 2177, "145": 2188, "146": 2198, "147": 2205, "148": 2226, "149": 2237, "150": 2260, "151": 2271, "152": 2282, "153": 2302, "154": 2322, "155": 2339, "156": 2350, "157": 2363, "158": 2381, "159": 2394, "160": 2412, "161": 2427, "162": 2445, "163": 2470, "164": 2488, "165": 2503, "166": 2516, "167": 2526, "168": 2542, "169": 2552, "170": 2569, "171": 2580, "172": 2594, "173": 2611, "174": 2630, "175": 2647, "176": 2664, "177": 2673, "178": 2682, "179": 2702, "180": 2717, "181": 2738, "182": 2750, "183": 2763, "184": 2776, "185": 2791, "186": 2807, "187": 2826, "188": 2840, "189": 2854, "190": 2870, "191": 2879, "192": 2891, "193": 2907, "194": 2914, "195": 2928, "196": 2945, "197": 2954, "198": 2974, "199": 2993, "200": 3006, "201": 3022, "202": 3032, "203": 3055, "204": 3062, "205": 3074, "206": 3094, "207": 3104, "208": 3124, "209": 3135, "210": 3157, "211": 3171, "212": 3182, "213": 3197, "214": 3217, "215": 3230, "216": 3241, "217": 3253, "218": 3266, "219": 3285, "220": 3304, "221": 3316, "222": 3330, "223": 3346, "224": 3361, "225": 3376, "226": 3392, "227": 3409, "228": 3425, "229": 3441, "230": 3453, "231": 3476, "232": 3493, "233": 3507, "234": 3518, "235": 3532, "236": 3544, "237": 3554, "238": 3564, "239": 3578, "240": 3600, "241": 3612, "242": 3628, "243": 3651, "244": 3660, "245": 3673, "246": 3699, "247": 3710, "248": 3725, "249": 3743, "250": 3753, "251": 3769, "252": 3782, "253": 3794, "254": 3808, "255": 3826, "256": 3838, "257": 3859, "258": 3875, "259": 3891, "260": 3901, "261": 3913, "262": 3928, "263": 3940, "264": 3952, "265": 3960, "266": 3976, "267": 3988, "268": 3999, "269": 4024, "270": 4036}
---

**Dave Jones:** Hi, welcome to the AAV blog and electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, someone mentioned a while back that I should do a blog on choosing a part or how I go about choosing a part for a typical circuit.

**Dave Jones:** Now, I've touched on this before with the design merry-go-round using Digikey and everything else and parametric search engines to find suitable parts, but can I do one in detail?

**Dave Jones:** Well, that sounds like a good idea and it just so happens that I'm working on a small little project at the moment where I think this might be an ideal example.

**Dave Jones:** So, let's see if we can do go through the process of choosing selecting a suitable part for a single cell DC to DC boost converter. The first thing you do is take a look at your basic requirements and in this case it doesn't matter what the product is.

**Dave Jones:** Let's just say I want to uh power my circuit from a single cell, a single alkaline AA, AAA cell, 1.5 V cell that you're familiar with. So, I need a boost converter and in this case I want to convert it to 5 V at a maximum of half an amp.

**Dave Jones:** So, that is 2.5 W of output power. It doesn't sound like much, V * I, okay? 2 and 1/2 W doesn't sound like much, but to get it from a single cell might be a bit tricky.

**Dave Jones:** Now, I've seen this circuit before. It's a basic uh boost converter circuit that I went through in the DC to DC converter tutorial. So, I won't go through it again, but the basic concept is that it has a FET here which stores energy in the inductor and then the inductor dumps the energy into the output capacitor and that forms a basic boost converter and this FET here is actually a uh chip.

**Dave Jones:** It's like a single chip solution and that's what we're going to look for today. We're going to try and select see if we can find out of all the millions of chips out there a chip that just does this job here for a boost converter.

**Dave Jones:** Now, because it's a single-cell, okay, the input voltage is going to vary from 0.8 volts to 1.5 volts. Why does it do that? Well, if you look at the characteristic discharge curve of a typical alkaline cell, it looks something like this.

**Dave Jones:** This is voltage of the cell versus time or or actual discharge time in minutes or hours or days or something like that depending on the current. And I'll I'll have to do a separate blog on this and I will.

**Dave Jones:** But basically, the input voltage starts out at 1.5 volts and then it it diminishes and it kind once it after it this little drop at the start, it's kind of sort of linear probably down to round about a volt and that's where most of the energy in the battery under that curve is used.

**Dave Jones:** But you might want to go down to say 0.8 volts which is deemed to be the typical cutoff point for a an a typical alkaline cell and that's where most of the energy is used.

**Dave Jones:** So, if you want to get an extra 10 or 20% energy out of it or something like that, you can see after about 0.8 volts it just drops off completely.

**Dave Jones:** So, I did so your ideal chip for a single-cell DC-to-DC boost converter is to have an input range from 0.8 volts to 1.5 volts. And in this case, we need 2.5 watts of output power.

**Dave Jones:** Now, as you'll see when we go through selecting a device in much more detail, let's do a basic calculation of how much switching current we need because these DC-to-DC boost converters are typically rated by their switch peak switch current capability.

**Dave Jones:** Now, 0.5 amps on the output, okay, 5 volts at 0.5 amps doesn't mean that our chip needs to be capable of 0.5 amps switching current. No, because this is a boost converter, the input current, which goes through here and down through the switch, is much, much higher than that 0.5 amps.

**Dave Jones:** And that is going to have a direct relationship to the input voltage. Because we've got a very low input voltage here of 0.8 volts, and we want 5-V out, out, that's quite a step up.

**Dave Jones:** So, therefore, this input or switching current down here is going to be much greater than our output current of 0.5 amps. So, it's going to be roughly, here it is, I switch, okay?

**Dave Jones:** I S W is approximately equal, I won't go into further details, but this is a rough rule of thumb you can use. V out on V in, 5-V on take our minimum 0.8 volts, times our output current of half an amp, is going to be approximately 3.1 amps or higher, possibly.

**Dave Jones:** Or maybe if we want only a 1-V cutoff down here, then we could be looking at you put 1-V into here, and you're looking at 2.5 amps. So, we're looking at probably 2.5 amps switching current capability in our DC-to-DC converter.

**Dave Jones:** Remember that for later. Now, if you look at the converters out there, there's probably thousands of different types of DC-to-DC converters. A lot of them operate at low voltage.

**Dave Jones:** So, we should have no real problem finding a converter, right? And what are the other requirements? You've got to think about those as well. And it just so happens, I have a quick list here.

**Dave Jones:** This is just a basic list. It's not complete by any means, but these are some of the things you might want to think about if you're choosing a DC-to-DC converter like this.

**Dave Jones:** First of all, number one, by far, is the efficiency versus the load current graph, which we'll go into great detail on. And you've got to be careful that's at 5 V cuz they'll have different curves for this in the data sheet for different output voltages.

**Dave Jones:** Trap for young players, big one. The minimum input voltage, of course, very important, tick. We need that cuz we need to go down to at least a volt. Maybe get away with 1.1 V minimum input voltage, I don't know, but that's very important.

**Dave Jones:** So, we have to care about that one. It's going to be one of our top requirements. The minimum startup voltage because while the chip might go down to say 0.8 V, might operate down to that, it might not start up at that.

**Dave Jones:** So, if your battery is very low and and you try to start up your circuit, boom, it may not do it. And that will change with the load as well.

**Dave Jones:** So, that might be important. In this case, for my particular project, not that important cuz I expect to start up the battery at 1.5 V and then just continuously drain it all the way down.

**Dave Jones:** But, for your particular requirements, it may be a big deal. Cost availability, always an issue. Can you get the damn thing? Is it a 40-week lead time? Is it 20 bucks a chip or is it $2 or 20 cents a chip?

**Dave Jones:** It matters. Um the component count because these DC to DC converters, some will have a built-in switch, a built-in FET switch. Some will have a built-in diode, and that minimizes the number of external components you've got to have.

**Dave Jones:** So, that might come into account here. Um what's the shutdown current? Because it's battery operated, do you want to just be able to switch this thing off and then the battery can last for a year or 5 years in standby?

**Dave Jones:** So, that might be important as well. Uh what's the footprint size? Is it a big monster footprint? Is it hard to solder? Do you need a hand solder it?

**Dave Jones:** Uh what frequency does it And what frequency do does it operate and that goes into the size of the inductor you need. No point having a little tiny little DC to DC converter chip if you need a massive big huge whopping and expensive inductor.

**Dave Jones:** So, frequency and and overall footprint size, not just the chip. Um, does it have a power good output? I don't know, that might be important. Um, do you want to know if your DC to DC converter is powered up properly or not and and actually regulating the output voltage?

**Dave Jones:** The noise, the switching noise, is that important? For my application, no, not really. Uh, the reference voltage stability over temperature. Is that a problem? My one, I don't really care that much.

**Dave Jones:** It's not that critical, but for your application, it might. Uh, transient response, do you have big loads going boom boom boom, you know, in and out? That could be important and that's not the end of the list.

**Dave Jones:** So, there you go, there's a lot to think about. That's just one component in our entire design just for the power supply. It's unbelievable. And you have to go through through similar things in your design cycle for other um for all the well, a lot of the other components in your design as well.

**Dave Jones:** It's crazy. Okay, here we go. Now, how do we find a part like this DC to DC converter? Well, I've mentioned this before, it's to use what's called a parametric search.

**Dave Jones:** Now, uh, most of the manufacturers websites will have parametric search, but because we don't know which manufacturer we want to use at the moment, we're going to use one of the component suppliers like Digi-Key here.

**Dave Jones:** So, I've opened up the Digi-Key website and we're going to search for our DC to DC converter. Now, let's try it. DC Yep. Let's try it. DC converter and let's see what we get.

**Dave Jones:** Here we go. Now, it's under integrated circuits down here and typically you can tell what you want because it'll have the most number. In this case, 17,000 items down here, switching DC to DC converters.

**Dave Jones:** That's what we want. So, we'll click on that. And here we are inside our DC to DC converter parametric search. Now, we can scroll across like this and you can see all the parameters.

**Dave Jones:** We've got things like pack packaging package case mounting type operating temp power output, which we'll be using cuz we know we want 1.2 2.5 W if if you remember that from the calculations.

**Dave Jones:** So, we can choose those. Voltage input's very important, so we'll be using that one. Switching frequency, not so much. We're not caring too much about the efficiency at the moment except for the fact that obviously we want the device to have as higher efficiency as possible because then there's that minimizes the waste from our battery.

**Dave Jones:** Our current output will be using. Our voltage output, we might be using that but because most of these DC to DC converters are adjustable, we might not touch the output.

**Dave Jones:** Number of outputs, we only need one. Whether or not we want in an internal FET switch here, we might use that. The type of converter we'll definitely be using and the manufacturer.

**Dave Jones:** Now, here's a tip. If you don't know who manufacturers various devices, then you can use a supplier like this to find which manufacturers we actually that actually manufacture these type of converters.

**Dave Jones:** So, as you can see, Analog Devices, Very Diodes Inc., XR, Fairchild, Freescale, they're all there. All the big names, Linear Tech, Maxim, Micrel, Microchip, Nat Semi, On Semi, NXP, etc.

**Dave Jones:** etc. They're all there and these are Texas Instruments. And these are the ones we can go to to use this list to go to the individual manufacturer's website, but let's get down to it.

**Dave Jones:** Now, because we know that we want to only look at a boost converter, we want a step up. Here it is, step up boost converter. We're not worried about [ __ ] or flyback.

**Dave Jones:** I won't go into those. We just want a standard step up boost converter. So, we select that and we go apply filter. And bingo, it is now only showing all of these manufacturers who manufacture boost converters and it's we we're using this to eventually narrow down to the part we want.

**Dave Jones:** Now, let's go for the output power, shall we? Because we know we want 2.5 watts, basically. Now, we could go current output like this. We could actually scroll down here and but current output is a bit deceptive because because as I said, you don't know these chips are designed for over a very wide input voltage range.

**Dave Jones:** So, the output current might it might be able to deliver 2.5 amps, for example, but it might be it might not be able to do that at a very low input voltage and we'll go into that.

**Dave Jones:** We'll find out all that sort of stuff from the data sheets later. So, let's clear that. We we don't want that item there and we only want to look at power output.

**Dave Jones:** Let's see what chips are available in our power output range. Let's let's be generous and go 1 and 1/2 watts. You can hold down the shift key and let's go up to well, 3.3 watts.

**Dave Jones:** That's the maximum. Okay, apply filter. And we've found it's selected 166 items across seven pages. Now, we can narrow them down to in stock, but I'm not too fussed if they're in stock at Digi-Key or not at this particular uh stage.

**Dave Jones:** Now, what we The other thing we need to do is the voltage input. There's no point selecting a chip that only has a minimum of say 2.3 V input like that.

**Dave Jones:** That's of no use to us at all. We want one that at least goes down to 1 V or lower. So, we're going to select 1 to 5. There's these whole bunch of these ones up here.

**Dave Jones:** So, adjustable down to 0.7. This one goes down to 0.3. Wow. You know, that's pretty incredible. So, we'll choose those and we'll ignore all the rest. So, we'll apply filter.

**Dave Jones:** And what have we found? We've got now 95 items down here. I'm fairly happy with that at the moment as a first pass, and you can see our manufacturers have dropped.

**Dave Jones:** We've only got Linear Tech, Maxim, ON Semi, and Texas Instruments here are available manufacturers, but I know other ones might be able to do it as well, but let's go into our view page, shall we?

**Dave Jones:** And have a look down here. Now, Digi-Key have a sort by price option because price is always, you know, price is always an option when you want to do these sort of things.

**Dave Jones:** So, we can sort from lowest to highest in ascending order. We won't worry about in stock, but let's get the one off price, shall we? So, sort by price ascending, one-off price, and it reorders it like that.

**Dave Jones:** $2 This first one up here, there's 10,000 available, $2.98 in one-off quantity. That's quite reasonable. And it's a TPS, it's a Texas Instruments part. I don't mind their parts at all.

**Dave Jones:** It's a TPS61028 device. Um that one certainly rings a bell. And uh it's got an output current of up to 800 mA, but we'll go into that. Now, at the switching frequency, we're not too worried about the moment, but the higher the switching frequency, the greater the Well, the smaller the inductor you need, cuz that's important as well.

**Dave Jones:** This design is going to be fairly small. So, a higher frequency giving us a smaller inductor will help a lot. Now, the maximum power output's only 2.05 W here, but I'm going to give this device a go.

**Dave Jones:** I'm not too fussed about the packaging um for this particular project. So, let's go in and check out this device. Here it is here. Let's have a look at the data sheet.

**Dave Jones:** And here we go. We've got the this TI devices part open, and once which is fairly common for a lot of these devices. As you can see, it's the same data sheet for many different types of chips.

**Dave Jones:** So, when you're looking through the data sheet, just keep that in mind that these devices are different, and they will have different graphs in there. They'll have different parameters and specs and all sorts of things.

**Dave Jones:** So, just be careful about what actual part number you are referring to. Now, this one sounds pretty good. 96% efficient synchronous boost converter. 96% Right, sounds very impressive, but we'll go into the details, shall we?

**Dave Jones:** Device quiescent current. I'm not too fussed about how much current it takes during actual operation. Not too fussed. Input voltage range 0.9 V. Great, not a problem. I'm fairly happy.

**Dave Jones:** Doesn't go down to 0.8, but hey, I'm fairly happy with 0.9. Anything 1 or under, I'm fairly happy with. Fixed and adjustable output options. That's great. We might be able to get a fixed output voltage option, which allows us to minimize to lower our component count.

**Dave Jones:** We don't need these two external voltage set resistors, which you'll typically use. Applications, one cell. There you go. It's It's specifically designed for one cell, two cell, three cell alkaline.

**Dave Jones:** So, let's see how good this puppy is. Now, as you can see, this is an example circuit here, and uh there's one thing you'll notice missing from this circuit.

**Dave Jones:** Where's the diode? It's not there. So, it must actually be built in. So, this one's fairly handy in that it actually um with a built-in diode, that lowers uh your parts count and lowers your component cost.

**Dave Jones:** So, that's That is definitely a good thing. So, let's scroll down here, and really, when we when we looking at a DC-to-DC converter like this, we really want to go down to the guts of it, which are the graphs, okay?

**Dave Jones:** So, we'll scroll down. This is the internal operation of it, but we'll scroll down, and we will get the characteristic curves. Let's find them. Now, what we want is uh-huh, now we're Now we're looking at it.

**Dave Jones:** We want the efficiency in percentage um on the Y axis there versus the output current milliamps on the X axis. Now, as you can see, um this is for the TPS61020, and Vbat, okay, is 0.9 volts, and that's what we want, 0.9 volts.

**Dave Jones:** As you can see, 85% efficiency down at 1 milliamp, really nice. It goes up, but look, 100 milliamps, okay, it's still 85% efficient. Awesome. Pretty happy with that. But then it tails off like this, and at 200 milliamps, um output voltage Ah, no, look, we've been fooled.

**Dave Jones:** Ah, no. Look, Vout equals 1.8 volts, okay? Ah, I've been fooled again. I do it every time, and this is a real trap for young players. These These characteristic curves are only for Vout of 1.8 volts.

**Dave Jones:** That So, these have no relationship at all to what we want. We want 5 volts output. So, what we need to do um is find a characteristic curve graph.

**Dave Jones:** But, let's look at this graph over here on the left-hand side. Maximum output current versus input voltage. Perfect. Okay? Our input voltage 0.9 volts down here. Our V out 5 volts.

**Dave Jones:** It's got multiple graphs superimposed. So, let's look at the 5 volt V out graph here, and it plummets down like that. So, at 0.9 input at 0.9 volts input on out for a 5 volt output, it's only going to do about 100 milliamps, maybe 150 milliamps.

**Dave Jones:** Or at 1 volt input, it might squeeze up to 200 milliamps output. But, look, this chip's a failure right there. We simply can't use it. Now, just to prove that, let's go down and find an efficiency graph for 5 volts out because it will have continue to have these graphs.

**Dave Jones:** Here we go. That's 3.3. And bingo, here's V out equals 5 volts for various input voltage levels. Now, as you can see, when the input voltage over here, the higher the input voltage, the more output current you can get.

**Dave Jones:** Look at this. If the V bat here is 3.6 volts over here, if your battery voltage is 3.6, you can go up to 1 amp output current. Huge, okay?

**Dave Jones:** 5 volts, 1 amp, that's 5 watts. And it still does 90% efficiency. It's awesome. But, the trick is for these low voltage converters, once you go down, you're looking at this graph here, which then tails off completely at 250 milliamps.

**Dave Jones:** 100 down here to to at about 250, there it is. It's tailed off completely. So, this thing is useless and that's just going to continue to plummet to to nothing right down here.

**Dave Jones:** So, we're we'd be lucky to get 300 milliamps out of that at V1 at a 1.2 V input voltage, but we want to go down to 1 V or lower.

**Dave Jones:** So, this device clearly is not capable of that. Okay, so that TI part's a failure. Well, let's go back. The good thing about this is that you can hit the back button here and it goes back to the list and you can hit the back button again and it goes back to your parametric search search you had before and you can just go forward and back and it actually

**Dave Jones:** keeps all that info there. But, let's look at these other devices. We've looked at the Texas Instruments. Now, let's look at a Maxim uh 1947. Let's take a look at that one.

**Dave Jones:** Let's open up the data sheet here. Okay, low input output voltage step-up DC-to-DC converter with reset. Sounds pretty good. Low input voltage, 0.7 V. Uh high in 94% efficiency.

**Dave Jones:** Sounds pretty good. Fixed output voltage is 3.3. Well, um hopefully it'll go up to 5. But, no. Look at it. These devices only go up to 3.3. So, this device is a failure straight away.

**Dave Jones:** And we could have fixed that by uh sorting our parametric search by output voltage as well, but we'll we'll just live with that for the time being. Now, I've done looking at the TI parts.

**Dave Jones:** I want something else. All right, I found a linear technology part here, LTC 3424. I've heard of that one before, so let's check it out. Oh, 3 MHz frequency operation, 2 amps output current.

**Dave Jones:** Sounds Sounds great. 1.5 W not quite there, but hey, let's because I can overdrive this. The little quirk with this design where it really doesn't matter if I overdrive it or something like that.

**Dave Jones:** I'm not too fussed. So, let's go into the LTC 3424. It's a non-stock part, but that's not going to stop us. We might be able to get it somewhere else.

**Dave Jones:** And let's take a look at the data sheet, shall we? 3 MHz, that is a very high frequency boost converter indeed. 1.5 V to 5.5 output voltage, excellent. 1 amp switch current.

**Dave Jones:** Well, we're we're going to need at least the 2 amp switch current there for the 3424. But, we might be able to overdrive. It's not a problem. Wide input voltage range, 0.5 V.

**Dave Jones:** Excellent. Great. But, what do we want to look at? Give us the efficiency graphs. Okay, now, let's have a look down here. The efficiency is these ones down here are for a V out of 1.

**Dave Jones:** 8 V. That's hopeless. A V out of 1.8. Ah, look over here on the left-hand side. Look at the circuit here. This one has two different input voltages. Notice how pin six is a VDD pin there, and that goes to a higher voltage from 2.7 to 5.5.

**Dave Jones:** So, this isn't a true single-cell device. It actually needs a a second um step-up converter to uh step up our single cell just to drive the VDD of the chip.

**Dave Jones:** And well, that's a bit of a showstopper. Um well, not so much a a showstopper. We might have to resort to using this device. So, let's let's not count it out yet.

**Dave Jones:** Let's go check out the input graph uh the efficiency graph, sorry. Let's go and find it for efficiency graph converter 1.2 to 1.8. No, we want 5 V. It Give us the 5 V converter graph.

**Dave Jones:** It doesn't have one. Look at that. No, it doesn't have a 5 V output graph. So, that's pretty useless this device. No, doesn't have a parametric curves for 5 V output.

**Dave Jones:** Not impressed at all. So, I'm going to rule this one out because it just doesn't have the information that's easily got um from the graphs because we want to know the typical performance of this thing.

**Dave Jones:** Um and quite frankly, if it doesn't have a parametric graph, I'm not going to use it. I might use it as a last resort if I have to go in there and calculate it or measure it, but I don't want to do that right now.

**Dave Jones:** I'm looking for devices. Now, let's check out a Maxim device down here, Maxim 1765. Let's open the data sheet. Okay, now this Maxim device is only an 800 mA step-up DC-to-DC converter, but it's got a 500 mA linear regulator.

**Dave Jones:** So, who knows? This might be good. Um adjustable output from 2.5 to 5.5 up to 800 mA output. Uh let's have a look at its parametric graphs. Okay, here we go.

**Dave Jones:** Efficiency versus load current for V out, the one in the middle here. Uh V out plus 5 volts. Now, let's take a look. V in at 1.2. Now, it has different modes of operation.

**Dave Jones:** You can see here that um there's actually a normal mode and there's a PWM mode as well. So, uh basically the normal mode modes, they will allow greater efficiency at very low or almost no load currents.

**Dave Jones:** But, um I don't need that for my circuit. I just need it to work in PWM mode at a fairly high, you know, a couple hundred milliamps up to the 500 milliamp maximum.

**Dave Jones:** So, we're looking at those black curves there and we're looking at V in equals uh plus 1.2 volts. Now, uh the load current we're looking at here is uh Now, I'm looking at these graphs here and something doesn't seem right.

**Dave Jones:** This one, efficiency versus load current for V out 5 volts. This is what we want. Now, this is These are the typical characteristic curves you get. But, look at this for V in 1.2 volts, it's saying it's this bottom curve here.

**Dave Jones:** And if we follow that curve up, it shows that it's this big one which goes right out here to about 7 or 800 milliamps. That's crazy. It seems almost as if it's back-to-front.

**Dave Jones:** And this V in at plus 3.6 volts back here is this curve here and it cuts out there at 200 milliamps output current. It's back-to-front. I reckon they've screwed that up.

**Dave Jones:** If we look at the one on the right on the left-hand side here, efficiency versus load current, exactly the same parametric graph, but for plus 3.3 volts out, look, this is what you'd expect.

**Dave Jones:** V in at plus 1.2 is this graph, the bottom one here, which comes short and stops short like that. That's what you'd expect, and you'd expect the same thing over here on this uh on this graph on the right here, but I think they've actually this is a data sheet mistake.

**Dave Jones:** I believe it is. They've actually labeled this one down the bottom here, that label down there should be plus 1.2, and this one in the middle they've got right at 2.4, and this one here that it extends all the way out to 700 milliamps or so should be plus 3.6 volts.

**Dave Jones:** Ah, Maxim, you've got your damn graph wrong. But, these are the things you've got to watch out for. So, that's a real interesting dilemma. If you didn't have the experience to know that uh what these graphs should typically do and know what to expect from them, and you read straight off this graph, you'd be reading the wrong data, and you're designing that part into your prototype, and the damn thing

**Dave Jones:** wouldn't work. So, data sheets are not infallible. You've got to watch out for them. And in this case, the good thing is we have another the same graph here on the uh left-hand side, exactly the same uh parametric result here.

**Dave Jones:** And look, efficiency in percent, they've got 1% up here from zero to one. That's crazy. What's going on here? That's hilarious. It looks like Maxim have completely screwed up this data sheet, totally balls'd it up.

**Dave Jones:** But, these sort of things happen, and you've got to keep your wits about you, and you've got to uh know what to expect from these things. Don't take the data at face value.

**Dave Jones:** Always ask yourself, is this the expected result? Are these graphs what you would expect? How do they compare with other manufacturers' data sheets and so forth? And a dead giveaway that they've actually got it wrong is, as you can see, it's this one is labeled VIN plus 1.2 volts and it overlays with this particular graph here.

**Dave Jones:** So, if you go down there, they've they've clearly labeled it incorrectly cuz these are supposed to match up at the high end and deviate at the low end. So, the labels are a clear giveaway that's incorrect.

**Dave Jones:** Back here at our parametric search page, we've got one device down here, right down the bottom from ON Semiconductor. I really like ON Semi. So, let's check out their part, the NCP1422.

**Dave Jones:** Let's go in call for the price. It doesn't give you the price at all, but that's not going to stop us. Let's take a look at the data sheet and see what this baby's got.

**Dave Jones:** And here it is, 800 milliamps, synchronous rectified. But, as I said, you can't take that 800 milliamps at face value because okay, we need 500 milliamps on our output and you think this one will balls it in easy with 800 milliamps.

**Dave Jones:** Well, I think we'll find that that's not the case. Now, let's go down and try and find the parametric graph again. And here we go. We've found the efficiency versus load current.

**Dave Jones:** Exactly what we want. Now, we want the output voltage. This is the one on the right-hand side here is Vout equals 3.3. That's not the graph we want. We want this one, Vout equals 5 volts.

**Dave Jones:** And notice also that they actually give you the typical values that these were measured at. So, it gives you an inductance value of 6.8 microhenries, C in and C out values as well.

**Dave Jones:** So, these parametric graphs will change with all of your circuit parameters as well. So, you're we're really only taking these as a guide at this stage, a rough, you know, ballpark um uh type thing to see if we can use this device, but it will actually require either further calculation, further looking into the um the parameters of the data sheet, and building up the prototype, and actually measuring it

**Dave Jones:** before we can actually make a call on any individual device. Now, this one only has a V in of 1.5 volts. So, really that's not helping us much. Now, if we go down here, there's a V out equals 1.8 with a V in of 1.2, but they don't have really the uh the the curve we want on this characteristic graph.

**Dave Jones:** We'd I'd like to see it down at 1.2 volts or or 1 volt or even lower. What does it actually do? But, so we're stuck with the 1.5, but even at the 1.5, look, uh it's only going to do 100 200 It's only going to do 300 milliamps at 5 volts at 1.5 volts.

**Dave Jones:** And you know that it's actually going to be worse than that at lower voltages. You'll have a curve that'll go something like that and then drop off much earlier at 1.2.

**Dave Jones:** So, this one's a clear loser. So, we've exhausted the parts we found on a first pass here for Digi-Key. Now, let's actually go back. We'll scroll back through these parametric uh search, and we'll take out the uh the power output, which we had cuz sometimes they don't specify it, okay?

**Dave Jones:** The power output here is not specified at all. So, we'll actually reset that. Now, let's go for say the output current. Let's try and use this as a search parameter, shall we?

**Dave Jones:** Now, Now, this is a trap because as I said, if you thought that the output current was only 500 milliamps capable, then really, you know, you're not going to find the devices you want in that region cuz the switch current is going to have to be much larger than that.

**Dave Jones:** But, let's choose 500 milliamps anyway. No, actually, we'll we'll start at 1 amp and we'll go up to say 10 amps. That's pretty extreme, but let's try it out.

**Dave Jones:** Apply filter and bingo, we've searched and once again, the voltage input is a really key requirement. So, we must have that. But, let's stretch a little bit. Let's stretch it and say VIN 1.2 volts, say.

**Dave Jones:** Let's Let's be fairly generous because it might operate a bit below that. The parametric search data could be wrong. You don't know. So, let's narrow that down and bingo, look at the manufacturers we've got.

**Dave Jones:** We've got Diodes Inc. We've got Micrel. I I like Micrel parts. Um we've got Torex Semiconductor, some of the smaller players, Semtech. So, let's take a look at those parts.

**Dave Jones:** There's 173 items down there and let's go into view page. And once again, we'll sort by price, shall we? Price is always a good indicator to search to do a first pass search on.

**Dave Jones:** So, as you can see, a dollar 35 each in one-off quantity. So, they're going to be really cheap. And these are tiny little devices. Look at this Torex device down here.

**Dave Jones:** Um it's got a 1 amp output capability, anywhere from 1.8 volts to 5.3 volts output, 0.8 volts to 6 volts input. Let's take a look at this. Let's see what Torex can do.

**Dave Jones:** The good thing about Digikey is that it just allows you to jump straight to the data sheets and you don't have to go to the manufacturer's website. Bingo, they pop open.

**Dave Jones:** When I was a boy, you had to have, you know, bookshelves full of these data books and they're the only devices you could use, but anyway, let's not go there.

**Dave Jones:** Let's see what this Torex device has to do. Now, output current Oop. No, we don't want that. Bit of a fail there. Okay. Now, down here it shows that we've got 500 milliamps output it's capable of at output of 3.3 volts at a VIN of 1.8.

**Dave Jones:** Uh, it's really not going to do it um because we just know from experience looking at the other graphs that it just gets worse with A, a lower input voltage and B, a higher output voltage.

**Dave Jones:** That differential between VIN and Vout, when that gets wider, you know, the current capability is going to drop. That's why um yep, we failed again. That's why this one here that has when VIN drops to 0.9 volts and it's got a greater VIN to Vout range, the max output current's only 150 milliamps.

**Dave Jones:** That's no good at all, but let's go have a look at the characteristic curves anyway. Output voltage 3 volts. Uh, no, it's no, let's not bother. This sucker's just not going to do the job.

**Dave Jones:** So, we're back at our Digikey search here and well, that price thing didn't work out. Let's search by output current, shall we? Uh, here it is. Output current column, let's sort downwards.

**Dave Jones:** So, descending order, max output current of 5 amps. Now we're talking, right? Linear Technology, look, this looks like a big pin count uh package, so it's probably a uh multi-channel converter or something like that, but its input voltage 0.5.

**Dave Jones:** Um so, let's go check that one out, shall we? It's $5.36 for one off, which I guess isn't too bad. LTC 3425 And yes, I was right. It's a four-phase synchronous step-up converter.

**Dave Jones:** So, that means it needs four inductors. If we go down here to the circuit, there it is. Four different inductors. So, that takes up a lot of board space, but that will definitely get you the extra the the efficiency is much better with these multi-phase devices.

**Dave Jones:** So, you might have to sacrifice board space for output current capability. So, let's keep this one in mind. Even though I don't have much board space, I'm going to keep an open mind.

**Dave Jones:** And this one is for a V out of 3.3. So, no, I don't like that at all. Let's go down and find. Bang. As you can see, we ignore all these all of this data here, all these specs.

**Dave Jones:** We just ignore them and we go straight to the bottom line of the efficiency graph. Here we go. Converter efficiency for V out at 5 V. And as you can see, V in Look, it only gives you a minimum V in of 2.4.

**Dave Jones:** That's useless. I want to go down to 1 V. So, So, it looks like this thing just doesn't give us the data that we want. V out of 5 V, discontinuous mode, forced mode.

**Dave Jones:** Gets all messy. Um and converter input current microamps. No, let's No, it just it's not really going to have what we want. Ah, so let's This is another one which another graph we can get the maximum output current in burst mode operation.

**Dave Jones:** V out equals 5 V at versus VIN output current VIN and as you can see at 5 volts at VIN of 1 volt it only does 50 milliamps. God, what a wimp.

**Dave Jones:** And let's just keep going through the list because this is what you have to do typically to find devices like this. You might get one that you like first go but this is a bit more of an obscure application to go from a true single cell up to a 5 volt output at 2 and 1/2 watts is actually quite a demanding application.

**Dave Jones:** So let's check out this LM 2623. Let's look at the data sheet. General purpose gated oscillator this is a this a converter. Boom, I don't care. Let's go down to the parametric graph and this one as you can see needs an external diode on it.

**Dave Jones:** Let's go down and try and find these graphs. Here we go. Efficiency versus VIN exactly what we want. For V out 5 volts. Bingo, no problems at all. VIN as you can see these graphs do change from manufacturer to manufacturer.

**Dave Jones:** They're not always the same. This is actually versus VIN. So this one at 600 milliamps it doesn't really have the 500 milliamps we want but we can sort of guess that 500 milliamps is sort of going to be well there there's the 300 milliamp one.

**Dave Jones:** So and that's the 600 so you can guess 500 let's just split it down the middle like that and say 500 goes down there like that and the problem is with this device it only has goes down to a VIN of 1.8.

**Dave Jones:** So that's no good at all. This graph you you don't know whether or not these things just gently go down like that or whether they tail off really quickly.

**Dave Jones:** So and in the case of the 600 milliamp you can see it really tails off very quickly and that's just going to plummet like that. So, really this one doesn't have the graph we need to to determine if this device is suitable or not.

**Dave Jones:** So, this one's scrapped, too. All right, I'm sick of using Digi-Key. It just hasn't produced what I want in this particular instance. So, let's choose one of those manufacturers.

**Dave Jones:** TI makes some really good converters. So, let's go to the TI website and let's go down here to the power management. There it is. And bingo, let's try and this list over here different types of switching regulators.

**Dave Jones:** As you can see, step down, step up. There's 90 of them. They have 90 different step up regulators. Surely we can find a regulator in here from 90 of them.

**Dave Jones:** Check this out. The good thing about Texas Instruments, look at this. They have a specific check box for one cell sorry, one cell alkaline, nickel metal hydride input. So, let's tick that.

**Dave Jones:** They're doing our hard work for us. It automatically refreshes the table. We don't have to do anything else. Look, we can type in the input voltage here and do better better parametric search, but let's search for a true one cell capable alkaline converter and bingo, these are the ones we've got here.

**Dave Jones:** The TPS 61026. That's what we looked at before originally. Here it is. You remember this? The Texas Instruments data sheet. We had the 61026. So, it looks like that's pretty much the only device they've got that will actually do it.

**Dave Jones:** There's another one here, the TPS 61220 series, which is that part of this one over here? 22 No. So, we can probably um take a look at this one.

**Dave Jones:** And here it is. We've got the TPS61220 and let's take a look at the data sheet. Let's not muck around. Waiting for the internet can be a real [ __ ] There we go.

**Dave Jones:** And we're up. Right, I don't care about the rest of the crap at the top. Just give me the graph. That's all I want, really. Oh, efficiency versus output current and input voltage.

**Dave Jones:** Oh, check it out. This is even in color. Isn't that neat? Let's see if we can make heads or tails out of this one. Now, the input voltage up here, it does go to 0.8.

**Dave Jones:** So, that's brilliant. I love that. But, this Look, there's the trap. Trap for young players. V out 3.3 V. That's no good at all. Let's see if we can find the graph down here, similar one for the 5 V, which is what we want.

**Dave Jones:** V out 1.8. Here we go. We've got it. Efficiency and versus output current and input voltage. Okay, now we're talking V in of 0.7 V. Excellent. Ah, this is a real wimpy device.

**Dave Jones:** Look at this. It's got output current at 0.7 V, only goes to 25 mA. Useless. No, this really isn't going to cut it. Even at the V in of 1.2, we're only talking at We're talking sub 100 mA.

**Dave Jones:** Useless. Scrapped. All right. So, we've done our dash at TI. Let's check out Microchip, shall we? Because Microchip are highly underrated when they come when it comes to analog parts.

**Dave Jones:** I've mentioned this before. They're very, very cheap and they're really quite good performance. So, let's check out their power management. One's down here. We're switching regulators. Microchip. Here we go.

**Dave Jones:** Jumps up with the parametric table, really nice. Now, what we want is input voltage range here. So, we want to sort here from low to high. So, there we go.

**Dave Jones:** They do make ones. It looks like they only make uh the MCP16 uh 1623, 1624, and 1640 range, which goes down to a low enough voltage for our particular use.

**Dave Jones:** Uh now, let's check out the output current milliamps. Well, this one only goes to 350. That's the beefiest one they've got. But, uh let's check it out anyway, just for fun.

**Dave Jones:** And, let's load up the data sheet. And, here we go. The MCP1640. It's quite a nice device. It's only a small footprint. And, typical converter for 3.3 volts out.

**Dave Jones:** Nah, give us the real graph. I want 5 volts. Thank you. Okay, here we go. 5 volts out. PFM or PWM mode, as we've mentioned before. Uh PFM mode allows you greater efficiency at lower current.

**Dave Jones:** So, we're looking at the dashed PWM only mode here. VIN at 1.2 is the lower graph. It goes up and starts to drop off, and the graph ends at about 100 milliamps for 5 volts out.

**Dave Jones:** So, we're about five times short. Oh, well. And, let's try National Semiconductor, cuz they're big in the uh converter market. So, let's go down and have a look at their boost converters down here, conveniently come on the front page here.

**Dave Jones:** And, they've got this like Java sort of app, which uh So, don't know. Don't really Don't really like it. It's a bit of a bit of a pain in the ass, but here we go.

**Dave Jones:** Minimum input voltage, okay, we're looking at 1 point Let's change the slider here. At It's a bit tricky, but let's go to 0.99. Actually, let's be generous. Let's type it in.

**Dave Jones:** 1.2. Let's hit go. And look, they've only got two devices, LM2621 and LM2623. So, that's no good at all. We've already looked at the LM2623. That's the best they had, and it wasn't suitable.

**Dave Jones:** And we can't stop there. Let's try at Linear Technology. They make some of the best devices in the business, so let's go to power management. Let's go to switching regulators.

**Dave Jones:** Let's go to step-up regulators. And let's see what they can do for us. Let's go down here. Let's not worry about all this quick search. I don't really like the Linear Tech thing they've got down here.

**Dave Jones:** It's a bit confusing. Let's go to view all products, view table down here, and we'll sort it out for ourselves rather than they use their silly little tool. We'll go VIN minimum, okay, so we're looking at Let's sort that column there.

**Dave Jones:** The VIN column, and as you can see, they've got quite a few devices which go down to 1.2 V here. They Look at them. There's a whole bunch of them.

**Dave Jones:** So, we're going to have to check these out, but let's also look at the switch current. Now, let's look at the switch currents for Well, 180 amps is just insane, but let's go for say anywhere from say 1 and 1/2 amps to there.

**Dave Jones:** So, let's update that. And bingo, we've still got a ton of devices which actually Oh, sorry. No, we have to go VIN minimum. So, let's go VIN 1.2. It It cleared the previous thing we had, and bingo, we've narrowed down our devices to these ones here.

**Dave Jones:** Now, let's take a look at uh they all do VIN minimum 1 V. That might be good enough. V out uh VIN max 10, switch current 3 amps. That's what we're talking about.

**Dave Jones:** Um so, in an SO8 package, let's take a look at the LT1308. And here you go, 5 V at 1 amp from a single lithium ion cell. Now we're talking.

**Dave Jones:** We've only got an alkaline uh cell, so maybe it won't do the 500 mA we're after, but hey, this is this sounds like it might certainly might be in the ballpark.

**Dave Jones:** So, let's open up the data sheet. Okay, let's not muck around. Let's go straight down to the graph, which is what we want. Although they've got one here for It doesn't tell you what the V out is.

**Dave Jones:** No, doesn't tell you on that graph. What's the point of that if they don't tell you what the V out voltage is? Crazy. All right, I can't see it there.

**Dave Jones:** I must be blind. Anyway, let's go down and find the proper graph down here. Here we go, 5 V output efficiency. Let's take a look at this baby. What can it What can it do for us?

**Dave Jones:** 1.5 V input voltage uh it drops out at 100 200 250 mA. What? Fail. And that looks like that was the best device that Linear Technology had, because if you go back and look at the Why do I have to click resend there?

**Dave Jones:** It's crazy. If you look at the ones that we had, that had the biggest uh switch current capability. So, that's going to be the best device out of all these.

**Dave Jones:** These ones won't be able to touch it, but if you want to go, we can look at the 35 39 just as a quick little aside, but you know, because the switch current isn't as large, that it's pretty much not going to do it, but hey, it might be a little bit more optimized, so let's give it the benefit benefit of the doubt, shall we?

**Dave Jones:** And we'll go down here in the efficiency low current at what Vout 1.8 3.3, there must be another one here, 5 volts, there it is. Our friend the 5 volt efficiency versus low current graph.

**Dave Jones:** Now, for VIN, it's only got VIN of 2.4. Once again, that's a fail because it doesn't um give us any data that we can use to actually uh to see if this device is suitable at um you know, at uh at low input voltages.

**Dave Jones:** So, the efficiency here at VIN 2.4 at 2.4 volts, yeah, it doesn't amp, but what does it do here? I don't want to have to buy the chip, build it up, and then actually measure these graphs myself.

**Dave Jones:** What a pain in the ass. So, I'm going to give Linear Technology the flick. Well, we're starting to get a bit slim pickings now, but let's go to Maxim, see what Maxim have.

**Dave Jones:** You know about Maxim's lead times, I've bitched about them before and their availability, but they do make a hell of a lot of uh devices, and they make a hell of a lot of uh power regulators and switching converters and stuff like that.

**Dave Jones:** So, let's go into power and battery management. They make 1,769 different power management devices. It's crazy, and this is one of the problems why Maxim can't actually supply their devices because they don't have enough factories to churn out the things cuz they've got, you know, 20,000 different parts or something.

**Dave Jones:** It's crazy. Anyway, rant over. DC to DC switching regulators, step up, there's 89. They make 89 different step-up converter chips, and that's fantastic for us. So, let's go in.

**Dave Jones:** VIN minimum. Aha, here we go. And this is I like Maxim because, as you can see, as I slide this um slider down here, it tells me fewer and fewer parts are available.

**Dave Jones:** So, let's go 1.2 V and under. We've got 31 parts out of the total of 87 up here. So, it it tells you I I I like it. It's a pretty good uh sorting capability.

**Dave Jones:** It's got all the info you want there right in front of you. Now, let's uh maximum IO. Let's go the minimum. It's got to be greater than let's say 1 and 1/2 A.

**Dave Jones:** Bingo, we're down to four parts. There you go. Once you start sorting these parameters down, it comes down pretty quickly. Now, the MAX1708, 1763, 1709, 1703. Um this one down here, the 1703 one-cell to three-cell high power.

**Dave Jones:** Whoa, ho. 1.5 A. Here we go. This might be a winner. Let's check it out. Let's hope it is. It's in an SOIC-16 package, so that tells me that's reasonably higher power than some of the other um packages we've been looking at.

**Dave Jones:** Um it's it's certainly a little bit bigger, so let's go down to the MAX1703. One cell. Ah, look at it pop up. GONE. NO. I DO not want it Yeah.

**Dave Jones:** You may be selected to take part in customer satisfaction survey. No. Go away. Gone. No, thanks. Should The button should be called piss off, not no, thanks. Anyway, let's not muck around.

**Dave Jones:** Um well, now I just noticed uh something down here. It's 140 m 75 m N-channel MOSFET switch, 2 amps. That's pretty nice. So, let's download the data sheet and take a look at the maximum 1703.

**Dave Jones:** And once again, let's not muck around. Let's go down to our parametric graph down here and efficiency versus load current at Vout 5 volts on the left-hand side here.

**Dave Jones:** Now, uh Vin 1.2 volts. Now, let's look at this one. Uh as you can see, it's look, it's getting up there. 100, 200, 300, 400. Ah, look, it's going to do it.

**Dave Jones:** The graph actually stops at about 350 milliamps. Uh sorry, 450 milliamps. So, it's all that graph almost goes to 500. If you extrapolate that graph, this one here is the one we're talking about.

**Dave Jones:** If you extrapolate that down a little bit further, it's going to plummet. At 500 milliamps here, it's going to be about still about maybe 65% to 70% efficient at a Vin of 1.2 volts at 500 milliamps.

**Dave Jones:** I think we've found a winner. It's a shame that it doesn't have a lower um input voltage graph, but you know, 1.1 volts isn't much lower than 1.2, so you can sort of, you know, guesstimate where the graph is going to be.

**Dave Jones:** And the efficiency, well, it might be down at 50% at 1-volt input. You don't know. You'd have to actually measure it, but it looks like after all that searching, we've finally found a chip that actually looks like it might do what we want.

**Dave Jones:** It certainly looks like it's capable of getting 500 milliamps out of it, or pretty close to it, for a good part of the input battery range. and that's what we want.

**Dave Jones:** Even though um because once you get down to 1 V, that's, you know, the lower sort of 30% of the battery capacity or something like that, but the majority of the battery capacity will occur at greater than 1.2 V, and if we use a lithium AA cell instead of an alkaline cell, then we'll get even better performance again.

**Dave Jones:** So, this one looks like it's going to do do the job. So, the MAX1703, I think we might have a winner here. So, let's go over to Digi-Key and go MAX1703, and once again, we didn't see that MAX1703 in our parametric searches on Digi-Key.

**Dave Jones:** So, we had to go This is an example of how you have to go direct to the manufacturer's website often to actually find these parts. You can't just rely on the on the supplier like Digi-Key and their search capability.

**Dave Jones:** So, let's go down here. It's found it. Do they have them in stock? Yes, they've got them in stock. Quantity available, 852. That's reasonable, but look at the unit price.

**Dave Jones:** Wow, 12 bucks and 10 cents and 9 cents for one chip. Geez. Ah, guy, you can buy a rocket for 12 bucks. Fly to the moon with that. It's crazy.

**Dave Jones:** But the the 100-off price down here, $5.48 at even a 100-off price. And if we go back to Maxim here, and they should have a typical That's a Digi-Key price.

**Dave Jones:** If we look at Maxim, they'll have a typical price. Here it is down here. There it is. It's $3.29 at 1K quantity. So, you can buy them directly from Maxim.

**Dave Jones:** They do sell them sell sell them themselves direct, I believe. So, you should be able to get them for $3.29. Bit more expensive than I wanted, but certainly not out of the ballpark.

**Dave Jones:** So, I like it. The MAX1703, I'm going to call that one a tentative winner. But, of course, that's not the end of it. Let's take a look through the data sheet a bit further, and let's uh look at some other stuff.

**Dave Jones:** Here's an interesting one, startup voltage versus load current. Now, this is important because if your converter can't start up, then you've got a real problem. Now, um due to the nature of this design, I don't actually expect it to start up at low uh battery voltages I expect it to start up with a fresh cell, and that's it.

**Dave Jones:** It'll just use up all the cell, and it shouldn't have a requirement to start up at low voltage. So, this is interesting. Startup voltage on the Y axis versus load current on the X axis down here.

**Dave Jones:** So, let's look at 1.5, smack in the middle there, the startup current, it looks like at 1.5 V, it can do 200 300 mA. So, anything greater than 300 mA uh load current, it's not going to be able to start up.

**Dave Jones:** So, really that's required that's dependent upon um that's that that might be pushing it for the design. I'll have to actually try it out practically and see if it works because if the load comes on instant, which it may not with this device, um in fact, you can use it in a mode where the um output isn't loaded until such time as you plug it in.

**Dave Jones:** So, the regulator would start up first, and then you can plug it in. So, it shouldn't be too much of a problem. Let's have a look at some other stuff.

**Dave Jones:** This uh peak inductor current limit versus output voltage for PWM mode. That's uh quite interesting. An output voltage of 5 V, it's about 2.7 A uh output current limit.

**Dave Jones:** So, this chip, it looks like it actually has uh current limiting um capability uh basically. So, that um might be a potential trap if we try and use it um in um in in an actual circuit where we're trying to maybe overpower the thing or, you know, uh uh over over spec the thing.

**Dave Jones:** So, it might actually shut down on us. So, we just have to be careful of that and we'll have to actually try this chip out in a um mock-up prototype first just to make sure it can do the job.

**Dave Jones:** Now, of course, I know what you're thinking. There's more than one uh component manufacturer out there. So, let's try Mouser, shall we? DC converter. Let's type that into Mouser and see what sort of parametric search it has.

**Dave Jones:** So, semiconductors down here. We want 3,666 devices. There we go. Power management ICs. That's what we want. And let's go to DC to DC switching converters. 1,544 cuz you want the converters instead of the controllers.

**Dave Jones:** Just watch out for that there. Normally, those controllers are normally used in higher power systems um that have more more discrete components external uh FETs and things like that.

**Dave Jones:** So, we want a switching all-in-one switching converters. So, let's go down into there and what? Look at the parametric search they got. It's hardly anything. It's hopeless. It it I don't think it used to be like this.

**Dave Jones:** Has something changed in Mouser? But, all they got is through hole and SMD and case and packaging. You're You've got to be kidding me. So, let's go to the through hole Sorry, the um SMD devices.

**Dave Jones:** But, look, it just doesn't work. It's hopeless. What's the point of that parametric search at all? Just none. So, we can limit products to manufacturers, which is quite good.

**Dave Jones:** Um but, really, I mean, god. Let's go down to Maxim products down here. And select manufacturer. And once again, it still hasn't given us the parametric search we need.

**Dave Jones:** So, Mouser is absolutely hopeless for DC-to-DC converters compared to Digikey. Mouser can be great for other stuff I found, but in this case, it's next to useless unless you're searching for a price, which we'll search for our Max1703 here.

**Dave Jones:** We'll type that into Mouser, and we'll get um yeah, they've got 215 in stock. They were $16 for a one-off. Um, $7.88 for 100. So, that's pretty much all it's good for.

**Dave Jones:** So, there you go. I did actually search uh many other manufacturers as well. I used their parametric searches directly on their sites, and I couldn't find anything. The best The closest device I could find is the Maxim Max1703 device here, which looks like it will get fairly close to my requirements, but I have to build it up and find out.

**Dave Jones:** But, these parametric searches usually uh you'll usually get like uh three, four, five devices turn up that will suit your particular requirements. You might even have more. It's It's fairly rare to get down to one device, which is your only choice.

**Dave Jones:** Um, cuz if you got three, four, five devices available, then you choose the one with the lowest price, the best availability, the best footprint, the best features, which have, you know, might have some stuff built in you might need, yada yada yada.

**Dave Jones:** But, um the best I could do here is the Max1703. Now, I also searched for devices with external FETs as well, and I still couldn't find anything um suitable.

**Dave Jones:** So, there are two other options left either apart from use the Max1703, which I am going to try out. I'll I'll uh breadboard that up and see what it's like.

**Dave Jones:** The other option is to actually get multiple DC-to-DC converters like this and actually put them in parallel and then sum them at their diode the actual cathode of the diode here.

**Dave Jones:** But that's a bit tricky because then you how do you equally share load across across the various regulators and but it might turn out because this MAX1703 is quite expensive.

**Dave Jones:** So it might turn out that it might be more cost beneficial to use five of those little cheap microchip devices at you know 40 cents each or something like that.

**Dave Jones:** Five of those with but then you're going to need five diodes and you know five inductors and stuff like that. Takes up more room but hey it might be more cost effective.

**Dave Jones:** So if your design is cost driven you might look down that avenue but I'm not so necessarily cost driven in this respect that I'd have to resort to paralleling DC-to-DC converters which is a pretty tricky business.

**Dave Jones:** You've it's quite hard to share power across these converters. They can upset each other and one hogs all the current and that just gets really nasty. And the third option would be to roll my own DC-to-DC converter.

**Dave Jones:** But really I don't want to go there. I haven't got the time nor the enthusiasm to dick around and try and do that sort of stuff. So I think there you go.

**Dave Jones:** I'll just buy the MAX1703 and suck it and see. So there you go. I hope that was interesting that this is a typical design example where it was actually quite hard and even though I might have compressed this into I don't know 20 or 30 minutes however long I've been going I've actually spent much much longer looking through all these data sheets trying to find all this stuff.

**Dave Jones:** It's crazy and this is just for one part for simple step-up DC-to-DC converter. You can see how much work's involved. But, this is what a typical design engineer would do a lot of the time.

**Dave Jones:** They're just looking through data sheets, parametric searches, trying to find suitable parts. So, good luck when you're trying to do this. See you next time.
