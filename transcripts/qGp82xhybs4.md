---
video_id: qGp82xhybs4
title: EEVblog #110 - Let's Design a DC to DC Switchmode Converter
url: https://www.youtube.com/watch?v=qGp82xhybs4
source: youtube-asr
timestamps: {"0": 0, "1": 20, "2": 34, "3": 49, "4": 62, "5": 85, "6": 100, "7": 114, "8": 138, "9": 151, "10": 163, "11": 180, "12": 194, "13": 209, "14": 223, "15": 235, "16": 244, "17": 252, "18": 264, "19": 276, "20": 286, "21": 305, "22": 322, "23": 334, "24": 351, "25": 362, "26": 371, "27": 394, "28": 409, "29": 422, "30": 430, "31": 441, "32": 455, "33": 466, "34": 479, "35": 488, "36": 504, "37": 522, "38": 537, "39": 553, "40": 567, "41": 584, "42": 597, "43": 614, "44": 625, "45": 643, "46": 658, "47": 669, "48": 688, "49": 702, "50": 713, "51": 728, "52": 738, "53": 749, "54": 756, "55": 767, "56": 780, "57": 795, "58": 820, "59": 833, "60": 849, "61": 859, "62": 870, "63": 888, "64": 901, "65": 915, "66": 929, "67": 939, "68": 950, "69": 962, "70": 974, "71": 983, "72": 993, "73": 1003, "74": 1016, "75": 1028, "76": 1043, "77": 1056, "78": 1069, "79": 1086, "80": 1097, "81": 1108, "82": 1122, "83": 1158, "84": 1167, "85": 1183, "86": 1195, "87": 1221, "88": 1235, "89": 1246, "90": 1260, "91": 1275, "92": 1286, "93": 1300, "94": 1313, "95": 1326, "96": 1346, "97": 1359, "98": 1381, "99": 1399, "100": 1414, "101": 1425, "102": 1444, "103": 1461, "104": 1470, "105": 1489, "106": 1502, "107": 1517, "108": 1529, "109": 1547, "110": 1562, "111": 1577, "112": 1591, "113": 1607, "114": 1613, "115": 1633, "116": 1645, "117": 1662, "118": 1675, "119": 1691, "120": 1703, "121": 1713, "122": 1731, "123": 1744, "124": 1761, "125": 1776, "126": 1787, "127": 1800, "128": 1820, "129": 1828, "130": 1847, "131": 1870, "132": 1882, "133": 1897, "134": 1907, "135": 1922, "136": 1939, "137": 1948, "138": 1962, "139": 1979, "140": 1989, "141": 2007, "142": 2017, "143": 2029, "144": 2044, "145": 2061, "146": 2076, "147": 2104, "148": 2122, "149": 2135, "150": 2153, "151": 2171, "152": 2186, "153": 2199, "154": 2220, "155": 2228}
---

**Dave Jones:** Hi, welcome to the EEVlog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, a little while ago I surprisingly showed that there wasn't much difference between a traditional linear voltage regulator and a switch mode voltage regulator.

**Dave Jones:** And well, I thought I'd do a follow-up video of that on designing a switch mode power supply cuz I got a lot of feedback. Everyone wanted to know, "Well, how can I design a switch mode power supply?" Let's go through it step by step.

**Dave Jones:** So, how do you design a switch mode voltage regulator? Well, you can do it using uh traditional discrete components, just transistors, inductors, capacitors, resistors, that sort of stuff, but ah that's that's really pretty ugly way to do it.

**Dave Jones:** And unless you have a very specific niche reason to do it, you shouldn't uh you shouldn't go down that avenue. You should use one of these standard off-the-shelf uh switch mode controller ICs available today, but which one?

**Dave Jones:** If you go to Mouser or Digi-Key and search for switch mode controller chips, there's thousands of them. The choice is crazy. It's ridiculous. Where do you start? Well, I'm going to use for this blog, I'm going to use one of my favorites, and it's probably the closest thing to a jelly bean uh generic uh switch mode controller IC on the market.

**Dave Jones:** It's almost certainly probably the world's most popular one. It's the MC34063. Now, you may not have heard of it before, but I can guarantee you it's been around a long time and it's used in practically everything.

**Dave Jones:** And one of the great advantages of it is that it's not available it's not just fixed from one manufacturer. Now, MC is uh the old uh code for Motorola, but Motorola don't make chips anymore.

**Dave Jones:** It's now ON Semiconductor. So, now ON semi make it, but trust me, if you just put in 34063 into Mouser or Digikey or any other part search engine, you'll get a whole bunch of different manufacturers who manufacture the identical functionally and pin compatible chip to the MC34063 and design in it the formulas are all exactly the same.

**Dave Jones:** So, it's a fantastic chip available from anyone. It's even available from no-name manufacturers. If you really want to go down to, you know, 1 or 2 cents per chip, you can get it.

**Dave Jones:** Whereas, as opposed to a lot of the other DC-to-DC converter switch mode controllers on the market there, they might be, you know, only available from National Semiconductor or only available from TI or something like that.

**Dave Jones:** And really, you don't want to be locked into that, especially for these hobby projects. And the other good thing about the MC34063 is that um uh it's available in a DIP, standard DIP-8 package and a uh SO-8 package as well.

**Dave Jones:** So, you can plug it straight into your breadboard or your through-hole design. Really easy, simple stuff. Now, let's take a look at the data sheet for the On Semi MC34063A.

**Dave Jones:** Here it is. Now, here's the internal circuitry for it and as you can see, it's an 8-pin device. It's very simple. It's uh just like in my previous blog, I showed how a a basic This is really I It's about as simple as it gets for a uh switch mode controller IC.

**Dave Jones:** And as you can see, it's got a comparator with a built-in 1.2-V voltage ref- reference. It's got an oscillator, which is controlled via an external capacitor, the timing capacitor on pin three there.

**Dave Jones:** It's got a um it's got a Darlington uh transistor uh pair that well, it's actually you can configure the output transistor. It's got a switching transistor Q1 there. It's got the separate collector and the separate switch emitter.

**Dave Jones:** And it's also got a drive collector as well, which is important and we'll go we might go into that later. And it's also got a current sense input pin.

**Dave Jones:** You put a current sense resistor on there. We'll show you that later. And it's it's basically and it's got the pin five there is the input for the feedback.

**Dave Jones:** So, it's very simple and it's very easy It's pretty easy to use, not as easy to use as many of the other ones on the market. In fact, you could probably argue this is one of the more difficult ones to design with.

**Dave Jones:** There's lots of formulas as we'll go through. But even because it's it might be one of the most hardest to use on the market. I'll show you just how easy it is if you go step by step through the calculations.

**Dave Jones:** And the other good thing is take a look at the take a look at the specs. It's got a very wide input voltage range from 3 volts to 40 volts input.

**Dave Jones:** That's huge. It's got 1.5 amps maximum output switching current. It's reasonably high frequent It's medium frequency. It goes up to 100 kilohertz, which is pretty good. You can adjust the voltage and it's got a precision 2-volt voltage reference.

**Dave Jones:** And the other good thing is that it's configurable to be either a step up or a boost converter. So, 5 volts in and 12 volts out for example. Or you can configure it the other way, a step down or a buck converter from say 5 volts down to 3.3 volts.

**Dave Jones:** It's very versatile. And it's got a third configuration, which is the inverting configuration. So, you might feed 12 volts in and you get minus 12 volts out. Very versatile chip.

**Dave Jones:** That's why I love it. It's one of the cheapest on the market. It's like 50 cents and it's available from everyone. Magic. And just to prove that it's really is a generic jelly bean switch mode controller used in cheap products.

**Dave Jones:** I've got one of these Nokia, you know, one of these just no name one hung low brand Nokia car chargers. You've seen them, right? They plug into your car cigarette lighter.

**Dave Jones:** Let's crack it open and see what's in there. And I've opened quite a few of these and check it out. You can see there's the input fuse and there's a there's a eight pin here we go.

**Dave Jones:** There's an eight pin standard dip package chip and bingo lo and behold what do you see? The MC34063. It's from UTC where so it's not an on semi one but as I said it's available from a bunch of manufacturers.

**Dave Jones:** And check it out. There's the inductor, there's the probably output filter cap, there's an input filter cap, there's the sense resistor there and very simple. So if it's used in these things which can buy on eBay for like $2 then you know that this chip is a beauty to use.

**Dave Jones:** It's an industry standard device. No problems at all. Now let's take a look at the three different configurations this chip can be used in on the data sheet. Here it is.

**Dave Jones:** The first one is the step up converter which is the example I'm going to use today. We're going to go through this step by step, calculate it, and build it and then measure it.

**Dave Jones:** Now here it is. As you can see there's on the left hand side then there's 12 volts input this is just an example. This is this is the example provided in the Motorola data sheet.

**Dave Jones:** There's 12 volts in, there's a 100 microfarad input filter cap, there's a a .22 ohm sense resistor between pin six and seven there. And then that goes through the inductor L up the top there.

**Dave Jones:** That's 170 microhenries and we'll go through the calculations how to get all these values and then that goes around into Q1, which is the switching transistor down to ground there.

**Dave Jones:** And then there's a 1N5819 Schottky diode. Now, that's important. It's got to be a Schottky type because they're fast and they're designed for high switching frequencies and they've got low voltage drop as well.

**Dave Jones:** Very important to choose a Schottky one there for most applications. And as you can see the example here, there's an output filter cap, C0 there, C out, 330 microfarads.

**Dave Jones:** And in this example, it's 28 V, 175 mA maximum output. And you can see R1 and R2 there are the feedback resistors which set the output voltage into pin five there in into the comparator.

**Dave Jones:** So, it's very simple to do. And let's take a look at the second configuration, which is the step-down converter here. Now, as you can see, it's it's not too different except that the inductor has been the inductor and diode have basically moved around a bit.

**Dave Jones:** They're still In this example, there's 25 V going in, the same filter cap as before, the same sense resistor as before. But now look, pins one and eight are now tied together, whereas before the inductor was between pins one and eight.

**Dave Jones:** That's how versatile this chip is. You just configure it in a different pin configuration and you get a totally different functionality out of the chip. So, it's going to take 25 V in and to give us 5 V out at 500 mA maximum.

**Dave Jones:** Now, as you can see, it goes into Q1, the switching the switching transistor there. And then there's a then there's a reverse-biased diode to ground. And I explained this last time how it all works, so I won't go through it again.

**Dave Jones:** But then there's a series output inductor, 220 microhenries microhenries this time, which goes to the output filter cap and then the sense resistors, as before. So, very simple once again, you just rearrange a few of the components, totally different functionality.

**Dave Jones:** I love it. And here's the third configuration, the voltage inverting configuration. Now, as you can see, it's got 4.5 volts to 6 volts input and it gives us -12 volts at 100 milliamps output.

**Dave Jones:** So, not only has it boosted it's it's actually boosted the voltage as well as inverted it. And this is very handy if you're say only got a single battery supply and you want to power a dual supply op-amp or something like that, you might use something like this.

**Dave Jones:** But, this is generally for higher power. You might use a switch capacitor converter for that, but we won't go into it. But, let's take a look. Once again, the configuration on the input on pin six there is exactly the same.

**Dave Jones:** You've got the voltage in filter cap, the current sense resistor once again. Pins eight and one are tied together just like our a step-down configuration. But, as you can see, the difference between the step-down and the inverting is that the inductor and the diode have switched places now.

**Dave Jones:** Instead of the diode going to ground on pin two there, you've got the inductor going to ground and then you've got the 1N5819 Schottky diode there, once again reversed bias going to the output.

**Dave Jones:** And then there's an output filter cap and the feedback resistors R1 and R2 again. As you can see, very versatile chip. Why wouldn't you have this as a standard component in your junk box?

**Dave Jones:** Okay, enough of the talk. Let's do a real design. Now, onto the real scary stuff. Hold onto your hat. Take a look at this from the data sheet. This is the table of formulas that you have to use to calculate all the different the different configurations.

**Dave Jones:** Now, as you can see the columns, there's one for um step up, there's one in the middle for step down, and there's one for voltage inverting. So, today we're going to look up at we're going to look at this step up configuration, which is in the second column there.

**Dave Jones:** And there are all the formulas that we're going to have to use um and the various calculations are on the side. Now, it looks complicated, but really it's not that bad.

**Dave Jones:** And I'll show you there, you know, there's no complex math here. You just have to basically fill in the blanks, go through step by step. And the good thing about this table is that the actual values, each row there, they are actually the steps you need to take.

**Dave Jones:** They're They're not numbered. They should be like They should be another column there that says um step step number, and then 1 2 3 4, because these you'll go through these formulas step by step.

**Dave Jones:** And really, if you just looked at this data sheet before, it might scare you off, but it's not that bad. So, let's give it a go. Okay, let's go through a real example.

**Dave Jones:** Basically, you got to start with what spec you want. Now, let's write these down, okay? So, we know we've got a good baseline to know what we're working with.

**Dave Jones:** We're going to use Let's say we want a step up converter. That's today's example, okay? We have We have an input voltage of five, let's say, 5 V, okay?

**Dave Jones:** We're taking a standard 5 V power supply. Let's say it's plus minus 10%. You need to know the variation in there, as you'll see later. Um now, the goal today is to get a voltage output of 15 V, okay?

**Dave Jones:** So, we want 5 V in, and we want our little circuit to give us 15 V out at 100 mA maximum current. Now, this isn't Don't confuse this with the constant current uh generator.

**Dave Jones:** It doesn't generate 100 mA. It just will generate 15 It's a voltage supply, so it'll generate 15 V and allow you to draw up to 100 100 mA. Now, you also need to know what sort of ripple you want on the output because DC to DC converters don't just if this is if this is volts up here and this is time down here, it doesn't just generate

**Dave Jones:** a flat voltage like that. You won't see if you hook your oscilloscope up to the output of this DC to DC converter that we're going to build, you won't just see a flat line, a nice steady voltage at 15 volts.

**Dave Jones:** You will actually see ripple like that. It will actually go up and down and you want to know the peak to peak value between there and there. Now, I'm just going to take in, you know, a reasonably low figure for a 15 volt supply.

**Dave Jones:** I'm going to be pretty happy if we get say 100 millivolts ripple. That's quite reasonable. So, they're the specs that we're going to work with. We're going to plug them into our formulas and we're going to design our circuit.

**Dave Jones:** We're going to build it and see what happens. Okay, here we go. All the calculations step by step as per that table I just showed you in the data sheet and here it is.

**Dave Jones:** Don't blame me, but check it out. It looks complicated, okay? It looks really complicated, I admit, but it's not. Stick with me. I know this looks like a mess, so instead of just holding it side by side like I normally do, I'm going to put it here and go through it because it's important.

**Dave Jones:** Let's check it out. Now, I'll try and do this in one take, okay? Now, these are the equation These are the These are the parameters of the circuit down here which we saw in our table before, okay?

**Dave Jones:** Here's our Here's our table. Here's the table we had, okay? And these values down here, these these parameters match these and the rows are the same and we've just We're just going through the calculations and our numbers will pop out the other end.

**Dave Jones:** Magic. Watch this. Now, the first thing we We to calculate is T on uh T off, T on on T on divided by T off. Now, this is the formula for it from the data sheet.

**Dave Jones:** Now, let's punch in the numbers. Now, our voltage output, okay? That is 15 V. That's the voltage we want out of our circuit. Now, the forward voltage drop, okay?

**Dave Jones:** You've got to choose a diode. Now, I've just chosen at one of, you know, I've used before. It's the B 220A from Diodes Inc. And you need to look at the VI curve, okay?

**Dave Jones:** For this particular diode. Now, as you can see on the Y axis here is the forward current for that diode, and on the X axis is the instantaneous forward voltage drop.

**Dave Jones:** So, the So, the current versus the voltage drop. Now, we don't know the actual peak current through the diode at the moment, okay? So, let's just take the example of say 1 amp.

**Dave Jones:** Let's just say it's going to be 1 amp for our 100 mV output, okay? You go across on that curve there, and you drop down, and that's 0.4 V.

**Dave Jones:** That's the voltage drop of the diode we're going to use. It's not going to be too critical because it's a small function of the 15 V we've got here.

**Dave Jones:** But, let's plug in 0.4 V, okay? And then, we have to subtract the input voltage minimum. You know how I said it was 5 V uh input voltage plus minus 10%?

**Dave Jones:** Well, 5 V minus 10% is 4 and 1/2 V. There it is. Now, there's the same value again. Plug in 4 and 1/2 minus the saturation voltage of the transistor.

**Dave Jones:** Now, the saturation voltage, you've got to go back to the data sheet. Now, here it is. I'll put it up. Now, here it is. Now, the saturation voltage is the output switch.

**Dave Jones:** Now, there's two saturation voltages. One is for the Darlington configuration, which is only applicable to the step down. We're using step up, so we have to look at the second one here, the saturation voltage over here, Vsat is let's take the typical value of 0.45.

**Dave Jones:** Let's round that up to 0.5, okay? So, we come back here, you plug it in, saturation voltage 0.5. You punch that into your calculator and you get a value of 2.7.

**Dave Jones:** Now, let's go on to the second parameter, T on plus T off. Has the simple formula of one on F. F is the switching frequency. Now, as I said, the switching frequency of this device has a maximum value of 100 kHz and I'm going to choose that maximum value.

**Dave Jones:** Why? Because a switching DC to DC converter, the higher frequency you go, the smaller the inductor you have to use and inductors are big devices. They, you know, if you've got a large value of inductance, it requires a large a physically large inductor.

**Dave Jones:** I don't want that, okay? So, the higher the switching frequency, the the more losses you will get at a higher switching frequency, but it's a bit of a trade-off, but we won't worry about that.

**Dave Jones:** I'm going to choose 100 kHz. That gives us 10 microseconds for T on plus T off. Now, let's go on to the next one, T off. T off is a bit more complicated formula.

**Dave Jones:** It's T on plus T off, right? It's not They're not separate values. It's that that parameter there, T on plus T off, okay? 10 microseconds, there it is. Uh divided by T on on T off, which is that one there, 2.7 plus one.

**Dave Jones:** Plug that into your calculator. See, it's not as complicated as it looks. 2.7 microseconds. Now, let's go on to T on, okay? T on is a simple, it's just T on plus T off, which is that value up there, 10 microseconds minus the T off value we just calculated, 2.7 microseconds, and it gives you a value of 7.3 microseconds because you'll have a waveform which has an on time like that and an off time

**Dave Jones:** like that. Okay, that's your switching. That'll be your on time, for example, and that'll be your off time. Now, the next thing we need to calculate is our timing capacitor called CT.

**Dave Jones:** This is the external capacitor that sets our switching frequency for us. Now, the formula is 4 * 10 ^ - 5 * T on. So, we know T on.

**Dave Jones:** We just calculated that, 7.3 microseconds. So, you multiply that by 4 * 10 ^ - 5 and you get 292 picofarads. And that's the value we will plug into our circuit for CT as we'll see later.

**Dave Jones:** Now, the next parameter is I peak, which is the peak current through your switching devices, i.e. your inductor and your diode. Okay? So, the formula is 2 * IO max * T on on T off, which we got up here, T on on T off, + 1 = and you plug the values in.

**Dave Jones:** Okay? So, our our output maximum current, as I said, 100 milliamps or .1 amps. Everything's in amps, okay? So, it's 2 * .1 * 2.7, which we got up there, + 1.

**Dave Jones:** Plug it in, 0.74 amps. And that is the peak current through our diode. Do you know how I said I chose a 2-amp B220 diode? Well, that would be a good ballpark.

**Dave Jones:** You'd need at least a 1-amp diode in there with a low enough voltage drop, a low enough a low enough VF, to get an efficient circuit. So, a 2-amp diode in this circuit would work nicely cuz that's our peak current.

**Dave Jones:** Our output current, as I said, is only 100 milliamps, okay? 100 milliamps output current, but our peak is 0.74. That's the thing with switching converters, you've got to watch out for.

**Dave Jones:** Okay? You don't go and use a an an inductor and a diode rated at 100 milliamps cuz that's your output current. No, you need to choose the inductor and the diode based on your peak current here.

**Dave Jones:** It's a very important, vital thing and a trap for young players. Now, our next value our next parameter down here is RSC, which is our sense current resistor. That's what SC stands for.

**Dave Jones:** Uh current sense resistor. And the formula is simple, it's 0.3 on the peak current we just calculated. Plug that in, 0.4 ohms. And that's the value we'll plug into our circuit for RSC, as we'll see later.

**Dave Jones:** Now, here's where we get down to our other values for our components. Our inductor L, the minimum value of our inductor for this particular circuit, this is the formula.

**Dave Jones:** VIN minimum, as we've seen we've seen that before, it's 4.5. Okay? There's the value minus Vsat. Now, we've seen Vsat before, it's 0.5. There it is. Divided by the peak current we calculated here, 0.74 times the on time, which we calculated up here.

**Dave Jones:** You see how all these previous calculations we've done allow us to fill in these equations later. So, you plug that in your calculator and you get 39 microhenries. That's the value of our inductor we need to use for our circuit.

**Dave Jones:** Pretty simple. Now, out C C out, our output capacitor, our filter capacitor here's the formula for it. It's nine times I I the output current, which is 100 milliamps, which is our which is our spec for our circuit, times T on, which we've calculated before, 7.3 microseconds on the output ripple.

**Dave Jones:** Now, as we said at the start, as per our spec, I said I'd be happy with say 100 millivolts ripple on this circuit. So, 0.1 volts, there it is, 100 milliamps, plug it in, and you get 66 microfarads, and that's the output capacitance we need on our switching regulator.

**Dave Jones:** Ta-da! Wasn't that easy? Piece of cake. It looks complicated, but it's not. You just need some basic math and go through step-by-step. Easy. And there's one more thing we have to calculate.

**Dave Jones:** We have to calculate the feedback resistor values for our circuit. Now, once again, on the data sheet down here, here it is. The desired output voltage, Vout, equals, here's the formula.

**Dave Jones:** It's a pretty standard formula used for a lot of DC-to-DC converters. 1.25, which is the internal reference voltage, uh times 1 + R2 on R1. Now, if you rearrange that formula, let's um let's say you want to pick and you can pick any value of R1, just rearrange it.

**Dave Jones:** It's R2 equals Vout on 1.25 minus 1 times R1, and that gives you your values. Now, we can go back to the data sheet, and we can plug in all of the values into our example step-up uh converter circuit here, straight out of the data sheet.

**Dave Jones:** Now, we've got 5 volts in, okay? We didn't need to calculate the value of the input cap, that can be um anything really, it depends on your source, but we won't go into that.

**Dave Jones:** Now, RSC, we calculated on the whiteboard before, that was 0.4 ohms, okay? Now, our inductor up Oh, sorry, this um this series resistor here to drive um for for this transistor over here, we'll leave that at the example value of 180 ohms, cuz we didn't need to calculate that, so we'll just leave it.

**Dave Jones:** Now, our inductor we calculated on the whiteboard was approximately 39 microhenries, there it is. Now, our timing capacitor here, we also CT, we calculated on the whiteboard before, was 292 pF.

**Dave Jones:** Doesn't have to be that exact. Um and our output filter cap, we calculated that as well, and there it is, 66 microfarads. And that those Oh, sorry. We've got one more thing here, R1 and R2.

**Dave Jones:** I showed you that formula just before. Now, if we choose R1 as 10k, then um 110k for R2 will give us 15 V out, 15 V at our 100 mA uh maximum.

**Dave Jones:** And so, if we plug these values, if we build this circuit and plug these values in, it should work exactly as we predict. Now, some of these values won't be spot on to the E12 or E24 preferred values.

**Dave Jones:** 39 micro-Henries um is in the E12 range, but you might find that a 33 micro-Henry is easier to get, so you might want to use, say, a 33. Um and once again, a 0.4 ohm sense resistor, you're not going to get one of them, so you might choose a 0.39 ohm sense resistor.

**Dave Jones:** It's not hugely critical. The timing capacitor, you you won't be able to buy a a 292 pF capacitor, matter. So, you might use a a 270 pF or even a 330 pF capacitor in there.

**Dave Jones:** Um these values you can get, 10k, 110k, no problems. 66 microfarads isn't a preferred value. You might get 68 uh microfarads you'll be able to get, but you might want to round that up to, say, a nice uh easier value to get, like 100 microfarads.

**Dave Jones:** So, we might use those values in our actual built-up circuit. And here we are. I've built up the actual circuit. I just so happen to have a board which matches the MC uh 34063 device, and uh we've I've wired it up.

**Dave Jones:** And as you can see, there's the output voltage. I'm putting 5 V into it uh from my power supply up here, we're getting in 15 V out, no problems.

**Dave Jones:** And here is the output. This is AC coupled, 100 mV per division. I'll try and get a better look at that, but um let's take a look at the output uh configuration the output ripple under load.

**Dave Jones:** Now, that's at zero load. I've got my dummy load from last time for a previous blog. So, I can dial in any load I want. That was that's with zero load.

**Dave Jones:** Now, as you can see, the ripple 100 mV per division, we we wanted about 100 mV ripple. We're getting about 200 mV peak, as you can see there. But, that isn't I guess that's not too bad at all, really.

**Dave Jones:** But, as you can increase the load, let's check it out. See, watch it change. That's now at 10 mA load. And let's take it up to 20 mA load.

**Dave Jones:** And as you can see, it the ripple starts to get it it changes. That's the operation mode of the DC-to-DC converter changing based on the load. But, we can actually freeze that and take a look at some of those peaks.

**Dave Jones:** As you can see, they're about almost 200 mV peak-to-peak ripple, which is probably a bit higher than what we actually wanted than what we calculated, but you know, it's still within the ballpark.

**Dave Jones:** And as you can see, the the peaks are actually different. You can see the different change in mode of operation of the actual device based on that particular load.

**Dave Jones:** And we can go past 100 mA, there's nothing stopping us there. That's 130 That's 150 mA. That's 170. That's 200 mA. So, that's double our calculated value and there you go.

**Dave Jones:** That's the output ripple. Um and as you can see, it's dropped down to the output voltage has dropped down to 13 V now at 200 milliamps. So, it's um starting to uh starting to drop out.

**Dave Jones:** Okay, now let's say we weren't happy with that output ripple, and I'm not. Let's add in an an optional uh LC output filter here. Because I'm using 33 microhenries up here, I'm going to use another one here, and I'm going to use the same 100 microfarad output cap as well.

**Dave Jones:** And I've built that up, and let's take a look at it. Here it is here. I've added As you can see, I've added in the extra uh I've added in the extra output cap and the inductor there, and this is the ripple at no load.

**Dave Jones:** This is no This is the same scale as before, 100 mV, but as you can see, it's much much cleaner. If we turn that up to 20 mV per division, there you go.

**Dave Jones:** It's actually quite clean. That's at no load. Now, let's turn this load up. That's now 30 milliamps, 40, 50, 60. Let's go up to our maximum of what we wanted, 100 milliamps.

**Dave Jones:** That's 100 milliamps. That's 20 mV per division ripple. As you can see, it's not It's not too bad at all. It's quite low, and you can add some extra filtering if you want if you weren't happy with that, but that's what an extra LC output filter can do for you.

**Dave Jones:** And also, let's see where the DC-to-DC converter drops out. Now, this is my current. Here, it's basically reading 2 milliamps at the moment. This is my output voltage, 15 V.

**Dave Jones:** If we wind the current up, let's see where it drops out. It easily meets our spec of 100 milliamps. That's what That's what we designed it for. And it goes a bit but a bit but a bit above that and 170 it's starting to drop.

**Dave Jones:** There we go. At about 170 milliamps, it's the output voltage is starting to drop. It enters drop out because our values aren't optimized for that higher current. But if you obviously wanted to go up to 220 milliamps, say, you would have done those calculations again and you would have got different values for the components which would have allowed you to go on up to that current.

**Dave Jones:** Okay, now let's see if we can actually characterize the performance of this DC-to-DC converter circuit over its entire current range. Now, ladies and gentlemen, boys and girls, I've mentioned this before but I will say it again.

**Dave Jones:** This is a classic example of why any good lab needs four multimeters because to measure the performance of a power supply like this, you need to measure the input voltage and current, which I'm doing with these two meters, and the output voltage and current with these two meters.

**Dave Jones:** So, I need four meters at the same time. Now, voltage times current is input power and that's what we want. We want to know the input power. So, this is measuring the input current.

**Dave Jones:** This is measuring the input voltage. And this these two here are measuring the output power. This is measuring the output current and measuring the output voltage. And let's um take, say, um our power supply is in 0 to 100 milliamps.

**Dave Jones:** Therefore, let's measure it in, say, 10 milliamp steps. Let's record all these values in 10 milliamp steps from 0 to 100 milliamps and that will give us a reasonable rough graph of the performance efficiency of this circuit.

**Dave Jones:** Let's do it. Now, I'll just go through the first reading. As you can see, this is our output current and it's roughly 10 milliamps. And our output voltage is 15.06 volts.

**Dave Jones:** And as you can see, our input voltage is 4.95 volts and the input current is uh 59.4 milliamps. So, let's uh write these down in a table format and increment it to 100 milliamps.

**Dave Jones:** And bingo, we have our figures from 10 to 100 milliamps. Let's go graph them. And after plotting the data, here's what we get. We've got efficiency on the Y axis here from 50 to 60% and we've got current on the X axis from 10 milliamps up to 120 milliamps.

**Dave Jones:** So, I just went over the 100 and as you can see it's a it's it's a fairly typical response for an efficiency curve for a DC-to-DC converter such as this.

**Dave Jones:** And it peaks at about 100 and odd milliamps there as our design example should have shown. But yeah, 59 almost 60% efficiency isn't that terrific, but it's okay. There's there's nothing inherently wrong with that.

**Dave Jones:** If you optimize the values of your inductor, if you optimize the type of the inductor, if you've got a certain inductor um type here, that's going to affect your efficiency.

**Dave Jones:** Your diode, your type of diode's going to affect your efficiency and so on. But you can modify those to increase your efficiency as required. Okay, I've changed the inductor on here.

**Dave Jones:** It's a different brand, different type. It's a 47 microhenries instead of a 33 microhenries. Let's get the efficiency graph again with that inductor and see how it goes. And one thing with this new inductor, as you can see at 120 milliamps output current, it's actually dropping out.

**Dave Jones:** The voltage is dropping out, whereas at 110 it was just about 100, it's just in there at 15. So, it drops out right on 100. And here's the efficiency graph again with the 47 microhenry inductor.

**Dave Jones:** As you can see, it peaks sooner. It's a higher efficiency. It goes up to almost it goes over 65% which isn't too bad, but it actually peaks at a at at at a lower current and then drops back down drastically.

**Dave Jones:** So, as you can see, changing the changing the parametric values in the circuit changes its characteristic efficiency response and all sorts of things. So, you can play around with this to your heart's content, choosing optimizing the type of inductor you've got based on the equivalent the series resistance of the inductor, the the Schottky diode you're using in your output filtering, all sorts of stuff will affect the efficiency

**Dave Jones:** performance graph. So, there you go. There's an example of using the MC34063 DC-to-DC converter chip for a basic step-up configuration. Now, you can do step down or inverting and you can play around with the efficiency and just change and just use the for the different configurations, you just use the different formulas.

**Dave Jones:** They're only slightly different, slightly different circuit configurations. But, as you can see, I mean, yeah, it looks quite complex, right? But, it's not, really. Um, they're very basic calculations.

**Dave Jones:** You just need to go through the motions and do it, build up your circuit, measure it. Component selection's a big thing. You might, you know, you have to look at the peak current is one of the major things you need to choose an inductor which is suitably rated for your peak current, which has the lowest series resistance possible.

**Dave Jones:** So, the physically the bigger inductor should in theory have a lower series resistance, which will help with your efficiency. So, you know, in this case, 0.7 amps peak current calculated, well, you might choose a 2-amp in inductor and a 2-amp diode or something like that.

**Dave Jones:** But, you can play around to your heart's content. So, there you go. DC-to-DC converters pretty easy to design. And this is one of the more complex examples. There are simpler to use devices than the MC34063.

**Dave Jones:** This is, you know, these formulas are quite complex. Usually, they're a lot simpler because the chip takes care of a lot of the stuff and you might only have a very simple one-line formula for one of the other National Instruments chips or something like that.

**Dave Jones:** But generally, they're more expensive, they're more obscure, single source. I love the MC34063. It's just a basic chip. It's not by far the highest performance device out there. If you want the utmost in, you know, efficiency and low power and all sorts of stuff, go for one of the more obscure devices out there.

**Dave Jones:** But for a jelly bean part that does almost everything, it's beautiful. Keep some in your junk box and think about using it next time you want a simple DC to DC converter.

**Dave Jones:** It ain't that hard. See you.
