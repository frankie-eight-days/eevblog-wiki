---
video_id: xUKf-4rv_sQ
title: EEVacademy #8 - Howland Current Pump
url: https://www.youtube.com/watch?v=xUKf-4rv_sQ
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 29, "3": 46, "4": 63, "5": 86, "6": 103, "7": 121, "8": 134, "9": 150, "10": 167, "11": 184, "12": 199, "13": 218, "14": 236, "15": 254, "16": 269, "17": 284, "18": 296, "19": 314, "20": 332, "21": 342, "22": 361, "23": 380, "24": 410, "25": 422, "26": 436, "27": 453, "28": 468, "29": 485, "30": 496, "31": 509}
---

**Dave Jones:** Okay, so today we're going to be talking about the improved Howland current pump. Um it's a op-amp circuit with five resistors and a voltage reference which can be used to generate a constant current for a few milliamps, tens of

**Dave Jones:** milliamps, which can be used to drive an LED or a sensor or anything that requires a small amount of current which doesn't require particularly high efficiency. So, let's get started. Here we have a difference amplifier. A difference amplifier is probably the

**Dave Jones:** fundamental building block of a Howland current pump. And you'll notice that this is a unity gain difference amplifier. That means that the input and output have a gain of one. They're multiplied by one. Um there's no scaling. Um

**Dave Jones:** and there's a few different things that are interesting about a difference amplifier. The first is that it doesn't matter if one of these terminals is ground. Um in fact, it doesn't matter what they are at all. You'll notice that

**Dave Jones:** the output voltage isn't changing. Um that's because the output is dependent on only the voltage at this node subtracted from the voltage at this node. It doesn't depend on the the values referenced to this ground at all. It's just subtraction of these two.

**Dave Jones:** And in this case, it's 1 - 0 is 1. And in this case, oh, it's 0 - -1, which is 1 again. And there you go, you have it at the output. So, that's the fundamental building block. And if you add a resistor to load the

**Dave Jones:** op-amp, just a load resistor, it doesn't actually do anything to the gain. It doesn't do anything to the grounds. Um and it really doesn't affect the circuit at all. So, that is probably the first step to building a Howland current pump. Um

**Dave Jones:** first I'm going to remove this ground cuz it really doesn't matter. It doesn't do anything for the circuit. And I guess the next thing to notice is that if you have 1 V on the output and 1 K

**Dave Jones:** here, then you're always going to have 1 mA going through it. And that that can be used that can be a useful trait in um understanding a Howland current pump. So, if we made this 1 ohm, which I'm going to do now,

**Dave Jones:** you'll notice that the output hasn't changed at all and the the um gain hasn't changed at all. There's an interesting property of this circuit and it's that the whole circuit is basically referenced to this point. It's the only

**Dave Jones:** ground in the circuit. And that means you can make it a virtual ground, um which um is frequently created with just a unity gain op-amp. So, let's create a um a buffer.

**Dave Jones:** And we're going to buffer ground. It's kind of useless, but I will get to this. And I'm just going to move the load all the way over here. And I'm still going to connect it to ground. And then I'm going to

**Dave Jones:** connect that buffer up here. Just move it down a little bit. And move that up. So, this is all fine. Now we've got this virtual ground here. And we can also connect it here. We can connect the virtual ground to the the

**Dave Jones:** ground over here. And it doesn't actually matter what this voltage is. The whole circuit will shift with it because every element every node in the circuit is referenced to this point here, the virtual ground. Um where the absolute ground is over

**Dave Jones:** here. So, what we're going to do is apply a voltage source here and see what happens. So, if I put 1 V here, the whole circuit has shifted up. That's 2 V. That's 2 V. Okay, so with that

**Dave Jones:** we can say that um this is a true virtual ground. We can use this as a virtual ground without really worrying too much. And this output is still actually 1 V when you compare it to the virtual ground, which

**Dave Jones:** is here. So, let's do that. Let's probe the op-amp output with respect to the virtual ground. Um and I'll just use one of these probes over here. Just like this one.

**Dave Jones:** And you'll see it is 1 V as it always should have been. So, if we change the offset of the whole circuit to 2 V, now it's it's outputting 3 V, but the virtual ground is now 2 V.

**Dave Jones:** And 3 - 2 is still 1 V. So, what we're able to do with that is create a constant voltage over this resistance. And a constant voltage over a resistor is a constant current. So, now what we can do is something like this. We can

**Dave Jones:** put a another resistor here. And no matter what we change this to, it will still have 1 mA going through it. Um where the path through the resistor is down here.

**Dave Jones:** And I'll just make more obviously labeled circuit. There you go. Where the path is down here for the current.

**Dave Jones:** And the reason it's constant is only because you've got a constant voltage across this resistor. Now, a unity gain buffer has a few properties to it. It has the property that the input is very high impedance. A very high impedance when compared to

**Dave Jones:** these values here. And the other property is that the output is very low impedance as in it has it has a very low output resistance. And that is actually what this has. This 1 ohm is very low resistance.

**Dave Jones:** Um so maybe without too much error, we can simply remove that buffer entirely and place it like this. Now, this has a problem. You'll notice that a lot of the current is flowing in from the um non-inverting of the op-amp.

**Dave Jones:** And that is creating error. See, we've actually got 1 and 1/2 amps going 1 and 1/2 milliamps going through that output resistor. Now, how do we deal with that? Well, the real issue was the impedance. We we want

**Dave Jones:** that that terminal here to be as high impedance as possible. So, all we have to do is increase the resistors for that section of the circuit. And now, almost no current is traveling through this section of the circuit

**Dave Jones:** because it's behaving very high impedance, as in um very high resistance. That means that you've got a very low current if the voltage isn't enormous. Um so, you can say that the vast majority of the current is flowing through this

**Dave Jones:** resistor here, through here. And you only lose a very small fraction through this wire. In this case, it's 5 microamps, which is just nothing. And this is the Howland current pump. It's a very simple circuit. The sources of error are of

**Dave Jones:** course um the current going through this section of the feedback loop, the input offset of the op amp. You With high impedance feedback resistors, you you get input current, you get this current bias, and that will create a sort of offset, which

**Dave Jones:** can become a problem. And you can also get some stability issues um with the circuit, and sometimes you'll want to do something like this. But often this isn't the case, and often you can just get away with just doing

**Dave Jones:** some old resistors, and yeah, be all right. Um um This is the Howland current pump. Hope you've learned something from this video. If you like it, leave a thumbs in the thingy, and uh I will see you next

**Dave Jones:** time. Bye.
