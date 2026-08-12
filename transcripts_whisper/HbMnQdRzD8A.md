---
video_id: HbMnQdRzD8A
title: Guest Video: Bob DuHamel - How Opamp Virtual Grounds Work
url: https://www.youtube.com/watch?v=HbMnQdRzD8A
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 16, "2": 33, "3": 51, "4": 69, "5": 88, "6": 105, "7": 121, "8": 144, "9": 156, "10": 180, "11": 190, "12": 213, "13": 224, "14": 248, "15": 261, "16": 289, "17": 303, "18": 324, "19": 342, "20": 361, "21": 374, "22": 402, "23": 423, "24": 442, "25": 455, "26": 474, "27": 493, "28": 505, "29": 522, "30": 539, "31": 550, "32": 562, "33": 581, "34": 598, "35": 614}
---

**Dave Jones:** Hello, Dave. I'm making this video in response to your video on operational amplifiers, particularly on the section on inverting amplifiers, where you said people become confused because of the signal at the input to the amplifier that seems to disappear at the virtual ground.

**Dave Jones:** I think the confusion happens because people see that we have an input at this point here, but by the time we get to the amplifier, it's zero volts, and the other input is also zero volts, so the inputs to the amplifier are always zero.

**Dave Jones:** So how on God's green earth can an input here be having any effect on the output if the two inputs to the amplifier are always zero volts? Let me give a quick explanation about how operational amplifiers work before I move on. As you said very well in your video, the operational amplifier

**Dave Jones:** will change its output voltage to whatever voltage it takes within the limits of the circuit to make the two input voltages equal. In the case of the inverting amplifier, we take the non-inverting input of the op-amp and tie it to ground. The ground is by definition zero volts,

**Dave Jones:** and it will remain zero no matter whatever else happens to the circuit. The operational amplifier will adjust its output to whatever voltage it takes to make the inverting input also zero volts, and so we call this inverting input a virtual ground. Now when we look at this ground and this

**Dave Jones:** virtual ground, it's important to remember that zero volts is not the absence of voltage. Here I have four 5-volt batteries giving us a total of 20 volts from here to here. Now let me use these pins as a virtual voltmeter, and if I put my voltmeter like this, of course I will read

**Dave Jones:** 20 volts. If I do like that, 5 volts, 5 volts, 5 volts, and 5 volts. If I put my voltmeters like this, once again I have 5 volts, now 10 volts, 15 volts, and 20 volts. But what if I put the black lead of my voltmeter right here?

**Dave Jones:** Then if I take the red lead and I put it here, I will measure positive 10 volts, positive 5 volts, zero volts, minus 5 volts, and minus 10 volts. So my zero volts simply depends on where I put the black lead of my voltmeter when I'm measuring my voltage.

**Dave Jones:** And if I decide that I'm going to measure all of my voltages from this point here, this becomes my ground. And so now my ground is not my lowest voltage, but it's between my lowest voltage and my highest voltage. So I have voltages higher than ground, and I have voltages lower than ground.

**Dave Jones:** So I have positive voltages, and I have negative voltages. So zero volts is not the absence of voltage. Here my zero volts is 10 volts above my lowest possible voltage, and it's 10 volts below my highest possible voltage. So in our typical op-amp circuit, we are going to put our ground

**Dave Jones:** in the middle of our stack of batteries or stack of power supplies. We don't have to, but this is the way we typically do it. And so we measure our voltages. Some are positive and some are negative with zero in the middle. Voltage, like altitude, is a type of potential energy.

**Dave Jones:** And so altitude can represent voltage. We have zero volts on up to 25 volts on the side of my building. I have my black lead of my voltmeter here that I can use to set my ground point. And wherever I put this becomes my

**Dave Jones:** actual zero volts for the circuit. This ruler represents the resistors in the circuit. Right now I have equal space on the sides of my marker here, which means that my resistors are equal. So we have a circuit with equal resistors in the feedback loop.

**Dave Jones:** Now if my lovely assistant will come here. Now she is the brains of the operational amplifier. Her job is to move the output voltage up or down to whatever voltage it takes to keep this centered on my zero volts. There is nothing to anchor this except her moving her output.

**Dave Jones:** And I will be moving the input to wherever I need to because I am the input signal and she is the output signal of the amplifier. So I'm going to put my black lead of my voltmeter at some arbitrary point, like right there.

**Dave Jones:** It says 15 volts, but now this is my new zero volts because zero is wherever you put the black lead of your voltmeter. So now this becomes 1, 2, 3, 4, 5 volts, 6, 7, 8, 9, 10. This becomes minus 1, 2, 3, 4, minus 5,

**Dave Jones:** 6, 7, 8, 9, 10, minus 10, and so forth. So we're going to put the middle of the ruler at the zero point level. I'm going to increase my input signal and she will compensate to make sure that that stays centered on zero volts.

**Dave Jones:** So here I go and there's no fulcrum there other than the op-amp changing its output voltage. So now if I decrease my voltage, the op-amp increases the voltage to make sure that the input stays, or the virtual ground, stays at that zero volts.

**Dave Jones:** Right now it's like DC, it's a steady voltage, but if I continually move this up and down, it becomes like alternating current. And no matter where I move it, she compensates to keep the middle at zero volts. So if I go down to

**Dave Jones:** minus 10 volts, she goes up to plus 10 volts. And that's what the inverting amplifier does. If your two resistors are equal, the output voltage will be the same as the input voltage, but the opposite polarity. Notice that our polarity is not an opposite type of voltage,

**Dave Jones:** but just a difference in the voltage itself. So a positive voltage is merely above zero, and a negative voltage is merely below zero. So I'm going to negative 10, she goes to positive 10. I move back up to positive 10, she goes down to negative 10 to compensate.

**Dave Jones:** Now she's not interested in her output voltage, only in keeping this at the zero. Now if I move my middle here, this is like changing the ratio of our resistors. Let me move this over. Now this is like having the main feedback resistor larger than the resistor on the input.

**Dave Jones:** And so now we put that at the ground, and as I move it, I'm going to move it to plus two volts, and notice she had to put the output to plus, to minus, one, two, three, four, five, six, two volts, and notice she had to put the output to plus, to minus, one, two, three, four, five,

**Dave Jones:** minus five volts to compensate. And as I move this down, she has to move up to compensate, and notice that she's making a bigger movement than I am, because the feedback resistor is bigger than the input resistor. And so the higher the ratio between the two resistors, the more she

**Dave Jones:** has to move her output to compensate. So now we have amplification. I make a small input change, and she has to make a large output change to compensate, always making sure that the junction between the two resistors, which is at the virtual ground, is at the same place.

**Dave Jones:** So as this voltage increases, it does increase the voltage at this point, but then the op-amp reacts by decreasing this voltage to make sure that this voltage stays equal to that voltage, or zero. So this is not zero volts because it is tied to this voltage.

**Dave Jones:** It's zero volts because the output of the amplifier constantly reacts to changes over here to make sure that this stays at the same voltage. If these two resistors are equal, then if this voltage goes up, this has to compensate by going down the same amount.

**Dave Jones:** But if this resistance is higher than that resistance, for example we have twice the resistance here as we have here, now the output will have to compensate by changing the voltage twice as much. So if this goes up one volt, this voltage will have to go down two volts.

**Dave Jones:** If this voltage goes down one volt, this voltage will have to compensate by going up two volts, all in order to keep this at zero volts. So the confusion appears to come from the fact that in an inverting amplifier, the two inputs appear to have no voltage in there.

**Dave Jones:** There appears to be no input. Even though I have five volts here and minus five volts out here, there's nothing at the inputs to the op-amp, so that can be confusing to some people. But remember that zero volts is not the absence of

**Dave Jones:** voltage. It is merely the voltage where we have put the black lead of our voltmeter. In this case, we have 20 volts worth of batteries, and the black lead is in the middle, so there's our zero volts, and we have plus 10 and minus 10.

**Dave Jones:** If we move the black lead down to here, now this is zero volts, and we have plus 5, plus 10, plus 15, and plus 20. And it changes all the voltages in our op-amp circuit too, where now our two inputs are at plus 10 volts, and this is plus 15, and this is plus 5 volts.

**Dave Jones:** This is probably confusing, and that's why we don't do op-amps this way. And we usually use op-amps in places where it makes sense to have both positive and negative voltages. So this is not a good place to designate as our ground or our zero volts.

**Dave Jones:** So let's move the black lead back here, make that our zero volts, make that our ground, and now things make a lot more sense. We have positive five volts here, negative five volts here. The op-amp is doing what op-amps always do. It's adjusting its output

**Dave Jones:** voltage to whatever it takes within the parameters available to make the two input voltages equal. Now those two voltages happen to be zero volts, but that's not because there's nothing there. It's simply the same voltage where the black lead happens to be. So thanks for watching,

**Dave Jones:** and thanks for your video, Dave. It's one of the better videos I've seen on operational amplifiers on the internet. But even you said people get confused about the voltages seeming to disappear when they get to the op-amp. So hopefully this cleared it up for some people.
