---
video_id: 8xX2SVcItOA
title: EEVblog #102 - DIY Constant Current Dummy Load for Power Supply and Battery Testing
url: https://www.youtube.com/watch?v=8xX2SVcItOA
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 38, "3": 51, "4": 62, "5": 71, "6": 93, "7": 110, "8": 136, "9": 145, "10": 170, "11": 184, "12": 196, "13": 213, "14": 225, "15": 242, "16": 252, "17": 262, "18": 277, "19": 293, "20": 307, "21": 318, "22": 326, "23": 355, "24": 370, "25": 391, "26": 403, "27": 421, "28": 431, "29": 444, "30": 460, "31": 468, "32": 488, "33": 507, "34": 520, "35": 534, "36": 548, "37": 560, "38": 578, "39": 590, "40": 605, "41": 619, "42": 635, "43": 644, "44": 658, "45": 680, "46": 704, "47": 728, "48": 743, "49": 759, "50": 767, "51": 782, "52": 807, "53": 822, "54": 839, "55": 858, "56": 872, "57": 884, "58": 899, "59": 912, "60": 937, "61": 949, "62": 962, "63": 977, "64": 991, "65": 1001, "66": 1016, "67": 1028, "68": 1049, "69": 1070, "70": 1086, "71": 1100, "72": 1109, "73": 1132}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it seems like I'm always designing a little switch mode power supply for whatever a project it is, for whatever purpose.

**Dave Jones:** And often you have to characterize these DC to DC converters, their performance, their efficiency performance, or just their performance over the entire load. From, you know, zero load up to say 1 amp, if the switch mode power supply is designed to deliver anywhere from zero to 1 amp.

**Dave Jones:** You have to characterize that. And how do you test it? How do you know? Sure, okay, you can hook on a bunch of different power resistors on the output and to simulate a different load, but that's a real pain in the ass.

**Dave Jones:** You got to have a big stock of power resistors, and it's just not nice. So, what's needed is an electronic load that you can just dial up whatever load you need to test out your power supply.

**Dave Jones:** And I thought it's about time I probably built one. So, I thought I would get some junk box components, see what I had lying around, and lash one up.

**Dave Jones:** And here's the result. Let's go through it. So, what's needed for a simple electronic load? Well, basically an electronic load is just a constant current sink. It's you need to dial in or select whatever constant current you want, and it will draw that constant current from the power supply regardless of the power supply's voltage.

**Dave Jones:** It can be, you know, 3 volts, 5 volts, 15 volts, 20 volts, whatever, and the load will actually adjust itself to extract that constant current. So, what would you think of when you're thinking about constant current generators?

**Dave Jones:** Well, you'd think about the classic circuit like the LM317. Normally it's a voltage regulator, but if you put a series resistor in there, an adjustable resistor, a pot, you can actually that actually becomes a constant current well, a in this case, a constant current generator, but if you just ground that output there, and hook this on into your power supply, bingo, it becomes a constant current load.

**Dave Jones:** But, it has certain disadvantages, this one. The resistor has to be a very low value. It can only be within a certain range to keep it stable. And there's other issues with it.

**Dave Jones:** And you need a big power wire around resistor. And you know, it's just not really a great solution, really. So, what I came up with is just a basic, a very standard building block circuit of a of a N-channel MOSFET I had lying around an MTP30 MOSFET.

**Dave Jones:** This is a logic level MOSFET, and it's important to get a logic level MOSFET, or something that operates down in this range. And it's basically hooked onto a standard LM324 as a series pass um transistor.

**Dave Jones:** And it's basically just a follower. So, any voltage on the input here, if you know your basic op amp theory, as you should, the op amp basically will keep these two input voltages the same.

**Dave Jones:** So, if you put 1 V in here, into the positive pin, it will do its thing, and adjust so that the other pin is also at 1 V. And if you have a resistor down here going to ground, that means that it will put 1 V across the resistor.

**Dave Jones:** In this case, I've chosen 1 ohm. 1 V across 1 ohm is 1 amp. So, basically, what you've got is an adjustable constant current load based on a voltage input here.

**Dave Jones:** Simple. Now, you may have noticed that I've got an extra voltage follower op amp here and a voltage divider and you don't really need that. You could just hook up a pot from say 0 to 5 volts, power your op amp from 5 5 volts and feed that straight in.

**Dave Jones:** But, I just happen to have a project board that I did a previous project with and it had the quad op amp there and it had it all wired up and everything.

**Dave Jones:** So, I just decided to just use an extra voltage follower I and actually divide that in half. So, if we've got a 5-volt power supply as I'll go into that's a 50k pot.

**Dave Jones:** That just gives you an adjustable voltage. I've used a 10-turn pot. Now, that's important because it allows you to give a very fine range. So, it means that I can adjust anywhere from like 1 milliamp up to an amp for example with 10 turns of the pots.

**Dave Jones:** If you've only got a single-turn pot, then you're going to get a very coarse adjustment. If you don't have a 10-turn pot, you can put a large value resistor in a small well, a large value pot and a small power value pot in series.

**Dave Jones:** So, you have a fine and a coarse adjustment. But, I had a 10-turn pot. So, it worked nice. So, it generates from 0 to 5 volts input on the pot and the voltage divider here just goes from 0 to 2 and 1/2.

**Dave Jones:** So, it it basically just allows me to go from 0 to 2 and 1/2 volts here is 0 and to 2 and 1/2 amps I can adjust with this particular circuit.

**Dave Jones:** But, the LM324 there's issues with it. Can't go to its supply rail and stuff like that. But, we won't go into that. Use a precision op amp if you want that sort of stuff.

**Dave Jones:** Rail-to-rail op amp and plus there's issues with the FET. But, anyway, I should easily be able to get 0 to an amp out of this particular circuit. Now, if you have a look at this characteristic curve for the MTP 3055 VL N-channel logic level MOSFET I'm using, you'll see that the Y axis is actually the gate voltage and the X axis is the output voltage or in this case the

**Dave Jones:** voltage across our load resistor, which is actually current. So, effectively the X axis is from 0 to 2 amps. Now, as you can see for a 0 for basically no load current at all, we require a gate voltage down around 1.5 V.

**Dave Jones:** Now, and for a um once again on the high end to get a 2 amp load current, we would we need a gate voltage of about 4 V. Now, our LM324 op amp, because it's been powered from 5 V and it's not a rail-to-rail output op amp, you most likely won't get that 4 V um output maximum.

**Dave Jones:** So, this circuit's probably not capable as it is of 2 V, but you might be able to get easily uh say 1.25 amps there, which is just over like 3.2 V or thereabouts.

**Dave Jones:** So, it should work quite well this logic level MOSFET. And I also thought it'd be quite neat to include a little panel meter as well on there to show me my uh set current, so that I didn't have to use my put my multimeter in series to actually measure the current.

**Dave Jones:** It just so happens in my junk bin I got a whole bunch of CX101 uh very nice little um three and a half digit uh panel meters, 0.1% accurate, really quite nice.

**Dave Jones:** They can be used in a ground configuration. The thing with these little panel meters, here they are, one of these little um you know, LCD panel meters you can buy for five or 10 bucks or something like that.

**Dave Jones:** This one's a bit more expensive, but some of them are not designed to be used for a common ground connection. So, you can't just hook them up and then power it from your 5 V up here into there and then share a common ground.

**Dave Jones:** Some of them will not work. It's a real trap for young players, so just be careful, but this particular one can be configured to work in a common ground configuration.

**Dave Jones:** And here's the actual circuitry as drawn in DaveCAD there. And as you can see, that's the input configuration for a divide by 10. So, because the panel meter is designed for 0 to 200 mV input, this will do from 0 to 2 V or 0 to 2 A.

**Dave Jones:** And so my display of 1999 will read directly in milliamps with a 1 ohm load. Nice. And check it out. Here's the finished design. It It actually looks quite nice because I just so happened to have an old PCB.

**Dave Jones:** It's a battery capacity logger design I worked on which had a little PIC microcontroller, and it happened to have just such the input configuration with the N-channel MOSFET and the op-amp here, and it was all pre-wired for me basically.

**Dave Jones:** And here's the load resistors which will go into. It had an RS232 interface, but basically this I already had it lying around, so that was pretty fortuitous. And here's the final built-up design.

**Dave Jones:** And there's the LM324 op-amp. Just some bypassing. It's got a 5 V input socket here because the panel meter happens to be a 5 V type. I've got my nice big 10-turn pot here.

**Dave Jones:** That's a 50k pot. It just goes in there. There's the divider resistors. And there's the N-channel MOSFET down in there, the MTP3055. And I've got 10 10 ohm 1% resistors.

**Dave Jones:** And the reason I did that, not only cuz I had the board, but to get a a an accurate It doesn't matter so much in this application, but if you're designing your own one to get an a 1% accurate 1 ohm load resistor is actually quite expensive.

**Dave Jones:** It's actually cheaper and simpler to get 10 10-ohm 1% actual power resistors. These are 1-watt resistors, much easier to get one of those, or half watt I think they are.

**Dave Jones:** Um much easier to get 10 of those, and cheaper and easier than to get one big single power resistor. So, there you go. We've got a nice big uh PCB mounted heat sink on here, which we'll go into, and that's the finished design, and it works quite well.

**Dave Jones:** I've got my panel meter hooked up, and on the back here I've just got the input uh the input resistors to set the um set the differential um input and and have the divide-by-10 ratio, but that's it.

**Dave Jones:** And here's the final design working. I've got the input here connected up to my power supply over there. It's about a 12-V um input at the moment, and I've dialed it up to 81 mA, and as you can see, the Gossett meter here is measuring the um input current from the power supply.

**Dave Jones:** And as you can see, it pretty it corresponds pretty well. And I go up, and it's upside down here. Sorry, the actual LCD display is up up the other way, so but my cable doesn't reach.

**Dave Jones:** But 244 mA, it's you know, it it works pretty well. So, and it goes all the way up to that's uh it's an amp at the moment, and no problems at all.

**Dave Jones:** It goes up to pretty much it's starting to max out there at 1.35 amps. So, there you go. That's about its maximum, and as you can see, the panel meters are quite um accurate there, and it can go all the way down to 1 or uh at least maybe can it do 1 mA?

**Dave Jones:** There we go. It can do 1.5 mA minimum, cuz that's basically 1 mA, because that's as low as the you know, the op amp's got some output um offset voltage there, and I can adjust that, you know even 5 milliamps I can tweak that and if I wanted a finer range from say 0 to 200 milliamps instead of 0 to 2 amps I would just adjust those divider resistors down

**Dave Jones:** there. Piece of cake so it works quite well. Thumbs up I'm happy with that. Now there's one thing to actually remember about these input panel meters if you don't use precision resistors on the input here I used I used just standard 1% resistors there was actually an of set of 16 millivolts so I had to actually tweak that value there I had to actually adjust it and put an extra one

**Dave Jones:** in series just to just to tweak just to trim it a little bit so I actually got zero on my display for zero current. Now one important thing you need to know is how much power you can dissipate in your heat sink here through your power MOSFET.

**Dave Jones:** Now let's go through the very simple calcs. Now I've said before that heat sink thermal calculations can get all messy and you don't want to get bogged down in the details but we can do some basic back of the envelope calcs that are going to be pretty close to what we're going to get.

**Dave Jones:** Now what you do is you look up the data sheet for this heat sink this is an avid thermal alloy brand and I've looked up the data sheet and it's 4.5 degrees C per watt.

**Dave Jones:** That's the spec you need to get for your heat sink. That means it will rise for for every one watt you put into this thing it will rise 4.5 degrees Celsius above the ambient temperature.

**Dave Jones:** That's the key above ambient whatever the current ambient temperature is. Now let's go through we've got our basic circuit here. Here's our power MOSFET okay we've got our load resistor here we've got our voltage in from our power supply and we've got a voltage across the resistor which we'll call VR here so we've got V in and VR and the uh current that we actually have.

**Dave Jones:** So, the power dissipated in the heat sink is going to be the input voltage minus the um minus the voltage across the load resistor here times the current flowing through it cuz there's nothing flowing into or out of the gate here.

**Dave Jones:** There's no gate current at all. So, all of the current flows through our power transistor. Now, uh let's assume that we want 1 amp, okay? So, we've got 1 V in here, which gives us 1 V across our load resistor of 1 Ω.

**Dave Jones:** So, that's 1 V. And let's say we have 12 V V in. Let's go through an example. If we have 12 V V in minus 1 V across our load resistor at 1 amp times 1 amp, then we're going to dissipate the power in the heat sink is going to be 11 W.

**Dave Jones:** Or and if you uh put that into the formula for the heat sink up here, bingo, we've got the heat sink will rise by 49.5° C above ambient for 11 W power dissipation.

**Dave Jones:** Easy. Out of curiosity, let's do a quick check to see what temperature rise we actually get in our real heat sink here. Now, I've got I've had 1 amp flowing through it for quite some time, okay?

**Dave Jones:** And I've got 12 V input voltage. There it is. So, we're dissipating the 11 W in our power resistor like that down there because we've got 1 V uh drop across our across our load resistor, as you can see, down here.

**Dave Jones:** If I can probe that, there's our 1 V drop across our power resistor. So, there's um 11 V times uh 1 amp in there. So, there's 11 W being dissipated.

**Dave Jones:** And that's quite hot to touch. So, let's get the temperature sensor and see what temperature it is. Okay, I've got my Fluke reference temperature probe here. As you can see, the ambient temperature is about 20°, and as per the calculations before, we said for 11 W into this heat sink, it should rise about 50°, let's say 50° C above ambient.

**Dave Jones:** So, we're looking for about 70° C. Ambient's 20 + 50°. Let's check it out. Okay, I've got my temperature probe on the heat sink, and as you can see, it's just a couple of degrees over 70.

**Dave Jones:** It's going to climb a bit more, but that's not bad. Confirmation of our back-of-the-envelope calculations. I like it. It's pretty good. And the FET we've used in our circuit here is a 60-V 12-A FET.

**Dave Jones:** So, it's actually capable of, you know, quite a decent load performance. And you can tweak the load resistor value, and you can tweak the op-amp power supply value, and all sorts of things to get to test almost any power supply possible.

**Dave Jones:** It's just a matter of I'm just specking it up, and you know, increasing the size of the heat sink, and changing the load resistor. Easy. And if you're wondering just what this original battery capacity logger board and circuit actually did, well, here it is.

**Dave Jones:** It's not too different to what we've been dealing with. It's the same circuit, but we add in an intelligent microcontroller, which is hooked up to a PC, so it can log things and do other stuff.

**Dave Jones:** But, by adding an intelligent micro, what you can do is you can generate different types of loads. You can generate constant current, constant power, constant resistance, or any type of pulse load you desire.

**Dave Jones:** And the way you do that is it's got a PWM output, which generates a voltage which simulates the pot that we had, and it has an ADC down here, which just measures the voltage across our sense resistor down here.

**Dave Jones:** And that allows the micro to, just with a simple bit of math, to generate constant power, constant resistance. I know constant resistance sounds a bit silly. You can just put a resistance there and actually, you know, a 5-cent resistor on the load, but hey, it allows you to do it under intelligent software control and all sorts of pulse loads and things like that.

**Dave Jones:** So, it's very flexible. Uh and if you've ever seen like a data sheet for a Energizer battery or something like that, they might have a battery capacity uh performance graph over that may um have constant power or a constant resistance load or constant current load or a pulse load over time to simulate a toy being turned on or off or something like that.

**Dave Jones:** And this circuit allows you to do something like that. Very versatile. So, there you go. From a couple of junk box parts, we've created a put together a pretty handy little uh constant current uh adjustable load there to test power supplies.

**Dave Jones:** And if you're testing a power supply, you might want to get a switch mode. You might want to get a graph of efficiency from 0 to 100% on the Y axis for a for versus load current, say from 0 to 1 amp.

**Dave Jones:** And you might actually get, you know, a response that looks, you know, something like that. It's going to peak at some particular current. It might It might be 100%.

**Dave Jones:** You'd have a damn good power supply if it was, but it might be, you know, 90% or something like that. And it might drop away there. And having a little um little constant current uh load like this, an adjustable DC load, just allows you to um graph uh power supplies, the efficiency of power supplies and all sorts of other stuff over whatever load you want.

**Dave Jones:** And I'll show you how to do that in a in a future blog episode. So, see you next time.
