---
video_id: E3G9G79YErg
title: EEVblog 1718 - Cheap 1GHz Oscilloscopes are Useless? ($5 DIY 1GHz Resistive Probe)
url: https://www.youtube.com/watch?v=E3G9G79YErg
source: youtube-asr
timestamps: {"0": 0, "1": 19, "2": 39, "3": 52, "4": 67, "5": 77, "6": 95, "7": 105, "8": 120, "9": 135, "10": 146, "11": 159, "12": 186, "13": 197, "14": 216, "15": 228, "16": 237, "17": 250, "18": 265, "19": 286, "20": 297, "21": 311, "22": 321, "23": 335, "24": 342, "25": 359, "26": 373, "27": 387, "28": 401, "29": 413, "30": 427, "31": 439, "32": 450, "33": 460, "34": 473, "35": 492, "36": 505, "37": 526, "38": 541, "39": 560, "40": 569, "41": 585, "42": 601, "43": 613, "44": 624, "45": 637, "46": 651, "47": 671, "48": 682, "49": 697, "50": 709, "51": 721, "52": 732, "53": 739, "54": 749, "55": 756, "56": 774, "57": 790, "58": 808, "59": 823, "60": 835, "61": 847, "62": 860, "63": 871, "64": 880, "65": 892, "66": 906, "67": 918, "68": 939, "69": 959, "70": 973, "71": 983, "72": 996, "73": 1015, "74": 1027, "75": 1042, "76": 1057, "77": 1072, "78": 1084, "79": 1095, "80": 1106, "81": 1120, "82": 1140, "83": 1151, "84": 1163, "85": 1176, "86": 1190, "87": 1206, "88": 1223, "89": 1235, "90": 1244, "91": 1255, "92": 1266, "93": 1280, "94": 1290, "95": 1307, "96": 1321, "97": 1333, "98": 1341, "99": 1355, "100": 1366, "101": 1385, "102": 1398, "103": 1416, "104": 1428, "105": 1441, "106": 1453, "107": 1463, "108": 1476, "109": 1495, "110": 1508, "111": 1523, "112": 1538, "113": 1554, "114": 1570, "115": 1582, "116": 1596}
---

**Dave Jones:** Hi. In my latest video about this new Rigol MSO 980 series oscilloscope, in particular this model which goes up to 1 GHz, but the 984, for example, goes up to 800 MHz, and you can software expand the base 350 MHz model right up to 800 MHz.

**Dave Jones:** It's just a software option. And thank you to one of my viewers, YAQ1988, for putting up this comment, which is rather interesting. Saying, basically, what use is greater than a 350 MHz scope, which is what the base model version of this introduces for like under $1,000 now.

**Dave Jones:** You can get a 350 MHz scope. The question is, well, what's the point of having anything higher frequency than that, like the 500 MHz model, the 800, or even the 1 GHz like this HDO98 here?

**Dave Jones:** What's the point of that if the inputs here, they don't even have the times 10 ringing around here to identify a times 10 probe, let alone an active probe interface to power a high frequency active probe?

**Dave Jones:** So, what is the like point of like having a higher frequency scope like this if you can't plug any high frequency probes into it? Well, that's a good question.

**Dave Jones:** The answer is, you actually can. And you can do it for like a couple of bucks. Now, I've actually done a video on this before, video number 1367, and that was actually a two-part video, but it was actually the pertinent information here was actually buried away within that video.

**Dave Jones:** So, I thought I'd extract that information out, and I'll include it at the end of this, but I'll just go over a brief summary. Now, this is the probe that comes with this new Rigol oscilloscope.

**Dave Jones:** It's a typical times 10 passive probe here, and it's a pretty high decently high frequency jobby here. It's the RP3500A. It's a 10 meg input impedance 500 megahertz bandwidth probe.

**Dave Jones:** And generally speaking, this is, you know, like really high end for a passive probe. They do actually go higher though. So, technically, you could buy the 500 megahertz model, you've got a matching 500 megahertz bandwidth probe here.

**Dave Jones:** What's the problem? Well, there's a big problem. It's this number right here, 13 picofarads or 13 puff input capacitance. And as he mentioned in the comment, well, what about high frequencies?

**Dave Jones:** That capacitance is going to matter. Yes, it is. You should be familiar with this formula, it's the capacitive reactance XC, and it's 1 over 2 * pi * the frequency you're talking about * the capacitance.

**Dave Jones:** And this is frequency is in hertz, capacitance is in farad. And if you take this 13 picofarads here, you plug it into the formula at 500 megahertz, you get an capacitive reactance or an impedance or AC resistance or AC impedance of or basically a resistance and input resistance of your probe at the tip, right at the tip here, it's not 10 megaohms anymore, it's 24.5 ohms.

**Dave Jones:** You've got to remember, this 10 meg only applies for DC. Anything over that, you have to apply the capacitive reactance formula due to the input tip capacitance of your probe here.

**Dave Jones:** So, you might have your fancy pantsy 500 megahertz oscilloscope and your fancy pantsy 500 megahertz passive probe here matching, but if you try to measure a 500 megahertz signal or 500 megahertz component of the signal at that frequency, you're really loading down your circuit under test.

**Dave Jones:** Like 25 ohms, that's that is ridiculously low loading there. That could definitely change your measurement, it could load down the line, it could cause your product to stop working or whatever.

**Dave Jones:** It's a really low value. It You don't get the 10 megaohms anymore. You don't get a free lunch with any probes. And you can get even higher bandwidth passive probes like this.

**Dave Jones:** This Rohde & Schwarz jobby here, it's a There you go. It's a 10 megaohm, but it's 9.5 pF, and this is 700 MHz. So, not too shabby, but they're a little bit pricey.

**Dave Jones:** And here's one of the ducks guts of the passive probe world, the Tektronix TPP1000. It's a 1 gig passive probe, standard times 10 passive probe. It's got 3.9 pF and 10 megaohms DC input impedance.

**Dave Jones:** So, this is really schmick. But, couple of downsides is it's not cheap, and B, it's like the customized tech interface. So, even though it's not active, it still physically can't plug into a normal scope, which is really annoying, but anyway, there's others on the market.

**Dave Jones:** But, doesn't matter how good these standard passive probes get, uh you're still bothered by that pesky input capacitance. This case, like 9.5 pF, almost 10 pF there. That's going to be a really low impedance.

**Dave Jones:** Run the numbers yourself. The general solution to this problem is, of course, the these fancy pantsy active probes here, and I've done videos on this. And this is a Keysight jobby, old school analog branding though.

**Dave Jones:** And once again, it's a 10 to 1 probe. It's input impedance though is 1 megaohm at DC, not 10 megaohms anymore, but that's neither here nor there. It's still massively high.

**Dave Jones:** It's a 2 GHz bandwidth probe, but it's only got an input tip capacitance of 1 pF, 1 pF there. So, if you whack that into the equation here, at 1 GHz, 1 pF is 159 ohms.

**Dave Jones:** So, that's still low, but it's not going to load down your circuit. That's way higher than the 13 pF passive probe up here. You've only got 1 pF now.

**Dave Jones:** It's 1/13 of the capacitance, but yeah, 159 ohms is still, you know, it's still high-ish, but it's probably not going to load down a you know, a decently low impedance driving circuit that you typically measure with these things.

**Dave Jones:** But the problem with these active probes is usually they require a custom interface matched to the manufacturer's oscilloscopes. And if your oscilloscope doesn't support those, then wah, wah, wah, you can't use an active probe.

**Dave Jones:** Or can you? Here's an active FET probe, and active probe means that it actually has a an an active amplifier circuit right in the tip there. So, you're minimizing your input capacitance, go straight to the amplifier.

**Dave Jones:** This one actually plugs into a regular oscilloscope. This particular one's actually discontinued, you can't buy it anymore, but there are other brands on the market that will plug into a standard oscilloscope 50 ohm input.

**Dave Jones:** So, you could use it with this new Rigol scope, for example. And this one here is 1.2 gig bandwidth, more than enough to match the scope at 10:1 and 1 megohm 3 pF input capacitance.

**Dave Jones:** Not bad. And sure enough, Rigol do not actually sell an active probe to go with this oscilloscope. They do sell active probes, but they are designed to use the custom interfaces you get on the higher end at Rigol scopes.

**Dave Jones:** So, you can't use them on this, but aha, all is not lost. You can actually get a Rigol 1.5 gig passive probe called the RP 61 50, and it's 279 Yankee bucks.

**Dave Jones:** You know, it's not that expensive, so you can actually get matching passive probes for your scope. And it uses a standard BNC 50 ohm input, which this scope is capable of.

**Dave Jones:** You don't need the active probe interface, you don't need any external power for this. This is a passive probe. And you can see that that probe has an input impedance of 500 ohms.

**Dave Jones:** So, at like across the entire frequency range, it doesn't really specify an input capacitance. It just says 500 ohms plus minus 10% across that 1.5 in gig bandwidth. So, that's pretty decent.

**Dave Jones:** How do they do it? Aha, that's the point of this video. And that brings me back to my previous video number 1367. You can actually build your own do-it-yourself passive resistor probe or a Z0 probe or they they go under various names.

**Dave Jones:** But, you know, a resistive probe like this, it's simply a BNC with some coax and in this particular case a 1K resistor, just a standard resistor, nothing fancy about it, right at the tip there.

**Dave Jones:** So, the relatively high input capacitance of this cable is isolated by the 1K resistor here. So, you get extremely low capacitance on the input. And you can build this thing yourself for a couple of bucks and they perform just as good as that $279 Rigol probe or even more expensive fully characterized resistive probe.

**Dave Jones:** So, what I'm going to do now is insert the video extracted from number 1367 explaining and demonstrating using one of these resistive probes here and how it compares with an active probe.

**Dave Jones:** A resistive probe, a Z0 or Z0 probe. And basically what it is is is a bit of coax home with a terminated standard BNC. And in the end here, it's just got it's simply a 1K series resistor.

**Dave Jones:** And the braid just goes off here to your ground tip. And that's it. A 1K series resistor in a coax. How can this perform as good as like a multi-thousand-dollar probe even?

**Dave Jones:** Well, there's a bit of art and science to it. And they can basically uh match the at least signal integrity uh performance of like a multi-thousand or even ten-thousand dollar ten gigahertz uh probe if you do these right.

**Dave Jones:** But, yeah, there's a lot of art and science in getting it right. And this one here I just uh crudely made up. I haven't measured uh its performance. Once again, if you actually want to characterize the performance of it um and know it's going to be good, then well, you need all the gear and the experience to do that.

**Dave Jones:** But, I have no doubt that even this simple one I just lashed together is probably uh as good in terms of uh signal fidelity as you know, this 500 meg um Agilent not that Keysight rubbish uh probe here.

**Dave Jones:** Okay, Dave, what's the catch? If anyone can just start lash a probe like this together practically zero cost, then why bother with like expensive high bandwidth uh probes like these ones?

**Dave Jones:** Well, the first thing is is of course that gorgeous input impedance. That ten megohms um at DC by the way, we'll get into that uh input impedance. And well, you know, it doesn't load down your circuit much at DC.

**Dave Jones:** But, unfortunately, this puppy with a 1K resistor in series, these of course have to be terminated cuz this is a transmission line and if you don't terminate the other end, you're going to get reflections galore and it's just well, it's not going to work as a probe.

**Dave Jones:** So, you have to have a 50 amp termination on your oscilloscope either internal uh to the scope or just an inline one that you actually plug in. And if you run the numbers, put that into Keysight Infiniium then with a 1K in series with a 50 ohm uh termination at the other end, you're talking about a 21 uh to one ratio as opposed to a ten to

**Dave Jones:** one probe. This is a 21 to one or one to 21. So, it divides your signal by 21 times and you've got a 1K uh DC impedance. So, that loads your line down substantially.

**Dave Jones:** And of course, you don't need a 1K uh resistor in here in series. You can basically make it any uh value you want. Make it larger or smaller and you can have it um of course, if you're putting in a 450 ohm resistor, then you'd have the same uh 10 to 1 probe as you would here.

**Dave Jones:** But, the difference is um instead of having a 10 meg input impedance here, this one would have a 500 ohm input impedance. And that's going to load down uh your lines at DC.

**Dave Jones:** But, the interesting thing is that uh this is 11 puff, 11 pica farad here. And at frequency, that is going to load down quite substantially. So, now we actually have to talk about uh probe loading.

**Dave Jones:** Whereas, this is not going to have much capacitance at all. So, hence why in theory, you know, if you use the right coax and everything else, you can get, you know, 10 gig bandwidth or something, many gigahertz bandwidth out of these sorts of probes.

**Dave Jones:** If you construct them right and terminate them right and all the rest. And this probe with a 1K resistor in series, that's kind of like a typical value everyone uses.

**Dave Jones:** It's not too high, it's not too low, it's just right. It's like the Goldilocks uh value. And this probe is only going to have like, you know, one or two puff.

**Dave Jones:** Although, I haven't measured this one, probably going to be better than this real expensive $800 probe here. So, there has to be another downside to this, and yeah, there could be.

**Dave Jones:** if you choose like the 1K value in here, you've got that oddball 21 to 1 uh divider ratio instead of your more standard 10 to 1. So, even a real like, you know, highish end expensive uh scope like this Tektronix MDO 3000 1 gig bandwidth up here, um check out the probe attenuation.

**Dave Jones:** There, it's 1, 2, 5, 10. Oh, we can get 20, we can get close, but we can't get that 21. So, if you use that oddball value, then well, you either have to just set it to one times one and then just do the calculations manually, or you can uh choose the resistor value to match.

**Dave Jones:** So, you can get an E96 value resistor like just over 950 ohms, that'll give you a reasonable like uh 20 uh to one ratio. But, one other advantage of these is that uh they're actually slightly more tolerant of uh longer ground leads than uh a FET probe.

**Dave Jones:** So, that's a benefit. So, you know, these things, if done right, are really very, very good. Okay, let's give you a probing example here. We've got a Raspberry Pi 3, for those playing along at home, and we're going to probe one of the memory pins on the bottom here.

**Dave Jones:** I don't care which one. I've just picked one at random. We're getting a signal on it. So, I'm using the 2 GHz active probe here, the N12796, overkill for what we're doing.

**Dave Jones:** Well, overkill for this scope, anyway, because this is a 500 MHz bandwidth scope. So, this active FET probe more than good enough for measuring the bandwidth that we've got here.

**Dave Jones:** So, I'll use this long lead here for my ground. I'll put it on the ground pin of the connector there, cuz that's just very convenient. For those who care about such things, you can actually see what point I'm probing.

**Dave Jones:** Where is it? I think it's there. Geez, I can barely see that. This is where, you know, magnification uh comes in. Okay, I'm probing a point there. I don't know what it is.

**Dave Jones:** I don't care. There it is. There's our signal. It's made up of a whole bunch of stuff, but basically, you can see, look, it's got some undershoot here. It's got a little bit of ringing there.

**Dave Jones:** It's got a little bit of ringing there. I'm going to hazard a guess that that's going to be due to our long ground lead there, right? Okay, so, we'll just try and capture that sort of like the most frequent one there.

**Dave Jones:** There it is. Got it. Okay, so, I'll store that. Right, so, what I'm going to do now is I'm going to actually change the ground into this. Instead of having this longer lead, I'm going to go for one of the shorter little adapter ground adapter pins we've got in there.

**Dave Jones:** It looks like there's a little bypass cap. I've determined that this right-hand side is the ground. So, that's very convenient, because that's right next to the point that I want to test.

**Dave Jones:** Otherwise, as I showed before, like that have to like install one of those copper pads or something. You might have to like scrape away some of the ground here or something like that and maybe put the copper tape over the top of the chip or something like that or you'd have to scrape away some other ground point somewhere or you know, soldering a little contact loop pin or something

**Dave Jones:** like that. So, here it is. I got my little adapter. Careful cuz you can stab yourself with these little bastards. There we go. So, we have this little now ground pin which can sort of like you know, pivot around like that and anyway, that will make better contact and this will be a higher frequency probe because it's a shorter inductive path.

**Dave Jones:** So, let's try that. We'll require the turn at the right angle and probably some magnification here. Okay, I've got my ground point and I've got my probe point. Pan up, pan up.

**Dave Jones:** Okay, let's have a look. I've changed my digitizer. Definitely getting 5 gig samples up second and I saved my reference waveform. So, let's single shot capture that. See if we can get it.

**Dave Jones:** No. There we go. Got it. Now, I can actually adjust that waveform there to show you. There you go. So, the orange one I've got there is the reference waveform and this new yellow one is the one that we just probed and there you go.

**Dave Jones:** It is like it's of course like the same wave shape. You can see it's got the longer ground lead one, the orange one has some extra undershoot there and comes back and takes more time to come back up like that and the one up here got some extra wiggle wiggle wiggle yeah on the top there, some overshoot.

**Dave Jones:** So, you know, there are differences in probing right there. But, at the moment this is the loading of the line with a one picofarad one puff active probe which costs a couple of thousand dollars.

**Dave Jones:** Okay, now I'm going to use my 500 megahertz passive probe here. It's the N28 43. It's 11 picofarads. okay? And yes, I've compensated this. You compensate it with your probe compensation on the front.

**Dave Jones:** So, everything's hunky-dory. I'm using my low inductance high frequency ground probe attachment, so that's equivalent to what we had before. So, we should get because we've only got a 500 bandwidth scope here, then the bandwidth of the probe isn't really going to matter that much.

**Dave Jones:** Hold my tongue at the right angle. And probe this. I think I got it. But here's the interesting thing. I've changed the reference waveform to my low inductance short ground one before, so the orange one is the best we could get with our active probe.

**Dave Jones:** So, the exact same ground point, basically the same ground length, and you can see that well, you know, our wave shape is the same, but look. Look at this.

**Dave Jones:** It's a much higher level down here. Okay, this is 200 mV per division, so it's like, you know, 50 odd mV higher there, and it's actually lower down here, our yellow waveform there.

**Dave Jones:** So, you know, all although we can see like the wave shape and everything up here, it's like when the bus is loaded differently cuz that's what this little you know, ramp up here is going here.

**Dave Jones:** I don't know the architecture of the Raspberry Pi. It it doesn't matter, but I know there's something happening there with there, and down here we're actually seeing a larger drop across the bus here, which is interesting, isn't it?

**Dave Jones:** I it you know, there's significant differences here. This is wasn't example I wanted to show. I just like it's a random example, but you can see the difference here between a 500 meg passive probe and and effectively a because of the bandwidth of the oscilloscope of 500 meg active probe.

**Dave Jones:** They load down the circuit differently. And I know you want to see it. Okay, let's compare Dave's dodgy homemade resistive probe here with a 1k resistor in the tip.

**Dave Jones:** We'll give that a burl. Got a 50 ohm terminate that. But scope can do that, no worries. Tongue at the right angle, tongue at the right angle. Fix that.

**Dave Jones:** Woah! Check this out. This is absolutely fan-freaking-tastic. Now, what we've got here, the orange waveform of course is our reference active FET waveform. That's a $2,500 active FET probe.

**Dave Jones:** Yes, it is compensated because you do still compensate them and it stores it internally because it knows the serial number of the probe, etc. And the yellow one is Dave's do-it-yourself couple of buck resistive probe.

**Dave Jones:** Look at this. What's going on here? Well, it's obvious that what's happening at this point right here is that the bus is actually going open or something. I don't know the exact architecture of what's you know, the pin I'm actually probing.

**Dave Jones:** It doesn't matter, right? It's like it's going open. And because the probe is 1 meg DC resistance, look at that. It's basically it's not going to discharge. Maybe if we got like a longer time period it'd eventually do a similar like eventually discharge or whatever.

**Dave Jones:** But you see that the bus is actively changed. But because we're now loading this bus down with a 1K resistor or a 1.05K resistor cuz we've got the 50 ohm terminator as well.

**Dave Jones:** It boom! This isn't This looks like for all the world and it is an RC discharge curve. So there you go. What's that? You know, 10 nanoseconds per division.

**Dave Jones:** I don't You can work that out, whatever. For those playing along at home. But you can see how the resistive probe actually completely changes the circuit that you're actually measuring.

**Dave Jones:** So sure, like the signal integrity is excellent. Let's let's take a look at this actually. If you have a look at the bottom here, you can see that both of them undershoot almost exactly the same.

**Dave Jones:** But you remember how I said that the resistive probe can actually be more tolerant of longer ground leads. I think they're both about the same length. I think they're practically near identical.

**Dave Jones:** Remember how I said it can be more tolerant on these than active FET probes. This might be an example of this cuz this is not This is not some controlled experiment.

**Dave Jones:** This is just something I slapped together willy-nilly and this is the result that we actually got. This is fascinating, right? They both undershoot exactly the same, but the active FET probe, the orange one, actually look it overshoots again when So and it takes much longer to recover than the resistive probe.

**Dave Jones:** Look at that. So this could be an example of where this cheap ass do-it-yourself resistive probe is actually outperforming this $2,500 active FET probe in terms of signal integrity.

**Dave Jones:** But once again, this is not a completely controlled experiment. But this is what you can actually get. But of course the limitation is that it loads it down much more.

**Dave Jones:** 1K as opposed to 1 meg, right? There's a huge difference there. And you might know oh what's the difference between this load you know look it's it's dropping with the 1K.

**Dave Jones:** Is that the effect of the 1K load over here? Well, it's actually not. If we actually measure that cuz you remember it's a divide by 21 probe as opposed to the active FET probe which is divide by 10.

**Dave Jones:** So if we actually set up our cursors here and go I've set them precisely to the same ground point here. Our resistive probe is we're getting 55 millivolts there.

**Dave Jones:** So if you get your confuser out, 55 millivolts times 21 which is our probe, 1.155 volts. And this is a looks like it's a 1.2 volt bus. So it's like it could be like it's maybe 50 millivolts under, but we have to measure the other one actually.

**Dave Jones:** So, if we adjust that, we're talking about 60 millivolts there. So, it's actually precisely six divisions there, and we were on 200 millivolts per division. So, that's precisely 1.2 volts.

**Dave Jones:** So, the resistive probe is actually measuring 50 millivolts less, and that could be the load the extra loading of the 1K load. Once you you'd have to check out the driving strength of the driver actually used in this, which is the whatever micro is used on the Raspberry Pi or whatever.

**Dave Jones:** But, because as I said, we can't actually put in a actual ratio, it doesn't let us put in our own user-defined value. It only does you know, these fixed ones.

**Dave Jones:** But, if it did do that, then we could actually get you know, well we've measured it. We we can see that it's basically 50 millivolts under. So, that could be like an extra 50 millivolts drop caused by the loading of the probe.

**Dave Jones:** That's what it seems to be the case. But, once again, this isn't exactly a really proper setup controlled experiment. But, that's possible, and it's kind of like you know, the sort of value that I'd expect.

**Dave Jones:** But, you can definitely see the loading there. And by the way, no, this is not just a like a freak capture where you know, the bus did something different than before.

**Dave Jones:** This happens every single time. No matter how many times I capture this, the 1K probe is definitely totally different to the active FET probe here. And you can see obviously the bus was floating there, and then it went boom, no.

**Dave Jones:** I'm going to go actively low. And of course, the choice of resistor value is always going to be a trade-off. Like if you go higher and higher in resistors, then your divider ratio gets higher and higher and higher, and you can't measure low-level signals, and it's not that great.

**Dave Jones:** But, the higher value in resistor you go, the more you can isolate the cable and system capacitance from the tip. So, technically, you know, the less you're loading your circuit, but it's all a big trade-off.

**Dave Jones:** So, there you go. I hope you found that useful. There's no shortage of either do-it-yourself or relatively cheap resistive probes or even, you know, active probes. Yeah, they're expensive, you know, many thousands of dollars.

**Dave Jones:** Although, there's do-it-yourself active probe designs as well. There's a lot of like open source ones as well, and they're just going to work just fine. So, certainly, don't worry about thinking that you're wasting your money buying a high bandwidth scope like this 1 GHz one or the 800 MHz model or the 500 MHz model or whatever.

**Dave Jones:** No, there's lots of probing solutions available for your scope, even though it has no fancy pantsy active input or even the times 10 input. Unfortunately, not all scopes have the ability to put in like a customized resistive probe value.

**Dave Jones:** You choose your resistor value based on your requirements, and it might be 10:1, it might be 20:1, it might be some oddball value or something like that. But, in this particular case, the Rigol, if we go into the probing interface here, we can choose all these standard ones, fantastic.

**Dave Jones:** But, in the case of my little custom one with a 1K probe here, this is actually a times 21 probe. So, I can actually choose the user thing here, and I can do 21 X like that.

**Dave Jones:** Okay. Bingo, I've got a times 21 probe calibrated for my little cheapy couple of dollar resistive probe here. Nice. So, if you found that video useful, please give it a big thumbs up.

**Dave Jones:** As always, discuss down below. Catch you next time.
