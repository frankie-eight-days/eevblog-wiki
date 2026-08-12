---
video_id: CIGjActDeoM
title: EEVblog #221 - Lab Power Supply Design - Part 1
url: https://www.youtube.com/watch?v=CIGjActDeoM
source: youtube-asr
timestamps: {"0": 0, "1": 11, "2": 20, "3": 33, "4": 49, "5": 64, "6": 75, "7": 84, "8": 100, "9": 108, "10": 128, "11": 141, "12": 155, "13": 176, "14": 189, "15": 196, "16": 219, "17": 238, "18": 250, "19": 262, "20": 288, "21": 301, "22": 323, "23": 338, "24": 351, "25": 366, "26": 389, "27": 405, "28": 430, "29": 444, "30": 456, "31": 470, "32": 480, "33": 489, "34": 507, "35": 516, "36": 528, "37": 540, "38": 559, "39": 577, "40": 588, "41": 599, "42": 614, "43": 634, "44": 646, "45": 666, "46": 684, "47": 696, "48": 710, "49": 720, "50": 733, "51": 755, "52": 770, "53": 779, "54": 797, "55": 809, "56": 822, "57": 835, "58": 848, "59": 863, "60": 872, "61": 886, "62": 898, "63": 914, "64": 931, "65": 945, "66": 965, "67": 977, "68": 992, "69": 1008, "70": 1031, "71": 1059, "72": 1078, "73": 1099, "74": 1121, "75": 1131, "76": 1142, "77": 1158, "78": 1171, "79": 1183, "80": 1196, "81": 1209, "82": 1224, "83": 1241, "84": 1250, "85": 1270, "86": 1292, "87": 1313, "88": 1327, "89": 1339, "90": 1361, "91": 1371, "92": 1385, "93": 1397, "94": 1414, "95": 1425, "96": 1439, "97": 1448, "98": 1463, "99": 1475, "100": 1486, "101": 1498, "102": 1508, "103": 1524, "104": 1533, "105": 1545, "106": 1555, "107": 1579, "108": 1593, "109": 1605, "110": 1613, "111": 1633, "112": 1648, "113": 1664, "114": 1679, "115": 1698, "116": 1723, "117": 1739, "118": 1755, "119": 1769, "120": 1780, "121": 1793, "122": 1806, "123": 1818, "124": 1831, "125": 1839, "126": 1853, "127": 1862, "128": 1870, "129": 1886, "130": 1897, "131": 1910, "132": 1931, "133": 1942, "134": 1959, "135": 1971, "136": 1990, "137": 1999, "138": 2013, "139": 2028, "140": 2047, "141": 2063, "142": 2075, "143": 2082, "144": 2099, "145": 2123, "146": 2140, "147": 2152, "148": 2178, "149": 2188, "150": 2200, "151": 2218, "152": 2232, "153": 2241}
---

**Dave Jones:** Hi, one of the most popular art projects in electronics, especially for beginners, is to build your own power supply, your own lab power supply, and I highly recommend it, as I've done on many occasions.

**Dave Jones:** You should build your own. And a good lab power supply is one that has constant voltage and constant current, as you might know. If you don't know, you do now.

**Dave Jones:** And how do you go about building one of those? Well, it's pretty simple. There's hundreds of designs out there using basic LM317s or whatever. You know, a voltage control knob, a current control knob for the constant current.

**Dave Jones:** Pretty simple, but a lot of people ask, how do you do it with software control or at least have the capability to add software control, be it from a PIC, from an Atmel, an Arduino, or a PC, or whatever processor or intelligent thing.

**Dave Jones:** You may not want to use a an expensive 10-turn pot, which I've recommended you should have on a good lab power supply. You may want to use an optical rotary encoder knob and hook it up to a microcontroller and then control the voltage and current that way.

**Dave Jones:** How do you do it? It's a good question. It's a bit more complicated than your more traditional design that just uses the knobs for the voltage and current. They're very simple designs.

**Dave Jones:** There's hundreds of them out there. Choose your own flavor for your own voltage and current requirements and stuff like that, but when you add that software capability, it's a bit more complex.

**Dave Jones:** And also, I thought I'd throw in an extra thing as a supply which goes down to zero volts as well. So, let's go through the process of designing, building, breadboarding, and testing a lab power supply that has that sort of capability.

**Dave Jones:** Let's go. And of course, the first thing we're going to start with are the specs, cuz if you don't have specs to work from, well, it's going to be a dog's breakfast.

**Dave Jones:** So, let's have a look. We want a very modest low range supply today, just for the sake of argument, zero to six volts. Now, that's important. Uh zero volts output uh is not always easy to obtain in a lab supply if you're using a basic LM317, especially when we get down to the last one here.

**Dave Jones:** I'll go into it. Anyway, it's not as easy. Uh a lot of power supplies, traditional ones, will only go down to 1.2 or 1.25 volts. And the reason for that is the reference voltage used in, say, an LM317 using the design.

**Dave Jones:** Anyway, we'll go into that. But, we want a complete from zero to six volt range. Uh we want a modest zero to one amp constant current adjustment on it cuz a good lab power supply has got to have constant current adjust knob on it.

**Dave Jones:** Uh we want uh and this is uh a key point. We want a optional, it's not mandatory, we can use knobs or we can replace those knobs with uh microcontroller uh software control of both the voltage and the uh constant current uh value.

**Dave Jones:** Usually using a pulse width um modulation scheme cuz that's how you generate a uh voltage and voltage output easily from microcontroller like a PIC. You use a PWM, a pulse width modulator.

**Dave Jones:** You can use a DAC, but most micros don't have a DAC built in. So, they have pulse width modulators. And we want a low noise, which basically means we're going to use a linear uh power supply.

**Dave Jones:** We're going to design a linear power supply today, not a switching one. And uh we want a single supply input. And you'll find um as we uh go through, you'll find why that's uh uh actually uh important because it's a hard harder to get a zero, a true zero volt output range with only a single supply input.

**Dave Jones:** So, there's our specs. Remember them. That's what we're designing around. So, let's get into the design. And of course, when you're building a lab power supply like this, one of the first devices you're going to consider is the classic LM317 and you've probably seen this before and both of these uh configurations.

**Dave Jones:** It's a classic device. It's a robust, it's low noise, it works, it's relatively stable, it uh works in constant current and constant voltage configurations which you can cascade as we've done here.

**Dave Jones:** Very versatile device and uh let's take a look at what uh how you can build a um a basic lab power supply with an LM 317 based uh system.

**Dave Jones:** Now, we've got our voltage input here and uh we've cascaded two LM317s in series. Now, what we've done is we've used the classic constant current configuration where we use a single, in this case adjustable resistor, you'd have to use a wire wound uh pot in there to set uh your constant current or in this case a maximum constant current which it won't uh exceed and it to this

**Dave Jones:** formula is uh very simple to uh calculate the maximum current is the reference voltage 1.25 V as we've seen uh divided by uh R1 up here and that gives you you your maximum constant current.

**Dave Jones:** And because uh basically very little uh current flows through these resistors and it's basically in series with your load, your output here, uh then your output load will not exceed that maximum value you've set, but it can draw less, no problems at all and it passes it straight through.

**Dave Jones:** So, if you put uh a constant current LM317 first uh before a voltage a standard voltage mode LM317, bingo, you've got your constant current and constant voltage lab power supply.

**Dave Jones:** And of course, the output is just the classic uh voltage configuration with the divider resistors and adjustable pot here. you can adjust your voltage. Beautiful. So, what's wrong with it for our design today?

**Dave Jones:** Well, turns out there's quite a few things wrong with it, actually. Uh the first one is, you remember I spec from 0 V up to whatever uh voltage. We need to go down to 0 V, but the LM317 doesn't allow you to go down to 0 V.

**Dave Jones:** It only allows you to go down to a minimum of 1.25 V, and that is because of the internal uh voltage uh reference inside of it. And uh the second one is is that um uh this adjustment uh pot here, it you can't it's uh not uh terribly good down at the very low level.

**Dave Jones:** So, if you wanted to set an output current of 1 mA, you know, it's not that great down there. Third, uh how do you adjust these with a uh you know, a microcontroller or a software function?

**Dave Jones:** It's quite difficult. Well, it turns out it's not that hard for the voltage. You can actually What you can do is get these out of the circuit completely and just drive this directly with a buffer from a pulse width modulated um uh filtered, of course, to turn it into a voltage, but you can feed that directly from a voltage.

**Dave Jones:** And that can come from your microcontroller or come from another part or whatever. You can drive it directly. You can effectively override um the internal uh reference and circuitry and actually drive it direct.

**Dave Jones:** Problem with that, though, is that whatever volt If you feed in 1 V here, you don't get 1 V out. You actually get 1 V plus the reference voltage of 1.25 V.

**Dave Jones:** You'll get out 2.25 V here. And well, you can take care of that in software. It's not too hard. So, the voltage configuration, you can actually drive it with software.

**Dave Jones:** So, let's actually build up this LM317 circuit and verify that it actually does what we think it does. Now, here it is. I've got my LM317. I've got bypass caps on the input and output.

**Dave Jones:** The input's the top rail up here coming from my lab power supply. Ground is down the bottom here. The right-hand pin over here is the input. There it is there.

**Dave Jones:** The output is the center pin or the tab. The center pin is electrically connected through to the tab up there. I've got a load here. I've got a 1K load just to because these devices, if you check the datasheet, do actually need a minimum load.

**Dave Jones:** And we'll take a look at that in a sec. And this orange wire over here is our adjust pin, which, with a typical LM317, as you would know, it's a basic building block circuit.

**Dave Jones:** You would have a voltage divider on the output and then you'd feed it back to the adjust pin to get your output voltage. But in this case, we're going to actually ground it like this and see what we get.

**Dave Jones:** And also then drive that from our low impedance second lab power supply, actually drive a voltage into that adjust pin and see what we get out. All right, let's check it out.

**Dave Jones:** See what we've got. Our input voltage is just over 7 volts. And our input pin is grounded. Let's measure our output here. Bingo. There it is. 1.253 volts. And that is the reference voltage, the internal reference voltage used in the LM317.

**Dave Jones:** And if you've only got a single supply input, like we've got here from 0 to um uh 0 to 7 or whatever voltage it is, then you can't get any lower than that 1.25 volts output cuz we've grounded our input here.

**Dave Jones:** We can't get any lower than that. So, that's why a lot of traditional lab power supplies will only go down to 1.25 volts because it's the reference voltage used in there.

**Dave Jones:** Now, I mentioned that load's important. Well, let's actually check what happens to the output if we disconnect the load like that. So, all we've All we've got now is the bypass cap.

**Dave Jones:** Well, let's check it out. Re- remember it was There we go. It's jumped up to 6.4 volts. It is not 1.25 anymore. And if we plug it back in, bingo, we'll get 1.25.

**Dave Jones:** There you go. Now, ordinarily, you don't really have to worry about this with a traditional LM317 circuit with a voltage divider on the input cuz the voltage divider, if you read the data sheet, is designed to the values are low enough to actually present the minimum load requirement of the LM317.

**Dave Jones:** But because we don't have that voltage divider and we're just driving the input pin like this, then there's no minimum load and we're going to need a minimum load on there to make to actually make this thing stable.

**Dave Jones:** Now, I've got the adjust pin of the LM317 connected through to my external another a second external variable lab supply which we can adjust here and I've got the meter just hooked up with some alligator clips there to the output and I'm feeding in 1.25 volts from my lab power supply and look what we're getting out.

**Dave Jones:** 2.51. Bingo. It adds up. So, any voltage you feed in to this adjust pin on the LM317, you've got to add 1.25 volts and there it is there. And if we adjust that set pin to 5 volts, what do we get?

**Dave Jones:** You guessed it. 6. 25 or 6.27. Bit of error there, but There there go. We whatever voltage you feed into that set pin, you've got to add 1.25 V.

**Dave Jones:** And that's really quite annoying from a um well, it's from a software point of view, it's probably not that bad because you can do the math and do the adjustment in software.

**Dave Jones:** Whatever value you set on your pot, you know you've got to output uh 1.25 V higher than that, but it's it's not nice. It's not elegant. And of course, the LM317 doesn't go down to 0 V.

**Dave Jones:** So, that's hopeless. And of course, uh I had to turn just in case for those who are wondering out there, yes, I did have to turn my input voltage up from the 7 V cuz we were too close to the dropout voltage of the regulator.

**Dave Jones:** Remember, there's a couple of volts dropout voltage on an LM317. Now, you can actually get the output of the LM317 to go down to uh closer to 0 V if you uh feed in a negative voltage uh into the set pin, and you offset it by that uh 1.25 V.

**Dave Jones:** Now, in this case, I am actually feeding in -1.25 V because I've swapped the leads. Look, I've got my negative lead going into the adjust pin. And so, I'm effectively feeding in -1.25 from my supply instead of +1.25.

**Dave Jones:** And I can do that because my power supply is floating. The outputs are floating. Remember that. That's important. Now, um I'm feeding in -1.25, and we're getting out 0.125 V.

**Dave Jones:** It's not quite the zero as you'd expect. That's because whoop, turned itself off there. We're falling victim to the uh minimum load requirement. You'll notice that this isn't the 1K value resistor anymore we were using before to get our minimum load.

**Dave Jones:** This is a uh this is a 100-ohm resistor. So, it's only going to let us go down to 0.125 V. If we lower that value resistor again, we'll our to be get closer to 0 V.

**Dave Jones:** And just to prove that, I changed the resistor value to 22 ohms and there you go, we're getting pretty darn close to zero, about 28 mV. So, that's an example of something you've got to be careful of when you're designing these sort of power supplies with these voltage regulators.

**Dave Jones:** That minimum load requirement is actually quite important and you'll find that we'll have to take that into account later on in our final design. But, it doesn't satisfy our requirement of a 0 V output.

**Dave Jones:** Not only unless you start using split supplies and driving things negative and doing fancy stuff like that, but yeah, it's just it doesn't meet our spec there. Another thing it doesn't meet is how do you adjust this pot here?

**Dave Jones:** How do you convert this pot into digital control? Well, it actually turns out that it's a reasonably difficult. You can't just Well, you could get like an E squared pot or something like that, but you've got to watch your maximum voltages.

**Dave Jones:** A lot of those will only go up to 6 or or you know, getting ones that go up to 12 V are quite rare. Any higher than that, rarer again.

**Dave Jones:** You've got big drop out voltages. Your voltage here has to be several volts greater than your output and you've got another drop on here. It's just it's not pretty at all and it's not going to meet our requirements.

**Dave Jones:** We're going to need something different. But, although we might end up using something different today for our final design, the configuration is going to be quite similar or can be quite similar.

**Dave Jones:** You can actually design some circuitry around here to replace an LM317 type constant current configuration and we will actually use the technique of overriding a pin on a voltage regulator.

**Dave Jones:** So, standby. So, how exactly do we start designing a circuit to overcome some of the limitations? Well, I think the first thing you should do is take a look at how these LM317s actually work because you might be able to maybe duplicate them with some similar circuitry.

**Dave Jones:** Now, if you have a look inside a typical LM317 broken down, you've seen this before. It's just an error amplifier with a series pass transistor. In this case, it's a Darlington, usually a Darlington transistor pair like that.

**Dave Jones:** Your input terminal, your output terminal. Usually, there's some like little protection, small amount of protection resistance in there, and there's overload protection circuitry in there and thermal overload. And there's some extra stuff, but the basic operation is just that series pass error amplifier and the voltage reference here.

**Dave Jones:** And whatever And of course, you've seen how this works before. The op amp controls the series pass transistor to make sure that the output voltage matches the input voltage cuz that's what an op amp does.

**Dave Jones:** It makes It does whatever it needs to on the output here to make sure that these two inputs are the same value. And in this very simplified block diagram here, you can actually see why we have to add on the reference voltage onto our adjust pin.

**Dave Jones:** But you can see that we can actually why we can force the adjust pin because it's effectively just setting the value on that op amp there. So, really in theory, it's possible we can use a discrete transistor, a Darlington transistor on the output like that.

**Dave Jones:** We can have an op amp like that, and we can feed it back, and we can just feed our voltage directly into this pin. And that's why you can actually design a constant voltage power supply using a a linear regulator like this using a software control or something like that cuz this value can come from a pulse width modulator {slash} DAC.

**Dave Jones:** It could come from a pot. Could come from whatever. So, as a first step, let's replace our LM317 voltage circuit with effectively what's inside there. If we use a discrete Darlington transistor on the output, can be a standard uh transistor, can be a MOSFET, you know, let's not get into the details of that, but we use a series pass transistor and op amp, just can be a regular uh op amp,

**Dave Jones:** and uh we put it in the error configuration like this, needs some output output capacitance uh to keep keep it stable, but there we get rid of the voltage reference which is inside, and our Vset pin, whatever voltage we put on the non-inverting input of the op amp like this, should be on the output like that.

**Dave Jones:** Bingo. But, you'll find that in practice this is not an inherently stable stable configuration. It's very tricky to get this stable in a lab power supply like this over a whole bunch of output load capacitances and and configurations and and currents and all sorts of things.

**Dave Jones:** So, by all means, build this up, try yourself, experiment with it. You will be able to get it to work, but I think you'll find be a little bit unstable, but anyway, that is a way that we can do the constant voltage uh aspect, and this Vset, of course, can go right down to zero, and the output will go down to zero, too, in theory, subject to minimum

**Dave Jones:** load and other things to keep it stable. So, we can drive this Vset directly from over a pot, multi-turn pot, single-turn pot, or from a DAC or pulse width modulator micro output.

**Dave Jones:** So, just like using an LM317, I don't want to muck around with trying to uh make, you know, stabilize this and worry about all that. I want to use an off-the-shelf solution.

**Dave Jones:** Aha! I remember the LT3080/3085 from my first blog, and I've mentioned it a couple of times. It's one of my uh favorite uh little linear regulators cuz it has, if you look inside of it, exactly this circuitry and it's designed to be stable.

**Dave Jones:** Bingo. We'll use the LT3080. So, I think we might have constant voltage part sorted out. What about constant current? It's a bit harder to try and adjust this value in here.

**Dave Jones:** But anyway, let's try using the same technique of replacing it with this kind of circuitry. And to do that, I think I'm going to need a little bit more room, so I'll erase all this and we'll concentrate on the constant current part.

**Dave Jones:** So, what have I come up with to replace the LM317 constant current circuit? Well, tada! Here it is. And it's rather neat, I think. I like it. Now, it looks a little bit complicated, but stick with me.

**Dave Jones:** It's not, trust me. Now, we've uh replaced We've got the LM31 circuit constant current equivalent circuit in this red box here. Remember, we've just replaced it with the error amplifier and the series pass transistor.

**Dave Jones:** And we've got a 1-ohm um current sense resistor here. It's 1 ohm because 1 ohm makes the math really easy. Because what we're after here is what we want to do is we want to because we want this PC-controlled, remember?

**Dave Jones:** We want software microcontrolled. We want to convert uh say 0 to 1 V from a microcontroller or from a pot or whatever source it is into a 0 to 1 A uh constant current limiter circuit like this.

**Dave Jones:** So, we want to feed in 0 to 1 V and get 0 to 1 A out. Okay, let's try and explain this circuit, shall we? Now, hopefully we won't get lost.

**Dave Jones:** Now, here's our voltage control input. We'll call it Vset. And we want 0 to 1 V to represent 0 to 1 A uh current limiting around this circuit. So, we've got a buffer here because you need a buffer if this comes from an pulse-width modulated output with an RC filter, you want that's not good enough to drive this circuit.

**Dave Jones:** So, you need a buffer there. So, this is our 0 to 1 V control input. Now, it goes into this adder or summer circuit here and then that is fed into a * 2 amplifier here into the non-inverting input of this constant current equivalent circuit.

**Dave Jones:** Now, if you remember how the LM317 worked, because it had a voltage reference in here of 1.25 V and it fed directly around to this pin here with no additional circuitry like that, then the current equaled 1.25 V divided by 1 ohm or 1.25 amps in this case.

**Dave Jones:** And we're basically replacing that direct feedback with a circuit that allows us to inject the 0 to 1 V signal and raise it up so that it can control this higher voltage circuit up here.

**Dave Jones:** And this is what this little part of the circuit does. Now, the reason we've got a gain of * 2 here is because this divider here is effectively dividing that this voltage by half.

**Dave Jones:** So, we need to compensate for that by having a gain of two here. And you can muck around with these ratios all you want, but they've got to basically match each other so that they're equivalent, but we need but because we have to feed in this voltage down here and it's got to go into this adder, we have to compensate with this gain of * 2 here.

**Dave Jones:** Now, I could try and explain it, but let's just go through a worked example. I think that's probably the best way to illustrate it. Let's start with the example at the extreme bottom where we've got 0 V here.

**Dave Jones:** So, this is effectively grounded. And let's say our output here is 10 V. So, this uh here is going to be exactly half of that, half of 10 uh minus zero.

**Dave Jones:** So, it's going to be 5 V here on this node. And of course, this has got a gain of two. So, we're going to have 10 V here. So, this voltage here at this point is going to be 10 V as well.

**Dave Jones:** And if you've got 10 V on either side of a resistor like that, what's the current flowing through it? Zero. Ohm's law. So, when we've got zero volts input here, we have zero current flowing through that resistor regardless of what the load is trying to do.

**Dave Jones:** The load still I want more current. I want more current. I'm short it out. I'm you know, I give me current. It's not going to because there's zero volts across that resistor.

**Dave Jones:** Can't beat Ohm's law. And just as a reminder, that works because of op amp action. This op amp tries to do whatever it can on its output to make sure that these two inputs are the same.

**Dave Jones:** So, if this voltage here is 10 V and we're feed well, 10 V here on this pin because it's being fed back and raised by two. There's 10 V here.

**Dave Jones:** It makes this pin here 10 V as well. It drives all this circuitry to make it 10 V. And that's why this input there's a dropout voltage. It needs to be higher than that 10 V significantly higher so that it can so that the actual circuit itself can function.

**Dave Jones:** And if you're wondering about the power supply for these op amps, it all this by the way works from our single supply because that's part of our spec. So, this would be grounded here like this.

**Dave Jones:** And this actually would be connected to the input like that. So, the input voltage must be significantly higher than uh than the voltage that we're actually trying to uh control.

**Dave Jones:** So, there will be some dropout uh voltage there. But all of this all these op amps can be powered from this one supply. All right, we've done the minimum case of 0 V control signal.

**Dave Jones:** What if we do our maximum case of 1 V? So, our control voltage here is 1 V, and once again, we're going to assume 10 V there just for the sake of this uh calculation.

**Dave Jones:** Now, if we've got 1 V here and 10 V there, it's actually 9 V drop across these. So, it's 4.5 V per resistor, and 4.5 V down from 10 V, our node here is going to be 5.5 V.

**Dave Jones:** And you see how it's added? That it's added that 1 V above it because if this was ground, it was only 9 V drop, it'd be 4 and 1/2 V here, but it's not.

**Dave Jones:** We've added on that 1 V because our reference point is up the top here. So, this node here is 5.5 V, a gain of 2. Bingo, we get 11 V out here.

**Dave Jones:** VR, our reference voltage, is 11 V, and that, due to op-amp action, we're going to get 11 V here. And what's 11 V - 10 V over 1 ohm?

**Dave Jones:** It's 1 V over 1 ohm is 1 amp. So, regardless of what the load is trying to do, it's screaming, it's shorted out, it's doing whatever. You can short this puppy out to ground like this, and it will it will generate 1 V across that resistor and limit the current to 1 amp.

**Dave Jones:** Magic! And it's pretty obvious that it's going to be linear within that range. We've tested the two extremes, and it works. So, you just because this, you know, there's nothing non-linear going on here, you know that it's going to work in those ranges.

**Dave Jones:** And if you want to, you can go through, and you can actually test out different cases and half a volt or 10, you know, 0.1 V or something like that for 100 mA.

**Dave Jones:** Do whatever. One thing to remember, though, is that with the 1 ohm resistor here, at 1 amp, you're going to get 1 V drop across there, and that's an additional drop.

**Dave Jones:** So, you've just got to take that into account in your design. It may be fine for you you cuz your input voltage may be quite high. You know, 1 V here plus your additional drop further on on your next stage for your voltage side of the voltage regulation, you've got a an additional minimum drop out voltage there, then it all adds up.

**Dave Jones:** Just make sure and if you wanted to lower the value of that resistor say to 0.1 ohms, then you can compensate with the gain of this circuit. No problems whatsoever to lower your voltage drop, but you know, you can't go arbitrarily low cuz then you get down in noise problems and things like that.

**Dave Jones:** Now, I encourage you to go and build this circuit up and try it for yourself and maybe even simulate it and do stuff like that. But ultimately, as with all these type of configurations, they can be quite hard to stabilize especially when you've got a variant load in lab power supply.

**Dave Jones:** So, ultimately, you might want to replace this with an already stabilized solution like the LT3080. Now, as it turns out, this circuit is quite inefficient in terms of parts utilization.

**Dave Jones:** We can actually eliminate an an op amp entirely from this circuit. How do we do that? If you had your thinking cap on, you could see that the gain of two can be actually put in this feedback path instead of the gain of two here, you can actually divide by two in this path.

**Dave Jones:** So, if we get rid of this and feed that directly into there like that, and then we break into here like this, we can add our 10 K there, and we can have a 10 K going to ground like that, and that is exactly the same configuration.

**Dave Jones:** If you don't believe me, go through the example and try it again. So, hey, now we're getting somewhere. Here is our lab power supply so far. It's got two LT 3080s, one for constant current, one for constant voltage.

**Dave Jones:** And we've got two voltage set pins from the current set pin goes from 0 to 1 V, which represents 0 to 1 A. We've got our voltage set pin from 0 to 10 V or whatever your maximum output voltage you want consistent with the maximum specs of your components.

**Dave Jones:** And you know, it's getting there. And of course, you probably want a few extras. You probably want a big beefy protection diode on the output like that. And you remember that thing we said about minimum current load as well.

**Dave Jones:** The output of this sucker, if it's drawing no current, not that great. Doesn't go down to that lower voltage and can cause issues. We could have some major issues there.

**Dave Jones:** So, we may have to add some some sort of load on there to get our minimum current out of there. And that's okay, but jeez, gosh darn it, I don't know.

**Dave Jones:** The LT3080, it runs to about three or four bucks each or something. Jeez, you want to shave that cost off. Simplicity. And if you got two devices like this, remember they will be sharing the heat as well.

**Dave Jones:** So, not only do you have to have a heat sink that actually you can mount both of both devices on there. In the constant current mode, you're going to be dissipating most of your heat in the constant current regulator.

**Dave Jones:** In constant voltage mode, you're going to be dissipating most of the heat in this regulator and so on. But I reckon we can eliminate one of these regulators. Let's give it a go.

**Dave Jones:** So, just how do we plan to eliminate one of these regulators, I hear you ask? Well, you've obviously got to have your voltage regulator. That's got to be there.

**Dave Jones:** But maybe we can do something with this adjust pin here to regulate the current instead of having a whole 'nother you know, instead of having limiting it back here, actually limit limit the current inside this device.

**Dave Jones:** Get this device to do both jobs, voltage and current limiting. How do we do that? Well, we'll find out. Now, if we want to get rid of this, we still need a current sense resistor.

**Dave Jones:** We're still going to sense the current. So, let's keep our 1 ohm resistor and let's tap off the voltage on there and see what we can do with it.

**Dave Jones:** Okay, here's what I've come up with. Now, once again, it may look a bit complicated, but it's not. Stick with me. It's all basic building block stuff. Now, what we've done is we've got rid of the current LT3080 up here, the current regulator up here, and we've replaced it.

**Dave Jones:** We've still got the 1 ohm current shunt resistor. You got to have that. You got to have something to measure the current actually flowing in the input. And you can do this, by the way, ignore this.

**Dave Jones:** You can put this before the regulator cuz there's basically there's very little current flowing out of the control pins of most voltage regulators. So, all the current in is going to be basically equal to the current out.

**Dave Jones:** You may have to take it into account as you might see, but basically that's how you can get away with doing it here instead of on the output, something like that, where you end up dropping the voltage cuz if you put it in the output, either the high side or in the return ground path, which is called the low side current shunt, then that will drop some

**Dave Jones:** voltage and your output voltage isn't going to be as well, it's going to have a voltage drop. It's not exactly what you set it. So, not ideal. So, it's better to have it on the input side of the voltage regulator and let it handle it.

**Dave Jones:** Anyway, we've replaced it with a differential amplifier. And if you know your basic building block op-amp configurations, this is a single op-amp differential amplifier. It's not that great, but it's probably good enough for our purposes.

**Dave Jones:** You could actually replace all that with um a a proper um off-the-shelf um differential amplifier like an AD620 or something like that. But, they're quite expensive and you know, yeah, you don't need that sort of precision.

**Dave Jones:** Anyway, what the differential amplifier does is the output voltage here, at this point here, will be equal to the difference in voltage across that resistor. So, if there's 1 amp flowing through there, there'll be a 1-V voltage drop and you'll get 1 V out of here.

**Dave Jones:** Simple. Now, one of the key parts to this is this little bit here and this is the current limiter. And how this works, it's using, you'll notice there's no feedback on this op amp.

**Dave Jones:** It's using it as a comparator. And once again, you could replace this with a comparator, but we'll use an op amp in this particular circuit. Now, you'll notice that because this input to this op amp is high impedance, you don't need this driver anymore.

**Dave Jones:** You can eliminate that entirely and just connect your ISET. So, we've still got our three op amp configuration. We haven't increased our number of op amps, but we have dropped one current regulator device over here.

**Dave Jones:** So, that's a parts count and possibly cost advantage. Now, obviously, if this is working as a comparator, if this voltage here, let's say we've got 1 amp flowing through here, 1 V, we've got 1 V here, if that is greater than the the current we've set on our pot, remember, from 0 to 1 V, 0 to 1 amp.

**Dave Jones:** If we set it to, you know, 0.99 V or 0.999 V, then this 1 V will be greater than that and it will switch on this transistor here, which is the same We've got the same circuit here before.

**Dave Jones:** Remember, this is exactly the same. Just ignore these resistors for a second. And before we had this connected directly to the adjust pin to control our output voltage. Simple, but we can't just short out.

**Dave Jones:** We can't just add this transistor which will short out the output of this op-amp. It's not very nice for the op-amp and it's not going to work too well.

**Dave Jones:** So, we need a series current limiter resistor in there. Let's make it 1K and let's make another 1K resistor there and bingo, when this input Sorry, when this is 1 volt, when it goes into current limiting mode, i.e.

**Dave Jones:** the volt the current flowing through this resistor has exceeded the value exceeded the value set by your adjustment pot or your microcontroller, whatever it is, then we'll turn on this transistor and pull this pin adjust pin low, which will then drag your output voltage low with it.

**Dave Jones:** But, of course, because you've got output capacitance here, it's not going to instantly drop to zero. It's actually going to slowly go down. It'll go down It'll go down reasonably quickly, but it'll drop and then it will sort of servo So, the current So, the output voltage will drop.

**Dave Jones:** So, therefore, your load the current in your load will drop. So, therefore, it will kind of like oscillate and servo and control that and keep it at an average value of 1 amp.

**Dave Jones:** And also, I think we're probably going to want to add in some capacitance in there as well. Not only to know it lower the noise of the regulator. If you look at the data sheet, which we will later for the LT3080, if you put a cap there, you can actually lower the output noise, but that will also just help stabilize things and you know, slow down the operation of the current

**Dave Jones:** adjustment and stuff like that. But, that's the whole mechanism behind this thing is that it basically switches the output off and on off and on so that it gets that average value.

**Dave Jones:** Only in current limiting mode though does that happen. When if you've got 1 V set for your current limit, 1 amp set up here, and your output current is less than 1 amp, then none of this turns on.

**Dave Jones:** This transistor just stays permanently switched off, and this acts just like a the standard voltage regulator by setting this pin. If you've got 1 V set in 1 V output, you'll have 1 V here, and bingo, this transistor is turned off, so that's not there.

**Dave Jones:** There's effectively no current drop through these resistors, and you'll have 1 V here, and you'll have 1 V there. Easy. But, as always, I simplified things and lied to you a little bit by saying that there was no current drop in these resistors.

**Dave Jones:** But, if we check out the data sheet for the LT3080, might be a couple of traps for young players. So, let's go have a look at the data sheet.

**Dave Jones:** But, hey, here's our circuit. I think we'll build this one up.
