---
video_id: R8hTQXqURB4
title: EEVblog #140 - Battery Capacity Tutorial
url: https://www.youtube.com/watch?v=R8hTQXqURB4
source: youtube-asr
timestamps: {"0": 3, "1": 25, "2": 38, "3": 53, "4": 71, "5": 90, "6": 103, "7": 123, "8": 141, "9": 154, "10": 170, "11": 186, "12": 201, "13": 214, "14": 228, "15": 244, "16": 259, "17": 277, "18": 291, "19": 305, "20": 320, "21": 337, "22": 354, "23": 375, "24": 390, "25": 409, "26": 423, "27": 439, "28": 454, "29": 474, "30": 493, "31": 508, "32": 526, "33": 538, "34": 554, "35": 570, "36": 586, "37": 603, "38": 618, "39": 635, "40": 652, "41": 666, "42": 679, "43": 693, "44": 708, "45": 725, "46": 740, "47": 757, "48": 777, "49": 792, "50": 805, "51": 824, "52": 842, "53": 858, "54": 873, "55": 887, "56": 905, "57": 924, "58": 943, "59": 959, "60": 977, "61": 994, "62": 1011, "63": 1028, "64": 1043, "65": 1060, "66": 1078, "67": 1094, "68": 1113, "69": 1132, "70": 1146, "71": 1164, "72": 1180, "73": 1196, "74": 1218, "75": 1238, "76": 1254, "77": 1268, "78": 1288, "79": 1304, "80": 1318, "81": 1334, "82": 1349, "83": 1367, "84": 1382, "85": 1395, "86": 1411, "87": 1427, "88": 1443, "89": 1463, "90": 1477, "91": 1491, "92": 1504, "93": 1522, "94": 1538, "95": 1557, "96": 1570, "97": 1588, "98": 1605, "99": 1625, "100": 1642, "101": 1653, "102": 1668, "103": 1685, "104": 1699, "105": 1718}
---

**Dave Jones:** Hi, welcome to the AEVblog, an electronic engineering video blog of interest to anyone involved in electronic design. I'm your host, Dave Jones. Hi, there's one very misunderstood aspect of electronics, and that's the humble battery, or more precisely, battery capacity. How much energy does

**Dave Jones:** one of these things hold? How much current can you get out of it? For how long? How long can you power your device for? How do you do the calculations? Well, it's a very good question, and a lot of people don't know the finer

**Dave Jones:** details of it. So, I thought we'd have a tutorial on battery capacity. Now, I'm sure everyone's familiar with a standard AA rechargeable battery. And look at the number on it, 2300. And I'm sure you're familiar with that figure,

**Dave Jones:** you know, 2300 milliamp hours, 2800 milliamp hours. And you think that's the capacity of the battery measured in milliamp hours. Well, is it? Well, not really. There's a lot more to it. That figure is very nominal figure. It's

**Dave Jones:** borderline So, what is the capacity of a battery? Well, the battery capacity is the ability of a battery to supply a constant current or a constant amount of energy into a load for a given amount of time. Simple as that.

**Dave Jones:** So, how do you characterize battery capacity? Well, you can do it in two different ways. There's two ways to specify it. The first and probably the most common is, you've probably seen it, amp hours or milliamp hours. It's

**Dave Jones:** specified AH or mAh, as the case may be. Now, this isn't strictly the correct way to specify battery capacity, cuz it makes some assumptions. It assumes that uh it's it it ignores totally ignores the voltage change in the battery and it

**Dave Jones:** assumes that you've got a constant current load and not all loads are like that, which we'll go into. But basically the capacity, let's say a battery is rated for 1 amp hour here, well that means it can deliver 1 amp for 1 hour or

**Dave Jones:** uh it can deliver .1 amps for 10 hours and so forth and so forth as you go as you drop in current. Usually, that's the upper limit. So 1 amp hour battery, you might be able to draw 2 amp hours from it, but the

**Dave Jones:** performance, the capacity is going to be much less. And the second way to define battery capacity is in what's called watt hours or Wh and you can get milliwatt hours and stuff like that as well. Same for milliamp hours up here. Now, this is the

**Dave Jones:** true, the only true way to measure the actual capacity of the battery. It actually measuring the true amount of energy in there because it takes into account the current and the voltage. Watts, V * I, Ohm's law, right? So

**Dave Jones:** um it doesn't make any assumptions at all. It's the true capacity. And it's the same thing for milliamp hours up here. What if you're if it's specified if you've got a 1 watt hour battery, it means it can deliver 1 watt for 1 hour

**Dave Jones:** or .1 watts for 10 hours and so forth. And once again, you can go higher than that. A 1 watt hour battery, you might be able to draw 2 watts for half an hour, but probably not. It's usually

**Dave Jones:** going to be less than that. So measuring in milliamp hours, capacity in milliamp hours is only valid if you assume that the battery voltage is constant. Now, let's take a look at this. It all comes down to what's called

**Dave Jones:** the discharge curve or the discharge characteristic curve of a battery. Now, there's lots of different batteries out there, lots of different technologies, and the curves, the characteristic curves, will all be different shapes, but they will all have a characteristic

**Dave Jones:** curve. No battery is perfect. Now, take the case of an ideal battery, okay? What a discharge curve is is the battery voltage on the Y axis in volts, in this case 1.5 volts for a, you know, double A

**Dave Jones:** a standard single cell alkaline cell everyone's familiar with, versus time on the X axis. Now, an ideal battery in this case is the one in red. It will start out at 1.5 volts, and it will stay at 1.5 volts for all of the

**Dave Jones:** time that you are discharging, powering your product, and then all of a sudden it will just die and drop straight off. That's called a brick wall response, an ideal brick wall response, and no battery will even ever come close to

**Dave Jones:** giving you that. It'll have a charac- characteristic curve, which is this green line down here, and it'll start out at say 1.5, it'll drop fairly quickly, it might flatten out and go or go a bit that or just drop at a linear

**Dave Jones:** rate for a while, and then curve off right at the end. And that's the true performance. Now, as you'll see with this laptop battery, its capacity is rated in milliamp hours and also in watt hours as well. What does that mean? What's the

**Dave Jones:** difference? Well, there's not really much difference in this in for this actual application because what they do to calculate the watt hours is they just take a nominal voltage figure. They don't actually take into account, they they just choose a nominal figure

**Dave Jones:** in the middle of the curve here somewhere. They don't actually take into account the full change in voltage, usually, anyway. So, there's not much difference, but watt hours is technically a better way to rate battery capacity. Or it's also the way that they

**Dave Jones:** actually rate the different technologies: alkaline, nickel-metal hydride, lithium-ion, lithium polymer, all that sort of stuff. It's um the capacity of those type of batteries and those battery technologies is rated in uh watt hours per something. So it's watt hours per kilogram of battery

**Dave Jones:** material. So just how much energy is in your humble double A or triple A battery? Well, it might surprise you. In fact, it might surprise you a lot. Now, because we're talking watt hours, watt hour, that's energy. So we can also talk

**Dave Jones:** joules as well. It's a direct relationship. Now, uh one joule here equals one watt second, not watt hour. So uh to get your energy in joules, you have to multiply your watt hour figure by 3,600 cuz there's 3,600 seconds in an hour. So if

**Dave Jones:** you do that and you look at a double a triple A and a double A battery, your triple A battery, 1.4 watt hours maybe, you know, it varies a lot and as we'll go into. Um and that's equivalent to about 5,000

**Dave Jones:** odd joules or thereabouts. A double A battery, 2.5 watt hours roughly or 9,000 joules. Okay? Don't even mention your huge uh D cell battery or something like that. These tiny little batteries. Now, to give you an idea of what many, many

**Dave Jones:** thousands of joules can do, you may have seen this video before. My friend Doug Ford and I blew up blew the out of a multimeter with 400 joules.

**Dave Jones:** That's right, 400. That even a triple A battery has over 10 times that amount of energy in it. It's incredible. So, why can't you blow up a multimeter into flames and make it explode with a AAA battery? Well, it all comes down to the internal

**Dave Jones:** resistance. So, internal resistance of a battery limits its capability to get the energy out of it and to do some serious damage. Even though there's a massive amount of energy stored in the chemicals in these batteries, a humble AAA or AA battery, a

**Dave Jones:** massive amount of energy, you can actually extract it. If you actually extracted the energy out of this and stored it in a massive big capacitor bank at large voltages with very low ESR and it's able to dump that energy, then

**Dave Jones:** you can well and truly blow a multimeter or something else to dust with a AAA battery. It's amazing. So, how do you actually measure the capacity of the battery? Well, if you look at the discharge curve again, that's the green one here, the capacity

**Dave Jones:** of any battery is the total area under that curve. And you know and you may know that the area under the curve is an integral. So, if you know how you how to do your integrals and you've got the

**Dave Jones:** actual data, you can do an integral of it. But, we won't do that. The other the easier way to actually do it, the more traditional method, is to log the voltage and the current from the battery for a given load. So, it must be at a

**Dave Jones:** given load and then you measure the voltage and the current at regular intervals all the way along and then you can calculate from that the total watt-hour capacity of the battery. And that's how it's traditionally done. What actually is the

**Dave Jones:** difference between the watt-hour capacity and the amp-hour capacity? Is there any major practical difference in practice? Well, the answer is not often. That's why a lot of batteries will be specified in amp hour capacity and their discharge will be assumed to be a

**Dave Jones:** constant current load. Now, the reason for this is fairly simple. Now, we've already mentioned that the true capacity of a battery is measured in watt hours and it's the total area under the curve under the green discharge curve there, which makes sense. But, if

**Dave Jones:** you want to make the If you want to measure the or specify the amp hour capacity of a battery, then you just assume a nominal voltage like that across there. You know, it might be 1.2 volts or something like that. Now,

**Dave Jones:** uh and for a nominal constant current load as well. Now, what happens in that case when you make those assumptions, you're actually measuring this area in here, which you normally shouldn't be, okay? So, there's going to be some extra

**Dave Jones:** capacity there, but you're not measuring this one up here. So, they can kind of sort of cancel each other out in terms of area. So, that's why the constant current amp hour capacity at a certain constant current load

**Dave Jones:** might often be similar to the watt hour capacity or the true capacity of the battery. So, what sort of things can affect battery capacity? It turns out there's quite a lot of things that can actually affect it. Number one, and

**Dave Jones:** we'll go through all these in detail later, but number one, the cutoff voltage that you choose to use in your circuit or the product you've got. Number two, the temperature of the battery, not just the ambient temperature, but we'll go into that. The

**Dave Jones:** discharge current or the discharge power or whatever you determine the discharge rate. The shelf life of the battery will affect it as well. If it's a 2-year-old battery, it will have lost some of its initial capacity. And then you've got

**Dave Jones:** the self-discharge as well. Some batteries are a lot better than others self-discharge, and that's tied into shelf life there as well. So, let's look at these. Okay, now let's take a look at some real data sheets. I've got an Energizer AA

**Dave Jones:** here. It's an alkaline AA standard Energizer. You know it, you've used it. And let's take a look at the effect of the cutout voltage on your actual product. So, if you're actually designing a product, and let's actually take a look at the discharge a typical

**Dave Jones:** discharge curve right here. Now, if you're actually designing a product, here is here is the voltage of the battery. Now, if you design your product to cut out at say or give you a low battery warning error at say 1.1 V here,

**Dave Jones:** then bingo, look at all this capacity under the curve here that you're throwing away. You're just pissing away all of that battery capacity. Now, it gets even worse if you do 1.2. Look at 1.2 V. If you set it to cut out at

**Dave Jones:** that, you're wasting half of your battery capacity. It's crazy. So, a well-designed product will have as low a cutout voltage as possible. And for an alkaline, that's about 0.8 V. A superbly designed product will operate all the way down to 0.8 V

**Dave Jones:** per cell. So, when you're actually designing your circuit to work off AA or AAA alkaline cells or primary cells, these are the voltages that you should design your product to work down to. Ideally, if you want to use the most

**Dave Jones:** capacity inside this battery that you can, then this is what you should do. For a single cell, 0.8 V as I said, because that just drops off like a brick wall down at 0.8 V there. So, but a

**Dave Jones:** two-cell design, normally 3-V, 1.6-V is the is what you want it to work down to. Three-cell and four-cell a nominal 6-V system, 3.2-V down to. And a six-cell system or your standard 9-V battery like this, ideally, your product should work down to 4.8-V.

**Dave Jones:** And this is why in my product reviews, you will see that I actually measure the the cutout voltage of the battery. So, if a multimeter's working from this 9-V battery and its cutout voltage is, you know, 6.5 or 7-V as some of them are

**Dave Jones:** or even higher, then they're just pissing away a ton of capacity in the battery. It's crazy. Don't do it. Now, one of the big things that affects batteries, particularly alkaline cells, is the temperature. Not just the ambient temperature, but the temperature of the

**Dave Jones:** cell as well. And in particular, low temperatures. Now, this is the Energizer L91. It's a AA, but it's one of these lithium. It's a lithium ion disulfide battery. And you've probably seen it, you've probably heard how great they are

**Dave Jones:** and how they work it at low temperatures and how they work at higher discharge currents and all that. But, they've actually got some some well, they've got some charts down here for the temperature. And let's take a look at them where they compare the

**Dave Jones:** this lithium to a standard alkaline cell. Now, these dark bars here represent the lithium battery. And these ones and the other one, they represent the alkaline. And as you can see, this is at cold temperature here, 0° C, and

**Dave Jones:** this is at room temperature, 21° C over here. Now, as you can see, at room temperature, at different discharge currents, you can see how the lithium totally outperforms the alkaline cell. But, the interesting thing to note is that notice the level of the alkaline

**Dave Jones:** cells here, here, here, and here. Now, that's at room temperature, 21°. Once you take them down to 0°, look, they're really dropped. They've more than halved. So, you're losing a lot of your capacity, especially at the high discharge temperatures. Now, that's

**Dave Jones:** pretty obvious when you take a look at the reason for it. It's pretty obvious. If you take a look at a temperature uh curve here, basically the uh series resistance in the cell versus temperature on the x-axis here, this is

**Dave Jones:** positive temperature, this is 40° up here, and -40° down here. You will see that as the temperature decreases, the series resistance in the cell increases. So, you're going to lose capacity due to your IR increasing. And, of course, the discharge current

**Dave Jones:** affects the capacity greatly as well. Now, as you can see, we've got the capacity of the battery in milliamp hours up here from 0 to 3,000, and different discharge currents, 25 milliamps up to 500 milliamps. As you can see, at 25 uh 25 milliamps, quite

**Dave Jones:** low discharge current for a AA battery, it's capacitally its capacity is a nominal, say, 2,800 uh milliamp hours. And, that's the figure that you'll typically hear about. But, hey, if you go to 500 milliamps, then the capacity is

**Dave Jones:** Look, it's only about 1,200 milliamp hours, a big difference. And, if you take a look at shelf life here, then you can see that after it's got to after 7 years from the date of manufacture at 21° C, it's only going to have 80% of

**Dave Jones:** its initial capacity. Now, that those figures aren't often true. It depends on the actual manuf- the manufacturing quality of this particular batch of it, you can't always rely on that figure strictly. So, take it with a grain of

**Dave Jones:** salt. Now comes the big reason why batteries have the discharge characteristic curve that they do and why it's not ideal like that. It's because of the internal resistance of the battery. Now, the internal resistance or the IR or

**Dave Jones:** sometimes called the ESR of the battery, the equivalent series resistance, is actually made up of two different types of resistances in series. One is the electrical resistance and that's like the internal metal contacts and things like that internal to the construction

**Dave Jones:** of the battery. And the other part is the ion what's called the ionic resistance or the electrochemical reaction inside the battery and that's to do with the electrolyte, you know, the conductivity of the electrolyte, the surface area of the electrode and

**Dave Jones:** polarization and that sort of stuff. And this one acts much slower than the electrical resistance. The electrical resistance will actually will always be there bang straight on, but the ionic resistance has a bit of lag, so it will only show up under um

**Dave Jones:** under pulse conditions. Now, as you can see, this is the data sheet for a CR2032 coin cell battery, which all familiar with, and it just happens so happens to have a pulse characteristic graph like this, which actually is the method used to measure these two

**Dave Jones:** different types of resistances down here. And you can actually see when you apply a pulse like this, this is the battery voltage in volts up here and this is time over here. And as you can see, if you apply a pulse bang here,

**Dave Jones:** then it drops down suddenly. And that part there, the very steep part, is the electrical resistance down here which works straight away. Okay, it's always there and then the ionic then after some time the ionic resistance will kick in

**Dave Jones:** and go like that. It'll take some time but it'll eventually settle down to a fixed value. And the total IR that you see in the graphs here, here's a graph of the IR versus the um versus the characteristic uh

**Dave Jones:** characteristic discharge curve. Uh you'll see that the IR is just one particular value which they'll actually specify up here in the data sheet. There it is, typical IR will start out at 10 ohms and increase to 40 ohms at the end

**Dave Jones:** of its life. Now, what I love about this particular discharge characteristic graph is it shows beautifully, it's splendid, how the IR increases at the same rate as the uh characteristic discharge curve decreases. Now, I've actually made a transparency of this. Look, okay? Now,

**Dave Jones:** it's no coincidence that if we flip that over look what happens. It matches the discharge characteristic curve almost exactly. Magic, huh? And of course, when you're talking about battery capacity, the load type is all important. Now, there are three

**Dave Jones:** different types of loads and you might see uh these three types, in fact, you might see all three types on a particular data sheet for a battery. Now, the most common is the constant current load type. Now, the second type

**Dave Jones:** is the constant resistance type and as it says, it's a resistance. So, to test that, they literally put, you know, a 10 ohm or 100 ohm resistor across the battery and that's it. Well, most circuits aren't going to be constant

**Dave Jones:** resistance, are they? Really, you know, they're going to actually be constant current or the third type, which is constant power. Now, this is probably the most accurate one for most circuits you're going to actually design, most products, which is why the watt hour

**Dave Jones:** capacity, cuz watt hours is power, okay? Watts is power. So, the constant power graph might be more important for you. If you've got a DC to DC converter circuit driving driving your particular circuit, then you probably might want to

**Dave Jones:** look at the constant power graph instead of the constant current or constant resistance characteristic graphs. And in a previous blog, I've showed how you can design a simple dummy load that can actually do all three of these in

**Dave Jones:** one. It's just got an op-amp, a FET, and a load resistor down here. And by hooking the In my example in the previous blog, I just hooked this up to a voltage source of pot, and that just worked as a constant current load. But,

**Dave Jones:** if you hook up if you feed this back if you feed the voltage back to a microcontroller and you actually control the input if you feed a via a DAC. So, if you're using intelligent micro in there, you can actually, by doing some

**Dave Jones:** simple Ohm's law calculations on the fly and actually changing this as the thing discharges, you can generate a constant resistance or a constant power in this load. So, this is a pretty handy way to measure battery capacity. And there's actually a fourth type of

**Dave Jones:** load as well, and that is the pulse load. And the pulse load can actually apply to any three of these types, and it just means that they'll typically have, if this is say current up here, then they might actually pulse it like

**Dave Jones:** this. They might have a steady low current down here and pulse it to a high current periodically. And as you can see, a good data sheet will actually have constant power performance curves and will also have constant current

**Dave Jones:** performance curves. And down here, it's got these what they call industry standard tests and they're based on old, you know, transistor radio kind of things and they're actually constant resistance tests. In this case, 43 ohms for 4 hours per day and stuff like that.

**Dave Jones:** They give service hours. So, you need to pick the performance graph that you think is acceptable for for the particular type of load that your product is going to represent. So, how do you calculate the battery life of your particular product? Well,

**Dave Jones:** as I said, you've got to pick the type of load which is typical of your product, constant current, constant power, constant resistance, whatever. It may be a combination, maybe it's got some pulse stuff as well. But, generally speaking, it's actually pretty darn hard

**Dave Jones:** to get a really accurate estimate of the battery life for your product based on just the characteristic curves in the data sheet. Really, if you're serious about it, there is no substitute for actually measuring the actual battery life in your actual

**Dave Jones:** product. And often, that is just what you have to do. You simply don't have enough data available to actually make a true calculation. So, you've just got to suck it and see. I mean, sometimes you can just, you know, rules of thumb,

**Dave Jones:** ballpark stuff. You know, if a battery's you know, 2,000 milliamp hours and you know it's going to roughly draw 50 milliamps plus minus 25, something like that, you can assume it's constant current and you can just, well, do the

**Dave Jones:** simple figures and calculate it's going to have X amount of life. And typically, those ballpark figures are usually pretty good. You might drop it down by, you know, 30% or calculate it and then drop it back by 30%, but really, it's

**Dave Jones:** just a guess. Now, of course, sometimes it's okay to just go, "Eh, near enough. And well, my circuit's got a DC-to-DC converter and it's delivering a constant power into my product. And because the efficiency curve is is doesn't drop off too much,

**Dave Jones:** you can say that there's a constant input power from the battery as well. And well, everything's hunky-dory." And you can get some reasonably accurate ballpark measurements from that. So, it's it's not bad engineering at all to just wet the finger and go, "Eh, near

**Dave Jones:** enough. In the ballpark." Especially for first-order calculations, just for product viability and general comparison work. Estimations are great. So, there you have it. Let's go through a quick summary or a cheat sheet of what battery capacity is all about. Now, number one,

**Dave Jones:** it's all about the battery cutoff voltage. There's absolutely no point specifying the capacity of a battery if you don't know what the cutoff if you don't specify or know what the cutoff voltage is. It's crazy. Second, if you

**Dave Jones:** increase the current or increase the load uh current, then you decrease the overall capacity of the battery due to IR. If you decrease the temperature, you decrease the capacity. And remember, that's the temperature of the cell, not necessarily the ambient temperature

**Dave Jones:** because the cell can heat up due to IR down here. Now, you've got to know your load type, constant current, constant power, constant resistance. Choose the one that's most appropriate for your particular product when you're dealing with the graphs. Um and if you're

**Dave Jones:** serious, use watt-hour plus constant power because true watt-hour, that is the true capacity of the battery. Milliamp hours is a bit of a guestimate, okay? And the really the only way to measure true capacity and battery life in your particular product is to

**Dave Jones:** actually measure it in your circuit. Do some real-world test. And IR is everything. It's all about the internal resistance of the battery. And that means power wasted in your product, just pissed away because you've got this X current. If you try and draw too much

**Dave Jones:** current from a you know, a double A battery, if you try and draw 2 amps out of this thing or 4 amps or 5 amps, it's just not going to do it because of the internal resistance. It's going to heat

**Dave Jones:** up, it's going to have a short life, and your characteristic curves aren't worth squat. Now, no talk about battery capacity would be complete without mentioning it a rather obscure law, which not very often used. A lot of people wouldn't

**Dave Jones:** have even heard of it, but you may come across it's worth mentioning briefly, Peukert's law. And it basically is the reduction in capacity at higher currents, as we've seen and discussed in the characteristic curves and all the rest of it. Okay? And it's actually a

**Dave Jones:** more complex formula than this. This is a simplified version, but this is most commonly used. Basically, T equals C on I to the power of K, where K is Peukert's constant, which is actually an empirical measured value for the

**Dave Jones:** battery. 1.0 being ideal, 1.2 might be typical, something like that for a battery. T is the discharge time, theoretical capacity, and the discharge current. So, as you can see, the the actual the discharge time goes down if if K

**Dave Jones:** actually goes up, the constant. So, your nominal, you know, 1 amp hour battery might drop to you know, 0.8 amp hours or something like that. Look it up if you want to know more.
