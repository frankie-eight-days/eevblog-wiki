---
video_id: li0XKnpOZyM
title: EEVblog #957 - How To Measure DC-DC Converter Efficiency
url: https://www.youtube.com/watch?v=li0XKnpOZyM
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 45, "3": 62, "4": 72, "5": 86, "6": 100, "7": 115, "8": 128, "9": 141, "10": 152, "11": 162, "12": 177, "13": 194, "14": 210, "15": 230, "16": 251, "17": 262, "18": 274, "19": 293, "20": 312, "21": 321, "22": 332, "23": 348, "24": 360, "25": 377, "26": 393, "27": 411, "28": 424, "29": 432, "30": 451, "31": 467, "32": 485, "33": 504, "34": 523, "35": 538, "36": 559, "37": 569, "38": 585, "39": 599, "40": 611, "41": 622, "42": 634, "43": 645, "44": 654, "45": 668, "46": 678, "47": 703, "48": 715, "49": 726, "50": 738, "51": 748, "52": 759, "53": 769, "54": 783, "55": 795, "56": 809, "57": 821, "58": 834, "59": 849, "60": 865, "61": 876, "62": 894, "63": 906, "64": 922, "65": 937, "66": 948, "67": 958, "68": 969, "69": 980, "70": 993, "71": 1004, "72": 1020, "73": 1033, "74": 1043, "75": 1059, "76": 1071, "77": 1086, "78": 1105, "79": 1118, "80": 1132, "81": 1143, "82": 1156, "83": 1165, "84": 1176, "85": 1185, "86": 1199, "87": 1211, "88": 1223, "89": 1232, "90": 1247, "91": 1261, "92": 1274, "93": 1286, "94": 1303, "95": 1318, "96": 1327, "97": 1340, "98": 1353, "99": 1372, "100": 1383, "101": 1408, "102": 1417, "103": 1434, "104": 1447, "105": 1460, "106": 1473, "107": 1494, "108": 1503, "109": 1514, "110": 1527, "111": 1541, "112": 1556, "113": 1579, "114": 1593, "115": 1605, "116": 1617, "117": 1633, "118": 1647, "119": 1664, "120": 1675, "121": 1684, "122": 1695, "123": 1707, "124": 1721, "125": 1734, "126": 1747, "127": 1763, "128": 1782, "129": 1793, "130": 1810, "131": 1821, "132": 1831, "133": 1842, "134": 1865, "135": 1885}
---

**Dave Jones:** Hi, let's say you've got a DC-to-DC converter that you want to measure the performance of whether or not you've designed it yourself into a particular product or you've bought maybe an off-the-shelf one like this which doesn't provide any characteristic graphs performance graphs and efficiency graphs for it.

**Dave Jones:** So, how do you actually measure the performance of a DC-to-DC converter and get your typical efficiency curve which is the efficiency in percentage versus the output current draw? And you'll find this in practically every data sheet for every DC-to-DC converter chip on the market and these are usually typical, but but the actual efficiency of your particular DC-to-DC converter that you design is dependent upon a whole host of things

**Dave Jones:** what type and what size inductor you've got, output capacitance, if you've got an external switching MOSFET, what type that is, and all sorts of and the frequency you operate at, all sorts of different parameters go into determine the efficiency of a DC-to-DC converter.

**Dave Jones:** And sometimes this efficiency characteristic graph will also include power loss as well which is quite typical cuz you want to know how much power's being dissipated in your little brick converter here.

**Dave Jones:** So, how do you actually measure and graph your own characteristic curve like this? Well, let's take a look at it. I've actually kind of done this in several old much older previous videos, but not a dedicated video for it.

**Dave Jones:** So, let's have a look in the case little Digi-Lint 12-V power brick here, it's a boost converter, 5 V into 12 V out. Data sheet doesn't have the efficiency curves.

**Dave Jones:** Let's measure it. The efficiency of a DC-to-DC converter is just the output power divided by the input power. If the output power exactly matches the input power, i.e. you get 1 W out for 1 W in, then it's a 100% efficient converter which is basically impossible.

**Dave Jones:** Uh you can't get a 100% efficient DC to DC uh converter. A typical really well-designed, good DC to DC converter will typically have an efficiency greater than 90%, you know, a real kick-ass one might be like 95%.

**Dave Jones:** So, you're going to have some loss in the converter here. So, what we need to do is measure the input power going in and the output power. So, we need a power supply and we need an electronic load.

**Dave Jones:** I've done a whole video on making your own electronic uh load, very popular do-it-yourself uh project. So, I'll link that in down below. If you haven't seen it, you can make it for using junk bin parts for practically uh nothing.

**Dave Jones:** But, we need to get the input power and the output power. So, we can actually do that with these two instruments here. So, we've got a modern smart uh lab bench power supply here.

**Dave Jones:** This is a Rigol DP832 and it uh shows our input voltage and our input current, 5 V, 140 mA, and it automatically calculates our input power for us, so we don't have to uh calculate that with our calculator later.

**Dave Jones:** Beauty. So, basically, the input power here is 0.7 W and on our output, we've got our electronic uh load. A modern one like this can easily uh accurately measure the output voltage and the uh output uh current as well here and it also calculates your output power.

**Dave Jones:** So, I'll set a constant current output load here of of 50 mA, 0.05 A, and our output power is 0.59 W. So, 0.59 W / 0.7 W input here gives us an efficiency around about 84%.

**Dave Jones:** That's okay. But, if you remember that efficiency curve that we want, it's efficiency on the Y axis versus output current on the X axis. So, we have to sweep the output current here, set different loads, and get all the data points for the efficiency, so that divided by that for different values of load current here.

**Dave Jones:** And we have to do that over an extremely wide range of output currents. It can typically for a, you know, a universal type DC-to-DC converter, the data sheets, as an example here, will show typically 10 microamps up to an amp, for example, and they'll do that on a logarithmic graph because otherwise you can't fit it all in.

**Dave Jones:** But, aha, there's a big trap for young players here and I've mentioned this in many previous videos, but it's very important in this scenario, so I'll go over it again.

**Dave Jones:** You'll notice how our power supply on our input here is showing nice precise 5.000 V. It's a real accurate power supply, so you can believe it. But, that's 5 V sensed right at the output terminals here.

**Dave Jones:** We've actually got these wires going over to the breadboard here. Now, I've actually got another multimeter set up that's actually probing directly on the input pin there, okay? So, it's actually after the drop in all in the in the wires here, okay?

**Dave Jones:** So, the ground and the input. And, bingo, look, 4.66 V at the input to the converter. So, our 5 V is way off there, right? So, we've got a real large, very significant error there due to the drop in our wires.

**Dave Jones:** Whoa, lucky we actually measured it right at the input. And likewise, we're going to get a similar error on our output here because we've got these long wires going over.

**Dave Jones:** They're you know, they're reasonably thin wires, they're long, there's going to be some drop on those at a significant current. We're only drawing 80 milliamps, but hey, look at the error here, okay?

**Dave Jones:** We've got our nice precision supply here. Look at this, 11.7737. And this is a this is a really kick-ass electronic load, 0.05% precision, fantastic. But, it's it at the output terminals here.

**Dave Jones:** So, it's including the drop along these wires. We don't want that. We're measuring the efficiency of the converter, not the converter plus the input and the output wires here.

**Dave Jones:** And once again, look at the discrepancy here. I've got a meter on the directly connected to the output pin and the output ground there. And you can do this because there's a 10 megaohm input impedance on your multimeter, so it's drawing no current through any of these leads.

**Dave Jones:** So, you are actually measuring the true voltage on the output there. You're sensing it. This is called a four-wire sense measurement. And look at the discrepancy. It's This converter is actually outputting 12.13 V, but the our load is only measuring 11.8.

**Dave Jones:** So, we've got a discrepancy here, very significant, and a very significant discrepancy on the output. So, if we just use these two instruments and didn't do four-wire terminal measurement, but we can get very significant errors, which would completely ruin our efficiency curve.

**Dave Jones:** So, real trap for young players. Beware. Make sure you do four-terminal measurement. So, a simple Dave CAD drawing showing you four-terminal or four-wire measurement, sometimes called a four-wire sense measurement, whatever you want to call it.

**Dave Jones:** We've got our DC-to-DC converter brick here, our input and our output. The ground, just assume that the ground is the same, one common pin, whatever it happens to be.

**Dave Jones:** And you see that we've got voltage sensing right at the input pin there and right at the output pin there for both the output, for the positive in and positive out, and also the grounds as well, because you're going to get losses in both your ground wiring and your positive wiring as well on both input and output.

**Dave Jones:** And and then your ammeter, your current meter goes after that. So, then you've got your variable load over here. It can be a dummy resistor, electronic load, doesn't matter what it is, and your input ammeter here, and your adjustable power supply here.

**Dave Jones:** So, you don't want to read the value on your power supply here. You want to read the value on your voltmeter here. Unless you're working at very low current, in which case you're not going to get any loss across your wires, but just assume that you're going to get losses, and you need to measure using the four-terminal technique.

**Dave Jones:** This is why it's called four-wire or four-terminal, because there's one, two, three, four wires for each measurement point. And of course, you don't need fancy gear like a a modern programmable power supply to display power, or a really, you know, high-end precision electronic load like this.

**Dave Jones:** All you need is four multimeters. And I said it before, I'll say it again, this is a classic example why any well-equipped electronics lab should have four multimeters. It's not hoarding, it's not a multimeter fetish, it's to measure input power and output power of a basic DC-to-DC converter power supply.

**Dave Jones:** Very common in any electronics lab to do this. If you haven't got four meters, you can do it, but it's a pain in the butt. So, all you need is any lab power supply, and you don't have to worry about the voltage and current readings.

**Dave Jones:** Doesn't matter, it doesn't have to be fancy pantsy, just any supply will do. Two meters measure input voltage and input current, and output voltage and output current. And the good thing about this, we will actually have to resort to this, because if you have a look at the efficiency curve again, you'll notice that it went down to 10 microamps, okay?

**Dave Jones:** Right up to an amp. And if we have a look at, you know, a really good lab electronic load like this, it's only got 1 milliamp precision here, only two digits on the output power.

**Dave Jones:** It's bugger all. So, you know, we can't we can use this for, you know, large output currents, and the voltmeter is very precise. So, that's no worries whatsoever. Um but the but setting our load current is no good.

**Dave Jones:** Okay? So, we need something else to actually generate the very low loads, the 10 microamps and stuff like that. We at least need to be able to measure it with our with a separate output current meter that can measure those low currents precisely.

**Dave Jones:** This particular thing can't do it. So, yeah, I can just use a resi- stor. Something like that. We know the output voltage roughly 12 volts. We can just whack a resistor in there and get our 10 microamps on the output.

**Dave Jones:** Just use Ohm's law. Very simple. And really good quality electronic loads know all about four-terminal measurement and remote sensing. And it's got a remote sense option. There's some sense terminals on the back.

**Dave Jones:** Sometimes they might be on the front. This time it's screw terminals on the back and we can just select our remote sense on. Fantastic. And if we go back out and bingo, this now matches our meter.

**Dave Jones:** Well, our resolution's not there, but yeah, it basically matches cuz we're now doing four-terminal measurement with our electronic load. And another thing to be aware of, in this case I'm just measuring on a breadboard.

**Dave Jones:** It's a little bit dicky in here. And if you muck around with the wiring and stuff like that, things can start to change, you know, dicky contacts on breadboards and wires and stuff like that.

**Dave Jones:** If I was doing this properly and professionally, I would actually sacrifice this thing and actually solder the wires directly on four wires on the input and four wires on the output directly on the terminals.

**Dave Jones:** So, then nothing can go dicky with your measurements. And along with your efficiency, if you want to, you can measure other parameters well. Like you might measure the switching frequency, for example.

**Dave Jones:** You'll get that by typically probing the inductor in there. Depends on the converter you're using. And you can have a look at the switching frequency because your switching frequency, it might be a converter type that's the switching frequency changes depending on the output power and this will fairly typically happen with converters that want to get maximum efficiency across like at very low currents as well.

**Dave Jones:** So, that's you know, it's not uncommon. A lot of DC-DC converters are fixed frequency but a lot of them will actually change their frequency to make them more efficient over a larger output current range.

**Dave Jones:** And you might want to measure temperature for example. So, you might actually get in there and attach a little thermocouple probe to your converter or near your converter or whatever.

**Dave Jones:** Maybe on if it's using a heat sink you might attach it to the heat sink or something like that and you can plot temperature versus your efficiency and output and load dissipation as well.

**Dave Jones:** Just you know, if you want to be thorough. And that could be a big deal because hey, your converter might work. No worries. It's ambient temperature or whatever. Everything works just fine in the lab.

**Dave Jones:** It gives you the efficiency you want. It gives you the output power you want. But if it's running at 100° C you could be in trouble. You could come a gutser and it's not going to work in the field.

**Dave Jones:** It's not going to you know, have a long lifespan whatever. So, you know, you might want to measure something like temperature as well and plot that along with your efficiency.

**Dave Jones:** But we won't do that today. Now, you could actually automate all this of course. of modern instrumentation is all ethernet LXI controlled. For example, this power supply is this BK Precision one can be remotely controlled as well.

**Dave Jones:** So, I could actually script this to generate different output voltages and stuff like that. But hey, we don't have four terminal measurement on here but I could hook up some data logging well, some ethernet LXI connected bench multimeters that I have.

**Dave Jones:** You could automate the whole thing. You could spend like a whole day just setting this up. It's easier just to hook four multimeters on the input and output and increase your current and just note them down on a notepad and then just whack them into a spreadsheet.

**Dave Jones:** So, you know, it's you'd only automate this if you really wanted to just for kicks or you had a lot of converters to measure. And you can use some more advanced instruments like say this Keithley 2400 source meter or shmoo SMU.

**Dave Jones:** For example, you might have like a multi-channel SMU system for a real complex measurement. But as I said, you don't need any of this. You can get away with just a couple of multimeters and a dodgy power supply.

**Dave Jones:** And a do-it-yourself electronic load. And other stuff like output ripple voltage might be important for example or versus output capacitance. There's many other different parameters that you can do to measure a DC to DC converter.

**Dave Jones:** It's almost the sky's the limit. Now, when we actually go to measure this, if we take a look at our little diagram again, the burden voltage on our current meter on our ammeter on the output here is basically not going to matter as long as we've dialed in the load to get our output current.

**Dave Jones:** So, if it's an active load, it's going to sync that. But if it's a resistive load, then you're going to have to tweak it depending upon your burden voltage here.

**Dave Jones:** Likewise on the input, the you might think that the burden voltage here ammeter doesn't matter because you're measuring the input voltage here and that might be true. But generally, you want to your performance curve for your DC to DC converter is at a known input voltage.

**Dave Jones:** So, it might be 5 volts DC input. So, you don't want it to vary based on the current because as you decrease your load, you draw more current on the output, you're going to draw proportionally more current from the input here.

**Dave Jones:** You're going to get extra losses across your burden voltage or your ammeter, your wires, whatever you've got in there. And sure, you're measuring the exact voltage, but that's no consolation if you actually wanted a performance curve with a fixed known input voltage, which is generally what you'd want.

**Dave Jones:** You don't want it to change. So, uh um really you need to tweak your supply so that uh so that you're taking into account the burden voltage of your multimeter, and you could use something like a microcurrent, for example, but uh yeah, you've still got It's still going to change.

**Dave Jones:** Uh you're going to get some loss across there. So, just watch out for that. You may have to tweak the uh power supply each time. So, this is where an automated uh setup helps.

**Dave Jones:** If you've got an automated uh power supply that has remote sensing like this, you can program it so to provide exactly 12 V on the input here as well as measuring the current.

**Dave Jones:** It can do all that. But, because we're using uh just manual multimeters, manual instruments like this, yeah, and we can have a look at the effect here of the burden voltage.

**Dave Jones:** You've got the input current here. Okay, I'm using my 10 amp uh current shunt range here. So, the burden voltage is really low, okay? So, it's It's the power supply's outputting 5 V.

**Dave Jones:** We're actually measuring the input here at 4.8, but if we actually want more precision on our current here, we switch over to our uh milliamp range, which has going to have a much higher burden voltage.

**Dave Jones:** And wow, look at it now. It The input voltage power supply is still outputting 5 V, but the input to our actual module, which is what we care about, is dropped down to like 4.1 V.

**Dave Jones:** And yeah, the input current. So, yeah, we can get the input power and the output power. That's still fine, but our input voltage is varying, and that's generally a variable we do not want to vary.

**Dave Jones:** Variable. In that case, variable's the wrong term. We want a fixed input voltage, a known input voltage. That's what DC-to-DC converters are typically specified at. So, as we start to record our values like this, I might start at the highest current.

**Dave Jones:** It doesn't matter. Lowest, highest, doesn't matter what it is. And we're going to do it in decades. So, we might go 100 milliamps in 10 milliamp steps down to 1 milliamp, and then we'll go under that.

**Dave Jones:** We'll go 900 microamps, 800 microamps, etc. down in decades cuz we're going to get a decade graph. So, the two key parameters here are our output current, which we that is the x-axis of our graph, but we also want V in to be fixed.

**Dave Jones:** So, we're going to have to go tweak knobs over here. Tweak this with our tongue at the right angle to get our input voltage at our fixed 5 volts every time.

**Dave Jones:** So, yeah, it's you know, got to tweak a few things. Oh, well. It's not easy being green. And I show you that here. Even if we've got no output current meter, we're just relying on our drop on our wires here to get our 5 volts on our output here.

**Dave Jones:** I've had to tweak this up to 5.31 at our 0.1 amp 100 milliamp output current, which is the first one that we want to measure. And then if we change our output current to say you know, 20 20 milliamps or something, you'll notice that bingo, our input voltage has changed.

**Dave Jones:** So, we need to get in here and hold our tongue at the right angle, tweak our knob down until we get that input. So, you got to do that every time, but you know, by the time you automate this thing, it's not that hard.

**Dave Jones:** I mean, it takes seconds to do this when you're sitting down going bang bang bang bang bang. Right. So, I've gotten down to 10 milliamps, and basically I've reached the limits of measurement precision on my electronic load here.

**Dave Jones:** So, I'm going to use my Keithley 2400 source meter, my SMU, to actually set the output the sink current. Cuz you can use this this can source and sink current.

**Dave Jones:** In this case, I can set it to minus 1 milliamp, which means sink 1 milliamp of current instead of source 1 milliamp if I actually put that to plus 1 milliamp and it actually output current from here.

**Dave Jones:** If I set it to negative, it'll source it back in. But, most people are not going to have an SMU and if you do have an SMU, you probably don't need this tutorial.

**Dave Jones:** Now, I can measure with really decent precision. I set my compliance voltage to 13 volts just above what I'm uh expecting on the output here, otherwise it'll load it'll clamp the output and load it.

**Dave Jones:** And uh my I'm now sinking uh 1 milliamp here. I can put a current meter in series with that to verify that, but you generally just don't need that.

**Dave Jones:** And I can put a current meter in series with that to measure that I'm actually measuring 1 milliamp, but hey, it can do that for me. We can just go measure and it's actually this is what we've set um and this is what it's actually measuring.

**Dave Jones:** So, I can get really precise stuff. This is a real schmick bit of kit. Um so, yeah, we can easily go down to microamps and and measure with the utmost of precision.

**Dave Jones:** No worries, but I've still got to tweak the input uh to get my input voltage. Okay, I'm down at 100 microamps now, 0.1 milliamps uh output current and we're drawing 13.16 milliamps input.

**Dave Jones:** And if I actually disconnect the output, you'll notice that it doesn't drop down by not much. We're basically down to the quiescent current of our DC to DC converter.

**Dave Jones:** So, there's no point going another decade from 100 microamps down. Uh this particular uh DC DC converter is just not optimized for low currents. And if we plot our three and a half decades worth of data, bingo, look at what we've got here.

**Dave Jones:** Here's our characteristic curve for the Digilent 9-volt power brick, the efficiency versus the output current. Efficiency on the Y axis here from 0 to 100% and then the output current on a logarithmic uh graph, which is important.

**Dave Jones:** I'll explain that in a second. Uh from 0.1 uh milliamps or 100 microamps right up to in this case I went up to about 320 milliamps before the overcurrent protection actually uh kicked in.

**Dave Jones:** Now, uh granted, this DC to DC converter is only rated to 100 milliamps output, um but I went beyond that because I wanted to show you how it actually uh tails off there, otherwise it wouldn't have been very exciting, would it?

**Dave Jones:** So, all our data's over here, and it was easy to enter it in by hand. It takes bugger all time once you've got it uh written down. You know, if you had thousands of points, it would take you some time, but when you only got, you know, like 60, 70 points or something like I've got here, then it's bugger all, really.

**Dave Jones:** Um and the V in is always fixed at 5 V, you remember. I always kept I always tweaked that knob until we had a fixed 5 V input. And uh the input uh current, that's the one we actually uh measured.

**Dave Jones:** And the output voltage pretty much remained uh constant. There were a little few little changes there. And the output uh current, of course, was our fixed nominal output current we're dialing in with our electronic load.

**Dave Jones:** And then uh the power output, we just uh calculate that. It's uh the voltage times the current uh divided by uh 1,000 in this case to get milliamps instead of uh amps.

**Dave Jones:** And then our power output, of course, is just uh the output voltage times the output current uh time divided by 1,000 once again for milliamps. And then our efficiency is just our output power minus our input power times 100 to scale it to 100%.

**Dave Jones:** And also, we've got uh the That's not uh display, that's power dissipation there in watts. But this has given us now a great characteristic curve. Look at this. There's a nice little hump in there, that's because of the uh curve fitting algorithm that uh it's used.

**Dave Jones:** I can change that, doesn't matter. So, here's our data points here, and you'll notice that because it's a logarithmic scale, like between 10 milliamps and 20 milliamps here is a fair jump, and we don't actually have any data points.

**Dave Jones:** That's just cuz I I chose to do a a logarithmic data plot instead of a linear data measurement instead of a linear data measurement. So, you know, it just so happens in this case, due to bad luck that and Murphy, that the you know, all the interest in the interesting drop here in this curve is between 10 and 20 milliamps where we didn't actually take any data points like that, but it's

**Dave Jones:** going to be a fairly linear fit. You you're not suddenly going to suddenly say it go up to 90%. You know, efficiency curves always pretty much look like this.

**Dave Jones:** They might have a few little, you know, ripples in there, but nothing's going to suddenly, you know, at say 1 milliamp, it's not going to suddenly curve back up and go there unless it changes uh conduction uh mode, unless it changes the way from uh pulse width modulation to pulse frequency modulation.

**Dave Jones:** So, as a converter here, you can see, you know, from basically 20 milliamps up to its nominal rated 100 uh milliamps output current, it's not too shabby at all.

**Dave Jones:** It's above 80%, which is reasonable for a little uh brick converter like this. It's not the most efficient. It never gets over 90% at any point. So, it's not spectacular, but for a general purpose little power brick like this, it's okay.

**Dave Jones:** And by the way, remember this thing actually gives out uh plus 9 volts and minus 9 volts as well. I didn't load or didn't test the minus 9-volt output, so there's going to be some uh loss there.

**Dave Jones:** But under 20 milliamps, you can really see it drop off a brick wall here. And uh you know, even at 10 milliamps, it's 60% efficient. That's not great. And down at 1 milliamp, you might, you know, if you thought, "Oh, I'll just use this power brick to uh power my uh and to give me plus minus 9 volts for my uh you know, a little op amp that I need

**Dave Jones:** or something like that." You'll realize it's only going to be 15% efficient at 1 milliamp. It's just And it basically is like at 100 microamps, it's like, oh my god, it's ridiculous.

**Dave Jones:** It's not optimized for low current operation. So, in the tens of milliamps, that's where it's uh designed to operate. But anyway, there you go. We got that nice characteristic curve.

**Dave Jones:** But uh-huh, we're not done yet. You're saying, "Dave, we haven't plotted this uh power dissipation." Well, yes, I have. I've made the graph a little bit nicer and tada, here's our final graph that includes the power loss.

**Dave Jones:** So, this is this red curve here and we I've inserted another Y axis on the right-hand side here. So, I've got power loss from 0 to 1.8 W up here and on the and the same efficiency over here.

**Dave Jones:** So, I should have color-coded those if I was doing this properly. I would have color-coded the right ax- Y axis there uh orange and the other one over here blue and you know, anyway, you'd fuss around with that if you're putting it in some report for management or something like that.

**Dave Jones:** Not that they'd ever bloody read it anyway. Uh goodness, don't get me started. Anyway, so this is the power dissipated in the actual uh power brick itself. And you can see up to the 100 milliamp rated uh current, you can see why they don't rate it for anything more than that cuz after 100 milliamps, it really the power dissipation in this little tiny surface mount brick really starts to rise.

**Dave Jones:** So, it's only like in the order of uh you know, 0.2 W there, 200 mW at the nominal 100 mA output current. But as that efficiency drops down, the power loss must go up.

**Dave Jones:** You'll always see these things match. It's just, you know, basic math. You can't avoid it. And uh yeah, you don't want to be dissipating a watt, for example, um in this tiny little surface mount power brick.

**Dave Jones:** There's no heat sink on it. Uh what is a fair bit of power for that tiny little power brick. So, it's yeah, it worked on my bench here, but it's going to it's not going to continue to work at those sort of uh power dissipation levels.

**Dave Jones:** It's going to be, you know, die temperatures are going to be up to 100 plus degrees, and it'll soon fail. And sure enough, the overcurrent protection or overtemperature or whatever protection they've got inside this thing actually kicked in at 320 milliamps, even though it's only rated for 100 milliamps there.

**Dave Jones:** So, you know, so they're they're fairly safe there. They are They have rated that fairly safely at 100 odd milliamps. But maybe it could go a little bit more, but I certainly wouldn't go, you know, anything past maybe 150 milliamps there.

**Dave Jones:** But anyway, always stick to the specs. Don't go over them. Unless you want to live dangerously. And you'll notice that I've actually labeled this VIN equals 5 volts because as we you saw in some of those data sheet ones, they'll have different characteristic curves for different input voltages.

**Dave Jones:** And if we wanted to do that, well, we'd have to go through and re-log all our data again again for a different input voltage. That's where something like a more automated test jig would be very nice.

**Dave Jones:** And if you had an automated jig, yes, you could do much finer steps in there and measure much quickly and get, you know, much, you know, more data-filled graph.

**Dave Jones:** But this data's more than enough to get our characteristic curve. So, no problems there. But yeah, we could go in there and plot all sorts of parameters that vary on this.

**Dave Jones:** You could have this vary with output load capacitance, for example. So, you could have VIN equals 5 volts for and then have 10 different output capacitances or 10 different, you know, whatever versus load.

**Dave Jones:** And you can measure a multitude of different things. It depends what's important to you. So, anyway, there's our finished graph. It's beautiful. It's like a bought one. And by the way, if you're wondering how I got this logarithmic graph, you can't ordinarily do this.

**Dave Jones:** Let's go over to the Y axis here and actually format the Y axis, and if we go into scale, Y of course has a logarithmic scale. So, you can choose that, but we don't want a logarithmic scale for our Y.

**Dave Jones:** Okay? So, that's all in there. It's It's no problem. You just tick that. But, you can't do that for the X axis if you've got if you're using a standard line chart type.

**Dave Jones:** Now, it does actually work in this case. We can go in and format our X axis, and sure enough, it's got logarithmic scale. So, we can just switch off the logarithmic scale, and you could have it like that, but it that's not the traditional way to display these sorts of characteristic curves.

**Dave Jones:** They in traditionally use a decade-based logarithmic scale. And cuz you can see why, you know, all the interesting stuff is all just jammed, you know, right down here. Whereas, if you choose the logarithmic scale, then it's you know, it's it's much easier to see those sort of, you know, interesting changes.

**Dave Jones:** So, that's the point, but you can only do this if you actually using a certain chart type. You notice that I'm using an XY scatter chart type. You have to choose XY scatter.

**Dave Jones:** If you chose your regular line chart, and went in here like this, you'll find that there's actually no option in there. Look, you can you can reverse the direction of the data, which flips it side to side, but you can't get that logarithmic scale.

**Dave Jones:** The line chart by choosing a line chart type, which is what almost everyone for something like this, it assumes that you want a linear X axis. It doesn't give you the option.

**Dave Jones:** Anyway, that's in LibreOffice, I believe. I think it's the same in the OpenOffice, and probably in Excel. I haven't used Excel for a long, long time now. I've been using LibreOffice.

**Dave Jones:** But, yeah, that's just a trap. You have to actually choose that specific XY scatter mode. So, there you go. Little trap for young players. Anyway, that is it for logarithmic scale.

**Dave Jones:** Thank you very much. Look at that beautiful graph. So, I hope you enjoyed that. It's been like half an hour video, much longer than I intended, but that is a step-by-step process with lots of traps for young players in there of how to get a characteristic curve of a DC-to-DC converter, which you might have to do one day if you're designing your own or you've got one, in this case without the

**Dave Jones:** specs. And now, hey, we have an efficiency curve for it. You're welcome. Welcome. Digilent, feel free to use it. So, as always, if you like this video, please give it a big thumbs up and comment and engage and all that sort of wonderful business and discuss it in the comments, EEVblog forums, links down below, all that sort of jazz.

**Dave Jones:** Hope you liked it. Catch you next time.
