---
video_id: gAu8CvMjDrU
title: 15kWh AERL LFP Home Storage Battery - First Analysis
url: https://www.youtube.com/watch?v=gAu8CvMjDrU
source: youtube-asr
timestamps: {"0": 0, "1": 9, "2": 23, "3": 36, "4": 46, "5": 56, "6": 67, "7": 78, "8": 85, "9": 101, "10": 122, "11": 133, "12": 143, "13": 158, "14": 168, "15": 186, "16": 198, "17": 206, "18": 224, "19": 236, "20": 246, "21": 259, "22": 273, "23": 295, "24": 306, "25": 316, "26": 345, "27": 358, "28": 386, "29": 397, "30": 407, "31": 427, "32": 447, "33": 460, "34": 471, "35": 489, "36": 512, "37": 528, "38": 539, "39": 546, "40": 560, "41": 581, "42": 599, "43": 611, "44": 629, "45": 638, "46": 654, "47": 666, "48": 680, "49": 690, "50": 698, "51": 711, "52": 725, "53": 747, "54": 757, "55": 769, "56": 785, "57": 802, "58": 822, "59": 834, "60": 848, "61": 860, "62": 873, "63": 884, "64": 895, "65": 922, "66": 936, "67": 949, "68": 961, "69": 973, "70": 987, "71": 996, "72": 1007, "73": 1018, "74": 1027, "75": 1043, "76": 1053, "77": 1069, "78": 1083, "79": 1091, "80": 1108, "81": 1121, "82": 1130, "83": 1140, "84": 1161, "85": 1175, "86": 1189, "87": 1203, "88": 1211, "89": 1231, "90": 1243, "91": 1254, "92": 1272, "93": 1282, "94": 1291, "95": 1305, "96": 1315, "97": 1322, "98": 1331, "99": 1342, "100": 1353, "101": 1362, "102": 1373, "103": 1382, "104": 1395, "105": 1408, "106": 1429, "107": 1439, "108": 1458, "109": 1466, "110": 1477, "111": 1498, "112": 1508, "113": 1520, "114": 1529, "115": 1543, "116": 1558, "117": 1565, "118": 1572, "119": 1584, "120": 1593, "121": 1601, "122": 1610, "123": 1621, "124": 1633, "125": 1645, "126": 1656, "127": 1671, "128": 1685, "129": 1693, "130": 1708, "131": 1718, "132": 1729, "133": 1738, "134": 1746, "135": 1756, "136": 1770, "137": 1781, "138": 1790, "139": 1802, "140": 1812, "141": 1823, "142": 1834, "143": 1844, "144": 1858, "145": 1871, "146": 1881, "147": 1894, "148": 1905, "149": 1914}
---

**Dave Jones:** All right, let me kind of briefly go over um what's happening here. It was uh quite a pain to set this up because of the DI inverter. Nothing to do with the AREL.

**Dave Jones:** The DI inverter is a real It's so flexible and the manual is well, everything seems to be there. It's almost impossible to understand. So, it took a while to actually uh figure out.

**Dave Jones:** Many days, in fact, to actually uh tweak and tailor this system to get it working. But, this is actually live data from the solar assistant, which is running on that Raspberry Pi that you saw, uh which is connected to the uh DI inverter.

**Dave Jones:** So, it's an entirely separate system. Don't bother even trying to use the DI uh software or their cloud solution or whatever. It's useless. And everyone who owns a DI says the same thing.

**Dave Jones:** Um and everyone told me to use uh solar assistant, and it is excellent, by the way. So, anyway, so this is today. You can see that the battery is uh 73% uh charged here.

**Dave Jones:** But, Mrs. EV blogs actually at home today. Um and she's obviously just switched on a load. It wasn't like this before. So, 3,300 W. So, the battery is actually there's 25 W going into the battery.

**Dave Jones:** But, you can see before, if I actually zoom into here, okay? You can see that this morning the battery started charging just at like, you know, 7:00, 7:15, something like that.

**Dave Jones:** And a little load switched on there or something. But, it basically looks like we have sunshine today. Even though I don't have a window, can't see outside, I can see that uh yeah.

**Dave Jones:** And all the excess power was being diverted into uh the battery. Now, when I first set this up, this was only the excess power from the panels that were uh connected to the DI inverter.

**Dave Jones:** Now, I have a diagram here. Please excuse the crudity of the model. Didn't have time to build it all to scale or to paint it. Now, I will be doing a separate video doing a much more detailed diagram of this cuz my system is actually really quite complex once you get into all the details and the extra panels I'm going to put into the generator port on the DI

**Dave Jones:** and my solar analytics system how that plays in and everything else. So, this is actually quite a simplified version of what I've got here. Um but it'll do uh for the purposes of today's uh explanation.

**Dave Jones:** Now, uh this is the new DI inverter that we stored. Uh we just installed the uh 48-V uh battery here. So, I've got a total of 15 kWh of battery here.

**Dave Jones:** So, this is the new AERL battery. Um so, that's Of course, we can charge the battery going in that direction and then we can draw load from the battery either during the day and or at uh night when it's actually needed based on the load of the uh house here.

**Dave Jones:** And obviously, the DI inverter has the ability to um import 5 kW. So, if it If you want to, I can charge from the grid, but I don't have a smart meter at the moment.

**Dave Jones:** I will get one installed. So, in theory, I can do all sorts of cool uh like a time of use uh stuff. currently have a plan or a smart meter to do that, but in theory, if your in depending on your particular country, state, or whatever and electricity provider, um you might be able to have like a really cheap night time tariff.

**Dave Jones:** So, you know, you can charge your EV at night or you can dump excess cheap battery and power into your battery at night and then uh you know, reuse that uh during a more expensive time period.

**Dave Jones:** And the DI inverter has all sorts of comprehensive timers in it where you can actually set that sort of stuff up. But I don't have that at the moment.

**Dave Jones:** So, basically, all I'm doing when I first installed this, as I said, okay, I've got two strings of panels connected directly to the DI inverter here, okay? So, basically, a um 5-kW system here and another 5-kW totally separate system, which is the Enphase system.

**Dave Jones:** And the DI has no idea that this Enphase system exists. But there's a trick to that, which I'll show you in a minute, and I've also done a second channel short video on that as well on EV blog, too.

**Dave Jones:** So, when I first set up the DI here, I could only use the excess power. So, let's say it was full sun, and this was generating 5 kW, even though it's winter here now.

**Dave Jones:** Let's just say it was generating 5 kW, and the house was using 1 kW, then, okay, so there's 1 kW going out here into the house, then it would have 4 kW spare to power to charge the battery here.

**Dave Jones:** So, that's no problem whatsoever. But, because I have connected a current clamp on here into the DI, the DI now knows what's going out to the grid and what's coming in from the grid like this.

**Dave Jones:** So, let's take the example of, let's say the house is drawing 1 kW here like this, okay? And these panels in total are producing, let's say, 2 kW like this, but the end-phase system is also producing a total of 2 kW like this.

**Dave Jones:** Now, normally under this situation, the DI inverter here would only know that there's 1 kW of excess power, so it only charge in the battery with the 1 kW of extra.

**Dave Jones:** But, there's a cool mode in the DI inverter called AC coupling. Why it's called that, I don't know. It doesn't really make that much sense, but anyway, I guess you could make sense of it.

**Dave Jones:** But, because it knows because of this current clamp in here, it knows that this 2 kW like this is now flowing out of here, it knows, "Aha, I've got an extra 2 kW available." So, in this particular case, it can have 1 kW of excess from these panels here because it'll divert 1 kW into the house like this, but it also knows that there's this extra 2 kW out

**Dave Jones:** here, which was otherwise being wasted going into the grid. So, aha, I can increase the charge of the battery by that 2 kW offset, which is matched over here.

**Dave Jones:** So, we'll get 3 kW total going into the battery. And that's a really cool feature. I really like that. Um so, yeah, even though my DI has no idea, it has no communication or ability to talk to the Enphase system at all, by having the current clamp on there, it knows there's excess power going in being generated somewhere, and I'm I I want to use that, please, to charge to store

**Dave Jones:** energy in my battery. So, it can use any excess uh power. So, that's really cool. Oh, sorry, I don't think my capture software was getting the pen, so I have to use my mouse here with the pointer.

**Dave Jones:** So, let's say that the house was drawing 5 kW uh for example, and these panels, it's overcast day, we're only generating 1 kW here and 1 kW in this system over here.

**Dave Jones:** So, 2 kW total power, but the house draws 5 kW, then it needs to take that 3 kW from somewhere. And if you set up the DI inverter properly, uh well, you can set it up in various ways depending how you want to use it, it'll take 3 kW that 3 kW from the battery, and then it'll use that to power the house.

**Dave Jones:** Or you can disable that with timers during the day or something like that. But I've got it set up so that just anytime there's excess power in the house drawn than what my solar being generated, the DI will actually uh put in will actually feed the excess power from the batteries like this.

**Dave Jones:** So, that will actually show up as solar production on my solar analytics system, which is kind of weird. So, all of this information in this solar assistant here, uh this is only the information that the DI knows about.

**Dave Jones:** So, it So, this solar production up here, it doesn't know that the Enphase is actually producing any extra energy. So, you know, we can go into the charts here and you get more detailed uh stuff.

**Dave Jones:** So, this yellow production data here, uh in in that only comes from the panels connected to the DI inverter. Doesn't know about the Enphase system, but it doesn't really need to in terms of actually charging the battery, as we said before, using that cool AC coupling feature.

**Dave Jones:** And just as an aside, for those that want to know, here's the manual uh for the DI, and uh I've I'm using zero export to CT mode here. So, uh basically, the current uh transformer here, so that's As I said, I've got the current transformer connected over here, and that's the mode that I'm actually using, but I've also got the AC coupling mode turned on, and there's the timers

**Dave Jones:** and stuff that you can actually set up. And here's this AC couple on grid side uh feature. So, that's the one that I had to tick in order for the DI inverter to know that I'm want to use any excess power from any other systems connected that it doesn't know about.

**Dave Jones:** In my case, the 5 uh kW Enphase uh system. I don't want to be pissing away that to the grid and getting paid nothing for it. In fact, I've got to pay now, apparently.

**Dave Jones:** Got to pay to actually export energy to the grid. No, I don't want that. I want to suck it all into my battery. Thank you very much, so I can use it at night time.

**Dave Jones:** So, here's my independent monitoring system, the SolarAnalytics here. And the interesting thing about the SolarAnalytics is it's kind of sort of broken now in terms of uh useful uh data showing the production.

**Dave Jones:** So, the actual production data here, okay? This is now technically completely incorrect because the production data will include any data being generated from the battery cuz the SolarAnalytics doesn't know that the uh actual current is being produced from the panels or whether it's coming from the battery.

**Dave Jones:** It just thinks the battery's another solar system connected to my to the AC grid. Basically, so you can see like it isn't like the sun was like flat here and the sun all of a sudden just boom came out and went up.

**Dave Jones:** No, this was actually Mrs. EV blog at home right now turning on the EV charger. There it is. So, she turned on the EV charger and it and now cuz the battery's producing all that energy from and now going from the storage i.e.

**Dave Jones:** our storage battery into the EV, the solar analytics system now thinks it's actually producing that power from the solar when it's not. And the reason it was flat here instead of showing your traditional curved solar shape like that cuz it looks like it's perfect sun today.

**Dave Jones:** Instead of showing that, which you've seen in my previous videos that it did, it now shows it flatline. Why is it flatline? Because all that excess energy was going into the battery.

**Dave Jones:** So, it thinks that so the solar analytics system thinks that it's that there's no excess energy being produced from the solar panels because it's all being absorbed via the battery.

**Dave Jones:** So, that is an unfortunate side effect of installing a battery here just from my solar analytics point of view. But of course, the solar analytics system is still absolutely fantastic for like a getting like for all the different current consumptions.

**Dave Jones:** Like here's the hot water turning on for example. Here's the like and then there's the overall consumption and stuff. So, it's still useful for energy draw. But solar analytics is now broken for solar production.

**Dave Jones:** But I can still get that data from solar assistant and from Enphase as well. So, from the solar assistant here, you can see the yellow graph there. We did actually have very nice solar.

**Dave Jones:** There was a little dip there. Cloud came over and then we've had some cloud coverage here. And otherwise the sun's been very good today. But you can see here the battery power graph.

**Dave Jones:** You can see that if if that's a positive value, if it's above the zero line, then that's charging the battery like that. You can see that it dropped to zero there because there was a little cloud came over that matched that one up there.

**Dave Jones:** You can see that the cloud just went, you know, covered over so the solar panel the solar energy just vanished for a minute, but it recovered there. And all that excess power is going into the battery until whoop whoop whoop.

**Dave Jones:** And now you can see how it's gone negative. This is when Mrs. EV Blog started using some stuff at home. But if our total solar production from both of the the Nphase system and the DI system, if that's greater than what our home's currently using, and that includes the EV charger, that includes the the pool, and that includes the heat pump for the hot water system, and all the home loads

**Dave Jones:** and everything else. If we have an excess there, then the excess will be dumped into the battery until I've got it set so it'll charge right up to 100% and it'll drop down to 20%.

**Dave Jones:** So I've had this battery installed for a couple of weeks now. Now the million-dollar question is did I have enough energy in the 15 kWh battery to power all my stuff at night?

**Dave Jones:** Cuz that's one of the things I want to do is, you know, excess solar energy during day, dump it in the battery. Can I power everything at night? And it turns out I've only had one good night so far where I was able to charge the battery to 100% and it lasted all night.

**Dave Jones:** And you can see that here, right? So here's the state here's the battery state of charge, okay? This is for the last 7 days, okay? So so during the day you can see that this it it only got to 88% maximum battery charge there because we didn't we've had a spate of bad weather recently.

**Dave Jones:** Or not terrific weather. It's been quite cloudy and overcast, particularly on this day here. Look, we we only got to half battery charge, 54% here. But, let's just take this first day here, the 30th of the 7th, then it got to 88%, which is decent cuz we're in the middle of winter here, remember, and we've had overcast weather.

**Dave Jones:** So, we haven't been able to charge the full 15 kWh battery. But, you can see the rate of discharge on that curve. You can see that we had a lot of discharge that night cuz we had the oven on and we were cooking.

**Dave Jones:** It was maybe a bit cold, so we turned on one of the air conditioners, for example, and it doesn't take long cuz the oven's 3 kW, the air con is going to take, you know, a kW, kW and a half for the bigger one, for example.

**Dave Jones:** And yeah, you can drain that battery pretty quick. And you can see that we drained it by down to 20% by 8:40. And I've set 20% as the cutoff cuz Peter recommends that we only go to 20%.

**Dave Jones:** So, we're not using the 100% capacity of the 15 kWh we're a battery. We're only using 80% just to get an extra longer life. But, I could go to 100% and then still get its 10-year warranty, for example.

**Dave Jones:** But, I want to maximize the life of my battery. So, I'm only down to 20% and then it started charging up the next day. Boom, by 4:00 it had got to 90%.

**Dave Jones:** But, once again, pretty steep discharge. And by 9:30 there, we're down to its the battery is totally discharged. And this day was horrible. We could only get 50%. The weather was terrible.

**Dave Jones:** And yeah, it was gone by we'd used it by, once again, 8:00 p.m. here, for example. And then the next day, no, we discharged that thoroughly by 9:00. But, you'll notice on the 3rd of August here, we did actually get to 100% and you'll notice that there's a few dips during the day here, which means the dips during the day means that Uh, we had excess we were

**Dave Jones:** using too much load in the house that the solar couldn't produce. So, there was no excess. So, the residual was coming from the battery during the day. And I could probably disable that sort of thing if I want, although I haven't figured out how to do it yet, but I'm fine with that.

**Dave Jones:** But anyway, we got to 100% ripper. And then we started using it or big the slope of the curve means that we're if it's a really sharp curve like that, then we're using of power.

**Dave Jones:** So, I was draining it a lot, but then by we're down to 40% by 9:00 p.m. there. But then you'll notice that the slope changed like that so that we weren't using as much.

**Dave Jones:** And you'll notice that it lasted all the way through the night and it didn't get we got to 23% but it lasted all night. So, there you go. And then it started what is it 8:00 a.m.

**Dave Jones:** the next day it started to charge up and then the clouds came over or we used excess energy during the day or whatever and only got to 50% and then the next night we only lasted until 7:00 and then then it was dead again.

**Dave Jones:** And then this dropped below 20% so I must have been playing around with it there. I was probably playing around with some settings or whatever. It's not supposed to go under 20% and then this day here was awful.

**Dave Jones:** The yesterday was just awful. Um, so yeah, we got absolutely nothing out of it. And you can see today that we've gotten up to 73% already this morning. So, there you go.

**Dave Jones:** I'll just show you a cool little thing that happened yesterday. Look, check check this out, right? This is the load blue is the load power and you'll see that load is switching off and on at about 3 kW.

**Dave Jones:** There's a 3 kW load switching off and on every few minutes here. What is that? That is actually the oven. Mrs. EV Blog actually did three lots of cooking.

**Dave Jones:** One was from here to here, another was from here to here, and another one from here to here. Different types of cooking so you can actually see it so the electric oven, it takes 3 kW, but it basically just switches relay just switches the element off and on.

**Dave Jones:** So, a different style of cooking here, different temperature, different you know, profile or whatever, than what was over here cuz these are shorter time periods uh for example, but they're all 3 kW peaks like that.

**Dave Jones:** And this one over here, this was actually turned on the dishwasher as well. So, the dishwasher heats up, so it's got a resistive element as well. So, that's why there's like the three levels there cuz the dishwasher was switching asynchronously.

**Dave Jones:** This dishwasher element was switching asynchronously with the oven, so that's why you get all the different things there. And most of that some of that was supplied via the battery, some was not because that just happened to be a really overcast day, but fascinating.

**Dave Jones:** So, I love this solar assistant cuz I've got it set up to like measure every 10 seconds or whatever. I can't remember what the period or every second or something.

**Dave Jones:** So, I can get really fine detail uh consumption graphs that I couldn't get before. So, this is very cool. So, it's very interesting that a 15 kW hour, which is a decent size battery, is bigger than a Tesla Powerwall, which is what 12 or 13 kW hours now, I think.

**Dave Jones:** So, I've got a bigger battery than that, although I only go to 80% discharge, so I'm not using the full 15 kW hours, but still um yeah, it's during wintertime.

**Dave Jones:** Um we use a lot of power at night. We've only had one day out of last seven that we've been able to have In fact, it's probably the first day out of the full 2 weeks that's lasted all night.

**Dave Jones:** So, yeah, I think we're going to have to add some extra batteries. Luckily, I have a rack base system. I can just buy an extra battery, 5 kW hours, and plug it in.

**Dave Jones:** Now, of course, this will improve during summer. Of course, we'll have greater solar insulation, greater number of hours per day. Summer is the weather's generally better. Um and yeah, so we should have oodles of excess to easily charge the battery, but you know, if we just happen to use a lot of, you know, do a lot of oven cooking, turn on a couple of air cons at night,

**Dave Jones:** stuff like that, then yeah, you could easily or we forgot to charge the EV during the day and we know we need it tomorrow, then we might have to use some of the 15 kWh from the storage battery now to dump back into the EV.

**Dave Jones:** But the thing is, it all comes out in the wash. The whole idea of a home storage battery is that you basically want to minimize your bill. So, it it doesn't matter like on a daily basis whether or not we're taking energy from the storage battery and dumping it into the EV.

**Dave Jones:** It doesn't matter what load we're dumping it into. The whole concept is that we store excess energy in the battery and then we reuse that to power the loads, whatever the load happens to be in the house or the car or whatever.

**Dave Jones:** And then at the end of the quarter when we get our power bill, it should be much lower. So, can we do some simple calcs right now? Sort of like a payback thing?

**Dave Jones:** Well, let's try it. We can do some reasonable back of the envelope calculations here just based on the cost of the battery and your typical daily usage. And you've seen in my data that I can pretty much almost any day, it'd have to be a really terrible day where I can't extract enough excess solar to charge the battery.

**Dave Jones:** And especially in summer time, I have oodles of energy to actually charge the battery with. So, even with like a Rolls you know, this is one of the Rolls-Royce type solutions here.

**Dave Jones:** Although the price on this is pretty reasonable. If we have a look at the street price here of the AERL the 5.1 kW LFP battery that I've got, about 2900 Aussie bucks per 5.1 kW.

**Dave Jones:** So, I've got three of those and that's actually quite a reasonable price for a battery. You can pay a lot more than that for like the Nphase batteries or the BYD batteries that go onto the Fronius inverter that I was looking at or other ones, right?

**Dave Jones:** So, they're actually quite reasonably priced. Now, you can get a little bit cheaper if you want to buy like a no-name solution and stuff like that and you want to cobble something together.

**Dave Jones:** Yeah, you can get something cheaper, but you know, this is a as you've seen, this is a really nice professional Australian solution here. So, you know, absolutely top-notch, right?

**Dave Jones:** But, still reasonable price. So, got some figures here. Now, we can just calculate this based on one battery. So, I'm going to assume that the NRE I'm going to take out the NRE cost cuz the solar panels have like the solar systems have basically paid for themselves.

**Dave Jones:** That's their own calculation. I've done payback videos on those. Yes, I did have just installed 14 new panels, but the other systems have basically the existing systems paid for themselves.

**Dave Jones:** So, that's a separate thing which which we're not going to include here. And we'll take out the cost of the rack, which I think's like 1,500 bucks or something like that, right?

**Dave Jones:** So, let let's just assume that I want to buy another battery, which I probably will do shortly, right? I'll buy another battery and I'll plug it in there. So, 5.1 kW hours.

**Dave Jones:** So, let's just say that's five Let's say we can use and extract that total 5 kW hour per day and we can do that pretty much every day of the year.

**Dave Jones:** So, if it's 2,900 bucks for 5 kW hours, basically my electricity bill, cuz I'm on a fixed rate at the moment, which will increase, but I'm on 29 cents per kW hour.

**Dave Jones:** I just changed to a cheaper plan. Yes, I was actually paying a lot more than that. It was like 37. It crept up to 37 cents per kW hour.

**Dave Jones:** Nuts. These are all Aussie dollars, too, by the way. So, I'm paying 29 cents per kW hour at the moment and fixed. So, I'm not on any time of day plan cuz I don't have the smart meter yet.

**Dave Jones:** I plan to do that. Maybe it'll give me a few more options in the future. But, assuming I can use the whole capacity, that will give me a $1.45 per day saving.

**Dave Jones:** Doesn't sound like a lot, but when you do use it every day, 365 days a year, that's $529 a year. So, that will So, basically, the payback on if I buy one more of these batteries would be 5.5 years.

**Dave Jones:** And given that it's got a 10-year warranty, here's the depth of discharge curve, the number of cycles it will should easily do that. I've got it in the garage, so it's in a more temperature-controlled environment.

**Dave Jones:** So, the hotter it gets, the lower your capacity your cycle life is going to be. So, yeah, 5.5 years isn't a bad payback. So, even without a solar system, if you're on one of these time of use plans, you can actually use this with a you'd need a separate charge controller, not a solar inverter, but you can get a charge controller that can do, you know, time of use things.

**Dave Jones:** You can suck energy from the grid cheaply if you're on one of those plans. And there people have been telling me there are some plans out there that basically will give you free energy during the middle of the night.

**Dave Jones:** I don't think I can get that here in Sydney, but let us know. Leave it down in the comments. Are you able to get real cheap or even free energy from the grid and you pull it in to your battery and then you can reuse it when they're charging like a wounded bull during the day or during peak hours at night usually, you know, peak usage like you

**Dave Jones:** know, from 5:00 p.m. when everyone's home and they're cooking dinner and they're, you know, doing all the family stuff. That's when typically energy is most expensive, but mine is just flat rate all day.

**Dave Jones:** So, I don't have that, but if you have that advantage, then leave it in the comments. But you can actually probably get even better payback if you can utilize, you know, some system like that.

**Dave Jones:** Now, Peter's actually provided this comprehensive spreadsheet here of years to payback basically and with different states in Australia like Queensland here for example for a 15 kWh system. He's put in 15 grand here, but you know, it depends how much you charge to install it and you know, all that sort of stuff.

**Dave Jones:** He's calculating it at 11.8 years to pay back. So, it'll it'll pay itself back. But, here in New South Wales, uh for example, what's what's tariff rate is he's got?

**Dave Jones:** He's got the 27 cents here, and he's got this Ovo EV plan. I can't get that at the moment cuz I don't have a smart meter, I believe. Um so, yeah, 27 cents, he's calculated 7.1 years.

**Dave Jones:** But, as I said, um because basically I installed this myself, um I can and if I just install an extra battery, I can get a payback in like 5 and 1/2 years.

**Dave Jones:** And that one's assuming that you've got existing uh solar. Um but, he's got one like no solar in Queensland, payback in 7.9 years, for example. And in South Australia, for example, payback in 3.9 years.

**Dave Jones:** Um so, yeah, it it it seems like a low no-brainer, depending on the state you're in. And once again, this will vary greatly, depending on the country you're in, the state, and even local uh things, and whether what plans are available to you, and all sorts of stuff.

**Dave Jones:** So, I still haven't sussed out all plans. I'll do that once I get a smart meter, cuz basically I'm on the cheapest plan I can get with a fixed meter at the moment.

**Dave Jones:** So, there you go. So, he's got some, you know, in in 6 and 1/2 years, five each battery I whack in here, I reckon in 5 and 1/2 year payback.

**Dave Jones:** That's pretty darn good. Anything after that is just free money, basically. So, of course, not everyone's able to do this. Not everyone has the cash to install a battery system like this, cuz it's a lot of money up front.

**Dave Jones:** That's where some governments actually provide a rebate or even a loan scheme. I think New South Wales government had a battery loan scheme at one point. They might even still do so.

**Dave Jones:** Um so, you could loan money from the government, they'll install the battery system for you, and then you pay it back or whatever, and you know, at 0% interest or something.

**Dave Jones:** I don't know. It is so choice. If you have the means, I highly recommend picking one up. Um but, yeah, leave it in the comments down below if you've got What is the best?

**Dave Jones:** I'd love to hear in the comments the best battery payback system cuz I said you can actually cobble together a cheaper solution, but the one I've got here is really, really schmick and nice.

**Dave Jones:** Um, but yeah, what is the best payback that somebody's got on a battery in years? Let us know. But, I do know it'll probably be significantly worse with say a more expensive Tesla Powerwall or an Enphase battery or something like that.

**Dave Jones:** Um, so I've got sort of like a middle-in range price solution here. And if I actually discharge these to 100% per day, then I could actually get an additional saving there.

**Dave Jones:** But, I'm going to I value the longevity of the battery. So, I want this to last like 15 years, hopefully. Um, so yeah, I get Yeah, payback. It looks like it's going to be an absolute winner.

**Dave Jones:** Yeah, there's some NRE cost there to install it and get the DI inverter and everything else. Battery storage looks good. It looks good. And yeah, it's a really great feeling knowing that all the energy at night is coming from the battery.

**Dave Jones:** We just have to, you know, tweak our usage scenarios, but the family's going to use what the family's going to use. Okay? So, but I'm sitting there going, "Oh, she's turned the oven on." You know, and I'm checking my app.

**Dave Jones:** Oh, it's discharging the battery, but I want to eat. So, yeah, electric oven's got to go on. All right. That's probably the biggest, apart from the EV, that is the biggest power hog in the house.

**Dave Jones:** Uh, cuz we've got a heat pump hot water system. That only draws a kilowatt, and you can see that There it is there. That blue one there is our heat pump, and draws 1 kilowatt for a couple of hours there, so it doesn't draw much at all.

**Dave Jones:** And there There's our pool pump there. And this will be different um in the peak sort of like the shoulder periods around summer when we want to use when we want to heat the pool using excess energy.

**Dave Jones:** So, there might be less available to go into the battery, for example. So, I'll do follow-up videos on that uh to tell you that goes. But, that's just the pool pump to keep it, you know, all circulated in winter and keep it all good.

**Dave Jones:** So, yeah, the main energy hog is actually uh the oven. Believe it or not, and the air cons as well. You know, you put on one or two air cons and you're going to chew a kilowatt or two there.

**Dave Jones:** So, um yeah, on a cold night or a hot uh summer night, for example, you may want to switch those on. But, of course, you can put those on timers to use them during the day.

**Dave Jones:** We've got And if you've got a fairly well-insulated house, you can uh you know, heat or cool your house and it should sort of like stay to a quite livable uh temperature.

**Dave Jones:** Um and you don't have to use it from your battery at night. But, battery storage, very cool. Um so, yeah, expect to see uh more videos. So, please leave it in the comments down below what type of videos you want to see, if you want to see any particular data or something.

**Dave Jones:** But, I will follow up with a more detailed explanation of how my uh solar system works because this is an incredibly simple diagram. It's much more complicated than this.

**Dave Jones:** The devil's in the detail, but yeah, I'll save that for a future video. But, so thank you very much, Peter, who's a long-time viewer of the channel. I think he said he has been watching since day one almost.

**Dave Jones:** Um and yeah, he runs AAREL. I might have him on the Amp Hour, too, discussing startups and solar and energy. So, um yeah, stay tuned for that one. Um but yeah, this is a very cool system.

**Dave Jones:** I really like this. I like the modular nature, and I didn't think that I'd need more than 15 kWh. I thought, oh, you know, that was my original guess.

**Dave Jones:** Oh, yeah, 15 kWh will be plenty. And now I'm looking at the usage during the night, and I'm going, eh, I think I'm going to be very shortly buying another module to slot in here.

**Dave Jones:** And I don't know, it may not stop at that. May not stop at 20 kWh. We'll see. And in summertime, oh, producing all this excess energy, I might want to stack this thing right up.

**Dave Jones:** So, don't be surprised if I get the uh itch and I end up with a full When I first saw the rack, I went, when am I ever going to use six batteries in this thing?

**Dave Jones:** This is ridiculous." And now, yeah, I realize I could easily um fill this and use all this power. No problems whatsoever. Which is scary. But yeah, battery prices are coming down and battery storage is awesome.

**Dave Jones:** So, thank you very much uh Peter. I'll link in um uh down below. So, check out their uh products. They are very cool. I'm very impressed with this. And hopefully, I'll do like a tear down video of the uh controller that's inside this thing.

**Dave Jones:** And uh maybe you can come on the Amp Hour and we can discuss some more stuff. But yeah, very cool solution. And this, of course, is lithium ion phosphate, quite a very safe battery uh technology.

**Dave Jones:** So, unless I'm like lighting flames around the battery and it happens to be shorting at the same time and producing some gas, should be right. It's not going to burn the house down like uh the LG battery recall recently.

**Dave Jones:** Um cuz they use the old school lithium ions. But lithium ion phosphate um very safe technology. So, no worries there cuz I know everyone will have that in the comments.

**Dave Jones:** But anyway, this is very cool. I'm very impressed with AEE RL products. And if you like these solar powered videos, sorry, it's gone a bit long. But anyway, give it a big thumbs up.

**Dave Jones:** Catch you next time.
