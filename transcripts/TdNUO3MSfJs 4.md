---
video_id: TdNUO3MSfJs
title: EEVblog #1147 - 1 Cent Regulator! That's MAD!
url: https://www.youtube.com/watch?v=TdNUO3MSfJs
source: youtube-asr
timestamps: {"0": 0, "1": 23, "2": 39, "3": 47, "4": 63, "5": 86, "6": 103, "7": 116, "8": 132, "9": 141, "10": 160, "11": 176, "12": 198, "13": 210, "14": 227, "15": 234, "16": 244, "17": 254, "18": 269, "19": 289, "20": 300, "21": 312, "22": 329, "23": 338, "24": 353, "25": 366, "26": 378, "27": 395, "28": 413, "29": 428, "30": 455, "31": 464, "32": 481, "33": 500, "34": 519, "35": 535, "36": 549, "37": 561, "38": 571, "39": 586, "40": 592, "41": 602, "42": 620, "43": 639, "44": 659, "45": 672, "46": 684, "47": 695, "48": 704, "49": 716, "50": 728, "51": 744, "52": 755, "53": 769, "54": 778, "55": 794, "56": 814, "57": 828, "58": 842, "59": 855, "60": 871, "61": 884, "62": 898, "63": 909, "64": 921, "65": 932, "66": 949, "67": 970, "68": 989, "69": 1003, "70": 1022, "71": 1053, "72": 1065, "73": 1075, "74": 1089, "75": 1099, "76": 1114, "77": 1126, "78": 1141, "79": 1153, "80": 1162, "81": 1178, "82": 1195, "83": 1207, "84": 1221, "85": 1236, "86": 1245, "87": 1260, "88": 1274, "89": 1285, "90": 1295, "91": 1304, "92": 1318, "93": 1330, "94": 1343, "95": 1358, "96": 1371, "97": 1393, "98": 1404, "99": 1428, "100": 1437, "101": 1451, "102": 1466, "103": 1483, "104": 1492, "105": 1506, "106": 1521, "107": 1532, "108": 1549, "109": 1562, "110": 1577, "111": 1595, "112": 1603, "113": 1617, "114": 1636, "115": 1653, "116": 1666, "117": 1681, "118": 1695, "119": 1710, "120": 1725, "121": 1736, "122": 1745, "123": 1760}
---

**Dave Jones:** Hi, sorry about the new office background here. I didn't have time to build it scale or to paint it. In a previous video and previous couple of videos, we looked at the 3 cent microcontroller from Paducah and we got that from LCSC, which is a Chinese catalog type Digi-Key kind of competitor Digi-Key Mouser Farnell's catalog competitor.

**Dave Jones:** And I thought we'd take a look at another part from them. It's not a microcontroller because well microcontrollers are expensive, right? At 3 cents. How about another jelly bean part which you'd be no doubt familiar with, the low dropout voltage regulator.

**Dave Jones:** How cheap can you get these on LCSC? Well, turns out you can get them for 1 cent or little bit of maybe 1 and 1/2 cents. I'm rounding down to 1 cent.

**Dave Jones:** The 1 cent linear regulator. I bought 3,000 of them. Let's check them out. So why on earth would you want a 1 cent voltage regulator? Well, why not? When you're optimizing the bill of materials for your product, it could matter.

**Dave Jones:** And with modern products like FPGAs and other like, you know, really high density logic, they often require lots of low voltage power supplies, not just 3.3 volts, you know, 2.5 volts, 1.8 volts, 1.2 volts, you know, even like 0.8 volt cores, 1 volt cores and things like that.

**Dave Jones:** So it's not uncommon to need even like half a dozen different voltage rails inside your product. And that really adds up when you're talking about, you know, selling thousands of items and you might have, you know, three or even five voltage regulators per products.

**Dave Jones:** So it can often pay you to have like a cheap jelly bean part like this voltage regulator, for example. This one's actually a fixed 3.3 volt one, but we might have a look at adjustable ones just to show you how cheap they are.

**Dave Jones:** and well, let's go to Digi-Key, for example, and do a search here on I've sorted by price here in volume. They start at like 3,600, they start at 4.5 cents, which is pretty cheap, but you'll note that's obsolete from a company that I've never heard of, Skyworks Solutions Inc.

**Dave Jones:** Meh, it's a nano power range, you know, but if you go down here, like the next one that's actually active, which is the cheapest, is basically 6 cents in uh volume.

**Dave Jones:** So, like 3,000 volume. And you add these up, you have multiple products times 1,000, you're trying to reduce your bill of materials and stuff like that. Well, why spend, you know, 6 cents plus uh tax, you know, they're 8.5 cents, stuff like that.

**Dave Jones:** Might not sound like a lot, but when trying to optimize your bill of materials, these sorts of stuff really add up. So, if you go over to LCSC here, which is kind of like the Chinese uh kind of competitor to Digi-Key that that specializes in having these Chinese brands.

**Dave Jones:** I didn't do a previous video looking at these. And if you search for positive linear regulators well, they've got 898 parts here. And here we go, look, the cheapest one, the LC6202 from Shenzhen Fuman Electric Corp um is like in the order of 1.6, but the one we're going to look at here that I've actually got 3,000 of.

**Dave Jones:** Why 3,000? Because they came on a reel of 3,000, and it was cheap as, so I just got a reel of 3,000 cuz they might come in handy. Anyway, the SC662K, and this is the 3.3 volt version.

**Dave Jones:** You can get other versions with uh different fixed voltages, and there's also And if you want to search for adjustable ones, you can search for adjustable. Often, it's sometimes better to say uh include like a jelly bean adjustable voltage regulator, so that uh you can just choose whatever.

**Dave Jones:** So, you've got the one bill of materials item there, but then you need your different resistors, three pick and place parts as opposed to just one and and stuff like that.

**Dave Jones:** So, it's nice just to have cuz you're always going to need a 3.3 V rail. So, it's nice to have this. Anyway, look at the price. In 20 of quantity, they're only 2.4 cents.

**Dave Jones:** And when you start talking serious volume here, 1 and 1/2 cents. And if you go up there, it's like 1.44 cents. And you got to remember, this is not direct from the manufacturer.

**Dave Jones:** This is from a Chinese Digikey equivalent catalog supplier who actually have stock. In this case, they don't actually have much of this. But look, these ones up here, 8,700, you know, 5,000, 4,000, 30,000 in stock, right?

**Dave Jones:** There's no shortage of these ones. So, here's another one that I had a look at. Um this one comes from Nat Linear. You might think, "Oh, National Linear. That sounds legit." No, Nat Linear is natlinear.com.

**Dave Jones:** It's China um it's got nothing to do with National Semiconductor or Linear Technology, but they said, "Hey, they're famous names. We'll just join them together. Hey, we'll sound legit." There you go.

**Dave Jones:** So, they sell they have this 300 mA linear regulator in different packages. It's not that it's a little bit more expensive than the one we've got here. Um but anyway, all Chinese data sheets.

**Dave Jones:** So, yep, knock yourself out. This one actually does have curves, but the one we're going to play with, the Fenjin Fuman Electric Co. If we have a look at the data sheet, Shenzhen Finemad Finemad Electronics Group.

**Dave Jones:** This is hilarious. So, that sounds ridiculous, the Shenzhen Finemad Electronics Group. In fact, I think I've they've got their name wrong in their own name wrong in the data sheet.

**Dave Jones:** Cuz if you go over here, it's the Shenzhen Finemade Electronics Group. Maybe it's not the same company. Like, anyway, they're listed on the Chinese stock exchange. They're currently 20 Chinese bucks.

**Dave Jones:** There you go, for the share price. Um I assume it's the same company. Anyway, maybe there is a Shenzhen Finedream, but it's nuts. But, it sounds like the right company.

**Dave Jones:** Shenzhen Finedream engages in design, development, packaging, testing, and sale of electronic and digital analog hybrid integrated circuits in China used in power management class. Bingo. And all sorts of So, it it sounds like them.

**Dave Jones:** Um and they superchip.cn. Is that them? Let's check them out. Yep, it's them. superchip.cn. So, Finedream. And yep, there it is. There's your data sheet. Once again, only available it's exactly the same one.

**Dave Jones:** So, FM is Finedream. And here's the actual part I've got here. It says 80 milliamps there, but that would be 18 millivolts drop out at 18 milliamps current. And you'll notice that they actually come in a hermetically sealed package like this.

**Dave Jones:** You don't generally don't want to take these out of their hermetically sealed packages like this until it gets to the pick and place machine. The reason that they do this, and this one doesn't include it, but they often include a little one of those dry desiccant bags in there to absorb absorb the moisture.

**Dave Jones:** And the whole part about that is that it keeps moisture from leaking into the parts before reflow. Plastic molded packages like this in general is that if moisture can seep into the packages just sitting there on the shelf, and once that moisture seeps in, then it can when it goes through the reflow oven, that heats up, the air can expand into a gas and can actually crack

**Dave Jones:** the plastic package of these things. So, yeah, just something to watch out for, but anyway, there's no desiccant bag in this one. Oh, yes there is. There it is.

**Dave Jones:** Little desiccant bag. Didn't see it. So, you don't have to read Chinese to be able to understand this data sheet. It's clearly plus minus 2% nominal tolerance there. 6 volts maximum input voltage very typical for these kind of low voltage low dropout regulators.

**Dave Jones:** Selectable output voltage from 1.5 volts to 5 volts in factory settable 0.1 volt increments. LCSC of course aren't going to carry all of the 0.1 inch voltage things. But hey, maybe you can you know, if you're serious about this and you could maybe order them direct from the manufacturer or maybe you can talk to LCSC and they might be able to source them for you.

**Dave Jones:** It would just be the part number difference at the end. 25 microamps quiescent current here. Looks like at V in at 4.3 volts, V out at 3.3. It's capable of 250 milliamps, which is quite a generous amount of current for a little saw 23 jelly bean regulator like this.

**Dave Jones:** Once again, you can get higher, you can get lower, but it's not too shabby. 0.2 volts dropout at 90 milliamps output current. That increases to 0.4 at 150. They don't tell you what the dropout is at 250 and they don't provide any graphs further on the data sheet.

**Dave Jones:** So, you just don't know. But hey, the whole idea is even if this data sheet, which doesn't have any performance graphs or anything like that, you know, just your basic data, there's no reason why you should avoid these types of chips if you qualify them.

**Dave Jones:** Which is you know, not an incredibly difficult process if you're serious about saving your bomb cost. You can qualify them, overload, temperature, very batch variability and all sorts of stuff.

**Dave Jones:** You can qualify these parts for your own in-house purposes and go, yep, we're going to use those. We're confident it's got X dropout and X performance under X load and all that sort of jazz.

**Dave Jones:** Anyway, typical line regulation there of 0.03% per volt So, in a SOT-23 package, it's a 1 and 1/2 cent jelly bean regulator. Power supply rejection ratio there, 50 dB.

**Dave Jones:** And it looks like it's got a current limit as well. If you short the output, it'll limit it to 30 milliamps. If you go up here, there it is.

**Dave Jones:** They've got a current limit there in the circuitry. There's not a lot of data on this thing, but who cares? I have 5 Why is it a 500 milliamps down here?

**Dave Jones:** Oh, that's absolute absolute maximum. I limit down here as 400. You know, you get what you get with these data sheets, but anyway, let's try out the fine mad voltage regulator for 1.5 cents.

**Dave Jones:** All right, let's power this thing up. Take a look. I've got it down on a little adapter down there, little SOT-23 jobby. Yes, I will No, I don't have any bypass caps cuz I thought we'd just uh have a look first to see uh the stability of thing without any bypass capacitors on it.

**Dave Jones:** Cuz this is a low dropout voltage regulator, an LDO. One of the classic issues with LDOs is uh stability. They can actually oscillate if you don't incorrect if you don't correctly load them with the correct amount of capacitance, the correct type of capacitor, the ESR, all that sort of stuff.

**Dave Jones:** So, they can potentially oscillate cuz they use a PNP or a P-channel uh pass element, which is inherently more unstable. And anyway, I won't go into the details, but the advantage of it is is that you get the low dropout voltage.

**Dave Jones:** For a 3.3 volt output voltage, you can only need to feed in say 3.4 volts or something like that. You know, if it's a 100 milliamps dropout, and of course that will change with current.

**Dave Jones:** So, let's actually I'm actually doing that at the moment. Actually had it loaded there. We've actually got no load at the moment. So, no load with no capacitance, absolutely no input or output capacitance.

**Dave Jones:** We're powering it from 5 V here. Our output here I am actually sensing. If you're wondering what this line is, this is actually the voltage sense line, which goes around to the back.

**Dave Jones:** And you can't see it, but there's actually external voltage sensing here. So, we're going to avoid any drops on the line actually going over when we load this thing down.

**Dave Jones:** And as you can see, 3.288 V there. No problems whatsoever. And you can see over on the scope here, like there's no oscillation at all. Well, nothing serious. We'll take a look at AC at the minute and in a minute.

**Dave Jones:** That's just DC there. Let's just change our input voltage here and see what happens. I know I've got absolutely no load. 4.3 3.4, sorry, input voltage and it's still outputting.

**Dave Jones:** There we go. It should 3.3. Oops. Yeah, it's dropping there, but anyway, that's all hunky-dory. So, let's actually Let Let's say 4 V input. Let's actually turn on a 100 mA load.

**Dave Jones:** So, there we go. Got a 100 mA load. You can see 100 mA on here. No problems and we're drawing 100 mA from the input because of course there's almost virtually no quiescent current in this thing.

**Dave Jones:** It's the order of, you know, what was it? 30 microamps or something? Tens of microamps. So, it's the input current is going to equal the output current and that's fine and dandy.

**Dave Jones:** Let's So, let's actually input So, let's increase our load current, shall we? Let's go up and nothing on our scope. It's looking good, isn't it? What was this? It was 300 It was 250, wasn't it?

**Dave Jones:** I think it said 400 Well, yeah. Yeah, we're starting to get some starting to get some funny business happening over here. Whoa, 400 Whoa. Anyway, 1.3 W output power and but it's still it's still regulated.

**Dave Jones:** So, that's AC coupling at 5 mV per division with that load there. Let's just switch the load off and on. And of course we can capture that. So, it's going to but that's basically going up to like 1.3 W.

**Dave Jones:** That's that's pretty abusive. And the thing is regulating that. It's handling that. No problems at all. All right, so let's see if we can capture a transient there as we switch it off and on.

**Dave Jones:** So, I'll set my trigger level just below that. So, we'll single shot capture that. So, let's switch that on. And yep, it really does not like that at all.

**Dave Jones:** So, that's terrible Muriel. Yep, look at that. There you go. So, we can see that it's just dropped. It's just dropped out completely there for a second, but uh it's kind of to be expected cuz our load is horrible.

**Dave Jones:** It's 390 mA. Okay, let's try that again but 100 mA this time. Bingo. There we go. We got So, don't worry about the one before. Oh, look at that.

**Dave Jones:** Isn't that a thing of beauty? When we switch it on, cuz we've got no output capacitance at all. But that's like it's pretty impressive for 100 mA load with no input or output capacitance.

**Dave Jones:** Fantastic. We can Let's whack on an output cap. See if we can get that to go away. All right, so I've got a 0.47 film cap across the output and ground there.

**Dave Jones:** Still no input capacitance. I've saved this as a reference waveform. So, that'll allow us to see the difference. Let's switch that off and on 100 mA load again. Bingo.

**Dave Jones:** Look at that. It's smaller, but it's still there. Look at that. But the response is basically still the same, but that extra output capacitance has helped. Let's go a bit larger.

**Dave Jones:** Well, I've gone a fair bit larger, uh 330 microfarads on the extended leads. Please forgive me. Ah, good enough for Australia. Let's go. And it's not even triggering now because it's just hunky-dory.

**Dave Jones:** Can we move the trigger point even closer to there? I suspect we may not even Yep, doesn't even get a blip. And that's what you expect cuz now our capacitance is more than enough capable to take that little switch-on transient there.

**Dave Jones:** So, yeah, anyway, it's still stable with 330 mic electro, no problems. Even with a 300 milliamp load, can't get that. Can't fold it. No problems. Anyway, just wanted to show you this is 10 millivolts per division.

**Dave Jones:** The There's no oscillation there. That's with it's max Oh. There you go. That's coupling through our probe. See our piezoelectric effect for you. Anyway, I'm at full load, 250 milliamps there.

**Dave Jones:** And we turn that off. Yeah, we can see at at no load, we can see a little bit of funny business going on there. And if we turn that on, tweak our load there, you can see it down at no load, there's some like lower frequency oscillation stuff there by the looks of it.

**Dave Jones:** So, anyway, that's that's not bad. That's with no output capacitance. That's crazy. And with half a mic output capacitance, change it in 1 milliamp increments two three Yeah, you can see it slowly start to change there, but basically that's I can wind the wick up way on that and No.

**Dave Jones:** This is a pretty stable part. I'm quite impressed. Okay, something pretty horrible now. No output capacitance with 330 microfarads right at the end of these long leads. I'll whack that in the back.

**Dave Jones:** There we go. Like there That is fine. That's at like almost 250 milliamps there. Of course, we get our big uh spike on our And of of course, we get our turn-on spike there.

**Dave Jones:** We'll see that. If we whoop, there we go. No problems whatsoever. Um so, yeah, this thing is stable with no or well, you wouldn't use it with no capacitive load.

**Dave Jones:** And the data sheet, unless you can read Chinese, I guess uh doesn't uh tell you a nominal um output capacitance or output capacitance type or an ESR range or anything like that.

**Dave Jones:** But of course, you'd put your nominal one, say you know, typically 1 microfarad uh ceramic across the output is uh usually fine for an LDO like this. Okay, let's be mean and look at what happens if we short our output.

**Dave Jones:** So, we're going to have a look at uh what sort of current it's going to take up here. Supposed to have a current limit. Yeah, there we go. It's dropping Now, wasn't it supposed to have like 30 milliamps or something?

**Dave Jones:** But anyway, it's dropping down to 120 milliamps. So, it's It's just oscillated the buggery over here. Wow, what's going on there? Wow. Check out that. I'm at 20 mV 50 mV per division.

**Dave Jones:** That is like I I got the short like directly across there like that. Of Of you know, there's some like there's some resistance in there. So, obviously something's happening.

**Dave Jones:** That's 50 mV per division, you know, the extra connections and stuff like that. So, it's not a direct short on the pins. And you can see So, there you go.

**Dave Jones:** About 70 Hz there. It's um entered some sort of you know current regulation uh you know pulse mode. And if we remove it, of course, we'll uh shoot back Well, let's try and get the recovery on that, shall we?

**Dave Jones:** So, I'm going to pull the plug on that. And What? Ah, no, we killed it. What's going on? Something's What What What What 0.1 Don't Silly me. Yeah, I had the uh had the load on there.

**Dave Jones:** So, it looks like it wouldn't recover from short to uh to the uh 250 mA load. But as soon as I turn the load off, of course, it recovered back like that.

**Dave Jones:** So, that's interesting. I wonder I I'll I'll try that again, but like at a lower current, say 50 mA or something. And so, 50 mA load this time. So, we're going from short back to a 50 mA constant current load, of course.

**Dave Jones:** It's not a uh it's not a resistor. It's an active Oh, look at that. Isn't that neat? Wow. And that's a something sort of started to recover there. Oh, well, of course, you know, there's could be contact uh bounce in there, of course.

**Dave Jones:** So, something happened. And we're at 5 ms per division. So, yeah, that could easily be like contact uh stuff. But yeah, it ramps back up. It recovers very nicely.

**Dave Jones:** I'm quite happy with that. No wackers. Like there And there's no oscillation. And that's once again with no output capac Well, sorry. No, I think I still got my 330 mic.

**Dave Jones:** My 330 microfarads plugged into the other end. I mean, that's as horrible as it gets. Wow. Okay, we'll try that again, but with no output capacitance this time. So, I got none at the end of the line.

**Dave Jones:** None on the board here. So, oh, there we go. Oh, that's that's what happens when you short it out, by the way. There you go. And 50 milliamp constant current load.

**Dave Jones:** So, there's going to be like a response for the electronic load, cuz it's an electronic software function which does it. So, it's not as good as like say having a resistor load and stuff like that.

**Dave Jones:** So, if you're testing like proper pulse response of a regulator or a power supply, you know, you need to do it with a proper resistive load, but here we go.

**Dave Jones:** Ah, there we go. Look at that. We got a similar Is that the same? Yeah, cuz we're at No, 5 milli seconds per division, and there's a little bit of over shoot there this time.

**Dave Jones:** Little bit, not much. Oh, yeah, oh, there's something, and then a little dip. But once again, as I said, there's no capacitance on there. But yeah, it's got this little shelf in there.

**Dave Jones:** So, obviously that's I reckon it'll do the same it'll repeat that. I reckon that that'll be repeatable. So, I reckon there's no that's not contact bounce. Yep. There you go.

**Dave Jones:** So, there's something in there that gives this like little shelf in there from from recovery from short recovery back up. But still, that's pretty good. These things It's almost bulletproof.

**Dave Jones:** One more time, but I've got Yeah, there we go. That's with the half a mic capacitance on there. So, no worries. And then we see that little dip, but it recovers quite nicely from that short.

**Dave Jones:** Of course, you know, this is obviously not something you hugely want to care about in Well, you might in normal operation, but of course, with the building current limit, what you're really concerned with is that you don't don't blow the ass out of your regulator, you don't release the magic smoke when, you know, if the mode on it shorts and you want it to recover.

**Dave Jones:** And this is pretty good. Okay, so let's look at the dropout voltage at its maximum rated current, 250 milliamps. It's not its absolute max, but that's its maximum recommended.

**Dave Jones:** And of course, we're getting our It's pretty It's pretty darn accurate, this, even though like plus minus 2%, of course, you'd have to test, you know, you know, a dozen units or 50 or 100 units or something, you know, to get an idea of normal accuracy, especially across different production reels as well, you know, if they all come from the same die wafer, then, you know, they're all going to be They should all

**Dave Jones:** be, you know, reasonably similar. Anyway, it's bang on. All right, so let's drop our voltage down. So, this is our input voltage here. I'm going to drop that down.

**Dave Jones:** And we're looking at the AC output here. So, 10 millivolts per Oh, there we go. Yep. So, dropout Oh, yeah, 3. Oh, yep, there we go. Let's call that it What?

**Dave Jones:** 300 and Yeah, let's call it 300 millivolts. 300 millivolts dropout. And by dropout, it means it drops out of regulation. And you can see that like it's still like it's still the voltage is still there, but it's You can see that it's becoming a bit unstable.

**Dave Jones:** Will that change? If we remove our capacitance? No, look at that. Wow. No capaci- no input output capacitance at all. That's crazy. Let's put 330 mic on that. No.

**Dave Jones:** Still in the same business. The response is all the same. So, this The response of this thing with a capacitive load, it's like it it really almost doesn't matter.

**Dave Jones:** Once again, I I recommend using it without a output capacitors. That's just silly. Um but yeah, it's it's really stable. So, quite impressed. Um yeah, so 300 mV uh dropout at full rated current.

**Dave Jones:** Let's go down to 100 mA and and let's keep going down down. There we go. So, at 100 mA, let's say the dropout is only talking at 150 mA dropout there.

**Dave Jones:** If we go down to say 10 mA, you know, not much at all, then our dropout voltage should be quite low. Yeah, there we go. Uh 3.3 like it's it's naff all.

**Dave Jones:** Like it's tens of millivolts uh dropout. So, yeah. This thing's pretty decent. I like it. And for those curious to know about ripple rejection, I'm feeding it from my function gen, which is generating uh 5 V with 500 mV uh peak-to-peak uh sine wave on there at 1 kHz.

**Dave Jones:** And my output there on the second channel, the green one, there you go. Rock solid. And if we AC couple that, uh there's nothing there. So, it is it's just fine.

**Dave Jones:** 2 kHz, 3, 4, 5, 6, 7, 8, 9, 10. Come on. Come on. And we've got no output capacitors, too, by the way. 30 kHz now. Of course, that was only a lower load there because I'm powering it from a a function gen here.

**Dave Jones:** I couldn't be bothered like getting a higher power uh solution for this. This is at 40 mHz mHz mHz 40 mA and get your units right, Dave. And 40 mA load, and that's where back to our 1 kHz um and it's it's just fine.

**Dave Jones:** 1 and 1/2 cents for this regulator. And a lot of people would say, "I wouldn't trust this thing any further than I can read the data sheet." Uh well, you know, like fair enough.

**Dave Jones:** But you know, if you're in the business where cents matters um on parts, and you know, you've got a lot of these on your board, and you're manufacturing a lot of boards and all that sort of stuff, and this seems like a good little bulletproof regulator.

**Dave Jones:** It's It's accuracy seems fine. It's load regulation seems fine. It's dropout performance is, you know, more than good enough. It's stability with capacitive loads or lack thereof, and, you know, distributed at the end of long lines, it seems fine as well.

**Dave Jones:** Seems absolutely bulletproof from a stability point of view. It's recovery from shorts is fine. Everything's hunky-dory in this thing. It It's almost like a bulletproof little, you know, jelly bean 1.5 cent sub-23 voltage regulator.

**Dave Jones:** So, it's like it's well worthy of consideration. Of course, like I haven't tested noise performance, and there's a whole bunch of other parameters which you can test. You could spend weeks qualifying a part like this.

**Dave Jones:** You know, I haven't tested it over temperature and all sorts of stuff. So, it might be worth considering these like, you know, generic Asian brand parts for your next project if you're looking to save the cost cuz haven't been able to fault this thing yet.

**Dave Jones:** So, pretty impressed by that. 1.5 cents. It's worth every microcent this part. So, anyway, if you like that video, please give it a big thumbs up, and as always, you can discuss down below.

**Dave Jones:** Let us know if you've used any of these, you know, non non mainstream in quote marks. I mean, these parts are probably bog standard in China used in every, you know, $2.40 novelty gadget that you can get.

**Dave Jones:** And probably just absolutely perfect little regulators. It's just that they're just not one of your, you know, Western brand known suppliers like your, you know, your TIs or your Nationals or whoever.

**Dave Jones:** And this thing it seems to work a treat. It's one like it's 1/5 the cost of any at least 1/5 the cost. It's just crazy. And that's from a catalog supplier.

**Dave Jones:** Imagine what if you did a deal if you needed hundreds of thousands or millions of these things and you bought them from directly from the manufacturer assuming that you can do that of course.

**Dave Jones:** I'm sure you could and like how much would these things cost when you like really wheel and deal the price let alone just from a off the shelf off like stock off the shelf catalog supplier like LCSC.

**Dave Jones:** It's nuts. Catch you next time.
