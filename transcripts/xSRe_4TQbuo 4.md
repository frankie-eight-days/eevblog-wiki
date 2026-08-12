---
video_id: xSRe_4TQbuo
title: EEVblog 1399 - DC Fundamentals Part 3: Voltage Dividers
url: https://www.youtube.com/watch?v=xSRe_4TQbuo
source: youtube-asr
timestamps: {"0": 0, "1": 9, "2": 30, "3": 46, "4": 63, "5": 77, "6": 87, "7": 98, "8": 117, "9": 127, "10": 137, "11": 165, "12": 184, "13": 193, "14": 203, "15": 217, "16": 233, "17": 245, "18": 256, "19": 266, "20": 279, "21": 308, "22": 314, "23": 329, "24": 340, "25": 359, "26": 372, "27": 384, "28": 395, "29": 403, "30": 414, "31": 431, "32": 442, "33": 459, "34": 478, "35": 498, "36": 512, "37": 524, "38": 534, "39": 551, "40": 563, "41": 574, "42": 589, "43": 600, "44": 614, "45": 626, "46": 638, "47": 649, "48": 661, "49": 672, "50": 681, "51": 694, "52": 715, "53": 724, "54": 738, "55": 745, "56": 759, "57": 767, "58": 779, "59": 795, "60": 807, "61": 816, "62": 831, "63": 847, "64": 853, "65": 868, "66": 889, "67": 908, "68": 916, "69": 928, "70": 936, "71": 949, "72": 962, "73": 972, "74": 987, "75": 1002, "76": 1013, "77": 1031, "78": 1048, "79": 1062, "80": 1073, "81": 1081, "82": 1093, "83": 1103, "84": 1118, "85": 1139, "86": 1163, "87": 1172, "88": 1179, "89": 1192, "90": 1206, "91": 1224, "92": 1238, "93": 1246, "94": 1259, "95": 1276, "96": 1291, "97": 1301, "98": 1312, "99": 1327, "100": 1342, "101": 1352, "102": 1361, "103": 1370, "104": 1385, "105": 1410, "106": 1435, "107": 1445, "108": 1460, "109": 1472, "110": 1487, "111": 1497}
---

**Dave Jones:** Hi, time for another fundamentals video and I know I said in the previous one that it doesn't get much more fundamental than voltage and current sources. Well, it does.

**Dave Jones:** I'm going back even more fundamental than this. Resistive voltage dividers and series and parallel resistors. I know it's incredibly simple stuff, but it's important. Trust me. If there's one bit of theory you're guaranteed to use in electronics in some form or another, it's voltage dividers.

**Dave Jones:** Resistive voltage dividers and there's more complex voltage dividers when you start and you can get capacitive voltage dividers and non-linear voltage dividers and all sorts of stuff. Now, we're only talking about in this video resistive voltage dividers, but they're absolutely everywhere.

**Dave Jones:** So, what is a resistive voltage divider? Well, in its most basic form, it's only two resistors like this. We've got an input voltage here and an output voltage. And as per regular convention in in electronics, the input or the input voltage in this case is on the left-hand side, the output voltage is on the right.

**Dave Jones:** That's just how you draw and conceive things in electronics. Stick to it. Trust me. Anyway, it's a resistive voltage divider where the output is always some voltage less than the input and that's it.

**Dave Jones:** It's incredibly simple because you're dropping voltage across this top resistor and tapping off the voltage from the lower resistor. So, it's always going to be less. There is no gain in this at all.

**Dave Jones:** So, V out has to be less than V in. So, what use is that? Well, it's used in practically every aspect of electronics. It's even on my t-shirt for goodness sake.

**Dave Jones:** It's used in amplifiers. It's used in attenuators. It's used in every form of voltage regulation and even appears in circuits where you don't think, "Oh, that's not a voltage divider cuz it's not drawn like a voltage divider." Like we had our in a previous video, which is actually the following video to this.

**Dave Jones:** I should have done the videos in order, but you know how we had our voltage source like this with our, you know, RS over here and this is VS, our voltage source.

**Dave Jones:** This is our battery or whatever. Well, once you go and put a load on here, it's exactly the same thing. That is a voltage divider. The output is going to be less than the voltage source.

**Dave Jones:** So, it's any sort of battery or power supply or feedback for regulation circuit or feedback for amplifiers. And you'll find voltage dividers embedded in all sorts of chips to actually get a feedback signal because what it's used for is to get a known precise fraction of, say, and it can be like in this case it's an output of an amplifier here and you can feed that back and feedback a known

**Dave Jones:** fraction of that's used in comparators and all sorts of analog circuits. It's everywhere. But first, absolutely fundamental electronics. I mean, I guarantee, apart from what is a voltage and what is a resistor, I am pretty sure it's as much unless you want to get into electron current flow and all that sort of crap.

**Dave Jones:** It doesn't get more much more simple than basic series and parallel resistors and some basic formulas you need to know and we've got some basic formulas for the voltage divider as well.

**Dave Jones:** But let's just recap cuz I don't think I've ever done it, series and parallel resistors. If you've got two or more resistors in series like this, the total resistance is just all of them added up.

**Dave Jones:** So, it's R1 + R2 + R3 or however many you've got in series, that is the total resistance. Simple. Parallel resistors like this where they're across each other, little bit more complicated.

**Dave Jones:** The total resistance here is 1 over R1 + 1 over R2 + 1 over R3 and then 1 over all of that. And then you've got a special case where you've only got two resistors, so there's no R3 like that, okay?

**Dave Jones:** Then you can actually use a different formula, and sometimes that's Some people just prefer to use this one. It's R1 * R2 / R1 + R2. That gives your total resistance for two resistors in parallel.

**Dave Jones:** So, that's absolutely fundamental, and of course, Vout is never going to be no load. There's no such thing as a no load source. So, you're going to have another resistor across here like this.

**Dave Jones:** So, this one's in parallel with this one, and you need to know your parallel resistance formulas to be able to then calculate voltage dividers and do other things. So, yeah, learn that.

**Dave Jones:** And very often you're going to use parallel resistors to actually trim resistor values, because you can't always get the exact value you need in your E12 range or E24, your E48, your E96 range, or whatever preferred resistor value you want.

**Dave Jones:** You have to tweak it a little bit by putting more one or more resistors in parallel. And that brings us to some rules of thumb for parallel resistors. If you want to lower the value, because putting a resistor in parallel always lowers the value, then if you want to lower the value by say 10% roughly, rule of thumb, then you use a value that's 10 times higher than the one that

**Dave Jones:** you're using. So, if you've got a 10K resistor there, then if you want to change lower that value by about 10%, you put a 100K in parallel with it.

**Dave Jones:** And likewise for 1%, and same thing for 0.1%, it's a thousand times, etc. Next rule of thumb is that if you want to halve the value of your resistance, then you simply put two resistors in parallel.

**Dave Jones:** That's what this little symbol, if you ever see these two parallel lines like that, that usually they'll have them sloping a bit like that, then that means parallel. And even some calculators have that.

**Dave Jones:** Hmm. And if you want to drop your resistance value by three times, you put three of the same value in parallel, etc., etc., etc. And you can also do the inverse of this for the series as well.

**Dave Jones:** If you've got a value that you want to increase by say 10% value, then you put 1/10 of the value in series with it instead of 10% instead of 10 times, you put 1/10.

**Dave Jones:** And likewise, if you got say a 10K resistor here and you want to increase it roughly rule of thumb by 1%, then you put a 1/100 of the value in parallel.

**Dave Jones:** So, if you've got a 100K there and you want to increase that value by 0.1%, you would whack a 1K in series with it and so on. Get you?

**Dave Jones:** Like these aren't exact values cuz you know, plug these numbers into these formulas and you'll find that they don't precisely work out. That's why they're called rules of thumb.

**Dave Jones:** Good enough for Australia. And as is common in electronics, you often don't need to be precise. You just need to be near enough. Even sometimes within an order of magnitude is good enough.

**Dave Jones:** Anyway, we're here to talk about resistive voltage dividers because they're so darn useful. I keep saying it and trust me, they are. Now, another formula you absolutely have to remember cuz I guarantee you're going to use this in all aspects of electronics.

**Dave Jones:** Vout here equals two which is the resistor that's across the Vout. Doesn't have to be labeled R2. I'm just labeling them R1 and R2 here. So, don't take that religiously.

**Dave Jones:** Somebody may This one may be labeled R2 and this may be labeled R1. In that case, you need to swap them around. Okay? So, it's the output resistor here, R2 over R1 plus R2 or the total resistance here times the input voltage like this.

**Dave Jones:** So, this actually applies to any arbitrary size network. So, if you've got any arbitrarily long voltage divider like this, and you want to know the tap across any one of these resistors, doesn't have to be the bottom one down here like this.

**Dave Jones:** Here I've got an example of four resistors like this. If we want to know what the output voltage here is across just R2, and you may want to do this, there's circuit configurations where this might be, like you might have and you may have like a split thing happening, or you may just be tapping off some sort of differential thing or something like that.

**Dave Jones:** There's many reasons why you might want to do this. Then the formula is exactly the same. It's actually R2. Just so happens to be the same, but anyway, it's it's the resistor you're interested in that you're getting the output voltage across divided by the total resistance.

**Dave Jones:** So, just add up R1 + R2 + R3 + R4. That gives you our total * Vin. And that will give you your output voltage. It's exactly the same for any sort of scenario.

**Dave Jones:** And likewise, it doesn't have to be across this bottom resistor. It can be across this top resistor up here like this. So, in this case, it'd be R1 over R1 + R2 * Vin.

**Dave Jones:** Got it? And just so I don't have to do another video, that leads us also into current dividers. Not nearly as common, but you should know this. And this formula applies itself again, although with a sneaky little reversal.

**Dave Jones:** Now, we've got our current source here, and we've got I, which is I total, okay? And then we've got two different current branches like this with two resistors like this, which is labeled I1 and I2.

**Dave Jones:** Let's say you want to find what the current is down I1 here, and you've got resistor one and resistor two here. What is the formula? Well, it looks very familiar like this.

**Dave Jones:** I one here equals R2 over R1 plus R2 times the total current over here. Now, you might think this looks identical, but aha, there's a sneaky difference. That's why I've put it in red.

**Dave Jones:** If it was exactly the same, this would be R1 on top over the total resistance here, but it's actually not. It's actually uh the opposite value, so it's R2.

**Dave Jones:** So, if you want to calculate I1 down here, it's R2 and so forth. Anyway, there's some really nice uh derivations of uh these formulas um actually, and I won't bog down this video with those.

**Dave Jones:** But anyway, and yes, it's not parallel cuz these resistors are in parallel, but it's actually plus. Hmm, that's interesting, isn't it? I'll leave that to those playing along at home to figure out why.

**Dave Jones:** Now, unfortunately, this current divider formula, it only applies for the case of two parallel resistors like this. You can't extend it by uh like we saw before like being uh total like this.

**Dave Jones:** You can't just add them up. It's uh it doesn't work the same way. So, if you want to extend that to more resistors in parallel, then you need to go to Kirchhoff's current laws.

**Dave Jones:** It this formula no longer applies like it does up here. It's just a little sneaky coincidence. And voltage dividers actually brings us nicely back to a previous video, or is that forward?

**Dave Jones:** Cuz technically, this is after voltage dividers in terms of theory. Anyway, brings us back to a previous video about voltage and current sources and Thevenin and Norton equivalent circuits.

**Dave Jones:** And I never did actually show you how to calculate the Thevenin voltage and the Thevenin resistance here. Thevenin and say that three times quickly. So, once again, we've got some formulas to remember.

**Dave Jones:** So, we're going to take the voltage divider here as the example. We've got a 10-V voltage source, and we've just got two 10-k resistors. The voltage is uh the output is across the bottom resistor here.

**Dave Jones:** So, what is that in terms of the Thevenin equivalent circuit in terms of just a voltage and a resistor here? Because if you remember from this previous video, which I'll link in if you haven't seen it, any combination of linear resistors and voltages and current sources can be replaced with a single voltage source and a single resistor.

**Dave Jones:** So, that's what we can do here. This voltage divider here is going to have an equivalent circuit as in it's a voltage source with a series resistance like this.

**Dave Jones:** In this case, it's going to be a pretty poor voltage source because ideally, of course, an ideal voltage source is the voltage source with zero series resistance. So, regardless of what load you put on there, it'll always give you that voltage.

**Dave Jones:** But, there's no such thing as an ideal voltage source. But, let's calculate it. How do you do it? It's easy. There's two simple formulas. One's not even a formula, really.

**Dave Jones:** It's just equals. The Thevenin voltage is equal to V open. What that means is open circuit. So, the circuit here, this is our output. So, we open circuit our output.

**Dave Jones:** So, we've got no load on there. What is the voltage across there? Well, it's easy. From your voltage divider, it's obviously 5 V. Although, we could go through the formula.

**Dave Jones:** So, of course, using your standard voltage divider formula, it's R2 over R1 + R2 * 10 V here, which is our source. And of course, that gives you 0.5 * 10, which is 5 V.

**Dave Jones:** So, Vth, our Thevenin resistance, is 5 V. What's Rth, our Thevenin equivalent resistance, series resistance? Well, it's actually equal to the V open circuit that we had before. So, that could be Vth, divided by the short circuit current.

**Dave Jones:** So, we take our circuit again, and we actually short circuit it like that. So, we short circuit that and calculate the current through there like that. What is it?

**Dave Jones:** Well, what's a short circuit across 10 K? Well, it's zero. So, all the current is now going to flow through the short circuit like this, and it's simply 10 V on 10 K.

**Dave Jones:** That's it, which is 1 mA. This is all just Ohm's law stuff, and Ohm's law's everywhere. Um so, RTH = VTH on I short circuit current. So, we've got our 5 V here, VTH / our short circuit current, which is 1 mA, = 5 K.

**Dave Jones:** So, RTH is 5 K here. So, our voltage divider here is equivalent to having a battery or a voltage source with a 5 K series resistance. It's absolutely equivalent.

**Dave Jones:** This is just not theoretical nonsense. This This is what it would be like. If you had a 5 V battery, if you get it like Seriously, go do it.

**Dave Jones:** Get a 5 V battery or 5 V voltage source, a regular 5 V, you've got them everywhere, and put a 5 K resistor in series with it, and have an experiment, and that's exactly what you'll get with a 10 V voltage source and two 10 K resistor voltage divider like this.

**Dave Jones:** And of course, that's a pretty piss-poor voltage source, cuz as I said, you ideally you want zero ohms in there. So, really it can only power like really high impedance, really high resistance loads, like say an op-amp for example, which has naff all getting towards naff all input current.

**Dave Jones:** So, 5 K series resistance in, you know, even like a bipolar op-amp input, not a problem whatsoever. This is why you'll find voltage dividers like this in all sorts of regulator circuits, switching regulators, linear regulators, and stuff like that in the feedback circuit for those circuits.

**Dave Jones:** I've done lots of power supply videos, and you've seen that before, and they can be up in, you know, the hundreds of K's and things like that, because what, you don't want to piss away your power, do you?

**Dave Jones:** So, you want to use particularly high value resistances, but then it can only drive really high value loads. As a rule of thumb, basically an order of magnitude or more.

**Dave Jones:** So, if your load is like 50k, for example, then you're only going to get like a 10%ish error. If it's 500k, boom, you're only going to get going to get a 1% error.

**Dave Jones:** If it's 5 meg, .1% etc. And from the previous video on this, how do we actually convert from a Thevenin voltage source into a Norton equivalent current source? Well, I'm glad you asked.

**Dave Jones:** Once again, a real simple formula based on Ohm's law, the Norton current here IN is just equal to VTH here divided by RTH. Once again, you just short circuit that like that and calculate the current just like we did down here.

**Dave Jones:** We short circuit it. You short circuit this like this. So, it'll in this particular case, it'll be uh 5 V divided by 5k. So, that once again, it'll be 1 mA.

**Dave Jones:** So, it'll be a 1 mA current source here and RN is equal to RTH. They're just equivalent. And likewise, if you want to go from a Norton equivalent current source back to a Thevenin voltage source, you just use Ohm's law in reverse.

**Dave Jones:** It's too easy. In this case, VTH Ohm's law equals IN * RN. Boring, huh? But, this is really powerful stuff. Thevenin equivalent circuits and voltage dividers like this, they're used everywhere.

**Dave Jones:** You've got to be aware that they're equivalent to a like relatively high impedance voltage source. And if you think voltage dividers are only used for analog circuits, well, think again.

**Dave Jones:** Although, technically, all your analog fanboys are going to say digital is just like analog anyway. But anyway, in digital systems, uh termination is a big deal. In very fast memory like DDR memory, for example, you might have midpoint termination.

**Dave Jones:** That's using voltage dividers and stuff like that. So, But, in the digital realm, you know, you can still use these analog voltage dividers. They're everywhere. Another place you use in voltage dividers, every time you use that times 10 oscilloscope probe, it's a voltage divider.

**Dave Jones:** It's quick experiment and trap for young players time. I've got a voltage divider. We've got a 10 K voltage source here power supply. We've got two 1 meg resistors like this and we've got a voltmeter over here.

**Dave Jones:** And there's my 1 meg resistor on the top. There's 1 meg resistor on the bottom. That way I'm measuring it's a decade box so that I can just, you know, trim precisely half value.

**Dave Jones:** And you can go through the formula on the whiteboard just for some practice, but of course, because they're the same value, it's of course the it's just 10 volts divided by two.

**Dave Jones:** It's half, so it's 5 volts. And that's exactly what we measure. Winner winner, chicken dinner. So, let's just double check that with another meter because, you know, you never know.

**Dave Jones:** Measure twice, cut once, is that it? Um for what? What? 4.785 volts. What the hell's going on? I think we're going to have to use a third meter to measure it.

**Dave Jones:** Um let's go like old-school. Come on, this will always work. Old-school meters, analog meters, they always work. We're on 10 volt voltage range. Um uh uh uh that's actually just a smidgen over 1.4 volts.

**Dave Jones:** Bit of parallax error there on the mirror. What the hell's going on? Go back over here just to verify and yeah, sure enough, 5 volts. Oh. Oops. If you're wondering what button I pushed there, there it is.

**Dave Jones:** Input Z, which is input impedance or input resistance. 10 meg or auto. Auto means basically there's no input resistance. It's really, really high. It's gigaohms. And you know that order of magnitude thing I was talking about on the whiteboard where if you had like one order of magnitude greater, in this case 10 meg ohms input impedance of the meter, then it causes like roughly that 10% error.

**Dave Jones:** Well, you have to go through the calculation. We'll go through that in a second. But and then if you have two orders of magnitude, or in this case that'd be 100 meg input impedance and you get 1% error.

**Dave Jones:** Or if you go up to like gig ohms and you have several orders of magnitude, then it's not really going to affect it at all. And that's why I measured 5 volts.

**Dave Jones:** Cuz when we had that meter set to effectively infinite input impedance, it's almost as if like it's an ideal multimeter and like there's just no load on there at all.

**Dave Jones:** So that's why we measured precisely 5 volts. But once we switched to that 10 meg ohm input impedance, we've now got another 10 meg resistor across here like this.

**Dave Jones:** And that's what's called your meter loading down is circuit under test. And for really high impedance stuff, like a 1 meg ohm voltage divider, even your 10 meg ohm input resistance of your standard multimeter, sometimes it's 11 but you know, it's around about that, then yeah, up you can get like a like an order of like 10% error.

**Dave Jones:** You've you've changed that value by 10%. That's pretty huge. And when your multimeter's, you know, you got your 0.05% accuracy multimeter, well, it's no good when it's causing a 10% error on your circuit.

**Dave Jones:** You've come a cropper. You might be asking why is our old school analog meter reading so low? I mean, you know, we've got 10 volts full scale at the moment.

**Dave Jones:** So 8642, it's just a smidge and over 1.4 volts there. And the interesting thing is, watch this. If I change it from 10 volt range to 2.5, you might think it'll jump up to you know, to 1.4.

**Dave Jones:** But it doesn't. And if we go to 1 volt range, so this is 1 volt full scale, It's now about 0.2 V. What the It's because of this little itty-bitty thing down here, 20,000 ohms per volt DC.

**Dave Jones:** Because this is not a fixed input resistance like your regular multimeter is. It's not just 10 megaohms. It varies with the range, and it's ohms per volt. This is a trap with old-school analog meters, and one of the huge reasons why digital meters took over.

**Dave Jones:** But, of course, you can actually get a FET analog meters that actually have active circuitry just like a digital meter, and there it is, 10 megaohms. Because, yeah, it's got little FETs in it.

**Dave Jones:** So, yeah, but this needs batteries. It doesn't rely on the 50 microamps to move the meter anymore. Well, it does, but it comes from the batteries inside, not from your circuit under test.

**Dave Jones:** So, what this 20 k ohms per volt means, it means that it actually takes 50 microamps of current to move that needle over full scale. And you can think of it in current terms, but we'll think of it in terms of resistance like this.

**Dave Jones:** So, 20 k ohms per volt, you've actually got to multiply that by the range you're on. So, that's 10 V. So, that's actually 200 k. So, effectively, we've got a 200 k input resistance on this multimeter instead of 10 meg.

**Dave Jones:** That's why it's reading low. So, how do we measure 1.4 V on our analog meter here? Well, it's easy. At 20 k ohms per volt on the 10 V range, it's equivalent to a 200 k resistor.

**Dave Jones:** So, a 200 k resistor is now in parallel with our 1 meg. There's various ways you can solve this, as we've looked at in other videos, but we're going to use the formulas that we did today.

**Dave Jones:** First of all, we work out the parallel resistance values. So, using our parallel resistance formula we saw earlier, we'll use the one over version instead of the other one.

**Dave Jones:** Then, we've got a 200 k invert plus 1 meg invert equals, and then invert all of that, 166.6 k. So, that's the bottom resistant. Now, we have to work out our voltage divider.

**Dave Jones:** It's 1 meg and 166.6k. So, remember our voltage divider formula? So, 166.6k / 1 I can add these up here 1.1666 meg like that * 10 Tada! 1.428 V so we measured it just a smidgen over 1.4 cuz the analog meter's not that precise.

**Dave Jones:** There you go. That's why we measured 1.4. Circuit loading of your test instrument. Classic trap for young players, especially in high impedance circuits. And you can actually use a second meter to measure the input impedance of our BM786 over here and you can see it's about 11.1 meg and that changes depending on the circuit design of the meter, but they're all, you know, roughly around that 10 11 meg value for

**Dave Jones:** a standard digital meter unless you've got a high input impedance meter which usually you'll only get that on like the millivolt the lower ranges like the millivolts and maybe if you're lucky in into the lower voltage ranges.

**Dave Jones:** So, there you go. As some homework, I want you to repeat that for 11.1 meg input impedance and of the BM786. I guarantee you'll work out roughly 4.78 V.

**Dave Jones:** So, there you have it. That's voltage dividers. I know this is normally like one page in a textbook. They'll just throw these formulas at you and that's it, but they're important to know cuz they use in practically every aspect of electronics.

**Dave Jones:** I guarantee there's a lot of stuff a lot of theory you learn in electronics that you may not touch for your entire career. In fact, probably like the majority of it you may not touch, but like voltage dividers they're absolutely everywhere.

**Dave Jones:** Yeah, just try and use your oscilloscope with your times 10 probe without knowing about voltage dividers. Anyway, hope you enjoyed that video and found it useful. If you did, please give it a big thumbs up.

**Dave Jones:** As always, discuss down below. Catch you next time.
