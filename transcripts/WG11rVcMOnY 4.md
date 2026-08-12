---
video_id: WG11rVcMOnY
title: EEVblog 1377 - The Amazing UNPREDICTABILITY of Fuses!
url: https://www.youtube.com/watch?v=WG11rVcMOnY
source: youtube-asr
timestamps: {"0": 0, "1": 26, "2": 39, "3": 57, "4": 84, "5": 97, "6": 118, "7": 132, "8": 142, "9": 158, "10": 170, "11": 186, "12": 197, "13": 212, "14": 225, "15": 236, "16": 250, "17": 272, "18": 287, "19": 302, "20": 323, "21": 342, "22": 354, "23": 361, "24": 367, "25": 376, "26": 391, "27": 401, "28": 414, "29": 426, "30": 442, "31": 452, "32": 461, "33": 475, "34": 488, "35": 497, "36": 515, "37": 534, "38": 544, "39": 561, "40": 580, "41": 600, "42": 613, "43": 622, "44": 635, "45": 646, "46": 662, "47": 675, "48": 691, "49": 704, "50": 718, "51": 729, "52": 737, "53": 753, "54": 762, "55": 781, "56": 793, "57": 809, "58": 820, "59": 836, "60": 849, "61": 867, "62": 876, "63": 885, "64": 900, "65": 910, "66": 923, "67": 933, "68": 948, "69": 961, "70": 975, "71": 987, "72": 1003, "73": 1010, "74": 1025, "75": 1039, "76": 1052, "77": 1064, "78": 1076, "79": 1086, "80": 1097, "81": 1112, "82": 1124, "83": 1133, "84": 1142, "85": 1155, "86": 1164, "87": 1174, "88": 1183, "89": 1192, "90": 1206, "91": 1216, "92": 1227, "93": 1238, "94": 1257, "95": 1271, "96": 1281, "97": 1293, "98": 1304, "99": 1318, "100": 1333, "101": 1341, "102": 1357, "103": 1370, "104": 1383, "105": 1397, "106": 1411, "107": 1435, "108": 1446, "109": 1460, "110": 1474, "111": 1486, "112": 1496, "113": 1502, "114": 1518, "115": 1527, "116": 1542, "117": 1564, "118": 1581, "119": 1589, "120": 1609, "121": 1622, "122": 1641, "123": 1666, "124": 1677, "125": 1686, "126": 1695, "127": 1708, "128": 1718, "129": 1730, "130": 1744, "131": 1756, "132": 1771, "133": 1782, "134": 1802, "135": 1822, "136": 1838, "137": 1855, "138": 1866, "139": 1878, "140": 1891, "141": 1901, "142": 1915, "143": 1939, "144": 1963, "145": 1976, "146": 1986, "147": 1998, "148": 2008, "149": 2020}
---

**Dave Jones:** Hi, just a quick video about multimeter fuses because somebody on the EVBlog forum raised this and it's not the first time and it is a legitimate question. Why on meters like the BM235 and BM786 here, 60 or 6,000 count meter or a 60,000 count meter, it's got a 600 milliamp range and it says it's fused but the supplied fuse in it is not actually a 600 milliamps.

**Dave Jones:** It's actually a 400 milliamps and I actually sell spare fuses for these meters and they're 400 milliamps. These are AST M brand fuses and I buy these in bulk and they're very popular.

**Dave Jones:** I also sell the bigger one for the 10 amp range and these are very nice fuses, the AST M ones. Anyway, yeah, these are only 400 milliamp fuses and that's actually what's supplied and that's actually what Brymen recommend for these meters and this is not specific to Brymen and it's for other manufacturers as well.

**Dave Jones:** And you know, there it is, HV620 400 milliamps 1,000 volts AC/DC UL listed of course by the way. And by the way, 1,000 volts AC/DC, make sure if you're replacing the fuses on your multimeter, make sure you get the high 1,000 volt rated or at least you know, like 600 volt rated ones because if you get like the the real cheap ass no name meters, they will have

**Dave Jones:** like only 250 volt mains rated fuses in them and you don't want that. They can arc over and ruin your day. So yeah, make sure you get like proper high voltage rating fuses if you're going to replace them.

**Dave Jones:** Anyway, why do they have 400 milliamps in here if it's actually 600 milliamp range? So what happens if you actually put 600 milliamps through this meter? As you can see, I got 400 milliamps going through there at the moment and I've got one of these fuses hooked up and it's not blowing because the rating of a fuse, a 400 milliamp rating is not the rating that it actually trips at.

**Dave Jones:** That's actually the sustaining current rating. So, in theory, we can leave 400 milliamps through this indefinitely and it will not break. It's only when it goes over 400 milliamps, will it start to break.

**Dave Jones:** And here's where it gets a bit loosey-goosey. So, let's take a look at the data sheet for the ASTM fuse that we've got here, right? So, we've got the 400 milliamp job here, right?

**Dave Jones:** 1,000 V rated. And a 400 milliamps is actually going to have quite a large voltage drop. And I've done, you know, burden voltage videos about that. So, yeah, putting a large amount of current through these, you can really get large burden voltage drops.

**Dave Jones:** Anyway, they don't actually give you an actual trip current on here, but that is its rated current is its implied holding current. Now, there is a mysterious figure here called typical pre-arcing.

**Dave Jones:** And this is also known as the melting thermal energy. And it's given in amp squared or I squared T. So, it's a time unit. This is the thermal energy required in order to basically melt the fuse.

**Dave Jones:** And well, you can whack, you know, your 400 milliamps into that, but it's not really going to give you like the time taken to actually melt. That's not really what it's for.

**Dave Jones:** So, for practical purposes, it's more academic. For practical purposes, you really have to go to the characteristic curves. So, you get these time versus current curves. Any good fuse manufacturer will give you these.

**Dave Jones:** And you've got to look at the individual specific curve for the actual fuse you've got. Now, unfortunately, they don't have a curve for the specific 400 milliamp one. But of course, you know, here's the 500, here's the 315.

**Dave Jones:** Let's just split it down the middle. Well, let's look at 400. 400, if we take 400 up, 400 up, 400 up, 400 up, 400 up. Oh, at 400 it's going to be like it's practically off the scale.

**Dave Jones:** It's practically indefinite. I mean, it might blow eventually, especially if it is in a confined space and it's heating up for example. So, let's actually measure the temperature of this one cuz it is actually going to get fairly warm.

**Dave Jones:** So, I've actually had this running for I don't know 10-15 minutes now or something like that. 37° also my air con's off so there's no air flow. But, of course if you put one of these inside like a sealed fuse compartment inside a multimeter, then it's going to heat up more cuz it takes you know more effort for the heat to actually radiate out.

**Dave Jones:** But, then again the heat can actually go into it might also be lower because the heat can actually dissipate bloody thing. The heat can actually battery. The heat can actually dissipate of course through the metal fuse contacts and into the PCB traces and stuff like that.

**Dave Jones:** So, they inherently have a bit of heat sinking on them. But, anyway, you know, this might eventually blow but like according to the data sheet it's it's going to take a long time and there's going to be like manufacturing tolerances in the fuse as well, the fuse wire itself.

**Dave Jones:** And well, you know, these are just like typical curves. They're not like absolute guaranteed. Anyway, what do we expect to happen at 600 milliamps? So, if we extrapolate this up here, it's going to be somewhere between here and here and I put that I my mark one eyeball says it's around about there.

**Dave Jones:** So, we're looking at 100 seconds, 200 seconds, 300 seconds, somewhere between 300 and 400 seconds. It should probably blow at 600 milliamps. So, you can like according to the data sheet, it actually does have a significant amount of time to actually measure.

**Dave Jones:** That's more than enough time to measure your uh the current your 600 your maximum 600 milliamps, but it's enough to protect the meter that it will eventually uh blow or certainly if it goes to an amp, it's going to blow a lot quicker.

**Dave Jones:** What do we get for an amp? Let's have a look. So, I've taken it up to an amp. Yeah, it could blow it's going to blow in a couple of seconds there.

**Dave Jones:** And that's what you want. And if you're going to get like an old overcurrent fault, you you know, you might get a couple of amps or something like that.

**Dave Jones:** And you can see how it gets, you know, pretty non-linear here at the higher end cuz it's all a bit yeah, it's all to do with the thermals and they blow.

**Dave Jones:** And it's it's really complicated stuff if you want to get into the physics of the real physics of how uh fuses blow. But bit non-linear, but like, you know, it's going to be blowing in like the upper at a couple of amps going to be blowing in like tens of milliseconds or something like that.

**Dave Jones:** Okay, so I'm going to increase this to 600 milliamps. We'll see how long with the stopwatch it takes to blow. There you go. 600 milliamps. As you can see, more than enough time to take your measurement and it's not blowing yet.

**Dave Jones:** Of course, it's had already had time to heat up from, you know, tens of minutes. 47°, you know, it's getting significantly hotter. So, oh no, she she blew. It was somewhere in 50 seconds there.

**Dave Jones:** Okay, so let's do that again. 600 milliamps. And I'll get some data on a couple of these. So, what we had at like 50-odd seconds before, which is, you know, as I said, it's going to vary quite substantially.

**Dave Jones:** If it blew in a couple of seconds, I would be concerned, but it's not. It's There you go. I've got some heat sinking here from the leads, but it might have more if it's like on a PCB and there's big current tree you know, big clamps right around it.

**Dave Jones:** Thermal transfer is not very good. They're like little spikes on them. So, you might actually get them better results inside the meter. But as you can see, look, we're going for a minute 20 now.

**Dave Jones:** Oh, there we go. Minute 57. Let's do another one. There is really going to be like a large tolerance difference between these, I think, if we test the whole box.

**Dave Jones:** Now, of course, it's got to be said that this is this specific type of fuse. Another brand 400 milliamp, even if it's a thousand volts, all the specs seem the same, they might have substantially different characteristic curves than these ASTM brand ones.

**Dave Jones:** So, wait, there we go. 3 minutes 47, was it? This one's up to 53 and a half after a minute 46. This one is about to crack 60. Yep, at 2 minutes 40.

**Dave Jones:** Well, this one's a champ. 63. Of course, we don't know what the internal temperature is because it's all embedded inside that the ceramic or the sand. Well, there we go.

**Dave Jones:** 3 minutes 22. At 63 degrees. We have our first 4-minute jobby. Look at this. Ha-ha, you little ripper. Really big tolerance range on these fuses, which is why, you know, you don't necessarily want to over-range, like over-rate them.

**Dave Jones:** It looks like they've chosen it right. Ah. Oh, you little beauty. It lasted three times longer than that first one we tested. That's incredible. And this is what you have to account for when you're designing fuses like this into a system, especially if it's, you know, critical.

**Dave Jones:** You don't don't want to oversize and don't want to undersize them for your task. It's, you know, and beware of our surge currents as well. By the way, I'm not turning this on 600 milliamp straight.

**Dave Jones:** I'm turning on 400 milliamps first and then ramping up to 600 so that, you know, any like power supply turn-on spikes don't the output capacitor or whatever doesn't dump some extra charge into it and make it, you know, surge blow or something like that.

**Dave Jones:** So, cuz these are quick-blow fuses. These aren't slow-blow jobbies. 77 degrees after 7 and a half minutes. Wow, this is crazy. This is going to last four times more than the first one we tested from exactly the same batch, like the same box.

**Dave Jones:** Check it out, 83°. So, I actually spoke to Brymen quite a few years ago now about cuz somebody asked this exact same question. So, I thought I'd get Brymen's opinion on it and they said yeah, like exactly this is that you know, it holds up for long enough but you don't want to oversize it.

**Dave Jones:** But then you can get potential temperature issues and that can damage other stuff in your meter or whatever. So, you don't you know you don't necessarily want these things to heat up too badly but you want to protect them.

**Dave Jones:** It's a trade but you want to protect your meter of course. So, you don't want to make it too high. So, it's a trade-off. So, there's a super fuse.

**Dave Jones:** Oh, yeah, yeah, Bernie Ernie Bernie Ernie Bernie don't touch these things. But that's that's a crazy yet 90°. Wow. Oh, there we go. It blew. I missed it. Walked away for a little bit, got our shortest one at 45 second.

**Dave Jones:** Okay, what I'm doing is measuring the voltage drop across there. As you can see, it is sort of ramping up, isn't it? I wonder if there's I don't think I've ever experimented with this.

**Dave Jones:** I wonder if there's like a really rapid ramp up right near the point of fire. You can really see what happens when these things really you know, heat it up because well, it's changing the resistance of the filament and it's just going upity up and up.

**Dave Jones:** So, there yeah, that's probably like an 80° or something now. More. Oh, and blow you bastard. By the way, I had a previous one that I didn't shoot. Um 45 seconds.

**Dave Jones:** Are we going to crack three volts? It's a massive drop. You really have to take all this into account when you're uh using your meter. Burn voltage can be a real bugger and changing your fuse from one brand to another can make a very large impact.

**Dave Jones:** And at high values like this, at really high temperatures, yeah, I mean, it will go to that maximum of you know, it'll it'll be able to measure your 600 milliamps, but at the huge cost of burden voltage.

**Dave Jones:** Wow, will this one crack the other one? I think we might have a new winner here. There's a huge difference in it's not like I'm adding, you know, really any extra major heat sinking there by adding those two extra clips on.

**Dave Jones:** This is why when you're measuring these sort of currents, you want to use your amps range instead of your milliamp range. You you know, sure you lose a digit, lose a digit of resolution, but well worth it.

**Dave Jones:** I want to get this video done and edit the thing. I came back to the lab. It's now it's now 20 past 9:00 p.m. Wish the meter had a feature when it would beep when it drops to zero.

**Dave Jones:** That'd be neat. Yes, 100 100 102 103°. Oh, we just lost a digit of resolution on our floor there. Wow, this is actually this is turning into a bit of a valuable lesson video here.

**Dave Jones:** Is that these things can get insanely hot and you know, hot enough to damage your product in some way, perhaps, damage surrounding components, or affect its performance, or whatever.

**Dave Jones:** We've gone from like the shortest one, 45 seconds, to 12 minutes. I I could be here all night. Who knows what the upper bound on this is? All it takes is for the wire to come out however they stretch the filament wires in the machine that extrudes them, or whatever, however it does it.

**Dave Jones:** I don't know how they actually manufacture that. That'd be a fascinating video, wouldn't it? Tour of a fuse factory. Um yeah, can't exactly travel at the moment, so it's not that we have any fuse factories here in Australia.

**Dave Jones:** 111, it just ain't stopping. So, you can imagine if you had that like inside a sealed case. I mean, I don't have my air con here, so there's really no air flow in here, but still we do have like it's just sitting there flapping around in the breeze, right?

**Dave Jones:** Well, it's flapping around in no breeze. It's a bit different to being cooped up in a uh little fuse compartment, sealed fuse compartment. Glad I I was almost going to stop my testing at five, after the 45-second one.

**Dave Jones:** I went, "Ah, yeah, do another couple." And I'm glad I did. Look at this, 14 minutes. I mean, what was the upper bound of that? 1,000 seconds. 1,000 / 60, um you know, that's 16.6 minutes.

**Dave Jones:** So, you know, that's like And that's just like eyeballing it and guesstimating that the characteristic curve is going to be in there somewhere, but you can see when you got huge vertical lines like this and not much differentiation.

**Dave Jones:** It's you know, the the more that these lines get vertical, the more they get vertical, the more uncertainty you have. That's how it works. If it's more slopey like that, then you're going to get a more a narrow a narrower band of uncertainty um for any given fuse, but they don't even give you uncertain characteristics.

**Dave Jones:** This is just like typical curve. So, they like they don't even give you any notes for it. They just say, "Here's the graph, you know, we've measured it." I don't know, did they take averages?

**Dave Jones:** They don't say. Like, so they don't really guarantee these things. So, I maybe see, you know, some other manufacturers might be different. You'd have to look at different uh data sheets and stuff.

**Dave Jones:** Got to got to remember, this graph you know, this axis, the Y axis is log axis. Um well, so is the X axis as well, but come on, give this video a thumbs-up just for my perseverance here.

**Dave Jones:** Perseverance, rover just landed, fantastic, did a video, I did a live stream of that. Come on, you got to give this video a thumbs-up just for me standing here waiting for a bloody fuse to blow.

**Dave Jones:** Ah, the glamorous life of engineering video blogging. 118. Why is the current dropping? I've got a constant current power supply. And unfortunately, I can't show you what power supply I'm using cuz it hasn't been released yet.

**Dave Jones:** It's up there. Hasn't been released yet. There it is. 22 minutes. I actually know why the current dropped though cuz it we've reached the compliance voltage of the power supply.

**Dave Jones:** I had it set to 6 V. 6.17 is the highest. So, yeah. Unfortunately, I chose a 6-V output power supply to do this test. Um I didn't even occur to me that we'd get to that sort of compliance voltage.

**Dave Jones:** That's just That's nuts. Um I might actually stop it because really the only I'd better not put paper on top of that. It'll burn. I've done that That's not the first time I've actually uh burnt paper from uh components.

**Dave Jones:** I've even put them in the report. I've even put the burnt piece of paper in the report to show the test report to show Anyway, long story. The only guaranteed spec they give you is up here in the uh vague electrical characteristics.

**Dave Jones:** And they just say, "Well, at one of its nominal current, I nominal, um it's it's going to last you know, it'll last at least 4 hours minimum. So, in theory, that 400 mA fuse can blow after 4 hours.

**Dave Jones:** But, then they only specify like 120 seconds absolute maximum 2.5 times the nominal current. And we're like nowhere near 2.5 times the nominal um current. So, yeah. Um take these curves with a grain of salt.

**Dave Jones:** I'm going to stop it and we'll um I'll change my uh supply and we'll try and ramp this thing up to uh say 700 mA. See if it blows.

**Dave Jones:** All right. So, I'm back to 400 mA. So, I've got a compliance voltage of uh 10 V this time. So, we're still at uh 3.6 V. Anyway, let's uh now ramp this up to Let's go 0.7, shall we?

**Dave Jones:** Let's try 700 mA. So, let's I'll reset that time. So, that lasted, you know, at least 30 minutes. Here we go. 0.7, go. And whoa, whoa, jeez. No, we're Oh, yeah.

**Dave Jones:** it yeah, it it blew. It blew straight away. It just couldn't handle it. So, yeah. So, you can see that like any gross overload will blow these things, you know, almost practically instantly.

**Dave Jones:** So, it'll save your meter, it'll save your circuit in a gross overload. And that's what fuses are designed to do. They're designed for gross overloads. They're not designed for like really, you know, discriminatory uh current.

**Dave Jones:** Like, you can't really design a product for a fuse to blow within a specific region. Cuz look at the slope of these curves. You're just not going to get that when you have a slope like that.

**Dave Jones:** You might get other brands of fuses where you might get a more controlled characteristic, uh so to speak, or a, you know, a softer, I don't know. What What What would be the word for that?

**Dave Jones:** For, you know, making the slope go, you know, near vertical and having a big tolerance, you know, maybe maybe a tighter tolerance, for example. Um something like that. You got a better word for that, leave it in the comments.

**Dave Jones:** I'm sure it's at the tip of my tongue if I actually thought about it. Anyway, uh yeah, you could, you know, different types, but then if the user goes and changes the fuse to whatever, like, that can totally um change your uh product and change the safety of your product.

**Dave Jones:** It can uh change the characteristics um based on burden voltage and other stuff. So, yeah, you really have to take this stuff into account. Anyway, that's fascinating. So, I've got one, you know, 30-plus minutes.

**Dave Jones:** So, there you go. We went from 45 seconds at the last one. The first one was around about that, wasn't it? And then we went up to 30-plus minutes.

**Dave Jones:** Massive tolerance in fuses like this. All right, what I've got here is a data sheet for a Seba brand. This is basically uh the identical fuse to the uh ASTM.

**Dave Jones:** So, uh once again, fast-blow fuse, 400 milliamps, 1,000 volts. Uh there's the actual uh part number there. Once again, UL uh uh, So, uh, the interesting thing is is that the characteristic curves are very different.

**Dave Jones:** I It only has one curve like this or that or that actually has two for different current ranges. One for 100 milliamps to 800 milliamps and one for 1 amp to 2 amps.

**Dave Jones:** Now, check this out. For 100 milliamps to 800 milliamps, they don't even give you a graph that extends down and this is, uh, times the nominal current times IN.

**Dave Jones:** So, they don't actually So, you have to multiply. So, this is, uh, So, this will be 400 milliamps. They don't give you any separate characteristic curves for all the different currents.

**Dave Jones:** It's the one curve for all of them. So, once again, like it it's totally different to the ASTM fuse, uh, which seems more comprehensive in terms of the characteristic curves.

**Dave Jones:** But, interestingly, look, it's the unfilled triangle there. It The curve stops at four times the nominal current. So, 4 4s, that's 1.6 amps. Beyond that, we we just don't know.

**Dave Jones:** I mean, you could, you know, kind of like say, "Oh, it's going to be a similar curve to that." But, they don't actually give you the data. So, we have no idea cuz we How's it be at 600 milliamps?

**Dave Jones:** It'll be 1.5 * 400 milliamps. So, it'll be this. This is, uh, seconds, but we just don't know the value. So, anyway, I'm just going to whack this in and test it.

**Dave Jones:** See what we get. Okay, this is the Seba at 400 milliamps. There you go. Um, a little bit lower, uh, drop, but, you know, it's neither here nor there.

**Dave Jones:** up bit. So, let's choose 0.6. There we go. It's jumped up to 1.1. And let's see how long it takes. Okay, we're at 4 minutes now, only 1.2 volts drop, and we're looking at 65° there.

**Dave Jones:** So, it just goes to show that, uh, really in Well, in this particular case, um, if you were designing a product, these, uh, Seba fuses, they're less predictable. than I mean you don't even have the data.

**Dave Jones:** You don't even have the data. You don't know what this curve like you can assume the curve's going to do something, but at least the ASTM fuses had all the multiple characteristics.

**Dave Jones:** At least you could you know get a indication. You don't get that with the Ciba fuses. So really the ASTM fuses are like more tightly spec. They're better controlled.

**Dave Jones:** They're better to design in your product than the Ciba fuses in this particular case cuz we have no idea. This could like just last forever. And well, if that's what you want, then that's fine.

**Dave Jones:** But you know, if you're trying to protect your product or do whatever, the lack of data like this could be a real problem. You would have to like do your own testing and then continue to do testing to ensure that they haven't changed their manufacturing process etc.

**Dave Jones:** over time. Because you can't design this Ciba fuse into your product and then measure them and they're all fine. You know, you've done all your due diligence and everything's hunky-dory and then year or two later out in the field you know all your fuses start blowing or they don't start blowing or whatever.

**Dave Jones:** And you go back to them say, "Hey, what's changed? What are you doing?" And they'll go, "Oh, sorry. We don't provide any data below four times the nominal current.

**Dave Jones:** So if you did your own testing, well, that's on you. That ain't our problem." Okay, we're getting towards 20 minutes now. 1.2 volts drop and 65° there. Like yeah, this this sucker's just not going to blow.

**Dave Jones:** So I'll ramp it up to 700 milliamps. Okay, 700 milliamps go. Yeah, significantly higher, but yeah, it's going to take a longer much longer to blow than the uh ASTM did.

**Dave Jones:** This This could This could last minutes at 700 milliamps. So this is a 400 milliamp fuse. No wonder they were a bit coy with their curves over here because well, yeah, they just well, they don't want to tell you.

**Dave Jones:** No, I just don't think it's got the balls to do it. Not at 1.6 volts. So, I don't think the temperature's going to be high enough, but you know, they've all got this secret sauce, their metallurgical secret sauce and everything, but I yeah, no, should I take it 800?

**Dave Jones:** Yeah, why not? Okay, 0.8 amps, go. 2 volts drop. This is double its rated current. 400 milliamp fuse. Yeah, it's it's still only creeping up though. I I think it's going to last a significant amount of time.

**Dave Jones:** Double the current, it's a scandalous. And after a minute, we're probably going to crack 100° shortly. Okay, no, this is getting ridiculous. 5 minutes at twice the current. And if you attempt to extrapolate the curve here, you're probably going to come a gutser because look, this is 1 second here at basically two two times the normal current, which is what we're at.

**Dave Jones:** It should last that 1 second, but uh nope. So, obviously, you know, something it's it's really ramping up when it gets past here. It's just going nuts. That's why they don't bother.

**Dave Jones:** And look how they actually reset this. I mean, what do you choose? If you're designing your product, let's say at four times nominal current in this particular case, 1.6 amps for a 400 milliamp fuse, which which data point do you choose?

**Dave Jones:** Do you choose this one or this one? But this is like Schrödinger's data. So, yeah, it's ridiculous, but anyway, you are down in like the, you know, the millisecond, you know, tens of milliseconds region.

**Dave Jones:** So, I guess it doesn't matter too much. Okay, so we have the data. Let's say three times here. Three times nominal current, 1.2 amps. You expect that to blow in like, well, a couple of hundred milliseconds here.

**Dave Jones:** This is 1 second. So, let's go. Let's give that a whirl. All right, here we go. I'm going to take it to 1.2 amps for a 400 milliamp fuse.

**Dave Jones:** Let's give it a go. I've currently I've just had it for like a minute. I've sort of like blown it let it cool down for a little bit at 400 milliamps.

**Dave Jones:** So, we're going to ramp it up right to 1.2. Here we go. Oh, an amp. Oh, what? Oh, that's right. Sorry. No, it blew. It blew. Sorry, doll. My power supply again.

**Dave Jones:** I Power supply was only capable of maximum of an amp. So, anyway, when you take it up to an amp, yeah, it blew within what sub 10 seconds there or something like that.

**Dave Jones:** So, okay. But, yeah, in any case, I think there's a a good reason why they're not giving you the data below like four times nominal. Bastards. And there are various standards for these fuses, by the way.

**Dave Jones:** There's an IEC standard, which is 6127-2, I believe, is the latest one. And also the UL 248 standard, which it looks like these fuses might actually go by. And of course, it's hard to get these standards, but I was able to get this page, which is a 6 by 32 quick acting low breaking capacity.

**Dave Jones:** It's not a high breaking high voltage capacity one. I don't know if that changes. Please leave it in the comments if you've actually got the standards and stuff. But, anyway, it does give you like a maximum voltage drops, maximum power dissipation, 1.6 watts and stuff like that for like, you know, nominal 400 milliamps.

**Dave Jones:** So, you know, take this with a grain of salt. But, it does actually give you down here. Look, it it actually doesn't give you anything actually below two times nominal current.

**Dave Jones:** It just says, "Look, at two times nominal current, a maximum for 100 milliamps to a 10 amp fuse is 20 seconds." So, yeah, what happens at 1.5? Like, but then it does have like as part of the endurance testing down here, it says, "Oh, 1.15 times nominal current for an hour" and things like that.

**Dave Jones:** It must do must survive 100 cycles at 1.05 times the rated current and stuff like that. So, yeah, you can actually heat these things up and cool them back down and there are endurance standards for these.

**Dave Jones:** So, yeah, but it just like complicates the whole thing, but it it certainly might explain why there's a difference between the Seba one and the ATSM one. They might be working to different standards and well, if you're serious about this sort of stuff, like you've got to take all this into consideration.

**Dave Jones:** I found something on the UL 248 standard anyway and there's all these different classes and things like that and of course, there's ambient like derating at temperatures. So, you know, if your product's being used from like zero to 40 or something like that, like that can like make a fairly big difference in the rating capacity, the effect on the blowing time, the effect on the carrying current and stuff like

**Dave Jones:** that. So, yeah, it's all it's all up in the air. Hold on to your hat. I just found this from Littlefuse, the importance of fuse low overload performance. A low overload is like a low grade fever.

**Dave Jones:** It doesn't cause immediate death, but indicates that something is wrong. It can cause localized overheating, weaken the spring clips or damage the plating on the fuse holders and increase their contact resistance.

**Dave Jones:** It can melt the solder on the surface mount fuses, can melt plastic housings and make fuses impossible to remove. Yeah, all are valid design points you've got to consider.

**Dave Jones:** Anyway, they say currents between 110 and 135% of fuse ratings present a severe challenge to the designer because they can subject parts to high heat for extended periods of time and because fuse behavior at these currents can be difficult to predict.

**Dave Jones:** The fuse does not blow before damage occurs, there can be claims under warranty, etc., etc. Fuses behave in predictable ways when subjected to substantial overloads or short circuits, but low overloads exist in a less predictable realm.

**Dave Jones:** For example, 110% of rating of a mini automotive fuse will open somewhere between 100 hours and never. At 135% of rating, the fuse opening time is between 0.75 seconds and 10 minutes.

**Dave Jones:** Yeah, that's the kind of variability we've seen here. Published curves are available from the fuse manufacturer. However, typically they apply to overloads in excess of 150%, hence why the Ciba fuse while Ciba they're they're just saying anything over anything under four times bugger it.

**Dave Jones:** And they show average characteristics. As I said, it's you know, they're not guaranteed. They only show averages. In fact, low value overloads are not generally considered part of fuse specification at all.

**Dave Jones:** Good luck. Another source of difficulty is that different technical standards for fuses describe different behaviors at low overloads. For example, with one exception it's impossible it's impossible for a fuse to satisfy both the UL CSA and the IEC rating standards.

**Dave Jones:** So, pick one. Calls for a fuse to operate continuously at 100% of its rating. A fuse made to the UL 248 and standard and operated at its rated current will eventually open.

**Dave Jones:** For this reason UL fuses are customarily operated well more than 75% their rated current. That's interesting. And look at all these different standards here. So, there's various standards and at the 600 milliamps we're looking at here or 150% of the rating, well, these are the SAE and the UL standards not even specified at all.

**Dave Jones:** This standard not specified like 60 minutes minimum for example. It's like it's all over the shop. But they say look there is a new 6127 IEC -4 standard. Fuses must not open in less than 1 hour at 125% of the rated current and must open within 2 minutes at 200% of the rated current.

**Dave Jones:** So, it can still at twice the current it can still last 2 minutes under this new IEC standard. Nuts. And here's a table for different little fuse they're different types and what the applicable standards are and the opening time at 135% for example.

**Dave Jones:** And look, it's just it's all over the Like, 0.75 seconds to 30 minutes. Come on. So, basically, one of the top manufacturers little fuse here, they're using like all the Fluke meters and everything, and they're just saying throwing up their hands and just saying you know, it's complicated.

**Dave Jones:** It's like, you're pretty much on your own. And you know, leave it in the comments if you want me to do more detailed test, but I'll leave it for now um cuz I've got no shortage of these.

**Dave Jones:** I've got many many boxes. I sell these on the EV blog store and bulk buy them like a thousand at a time, so it's not a problem. If I wanted to a huge number of test, I'd have to automate this rig.

**Dave Jones:** There's no way I'd want to sit there. Maybe that's a It would that be a mini project anyone would want to see? Would be designing like a a little board that had like, you know, like 20 fuse holders on it or something.

**Dave Jones:** And 10 of you measure 10 at a time, you'd have like independent current generators for each one, and then you'd have like a timer for each one, and then you'd have like You could automate them.

**Dave Jones:** You would actually do that if you were a test engineer as I was donkeys years. Did test engineering, and they they're the sort of jigs that you would actually design for stuff like this for measuring production characteristics.

**Dave Jones:** Although, you know, if you want the full characteristics and stuff like that, that's more complicated. If you just wanted to like sample test fuses coming off the production line, you might actually have a jig, and they probably do have a jig, and they might, you know, just sample test a handful from each batch or something like that just to see that they're within the rather large tolerance that they actually

**Dave Jones:** have here. It's interesting cuz they sell like 315 milliamps, 400 milliamps, 500 milliamps. They don't even give you a curve for the 400 milliamp job, right? And the tolerance between like even the 315 milliamp and the half amp here, like you might find and half amp might blow quicker than a particular 315 mA just based on the tolerance and the massive slope of this line here.

**Dave Jones:** So, yeah, fuses. Fascinating business. Anyway, I think this video is probably fascinating enough to elevate to the main channel. So, if you like the video, please give it a big thumbs up.

**Dave Jones:** As always, comment down below. Do you work in a fuse factory? I'm sure somebody out there does. There's always a viewer out there that has worked in something or other that I mentioned.

**Dave Jones:** Doesn't matter how obscure it is. And uh leave it in the comments down below. So, I hope you found that fascinating. Yeah, fuses. Anyway, so to answer the question, like is a 400 mA fuse suitable for a meter like this?

**Dave Jones:** And Brymen is not the only one that I'm sort of like underrates their fuses like this. And there's probably good reasons why you would actually want to do that.

**Dave Jones:** And yeah, sure, you can measure up to your 600 mA, but it could uh blow depending on what type of fuse you've got. It'll eventually blow. Could blow in seconds, tens of seconds, minutes, tens of minutes.

**Dave Jones:** So, huge variability. Anyway, fascinating stuff. Catch you next time.
