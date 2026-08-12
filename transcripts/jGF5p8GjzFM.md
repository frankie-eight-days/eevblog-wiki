---
video_id: jGF5p8GjzFM
title: EEVblog #233 - Lab Power Supply Design Part 6 - LT3080 Testing
url: https://www.youtube.com/watch?v=jGF5p8GjzFM
source: youtube-asr
timestamps: {"0": 0, "1": 11, "2": 27, "3": 41, "4": 66, "5": 79, "6": 92, "7": 106, "8": 123, "9": 141, "10": 154, "11": 162, "12": 172, "13": 182, "14": 197, "15": 214, "16": 231, "17": 249, "18": 260, "19": 275, "20": 289, "21": 308, "22": 322, "23": 334, "24": 353, "25": 371, "26": 389, "27": 401, "28": 411, "29": 424, "30": 437, "31": 459, "32": 467, "33": 485, "34": 496, "35": 509, "36": 523, "37": 541, "38": 570, "39": 590, "40": 601, "41": 611, "42": 642, "43": 657, "44": 674, "45": 687, "46": 707, "47": 720, "48": 735, "49": 748, "50": 767, "51": 779, "52": 791, "53": 807, "54": 821, "55": 831, "56": 845, "57": 866, "58": 885, "59": 895, "60": 908, "61": 921, "62": 936, "63": 948, "64": 963, "65": 978, "66": 991, "67": 1010, "68": 1024, "69": 1043}
---

**Dave Jones:** Hi, just a quick aside on the power supply. A few people mentioned what happens if you say charging a battery with this power supply and you disconnect the input voltage while you still got that battery on the output.

**Dave Jones:** I mean, you're feeding a voltage back into the power supply and you switch off the input. What happens? Will the regulator blow? And this is quite a common scenario for a traditional linear power supplies and let's take a look at it.

**Dave Jones:** You've got your voltage regulator like this. You've got your input voltage, doesn't matter where it comes from. You've got the output voltage of your power supply. If you're feeding back in a supply from a battery, say you're charging it or something like that, and it's going back in.

**Dave Jones:** What happens if you've still got the output battery connected but you disconnect this input supply and well, you can blow up your regulator and a lot of power supplies will typically or traditionally have a reverse protection diode on there so you don't blow the pass transistor in the voltage regulator.

**Dave Jones:** And my design doesn't have that and I didn't include that because the none of the app notes for the LT3080 actually show that including their own lab power supply circuit.

**Dave Jones:** So I figure it's a new design, should be robust enough that it doesn't need that. But hmm let's test it. All right. Now what I've got here is I've got my power supply circuit built up.

**Dave Jones:** Not that we actually need the circuit itself because we're just testing the regulator effectively. But I've left the circuitry there as is. What I've got is I've got it hooked up to two external power supplies up here.

**Dave Jones:** This one here is the input supply and this one is feeding a voltage back out into the output of the voltage regulator. And what these meters are measuring, I've set the output voltage to 5 volts here, so that's the output voltage of our regulator.

**Dave Jones:** This is our input voltage of our regulator, and this is the current being fed back into the input from the external power supply just so we can monitor how much current's actually going back in when we switch this thing on or off and play with it.

**Dave Jones:** Now, of course, if I switch off my input voltage, I've got no input voltage here, and my output voltage is nothing, okay? I'm not so I'm not actually feeding in the output voltage.

**Dave Jones:** All right, so what I'm going to do now is I'm going to switch on this output voltage, so I'm feeding a voltage back into the regulator, and this will monitor the current.

**Dave Jones:** Remember, this is monitoring the output voltage of the regulator, so we should be able to force that output voltage higher than the 5 volts that it's trying to actually regulate.

**Dave Jones:** So, I'll switch that on now. I've got it set to 5 volts, so it doesn't really change at all because they're the same voltage, but let me wind that up a bit.

**Dave Jones:** And let's see if we can There we go. Bingo. I can actually I'm driving that output voltage from my external supply. My external supply is six Well, it's saying six point It's measuring 6.25, and sure enough, it is.

**Dave Jones:** There There it is. 6.26. So, I'm feeding in that external supply. Now, what happens? Let's actually Well, let Let's just leave it there. Let's say it's 6.2 volts. Doesn't really matter, and let's switch off our input voltage and see what happens.

**Dave Jones:** Here we go. And it's feeding eight milliamps back in, but it's doing it's doing nothing. There you go. We're still getting an input voltage being fed back through the regulator.

**Dave Jones:** So, even though our circuit is actually disconnected, if we have a look at our circuit here, this switch is actually disconnected and we're and we're measuring our input voltage, which is 5.57 because it's being fed back through the regulator.

**Dave Jones:** Remember, there there is no diode there at the moment. Okay, so we're feeding the voltage back in and well, let's see if that has killed it. So, I'll switch my input voltage back on.

**Dave Jones:** I'll switch my load voltage off. No, it's survived that quite well. Not a problem whatsoever. Let's wind the output voltage all the way up to Okay, I've got a 12-V input voltage.

**Dave Jones:** Let's wind the output voltage up to 12 as well. So, there you go. I've got 12-V output voltage and let's switch off let's switch that on and force the output voltage up to 12-V.

**Dave Jones:** Bang, we've done that. It's only feeding, you know, 10 milliamps back into the thing, but let's switch our input voltage off and bang, and our input voltage is still 11.3, but I've switched it off and let's see if it recovers.

**Dave Jones:** I'll switch the input voltage back on, turn off the output, and it's recovered. No problems at all. So, we haven't killed this thing. If you switch off the input voltage, not at all.

**Dave Jones:** All right, it's time to get a bit drastic. Instead of just switching this input voltage off, let's actually short it out to ground and see what happens. So, our output voltage is at 12-V.

**Dave Jones:** Let's force that on again. Bingo, there we go. We've forced our output voltage to 12-V with the external supply and not only will I switch off the input voltage, but I'll disconnect the leads from the power supply.

**Dave Jones:** They're the input leads and I will short them. And we'll probably see an increase in current here. Whoa, yeah. Bingo. Whoa. Oh, yeah. There was some smoke somewhere. You better believe it.

**Dave Jones:** Let's actually um switch the input voltage back on and see if we've killed the regulator. Nope. It's still fine. It survived that no problems whatsoever. Bang, we're forcing our output voltage to 12 volts and this time I'll probably hold it and see what happens.

**Dave Jones:** Oh, yeah. Look at that three Whoa, there we go. Hoho, what smoked? Check it out. And the poor little sucker there never stood a chance. Little quarter watt resistor.

**Dave Jones:** So, you actually saw it there. It was getting over 3 amps feeding back into that regulator. All of that current must have gone through the voltage regulator. There's nowhere in the LT3080.

**Dave Jones:** There's nowhere else for it to go. So, let's see if it's if it's killed it or not. I've disconnected the output and yeah, it's something's going on, but our current shunt resistor might have blown.

**Dave Jones:** Let me check that and see what's happening. Let's measure our current shunt resistor. Should be 1 ohm, but what? 7.5k. Dead as a dodo. Okay, I've replaced the shunt with a short.

**Dave Jones:** I didn't bother putting a 1 ohm resistor back in and let's switch the power input supply back on and hey, no problems whatsoever. The regulator survived just fine. So much for blowing the thing that was over 3 amps if I recall from that meter going back through the LT3080.

**Dave Jones:** And there's nothing wrong with it at all. It is a really, quite a robust device. You know, I'd probably have to take it to its extreme limits to actually see where it blows.

**Dave Jones:** Well, it seems we may have actually done some damage to it. I re-hooked it back up and tried to play around with it again and it was it was kind of working but the output was about 1.8 volts or thereabouts tracking 1.8 volts higher than the set pin voltage.

**Dave Jones:** So, I replaced the regulator and and now it's it's just fine. So, I'm not sure what happened there because it you know, it was working okay to begin with but then seems to have died.

**Dave Jones:** So, bummer. And there it is. It actually has a low of 3.86 volts and it goes up to a high of seven odd volts and that should be zero to five.

**Dave Jones:** So, that regulator, unfortunately, we have killed it. What? But that was a pretty extreme case though. I mean, you know, shorting shorting this input directly here was a little bit extreme.

**Dave Jones:** So, if we did actually have the diode in there, that would have shunted all of the current through the diode. And if you've got a big beefy, you know, five amp diode in there, it should actually handle that while actually preventing, you know, like a maximum voltage of like a volt across the regulator there.

**Dave Jones:** So, do we actually need a diode across here? Well, unless you somehow short out this or connect or this is connected through to the supply and you force your voltage to a much higher voltage which then can cause enough current to flow through the device and into your low impedance supply at the front end to actually kill the device, then the answer is no, not really.

**Dave Jones:** It doesn't It seems to survive quite fine if you simply just switch it off like that. And of course, if you go in, if you're feeding in big voltages from outside, then you've got other things to worry about like, you know, maximum voltage on your on your op amps and your other components that are supplied from this positive input voltage here.

**Dave Jones:** And well, if you wanted to solve that, then you'd have to have another regulator on the input here just to power all of your other stuff. So, you know, I don't know.

**Dave Jones:** As it As it stands, the answer is not really. And if you remember the internal block diagram of the LT1080, here it is. It's got the standard NPN series pass element here.

**Dave Jones:** So, when you feed in a a voltage from the output and your input is either floating or at grounded grounded potential, which it certainly could be if this capacitor is discharged and you input a voltage in here and you've got significant bulk capacitance on your input or your clamping it deliberately clamping it low for some overcurrent reason or something else, then you can get a reversed bias situation in

**Dave Jones:** your NPN transistor here. You can reverse bias your base emitter junction and you can actually blow that series pass transistor, not to mention any other internal circuitry in there.

**Dave Jones:** And if we take a look at a standard 78 series 7805 voltage regulator, you'll note it's basically the same thing. There's your series pass element NPN right there. And then this is like a Darlington configuration on the output here.

**Dave Jones:** And this is specifically the Texas Instruments data sheet for the 78 XX series and it specifically tells you reverse bias protection. Occasionally, the input voltage to the regulator can collapse faster than the output voltage.

**Dave Jones:** This can occur, for example, when the input supply is crowbar during an output over voltage condition. If the output voltage is greater than approximately 7 volts, the emitter base junction of the series pass element internal or if you're using an external series pass transistor for extra current, it can break down, it can be damaged.

**Dave Jones:** And and to prevent this, it's a standard industry practice to put a reversed biased diode in there which actually limits the voltage across the input and output differential on the voltage regulator.

**Dave Jones:** It's the same for the 7805 or for the LM 3080 and LT3080, sorry. So, whether or not you actually on this power supply designer, your own power supply design, put that reverse biased diode, it's up to you.

**Dave Jones:** I've it I was able to damage an LT 3080, but then it but it actually recovered after that serious 3 amp shorting. So, I'm not actually sure what happened to it after that.

**Dave Jones:** I'd have to do further testing more methodical to find out exactly how to actually break the thing, but it seemed actually to survive a fair amount. And if you don't short V in, then it survived 40 volts, no problems whatsoever.

**Dave Jones:** Whether or not your other circuitry connected to there would survive 40 volts, well, you know, that's up to your design. You could limit it with a Zener diode clamping or something like that.

**Dave Jones:** Or or you could have a Zener diode clamping on the output as well. If your output if you've got a 0 to 10 volt bench power supply, you might put say a 12 volt Zener on the output so that you can't get dangerously high voltages.

**Dave Jones:** So, you're going to blow your Zener before you're going to or the Zener should clamp anyway. You might blow it depending on the capability of the supply you're hooking up, but it's really hard to cater for all types of scenarios.

**Dave Jones:** If you're going to start applying you know large voltages to the output of your power supply, well, you're eventually going to break something. So, whether or not you put it in, I don't think I'll have it in my design.

**Dave Jones:** But, if people want to add it, that's up to them because configurations might be different. Or a better solution might be one of these TVSs or a transient voltage suppressor.

**Dave Jones:** They're also called transorbs and all sorts of other trademark names like that from various manufacturers. And they're basically a Zener diode, a high energy Zener diode to protect you against overvoltage conditions.

**Dave Jones:** And they're they're really nice. So, if you had say a 0 to 10-V power supply, you might say use a 12-V one of these to not only protect you from transient overvoltage conditions feeding back into your supply, but also basically for your negative protection as well.

**Dave Jones:** Because if we take a look at our circuit here, this D1 here, this diode, then if you replace that with a TVS instead of a Schottky diode, then you get the best of both worlds, high high voltage over protection and also reverse voltage protection as well.

**Dave Jones:** Well worth using one of those. And if we take a look at a data sheet for a typical NPN transistor, in this case we've only got a low power one.

**Dave Jones:** We've got a PNW222, also known as a 2N2222, which you're probably familiar with. Now, the thing we're concerned with here is the emitter base breakdown voltage which they specify.

**Dave Jones:** And you'll notice that it's not base emitter breakdown voltage, it's emitter base, which means that it's actually the the reverse voltage applied to the standard base emitter junction for an NPN transistor.

**Dave Jones:** In this case, it's only 6 volts. And as you saw in the LM 7805 data sheet, that was a very similar value as well. They said, you know, order of 7 volts.

**Dave Jones:** So, that that's really going to be the killer inside the device. Okay, one last thing. I've now got the regulator circuitry separated from the rest of the circuitry so I don't blow up the rest.

**Dave Jones:** And I'm going to wind the wick up on the output voltage. It's currently 12 volts. I'll wind that up and I've got a fixed resistor there actually with the 10 microamps through to give me a 5-V out.

**Dave Jones:** So, there's really nothing else connected on the input side and I'm going to force the output side up. So, let's switch that voltage off. There we go. And let's switch the output voltage on.

**Dave Jones:** There it is. Okay, so we're feeding in our output voltage and let's wind that up, shall we? Let's wind it up. And as you can see See, it's still you know, there's there's really nothing flowing into that regulator.

**Dave Jones:** So, I'd be surprised if there's any damage happening there at all. It's only a milliamp, 20 volts. We're really feeding a lot Well, 1 milliamp. We're really feeding a lot of voltage into this uh output uh pin.

**Dave Jones:** Let me tell you, 30 volts. My supply only goes up to 40. I think 40's the maximum voltage for the LT 3080. Don't quote me on that. But let's wind it up.

**Dave Jones:** And all the way to what my supply is capable of, 41 volts. Okay, there you go. Let's wind it back down, switch it off. And uh let's switch the power back on and see if we've done any damage at all.

**Dave Jones:** None whatsoever. Works just fine. It's a nice robust little device. I like it. Catch you next time.
