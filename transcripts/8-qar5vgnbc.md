---
video_id: 8-qar5vgnbc
title: EEVblog #224 - Lab Power Supply Design - Part 3
url: https://www.youtube.com/watch?v=8-qar5vgnbc
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 24, "3": 34, "4": 52, "5": 60, "6": 75, "7": 95, "8": 123, "9": 135, "10": 150, "11": 173, "12": 187, "13": 200, "14": 214, "15": 224, "16": 241, "17": 252, "18": 266, "19": 283, "20": 294, "21": 306, "22": 322, "23": 334, "24": 346, "25": 360, "26": 375, "27": 395, "28": 408, "29": 418, "30": 434, "31": 446, "32": 461, "33": 473, "34": 485, "35": 502, "36": 509, "37": 523, "38": 539, "39": 549, "40": 564, "41": 580, "42": 590, "43": 606, "44": 620, "45": 647, "46": 666, "47": 677, "48": 687, "49": 702, "50": 711, "51": 721, "52": 737, "53": 749, "54": 759, "55": 769, "56": 791, "57": 802, "58": 819, "59": 833, "60": 850, "61": 865, "62": 870, "63": 898, "64": 906, "65": 921, "66": 943, "67": 953, "68": 971, "69": 982, "70": 993, "71": 1004, "72": 1018, "73": 1030, "74": 1054, "75": 1077, "76": 1097, "77": 1126, "78": 1155, "79": 1170, "80": 1183, "81": 1193, "82": 1209, "83": 1228, "84": 1246, "85": 1256, "86": 1267, "87": 1289, "88": 1310, "89": 1319, "90": 1342, "91": 1355, "92": 1372, "93": 1383, "94": 1389, "95": 1398, "96": 1413, "97": 1424, "98": 1436, "99": 1451, "100": 1465, "101": 1487, "102": 1504, "103": 1515, "104": 1535, "105": 1547, "106": 1553, "107": 1565, "108": 1575, "109": 1586, "110": 1604, "111": 1618, "112": 1633, "113": 1658, "114": 1671, "115": 1679, "116": 1695, "117": 1710, "118": 1730, "119": 1743, "120": 1770, "121": 1785, "122": 1797, "123": 1810, "124": 1819, "125": 1829, "126": 1848, "127": 1858, "128": 1872, "129": 1883, "130": 1897, "131": 1911, "132": 1919, "133": 1936, "134": 1957, "135": 1966, "136": 1979, "137": 1996, "138": 2009, "139": 2032, "140": 2039, "141": 2049, "142": 2061, "143": 2080, "144": 2100, "145": 2116, "146": 2127, "147": 2142, "148": 2148, "149": 2167, "150": 2182, "151": 2198, "152": 2215, "153": 2223, "154": 2251, "155": 2271, "156": 2287, "157": 2301, "158": 2320, "159": 2334, "160": 2352, "161": 2363, "162": 2377, "163": 2391, "164": 2406, "165": 2426, "166": 2440, "167": 2451, "168": 2463, "169": 2478, "170": 2496, "171": 2510, "172": 2528, "173": 2541, "174": 2551, "175": 2566, "176": 2580, "177": 2593, "178": 2610, "179": 2629, "180": 2650, "181": 2658, "182": 2669}
---

**Dave Jones:** Hi, now it's time to build up the constant current power supply which I've described in the previous two episodes. I've got it up here on built on the breadboard and we'll take a look at it in depth and we'll see if this thing actually works.

**Dave Jones:** I hope it does. I expect it to and if not, well, I guess we'll have to fix it. I've got current and voltage pots here. These are only cheap crap single turn ones.

**Dave Jones:** I don't have any free 10 turn ones to hand. So, these will do. Good enough for testing. I've I've got my constant current load over here which you've seen described before.

**Dave Jones:** That'll help us test it. I've just got a resistor for a dummy load here which we can attach and do some testing. I've got the LT3080 mounted on a heat sink here which is the same heat sink I plan to use in my final design actually and let's go.

**Dave Jones:** Let's see if this sucker actually works. And here's the circuit we'll be using today. It's pretty much identical to the whiteboard. One that I've done in the last two videos.

**Dave Jones:** I've added a couple of things. I've added a limit lead on the output of the current limit comparator down here. So, when the output of the current limiter goes high and turns on the transistor and goes into current limit mode, it also lights an LED.

**Dave Jones:** So, we can visually see and if that happens really fast and you'll see should see some flicker on the LED there or something like that. Um. I've added a 2.5 volt voltage reference because a power supply is no and power supply is only as good as its voltage reference because that's where additional noise will come from.

**Dave Jones:** That's where it gets its absolute values from. I've used an LT1009 here. Slight overkill in this instance, but in the final design, it's like a 0.2% 2.5 volt voltage reference, but it will allow us to drive the voltage reference input of a PIC microcontroller or something like that which which we can use for our digital panel metering and we'll have to go into that in some further video.

**Dave Jones:** But today you can just use an LM336 or something like that. 2.5 volt voltage reference. Um we've got another dropper resistor in here to give our current range from 0 to 1 amp.

**Dave Jones:** And our voltage here I've added uh some gain here with these two resistors. Um so our gain should um so our final voltage that multiplies um that 2.5 by a value of uh that has a gain of 2.2.

**Dave Jones:** So that will be our maximum voltage output. And up here for our current shunt measurement, I've um actually matched these 10k resistors here. So I've picked ones out of my bin and I've physically measured them on the multimeter and actually matched them so they're within I don't know I'm not sure what it was but they're pretty close sort of you know plus minus two least significant digits or something.

**Dave Jones:** So much better than the standard 1% tolerance which is what these resistors are marked as. And the op amps we'll be using today are TLC2272s. You could use a quad op amp which is a 2274.

**Dave Jones:** This is just like a cheap uh a cheap sub 1 millivolt offset op amp. You could use like a you know a generic jelly bean LM324 or something like that.

**Dave Jones:** But realistically when you're talking about the current shunt measurement up here the voltage offsets probably going to be too uh too high for that. So you want to use a semi-precision type device here unless you want to tweak these values and put pots in and tweak it.

**Dave Jones:** Uh gets nasty. We don't want to do that. And we'll just go through the layout very quickly here. I've got my positive rail up the top here. I've got my negative rail all along the bottom.

**Dave Jones:** So all that bottom stuff is all ground. Um this is my uh voltage reference over here. This is my uh a constant current load, the LM334 here. And we have that's our our current limiting transistor.

**Dave Jones:** And that's IC1 and that's IC2. And that's our current shunt resistor there. It's only a quarter watt one, 1 ohm. So I don't have a 1 watt or 3 watt version.

**Dave Jones:** I have to go to Jaycar quickly to pick up a higher wattage one to measure some higher power stuff. But there's our output caps and there's our cap which bypasses the adjust pin on the LM3080.

**Dave Jones:** And that's about it really. Bypass capacitors on the ICs there. Input bypassing on the LM3080. That's about all. We've got our output LED here for the current limit. So that should light up and well, let's power this thing up and see how she goes.

**Dave Jones:** All right, let's power this thing up. I've got it powered from about 8 volts from an external supply over here cuz we're only going for a 5.5 volts or there about output range today.

**Dave Jones:** So let's flick it on and see what we get. Our meter over here, this is the output voltage. We've got nothing. Oh, our current limit led's on. Let's Ah yeah, the current limit the current limit's all the way down.

**Dave Jones:** That's why. So if we turn our current limit up, let's turn current limit up to maximum so we don't muck around. Our output voltage is 5. 5 volts. Yeah, that's because the pot the voltage adjust pot is at maximum.

**Dave Jones:** It seems to be working. I've got my constant current load set to minimum down here so it shouldn't be doing anything much if anything. And what do we go down to?

**Dave Jones:** Oh hey, we go down to 0 volts. What do you know? And there we go. That appears to be working just fine. I like it. I'm surprised that it does actually go down to zero there.

**Dave Jones:** I think our constant current load could have something to do with that. So, let's turn it up. I'm drawing 60 milliamps. Let's say draw 100 milliamps out of this thing.

**Dave Jones:** There we go. 100 milliamps. And let's adjust that voltage down again and see what see what happens here. We've still got uh No, we still it's still going to allow us to go down to zero there.

**Dave Jones:** I'm going to disconnect this constant current load. And without the load on there, it only goes down to 0.7 volts. And that's pretty much what I expected. Perfect. And let's actually remove that LM334 current source and see what we get at the minimum.

**Dave Jones:** There we go. It only goes down without that 1 milliamp current source, it only goes down to 1.59 volts. That's cuz there's no load at all on the output of the multimeter, which is a 10 megaohm input impedance.

**Dave Jones:** Now, let's check the output on the scope to see if it's clean, to see if it's oscillating or not. I've got set to 1 volt per division. We've got our maximum 5.5 volts output.

**Dave Jones:** And let's wind that down and uh I don't see any resemblance of any oscillation at anything during that range. Once again, we've got just the minimum load there. There's the 0.7 volts at minimum.

**Dave Jones:** But let's switch that to AC coupling on the input so that we can see wind it right down to 10 millivolts per division. And as you can see, it's nice and clean.

**Dave Jones:** Okay, so this is the output noise here. As you can see, 10 millivolts per division. No problems whatsoever. If we wind it right up, of Of the bandwidth of the scope, it gets noisier and noisier.

**Dave Jones:** And I haven't uh probed it, you know, it's a breadboard. So, we're just getting ballpark sort of noise thing noise figures here. And that was it that's at minimum voltage.

**Dave Jones:** Okay, that's at minimum output voltage, minimum load. Let's go maximum output voltage, minimum load. There it is there. No problems at all. And it jumps around, of course, cuz it's AC coupling.

**Dave Jones:** So, you'd expect it to jump around until it settles through the AC coupling input cap. And I like that. No complaints at all. It looks like it looks very clean, as you'd expect from a linear voltage regulator with a rated 40 microvolts output noise.

**Dave Jones:** In fact, I don't have the gear to measure 40 microvolts output noise. I'd have to roll my own amp and do all sorts of other things. And ah, gah, too hard.

**Dave Jones:** And if you actually want to see the difference, okay, I'm probing the output at the moment. We're at 10 millivolts per division. Let me probe the ground. So, I'm leaving the ground hooked up, but I'm now probing the ground of the circuit.

**Dave Jones:** As you can see, virtually no difference. As you'd expect with 40 microvolts output noise RMS. Now, let's do the same thing again at 250 milliamps, cuz that's in theory the limit of our quarter watt resistor there.

**Dave Jones:** We'll now be dissipating a quarter watt in that 1 ohm current sense resistor. I don't want to go over that until I get a bigger current sense resistor. So, we're drawing 250 milliamps.

**Dave Jones:** And then measuring the output noise. Again, let's go down to minimum. There you go. Even down at 0.0, this is our output voltage, of course. And And no problems whatsoever.

**Dave Jones:** And let's go right up to our 5.5 volts. No. It's It's perfect. It's working exactly as I expected in terms of uh output voltage regulation. I like it. Okay, now we'll check our basic current limit.

**Dave Jones:** Uh up until now we've had our current limit up on uh maximum, and we've had our Well, let's set our way we're going to test that is to set our output voltage to maximum.

**Dave Jones:** We get now 5.5 V out, and let's wind we drawing 250 milliamps constant current on the output, and let's wind our pot down until we start We should If it enters current limit, we should see that LED turn on, and this start to drop.

**Dave Jones:** As soon as we reach the limit, turn it down. Turn it down. Come on. Right, there we go. There we go. Just the point it starts to drop out.

**Dave Jones:** Now, if we measure the voltage on that pot, it should be 250 250 mV because if you look at our circuit here, our Here we go. If I get it in here, uh our current adjust pot down here to uh have our current limit at 250 mA, we expect 250 mV on that um pot there, which sets the threshold where it goes into current limit mode.

**Dave Jones:** So, if I tap the measure the center point of that pot, it should measure just either on or slightly over 250 mV. 262, bang. And when we turn it down, it's got to 250 uh three.

**Dave Jones:** There's a bit of error there. It started to go into current limit mode. Got a little bit of error there, but basically it's working. So, let's set this to 100.

**Dave Jones:** I'm not looking at the other one, and we should be pretty close to 100 down here, and we are. You know, there's going to be some error here. You know, 50 milliamps, 55.

**Dave Jones:** These basically should uh should match. And they do. So, constant current limiting is working. Okay, now what I'm doing is, uh, going to probe the output pin seven here of our current, uh, sense amp.

**Dave Jones:** And let's have a look at what that's doing when it enters current, uh, output, uh, current limit mode. I've got it, uh, set to 1 V per division here.

**Dave Jones:** And of course, it's not doing anything at the moment because it's it's not actually current limiting. But if we turn this pot down slightly, it'll enter, wait, there we go.

**Dave Jones:** Bang, it's just looks like it's jumped from there up to just under a volt, 0.8 V, and let's continue to turn that pot down and lower the current. And yeah, as you lower it, it looks like it's going up.

**Dave Jones:** And that's why our LED doesn't turn on cuz there's not enough voltage to switch on the, LED only when it gets to the, you know, way, only when it gets to about 2 V is it going to turn on our LED there.

**Dave Jones:** Now, clearly what you're seeing here is this, although it's still acting like a comparator, it's doing the job of a comparator, it's not strictly just going between one and zero in in the output.

**Dave Jones:** That's because it's in the feedback loop here via the, uh, current limit transistor, via the LT3080, via the, you know, current sense. It's all happening all in real time.

**Dave Jones:** And it's a it's linear, it's working in in a linear type, uh, region now in the feedback configuration. Now, if we actually disconnect the transistor from here and actually remove the loop there, the control loop, then, uh, we'll find that this, uh, device will actually switch like a comparator as you'd expect when we adjust the control pot.

**Dave Jones:** So, this is with the transistor in place, it jumps up to there, and then it does, you know, that's where it entered current limit, bang, and then it's works in a linear type region from then on.

**Dave Jones:** And if we disconnect the base of that transistor, gone. There we go, but we're still measuring the output. Bang. Our LED is on and it switches bang like a true comparator cuz there's no feedback happening there.

**Dave Jones:** So, clearly just trying to put the LED on the output of that comparator is is not a good idea. It's not going to work. We need some sort of other mechanism to keep that LED on when it enters constant current mode.

**Dave Jones:** Now, you might think that the solution to this current limit LED is easy. Aha, we've got a spare op-amp here. Why not just parallel these inputs up here, get rid of the feedback loop there, and put the LED straight on the output like that.

**Dave Jones:** Well, if you do that, it's going to be a problem and I'll show you why. Now, if we go into current limit mode here, so when it drops 250, watch the LED here.

**Dave Jones:** And bang, see it flashed on for a second. So, it it worked for a split second, but you continue it's in current limit mode, but the LED's not on.

**Dave Jones:** And it really only comes on when you get right down in the noise down in there. And the reason for that is because the input is so these inputs are so marginal, of course they're going to actually be equal very close to equal because that's the idea of the current limit loop is that it makes, you know, the output voltage of this exactly the same as the

**Dave Jones:** set current here by way of that loop. And if they're exactly like that, then well, it's it's, you know, it's going to be hit or miss whether it works.

**Dave Jones:** It depends on slight offset voltages and things inside the op-amp. That's bad design. So, we need another method. And as usual, the solution's pretty simple. All we want to do is just change the margin on this input just a smidge.

**Dave Jones:** So, what we want to do is lower the voltage on this non-inverting input just a tiny little fraction uh compared to what it is to the loop over here so that when we uh adjust this uh pot down and it gets just on the current limit, it's going to There's going to be some margin on these pins and this LED is going to switch on.

**Dave Jones:** So, this input, instead of being exactly the same as this input and having no margin, the non-inverting input will be slightly lower than this one up here. So, when the pot gets just right on the margin, bang, it'll switch on.

**Dave Jones:** Now, I've used a 10K and a 2 meg 2 here. That'll give us about 4.5 mV uh margin at a full-scale volt input and when you get at lower, you know, down at uh 0.1 V, it's only 450 uh microvolts or something like that, but it's just going to give it enough.

**Dave Jones:** So, let's try that out. I've I've added the um I've added the uh 10K in there, coming back in the op-amp, I've added the extra uh 2 meg 2 going to ground there.

**Dave Jones:** And well, let's try it. We're Let's get down to our margin here and watch this is our current limit. This is the output of our um op-amp of our current loop op-amp.

**Dave Jones:** And watch the LED. Watch the LED. It'll just switches on. We're not quite in current limit mode yet. Bang. So, it's it's just on the margin. But, check this out.

**Dave Jones:** It's not perfect. If we wind it down, it will actually go off because there's probably some noise on there which is causing us an issue and then it comes back on solid right down at the lower end of the scale.

**Dave Jones:** So, uh we're going to have to fix that one as well. So, let's replace that with a 470K and see if that's any better. Let's try it out. Yep, I like that.

**Dave Jones:** 470K it is. And of course, you can take that uh current limit output off to a uh digital pic uh input to your controller if you have one but of course if you have an intelligent controller and you're not using that pots like we are here today it is just the voltage current and you're using a digital controller like a pic or an Atmel or something else to actually

**Dave Jones:** drive to generate the voltages to drive the voltage and current it knows what voltage and current it's driving at and you would of course read the output voltage back off and you'd read the output current back off as well both of those then the microcontroller knows you don't need any of this current limit it knows that the output voltage has not matched what it set so therefore it must

**Dave Jones:** be in current limit mode or vice versa it just knows all of those values so it can figure it out itself quite easily. We'll just check that out LM334 is actually 1 milliamp and it is with our 68 ohm sense resistor there so not a problem let's just check that over the whole output voltage range.

**Dave Jones:** That's our output voltage there and it's still sticking with 1 milliamp and let's go let's drop it down. And you know it's only going to go down to about 0.9 before it Yeah there we go it's starting to starting to muck up now and the good thing is is that it's still drawing that half you remember from the data sheet from the previous thought that it would get down to

**Dave Jones:** about it would still be drawing half a milliamp about 0.8 volts or of thereabouts I think we said and I just wanted to point out that up until now my output capacitance here although the data sheet says 2.2 microfarads minimum to make it stable I'm only actually using one microfarad not even using a ceramic either as as recommended so it's cuz I don't actually have a a you know a normal 2.2 micro farad

**Dave Jones:** ceramic to hand. So it's just fine with that output capacitance and we can add some more later and stuff like that. We'll play around with that. But no, it seems to be quite good and let's actually remove the output capacitance all together and see what happens.

**Dave Jones:** Okay, that's with no output capacitance at around about 2 volts and as you can see it's a lot noisier than what we're getting before and let me put on a point 47.

**Dave Jones:** Bang. And we'll just go down to our 10 millivolts per division AC coupled. That's with the point 47 microfarad bypass cap on there. That's by the way this is at 0.2 amps load.

**Dave Jones:** By the way, I am driving 200 milliamps. So let's remove it and bang. There you go. It does that's with no output capacitance. It really does not like that at all as you'd expect for a low drop out voltage regulator like this.

**Dave Jones:** So it seems to be stable but you know at high you'd have to test it at higher current but of course you wouldn't just as good design practice putting anything less than the recommended 2.2 microfarad ceramic output capacitance but even point 47 seems to work fine at at about a quarter of an amp.

**Dave Jones:** Okay, let's test the drop out voltage at no load. So there's no load on the output. The output voltage is at maximum at 5.5. Let's tweak it down to if we can to 5.50 just as a nice round number.

**Dave Jones:** It's a bit hard with these single turn pots really dicky. That's why you need a 10 turn pot. Let me tell you any good lab power supply should have 10 turn pot.

**Dave Jones:** I breathe on that. Fart halfway across the room and that thing's going to change. Okay, this is our input voltage. This is our output voltage. The green is the input voltage here on the scope.

**Dave Jones:** The yellow is the output voltage down there. The red ground reference is right on the bottom graticule down there. And let's wind the input down until we start either seeing Well, we probably won't see it oscillate, but until we start seeing that drop there.

**Dave Jones:** Up. Is that it? Yep, there we go. So, Woah. So, we're talking 1.25 V or thereabouts drop out voltage at no load. And if you're curious to see the drop out voltage at an amp here, this is our input voltage I'm probing that directly on the input pin of the LT 3080.

**Dave Jones:** So, that's bypassing all the wiring on the breadboard and stuff like that. And I'm measuring the output directly on the pin as well. And that's still the output noise there.

**Dave Jones:** So, let's wind the input down. And see where the output starts to drop. There we go. Around about 6.8 V by the looks of it. Yep, about 6. 6.85 6.9 V.

**Dave Jones:** So, that's about 1.35 to 1.4 V drop out voltage. And is that what we expect? Well, let's have a look here at the drop out voltage minimum because the V control pin, remember it's not the quoted specs cuz we've tied the V control pin and V in pin together.

**Dave Jones:** And sure enough, at an amp up here at junction temperature, well, we're going to be above 25°. Let's go up to 50°. You know, we're about 1.4 V. So, yep, it's pretty much agrees with the data sheet as you'd expect.

**Dave Jones:** Now, one thing we really want to check is the power up performance of this because the power up performance of any bench power supply is very important. You don't want it to uh overshoot.

**Dave Jones:** If you've got your output voltage set to 5 V, you don't want a big spike like that and then it to, you know, level back down at 5 V.

**Dave Jones:** You want it to ramp up nicely and then go rock steady at 5 V. Now, let's have a look here and try and predict what's actually going to happen here.

**Dave Jones:** Now, uh the input voltage up here is pretty much it technically it's going through an RC filter here with the current shunt resistor, but it's negligible, really. So, it's a So, the voltage is going to go straight through to power the uh LT1080 straight to the output.

**Dave Jones:** There's no uh there's no capacitance um around our voltage adjust pot or anything like that um or our voltage reference. So, that's going to power straight up instantly power the pot instantly.

**Dave Jones:** This op amp's going to turn on instantly and it's going to try and drive the set pin of the LT1080 instantly. Assuming our constant current uh control is set all the way to maximum, of course.

**Dave Jones:** Um now, BUT WE'VE GOT THIS MASSIVE 22 microfarad here with these uh with this 2K series resistance here total. Cuz remember that transistor's not going to uh switch on during um unless there's current limit.

**Dave Jones:** So, that basically does not exist. So, uh our turn-on RC time constant is going to be there. These two series resistors plus this cap. We're going to see this thing uh ramp up and um and go to the output.

**Dave Jones:** But, because that's actually in an active uh feedback loop and we're actually driving this with an op amp, um it's not it's uh going to actually charge uh faster than our uh if we Say if we set our output voltage to a volt, then it's going to charge up much faster than you'd expect based on that RC RC time constant.

**Dave Jones:** So, let's uh power this thing up and um and actually capture that on the digital scope and see if that's confirmed. Now, what I've got here is uh the yellow trace here is the uh output uh voltage and I've set that to 5 V and we're at uh 1 V per division, as you can see.

**Dave Jones:** Spot on 5 V and the green trace here is actually the um output from the op-amp here, pin seven, that actually uh drives that. And as you can see, it's significantly higher.

**Dave Jones:** And the reason for that is uh fairly obvious. Not only do we have the 10 microamps current flowing through there, which will give us a slight uh drop across there, but we have also these values here, the uh feedback resistor and uh the gain setting resistors here are fairly low value uh compared to these.

**Dave Jones:** So, there's going to be uh some output current flowing through there and some drop across there. But because the feedback tap is there, it uh takes care of any extra current flowing through there.

**Dave Jones:** That's why there's that difference. So, uh we're going to have a look at these and we're going to capture these two points uh when the circuit powers on. I've got it into no load.

**Dave Jones:** So, this will just be switching on into no load with say a 7 1/2 or 8 V input voltage. So, to do that, we're going to set our trigger point to about a volt there.

**Dave Jones:** We're going to um have it uh on the uh positive edge. We're triggering off channel one, which is our output uh voltage. So, on the rising edge, as soon as it gets to a volt, we're going to uh trigger that.

**Dave Jones:** Let's set it to 50 milliseconds per division or so. Let's switch the voltage off. Let's uh trigger that. Put it into single shot mode. And uh let's give it a go.

**Dave Jones:** Here we go. Bang! I switched the power on and you can see it ramp up. Ooh, what's that down there? That's interesting. And uh you can see the output of the uh op-amp uh go up like that and then come back down when it starts to regulate like that.

**Dave Jones:** And that's a very clean response. I like it. There's no overshoot or anything. There's We'll have a look at this thing down here later, but uh basically all we care about with switch on power supply is that it ramps up cleanly and doesn't overshoot and this one doesn't overshoot at all.

**Dave Jones:** It ramps up like that almost linearly and then it clamps into into voltage regulation like that. Our op-amp response of course it's it's got to do things cuz it's an active loop there and it's trying to stabilize itself and it comes down like that.

**Dave Jones:** Now, this looks kind of linear but it's not. That's actually going to be the the exponential uh a curve caused by this RC here, but it's but you'll find that it's time constant is going to be a lot faster than if than what you'd expect from zero.

**Dave Jones:** If you do the math from zero to 5 volts. And why is it going to be quicker? Well, that's a good question. It's because it is not power it's not going to be 5 volts here instantly.

**Dave Jones:** This op-amp is going to be higher than that and as you can see the op-amp right there suddenly went wham right up to there and then started to go up like that.

**Dave Jones:** So, that's going to affect the output voltage is higher than 5 volts there. So, it's going to charge that capacitor quicker than what you'd expect. And if we lower the output voltage, I think we'll find that that will look even more linear because you're right down in this curve there.

**Dave Jones:** So, let's give that a go. All right, I'll set my output voltage at a volt. So, let's do five let's do 200 millivolts per division. So, that will end up ramping up to the same value there, but I think you'll find it's going to be pretty linear.

**Dave Jones:** Let's capture that again single shot mode and whoop we're ready to go. Here we go. Bang! There it is there and we can actually see that if we zoom in on that, yeah, look that is that looks linear but that is actually the start of the um exponential RC curve.

**Dave Jones:** It's because that active op-amp there is driving it faster than a normal RC curve. Now, this little bit here is is interesting. What's that? That's 200, 400, 600, 700 mV.

**Dave Jones:** Aha. That 700 mV um happens to be the same as what our regulator is capable going down to with no load. So, there's some turn-on mechanism there internally to the LT3080 device that uh that causes that sort of jump up there and then flat for a little bit.

**Dave Jones:** But, if you follow that curve down there, I think you'll find that that will intersect precisely down the bottom like that. So, it's got this little knee characteristic uh switch on like that, but it's not a problem because it doesn't overshoot cuz our output voltage is 1 V.

**Dave Jones:** And there's no over There's a tiny little bit of overshoot in there. There's not, you know, it's nothing to worry about at all. So, it's nice and clean turn-on really.

**Dave Jones:** I don't mind that at all. Now, I've switched it back to our 5 V output voltage here, exactly what we're getting before. And just to demonstrate, uh we'll see if we can demonstrate that uh faster ramp-up time due to the uh op-amp there.

**Dave Jones:** What I'm going to do is I'm going to temporarily move this uh sense point back to here and then power up power it up and uh see what we get.

**Dave Jones:** And I think you'll find that the time constant will be longer and match the math exactly for 1 K and 22 microfarads. All right, let's give it a go on exactly the same time base.

**Dave Jones:** So, I've got my power switched off. Let's single shot that and let's turn it on. Bang. There we go. And you can see that the output of the op-amp has just switched on instantly like that as you'd expect because there's no RC time constant in the feedback loop anymore.

**Dave Jones:** So, it just bang it due to op-amp action. This output here instantly becomes this input here. So, it ramps up to there and bang 5 volts and this is your RC time constant.

**Dave Jones:** But, you've still got this little knee here due to the that's probably due to the constant current source in there perhaps something like that. So, that's still causing that little knee.

**Dave Jones:** But, as you can see the RC time constant changed. That was so much fun. Let's do it one more time backwards. We'll switch it off. Going to single shot mode, switch it back on and bang there we go.

**Dave Jones:** Much faster rise time but still that exponential curve. As you can see the slight curve in there and the op-amp of course has to compensate for it all now hence all that crap in there.

**Dave Jones:** And you can see that the output of the op-amp rings a little once it hits that point and it goes bang straight down. There's a little bit of undershoot and recovery there and that's but I like it.

**Dave Jones:** Powers on cleanly as far as I'm concerned. Now, I know what you're thinking. 22 mic do we need it that high? What if we change it to slide a 100 n?

**Dave Jones:** Cuz we do need some capacitance on there just to lower the output noise and we'll need it for our current limit as well as we'll probably find out in some further testing but let's lower that to 100 n.

**Dave Jones:** See what happens at switch on. So, let's take out the 22 and we'll put in the 0.1 mic in there. And uh that should work. A treat. Let's see what happens when we switch it on.

**Dave Jones:** All right, I'm going to keep the same uh time base there as we had before, 20 milliseconds per division. Let's go into single shot mode. Let's switch this sucker on and I think it'll turn on.

**Dave Jones:** Well, it definitely will turn on much quicker. Bang. Look at that. Woohoo. Check out the ringing on the op amp. It's trying to recover there, but the switch on is actually quite clean.

**Dave Jones:** Still very little overshoot there and that's at a 5-V output, but there is, you know, it's I, you know, it's not as nice. I don't like it. I don't like all that ringing and and and all that decay on the op amp like that.

**Dave Jones:** I think I much preferred the It was a bit smoother with the 22 mic, but that's a 100 n for you. Now, it might be tempting to use that 0.1 mic there and have a faster switch on.

**Dave Jones:** Who cares what the op amp's doing? The output, you know, it's not too bad at all. Well, let's try to see what happens in current limit mode. And to capture that, we'll change our trigger to up just below the 5-V level there and we'll trigger on the negative slope because when it goes into constant current mode, the output voltage is going to fall and well, let's try that

**Dave Jones:** and see what we get. I've put the 22 microfarad back in, so this is our normal circuit configuration now. All right, we'll see if we can capture it going into constant current mode.

**Dave Jones:** Now, we're exactly the same before as before. The yellow is the output voltage at 5 V and the green is the output of the hour our control op amp.

**Dave Jones:** Now, I'm going to turn the the pot the current pot down so that the Well, let's go into single shot mode. Okay, I'll set my trigger below there and I'm going to turn my current pot down.

**Dave Jones:** I've got no load, but it will actually switch on right down at the low end when it hits zero. Bang. There it is. And you can see the, um, exponential uh, discharge due to you guessed it, um, this resistor R2 here.

**Dave Jones:** Because when it goes into constant current mode like that, bang, it, uh, switches on this transistor, which then discharges this 22 microfarad cap through that 1K to ground. And, uh, that's taking about, uh, 10 20 30 40 50 milliseconds or so there to switch that off.

**Dave Jones:** So, we can actually tweak the value of, uh, that 1K. You wouldn't want it any higher, but, uh, we could, uh, certainly, uh, lower that, um, almost down to, well, effectively down to zero so that we can, uh, short, uh, short out the cap directly and, uh, get that fast turn on.

**Dave Jones:** But it seems, uh, very well-behaved, uh, in, uh, current, um, in in switchover to constant current mode. So, let's try that again. But this time I've got a, uh, 1 V output.

**Dave Jones:** So, I've changed my volts per division and my trigger, uh, point. And we're got, uh, driving 100 milliamps, uh, into a load. So, let's turn our constant current pot and bang, that's what we get.

**Dave Jones:** But you'll find, I think, that that, uh, wiggling there was me, uh, turning the pot. Let's see if I can, uh, do it a bit quicker. So, let's try it again.

**Dave Jones:** Single shot. Bang. There we go. And let's do it slowly again. Here we go. Bang and yay. That's me actually turning turning the pot there. So, bang, that's as fast as I can turn it, pretty much.

**Dave Jones:** And you see the op amps, uh, doing some business there, but, uh, the output, uh, just drops very smoothly and very cleanly. All right, I've changed R2 there to 100 ohms, dropped it by an order of magnitude, and let's, uh, see what we get.

**Dave Jones:** Once again, you can see the op amp oscillating in there. And if we actually zoom right in on that, you can see that it is actually oscillating like that, doing its thing, but that doesn't manifest itself on our output here.

**Dave Jones:** Our output is dropping very smoothly because we've got the 22 mic cap on there, but let's drop that capacitor, as we mentioned way back, down to 100 n, and see if we get a similar response.

**Dave Jones:** So, we now have a 100 R in there with a 100 n in there where where 1 V output with a 100 mA load, and let's give that a go.

**Dave Jones:** Let's go into constant current mode, turn our pot. Bang. And this is rather interesting. Look, that the the output voltage the yellow trace looks fairly clean, but when we zoom in, it goes up, and you can see that there's noise following in there like that, and I think that is possibly because we're in high res mode.

**Dave Jones:** So, let's actually switch off high res mode, and we'll try that one more time. Bang. There we go. It's exactly the same. So, that is a disadvantage. You can see the rolling average done in high res mode on the scope.

**Dave Jones:** Bit of a trap for young players, that one. Now, I'll put my 22 microfarads back in, and let's give that a go. Bang. Look at that. See? So, it is much cleaner, much cleaner response with the 22 microfarads.

**Dave Jones:** And you can see that live here, too, with the uh 100 n. There it is. As I turn it down, bang. Look at that. Terrible. And with no capacitor at all, by the way, it's an absolute shocker.

**Dave Jones:** You don't even want to go there. So, put that 22 mic back in. Bang. Clean as a whistle. Look at that. And there you go. Not a problem. And I've put it to AC coupling 10 mV per division, and that's the noise.

**Dave Jones:** If I adjust it, I'm adjusting the pot there. So, you see the AC That's in voltage mode, and we switch to current mode. Bang. Exactly the same noise. All right, we'll measure this switch off transient now.

**Dave Jones:** I'll set up a current for 250 mA. There we go. We've got 250 mA running on there. And this is our output AC coupled 50 mV per division. And the green trace again is our is our control op amp output.

**Dave Jones:** So, let's trigger that and just disconnect the load. I know this isn't ideal. Normally, you'd electronic switches. But, we'll just disconnect that real quick and bam, there it is.

**Dave Jones:** And you can see how it's immediately switched off there. There's a bit of high frequency stuff there as you'd expect. And then it boop, ramps back down, and then it kicks in, and the op amp kicks in and controls it all, and all settles back down nicely.

**Dave Jones:** But, that's 50 mV per division. So, that's only jumped 50 mV there for a quarter of an amp output current. And of course, that's with our 1 microfarad output capacitance.

**Dave Jones:** Let's change that. Let's actually add some extra capacitance in there. I'll get an extra 47 microfarads, and I'll whack that on the output, and see what difference that makes.

**Dave Jones:** Here we go. Didn't even trigger. There we go. We're Looks like we have to lower our trigger there. Let's try it again. And bang, there we go. Much smaller output transient this time cuz we've got greater output capacitance.

**Dave Jones:** But, as I mentioned in the previous video, it's a bit of a trade-off. You can't have an infinite amount of output output capacitance cuz then it when it switches into constant current mode, all that energy from the output capacitance can be dumped into the load before it has time to regulate the current.

**Dave Jones:** So, probably not a good idea. And we'll check the load when we do the switch on transient. So, we want to set our trigger signal below like that. So, because we expect it to drip down like that.

**Dave Jones:** 50 mV per division. So, let's set it down there. And let's disconnect our load. And here we go. We're going to connect our load real quick. And bang, there we go.

**Dave Jones:** There's our switch on transient. 100 mV, uh round about two divisions. And then you can see the op amp recovering there. And stabilizing. And of course, that was with the 1-microfarad output capacitance.

**Dave Jones:** Let's uh try it again with the 47-microfarad. And uh Oh. There we go. We've got a lot a whole bunch of noise this time, but the transient's not as large as before.

**Dave Jones:** Let's try that again. There we go. So, it's uh a little bit smaller than before. Now, set my output to maximum here, and it should be 5.5 V, but it's not.

**Dave Jones:** And once again, another trap for young players, it depends on where you actually measure that voltage. I've got the ground reference over here on this side of the load, but I'm actually uh attaching the uh I'm actually measuring the load voltage right on that right on that resistor there.

**Dave Jones:** Now, the problem with that is is that the burden voltage in my multimeter is in place there plus plus the plus the voltage drop in the wiring and the breadboard and stuff like that.

**Dave Jones:** So, if I disconnect that, it's a little bit hot and I connect it straight onto the tab of my TO220 device, I think we'll find it's exactly 5.5 V.

**Dave Jones:** Bang, there it is. So, that drop is in your breadboard and and your wiring and your burden voltage. Just be careful. Okay, I've replaced the current shunt resistor with just a jumper link to get us greater output current capability.

**Dave Jones:** I've currently got it set to just over an amp and there's our output noise. Not a not a problem at all. We're still getting a 5. 48 V out maximum and I can wind that wick up a bit.

**Dave Jones:** Of course, things are starting to warm up a tad now and it is rated to uh this, but now we're going a bit over. Starting to see some funny business now, are we?

**Dave Jones:** Maybe the uh thermal overload's kicking something's kicking in, perhaps. Yeah, there we go. Our output's dropped to to 2 V. It's dropped out. Bang. But, there you go. It actually recovers at 1.2 amps.

**Dave Jones:** Not a problem. I like it. And just for fun, we'll measure that heat sink temperature. We'll be at the 1 amp It's about 28.5 29° ambient here in the lab and let's uh let's probe that case and see what it's at.

**Dave Jones:** Okay, it looks like it's settling at about 43.5°. And the heat sink itself is at about 41.5° C. So, there you have it. There's some basic really rough and ready tests, not sort of really precision power supply measurements at all, but I I think it passed with uh, flying colors on the uh, breadboard.

**Dave Jones:** It pretty much uh, worked as expected. I'm happy with that. So, I might have to get on to uh, laying out the board and building this thing up um, for the final project.

**Dave Jones:** And uh, I'll eventually uh, show that one. So, um, I guess it's to be continued. And there might be some more uh, performance checks and other things on this, but anyway, hope you enjoyed that.

**Dave Jones:** See you next time.
