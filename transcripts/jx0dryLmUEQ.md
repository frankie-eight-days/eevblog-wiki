---
video_id: jx0dryLmUEQ
title: EEVblog #929 - Designing A Better Multimeter
url: https://www.youtube.com/watch?v=jx0dryLmUEQ
source: youtube-asr
timestamps: {"0": 1, "1": 10, "2": 19, "3": 28, "4": 42, "5": 50, "6": 60, "7": 73, "8": 84, "9": 93, "10": 106, "11": 124, "12": 141, "13": 153, "14": 162, "15": 180, "16": 191, "17": 209, "18": 223, "19": 236, "20": 249, "21": 264, "22": 275, "23": 287, "24": 300, "25": 309, "26": 337, "27": 347, "28": 355, "29": 377, "30": 384, "31": 401, "32": 411, "33": 430, "34": 444, "35": 463, "36": 478, "37": 490, "38": 501, "39": 509, "40": 525, "41": 535, "42": 551, "43": 558, "44": 570, "45": 596, "46": 617, "47": 629, "48": 641, "49": 656, "50": 663, "51": 676, "52": 687, "53": 702, "54": 717, "55": 738, "56": 751, "57": 762, "58": 772, "59": 786, "60": 807, "61": 820, "62": 833, "63": 840, "64": 851, "65": 878, "66": 894, "67": 914, "68": 929, "69": 944, "70": 957, "71": 971, "72": 983, "73": 999, "74": 1006, "75": 1020, "76": 1032, "77": 1045, "78": 1057, "79": 1067, "80": 1086, "81": 1100, "82": 1115, "83": 1129, "84": 1138, "85": 1152, "86": 1164, "87": 1174, "88": 1189, "89": 1203, "90": 1216, "91": 1239, "92": 1248, "93": 1263, "94": 1273, "95": 1294, "96": 1317, "97": 1330, "98": 1340, "99": 1349, "100": 1371, "101": 1386, "102": 1400, "103": 1418, "104": 1434, "105": 1453, "106": 1462, "107": 1474, "108": 1485, "109": 1510, "110": 1523, "111": 1535, "112": 1553, "113": 1584, "114": 1603, "115": 1615, "116": 1632, "117": 1640, "118": 1659, "119": 1673, "120": 1683, "121": 1696, "122": 1711, "123": 1719, "124": 1744, "125": 1754, "126": 1764, "127": 1787, "128": 1800, "129": 1814, "130": 1828, "131": 1845, "132": 1859, "133": 1876, "134": 1889, "135": 1899, "136": 1918, "137": 1935, "138": 1945, "139": 1958, "140": 1969, "141": 1979, "142": 1994, "143": 2013, "144": 2033, "145": 2049, "146": 2061, "147": 2074, "148": 2092, "149": 2111, "150": 2126, "151": 2138, "152": 2147}
---

**Dave Jones:** Hi, what if you wanted to design a better multimeter? Not one in terms of features, but in one in terms of lower burden voltage. Now, I've mentioned burden voltage before.

**Dave Jones:** I've even designed a product to overcome burden voltage limitations on a multimeter. It's the micro current. You've seen many times I've mentioned it and had it in many videos.

**Dave Jones:** I've even written a whole article on the project and burden voltage and what it is and how it's a problem. So, click here or down below somewhere to check that one out.

**Dave Jones:** So, I thought we'd take a look at a typical multimeter current measurement front end and see if we can actually redesign it so that we get improved burden voltage performance.

**Dave Jones:** There could be a few traps in this. May not be as easy as you think. So, let's go. So, what I've got here is actually a typical multimeter front end for the current measurement inputs.

**Dave Jones:** So, we've got our milliamps and microamps shared jack. That's fairly typical for a multimeter. Probably the majority out there have them shared and then they have a separate amps jack as well.

**Dave Jones:** And of course, the ground jack here. We're not worried about the positive voltage input for voltage and resistance and and all the other measurements. That's actually an entirely separate circuit effectively.

**Dave Jones:** They might even have like a big isolation slot on the PC physical isolation slot on the PCB itself to actually separate the two sections. So, we're not interested in any of that.

**Dave Jones:** Just the current measurement capability cuz that's where burden voltage is a problem. Just a quick recap. Burden voltage is a voltage dropped across your multimeter across the terminals of your multimeter when you measure current.

**Dave Jones:** And it's to do with these internal current shunt resistors that are used. They're they're resistors. So, when you pass current through them, they drop voltage. And in many cases, this can be a very significant voltage.

**Dave Jones:** It could be in the order of hundreds of millivolts or even several volts drop. And if you're trying to measure uh measure the current in say a 3.3-V circuit and your multimeter's actually dropping a volt or even half a volt, that can cause a real big problems in your circuit.

**Dave Jones:** So, that's why we want to minimize it. So, a typical multimeter front end looks exactly like this. And we've got our amps jack here. It goes through uh the HRC fuse, uh 10 or 11 or 15 amps sometimes, high rupture capacity fuse designed to fail really safe with high surge overloads.

**Dave Jones:** And they're typically rated at 1,000 V because that have Otherwise, if they're too low a voltage, some of the cheap multimeters, they might be HRC fuses, but they might not be rated 1,000 V.

**Dave Jones:** They might be 250 V or something like that. So, they're not nearly as safe as uh the 1,000-V ones that which are designed to stop arc over and stuff like that.

**Dave Jones:** Anyway, that goes in. It goes into a current shunt resistor here. In this case, it's uh 10 mΩ or 0R01. If you haven't seen that terminology before, I could have written this as 0.01 Ω like that, but it's typical to replace the decimal point with the R like that.

**Dave Jones:** Um it's just common terminology. You don't need to be uh confused. Just understand it. So, that's what we're going to use here. So, 10 mΩ current shunt resistor for the amps range.

**Dave Jones:** Almost every multimeter out there is going to use a 10-mΩ shunt. And you've seen these if you open up a multimeter, uh that it's typically a like a little bent uh wire that's uh like nichrome or some other some other low temperature coefficient uh metal that they use to form the current shunt.

**Dave Jones:** There's a few multimeters, real high price, high quality ones on the market that might use a proper SMD uh current shunt uh for example, a four-terminal one, but most multimeters on the market just use a nichrome resistance wire because A, they're very high power.

**Dave Jones:** B, they're cheap. And they just do the job. Now, of course, you've got to sense the voltage on that. So, that's why I've shown these two sense terminals. That's a four-wire sense terminal measurement and I won't go over that why I've done that in separate videos.

**Dave Jones:** I'm sure, but because it's such a low value resistance, 10 m all of your PCB trace resistance can cause a problem. So, if you're not sensing the voltage directly across the current shunt terminal, then it can cause issues.

**Dave Jones:** Yes, you can software calibrate that out of your with your multimeter calibration, but typically the copper on your PCB is a different temperature coefficient to the year current shunt resistor and it can get all messy and changes with temperature and stuff like that.

**Dave Jones:** So, you really need to sense that properly and a well-designed multimeter will do just that. Now, your milliamp and microamp jack typically shared up here gets a little bit more complicated.

**Dave Jones:** It does go through a fuse just like down here, but a lower rated one. Once again, it's high rupture capacity HRC, but a lower value typically like 600 milliamps for example for a 500 milliamp maximum current range.

**Dave Jones:** Once again, 1,000 V for that arc over protection. And then, generally they're going to have a diode bridge to actually clamp that voltage across the current shunt resistor and they'll typically have that directly here.

**Dave Jones:** So, you've no doubt seen diode bridges before and this is a typical surface mount package might be the DF 10S for example and these are going to be rated at 1,000 V.

**Dave Jones:** Now, they don't always use a diode bridge like this. You might open up your multimeter, you might find that they're using four or sometimes five or six diodes in various configurations, usually a bridge configuration to actually clamp the voltage across to protect your current shunt resistors inside because if you uh accidentally use your multimeter incorrectly and put a voltage across here, um then it's going to be presented

**Dave Jones:** straight across the current shunt resistor and that could blow the ass out of the current shunt resistor. So, you want to clamp the voltage. The reason they use a diode bridge like this is just to give a slightly higher voltage.

**Dave Jones:** I won't go into the details. You'd have to go into the parametric curves and all that sort of stuff, but it kind of matters down on the microamp range and things like that.

**Dave Jones:** So, they've basically got two diodes in series and then back-to-back to actually protect it. So, it might be say a 2-V clamping protection across your current shunt resistor. So, I'll just leave that to you to figure out what say 2 V across you know, a 100-ohm current shunt or a 1-ohm current shunt, how much power can be dissipated in there and hence why you don't want to blow up your current shunt

**Dave Jones:** resistor. It's just some protection. So, it's just protecting your resistor just long enough for the fuse to blow. Now, after the fuse, it's going to go into this weird-looking thing here.

**Dave Jones:** I've actually tried to draw a range switch. And the range switch is that switch on the front of the multimeter. And if you've taken a multimeter apart, seen one of my teardowns, or go do it yourself right now, you'll see that there's little contacts, wiper contacts on these range switches, and there's traces on the PCB.

**Dave Jones:** So, I've just sort of, you know, simulated that. I've got two different positions here, basically, and the red just shows the shorting bar there for the microamp range or there for the milliamp range.

**Dave Jones:** So, it's just a switch, basically, single pole double throw. So, on the microamp range, it goes straight into a 100-ohm current shunt resistor. Easy. That's a very, very typical value you'll find on probably most multimeters, very close to that sort of value for your microamp range.

**Dave Jones:** And then if you switch to the milliamp range, well, it disconnects this 100-ohm resistor and then goes down here, and we've now got a 1-ohm current shunt resistor. And that's actually in series with the 10-milliamp current shunt resistor down here.

**Dave Jones:** And sometimes they might actually put in, not 1 ohm, but they'll actually put in 0. 99 ohms like that or 0.99 if we want to keep that terminology. So, that when you put it in series with the 10 milliohms down here, it equals 1 ohm total.

**Dave Jones:** So, it's actually using both of those as the current shunt resistor effectively. And the reason they do that, engineers just like nice round numbers. It comes out nice. You can It didn't matter if you did that and had 1 ohm plus 10 milliohms down here.

**Dave Jones:** You could calibrate it out in software. It's no problem. Now, unlike for the 10 milliohm shunt resistor down here, this one up here, I've only shown one wire going off cuz you don't really have to four-terminal measure that.

**Dave Jones:** You don't really have to do it because the PCB trace resistance is a tiny, tiny fraction of that 100 ohms out up here. It's going to matter for this 1 ohm one cuz you're getting down there.

**Dave Jones:** So, typically they might take a sense point there on that 1 ohm resistor and actually the other sense point down here. So, they're actually using both of those as the current sense resistor.

**Dave Jones:** But they are typical values that you'll find in probably the vast majority of multimeters out there. 100 ohms, 1 ohm, and 10 milliohms. So, now let's take a look at this table down here and see what our burden voltage is for the different ranges.

**Dave Jones:** A typical multimeter, I'm taking the case of a 50,000 count multimeter or a 5,000 count multimeter. So, it'll have a 500 microamp range, a 5,000 microamps or 5 milliamps.

**Dave Jones:** It's actually microamps as we'll see, but it could be displayed as 5 milliamps. Then 50 milliamps, 500, 5 amps, and then 10 amps down here. 10 amps is limited by the power in the current shunt resistor and other stuff.

**Dave Jones:** Sometimes they can go up to 20 amps peak for 20 seconds or something like that. Then you've got to let them cool down, otherwise the current shunt heats up too much.

**Dave Jones:** Anyway, so these are the different shunts that are used. So, in the microamp range, both 500 microamps and 5,000 microamps, it's they switch in the 100 ohm shunt resistor here.

**Dave Jones:** And in the 50 milliamp and 500 milliamp ranges, then they switch in You can put it down to the milliamp uh uh, setting. You switch your range switch to the milliamps, goes down here, and then you're using your 1 ohm current shunt resistor, and then when you specify amps, you've got to physically move not only well, put your switch to the amps milliamps position, and then move your probe down to here,

**Dave Jones:** and of course it's using the 10 milliohm resistor down here for the 5 amp and 10 amp ranges. And then if you just use Ohm's law, 500 microamps times 100 ohms here, then that's 50 millivolts, or uh, what's called 50 millivolts full scale, or sometimes you read the data sheet for a multimeter, it might say the burden voltage is 50 millivolts max, or something like that.

**Dave Jones:** They might use a max figure. It's the same as I'm just using full scale there. So, that is a typical figure, and then once you go up, of course, we're using the same current shunt resistor here for both of these ranges.

**Dave Jones:** So, but because this one goes up to 5,000 microamps, you've got to multiply 5,000 microamps maximum figure, maximum current you can measure on that range, by the 100 ohms, bingo, you get 500 millivolts full scale.

**Dave Jones:** So, as you can see, we've got the same current shunt resistor being shared between two different ranges, and we get two different burden voltages here. 50 millivolts, that's not really a big deal, you know, like you wouldn't really worry about that.

**Dave Jones:** You'd be pretty darn happy if your multimeter had 50 millivolts burden voltage on every range. That'd be a kickass multimeter, let me tell you. But 500 millivolts, that's half a volt.

**Dave Jones:** So, if you're measuring a 3.3 volt rail, the current on the 3.3 volt rail, it's dropping it down to 2.8 by the time it actually gets to your chip in your circuitry.

**Dave Jones:** That can cause a lot of problems. So, that's a real issue. That's really quite high. And then you can just go do the same math here. 50 milliamps times 1 ohm is 50 millivolts, and it's the same order like this.

**Dave Jones:** So, 500 milliamps times 1 ohm, 500 millivolts again. So, we've got these sets of ranges like this based on our current shunt resistor and the amps one down here, 50 millivolts and 100 millivolts.

**Dave Jones:** So, you can see that there's a couple of ranges in there that are really troublesome. The 5,000 microamp and the 500 milliamp. We really want to fix those. And just to be complete, burden voltage is often, in fact, probably more correctly specified in volts per amps.

**Dave Jones:** So, I've just calculated the volts per amp. It's figuring out you can go through and double-check that. Anyway, we'll work with the full-scale burden voltage here. But, what that burden voltage here does tell you is allows you to calculate if you're if you're on the 500 microamp range and you're only measuring 100 microamps, then we're 0.1 millivolts per microamp.

**Dave Jones:** So, the 100 microamps will give us a 10 millivolt drop on there. And of course, that's obvious cuz it's 50 millivolts full scale. We're 1/5 of that, 10 millivolts.

**Dave Jones:** But, that's the thing. Murphy will get you every time. I guarantee that your project you're trying to measure will want to take like 490 milliamps or something like that.

**Dave Jones:** So, you'll have to go, if you want the most resolution on your multimeter, which you do, you'd go to the 500 milliamp range. But, then you're going to get a 490 millivolt burden voltage drop.

**Dave Jones:** It's terrible. Now, there's actually a couple of ways to overcome burden voltage with just your regular multimeter. You can A, switch up a range. So, if you're measuring that 490 milliamps, you can switch up to the 5 amp range and you're going to be dropping bugger all.

**Dave Jones:** What what are you going to be dropping there? Like, you know, 5 millivolts, right? Bugger all. But, you you lose resolution on your multimeter. So, it's a trade-off. The other way to do it is to hook your project up to a power supply and tweak that power supply to compensate for the drop on your multimeter, the burden voltage.

**Dave Jones:** But then if your product is changing currents all the time, that's not necessarily a good thing to do. But as many of you may have already guessed, these figures aren't right.

**Dave Jones:** It's a bunch of theoretical BS. Why? Because we've only taken into account the actual shunt resistor value in here. We haven't taken into account all the other stuff which is in here.

**Dave Jones:** And well, what other stuff you might be saying? Well, we've got some contact resistance here on the switch, but that's not going to be much, right? It's going to be milliohms.

**Dave Jones:** It's going to be, you know, nothing, right? Really compared to 1 ohm and 100 ohms, don't even worry about it. But we got a fuse. And we got a fuse here as well.

**Dave Jones:** But you might be thinking, well, fuses are just a bit of wire, right? That melts. It's a short circuit. Uh-uh. These HRC fuses, and in particular the high voltage ones, the 1,000 volt ones you want to use for safety and that are specified into your high-quality multimeters, they actually have quite a high resistance in them and we'll take a look at the data sheet and we'll measure a couple of these typical

**Dave Jones:** fuses and you'll see that the fuse resistance can actually be higher than your current shunt resistor in here. You might be using a 1 ohm current shunt resistor for your milliamp ranges here, but your fuse might be 1 ohm or even 2 or more ohms.

**Dave Jones:** So it's higher, it dominates your voltage. So the our 500 millivolts burden voltage that we thought was fairly bad down here, it can be easily be double that. In fact, you can almost on a good quality multimeter with that value shunt resistor, you can guarantee that it's going to be double that, pretty much.

**Dave Jones:** So I'll just measure some real fuses here, their cold DC resistance at room temperature, and let's actually see what they are. First we'll actually null this out. I like using my LCR meter for this cuz it goes down to 100 micro-ohms resolution.

**Dave Jones:** Very nice. So, this is this you know a top you know really good quality ASTM HV620 600 milliamps 1000 volt one. Okay? So, this is a 1000 volt fuse you'd typically find in a multimeter.

**Dave Jones:** There we go. You do get around about that 1 ohm figure. Let's try another one. A Sibur, another top brand 400 milliamp one. This one's a bit lower. Once again, it's a 1000 volt rated on there.

**Dave Jones:** And what does this one measure? Look at that. 1.3. Yeah, that might be because it's a bit lower in current, but it's it's that order of things. And hey, let's take a look at this big Sibur one.

**Dave Jones:** Look at this big ass thing. 440 milliamps. You might think, "Oh, this is going to be really low." Right? This is a multimeter fuse. Look at that. 1 ohm once again.

**Dave Jones:** Unbelievable. And this bus fuse Bussmann fuse the ones that I think a Fluke specify these ones. So, it's 440 milliamps again. And that one's better. 0.66 volts is that?

**Dave Jones:** I don't know if that's a 1000 volt. Is that a 1000 volt? Yes, it is a 1000 volt rated. So, that one's not too shabby. And look, here's another bus fuse.

**Dave Jones:** This is a 1 amp one. Okay? So, you'd think this would be low cuz it's 1 amp. No sirree Bob. That's still 0.55 ohms. That's very significant. And here's an 11 amp one.

**Dave Jones:** So, this is typically on the 10 amp range. So, once again, quality one Sibur 1000 volts. Excellent. And there you go. That's around that 10 milliamp figure that we were talking about.

**Dave Jones:** And once again, here's a Fluke is a little fuse designed for FLU, so they're designed for use in the flukes. Once again, that one's going to be around that 10 m figure as well.

**Dave Jones:** Now, I'm not sure if you can see that, but this is actually a 500 mA fuse. I've got two different 500 mA just M205, you know, crappy one hung low brand glass fuse.

**Dave Jones:** In fact, this one's not. I'll show you this one is though. This is just an absolute cheapy, right? So, this is 500 mA, okay? And let's have a look at what this one is.

**Dave Jones:** Look at that. Look at that. Less than 100 m, 93 m for half an amp. So, these crap little glass fuses, which you should never use in multimeters if you're doing anything serious at all, and you know, these top quality 1,000 V rated ones are like 10 times larger resistance.

**Dave Jones:** That's just the, you know, we're into material science now. So, if anyone knows, I don't really know what causes that. It's the material inside and construction, yeah, like I don't know.

**Dave Jones:** If anyone's actually got any real proper detailed info from the manufacturers on what's causing them to be this high, but the fact is they are. Then we've got this one here, which is like got a little ceramic former in there.

**Dave Jones:** It's a fast blow 500 mA fuse yet again, only 250 V rated, okay? And that one, this is not a no namer. It's got all the requisite standards and stuff like that, but it's, you know, 0.3 m.

**Dave Jones:** So, still 1/3 of the resistance of a proper one at a similar sort of rating. And you're going to see a similar thing on the amps range here with the 11 amp HRC fuse.

**Dave Jones:** It's about 10 m or thereabouts, about the same as the shunt, but typically on your amps ranges you're measuring bigger system things and usually probably at a higher input voltage like 12 V or something like that going into your product.

**Dave Jones:** You're not generally measuring low logic rail low voltage rail stuff. So, it burden voltage is typically never really an issue on the amps range. It's not really a problem that needs solving.

**Dave Jones:** But, certainly on the milliamps and the microamp ranges here, these two ones in particular, they we really need to fix those. So, let's take a look, but may not be as easy as you think.

**Dave Jones:** Otherwise, every manufacturer would fix it, but they don't. So, how do we fix this burden voltage problem? Well, it might seem easy. Just like my microcurrent, I use very low value shunt resistors and I use a times 100 amp amplifier.

**Dave Jones:** Times 100 amp amplifier is a little bit tricky. Offset noise and stuff starts to be a problem. But, hey, we could say drop this 100 ohm one, especially for this range here, 5,000 microamps.

**Dave Jones:** We can drop that by an order of magnitude, i.e. 10 times, down to 10 ohms, and then we can feed that into a times 10 amplifier, which shouldn't be too much of a bother, and Bob's your uncle.

**Dave Jones:** We've fixed the burden voltage on the 5,000 microamp or 5 milliamp range here. And likewise, we could change this 1 ohm one for the milliamps. We can change that down to 0.1 or 0.1 ohms, and then once again, take that out, and we put that into a times 10 amp, and bingo.

**Dave Jones:** And like I said, we don't really have to worry about the amps range, so we're not going to bother fixing that, but surely that's all we have to do.

**Dave Jones:** And we've fixed our burden voltage problem. But, aha, you remember the fuse. We might have dropped this by an order of magnitude, right? And nice 0.1 ohms. Oh, yeah, that'll drop our 500 millivolts full scale down to 50 millivolts.

**Dave Jones:** Yeah, for the shunt resistor, but you've still got 1 ohm in your fuse up here. So, it's still going to be in this order of 500 mV. Sure, you've made an improvement.

**Dave Jones:** You've like halved it. It used to be a volt because of the 1 ohm plus the 1 ohm in the fuse. So, that was, you know, you've halved it, but that's you know, it's almost not worthy of your, you know, the cost of implementing your nice, fairly reasonable cost uh times 10 low offset chopper amplifier in there, like a MAX4238 like I use in the uh microcurrent.

**Dave Jones:** It's almost not worthy of the cost for that. So, really, we can't just do that. We have to do something with the configuration here to fix this, cuz this fuse is a real pain in the ass, and we can't just get rid of it because the fuse is all part of the uh safety ratings, the, you know, the UL testing, and the CAT standards, and all that uh sort of jazz, you know.

**Dave Jones:** Can't just take it out willy-nilly um just to get that, although you can temporarily take it out and uh do that, and you can lower your burden voltage of your multimeter, but that's not what what we're talking about here.

**Dave Jones:** Trying to fix it from a design standpoint. Now, some people might mention poly switches. You know, just whack a poly switch in there, and she'll be right. Well, it's not the same thing.

**Dave Jones:** You don't have the same high rupture uh protection, the arc over, and everything else. There's a reason that these high rupture capacity fuses are used in multimeters, and we want to stick with it.

**Dave Jones:** Now, there's several ways you can approach skinning this cat, and well, one of the first things that might come to mind is, well, and you might have actually seen on some multimeters, instead of having milliamps here, let's have a combined milliamps and amps jack here, and then take this out to our amplifier, which can be times 10 and times 100, for example.

**Dave Jones:** So, now we can actually go through with this would be 0 01 and 0 01. Let's go through and actually do the calculations again to see if we can actually do this with the times 10 and times 100 amplifier.

**Dave Jones:** So, the burden voltage is now well, this remains the same. 5 amp range is was 50 mV before. It's It's still 50 mV cuz nothing's changed. But now we've got the milliamps with our 10 m current shunt resistor here.

**Dave Jones:** So, it was 500 mV full scale before. Now it's 5 mV full scale. And for the 50 mA range here, well, uh it was So, 50 mA * 0.01 ohms is 500 µV full scale.

**Dave Jones:** And well, that might sound okay. 500 µV full scale drop across here. Just whack a times 100 amplifier in and Bob's your uncle, right? Well, no. Let's take a look at the data sheet for the MAX4238/4239 that are using Microchip.

**Dave Jones:** It's one of the best low offset almost zero offset chopper amplifiers on the market. And it's got a typical, in quote marks, offset voltage of 0.1 µV. And you of course have to multiply that by the gain here.

**Dave Jones:** And if you have a look at the Microchip here, you can see it is very typically around about that 0.1 V typical figure on the data sheet here at room temperature.

**Dave Jones:** And I've got it actually the input shorted there like that. But you know, we could have we could have it on the actual range itself. There you go. It's on the 10 m current shunt resistor there.

**Dave Jones:** You'll notice that it is 0.01 mV or can get that high. It drifts a bit with temperature and stuff like that. But the typical figure, yeah, it's 10 Let's take it as say 10 micro volts on here.

**Dave Jones:** But because this has got a times 100 amplifier on it, you got to divide that by 100. And that's the input offset voltage. And it is around about that typical figure you find in the data sheet, but hey, the maximum figure, if you're really going to town, the maximum figure could be up to two microvolts, but hey, that's over the entire full temperature range and worst case process

**Dave Jones:** characteristic and everything else, but I've manufactured thousands of these and each one's individually tested and it really is that low. And that sounds pretty low, but hey, let's take a look at the resolution.

**Dave Jones:** If we've got a 5,000 count multimeter, we might get away with this, but you know, we're designing a reasonable multimeter here. It's let's say it's 50,000 count 4 and 1/2 digit class multimeter.

**Dave Jones:** What's the resolution? What's that least significant digit on the display representing in terms of a voltage at this at the point across the current shunt here? Well, at at 50 millivolts full scale, 50, you can see that it's that's that's 50 millivolts.

**Dave Jones:** It's 000 after that, so it's 1 microvolt. And likewise, we just scale it down by a decade, 5 millivolts full scale, 0.1 microvolts. Bingo, we've already matched the typical offset figure of our op amp, so ooh, we're starting to get a bit scared now, but now we want the 50 milliamp range, 500 microvolts full scale with So, if that's 500, put the decimal point there, 00, we're talking about 0.01

**Dave Jones:** microvolts resolution. It's ridiculous. It's an order of magnitude better resolution than what our amplifier is actually capable of. So, when you whacking your times 100 amplifier in there, and that typical 0.1 microvolt offset is going to be amplified 100 times.

**Dave Jones:** So, you're on your 50 milliamp range, you're going to get the couple of least significant digits just flapping around in the breeze because well, that's just the offset voltage.

**Dave Jones:** Sure, you can fix it with like the null button on the multimeter, but it's going to drift a bit. It's going to change with temperature and all sorts of stuff and it really people don't expect a multimeter, especially on the milliamp range, to be flapping around with two least significant digits in the breeze.

**Dave Jones:** So, really that is not a solution. We can't just whack in a times 100 amplifier there cuz the best chopper amp you can get is not going to be able to do the business.

**Dave Jones:** But hey, we are getting towards a solution. So, that one's actually a tick. That one is probably a tick. The maybe the least significant digit might flap around by a few digits, but you know, it's probably going to be good enough, but this one is definitely out.

**Dave Jones:** But hey, there's probably no reason why we couldn't have the amps terminal actually do our 10 amp, our 5 amp, and our 500 milliamp ranges. Cuz we really are quite stuck with this 500 milliamp range.

**Dave Jones:** We can't use a 1 ohm current shunt resistor or a 0.1, for example, because our we've got to go through this 600 milliamp fuse, which is going to be 1 ohm.

**Dave Jones:** So, we're going to be stuck with that high 500 millivolts burden voltage. There's almost no way around it apart from implementing some sort of switching solution here that goes through our 11 amp fuse.

**Dave Jones:** But then we'd have to put some real beefy heavy duty MOSFETs in there or a relay to switch our 10 milliohm current shunt resistor. And there is one like a high-end Gossum, they actually do that.

**Dave Jones:** They do actually MOSFET switch the 10 milliohm current shunt resistor in there and then they can switch in. Once you've got rid of that then you can put other resistors in parallel here.

**Dave Jones:** So, that's why they actually only have one amp jack like this and it measure down to like a 100 micro amp range or I think it's 300 micro amp range or something like that cuz then once you disable if you're able to disable that current shunt resistor there then you can put others in series real easy because you know if it's 1 ohm or something like that you can switch it in no problems.

**Dave Jones:** So that is one possible solution just to do away completely with all this crap up here and just do it all from the one jack with switching but that's not what I want to do here.

**Dave Jones:** I want to solve the problem for the existing jacks that we've got available. One of the reasons is is that those MOSFETs or a relay or whatever they're really big ones have to be big and beefy.

**Dave Jones:** They take up a lot of room inside a multimeter. So you've got to clear out all the space. So I'm going to propose sticking with using the amps jack and the 11 amp fuse and the 10 milliamp shunt for the 500 milliamp range but this 50 milliamp range hey let's go back to the existing solution here and just use we don't even need this uh 10 this point 1 ohm shunt here.

**Dave Jones:** We can get away with just our 1 ohm shunt in there because we only had originally we only had 50 millivolts full scale drop. That's more than adequate even with the 1 ohm up here.

**Dave Jones:** It's only going to be like 100 millivolts typical full scale. So I'm I'm reasonably happy with that. That's lowish burden voltage. It's not it's not micro current low but hey you know it's good enough.

**Dave Jones:** So I've gone and filled in a more detailed table here with the typical drop we're going to get for each of these ranges which I'm proposing here plus the value due to the fuse up here.

**Dave Jones:** So the 50 milliamp range let's use our existing 1 ohm resistor here so we don't really have to change anything and then that gives us 50 millivolts full scale so that gives us 50 mV plus remember another 1 ohm up here, so that gives us another 50 mV.

**Dave Jones:** 100 mV there. We're pretty happy with that. I'm not going to quibble over 100 mV true system burden voltage. That's pretty good. Um it was really the 500 mV and the 1 V that we wanted to fix.

**Dave Jones:** So, that's an order of magnitude lower than that. Beauty. So, that gives us 1 µV resolution. We don't need an amplifier in there. That can just go up bugger off into the existing uh multimeter chip set, which has its own internal amps and stuff like that, but it expects that 50 mV, so it's not a problem.

**Dave Jones:** So, we don't need any um extra amplifier for that range. Now, for the 5,000 µA range, instead of having it go before, we had it going into the 100 ohm or 10 ohm resistor over here.

**Dave Jones:** Let's actually put that into the 1 ohm resistor. So, we just have to uh reconfigure our uh range switch there. So, well, not really. We just call it milliamps.

**Dave Jones:** Instead of 5,000 µA, just call it 5 milliamps. So, it goes through here into our 1 ohm resistor. If we do that, instead of the 500 mV we're getting before, bingo, we're now getting uh because it's 1 ohm, 500 uh 5 milliamps times 1 ohm is 5 mV, is it not?

**Dave Jones:** Plus the extra ohm up here, 10 mV total. Beauty, right? And once again, our resolution is only 0.1 µV. It's in, you know, it's it's doable with the uh that uh Maxim chip that we can actually get, and we only need that times 10 amplifier.

**Dave Jones:** And then, uh this microamp range is now only used for one range, and that is now, of course, we reduce it by an order of magnitude, 10 ohms, just like we said before.

**Dave Jones:** So, 500 µA times 10 ohms is 5 mV plus 1 ohm up here. 1 ohm and 10 ohms, it's If something is an order of magnitude less, you just go meh.

**Dave Jones:** So, I've just written meh in there. It doesn't, you know, it's going to be like plus, you know, 0.5 mV or something. Doesn't matter. Meh. So, 5 mV system uh burden voltage, absolute ripper.

**Dave Jones:** And we just need our times 10 amp there. I think we got a solution. So, what extra circuitry do we have to add to this thing to make it work?

**Dave Jones:** Well, we need a couple of muxes in here, i.e. just uh some switches to switch the voltage across here. So, we've got three points now. We've got one across our 10 ohm shunt resistor, one across our 1 ohm shunt resistor, and one across our 10 m shunt resistor.

**Dave Jones:** So, we can select either of those three inputs. It comes out here, and this is Sorry, that's a times 10 amplifier that goes into our times 10 amplifier, which amplifies that, and then we've got another mux which can select between the times one or the times 10 position, cuz we need both of those selections here for that.

**Dave Jones:** And that just goes to the output. And of course, yeah, this is you remember we said down here that our sensing matters. So, you know, we'd bring our sense line there, and you have to I won't go into details of how you would lay that out on the board, but yeah, we would have to take that as our sense terminal cuz that matters.

**Dave Jones:** Um otherwise, we'd get offset issues uh caused by the traces and things like that. But that, I think, is our better multimeter. It's not super low, you know, burden voltage, absolutely fantastic.

**Dave Jones:** But hey, it's probably a good order of magnitude or thereabouts better than your typical multimeter, cuz some can be like like worst case, we're talking 100 mV here. It's not So, it's very typical down here.

**Dave Jones:** We haven't fixed anything with the amps range. So, that's just, you know, a typical uh multimeter on amps. But as we said way back at the start, it's not really for most measurement applications, it's not really a problem.

**Dave Jones:** I don't don't think I've ever encountered an issue where burden voltage has been a problem on the amps range really, but there might be some obscure case, but we don't really need to fix that, but we definitely fixed these five 5 milliamp range and the 500 milliamp range we had problems with before.

**Dave Jones:** Ripper. So, there you have it. This has probably been a lot longer than what I intended, but I think this is quite a neat solution. There's other ways to do it as I said, switching having the one input jack and having MOSFETs switching and stuff like that is, you know, a really nice way to do it, but it's big and complicated and expensive.

**Dave Jones:** So, yeah, it's you know, but just to modify an existing type traditional meter design like this, that probably does the business. The only kind of confusing part is maybe the 500 milliamp range here would have to be marked on that jack.

**Dave Jones:** It'd be amps and 500 milliamps. And this would be milliamps and microamps like that, but you just annotate it on your silk screen on the front of your meter and Bob's your uncle.

**Dave Jones:** So, there you go. Hope you got something useful out of that. If you got any better ideas, then yeah, leave it in the comments down below. Hope you enjoyed it.

**Dave Jones:** Catch you next time.
