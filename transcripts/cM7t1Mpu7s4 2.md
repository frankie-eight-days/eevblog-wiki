---
video_id: cM7t1Mpu7s4
title: EEVblog #90 - Linear and LDO regulators and Switch Mode Power Supply Tutorial
url: https://www.youtube.com/watch?v=cM7t1Mpu7s4
source: youtube-asr
timestamps: {"0": 0, "1": 36, "2": 54, "3": 69, "4": 106, "5": 138, "6": 178, "7": 215, "8": 247, "9": 268, "10": 292, "11": 325, "12": 341, "13": 361, "14": 395, "15": 422, "16": 446, "17": 464, "18": 497, "19": 531, "20": 570, "21": 591, "22": 625, "23": 654, "24": 670, "25": 701, "26": 718, "27": 738, "28": 773, "29": 790, "30": 826, "31": 840, "32": 872, "33": 893, "34": 919, "35": 955, "36": 988, "37": 1010}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it's time for another tutorial. This time around, it's switch mode power supplies. Why? Because, well, I keep hearing that beginners are scared of switch mode power supplies. They don't understand them, and that they're complex, and they're different to linear regulators, and linear regulators are so much easier, and they just don't understand how they work, and it's all too much. So, I thought, that's

**Dave Jones:** not right, because you shouldn't be taught that switch modes are all that much different to linear supplies, because if you look at it, they're not. And I know that might sound crazy, but trust me, they're not that much different, and I'm going to show you why.

**Dave Jones:** Okay, so if you're a beginner, you might have seen something typically like this. Linear power supplies, real simple, little three-terminal devices, input, output, and they step down the voltage from like 9 volts down to 5 volts for like a 7805.

**Dave Jones:** Very simple to use, very simple to understand, a couple of filter caps, and that's it. And you might have seen something like this for a switch mode power supply, much more complex, a lot more components, this magic black box down here. We've got diode, inductor, capacitors, um, output sense resistors, and other sense and, um, compensation components around here. And, well, I admit, it does look a lot more complex, but when you get down to it, how much different is a switch mode power supply from a linear power supply? Well, I'm

**Dave Jones:** glad you asked. Let's take a look at it, because if you actually look at what goes on inside these boxes here, they're not that much different at all. In fact, there's hardly any difference, really. Different modes of operation, but the circuitry is very similar. Let's take a look at it. Okay, let's take a look inside a linear regulator, one of those 7805 three-terminal devices. What do you have? What's the circuitry actually look like? Well, here it is. It's a very simple. It's got an NPN series pass

**Dave Jones:** transistor. It's got an op amp. It's got a voltage reference. And it's got two uh feedback uh voltage divider resistors. And that's it. That is a complete traditional three-terminal linear regulator. Now, the 7805 type will have these resistors uh built in to set the output voltage. But something like an LM317, which is um an adjustable linear regulator, these resistors will be outside the chip, and it will have that uh feedback pin. But they work exactly the same. So, there's essentially no difference between an LM317 and a 7805

**Dave Jones:** traditional linear regulator. Now, it works um the basic principle is very simple. It's just a negative feedback loop here. And if you know about your op amps, your op amp building blocks, an op amp will try and drive its output voltage here so that the input voltages match. And that's all there is to it. Um so, it basically the it will adjust this output voltage via this NPN series pass transistor here but to match this reference voltage here. Now, if we And it will continually do that as an as

**Dave Jones:** an analog uh loop. Now, if we redraw this, I've done no trickiness at all. If you redraw it, you might actually recognize this circuit as a bit more familiar. It's exactly the same as here. I've just redrawn it and taken out these uh these voltage divider resistors here because you don't actually need the voltage divider resistors. If this reference voltage here is say 5 volts for a 7805 then you can feed in your 9 or your 12 volts here and you don't need these resistors at all. This output

**Dave Jones:** voltage can go straight back into there just like that and the op amp will adjust the output so that the two inputs match. So the output here will match the other input here which is the reference 5 volt input. It's very, very simple and that's how a linear regulator works.

**Dave Jones:** It's no more complex than that. Now I know you've got a question about this and I'm glad you asked. Why bother having these feedback resistors at all if you can just make the reference voltage the same as the output voltage you want like 5 volts. Well, it's it's due to a manufacturing thing. It's much easier to manufacture a band gap voltage reference at a lower voltage. Let's say 1.2 volts for example.

**Dave Jones:** But let's take a simpler example of 2.5 volts. Let's say this reference voltage was 2.5 volts. Well, to get 5 volts out here you need a gain of two in your non-inverting amplifier. Look, it's a standard non-inverting amplifier here. You've seen that in the classic textbooks. That's all it is with a series pass NPN transistor. So if you've got 2.5 volts here you want 5 volts you want a gain of two in these resistors. Here's your standard non-inverting op amp formula and likewise if you've got a reference

**Dave Jones:** voltage of one volt you want a gain of five here to get 5 volts on the output. That's it. Simple. So what's all this I was talking about that switch mode supplies aren't that much different to linear supplies? Well, let's take a look at it.

**Dave Jones:** I've already drawn the linear supply up here. I've already gone through that. This is exactly the same switch mode power supply. It's a step down. We'll only look at the step down case. So, you know, 9 volts or 12 volts down to 5 volts. Same thing here. This is a step down switch mode power supply. And this is actually what goes on in the chip.

**Dave Jones:** Check it out. They're not that much different at all. Look, series pass NPN transistor, exactly the same. Op-amp with a voltage reference, exactly the same. Feedback resistor network, exactly the same. So, what's different? Well, if you look at it, there's a gated oscillator down here. There's a There's an oscillator. Let's just take an example of a fixed oscillator for the time being. And the op-amp actually switches that oscillator off and on to drive the series pass transistor.

**Dave Jones:** Instead of driving it directly, it drives It just switches an oscillator in there. And we've added external to the chip, hence the little um little dot there, external components. We've got a catch diode. We've got an inductor. The inductor is the important thing. It's what stores the energy. And then you've just got an output filter cap, just like you would have on a linear supply as well. Well, let's not go into that, but an output filter cap.

**Dave Jones:** But they're the only differences. We've added an energy storage component here. And uh we're just switching the transistor differently. We're switching it in bursts, so to speak, um instead of a continuously variable loop for the linear regulator. And seriously, that's what's inside a basic switch mode step down power supply.

**Dave Jones:** They're not much different at all. I told you so. Yet that's not what you might learn in a course. You might learn that switch modes there's all sorts of complex theory, and there is. Um we won't go into it, but I just wanted to show how very similar they are.

**Dave Jones:** Now, just for a bit of completeness, cuz I know some people will complain, this NPN series pass transistor here is not just a basic NPN transistor. It's actually a um a Darlington transistor like this. So, whoop. There you go. It's actually an NPN Darlington transistor. And same down here as well. Now, you've probably heard about low dropout regulators, and you might think they're all mysterious, too.

**Dave Jones:** What is a low dropout uh voltage regulator? Well, it's just got a lower voltage drop, a lower tolerance between input and output than a than a standard linear regulator. Cuz this standard linear regulator, cuz it uses a Darlington pair like this, you're actually going to have two VBE drops plus the saturation voltage of that transistor. So, that's why, in say a 7805, you'll see a typical dropout voltage of like 1 and 1/2 or 2 V or something like that, or even higher, because it's just a function of the

**Dave Jones:** Darlington NPN transistor and how it's used. But an LDO, what is an LDO? Is it totally different? No, it's exactly the same as well. I'm glad you asked. Let's take a look at that. What is an LDO? Everything else is exactly the same, but an LDO uses All right, it's a bit hard to draw like this. Uses a PNP transistor. That's it. Not in the Darlington configuration. It's just a standard PNP transistor instead of an NPN. And that actually allows a lower saturation voltage. But that also has

**Dave Jones:** complications in terms of loop stability and stuff like that. That's why LDO regulators are a bit inherently more a lot inherently more unstable than a standard linear regulator with the NPN transistor. But, there you go. That's an LDO regulator. They're no different either. Amazing, isn't it?

**Dave Jones:** I thought I'd also make quick mention of transient response. You've probably heard that in regards to regulators. And basically, what it is is because this is a continuous feedback loop, it takes time for the output to adjust to well, changes in load for the you know, for the loop to respond to changes in the load. So, that is the the time it takes for it to actually propagate through the loop and actually correct the output is the is effectively the transient response of the linear regulator. So, if you have a

**Dave Jones:** big sharp change in your load, it's going to take some time for the loop to actually compensate. So, there you go. Look that one up. And I should also talk very quickly about the differences between standard linear regulators and LDOs. LDOs, of course, have a lower dropout voltage, a lower you know, you can the input can be much closer to the output because a standard linear one might take two or three volts, and that can be really annoying for low voltage systems. So, that's why LDOs are very popular. But,

**Dave Jones:** they have the downside LDOs have the downside of having not only a a greater inherent instability in the loop. So, you have to be very careful about what capacitor the ESR and the value of the capacitor that you use on the output.

**Dave Jones:** But, I have to do a whole totally different blog on that one. Um But, so that's one of their disadvantages. And also, the other disadvantage of LDOs is that they have a greater ground current as well, which changes with the load. There's all sorts of fancy new LDO topologies to get around those sort of problems, but that can be a basic inherent uh disadvantage as well cuz the actual the ground current can have a direct relationship between the output current and it can be quite high and you can

**Dave Jones:** waste a bit of power there as well. So, they're the basic differences. So, linear regulators are much simpler and more stable but they're got a greater voltage drop across the input and output. So, they're the basic pros and cons.

**Dave Jones:** So, how does the switch mode actually work? Well, I'm glad you asked. But unfortunately, I won't go into the whole detailed operation of it cuz that can take a whole blog in itself. Now, by the way, this is called a buck switch mode power supply. A step down is a buck. So, you can go look up that and you can look up the complex theory and the math and all sorts of things which goes into it.

**Dave Jones:** But basically, let's say 5 V is our set voltage on our output that we want, then this transistor here switches off and on based on whether or not the output needs correction like that. So, this is highly exaggerated. It's going to be much smaller voltage than that up here but the voltage is going to correct itself by switching this series pass transistor off and on via this oscillator in bursts and so, the green thing here is the switch transistor switching off and on. So, any positive

**Dave Jones:** ramp like that, this the transistor is switched on and what happens when the transistor switched on is the current flows through the in like that and through to the out. Now, when through through the inductor and to the output and it stores energy in the inductor.

**Dave Jones:** Now, when the switch switches off, when this goes low and it ramps back down like that, then the current is actually flowing up through the diode like that through the loop like that. So, it just switches from that loop to that loop there. And that's basically all there is to it. It's two modes, off and on. And the reason switch mode power supplies are more efficient than linear regulators is because of this this transistor switch here is either fully saturated or completely off. And when it's fully saturated, it doesn't

**Dave Jones:** drop much power at all. And when it's off, it doesn't use any power at all, essentially. But there are losses in the loops and things like that, which we won't go into cuz it just complicates it and there's no need for that. But basically, it's either off or on.

**Dave Jones:** Whereas a linear regulator, I don't have the circuit here anymore, but as you saw, it's a continuous loop and it's continuously dissipating power in the past transistor. So that's why linear regulators are very inefficient and switch mode power supplies are quite efficient. They can be up to greater than 90% efficient for a buck. Now, that's not always the case though. It depends on the load and all sorts of things. Switch modes can have a great range of inefficiency. And sometimes, a linear regulator will actually be more

**Dave Jones:** efficient. If you use an LDO regulator, let's say you've got 6 volts in here and 5 volts out there. Well, that's already for a linear regulator, that's 80% efficient. And a good switch mode might only be 80, 90% or if you've only got 5.5 volts input, you're using an LDO, forget I'm using a switch mode circuit here.

**Dave Jones:** And you want 5 volts out, that's only half a volt drop for the linear regulator. Bingo, you've got 90% efficiency for a linear regulator. Just with linear regulators and with switch modes, too, there's lots of other often internal circuitry in there for overcurrent protection, overvoltage protection, overtemperature protection, all sorts of other little things that they add in to make the chips more useful. But don't let those confuse you.

**Dave Jones:** The basic operations is basically as I've shown here and that's going to be the same for all for those LDOs, those linear regulators and those switching regulators I've shown. They're not that hard to understand at all once you strip away all the other stuff. So, there you go. I know that's not a complete tutorial on switching regulators, not even close cuz there's so many types out there. It's almost endless. Boost, buck, inverting, synchronous, you know, power factor corrector ones, isolated, non-isolated.

**Dave Jones:** It's just It's crazy. There's And there's countless theories behind all of them, too, and it can get very, very complex. And I'm sure I could do a 1-hour blog on each and every type of those switching regulators and well, I might do in the future anyway, but I just wanted to make this one quick and simple to show that there really isn't much internal circuitry difference between a standard buck switching regulator and a linear regulator, not much at all as you saw. And that's something you traditionally don't learn

**Dave Jones:** in school or courses or things like that. They don't teach us switch modes as totally separate. So, I thought that I hope that was a a bit of clarity for you and to show beginners that they are they can be pretty simple these switching regulators. So, I hope that's given you more confidence to go out there, learn more, and try and use them.

**Dave Jones:** So, I hope that helped you out. See you next time.
