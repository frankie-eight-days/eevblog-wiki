---
video_id: Cw2AjcczHg4
title: EEVblog #1030 - $20 DIY Bench Power Supply!
url: https://www.youtube.com/watch?v=Cw2AjcczHg4
source: youtube-asr
timestamps: {"0": 0, "1": 33, "2": 68, "3": 101, "4": 133, "5": 162, "6": 183, "7": 213, "8": 234, "9": 250, "10": 284, "11": 318, "12": 351, "13": 379, "14": 398, "15": 418, "16": 454, "17": 481, "18": 503, "19": 535, "20": 565, "21": 593, "22": 623, "23": 647, "24": 670, "25": 695, "26": 716, "27": 747, "28": 766, "29": 793, "30": 813, "31": 836, "32": 857, "33": 879, "34": 910, "35": 926, "36": 952, "37": 985, "38": 1011, "39": 1033, "40": 1045, "41": 1065, "42": 1093, "43": 1125, "44": 1152, "45": 1173, "46": 1195, "47": 1224, "48": 1258, "49": 1279, "50": 1294, "51": 1322, "52": 1340}
---

**Dave Jones:** Hi, here's a do-it-yourself power supply that you can build for about 20, 25 bucks, maybe, and you can do it in about like 30 minutes, which is what it took me to build this one. It works on an external plug pack of any voltage, and I just built it into a case that I had lying around, had some binding posts lying around, and it's a little cute little bench power supply, and it can do 0 to 20 volts output, up to 0 to 2 amps constant current and constant voltage,

**Dave Jones:** and it's got this neat display here that basically shows you all the current and output power. And the interface here, a nice little multi-line LCD that shows the set voltage, the output voltage, the set current, the output current, and the power, and some preset voltages. There's an on-off button here, which is not on its output on-off. There we got ourselves a selection knob, and if we switch it on here, it's got constant See, we're in constant voltage mode, and we've got an output voltage of 5 volts and an output

**Dave Jones:** of 0.99 amps, and that matches our load up here precisely. Beauty. So, how do you build one of these puppies for like 20-odd dollars and build it in 30 minutes? Well, you might have guessed that this module is a complete off-the-shelf module. This is not a kit. I'll open it up and show you that there's virtually nothing in here except ta-da! This little module here that you can buy on eBay, AliExpress, or whoever.

**Dave Jones:** Not actually sure who manufactures this, but it's a very cute little module that we'll take a look at, and there's basically just the external DC in and the output. It's all self-contained, but some company designs and manufactures a complete range of these with a whole different bunch of voltage and current and power output capabilities. And you can like I found a price one of this module in particular the 20 volt 2 amp one was like 17 US dollars on eBay delivered.

**Dave Jones:** And that's your entire bench power supply. It's ridiculous. So the one we've got here is here's the manual that comes with it. It's in Chinese or English here. It's the DP 20 V 2 amp module. And this is a 4.5 to 23 volt input which is great. So you could actually power it from a USB, you know, power bank if you want to any USB thing you wanted to. I haven't tried it that low yet, but I've just using a 12 volt 3 amp plug pack. But basically you

**Dave Jones:** can throw any plug pack. I mean, if you haven't got a whole bunch of spare plug packs sitting around from old laptops or any old gear or whatever then well you're not really trying. So yeah, you don't have to buy anything else just the module and a couple of binding posts and a DC jack and that's basically it.

**Dave Jones:** 0 to 20 volts output 0 to 2 amps maximum 40 watts. I am doubting that. I haven't actually tested it yet, but I am very much doubting it. Specs aren't going to set the world on fire in terms of peak to peak ripple. It's a switching converter of course. It's not a linear converter, but hey, for for 20 bucks like you can't complain. This thing's great. And if you're not a fan of the real tiny display down here, you can get other ones like this one. I could

**Dave Jones:** actually power it up. This is it from the you know, the same anonymous designer manufacturer whoever it is. If I find out who it is, I'll link it in down below. But this is a input voltage range 6 to 40 volts. It's got a larger, you know, a better looking display like this. And uh this one is a higher power device. It's got a larger heat sink.

**Dave Jones:** I'll show you the other one that I'm uh using but uh yeah, this is a higher power job but basically voltage in, voltage out, completely self-contained. These modules are fantastic. Um this one might be a little bit uh more expensive but uh yeah, just uh choose your flavor.

**Dave Jones:** And here's another one. It's the uh DPS 3003 and uh adjustable in 0.01 V steps 4 to uh 40 V. This one uses uh SMD uh parts. The other one was kind of uh through-holey. So, if you Oh, there we go. Compare those two. So, they're just available in all sorts of different uh versions. This one looks to be a little bit more high power, bigger inductor, bigger heat sink, bigger uh power transistors. This uses SMD ones but even this one is very nice. They claim an

**Dave Jones:** output power range of uh 96 W. Well, yeah, good luck 96 W out of this output power because I haven't measured the efficiency of this thing uh at all but if you like assume like it's really fantastic at like 90% over the range, for example, then if you're delivering let's say in the order of 100 W to your load, then this thing has to dissipate 10 W and well, that's just not going to happen on a heat sink of that size with no airflow. But you can see that this

**Dave Jones:** one here can uh do 0 to 3 A 0 to 32 V in 10 mV, 0 to 3 A in 1 mA steps and it's got 1 mA resolution. Whereas the one I just uh whacked in the uh case here is only uh 100 mV resolution um on the voltage and 10 mV resolution on the current, which is okay. And here's a look inside and well, it's a bit how you doing. Some of those joints it looks pretty crusty but hey, what do you want for the money? You

**Dave Jones:** know, it May like it's going to kind of sort of do the job. Meh. And bingo. Just in a minute, I changed my supply over to the DPS3003 supply. Is that the designer? And nope, it's I don't know what that symbol is. Anyway, that's the model number and we've got a much larger, colorful display here. Very, very nice.

**Dave Jones:** Now, I'm going to admit that the user interface on these is pretty terrible, but you know, you kind of get used to it. Voltage set here, we've actually got to push the knob. It's pushable like this. Well, actually let's just say we can go up like that. We've got ourselves a five There we go.

**Dave Jones:** Boom. And up. How do we get out of there? There we go. And we can actually go down like this and we can set our output uh current limit, of course. And uh you can set LED is just your LED brightness and there's some presets if you want to do it that way. But it certainly is not the most user-friendly thing. But anyway, we'll switch that on.

**Dave Jones:** There we go. 5.993 amps. 0.999 on electronic BK Precision electronic load here, which is 0.005% class. So, you know, there's a little bit of error there on the measured current. So, but it's not too far off at all. So, that's not too shabby. Mhm. I like that. By the way, the output voltage is going to drop because of the leads there. I haven't got any remote sensing or anything like that. So, don't worry about that. But that is That is very nice. Now, this DPS3003 module is a little bit more expensive

**Dave Jones:** than this one here, which we had before, but not much. This was like $18 on eBay delivered. This one's like $23, $24 delivered. So, like there's nothing much in it. I kind of like this one a bit better, but of course this doesn't operate if you want to use it say for a 5 volt plug pack or something like that, this one won't be suitable. You've got to get the other module which goes down to our 5 volts. This is only 6 volt minimum input voltage. And anyway, this

**Dave Jones:** module only claims 0.5% plus one digit, which is hey, more than enough for a just a a cheap bench supply like this. No worries at all. And there we are, we are able to draw up to the maximum 3 amps and I'm drawing 3 amps from my constant current load there, 3.00 2.999 and we're getting 2.988.

**Dave Jones:** Reading's a little bit out, but hey, that's doing that. So, we'll actually get the thermal camera on the back of that and have a look. Well, I'll tell you what, I don't even need the thermal camera. We're delivering 15 watts here and I can stick my fingers on the back of that heat sink there and no problems whatsoever. It's barely even warm. So, this sucker at that at 12 volt input voltage with 15 watts output like that is a pretty darn efficient. I'm happy with that.

**Dave Jones:** Nice. Okay, I've had this running for a while at 10.91 volts output at 3 amps and it's starting to get fairly warm, but I can still keep my fingers on that. So, it's not up to 50. It's probably at you know, the high 30s, maybe the low 40s there. But this is kind of the level at the sort of you know, the 33 watt level. Especially if you put this in a sealed case, you'd be looking at maybe having a little fan in there just to actually add some vent

**Dave Jones:** holes to you know, get some air flow over the heat sink fins in there and things like that. But you know, that's a fair amount. You know, when you're powering projects, you're generally not going to do that from like just a simple plug pack type um input like this. But anyway, the purpose of of today's video is just to show you these little modules, not to actually characterize them and and do everything else cuz I'd need a different plug pack if I wanted to fully characterize this

**Dave Jones:** module which is 96 watts. Anyway, I do like the secondary output display up here. It still shows the output when you're in the set menu. That's kind of cool. The knob does absolutely nothing when you're in the when you're in the main display mode like this which is good. Can't accidentally bump the output. And I also like that it shows the voltage input here coming from the plug pack. That's really handy. I probably prefer this module over the other one we originally saw with the multi line display. It's

**Dave Jones:** just like it's like bigger, color coded. It's just kind of nicer. I'd I'd go for this one. Anyway, if we have a closer look inside the DPS 3003 here, bottom is a display board in here. The top is obviously your main switching converter for your main switching is under here. We've got ourselves the big current shunt there. That's kind of neat. Which device does it use?

**Dave Jones:** I'd like to reverse engineer the circuit on these. And the main converter chip in here is an XL 7005. Never heard of it. It comes from a company called XL semi. I'll link in the data sheet down below, but that's only rated for 1.25 volt minimum output as most converters are. That's soldering a bit how you doing, isn't it?

**Dave Jones:** Um yeah. Yeah, Frosty the Snowman. So yeah, I'm not sure how they're getting the 1.0 the 0 volt output from that. But there you go. We've got a few miscellaneous other devices down there. And like I said, I'd like to reverse engineer. If anyone knows where you can get a schematic for any of these, then I'd love to know. Please, leave it in the comments. Otherwise, yeah.

**Dave Jones:** Requires a little bit of RE. And if you think these modules are a little bit wimpy, and you want something better, well, you can try one of these bad boys. Here we go. Where are we? Digital buck boost power supply. 6 to 40 volts input, 32 volts output, 0 to 5 amps, 160 watts maximum allowable input current 10 amps.

**Dave Jones:** Blah, blah, blah. Make sure higher than 18 volts. Blah. Okay. So, they've got some Once again, 0.5% 1 milliamp output. Um, quite nice. So, they've got the But, these are separate. So, you actually get the module separate on here, and this one is Oh, there you go. It's the same sort of interface, but except it's on a cable, which then you hook up. You get the cable with it, by the way. And this one's about four just over 40 US bucks.

**Dave Jones:** Um, and this one's got the little mini fan on the back. So, that's quite nice. You can actually mount that easily in a little case like I've got here. You could Yeah, that That would fit in there. That would fit in there a treat. Look at that. So, I can fit that in the little case I've got. So, that looks really quite neat and jazzy, doesn't it?

**Dave Jones:** There's our output current shunt. We've got a couple of big in there. Not sure what those ones Who are those caps from? Do we want to know? Anyway, nice little secondary board there. You got your micro powering the whole damn thing, but that is really quite nice. And it looks like there's four terminals on the inputs, four terminals on the output, and the little mini fan is probably as loud as buggery, but you know, what not.

**Dave Jones:** But, just these modules, the fact that you can get these in any flavor is just fantastic. I've got another one. Hang on. You really want a bad boy, 0 to 32 volt output, 0 to 12 amps, DPS3012. I might have to do a separate video actually building one. Once again, you get that and you get the board in there.

**Dave Jones:** Oh, look, dual current shunts down in there for that one. Forgive me for taking it out, but like like little piss ant fan on there for like Give me a break. 32 V 12 amp output capability with that kind of heat sinking. That's a joke, right? But anyway, for the price, you're not going to complain. These things are just cute.

**Dave Jones:** Anyway, this one's rather interesting. Got ourselves an ST Micro there running the show. There's our converter, is it? TI job, TL594, classic. Um going have a look around at some of the other stuff if you're the least bit interested.

**Dave Jones:** There you go. Got a couple of They were a couple of MOSFETs, were they? Hm. Anyway, this looks like a rather neat module. Who's the brand on that? I'm not entirely sure. One hung low are they? Oh, are they Rohm power transistors? Is that the R?

**Dave Jones:** Ah, there you go. Two of them. Are they doing a parallel jobby there, are they? Anyway, that would make a very interesting project. Maybe like you can always take those transistors off, mount them externally on a much larger heat sink, and actually turn that into a really neat project cuz you know, like 12 V like I don't really believe the specs on these things, but yet to be proven. But you know, to have a 0 to 32 V 12 amp supply, um basically all done for you with the

**Dave Jones:** user interface and all the power supply control stuff, um that you know, for the price is just absolutely amazing. Just whack it into a case and have a suitable power supply like a PC, modified PC power supply hooked up to it for example, that would do the business.

**Dave Jones:** So, that might make an interesting project. I might give you know, work on putting it you know, you put in a nice case and everything do it properly and everything else. But yeah, I just like the concept of these modules that you can get them in any shape or form for you know, hardly any cost and they might be a bit buggy or whatnot and the performance probably isn't going to be great and they're probably not going to live up to their specs or whatever. But

**Dave Jones:** the fact that they're so cheap and can make you know, like a half-decent power supply. Hmm. Anyway, let's whack a scope up to this and see what's what. All right, let's power this thing up. I've got a 10-V I set a 10-V output with a 3-A load on our constant current load here and let's switch the digital output on and we'll capture that. And that is as clean as a whistle. What's that 500 milliseconds per division 100-mV switch on? That's just fine and dandy.

**Dave Jones:** There's no overshoot whatsoever. It has overcurrent and overvoltage setpoint protection as well. That's just a soft software thing. They're not doing that in hardware, but that's good. You can you know, if you don't want to damage something set it to you know, 5.5 V or something you got a critical board 5.5 V and it shouldn't go over, but it's a software thing. So, I wouldn't rely on that and not as good as a hardware one.

**Dave Jones:** And something you don't see that often is a output power protection as well. I don't know. Some people might need that. Okay, I've got the constant current set to 2-A here, but I've got a 3-A load. So, let's just switch that on and see what happens. It should yeah, 2-A. There you go.

**Dave Jones:** We've only got 0.12 V out, but uh we are getting our constant current 2 amps. It's limited that. All right, so that's going to be our bloody load here. Let's just uh set it and we'll just short the output with the leads. That's better.

**Dave Jones:** These loads can be annoying sometimes. All right, so we just set uh 10 volts 2 amp output and we'll just short this puppy and see what we get. Hey, that's a nice nice clean response. Look at that. No worries. And let's see what response we get if we uh take it out of short and it goes back to 10 volts.

**Dave Jones:** That's pretty clean, too. Don't mind that at all. And by the way, these are all uh step-down converters. They're not uh buck and boost. So, it's not like you're feeding 5 volts in and then get um the other outputs. That's why this one only goes to a maximum of 11. 26 volts cuz we're only feeding in uh 12 volts. So, if you want higher than that, then you have to go up. This is rated from 0 to 40 volts input. So, if you want the 32 volts out, you've got to

**Dave Jones:** have at least 32 volts plus the dropout voltage cuz they're only a buck type device. Anyway, in constant uh current mode, I've had the output uh on that whoop. I've had the output uh shorted at uh 2 amps on this thing for quite some time now and that's not even warm. Uh not at all. So, neat. And for those who want to see the uh switching noise, 65 kHz there. Uh this is at uh 3 amps at uh 10-volt output and well, it is what it is, you know. Like it just

**Dave Jones:** for a rough as guts uh power supply, that's just fine. You could probably add some extra filtering on the output if you really wanted to, but you know, meh, that'll do for a lot of projects. Let's just repeat that power on test with a 22 ohm load here so we don't have the active electronic load in place and we'll switch it on and clean as a whistle. We'll just set the negative trigger there and we'll switch it off and bingo, that's uh a nice clean switch

**Dave Jones:** off in 50 milliseconds or so with that load, of course. It'll take longer if you totally disconnect the load, of course. And that was a bit warmy. And uh then single shot switch it off, of course the output capacitance will take forever.

**Dave Jones:** So, that takes about 400 and something milliamps. So, if we set it to 300 milliamp current limit, and I've got 10-volt output, and we and I'll just uh give that a little whoop switch on. There we go. That's actually the uh response of the constant current mode. So, it it undershoots there in terms of the voltage, but that's okay.

**Dave Jones:** Um no harm done there, but it recovers, you know, 50 milliseconds or so. So, that's quite nice. And then, if I set it to the positive edge and lift her up, there we go. That's the response going from constant current mode um with the voltage limit there up to the 10 volts, and there's very little overshoot there. That's very nice. No problems. Of course, we haven't checked this over its full operational range, but that's a pretty good indication it's going to work like that over the full

**Dave Jones:** range, though. So, there you have it. These these nifty little modules from company unknown available from all and sundry on AliExpress and eBay and uh Banggood, wherever you want to get these things from. Um and they cost practically nothing. Like 17 Like no, sorry, this module's about 20 uh 3 $24 delivered or whatever. And you just have to whack in a plug pack of a suitably high voltage. Depends on what output voltage you're looking at for this thing. And the performance is probably going to be half

**Dave Jones:** reasonable. The UI's half reasonable, and I jeez, it's worth like probably building one of these. They've found a real nice niche with these uh modules, I think. I don't think there's anyone else actually doing these. Whether or not it's one company making them or others have ripped them off and there's clones of whatever, I have no idea.

**Dave Jones:** But yeah, they've got a pretty nice little niche with these modules. I don't rather like them. And more experimentation required. I'd like to fully characterize them, but that's a lot of effort to fully characterize them over the input voltage range.

**Dave Jones:** All right, various simple voltage ranges for all the different output voltages, for all the different output currents and get all the characteristic curves and uh, makes my head spin just thinking about it. And but they're probably going to give reasonable performance. So, it's worth for the money. It absolutely cannot be beat. Just build it using junk bin, you know, parts, a couple of binding posts and an old plug pack you've got lying around. Winner winner, chicken dinner. Anyway, I hope you like that. If you did, please give a big

**Dave Jones:** thumbs up. And if you want me to do more videos on these modules, either, you know, taking one of these big beefy ones and actually, you know, making up a big beefy, like, you know, 10 or 12 amp power supply or something like that, let me know in the comments down below. And as always, discuss over on the EEVblog forum.

**Dave Jones:** Catch you next time.
