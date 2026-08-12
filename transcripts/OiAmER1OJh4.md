---
video_id: OiAmER1OJh4
title: EEVblog #453 - Mysteries of x1 Oscilloscope Probes Revealed
url: https://www.youtube.com/watch?v=OiAmER1OJh4
source: youtube-asr
timestamps: {"0": 1, "1": 15, "2": 24, "3": 41, "4": 55, "5": 81, "6": 92, "7": 103, "8": 119, "9": 135, "10": 152, "11": 165, "12": 179, "13": 197, "14": 211, "15": 222, "16": 230, "17": 246, "18": 259, "19": 267, "20": 276, "21": 289, "22": 301, "23": 317, "24": 331, "25": 353, "26": 361, "27": 377, "28": 388, "29": 405, "30": 415, "31": 432, "32": 444, "33": 456, "34": 472, "35": 490, "36": 507, "37": 521, "38": 529, "39": 541, "40": 557, "41": 566, "42": 580, "43": 593, "44": 606, "45": 618, "46": 631, "47": 648, "48": 659, "49": 674, "50": 684, "51": 696, "52": 709, "53": 719, "54": 727, "55": 739, "56": 755, "57": 777, "58": 794, "59": 817, "60": 841, "61": 859, "62": 885, "63": 900, "64": 913, "65": 924, "66": 941, "67": 952, "68": 964, "69": 979, "70": 988, "71": 1012, "72": 1023, "73": 1033, "74": 1046, "75": 1062, "76": 1071, "77": 1094, "78": 1104, "79": 1114, "80": 1126, "81": 1144, "82": 1157, "83": 1169, "84": 1184, "85": 1197, "86": 1218, "87": 1227, "88": 1249, "89": 1266, "90": 1286, "91": 1302, "92": 1326, "93": 1346, "94": 1357, "95": 1371, "96": 1382, "97": 1393, "98": 1406, "99": 1422, "100": 1432, "101": 1446, "102": 1460, "103": 1469, "104": 1481, "105": 1493, "106": 1502, "107": 1513, "108": 1528, "109": 1543, "110": 1562, "111": 1588, "112": 1600, "113": 1616, "114": 1637, "115": 1661, "116": 1683, "117": 1698, "118": 1712, "119": 1734, "120": 1747, "121": 1762, "122": 1771}
---

**Dave Jones:** Hi, in a recent video I casually mentioned that one of these switchable times one times 10 oscilloscope probes has a drastically reduced bandwidth in times one mode compared to times 10.

**Dave Jones:** We're talking like order of magnitude or more lower bandwidth. So like a 100 megahertz bandwidth probe or a 200 megahertz bandwidth probe does not have that same bandwidth on times one.

**Dave Jones:** It is much much lower. And a lot of people were surprised by that and I actually didn't find that rather surprising because it's not a well-known thing that's and it's not something that's mentioned in a lot of places at all.

**Dave Jones:** People just go blindly around thinking that my 100 megahertz probe is 100 megahertz regardless, but it's not. So few people asked me could I explain why that times one bandwidth is lower than times 10.

**Dave Jones:** As it turns out, it's rather interesting. So let's discuss that. I don't think this has actually been discussed anywhere not as a topic on its own. Anyway, there's a lots of tutorials out there on how times 10 probes work and compensation and all that sort of stuff, but um why is the bandwidth of a times one probe lower?

**Dave Jones:** I don't think that info's readily available out there. So let's investigate. Now, I'll just say that this certainly is not going to be a tutorial on how to use probes and why and all that sort of stuff.

**Dave Jones:** That needs to be an entirely separate video and there's other ones out there. So we're just going to focus on why the times one is slower than the times 10 or has lower bandwidth.

**Dave Jones:** So as an example, we're going to look at this some RP 3300 passive oscilloscope probe fairly typical. It's a high bandwidth one 350 megahertz comes with the Rigol DS2000 series scopes and this is what I showed last time in the video that caused people to ask about this.

**Dave Jones:** Now, let's have It's a very very typical times one times 10 probe. There's no compensation up the top here. The compensation is done down the bottom, but it can be done in either place, but on the higher bandwidth ones, typically done down the bottom.

**Dave Jones:** Now, let's take a look at the specs, shall we? Look at this. Bandwidth times one DC to 8 MHz. 8 MHz? Are you kidding me? It's useless. God. Anyway, times 10, look, DC to 350 MHz.

**Dave Jones:** So, they sell these as 350 MHz rated probes, but you switch it to times one, you got this crap 8 MHz probe. You bought this wonderful 200 MHz bandwidth scope, and you switch it to times one, and it's just garbage.

**Dave Jones:** Why? Well, we're going to find out. And because of that, of course, the rise time, big difference, 900 picoseconds, 900 puff. Look at that. Uh times 10, and 40 nanoseconds for times one.

**Dave Jones:** Huge difference, but that's not surprising considering the the relative bandwidth difference there. And of course, the input resistance is going to be different between the two. 1 meg, everyone knows that 1 meg standard input impedance cuz it just goes through to your It's basically just a bit of coax.

**Dave Jones:** When you put it on times one there, basically just a bit of coax. Well, we'll see. Goes all the way through to your scope. But in times 10 mode, of course, it's 10 megohms input impedance because of the extra 9 meg resistor in here, which a lot of people are familiar with.

**Dave Jones:** And of course, the input capacitance, that will come into play as well. Times 10, it's only 16 picofarads, very small, equivalent to the tip capacitance, which we'll take a look at.

**Dave Jones:** Times one is 100 picofarads, huge amount of capacitance there. So, that will come into it. Now, the first thing you should say is, "Well, [ __ ] Show us.

**Dave Jones:** All right. We've got our signal generator here. We've got our scope. I've got it set to uh 1 V peak-to-peak sine wave at 1 MHz. So, we'll be able to adjust the frequency and there it is 1 V peak-to-peak.

**Dave Jones:** You probably can't see that down there unless you're watching in HD, but that is 1 V peak-to-peak. Not a problem, right? At 1 MHz, it's you know, the probe really isn't uh introducing any attenuation at all.

**Dave Jones:** And with limit doesn't come into it because as we saw, oh by the way, I'm on times one here with the uh scope probe. I can switch it to times 10, of course.

**Dave Jones:** And there we go, we get 1/10 the amplitude. So, we're on times one. So, let's actually adjust the frequency here up and see if we do get that rated 8 MHz bandwidth.

**Dave Jones:** So, cuz we're 1 V peak-to-peak, um it's specified typically at minus uh 3 dB bandwidth, which should be uh 0.707. So, point if it's 1 V peak-to-peak, should be 0.707 V.

**Dave Jones:** say 0.7 V peak-to-peak. So, here we go. We'll wind the frequency up. 2 MHz, 3. Aha, you can see the amplitude dropping. Look at that. Let's see what we get at 8 MHz.

**Dave Jones:** There we go. We're getting 800 mV. So, it it's actually bandwidth is better than what it uh says on the data sheet. And 707 Let's go down. Probably can't read that.

**Dave Jones:** There we go. That's practically 0.707 10.1 MHz bandwidth of this probe on times one mode. Huh, useless. And of course, if we keep uh increasing the frequency on that, I'll go up a digit.

**Dave Jones:** Here we go. And we're up at 30 meg 40 MHz, 50, 60. See, this is a 350 MHz rated probe. And it's absolute There's 150 MHz. Useless. I mean, you know, yeah, we're still getting something down there, but you know, I mean, the attenuation is is absolutely horrible.

**Dave Jones:** And we'll switch it to times 10. Here we go. And we'll do the same thing. We've got to turn our vertical up there. And we're at one We're at 1 MHz at the moment.

**Dave Jones:** And let's keep going. There we go. It's dropping a little bit, but I think that's probably No, it's going back up a little bit. So, that's probably the amplitude stability of this Rigol function gen.

**Dave Jones:** But, we're up at 160 MHz now. And that And well, 160 MHz is the maximum frequency of this uh sig gen. But, there you go. It basically did not drop in amplitude.

**Dave Jones:** You know, there's a little bit of change there, but the amplitude stability of this I don't know the spec, but it basically That probe is just fine. It is not attenuating at all because it has a rated bandwidth of 350 MHz on times 10 mode.

**Dave Jones:** And of course, that bandwidth limit is going to kill any high frequency content like this square wave, for example. Here's a 10 MHz square wave on times 10 mode.

**Dave Jones:** bandwidth of our probe is 350 MHz. And of course, it looks like a square wave. I didn't see the overshoot in the actual signal fidelity in there. But, if we switch it to times one, that bit Look at that.

**Dave Jones:** Bandwidth limit of that times one probe. It's useless. Now, you're probably asking yourself at this point, something smells a bit funny here because isn't like a scope probes supposed to be like good quality coax?

**Dave Jones:** And when you put it on times one mode, it's just a bit of coax going in, right? Well, yeah, it should be. So, let's get a bit of coax.

**Dave Jones:** There we go. And let's whack it in there. And see what we get. Here we go. Look at that, a bit of overshoot there. Bit of ringing because it's not terminated properly, but let's increase this in frequency.

**Dave Jones:** We're at one We're at 1 MHz there. So, let's wind it up and as you can see, 40 MHz, 50 MHz, no problem. Look at the Well, it's rounding off there, but let's not Look, but there is no attenuation of that signal by just a bit of coax.

**Dave Jones:** So, why is your humble oscilloscope probe got a lousy 10 MHz barely 10 MHz bandwidth on times one mode when it's supposed to be just switched directly through? Hmm.

**Dave Jones:** Let's go to the whiteboard. And tada, here we have the circuit of a typical times one times 10 switchable probe. You may have seen these before. Yes, this is a new whiteboard mounted on the wall.

**Dave Jones:** Isn't it neat? And yeah, you may have seen this circuit all over the place. Very typical. There's lots of articles and tutorials on how times 10 compensated probes work.

**Dave Jones:** We won't necessarily go into that here. What we want to find out is why that pesky times one probe has that really low bandwidth. So, let's start out at the tip over here.

**Dave Jones:** Here's the probe tip. There's a little bit of probe tip capacitance. They don't often show this in the circuit. They just show the typical 9 meg resistor and the compensation cap, but we'll show it because it's actually rather valid and it'll come from the data sheet as well.

**Dave Jones:** Uh these are all going to be uh typical values. Of course, they will kind of vary, but uh let's just go for typical. Now, on a times 10 probe, you have a series 9 meg resistor in here.

**Dave Jones:** So, it voltage divider with the 1 meg input on the oscilloscope over here. It forms at DC forms that uh uh times 10 divider. They call it times 10.

**Dave Jones:** Yeah, I know it's really weird. It's divide by 10. Now, of course, there has to be a compensation cap across that 9 meg resistor to um take into account the AC bandwidth of the probe.

**Dave Jones:** So, you've got to compensate that for your input because the input of the oscilloscope here also has about 15 pF of input capacitance. Very typical across the three scopes I've got here.

**Dave Jones:** Um even from the 500 MHz Agilent right down to the DS1052E, they're all around 50 around 15 pF plus minus a few pF input capacitance. So, that is designed to compensate for that.

**Dave Jones:** Ignoring the coax at the moment, just assume it's an ideal coax ideal transmission line. And that's all there is to it. Now, there is actually two different schemes and I've shown you before.

**Dave Jones:** There are these types which have the compensation not in the probe tip here. So, this capacitor is actually fixed. It's not variable like I've shown here. The variable capacitor is over here in a little RC network over here.

**Dave Jones:** Typically, it's going to be a series resistor in here with an adjustable cap, 0 to 50 pF, something like that. Exact values are going to change depending on how the probe is actually manufactured.

**Dave Jones:** And typically, your high bandwidth ones are you won't get the adjustment in the top here. You'll typically get it at the base down here. But, you can also get the uh uh lower bandwidth ones which have the adjustment in the top here.

**Dave Jones:** So, they actually have the adjustable capacitor in there, the trimmer cap, and they don't have any network down here. So, the coax just goes directly into the scope. So, you can ignore that.

**Dave Jones:** Those components don't exist. All you've got is the 1 meg and 15 pF input capacitance of your scope. Now, let's take a look at a times one probe and how that works here.

**Dave Jones:** And you notice I've added some sneaky little calculations in here. Now, how times one probe works incredibly simple. All it does is it's got a switch in there and shorts out the nine meg resistor and the compensation capacitor.

**Dave Jones:** That's it. So, these no longer exist. So, you've got a direct connection from the tip directly through to your oscilloscope input. And of course, if you don't uh have that network there, you've got nothing.

**Dave Jones:** So, all you've got is your tip capacitance, you've got the capacitance of your coax, which uh let's just say it's 100 pF for a meter for uh argument's sake.

**Dave Jones:** It's going to vary depending on the type. But let's just say it's 100 pF, and once again, that will be, you know, equivalent to another capacitor in there like that, distributed, uh whatever.

**Dave Jones:** Capacitance of the coax and the capacitance of your um scope input and your one meg input resistor. So, you would think that Okay, you've got all this capacitance on here, and it's going to have an impedance at frequency.

**Dave Jones:** Now, you should know your formula for uh capacitive reactance or uh the effective AC resistance of the capacitance at a frequency. It's one over 2 pi FC. So, let's take an example of 10 MHz, which is roughly the bandwidth of the times one probe we measured, and let's plug in these values of 15 pF, which we got here and here, and that works out to about 1 K.

**Dave Jones:** So, at 10 MHz, you've effectively got no longer got a one meg ohm um oscilloscope input here. You've got one meg in parallel with one K here in parallel with one K here, and then the capacitance of the coax, 100 pF, that's about 159 ohms at 10 MHz.

**Dave Jones:** So, very low. Your one meg input impedance scope is now like, you know, 100 ohms or thereabouts. Incredibly low input, but still, let's say you've got no um loading effects on your circuit, you're driving it with a low impedance load, then your signal should go faithfully directly from the input through to the scope without any attenuation.

**Dave Jones:** So, why are we getting uh the attenuation on that that um drastic attenuation about 10 MHz bandwidth on the times one probe, whereas a bit of coax, which is essentially exactly the same thing, it's just well, let's say it's longer, you know, it's got 115, then effectively what's the difference between the times one probe and a bit of coax?

**Dave Jones:** There shouldn't be any difference, but there is. We measured it. Why? Hmm. Think we can solve this one with a multimeter. Now, before we get to the multimeter, let's just have a look at the input specs again and see how they relate to what we've seen on the whiteboard.

**Dave Jones:** Let's look at the input capacitance here in times one mode, 100 pF. Now, that's effectively the capacitance of your coax cable only, because the times one switch, of course, shorts out the input compensation network, and all you're left is with the coax, but it can actually also include um the in compensation network if you've got it at the end of the cable like here um at the scope end rather than um this

**Dave Jones:** one here, which it just has the coax going directly into the uh scope. And that is like in that case, they'll have the compensation network up here. Now, there's actually not much um difference between having the compensation network in here and down at the end of uh the probe down here.

**Dave Jones:** You can the performance can be uh the same effectively. Uh depends on how you tweak it and uh actually design it. But, um most of your high-performance times 10 uh probes will have uh your compensation network down this end here.

**Dave Jones:** Now, if we have a look at the uh times 10 mode here, it's 16 pF, an order of magnitude less effectively. The reason for that, that is the effective tip capacitance.

**Dave Jones:** And I say the word effective because it not only includes the small amount of capacitance between your tip here and your input compensation network in here, your standard in 9 meg resistor down in there, but it's also the effective reflected capacitance from your coax as well.

**Dave Jones:** So, it's that 100 pF, but because we've got a times 10 divider in there, that capacitance gets divided down and then becomes effectively 10 times less at your tip.

**Dave Jones:** So, that's why that one's 10 times less. This one's a little bit higher at 16 pF, usually a little bit less than that. Usually, but usually you'll see an order of magnitude difference between those.

**Dave Jones:** And also, this is why uh your fixed times 10 probes um have it can have a better performance than these compromised times one times 10 probes because your compensation network can be right at the tip.

**Dave Jones:** That 9 meg resistor can be right up there, and there's bugger all tip capacitance, whereas this one's got just a little bit extra and a bit of extra transmission line in there as well to deal with.

**Dave Jones:** So, yeah, your fixed times 10 probes are always going to be um uh higher performance or can potentially be higher performance than these switchable compromise blah probes. And that's why a times 10 probe is highly valued because um it has a much lower input capacitance than your times one.

**Dave Jones:** So, it loads your circuit down much less at high frequencies. That capacitive reactive reactance formula we looked at, remember that? Now, what we're going to do, we've got our regular coax here.

**Dave Jones:** It's just like half a meter of uh coax, and we're going to measure the center conductor. And well, no surprises what we're going to get here, folks. 0 ohms.

**Dave Jones:** There you go. It's a a short because the coax just goes directly through. Uh yeah, it works as a transmission line and everything else, which we won't go into today, but what happens if we measure this scope probe on times one, by the way?

**Dave Jones:** So, let's Well, let's put it on times 10 first, okay? And we should get our nine meg that we looked at on the board there. There it is, spot on nine meg, no worries.

**Dave Jones:** But, we switch it to times one and there should be nothing else in there but the switch, right? That's it. You'd expect to get exactly the same as the coax.

**Dave Jones:** Do we? There we go, 330 odd ohms between the tip and down here. What is doing that? Is there a series resistor in there? Well, to show you that there's nothing uh no funny business going on in this tip here, I've taken apart a times 10 uh well, switchable times one times 10 probe.

**Dave Jones:** Yes, it is um different to the Rigol, it's not a Rigol brand, it's a Velleman brand, it's just a cheap ass old one I had lying around, and there's the times one times 10 switch.

**Dave Jones:** So, times 10 is down in that position down there, so we're up in times one position, and that should short out the uh network there. So, the compensation network.

**Dave Jones:** So, let's measure between that probe point and here. What do we get? A dead short. So, there's no funny business going on inside that probe that uh well, what we'll call the probe.

**Dave Jones:** It must be in the coax or the end of the coax. And here's the part of that uh chopped off Velleman probe and let's measure it. There we go, and the fine wire, I'll show I'll get a very good close-up of this in a minute, but basically, I'll have to hold my finger on there, I'm not touching the other one.

**Dave Jones:** There you go, 230 odd ohms. This oscilloscope coax, and trust me, folks, there is nothing There's no series resistor or other circuitry inside. There I could chop it open to prove it, but I don't know.

**Dave Jones:** Couldn't be bothered. Oscilloscope probes do not use regular coax like a regular coax cable. These are what's called a lossy transmission line. They're designed to have that high resistance.

**Dave Jones:** And check it out. That's what's inside an oscilloscope coax cable. It's a single strand there. No, I haven't actually You know, when I stripped it, no, I didn't accidentally cut off all the other strands.

**Dave Jones:** It is a single tiny strand like that. And often, it is You might be able to see that it's actually not entirely straight. It's actually got little kinks and bends in there, and that's actually designed in.

**Dave Jones:** In some of the more higher-quality ones, remember, this is only a 60 MHz Velleman heap crap. And that's what these probes are optimized for. They're optimized for their times 10 mode, the high-bandwidth mode, which is why they're going to use this lossy transmission line, which has Typically, most of probes are going to have a couple hundred ohms.

**Dave Jones:** It will vary by plus minus a couple hundred. You know, the actual DC resistance isn't in actually, you know, it's it's important, but it's not the main, you know, driving factor.

**Dave Jones:** Transmission line design theory, I won't go into it. It it is actually quite complex. I may have to do a separate video on this, actually simulating all this stuff and exactly how it works, but that's these probes are optimized for or the transmission line coax, the lossy transmission line, is optimized for the high-bandwidth times 10 mode.

**Dave Jones:** So, the times one mode is actually just a bit of a kludge added on, and that's why we're crippled with the low bandwidth on the times one mode because they're trying to incorporate both features into a times 10 probe.

**Dave Jones:** So, just a bit more of that out and you can see somewhere along here the crinkled nature of that wire. There it is. See it's sort of crinkled and uh some of your more high performance ones are much more crinkled than that and uh presumably they do that to uh help with the flexibility of the cable and of course but you'd have to take all that into

**Dave Jones:** account about the final resistance cuz this is actually not just regular wire of course. It is resistance wire which uh has a certain specific high resistance uh designed to match the compensation network and that's how the whole probe is able to get its high performance.

**Dave Jones:** I mean this is only a 60 MHz one so this isn't a particularly high performance one at all but you can see the white foam uh insulation in the core there and that would have a very low dielectric loss very specifically chosen for the task and there's a black outer protective jacket there and then the braid shield and then the outer jacket on top of that.

**Dave Jones:** So there's a lot of art and science which goes into the design of these probes and then the matching of the coax used in these and then the matching compensation networks to give you a flat uh usable response up to you know in some cases well over 500 MHz which is really amazing technology.

**Dave Jones:** So these aren't just regular coaxes. So after that little investigation what are we left with? We're left with the knowledge that this bit of coax ain't a bit of coax.

**Dave Jones:** It's a lossy transmission line. It has DC resistance in there and that's going to which we measured at around about 330 ohms. So that now aha we have an attenuator.

**Dave Jones:** Whenever you got a series resistance and a resistance at the other end you've got an attenuator. So let's look at the entire circuit we've got now for our times one probe, okay?

**Dave Jones:** These don't exist anymore. Our resistor and cap don't exist. So, that just goes straight through. Wired straight through like that. This 1K really doesn't come into the equation at all.

**Dave Jones:** So, what might as well not even exist. So, we'll leave that out and we've got 330 ohms now in series with Let's take out our compensation network here. Let's assume we have a probe that doesn't have the compensation network at this end.

**Dave Jones:** And then our 15 picofarad scope input has now become a 1K resistor as well. So, we effectively have 330 ohms in series with 1K. Ignore the one meg. It's couple orders magnitude bigger than the 1K.

**Dave Jones:** So, it doesn't matter. A rough rule of thumb is something's an order magnitude bigger, 10 times bigger, you don't worry about it. You just take it out of the equation for back of the envelope type calculations.

**Dave Jones:** So, if you do the math with that 330 ohm and the 1K over here, which is the impedance at the roll off from minus 3dB roll off frequency at 10 megahertz we measured, it's around about that minus 3dB point.

**Dave Jones:** Well, that point 0.707, I think it's 0.75 or something like that. Near enough. So, that's what determines your upper frequency limit. This series resistance um and your capacitive reactance of the input is scope.

**Dave Jones:** But, of course, it gets a little bit more complicated than that because that 330 ohms, yes, it's at DC and yes, it's going to be quite similar at um AC as well.

**Dave Jones:** But, this is because it's a distributed resistance, it's actually all the way through here. So, I've shown this is all different resistors in there. And this is how you can actually simulate the thing using the lumped model like this.

**Dave Jones:** And then you've got the individual capacitance is in here. And there'll also be inductance as well in any model of a trans of a lossy transmission line like this, but I haven't shown any of the inductors.

**Dave Jones:** So, of course, that's 330 ohms at you know, let's just say it's going to be constant at AC and DC. The input is going to be different at DC.

**Dave Jones:** At DC, we're going to have our 1 meg. So, that's why down at the low frequencies with the times 10 probe, this 330 the resistance of this um coax doesn't matter at all cuz you know, 1 meg.

**Dave Jones:** Do your voltage divider math there and this doesn't matter a rat's ass. So, the higher frequency you go, the greater attenuation you got and and you know, you can muck around with all little Rs and Cs and stuff in the lumped model, but basically, you're going to have that upper frequency.

**Dave Jones:** So, you're going to get that frequency roll off that looks like that at a certain frequency and it's going to be 3 dB down at about 10 megahertz there.

**Dave Jones:** If that's your 1 volt input, it's going to be 0.707 as we measured on the scope. It's going to have a roll off because you've got effectively a a capacity here which changes with frequency and let's say a fixed series resistor element.

**Dave Jones:** So, why do they even bother having these switchable times 1 times 10 probes if the times 1 mode bandwidth is useless? Well, it's just convenience. Um essentially, they design these things for the high bandwidth on the times 1 mode uh but they're but that by nature of its very design with the lossy transmission line, um it just cripples uh the times 1 mode and makes it pretty

**Dave Jones:** much useless. Well, it's not useless. It's just low bandwidth. So, the rule is if you want high bandwidth and you don't want to attenuate your signal which the times 10 probe does, that's one of its disadvantages.

**Dave Jones:** One of the advantages of the times 1 mode, you're not attenuating your signal by 10 times, then use a regular coax. And of course, you can get very high bandwidth probing with just a regular coax if you you know there's various uh termination resistors on the input and stuff like that.

**Dave Jones:** These can be very high bandwidth probes. Incredibly low impedance of course because you've got the direct capacitance of the coax there and at high frequencies but if you want high speed with no attenuation then just a regular coax can be useful and I might do a video on that too and there's other videos out there that explain that.

**Dave Jones:** So why do they go to all the effort to have a lossy transmission line in here when you know you can just use an ordinary coax? Well, it this is the way this is the technique that they use to get ensure the widest bandwidth possible in a times 10 probe and also the flattest bandwidth possible over that mode so it doesn't at the end at the end

**Dave Jones:** of the bandwidth doesn't ring up like that or doesn't go down like that or anything like that. Does no funny business. It's a lot of art and science goes into this and it was originally developed by Tektronix way way back and they were the ones who pioneered the lossy transmission line technique and they're very cleverly and very carefully designed to get like the you know your 5

**Dave Jones:** 6 700 MHz bandwidth passive probes which you know you take for granted these days but they're you know you're paying a lot for that and there's a huge difference between a cheap ass 60 MHz probe and a 600 MHz passive probe and that's often why they cost so much.

**Dave Jones:** They're very difficult to actually get right and trim all and get it all right in terms of the compensation network in here that we looked at matched to the actual physical properties of the coax.

**Dave Jones:** So a lot of art and art and science goes into just designing the physical properties of that cable getting that getting that little wiggle inside exactly right getting the lossy uh, parameters all right so that they match and you don't get any funny business, overshoot, undershoot at the end of your bandwidth and all that sort of stuff.

**Dave Jones:** That requires a whole separate video, though. Woo. Well, that was a lot of talk just to get to the simple conclusion that a, uh, oscilloscope probe coax actually has a lossy transmission line resistance in it.

**Dave Jones:** I could have just told you that at the start and saved you, what is it, 15, 20 minutes worth or something, but ah, I hope you found that interesting and that is why these times one probes have a lower bandwidth than a times 10 probe, order of magnitude or greater.

**Dave Jones:** It's something a lot of people don't know, so I hope that was useful and, uh, if you want to discuss it, jump on over to the EEVblog forum and if you like the video, please give it a big thumbs up.

**Dave Jones:** Catch you next time.
