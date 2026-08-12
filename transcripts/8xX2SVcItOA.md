---
video_id: 8xX2SVcItOA
title: EEVblog #102 - DIY Constant Current Dummy Load for Power Supply and Battery Testing
url: https://www.youtube.com/watch?v=8xX2SVcItOA
source: youtube-asr
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it seems like I'm always designing a little switch mode power supply for whatever a project it is, for whatever

**Dave Jones:** purpose. And often you have to characterize these DC to DC converters, their performance, their efficiency performance, or just their performance over the entire load. From, you know, zero load up to say 1 amp, if the switch mode power supply is designed to

**Dave Jones:** deliver anywhere from zero to 1 amp. You have to characterize that. And how do you test it? How do you know? Sure, okay, you can hook on a bunch of different power resistors on the output and to simulate a different load, but

**Dave Jones:** that's a real pain in the ass. You got to have a big stock of power resistors, and it's just not nice. So, what's needed is an electronic load that you can just dial up whatever load you need to test out your power supply. And I

**Dave Jones:** thought it's about time I probably built one. So, I thought I would get some junk box components, see what I had lying around, and lash one up. And here's the result. Let's go through it. So, what's needed for a simple electronic load?

**Dave Jones:** Well, basically an electronic load is just a constant current sink. It's you need to dial in or select whatever constant current you want, and it will draw that constant current from the power supply regardless of the power supply's voltage. It can be, you know, 3

**Dave Jones:** volts, 5 volts, 15 volts, 20 volts, whatever, and the load will actually adjust itself to extract that constant current. So, what would you think of when you're thinking about constant current generators? Well, you'd think about the classic circuit like the LM317.

**Dave Jones:** Normally it's a voltage regulator, but if you put a series resistor in there, an adjustable resistor, a pot, you can actually that actually becomes a constant current well, a in this case, a constant current generator, but if you just ground that

**Dave Jones:** output there, and hook this on into your power supply, bingo, it becomes a constant current load. But, it has certain disadvantages, this one. The resistor has to be a very low value. It can only be within a certain range to keep it stable. And

**Dave Jones:** there's other issues with it. And you need a big power wire around resistor. And you know, it's just not really a great solution, really. So, what I came up with is just a basic, a very standard building block circuit of a of a

**Dave Jones:** N-channel MOSFET I had lying around an MTP30 MOSFET. This is a logic level MOSFET, and it's important to get a logic level MOSFET, or something that operates down in this range. And it's basically hooked onto a standard LM324

**Dave Jones:** as a series pass um transistor. And it's basically just a follower. So, any voltage on the input here, if you know your basic op amp theory, as you should, the op amp basically will keep these two input voltages the same. So, if you put 1 V in

**Dave Jones:** here, into the positive pin, it will do its thing, and adjust so that the other pin is also at 1 V. And if you have a resistor down here going to ground, that means that it will put 1 V

**Dave Jones:** across the resistor. In this case, I've chosen 1 ohm. 1 V across 1 ohm is 1 amp. So, basically, what you've got is an adjustable constant current load based on a voltage input here. Simple. Now, you may have noticed that I've got

**Dave Jones:** an extra voltage follower op amp here and a voltage divider and you don't really need that. You could just hook up a pot from say 0 to 5 volts, power your op amp from 5 5 volts and feed that

**Dave Jones:** straight in. But, I just happen to have a project board that I did a previous project with and it had the quad op amp there and it had it all wired up and everything. So, I just decided to just

**Dave Jones:** use an extra voltage follower I and actually divide that in half. So, if we've got a 5-volt power supply as I'll go into that's a 50k pot. That just gives you an adjustable voltage. I've used a 10-turn pot. Now, that's important

**Dave Jones:** because it allows you to give a very fine range. So, it means that I can adjust anywhere from like 1 milliamp up to an amp for example with 10 turns of the pots. If you've only got a single-turn pot, then you're

**Dave Jones:** going to get a very coarse adjustment. If you don't have a 10-turn pot, you can put a large value resistor in a small well, a large value pot and a small power value pot in series. So, you have a fine and a

**Dave Jones:** coarse adjustment. But, I had a 10-turn pot. So, it worked nice. So, it generates from 0 to 5 volts input on the pot and the voltage divider here just goes from 0 to 2 and 1/2. So, it it basically just

**Dave Jones:** allows me to go from 0 to 2 and 1/2 volts here is 0 and to 2 and 1/2 amps I can adjust with this particular circuit. But, the LM324 there's issues with it. Can't go to its supply rail and stuff

**Dave Jones:** like that. But, we won't go into that. Use a precision op amp if you want that sort of stuff. Rail-to-rail op amp and plus there's issues with the FET. But, anyway, I should easily be able to get 0

**Dave Jones:** to an amp out of this particular circuit. Now, if you have a look at this characteristic curve for the MTP 3055 VL N-channel logic level MOSFET I'm using, you'll see that the Y axis is actually the gate voltage and the X axis is the

**Dave Jones:** output voltage or in this case the voltage across our load resistor, which is actually current. So, effectively the X axis is from 0 to 2 amps. Now, as you can see for a 0 for basically no load current at all, we require a gate

**Dave Jones:** voltage down around 1.5 V. Now, and for a um once again on the high end to get a 2 amp load current, we would we need a gate voltage of about 4 V. Now, our LM324 op amp, because it's been powered

**Dave Jones:** from 5 V and it's not a rail-to-rail output op amp, you most likely won't get that 4 V um output maximum. So, this circuit's probably not capable as it is of 2 V, but you might be able to get

**Dave Jones:** easily uh say 1.25 amps there, which is just over like 3.2 V or thereabouts. So, it should work quite well this logic level MOSFET. And I also thought it'd be quite neat to include a little panel meter as well on

**Dave Jones:** there to show me my uh set current, so that I didn't have to use my put my multimeter in series to actually measure the current. It just so happens in my junk bin I got a whole bunch of CX101

**Dave Jones:** uh very nice little um three and a half digit uh panel meters, 0.1% accurate, really quite nice. They can be used in a ground configuration. The thing with these little panel meters, here they are, one of these little

**Dave Jones:** um you know, LCD panel meters you can buy for five or 10 bucks or something like that. This one's a bit more expensive, but some of them are not designed to be used for a common ground connection. So,

**Dave Jones:** you can't just hook them up and then power it from your 5 V up here into there and then share a common ground. Some of them will not work. It's a real trap for young players, so just be

**Dave Jones:** careful, but this particular one can be configured to work in a common ground configuration. And here's the actual circuitry as drawn in DaveCAD there. And as you can see, that's the input configuration for a divide by 10. So, because the

**Dave Jones:** panel meter is designed for 0 to 200 mV input, this will do from 0 to 2 V or 0 to 2 A. And so my display of 1999 will read directly in milliamps with a 1 ohm load. Nice.

**Dave Jones:** And check it out. Here's the finished design. It It actually looks quite nice because I just so happened to have an old PCB. It's a battery capacity logger design I worked on which had a little PIC microcontroller, and it

**Dave Jones:** happened to have just such the input configuration with the N-channel MOSFET and the op-amp here, and it was all pre-wired for me basically. And here's the load resistors which will go into. It had an RS232 interface, but basically

**Dave Jones:** this I already had it lying around, so that was pretty fortuitous. And here's the final built-up design. And there's the LM324 op-amp. Just some bypassing. It's got a 5 V input socket here because the panel meter happens to be a 5 V

**Dave Jones:** type. I've got my nice big 10-turn pot here. That's a 50k pot. It just goes in there. There's the divider resistors. And there's the N-channel MOSFET down in there, the MTP3055. And I've got 10 10 ohm 1% resistors. And the reason I did

**Dave Jones:** that, not only cuz I had the board, but to get a a an accurate It doesn't matter so much in this application, but if you're designing your own one to get an a 1% accurate 1 ohm load resistor is actually

**Dave Jones:** quite expensive. It's actually cheaper and simpler to get 10 10-ohm 1% actual power resistors. These are 1-watt resistors, much easier to get one of those, or half watt I think they are. Um much easier to get 10 of those, and

**Dave Jones:** cheaper and easier than to get one big single power resistor. So, there you go. We've got a nice big uh PCB mounted heat sink on here, which we'll go into, and that's the finished design, and it works quite well. I've got my panel meter

**Dave Jones:** hooked up, and on the back here I've just got the input uh the input resistors to set the um set the differential um input and and have the divide-by-10 ratio, but that's it. And here's the final design working.

**Dave Jones:** I've got the input here connected up to my power supply over there. It's about a 12-V um input at the moment, and I've dialed it up to 81 mA, and as you can see, the Gossett meter here is measuring

**Dave Jones:** the um input current from the power supply. And as you can see, it pretty it corresponds pretty well. And I go up, and it's upside down here. Sorry, the actual LCD display is up up the other way, so but my cable doesn't reach. But

**Dave Jones:** 244 mA, it's you know, it it works pretty well. So, and it goes all the way up to that's uh it's an amp at the moment, and no problems at all. It goes up to pretty much it's starting to

**Dave Jones:** max out there at 1.35 amps. So, there you go. That's about its maximum, and as you can see, the panel meters are quite um accurate there, and it can go all the way down to 1 or uh at least maybe can it do 1 mA?

**Dave Jones:** There we go. It can do 1.5 mA minimum, cuz that's basically 1 mA, because that's as low as the you know, the op amp's got some output um offset voltage there, and I can adjust that, you know even 5 milliamps I can tweak that and if

**Dave Jones:** I wanted a finer range from say 0 to 200 milliamps instead of 0 to 2 amps I would just adjust those divider resistors down there. Piece of cake so it works quite well. Thumbs up I'm happy with that.

**Dave Jones:** Now there's one thing to actually remember about these input panel meters if you don't use precision resistors on the input here I used I used just standard 1% resistors there was actually an of set of 16 millivolts so I had to

**Dave Jones:** actually tweak that value there I had to actually adjust it and put an extra one in series just to just to tweak just to trim it a little bit so I actually got zero on my display for zero current.

**Dave Jones:** Now one important thing you need to know is how much power you can dissipate in your heat sink here through your power MOSFET. Now let's go through the very simple calcs. Now I've said before that heat sink thermal calculations can

**Dave Jones:** get all messy and you don't want to get bogged down in the details but we can do some basic back of the envelope calcs that are going to be pretty close to what we're going to get. Now what you do

**Dave Jones:** is you look up the data sheet for this heat sink this is an avid thermal alloy brand and I've looked up the data sheet and it's 4.5 degrees C per watt. That's the spec you need to get for your heat

**Dave Jones:** sink. That means it will rise for for every one watt you put into this thing it will rise 4.5 degrees Celsius above the ambient temperature. That's the key above ambient whatever the current ambient temperature is. Now let's go through we've got our basic

**Dave Jones:** circuit here. Here's our power MOSFET okay we've got our load resistor here we've got our voltage in from our power supply and we've got a voltage across the resistor which we'll call VR here so we've got V in and VR and the uh current

**Dave Jones:** that we actually have. So, the power dissipated in the heat sink is going to be the input voltage minus the um minus the voltage across the load resistor here times the current flowing through it cuz there's nothing flowing

**Dave Jones:** into or out of the gate here. There's no gate current at all. So, all of the current flows through our power transistor. Now, uh let's assume that we want 1 amp, okay? So, we've got 1 V in here, which gives us 1 V across our load

**Dave Jones:** resistor of 1 Ω. So, that's 1 V. And let's say we have 12 V V in. Let's go through an example. If we have 12 V V in minus 1 V across our load resistor at 1 amp times 1 amp, then we're going to

**Dave Jones:** dissipate the power in the heat sink is going to be 11 W. Or and if you uh put that into the formula for the heat sink up here, bingo, we've got the heat sink will rise by 49.5° C above ambient for 11 W power

**Dave Jones:** dissipation. Easy. Out of curiosity, let's do a quick check to see what temperature rise we actually get in our real heat sink here. Now, I've got I've had 1 amp flowing through it for quite some time, okay? And I've got 12 V input

**Dave Jones:** voltage. There it is. So, we're dissipating the 11 W in our power resistor like that down there because we've got 1 V uh drop across our across our load resistor, as you can see, down here. If I can probe

**Dave Jones:** that, there's our 1 V drop across our power resistor. So, there's um 11 V times uh 1 amp in there. So, there's 11 W being dissipated. And that's quite hot to touch. So, let's get the temperature sensor and see what

**Dave Jones:** temperature it is. Okay, I've got my Fluke reference temperature probe here. As you can see, the ambient temperature is about 20°, and as per the calculations before, we said for 11 W into this heat sink, it should rise

**Dave Jones:** about 50°, let's say 50° C above ambient. So, we're looking for about 70° C. Ambient's 20 + 50°. Let's check it out. Okay, I've got my temperature probe on the heat sink, and as you can see, it's just a couple of degrees over 70. It's

**Dave Jones:** going to climb a bit more, but that's not bad. Confirmation of our back-of-the-envelope calculations. I like it. It's pretty good. And the FET we've used in our circuit here is a 60-V 12-A FET. So, it's actually capable of,

**Dave Jones:** you know, quite a decent load performance. And you can tweak the load resistor value, and you can tweak the op-amp power supply value, and all sorts of things to get to test almost any power supply possible. It's just a

**Dave Jones:** matter of I'm just specking it up, and you know, increasing the size of the heat sink, and changing the load resistor. Easy. And if you're wondering just what this original battery capacity logger board and circuit actually did, well, here it is. It's not too different

**Dave Jones:** to what we've been dealing with. It's the same circuit, but we add in an intelligent microcontroller, which is hooked up to a PC, so it can log things and do other stuff. But, by adding an intelligent micro, what you can do is

**Dave Jones:** you can generate different types of loads. You can generate constant current, constant power, constant resistance, or any type of pulse load you desire. And the way you do that is it's got a PWM output, which generates a voltage which simulates the pot that we

**Dave Jones:** had, and it has an ADC down here, which just measures the voltage across our sense resistor down here. And that allows the micro to, just with a simple bit of math, to generate constant power, constant resistance. I know constant

**Dave Jones:** resistance sounds a bit silly. You can just put a resistance there and actually, you know, a 5-cent resistor on the load, but hey, it allows you to do it under intelligent software control and all sorts of pulse loads and things

**Dave Jones:** like that. So, it's very flexible. Uh and if you've ever seen like a data sheet for a Energizer battery or something like that, they might have a battery capacity uh performance graph over that may um have constant power or

**Dave Jones:** a constant resistance load or constant current load or a pulse load over time to simulate a toy being turned on or off or something like that. And this circuit allows you to do something like that. Very versatile. So, there you go. From a couple of junk

**Dave Jones:** box parts, we've created a put together a pretty handy little uh constant current uh adjustable load there to test power supplies. And if you're testing a power supply, you might want to get a switch mode. You might want to get a

**Dave Jones:** graph of efficiency from 0 to 100% on the Y axis for a for versus load current, say from 0 to 1 amp. And you might actually get, you know, a response that looks, you know, something like that. It's going to peak at some

**Dave Jones:** particular current. It might It might be 100%. You'd have a damn good power supply if it was, but it might be, you know, 90% or something like that. And it might drop away there. And having a little um

**Dave Jones:** little constant current uh load like this, an adjustable DC load, just allows you to um graph uh power supplies, the efficiency of power supplies and all sorts of other stuff over whatever load you want. And I'll show you how to do

**Dave Jones:** that in a in a future blog episode. So, see you next time.
