---
video_id: hReCPMIcLHg
title: EEVblog 1409 - The DANGERS of Inductor Back EMF
url: https://www.youtube.com/watch?v=hReCPMIcLHg
source: youtube-asr
timestamps: {"0": 0, "1": 27, "2": 38, "3": 57, "4": 71, "5": 81, "6": 98, "7": 109, "8": 125, "9": 136, "10": 154, "11": 165, "12": 179, "13": 189, "14": 203, "15": 222, "16": 233, "17": 245, "18": 260, "19": 271, "20": 283, "21": 302, "22": 313, "23": 327, "24": 344, "25": 359, "26": 372, "27": 383, "28": 393, "29": 411, "30": 427, "31": 446, "32": 461, "33": 479, "34": 495, "35": 510, "36": 524, "37": 535, "38": 555, "39": 565, "40": 575, "41": 586, "42": 597, "43": 615, "44": 628, "45": 637, "46": 651, "47": 664, "48": 673, "49": 683, "50": 710, "51": 730, "52": 743, "53": 753, "54": 768, "55": 780, "56": 798, "57": 811, "58": 832, "59": 846, "60": 862, "61": 879, "62": 893, "63": 907, "64": 918, "65": 933, "66": 942, "67": 951, "68": 965, "69": 976, "70": 989, "71": 1005, "72": 1016, "73": 1037, "74": 1047, "75": 1060, "76": 1074, "77": 1086, "78": 1099, "79": 1118, "80": 1128, "81": 1146, "82": 1156, "83": 1165, "84": 1176, "85": 1190, "86": 1201, "87": 1217, "88": 1227, "89": 1240, "90": 1253, "91": 1274, "92": 1289, "93": 1304, "94": 1326, "95": 1342, "96": 1352, "97": 1370, "98": 1391, "99": 1413, "100": 1434, "101": 1445, "102": 1459, "103": 1472, "104": 1483, "105": 1504, "106": 1514, "107": 1529, "108": 1544, "109": 1558, "110": 1572, "111": 1588, "112": 1601, "113": 1623, "114": 1633, "115": 1645, "116": 1658, "117": 1670, "118": 1685, "119": 1698, "120": 1716, "121": 1730, "122": 1752, "123": 1764, "124": 1774}
---

**Dave Jones:** Hi, in a previous tutorial video on DC circuit transients, we took a look at capacitors and inductors and how they uh store energy. Capacitors store energy in a dielectric material using an electric field, and inductors, like uh are used in relays, for example, store energy in the magnetic field in the coil and any ferrite or, you know, high permeability material uh that happens to be used as

**Dave Jones:** the core. And of course, an inductor can be a coil in a relay like this, for example. It could be like a just a like a common mode or just a regular wound choke like this.

**Dave Jones:** It could be a switching transformer in a switch-mode power supply, for example. These are all magnetic inductive components. So, we're going to have a look at one of the traps of these, and I mentioned this in the tutorial video, but I didn't have time to give you a practical demonstration.

**Dave Jones:** So, we're going to show a couple of traps, one of which you probably haven't seen demonstrated before, which is really interesting. But today, we're going to take a look at some practical examples of, in this particular case, using a relay and some of the traps involved in this.

**Dave Jones:** But it, like I said, it doesn't have to be a relay. It could be a switching transformer. It could in a switch-mode power supply. It could be a motor, for example.

**Dave Jones:** And a similar trap is involved because of Faraday's law of electromagnetic we briefly covered in the previous video, but I'll just mention it here again. And basically, E, which is the electromotive force, basically the voltage, is minus N.

**Dave Jones:** N is just the number of turns. If you've only got like a single wire that your magnetic field is around, then obviously N is one, and you can take it out of the equation.

**Dave Jones:** But it's basically minus d phi dt, which sounds complicated cuz it's differential calculus, essentially. But it's not. It's easy to understand. d phi dt is just the change, the difference, or the change in magnetic flux over time.

**Dave Jones:** That's all it is, and that of course is in Weber's per second, but we won't go into the details. Now, as I mentioned in the previous video, the interesting thing is this Why is this negative here?

**Dave Jones:** Well, this is Lenz's law. And Lenz's law basically says that the induced voltage is opposite to what actually caused the magnetic build-up in the first place. So, if we've got a basic circuit with a switching NPN transistor like this, obviously you've seen this circuit before.

**Dave Jones:** You put a base current in here, switches the transistor on, acts as a short circuit, current flows from our power supply through the relay of the coil, and the relay activates and changes the contact.

**Dave Jones:** So, that current flows down through there, and there will be a minimum like turn-on voltage of the relay here, and here's a data sheet showing that it might be, you know, 80% or something like that of the turn-on voltage.

**Dave Jones:** As soon as it hits that voltage, it switches on. And of course, you would leave that current flowing through there if you want the switch position like permanently over here like this.

**Dave Jones:** You've got to keep the current flowing like that. But when you switch the relay off, you ground this. There's no more current flowing here. The relay switches off, but the magnetic field built up in this relay coil, it's got to go somewhere.

**Dave Jones:** It doesn't vanish instantly. You can turn the transistor off instantly, but the magnetic field has to go somewhere. And that energy has to go somewhere in the form of current going somewhere through a path, or in the form of a voltage that just gets higher and higher and higher.

**Dave Jones:** Something has to give. The stored energy in that magnetic field has to go somewhere. Just like if you short out a battery, there's energy build-up in that battery. You'll, you know, get sparks, and there's a lot of energy in there and you can short it out.

**Dave Jones:** And the same thing happens with the coil. There's X amount of energy built up and something's got to happen to it. And this is what Faraday's law of electromagnetic induction is about and in particular, Lenz's law.

**Dave Jones:** Lenz's law says that the volt that the induced voltage in the inductor, in this particular case the relay coil, will the voltage will actually be opposite to what actually produced it.

**Dave Jones:** So, when we got the transistor switched on, of course, the voltage will be positive and negative like this. It's flowing through and of course, you know, this is our ground voltage reference where we're actually uh measuring from.

**Dave Jones:** So, everything is uh positive in regards to that. But, that's not what happens. When we turn the switch off like this, the magnetic field collapses. When that collapses, the voltage will go negative.

**Dave Jones:** So, this will then become negative and this will become positive. And, assuming you don't have a diode like this, this current that was flowing through here like this, it will still continue to flow because the inductor, when you switch it on, opposes the flow of current.

**Dave Jones:** But, when you switch it off, it wants to keep the current flowing. So, it's still the current still flows out of here, but the switch is off. So, it's got nowhere else to flow.

**Dave Jones:** So, this voltage at this point here must rise to follow uh Faraday's law and Lenz's law over here. So, if the current keeps flowing like this, this voltage now becomes positive and it'll rise and rise and rise.

**Dave Jones:** In theory, it'll rise to infinity, but of course, in practice you never get infinite. So, it'll That's what we're going to look at today. What happens when you uh open this transistor switch, what happens to this magnetic field stored in here?

**Dave Jones:** Haha. It can really ruin your day unless you put in a diode. And that's what we're going to look at. You might have heard these called back EMF diodes, freewheeling diodes, snubber diodes, or flyback diodes.

**Dave Jones:** There might be other names, too. Leave it in the comments if you've got a seen a different name for these. But basically, what this diode solves is the problem with back EMF, because when you open this switch here, this current has to flow somewhere.

**Dave Jones:** And if it's got nowhere to flow, then this voltage just rises to the moon, right? And you can get hundreds or even thousands of volts, as we're going to demonstrate here today.

**Dave Jones:** But if you put a back EMF diode in here, the current has somewhere to flow. Like this, it flows in there, and it stops this voltage rising to infinity.

**Dave Jones:** And which can blow the the transistor that's connected to it, can blow any circuit that you use to drive it. And this is why you'll find these diodes actually packaged inside relay driver chips, like the ULN2003, for example.

**Dave Jones:** You'll find that there's a basically a common terminal for the diode, and there's a whole bunch of different diodes in there, one for each output. This is designed, if you're using those eight outputs to drive eight relays, then you need eight back EMF or snubber or flyback or freewheeling diodes.

**Dave Jones:** And the reason they're also called freewheeling diodes is because you can imagine that the stored energy in the inductor is like a big flywheel. So, imagine this is a big flywheel that's just spinning and spinning and spinning and spinning like this, because you're spinning it in this direction, cuz you're putting in energy from the current, it's spinning and spinning.

**Dave Jones:** And then when you when you stop spinning it, you remove the current, the flywheel still wants to keep going. And this is why you put in a reverse diode like this to give it a path, so it can flow like that.

**Dave Jones:** And then it'll stop very quickly cuz you're loading it down, and the back EMF diode will, of course, conduct all that current, stop the voltage from rising dramatically, and it will absorb all of the energy that was stored in the coil, and it'll absorb it very quickly so it doesn't damage your circuits.

**Dave Jones:** And this is the importance of back EMF and freewheeling diodes. They could can also be a clamping diode as well. That would be another name. And flyback actually comes from You'll actually find a back EMF diode on the primary side of a switching power supply like this.

**Dave Jones:** And you can see inside there is the coil of wire and the two contacts. That's the center, and it's just when you activate the relay, it just pulls this armature across and moves that contact from one side to the other.

**Dave Jones:** Okay, so what we've got is a 12-V relay here. We've got a 12-V power supply. We've got an NPN bipolar transistor and another that MOSFET that it's a 2SC2610, and that's important, and we'll change that around later to show you.

**Dave Jones:** It's a high-voltage transistor, 300-V rated. You'll see there's a reason for that. I've got a pulse generator over here, which just generates like a 1-Hz 200-ms pulse like this over and over.

**Dave Jones:** 50-Ω terminator just for your transmission line aficionados. Then a base resistor 1K, and that will turn on the transistor. I've got a current sensing resistor down here, so that lets us hook this up to our scope and look at our emitter current flowing down here because it may actually be different.

**Dave Jones:** Well, it will be different, spoiler alert, to the relay current up here. And I've got another magnetic current probe up here, which is a relay current probe. I just realized I put that in the wrong spot.

**Dave Jones:** It It's actually in here so that we can get the current flowing around this when we release our relay. Anyway, and here's our circuit here. We've got our Omron relay.

**Dave Jones:** You can see it. I've just This led just shows which contact is just switching back and forth. Clunk clunk. That's our switching transistor. I don't have the freewheeling back EMF diode in there at the moment.

**Dave Jones:** We've got our current sensor up there and just a few probes to measure the current and voltages. Oh, and I've got another probe off here going off to the collector voltage.

**Dave Jones:** So we can see cuz this is what we're really concerned about today. What happens to the voltage at this point and will we blow up our driver Okay, so I've got it going here switching at a 1 Hz repetition rate as you can probably hear and it's exactly what you expect.

**Dave Jones:** When we switch on the relay here, this is our input pulse. This is our emitter current. This is in 2 mA per division and this up here is our current probe showing it through the coil.

**Dave Jones:** You can see these two match like this. I can actually clean this up cuz I'm actually using the high current probe available in the EEVblog shop by the way.

**Dave Jones:** It's excellent this Micsig current probe here. Great for doing stuff like this. Not for really low currents like we're dealing with here, but I can fix that by just going into the acquisition here and going into average mode.

**Dave Jones:** There you go. You can see that they're practically identical. They've even got that same little blip in there. So obviously the emitter current's going to match the coil current up here because well, it's it's the same, right?

**Dave Jones:** The current just flows down in the circuit. The current through the coil is the same as the current through the emitter here. So you'd expect the waveforms to be the same.

**Dave Jones:** That's just my averaging again. We'll just go back to sample mode there. So it's just going to be a bit noisier. So I'll just expand that emitter current there and you can see you might notice just ignore this little blip here.

**Dave Jones:** This is the exponential rise that we saw in the inductor. When an inductor is not energized and then you put a current through it you a lot i.e. put a voltage across it in this case which causes a current to flow, it doesn't change instantly cuz here's our input pulse changes instantly, our transistor this is our transistor it's switching on instantly but the current actually through the transistor and

**Dave Jones:** hence through the coil as well does not switch on instantly it follows that exponential curve like that. It's going to follow that precisely. I guarantee it. Now, the reason that we're getting this little blip in here is because this has to do with the magnetics of the coil and how it's physically starting to do some work at this point.

**Dave Jones:** It actually reaches the what's called the trip current of the relay and then it's it's doing work it's pulling the armatures. So that's the point there where the armatures is actually kicking in and then it goes up.

**Dave Jones:** But if that wasn't there if it wasn't physically doing any mechanical work then if it was just an inductor just the coil itself you would get a perfect exponential rise.

**Dave Jones:** Just as the formula predicts. But all the interesting stuff happens on this negative edge when we de-energize the coil. So I'll just switch to the negative edge there and now we can zoom in and have a look at some interesting stuff that's happening here.

**Dave Jones:** So as you can see our emitter current the current through our transistor doesn't suddenly fall cuz this is our input to our transistor it doesn't just go to zero like this as you'd expect.

**Dave Jones:** There's actually still a significant amount of time where the current does something. We're only talking 10 microseconds here. We're not talking much but the devil's in the detail. So let me actually switch on channel two which is the collector voltage.

**Dave Jones:** So we're looking at the emitter current which is the blue there, the collector voltage which is the green. Now the interesting thing to note with the collector voltage is what scale we're looking at.

**Dave Jones:** 100 V per division. 100 200 300 400 500 600 700 V. This is not a mistake. I am using a 100 to 1 probe. There's my high voltage 100 to 1 probe which you've seen in my probe video.

**Dave Jones:** I've actually done a video actually comparing different types of oscilloscope probes, a high voltage probe. And this, remember, is with no back EMF diode on there. And that's what you get if you forget to put your back EMF diode.

**Dave Jones:** It rises to hundreds and hundreds of volts. It could even be thousands of volts. Now, this is actually even exceeding the data sheet value of our transistor. So, no, we're not damaging our transistor cuz there's not actually not a huge amount of energy in this coil.

**Dave Jones:** So, even if you didn't have a high voltage probe and you hook this up to your oscilloscope which has a nominal like 300 V peak input, you're still not going to damage your oscilloscope because it's not a lot of energy and it only lasts, you know, tens of microseconds, something like that.

**Dave Jones:** So, it's not a lot, but this is what happens. The voltage rises. So, if our input switches off here, why does it take like 5 microseconds here for our voltage to rise and our current to actually drop like this?

**Dave Jones:** Well, this is actually a a quirk of bipolar transistors. It's what's called the storage time. And not all data sheets will have it, but here's a data sheet that actually does have it and I'll show you this transistor in a minute.

**Dave Jones:** And this storage time of bipolar transistors, it's in the order of, you know, microseconds. It's not long, but it this what's is what limits the switching frequency of bipolar transistors.

**Dave Jones:** Generally, they actually um have this like a a delay. They actually retain the current in there for a you know a short amount of time, the base current. They essentially retain that and keep the transistor switched on.

**Dave Jones:** It does take some time for them to switch off. In this case, about 5 microseconds. Just be aware of that with bipolar transistors. All right, so I've stopped that.

**Dave Jones:** So, let's have a look at what's going on here. Uh as you can see, we've got our collector voltage here. It's going up to 700 V, so it's breaking down.

**Dave Jones:** So, after our delay time there, after our storage delay time, then the collector voltage starts to rise like this, right up to you know 700 V peak, and then the blue trace here, you can see our our emitter current down here through the 10-ohm resistor.

**Dave Jones:** So, it's flowing through the transistor cuz the transistor is broken down. It's only a 300-V uh rated transistor, so we're going to get some flow through this emitter resistor down here.

**Dave Jones:** But, you'll notice that it that the emitter current ends at the same point as when the transistor when when the collector voltage here starts to go back down. So, the transistor's gone, "Well, I'm done breaking down.

**Dave Jones:** I'm going to stop breaking down, so there's no more current flowing through the transistor like this." But, you can see that it takes significant amount of time for the actual collector voltage here to actually decay.

**Dave Jones:** It could be like maybe hundreds of microseconds even. It takes a you know it takes a significant amount of time. It's gone right off the uh screen there. And that would be due the transistor's not breaking down anymore.

**Dave Jones:** That would be due to other parasitics in the uh breadboard, in the physical uh construction of the breadboard. So, what I'm going to do now is put in the back EMF diode in here across the relay coil, and that will conduct all of the current and keep it within here and clamp the voltage at this point to 12 V plus a diode drop.

**Dave Jones:** I can do this safely even though it's 700 volts cuz as I said, you're not going to feel it cuz it's a low amount of energy. Bingo, you see the green trace, which is our high voltage trace, it's dropped down to nothing.

**Dave Jones:** You might be able to see. Hang on. There we go. What are we at now? 2 volts per division. 2 4 6 8 10 12.6. That's our diode drop.

**Dave Jones:** 12.6 volts there and it's clamped. We have now saved We've now saved our poor transistor or our driving circuit, whatever it is, from the hundreds of volts peak that we had before.

**Dave Jones:** It's now going to clamp at 12 plus whatever the diode drop. Could be up to a volt or whatever depending on, you know, whatever. And that diode can be pretty much any type, just a fast switching signal diode.

**Dave Jones:** You don't need anything more than that cuz the energy is like it's it's naff all. The area under that curve for like 10 microseconds is nothing. So, you don't need like a big 1N4004 or something like that.

**Dave Jones:** I generally prefer to use the fast faster switching diodes. That's all you need. So, you know, a 914 4148. So, that's why in every relay driver circuit, you'll find a back EMF diode or a freewheeling diode or a snubber diode or a flyback diode.

**Dave Jones:** And you can see why it's called a snubber diode because it snubs the voltage. Instead of going up hundreds and you know, hundreds and hundreds of volts right off here, it just snubs it or clamps it.

**Dave Jones:** Also called a clamping diode. And you don't actually need a high voltage rated diode in there because the act of putting the diode in circuit means that the collector voltage, it will never ever rise up to those hundreds of volts because the current is clamped through the diode.

**Dave Jones:** Now, let me show you something really cool. We're going to make an RF transmitter. We're going to ruin our day by replacing our high voltage transistor there, which is still breaking down, with an even wimpier one.

**Dave Jones:** I've got like a PN100. This is like a 40-50 V rated transistor. Let's whack that in there and see what happens. This is really neat. So, there it is.

**Dave Jones:** That's now in circuit and we've got our back EMF diode in there. So, nothing has really changed here except for the fact you can see we're on the same time base, 10 microseconds.

**Dave Jones:** Our storage delay here isn't nearly as much. 1 microsecond there. So, because this is a higher speed transistor than that high voltage one we had before. So, there's less storage time.

**Dave Jones:** But, you can see it's doing exactly the same thing. It's clamping at that like 12.6 V there. There it is. No worries. We've saved our circuit. But, let's take out that back EMF diode, shall we?

**Dave Jones:** And tada! Look at that. Woah! This is heavy. What's going on? In fact, we've got a whole lot of action happening here for a good more than a millisecond.

**Dave Jones:** Look at this. There's a whole bunch of stuff. We can't see anything here. We're going to have to actually zoom in to see what's what. And we're just going to take a look at what's happening in here.

**Dave Jones:** So, the green is our collector voltage again and that is the interesting one we want to look at. 20 V per division. So, 20, 40, 60, 80, you know, 90 odd volts.

**Dave Jones:** It's ramping up there after our delay time there of one storage delay of 1 microsecond. So, at this point the current to our relay switched off and the voltage starts to rise just like it did before until the transistor breaks down.

**Dave Jones:** It's like it's only rated like 60 50-60 V or something, but survived a bit more. So, at this point the transistor breaks down and basically shorts out pretty much because our our voltage at this point has dropped down to zero and the only way it can drop down to zero is if it if it goes through this transistor and is pulled low by this 10 ohm current

**Dave Jones:** sense resistor here. So, it's basically the transistor's just broken down, it's conducting, but because it's broken down and the voltage starts to drop like this because it's shorted out, then well, where's the voltage to continue to keep it broken down?

**Dave Jones:** It's not. The voltage is dropping drastically drastically until the transistor goes, "Ooh, I've got no high voltage on me anymore. I'm not broken down. I'm going to start up again." And then it starts up again and then again and again and it oscillates.

**Dave Jones:** We've got ourselves an RF oscillator at well, what sort of frequency? We can measure that. It's about 1.5 MHz. So, we've now got ourselves a little RF transmit for however many said like almost a millisecond, this thing is going to be acting as this like little mini RF transmitter.

**Dave Jones:** Isn't that cool? And you could really come a gutser if you don't put in your back EMF diode. You can actually something like this can start oscillating and of course the oscillation frequency is going to depend on like the parasitics of your parasitic capacitance of your breadboard and circuit and other stuff.

**Dave Jones:** And in other cases it may not oscillate as we saw before even though the previous transistor broke down, but this one certainly does do that. So, we're going to do this live.

**Dave Jones:** I'm going to replace the PN100 with a classic 3904. They're practically equivalent. I mean, the PN100 is like a an equivalent it stopped going and there we go. It's it's similar sort of duration, but I expect our frequency to change a little bit.

**Dave Jones:** Hold your tongue at right angle, good enough for Australia. Almost 2 MHz now. And you can see how that's slowly rising up there. Not sure why it's doing that, but the reason why it changes here, I would imagine that that's actually the physical relay actually moving back.

**Dave Jones:** So, that's going to make a difference in the properties of the coil. So, you'd expect some sort of change there. But you can see it eventually reaches a point where it's going, "Well, I don't have enough sustaining voltage in the coil in here to actually break down the transistor anymore." So, we're talking 20, 40, you know, 60 certain volts, something like that.

**Dave Jones:** The energy in the coil eventually drains out oscillating it like this. You know, it's it's not free energy here. The energy comes from the magnetic field build up in there and as magnetic field is slowly decreasing through all this switching and other losses and it just doesn't have enough energy anymore and then it eventually just tapers off just like we saw before.

**Dave Jones:** And because the transistor is not breaking down anymore, we're now getting into just, you know, the parasitics of the breadboard and the circuit actually just slowly discharging that is just leaking out.

**Dave Jones:** And that takes, you know, 10 milliseconds or something. And I can actually fix that off operation if I put a capacitor across the collector and emitter. Let me There we There we go.

**Dave Jones:** There's a capacitor across the collector and emitter and it's well doing something else weird now because of the parasitics of our circuit. So, there you go. I promised to show you something neat you may not have seen before.

**Dave Jones:** A transistor relay RF transmitter. Cool, huh? Big trap for young players. And if you zoom out to your regular time base to see your thing like you might think, "Oh, it's just it's just a spike.

**Dave Jones:** That could be, I don't know, my like a big inductive earth loop or whatever." And you know, yeah, no worries, right? You wouldn't think anything of it. And this RF, if you don't have the back EMF diode in there, then if you don't actually go in there and check the negative edge of that, you wouldn't know that all of this magic is happening in there.

**Dave Jones:** Can be hundreds of volts like and and RF transmitter as well, a very brief one, and that could like couple into other parts of your circuit and really ruin your day.

**Dave Jones:** And unless you actually zoomed in there and really had a good look at what's going on there, you wouldn't never know. Now, here's the interesting bit and why I've included this current probe in here like this.

**Dave Jones:** Normally, the emitter current down here matches the inductor current, but with the back EMF diode installed, you'll notice that we're at 10 milliseconds per division. It takes 10 20-odd milliseconds at least for the orange relay current here.

**Dave Jones:** So, this is the current circulating in the back EMF diode here. It takes much longer for this to actually decay down because the energy stored in there, it can keep that voltage up longer and keep that current flowing.

**Dave Jones:** And our blue waveform here, that's our emitter current. It's dropped to zero, but it's there's still that huge delay while that current is circulating in that driver there. This is why it takes longer when you include a back EMF diode.

**Dave Jones:** It takes much longer to switch the relay off. Now, I'll physically remove that like that. And if I rescale that, just to start the averaging again, you'll notice that it's where exactly the same scale as before, but now the relay turns off much quicker.

**Dave Jones:** And just as a brief aside, a back EMF diode like this is technically not the best solution for this. There are other solutions out there, but it's the simplest and the cheapest, and some relays might actually be polarized.

**Dave Jones:** The coil is polarized because if it is polarized, then it'll have an internal back EMF diode in there. But technically, um, a back EMF diode like this can actually, because the current's actually flowing around here, and it can flow around for quite some time, then this can actually keep the relay actually energized, and it can take longer for the relay to switch off.

**Dave Jones:** And in some cases, there might be some extra contact bounce or something like that, uh, due to the back EMF diode. But of course, you got to uh, protect your circuit.

**Dave Jones:** You can't just have nothing in there, but sometimes you can have just a resistor in there if under certain circumstances. Sometimes you can uh, put in an extra uh, Zener diode like that.

**Dave Jones:** That's probably like the best case uh, solution. It's then it's going to switch off quicker, and you can put like a a varistor in there, and a like a TVS like MOV type device or something like that.

**Dave Jones:** Some sort of clamp device. But yeah, back EMF is just your traditional solution, cheap and simple, but you got to know there are technically some downsides. And it's not just the coil.

**Dave Jones:** Even, you might actually want to put a clamp across switches, cuz one of the problems, if you're driving an inductive load, you know, it could be a motor or something like that with a relay or some other, you know, large inductive load, you can actually get arcing across your contacts here when it opens up.

**Dave Jones:** You can get high voltage arcing. It's exactly the same back EMF problem. So, you might want to put a clamp across here, and you might see this as a capacitor resistor snubber.

**Dave Jones:** Uh, for example, that that goes across switches. So, if you've ever seen a capacitor and resistor in series across like a switching SCR or or some sort of switch contacts or something something like that, you know they're doing that as a clamping solution, because inductive loads, doesn't matter what it is.

**Dave Jones:** Not just talking about relays here. And extra cool bonus thing, I've got my microphone right next to the relay without the back EMF diode. So, listen to that. And now, listen what happens when I plug in my back EMF diode.

**Dave Jones:** I do nothing else. Ready? It's changed. It's lower amplitude. Listen. Clunk. Clunk. It's louder. Cool, huh? I'll leave people in the comments to figure out why that's happening. So, that's pretty cool, huh?

**Dave Jones:** Back EMF diodes, they are a big deal. Got to have them. Otherwise, that pesky collapsing magnetic field and bloody Faraday and Lenz, they're going to come and bite you.

**Dave Jones:** You can't beat the laws of physics, Captain. That collapsing magnetic field, if there's nowhere for the current to flow through our diode, then, well, the voltage must go up.

**Dave Jones:** You must obey the formula. I hope you liked it. If you did, give it a big thumbs up. As always, discuss down below. Catch you next time.
