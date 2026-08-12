---
video_id: BhnoSREmWVY
title: EEVblog #881 - Fontus Self Filling Water Bottle BUSTED!
url: https://www.youtube.com/watch?v=BhnoSREmWVY
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 38, "3": 53, "4": 65, "5": 83, "6": 95, "7": 109, "8": 125, "9": 137, "10": 151, "11": 165, "12": 181, "13": 193, "14": 207, "15": 225, "16": 242, "17": 257, "18": 274, "19": 290, "20": 307, "21": 320, "22": 335, "23": 353, "24": 367, "25": 381, "26": 397, "27": 416, "28": 434, "29": 451, "30": 465, "31": 479, "32": 494, "33": 507, "34": 518, "35": 534, "36": 546, "37": 562, "38": 580, "39": 597, "40": 610, "41": 624, "42": 639, "43": 657, "44": 678, "45": 689, "46": 704, "47": 717, "48": 729, "49": 743, "50": 761, "51": 775, "52": 790, "53": 803, "54": 816, "55": 828, "56": 842, "57": 857, "58": 872, "59": 885, "60": 899, "61": 910, "62": 929}
---

**Dave Jones:** Hi, it's Shonky Product Bustin Time again with love this year on the EE blog. I got many requests for this one and it's been discussed on the forum and various places. It's the Fontus, the self-filling water bottle on the

**Dave Jones:** crowdfunding site of choice Indiegogo. And of course, it has flexible funding, the funding choice of champion scam campaigns everywhere. So, let's check it out and yes, spoiler, it's 100% grade A baloney. So, what is it? Well, the Fontus creates water out of light and

**Dave Jones:** air. And how does it do this? Well, if you go all the way down here, it's a dehumidifier. And here it is. It uses a solar panel, like a flexible one that you can just unfold and then it's got a Peltier

**Dave Jones:** device in there, which then cools down one side and a fan for the air flow. There's another version for a bike as well, which uses as your bike goes along the ride. Here it is. So, the air flow

**Dave Jones:** instead of coming from a fan, it comes from you actually riding your bike. And it's a dehumidifier. That's it. Peltier device cools down on one side and it extracts water out of the air. Yes, technically possible. But hmm,

**Dave Jones:** is it going to work as claimed? Now, let's bust this thing wide open using a basic principle of thermodynamic systems. It's called latent heat, specific heat. And you can just go on Wikipedia and look this up. So, in this

**Dave Jones:** particular example of dehumidification, what we're looking at is the gas to liquid phase change specifically. And we can get the latent heat of vaporization for this. Very easy. It's right there in the table on Wikipedia. So, we're going

**Dave Jones:** to use the basic equation Q = ML. And this is specifically for heat vaporization. It's not for latent heat fusion, which is the solid to liquid phase change. We're looking at gas to liquid or vice versa phase change. So, Q

**Dave Jones:** is the amount of energy released or absorbed during that particular phase change. In this case, we're actually trying to draw energy from the system. We're trying to convert from a gas into a liquid. So, this is the energy we have

**Dave Jones:** to put into our system, into our Peltier device to actually cool down the air to extract the water. So, in this case, the units of energy are kilojoules and M equals the mass in kilograms and L is our specific heat. In this particular

**Dave Jones:** case, LV, the specific heat of vaporization, which we can get from the table. So, the amount of energy Q that we have to put into the system in order to cool down the air to convert it to water. And we have a mass of 1 kg of

**Dave Jones:** water is what we want. So, we multiply that by 2264 kilojoules per kilogram. And of course, that's the world's easiest equation. It gives us an answer of 2264 kilojoules. And look, they've got some data. So, let's use their real

**Dave Jones:** data here that they've got very comprehensive table. What this one shows us is how much water the Aero, which is the blue circles. Don't worry about the ride, the bike one. It can't produce as much water. Let's go for the Aero. The

**Dave Jones:** blue circles here, you'll note the size of those represents 1 L of water. So, let's go for the absolute best-case scenario for this thing, okay? Not the worst case, the absolute best case. What we've got here is the amount of water it

**Dave Jones:** can produce, the bubble size in what time on the x-axis here in minutes versus on the y-axis, the humidity and the temperature. So, let's take the absolute best case here at 90% humidity and 40° C. It's a pretty crap environment, isn't

**Dave Jones:** it? It'll take in that condition, let's call that about 150 minutes to produce 1 L of water, 90% humidity, 40° C. Obviously, as the temperature drops, you're going to produce less and less water even for the same for a given

**Dave Jones:** amount of time, even for the same humidity environment. So, this is the absolute best case using their own data that this thing can actually produce. So, now we can actually do a calculation for 1 hour. Now, they claim to be able

**Dave Jones:** to produce 1 L of water in 150 minutes in a 90% humidity environment at 40° C, okay? Accidentally wrote 99% there. Oops. So, how much energy do we need to put into the system for 1 hour to get

**Dave Jones:** that 1 L of water? Well, we can just take the 2264 kJ we got earlier divided by 2.5 because we're 150 minutes and it takes 905 kJ to produce 1 L of water in 1 hour. And we can work that out in watts. What's

**Dave Jones:** kJ? No one knows about kJ. That is equal to 250 W per liter for 1 hour. And of course, that is just the basic thermodynamics. It's for a 100% efficient system. We haven't talked about anything else involved in like the temperature

**Dave Jones:** gradients and everything. Like there's a whole bunch of other stuff. This is 100% efficient system. So, what does a 250 W solar cell look like to produce 1 L of water in 1 hour? Well, let me show you.

**Dave Jones:** This is one of the most efficient 250 W panels. Look at the size of this thing. It's one of these rooftop installation ones. This will produce 250 W in ideal solar insulation, i.e. middle of summer, the absolute best case

**Dave Jones:** conditions. And also, you've got to track the thing like this, too. You've got to track the sun to get the optimum efficiency out of the damn thing. You've got to be kidding me. That will fill it up in 1 hour. Ooh. Ooh.

**Dave Jones:** But, of course, that's not going to give you 1 L of water cuz they're talking about a 100% efficient system here. That 250 W panel is 1.5 square meters. Even if you scale that back for the 150 minutes that they uh claimed here, then

**Dave Jones:** you would still need 0.6 square meter solar panel with 100% efficiency tracking the sun with solar you know the best solar insulation in the middle of summer else to get their claimed 1 L of water on a but you're not going to get

**Dave Jones:** it because it's 100% efficient system. Oh. You can see how they've just plucked this data out of their ass. But, look at this solar panel. It's got to be like 30 cm uh on a side. So, 0.1 square meters,

**Dave Jones:** 1/6 of the size required to get their claimed data down here at 100% efficiency in the entire system. Like I don't even have to get into Peltier devices and the rest of the thermodynamics of the thing. Right there, you know their data is busted.

**Dave Jones:** 100% grade A [ __ ] And remember, that was ideal case for 40° C 90% humidity environment. It's just going to drop to bugger all. They are out by several orders of magnitude. So, sorry to anyone who backed this turd because

**Dave Jones:** it will not happen. This thing will produce bugger all water and you would have just pissed away your money. $341,000 with 3 days left. Unbelievable. But, this is what you get when you get a art student. This is from

**Dave Jones:** like a university school of art like design arts and things. And it won all these awards and got you know awarded and got backed every like mentioned everywhere all over the place and it's just back of the envelope stuff. You can tell

**Dave Jones:** they're out by several orders of magnitude. Now, just a quick note about the efficiency there. I've been saying, you know, assuming 100% efficiency. Well, some people might point out that heat pumps that you typically get in your air

**Dave Jones:** conditioner and things like that can actually have more than 100% efficiency in terms of pumping heat. I mean, it might be a 5 kW heat pump in air conditioner, but it might take, you know, 2,000 W or 2 kW for example. So,

**Dave Jones:** it can actually be more efficient than that. But, we're not dealing with your more traditional air con type heat pumps here. We're dealing with a Peltier device. And if we go and have a look at one of the you know, one of the top

**Dave Jones:** quality brand one on the market and have a look at the data sheet here for this one. This is like a 30 W. I've got Yeah, this is a 36 W model that we're going to take a look at

**Dave Jones:** here. And it will actually have a graph for the coefficient of performance. COP, it's called. And here it is here. And you can see that the coefficient of performance one on the Y axis here actually means 100% efficient, okay? And

**Dave Jones:** look, it can actually go greater than one. These Peltier devices can. And this is extremely typical of Peltier devices. They're almost all identical, give or take, you know, a few tens of percent or something like that. Or, you know, if

**Dave Jones:** you get some weird, you know, researchy type one, they can be better. But, that's only at low input voltages, I mean, low currents, low powers. So, when we're operating here, we're going to be operating this thing at the

**Dave Jones:** maximum power possible. So, that figure, the efficiency figure, is actually typically taken for these Peltier devices. A nominal industry rule of thumb is that about 0.4 to 0.7 coefficient of performance. So, about 40% to 70% efficient. So, the figures we've been

**Dave Jones:** looking at eh, it's going to be worse. Oh, and the different parametric curves here, they're actually for different delta temperatures. That's what DT is. The differential temperature between one plate and the other. So, you know, the higher the temperature difference

**Dave Jones:** between the plates, the lower efficiency you actually get. But, hey, you know, these things can actually be reasonably efficient at low powers with low temperature differentials. But, that's not what we're dealing with here. And of course, there's nothing new here. No new

**Dave Jones:** technology at all. It's just a thermoelectric Peltier effect dehumidifier. And tada! Here's a buyer's guide of all the thermoelectric dehumidifiers on the market. Some of the best ones. Let's take a look at it. So, if we have a look at this one which they

**Dave Jones:** rate is the highest tested moisture removal rate in its class. If we have a look at this this Ivation one, we can actually look at the moisture removal rate and see how much. And here it is. It's rated by the manufacturer to remove

**Dave Jones:** 6 oz of moisture per day from the air. And this one draws about 13 and 1/2 W. And basically exactly what that solar panel will might typically get on a good, you know, cloudless day, you know, good solar

**Dave Jones:** insulation, good position, angle, everything else. 6 oz. I don't know what an ounce is. I had to use my converter. 0.17 L per day. That's for 24 hours continuous operation from that solar panel. You do not get uh, 24 hours of sun. You get like peak

**Dave Jones:** during the day and it it's a curve like this. So, even, you know, like if you're lucky, you might get like, you know, 6 hours of sort of, you know, really good usable energy. Maybe in summer, 8 hours

**Dave Jones:** or something like that. But, you're still not going to You're even if you had it for 24 hours, you're still only going to get .177. That's one of the best and most efficient tested thermo-electric dehumidifiers on the market. And I

**Dave Jones:** really shouldn't even have to mention the stupid bike version. Look, you've got it strapped on the bottom here. Like, solar panels, are you kidding me? The surface area, the angle's half the side won't be used and your knees will be

**Dave Jones:** blocking it. Like, no. Oh, jeez, you'd be lucky to get a couple of watts out of it. So, if we have a quick look at the ride here, this is the render for the thing, which is very similar to their prototype, which

**Dave Jones:** I'll show you in a second. We have our old friend, look, the storage battery. Why? Because the solar panel's going to do bugger all. And check this out. This is a real hoot. Current status of technical development. The basic

**Dave Jones:** principles of the Fontus technology, atmospheric water generation through condensation, i.e. a dehumidifier, has been proven and tested in monitored conditions. With your support, we will be able enter into a higher development phase, optimize efficiency. Yeah, you think? Refine the design and provide

**Dave Jones:** test data. Because we don't have test data. So, if they don't have any test data, they've just admitted it. Provide test data. Where did this come from? Came out of their ass, that's where it came from. And more gems, we can't

**Dave Jones:** guarantee that Fontus will deliver a constant water output in all conditions and may produce little or no water at all under some conditions. No [ __ ] Sherlock. So, they've been working on this thing for years and they've got a real flashy video, they're

**Dave Jones:** all confident, it's fantastic, everyone's sold, and right down the bottom, here it is. It's explicitly pointed out that the products which serve as perks are in the development phase. It cannot be excluded that during the development phase, technical,

**Dave Jones:** economic, or other circumstances may arise in a delay of the delivery of the perk, production and delivery of the perk in a different form as regards to functionality and or design and non production of the perk. They're saying,

**Dave Jones:** well, if it doesn't work technically and we can't meet our claims, which they can't, then we just not going to deliver it. Suck it in. Thanks for the money though. So it's done. I don't know what else I

**Dave Jones:** have to say about this thing. It's just It's just ridiculous. It's a case This is what happens when you get a timeline like this where they actually do the engineering. If you have a look at the timeline, they actually did production

**Dave Jones:** design, patent filed, Australian design award, company founded and then the Indiegogo campaign we've got down after the Indiegogo campaign. Oh, they'll just do some technical development and they'll refine it and optimize it. You can't design You can't refine and

**Dave Jones:** optimize by several orders of magnitude. They simply failed to do basic engineering, basic physics on this thing. You've got to obey the laws of thermodynamics. You just can't get around it. You need this sort of energy to put in and then the efficiency of

**Dave Jones:** this system and the whole rest of it. It's busted. So there you go. That's the Fontus, another ridiculous, impractical Indiegogo campaign. You'll get bugger all water from it. Won't be worth your while. And if you want to know a bit

**Dave Jones:** more of the physics behind this, Thunderf00t's done an excellent video on this as well. I'll link that in so check that out. Well, there's only one thing left to do with this and that is to do a community service and post it. I

**Dave Jones:** found their address on the university website, so maybe they'll learn something from it. So here we go.

**Dave Jones:** Catch you next time. For me, it's like magic because out of thin air and sun, we are bringing this bottle to fill itself with drinkable water. A bottle that gives you the freedom to go anywhere. And yes, it's complete [ __ ] But

**Dave Jones:** it's not stopped it from being given about a third of a million dollars and featured all over the place. So, imagine you have a glass of water and you put a seal on the top, the water will establish
