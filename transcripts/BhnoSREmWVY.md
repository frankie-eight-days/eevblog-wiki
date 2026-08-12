---
video_id: BhnoSREmWVY
title: EEVblog #881 - Fontus Self Filling Water Bottle BUSTED!
url: https://www.youtube.com/watch?v=BhnoSREmWVY
source: youtube-asr
timestamps: {"0": 0, "1": 9, "2": 32, "3": 45, "4": 57, "5": 68, "6": 83, "7": 92, "8": 105, "9": 120, "10": 133, "11": 142, "12": 155, "13": 165, "14": 179, "15": 189, "16": 201, "17": 215, "18": 235, "19": 253, "20": 267, "21": 284, "22": 300, "23": 312, "24": 323, "25": 335, "26": 347, "27": 356, "28": 384, "29": 393, "30": 411, "31": 424, "32": 441, "33": 453, "34": 463, "35": 483, "36": 496, "37": 511, "38": 521, "39": 536, "40": 544, "41": 554, "42": 568, "43": 583, "44": 599, "45": 608, "46": 621, "47": 634, "48": 659, "49": 674, "50": 687, "51": 697, "52": 710, "53": 722, "54": 729, "55": 741, "56": 755, "57": 769, "58": 784, "59": 794, "60": 814, "61": 826, "62": 839, "63": 848, "64": 864, "65": 875, "66": 889, "67": 904, "68": 920, "69": 936}
---

**Dave Jones:** Hi, it's Shonky Product Bustin Time again with love this year on the EE blog. I got many requests for this one and it's been discussed on the forum and various places.

**Dave Jones:** It's the Fontus, the self-filling water bottle on the crowdfunding site of choice Indiegogo. And of course, it has flexible funding, the funding choice of champion scam campaigns everywhere. So, let's check it out and yes, spoiler, it's 100% grade A baloney.

**Dave Jones:** So, what is it? Well, the Fontus creates water out of light and air. And how does it do this? Well, if you go all the way down here, it's a dehumidifier.

**Dave Jones:** And here it is. It uses a solar panel, like a flexible one that you can just unfold and then it's got a Peltier device in there, which then cools down one side and a fan for the air flow.

**Dave Jones:** There's another version for a bike as well, which uses as your bike goes along the ride. Here it is. So, the air flow instead of coming from a fan, it comes from you actually riding your bike.

**Dave Jones:** And it's a dehumidifier. That's it. Peltier device cools down on one side and it extracts water out of the air. Yes, technically possible. But hmm, is it going to work as claimed?

**Dave Jones:** Now, let's bust this thing wide open using a basic principle of thermodynamic systems. It's called latent heat, specific heat. And you can just go on Wikipedia and look this up.

**Dave Jones:** So, in this particular example of dehumidification, what we're looking at is the gas to liquid phase change specifically. And we can get the latent heat of vaporization for this.

**Dave Jones:** Very easy. It's right there in the table on Wikipedia. So, we're going to use the basic equation Q = ML. And this is specifically for heat vaporization. It's not for latent heat fusion, which is the solid to liquid phase change.

**Dave Jones:** We're looking at gas to liquid or vice versa phase change. So, Q is the amount of energy released or absorbed during that particular phase change. In this case, we're actually trying to draw energy from the system.

**Dave Jones:** We're trying to convert from a gas into a liquid. So, this is the energy we have to put into our system, into our Peltier device to actually cool down the air to extract the water.

**Dave Jones:** So, in this case, the units of energy are kilojoules and M equals the mass in kilograms and L is our specific heat. In this particular case, LV, the specific heat of vaporization, which we can get from the table.

**Dave Jones:** So, the amount of energy Q that we have to put into the system in order to cool down the air to convert it to water. And we have a mass of 1 kg of water is what we want.

**Dave Jones:** So, we multiply that by 2264 kilojoules per kilogram. And of course, that's the world's easiest equation. It gives us an answer of 2264 kilojoules. And look, they've got some data.

**Dave Jones:** So, let's use their real data here that they've got very comprehensive table. What this one shows us is how much water the Aero, which is the blue circles. Don't worry about the ride, the bike one.

**Dave Jones:** It can't produce as much water. Let's go for the Aero. The blue circles here, you'll note the size of those represents 1 L of water. So, let's go for the absolute best-case scenario for this thing, okay?

**Dave Jones:** Not the worst case, the absolute best case. What we've got here is the amount of water it can produce, the bubble size in what time on the x-axis here in minutes versus on the y-axis, the humidity and the temperature.

**Dave Jones:** So, let's take the absolute best case here at 90% humidity and 40° C. It's a pretty crap environment, isn't it? It'll take in that condition, let's call that about 150 minutes to produce 1 L of water, 90% humidity, 40° C.

**Dave Jones:** Obviously, as the temperature drops, you're going to produce less and less water even for the same for a given amount of time, even for the same humidity environment. So, this is the absolute best case using their own data that this thing can actually produce.

**Dave Jones:** So, now we can actually do a calculation for 1 hour. Now, they claim to be able to produce 1 L of water in 150 minutes in a 90% humidity environment at 40° C, okay?

**Dave Jones:** Accidentally wrote 99% there. Oops. So, how much energy do we need to put into the system for 1 hour to get that 1 L of water? Well, we can just take the 2264 kJ we got earlier divided by 2.5 because we're 150 minutes and it takes 905 kJ to produce 1 L of water in 1 hour.

**Dave Jones:** And we can work that out in watts. What's kJ? No one knows about kJ. That is equal to 250 W per liter for 1 hour. And of course, that is just the basic thermodynamics.

**Dave Jones:** It's for a 100% efficient system. We haven't talked about anything else involved in like the temperature gradients and everything. Like there's a whole bunch of other stuff. This is 100% efficient system.

**Dave Jones:** So, what does a 250 W solar cell look like to produce 1 L of water in 1 hour? Well, let me show you. This is one of the most efficient 250 W panels.

**Dave Jones:** Look at the size of this thing. It's one of these rooftop installation ones. This will produce 250 W in ideal solar insulation, i.e. middle of summer, the absolute best case conditions.

**Dave Jones:** And also, you've got to track the thing like this, too. You've got to track the sun to get the optimum efficiency out of the damn thing. You've got to be kidding me.

**Dave Jones:** That will fill it up in 1 hour. Ooh. Ooh. But, of course, that's not going to give you 1 L of water cuz they're talking about a 100% efficient system here.

**Dave Jones:** That 250 W panel is 1.5 square meters. Even if you scale that back for the 150 minutes that they uh claimed here, then you would still need 0.6 square meter solar panel with 100% efficiency tracking the sun with solar you know the best solar insulation in the middle of summer else to get their claimed 1 L of water on a but you're not going to get it because it's 100% efficient system.

**Dave Jones:** Oh. You can see how they've just plucked this data out of their ass. But, look at this solar panel. It's got to be like 30 cm uh on a side.

**Dave Jones:** So, 0.1 square meters, 1/6 of the size required to get their claimed data down here at 100% efficiency in the entire system. Like I don't even have to get into Peltier devices and the rest of the thermodynamics of the thing.

**Dave Jones:** Right there, you know their data is busted. 100% grade A [ __ ] And remember, that was ideal case for 40° C 90% humidity environment. It's just going to drop to bugger all.

**Dave Jones:** They are out by several orders of magnitude. So, sorry to anyone who backed this turd because it will not happen. This thing will produce bugger all water and you would have just pissed away your money.

**Dave Jones:** $341,000 with 3 days left. Unbelievable. But, this is what you get when you get a art student. This is from like a university school of art like design arts and things.

**Dave Jones:** And it won all these awards and got you know awarded and got backed every like mentioned everywhere all over the place and it's just back of the envelope stuff.

**Dave Jones:** You can tell they're out by several orders of magnitude. Now, just a quick note about the efficiency there. I've been saying, you know, assuming 100% efficiency. Well, some people might point out that heat pumps that you typically get in your air conditioner and things like that can actually have more than 100% efficiency in terms of pumping heat.

**Dave Jones:** I mean, it might be a 5 kW heat pump in air conditioner, but it might take, you know, 2,000 W or 2 kW for example. So, it can actually be more efficient than that.

**Dave Jones:** But, we're not dealing with your more traditional air con type heat pumps here. We're dealing with a Peltier device. And if we go and have a look at one of the you know, one of the top quality brand one on the market and have a look at the data sheet here for this one.

**Dave Jones:** This is like a 30 W. I've got Yeah, this is a 36 W model that we're going to take a look at here. And it will actually have a graph for the coefficient of performance.

**Dave Jones:** COP, it's called. And here it is here. And you can see that the coefficient of performance one on the Y axis here actually means 100% efficient, okay? And look, it can actually go greater than one.

**Dave Jones:** These Peltier devices can. And this is extremely typical of Peltier devices. They're almost all identical, give or take, you know, a few tens of percent or something like that.

**Dave Jones:** Or, you know, if you get some weird, you know, researchy type one, they can be better. But, that's only at low input voltages, I mean, low currents, low powers.

**Dave Jones:** So, when we're operating here, we're going to be operating this thing at the maximum power possible. So, that figure, the efficiency figure, is actually typically taken for these Peltier devices.

**Dave Jones:** A nominal industry rule of thumb is that about 0.4 to 0.7 coefficient of performance. So, about 40% to 70% efficient. So, the figures we've been looking at eh, it's going to be worse.

**Dave Jones:** Oh, and the different parametric curves here, they're actually for different delta temperatures. That's what DT is. The differential temperature between one plate and the other. So, you know, the higher the temperature difference between the plates, the lower efficiency you actually get.

**Dave Jones:** But, hey, you know, these things can actually be reasonably efficient at low powers with low temperature differentials. But, that's not what we're dealing with here. And of course, there's nothing new here.

**Dave Jones:** No new technology at all. It's just a thermoelectric Peltier effect dehumidifier. And tada! Here's a buyer's guide of all the thermoelectric dehumidifiers on the market. Some of the best ones.

**Dave Jones:** Let's take a look at it. So, if we have a look at this one which they rate is the highest tested moisture removal rate in its class. If we have a look at this this Ivation one, we can actually look at the moisture removal rate and see how much.

**Dave Jones:** And here it is. It's rated by the manufacturer to remove 6 oz of moisture per day from the air. And this one draws about 13 and 1/2 W. And basically exactly what that solar panel will might typically get on a good, you know, cloudless day, you know, good solar insulation, good position, angle, everything else.

**Dave Jones:** 6 oz. I don't know what an ounce is. I had to use my converter. 0.17 L per day. That's for 24 hours continuous operation from that solar panel. You do not get uh, 24 hours of sun.

**Dave Jones:** You get like peak during the day and it it's a curve like this. So, even, you know, like if you're lucky, you might get like, you know, 6 hours of sort of, you know, really good usable energy.

**Dave Jones:** Maybe in summer, 8 hours or something like that. But, you're still not going to You're even if you had it for 24 hours, you're still only going to get .177.

**Dave Jones:** That's one of the best and most efficient tested thermo-electric dehumidifiers on the market. And I really shouldn't even have to mention the stupid bike version. Look, you've got it strapped on the bottom here.

**Dave Jones:** Like, solar panels, are you kidding me? The surface area, the angle's half the side won't be used and your knees will be blocking it. Like, no. Oh, jeez, you'd be lucky to get a couple of watts out of it.

**Dave Jones:** So, if we have a quick look at the ride here, this is the render for the thing, which is very similar to their prototype, which I'll show you in a second.

**Dave Jones:** We have our old friend, look, the storage battery. Why? Because the solar panel's going to do bugger all. And check this out. This is a real hoot. Current status of technical development.

**Dave Jones:** The basic principles of the Fontus technology, atmospheric water generation through condensation, i.e. a dehumidifier, has been proven and tested in monitored conditions. With your support, we will be able enter into a higher development phase, optimize efficiency.

**Dave Jones:** Yeah, you think? Refine the design and provide test data. Because we don't have test data. So, if they don't have any test data, they've just admitted it. Provide test data.

**Dave Jones:** Where did this come from? Came out of their ass, that's where it came from. And more gems, we can't guarantee that Fontus will deliver a constant water output in all conditions and may produce little or no water at all under some conditions.

**Dave Jones:** No [ __ ] Sherlock. So, they've been working on this thing for years and they've got a real flashy video, they're all confident, it's fantastic, everyone's sold, and right down the bottom, here it is.

**Dave Jones:** It's explicitly pointed out that the products which serve as perks are in the development phase. It cannot be excluded that during the development phase, technical, economic, or other circumstances may arise in a delay of the delivery of the perk, production and delivery of the perk in a different form as regards to functionality and or design and non production of the perk.

**Dave Jones:** They're saying, well, if it doesn't work technically and we can't meet our claims, which they can't, then we just not going to deliver it. Suck it in. Thanks for the money though.

**Dave Jones:** So it's done. I don't know what else I have to say about this thing. It's just It's just ridiculous. It's a case This is what happens when you get a timeline like this where they actually do the engineering.

**Dave Jones:** If you have a look at the timeline, they actually did production design, patent filed, Australian design award, company founded and then the Indiegogo campaign we've got down after the Indiegogo campaign.

**Dave Jones:** Oh, they'll just do some technical development and they'll refine it and optimize it. You can't design You can't refine and optimize by several orders of magnitude. They simply failed to do basic engineering, basic physics on this thing.

**Dave Jones:** You've got to obey the laws of thermodynamics. You just can't get around it. You need this sort of energy to put in and then the efficiency of this system and the whole rest of it.

**Dave Jones:** It's busted. So there you go. That's the Fontus, another ridiculous, impractical Indiegogo campaign. You'll get bugger all water from it. Won't be worth your while. And if you want to know a bit more of the physics behind this, Thunderf00t's done an excellent video on this as well.

**Dave Jones:** I'll link that in so check that out. Well, there's only one thing left to do with this and that is to do a community service and post it. I found their address on the university website, so maybe they'll learn something from it.

**Dave Jones:** So here we go. Catch you next time. For me, it's like magic because out of thin air and sun, we are bringing this bottle to fill itself with drinkable water.

**Dave Jones:** A bottle that gives you the freedom to go anywhere. And yes, it's complete [ __ ] But it's not stopped it from being given about a third of a million dollars and featured all over the place.

**Dave Jones:** So, imagine you have a glass of water and you put a seal on the top, the water will establish
