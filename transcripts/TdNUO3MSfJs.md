---
video_id: TdNUO3MSfJs
title: EEVblog #1147 - 1 Cent Regulator! That's MAD!
url: https://www.youtube.com/watch?v=TdNUO3MSfJs
source: youtube-asr
---

**Dave Jones:** Hi, sorry about the new office background here. I didn't have time to build it scale or to paint it. In a previous video and previous couple of videos, we looked at the 3 cent microcontroller from Paducah and we got that from LCSC, which is a

**Dave Jones:** Chinese catalog type Digi-Key kind of competitor Digi-Key Mouser Farnell's catalog competitor. And I thought we'd take a look at another part from them. It's not a microcontroller because well microcontrollers are expensive, right? At 3 cents. How about another jelly bean

**Dave Jones:** part which you'd be no doubt familiar with, the low dropout voltage regulator. How cheap can you get these on LCSC? Well, turns out you can get them for 1 cent or little bit of maybe 1 and 1/2 cents. I'm rounding down to 1 cent. The

**Dave Jones:** 1 cent linear regulator. I bought 3,000 of them. Let's check them out. So why on earth would you want a 1 cent voltage regulator? Well, why not? When you're optimizing the bill of materials for your product, it could matter. And with

**Dave Jones:** modern products like FPGAs and other like, you know, really high density logic, they often require lots of low voltage power supplies, not just 3.3 volts, you know, 2.5 volts, 1.8 volts, 1.2 volts, you know, even like 0.8 volt

**Dave Jones:** cores, 1 volt cores and things like that. So it's not uncommon to need even like half a dozen different voltage rails inside your product. And that really adds up when you're talking about, you know, selling thousands of items and you might have, you know,

**Dave Jones:** three or even five voltage regulators per products. So it can often pay you to have like a cheap jelly bean part like this voltage regulator, for example. This one's actually a fixed 3.3 volt one, but we might have a look at

**Dave Jones:** adjustable ones just to show you how cheap they are. and well, let's go to Digi-Key, for example, and do a search here on I've sorted by price here in volume. They start at like 3,600, they start at 4.5 cents, which is pretty

**Dave Jones:** cheap, but you'll note that's obsolete from a company that I've never heard of, Skyworks Solutions Inc. Meh, it's a nano power range, you know, but if you go down here, like the next one that's actually active, which is the cheapest,

**Dave Jones:** is basically 6 cents in uh volume. So, like 3,000 volume. And you add these up, you have multiple products times 1,000, you're trying to reduce your bill of materials and stuff like that. Well, why spend, you know, 6 cents plus uh tax,

**Dave Jones:** you know, they're 8.5 cents, stuff like that. Might not sound like a lot, but when trying to optimize your bill of materials, these sorts of stuff really add up. So, if you go over to LCSC here, which is kind of like the Chinese uh

**Dave Jones:** kind of competitor to Digi-Key that that specializes in having these Chinese brands. I didn't do a previous video looking at these. And if you search for positive linear regulators well, they've got 898 parts here. And here we go,

**Dave Jones:** look, the cheapest one, the LC6202 from Shenzhen Fuman Electric Corp um is like in the order of 1.6, but the one we're going to look at here that I've actually got 3,000 of. Why 3,000? Because they came on a reel of 3,000, and it was cheap as,

**Dave Jones:** so I just got a reel of 3,000 cuz they might come in handy. Anyway, the SC662K, and this is the 3.3 volt version. You can get other versions with uh different fixed voltages, and there's also And if you want to search for adjustable ones,

**Dave Jones:** you can search for adjustable. Often, it's sometimes better to say uh include like a jelly bean adjustable voltage regulator, so that uh you can just choose whatever. So, you've got the one bill of materials item there, but then

**Dave Jones:** you need your different resistors, three pick and place parts as opposed to just one and and stuff like that. So, it's nice just to have cuz you're always going to need a 3.3 V rail. So, it's nice to have this. Anyway, look at the

**Dave Jones:** price. In 20 of quantity, they're only 2.4 cents. And when you start talking serious volume here, 1 and 1/2 cents. And if you go up there, it's like 1.44 cents. And you got to remember, this is not direct from the manufacturer. This

**Dave Jones:** is from a Chinese Digikey equivalent catalog supplier who actually have stock. In this case, they don't actually have much of this. But look, these ones up here, 8,700, you know, 5,000, 4,000, 30,000 in stock, right? There's no shortage of these ones. So, here's

**Dave Jones:** another one that I had a look at. Um this one comes from Nat Linear. You might think, "Oh, National Linear. That sounds legit." No, Nat Linear is natlinear.com. It's China um it's got nothing to do with National Semiconductor or Linear

**Dave Jones:** Technology, but they said, "Hey, they're famous names. We'll just join them together. Hey, we'll sound legit." There you go. So, they sell they have this 300 mA linear regulator in different packages. It's not that it's a little bit more

**Dave Jones:** expensive than the one we've got here. Um but anyway, all Chinese data sheets. So, yep, knock yourself out. This one actually does have curves, but the one we're going to play with, the Fenjin Fuman Electric Co. If we have a look at

**Dave Jones:** the data sheet, Shenzhen Finemad Finemad Electronics Group. This is hilarious. So, that sounds ridiculous, the Shenzhen Finemad Electronics Group. In fact, I think I've they've got their name wrong in their own name wrong in the data sheet. Cuz if

**Dave Jones:** you go over here, it's the Shenzhen Finemade Electronics Group. Maybe it's not the same company. Like, anyway, they're listed on the Chinese stock exchange. They're currently 20 Chinese bucks. There you go, for the share price. Um I assume it's the same company. Anyway,

**Dave Jones:** maybe there is a Shenzhen Finedream, but it's nuts. But, it sounds like the right company. Shenzhen Finedream engages in design, development, packaging, testing, and sale of electronic and digital analog hybrid integrated circuits in China used in power management class.

**Dave Jones:** Bingo. And all sorts of So, it it sounds like them. Um and they superchip.cn. Is that them? Let's check them out. Yep, it's them. superchip.cn. So, Finedream. And yep, there it is. There's your data sheet. Once again, only available it's exactly the same

**Dave Jones:** one. So, FM is Finedream. And here's the actual part I've got here. It says 80 milliamps there, but that would be 18 millivolts drop out at 18 milliamps current. And you'll notice that they actually come in a hermetically sealed package like this.

**Dave Jones:** You don't generally don't want to take these out of their hermetically sealed packages like this until it gets to the pick and place machine. The reason that they do this, and this one doesn't include it, but they often include a

**Dave Jones:** little one of those dry desiccant bags in there to absorb absorb the moisture. And the whole part about that is that it keeps moisture from leaking into the parts before reflow. Plastic molded packages like this in general is that if moisture can seep

**Dave Jones:** into the packages just sitting there on the shelf, and once that moisture seeps in, then it can when it goes through the reflow oven, that heats up, the air can expand into a gas and can actually crack the plastic package of these things. So,

**Dave Jones:** yeah, just something to watch out for, but anyway, there's no desiccant bag in this one. Oh, yes there is. There it is. Little desiccant bag. Didn't see it. So, you don't have to read Chinese to be able to understand this data sheet. It's

**Dave Jones:** clearly plus minus 2% nominal tolerance there. 6 volts maximum input voltage very typical for these kind of low voltage low dropout regulators. Selectable output voltage from 1.5 volts to 5 volts in factory settable 0.1 volt increments. LCSC of course aren't going

**Dave Jones:** to carry all of the 0.1 inch voltage things. But hey, maybe you can you know, if you're serious about this and you could maybe order them direct from the manufacturer or maybe you can talk to LCSC and they might be able to source

**Dave Jones:** them for you. It would just be the part number difference at the end. 25 microamps quiescent current here. Looks like at V in at 4.3 volts, V out at 3.3. It's capable of 250 milliamps, which is quite a generous amount of

**Dave Jones:** current for a little saw 23 jelly bean regulator like this. Once again, you can get higher, you can get lower, but it's not too shabby. 0.2 volts dropout at 90 milliamps output current. That increases to 0.4 at 150. They don't

**Dave Jones:** tell you what the dropout is at 250 and they don't provide any graphs further on the data sheet. So, you just don't know. But hey, the whole idea is even if this data sheet, which doesn't have any performance graphs or anything like

**Dave Jones:** that, you know, just your basic data, there's no reason why you should avoid these types of chips if you qualify them. Which is you know, not an incredibly difficult process if you're serious about saving your bomb cost. You

**Dave Jones:** can qualify them, overload, temperature, very batch variability and all sorts of stuff. You can qualify these parts for your own in-house purposes and go, yep, we're going to use those. We're confident it's got X dropout and X performance under X load and all that

**Dave Jones:** sort of jazz. Anyway, typical line regulation there of 0.03% per volt So, in a SOT-23 package, it's a 1 and 1/2 cent jelly bean regulator. Power supply rejection ratio there, 50 dB. And it looks like it's got a current

**Dave Jones:** limit as well. If you short the output, it'll limit it to 30 milliamps. If you go up here, there it is. They've got a current limit there in the circuitry. There's not a lot of data on this thing,

**Dave Jones:** but who cares? I have 5 Why is it a 500 milliamps down here? Oh, that's absolute absolute maximum. I limit down here as 400. You know, you get what you get with these data sheets, but anyway, let's try

**Dave Jones:** out the fine mad voltage regulator for 1.5 cents. All right, let's power this thing up. Take a look. I've got it down on a little adapter down there, little SOT-23 jobby. Yes, I will No, I don't have any bypass caps

**Dave Jones:** cuz I thought we'd just uh have a look first to see uh the stability of thing without any bypass capacitors on it. Cuz this is a low dropout voltage regulator, an LDO. One of the classic issues with LDOs is uh

**Dave Jones:** stability. They can actually oscillate if you don't incorrect if you don't correctly load them with the correct amount of capacitance, the correct type of capacitor, the ESR, all that sort of stuff. So, they can potentially oscillate cuz they use a PNP or a

**Dave Jones:** P-channel uh pass element, which is inherently more unstable. And anyway, I won't go into the details, but the advantage of it is is that you get the low dropout voltage. For a 3.3 volt output voltage, you can only need to

**Dave Jones:** feed in say 3.4 volts or something like that. You know, if it's a 100 milliamps dropout, and of course that will change with current. So, let's actually I'm actually doing that at the moment. Actually had it loaded there. We've

**Dave Jones:** actually got no load at the moment. So, no load with no capacitance, absolutely no input or output capacitance. We're powering it from 5 V here. Our output here I am actually sensing. If you're wondering what this line is, this is

**Dave Jones:** actually the voltage sense line, which goes around to the back. And you can't see it, but there's actually external voltage sensing here. So, we're going to avoid any drops on the line actually going over when we load this

**Dave Jones:** thing down. And as you can see, 3.288 V there. No problems whatsoever. And you can see over on the scope here, like there's no oscillation at all. Well, nothing serious. We'll take a look at AC at the minute and in a minute. That's

**Dave Jones:** just DC there. Let's just change our input voltage here and see what happens. I know I've got absolutely no load. 4.3 3.4, sorry, input voltage and it's still outputting. There we go. It should 3.3. Oops. Yeah, it's dropping there, but

**Dave Jones:** anyway, that's all hunky-dory. So, let's actually Let Let's say 4 V input. Let's actually turn on a 100 mA load. So, there we go. Got a 100 mA load. You can see 100 mA on here. No problems and

**Dave Jones:** we're drawing 100 mA from the input because of course there's almost virtually no quiescent current in this thing. It's the order of, you know, what was it? 30 microamps or something? Tens of microamps. So, it's the input current is going to

**Dave Jones:** equal the output current and that's fine and dandy. Let's So, let's actually input So, let's increase our load current, shall we? Let's go up and nothing on our scope. It's looking good, isn't it? What was this? It was 300 It

**Dave Jones:** was 250, wasn't it? I think it said 400 Well, yeah. Yeah, we're starting to get some starting to get some funny business happening over here. Whoa, 400 Whoa. Anyway, 1.3 W output power and but it's still it's still regulated. So, that's AC coupling

**Dave Jones:** at 5 mV per division with that load there. Let's just switch the load off and on. And of course we can capture that. So, it's going to but that's basically going up to like 1.3 W. That's that's pretty abusive.

**Dave Jones:** And the thing is regulating that. It's handling that. No problems at all. All right, so let's see if we can capture a transient there as we switch it off and on. So, I'll set my trigger level just below that.

**Dave Jones:** So, we'll single shot capture that. So, let's switch that on. And yep, it really does not like that at all. So, that's terrible Muriel. Yep, look at that. There you go. So, we can see that it's just dropped.

**Dave Jones:** It's just dropped out completely there for a second, but uh it's kind of to be expected cuz our load is horrible. It's 390 mA. Okay, let's try that again but 100 mA this time. Bingo. There we go. We got So, don't worry about the one

**Dave Jones:** before. Oh, look at that. Isn't that a thing of beauty? When we switch it on, cuz we've got no output capacitance at all. But that's like it's pretty impressive for 100 mA load with no input or output capacitance. Fantastic. We can

**Dave Jones:** Let's whack on an output cap. See if we can get that to go away. All right, so I've got a 0.47 film cap across the output and ground there. Still no input capacitance. I've saved this as a reference waveform. So,

**Dave Jones:** that'll allow us to see the difference. Let's switch that off and on 100 mA load again. Bingo. Look at that. It's smaller, but it's still there. Look at that. But the response is basically still the same, but that extra output capacitance

**Dave Jones:** has helped. Let's go a bit larger. Well, I've gone a fair bit larger, uh 330 microfarads on the extended leads. Please forgive me. Ah, good enough for Australia. Let's go. And it's not even triggering now because it's just hunky-dory. Can we

**Dave Jones:** move the trigger point even closer to there? I suspect we may not even Yep, doesn't even get a blip. And that's what you expect cuz now our capacitance is more than enough capable to take that little switch-on transient

**Dave Jones:** there. So, yeah, anyway, it's still stable with 330 mic electro, no problems. Even with a 300 milliamp load, can't get that. Can't fold it. No problems. Anyway, just wanted to show you this is 10 millivolts per division. The There's no oscillation there. That's

**Dave Jones:** with it's max Oh. There you go. That's coupling through our probe. See our piezoelectric effect for you. Anyway, I'm at full load, 250 milliamps there. And we turn that off. Yeah, we can see at at no load, we can see a

**Dave Jones:** little bit of funny business going on there. And if we turn that on, tweak our load there, you can see it down at no load, there's some like lower frequency oscillation stuff there by the looks of it. So,

**Dave Jones:** anyway, that's that's not bad. That's with no output capacitance. That's crazy. And with half a mic output capacitance, change it in 1 milliamp increments two three Yeah, you can see it slowly start to change there, but basically that's

**Dave Jones:** I can wind the wick up way on that and No. This is a pretty stable part. I'm quite impressed. Okay, something pretty horrible now. No output capacitance with 330 microfarads right at the end of these long leads. I'll whack that in the

**Dave Jones:** back. There we go. Like there That is fine. That's at like almost 250 milliamps there. Of course, we get our big uh spike on our And of of course, we get our turn-on spike there. We'll see that. If we whoop, there we go.

**Dave Jones:** No problems whatsoever. Um so, yeah, this thing is stable with no or well, you wouldn't use it with no capacitive load. And the data sheet, unless you can read Chinese, I guess uh doesn't uh tell you a nominal

**Dave Jones:** um output capacitance or output capacitance type or an ESR range or anything like that. But of course, you'd put your nominal one, say you know, typically 1 microfarad uh ceramic across the output is uh usually fine for an LDO

**Dave Jones:** like this. Okay, let's be mean and look at what happens if we short our output. So, we're going to have a look at uh what sort of current it's going to take up here. Supposed to have a current limit.

**Dave Jones:** Yeah, there we go. It's dropping Now, wasn't it supposed to have like 30 milliamps or something? But anyway, it's dropping down to 120 milliamps. So, it's It's just oscillated the buggery over here. Wow, what's going on there? Wow.

**Dave Jones:** Check out that. I'm at 20 mV 50 mV per division. That is like I I got the short like directly across there like that. Of Of you know, there's some like there's some resistance in there. So, obviously something's

**Dave Jones:** happening. That's 50 mV per division, you know, the extra connections and stuff like that. So, it's not a direct short on the pins. And you can see So, there you go. About 70 Hz there. It's um entered some sort of you know current

**Dave Jones:** regulation uh you know pulse mode. And if we remove it, of course, we'll uh shoot back Well, let's try and get the recovery on that, shall we? So, I'm going to pull the plug on that. And What? Ah, no, we killed it. What's going

**Dave Jones:** on? Something's What What What What 0.1 Don't Silly me. Yeah, I had the uh had the load on there. So, it looks like it wouldn't recover from short to uh to the uh 250 mA load. But as soon as I turn

**Dave Jones:** the load off, of course, it recovered back like that. So, that's interesting. I wonder I I'll I'll try that again, but like at a lower current, say 50 mA or something. And so, 50 mA load this time. So, we're going from short back to a 50

**Dave Jones:** mA constant current load, of course. It's not a uh it's not a resistor. It's an active Oh, look at that. Isn't that neat? Wow. And that's a something sort of started to recover there. Oh, well, of course, you know, there's could be

**Dave Jones:** contact uh bounce in there, of course. So, something happened. And we're at 5 ms per division. So, yeah, that could easily be like contact uh stuff. But yeah, it ramps back up. It recovers very nicely. I'm quite happy with that.

**Dave Jones:** No wackers. Like there And there's no oscillation. And that's once again with no output capac Well, sorry. No, I think I still got my 330 mic. My 330 microfarads plugged into the other end. I mean, that's as horrible as

**Dave Jones:** it gets. Wow. Okay, we'll try that again, but with no output capacitance this time. So, I got none at the end of the line. None on the board here. So, oh, there we go. Oh, that's that's what happens when you short it out, by

**Dave Jones:** the way. There you go. And 50 milliamp constant current load. So, there's going to be like a response for the electronic load, cuz it's an electronic software function which does it. So, it's not as good as like say

**Dave Jones:** having a resistor load and stuff like that. So, if you're testing like proper pulse response of a regulator or a power supply, you know, you need to do it with a proper resistive load, but here we go. Ah, there we go. Look at that. We got a

**Dave Jones:** similar Is that the same? Yeah, cuz we're at No, 5 milli seconds per division, and there's a little bit of over shoot there this time. Little bit, not much. Oh, yeah, oh, there's something, and then a little dip. But once again, as I said, there's

**Dave Jones:** no capacitance on there. But yeah, it's got this little shelf in there. So, obviously that's I reckon it'll do the same it'll repeat that. I reckon that that'll be repeatable. So, I reckon there's no that's not contact bounce.

**Dave Jones:** Yep. There you go. So, there's something in there that gives this like little shelf in there from from recovery from short recovery back up. But still, that's pretty good. These things It's almost bulletproof. One more time, but I've got Yeah, there we go. That's

**Dave Jones:** with the half a mic capacitance on there. So, no worries. And then we see that little dip, but it recovers quite nicely from that short. Of course, you know, this is obviously not something you hugely want to care about in Well, you might in normal

**Dave Jones:** operation, but of course, with the building current limit, what you're really concerned with is that you don't don't blow the ass out of your regulator, you don't release the magic smoke when, you know, if the mode on it

**Dave Jones:** shorts and you want it to recover. And this is pretty good. Okay, so let's look at the dropout voltage at its maximum rated current, 250 milliamps. It's not its absolute max, but that's its maximum recommended. And of course, we're

**Dave Jones:** getting our It's pretty It's pretty darn accurate, this, even though like plus minus 2%, of course, you'd have to test, you know, you know, a dozen units or 50 or 100 units or something, you know, to get an

**Dave Jones:** idea of normal accuracy, especially across different production reels as well, you know, if they all come from the same die wafer, then, you know, they're all going to be They should all be, you know, reasonably similar. Anyway, it's bang on. All right, so

**Dave Jones:** let's drop our voltage down. So, this is our input voltage here. I'm going to drop that down. And we're looking at the AC output here. So, 10 millivolts per Oh, there we go. Yep. So, dropout Oh, yeah, 3.

**Dave Jones:** Oh, yep, there we go. Let's call that it What? 300 and Yeah, let's call it 300 millivolts. 300 millivolts dropout. And by dropout, it means it drops out of regulation. And you can see that like it's still like it's still the voltage

**Dave Jones:** is still there, but it's You can see that it's becoming a bit unstable. Will that change? If we remove our capacitance? No, look at that. Wow. No capaci- no input output capacitance at all. That's crazy. Let's put 330 mic

**Dave Jones:** on that. No. Still in the same business. The response is all the same. So, this The response of this thing with a capacitive load, it's like it it really almost doesn't matter. Once again, I I recommend using it without a

**Dave Jones:** output capacitors. That's just silly. Um but yeah, it's it's really stable. So, quite impressed. Um yeah, so 300 mV uh dropout at full rated current. Let's go down to 100 mA and and let's keep going down down. There we go. So, at 100 mA, let's say

**Dave Jones:** the dropout is only talking at 150 mA dropout there. If we go down to say 10 mA, you know, not much at all, then our dropout voltage should be quite low. Yeah, there we go. Uh 3.3 like it's it's naff all.

**Dave Jones:** Like it's tens of millivolts uh dropout. So, yeah. This thing's pretty decent. I like it. And for those curious to know about ripple rejection, I'm feeding it from my function gen, which is generating uh 5 V with 500 mV uh peak-to-peak

**Dave Jones:** uh sine wave on there at 1 kHz. And my output there on the second channel, the green one, there you go. Rock solid. And if we AC couple that, uh there's nothing there. So, it is it's just fine. 2 kHz, 3, 4, 5, 6, 7, 8, 9,

**Dave Jones:** 10. Come on. Come on. And we've got no output capacitors, too, by the way. 30 kHz now. Of course, that was only a lower load there because I'm powering it from a a function gen here. I couldn't be

**Dave Jones:** bothered like getting a higher power uh solution for this. This is at 40 mHz mHz mHz 40 mA and get your units right, Dave. And 40 mA load, and that's where back to our 1 kHz um and it's

**Dave Jones:** it's just fine. 1 and 1/2 cents for this regulator. And a lot of people would say, "I wouldn't trust this thing any further than I can read the data sheet." Uh well, you know, like fair enough. But you know, if you're in the business

**Dave Jones:** where cents matters um on parts, and you know, you've got a lot of these on your board, and you're manufacturing a lot of boards and all that sort of stuff, and this seems like a good little bulletproof regulator. It's It's

**Dave Jones:** accuracy seems fine. It's load regulation seems fine. It's dropout performance is, you know, more than good enough. It's stability with capacitive loads or lack thereof, and, you know, distributed at the end of long lines, it seems fine as well. Seems

**Dave Jones:** absolutely bulletproof from a stability point of view. It's recovery from shorts is fine. Everything's hunky-dory in this thing. It It's almost like a bulletproof little, you know, jelly bean 1.5 cent sub-23 voltage regulator. So, it's like it's well worthy of consideration. Of

**Dave Jones:** course, like I haven't tested noise performance, and there's a whole bunch of other parameters which you can test. You could spend weeks qualifying a part like this. You know, I haven't tested it over temperature and all sorts of stuff.

**Dave Jones:** So, it might be worth considering these like, you know, generic Asian brand parts for your next project if you're looking to save the cost cuz haven't been able to fault this thing yet. So, pretty impressed by that. 1.5 cents.

**Dave Jones:** It's worth every microcent this part. So, anyway, if you like that video, please give it a big thumbs up, and as always, you can discuss down below. Let us know if you've used any of these, you know, non non mainstream in

**Dave Jones:** quote marks. I mean, these parts are probably bog standard in China used in every, you know, $2.40 novelty gadget that you can get. And probably just absolutely perfect little regulators. It's just that they're just not one of your, you know, Western brand

**Dave Jones:** known suppliers like your, you know, your TIs or your Nationals or whoever. And this thing it seems to work a treat. It's one like it's 1/5 the cost of any at least 1/5 the cost. It's just crazy. And that's from a catalog supplier.

**Dave Jones:** Imagine what if you did a deal if you needed hundreds of thousands or millions of these things and you bought them from directly from the manufacturer assuming that you can do that of course. I'm sure you could and like

**Dave Jones:** how much would these things cost when you like really wheel and deal the price let alone just from a off the shelf off like stock off the shelf catalog supplier like LCSC. It's nuts. Catch you next time.
