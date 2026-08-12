---
video_id: xUKf-4rv_sQ
title: EEVacademy #8 - Howland Current Pump
url: https://www.youtube.com/watch?v=xUKf-4rv_sQ
source: youtube-asr
timestamps: {"0": 0, "1": 23, "2": 36, "3": 52, "4": 63, "5": 83, "6": 97, "7": 110, "8": 122, "9": 137, "10": 156, "11": 177, "12": 194, "13": 207, "14": 220, "15": 234, "16": 247, "17": 263, "18": 277, "19": 296, "20": 309, "21": 324, "22": 342, "23": 359, "24": 373, "25": 397, "26": 417, "27": 432, "28": 448, "29": 457, "30": 474, "31": 493, "32": 501}
---

**Dave Jones:** Okay, so today we're going to be talking about the improved Howland current pump. Um it's a op-amp circuit with five resistors and a voltage reference which can be used to generate a constant current for a few milliamps, tens of milliamps, which can be used to drive an LED or a sensor or anything that requires a small amount of current which doesn't require particularly high efficiency.

**Dave Jones:** So, let's get started. Here we have a difference amplifier. A difference amplifier is probably the fundamental building block of a Howland current pump. And you'll notice that this is a unity gain difference amplifier.

**Dave Jones:** That means that the input and output have a gain of one. They're multiplied by one. Um there's no scaling. Um and there's a few different things that are interesting about a difference amplifier.

**Dave Jones:** The first is that it doesn't matter if one of these terminals is ground. Um in fact, it doesn't matter what they are at all. You'll notice that the output voltage isn't changing.

**Dave Jones:** Um that's because the output is dependent on only the voltage at this node subtracted from the voltage at this node. It doesn't depend on the the values referenced to this ground at all.

**Dave Jones:** It's just subtraction of these two. And in this case, it's 1 - 0 is 1. And in this case, oh, it's 0 - -1, which is 1 again. And there you go, you have it at the output.

**Dave Jones:** So, that's the fundamental building block. And if you add a resistor to load the op-amp, just a load resistor, it doesn't actually do anything to the gain. It doesn't do anything to the grounds.

**Dave Jones:** Um and it really doesn't affect the circuit at all. So, that is probably the first step to building a Howland current pump. Um first I'm going to remove this ground cuz it really doesn't matter.

**Dave Jones:** It doesn't do anything for the circuit. And I guess the next thing to notice is that if you have 1 V on the output and 1 K here, then you're always going to have 1 mA going through it.

**Dave Jones:** And that that can be used that can be a useful trait in um understanding a Howland current pump. So, if we made this 1 ohm, which I'm going to do now, you'll notice that the output hasn't changed at all and the the um gain hasn't changed at all.

**Dave Jones:** There's an interesting property of this circuit and it's that the whole circuit is basically referenced to this point. It's the only ground in the circuit. And that means you can make it a virtual ground, um which um is frequently created with just a unity gain op-amp.

**Dave Jones:** So, let's create a um a buffer. And we're going to buffer ground. It's kind of useless, but I will get to this. And I'm just going to move the load all the way over here.

**Dave Jones:** And I'm still going to connect it to ground. And then I'm going to connect that buffer up here. Just move it down a little bit. And move that up.

**Dave Jones:** So, this is all fine. Now we've got this virtual ground here. And we can also connect it here. We can connect the virtual ground to the the ground over here.

**Dave Jones:** And it doesn't actually matter what this voltage is. The whole circuit will shift with it because every element every node in the circuit is referenced to this point here, the virtual ground.

**Dave Jones:** Um where the absolute ground is over here. So, what we're going to do is apply a voltage source here and see what happens. So, if I put 1 V here, the whole circuit has shifted up.

**Dave Jones:** That's 2 V. That's 2 V. Okay, so with that we can say that um this is a true virtual ground. We can use this as a virtual ground without really worrying too much.

**Dave Jones:** And this output is still actually 1 V when you compare it to the virtual ground, which is here. So, let's do that. Let's probe the op-amp output with respect to the virtual ground.

**Dave Jones:** Um and I'll just use one of these probes over here. Just like this one. And you'll see it is 1 V as it always should have been. So, if we change the offset of the whole circuit to 2 V, now it's it's outputting 3 V, but the virtual ground is now 2 V.

**Dave Jones:** And 3 - 2 is still 1 V. So, what we're able to do with that is create a constant voltage over this resistance. And a constant voltage over a resistor is a constant current.

**Dave Jones:** So, now what we can do is something like this. We can put a another resistor here. And no matter what we change this to, it will still have 1 mA going through it.

**Dave Jones:** Um where the path through the resistor is down here. And I'll just make more obviously labeled circuit. There you go. Where the path is down here for the current.

**Dave Jones:** And the reason it's constant is only because you've got a constant voltage across this resistor. Now, a unity gain buffer has a few properties to it. It has the property that the input is very high impedance.

**Dave Jones:** A very high impedance when compared to these values here. And the other property is that the output is very low impedance as in it has it has a very low output resistance.

**Dave Jones:** And that is actually what this has. This 1 ohm is very low resistance. Um so maybe without too much error, we can simply remove that buffer entirely and place it like this.

**Dave Jones:** Now, this has a problem. You'll notice that a lot of the current is flowing in from the um non-inverting of the op-amp. And that is creating error. See, we've actually got 1 and 1/2 amps going 1 and 1/2 milliamps going through that output resistor.

**Dave Jones:** Now, how do we deal with that? Well, the real issue was the impedance. We we want that that terminal here to be as high impedance as possible. So, all we have to do is increase the resistors for that section of the circuit.

**Dave Jones:** And now, almost no current is traveling through this section of the circuit because it's behaving very high impedance, as in um very high resistance. That means that you've got a very low current if the voltage isn't enormous.

**Dave Jones:** Um so, you can say that the vast majority of the current is flowing through this resistor here, through here. And you only lose a very small fraction through this wire.

**Dave Jones:** In this case, it's 5 microamps, which is just nothing. And this is the Howland current pump. It's a very simple circuit. The sources of error are of course um the current going through this section of the feedback loop, the input offset of the op amp.

**Dave Jones:** You With high impedance feedback resistors, you you get input current, you get this current bias, and that will create a sort of offset, which can become a problem. And you can also get some stability issues um with the circuit, and sometimes you'll want to do something like this.

**Dave Jones:** But often this isn't the case, and often you can just get away with just doing some old resistors, and yeah, be all right. Um um This is the Howland current pump.

**Dave Jones:** Hope you've learned something from this video. If you like it, leave a thumbs in the thingy, and uh I will see you next time. Bye.
