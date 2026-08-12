---
video_id: b7UQVZaqxg0
title: EEVblog #95 - Linear Regulators, Closed Loops, Simulations, & Brand Shenanigans
url: https://www.youtube.com/watch?v=b7UQVZaqxg0
source: youtube-asr
---

**Dave Jones:** Hi, welcome to the AAVlog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, now a couple of episodes ago, I showed you a standard linear regulator circuit and how it wasn't that

**Dave Jones:** much different to LDOs and even switch mode power supply regulators. Now, as it so happened, I've actually been playing around with just such a circuit recently. In In fact, pretty much exactly this. I've been using a TLC 2252

**Dave Jones:** op-amp with an MJD 212. In In fact, this is an old circuit I've used and it's just the same as a linear regulator. It's got the op-amp as the error amplifier. It's got the Darlington series pass transistor and it's a very

**Dave Jones:** simple circuit and I touched on how these linear regulator circuits can actually be a bit unstable. In fact, the LDO version with the PNP pass transistor instead of the NPN is more unstable. It requires a certain minimum capacitance

**Dave Jones:** and a or a certain capacitance in a certain range, a certain ESR value of the output capacitor in a certain range to be to have the loop actually stable. And it's the same thing with these linear the standard NPN linear regulator, too.

**Dave Jones:** They actually traditionally require a minimum output capacitance to keep the loop stable. And there's a whole bunch of theory involved in that with, you know, Bode plots and doing phase diagrams and, you know, nulls and and zip poles and zeros and

**Dave Jones:** things like that in the response. I won't go into that. But, what happened is I've used this circuit before, no problems at all, right? But, something happened when I decided to change it a little bit. Let's have a look.

**Dave Jones:** Now, here's the story of what happened this morning. I've used this circuit before as I said and it's stable with hardly any output capacitance and it worked really well. But what I wanted is I wanted to lower the cost. The TLC2252

**Dave Jones:** part is a little bit expensive so I wanted to lower the cost there and I also instead of having a gain of one because you can see it's just a standard follower circuit. I needed about a gain of four or something. So even though I

**Dave Jones:** had a spare op-amp because I was using a quad op-amp chip this time. I had a spare op-amp. I didn't want to do a times four gain on the input. So I thought I'd be smart and I'd change the

**Dave Jones:** TLC2252 to a much cheaper more generic jelly bean LM32 four quad op-amp. You know, it's it's pretty much the industry standard quad op-amp. It's not a bad device actually. It's internally frequency compensated and it's got it works down to common

**Dave Jones:** mode range down to zero and it's you know, it works up to high voltages. It's not a bad you know, basic device at all. But instead of using that extra op-amp I had to do a times gain of four here. I

**Dave Jones:** thought I'd be smart and just whack the times four gain in the in the loop here in the linear regulator loop and that's a standard standard technique. You can do that too. But what happened? No. I built this thing up

**Dave Jones:** and it oscillated to buggery and it didn't matter how much output capacitance I put on there. It was just horrible. It it was just awful. There was nothing I could do to stabilize this loop at all. Terrible. Epic fail. And

**Dave Jones:** yeah, it serves me right. I was a little bit overconfident cuz I used the same circuit before and you know, I thought oh, I'll just use an LM324 pretty basic op-amp. Not much can go wrong there. And I'll just put the gain

**Dave Jones:** in there. And when you add all these things together, yep, Murphy's Law, you guessed it, steps in and ruins your day. And I was using recently high values in the feedback resistors here, too. So, I lowered those to change the pole

**Dave Jones:** response of the thing, and I still couldn't get the sucker stable. So, I thought I'd experiment with some different chips and do a little bit of very quick simulation, and here's what happened. Okay, so I thought I'd just grab my

**Dave Jones:** LTSpice simulation package and see if I could at least try and simulate what I was actually getting in the circuit I physically built up. Now, I didn't have an LM324, so I picked the nearest Linear Technology's equivalent, which is the

**Dave Jones:** LT1014. In fact, it's an LM324 replacement chip. It's like a high-spec version of the LM324, so it's functionally equivalent. So, I thought that'd be near enough. I've got a 15-V power supply over here. I didn't have the exact MJD

**Dave Jones:** 112 Darlington output transistor, so I thought I'd just change simulate that with two 2N2222 industry standard NPN transistors. I know it's all quite a bit dodgy, but I just wanted to see if I could get in the ballpark and at least get this thing to

**Dave Jones:** oscillate in simulation mode. Now, I've got the gain of 3.7. It is actually with the 10K and the 27K feedback resistors here. I've got a nominal load here, which is 10K, and we can play with that later. And I've got a nominal output

**Dave Jones:** capacitance, which I had in the circuit I built up, which was 100 nF. Now, let's run the simulation on that and try it. Here we go. We'll simulate it over 0 to 10 ms, shall we? Let's look at the

**Dave Jones:** output. The output's exactly what we expect. There it is, 370 mV cuz we've got 0.1 V input voltage times the gain of 3.7 is 370 mV and it looks stable at least for the first 10 milliseconds at least. So, very stable.

**Dave Jones:** I'm quite happy with that. Now, let's check the output here of the op-amp. The op-amp doesn't look to be oscillating at all once again over the 10 ms period. So, you know, a bit of a bummer. So, I

**Dave Jones:** thought I'd change the parameters of the circuit a bit by changing the output transistor here. Now, let's pick a new one. For argument's sake, let's just get the FZT849. It's not really critical what one it is. I just wanted to change the capacitance

**Dave Jones:** of the transistor, which will change the zeros and poles in the circuit and and it will just upset the loop stability or change the loop stability of that circuit. So, I've changed that transistor and let's run that simulation

**Dave Jones:** again. Bingo! Look, there's the output of the op-amp oscillating and that's pretty much exactly what I've seen on my oscilloscope. It's quite amazing. Let's look at the output here. Bingo, there it is. The output is also oscillating and

**Dave Jones:** you switch that on at the switch both of them on and you can see that that sucker is completely oscillating. Now, if we change the let's see if we can make it stable by increasing the output capacitance to 1

**Dave Jones:** microfarad, shall we? Let's run it again. No, doesn't make it any more stable. It just changes the frequency of it there. Let's go up to 10 microfarads and let's run that again and no, we're still not getting there.

**Dave Jones:** Let's change it to 100 microfarads and let's run the simulation again. See if it's stable. Now, it looks like it might be reasonably stable, but you can see that it starts there's a little bit of something up there on the output of the

**Dave Jones:** op amp. Now, that's because we're only simulating from 0 to 10 milliseconds. Let's change the simulation time to say 100 milliseconds, and let's try that again, shall we? Bingo, there it is. There was the first 10 milliseconds. We couldn't really see

**Dave Jones:** anything, but as you can see after that, it's still doing the same oscillation. Now, the as you can see the output voltage is actually the output voltage is a bit more a lot more stable than it was before, okay?

**Dave Jones:** So, that output capacitance is solving the problem, you know, that looks like a lot there, but as you can see it's only 370 mV to 368. It's barely half a mV ripple, okay? Or one Yeah, half a mV,

**Dave Jones:** you know, ripple. So, it's not much at all. So, you can make that go away with the output capacitance, but the fact is the op amp is still oscillating like that, and that's horrible. So, that's not a solution at all. So, let's see

**Dave Jones:** what happens if we change the gain of the circuit, shall we? So, let's change that 10K. I won't delete it entirely. I'll just change it to say 10 meg, which will effectively make the gain of that Well, better put in actual meg there,

**Dave Jones:** otherwise it won't work. 10 meg, and that should change Bingo, there There it is. It's still It's still oscillating. It doesn't like that at all. Let's lower this capacitance right back down to 10 microfarads, and let's do it again.

**Dave Jones:** Uh, it's still there. 1 microfarad, and let's try it again. No, it's still going to oscillate regardless. Let's actually delete physically delete that component, and see if we can get that to No, it doesn't like that at all. So,

**Dave Jones:** even let's change that to say 10 ohms. Let's try it again. No, that's not going to make a difference cuz there's not no parasitics there that models not that great, but as you can see, we actually made it do exactly the same

**Dave Jones:** simulation as pretty much what I measured. And I'll show a screenshot of what I actually measured and you'll see that the difference isn't much at all. And of course, if we change this back to the 2N2222, you'll find that it will be Oh, no,

**Dave Jones:** there we go. The 2N2222 also oscillates way up in the region up there. Look at that. Wow. Let's change that to 100 n. And yeah, it's much smaller. So, we're actually getting this sucker to oscillate fairly well. Really quite

**Dave Jones:** amazing the difference in the simulation model and the loop response of just this basic NPN linear regulator when you change the output transistor which has various different characteristics. Really is quite amazing. Let's just do one more little experiment

**Dave Jones:** here because the MJD112 Darlington transistor actually includes two on die on die resistors uh 8K and 120 in this case. We'll add those to these even though it's not an exact simulation. We'll just add them in and see if it changes the power response.

**Dave Jones:** And as you can see, it it it does. It's made it stable. Let's change this output capacitance to I don't know, something silly like 10 pF and have a look. No, it's still stable from 0 to 100 milliseconds. That looks

**Dave Jones:** really quite good. 100 microfarads, but you know, it it's not really um this really isn't an exact um simulation. It's you know, it's probably not even close, but um at least it does show you the uh variability in changing um the

**Dave Jones:** you know, certain circuit parameters in just this uh basic uh linear voltage regulator loop like this. So, you have to be really careful about what um you know, to well, either simulate it extremely closely, but as everyone knows,

**Dave Jones:** simulation really um can't cater for uh the parasitic effects of your circuit when you actually build it on a PCB, parasitic capacitance and and power supply and noise and all sorts of things like that. So, um really it's you know,

**Dave Jones:** it's quite it's just fun and it's quite remarkable to actually just be able to simulate um stuff like the the even using um effectively different components and get a similar result. It's actually you can't always get this, but I thought that was really quite neat

**Dave Jones:** and I thought I'd show it to you. So, there you go. Just be careful when you're doing um even simple loops like this, um look up things like the um zero and pole uh responses of um closed loops like this and it's a really

**Dave Jones:** fascinating subject. It's really quite in-depth if you go into it, but uh I highly recommend you check it out and just be careful next time when you're designing uh even a simple circuit like this. So, what's the solution? Well,

**Dave Jones:** I've still got some experimenting to do, but I had some um LP2902 quad op amps, which is almost identical to the LM324. In fact, they um often share the same uh data sheet, um but it's just a um it's a slightly it's got

**Dave Jones:** an extra current source in there and I wired one of those in, and it made a hell of a difference. It's a hell of a lot more stable. All I need is a little bit more output capacitance, and it

**Dave Jones:** looks like a winner. And also, um I decided to get rid of this times four gain out of the control loop here, cuz that was just causing too much instability. So, I had a spare um op amp, so I'm going to do times four

**Dave Jones:** outside of the control loop, and then add some little bit of extra output output capacitance, use the LP29 02, still the LM324. They're about the same price. Um in fact, they they might even be a little bit uh cheaper, and

**Dave Jones:** uh you know, bingo. It should work a treat. I still got some more experimenting to do, but there you go. That's just an interesting um thing that I was doing this morning. I thought I'd share with you, and it just goes to show

**Dave Jones:** how much a difference slight uh component changes can make in uh in basically very simple control loops like these. And brands of chips can matter, too. There's um a big tip for you. If you change brands of chips, they can be

**Dave Jones:** slightly different, change the parasitic uh you know, effect of your um of your control loop. The pole and the zeros might change slightly, and bingo, it can throw your whole thing out. So, that's something to keep in mind next time

**Dave Jones:** you're designing even simple circuits like this, control loops. You got to know how to optimize them. And yes, there's a lot of theory and math involved in the whole thing, and you can go through that, but in the end, it's

**Dave Jones:** easier just to build your circuit up, cuz all that theory is not going to be right often. It's just going to not take into account um lots of parasitic effects and different brands of components and things like that. So,

**Dave Jones:** really, uh you've just got to build it up, check it, and optimize your circuit for the parts you're actually using. So, just be careful next time. See you.

**Dave Jones:** Mhm.
