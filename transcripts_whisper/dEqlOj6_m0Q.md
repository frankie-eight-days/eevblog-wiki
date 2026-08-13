---
video_id: dEqlOj6_m0Q
title: EEVblog #877 - Solar Analytics Home Energy Monitoring Installation
url: https://www.youtube.com/watch?v=dEqlOj6_m0Q
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 19, "2": 40, "3": 59, "4": 78, "5": 97, "6": 109, "7": 132, "8": 151, "9": 165, "10": 177, "11": 197, "12": 210, "13": 231, "14": 245, "15": 261, "16": 277, "17": 294, "18": 310, "19": 325, "20": 346, "21": 365, "22": 380, "23": 397, "24": 410, "25": 424, "26": 439, "27": 457, "28": 477, "29": 492, "30": 507, "31": 523, "32": 543, "33": 565, "34": 582, "35": 600, "36": 617, "37": 630, "38": 644, "39": 662, "40": 686, "41": 703, "42": 724, "43": 738, "44": 753, "45": 769, "46": 786, "47": 804, "48": 819, "49": 838, "50": 860, "51": 879, "52": 894, "53": 918, "54": 933, "55": 950, "56": 966, "57": 980, "58": 994, "59": 1008, "60": 1024, "61": 1042, "62": 1056, "63": 1071, "64": 1089, "65": 1106, "66": 1125, "67": 1140, "68": 1157, "69": 1176, "70": 1189, "71": 1206, "72": 1220, "73": 1238, "74": 1259, "75": 1276, "76": 1295, "77": 1311, "78": 1330, "79": 1352, "80": 1366, "81": 1381, "82": 1396, "83": 1417, "84": 1434, "85": 1449, "86": 1465, "87": 1484, "88": 1497, "89": 1523, "90": 1543, "91": 1558, "92": 1579, "93": 1594, "94": 1609, "95": 1624, "96": 1639, "97": 1655, "98": 1671, "99": 1685, "100": 1698, "101": 1718, "102": 1732, "103": 1745, "104": 1760, "105": 1777, "106": 1793, "107": 1810, "108": 1824, "109": 1840, "110": 1854, "111": 1872, "112": 1886, "113": 1900, "114": 1918, "115": 1936, "116": 1954, "117": 1972, "118": 1986, "119": 2003, "120": 2018, "121": 2033, "122": 2050, "123": 2068, "124": 2081, "125": 2101, "126": 2122, "127": 2137, "128": 2156, "129": 2176, "130": 2193, "131": 2211, "132": 2226, "133": 2242, "134": 2258, "135": 2275, "136": 2291, "137": 2306, "138": 2322, "139": 2343, "140": 2364, "141": 2385, "142": 2401, "143": 2417, "144": 2436, "145": 2453, "146": 2471, "147": 2487, "148": 2503, "149": 2520}
---

**Dave Jones:** Hi! It's time for another solar video. I've done many videos on my home solar power system here, so I'll link in a playlist thing here, so check out all my solar power videos. One thing I have not had on this system for, like, the two or three years I've had it installed

**Dave Jones:** is consumption data for my house. And you can buy little dicky consumption units from JCAR and you can hook them onto the pvoutput.org website, which is what I typically use to log my data here. But a company called Solar Analytics, they're an Australian company, were kind enough to contact me

**Dave Jones:** and say, hey, would you like one of these, our Whizbang solar monitoring systems? So, thank you very much, Solar Analytics. They're going to, right now, in a few minutes, just install this thing. So we'll have a quick check out first, and what it does is it not only logs your house consumption data,

**Dave Jones:** but it also logs your solar production as well, and it ties into a website. This is a 3G model, so it actually has a SIM card, talks back to the system, they've got an online plan and things like that, so that you can actually track and log all your data, and it can make predictions about what's going to happen in the future,

**Dave Jones:** all sorts of stuff. So, really excited to check this thing out and actually get even more data, because I love getting data from my solar system. It's awesome. So this is the SC23 solar smart monitor, and they do have a Wi-Fi version as well, but I was recommended the 3G version.

**Dave Jones:** So they've supplied this, and we'll install it. Apparently it's a real simple install, so we won't go into details on that, but yeah, let's go. And here's the SC23 unit, which we're going to install today. It's actually a three-phase one, hence L1, L2, L3.

**Dave Jones:** We've got our 3G antenna here. Hopefully it works inside my metal box, because I'm not in the best reception area here. There's a helicopter going overhead. And then we've got three, but my house is only a single-phase system, of course, so we can actually use multiple channels to measure other things.

**Dave Jones:** So if you've got like a hot water system, for example, you can hook that up to one of the phases. So there's going to be current transformers with this, and voltage as well. It's powered, it hasn't got batteries inside, so it's powered from the line.

**Dave Jones:** And yeah, we're just going to install this now and hook it up. I'm not sure what lines we're going to hook it up to, but we'll be able to collect three channels of data anyway. And it does log it internally at five-second intervals, I believe,

**Dave Jones:** and then sends it out burst via the 3G. And you can set that up in the software and things like that. And you get the current transformers in the box. Actually, here they are. So we get three of those. We just strap those over so you don't have to wire it in series.

**Dave Jones:** It's just a current transformer, so you can pick it up. So really simple and quite safe to install. Although we do have an electrician here today. They kindly sent one over to install it. And ta-da! Here is the diagram for the single phase system.

**Dave Jones:** So I've got a net meter. So we're going to put one here onto the load. So that'll be the whole house load here. And then the ones for the solar supply, so we can get our consumption data. And then we can hook a third channel up to something else.

**Dave Jones:** I don't know, I've got gas hot water here, so I don't really need that channel. But I don't know, maybe you can hook it up to the lights or something and log your lights separately to your power points, perhaps? Hmm. Actually, I just remembered, I've got two air conditioners at home, so in theory we could hook that third auxiliary channel

**Dave Jones:** up to the air cons. But I don't think that the current transformer is big enough. You could, in theory, put both wires for both air cons through there to get the total air con consumption. I'm not sure if they will fit. Maybe they will.

**Dave Jones:** What do you think, Alex? Yes, they will. They're small. Only 20 amp circuits, 2.5 mil, so we should be able to fit two in there. Yep. Something new for me. Excellent. Oh no, he hasn't done it before. Alright, let's go. So we're here with Alex.

**Dave Jones:** He's going to install it for us. Say hi Alex. Hi Alex. And we have to get an enclosure first, and then we're going to whack it in. He has not done one with a dual air con through the same current transformer, have you?

**Dave Jones:** No, not yet. First time for everything. Well, first time for everything. It should work, because the current will be, will generate extra magnetic field in the current transformer it's going through, so it should work, whether you have one wire going through or multiple ones.

**Dave Jones:** So, there you go. That's the back of my fuse box for those playing along at home. It's a compliant fuse box, is it Alex? Yes, it looks pretty, relatively neat to me, yes. In what way wouldn't it comply? In what way wouldn't it comply?

**Dave Jones:** Yeah, if it was a bad one. Well, the first thing you'd look at is the incoming mains. It has to be double insulated all the way inside that hole there. Got it. If it's not, then the earth wire that goes to the frame will have to be 16mm, and it isn't.

**Dave Jones:** It looks like it's about 6mm to me. Ah, okay. So, that's quite okay, and you've got two meters, yes? Two electronic meters. Two electronic meters, yes. One's a solar, and one's general consumption, yeah? That's correct, yep. And you've got a, yeah, you've got a Zellweger relay to turn on the hot water, but...

**Dave Jones:** Ah, we don't, yes, we don't, we have gas hot water. Yes, there you go. So, there you go. So, we don't need to hook that up today? No. An interesting point, I don't think, I wouldn't be allowed to take that off. Okay. It's got radioactive material in it, and they have to be disposed of and done by, who are you?

**Dave Jones:** Endeavour. I think Endeavour will have to do that. Really? It's got, like, concentration... Yeah, I only found that out a few weeks ago. Wow. And I don't know why. Like, your smoke detector in your house will have a bit of... Yeah, it does, it's more of it.

**Dave Jones:** Like that, yeah? Yep. But, supposedly, you can throw them away in the bin, which is a bit irresponsible, but it's so small, and it's got half-life, I suppose. I don't know, that's not uranium, so... Right. If you turn the light circuit off, which I just did, that means your controller will turn off.

**Dave Jones:** Right, so we're powering the controller from the light circuit. Yeah, that's the, that's possibly written on your little... Yep, I think, I think it's... What's his name? Your document, yeah? Yep, that's right. That's the generalised way. Yep. You can do that here. There it is.

**Dave Jones:** Or in some other situations. Yep. We can, um, utilise a, our own control breaker if we can't fit the stuff in there. Got it. Like, if we needed to put this a bit remote, you're not allowed to have it be live by itself.

**Dave Jones:** You're not supposed to be able to switch it off here, so we could work on it. Got to work on it. And here's our current transformer. It's 60 amps, although I'm told it's linear up to about 75. Um, so for the full, presumably the full 60 amps, we're going to get 80 milliamps out of it, 1%.

**Dave Jones:** Um, and I think the whole system is spec'd at that roughly 1% or thereabouts. So, you know, it's fairly accurate. We were just talking about the panels. Some of them are made out of, uh, asbestos. And, uh, yeah, we've got to wear a special, uh, use a special vacuum.

**Dave Jones:** Yes. Right. Nasty. Sure, there's lots of regulations. You'd probably think it's stinky. I think it smells alright. No, I think it smells good, huh? Yes. You've done too many of them. Alex, I've got to ask, what is your multimeter of choice? Well, it would be a Flute, but here I'm just using a Jaycar.

**Dave Jones:** Oh, you're not using a Jaycar. Yeah, because it's a DC Tonga meter up to 40 or 400 amps, actually. Yep. But ordinarily you'd have a Flute with you. I have a Flute, yes, and I've used other, what, a Bryman or something. Yeah, Bryman.

**Dave Jones:** A Coltronic, I think, yes. I resell a Bryman. Half decent meat are the Brymans. Yes, that's the one I use at home for electronics. Excellent. I don't take that to work. So you're a hobbyist. You do electronics at home. Yes. Awesome. Old time electronics.

**Dave Jones:** Old time. What sort of stuff? Tell us. Through hole and valve amplifiers and guitar effects and things like that. Nice. I haven't really mucked around with any SMD components. Yeah, all this newfangled surface mount rubbish. Well, I don't know. I could probably do it.

**Dave Jones:** I need the sucker and the reflow station, and I'm a tight ass. I'm not willing to restock with all the gear. Awesome. Some of the gear I fix, I haven't been able to fix lately. Some Roland amplifiers and things, because miniaturized components getting down to computer

**Dave Jones:** chip stuff, and I'm sorry, I don't know if they designed that for someone to fix it. They didn't. I am not good enough to fault find that in quick enough time. Yep. Don't blame you. Bloody dual screen, bloody blah, blah, blah. Yeah, you should get a Rygold DS1054Z or something like that, but nothing wrong with the old tricky

**Dave Jones:** dick analog scope. Yeah, we won't be getting any more of them, will we, repackaged? No, I don't think so. No. And it looks like we are able to put the current transformer, those two wires up there are the ones that go to the air con circuit breakers there, so we should be able to put both of

**Dave Jones:** those wires through that one current transformer and log both air conditioners separate. Awesome. So I'll show you that. There we go. There's the air con circuit breakers there. And we've got one for the main part of the house, another one for the bedrooms.

**Dave Jones:** And that's my main breaker, of course, coming in for the whole house. 60 slash 80 amps, I guess, 60 amps continuous, 80 peak or something. Hmm. And here we go. It's starting to look good. There we go. Alex has done a good job there.

**Dave Jones:** We've placed it in. Are there some times you can't, like there's no room left on the panel or somebody's been a dick and they've installed things too sparsely? Yes, and then you'll have to start modifying, you'll have to be moving these, you'll have

**Dave Jones:** to be turning the main supply off and moving stuff, but it gets harder when there's labels as well. But yes, you're going to try and do it. We've never had a time we can't do it, but we've said, oh, it's an hour. And no, it's not.

**Dave Jones:** Right. So mine's pretty chock-a-block now. I don't think I can fit much else in here. Looks pretty good on the back. Yeah. And of course, the old meter's still installed up there, but it's not operational since they installed the solar meters that you've seen, the solar net metering system.

**Dave Jones:** And as you've seen in a previous video, this meter here actually shows what I'm exporting to the grid. 77669 kilowatt hours. There we go. And this shows what I've actually generated from my panels. And so this will be, because any energy during the day that I use in the house, it gets used

**Dave Jones:** from here and won't be exported. So that's only the excess, which I don't use. So Alex was just saying that you install the Sunnyboy SMA inverters. Are they the best, pretty much the best you can get? We install them pretty much exclusively because of their reliability.

**Dave Jones:** We've done them in schools and government organizations and things. And I've replaced a few little chips in them, and we've had about two go out. And I've been here seven years, eight years. So I put one on my own house. Got it. So you actually do component-level repair on those?

**Dave Jones:** You can. You can? It's a little baby chip, you know, like one of those, I can't remember what the name of it is, but yeah, just with a little tool. Okay. You just drop it straight into the zero insertion socket. Ah, that would be the EEPROM.

**Dave Jones:** Yeah, EEPROM. Okay, you just upgrade the firmware in it. Yes. And stuff, okay. So that's one fault, and then another couple internal faults, which were under warranty, so they were quite good about it. All right. Ah, so the actual EEPROM itself would fail?

**Dave Jones:** Causing a K1 relay hunt, so it's hunting for the grid all the time. Interesting, okay. Yeah. Wow. We're about to plug on our current transformers, and the good thing about the current transformers is that you can put them on any channel because they're not set.

**Dave Jones:** You can just change it in software setup, so beauty. Here we go, we're installed. We've got one current transformer, another one for the aircon right there, and one for the main up there, which of course will, the output from that, which will go positive

**Dave Jones:** and negative depending on whether or not I'm using, I'm importing power or I'm exporting power to the grid, so I can handle that. And there we go, we're installed. The SC23. Good job, Alex. No worries. And we've got Vishnu. How's it going? Good.

**Dave Jones:** He's actually a viewer. Yes. Yes, awesome, he watches. And he's going to set it up for me, so let's take a look at how, at some of the data, well actually explain some of the data that you have to put in to actually set this thing up.

**Dave Jones:** Okay, for the inverter we have to select the type of inverter, so the make and model. Yep, so you've got a huge database of every inverter. Yep, and we've got all the parameters so we can work out the efficiencies and so on. So, you've got an SMA inverter and that's rated at?

**Dave Jones:** 3 kilowatt inverter. Yep. Yep, Sunny Boy, yep. TL2 or something. Jeez, you've got them all. Yeah, I had to put in a few. Right, and you've put in my exact solar panel model number as well, so you've got a huge database of all, they're all a different solar panel you've got in your database.

**Dave Jones:** Awesome. Absolutely. So you've entered, so behind that is the technical parameters for each solar panel. Yes. Wow. Voltages, currents and so on. And you were telling me that you can get this solar insulation data as well, so that comes from where? That comes from the Bureau of Meteorology.

**Dave Jones:** Right, so they have a couple of sites in Sydney, I guess, with the insulation data. Yep, and we also do what's called near-site analysis, so we can look at near-sites, the insulation data from that. Right. And we can work out what it should be approximately here.

**Dave Jones:** Now one thing I'm wondering is how this 3G wireless thing works inside an earthed, look at this, earthed Faraday cage. Look, it's like, it's surrounded, but I've been assured that they still work, so go figure they do have an external antenna option available if it doesn't, but hmm.

**Dave Jones:** Are we? Has it connected? It says congratulations. It's connected! Woohoo! Incepts the upper account, and they're going to give me an installer account, which is awesome, so we can get extra technical info, which is great. Here we go, we've got data coming through.

**Dave Jones:** I've closed the box. Is it still coming through? What's the burst period? Every 30 seconds. Every 30 seconds. Wait, 30 seconds. I'll get back to you. Alright, so it's a couple of days later, and so I got some data. I couldn't do anything with it straight away, and here's the dashboard that I can go to.

**Dave Jones:** I can access this through my phone as well as any web browser or tablet or anything like that. And here's my production today. It was an extremely overcast day. In fact, the last couple of days we've had bad smoke pollution here in Sydney due to

**Dave Jones:** backburning and things like that, so it's pretty terrible. But this is the main dashboard page. Here's a live monitor. It's currently at 5.51 p.m. Yes, it is, and you can see that there. So obviously the sun has set. My panels aren't quite about.

**Dave Jones:** Actually, we'll be able to see it. So what we can look at here is we can look at our production, which is our energy production, and bingo, this is actually today. We can look at yesterday and the day before. It was pretty terrible.

**Dave Jones:** Here we go. Here's a more typical profile. This was the first day. It was installed. No, hang on. It was installed on the Thursday. So 3.15 p.m. That's when it started to die, and you can actually see a little bit of ramping down there.

**Dave Jones:** That's rather interesting, like a staircase-type waveform. I'm not exactly sure why it's doing that, but that's interesting nonetheless. You can look into it, but you can see when we installed it, it had just dropped off the cliff here, and we were just looking at that the day before.

**Dave Jones:** So this was my first full day's worth of data. And, of course, this curve exactly matches the one I get from my Sunnyboy inverter, so I can show you that as well. So here's my pvoutput.org website. You've actually seen that before. This is all my publicly available data.

**Dave Jones:** You can actually have a look at my solar system on here, and we can go into a day. It hasn't been working for the last couple of weeks, which is weird. I've got a problem with the PV beam counter software that I use and the Bluetooth connection.

**Dave Jones:** It's really dicky. Anyway, we can go into, say, a typical day. Oh, by the way, you can actually see it. This is like a daily thing, and you see it slowly dropping as we come towards winter here. It's not quite winter yet, but you can see the output slowly dropping,

**Dave Jones:** and then we can have a look at it weekly data. And there we go. You can probably see it slowly starting to go off, and then that's the monthly. If you're interested in that, you can see the cycles, winter, June here. So they're the minimums, and then the peak, obviously, around November, December,

**Dave Jones:** something like that, in summertime. And yearly as well, since I've had it installed, if you're interested in that. Anyway, let's go have a look at the daily one, and let's pick a really good day. This one, 12 kilowatts. There we go. And it's basically the same graph that we saw before.

**Dave Jones:** It's exactly the same, but of course this obviously has some clouds coming over and things like that. So it's a bit more ripply like this production, but you see it dropped off at a later time. This was like three or four weeks ago, so it dropped off at 3, what is it, 3.50 p.m.,

**Dave Jones:** where as you can see it's now dropping off like a rock. This is due to shading on my panels caused by the house next door. They're like up on a slope, and they've got a big double-story house, and in the middle of winter it's really quite horrid.

**Dave Jones:** So now you can see it dropping off at about 3 p.m. So that's a good confirmation that it's working. We're getting the production data. Everything's hunky-dory. So that's the power produced daily on my solar panel. But, which I already had that data coming from my sunny boy inverter,

**Dave Jones:** but what we've got now is we've got the consumption data now. And this is great. We can actually have a look. Here's the data for today. It's currently almost 6 p.m., and you can see that during the night, 12 a.m., we're sleeping. You can see some data down here.

**Dave Jones:** This is like, that'd be like the fridge turning off and on. For example, overnight we've got two fridges, so a couple of fridges turning off and on there. And you can see my, the wife obviously got up at, what was it, I can see at 7 a.m.

**Dave Jones:** or something like that, turned something on that drew 1.6 kilowatts. I'm not sure what. And then a couple of 3 kilowatt peaks might have put the dishwasher on, perhaps, or something like that. So it's got to heat up the water. So it's got to produce the 3 kilowatts.

**Dave Jones:** We typically put that in the morning so we can use our solar power. And then she obviously went out for part of the day and then popped back in around about just after lunchtime, and then went again, picked up Sagan from school, for example,

**Dave Jones:** and then didn't get back until 5 p.m. There you go. So you can actually, here's the power of the data, and possibly one of the reasons why a company like Google bought Nest for that ridiculous $4 billion. And Nest is like going down the toilet.

**Dave Jones:** But yeah, they paid a ridiculous $4 billion, and so potentially for that silly thermostat thing, you know, Internet of Things thermostat, and the smoke alarm that they had, bloody ridiculous. Anyway, so that you can actually get data like this. And this data is useful to utility companies and things like that.

**Dave Jones:** It has worth. You can actually, you know, all that big data stuff is quite valuable. So if you actually put your tinfoil hat on there, then, you know, the government can track you and things like that when all this live data's available. They know when you're home, they know when you're out,

**Dave Jones:** and all that sort of jazz. But yeah, hmm. Maybe we can actually go back to another day here. And you can actually see, here's that good day. You can see the yellow one. Unfortunately, it's scaled. You can't, unfortunately, rescale this thing. It would have been nice to, like, drag the scale and things like that

**Dave Jones:** and just go, you know, drag the mouse and go, I want to see between there and there. But unfortunately, you can only see a single day here, which is a bit disappointing. But it does auto-scale this y-axis here. So if we looked at the data just here, it would have scaled it right up.

**Dave Jones:** And you see the yellow one, of course, is the production. And then the purple is the consumption. And then the brown is the mix of those two in there. So we can actually see, and at breakdown, we can see for the last seven days,

**Dave Jones:** consumed 11.8 kilowatts-hour of my solar energy produced. And 13.1 kilowatt-hours I didn't use, so I didn't take advantage of that, and exported it to the grid. And I imported from the grid 46.3 kilowatt-hours. My system's not very efficient in winter and things like that.

**Dave Jones:** This would be much better in summer, where I might actually, you know, import very little from the grid. But this visual representation is really quite nice. And it actually tells me how much I saved down here. And solar analytics actually have a money-back guarantee.

**Dave Jones:** Apparently if you don't save X amount of money in your, or what you paid for it over time, then they'll give you your money back, apparently. And how much I spent on energy and things like that. And I can go in and set up my export tariff here,

**Dave Jones:** which is $0.06 per kilowatt-hour. I get paid bugger all, so that's why I want to use it during the day. And the import tariff there at what I buy the electricity for from the grid, I think it's about 26 kilowatt-hours, including the green levy,

**Dave Jones:** because I pay for 100% green energy. That mostly comes from wind, I believe. So it doesn't actually come from, but I pay to have somebody put that energy onto the grid. So my one doesn't actually magically, you know, route its way through the grid and come from a wind farm somewhere.

**Dave Jones:** But anyway, that's pretty cool. So I can now monitor all that sort of stuff. And then we've got performance data here for week, month, year, total, all that sort of stuff. And savings, here we go. And like I said, we haven't got much data already.

**Dave Jones:** I only got like four or five days worth of data. So there's not much at all. And then you can get monthly reports and things like that. And then it can give you recommendations of, you know, like, oh, this alerts you that there's something wrong with your panel

**Dave Jones:** and things like that. So one thing I've got, which I'll show you, is that I've got an installer account, which allows us to look at the live data, including the voltage, current, reactive power, and everything. Let me show you. All right, so here we are looking at the live data here.

**Dave Jones:** And this updates in 30-second increments here. And we can see that we've got the yellow one is produced. There's not much there yet. So we're not producing anything. So it's right down at zero. And then consume. We're currently consuming about 550 watts at home at the moment.

**Dave Jones:** But I'm here in the lab. And the air conditioner is not switched on. You can see the air conditioner down here. It's actually drawing 17.8 watts on standby on all three of our air conditioners. We've got three hooked up to the same one.

**Dave Jones:** And there you go. And it's got the reactive power as well. This is all live data. And I've got Mrs. EEVblog on the phone. Say hi. Hello. And she's going to turn on the air conditioner for us. And it's on. And there will be like a 30-second lag or something like that.

**Dave Jones:** Maybe a minute or something like that. There might be that. Thank you very much. Bye. And we should see the air conditioner one actually pop up. So you remember how we installed it on the third channel there? So we should actually give it a minute or two.

**Dave Jones:** And it should actually catch up and produce a spike. It'll probably jump up to, you know, 500, 600 watts or something. I don't know how much the air conditioner takes. But we can actually monitor the voltage here. The line voltage. We've got the line frequency as well.

**Dave Jones:** Very occasionally I see the least significant digit on the frequency fluctuate here. But this allows us to get the live data. But unfortunately, only installers have access to this. So that's very disappointing. Here we go. It's ramping up. There we go. And 30 seconds later it'll get to the true value.

**Dave Jones:** There'll probably be some overshoot or something there as it starts up and things like that. But we can get the reactive energy, the reactive power, the voltage, the frequency. And we can actually monitor the line voltage. That's pretty cool. And it's all there.

**Dave Jones:** But why hide this from the customer? I think they should just give it to the customer. I don't see any harm in that. I think it's great. You know, there's going to be a lot of technical customers who install these things. But they've given me a specific installer account.

**Dave Jones:** And as you can see on the side here, it allows me, I've got a data download option. Which once again, the regular customer does not have the ability to download the data, I don't believe. And that's a, I don't know why that restriction is there.

**Dave Jones:** That seems quite silly. But yeah, I can set up, I can look at stuff that your average punter can't. So there we go. Oh, we've jumped up. So you can see that the, we were drawing the purple one there. The house was drawing, total was drawing 600 watts.

**Dave Jones:** But now it's jumped up in line with the air conditioner. But the good thing about having the air conditioner separate, you can know just how much money and energy you're spending on just your air conditioner. Or it could be your electric hot water system or anything like that.

**Dave Jones:** And remember, you've got three channels to hook up on this thing. So, of course, you want one for the production of your energy. You want one for your entire house. And there's a third one, I hooked it up to the air con. And a minute later, we'll actually probably see that peak out.

**Dave Jones:** So I might come back. But look, it's drawing 1500 watts at the moment. So that's our main air conditioner in the house. I'll come back. And there we go. You can see that we had some overshoot there, because the air con's got to start up and do whatever and operate however.

**Dave Jones:** Air cons do what they start up, and then it's going to level out like that. And that should be fairly level now. So there you go. That's a pretty cool look at just being able to do your live data. And you can get a longer period as well.

**Dave Jones:** So here's a much longer time period. But this short energy one is over the 30-second time intervals, which allows you to walk around your house and go and switch appliances off and on. And you don't need this live graph like this. You can actually go back to the page we saw before with the live monitor.

**Dave Jones:** It actually has the live monitor there. It tells you exactly how much power you're using. You can go around and just switch things off and on, and figure out how much power they take. So that's really easy. And also, say at night time when you've got everything powered off,

**Dave Jones:** and you can zoom in all that residual, any, you know, that standby power. You know, you've got all your 20 million things plugged in, and they're drawing, you know, a couple of watts each. You can go around and unplug those and see how they make a difference,

**Dave Jones:** because it does have the resolution to do that. You could unplug a little plug pack or something like that, mobile phone charger plug pack or something like that, and see, you know, where all your energy's being wasted. So very useful having this power monitor system.

**Dave Jones:** And I haven't had it before. This is great. Now they've actually given me a demo of their site here. This is actually real data coming from their facility at Alexandria here. And we can see that their daily data, that would have been very similar to mine,

**Dave Jones:** that we saw before. And it can also, thinking about a battery for your home, it can calculate how much battery capacity you need. Here it is. Based on all the historical data, once again, they do lots of big data analytics and things like that

**Dave Jones:** to calculate this sort of stuff. And it's recommending, based on all the data that we've got down here, you can actually see all that data there that's been logging for, I don't know, a year or something, or more, then it can calculate you need a 7 kilowatt hour battery system

**Dave Jones:** and grid usage will reduce by 36%. There'll be some error in that and things like that. But it's going to be, you know, it's going to be a really reasonable ballpark estimate. And cost of the battery, $9,600. That's a new beta function they've got.

**Dave Jones:** I really like that. That hasn't popped up on mine yet. Probably don't have enough data for it to actually calculate that yet. And in the performance section here, it tells you your performance of your system at the moment, 88.1%. So, you know, if you've got dirt or something built up on your panels

**Dave Jones:** or maybe one of your panels was broken, like one of my ones, for example, or, you know, you've got some excess shading or, you know, something else is happening to your panels, then your system performance will drop and it can actually detect and alert you about that.

**Dave Jones:** So the 7-day average here, you can see it was 106.8% up here, 107% average since installed, 92%. So you can see that their particular panel isn't performing that well at all. And you can actually see, look, it dipped down recently to 88%. So you go, ooh, something happened there.

**Dave Jones:** I don't know. Did, you know, did it get all dirt and grime and then you suddenly cleaned it and it'll jump back up, for example. And it's got a system log, so there's like a communications fault down here that could be like the 3G system or something like that.

**Dave Jones:** You know, it looks like it happened a couple of times in a day or maybe they're working on it or something like that, but it just logs errors and things like that. So I'm back to my system here now, and you can see that yellow hemisphere there,

**Dave Jones:** that shows the theoretical for based on my current location because it knows exactly where I am. It knows the tilt of my panels. It knows the solar insulation. It knows everything. That's the sunrise and the sunset there. And if we go into the performance side of things, once again,

**Dave Jones:** my system's operating at 70%. It probably doesn't have enough data to actually, you know, show, you know, like to actually calculate a good value at the moment. But that could just, that performance data will change with the solar insulation, for example. They said they get that data from the Bureau of Meteorology.

**Dave Jones:** And so we'd know how much the solar insulation is, how much solar energy is actually hitting. It's not just about clouds. It's about how much the sun is actually producing, amount of power per square meter. And so it knows all this data. It's a shame it doesn't like show it and things like that.

**Dave Jones:** I'd love to see like a temperature plot with it or something like that because they've got all that data in the background, solar insulation, all those figures. It's all hidden away in the magic algorithm to calculate this performance figure. And I think, you know, customers are, you know,

**Dave Jones:** at least a good lot of them are technical enough. There should be like a technical section where every customer can see the voltage and the current and the apparent power and everything else and all that live data. I think they, you know, they really should make that available,

**Dave Jones:** not just for the installers. So yeah, one of my main gripes is that, like why can't I expand the data in there? I want to see it. They've got all this resolution. They've got a great resolution ADC in this thing so that it's getting all this data.

**Dave Jones:** It knows down to like the 0.1 watts or something like that in a couple of kilowatts. And why can't I like expand this graph, just this daily consumption graph up to full screen here so I can see all the data and then, you know,

**Dave Jones:** be able to change, you know, scale the graph and expand it and do all that sort of jazz. Like people want to manipulate their data. I can't be the only one, surely. Now the user does actually have the ability to go in and edit their system.

**Dave Jones:** So if you change your inverter, you can just go in there and change that yourself. So edit inverter number one. Oh, these are all the different brands. Look at them. They've got all these inverter brands. Wow. Look, I had no idea there were so many inverters on the market,

**Dave Jones:** but they've got the data sheet for everyone. They've put all the data in, all the support, everything else. And here's all the Sunny Boys. Wow. And my one's in there. Look at just how many Sunny Boys they've got. That's ridiculous. Wow. Anyway, the rating and things like that.

**Dave Jones:** And if your one's not listed, you can get it added. You can tell them and they'll happily add it. And then if you add some extra panels yourself, for example, you can go edit. If you add an extra string in there, I've only got a single string of 12 panels.

**Dave Jones:** So I've got one string. There it is, one string of 12 panels there. And my orientation is minus 49 degrees. So subtract that, you know, from 360 from north, basically. And a 15-degree tilt on my roof. And once again, here's all the manufacturers of the solar panels.

**Dave Jones:** Wow. Wow. So they've got all the performance data for these things. So they know and can magically calculate that performance figure based on the current solar installation. So they know how big your panel is in square meters. They know what the amount of solar is hitting at that particular time.

**Dave Jones:** And then they can calculate the efficiency of your solar system. So they've got all that huge, big metadata in there. But, you know, and they're coming up with the performance figure, which is great and good for your average consumer who doesn't know anything at all.

**Dave Jones:** But, yeah, I want to see all the technical details. Anyway, it's cool. You can actually set up all that sort of stuff. So if you want one of these very cool systems, go check out solaranalytics.com.au, an Australian-based system. And how much? Tell us the price, son.

**Dave Jones:** Okay, it's a one-off payment of $860. And that sounds like a lot, but that supplies the 3G Connect thing that includes all the bandwidth and everything else with it. It includes somebody to install it for you. And it includes a five-year subscription to the analytics of the thing.

**Dave Jones:** And all that sort of stuff, local customer support, friendly alerts, fault diagnostics, expected performance predictions, live energy use, and all that sort of jazz that we're seeing. Or you can get it for $11 a month for five years. Choose your poison. So thank you very much, Solar Analytics,

**Dave Jones:** for providing this one so that I can now get the consumption data of my house. Brilliant. Check them out. So, yeah, I was going to kludge something together with one of the ones that support PV, one of the monitors that you can get from Jaycar or whatever

**Dave Jones:** for $150 or $200 or something like that. You can hook it on, and then you get a little monitor unit. You can sit on your kitchen table or something like that and monitor it. It's got a USB connection. You don't have to hook it up to a PC, which is always running.

**Dave Jones:** It's ugly. I've got enough problems with the Bluetooth connection. I've got to connect daily to my Sunnyboy inverter. It's a real pain in the butt. So this 3G thing, it's just always working. It's always on. You don't have to worry about it. It's absolutely brilliant.

**Dave Jones:** So, yeah, highly recommend a really professional solution like this instead of cobbling something together. There's nothing worse than having to massage and maintain your solar monitor system. It's just a pain in the butt. I've had no end of problems with a PV bean counter

**Dave Jones:** and the Sunnyboy inverter and the Bluetooth connection and the whole works. It's just nuts. Yeah, just don't go there. So this is the one I got, the Solar Connect 23. And we can have a look at the data sheet and all that sort of jazz.

**Dave Jones:** And here it is. There you go. Five seconds, five-minute measurement, 1% revenue grade accuracy, five-year warranty on the thing. Absolutely brilliant. And as I said, it can support a three-phase system as well. And it's got the installation guide and all sorts of stuff.

**Dave Jones:** There's the specs for those playing along at home. Fantastic. Now, Solar Analytics are the sort of top-level company who you interact with, who install this and collect the data and have all the fancy algorithms and plot all the graphs and allow you to, you know,

**Dave Jones:** and log the data and capture it from the 3G and all that sort of stuff. But the individual unit that we installed, the 23, Solar Connect 23 or whatever it's called, was manufactured by a Sydney company called What Watches. And it's manufactured right here in Sydney as well.

**Dave Jones:** So huge thumbs up there. And they produce all sorts of commercial and residential systems. So we've got the residential one here, but, you know, you can get sort of private key authentication and encryption for all the, you know, really fancy-pantsy systems. And by the way, they're only,

**Dave Jones:** they fit in a single DIN rack. So it's a two-width DIN rail system. So it's really quite nice. And by the way, the designer, John Keeble, of these things, he has said that he will drop by the lab sometime next month and we can do a teardown.

**Dave Jones:** And he'll explain how he designed all these things. And he really knows his stuff. I've spoken to him. So that could be a really long whiteboard discussion. So look forward to that in June, hopefully. So my home solar system is nearing completion. The only thing I have left is solar storage,

**Dave Jones:** is energy storage during the day, that excess usage. Because we saw down here, here we go, that I, look, 13.1 kilowatt-hours in the last week. And I've just thrown away, I've exported, well, it's not thrown away, somebody on the grid is using it.

**Dave Jones:** But I'm only getting six cents, lousy six cents per kilowatt-hour here in New South Wales. It's not much higher in other states. But as they set up here, here we go, for New South Wales solar owners, the solar bonus scheme is expiring. Get more info.

**Dave Jones:** They were giving 60 cents feed-in tariff here in New South Wales, which was ridiculous and almost bankrupted the state. They couldn't afford it. And so that's ending soon. But I get six cents per kilowatt-hour, dropped by an order of magnitude. I'd never got the 60 cents.

**Dave Jones:** I signed up after, I installed my system after the cut-off date. So, bummer. Ah, well. Anyway, didn't want to feed off the government teat anyway. But yeah, 13.1 kilowatt-hours that I can otherwise, in the last seven days, that I can otherwise store. And that's in the middle of winter.

**Dave Jones:** Well, it's not quite winter yet. It's another few weeks away to wintertime. But yeah, it'd be great if I could install that. So, um, the Tesla, apparently nobody, I've been trying to get Tesla, contact Tesla to try and get them that Tesla Powerwall installed,

**Dave Jones:** but nobody at Tesla or the local installers want to talk to me at all. I don't know what the deal is. Anyway, LG have a system who make my LG Mono XR panels, of course, and they supplied me the panel after I had one broken.

**Dave Jones:** They said that they've got a storage solution coming out this year, so they might be interested in working with me. But Tesla aren't, so hey, LG might. Anyway, so that's the last step to complete my solar, home solar power system. So anyway, thank you very much,

**Dave Jones:** Solar Analytics is very cool. Check it out. It's a really good professional option, and I'm sure it will only get better and better. And if they could add those features for the users, please. Export and support other systems and things like that. That'd be great.

**Dave Jones:** So anyway, hope you enjoyed that. Catch you next time. .
