---
video_id: 7FYHt5XviKc
title: EEVblog #600 - OpAmps Tutorial - What is an Operational Amplifier?
url: https://www.youtube.com/watch?v=7FYHt5XviKc
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 27, "3": 40, "4": 59, "5": 73, "6": 89, "7": 99, "8": 108, "9": 121, "10": 136, "11": 149, "12": 160, "13": 177, "14": 186, "15": 204, "16": 218, "17": 227, "18": 241, "19": 255, "20": 268, "21": 278, "22": 291, "23": 303, "24": 315, "25": 330, "26": 356, "27": 370, "28": 386, "29": 405, "30": 421, "31": 434, "32": 449, "33": 467, "34": 484, "35": 497, "36": 517, "37": 532, "38": 548, "39": 570, "40": 589, "41": 606, "42": 621, "43": 636, "44": 646, "45": 655, "46": 669, "47": 682, "48": 697, "49": 710, "50": 724, "51": 735, "52": 749, "53": 778, "54": 795, "55": 814, "56": 827, "57": 836, "58": 858, "59": 871, "60": 882, "61": 893, "62": 904, "63": 918, "64": 932, "65": 941, "66": 965, "67": 979, "68": 993, "69": 1004, "70": 1020, "71": 1033, "72": 1044, "73": 1057, "74": 1074, "75": 1084, "76": 1096, "77": 1110, "78": 1129, "79": 1139, "80": 1150, "81": 1161, "82": 1175, "83": 1191, "84": 1203, "85": 1215, "86": 1227, "87": 1242, "88": 1257, "89": 1269, "90": 1278, "91": 1293, "92": 1313, "93": 1323, "94": 1340, "95": 1357, "96": 1375, "97": 1388, "98": 1409, "99": 1420, "100": 1434, "101": 1456, "102": 1467, "103": 1480, "104": 1491, "105": 1503, "106": 1515, "107": 1528, "108": 1543, "109": 1558, "110": 1573, "111": 1586, "112": 1603, "113": 1619, "114": 1638, "115": 1661, "116": 1676, "117": 1690, "118": 1706, "119": 1715, "120": 1732, "121": 1745, "122": 1761, "123": 1774, "124": 1786, "125": 1804, "126": 1816, "127": 1827, "128": 1837, "129": 1851, "130": 1869, "131": 1880, "132": 1891, "133": 1906, "134": 1919, "135": 1934, "136": 1953, "137": 1980, "138": 1991, "139": 2007, "140": 2016, "141": 2044, "142": 2069, "143": 2086, "144": 2100, "145": 2109, "146": 2129, "147": 2140, "148": 2157, "149": 2172, "150": 2184, "151": 2199, "152": 2216, "153": 2242, "154": 2254, "155": 2267, "156": 2278, "157": 2289, "158": 2304, "159": 2316, "160": 2326, "161": 2340, "162": 2353, "163": 2363, "164": 2378, "165": 2392, "166": 2402, "167": 2419, "168": 2432, "169": 2447, "170": 2460, "171": 2470, "172": 2480, "173": 2493, "174": 2506, "175": 2516, "176": 2536, "177": 2552, "178": 2562, "179": 2575, "180": 2585, "181": 2601, "182": 2612, "183": 2625, "184": 2647, "185": 2658, "186": 2668, "187": 2677, "188": 2696, "189": 2711, "190": 2738, "191": 2747, "192": 2758, "193": 2771, "194": 2788, "195": 2801, "196": 2817, "197": 2826, "198": 2839, "199": 2853, "200": 2868, "201": 2886, "202": 2894, "203": 2911, "204": 2923, "205": 2950}
---

**Dave Jones:** Hi, welcome to Fundamentals Friday. Today we're going to take a look at the operational amplifier or better known as the op-amp. Really important building block, absolutely essential that you understand how they work.

**Dave Jones:** Now, there are two ways to learn about op-amps. One is this way, the hard way. We don't want to do it that way. That sucks. So, let's get rid of this and let's do it the easy way.

**Dave Jones:** So, what is an op-amp or an operational amplifier? Well, the name operational amplifier comes from the fact that when they were first developed, they were developed to do mathematical operations, hence the name operational amplifier.

**Dave Jones:** And back then we didn't have digital computers. They did they used these for analog computers. So, analog mathematical operations, addition, subtraction, integration, differentiation, stuff like that. Even that real hard calculus stuff, op-amps could actually do these operations in hardware.

**Dave Jones:** Now, this digital software, right? So, that's where they came from. So, although we don't have analog computers today, we still use them for those mathematical operations. You can turn an op-amp into an integrator, for example.

**Dave Jones:** You can turn it into a summer, which is just an adder, and things like that. So, they're really useful circuit building blocks. But, the main thing we're going to look at is the operational amplifier as an actual amplifier cuz that's what they're most commonly used for and probably what you'll mostly use them for as well.

**Dave Jones:** So, an op-amp is essentially just an amplifier. Yes, it can be used for those mathematical operations, but essentially what it comes down to is this is a differential amplifier.

**Dave Jones:** And what that means is that it's got two inputs over here, which we'll talk about, and an output, and it's got some gain in there because amplifiers have a gain.

**Dave Jones:** And what it does is it takes the difference between these two input signals, amplifies it by its internal gain, or what's called open loop gain, and gives you an output voltage.

**Dave Jones:** But, op-amps really can't be used as differential amplifiers on their own, even though that's what they are. Rather confusing, but an important aspect you should understand. So, why can't this be used as just a differential amplifier?

**Dave Jones:** Input signal here, output signal with some gain in there? Well, the answer is they're not designed to be used as differential amplifiers, as strange as that may seem, because they are essentially differential amplifiers.

**Dave Jones:** That was That was that hard circuit you saw over here before was actually the internal circuitry of an op-amp, showing it as a differential amplifier. But, hey, let's forget about differential amplifiers.

**Dave Jones:** I shouldn't even mention it. But, it is important to understand the operation of how an op-amp actually works. Now, the reason they don't work as differential amplifiers because the op-amp The gain of the natural gain, the internal natural gain of the op-amp, is enormous.

**Dave Jones:** And that's the first thing you need to know about op-amps. Is it's almost not quite infinite, but you can think of it as infinitely large. It's like millions of times.

**Dave Jones:** And, well, the data sheet won't even tell you. So, if we just tried to use an op-amp like this with no external circuitry and just fed, you know, like 1 mV on the input here, the gain is so large that the output voltage is going to be so huge that it's just not a practical device at all.

**Dave Jones:** So, that's why you never see an op-amp without any external circuitry, or what's called negative feedback. So, that brings us to our first practical application for the op-amp, which is a comparator.

**Dave Jones:** But, before we look at that, we will look at the symbol here. Now, an op-amp is typically drawn as a triangle like this. It's got two inputs over here, and one input here.

**Dave Jones:** Sometimes it might be flipped, depending on uh the ease of uh drawing your circuit and the way the signal flows, but it's exactly the same thing. Now, these two inputs here, one is the positive input is called the non-inverting input.

**Dave Jones:** Easy to remember because it's positive. The inverting input is likewise easy to remember cuz it's negative. Negative inverts something. So, that's the terminology you should be using when referring to op-amps.

**Dave Jones:** Very important to get the terminology right, otherwise you sound like a bit of a dill. Now, there's an output pin here, easy, and there's two power supply pins, a positive and a negative one, which we'll talk about as well.

**Dave Jones:** So, I mentioned that the gain of an op-amp naturally inside is designed to be enormous, almost infinite. So, what happens if you just feed voltage on the input here?

**Dave Jones:** Well, let's assume that we have 1 V on our non-inverting input here, and we have 1.01 V or slightly above 10 mV or even 1 mV above this one here.

**Dave Jones:** Well, the amplifier will actually amplify the difference or attempt to amplify the difference between these two inputs. So, the output here will be this huge gain, like a million times, that one millivolt.

**Dave Jones:** So, it'll try and output hundreds and hundreds or thousands of volts, and well, it can't do it because well, your circuit's only, you know, 5, 10, 15 V, something like that.

**Dave Jones:** So, your output is going to saturate. So, if you've got 1 V here, and let's say 1.001 V here, then your output is going to go boom, right up to V+.

**Dave Jones:** It's just going to saturate right up at the positive voltage. So, we've got ourselves a comparator. And likewise, if you sweep switch those voltages around so that the non-inverting input is bigger than the inverting input, even by a tiny amount, bingo, your output is then going to go from positive and it's going to slam right down to the negative rail down here.

**Dave Jones:** So, you can see that it's just used as a comparator. It's a going to be a very crude comparator and you can use an op-amp as a comparator in a pinch, but they aren't quite as good as a proper comparator that you can actually buy.

**Dave Jones:** They're designed to be comparators, but hey, you can actually use op-amps as comparators, but that's what happens if you connect an op-amp with no feedback at all and what that's called is the open-loop configuration cuz there is no loop.

**Dave Jones:** There's no loop. The loop is open and we'll close the loop in a minute, but with an open-loop configuration like that, an op-amp is just a comparator. So, now that we got that little non sequitur out of the way, the the oddball configuration of the comparator for the op-amp, let's have a look at what where op-amps come really useful.

**Dave Jones:** And that's as proper amplifiers. Now, to do that, as I said, we need to go from the open-loop configuration with no feedback to add in what's called negative feedback and hence the t-shirt, negative feedback.

**Dave Jones:** And once you do that, op-amps become incredibly useful and powerful devices. Now, there are two rules with op-amps. That's all you have to remember. It's fantastic. This is how easy op-amps are.

**Dave Jones:** If you know these two rules, if you remember these two rules, you can analyze practically any op-amp circuit. You can't get into the real nitty-gritty details of the performance of it perhaps, but you can look at a schematic and you can understand how it works.

**Dave Jones:** And the two rules are very simple. Rule number one, no current flows in or out of these inputs. So, there's nothing flowing in or out of these two input pins ever.

**Dave Jones:** That's it. Nothing. Nothing flows in or out regardless of how you connect the circuit up whether it was the open loop comparator configuration we saw before or whether or not it's a closed loop configuration and inverting or non-inverting amplifier as we're going to look at.

**Dave Jones:** Nothing flows in or out. Rule number two. Now, this rule only applies when you have a closed loop like this. It doesn't apply at all to the open loop one we just saw with the comparator.

**Dave Jones:** That's why I did the comparator first even though it might have been a little bit confusing to start that way. Most people start op-amp explanations with these two rules, but I wanted to show you that comparator first because to highlight that rule number two it does not apply or only applies to closed loop configurations with negative feedback.

**Dave Jones:** Now, rule number two is the op-amp does whatever it can internally, right? Internal circuitry which we're not going to into, but it does whatever it can to keep these two input voltages the same.

**Dave Jones:** Now, the op-amp can't actually change its input voltage. It has These are inputs. It has no way to actually drive a voltage out and keep them the same, but it can do it with feedback and that's why this rule only applies to closed loop configurations.

**Dave Jones:** So, the op-amp only has control over its output, but if you have feedback, it will change this output voltage to make sure this input equals this input here. And that's a very powerful rule of op-amps and if you see a closed loop configuration like this, you can be pretty sure that rule is going to apply.

**Dave Jones:** So, using these two rules, let's look at the simplest config op-amp configuration possible and it's not this, it actually has no external components. So, what it has is the output tied back to the inverting input like this, and you feed your signal or your voltage into the non-inverting positive input like that.

**Dave Jones:** And this is called an op-amp buffer. So, using our two rules, very easy to analyze this op-amp buffer circuit. Let's say we Let's just do DC because op-amps The other thing is op-amps are DC-coupled amplifiers.

**Dave Jones:** They can amplify DC as well as AC signals, very important property. So, but let's do the DC case. We're feeding 1 V into our non-inverting input here. What do we get on the output of our op-amp?

**Dave Jones:** Well, look, rule number two always applies when you're when you've got feedback in a circuit in in op-amp circuit. The op-amp tries to keep these two input voltages identical.

**Dave Jones:** So, because of the rule, this inverting input here is going to be equal to this pin up here. The op-amp will ensure that by driving this output to get this input to match this one.

**Dave Jones:** So, if we've got 1 V here, then we've got 1 V here, and because it's just connected by a bit of wire, we're going to get 1 V out here.

**Dave Jones:** That's why it's called a buffer. It's not an amplifier it because there is no gain. 1 V in, 1 V out. -1 V in, -1 V out. Whatever the voltage is within within the limits of the power supply voltages here.

**Dave Jones:** What use is that? Well, rule number one, no current flows in or out of the inputs. So, nothing no current flows in. So, if you've got a load over here, I don't know, it could be some sort of sensor or whatever.

**Dave Jones:** It could be a low-pass filter, for example, like you're feeding a pulse-width modulated signal from your microcontroller or something like that, and then you want to buffer that voltage off there.

**Dave Jones:** Because no current flows into the input, this op amp does not disturb your sensor or your circuit that you're actually trying to do. It's a what's called a very high impedance input, essentially open circuit.

**Dave Jones:** So, it doesn't disturb anything you hook up to it. But, the op amp has a what's called a low impedance output. So, it can drive a reasonable amount of current, you know, milliamps, tens of milliamps, that sort of thing.

**Dave Jones:** Some can go as high as a couple of hundred milliamps for your power op amps, but it can drive a reasonable amount of current. So, that's why it's buffering the signal, a high impedance signal, and giving you a low impedance output.

**Dave Jones:** Just allows you to drive things with a sensitive input like that. Pretty easy, very useful configuration, the op amp buffer. Now, the next configuration we're going to take a look at is what's called the non-inverting amplifier.

**Dave Jones:** And this is where we tame our op amp beast, that huge unwieldy gain that changes everywhere with temperature and ah, it's horrible. Anyway, it's got this massive unusable gain in there as a differential amplifier, but as a single-ended amplifier, that's what single-ended means, you feed the input here, and it's always referenced to ground, we can use this as a single-ended amplifier, and we can tame that gain by

**Dave Jones:** adding negative feedback on it. And I won't explain negative and positive feedback and the mechanisms and how it works, because, well, that's for a more advanced topic. But anyway, we feed in a feedback resistor here, just like we did before, it was shorted out, but we put a resistor in there, and we put a resistor back down to ground.

**Dave Jones:** So, what it's doing now is this input, the inverting input, is taking a small portion, our this feedback resistor, we'll call RF, is always bigger than R1 here. So, we fit So, we've just got a voltage divider here that feeds back a smaller part of the input.

**Dave Jones:** And that's essentially what negative feedback is. You're taking a part of the output and you're feeding it back to the input. And there's a very simple formula you need to remember for this non-inverting amplifier configuration.

**Dave Jones:** And I won't try and derive it, but the gain of this amplifier, or what's called AV, that's the actual terminology used. AV is just gain. You can use gain.

**Dave Jones:** Gain equals RF, the feedback resistor, divided by R1, which goes down to ground here, plus one. You've got to add that plus one on there. So, easy. If we've got a 9K feedback resistor and a 1K resistor down to ground here, our gain is 9K on 1K, or nine, plus one, our gain is equal to 10.

**Dave Jones:** So, if we feed 1 V into the input here, we'll get 10 V on the output. Easy. And because we've got positive and negative rails, which we'll get into, we can feed AC or DC signals into here about ground.

**Dave Jones:** And so, we can feed negative 1 V into here and we'll get negative 10 V out. So, there you go. That is the basic configuration of a non-inverting amplifier.

**Dave Jones:** And you might see weird configurations. There might be a capacitor across here or something like that, which we won't get into in this one, but you know, the configuration is the same.

**Dave Jones:** If you see your input being fed into the non-inverting input and the feedback going back to the inverting input, you know that's a non-inverting amplifier. And this formula here applies.

**Dave Jones:** And from this formula, you can also see why our buffer amplifier had a gain of one before, because our feedback resistor is zero, was zero ohms. So, zero on R1 here, which was infinite.

**Dave Jones:** So, zero on over infinity, or a very large value is zero plus one. So, our gain is one. That's why our buffer had a gain of one. Easy. The math doesn't lie.

**Dave Jones:** So, now we get on to the second of our two major configurations. We've already looked at the first one, which was the non-inverting amplifier. The buffer was just a variation of that.

**Dave Jones:** Now, we have, instead of the non-inverting amplifier, we have the inverting amplifier. How can you tell it's an inverting amplifier? Well, just like before we could tell it was a non-inverting one by the signal going into the positive input, here the non-inverting input, hence the name non-inverting amplifier, our signal now goes into our inverting amplifier pin.

**Dave Jones:** So, hence it's called an inverting amplifier. And you'll notice that I've switched the two symbols around here. The positive is now on the bottom. Our op-amp hasn't changed. I've just done that visually to you know, to make it a bit easier here.

**Dave Jones:** And that's what you'll commonly find in schematics and CAD packages and all sorts of stuff. You might find them flipped around, upside down, back to front, whoop-de-do, all going all around the place, some pointing down for various feedback paths and all sorts of things.

**Dave Jones:** It's exactly the same op-amp. It's just visually different. You can draw it any way you will not want. Now, our inverting amplifier that this one is, we have the same as before.

**Dave Jones:** We have our feedback resistor. We have our negative feedback going to in this case our inverting amplifier pin instead of our non-inverting one. So, now we feeding our input into through the resistor here.

**Dave Jones:** So, it's a different configuration. Our signal is not going directly into the non-inverting pin. And this brings up our next really important concept with op-amps that you really need to understand.

**Dave Jones:** And here's where rule number one really comes into play in trying to analyze this thing. It's called virtual ground. Stick with me. So, once again, how do we analyze this?

**Dave Jones:** Always go back to your two rules. What's our second rule here? The op-amp tries to keep the input voltages the same. In fact, it will if you've got this non-inverting configuration and you haven't hit the rails yet.

**Dave Jones:** So, if the amplifier's working normally and within normal bounds of your power supply rail, these two inputs will always be the same. So, we're actually connected our non-inverting input down to ground here.

**Dave Jones:** It's connected to ground. We're forced to the ground. It's never going to change. So, what is the inverting input here going to do? Well, of course, rule number two, it's going to be identical.

**Dave Jones:** It's going to be the same. So, this point is also going to be ground or 0 V. So, this seems like almost like a pointless circuit cuz look at rule number one, no current flows in or out.

**Dave Jones:** So, there's no current flowing in or out of that pin and it's ground. We've got both pins grounded and no current flows in or out. It's almost as what's the point of having an op-amp?

**Dave Jones:** It's very confusing concept, but once you grasp it, you go, "That's easy." And it's quite brilliant. So, the op-amp, remember, does whatever it needs to on the output, drives it to whatever voltage, positive or negative, in order to make sure that this inverting pin here is equal to the non-inverting pin down here.

**Dave Jones:** Makes them the same. We've forced this pin, so it can't change this pin. All it can do is change the voltage via the nature of the feedback resistor here to make this zero.

**Dave Jones:** And trust me, we'll do a practical measurement of this in a minute and this node here will actually be 0 V. This confuses the heck out of a lot of beginners.

**Dave Jones:** They build up their op-amp circuit. They start probing around, and they've got their input signal here. You know, it's a 1 kHz 1 V sine wave, for example. And let's say they measure this side of the resistor, and the signal's there.

**Dave Jones:** They measure this side of the resistor, and it's ground. The signal's vanished. Where's it gone? Strange, but true. So, let's follow this through and use our rules and see if we can analyze this circuit.

**Dave Jones:** Once again, the DC case to make it make it easy. We've got 1 V on the input here, positive 1 V with respect to ground, of course. Now, we've said before that trust me, we'll measure it later, but this pin is going to be ground.

**Dave Jones:** It is going to be 0 V there, always. So, all we've got is 1 V across our R1 here, which is 1 K. So, we're going to have 1 mA flowing through there.

**Dave Jones:** Where does it flow? Well, it doesn't flow down here to ground. How can it? Because no current, rule number one, no current flows into or out of the input pins.

**Dave Jones:** So, it can't flow through to ground here. It has to flow, it's going through here, it's going somewhere. There's 1 V across that 1 K resistor. Ohm's law always it must be obeyed.

**Dave Jones:** So, that current is flowing. Trust me. It can't flow into the input pin. We we know it's high impedance, so it must be flowing up here like this, through this 10 K resistor, and it's being sourced from the output.

**Dave Jones:** Remember, this op-amp has internal circuitry. It's got an output buffer, so it can actually drive currents into and out of the various supplies back into there. And that is where it's sinking the current to.

**Dave Jones:** And that's the sneaky part about this. Our current has now been forced up this node here and is flowing through, in this case our feedback resistor RF, which is 10K.

**Dave Jones:** I've made it 10 times larger, you'll see why in a minute. Then, it's it must be flowing through there, so we must have a voltage drop across that resistor.

**Dave Jones:** Once again, Ohm's law always must be obeyed. So, if we've got that 1 mA flowing through our 10K there, we're going to have 10 V drop across this resistor with positive here and negative here.

**Dave Jones:** Aha, negative. This is These voltages are with respect to the ground here. Now, here's where it gets a little bit tricky. This positive voltage here, it's we are going to get the plus 10 V across that resistor there, but because this pin is positive, but we're forced we know this pin is zero.

**Dave Jones:** Okay? We know it's zero because we're forced it by way of the op-amp action and rule number two here in what's called a virtual ground, which I talk about in a minute.

**Dave Jones:** Then, we have That means if this is ground, this is positive, then we've got minus 10 V coming out of here. Bingo. There's our inverting amplifier. 1 V in, minus 10 V out.

**Dave Jones:** So, our gain, our formula, AV gain equals RF on R1. There is no plus one with the inverting amplifier. The plus one only applies to the other non-inverting configuration.

**Dave Jones:** So, by way of op-amp action, we'll call it, and negative feedback here, this point, this node here at the non- at the inverting pin, is what's called a virtual ground because typically in this configuration, it is actually grounded because we've grounded this pin.

**Dave Jones:** Doesn't have to be. We can feed other voltages into with pin and offset and do all sorts of other stuff, but it's still called even if you do feed another pin in here, it's still called virtual ground because it's virtual.

**Dave Jones:** It's not real. It's not hard tied. If it was hard tied to ground, if we actually tied that pin to ground, this thing wouldn't work because all of our current would flow through here like through this resistor down to ground and around like that and then this output here, well, it wouldn't know what to do.

**Dave Jones:** The output would be zero because there'd be zero volts difference in here. Remember, it's still a differential amplifier as such. So, we've got zero volts difference here. We're going to get zero out.

**Dave Jones:** We'd have no current flowing through here and we'd have zero volts out. So, you can see that it doesn't work unless if you tied that hard ground, but when it becomes a virtual ground by nature of the op amp action, it all magically works.

**Dave Jones:** I hope that makes sense cuz once you get it, it's really easy. So, functionality-wise, it's pretty much exactly like the non-inverting amplifier except it inverts and that's it and the gain formula is slightly different, but apart from that, pretty much works exactly the same, but that magic virtual ground is at play in this configuration.

**Dave Jones:** And of course, as with op amps, they're DC coupled, so it works with DC signals. You can just feed in a fixed DC voltage. As I said, 1 volt DC in would give minus 10 volts out in this case with these value resistors.

**Dave Jones:** Or, we can feed in a 1 volt peak to peak or RMS sine wave, for example, about ground, so it's centered on ground like this. This is the blue waveform here.

**Dave Jones:** Let's just say that's 1 volt. It's not quite to scale, but you'll get the idea. And then our output will be the inverse of that. So, when the input rises, the output goes negative because it's an inverting amplifier.

**Dave Jones:** Now, of course, one of the disadvantages of the inverting amplifier compared to the non-inverting we saw before is that as you can see there is input current coming from your load here.

**Dave Jones:** So, you don't want to use this where you have a high impedance load because then it can change the gain equation and mess everything up. That's where you want a non-inverting amplifier or at least a buffer.

**Dave Jones:** Some people will actually follow will put a buffer on the input here and then drive the inverting amplifier, but usually in that sort of case you'd probably use a non-inverting amplifier.

**Dave Jones:** Now, we have to go deeper into this and talk about the power supplies and split rails and all this sort of stuff and single supply op-amps. I'll try and keep it as brief as possible, but you saw in this configuration the op-amp only has two power pins, okay?

**Dave Jones:** It's usually called V+ and V-. Now, V- you can actually connect that to ground. There is nothing, regardless of what the data sheets tell you, there's nothing inherent in op-amps that make them really a single supply op-amp.

**Dave Jones:** So, you can take an op-amp that has V+ and V- and connect this down to ground like that. There's nothing to stop you as long as you meet the minimum voltage specification and don't exceed the maximum, etc.

**Dave Jones:** So, what happens if we did that in this case? Our input is all our non-inverting input is also grounded here. Well, now it becomes a problem. You get into the practical limitations of op-amps.

**Dave Jones:** We've been talking about what's called an ideal op-amp up until this point. These rules here aren't strictly true. I lied. But they're still a fantastic way, even professionals use to analyze these circuits as a first order as a first pass.

**Dave Jones:** No current flows in or out. Well, if you've been watching my videos you'll know I've done a previous video on this talking about input bias current. So, little itty-bitty, teeny-weeny currents can flow into and out of these pins depending on what type of op-amp you're actually got.

**Dave Jones:** And that's a real practical uh limitation of these things. And the other one is that I've talked about in previous video, which I'll link in down below if you haven't seen it, the inputs cannot necessarily go right to the rails, be it uh whether it's positive, negative, reference to ground, or whatever.

**Dave Jones:** So, you can get uh what's called a rail-to-rail op-amps or rail-to-rail input op-amps. In this case, if you had a rail-to-rail input op-amp, then yeah, you might be able to get away with this and have the uh invert and have the uh non-inverting input tied down to ground like this, but hang on.

**Dave Jones:** What's the point of that? If you've only got ground, this is an inverting amplifier. It inverts your signal. So, if you feed 1 V in, you're going to try and the op-amp is going to try and give you 1 or -10 V out.

**Dave Jones:** But how does it do that when your supply is negative like that? It doesn't work. So, you have to um it's got no room to do it. So, your op-amp has to always be powered in the configuration that you expect your input signals to be referenced to.

**Dave Jones:** So, if we were to use uh the inverting op-amp configuration like this with a single supply rail like this, and we wanted to amplify AC signals, well, the signals can't go negative like this.

**Dave Jones:** They can go negative on the input, but you're never going to get that negative voltage on the output. But you still want to amplify your signal clearly like this.

**Dave Jones:** Well, what we need to do is the zero point needs to go right down the bottom here like this. So, we need to offset. So, if that's 0 V, we need to offset our input wave our input and output reference by a certain amount of voltage.

**Dave Jones:** How much? Well, typically half of your supply rail to maximize your headroom. How do we do that? I hinted at it before. You feed in if this is V plus, you would go V plus on two.

**Dave Jones:** You would feed that voltage half rail in there. You'd usually do that simply by putting a resistor like that going to V plus and a resistor down there going down to ground and bingo, voltage divider, there's your half rail.

**Dave Jones:** So, we're offsetting our voltage here our virtual ground. Remember, this is still called a virtual ground even though it's not going to be. So, the voltage here is going to be equal to the voltage here due to our second op amp rule.

**Dave Jones:** So, if our power supply is 20 V, for example, this point here would be half that if we make these, you know, exactly the same value, of course. Make them the same value, half rail.

**Dave Jones:** So, we're going to have an offset voltage here at this point and that shifts our waveform up and we'll see that in the practical experiments to follow. Now, as I said sometime back, you might see some other components around here like some capacitors and things like that around the circuit.

**Dave Jones:** That is to change the bandwidth of the circuit effectively. Um because we're not going to go into it. I'll have to do a second part to this video that goes into op amp bandwidth and things like that.

**Dave Jones:** I have done one on cascading op amp bandwidth which I'll link in down below. But, for suffice it to say that an ideal op amp that we've been looking at has an infinite bandwidth.

**Dave Jones:** That's infinite frequencies and signals, but in practice, no, of course not. Your practical op amp might have a 1 MHz bandwidth or a 100 kHz bandwidth or something like that.

**Dave Jones:** You know, it could be a nice fast 100 MHz, but it's always going to have a bandwidth which changes with your gain or gain bandwidth product. And I've done a separate video, I'll link it in, but sometimes you might see a little bypass cap in there.

**Dave Jones:** It might be, you know, 10 puff or 100 puff or something like that. And that's just rolling off the frequency response of that. And likewise, you might see a little cap across something like this, for example, if you have if you are offsetting this thing using a single supply like this.

**Dave Jones:** You know, I I won't go into the details, but basically any noise on this point here will be amplified and picked up on that virtual ground, so you'll get noise on your output signal.

**Dave Jones:** So, you might stick a big ass, you know, 1 or 10 microfarad cap across here, for example, and really make that virtual ground really noise-free. But, hey, that's that's beyond the basics.

**Dave Jones:** One little mistake I noticed, oops, my formula here for the inverting amplifier, it needs a negative in front of it because the gain is actually negative. So, it's So, the gain is not in this case is not 10k is not 10, it's minus 10.

**Dave Jones:** Oops. So, just back to this voltage rail thing briefly because it is something that is rather confusing because there is no ground pin on an op amp. There's only the positive and negative.

**Dave Jones:** So, well, where does your reference go? Well, the reference is part of the external circuit. In this case, back to our non-inverting amplifier configuration, here is our ground reference here, and then our positive and negative supply is here like this.

**Dave Jones:** So, plus 15 volts and minus 15 volts. If we want to feed in a signal that goes both positive and negative. If we're only feeding in a signal that is positive, above ground, then this here could be tied down to here like this, and then it has to be above that.

**Dave Jones:** The output cannot magically go negative. It can only go negative to your ground reference if you have that minus 15 volt rail in there. Clear as mud? And just like the inverting configuration, if we wanted to power this from a split supply, we could have this grounded like this and then we can add a bias voltage in here like this to actually offset the voltage.

**Dave Jones:** And then you can get into all sorts of weird and wonderful things with AC coupling these amplifiers. All of the op-amp configurations we've looked at have been DC coupled, but you can actually AC couple them.

**Dave Jones:** So, that's why you start might seeing capacitors on the inputs and outputs to the op-amps. Now, here's a tricky configuration which I'll briefly touch on that combines the two different configurations we've seen before and a couple of the things we've looked at.

**Dave Jones:** It's the differential amplifier. You know how I said op-amps are essentially a differential amplifier? That's how they work, but they have to but they do that in the open-loop configuration.

**Dave Jones:** So, they're hopeless. They're useless for that. But, if you combine the the inverting amplifier configuration that we just saw, so we've got the feedback going here, our signal going in, that's a standard inverting configuration, and we have exactly those two resistors that we saw before to bias that voltage up, but instead of going to the supply rail, we make that our other differential input.

**Dave Jones:** And bingo, it becomes a differential amplifier. I'll let you go through the actual calculation yourself to find out, but basically, the difference that we feed in in if we're feeding in 1 V into here and 1.1 V into here, we have a difference of 0.1 V, and the gain of this amplifier, exactly like the inverting configuration, -R2 on R1, we used RF before, I'll call it R2 here.

**Dave Jones:** So, R2 on R1, 10 K on 1 K, we have a gain and you got to add negative in there so it's a gain of minus 10. But because our bias voltage is not fixed, it's actually the differential input signal, aha, look what happens.

**Dave Jones:** We've got 1 volt here, we've got our divider here, R1, these two values are the same. R1 is equal to R1 here, R2 is equal to R2 here. They must match precisely to get good common mode rejection ratio, which we won't go into.

**Dave Jones:** But suffice it to say if we've got 1 volt on this point here relative to ground, we'll have 0.9090909 repeater at that point there and that becomes our virtual ground.

**Dave Jones:** Bingo, we'll have that same voltage there and then we'll have our 1.1 volts here. That has X and then you subtract uh that from that that and you get X amount of current flowing through here, which then must flow through the 10K which has 1.0909 voltage across it, subtract the difference there.

**Dave Jones:** It's exactly the same configuration as before with the bias voltage, but then we're left with an output voltage of minus one. So we've amplified the difference in our input signal by the gain here, 10.

**Dave Jones:** It's not a terrific differential amplifier, but it works. So we've tamed our op amp that is a differential amplifier anyway, but pretty unusable, we've actually made it into a pretty usable differential amplifier.

**Dave Jones:** Beauty. Just combines both those techniques and there's lots of tricky stuff like this you can do with op amps. And just briefly, another one of these tricky configurations goes back to the name, the operational amplifier, and one of those mathematical operations, the integrator.

**Dave Jones:** We won't go into integrals and all that sort of stuff, but what we can do, a basic inverting configuration here, except instead of a feedback resistor, we have a feedback capacitor.

**Dave Jones:** What does that do? Well, our standard input voltage here, following the rule, no current flows in, but we have a virtual ground, of course, rule number two. So, if that's 1K and that's 1 V there, well, we have 1 mA flowing through that resistor.

**Dave Jones:** Where does it flow? Can't flow into the op-amp. It's got to flow up here and through the capacitor. So, you've got, effectively, a constant current of 1 mA. You've just made This is now a constant current flowing this through this resistor.

**Dave Jones:** And when you have a constant current flowing through a capacitor, you end up with a Well, in this case, it's going to ramp negative down like that. If our input go If our input is a step and it goes up like that, the constant current, because it takes time to charge a capacitor, the voltage on the capacitor will increase like that.

**Dave Jones:** I say increase cuz it's an inverting amplifier. So, it's just going to go negative, but that's what it does. And that's an integrator, and that is actually a mathematical integral of your input signal.

**Dave Jones:** Anyway, that's way too much theory, more than I wanted to do and longer than I wanted to take, actually. But, suffice it to remember that these two rules of op-amps allow you to analyze practically any configuration.

**Dave Jones:** And as a bit of homework, I go recommend you look at the summing op-amp configuration, the summing amplifier, and figure out how it works, because you're going to be using those two rules to figure it out.

**Dave Jones:** So, I'll leave that one up to you. But, enough of that, let's head on over to the bench here and see if we can measure some stuff, make sure I wasn't bullshitting in you about this virtual ground stuff.

**Dave Jones:** Let's check it out. Sounds a bit sus. See if it really works. All right, we're at the breadboard. Let's take a look at an inverting amplifier here, because I wanted to show you that virtual ground point there, just to show you that there really is no signal there.

**Dave Jones:** It actually vanishes in quote marks when you go from the input here to here, and then it magically reappears at the output, cuz that's how an op amp works, as I've explained.

**Dave Jones:** Anyway, got a jelly bean LM358 here. It's actually a dual op amp, so we've just uh tied off the uh terminated the top op amp here. I could probably do a separate video on that on how to properly terminate uh op amps.

**Dave Jones:** That might make an interesting video. Um thumbs up if you want to see that one. Anyway, here we go. I've got it configured. I've got a uh 10K input resistor here, 100K feedback, so we've got a gain of 10.

**Dave Jones:** The formula, of course, is the feedback resistor on that one. Bingo. Easy. Times 10. So, I'm going to feed uh 2 V peak-to-peak input here. We should get uh 20 V peak-to-peak on the output.

**Dave Jones:** So, we're using pretty much near the maximum supply rail of the LM358. In this case, I'm powering it from plus minus 15 V. So, we have a split supply.

**Dave Jones:** So, our ground reference, our input signal, is referenced to ground. I should actually draw that on there. There we go. That's clearer. So, our input is referenced to ground, and our non-inverting input here is referenced to ground, and our output is referenced to ground also.

**Dave Jones:** But, for signals to go negative, uh for output signals to go negative, we need a negative rail on here. So, we're using minus 15 V. So, plus 15 to power it, minus 15 as well.

**Dave Jones:** So, 30 V total supply on there allows us to go positive and negative signals input and output. So, let's go over to our power supply. Here it is. Plus minus 15 V.

**Dave Jones:** I've got uh dual tracking on there, and you notice that I've joined the um uh supplies here, generating the split supply. So, this one actually becomes the negative. So, this is our positive 15 from here to here, and this is our negative 15 relative to here, because we've strapped the positive one over and tada, there we go.

**Dave Jones:** We're feeding in our one We've just got a 1 kHz low frequency signal, 2 V peak-to-peak here on the input and you can see our input and output waveforms.

**Dave Jones:** And these inputs are of course all AC coupled and they're bandwidth limited as well to 20 MHz to reduce the noise and we're using our high resolution mode as well so we get some boxcar in there and that's why we've got a nice nice crisp waveform like that.

**Dave Jones:** Beautiful. So what happens if we turn our bandwidths back to full? In this case it's my 1 GHz Tektronix 3000 series and we turn off high res mode, go back to sample mode.

**Dave Jones:** There we go. We get our nice fuzzy waveforms because we've got that massively high bandwidth. That's the advantage. You can go into averaging of course but high res mode does boxcar averaging.

**Dave Jones:** Just cleans it up. Of course you can do envelope mode. Look at that. Pretty horrible waveform. So when looking at this sort of stuff you definitely don't want to use your regular mode.

**Dave Jones:** You want high res mode if you've got it. There you go. We're getting exactly what we expect. Look at that. 2 V peak-to-peak in, roughly 20 V out. There's probably going to be some error due to the resistors in here.

**Dave Jones:** Anyway, we're getting our times 10 and of course the blue the blue waveform there is the input. That's 500 mV per division so we're getting our 2 V peak-to-peak and our output is 5 V per division so which is the yellow waveform there.

**Dave Jones:** And look at that. And of course because it's an inverting amplifier, the output is exactly 180° out of phase. It's inverted. So at the moment I'm probing the input and the output.

**Dave Jones:** Now you want to see the virtual ground, didn't you? What happens if I move my input probe, the blue waveform here from the input over to this? You'd expect to see the signal but as I've told you and as you should trust me, let's move the probe over.

**Dave Jones:** That is our virtual ground point. Look. Flat as a tack. The signal has vanished. Magic. But, of course, you know it's not magic. It's just standard op-amp behavior with virtual ground on the input.

**Dave Jones:** That's how an op-amp works. And no, the current hasn't magically vanished. The current is going through the resistor. Ohm's law still holds. Current is changing because we've got an AC resistor here.

**Dave Jones:** There's AC current flowing through this resistor, and it's all flowing up here. But, this point, by nature of the op-amp action and the negative feedback, that is a virtual ground.

**Dave Jones:** Our op-amp rule number two there. Inputs are the same. The op-amp changes the output here in order to ensure that that point is equal to that input there. Easy.

**Dave Jones:** And that's why we don't see any signal on there. So, trap for young players. When you're probing around circuits like this, don't think the signal's vanished. Virtual ground. Remember your op-amp rules, always.

**Dave Jones:** Now, I actually chose the LM358 for a reason, because it is not like a regular op-amp and not quite like a rail-to-rail op-amp. It's sort of halfway in between.

**Dave Jones:** Check it out. Here we go. It It eliminates the need for dual supplies, okay? You can use it as a single supply op-amp. But, as I said, you can use any op-amp as a single supply op-amp.

**Dave Jones:** But, this one is extra special in that it allows direct sensing near ground. So, and Vout also goes to ground. So, effectively, it's it's not rail-to-rail. It won't go up to the all the way to the positive rail on the input and output, but it will go down to ground or the negative or well, because an op-amp doesn't have a ground pin.

**Dave Jones:** it's the negative rail. So, even if we power it from split supplies plus minus 15 like we are now, it'll still go down to that minus 15 volt pin or that pin four.

**Dave Jones:** It'll go down, the input will this input here will allow to sense all the way down to the negative rail and also the output will go all the way down to the negative rail.

**Dave Jones:** And I'll demonstrate. But what we've got to look at here is a couple of things on the data sheet. Our input common mode range and our voltage range here.

**Dave Jones:** As we said, it goes all the way down to that negative pin or zero volts as they're calling it here. But on the positive side, this op amp will not go uh sense or go to the output less than 1.5 volts below or above 1.5 volts below the positive rail V plus there.

**Dave Jones:** So, if we've got an output signal of 10 volts for example, the voltage range says if we want to output voltage of 10 volts peak, well, we need a V plus rail of at least 1 and 1/2 volts above that.

**Dave Jones:** So, 11.5 volts. So, what we're going to do is lower the voltages here on these rails. We're going to lower V plus from 15 volts down to 11.5 and around about that 11.5 volts because we're getting 10 volts peak on the output 20 volts peak to peak 10 volts peak, we should start seeing distortion or clipping of our waveform at around about 11 and 1/2 volts.

**Dave Jones:** Let's see if we do. Okay, so here we go. We're 15 volts. I'm going to drop it down by 0.1 volts at a time. Notice that it's split supply, it's dual tracking.

**Dave Jones:** So, our waveform is still looking good. Still looking good, but we expect it to start clipping around about 11 and 1/2. It may not be precise. This is not an exact value on the data sheet, but there we go.

**Dave Jones:** 11 and 1/2 it's still there. Still there. There we go. It's starting to clip. It's starting to clip. You can see it. It's actually about 11.2 volts there, but you can start to see that waveform flatten out.

**Dave Jones:** Now, I'll wind it down even more because this is a not a symmetrical supply op-amp. It actually goes down to zero. We don't start seeing clipping on the bottom here on the bottom rail until a significant time after that.

**Dave Jones:** Now, we're getting both, but I wind it back up there, and that's about 11.1 volts, but we're seeing that clipping on the top, and we won't see it on the bottom for time after.

**Dave Jones:** So, there you go. Just be aware of that. And if we had a a even a worse op-amp in this respect, like a LM741 or something like that that can't even go down to the negative rail, we would start to see these rails clip right roughly at the same time.

**Dave Jones:** And you remember that open-loop gain I was telling you about? How large is it? Well, it tells you a couple of ways in the data sheet. Not all data sheets will have it, but this one does.

**Dave Jones:** Large DC voltage gain. So, it doesn't say it's open-loop gain, but that is effectively the DC voltage gain is the gain of the the inherent differential amplifier in there, and they put it in DB.

**Dave Jones:** So, you use your 20 log formula, you reverse that, and you get about 100,000. And likewise here on the data sheet, they've got another way to tell you. It's called Now, it's called something different.

**Dave Jones:** It's got the large signal voltage gain there. It's specified for a certain rail, but there we go. Typically, 100, and they specify it in volts per millivolt. So, if if you uh divide 100 volts by 1 millivolt, what do you get?

**Dave Jones:** Same figure, 100,000. There's your open-loop gain. So, there's just a quick practical demonstration showing the virtual ground effect there, and also the voltage rail limitations positive and negative. I should do another part of this video on op-amp limitations, practical limitations, things like that.

**Dave Jones:** That would be interesting. Thumbs up if you want to see that one. But, I've got I'll leave you with one last thing, and I won't explain it. I'll leave it to you to try and figure out.

**Dave Jones:** I chose these values higher than what I had on the whiteboard there. I chose them for a reason. Let's lower them down to 10K and 1K here, and see what happens with this specific op-amp, LM358.

**Dave Jones:** Hmm, let's drop these down. Still quite high values, 1K and 10K. They're not, you know, like 10 ohms or something like that. But, let's give it a go. And there it is, a 1K input resistor, 10K feedback resistor.

**Dave Jones:** Exactly the same gain, exactly the same input signal, but what's that little funny business going on in there? And over there? Hmm, and if we measure our virtual ground point, look at these little spikes there and there corresponding to that little bump in that waveform.

**Dave Jones:** Interesting. So, as Professor Julius Sumner Miller said, "Why is it so?" I'll leave that to you to figure out. Catch you next time.
