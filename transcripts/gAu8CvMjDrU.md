---
video_id: gAu8CvMjDrU
title: 15kWh AERL LFP Home Storage Battery - First Analysis
url: https://www.youtube.com/watch?v=gAu8CvMjDrU
source: youtube-asr
---

**Dave Jones:** All right, let me kind of briefly go over um what's happening here. It was uh quite a pain to set this up because of the DI inverter. Nothing to do with the AREL. The DI inverter is a real It's so

**Dave Jones:** flexible and the manual is well, everything seems to be there. It's almost impossible to understand. So, it took a while to actually uh figure out. Many days, in fact, to actually uh tweak and tailor this system to get it

**Dave Jones:** working. But, this is actually live data from the solar assistant, which is running on that Raspberry Pi that you saw, uh which is connected to the uh DI inverter. So, it's an entirely separate system. Don't bother even trying to use

**Dave Jones:** the DI uh software or their cloud solution or whatever. It's useless. And everyone who owns a DI says the same thing. Um and everyone told me to use uh solar assistant, and it is excellent, by the way. So, anyway, so this is today.

**Dave Jones:** You can see that the battery is uh 73% uh charged here. But, Mrs. EV blogs actually at home today. Um and she's obviously just switched on a load. It wasn't like this before. So, 3,300 W. So, the battery is actually there's 25 W

**Dave Jones:** going into the battery. But, you can see before, if I actually zoom into here, okay? You can see that this morning the battery started charging just at like, you know, 7:00, 7:15, something like that. And a little load switched on

**Dave Jones:** there or something. But, it basically looks like we have sunshine today. Even though I don't have a window, can't see outside, I can see that uh yeah. And all the excess power was being diverted into uh the battery. Now, when I first set

**Dave Jones:** this up, this was only the excess power from the panels that were uh connected to the DI inverter. Now, I have a diagram here. Please excuse the crudity of the model. Didn't have time to build it all to scale or to paint it. Now, I

**Dave Jones:** will be doing a separate video doing a much more detailed diagram of this cuz my system is actually really quite complex once you get into all the details and the extra panels I'm going to put into the generator port on the DI

**Dave Jones:** and my solar analytics system how that plays in and everything else. So, this is actually quite a simplified version of what I've got here. Um but it'll do uh for the purposes of today's uh explanation. Now, uh this is the new DI

**Dave Jones:** inverter that we stored. Uh we just installed the uh 48-V uh battery here. So, I've got a total of 15 kWh of battery here. So, this is the new AERL battery. Um so, that's Of course, we can charge the battery going in that

**Dave Jones:** direction and then we can draw load from the battery either during the day and or at uh night when it's actually needed based on the load of the uh house here. And obviously, the DI inverter has the ability to um import 5 kW. So, if it If

**Dave Jones:** you want to, I can charge from the grid, but I don't have a smart meter at the moment. I will get one installed. So, in theory, I can do all sorts of cool uh like a time of use uh stuff. currently

**Dave Jones:** have a plan or a smart meter to do that, but in theory, if your in depending on your particular country, state, or whatever and electricity provider, um you might be able to have like a really cheap night time tariff. So, you know,

**Dave Jones:** you can charge your EV at night or you can dump excess cheap battery and power into your battery at night and then uh you know, reuse that uh during a more expensive time period. And the DI inverter has all sorts of comprehensive

**Dave Jones:** timers in it where you can actually set that sort of stuff up. But I don't have that at the moment. So, basically, all I'm doing when I first installed this, as I said, okay, I've got two strings of

**Dave Jones:** panels connected directly to the DI inverter here, okay? So, basically, a um 5-kW system here and another 5-kW totally separate system, which is the Enphase system. And the DI has no idea that this Enphase system exists. But there's a trick to that, which I'll show

**Dave Jones:** you in a minute, and I've also done a second channel short video on that as well on EV blog, too. So, when I first set up the DI here, I could only use the excess power. So, let's say it was full

**Dave Jones:** sun, and this was generating 5 kW, even though it's winter here now. Let's just say it was generating 5 kW, and the house was using 1 kW, then, okay, so there's 1 kW going out here into the house, then it would have 4 kW spare to

**Dave Jones:** power to charge the battery here. So, that's no problem whatsoever. But, because I have connected a current clamp on here into the DI, the DI now knows what's going out to the grid and what's coming in from the grid like this. So,

**Dave Jones:** let's take the example of, let's say the house is drawing 1 kW here like this, okay? And these panels in total are producing, let's say, 2 kW like this, but the end-phase system is also producing a total of 2 kW like this.

**Dave Jones:** Now, normally under this situation, the DI inverter here would only know that there's 1 kW of excess power, so it only charge in the battery with the 1 kW of extra. But, there's a cool mode in the DI inverter called AC coupling. Why it's

**Dave Jones:** called that, I don't know. It doesn't really make that much sense, but anyway, I guess you could make sense of it. But, because it knows because of this current clamp in here, it knows that this 2 kW like this is now flowing out of here, it

**Dave Jones:** knows, "Aha, I've got an extra 2 kW available." So, in this particular case, it can have 1 kW of excess from these panels here because it'll divert 1 kW into the house like this, but it also knows that there's this extra 2 kW out

**Dave Jones:** here, which was otherwise being wasted going into the grid. So, aha, I can increase the charge of the battery by that 2 kW offset, which is matched over here. So, we'll get 3 kW total going into the battery. And that's a really

**Dave Jones:** cool feature. I really like that. Um so, yeah, even though my DI has no idea, it has no communication or ability to talk to the Enphase system at all, by having the current clamp on there, it knows there's excess power going in being

**Dave Jones:** generated somewhere, and I'm I I want to use that, please, to charge to store energy in my battery. So, it can use any excess uh power. So, that's really cool. Oh, sorry, I don't think my capture software was getting the pen, so I have

**Dave Jones:** to use my mouse here with the pointer. So, let's say that the house was drawing 5 kW uh for example, and these panels, it's overcast day, we're only generating 1 kW here and 1 kW in this system over

**Dave Jones:** here. So, 2 kW total power, but the house draws 5 kW, then it needs to take that 3 kW from somewhere. And if you set up the DI inverter properly, uh well, you can set it up in various ways

**Dave Jones:** depending how you want to use it, it'll take 3 kW that 3 kW from the battery, and then it'll use that to power the house. Or you can disable that with timers during the day or something like that. But I've got it set up so that

**Dave Jones:** just anytime there's excess power in the house drawn than what my solar being generated, the DI will actually uh put in will actually feed the excess power from the batteries like this. So, that will actually show up as solar production on my solar

**Dave Jones:** analytics system, which is kind of weird. So, all of this information in this solar assistant here, uh this is only the information that the DI knows about. So, it So, this solar production up here, it doesn't know that the

**Dave Jones:** Enphase is actually producing any extra energy. So, you know, we can go into the charts here and you get more detailed uh stuff. So, this yellow production data here, uh in in that only comes from the panels connected to the DI inverter.

**Dave Jones:** Doesn't know about the Enphase system, but it doesn't really need to in terms of actually charging the battery, as we said before, using that cool AC coupling feature. And just as an aside, for those that want to know, here's the manual uh

**Dave Jones:** for the DI, and uh I've I'm using zero export to CT mode here. So, uh basically, the current uh transformer here, so that's As I said, I've got the current transformer connected over here, and that's the mode that I'm actually

**Dave Jones:** using, but I've also got the AC coupling mode turned on, and there's the timers and stuff that you can actually set up. And here's this AC couple on grid side uh feature. So, that's the one that I had to tick in order for the DI inverter

**Dave Jones:** to know that I'm want to use any excess power from any other systems connected that it doesn't know about. In my case, the 5 uh kW Enphase uh system. I don't want to be pissing away that to the grid

**Dave Jones:** and getting paid nothing for it. In fact, I've got to pay now, apparently. Got to pay to actually export energy to the grid. No, I don't want that. I want to suck it all into my battery. Thank you very much, so I can use it at night

**Dave Jones:** time. So, here's my independent monitoring system, the SolarAnalytics here. And the interesting thing about the SolarAnalytics is it's kind of sort of broken now in terms of uh useful uh data showing the production. So, the actual production data here, okay? This

**Dave Jones:** is now technically completely incorrect because the production data will include any data being generated from the battery cuz the SolarAnalytics doesn't know that the uh actual current is being produced from the panels or whether it's coming from the battery. It

**Dave Jones:** just thinks the battery's another solar system connected to my to the AC grid. Basically, so you can see like it isn't like the sun was like flat here and the sun all of a sudden just boom came out and

**Dave Jones:** went up. No, this was actually Mrs. EV blog at home right now turning on the EV charger. There it is. So, she turned on the EV charger and it and now cuz the battery's producing all that energy from

**Dave Jones:** and now going from the storage i.e. our storage battery into the EV, the solar analytics system now thinks it's actually producing that power from the solar when it's not. And the reason it was flat here instead of showing your

**Dave Jones:** traditional curved solar shape like that cuz it looks like it's perfect sun today. Instead of showing that, which you've seen in my previous videos that it did, it now shows it flatline. Why is it flatline? Because all that excess

**Dave Jones:** energy was going into the battery. So, it thinks that so the solar analytics system thinks that it's that there's no excess energy being produced from the solar panels because it's all being absorbed via the battery. So, that is an unfortunate side

**Dave Jones:** effect of installing a battery here just from my solar analytics point of view. But of course, the solar analytics system is still absolutely fantastic for like a getting like for all the different current consumptions. Like here's the hot water turning on for

**Dave Jones:** example. Here's the like and then there's the overall consumption and stuff. So, it's still useful for energy draw. But solar analytics is now broken for solar production. But I can still get that data from solar assistant and from

**Dave Jones:** Enphase as well. So, from the solar assistant here, you can see the yellow graph there. We did actually have very nice solar. There was a little dip there. Cloud came over and then we've had some cloud coverage here. And

**Dave Jones:** otherwise the sun's been very good today. But you can see here the battery power graph. You can see that if if that's a positive value, if it's above the zero line, then that's charging the battery like that. You can see that it

**Dave Jones:** dropped to zero there because there was a little cloud came over that matched that one up there. You can see that the cloud just went, you know, covered over so the solar panel the solar energy just vanished for a minute, but it recovered

**Dave Jones:** there. And all that excess power is going into the battery until whoop whoop whoop. And now you can see how it's gone negative. This is when Mrs. EV Blog started using some stuff at home. But if our total solar production from both of

**Dave Jones:** the the Nphase system and the DI system, if that's greater than what our home's currently using, and that includes the EV charger, that includes the the pool, and that includes the heat pump for the hot water system, and all the home loads

**Dave Jones:** and everything else. If we have an excess there, then the excess will be dumped into the battery until I've got it set so it'll charge right up to 100% and it'll drop down to 20%. So I've had this battery installed for a couple of

**Dave Jones:** weeks now. Now the million-dollar question is did I have enough energy in the 15 kWh battery to power all my stuff at night? Cuz that's one of the things I want to do is, you know, excess solar energy during day, dump it in the

**Dave Jones:** battery. Can I power everything at night? And it turns out I've only had one good night so far where I was able to charge the battery to 100% and it lasted all night. And you can see that here, right? So here's the state here's

**Dave Jones:** the battery state of charge, okay? This is for the last 7 days, okay? So so during the day you can see that this it it only got to 88% maximum battery charge there because we didn't we've had a spate of bad weather recently. Or not

**Dave Jones:** terrific weather. It's been quite cloudy and overcast, particularly on this day here. Look, we we only got to half battery charge, 54% here. But, let's just take this first day here, the 30th of the 7th, then it got to 88%, which is

**Dave Jones:** decent cuz we're in the middle of winter here, remember, and we've had overcast weather. So, we haven't been able to charge the full 15 kWh battery. But, you can see the rate of discharge on that curve. You can see that we had a lot of

**Dave Jones:** discharge that night cuz we had the oven on and we were cooking. It was maybe a bit cold, so we turned on one of the air conditioners, for example, and it doesn't take long cuz the oven's 3 kW,

**Dave Jones:** the air con is going to take, you know, a kW, kW and a half for the bigger one, for example. And yeah, you can drain that battery pretty quick. And you can see that we drained it by down to 20% by

**Dave Jones:** 8:40. And I've set 20% as the cutoff cuz Peter recommends that we only go to 20%. So, we're not using the 100% capacity of the 15 kWh we're a battery. We're only using 80% just to get an extra longer life.

**Dave Jones:** But, I could go to 100% and then still get its 10-year warranty, for example. But, I want to maximize the life of my battery. So, I'm only down to 20% and then it started charging up the next day. Boom, by 4:00 it had got to 90%.

**Dave Jones:** But, once again, pretty steep discharge. And by 9:30 there, we're down to its the battery is totally discharged. And this day was horrible. We could only get 50%. The weather was terrible. And yeah, it was gone by we'd used it by, once again,

**Dave Jones:** 8:00 p.m. here, for example. And then the next day, no, we discharged that thoroughly by 9:00. But, you'll notice on the 3rd of August here, we did actually get to 100% and you'll notice that there's a few dips during the day

**Dave Jones:** here, which means the dips during the day means that Uh, we had excess we were using too much load in the house that the solar couldn't produce. So, there was no excess. So, the residual was coming from the battery during the day.

**Dave Jones:** And I could probably disable that sort of thing if I want, although I haven't figured out how to do it yet, but I'm fine with that. But anyway, we got to 100% ripper. And then we started using it or big the slope of

**Dave Jones:** the curve means that we're if it's a really sharp curve like that, then we're using of power. So, I was draining it a lot, but then by we're down to 40% by 9:00 p.m. there. But then you'll notice

**Dave Jones:** that the slope changed like that so that we weren't using as much. And you'll notice that it lasted all the way through the night and it didn't get we got to 23% but it lasted all night. So, there you go. And then it started what

**Dave Jones:** is it 8:00 a.m. the next day it started to charge up and then the clouds came over or we used excess energy during the day or whatever and only got to 50% and then the next night we only lasted until

**Dave Jones:** 7:00 and then then it was dead again. And then this dropped below 20% so I must have been playing around with it there. I was probably playing around with some settings or whatever. It's not supposed to go under 20% and then this

**Dave Jones:** day here was awful. The yesterday was just awful. Um, so yeah, we got absolutely nothing out of it. And you can see today that we've gotten up to 73% already this morning. So, there you go. I'll just show you a cool little

**Dave Jones:** thing that happened yesterday. Look, check check this out, right? This is the load blue is the load power and you'll see that load is switching off and on at about 3 kW. There's a 3 kW load switching off and on every few minutes

**Dave Jones:** here. What is that? That is actually the oven. Mrs. EV Blog actually did three lots of cooking. One was from here to here, another was from here to here, and another one from here to here. Different types of cooking so you can actually see

**Dave Jones:** it so the electric oven, it takes 3 kW, but it basically just switches relay just switches the element off and on. So, a different style of cooking here, different temperature, different you know, profile or whatever, than what was over here cuz these are

**Dave Jones:** shorter time periods uh for example, but they're all 3 kW peaks like that. And this one over here, this was actually turned on the dishwasher as well. So, the dishwasher heats up, so it's got a resistive element as well. So, that's

**Dave Jones:** why there's like the three levels there cuz the dishwasher was switching asynchronously. This dishwasher element was switching asynchronously with the oven, so that's why you get all the different things there. And most of that some of that was supplied via the

**Dave Jones:** battery, some was not because that just happened to be a really overcast day, but fascinating. So, I love this solar assistant cuz I've got it set up to like measure every 10 seconds or whatever. I can't remember what the period or every

**Dave Jones:** second or something. So, I can get really fine detail uh consumption graphs that I couldn't get before. So, this is very cool. So, it's very interesting that a 15 kW hour, which is a decent size battery, is bigger than a Tesla

**Dave Jones:** Powerwall, which is what 12 or 13 kW hours now, I think. So, I've got a bigger battery than that, although I only go to 80% discharge, so I'm not using the full 15 kW hours, but still um yeah, it's during wintertime.

**Dave Jones:** Um we use a lot of power at night. We've only had one day out of last seven that we've been able to have In fact, it's probably the first day out of the full 2 weeks that's lasted all night. So, yeah,

**Dave Jones:** I think we're going to have to add some extra batteries. Luckily, I have a rack base system. I can just buy an extra battery, 5 kW hours, and plug it in. Now, of course, this will improve during summer. Of course, we'll have greater

**Dave Jones:** solar insulation, greater number of hours per day. Summer is the weather's generally better. Um and yeah, so we should have oodles of excess to easily charge the battery, but you know, if we just happen to use a lot

**Dave Jones:** of, you know, do a lot of oven cooking, turn on a couple of air cons at night, stuff like that, then yeah, you could easily or we forgot to charge the EV during the day and we know we need it

**Dave Jones:** tomorrow, then we might have to use some of the 15 kWh from the storage battery now to dump back into the EV. But the thing is, it all comes out in the wash. The whole idea of a home

**Dave Jones:** storage battery is that you basically want to minimize your bill. So, it it doesn't matter like on a daily basis whether or not we're taking energy from the storage battery and dumping it into the EV. It doesn't matter what load

**Dave Jones:** we're dumping it into. The whole concept is that we store excess energy in the battery and then we reuse that to power the loads, whatever the load happens to be in the house or the car or whatever. And then at the end of the quarter when

**Dave Jones:** we get our power bill, it should be much lower. So, can we do some simple calcs right now? Sort of like a payback thing? Well, let's try it. We can do some reasonable back of the envelope calculations here

**Dave Jones:** just based on the cost of the battery and your typical daily usage. And you've seen in my data that I can pretty much almost any day, it'd have to be a really terrible day where I can't extract enough excess solar to charge the

**Dave Jones:** battery. And especially in summer time, I have oodles of energy to actually charge the battery with. So, even with like a Rolls you know, this is one of the Rolls-Royce type solutions here. Although the price on this is pretty

**Dave Jones:** reasonable. If we have a look at the street price here of the AERL the 5.1 kW LFP battery that I've got, about 2900 Aussie bucks per 5.1 kW. So, I've got three of those and that's actually quite a reasonable price for a battery. You

**Dave Jones:** can pay a lot more than that for like the Nphase batteries or the BYD batteries that go onto the Fronius inverter that I was looking at or other ones, right? So, they're actually quite reasonably priced. Now, you can get a little bit

**Dave Jones:** cheaper if you want to buy like a no-name solution and stuff like that and you want to cobble something together. Yeah, you can get something cheaper, but you know, this is a as you've seen, this is a really nice professional

**Dave Jones:** Australian solution here. So, you know, absolutely top-notch, right? But, still reasonable price. So, got some figures here. Now, we can just calculate this based on one battery. So, I'm going to assume that the NRE I'm going to take out the NRE

**Dave Jones:** cost cuz the solar panels have like the solar systems have basically paid for themselves. That's their own calculation. I've done payback videos on those. Yes, I did have just installed 14 new panels, but the other systems have basically the existing systems paid for

**Dave Jones:** themselves. So, that's a separate thing which which we're not going to include here. And we'll take out the cost of the rack, which I think's like 1,500 bucks or something like that, right? So, let let's just assume that I want to buy

**Dave Jones:** another battery, which I probably will do shortly, right? I'll buy another battery and I'll plug it in there. So, 5.1 kW hours. So, let's just say that's five Let's say we can use and extract that total 5 kW hour

**Dave Jones:** per day and we can do that pretty much every day of the year. So, if it's 2,900 bucks for 5 kW hours, basically my electricity bill, cuz I'm on a fixed rate at the moment, which will increase, but I'm on 29 cents per kW hour. I just

**Dave Jones:** changed to a cheaper plan. Yes, I was actually paying a lot more than that. It was like 37. It crept up to 37 cents per kW hour. Nuts. These are all Aussie dollars, too, by the way. So, I'm paying 29 cents per kW hour at

**Dave Jones:** the moment and fixed. So, I'm not on any time of day plan cuz I don't have the smart meter yet. I plan to do that. Maybe it'll give me a few more options in the future. But, assuming I can use

**Dave Jones:** the whole capacity, that will give me a $1.45 per day saving. Doesn't sound like a lot, but when you do use it every day, 365 days a year, that's $529 a year. So, that will So, basically, the payback on if I buy one more of these

**Dave Jones:** batteries would be 5.5 years. And given that it's got a 10-year warranty, here's the depth of discharge curve, the number of cycles it will should easily do that. I've got it in the garage, so it's in a more temperature-controlled

**Dave Jones:** environment. So, the hotter it gets, the lower your capacity your cycle life is going to be. So, yeah, 5.5 years isn't a bad payback. So, even without a solar system, if you're on one of these time of use

**Dave Jones:** plans, you can actually use this with a you'd need a separate charge controller, not a solar inverter, but you can get a charge controller that can do, you know, time of use things. You can suck energy from the grid cheaply if you're on one

**Dave Jones:** of those plans. And there people have been telling me there are some plans out there that basically will give you free energy during the middle of the night. I don't think I can get that here in Sydney, but let us know. Leave it down

**Dave Jones:** in the comments. Are you able to get real cheap or even free energy from the grid and you pull it in to your battery and then you can reuse it when they're charging like a wounded bull during the

**Dave Jones:** day or during peak hours at night usually, you know, peak usage like you know, from 5:00 p.m. when everyone's home and they're cooking dinner and they're, you know, doing all the family stuff. That's when typically energy is most expensive, but mine is just flat

**Dave Jones:** rate all day. So, I don't have that, but if you have that advantage, then leave it in the comments. But you can actually probably get even better payback if you can utilize, you know, some system like that. Now, Peter's actually provided

**Dave Jones:** this comprehensive spreadsheet here of years to payback basically and with different states in Australia like Queensland here for example for a 15 kWh system. He's put in 15 grand here, but you know, it depends how much you charge

**Dave Jones:** to install it and you know, all that sort of stuff. He's calculating it at 11.8 years to pay back. So, it'll it'll pay itself back. But, here in New South Wales, uh for example, what's what's tariff rate is he's got? He's got the 27 cents

**Dave Jones:** here, and he's got this Ovo EV plan. I can't get that at the moment cuz I don't have a smart meter, I believe. Um so, yeah, 27 cents, he's calculated 7.1 years. But, as I said, um because basically I installed this

**Dave Jones:** myself, um I can and if I just install an extra battery, I can get a payback in like 5 and 1/2 years. And that one's assuming that you've got existing uh solar. Um but, he's got one like no

**Dave Jones:** solar in Queensland, payback in 7.9 years, for example. And in South Australia, for example, payback in 3.9 years. Um so, yeah, it it it seems like a low no-brainer, depending on the state you're in. And once again, this will

**Dave Jones:** vary greatly, depending on the country you're in, the state, and even local uh things, and whether what plans are available to you, and all sorts of stuff. So, I still haven't sussed out all plans. I'll do that once I get a

**Dave Jones:** smart meter, cuz basically I'm on the cheapest plan I can get with a fixed meter at the moment. So, there you go. So, he's got some, you know, in in 6 and 1/2 years, five each battery I whack in here, I reckon

**Dave Jones:** in 5 and 1/2 year payback. That's pretty darn good. Anything after that is just free money, basically. So, of course, not everyone's able to do this. Not everyone has the cash to install a battery system like this, cuz it's a lot

**Dave Jones:** of money up front. That's where some governments actually provide a rebate or even a loan scheme. I think New South Wales government had a battery loan scheme at one point. They might even still do so. Um so, you could loan money

**Dave Jones:** from the government, they'll install the battery system for you, and then you pay it back or whatever, and you know, at 0% interest or something. I don't know. It is so choice. If you have the means, I highly

**Dave Jones:** recommend picking one up. Um but, yeah, leave it in the comments down below if you've got What is the best? I'd love to hear in the comments the best battery payback system cuz I said you can actually cobble together a

**Dave Jones:** cheaper solution, but the one I've got here is really, really schmick and nice. Um, but yeah, what is the best payback that somebody's got on a battery in years? Let us know. But, I do know it'll probably be

**Dave Jones:** significantly worse with say a more expensive Tesla Powerwall or an Enphase battery or something like that. Um, so I've got sort of like a middle-in range price solution here. And if I actually discharge these to 100% per day, then I

**Dave Jones:** could actually get an additional saving there. But, I'm going to I value the longevity of the battery. So, I want this to last like 15 years, hopefully. Um, so yeah, I get Yeah, payback. It looks like it's going to be an

**Dave Jones:** absolute winner. Yeah, there's some NRE cost there to install it and get the DI inverter and everything else. Battery storage looks good. It looks good. And yeah, it's a really great feeling knowing that all the energy at night is coming from the

**Dave Jones:** battery. We just have to, you know, tweak our usage scenarios, but the family's going to use what the family's going to use. Okay? So, but I'm sitting there going, "Oh, she's turned the oven on." You know, and I'm checking

**Dave Jones:** my app. Oh, it's discharging the battery, but I want to eat. So, yeah, electric oven's got to go on. All right. That's probably the biggest, apart from the EV, that is the biggest power hog in the house. Uh,

**Dave Jones:** cuz we've got a heat pump hot water system. That only draws a kilowatt, and you can see that There it is there. That blue one there is our heat pump, and draws 1 kilowatt for a couple of hours

**Dave Jones:** there, so it doesn't draw much at all. And there There's our pool pump there. And this will be different um in the peak sort of like the shoulder periods around summer when we want to use when we want to heat the pool using excess

**Dave Jones:** energy. So, there might be less available to go into the battery, for example. So, I'll do follow-up videos on that uh to tell you that goes. But, that's just the pool pump to keep it, you know, all circulated in winter and

**Dave Jones:** keep it all good. So, yeah, the main energy hog is actually uh the oven. Believe it or not, and the air cons as well. You know, you put on one or two air cons and you're going to chew a

**Dave Jones:** kilowatt or two there. So, um yeah, on a cold night or a hot uh summer night, for example, you may want to switch those on. But, of course, you can put those on timers to use them during the day. We've

**Dave Jones:** got And if you've got a fairly well-insulated house, you can uh you know, heat or cool your house and it should sort of like stay to a quite livable uh temperature. Um and you don't have to use it from your battery at

**Dave Jones:** night. But, battery storage, very cool. Um so, yeah, expect to see uh more videos. So, please leave it in the comments down below what type of videos you want to see, if you want to see any particular data or something. But, I

**Dave Jones:** will follow up with a more detailed explanation of how my uh solar system works because this is an incredibly simple diagram. It's much more complicated than this. The devil's in the detail, but yeah, I'll save that for a future video. But, so thank you very

**Dave Jones:** much, Peter, who's a long-time viewer of the channel. I think he said he has been watching since day one almost. Um and yeah, he runs AAREL. I might have him on the Amp Hour, too, discussing startups and solar and energy. So, um yeah, stay

**Dave Jones:** tuned for that one. Um but yeah, this is a very cool system. I really like this. I like the modular nature, and I didn't think that I'd need more than 15 kWh. I thought, oh, you know, that was my

**Dave Jones:** original guess. Oh, yeah, 15 kWh will be plenty. And now I'm looking at the usage during the night, and I'm going, eh, I think I'm going to be very shortly buying another module to slot in here. And I don't know, it may not stop at

**Dave Jones:** that. May not stop at 20 kWh. We'll see. And in summertime, oh, producing all this excess energy, I might want to stack this thing right up. So, don't be surprised if I get the uh itch and I end up with a full

**Dave Jones:** When I first saw the rack, I went, when am I ever going to use six batteries in this thing? This is ridiculous." And now, yeah, I realize I could easily um fill this and use all this power. No problems

**Dave Jones:** whatsoever. Which is scary. But yeah, battery prices are coming down and battery storage is awesome. So, thank you very much uh Peter. I'll link in um uh down below. So, check out their uh products. They are very cool. I'm very

**Dave Jones:** impressed with this. And hopefully, I'll do like a tear down video of the uh controller that's inside this thing. And uh maybe you can come on the Amp Hour and we can discuss some more stuff. But yeah, very cool solution. And this, of

**Dave Jones:** course, is lithium ion phosphate, quite a very safe battery uh technology. So, unless I'm like lighting flames around the battery and it happens to be shorting at the same time and producing some gas, should be right. It's not

**Dave Jones:** going to burn the house down like uh the LG battery recall recently. Um cuz they use the old school lithium ions. But lithium ion phosphate um very safe technology. So, no worries there cuz I know everyone will have that in

**Dave Jones:** the comments. But anyway, this is very cool. I'm very impressed with AEE RL products. And if you like these solar powered videos, sorry, it's gone a bit long. But anyway, give it a big thumbs up. Catch you next time.
