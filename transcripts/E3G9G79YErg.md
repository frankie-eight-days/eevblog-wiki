---
video_id: E3G9G79YErg
title: EEVblog 1718 - Cheap 1GHz Oscilloscopes are Useless? ($5 DIY 1GHz Resistive Probe)
url: https://www.youtube.com/watch?v=E3G9G79YErg
source: youtube-asr
timestamps: {"0": 0, "1": 19, "2": 37, "3": 51, "4": 70, "5": 85, "6": 100, "7": 114, "8": 131, "9": 148, "10": 161, "11": 178, "12": 194, "13": 211, "14": 228, "15": 243, "16": 260, "17": 280, "18": 295, "19": 309, "20": 323, "21": 338, "22": 353, "23": 370, "24": 386, "25": 401, "26": 416, "27": 428, "28": 444, "29": 458, "30": 473, "31": 492, "32": 507, "33": 524, "34": 543, "35": 562, "36": 577, "37": 591, "38": 603, "39": 615, "40": 631, "41": 644, "42": 655, "43": 667, "44": 682, "45": 692, "46": 706, "47": 721, "48": 732, "49": 743, "50": 755, "51": 767, "52": 782, "53": 795, "54": 810, "55": 827, "56": 843, "57": 856, "58": 871, "59": 882, "60": 896, "61": 908, "62": 922, "63": 933, "64": 949, "65": 964, "66": 981, "67": 994, "68": 1006, "69": 1019, "70": 1035, "71": 1051, "72": 1065, "73": 1079, "74": 1095, "75": 1107, "76": 1122, "77": 1138, "78": 1153, "79": 1173, "80": 1188, "81": 1206, "82": 1220, "83": 1235, "84": 1249, "85": 1263, "86": 1278, "87": 1291, "88": 1307, "89": 1326, "90": 1339, "91": 1353, "92": 1367, "93": 1385, "94": 1403, "95": 1418, "96": 1433, "97": 1445, "98": 1457, "99": 1474, "100": 1483, "101": 1495, "102": 1509, "103": 1526, "104": 1538, "105": 1554, "106": 1566, "107": 1582, "108": 1598}
---

**Dave Jones:** Hi. In my latest video about this new Rigol MSO 980 series oscilloscope, in particular this model which goes up to 1 GHz, but the 984, for example, goes up to 800 MHz, and you can software expand the base 350 MHz model right up to 800

**Dave Jones:** MHz. It's just a software option. And thank you to one of my viewers, YAQ1988, for putting up this comment, which is rather interesting. Saying, basically, what use is greater than a 350 MHz scope, which is what the base model

**Dave Jones:** version of this introduces for like under $1,000 now. You can get a 350 MHz scope. The question is, well, what's the point of having anything higher frequency than that, like the 500 MHz model, the 800, or even the 1 GHz like

**Dave Jones:** this HDO98 here? What's the point of that if the inputs here, they don't even have the times 10 ringing around here to identify a times 10 probe, let alone an active probe interface to power a high frequency active probe? So, what is the

**Dave Jones:** like point of like having a higher frequency scope like this if you can't plug any high frequency probes into it? Well, that's a good question. The answer is, you actually can. And you can do it for like a couple of bucks. Now, I've

**Dave Jones:** actually done a video on this before, video number 1367, and that was actually a two-part video, but it was actually the pertinent information here was actually buried away within that video. So, I thought I'd extract that information out, and

**Dave Jones:** I'll include it at the end of this, but I'll just go over a brief summary. Now, this is the probe that comes with this new Rigol oscilloscope. It's a typical times 10 passive probe here, and it's a pretty high decently high frequency

**Dave Jones:** jobby here. It's the RP3500A. It's a 10 meg input impedance 500 megahertz bandwidth probe. And generally speaking, this is, you know, like really high end for a passive probe. They do actually go higher though. So, technically, you could buy the 500

**Dave Jones:** megahertz model, you've got a matching 500 megahertz bandwidth probe here. What's the problem? Well, there's a big problem. It's this number right here, 13 picofarads or 13 puff input capacitance. And as he mentioned in the comment, well, what about high frequencies? That

**Dave Jones:** capacitance is going to matter. Yes, it is. You should be familiar with this formula, it's the capacitive reactance XC, and it's 1 over 2 * pi * the frequency you're talking about * the capacitance. And this is frequency is in

**Dave Jones:** hertz, capacitance is in farad. And if you take this 13 picofarads here, you plug it into the formula at 500 megahertz, you get an capacitive reactance or an impedance or AC resistance or AC impedance of or basically a resistance and input

**Dave Jones:** resistance of your probe at the tip, right at the tip here, it's not 10 megaohms anymore, it's 24.5 ohms. You've got to remember, this 10 meg only applies for DC. Anything over that, you have to apply the capacitive

**Dave Jones:** reactance formula due to the input tip capacitance of your probe here. So, you might have your fancy pantsy 500 megahertz oscilloscope and your fancy pantsy 500 megahertz passive probe here matching, but if you try to measure a 500 megahertz signal or 500 megahertz

**Dave Jones:** component of the signal at that frequency, you're really loading down your circuit under test. Like 25 ohms, that's that is ridiculously low loading there. That could definitely change your measurement, it could load down the line, it could cause your product to stop working or

**Dave Jones:** whatever. It's a really low value. It You don't get the 10 megaohms anymore. You don't get a free lunch with any probes. And you can get even higher bandwidth passive probes like this. This Rohde & Schwarz jobby here, it's a There

**Dave Jones:** you go. It's a 10 megaohm, but it's 9.5 pF, and this is 700 MHz. So, not too shabby, but they're a little bit pricey. And here's one of the ducks guts of the passive probe world, the Tektronix TPP1000. It's a 1 gig passive probe,

**Dave Jones:** standard times 10 passive probe. It's got 3.9 pF and 10 megaohms DC input impedance. So, this is really schmick. But, couple of downsides is it's not cheap, and B, it's like the customized tech interface. So, even though it's not active, it still

**Dave Jones:** physically can't plug into a normal scope, which is really annoying, but anyway, there's others on the market. But, doesn't matter how good these standard passive probes get, uh you're still bothered by that pesky input capacitance. This case, like 9.5 pF,

**Dave Jones:** almost 10 pF there. That's going to be a really low impedance. Run the numbers yourself. The general solution to this problem is, of course, the these fancy pantsy active probes here, and I've done videos on this. And this is a Keysight

**Dave Jones:** jobby, old school analog branding though. And once again, it's a 10 to 1 probe. It's input impedance though is 1 megaohm at DC, not 10 megaohms anymore, but that's neither here nor there. It's still massively high. It's a 2 GHz

**Dave Jones:** bandwidth probe, but it's only got an input tip capacitance of 1 pF, 1 pF there. So, if you whack that into the equation here, at 1 GHz, 1 pF is 159 ohms. So, that's still low, but it's not

**Dave Jones:** going to load down your circuit. That's way higher than the 13 pF passive probe up here. You've only got 1 pF now. It's 1/13 of the capacitance, but yeah, 159 ohms is still, you know, it's still high-ish, but it's probably not going to

**Dave Jones:** load down a you know, a decently low impedance driving circuit that you typically measure with these things. But the problem with these active probes is usually they require a custom interface matched to the manufacturer's oscilloscopes. And if your oscilloscope

**Dave Jones:** doesn't support those, then wah, wah, wah, you can't use an active probe. Or can you? Here's an active FET probe, and active probe means that it actually has a an an active amplifier circuit right in the tip there. So, you're minimizing

**Dave Jones:** your input capacitance, go straight to the amplifier. This one actually plugs into a regular oscilloscope. This particular one's actually discontinued, you can't buy it anymore, but there are other brands on the market that will plug into a standard oscilloscope 50 ohm

**Dave Jones:** input. So, you could use it with this new Rigol scope, for example. And this one here is 1.2 gig bandwidth, more than enough to match the scope at 10:1 and 1 megohm 3 pF input capacitance. Not bad. And sure

**Dave Jones:** enough, Rigol do not actually sell an active probe to go with this oscilloscope. They do sell active probes, but they are designed to use the custom interfaces you get on the higher end at Rigol scopes. So, you can't use

**Dave Jones:** them on this, but aha, all is not lost. You can actually get a Rigol 1.5 gig passive probe called the RP 61 50, and it's 279 Yankee bucks. You know, it's not that expensive, so you can actually get

**Dave Jones:** matching passive probes for your scope. And it uses a standard BNC 50 ohm input, which this scope is capable of. You don't need the active probe interface, you don't need any external power for this. This is a passive probe. And you

**Dave Jones:** can see that that probe has an input impedance of 500 ohms. So, at like across the entire frequency range, it doesn't really specify an input capacitance. It just says 500 ohms plus minus 10% across that 1.5 in gig

**Dave Jones:** bandwidth. So, that's pretty decent. How do they do it? Aha, that's the point of this video. And that brings me back to my previous video number 1367. You can actually build your own do-it-yourself passive resistor probe or a Z0 probe or they they go under various

**Dave Jones:** names. But, you know, a resistive probe like this, it's simply a BNC with some coax and in this particular case a 1K resistor, just a standard resistor, nothing fancy about it, right at the tip there. So, the relatively high input

**Dave Jones:** capacitance of this cable is isolated by the 1K resistor here. So, you get extremely low capacitance on the input. And you can build this thing yourself for a couple of bucks and they perform just as good as that $279 Rigol probe or

**Dave Jones:** even more expensive fully characterized resistive probe. So, what I'm going to do now is insert the video extracted from number 1367 explaining and demonstrating using one of these resistive probes here and how it compares with an active probe. A

**Dave Jones:** resistive probe, a Z0 or Z0 probe. And basically what it is is is a bit of coax home with a terminated standard BNC. And in the end here, it's just got it's simply a 1K series resistor. And the braid just goes off

**Dave Jones:** here to your ground tip. And that's it. A 1K series resistor in a coax. How can this perform as good as like a multi-thousand-dollar probe even? Well, there's a bit of art and science to it. And they can basically uh match the at

**Dave Jones:** least signal integrity uh performance of like a multi-thousand or even ten-thousand dollar ten gigahertz uh probe if you do these right. But, yeah, there's a lot of art and science in getting it right. And this one here I

**Dave Jones:** just uh crudely made up. I haven't measured uh its performance. Once again, if you actually want to characterize the performance of it um and know it's going to be good, then well, you need all the gear and the experience to do that. But,

**Dave Jones:** I have no doubt that even this simple one I just lashed together is probably uh as good in terms of uh signal fidelity as you know, this 500 meg um Agilent not that Keysight rubbish uh probe here. Okay, Dave, what's the

**Dave Jones:** catch? If anyone can just start lash a probe like this together practically zero cost, then why bother with like expensive high bandwidth uh probes like these ones? Well, the first thing is is of course that gorgeous input impedance. That ten megohms um at

**Dave Jones:** DC by the way, we'll get into that uh input impedance. And well, you know, it doesn't load down your circuit much at DC. But, unfortunately, this puppy with a 1K resistor in series, these of course have to be terminated cuz this is a

**Dave Jones:** transmission line and if you don't terminate the other end, you're going to get reflections galore and it's just well, it's not going to work as a probe. So, you have to have a 50 amp termination on your oscilloscope either

**Dave Jones:** internal uh to the scope or just an inline one that you actually plug in. And if you run the numbers, put that into Keysight Infiniium then with a 1K in series with a 50 ohm uh termination at the other end, you're talking about a

**Dave Jones:** 21 uh to one ratio as opposed to a ten to one probe. This is a 21 to one or one to 21. So, it divides your signal by 21 times and you've got a 1K uh DC impedance. So, that loads your line down

**Dave Jones:** substantially. And of course, you don't need a 1K uh resistor in here in series. You can basically make it any uh value you want. Make it larger or smaller and you can have it um of course, if you're

**Dave Jones:** putting in a 450 ohm resistor, then you'd have the same uh 10 to 1 probe as you would here. But, the difference is um instead of having a 10 meg input impedance here, this one would have a 500 ohm input impedance. And that's

**Dave Jones:** going to load down uh your lines at DC. But, the interesting thing is that uh this is 11 puff, 11 pica farad here. And at frequency, that is going to load down quite substantially. So, now we actually have to talk about uh probe loading.

**Dave Jones:** Whereas, this is not going to have much capacitance at all. So, hence why in theory, you know, if you use the right coax and everything else, you can get, you know, 10 gig bandwidth or something, many gigahertz bandwidth out of these

**Dave Jones:** sorts of probes. If you construct them right and terminate them right and all the rest. And this probe with a 1K resistor in series, that's kind of like a typical value everyone uses. It's not too high, it's not too low, it's just

**Dave Jones:** right. It's like the Goldilocks uh value. And this probe is only going to have like, you know, one or two puff. Although, I haven't measured this one, probably going to be better than this real expensive $800 probe here. So,

**Dave Jones:** there has to be another downside to this, and yeah, there could be. if you choose like the 1K value in here, you've got that oddball 21 to 1 uh divider ratio instead of your more standard 10 to 1. So, even a real like, you know,

**Dave Jones:** highish end expensive uh scope like this Tektronix MDO 3000 1 gig bandwidth up here, um check out the probe attenuation. There, it's 1, 2, 5, 10. Oh, we can get 20, we can get close, but we can't get that 21. So, if you use

**Dave Jones:** that oddball value, then well, you either have to just set it to one times one and then just do the calculations manually, or you can uh choose the resistor value to match. So, you can get an E96 value resistor like just over 950

**Dave Jones:** ohms, that'll give you a reasonable like uh 20 uh to one ratio. But, one other advantage of these is that uh they're actually slightly more tolerant of uh longer ground leads than uh a FET probe. So, that's a benefit. So, you know,

**Dave Jones:** these things, if done right, are really very, very good. Okay, let's give you a probing example here. We've got a Raspberry Pi 3, for those playing along at home, and we're going to probe one of the memory pins on the bottom here. I

**Dave Jones:** don't care which one. I've just picked one at random. We're getting a signal on it. So, I'm using the 2 GHz active probe here, the N12796, overkill for what we're doing. Well, overkill for this scope, anyway, because this is a 500 MHz bandwidth scope. So,

**Dave Jones:** this active FET probe more than good enough for measuring the bandwidth that we've got here. So, I'll use this long lead here for my ground. I'll put it on the ground pin of the connector there, cuz that's just very

**Dave Jones:** convenient. For those who care about such things, you can actually see what point I'm probing. Where is it? I think it's there. Geez, I can barely see that. This is where, you know, magnification uh comes in. Okay, I'm probing a point there. I don't

**Dave Jones:** know what it is. I don't care. There it is. There's our signal. It's made up of a whole bunch of stuff, but basically, you can see, look, it's got some undershoot here. It's got a little bit of ringing there. It's got a little bit

**Dave Jones:** of ringing there. I'm going to hazard a guess that that's going to be due to our long ground lead there, right? Okay, so, we'll just try and capture that sort of like the most frequent one there. There it is. Got it. Okay, so, I'll store

**Dave Jones:** that. Right, so, what I'm going to do now is I'm going to actually change the ground into this. Instead of having this longer lead, I'm going to go for one of the shorter little adapter ground adapter pins we've got in there. It

**Dave Jones:** looks like there's a little bypass cap. I've determined that this right-hand side is the ground. So, that's very convenient, because that's right next to the point that I want to test. Otherwise, as I showed before, like that have to

**Dave Jones:** like install one of those copper pads or something. You might have to like scrape away some of the ground here or something like that and maybe put the copper tape over the top of the chip or something like that or you'd have to

**Dave Jones:** scrape away some other ground point somewhere or you know, soldering a little contact loop pin or something like that. So, here it is. I got my little adapter. Careful cuz you can stab yourself with these little bastards. There we go. So, we have this little now

**Dave Jones:** ground pin which can sort of like you know, pivot around like that and anyway, that will make better contact and this will be a higher frequency probe because it's a shorter inductive path. So, let's try that. We'll require the turn at the

**Dave Jones:** right angle and probably some magnification here. Okay, I've got my ground point and I've got my probe point. Pan up, pan up. Okay, let's have a look. I've changed my digitizer. Definitely getting 5 gig samples up second and I saved my reference

**Dave Jones:** waveform. So, let's single shot capture that. See if we can get it. No. There we go. Got it. Now, I can actually adjust that waveform there to show you. There you go. So, the orange one I've got there is the reference waveform and this

**Dave Jones:** new yellow one is the one that we just probed and there you go. It is like it's of course like the same wave shape. You can see it's got the longer ground lead one, the orange one has some extra

**Dave Jones:** undershoot there and comes back and takes more time to come back up like that and the one up here got some extra wiggle wiggle wiggle yeah on the top there, some overshoot. So, you know, there are differences in probing right

**Dave Jones:** there. But, at the moment this is the loading of the line with a one picofarad one puff active probe which costs a couple of thousand dollars. Okay, now I'm going to use my 500 megahertz passive probe here. It's the N28 43.

**Dave Jones:** It's 11 picofarads. okay? And yes, I've compensated this. You compensate it with your probe compensation on the front. So, everything's hunky-dory. I'm using my low inductance high frequency ground probe attachment, so that's equivalent to what we had before. So, we should get

**Dave Jones:** because we've only got a 500 bandwidth scope here, then the bandwidth of the probe isn't really going to matter that much. Hold my tongue at the right angle. And probe this. I think I got it. But here's the interesting thing. I've

**Dave Jones:** changed the reference waveform to my low inductance short ground one before, so the orange one is the best we could get with our active probe. So, the exact same ground point, basically the same ground length, and you can see that

**Dave Jones:** well, you know, our wave shape is the same, but look. Look at this. It's a much higher level down here. Okay, this is 200 mV per division, so it's like, you know, 50 odd mV higher there, and it's actually lower down

**Dave Jones:** here, our yellow waveform there. So, you know, all although we can see like the wave shape and everything up here, it's like when the bus is loaded differently cuz that's what this little you know, ramp up here is going here. I

**Dave Jones:** don't know the architecture of the Raspberry Pi. It it doesn't matter, but I know there's something happening there with there, and down here we're actually seeing a larger drop across the bus here, which is interesting, isn't it? I

**Dave Jones:** it you know, there's significant differences here. This is wasn't example I wanted to show. I just like it's a random example, but you can see the difference here between a 500 meg passive probe and and effectively a because of the bandwidth of the

**Dave Jones:** oscilloscope of 500 meg active probe. They load down the circuit differently. And I know you want to see it. Okay, let's compare Dave's dodgy homemade resistive probe here with a 1k resistor in the tip. We'll give that a burl. Got

**Dave Jones:** a 50 ohm terminate that. But scope can do that, no worries. Tongue at the right angle, tongue at the right angle. Fix that. Woah! Check this out. This is absolutely fan-freaking-tastic. Now, what we've got here, the orange waveform of course is our reference

**Dave Jones:** active FET waveform. That's a $2,500 active FET probe. Yes, it is compensated because you do still compensate them and it stores it internally because it knows the serial number of the probe, etc. And the yellow one is Dave's do-it-yourself

**Dave Jones:** couple of buck resistive probe. Look at this. What's going on here? Well, it's obvious that what's happening at this point right here is that the bus is actually going open or something. I don't know the exact architecture of what's you

**Dave Jones:** know, the pin I'm actually probing. It doesn't matter, right? It's like it's going open. And because the probe is 1 meg DC resistance, look at that. It's basically it's not going to discharge. Maybe if we got like a longer time period it'd

**Dave Jones:** eventually do a similar like eventually discharge or whatever. But you see that the bus is actively changed. But because we're now loading this bus down with a 1K resistor or a 1.05K resistor cuz we've got the 50 ohm terminator as well.

**Dave Jones:** It boom! This isn't This looks like for all the world and it is an RC discharge curve. So there you go. What's that? You know, 10 nanoseconds per division. I don't You can work that out, whatever. For those playing along at home. But you

**Dave Jones:** can see how the resistive probe actually completely changes the circuit that you're actually measuring. So sure, like the signal integrity is excellent. Let's let's take a look at this actually. If you have a look at the bottom here, you

**Dave Jones:** can see that both of them undershoot almost exactly the same. But you remember how I said that the resistive probe can actually be more tolerant of longer ground leads. I think they're both about the same length. I think

**Dave Jones:** they're practically near identical. Remember how I said it can be more tolerant on these than active FET probes. This might be an example of this cuz this is not This is not some controlled experiment. This is just something I slapped

**Dave Jones:** together willy-nilly and this is the result that we actually got. This is fascinating, right? They both undershoot exactly the same, but the active FET probe, the orange one, actually look it overshoots again when So and it takes much longer to recover

**Dave Jones:** than the resistive probe. Look at that. So this could be an example of where this cheap ass do-it-yourself resistive probe is actually outperforming this $2,500 active FET probe in terms of signal integrity. But once again, this is not a completely controlled

**Dave Jones:** experiment. But this is what you can actually get. But of course the limitation is that it loads it down much more. 1K as opposed to 1 meg, right? There's a huge difference there. And you might know oh what's the difference

**Dave Jones:** between this load you know look it's it's dropping with the 1K. Is that the effect of the 1K load over here? Well, it's actually not. If we actually measure that cuz you remember it's a divide by 21 probe as opposed to the

**Dave Jones:** active FET probe which is divide by 10. So if we actually set up our cursors here and go I've set them precisely to the same ground point here. Our resistive probe is we're getting 55 millivolts there. So if you get your

**Dave Jones:** confuser out, 55 millivolts times 21 which is our probe, 1.155 volts. And this is a looks like it's a 1.2 volt bus. So it's like it could be like it's maybe 50 millivolts under, but we have to measure the other one

**Dave Jones:** actually. So, if we adjust that, we're talking about 60 millivolts there. So, it's actually precisely six divisions there, and we were on 200 millivolts per division. So, that's precisely 1.2 volts. So, the resistive probe is actually measuring 50 millivolts less,

**Dave Jones:** and that could be the load the extra loading of the 1K load. Once you you'd have to check out the driving strength of the driver actually used in this, which is the whatever micro is used on the Raspberry Pi or whatever. But,

**Dave Jones:** because as I said, we can't actually put in a actual ratio, it doesn't let us put in our own user-defined value. It only does you know, these fixed ones. But, if it did do that, then we could actually get

**Dave Jones:** you know, well we've measured it. We we can see that it's basically 50 millivolts under. So, that could be like an extra 50 millivolts drop caused by the loading of the probe. That's what it seems to be the case. But, once again,

**Dave Jones:** this isn't exactly a really proper setup controlled experiment. But, that's possible, and it's kind of like you know, the sort of value that I'd expect. But, you can definitely see the loading there. And by the way, no, this is not

**Dave Jones:** just a like a freak capture where you know, the bus did something different than before. This happens every single time. No matter how many times I capture this, the 1K probe is definitely totally different to the active FET probe here. And you can see

**Dave Jones:** obviously the bus was floating there, and then it went boom, no. I'm going to go actively low.

**Dave Jones:** And of course, the choice of resistor value is always going to be a trade-off. Like if you go higher and higher in resistors, then your divider ratio gets higher and higher and higher, and you can't measure low-level signals, and

**Dave Jones:** it's not that great. But, the higher value in resistor you go, the more you can isolate the cable and system capacitance from the tip. So, technically, you know, the less you're loading your circuit, but it's all a big trade-off. So, there you

**Dave Jones:** go. I hope you found that useful. There's no shortage of either do-it-yourself or relatively cheap resistive probes or even, you know, active probes. Yeah, they're expensive, you know, many thousands of dollars. Although, there's do-it-yourself active probe designs as

**Dave Jones:** well. There's a lot of like open source ones as well, and they're just going to work just fine. So, certainly, don't worry about thinking that you're wasting your money buying a high bandwidth scope like this 1 GHz one or the 800 MHz model

**Dave Jones:** or the 500 MHz model or whatever. No, there's lots of probing solutions available for your scope, even though it has no fancy pantsy active input or even the times 10 input. Unfortunately, not all scopes have the ability to put in like a customized

**Dave Jones:** resistive probe value. You choose your resistor value based on your requirements, and it might be 10:1, it might be 20:1, it might be some oddball value or something like that. But, in this particular case, the Rigol, if we

**Dave Jones:** go into the probing interface here, we can choose all these standard ones, fantastic. But, in the case of my little custom one with a 1K probe here, this is actually a times 21 probe. So, I can actually choose the user thing here, and

**Dave Jones:** I can do 21 X like that. Okay. Bingo, I've got a times 21 probe calibrated for my little cheapy couple of dollar resistive probe here. Nice. So, if you found that video useful, please give it a big thumbs up. As always, discuss down

**Dave Jones:** below. Catch you next time.
