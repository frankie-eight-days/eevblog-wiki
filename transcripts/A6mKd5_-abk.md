---
video_id: A6mKd5_-abk
title: EEVblog #176 - Lithium Ion/Polymer Battery Charging Tutorial
url: https://www.youtube.com/watch?v=A6mKd5_-abk
source: youtube-asr
timestamps: {"0": 0, "1": 19, "2": 33, "3": 50, "4": 64, "5": 84, "6": 102, "7": 122, "8": 134, "9": 149, "10": 164, "11": 182, "12": 198, "13": 216, "14": 233, "15": 245, "16": 259, "17": 276, "18": 291, "19": 309, "20": 325, "21": 343, "22": 358, "23": 374, "24": 389, "25": 404, "26": 420, "27": 436, "28": 450, "29": 465, "30": 481, "31": 497, "32": 515, "33": 531, "34": 545, "35": 565, "36": 578, "37": 596, "38": 617, "39": 636, "40": 653, "41": 667, "42": 686, "43": 701, "44": 719, "45": 734, "46": 748, "47": 767, "48": 782, "49": 801, "50": 814, "51": 833, "52": 855, "53": 871, "54": 882, "55": 899, "56": 916, "57": 934, "58": 946, "59": 961, "60": 980, "61": 995, "62": 1013, "63": 1027, "64": 1041, "65": 1054, "66": 1067, "67": 1084, "68": 1099, "69": 1114, "70": 1127, "71": 1142, "72": 1162, "73": 1173, "74": 1192, "75": 1207, "76": 1223, "77": 1237, "78": 1250, "79": 1265, "80": 1276, "81": 1288, "82": 1296, "83": 1309, "84": 1330, "85": 1340, "86": 1359, "87": 1375, "88": 1392, "89": 1409, "90": 1423, "91": 1434, "92": 1454, "93": 1472, "94": 1488, "95": 1505, "96": 1522, "97": 1539, "98": 1555, "99": 1571, "100": 1588, "101": 1605, "102": 1624, "103": 1642, "104": 1661, "105": 1681, "106": 1696, "107": 1709, "108": 1722, "109": 1736, "110": 1755, "111": 1769, "112": 1785, "113": 1798, "114": 1815, "115": 1828, "116": 1845, "117": 1860, "118": 1879, "119": 1896, "120": 1908, "121": 1924, "122": 1937, "123": 1946, "124": 1963, "125": 1980, "126": 1997, "127": 2012, "128": 2028, "129": 2043, "130": 2061, "131": 2077, "132": 2095, "133": 2111, "134": 2125, "135": 2138, "136": 2157, "137": 2172, "138": 2187, "139": 2204, "140": 2224, "141": 2236, "142": 2251, "143": 2267, "144": 2283, "145": 2299, "146": 2315, "147": 2330}
---

**Dave Jones:** Hi, welcome to the AAV blog and electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it's lithium ion battery tutorial time. Why? Because these lithium ion battery cells that you

**Dave Jones:** can get these days from hobby supplies, professional supplies, whatever, are great for designing into your next product or gadget that you want to build. Now, when you uh build a gadget and you want to build in some rechargeable batteries, you have a

**Dave Jones:** couple of choices. One is your traditional nickel metal hydride rechargeable double A, triple A, whatever um batteries, right? Well, they're a bit of a pain in the butt. They're old hat chemistry. They're a low terminal voltage, so you've got to often

**Dave Jones:** wire a lot of them in series to get the voltage you want. Um and they're just, you know, big pain in the butt, not available in really nice tiny shapes and sizes like these lithium ion cells. Here's a

**Dave Jones:** 230 milliamp hour cell. Here's a 50 milliamp hour cell. You can get these from companies like powerstream.com and many, many other places, um hobbyist outlets for for remote control stuff all over the place. And as it turns out, they're cheap, readily

**Dave Jones:** available, and really easy to use in terms of charging circuitry and stuff like that. So, we'll go into it. And you've seen your standard Nokia 3.6 volt nominal battery or actually this isn't quite a battery pack. It's actually a single

**Dave Jones:** lithium ion cell because a battery pack is multiple cells like these in series. And you can get those and they charge exactly the same way. So, but we're going to stick to the individual lithium-ion {slash} lithium polymer. There's no real

**Dave Jones:** difference between lithium-ion and lithium polymer. Don't fall for it. It's a bit of a marketing gimmick. Okay, so we're going to take a look at these, how you can charge them, how you can build them into your next product. Let's go.

**Dave Jones:** And the great thing about these cells, as I said, is their size and shape. Take a look at these. They're only a couple of millimeters thick and they come in various sizes. You can actually get them under a millimeter thick. They can You

**Dave Jones:** know, they can They're actually flexible. They're absolutely amazing. So, if you're designing something really weird and unusual, say I'm designing my new calculator watch or something like that, right? I would use one of these because they come in a whole variety,

**Dave Jones:** hundreds of different shapes and sizes. You just pick one that's optimized for your particular purpose. Fantastic. Now, let's take a look at the standard characteristic discharge curve of a typical lithium-ion {slash} lithium polymer. As I said, no difference

**Dave Jones:** whatsoever. Don't let anyone fool you otherwise. Okay, lithium-ion cell. That's just one cell, remember, not a battery pack. A battery pack will have two or more cells in series, but we're only going to consider the one cell. Now, you'll notice this curve, if you've

**Dave Jones:** seen some of my other tutorials on the on double A nickel metal standard nickel metal hydride batteries, alkaline batteries. They all have a very similar characteristic curve like this. They all start off at a particular voltage. They sometimes they drop a bit quickly and

**Dave Jones:** then they have sort of a flat slopey kind of bit and then they drop off fairly abruptly at the end. And lithium-ion lithium polymer batteries are no different at all. Now, uh there are actually two different types. Don't confuse these with lithium

**Dave Jones:** ion and lithium polymer cuz they're the same thing. In fact, they're the uh new type of anode material. I won't go into the construction of batteries. You can look those up yourself. But, the anode in there can use two different

**Dave Jones:** types of materials in lithium ion batteries. The first one and the first one they ever used um and is the traditional type, older type, uses a coke material. Not com- not to be confused with the trademark Coke or the other type of Coke. This

**Dave Jones:** actually comes from uh coal. It's actually derived from that. Or, the new modern ones, in fact, the vast majority of lithium ion batteries you can buy uh and lithium polymer batteries will have a graphite anode. Now, the advantage of the graphite anode one, as

**Dave Jones:** you can see, it starts off and maintains a higher voltage for a longer amount of time. And this is flatter. Uh the curve here is flatter than the coke anode one. And it drops off much later in voltage

**Dave Jones:** as well. So, the advantage of that is that you can power your 3.3 V circuit, a modern circuit, microcontroller, whatever at 3.3 V directly from the battery using the low dropout voltage regulator. Because if your circuit is 3.3 V, there it is,

**Dave Jones:** okay? But, uh you might use a linear low dropout voltage regulator. Might have a dropout voltage of 0.1 V or even 0.2 V. Even at 3.5 V dropout voltage, you're using most of the capacity of that battery. It's

**Dave Jones:** fantastic. Now, the difference between a graphite one is typically determined to be dead at around about 3 V level or something like that. And a coke anode, the older type batteries, are typically taken to be dead around uh you know, 2.5 V, 2.6,

**Dave Jones:** 2.7, something like that. Um even the uh even some of the graphite and our ones are determined to be dead at 2.7. Now, these curves will vary by manufacturer, they'll vary by battery type, um slightly different process variations in

**Dave Jones:** the manufacture of the battery, all sorts of stuff, but these curves are going to be very similar and they're handy cuz you can power your 3.3-V circuits directly from one of these little lithium ion cells. Fantastic. Just something quick I forgot to add

**Dave Jones:** that the x-axis here is actually uh time or capacity, like from 0 to 100% the capacity of your battery or C as it's called or it could be 0 to 1 hour or 0 to 10 hours in terms of time. Makes

**Dave Jones:** no difference, but that is the standard characteristic curve of a battery, the voltage of the cell versus time or capacity. So, how do you charge one of these lithium ion cells? I'm glad you asked. It's pretty darn easy regardless of how

**Dave Jones:** complicated all this stuff here looks. It turns out to be pretty simple, so stick with me. Now, the when you charge the traditional nickel metal hydride batteries and stuff like that, they're a bit of a pain because um they're an

**Dave Jones:** exothermic uh thing, so lithium ion as well, but really to charge them properly you should sense the temperature of them as well to determine as well as the voltage on them to determine when to stop charging or when they're full. Now, with

**Dave Jones:** lithium ions, you're supposed to do the same thing, but these small capacity ones, if you charge them at a low enough current, you don't have to worry about sensing uh the temperature of them to determine when the charge when you're

**Dave Jones:** finished charging these things and it's full. Uh really a lot of the charger chips on the market, which we'll go into, they do have built-in uh temperature interfaces for temperature sensors which sense the cell, but really that's just um not to

**Dave Jones:** detect that the cell is finished charging, just to really actually protect it from gross overloads and things like that. If it shorts out, something goes horribly wrong, something like that. So, uh to charge them is really easy. Any lithium ion or lithium

**Dave Jones:** polymer cell, they charge exactly the same way. As we said, there's only two differences. One is Well, the only difference is the charge voltage, which we'll have a look at here. 4.1 V or 4.2. That value is very critical. It's got to

**Dave Jones:** be within like 1% or something like that. So, that's why you'll find that most uh well, all lithium ion charger cells on the market uh will be 4.1 or 4.2 is the most common by far, volts plus minus at least 1% Some are capable

**Dave Jones:** of going down to 0.3 or 0.4% accuracy. And I won't go into it, but you can look up the research yourself. Uh lithium ion batteries, their shelf life and their number of recharges is pretty much directly um or the biggest factor the

**Dave Jones:** directly proportional pretty much to what maximum voltage you actually charge them at and the charge rate as well. But that voltage critical. Okay? You've got to get it right. The chips handle it for you. So, don't worry about it. Just

**Dave Jones:** giving you some background info now. To charge your lithium ion battery, uses what's called a constant current and constant voltage process or CC-CV process. Constant current, constant voltage. It's a two-step process. I've got three steps here, but the first step

**Dave Jones:** is actually optional. So, we're only going to deal with step number one and step number two. And it's really quite easy and the chip does handle it all for you, but I'm just explaining how it works if Well, you really know cuz it's

**Dave Jones:** interesting for starters, okay? Now, the uh X uh the Y axis here, we've got volts in green, okay? So, the green curve here is the battery voltage, the terminal voltage of the battery during the charging process. This is time on the X

**Dave Jones:** axis and the blue curve here is the battery current or the cell current. Now, uh the current this is important. If this little thing here is a 50 milliamp hour battery, which is what it is, okay? Then, uh that is called 1 C or 1 That's the

**Dave Jones:** charge rate. It's just called C or 1 C, okay? Now, lithium-ion batteries, most Make sure you always check the data sheet for your cell, but most of them will uh be charged around typically 0.5 C. So, if this is 50 milliamp hours or yeah, 50

**Dave Jones:** milliamp hour battery capacity or 1 C, we'll charge it at half that rate or 25 milliamps. So, from So, this blue curve, which is the battery current, 100% actually means 25 milliamps or half C. Some of them can be

**Dave Jones:** charged at 1 C if you want to charge them faster. Some Maybe you can even charge them faster than that, but we're not going to go into it. A typical thing for one of these low-capacity uh lithium-ion cells, half C. So, that 100%

**Dave Jones:** means in this case 25 milliamps, from 0 to 25 milliamps, and voltage, the green curve, from 0 in this case, 4.2 volts. Now, it starts off at Ignore this one called pre process, okay? We'll go into that later, but starts off with a constant

**Dave Jones:** current process. As you can see, the charger just starts, goes from well, zero, right? It goes from zero to 100% charging capacity or half C 25 milliamps. So, it sits there for I don't know, it might sit there for an hour,

**Dave Jones:** whatever. Okay, it depends on the capacity of of your battery. And during that time, it's pushing a constant current into the battery. It's a constant current process. And as that happens, the cell voltage, assuming the cell's already dead, okay, at 2.8 volts.

**Dave Jones:** There Look, let's say the battery is 2.8 volts when you start charging. It'll slowly rise like that, fairly sort of linear, and then it starts to taper off like that until it eventually gets to 4.2 volts, which is the upper

**Dave Jones:** threshold of a float charge voltage threshold. And it goes by many different names in the data sheets and stuff like that, but that's the float charge voltage. And once it hits that point, that very critical voltage point, got to

**Dave Jones:** be within like 1% or better, then it char it changes modes from constant current charging into constant voltage charging, where all it does is now, instead of pushing a constant current into the battery, it maintains that uh it goes constant voltage 4.2,

**Dave Jones:** just like a voltage regulator. In fact, it works exactly like a linear regulator, as we'll check out down here. And it keeps it at that 4.2 volt level. But what happens to the current? I hear you ask. Well, it actually starts to

**Dave Jones:** drop and taper off, and it takes quite some time until it gets down to a threshold level down here, which is actually uh set by a percentage of your charge current. So, if charge current is 100%, this is why I called it 100%

**Dave Jones:** because this is what they call it in the data sheets when you look at it. The value that it stops charging at is deemed to be full, okay? So, this value down here, your battery is full, it's fully charged, Bob's your uncle, okay?

**Dave Jones:** Is typically taken at 10% of the full current. So, if this was 25 milliamps constant current charging level, once that once the current level got down to uh 2.5 milliamps for this particular little tiny cell here, then bang, it

**Dave Jones:** stops charging and that's it, fully charged battery. Woo, piece of cake. Now, that two-step process is what's required to really get full utilize the full capacity and the full life of your battery, but some cheap chargers and very fast chargers, quote marks, will

**Dave Jones:** actually just totally skip this constant voltage process and just do constant current current and then stop when it gets to 4.2 volts. And it's still going to have, say, 80 or maybe even 90% of the battery's full capacity if you just

**Dave Jones:** do this mode. So, this mode here may take an extra hour or something and you may only get an extra 10 or 20% out of it. So, you've really got to weigh up you know, the pros and cons of actually

**Dave Jones:** doing that, but all good battery charger lithium ion battery charger chips will be a two-step process and they'll only stop when they're finished this constant voltage charge process. Now, what's this first stage here, I hear you ask? Well, it's called the

**Dave Jones:** pre-charge stage and this is used some lithium ion battery charger ICs have this mode, some don't, but your good ones will. This mode will only be used if the battery voltage, when you first turn on that chip and it measures the battery

**Dave Jones:** voltage, if it's less than the pre-charge voltage threshold, goes under different names depending on the manufacturer and the data sheet, but typically around say 2.8 volts, that battery is deemed to be really dead, fully dead, it needs rejuvenating, okay?

**Dave Jones:** So, it needs to be fixed. If you get a really completely dead cell that's only got 1 volt on it or half a volt or no volts on it, okay? You've really left your product on, it had no low voltage

**Dave Jones:** cut out, the cell it's completely killed the cell. You can rejuvenate it, but you can't just jump straight into 100% current because you'll you'll further damage the cell, you'll ruin it. So, what they do is they have a

**Dave Jones:** pre-charge uh a pre-charge process where it only charges it at typically 20% of the full capacity. Now, uh that value varies as does this pre as does this full charge value. These can vary. Some chips even allow you to

**Dave Jones:** adjust this and this as well as the charge current. And they're you're really flexible chips, but uh typically if if you plug your charger chip on and it measures that the voltage is less than 2.8, we will only apply 20% of the

**Dave Jones:** current until such time as it reaches 2.8 and then it'll go into the next constant current process. So, what's this circuit down here? Well, this is uh very simplistically what's inside a lithium ion charger battery chip. They can be incredibly simple, so

**Dave Jones:** simple that they can only have uh three terminals on them really. If they have a fixed there's an input terminal where you plug your charging voltage in, there's an output terminal which goes to your battery, and there's a ground. If

**Dave Jones:** it's got its own building voltage reference and it's a fixed charge current. Some chips might charge it say half an amp or 100 milliamps or something like that fixed. You can't change it, and it all handles it internally. Uh Uh a more a slightly more

**Dave Jones:** advanced charger chip might have an extra pin, which allows you to typically set the charge current with a single resistor. Because it that will actually be a percentage uh we'll we'll go into it. Anyway, it allows you to set the

**Dave Jones:** charge current with that value resistor. There's a little formula in there, varies by the manufacturer and the type of chip, uh but it allows you to calculate, "Okay, I've got my little 50 milliamp hour battery. I want to

**Dave Jones:** charge that at half C to be on the safe side, 25 milliamps." I would plug 25 milliamps into the formula in the data sheet, and that would give us a resistor value that allows this chip to charge constant current here of 25 milliamps.

**Dave Jones:** And to do that, most uh chips, the fully integrated ones, will have a built-in uh current shunt sense resistor there with a little amplifier with a little um differential amplifier there as well, and a series pass transistor or a series

**Dave Jones:** pass MOSFET in there driven by an op amp. And you've seen these type of uh circuit configurations before. Now, this pass transistor can depending on there's a lot of control circuitry in here and voltage references and stuff like that

**Dave Jones:** that go between the different modes, but you don't have to worry about that. With when you've got a uh pass transistor like this, you can make it operate in constant current mode like this by determining the voltage drop across that

**Dave Jones:** current that shunt sense resistor there. You can keep it at a fixed current. And then when it switches into another mode, it can work as a linear voltage regulator. And that's why these um are typically lithium ion charger ICs are

**Dave Jones:** typically a linear type because they drive the pass transistor with a DC voltage. It's a linear thing. Some will actually, uh, drive this with a pulse width modulator, okay? And they're your switch mode types, but you can look at the data

**Dave Jones:** sheets to see the differences between those, but the most of the simple ones, and and there's nothing wrong with them, uh, most of them will be of the linear type. The switch mode ones are more advanced if you want to get greater

**Dave Jones:** efficiency based on various input voltages and stuff like that. Anyway, these automatically charge the battery using this, uh, three or two-step charging process, instantly determine, uh, the current flowing through the cell, and they determine the voltage on the cell. They've got built-in voltage

**Dave Jones:** references, and they do everything for you, and you can just hang your circuitry via a low dropout voltage regulator, as we mentioned before. If you're powering a 3.3 V circuit, no problems at all, hang it straight off, but always remember when you're charging

**Dave Jones:** that your circuit will also take a certain amount of current as well. So, you have to take that into account when you calculate this value up here. So, if our circuit was taking an extra 25 milliamps, uh, then

**Dave Jones:** our cell at half C 25, we'd need to set this value to 50 milliamps to cater for the current down into the cell, and also to power the circuit under test. And the good thing about most of these

**Dave Jones:** lithium ion charger chips is that you can leave them permanently connected to the cell like this. And when they're finished charging, they will actually, uh, stop they won't draw any current back out of the cell like that, and

**Dave Jones:** they'll actually have a diodes built across the, uh, pass built into the pass transistor here to actually stop if if you're if you physically remove or short out, um, your charger input, it won't drain the battery back out of it. And

**Dave Jones:** you can get, uh, specs for for the current that leaks back out of the battery battery. It's usually quite small in the order of them, you know, microamps or sub microamps or something like that. So, you can really leave

**Dave Jones:** these things just permanently hooked on to your circuit under test. It's fantastic. So, if you've got one of if you've got a product that say goes into sleep mode all the time, it's got no on-off switch, it just wakes up, then

**Dave Jones:** you can just leave all this permanently attached and you got no power switch whatsoever. Brilliant.

**Dave Jones:** Okay, let's take a quick look at some lithium ion batteries that you can get on the market. I'm using that powerstream.com, which is a provider of a whole bunch of battery cells, some of the largest selection on the market. So,

**Dave Jones:** let's go into batteries and packs down here and check out some of these. Now, there's there's some primary lithium batteries, but look at these babies. Ultra-thin rechargeable lithium polymer {slash} lithium ion batteries. 500 microns. From 0.5 mm to 1 mm thick, and you can

**Dave Jones:** bend them. If you've got a product which needs to be, you know, flexible, and like you can't just put a square battery into it. Like if you've got something that's mounted on your wrist, you want to wrap the

**Dave Jones:** whole battery around your wrist wrist, no problems whatsoever. Awesome. But, um let's go into say the standard uh lithium polymer cells here, and let's take a look at the whole range of them. They're all nominally Don't worry about the nominal voltage,

**Dave Jones:** that's just the average voltage. They're all actually the four-point I believe they're all the standard 4.2 V variety, but you'd have to read the data sheet for that. But, you can get them in capacities as low as 8 to 12 mA hours. Really tiny stuff, but

**Dave Jones:** let me tell you it is very, very difficult actually to find a lithium ion battery charger chip that actually handles battery capacities that small. So, just be wary of that. It can actually be difficult cuz most lithium ion battery charger ICs are actually

**Dave Jones:** optimized for, you know, half an amp or an amp or 2 amps or something like that. And then it's a bit of a trade-off between the circuitry inside is designed for those for current and voltage current accuracy at those sort of currents. Yet,

**Dave Jones:** if you try and that charge them at very low currents like if this is a 12 milliamp hour nominal cell, you would have to charge that at half C or 6 milliamps, then the current accuracy of those battery charger chips is going to

**Dave Jones:** be very difficult to get at 6 milliamp hours. And I've tried to find some and trust me, they can be quite difficult. So, just be wary of that if you do go that low if you're designing ultra tiny

**Dave Jones:** products. But, check out the size of these. Dimensions: 3 by 9 millimeters, 2 by 4, and you know, 18 by 5.2. And there's countless different sizes and thicknesses and capacities and things like that. And here's the data sheet for

**Dave Jones:** that particular battery we just chose. It was one completely at random and there it is. The charging voltage is 4.2, so it is a graphite type anode plus minus 0.03 volts. That is quite tight indeed. That's why you have to have a very

**Dave Jones:** accurate lithium dedicated lithium ion charging IC that has that sort of accuracy. And then, as you can see, it actually recommends a 0.5 C constant charge rate for a standard charge. If you do want to do a fast

**Dave Jones:** charge, it can do it at 1 C. And then the cutoff, you remember that actual percentage value we're talking about, there is 0.01 C. All right, let's do a quick search here using Digikey for a suitable battery charger

**Dave Jones:** IC for that example battery we were using before, the little 50 mA hour capacity battery. And I'm going to charge that at 0.5 C or 25 mA. So, let's type battery charger into Digikey search here and see what we get.

**Dave Jones:** If we scroll down here, we've got battery management ICs, 2,529 of them. Then as you can see, here's the parametric table. There's a different battery chemistry. Now, unfortunately, Digikey don't let you select the charge voltage because it doesn't really know,

**Dave Jones:** even if you go drill deeper into the specific lithium ion batteries here, which we can actually do, but it still doesn't know the difference between those. So, it won't give you an extra charging voltage. It's got supply voltage here, but it'd be nice if you

**Dave Jones:** could actually choose 4.1 or 4.2 volts, but it doesn't do that. But most I know most are going to be 4.2 anyway. So, let's choose a manufacturer which we like here. Now, it hasn't popped up with strangely it hasn't popped up with

**Dave Jones:** Microchip. Microchip's actually the one I wanted. That's a bit of a fail there. Maybe there's an extra There we go. I didn't actually choose it must be in those categories there cuz they're multi-chemistry devices. Just be careful that you can actually miss quite a few

**Dave Jones:** manufacturers if you don't select the the correct actual battery chemistry here, but we can just ignore that. We can just reset that and say I want Microchip parts cuz I know Microchip parts are in stock. I like them. They're cheap. They're small.

**Dave Jones:** They work. So, I'm going to try those. And as you can see, most of them are lithium-ion based ones, but let's go for the in-stock parts, shall we? And let's have a look. We've got 80 items. Well, let's just view those. I'm happy with

**Dave Jones:** that. And what's first? First cab off the rank here, we could actually search by price if we were price sensitive or something like that, but the MCP73812 MCP73831.

**Dave Jones:** You can actually get those for 42 cents each for 3,000 or 68 cents for one off. So, they're very cheap. They're in a five-pin SOIC-23 package, and that's incredibly small, simple obviously, and there's 21,000 in stock. I'm happy with that. I'm actually

**Dave Jones:** going to check out the MCP73831. Let's take a look at the data sheet. They call it a miniature single-cell fully integrated lithium-ion lithium-polymer charge management controller. Fantastic. It's a linear one, it says it's an integrated it's a linear type device. It's got an

**Dave Jones:** integrated pass transistor. It's got integrated current sets, and it's got reverse discharge protection, which we also mentioned, which is great. So, when you disconnect the input, it doesn't drain your battery on you. It's got high accuracy. Pretty good, better than the

**Dave Jones:** standard 1%. It's got plus minus .75 percent there, which is really nice. I like that. You can get it in four different options for different chemistry batteries, but we want the 4.2 volt device. Just make sure that you

**Dave Jones:** order the right one. Some of them aren't pin selectable. In fact, most of them won't be, they'll be a fixed voltage. So, just make sure you do get the 4.2 volt or whichever voltage for your particular cell, which you'll get on the

**Dave Jones:** data sheet. Now, programmable current range. Now, here's where I mentioned before, not all of them will go down to a low current for very low capacity batteries. But, this one says it'll handle from 15 milliamps up to 500

**Dave Jones:** milliamps. Great. We need 25. It'll be within the ballpark on the graph, as we'll see later. Fantastic. It'll still maintain its current accuracy down to 15 milliamps. It's got selectable preconditioning. Um that uh precharge the that actual rejuvenation charge 10, 20, 40, or you

**Dave Jones:** can actually disable that if you don't want it at all. And, it's got selectable end of charge control, too. Um but, because as we'll see down here, there are hardly any pins on it at all. I think those

**Dave Jones:** options will actually be a factory option and not a um and not a pin settable option. So, just be careful of that. Larger pin count devices are more flexible. They will have uh these they will often have these settings on a

**Dave Jones:** separate pin with a separate program resistor. You just choose the right value resistor, and you can set your end charge control to anything you like. But, I don't think this device will have that. Anyway, uh it's got thermal

**Dave Jones:** regulation. It automatically powers down. It's nice. It's in a You can get it in a tiny 2 mm by 3 mm DFM or an easier-to-use uh five-pin SOT23. Fantastic. I like it. And, this is the typical application. This is how simple

**Dave Jones:** it is here. Your voltage input from your charger, decoupling cap, your output voltage. You've got to have a decoupling cap on there, otherwise it can oscillate just like any linear or low dropout voltage regulator can. Same thing here.

**Dave Jones:** The internal charging circuitry is the same uh if it's similar circuitry to what's used, and it will be an unstable loop unless you add the output the recommended value of output capacitance. So, just make sure you do that and it's got ground pin And and a

**Dave Jones:** programming pin which allows you to set the programming current. And it's got a stat output which couldn't can drive an LED to presumably tell you that it's finished charging. And here's the internal circuitry for it. It's not much at all, but as you can

**Dave Jones:** see you've input pin here, your battery output pin here. Here's your pass transistor with the internal blocking diode so it stops discharging from the battery. There's another smaller pass transistor there, reference voltage generator, a whole bunch of whole bunch of comparators for your

**Dave Jones:** different modes, your preconditioning mode, your termination mode, your end of charge and all that sort of stuff. And that and there's your stat output pin. That's only available on the 73831. The 73832 presumably doesn't have that pin. If you don't want it, you can

**Dave Jones:** probably save half a cent there or something like that. And as you can see there's not really much in them at all. Voltage couple of constant current generators and things like that. They're pretty simplistic devices because they don't

**Dave Jones:** really have to do much at all apart from transition from a constant current mode into a constant voltage mode. And to do that doesn't require much circuitry at all. It's supply voltage range from 3.75 to 6 volts. Brilliant, not a problem.

**Dave Jones:** Let's look through some of the other stats here. As you can see the regulated output voltage 4.2 volts. Um from there's there's a different part numbers that you can buy with the different charging float voltages. Make sure you

**Dave Jones:** get the right one. Don't want to goof that up at all otherwise you'll be in big trouble and you'll damage your cell.

**Dave Jones:** And there's the current regulation. It looks like it's got plus minus 10% current regulation there which isn't too bad. The precondition current is set to 10%. Now, the program resistor 2K to 10K, I don't know what what's going on there. The precondition

**Dave Jones:** current, this seems weird. They've got the the same condition over here, yet different values. I think that's a data sheet mistake. Anyway, not sure what's going on there. Aha, here it is. I've scrolled down to the product identification system right at the end

**Dave Jones:** of the data sheet, and this clears up the confusion we saw before with the with the pre and post current termination ratios that were it said were programmable. Well, they're programmable as factory options. So, up here you've got the part number. You've

**Dave Jones:** got to order exactly the right option. The options are AC, AD, AT, DC, and they give you various um options for the pre and post charge termination and other things. So, you've got to make sure that you order exactly the right part.

**Dave Jones:** Otherwise, you could easily end up with being actually delivered or ordering the wrong part, and that could slip into your product, and you can wonder why your battery um battery charge performance isn't as good as your prototype and your testing

**Dave Jones:** showed, because you might have the wrong part. Something to be wary of. The precondition voltage on this is quite high. It's 66. 5%. That's much higher than the 20% I said before, but many chips use different lots of

**Dave Jones:** different value default ratios for that sort of thing. Now, the charge termination ratio by default is 5%, and the charge termination, once it reaches 5% as we saw on that curve, it will actually turn off, and you finish charging. Pass

**Dave Jones:** transistor on resistance, there's the battery discharge leakage, okay? So, when it's finished charging, it will only take 0.15 microamps and under the various conditions, so it doesn't take much current at all once the charge is complete and it's

**Dave Jones:** still got the input voltage on there. It takes up to 5.5 or maybe even as much as -15 microamps from your battery. So, just take that into account. This isn't the lowest power device I've seen in terms of off-state leakage current.

**Dave Jones:** And if we look at some of the characteristic curves here, these are very interesting. Now, this is an important one here. This is the charge current on the Y axis in milliamps versus the programming resistor. And as you can see, they give a range in the

**Dave Jones:** data sheet above for 2 to 67k or something like that. But as you can see, it is not a linear type thing. So, you can't just arbitrarily put in like a 100k resistor or a 1 meg resistor and

**Dave Jones:** get really low charge values because then the current accuracy is going to be all over the place, and it's it's not characterized on this curve. So, really, it looks like that value there if you extrapolate across there, it goes down

**Dave Jones:** Well, it tells you above that it was 15 milliamps, and that's sure enough on the graph, it looks like about 15 milliamps. That's really something to to consider when you're choosing these chips for low value, low capacity, ultra-low capacity batteries.

**Dave Jones:** And last of all, I'm just going to take a quick look at a more flexible charging IC, the ST Micro L6924D. It's You'll find that's got It says it's got programmable pre-charge current, programmable end of charge current, programmable pre-charge voltage

**Dave Jones:** threshold, and it's got a programmable charge timer as well, which will be a backup device just in case the voltage cut-out doesn't work. It'll have a fixed time and then cut off just as a secondary uh safety feature. And it's

**Dave Jones:** also got an NTC or PTC thermistor uh temperature interface, which will limit the charge current if the uh if the temperature of the battery goes up past a certain setting. Now, let's take a look at the um You can see here that it's got the

**Dave Jones:** different different resistors on here to charge uh to change those various um aspects of the charging cycle, the pre and the post uh charge current. Now, if we go down here and take a look at uh the internal block diagram, it's got um

**Dave Jones:** There's the uh There's the pass transistor as well. There's V in here, V out on the right here, which goes to the battery. It's got current detection, uh fault detection logic. Um There's There's a diode that actually blocks it

**Dave Jones:** as well. Um It's got a gas gauge uh function as well. And this is what a lot of uh devices will have if they actually use the if if they use the resistor to set the charge current, it it actually drives a

**Dave Jones:** voltage a current through that resistor, which is proportional to your charge charge current. So, you can hook that up to an ADC on your microcontroller, and you can actually uh log how much uh current is going into your battery during charging. It's quite

**Dave Jones:** nice. So, that's just a more flexible um IC that just allows you to do a a fair few more things than uh than the Microchip one we saw before. So, if you really um have to my you know, get a really

**Dave Jones:** precise uh value of charge and capacity and long life in a in a professionally designed product, you would use a more advanced IC like this, and you would uh go through all the various aspects, and you would design it properly so that

**Dave Jones:** your your built-in battery would have the longest life possible. And if we take a look at the final application demo circuit down here, as you can see, it's just got programmable these these resistors here program all the various

**Dave Jones:** aspects of the charging cycles. So, there you go. That's a more advanced one. There's simple ones available, some real dumb-ass three-terminal ones. Take your pick. But, lithium-ion battery charging is pretty simple with these dedicated ICs. So, next time you're

**Dave Jones:** designing a product and you want to build in a recharging solution, use lithium-ion. The cells are incredibly versatile in shape and size, low cost, the chips are dirt cheap, readily available, easy to use. Go for it. Hope you enjoyed it. See you.
