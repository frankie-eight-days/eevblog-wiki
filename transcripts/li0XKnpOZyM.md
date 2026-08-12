---
video_id: li0XKnpOZyM
title: EEVblog #957 - How To Measure DC-DC Converter Efficiency
url: https://www.youtube.com/watch?v=li0XKnpOZyM
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 30, "3": 48, "4": 63, "5": 79, "6": 94, "7": 109, "8": 125, "9": 137, "10": 149, "11": 162, "12": 177, "13": 192, "14": 210, "15": 226, "16": 240, "17": 253, "18": 266, "19": 281, "20": 302, "21": 319, "22": 334, "23": 354, "24": 371, "25": 383, "26": 400, "27": 417, "28": 432, "29": 447, "30": 460, "31": 474, "32": 487, "33": 504, "34": 519, "35": 535, "36": 550, "37": 561, "38": 576, "39": 592, "40": 606, "41": 618, "42": 631, "43": 645, "44": 656, "45": 672, "46": 685, "47": 703, "48": 717, "49": 729, "50": 744, "51": 757, "52": 769, "53": 784, "54": 798, "55": 811, "56": 824, "57": 836, "58": 851, "59": 865, "60": 878, "61": 894, "62": 906, "63": 920, "64": 933, "65": 946, "66": 960, "67": 974, "68": 988, "69": 1002, "70": 1017, "71": 1033, "72": 1046, "73": 1061, "74": 1075, "75": 1088, "76": 1103, "77": 1117, "78": 1129, "79": 1145, "80": 1158, "81": 1172, "82": 1185, "83": 1197, "84": 1212, "85": 1230, "86": 1243, "87": 1256, "88": 1271, "89": 1286, "90": 1297, "91": 1309, "92": 1323, "93": 1338, "94": 1351, "95": 1367, "96": 1379, "97": 1393, "98": 1407, "99": 1419, "100": 1434, "101": 1449, "102": 1463, "103": 1478, "104": 1491, "105": 1503, "106": 1516, "107": 1532, "108": 1545, "109": 1557, "110": 1572, "111": 1586, "112": 1600, "113": 1613, "114": 1624, "115": 1638, "116": 1653, "117": 1666, "118": 1678, "119": 1695, "120": 1709, "121": 1721, "122": 1734, "123": 1749, "124": 1759, "125": 1777, "126": 1793, "127": 1807, "128": 1821, "129": 1833, "130": 1848, "131": 1861, "132": 1874}
---

**Dave Jones:** Hi, let's say you've got a DC-to-DC converter that you want to measure the performance of whether or not you've designed it yourself into a particular product or you've bought maybe an off-the-shelf one like this which doesn't provide any characteristic

**Dave Jones:** graphs performance graphs and efficiency graphs for it. So, how do you actually measure the performance of a DC-to-DC converter and get your typical efficiency curve which is the efficiency in percentage versus the output current draw? And you'll find this in

**Dave Jones:** practically every data sheet for every DC-to-DC converter chip on the market and these are usually typical, but but the actual efficiency of your particular DC-to-DC converter that you design is dependent upon a whole host of things what type and what size inductor you've

**Dave Jones:** got, output capacitance, if you've got an external switching MOSFET, what type that is, and all sorts of and the frequency you operate at, all sorts of different parameters go into determine the efficiency of a DC-to-DC converter. And sometimes this efficiency

**Dave Jones:** characteristic graph will also include power loss as well which is quite typical cuz you want to know how much power's being dissipated in your little brick converter here. So, how do you actually measure and graph your own characteristic curve like this? Well,

**Dave Jones:** let's take a look at it. I've actually kind of done this in several old much older previous videos, but not a dedicated video for it. So, let's have a look in the case little Digi-Lint 12-V power brick here, it's a

**Dave Jones:** boost converter, 5 V into 12 V out. Data sheet doesn't have the efficiency curves. Let's measure it. The efficiency of a DC-to-DC converter is just the output power divided by the input power. If the output power exactly matches the input

**Dave Jones:** power, i.e. you get 1 W out for 1 W in, then it's a 100% efficient converter which is basically impossible. Uh you can't get a 100% efficient DC to DC uh converter. A typical really well-designed, good DC to DC converter

**Dave Jones:** will typically have an efficiency greater than 90%, you know, a real kick-ass one might be like 95%. So, you're going to have some loss in the converter here. So, what we need to do is measure the input power going in and

**Dave Jones:** the output power. So, we need a power supply and we need an electronic load. I've done a whole video on making your own electronic uh load, very popular do-it-yourself uh project. So, I'll link that in down below. If you haven't seen

**Dave Jones:** it, you can make it for using junk bin parts for practically uh nothing. But, we need to get the input power and the output power. So, we can actually do that with these two instruments here. So, we've got a modern smart uh lab

**Dave Jones:** bench power supply here. This is a Rigol DP832 and it uh shows our input voltage and our input current, 5 V, 140 mA, and it automatically calculates our input power for us, so we don't have to uh calculate that with our calculator

**Dave Jones:** later. Beauty. So, basically, the input power here is 0.7 W and on our output, we've got our electronic uh load. A modern one like this can easily uh accurately measure the output voltage and the uh output uh current as well

**Dave Jones:** here and it also calculates your output power. So, I'll set a constant current output load here of of 50 mA, 0.05 A, and our output power is 0.59 W. So, 0.59 W / 0.7 W input here gives us an efficiency

**Dave Jones:** around about 84%. That's okay. But, if you remember that efficiency curve that we want, it's efficiency on the Y axis versus output current on the X axis. So, we have to sweep the output current here, set different loads, and get all

**Dave Jones:** the data points for the efficiency, so that divided by that for different values of load current here. And we have to do that over an extremely wide range of output currents. It can typically for a, you know, a universal

**Dave Jones:** type DC-to-DC converter, the data sheets, as an example here, will show typically 10 microamps up to an amp, for example, and they'll do that on a logarithmic graph because otherwise you can't fit it all in. But, aha, there's a

**Dave Jones:** big trap for young players here and I've mentioned this in many previous videos, but it's very important in this scenario, so I'll go over it again. You'll notice how our power supply on our input here is showing nice precise

**Dave Jones:** 5.000 V. It's a real accurate power supply, so you can believe it. But, that's 5 V sensed right at the output terminals here. We've actually got these wires going over to the breadboard here. Now, I've actually got another

**Dave Jones:** multimeter set up that's actually probing directly on the input pin there, okay? So, it's actually after the drop in all in the in the wires here, okay? So, the ground and the input. And, bingo, look, 4.66 V at the input to the converter. So, our

**Dave Jones:** 5 V is way off there, right? So, we've got a real large, very significant error there due to the drop in our wires. Whoa, lucky we actually measured it right at the input. And likewise, we're going to get a similar error on our

**Dave Jones:** output here because we've got these long wires going over. They're you know, they're reasonably thin wires, they're long, there's going to be some drop on those at a significant current. We're only drawing 80 milliamps, but hey, look at the error here, okay? We've got our

**Dave Jones:** nice precision supply here. Look at this, 11.7737. And this is a this is a really kick-ass electronic load, 0.05% precision, fantastic. But, it's it at the output terminals here. So, it's including the drop along these wires. We don't want that. We're

**Dave Jones:** measuring the efficiency of the converter, not the converter plus the input and the output wires here. And once again, look at the discrepancy here. I've got a meter on the directly connected to the output pin and the output ground there. And you can

**Dave Jones:** do this because there's a 10 megaohm input impedance on your multimeter, so it's drawing no current through any of these leads. So, you are actually measuring the true voltage on the output there. You're sensing it. This is called

**Dave Jones:** a four-wire sense measurement. And look at the discrepancy. It's This converter is actually outputting 12.13 V, but the our load is only measuring 11.8. So, we've got a discrepancy here, very significant, and a very significant discrepancy on the output. So, if we

**Dave Jones:** just use these two instruments and didn't do four-wire terminal measurement, but we can get very significant errors, which would completely ruin our efficiency curve. So, real trap for young players. Beware. Make sure you do four-terminal measurement. So, a simple Dave CAD

**Dave Jones:** drawing showing you four-terminal or four-wire measurement, sometimes called a four-wire sense measurement, whatever you want to call it. We've got our DC-to-DC converter brick here, our input and our output. The ground, just assume that the ground is the same, one common

**Dave Jones:** pin, whatever it happens to be. And you see that we've got voltage sensing right at the input pin there and right at the output pin there for both the output, for the positive in and positive out, and also the grounds as well, because

**Dave Jones:** you're going to get losses in both your ground wiring and your positive wiring as well on both input and output. And and then your ammeter, your current meter goes after that. So, then you've got your variable load over here. It can

**Dave Jones:** be a dummy resistor, electronic load, doesn't matter what it is, and your input ammeter here, and your adjustable power supply here. So, you don't want to read the value on your power supply here. You want to read the value on your

**Dave Jones:** voltmeter here. Unless you're working at very low current, in which case you're not going to get any loss across your wires, but just assume that you're going to get losses, and you need to measure using the four-terminal technique. This

**Dave Jones:** is why it's called four-wire or four-terminal, because there's one, two, three, four wires for each measurement point. And of course, you don't need fancy gear like a a modern programmable power supply to display power, or a really, you know, high-end precision

**Dave Jones:** electronic load like this. All you need is four multimeters. And I said it before, I'll say it again, this is a classic example why any well-equipped electronics lab should have four multimeters. It's not hoarding, it's not a multimeter fetish, it's to measure

**Dave Jones:** input power and output power of a basic DC-to-DC converter power supply. Very common in any electronics lab to do this. If you haven't got four meters, you can do it, but it's a pain in the butt. So, all you need is any lab power

**Dave Jones:** supply, and you don't have to worry about the voltage and current readings. Doesn't matter, it doesn't have to be fancy pantsy, just any supply will do. Two meters measure input voltage and input current, and output voltage and output current. And the good thing about

**Dave Jones:** this, we will actually have to resort to this, because if you have a look at the efficiency curve again, you'll notice that it went down to 10 microamps, okay? Right up to an amp. And if we have a

**Dave Jones:** look at, you know, a really good lab electronic load like this, it's only got 1 milliamp precision here, only two digits on the output power. It's bugger all. So, you know, we can't we can use this for, you know, large output

**Dave Jones:** currents, and the voltmeter is very precise. So, that's no worries whatsoever. Um but the but setting our load current is no good. Okay? So, we need something else to actually generate the very low loads, the 10 microamps and stuff like that. We

**Dave Jones:** at least need to be able to measure it with our with a separate output current meter that can measure those low currents precisely. This particular thing can't do it. So, yeah, I can just use a resi- stor. Something like that.

**Dave Jones:** We know the output voltage roughly 12 volts. We can just whack a resistor in there and get our 10 microamps on the output. Just use Ohm's law. Very simple. And really good quality electronic loads know all about four-terminal measurement

**Dave Jones:** and remote sensing. And it's got a remote sense option. There's some sense terminals on the back. Sometimes they might be on the front. This time it's screw terminals on the back and we can just select our remote sense on.

**Dave Jones:** Fantastic. And if we go back out and bingo, this now matches our meter. Well, our resolution's not there, but yeah, it basically matches cuz we're now doing four-terminal measurement with our electronic load. And another thing to be aware of, in this case I'm just

**Dave Jones:** measuring on a breadboard. It's a little bit dicky in here. And if you muck around with the wiring and stuff like that, things can start to change, you know, dicky contacts on breadboards and wires and stuff like that. If I was

**Dave Jones:** doing this properly and professionally, I would actually sacrifice this thing and actually solder the wires directly on four wires on the input and four wires on the output directly on the terminals. So, then nothing can go dicky with your measurements. And along with

**Dave Jones:** your efficiency, if you want to, you can measure other parameters well. Like you might measure the switching frequency, for example. You'll get that by typically probing the inductor in there. Depends on the converter you're using. And you can have

**Dave Jones:** a look at the switching frequency because your switching frequency, it might be a converter type that's the switching frequency changes depending on the output power and this will fairly typically happen with converters that want to get maximum efficiency across like at very low

**Dave Jones:** currents as well. So, that's you know, it's not uncommon. A lot of DC-DC converters are fixed frequency but a lot of them will actually change their frequency to make them more efficient over a larger output current range. And you might want

**Dave Jones:** to measure temperature for example. So, you might actually get in there and attach a little thermocouple probe to your converter or near your converter or whatever. Maybe on if it's using a heat sink you might attach it to the heat

**Dave Jones:** sink or something like that and you can plot temperature versus your efficiency and output and load dissipation as well. Just you know, if you want to be thorough. And that could be a big deal because hey, your converter might work.

**Dave Jones:** No worries. It's ambient temperature or whatever. Everything works just fine in the lab. It gives you the efficiency you want. It gives you the output power you want. But if it's running at 100° C you could be in trouble. You could come

**Dave Jones:** a gutser and it's not going to work in the field. It's not going to you know, have a long lifespan whatever. So, you know, you might want to measure something like temperature as well and plot that along with your efficiency.

**Dave Jones:** But we won't do that today. Now, you could actually automate all this of course. of modern instrumentation is all ethernet LXI controlled. For example, this power supply is this BK Precision one can be remotely controlled as well. So, I could actually script this to

**Dave Jones:** generate different output voltages and stuff like that. But hey, we don't have four terminal measurement on here but I could hook up some data logging well, some ethernet LXI connected bench multimeters that I have. You could automate the whole thing. You could

**Dave Jones:** spend like a whole day just setting this up. It's easier just to hook four multimeters on the input and output and increase your current and just note them down on a notepad and then just whack them into a spreadsheet. So, you know,

**Dave Jones:** it's you'd only automate this if you really wanted to just for kicks or you had a lot of converters to measure. And you can use some more advanced instruments like say this Keithley 2400 source meter or shmoo SMU. For example,

**Dave Jones:** you might have like a multi-channel SMU system for a real complex measurement. But as I said, you don't need any of this. You can get away with just a couple of multimeters and a dodgy power supply. And a do-it-yourself electronic

**Dave Jones:** load. And other stuff like output ripple voltage might be important for example or versus output capacitance. There's many other different parameters that you can do to measure a DC to DC converter. It's almost the sky's the limit. Now,

**Dave Jones:** when we actually go to measure this, if we take a look at our little diagram again, the burden voltage on our current meter on our ammeter on the output here is basically not going to matter as long as we've dialed in the

**Dave Jones:** load to get our output current. So, if it's an active load, it's going to sync that. But if it's a resistive load, then you're going to have to tweak it depending upon your burden voltage here. Likewise on the

**Dave Jones:** input, the you might think that the burden voltage here ammeter doesn't matter because you're measuring the input voltage here and that might be true. But generally, you want to your performance curve for your DC to DC converter is at a known input voltage.

**Dave Jones:** So, it might be 5 volts DC input. So, you don't want it to vary based on the current because as you decrease your load, you draw more current on the output, you're going to draw proportionally more current from the

**Dave Jones:** input here. You're going to get extra losses across your burden voltage or your ammeter, your wires, whatever you've got in there. And sure, you're measuring the exact voltage, but that's no consolation if you actually wanted a performance curve with a fixed known

**Dave Jones:** input voltage, which is generally what you'd want. You don't want it to change. So, uh um really you need to tweak your supply so that uh so that you're taking into account the burden voltage of your multimeter, and you could use something like a

**Dave Jones:** microcurrent, for example, but uh yeah, you've still got It's still going to change. Uh you're going to get some loss across there. So, just watch out for that. You may have to tweak the uh power supply each time. So,

**Dave Jones:** this is where an automated uh setup helps. If you've got an automated uh power supply that has remote sensing like this, you can program it so to provide exactly 12 V on the input here as well as measuring the current. It can

**Dave Jones:** do all that. But, because we're using uh just manual multimeters, manual instruments like this, yeah, and we can have a look at the effect here of the burden voltage. You've got the input current here. Okay, I'm using my 10 amp

**Dave Jones:** uh current shunt range here. So, the burden voltage is really low, okay? So, it's It's the power supply's outputting 5 V. We're actually measuring the input here at 4.8, but if we actually want more precision on our current here, we

**Dave Jones:** switch over to our uh milliamp range, which has going to have a much higher burden voltage. And wow, look at it now. It The input voltage power supply is still outputting 5 V, but the input to our actual module,

**Dave Jones:** which is what we care about, is dropped down to like 4.1 V. And yeah, the input current. So, yeah, we can get the input power and the output power. That's still fine, but our input voltage is varying, and that's generally a

**Dave Jones:** variable we do not want to vary. Variable. In that case, variable's the wrong term. We want a fixed input voltage, a known input voltage. That's what DC-to-DC converters are typically specified at. So, as we start to record our values like this, I might start at

**Dave Jones:** the highest current. It doesn't matter. Lowest, highest, doesn't matter what it is. And we're going to do it in decades. So, we might go 100 milliamps in 10 milliamp steps down to 1 milliamp, and then we'll go under that. We'll go

**Dave Jones:** 900 microamps, 800 microamps, etc. down in decades cuz we're going to get a decade graph. So, the two key parameters here are our output current, which we that is the x-axis of our graph, but we also want V in to be fixed. So, we're

**Dave Jones:** going to have to go tweak knobs over here. Tweak this with our tongue at the right angle to get our input voltage at our fixed 5 volts every time. So, yeah, it's you know, got to tweak a few

**Dave Jones:** things. Oh, well. It's not easy being green. And I show you that here. Even if we've got no output current meter, we're just relying on our drop on our wires here to get our 5 volts on our output here. I've had to

**Dave Jones:** tweak this up to 5.31 at our 0.1 amp 100 milliamp output current, which is the first one that we want to measure. And then if we change our output current to say you know, 20 20 milliamps or something, you'll notice

**Dave Jones:** that bingo, our input voltage has changed. So, we need to get in here and hold our tongue at the right angle, tweak our knob down until we get that input. So, you got to do that every time, but you know, by the time

**Dave Jones:** you automate this thing, it's not that hard. I mean, it takes seconds to do this when you're sitting down going bang bang bang bang bang. Right. So, I've gotten down to 10 milliamps, and basically I've reached the limits of

**Dave Jones:** measurement precision on my electronic load here. So, I'm going to use my Keithley 2400 source meter, my SMU, to actually set the output the sink current. Cuz you can use this this can source and sink current. In this case, I

**Dave Jones:** can set it to minus 1 milliamp, which means sink 1 milliamp of current instead of source 1 milliamp if I actually put that to plus 1 milliamp and it actually output current from here. If I set it to

**Dave Jones:** negative, it'll source it back in. But, most people are not going to have an SMU and if you do have an SMU, you probably don't need this tutorial. Now, I can measure with really decent precision. I set my compliance voltage to 13 volts

**Dave Jones:** just above what I'm uh expecting on the output here, otherwise it'll load it'll clamp the output and load it. And uh my I'm now sinking uh 1 milliamp here. I can put a current meter in series with that to verify that, but you generally

**Dave Jones:** just don't need that. And I can put a current meter in series with that to measure that I'm actually measuring 1 milliamp, but hey, it can do that for me. We can just go measure and it's actually this is what we've set um and

**Dave Jones:** this is what it's actually measuring. So, I can get really precise stuff. This is a real schmick bit of kit. Um so, yeah, we can easily go down to microamps and and measure with the utmost of precision. No worries, but I've still

**Dave Jones:** got to tweak the input uh to get my input voltage. Okay, I'm down at 100 microamps now, 0.1 milliamps uh output current and we're drawing 13.16 milliamps input. And if I actually disconnect the output, you'll notice that it doesn't drop down by not much.

**Dave Jones:** We're basically down to the quiescent current of our DC to DC converter. So, there's no point going another decade from 100 microamps down. Uh this particular uh DC DC converter is just not optimized for low currents. And if

**Dave Jones:** we plot our three and a half decades worth of data, bingo, look at what we've got here. Here's our characteristic curve for the Digilent 9-volt power brick, the efficiency versus the output current. Efficiency on the Y axis here

**Dave Jones:** from 0 to 100% and then the output current on a logarithmic uh graph, which is important. I'll explain that in a second. Uh from 0.1 uh milliamps or 100 microamps right up to in this case I went up to about 320 milliamps before

**Dave Jones:** the overcurrent protection actually uh kicked in. Now, uh granted, this DC to DC converter is only rated to 100 milliamps output, um but I went beyond that because I wanted to show you how it actually uh tails off there, otherwise it wouldn't

**Dave Jones:** have been very exciting, would it? So, all our data's over here, and it was easy to enter it in by hand. It takes bugger all time once you've got it uh written down. You know, if you had thousands of points, it would take you

**Dave Jones:** some time, but when you only got, you know, like 60, 70 points or something like I've got here, then it's bugger all, really. Um and the V in is always fixed at 5 V, you remember. I always kept I always

**Dave Jones:** tweaked that knob until we had a fixed 5 V input. And uh the input uh current, that's the one we actually uh measured. And the output voltage pretty much remained uh constant. There were a little few little changes there. And the

**Dave Jones:** output uh current, of course, was our fixed nominal output current we're dialing in with our electronic load. And then uh the power output, we just uh calculate that. It's uh the voltage times the current uh divided by uh 1,000

**Dave Jones:** in this case to get milliamps instead of uh amps. And then our power output, of course, is just uh the output voltage times the output current uh time divided by 1,000 once again for milliamps. And then our efficiency is just our output

**Dave Jones:** power minus our input power times 100 to scale it to 100%. And also, we've got uh the That's not uh display, that's power dissipation there in watts. But this has given us now a great characteristic curve. Look at this. There's a nice

**Dave Jones:** little hump in there, that's because of the uh curve fitting algorithm that uh it's used. I can change that, doesn't matter. So, here's our data points here, and you'll notice that because it's a logarithmic scale, like between 10

**Dave Jones:** milliamps and 20 milliamps here is a fair jump, and we don't actually have any data points. That's just cuz I I chose to do a a logarithmic data plot instead of a linear data measurement instead of a linear data

**Dave Jones:** measurement. So, you know, it just so happens in this case, due to bad luck that and Murphy, that the you know, all the interest in the interesting drop here in this curve is between 10 and 20 milliamps where we didn't actually take

**Dave Jones:** any data points like that, but it's going to be a fairly linear fit. You you're not suddenly going to suddenly say it go up to 90%. You know, efficiency curves always pretty much look like this. They might have a few little, you

**Dave Jones:** know, ripples in there, but nothing's going to suddenly, you know, at say 1 milliamp, it's not going to suddenly curve back up and go there unless it changes uh conduction uh mode, unless it changes the way from uh pulse width modulation

**Dave Jones:** to pulse frequency modulation. So, as a converter here, you can see, you know, from basically 20 milliamps up to its nominal rated 100 uh milliamps output current, it's not too shabby at all. It's above 80%, which is reasonable for

**Dave Jones:** a little uh brick converter like this. It's not the most efficient. It never gets over 90% at any point. So, it's not spectacular, but for a general purpose little power brick like this, it's okay. And by the way, remember this

**Dave Jones:** thing actually gives out uh plus 9 volts and minus 9 volts as well. I didn't load or didn't test the minus 9-volt output, so there's going to be some uh loss there. But under 20 milliamps, you can really see it drop off a brick wall

**Dave Jones:** here. And uh you know, even at 10 milliamps, it's 60% efficient. That's not great. And down at 1 milliamp, you might, you know, if you thought, "Oh, I'll just use this power brick to uh power my uh and to give me plus minus 9

**Dave Jones:** volts for my uh you know, a little op amp that I need or something like that." You'll realize it's only going to be 15% efficient at 1 milliamp. It's just And it basically is like at 100 microamps, it's like, oh my

**Dave Jones:** god, it's ridiculous. It's not optimized for low current operation. So, in the tens of milliamps, that's where it's uh designed to operate. But anyway, there you go. We got that nice characteristic curve. But uh-huh, we're not done yet.

**Dave Jones:** You're saying, "Dave, we haven't plotted this uh power dissipation." Well, yes, I have. I've made the graph a little bit nicer and tada, here's our final graph that includes the power loss. So, this is this red curve here and we I've inserted

**Dave Jones:** another Y axis on the right-hand side here. So, I've got power loss from 0 to 1.8 W up here and on the and the same efficiency over here. So, I should have color-coded those if I was doing this

**Dave Jones:** properly. I would have color-coded the right ax- Y axis there uh orange and the other one over here blue and you know, anyway, you'd fuss around with that if you're putting it in some report for management or something like that. Not

**Dave Jones:** that they'd ever bloody read it anyway. Uh goodness, don't get me started. Anyway, so this is the power dissipated in the actual uh power brick itself. And you can see up to the 100 milliamp rated uh current, you can see why they don't

**Dave Jones:** rate it for anything more than that cuz after 100 milliamps, it really the power dissipation in this little tiny surface mount brick really starts to rise. So, it's only like in the order of uh you know, 0.2 W

**Dave Jones:** there, 200 mW at the nominal 100 mA output current. But as that efficiency drops down, the power loss must go up. You'll always see these things match. It's just, you know, basic math. You can't avoid it. And uh yeah, you don't

**Dave Jones:** want to be dissipating a watt, for example, um in this tiny little surface mount power brick. There's no heat sink on it. Uh what is a fair bit of power for that tiny little power brick. So, it's yeah, it worked on my bench here,

**Dave Jones:** but it's going to it's not going to continue to work at those sort of uh power dissipation levels. It's going to be, you know, die temperatures are going to be up to 100 plus degrees, and it'll soon fail. And sure enough, the

**Dave Jones:** overcurrent protection or overtemperature or whatever protection they've got inside this thing actually kicked in at 320 milliamps, even though it's only rated for 100 milliamps there. So, you know, so they're they're fairly safe there. They are They have rated

**Dave Jones:** that fairly safely at 100 odd milliamps. But maybe it could go a little bit more, but I certainly wouldn't go, you know, anything past maybe 150 milliamps there. But anyway, always stick to the specs. Don't go over them.

**Dave Jones:** Unless you want to live dangerously. And you'll notice that I've actually labeled this VIN equals 5 volts because as we you saw in some of those data sheet ones, they'll have different characteristic curves for different input voltages. And if we wanted to do

**Dave Jones:** that, well, we'd have to go through and re-log all our data again again for a different input voltage. That's where something like a more automated test jig would be very nice. And if you had an automated jig, yes, you could do much

**Dave Jones:** finer steps in there and measure much quickly and get, you know, much, you know, more data-filled graph. But this data's more than enough to get our characteristic curve. So, no problems there. But yeah, we could go in there and plot all sorts of parameters

**Dave Jones:** that vary on this. You could have this vary with output load capacitance, for example. So, you could have VIN equals 5 volts for and then have 10 different output capacitances or 10 different, you know, whatever versus load. And you can

**Dave Jones:** measure a multitude of different things. It depends what's important to you. So, anyway, there's our finished graph. It's beautiful. It's like a bought one. And by the way, if you're wondering how I got this logarithmic graph, you can't

**Dave Jones:** ordinarily do this. Let's go over to the Y axis here and actually format the Y axis, and if we go into scale, Y of course has a logarithmic scale. So, you can choose that, but we don't want a

**Dave Jones:** logarithmic scale for our Y. Okay? So, that's all in there. It's It's no problem. You just tick that. But, you can't do that for the X axis if you've got if you're using a standard line chart type. Now, it does actually work

**Dave Jones:** in this case. We can go in and format our X axis, and sure enough, it's got logarithmic scale. So, we can just switch off the logarithmic scale, and you could have it like that, but it that's not the traditional way to

**Dave Jones:** display these sorts of characteristic curves. They in traditionally use a decade-based logarithmic scale. And cuz you can see why, you know, all the interesting stuff is all just jammed, you know, right down here. Whereas, if you choose the logarithmic scale, then

**Dave Jones:** it's you know, it's it's much easier to see those sort of, you know, interesting changes. So, that's the point, but you can only do this if you actually using a certain chart type. You notice that I'm using an XY scatter chart type.

**Dave Jones:** You have to choose XY scatter. If you chose your regular line chart, and went in here like this, you'll find that there's actually no option in there. Look, you can you can reverse the direction of the data, which flips it

**Dave Jones:** side to side, but you can't get that logarithmic scale. The line chart by choosing a line chart type, which is what almost everyone for something like this, it assumes that you want a linear X axis. It doesn't give you the option.

**Dave Jones:** Anyway, that's in LibreOffice, I believe. I think it's the same in the OpenOffice, and probably in Excel. I haven't used Excel for a long, long time now. I've been using LibreOffice. But, yeah, that's just a trap. You have

**Dave Jones:** to actually choose that specific XY scatter mode. So, there you go. Little trap for young players. Anyway, that is it for logarithmic scale. Thank you very much. Look at that beautiful graph. So, I hope you enjoyed that. It's

**Dave Jones:** been like half an hour video, much longer than I intended, but that is a step-by-step process with lots of traps for young players in there of how to get a characteristic curve of a DC-to-DC converter, which you might have to do

**Dave Jones:** one day if you're designing your own or you've got one, in this case without the specs. And now, hey, we have an efficiency curve for it. You're welcome. Welcome. Digilent, feel free to use it. So, as always, if you like this video,

**Dave Jones:** please give it a big thumbs up and comment and engage and all that sort of wonderful business and discuss it in the comments, EEVblog forums, links down below, all that sort of jazz. Hope you liked it. Catch you next time.
