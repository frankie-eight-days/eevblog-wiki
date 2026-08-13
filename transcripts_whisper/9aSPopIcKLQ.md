---
video_id: 9aSPopIcKLQ
title: EEVblog #664 - Peltier TEG Energy Harvesting Experiments
url: https://www.youtube.com/watch?v=9aSPopIcKLQ
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 16, "2": 30, "3": 51, "4": 69, "5": 91, "6": 111, "7": 125, "8": 142, "9": 156, "10": 174, "11": 193, "12": 214, "13": 232, "14": 254, "15": 269, "16": 288, "17": 304, "18": 324, "19": 340, "20": 357, "21": 371, "22": 391, "23": 406, "24": 424, "25": 437, "26": 455, "27": 473, "28": 488, "29": 508, "30": 524, "31": 544, "32": 560, "33": 574, "34": 594, "35": 612, "36": 626, "37": 649, "38": 669, "39": 686, "40": 701, "41": 719, "42": 732, "43": 748, "44": 763, "45": 782, "46": 801, "47": 818, "48": 836, "49": 848, "50": 867, "51": 887, "52": 901, "53": 919, "54": 936, "55": 952, "56": 969, "57": 983, "58": 1001, "59": 1021, "60": 1039, "61": 1057, "62": 1075, "63": 1090, "64": 1111, "65": 1129, "66": 1147, "67": 1165, "68": 1180, "69": 1195, "70": 1210, "71": 1222, "72": 1237, "73": 1252, "74": 1267, "75": 1282, "76": 1297, "77": 1309, "78": 1330, "79": 1351, "80": 1366, "81": 1384, "82": 1399, "83": 1414, "84": 1435, "85": 1450, "86": 1465, "87": 1480, "88": 1495, "89": 1507, "90": 1525, "91": 1543, "92": 1558, "93": 1573, "94": 1594, "95": 1609, "96": 1627, "97": 1642, "98": 1660, "99": 1678, "100": 1693, "101": 1714, "102": 1732, "103": 1753, "104": 1768, "105": 1783, "106": 1801, "107": 1819, "108": 1840, "109": 1861, "110": 1879, "111": 1900, "112": 1921, "113": 1936, "114": 1954, "115": 1969, "116": 1984, "117": 1999, "118": 2014, "119": 2026, "120": 2041, "121": 2056, "122": 2074, "123": 2089, "124": 2104, "125": 2119, "126": 2131, "127": 2143, "128": 2164, "129": 2179, "130": 2194, "131": 2212, "132": 2227, "133": 2242, "134": 2254, "135": 2269, "136": 2287, "137": 2305, "138": 2323, "139": 2341, "140": 2359, "141": 2371, "142": 2389, "143": 2407, "144": 2428, "145": 2457, "146": 2478, "147": 2502, "148": 2523, "149": 2541, "150": 2559, "151": 2580, "152": 2598, "153": 2616, "154": 2634, "155": 2649, "156": 2664, "157": 2682, "158": 2700, "159": 2718, "160": 2733, "161": 2748, "162": 2763, "163": 2778, "164": 2793, "165": 2811, "166": 2829, "167": 2847, "168": 2865, "169": 2883, "170": 2898, "171": 2913, "172": 2928, "173": 2949, "174": 2961, "175": 2976, "176": 2994, "177": 3012, "178": 3027, "179": 3042, "180": 3057, "181": 3075, "182": 3090, "183": 3111, "184": 3126, "185": 3147, "186": 3162, "187": 3180, "188": 3195, "189": 3210, "190": 3228, "191": 3240, "192": 3255, "193": 3264}
---

**Dave Jones:** Hi, we're going to take a quick look at some energy harvesting today, because I want to play around with a thermoelectric energy harvesting device, just to see how much power we can get out of them. It's only going to be a relatively quick experiment today,

**Dave Jones:** but anyway, I thought we'd take a look at that. And, of course, it brings up the subject of Peltier devices and the Seebeck effect. So I'll quickly go over what a Peltier device is that we're actually going to use today. You've probably no doubt heard of them.

**Dave Jones:** Peltier devices are essentially solid-state heat pumps. So you apply a current through them, and you can actually heat up one side of them, or cool down, depending on which way around you go. And here's how they basically work, okay? They contain two ceramic substrates, like this top and bottom,

**Dave Jones:** with a metallized layer on them that have some conductive traces on them. And then wedged between there, we've got some semiconductor pellets in there. And these are made of bismuth telluride, and you can go look that up. There are other materials, but they're not that better at higher temperatures and things like that.

**Dave Jones:** But anyway, that's a common one for these sort of, you know, 0 to 100 degree C range Peltier devices like this. And these are little individually doped, N and P doped, semiconductor bismuth telluride pellets. And they're arranged like this, so the green ones there are the N type, the red ones are the P type.

**Dave Jones:** And then on the metallized ceramic substrate here, they have printed conductive traces, so you can actually put these in series, so you can join them together. And then they have matching ones on the top, and then they wedge them all down, and they form a big series chain of PN junctions.

**Dave Jones:** And then you've got two leads coming out, your positive and your negative lead here. And these are relatively low resistance, low impedance devices there. The one we're going to look at today is like 1.5 ohms or something like that, so relatively low impedance.

**Dave Jones:** So you apply a voltage to them, a current flows through, and we can actually transfer heat from one side to the other. Brilliant! So this is known as the Peltier effect, and we'll take a look here very quickly at what's happening here. Here's our bottom plate like this with the electrodes and our batteries hooking up.

**Dave Jones:** Let's just assume that we've only got one in there. In practice, there's like, you know, 50 or 100 of them in series in here. But let's just assume that we've got one. You apply a voltage, and of course current flows, because the top plate is electrically conductive,

**Dave Jones:** and you've basically got, and the bottom plate is electrically conductive, you've got a PN junction there, and if you bias it the right way, current flows through the thing. Now, the key to this is that they're all electrically series connected, but they're thermally connected in parallel.

**Dave Jones:** That's why they split them together. If you put the P on top of the N and then tried to get the heat to flow through, it wouldn't work. So this is why you have to thermally parallel them like this. So what happens is when a current flows through here like this, you get electron flow,

**Dave Jones:** then the heat is absorbed into this bottom panel here, and then it's released from this top panel, or vice versa, depending on which way around you actually have the voltage. And that's basically why it is a heat pump, because heat is pumped from one side, one plate, to the other plate.

**Dave Jones:** And that allows them to heat up things or cool down things relative to ambient or the other plate. And these devices are very useful and used in a lot of applications these days. One of the most common, of course, is these little, you know, tiny desktop fridges and things like that.

**Dave Jones:** You know, you can cool down your beer or whatever. They will typically use these Peltier devices. Usually a large amount of current's flowing through here, like tens of amps kind of stuff, and then you can get reasonably efficient heat pump transfer. And because it's a heat pump, for example, that's why you will have, say, this side here,

**Dave Jones:** the cool side of the device, the one that's absorbing the heat, that will be inside the thermal chamber or the little fridge that you've got. And then on the outside here, you'll have a big heat sink on the back of this thing, which will be ambient temperature.

**Dave Jones:** So when you apply current through, it absorbs the heat from inside your little fridge or your thermal chamber and extracts it to the outside. So the inside of your little fridge or thermal chamber cools down and outside heats up. That heat sink gets hot on the outside and it dissipates into free air.

**Dave Jones:** So that's Peltier devices, which actually we're not going to look at today. We're not going to apply voltage to these things and actually get them to heat up or cool down something. No, we're going to actually use the opposite effect, which is called the Seebeck effect.

**Dave Jones:** So what we're going to do is turn this Peltier module into what's effectively known as a Seebeck module. You can reverse the process. Instead of applying a voltage and current to it and heating or cooling something, we actually apply a thermal gradient, a temperature differential between one side and the other,

**Dave Jones:** and we can generate voltage out. And that's what we're going to get and use today. And so it effectively becomes a Seebeck module. And a lot of people mix up these terms when they're actually using them as thermoelectric generators, which is what we're going to look at.

**Dave Jones:** They often call them, you know, Peltier generators or something like that. Strictly, that's not correct. When you use it in the opposite mode of operation, it becomes a Seebeck module. So a Seebeck module is known as a thermoelectric generator or TEG, and that's how we're going to use it today as a generator.

**Dave Jones:** Now, before we go and take a look at an actual module, it's important to just grasp a little concept here, and that is what we're trying to do here. Yes, if the temperature on this plate here is different to this plate here, you will get a voltage out of there.

**Dave Jones:** And if the temperature differential changes like this, the polarity of the output will change as well. And, well, that's fine and dandy, voltage, but where does the current come from? The current comes from the actual heat, just like the heat pump. The current comes from the actual heat transfer through from one side to the other,

**Dave Jones:** because that heat contains energy. And if you want any sort of decent current out of this thing to actually power your device, then, well, you need to actually transfer heat from one side to the other. It's not good enough just to get a temperature differential.

**Dave Jones:** That's why if you just have the Seebeck module on its own, your thermoelectric generator module just sitting there like that, if you try and heat up one side, well, the other side will just quickly get to the same temperature, and, well, it's not really, and then it's going to equalize,

**Dave Jones:** and you will stop getting voltage and current out of this thing. So what you always see with these things is you've got to have a thermal mass on one side. So that's why today we're going to see a big heat sink on one side of this thing,

**Dave Jones:** which effectively keeps one plate here, well, in this case it might be this bottom plate, sort of like anchored, thermally anchored to the ambient temperature. It takes, you know, quite a lot of energy to heat up that heat sink. So when we actually touch the top plate here,

**Dave Jones:** then the bottom plate is being kept, or anchored, at that ambient room temperature so that we can actually get heat flowing through, and therefore that heat contains energy, and that will translate into current on the output. Just important to understand that little concept which, you know,

**Dave Jones:** people think it's just the temperature differential. Nope. Got to have the heat, and therefore energy, flowing through the device. And here's the kit we're going to take a look at today. You've seen it in the mail bag before. It comes from Wirth Electronic, and they're the ones who do the kit.

**Dave Jones:** If you want this demo board, you have to buy this kit. It's not sold separately. It is actually a linear technology demo board with a giant Gecko EFM arm processor demo board. So it's a combination. I mean, Wirth Electronic, they're the ones who sell a lot of these parts.

**Dave Jones:** So they've developed this kit as sort of a demonstration. They show you which Wirth product numbers and stuff are used on the modules and things like that. So it's a combination of, you know, various manufacturers and suppliers coming together. And you have to buy the whole kit.

**Dave Jones:** So yes, I'm pretty sure that you can't just buy this linear technology demo board on its own. It's the EHR multisource board. I will provide a link to the product page for this for the schematics and everything else. But basically, it's an energy harvesting demo kit using various linear technology parts.

**Dave Jones:** And it supports piezoelectric generation here, TEG or thermoelectric generation. So this is the one we're going to use today with the Peltier device on it, or the Seebeck module on it. And it's got solar cell generation as well, because there's a solar cell

**Dave Jones:** and there's our Peltier device which we'll take a look at. And it also has some energy storage on the back which we'll be using. These are 100 microfarad caps and all up there about 1500 microfarads or something like that, which we'll take a look at.

**Dave Jones:** But we're interested in this Peltier device hooked up as a Seebeck thermoelectric generator. And we're going to use this LTC part down here. And the whole idea of this energy harvesting board is that, and in your products as well, you can actually not only use, like, just the solar cell or just the thermoelectric generator

**Dave Jones:** or just the external piezoelectric generator which you hook onto here, piezoelectric device, you can actually combine all these different sources together to actually power your product. And that's not that uncommon in these energy harvesting applications. But I want to look at this for a certain application.

**Dave Jones:** We're only going to be looking at the thermoelectric generator here. Now it's already stuck onto the heat sink here, can't show you the other side, which probably has the part number on. But from the schematic, which I'll link in down below, I do know that this is from CUI,

**Dave Jones:** is the manufacturer, and the part number is CP85438. So I'll link in the data sheet for this Peltier device down below. And it's an 8.5 amp rated one, nominal 1.5 ohms series resistance, 80 degrees C maximum on the plate, and an overall maximum of 138 degrees C.

**Dave Jones:** If you go over that, you actually melt the solder joints inside. So yeah, this is not for high temperature applications, but, you know, just fine for, you know, most sort of those high ambient condition, you know, applications in electronics typically over that commercial temperature operating range.

**Dave Jones:** Now I explained before why this is on a heat sink. Because if it was just sitting on the board and we put our hand on there to actually heat up this one plate here, well, the heat energy would flow through the device and the bottom plate would heat up fairly quickly as well,

**Dave Jones:** and it would reach thermal equilibrium. And sure, we'll get a little bit of energy out of the thing, a little bit of current for, you know, a short amount of time until both plates reach thermal equilibrium. And then, well, it doesn't generate anymore

**Dave Jones:** because there's no temperature differential across the two surfaces here. So you need this big heat sink on the bottom, and this will be attached with thermal adhesive, by the way, so that, you know, there's good thermal contact between the bottom plate and the heat sink.

**Dave Jones:** And this effectively keeps it at, sort of, you know, anchors it for as long as possible. It will eventually heat up, but as long as possible at ambient temperature. So when we do put our hand on here, the heat flows through the device,

**Dave Jones:** we get a current out of the thing, and we can use that to, you know, charge our energy storage capacitors, run our board over here, and everything else. So let's try this, shall we? I've got the jumper set here to on, so the only thing that we've got is the thermoelectric generator hooked up.

**Dave Jones:** We can actually measure the output on these two test pins. These are just connected straight through to the two pins over there. And I will hook up some instruments and measure stuff later. I just want to see if it measures the board. And I can switch that capacitor bank on the back.

**Dave Jones:** It's already got 100 microfarads storage cap on there, but I'm actually hooking up the larger 1500 microfarads on the back there. So let's actually see if this thing can power up. So I'll put my hand on here. The heat sink is at ambient room temperature, of course.

**Dave Jones:** And bingo, look, it switched on. And the application built into this little Arm Gecko processor is just measuring the ambient temperature. There it is, 23.7 degrees Celsius. And I think we can switch through. Yeah, display it for you, Yanks. There we go. So that is the ambient temperature, just the temperature center of this board.

**Dave Jones:** It's not measuring the temperature of the heat sink or anything. Oh, there we go, the power's drooping. It's fading, it's fading. Quick, press harder, press harder. So there you go, it works. And, of course, if I take my hand off, there is some of that charge is stored in the capacitor bank on there.

**Dave Jones:** It will last and then eventually will fade out. So it works. But then again, this Arm Gecko microcontroller, we're only talking, you know, tens of microamps to sort of display that LCD there. You saw that in a previous video, actually. To do that, it probably takes like little pulses,

**Dave Jones:** one milliamp or something like that, to sort of power up, read the temperature sensor, and then, you know, for the process to fire up, read the temperature sensor, display on the LCD, and then shut back down and goes to sleep. And it probably does that like once a second.

**Dave Jones:** And that energy is coming, those little, the energy for those pulses, as you've seen in a previous video on integration and how to measure that on your oscilloscope, which I'll link in below. Check that out if you haven't seen it. They will come from the bypass capacitors

**Dave Jones:** on the output of the chip, as we'll take a look at on the circuit now. Now the chip we're actually looking at here is the linear technology LTC3108. And there's a couple of chips in the range. The 3109 is different again, which accepts thermoelectric generator of any polarity.

**Dave Jones:** So it's actually dual polarity input. So this is only the single polarity input, so we have to hook it up the right way and get the correct thermal differential between the plates. But if you do have an application where your temperature differential on the plates

**Dave Jones:** might go positive and negative, then you'd use the 3109. But anyway, this is a really nice chip designed exactly for this application to hook up to a thermoelectric generator and designed to operate at the really low levels that we're going to get out of these

**Dave Jones:** Seebeck or Peltier modules And when they're operating as a Seebeck device, we're typically only going to get out of these things, we're only going to get like, you know, tens of millivolts up to maybe hundreds of millivolts and that's about it, depending on the temperature differential

**Dave Jones:** and the, you know, the exact type of material used in there and how many, blah blah blah blah blah, and everything else, right? So, but essentially its output is proportional to the temperature difference between the plates on there. And this is the input over here

**Dave Jones:** and this shows the internal block diagram of the LTC3108, so let's take a look at it. So if we have a look at this part of the circuit I've drawn in red, this forms a resonant step-up oscillator because, of course, no, basically, no ordinary DC to DC converter

**Dave Jones:** can work down to the very low voltages like, you know, 20 millivolts or 10 or 20 millivolts or something like that out of this module. Well, this chip actually works with voltages, will start up and actually do the step-up DC to DC function

**Dave Jones:** with as little as 20 millivolts on the input. If you actually look at the spec, it could be as much as 50, but anyway, it's typically around 20 millivolts start-up. Absolutely incredible. So perfect and purpose-designed for this application. So what this transformer here and this MOSFET

**Dave Jones:** and this capacitor form is a resonant step-up oscillator which will depend, the frequency of operation depends upon the secondary value of the inductance in there and that will self-resonate and bootstrap and start up with as little as 20 millivolts across the input from our thermoelectric generator.

**Dave Jones:** Very nice. So when we've got an oscillator here, what can we do? Well, we can tap off that signal, AC-couple it, and that's what C1 here does. AC-couples it and then rectifies it to form a, and then filters it, that's a, you know, a basic single diode rectifier

**Dave Jones:** and filter there, and that will generate an internal voltage called Vox and that's what powers all the circuitry in here and then ultimately can, you know, power the internal regulator and do all sorts of goodness like that. And how we get voltage out of the thing.

**Dave Jones:** So once the voltage here is ramped up on this capacitor here, ramped up to a certain threshold, then these synchronous rectifier circuit here switches on to make this more efficient so, you know, you don't have a horrible voltage drop and power loss across that internal diode

**Dave Jones:** so that circuitry will kick in and activate and make the whole thing more efficient once it gets to a certain point. So you've got to have a reasonable size cap on here to do that. And actually once the Vox voltage on this pin

**Dave Jones:** reaches 2.5 volts, then the charge controller switches on and then V out here can start regulating at a programmable voltage which is set by these two program pins here and you can set it for 2.35 volts 3.3, 4.1 or 5 volts output. I think this one is set to 3.3

**Dave Jones:** today as a fixed voltage. So that works as a voltage regulator and you just feed your tens of millivolts or hundreds of millivolts in from your thermoelectric generator and bingo, you get out a regulated 3.3 or 5 volts. Fantastic. Now you'll notice that down here there's another

**Dave Jones:** low dropout regulator at a 2.2 volts this is a separate output which actually turns on quicker than the main output here so once this Vox voltage actually gets to 2.3 volts, then this LDO here will switch on so you can actually start up your

**Dave Jones:** processor first or something else before this main output here and this main output capacitor here charges up because remember we may not, this is energy harvesting by definition it's really ultra sort of low power so we're not going to get a huge amount of

**Dave Jones:** power out of this thing so it's going to take time for this output storage capacitor to charge up. I'll explain in a minute why you would have different values there but that could take some time to charge that up and then get to your

**Dave Jones:** programmed output voltage. It's not like a regular power supply where there's a ton of current to go through here and then just charge up your output bypass cap instantly. No, this thing can actually take some time so with this one powering up first

**Dave Jones:** that could allow you to charge up some circuitry and do some other housekeeping stuff before your main output switches on. Whether or not you use that depends on your application but it's there. And this output capacity here has to be a minimum of 2.2 microfarads

**Dave Jones:** because as you should be aware, low dropout regulators are inherently unstable so you need a minimum amount of output capacitance there and of course you don't want to make that too large because then you get into the same problem of here of this output

**Dave Jones:** capacitor of having to charge the thing up, etc. So you can have a really large value over here and a small value here of minimum 2.2 so this one can charge up quicker. So usually this value is going to be a lot lower than your one over here because you have to draw current

**Dave Jones:** spikes. So this one should power up quicker than this output here. And also we've got a separate voltage output here which has a MOSFET switch so you can actually feed an external signal to switch that off and on. Internal current limited to 300 milliamps

**Dave Jones:** so that could be handy for certain applications. And then we've got a power good output here which is an open drain logic output that allows to signal to microprocessors or anything else so you can hook an LED up to there. When the voltage output here gets

**Dave Jones:** to within 7.5% I think it is of its regulated output voltage and if it drops there, it's got some hysteresis on there, and if it drops below I think 9% of the output voltage then it'll switch off to indicate that your regulator power

**Dave Jones:** is no good. But yeah, it's not a close tolerance thing because these energy harvesting stuff, well, you kind of need, you know, as much power you can get for as long as possible. Now this is an interesting bit here. This MOSFET going over to

**Dave Jones:** the V store pin and a storage cap. Aha! This is where you can whack on a large amount of capacitance like a super cap or something like that, you know, you can whack on a one farad cap if you want to and you can

**Dave Jones:** accumulate and store energy from your thermoelectric generator from this internal ox bus in here which also supplies your output. You can also simultaneously charge up this storage capacitor. So like, you know, under normal conditions when you're generating enough power from your thermoelectric generator, you're powering your

**Dave Jones:** circuitry over here just fine, but if this input drops below this voltage this auxiliary voltage inside here, then the charge control will switch on this MOSFET and then it will draw current from the storage cap until such time as your thermoelectric generator can generate more power

**Dave Jones:** than that voltage. So it can account for all the times when your input actually drops out and you can just continue to power your product without problem until your storage cap has drained and then wah, game's over. Now here's where we came to this

**Dave Jones:** C out thing I talked about before. This energy storage cap here, this only charges and can deliver only a couple of milliamps back through. So if you're, if this input is dropped out and you're powering your circuitry on V out from your storage capacitor here,

**Dave Jones:** it can only supply a couple of milliamps tops. So if you've got something hooked onto here, like a typical application for these energy harvesting devices is like a little RF transmitter for example might turn on every minute or every second or every hour or once a day

**Dave Jones:** or something and send some data. Well, you know, a short burst of data. And that could require, you know, tens or hundreds of milliamps or something like that. And that cannot be provided from this storage cap. It can't do it. It's only limited to, you know, one or two,

**Dave Jones:** a couple of milliamps at most. So that's why you typically need, if you have got those short bursts of power requirements for like an RF transmitter, for example, then that, or just your actual processor itself, if it might draw 10 milliamps for example when it wakes up, this micro,

**Dave Jones:** you know, if it was running at full pelt and it was, you know, took maybe, I don't know, 10 milliamps because you're running the thing at 20 megahertz or something, and you do that and process something for like 10 milliseconds or something for example, then all of that pulse energy

**Dave Jones:** must come from this storage cap here. So that's why, if you've got those applications, you would have to size that cap accordingly to supply all that pulse current requirement. Well that's enough yapping, let's actually do some measurements. I was going to like jump straight into this.

**Dave Jones:** But at the last minute I decided to do the whiteboard thing and explain the chip and do, why not, you know, can't help myself, got a yap on. Anyway, got my Breiman 257 here, it's got 10 microvolts resolution here, it's got a 50 millivolt mode,

**Dave Jones:** very good, very handy for this sort of application. As you can see, we're getting basically bugger all out at the moment. It's connected across those two test pins, which as I said are directly across there. Now the loading of this thing, I don't know if this is

**Dave Jones:** offhand, if this is 10 megaohms or has a high impedance, but that's not going to matter, it's going to be NAF4. Same with the, having the generator actually hooked up to here, because this is a low impedance output. Wait! You saw it go up there!

**Dave Jones:** Look at that! This is a low impedance output, so having that on there is, you know, is not going to do anything. So we're getting the true voltage out of this thing. So if I touch that, look at that! We're getting 50, 60,

**Dave Jones:** yeah, 60, not a huge, not a huge amount there, so you know, the ambient here in the lab is like 22, 23 degrees, and I don't know what my hand is, it's probably you know, should be 37, around about there. So we're only getting 52 millivolts, but as I said,

**Dave Jones:** that is enough, the LCD is on again, that is enough to start this oscillator up and actually provide that output power. But how much current does this thing output? Well, you can do exactly the same thing as you do with solar cells, you can do a short circuit

**Dave Jones:** test. So we can actually hook this over here, it'll, yep, insertion error, blah blah blah, and we can actually hook that over to here, and it's going down, it's already generating, look, a couple of milliamps there as it cools down. So that's not too bad

**Dave Jones:** at all. So let's put our hand on there, look at that, we're generating, you know, 14 milliamps. That's pretty darn good. You know, you could power a LED from that, well, could you? No. The problem is, is that the voltage, of course, isn't there, we're only

**Dave Jones:** yeah, we might be getting, you know, 15 milliamps out of the thing, but there's just not that voltage there to actually power a LED on this thing. So that's why, you know, the LED threshold and all that, so that's why we need this step-up converter in here

**Dave Jones:** to generate a higher voltage, but at a proportionally lower current, of course. Now, what I've got here, I've hooked up my fluke across the storage capacitor in there, and we'll be able to see the charge on that capacitor slowly climb up. And of course, it should get to that full

**Dave Jones:** 2 point, that auxiliary voltage of what is it? 2.5 volts, or whatever it is internally to the regulator. So, but it'll take a lot of time, because it's 1500 microfarads. And of course, the voltage on this storage cap here is going to be

**Dave Jones:** no good unless we can actually reach that auxiliary, that internal auxiliary voltage. Because if you remember back here, this is the internal storage this is the capacitor storage voltage, and this is the internal auxiliary bus. And of course, that voltage can't be the 20 millivolts like we get

**Dave Jones:** from the input. That's why we have this step-up oscillator, step-up boost converter here on the input. So this storage cap is you know, it might be charged to 100 millivolts, but that's no good until it reaches the auxiliary voltage, the 2.3 or 2.5 volts required on this

**Dave Jones:** auxiliary voltage here to power the output. So at a minimum. So it has to charge up to that value until it becomes any good. And as you can see, with just my body heat on that top plate, jeez. That could take a while.

**Dave Jones:** Hmm. Extrapolate that. And here we go, we're quickly racing up look at this, I've put a large heatsink on here with some power resistors, and I'm just generating that, and look look at that, we're climbing right up there climbing right up, and then we should be able to keep

**Dave Jones:** the power going from that, from the storage element very shortly, because we're feeding, although look, check out the actual voltage isn't much, but the amount of heat energy being transferred through that is now so much that we can really charge up that storage cap quickly.

**Dave Jones:** There we go. Beautiful. You can see that's still climbing well, it's sort of, no, it looks like it's going to cap about there at about 5.2 volts internal. So now all that storage capacitance in there is now fully charged, so if we release this

**Dave Jones:** of course, then we can power our circuit for quite some time based on all of that charge storage in that capacitance. You can calculate your charge based on the total capacitance you have. You can see how this was much more efficient, even though this is not

**Dave Jones:** very warm, I think it's, I don't know, I can get a I can obviously keep my hand on this, no problems at all but it was able to transfer a lot more energy through, even though, look, our voltages bugger all is still, you know, not too much higher than what we were getting

**Dave Jones:** before, really, out of the thermoelectric generator, but it's able to supply a lot more current and hence charge up all the storage elements much better. So if we can take that off and we'll find that our device will, no, there we go, it's

**Dave Jones:** still taking some current. So you can see it dropping down, it's still working. So but it would have died by now when I did it with my hand before. Now it's completely under the dropout voltage of that voltage regulator OK, so there's basically nothing coming out of the thermoelectric

**Dave Jones:** generator anymore, so it's all operating from the storage capacitance in there, well, no, it's just faded out, once it got to, there we go, there's that 2.5 volt threshold voltage of your internal auxiliary voltage, it needs that to keep maintaining the V-out to keep maintaining that V-out that we saw here

**Dave Jones:** once, you've got to have at least 2.5 volts there really, so when you're calculating the energy stored in your storage capacitance on here, attached to there, then you've got to calculate not the discharge down to 0, but the discharge from that full 5.2 volts, yep, there it is

**Dave Jones:** 5.25, there's our limit in, there we go that's why it limits it to 5.25 we have ourselves a zener in there, which limits that so 5.25 volts maximum voltage down to 2.5 volts, so you can do the math on that to figure out how much

**Dave Jones:** energy is in a given storage capacitance and if we do that again, I've disconnected the 1500 microfarads, now I've only got 100 microfarads storage on there, let's ramp this sucker back up and it takes time for it to start charging, but it very quickly, you see

**Dave Jones:** how quickly that charged up to that 5.25 there, no problems whatsoever now if we release that, it'll won't power it for nearly as long as what that 1500 microfarads did of course, and it'll be gone right about now, there we go magic. And there you go, that heatsink

**Dave Jones:** there has absorbed some energy of course, as you'd expect so it's, you know, up over 30 degrees, I could leave it there and get better contact, yada yada, but you know, it's certainly like, you know, at least 5, 6, 7 degrees above ambient room temperature here

**Dave Jones:** so if I left that heatsink on there for quite a significant amount of time, this bottom heatsink down here would eventually reach thermal equilibrium with this massive heat source up the top here, and it wouldn't work anymore we wouldn't get any more energy out of the thing

**Dave Jones:** even though we've got all this heat there it's not being pumped through the device anymore, there's no heat through. Remember, these things are heat pumps when you use them as a Peltier device, and likewise the same way when you use them as a Seebeck

**Dave Jones:** thermoelectric generator, you need heat to be flowing, heat energy to be flowing through the device in order to do that. And if this, once this heatsink on the bottom, because it's quite small in relation to this big heat source up here, once it

**Dave Jones:** reaches thermal equilibrium with that, the temperature differential across the two plates there is zero, and you'll get nothing out of it, no energy, no charge, no nothing and, well, that ruins your day. So the design of these things is all about thermal management

**Dave Jones:** I mean, you know, if you get into that case there, it might work for half an hour or an hour or something but once that heatsink there gets to the temperature you know, if you don't have an adequate way to sink and dissipate that energy on the other side of the plate

**Dave Jones:** then, well, your thermoelectric generator's pretty useless. So how much short circuit current can we get out of this thing? Well, check out that! About 30 milliamps, about, you know, double what I had with just my hand. Ooh, that's getting a bit hot now.

**Dave Jones:** It's getting a bit hot. It's getting hard to keep my hand on there, but yeah, there we go. I mean, you know, we're not getting the best thermal contact. If you wanted to get the best thermal contact in there, I'd have to put some thermal paste

**Dave Jones:** in there to really, no, there we go. You know, it could get up to 50 milliamps or something like that easily if I got some decent thermal contact with that but, you know, we're just playing around here, getting some ballpark figures. Now, going back to this Vout2 over here

**Dave Jones:** this is a way for us to get a high current output. Because as I said, this is limited here to 0.3 amps. So we can get 0.3 amps out of here assuming that our input, you know, our thermoelectric generator can actually, you know, put out that kind of

**Dave Jones:** power out of there. We should be able to suck as much power out of there as we can get from our thermoelectric generator coming in. As I said, this Vout2, which is powering the processor, and that we've been looking at that one's only capable of like 4 or 5 milliamps.

**Dave Jones:** So not much at all. So, you know, if you do have like a high power transmitter you want to turn off or on for extended periods that aren't catered for by little pulse currents for your output capacitance here, you can do that using Vout here and then switch it on.

**Dave Jones:** Okay, I've got a bit more of a complicated test set up at the moment, and I'll explain what's happening here. And by the way this is a classic example where 4 multimeters in your lab can come in real handy. I've explained why any decent lab should have

**Dave Jones:** at least 2 as an absolute minimum to measure voltage and current at the same time. This one's set up, it's actually using 4 because this Gossen metrihit energy here is working as 2 meters. I'm able to measure the voltage and the current at

**Dave Jones:** the same time with this, and then we can get power and then the good thing about this is that we can get energy and hence the name, the metrihit energy, we can get the microwatt hours or whatever over time. So over a certain time period.

**Dave Jones:** So that's really quite neat. So I'm basically replacing 2 multimeters with 1, and this isn't even a full set up. I could probably use 5 or 6 multimeters here easily because I'm not measuring everything. Anyway, what I've got is the Fluke over here, it's measuring the storage

**Dave Jones:** voltage here, so the voltage that's stored on our cap. So I've got the jumper link in there, so I've got the 1500 microfarad storage cap, so it will take some time to ramp up. Just like before, the Breiman is measuring the Seebeck input

**Dave Jones:** module, input voltage right over here. So that's the output directly from the module, and the metrihit energy here is connected to Vout here, and through this decade resistance box here where I can just dial in a load and I can see where the voltage drops out.

**Dave Jones:** So oops, it switched off there. So we're expecting the regulated 3.3 volts out of here. It might take some time to ramp up depending upon our heat source here. So now we can experiment putting different types of heat sources. I'll start out with just my hand, and I'd expect

**Dave Jones:** a slow ramping on the output voltage until it gets to 3.3 volts and regulate and then we can adjust the load. We can just dial that back until we get, like, our maximum current on the output. Because this chip doesn't have a maximum power point

**Dave Jones:** circuit where it can actually, you know, dial back the output current and, you know, so the input voltage doesn't drop and all that sort of jazz. A higher-end TI chip actually has that functionality. But anyway, we can test how much current we can get out of

**Dave Jones:** this with just our hand, and then we can try the heatsink and other stuff. So let's give this a boil. Like I wanted to also measure this auxiliary voltage here, but it's a real pain in the ass to get right into that pin.

**Dave Jones:** They haven't actually taken that out to any test point, which is really annoying. It's very, it's right next to a huge cap, very difficult to get your iron in there. Anyway, let's go. So here we go. We've already got half a volt storage on our cap

**Dave Jones:** there, but that really doesn't come into play. So here we go. I'm gonna, let me go around here and I'll put my hand on there, and let's watch this thing ramp up. There we go. It's ramping up reasonably quick. And bingo! We're at our regulated 3.3 volts now, and

**Dave Jones:** we're drawing about 120 microwatts there. And we're only getting 55 volts out of our Seebeck device. And you can see our storage cap is charging up, we've got that 1500 microfarads, and as I've showed before, if I disconnect that jumper in there, it should charge up quicker.

**Dave Jones:** There we go. It charges up quicker because we haven't got the full 1500 microfarads in there. So there you go, it's regulated, now we can dial back our load. I've got a 90k load on there at the moment, okay? So we can dial that back until we can

**Dave Jones:** see... yeah, see it's starting to yeah, it's starting to drop out, there you go, with a 60k load at only 50 microamps there. It's starting to die there. So there we go, it's ramping back up. So with my hand on this thing, we're

**Dave Jones:** only getting, you know, 100 microwatts sort of out of that regulated 3.3 volt output. So that's not great at all. But this is energy harvesting, right? You can charge up this cap, it will eventually get there, and well, you know, you can do some useful

**Dave Jones:** things with that. See, now the problem with just using my hand, it's not very controlled. Like I can try and put a thermocouple under that, and I'm getting up to, you know, sort of near 30 degrees, but really it is, you know, it's not great.

**Dave Jones:** So I'm just mucking around here just by hand and seeing that we can actually get some regulated voltage out of that thing. So this heatsink should be much better. We can put a decent amount of power into this Seebeck device, and we should be able to get a decent amount of

**Dave Jones:** energy out of the circuit. Let's have a look. And here we go, we're starting to ramp up here, and that heatsink's at 34 degrees. And I don't know about the coupling in there. The coupling's obviously going to be reasonably poor because we don't have any thermal compound

**Dave Jones:** under there at all. So you know, if we had a nice seal pad or something like that, I've got some somewhere, I should probably use it. But yeah, we're not getting the best coupling to that Seebeck module there. So anyway, we are getting up to our 3.3

**Dave Jones:** and we're getting 38 millivolts out of it, 39, it's climbing. So and we're getting our regulated 3.3 volts out of this thing. I wish I could keep that thermocouple on there. And I'd have one hand free. But here we go. Let's dial that back.

**Dave Jones:** 50k, 40, see? We're still... oh no, it's dropping out of regulation there at about 30k at a time. At about point... at 90 microamps load or thereabouts. So not a huge amount of power out of this thing. So there you go, at a good like 15

**Dave Jones:** degree differential there between the... on either side of the Seebeck device. Okay, so I'll take that off. So at a good 15 degrees there, we're only getting... before it drops out of regulation here, we're getting 160 microamps. Oh there we go, it's starting to drop out, you know.

**Dave Jones:** We're not getting... yeah, not getting a huge amount. You know, let's, I don't know, call it 140 microamps or thereabouts. Nah, 100 microamps, sort of safe figure that we can get out of this. Or 0.3 milliwatts. So 350 microwatts out of this thing

**Dave Jones:** for that sort of good, you know, 15 degree differential on there. But then again, like once again, to measure all this stuff really properly, you know, I have to have the correct thermal coupling on there, I've got to have another temperature probe on the bottom heat sink

**Dave Jones:** connected correctly, I've got to have the temperature probe actually on the top connected correctly, and you know, it just gets really complicated to accurately measure these sort of things. You know, this is just a quick sort of ballpark setup here. If I really wanted to do this properly, you could fit around

**Dave Jones:** all day setting it up before you actually could take some decently accurate measurements out of this thing. And there we go, at a good like 20 degree differential there, at least. Could be like 25 degree differential. I am able to get like 150 microamps at 3.3 volts

**Dave Jones:** out of the thing anyway, so I haven't got enough hands. You'll notice that the storage capacity here isn't charging up hugely quickly. If I... I can increase that rate there by of course decreasing our load, and then there's more charge available to actually charge up the cap.

**Dave Jones:** So you know, once you go to really light loads, then pretty much all of the charge is being dumped into that storage cap there. So you can actually get that up pretty quick to that 5.25 volts, and then it clips at that, and then that storage capacitor is

**Dave Jones:** fully charged. So then we can actually dump some of that back into our load. There we go, it's going back down. It's going to be using some of that to maintain the regulation over here. So we can get over a milliwatt now, because we're getting some from our storage cap

**Dave Jones:** but you'll see this drop, you'll see this drop out of regulation as soon as that gets down to that threshold. No, there we go, no, 3, yep, it's starting to drop. It couldn't maintain that. So if we take the load back up, we can, our capacitor

**Dave Jones:** can charge back up, we're back up at voltage regulation on our output, and then you can use, whoa, this is getting a bit hot. It's getting a bit hot to touch. Let me just switch that off. Good thing is there's still a lot of

**Dave Jones:** stored heat energy in here, even if I switch that power supply off, it can still deliver that energy through for quite some time, no problems whatsoever. So yeah, if we bring that load back down you can see that we're going to start taking it, at some point we're going to start

**Dave Jones:** taking it from the storage cap instead of from the CBEC. Here, there we go, we're starting to use some of that and then I can, whoa, bring that load back up, and it'll climb back up. There you go. So that is what your storage capacitor is good for

**Dave Jones:** on here. You can actually, for those particular type of loads or pulse loads, but as I said, subject to the couple of milliamp here, then yeah, it's good to have a storage cap on there. It's effectively free. All you've got to do is pay for the storage cap and you get that extra

**Dave Jones:** energy reserve storing up. So any energy which comes into this thing that's not being used in the load will get stored in that cap until the cap's full. And if I measure the Vout2 here of course, we're not talking about any currents here

**Dave Jones:** that warrant using this output. It's always we can easily use our Vout here. So this 0.3 amp current limit we've got in here, I mean, you know, just the input circuitry in here isn't going to do that. Just the amount of power that this thing is designed for

**Dave Jones:** with our little module here. Eh, not a problem. I've actually held the temperature probe in place now, putting a bit of force down on there with the weight of an old Tektronix multimeter here. And we're up to 47 degrees there, so you know,

**Dave Jones:** we are a good 25 degree differential there. And yeah, this is the second output by the way, this is the V2 output and you can see it's charging up. But if once again if I go down to that 10k load there at 300 microamps

**Dave Jones:** we're just drawing from our storage cap and bingo, we just drop out there. So about a 20k load there is all that's capable of at 163. You know, half a milliwatt, you know, 500 microwatts we can get out of that sort of thing, which isn't

**Dave Jones:** a huge amount, but for these energy harvesting applications could be good enough. And these particular type of Peltier module that we're using here, when you use them as a Seebeck module, they're about 5% efficient, or thereabouts. So, you know, we have to know the power input

**Dave Jones:** actually going in, and people have done, the manufacturers have done measurements on these, they are about 5% efficient. I mean, you know, we are like taking, you know, we're putting in like 17 watts into that heatsink of course, but that 17 watts isn't flowing through

**Dave Jones:** our Peltier device there, so you'd have to do, it might be tricky to do accurate measurements of the actual heat energy flowing through your module down in there, but yeah, it's going to be about 5%. So if we know that figure of 5%,

**Dave Jones:** we can actually figure out how much flowing through our device there, you know, we're getting roughly about 0.5 milliwatts, or 500 microwatts out of this thing, so at 5% we're going to get about, we're going to be having about 10 milliwatts flowing through our Seebeck module down under there.

**Dave Jones:** So not much, a very small fraction of the 17 or 18 watts that we're actually pumping into this heatsink. And of course those sort of calculations don't include any loss in your converter here, and the loss can be actually quite significant. These things aren't super-duper efficient,

**Dave Jones:** but it all comes down to how you actually design your converter down in here. You have to really tailor it for your particular source, your particular application, your particular load, all that kind of jazz. And if we go back to the circuit here, we can see

**Dave Jones:** that the turns ratio of your transformer is going to have a big impact on this. And it turns out that we do actually have a 1 to 100 transformer in here, so I've double-checked that on the schematic. And we can check out the data sheet for that Wirth

**Dave Jones:** transformer, but it's basically the turns ratio which is going to affect stuff based on the value of the capacitance you have here, the type of load, and you know, all sorts of stuff. And there's some graphs in the data sheet which show the complex interaction

**Dave Jones:** of, in terms of output efficiency versus your input voltage, versus your load, versus your capacitance for Vox down in here, and well, it just, you know, it really gets incredibly complicated really quick. If you want to engineer a specific tailored solution for your particular requirement,

**Dave Jones:** if you're just going after a general purpose thing and you don't know what your load is, well, you know, you're just going to have to sort of suck it and see, and you're just going to get like a general output like here. You know, we can get half a milliwatt

**Dave Jones:** out of this thing basically and keep it within regulation for sort of this sort of differential from the 23, 24 degree ambient that we've got here. And if we have a very quick look at the data sheet here of these performance curves I was telling you about, here we go.

**Dave Jones:** Look at this one on the left here, IV out. So the current from the V out pin and efficiency versus the input voltage for that 1, 100th ratio transformer which we've got and for a nominal C1, that's the input coupling capacitor of 1

**Dave Jones:** nanofarad. And look, here's the efficiency curve so the efficiency is the y-axis on the right hand side here from 0 to 70%, and it's the red curve here. So you can see that the efficiency is actually, you know, it's only going to peak for this particular transformer

**Dave Jones:** of about 40%. It's not that great. And it's going to peak at around about that figure there, about 60 millivolts, about where we were operating. So we were sort of operating in the sort of, you know, the maximum efficiency part of the curve down in there.

**Dave Jones:** And it's rather interesting to note that look at the drop off in the efficiency. It only goes down to like 5% efficient. When you've got that higher input voltage, you would think that with the higher input voltage it would be more efficient. But no, because you're

**Dave Jones:** using that big step up transformer here, that 1, 100th ratio, it's not very good over that full operational range. It's designed to be targeted around your particular range that you want. So you have to pick the transformer ratio. Here's where you have to know your design.

**Dave Jones:** So if we look at the one on the right hand side, this is 1 to 50 transformer ratio. And you'll see a similar sort of peak down around at that 50 millivolt input range. But you can see it is higher efficiency down at the higher input voltages

**Dave Jones:** here, and so on. They've got various curves there. Here we go, here's 1 to 20 ratio transformer. By the way, this is at efficiencies only at V out of 4.5 volts. So all that's going to change. So you really need to measure your own performance here.

**Dave Jones:** So efficiency can be up to that 60% mark, which isn't too bad, at 3 milliamps output current there, 3,000 microamps on that left hand y-axis there. At 100 millivolts input, etc. for a 1 to 20 ratio transformer. And you can see that your input coupling cap changes.

**Dave Jones:** That's from 10 nanofarads, and this is 1 nanofarad and 4.7. So all these trade-offs you've got to deal with, and there's tons of graphs like this in the data sheet. Ah, hours of fun for the whole family. And as it turns out, they've actually done some testing for us, and look at this.

**Dave Jones:** Here's a current output graph, so I from the V out pin versus the temperature differential DT there, and for a various sizes of Teg for the 1 to 100 ratio transformer. Well it turns out we've got the 40mm one here, and we're operating at 1 to 100

**Dave Jones:** ratio, so we're going to follow that blue line there. And as you can see, when we're getting like a 10 degree C differential, you know, we should have been getting 400 microamps out of that thing, or whatever. But that is, look, at a V

**Dave Jones:** out of 0 volts. So that's actually short, that's like a maximum short circuit current output. So of course your actual usable output current when you're getting the 3.3 volt regulated voltage that you're typically going to want to power your circuitry as we saw in the practical measurements there, it's

**Dave Jones:** going to be lower than that maximum current output which they show on these graphs. So yeah, you've got to measure the thing, got to build it up and measure it. No substitute for it, they just simply don't have enough graphs and performance data in these data sheets.

**Dave Jones:** You've got to suck it and see. So there you go, I hope you enjoyed that video, just playing around with this energy harvesting kit, getting some ballpark measurements just to sort of see what it's capable of playing around. And it was kind of fun, I need to do a lot more experimentation for

**Dave Jones:** the particular application I've got in mind. But yeah, this does give me some ballpark figures anyway to work with. So it's really quite good, and the linear tech chip, the LTC3108, quite a nice little device, I really like it. Purpose designed for the application, there's

**Dave Jones:** probably others on the market that do a similar sort of job, but yeah, it's pretty much tailor made for this sort of thing. And these dev kits really help a lot, you know, it's a pain in the ass little package down there to sort of do it.

**Dave Jones:** It's just nice, you know, it's got the proper turns ratio transformer, all that sort of stuff. So you know, if you're going to muck around with these energy harvesting stuff, then these energy harvesting kits are really quite neat. But remember, you need a lot of multimeters

**Dave Jones:** and a lot of stuff, and you know, I could hook up the scope, I could use four channels on a scope to get the voltage ramps on all the waveforms and all that sort of jazz. And wow, you can really go to town with these things.

**Dave Jones:** Anyway, if you want to discuss it, jump on over to the EEVblog forum. Hope you liked it. Catch you next time. Transcribed by https://otter.ai
