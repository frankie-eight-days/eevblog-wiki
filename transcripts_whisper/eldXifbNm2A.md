---
video_id: eldXifbNm2A
title: Talk with Peter Watkinson from AERL about LFP Battery Storage
url: https://www.youtube.com/watch?v=eldXifbNm2A
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 14, "2": 38, "3": 60, "4": 80, "5": 103, "6": 118, "7": 135, "8": 149, "9": 170, "10": 188, "11": 207, "12": 226, "13": 253, "14": 269, "15": 288, "16": 307, "17": 322, "18": 336, "19": 353, "20": 370, "21": 388, "22": 408, "23": 424, "24": 441, "25": 458, "26": 471, "27": 487, "28": 500, "29": 520, "30": 540, "31": 559, "32": 576, "33": 590, "34": 605, "35": 619, "36": 635, "37": 653, "38": 669, "39": 680, "40": 696, "41": 715, "42": 724, "43": 738, "44": 752, "45": 766, "46": 781, "47": 795, "48": 805, "49": 818, "50": 837, "51": 854, "52": 869, "53": 888, "54": 906, "55": 924, "56": 936, "57": 952, "58": 964, "59": 979, "60": 991, "61": 1011, "62": 1026, "63": 1040, "64": 1054, "65": 1074, "66": 1091, "67": 1106, "68": 1124, "69": 1139, "70": 1156, "71": 1167, "72": 1186, "73": 1205, "74": 1223, "75": 1238, "76": 1260, "77": 1277, "78": 1296, "79": 1314, "80": 1330, "81": 1342, "82": 1360, "83": 1377, "84": 1390, "85": 1402}
---

**Dave Jones:** I was going to ask what the plan was, but that works. No, there is no plan. No plan. Cool. And here is Peter Watkinson, owner and CEO of Australian Energy Renewable Labs. Research. Research. Oh, I've been saying renewable. Sorry. Yeah, it keeps up your company name.

**Dave Jones:** Great. Good work, Dave. All right. Give us a brief history, because you're an Aussie, technically a start-up, but a start-up with a 30-year history. Yeah, which is a really unique situation to be in. But originally, AERL dates back to the early 80s, sort of in the pioneering days of the industry.

**Dave Jones:** And it was born out of the development of the first maximum PowerPoint trackers, which just didn't exist back then and really made a big difference on the economics of PV, back when solar panels were like $800 for an 80-watt panel. 80 watts! So, you know, getting 25 to 30 percent more out of your $800 panel made a big difference.

**Dave Jones:** So originally, AERL was born and it sort of started that journey. Industry was much smaller back then. But unfortunately, we lost the founder in 2008, and the business kind of just sort of fizzled out after that. It was one of those one-man sort of show, sort of engineering businesses.

**Dave Jones:** But we decided, a series of events, decided to relaunch the company in 2018 and have been sort of diving back into the industry on sort of the winds behind the battery movement. Yeah, so what range of products do you have? Yeah, so we've got some, well now we've got some really nice lithium phosphate 5.1 kilowatt-hour battery modules.

**Dave Jones:** Which we're going to install today. Yep, and a pre-wired cabinet. But, you know, we've been doing, we've been in the stand-alone power space now for quite a few years. So we do PV charges, communications, gateways, a whole bunch of other DC-to-DC power application products.

**Dave Jones:** But yeah, mainly stand-alone power stuff. Well, here's the gateway, so we're going to install that as well. So we've got a cool little gateway, which will talk to the DI? Yes, yes it will. So it'll talk to the DI, it also talks directly to the batteries over CAN bus,

**Dave Jones:** connects back to the ARL cloud servers, which we have a nice web portal on too, so you can see what everything's doing. Fantastic, and we have one of the battery management boards. We will take the cover off a battery, but it's basically a bunch of cells and the battery management thing.

**Dave Jones:** I'll do a separate teardown analysis video of that, so stick around for that. So this is the only battery that you do? Yes, at the moment this is just the latest and greatest, so 48 volts, 5.1 kilowatt-hour life squared. So it's a 16S prismatic battery.

**Dave Jones:** Cells are manufactured by a company called Great Power, which is basically kind of the... Yeah, tell us the history. It's very interesting how they inclined all these companies. Give us the brief. That part of the world has kind of got its own Silicon Valley thing going,

**Dave Jones:** but basically the founder of BYD and the founder of Great Power were college roommates, both chemical engineers and both wanted to start battery companies, and both did start battery companies actually, but they both had sort of different ideas about it, and now they are two of the biggest LFP manufacturers globally

**Dave Jones:** and have quite the friendly rivalry going on. So we're using Great Power cells in this, which are really like awesome premium cell, and coupled with BMS and tightly integrated into our whole ecosystem basically. And I know because a lot of people are going to ask,

**Dave Jones:** lithium-ion phosphate safety versus lithium-ion? So yeah, NMC versus LFP. Yeah, that's a good one. LFP is a much more stable chemistry. It's far less likely to catch fire, but it will still... So NMC is somewhat explosive. Well, it's actually exothermic, so it will heat up.

**Dave Jones:** If you get a short internally in the battery, you're going to get an exothermic reaction, and that's going to lead very quickly to thermal runaway, which is not good for anyone involved. That's why they recalled the LG batteries here in Australia, because they were lithium-ion, not lithium-ion phosphate.

**Dave Jones:** It was one hell of a recall. How many packs did they have here, do you know? Hundreds of thousands, I would say, around the country. They're still calling them out. It's hurt them. So the biggest manufacturers of NMC are the Koreans. You've got Panasonic, LG, and of course everyone knows,

**Dave Jones:** or a lot of people know Panasonic's relationship with Tesla. So Tesla-Panasonic co-op manufactures NMC, and basically the Chinese giants, BYD, Great Power, and another one called CATL, are the sort of three major manufacturers of LFP, and China kind of owns the LFP supply chain there.

**Dave Jones:** But LFP is now becoming, because it's a safer chemistry, and because of its price point and scale, it's now becoming the dominant chemistry. So you'll see a lot of... For home storage? For home storage, but also for EVs. So they're good enough for EVs now?

**Dave Jones:** Yeah, so if you go buy a base model Tesla Model 3, or basically any of the BYDs, it's all got LFP packs. Oh, it does? Okay, I didn't realize they switched. Yeah, so everything's moved to basically the same cells that we've got in here,

**Dave Jones:** because they're a larger prismatic cell, which means less sort of overhead. Okay, so these aren't 18650s, they're a square prism. That's right. Yeah, so your 18650s are your NMCs, and any variation of 18650 cylindrical generally is an NMC. Actually, sorry, no, that's wrong.

**Dave Jones:** It started as them all being NMC, but they do make LFPs in that same form factor now too. But everything's moving towards prismatic, because you get a lot more battery in your cell, basically, without the same sort of overhead of all the different metal casing

**Dave Jones:** that comes with all those little cells. So effectively, much more jelly roll per cell. Better density, higher energy density per line of work. The whole show. Makes sense. Bigger cells make LFP very viable for EVs as well. But for home storage, you don't really care about that sort of thing too much, do you?

**Dave Jones:** Don't. But, you know, there is something to be said for the economy of scale that comes with the automotive industry. Of course. So with the scale-up of LFP and transition into using LFP for automotive applications, LFP is just now dominating everywhere. And, of course, everyone's watched the LG recall and gone,

**Dave Jones:** hmm, no, we don't want to do that anymore. We want to use LFP. So they're not exothermic in the same way? No, they're not. So they're not the same level of fire hazard. But if they do have a short circuit internally or something like that,

**Dave Jones:** they will generate gas. So the only time generally that you'll see an LFP cause an issue is if that gas is then subsequently ignited. Right. So you've got to have a secondary source to ignite it. That's right, yeah. So whereas the NMC, well, it'll start to ignite very quickly.

**Dave Jones:** It'll self-immolate and, yeah. Yeah, and then everything else is... So we're good to install in the garage, is what you're saying? Yeah, yeah, that's right. You just won't use any barbecue lighters around it. All right. That's it. That's it. Like, installing in a garage does still come up.

**Dave Jones:** There are a whole bunch of Australian standards that you have to adhere to. The standard particular, if someone wants to do a lot of bedtime reading, it's like 100 and something pages, is 5139. And that just lays out all the ground rules around, you know,

**Dave Jones:** not putting it in front of the front door, not putting it beneath a habitable space, you know, good backing, your safety circuit breakers and things like that. So technically you can install these yourself because they're 48 volt. Yes. But you've got to make sure that you do, you know...

**Dave Jones:** It's better to meet the compliance. Yeah, yeah, you've got to be compliant because if you're not compliant and, you know, something happens, you've got a loose connection or something like that and it does cause a fire, you're going to be in trouble. Yep.

**Dave Jones:** Let's talk about this rack briefly. Yeah, absolutely. What have we got here? So this is our six-way pre-wired battery cabinet for the LifeSquared. So we have everything in here you need, basically, to just slot the modules in and plug and play. We've got our 600 amp DC bus, 100 amp per battery,

**Dave Jones:** that you effectively just connect off through to... Yeah, so we'll be joining into here today. Yeah, absolutely. Yep, that's it, via a giant, giant, giant breaker in there. So that's absolutely... That's our DC, two-pole DC circuit breaker that will be between this cabinet and the day inverter.

**Dave Jones:** And that's kind of basically it. The only other thing we need to run is a Cat6 comms cable between the batteries and the inverter. Yep. And the inverter will self-detect the batteries and that's kind of it. Got it. But DI technically... You were telling me that DI don't technically support your battery

**Dave Jones:** but you support them in your firmware. Yeah, so... Instead, using a generic protocol, so to speak? So we don't... Yeah, we haven't actually worked with DI to integrate the product but the industry is moving at the moment towards a little bit of standardisation around battery protocols.

**Dave Jones:** So there's a couple of particular brands in China that were very dominant for a number of years and so what started happening is rather than everyone, you know, doing custom integration work with every new product that came, people started just going, well, we'll use their protocol

**Dave Jones:** because it's already integrated with that inverter. Got it. So now there's a couple of key protocols in the industry that just work with everything. Excellent. And that's... We're now very, very close to a standard battery comms protocol and these use that. So, effectively, that just talks straight to the day.

**Dave Jones:** Fantastic. But there's some inverter manufacturers out there which will still lock you into their batteries. Oh, yeah. So there's... There are a number of inverter manufacturers out there, some of the more dominant ones because they have the sort of pool to be able to do it,

**Dave Jones:** that have basically gone... They used to support other batteries and they've gone, you know what, we'd rather sell a battery. So, you know, you can only use our battery now and we're changing our protocols to proprietary protocols. So, yeah, if you're looking at a hybrid inverter,

**Dave Jones:** definitely have a look at what batteries are supported and whether they are sort of open to different batteries because, yeah, like if you go with a Fronius... The Fronius hybrid inverter, which the name... I was considering that. Yeah, yeah. You can only use a BYD battery box with that, basically.

**Dave Jones:** That's the only thing they support. So they have a nice little cushy relationship there that makes that happen. And then Enphase are super special. Oh, Enphase, you need your own specific Enphase battery. So, yeah, there's quite limited hybrid inverters out there that actually are really flexible.

**Dave Jones:** The Day is kind of one of the more unique ones in that space that lets you do basically anything with it. They've just given you the hardware to sort of configure it in any way you want, which is quite cool, makes them quite unique,

**Dave Jones:** which is why they are sort of being relatively dominant in some of the markets they play in. What is your main market for these? Actually, standalone power. So we do a lot of work with the Australian utilities building systems to disconnect power lines

**Dave Jones:** on edge applications. Ah! So someone ran the numbers a few years ago and realised having, you know, like 50km of power lines and having two customers hanging off the end of it doesn't actually make economic sense. Aha! And around the same time, this sort of, you know,

**Dave Jones:** the battery tech and the charge to inverter tech all got to the point... It was all ramping up at the same time? Yeah, it was getting to the point where it was like, you know, it's actually pretty good now, this stuff works, it's really reliable,

**Dave Jones:** so why don't we snip the poles and wires and put some standalone power systems and save ourselves a buttload of maintenance costs? So we've been doing a lot of that. Right. But we also do, like, standalone power systems, you know, if you've got a cabin

**Dave Jones:** that doesn't have the grid connected or you want to disconnect, we'll design a whole power system for your application, basically. So then... It's pretty busy. How much is the residential? Do you really even tap the residential at all? Yeah, we do, but it's kind of like mum and pop farm stuff.

**Dave Jones:** Oh, it's more farm. Yeah, so anything, yeah, a little bit more rural. Yep. In terms of... This is the first real product we're doing that is, like, you know, coupled with something like the day, is a true residential product. You know, if you've got a house with solar,

**Dave Jones:** you might have noticed recently that your feed-in tariffs are down there. Yes. And it sucks. So we're all suddenly getting power bills again, yay. Yay, yay. But, hey, the solution to that and the reason you're getting power bills is because of the fact that you're using power at night

**Dave Jones:** when the sun's not shining. Exactly. And you're buying that from the grid at a rather high rate because that's also gone up. So the solution to that is there's tonnes of excess potential generally during the day. Often we're not home, so we're not using the solar and we're not, you know...

**Dave Jones:** That energy is just not being generated. The solar panels are sitting there idle. So the solution to that is put it in some batteries. That's it. And that's what we're going to do today. Yeah, and then we can use the power at night

**Dave Jones:** and nick that power bill in the bud. That is the plan. That is the plan. So, yeah, I think 15 kilowatt hours should cover it. I think so. But we'll only run it to 80... We'll only run it to 80%, which is what you recommend.

**Dave Jones:** Yeah, so these... We do warranty the life squareds to 100%. But, you know, it's kind of... If you want maximum... You get a lot out of them at 100% for, like, the 10-year warranty that we do offer on them. But, you know, if you want to get a really, really good run out of them

**Dave Jones:** as long as possible, 80% is the way to go. So 100% to 20% is sort of the area you want to play in in terms of your charge and capacity usage. Got it. Does the industry have any real data on, like, genuine life on these type of cells yet?

**Dave Jones:** Yeah, yeah, absolutely. So we've actually done full life cycle testing on these in all different ambient conditions because we'd like to know how they're going to perform. Well, yeah, but you can't age it for 10 or 15 years. But you can simulate the...

**Dave Jones:** Yeah, we can simulate the cycle. Yeah, so we can't age it. But LFP's kind of been around... We're getting very close to 10 or 15 years in terms of when the early LFP was first introduced. And the fact that every major automaker is switching to LFP

**Dave Jones:** is a pretty good tick for LFP that, you know, the confidence is high. Confidence is high. I repeat, confidence is high. Especially... More gas reference. Yeah. Especially, like, you know, it's this comparative use case compared to an automotive application is vastly different, right?

**Dave Jones:** We're potentially discharging these batteries at maybe a maximum of 5 kilowatts or so with your day inverter. You think about the amount of power that electric motors draw instantaneously. Yes. You're looking at hundreds of kilowatts. And that just, that's a much harder life.

**Dave Jones:** And if they stand up to that pretty well, this is... This is an absolute cakewalk. Yeah, that's right. All right. So these are self-managed batteries, right? They have a self-management system in them? Yeah, so there's actually... So one of the key unique things about the Life 2

**Dave Jones:** is they're either or. So historically in our space, we've had a whole bunch of lead-acid replacements that are self-managed, which means they just... They have no comms. They don't talk to the inverter, which I don't really like because it's like... It makes for a slightly unstable system

**Dave Jones:** when things aren't talking to each other. Yes. So the way that we work with these is we take the best of both worlds. We have comms. But if we lose comms, for example, like a mouse decides it likes the taste of your Cat6

**Dave Jones:** that's running in the wall, rather than... This is more critical for stand-alone power applications, but rather than turning off the power and, you know, shutting down the system, we'll actually revert to a sort of self-managed mode. Oh, OK. Right, so it's not self-managed until there's a fault.

**Dave Jones:** Is that...? Unless you're using it with an inverter it doesn't talk to. Oh, OK. Yeah, so it's like... But your one does talk to the DAE in a basic way? Yeah, it does. Yeah, so it's fully integrated with the DAE based on that comms protocol we were talking about earlier.

**Dave Jones:** Yeah, most of the... So if you're playing in the stand-alone space you would have heard of Victron. Also fully integrated with Victron products through their Servo GX. And then we do a stand-alone configuration, a semi-stand-alone configuration, with, if you use the Australian inverter brand,

**Dave Jones:** Selectronic down in Melbourne, with our chargers, basically. So the inverter just adverts and does nothing else and then our chargers have a managed communication system with the chargers. And they're kind of the three main configurations that these are installed in at this point.

**Dave Jones:** Are your chargers suitable for residential use? Yeah, they are. They're not IP rated though, so... Oh, OK, they've got to be in a shed somewhere. Yeah, you've got to need a power room or something like that. Got it. So that kind of limits the use cases.

**Dave Jones:** Are you working on that? Because you talked about you might have an outdoor rated rack at one point? Yeah, yeah. We've got stuff coming in that space. So, yeah, no, stay tuned. We'll definitely have some cool alternatives to integrating it with the day

**Dave Jones:** in the next sort of 12 months or so. Fantastic. And once we get batteries installed, does it self... Like, if we're drawing, you know, five kilowatts, does it come evenly from all the different batteries? Yeah, so... Or how does that work? So unlike an analogue self-managed BMS,

**Dave Jones:** which really, really heavily relies on cable impedances and cell matching and things like that, our BMS is a little bit smarter than that. We're actively managing... And we've got way less cells to manage too, being only 16 cells. So we don't have long strings of cells.

**Dave Jones:** We're not managing strings, we're managing individual cells in the pack, which means it's substantially easier to regulate. But basically, we'll actively balance all the cells in the modules. So even if one battery is doing slightly more, effectively, they'll talk to each other and balance it out,

**Dave Jones:** and then make sure that the current load is nice and even. Oh, fan. Is that programmable? No, that's all automatic. It's all totally automatic. Yeah, it's just... They just do it. Right, got it. So this is a low-voltage 48-volt battery. Yes. Do you make the high-voltage version as well?

**Dave Jones:** We do have a high-voltage version coming later in the year. What is the difference in the markets for those? Difference in the markets... So the high-voltage one is a little bit interesting in terms of the... just the compatible inverter products at the moment.

**Dave Jones:** There's... I mean, again, it's probably Day is one of the only ones. But, you know, you can't... Like, Victron and all the standalone power players don't have a high-voltage inverter. Oh, really? So it's... And, of course, Euphronia's high-voltage products and things like that are all closed ecosystems.

**Dave Jones:** So we do have it coming and we do have a nice compatible product that we're going to pair it with. But it's a bit more effort because, you know, we have to do both sides of the system to actually launch it into the market.

**Dave Jones:** Right. So who should... If viewers are out there looking for a high-voltage or low-voltage battery, which one is better for what situation? Well, this is available now, so... Right, yeah. So this one. But... Like, in general, in the industry, because there are a few high-voltage solutions out there.

**Dave Jones:** Yeah, there are a few high-voltage. High-voltage has some technical things that do make it quite nice, but also has some drawbacks in the sense that it's high-voltage and you can't touch it. So 48-volt is considered an extra-low voltage, which means it's a lot more serviceable and accessible.

**Dave Jones:** The high-voltage batteries are like sealed modules. You can't do anything with them. They're just... You're fully reliant on the manufacturer to make sure that everything works. So that's the drawback. But being high-voltage, lower current... I was going to say... Basic math. Basic I squared R loss.

**Dave Jones:** Can't escape that, right? Yeah, I figured that's the reason that they did the high-voltage ones, just for a bit more efficiency out of the system, maybe. Yeah, I think, especially now that we've got... For the power guys out there, now that we've got really nice silicon carbide

**Dave Jones:** commercially available at scale, high-voltage makes sense, right? We've got... We can get... We can get 20 milliohm, which is not super low, but it's pretty decent, 1200-volt silicon carbide MOSFETs for a couple of dollars. Yeah, that's nuts. Which means, you know, why the hell wouldn't you do high-voltage, right?

**Dave Jones:** And that's why we're seeing such high efficiencies in some of the power converters now. We are kind of at the upper limit of high-voltage... Of low-voltage, sorry, at 48-volt. Like, you know, some of the... You know, 10 kilowatts at 48-volt is a lot of current.

**Dave Jones:** And that starts to generate heat, right? You can't get away from that. So where I think high-voltage really has a major part to play is EV integration. So having a whole high-voltage DC system, because EVs run 400 to 800-volt DC packs, as well as larger applications

**Dave Jones:** where you've got to draw, you know, 30 to 100 kilowatts, fast charging, all those sorts of things, because, yeah, the I squared R losses just become too dramatic at 48-volts. But for a house... House, that's fine. Yeah, five kilowatts. We'd rarely use more than five at night, you know, so...

**Dave Jones:** Yeah, no, that's manageable. Yeah, for this sort of application, 48-volt makes sense. But if you're doing larger applications, that's when it really makes sense to look at high-voltage. Battery prices. Ah, battery prices. Why have they not dropped? Why have they not dropped? As promised.

**Dave Jones:** Well, I mean, they have dropped a lot. Well, they have. OK, how much? How much have they dropped? They've been going down year on year. Not sure of the percentage off the top of my head. But, you know, now we've got things like

**Dave Jones:** this sort of LFP cell, as well as new sodium ion chemistries coming online, which is even simpler in terms of the ingredient mix, virtually sodium. But, yeah, much simpler again. So it's, you know, I think there'll be a point in the next sort of five or ten years

**Dave Jones:** where it's like battery everywhere, tons of capacity, everyone's home's powered, that sort of thing. It's on that trajectory at this stage. And can the US ramp up their manufacturing or not? Well, that's going to be interesting. We're going to find out over the next 24 months.

**Dave Jones:** All right, we'll find out. Stay tuned. But, you know, we've already got somewhat of an oversupply in China at the moment. So if the US ramps up their capacity as well, it's going to be really interesting. Like, I think we'll see a lot of companies

**Dave Jones:** taking big hits because effectively they'll be forced to sell below cost to try and survive. And then some level of consolidation in the industry and then we'll see what it looks like on the other side of that. But it's going to be crazy

**Dave Jones:** if they get that capacity online as well.
