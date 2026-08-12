---
video_id: 8ruFVmxf0zs
title: EEVblog #105 - Electronics Thermal Heatsink Design Tutorial
url: https://www.youtube.com/watch?v=8ruFVmxf0zs
source: youtube-asr
timestamps: {"0": 0, "1": 23, "2": 34, "3": 51, "4": 73, "5": 90, "6": 105, "7": 120, "8": 132, "9": 149, "10": 173, "11": 182, "12": 200, "13": 219, "14": 231, "15": 245, "16": 256, "17": 276, "18": 288, "19": 301, "20": 317, "21": 333, "22": 345, "23": 362, "24": 376, "25": 388, "26": 416, "27": 426, "28": 440, "29": 457, "30": 468, "31": 485, "32": 496, "33": 517, "34": 536, "35": 553, "36": 566, "37": 591, "38": 607, "39": 624, "40": 639, "41": 651, "42": 667, "43": 681, "44": 699, "45": 717, "46": 744, "47": 759, "48": 771, "49": 784, "50": 803, "51": 813, "52": 836, "53": 849, "54": 869, "55": 882, "56": 897, "57": 910, "58": 925, "59": 947, "60": 972, "61": 986, "62": 1020, "63": 1037, "64": 1051, "65": 1065, "66": 1092, "67": 1109, "68": 1120, "69": 1134, "70": 1141, "71": 1153, "72": 1163, "73": 1176, "74": 1191, "75": 1206, "76": 1215, "77": 1229, "78": 1252, "79": 1264, "80": 1282, "81": 1290, "82": 1302, "83": 1315, "84": 1331, "85": 1348, "86": 1362, "87": 1380, "88": 1388, "89": 1399, "90": 1415, "91": 1442, "92": 1465, "93": 1478, "94": 1491, "95": 1504, "96": 1515, "97": 1527, "98": 1538, "99": 1552, "100": 1565, "101": 1575, "102": 1600, "103": 1613, "104": 1627, "105": 1641, "106": 1654, "107": 1681, "108": 1699, "109": 1723, "110": 1739, "111": 1750, "112": 1764, "113": 1778, "114": 1791, "115": 1811, "116": 1821, "117": 1833, "118": 1852, "119": 1870, "120": 1884}
---

**Dave Jones:** Hi, welcome to the AEV Blog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, a couple of blogs ago, I discussed designing this little constant current dummy load, and I did some heat sink very basic back of the envelope heat sink calculation, and I got quite a few emails about it.

**Dave Jones:** Can I go into thermal design in a little bit more detail? All right, let's give it a go. This one will be all about thermal design. So, what is thermal design when it comes to electronics?

**Dave Jones:** Well, I'm glad you asked. Now, in the case of almost any electronic any bit of electronics that you design, it is going to dissipate heat in the form of waste heat in virtually well, every component.

**Dave Jones:** Essentially, and it's especially true in this example I did of this high power well, reasonably medium power dummy load I did the other week. We need a heat sink on our component to dissipate or disperse the heat into the air so that the little power transistor in there keeps at a reasonable operating temperature.

**Dave Jones:** Because most electronic components it's not well known, but their reliability, you think they're you know, they'll they'll last forever, but their reliability actually drops with a square of the increase in temperature.

**Dave Jones:** So, if you double your temperature, then the component is going to only be 25% as reliable or you know, uh four times less reliable than it was at that lower temperature.

**Dave Jones:** So, the ultimate goal of most thermal design in electronics is to ensure that you design your entire circuit with all your components that they operate at a reasonable, safe, and reliable temperature.

**Dave Jones:** When it's and it's thermal design, you have to take into account all sorts of things. The airflow over it, whether you or not you mount what type of case you mount it in, how it dissipates to the air, do you have it How much ventilation do you have?

**Dave Jones:** And all sorts of stuff. But the goal is to keep your little power transistor or your component, your microprocessor, or whatever it is at a reliable and safe junction temperature, the actual die.

**Dave Jones:** And that's the key, the junction temperature. So, let's take a look at it. And if you've seen my blog a long time ago on these um Cree star LEDs, well, you'll know I did a bit of thermal design calculation in that and how it was pretty messy stuff and how that uh the LED is a certain efficiency and it emits a certain amount of um energy or a

**Dave Jones:** certain amount of power as visible light, but the rest of it dissipates through the aluminum at the back uh as you know waste heat and you have to get rid of that.

**Dave Jones:** So, in solid state lighting design, it's important, for example, to keep the uh die temperature of the LED as low as possible because these LEDs don't last forever. As I said, it's going to be roughly a uh square of the temperature, the lifetime of these LEDs.

**Dave Jones:** So, it's important to keep that junction temperature low. So, how exactly do we do the calculations for a heat sink to get the junction temperature of our little power transistor, MOSFET, LED, IC, whatever it is, down to a reasonable temperature?

**Dave Jones:** Well, let's take a look at it. There's some very basic theory here, which I'll take you through. Now, the good news about thermal design is that it's incredibly simple and believe it or not, you already know it.

**Dave Jones:** It's just like Ohm's law and basic circuit theory. It's no different. It's completely thermal design and circuit design are completely equivalent in concepts and math. So, let's check it out.

**Dave Jones:** Now, this is the basic theory, okay? As you can see, there's resistances. There's voltages down here, and there's a current source. That's a symbol for a current source up there if you haven't seen it.

**Dave Jones:** But, so we have resistances, current, and voltages, and they're actually equivalent to they they have equivalent aspects in thermal design. In this case, current is equivalent to power. So, the current flowing through our circuit here is the same as power or the heat in watts, okay?

**Dave Jones:** Now, the resistors, they're standard you just draw them as standard resistors. This is all by I'm not simplifying this at all. This is how you do real calculations in the real world with thermal design.

**Dave Jones:** Uh uh in in basic circuit theory, a resistor now in thermal design becomes a thermal resistance. It's called in degrees. Instead of being in ohms, it's degrees C per watt.

**Dave Jones:** And for thermal resistance, what that means is that for every say 1 W increase, uh the temperature will increase by X degrees C for however much power you put through that thermal resistance.

**Dave Jones:** So, it's called uh theta. That's actually a theta uh symbol. So, it's theta is like it's thermal resistance. That's just how it is. That's just the units used. And in circuit theory, voltage now becomes temperature.

**Dave Jones:** So, as you can see, current, resistance, and voltage become power, thermal resistance, and temperature. Simple. You already know it, and you just uh apply it to basic circuit theory.

**Dave Jones:** In this case, it's a series um circuit because the power flows from the junction through to the case, through to the heat sink, and then through to ambient. There are, as I've explained in my LED one, there are parallel equivalent circuits, but we won't go into those, but the same circuit theory applies.

**Dave Jones:** Simple. As I said before, the goal with thermal design is to keep the junction in your little power transistor or IC or whatever it is at a safe and desirable operating temperature.

**Dave Jones:** Now, the good news is is that you'll have several uh known values in the circuit, okay? You have the ambient temperature down here, which is look, it's just like a battery, okay?

**Dave Jones:** It generates a voltage, okay? So, you might have, say, 20° C here, which is our ambient temperature. And then, the heat sink will have a thermal resistance, so the amount of power going through the heat sink um if the heat sink is uh 5° C per watt, for example, if you put 1 watt flowing through there, it will increase the temperature by 5° C.

**Dave Jones:** So, the heat sink will be at 25°, uh or 5° C above ambient. Everything is always above ambient in thermal design. That's what you got to remember. It's a key uh important thing.

**Dave Jones:** Now, once again, if you've got your uh 1 watt flowing through there, then you get the thermal resistance of the case to the heat sink. I'll explain this terminology here.

**Dave Jones:** You'll see terminology like this in component data sheets, heat sink data sheets, and so on. It'll be thermal resistance R theta JC, for example. That means they always have an equivalent word, so J is junction, the actual junction, the silicon junction, and junction to case.

**Dave Jones:** C is case. So, So, the thermal resistance between the little junction right in there and the tab on your on and the metal tab on your little power transistor.

**Dave Jones:** So, that's junction to case and then you'll have a thermal resistance of case to heat sink because your heat sink is not a perfect um if you just bolt this little power transistor onto this heat sink, okay?

**Dave Jones:** Just like in here, you can see I've got a bolt I've got a bolt inside there. You can see it. Okay, if you just bolt that on there, these surfaces aren't completely flat, okay?

**Dave Jones:** They'll be like they'll have like little jaggies on them like that. So, you're trying to mate up, okay? You're trying to mate up the back of the power transistor to the heat sink and they're they've actually got little, you know, it can only be a few microns or something like that, but they won't make really good contact and that's why there will be some thermal resistance there

**Dave Jones:** and you try and lower that by using uh you've probably seen it, the white thermal heat sink compound paste which you put between there which helps it fills in all those little air gaps and lowers the value of this thermal resistance or you can use a seal pad um which is an industry um it's a trademark term.

**Dave Jones:** It's like a silicone rubber pad which goes in there and you can use um all sorts of things to lower that thermal resistance. And last of all and probably the most important factor is the thermal resistance of the heat sink to ambient.

**Dave Jones:** Now, this heat sink that I used in my design is actually 2.7 degrees C per watt, but as we'll go into, that's not a fixed figure. That's just a nominal figure which will change with the air flow.

**Dave Jones:** That's why they have actual fins like that, okay? It's designed so that when air flows forced air flows over them, um it helps cool them down. And if you wonder why they're actually black, go I won't go into the um quantum theory of it cuz if you it can get right down to actual quantum physics and stuff like that and how um uh you know, how objects radiate and absorb uh energy.

**Dave Jones:** It goes back to Einstein and all that sort of stuff, but being black, check out the word emissivity. The emissivity um of an object a an ideal black body, you may have heard of black body radiation.

**Dave Jones:** Well, same thing. That's the reason why the heat sink is black because that gives closer to an ideal black body radiator because um all objects have the same properties of absorbing and also emitting radiation.

**Dave Jones:** And if it's black, it gets closer to the ideal one for emissivity. So, that's why they use um that's why they anodize aluminum heat sinks black. Now, go into some real calculations and measurements later, but as you can see, you've got an ambient temperature.

**Dave Jones:** It increases the temperature on the heat sink and then the temperature gets higher again and then the temperature, ultimately, the answer you want, you want a value for how hot your junction temperature's going to be.

**Dave Jones:** And you just optimize your design the how the heat sink, the um air flow and all that sort of stuff to get a reasonable junction temperature. Now, if you want to get a little bit more tricky and theoretical, then I've drawn some capacitors in here.

**Dave Jones:** Once again, the electric electrical thermal analogy. There's some capacitance from the junction. Um there's capacitance in the um in the junction to case, there's capacitance in the heat sink.

**Dave Jones:** And what that capacitance is equivalent to in thermal design is thermal inertia. Something like this doesn't heat up instantly, okay? It It can absorb little pulses of heat and and not heat up um as it normally would under steady state conditions.

**Dave Jones:** And that's what the capacitors um um you know, actually represent. Is that when you apply some pulse power, some pulse heat into your um into your thermal design, then it's going to absorb some of that uh pulse heat.

**Dave Jones:** But, generally, you don't really take these much into account in thermal design unless you're doing really high-power pulse up very, you know, um very more obscure type applications. Generally, you only take the steady state example when it's all when if you've got constant current or constant heat flowing through your thermal design, then these don't matter in the end and you can take them out of the equation.

**Dave Jones:** But, I just thought for completeness, I'll mention them. Okay, so enough of the theory stuff. Let's go through a practical example, shall we? I'll go through the same example I used last time with my um MTP3055 uh power MOSFET transistor.

**Dave Jones:** Now, take a look at the data sheet here, okay? Now, as you can see in the maximum ratings down here, down the bottom there, you can actually see the thermal resistance.

**Dave Jones:** It's got junction to case of 3.13 degrees C per watt. And it's also got the junction to ambient uh thermal resistance of 62.5 degrees C per watt. So, what does that mean?

**Dave Jones:** Well, if you just mount this power transistor on your board free standing like that with no heat sink attached to it uh whatsoever, then um if you put 1 W into it, one if it's dissipating 1 W of power, then it's going to increase by 62.5 degrees C above ambient.

**Dave Jones:** So, if the ambient's 20, then this is going to reach for 1 W, it's going to reach 82° C. And if you put your finger on there, you'll burn it.

**Dave Jones:** So, uh that's a very simple That's why they have the junction to ambient, just in case you don't want to use it with a heat sink. But, if you do, if you attach it to a heat sink like this, then you use the junction to case, and that's the figure that we saw in the diagram before, and you plug that into your thermal design calculations, and you

**Dave Jones:** work from there. And somebody actually asked me last week, it was a question on YouTube. Um somebody asked me, "Well, I didn't take into account the uh junction to case thermal resistance." And I didn't, cuz it was just a ballpark application.

**Dave Jones:** But, in this In this exact example, okay, if you put 10 W into here, which is uh close to what I did last time, and it's 3° C per W, then my heat sink was only at seven uh 70° C, as we measured and calculated, but the junction is going to be 3° C per W above that.

**Dave Jones:** In this case, 3 * 10 W is 30° C, the junction in there would have been at 100° C. There you go. So, what actual target temperature do you want for your junction?

**Dave Jones:** Well, how long is a piece of string? Really. Um you've got to You know, a lot of the time it's just a ballpark uh number. You might say, "Oh, it'd be nice to keep my junction temperature at 80." But, you know that if you go 10° C below that, your liability increases.

**Dave Jones:** So, it's just good to keep it as low as possible. So, let's get the thermal resistance of our heat sink from the data sheet. Now, here's the data sheet for this particular heat sink, which is the Aavid Thermalloy 6400.

**Dave Jones:** Now, as you can see right on the right there, its nominal thermal resistance is quoted, and you'll get this in the Farnell catalog, of 2.7° C per W. And well, you know, it's that's it's actually not going to be that.

**Dave Jones:** It varies, as I said. So, now let's take a look at this graph. It looks a bit complicated, but there's two actual graphs here superimposed on each other. Now, take the uh take the x-axis, the heat dissipated in watts, and the vertical left-hand y-axis there, which is the temperature rise above ambient in degrees C.

**Dave Jones:** Now, that those two axes relate to the curve that uh linear almost linear curve which goes from uh the bottom left corner to the top right. Now, as you can see, um uh if we've we've going to we're going to choose a reference value of 10 watts for this system, okay?

**Dave Jones:** We're going to put 10 watts into it. So, we extrapolate that graph from the bottom x-axis, we go up 10 watts, and then we then we go to the left-hand y-axis, and as you can see, it's about, let's say, a 42 degrees C rise above ambient.

**Dave Jones:** So, uh that means for 10 watts, you divide 42 by 10, it's 4.2 degrees C per watt. And that is the thermal uh thermal resistance of the heat sink ideally, but the problem with that is um that a heat sink um this thermal response graphs are really are designed assuming that the heat is going to be input and um input onto the heat sink evenly across all the surface.

**Dave Jones:** And well, that's never the case in terms of like a you've got a little TO-220 transistor there. It's a It's a point um heat source. So, you're going to have an extra um spreading resistance, it's called, and the heat has to actually spread from a point source through the heating.

**Dave Jones:** And that's not shown on the graph, and that's what makes these graphs a bit tricky to interpret. Now, a rule of thumb, generally which they won't generally tell you is to increase that by, you know, a third, 33% or so.

**Dave Jones:** So, if we take our 4.2 °C per watt, which we just got from the graph, we multiply that by 33, we add on 33%, and we got 5.5°C per watt.

**Dave Jones:** Bingo. So, that's the figure, that's the rule of thumb figure I'm going to take for um this heat sink at 10 watts power dissipation. Now, just to clarify that a bit more, that graph we just used from the bottom left corner, which goes upwards, that is called the natural convection graph, and that is the graph you use, that's the curve you use when your heat sink is

**Dave Jones:** just sitting there in still free air like that. It's assuming all sorts of things, it's assuming it's painted black, it's assuming that it's mounted vertically instead of horizontally, and there's natural gravity, you know, feed of the air, and you know, and there's no air flow over it or things like that.

**Dave Jones:** So, it's assuming a lot of stuff, as well as it's assuming a not a point load as well. So, that's the natural convection graph, and we'll look in the other graph later.

**Dave Jones:** Okay, let's put all of those values into our thermal system diagram here. We've got the thermal resistance the junction to case, the data sheet value we got for the MOSFET, 3.1°C per watt.

**Dave Jones:** Now, the thermal resistance of the case to heat sink, we don't really know what that is, but it's going to be in the order of 0.5°C per watt or something like that.

**Dave Jones:** We can kind of figure that out later, but it's going to depend if you use a a sil pad or thermal compound, but in my practical example, I've got no compound at all.

**Dave Jones:** It's just a direct connection. So, let's just say that's not applicable for the minute. And the thermal resistance of the heatsink to ambient, as you saw, we're going to take it normally as 5.5° C per watt.

**Dave Jones:** And we've got the ambient temperature down here. And let's see what we measure. Okay, let's just take a reference reading here. I've got my Fluke 87V here with my thermocouple temperature probe.

**Dave Jones:** It's measuring the ambient temperature. Let's take that at 18° C. Let's not worry about the point two there. Now, the Metrahit Xtra is 10 V here. That is measuring the voltage directly across the MOSFET power transistor down in there.

**Dave Jones:** And as you can see, this has a little current meter on it and it's 1 amp. That's 1,000 mA is 1 amp. So, we've got 10 W, pretty close to exactly 10 W being dissipated in our power transistor and our heatsink there.

**Dave Jones:** So, let's let that settle for a while. In fact, I can feel that. I can smell it. That's That's too hot to touch. That's got to be about That's got to be well over 60° now.

**Dave Jones:** But let's let it settle for a while and then we'll take some stable reference temperature readings. Okay, it's been settling there for a while and it's stabilized. I've got the thermocouple right down into the metal junction right down in the heatsink.

**Dave Jones:** You can't see it, but it's there. And as you can see, the heatsink is at 76.3° C. And I'm probing the case of the MOSFET down there and it's very hard to actually get good reliable contact on there, but let's take that as 86 Let's take that as There you go, 87° C.

**Dave Jones:** Now, out of interest, let's actually fan force cool this heatsink and see what we get. Exactly same conditions as before, 10 W, but I've got air flowing over it.

**Dave Jones:** I've let it reach steady state. And as you can see the temperature of the heat sink has dropped drastically to 35.7°C. And once again, it's very difficult to get that case temperature, but it's around about, let's say 47°C.

**Dave Jones:** And for the sake of completeness, you probably can't see that there, but I'm using my anemometer, which measures the air flow, and it's around about Let's take that as about 10 km/h.

**Dave Jones:** It's very difficult to actually get that, but we have to convert 10 km/h to feet per minute, which was on our performance graph. But there you go, that's the figure.

**Dave Jones:** So, after those practical measurements, how far were we off? Well, let's check it out, okay? We had an ambient temperature of 18°, we had a heat sink temperature of 76°C.

**Dave Jones:** We had a junction Sorry, a case temperature of 87°C. Now, let's see if our figure from the graph of 5.5°C per watt was reasonable. Well, you do 76, like the Remember the voltage thermal analogy?

**Dave Jones:** 70 76 - 18, that's the drop across the heat sink. Okay, 76 - 18 is 58°C. 58°C divided by the power flowing through it is 10 W. That's 5.8°C per watt.

**Dave Jones:** And we got a value of 5.5°C per watt from the graph, roughly. So, there you go, it matches up fairly well for the case of the still air or the steady state condition with no air flow at all.

**Dave Jones:** Now, as you can see, our case temperature was actually quite substantially above the heat sink temperature. And once again, if you do the math, 87 76 / 10 is 1.1°C per watt.

**Dave Jones:** So, there you go, the figure we couldn't work out before, the thermal resistance of the case and the heat sink. As I said, I've got no thermal compound in there.

**Dave Jones:** It's just bolted straight on raw. It's pretty poor, actually. It's not that great. It's 1.1° C per watt. So, in our thermal system here, we can that's 11 for 10 watts going through.

**Dave Jones:** That's 11° C rise. That's quite That's quite a lot, actually. So, as you can see, we can increase the thermal per thermal performance of this system by adding in a proper um a seal pad or some thermal heat sink compound.

**Dave Jones:** Now, the thermal but what we want the ultimate goal of this is what is the junction temperature of our power transistor. That's the important thing, okay? Now, um if we've got 87° C case temperature as we actually measured, and we know we've we know the thermal resistance of the junction to case from the data sheet.

**Dave Jones:** Remember that value we got from the data sheet? So, that value is uh 10 watts * 3.1° C per watt, which is 31° C. That's the increase in temperature between the case and the junction, 31° plus the um temperature of the uh case is 118° C.

**Dave Jones:** That's roughly what the junction of that power transistor is going to measure. We can't actually um physically probe that. It's not it's not that easy to actually do, but you can calculate it.

**Dave Jones:** There you go. And you can just um uh you know, tweak the thermal performance of your system either with air flow, as we saw, or with um by adding proper thermal compound in there.

**Dave Jones:** You can lower that junction temperature and um increase the uh increase the reliability and the longevity of your system. Now, let's get the thermal resistance of the heat sink for the forced air configuration.

**Dave Jones:** So, let's take a look at that graph again. Here we go. Now, we're concerned with the x-axis, which is on the top, the air velocity in feet per minute this time.

**Dave Jones:** That's what we care about and we care about the y-axis on the right-hand side, which reads directly in thermal resistance, whereas it didn't before. You remember that we had to actually actually calculate it.

**Dave Jones:** Well, now it reads directly. It does that because in the forced air configuration, the heat dissipation in watts doesn't actually affect the thermal resistance in a forced air configuration.

**Dave Jones:** So, we can read it directly from the graph. Now, as you can see, it doesn't the graph actually doesn't extend all the way where we're reading the graph, which starts the curve, which starts in the top left corner, by the way, and goes down to the bottom right.

**Dave Jones:** Now, as you can see, it doesn't go it it stops at about 200 ft per minute. It doesn't go anything below that because it starts getting very non-linear there.

**Dave Jones:** It starts, you know, going exponentially up and and you know, and really you can wouldn't be able to read it cuz it would just go off the scale at 0 ft per minute.

**Dave Jones:** You're better off reading the still graph. So, they sort of overlap each other in that respect. So, that's why you usually won't see the curves go all the way to zero cuz they just go off to infinity basically, but for the value of airflow we measured, which was around about 550 ft per minute, as you can see, it's around about if you take that graph, there it's

**Dave Jones:** about take it over to the right-hand side, about 1.2° C per watt. So, that's the figure we're going to going to use for forced air cooling. So, as you can see there with those graphs, they're a bit of a trap for young players.

**Dave Jones:** It's got two different thermal properties on there and you can't get them confused. One's still air and one's forced air. Um so just don't get them mixed up and read the wrong axes for the wrong graph.

**Dave Jones:** Watch out for it. So let's put those values for the forced cooling at 550 ft per minute uh over here. Our temperature with ambient temperature was 18° our uh temperature of our heat sink we measured at 36° C.

**Dave Jones:** So 36 - 18 is 18° C. 18 / 10 W flowing through the system is around about 1.8 uh ° C per watt. And we got roughly from the graphs maybe a figure of say 1.2.

**Dave Jones:** You know, it's it's in the ballpark. So um that's that's quite reasonable. Now as you can see the uh temperature of the um case we measured at 47. Exactly the same differential as before because whether or not it's uh forced cooling it doesn't matter because the um the case to heat sink is just going to be that little air gap in there between the uh power transistor and the

**Dave Jones:** heat sink. So as you can see that's 11° difference. That hasn't changed. It's still 1.1 ° C per watt. Same as last time. Now what's our junction temperature? Well, it's uh 47° C um Celsius on the case plus the 3.1 ° C per watt * 10 31°.

**Dave Jones:** Add them together junction temperature bingo 78° C. As you can see it was much higher than that before. So just by adding some forced cooling we've uh drastically reduced the junction temperature of our power transistor and just for fun I thought I'd see what happens if I enclose this in a box with basically no ventilation.

**Dave Jones:** I've taped it up around here. Exactly the same conditions as before. It's dissipating 10 W. I can feel the heat on top of that. And as you can see, it's rose It's risen up to 96.7°C, almost 100°C.

**Dave Jones:** That's a huge difference to what we had before. And that, in theory, okay, if you enclose something in there and keep on pumping power in and if it's perfectly insulated, the temperature will increase without bounds.

**Dave Jones:** But that doesn't happen in actual practice because the heat eventually dissipates somewhere. But as you can see, putting things in enclosed boxes can be a real pain. Now, there's one other thing to consider with heat sinks, okay?

**Dave Jones:** They actually radiate heat. But if you've mounted it on a board and you mount it, say, next to a you know, if you've got like a voltage regulator there and you put a big input filter cap next to it, all that heat's going to radiate into the capacitor.

**Dave Jones:** And if you watch my capacitor tutorial, you'll know that that electrolytic capacitors are affected by heat. That's why they got a maximum life maximum rating on there of 105°.

**Dave Jones:** Their life shortens based on drastically shortens based on the higher temperature they get. So, heat sinks, it's not just about keeping your junction temperature cool. It's also about keeping other components near it which have a which have a life based on temperature, keeping those cool or separated as well.

**Dave Jones:** And as I showed in my LED blog, you can get parallel systems as well. In this case, we've got a whole bunch of LEDs mounted in parallel on the one heat sink.

**Dave Jones:** So, we've got separate sources of power going into the heat sink. And that can get a bit more complicated and a really quite messy to actually do the thermal calculations for that as I explained in my previous blog.

**Dave Jones:** So, there you go. Thermal design. It isn't that hard, really. It's a bit tricky and there's lots of unknowns and sort of, you know, fuzzy figures, no pun intended, but, you know, in the end, it comes down that simple analogy between basic circuit theory and and thermal.

**Dave Jones:** So, if you understand Ohm's law and basic series circuit theory, then, you know, you can you can pretty much do anything. And they're real design examples. That's what a real design engineer would go through, some just basic measurements, basic calculations like that, and back of the envelope calculations are pretty much all you need in most cases.

**Dave Jones:** And then you do some real measurements, you add in some safety factor, you know, some some fudge factors, you know, you choose a heat sink twice as big as you need as you calculate, stuff like that, and your designs will be a winner.

**Dave Jones:** Catch you next time.
