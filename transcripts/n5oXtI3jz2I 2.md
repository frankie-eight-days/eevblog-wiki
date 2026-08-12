---
video_id: n5oXtI3jz2I
title: EEVblog 1728 - AC Basics Tutorial Part 6: Impedance, Conductance, Susceptance, Admittance
url: https://www.youtube.com/watch?v=n5oXtI3jz2I
source: youtube-asr
timestamps: {"0": 0, "1": 11, "2": 25, "3": 40, "4": 57, "5": 76, "6": 93, "7": 111, "8": 130, "9": 146, "10": 162, "11": 178, "12": 195, "13": 210, "14": 224, "15": 241, "16": 260, "17": 273, "18": 288, "19": 301, "20": 319, "21": 333, "22": 345, "23": 360, "24": 373, "25": 392, "26": 412, "27": 428, "28": 445, "29": 461, "30": 479, "31": 495, "32": 509, "33": 524, "34": 541, "35": 557, "36": 569, "37": 585, "38": 600, "39": 614, "40": 629, "41": 644, "42": 658, "43": 674, "44": 689, "45": 705, "46": 717, "47": 733, "48": 750, "49": 769, "50": 788, "51": 811, "52": 830, "53": 851, "54": 866, "55": 885, "56": 904, "57": 918, "58": 932, "59": 945}
---

**Dave Jones:** Hi, welcome to part six in the AC basics tutorial series. This one actually follows on from part four, so linked in down below. The entire playlist is linked in down below if you haven't seen it. You've got to watch the previous

**Dave Jones:** ones to follow along. Today we're going to take a look at impedance, conductance, susceptance. Say that three times quickly and admittance. And the most important one here, the most common one that you're going to use is of course impedance. And you'll hear me

**Dave Jones:** just throw the word impedance out there in countless videos. And also we'll talk about what that actually means. Conductance probably the next one you might have heard about, but you might not know why you might want to use it.

**Dave Jones:** And susceptance and admittance, they're more obscure that you might use for complex circuit solving or something like that. Generally not something that you'd use in most everyday practical usage, but impedance certainly. So let's start with that. Now you can think of

**Dave Jones:** impedance as AC resistance if you want. And it's designated by the letter Z here. No that Z, American rubbish, Z. Thank you very much. And its units are in ohms just like regular DC resistance, but this is AC resistance and your AC Ohm's law

**Dave Jones:** equation still applies. So the impedance in ohms, the AC resistance, is the AC voltage divided by the AC current. Basic Ohm's law except applied to AC. Because as you'll see here we've got AC power sources generating in this case a

**Dave Jones:** sinusoidal, but it doesn't matter. Now in part four we looked at inductive reactance and capacitive reactance designated by XL and XC here. Every inductor is going to have an equivalent reactance which is also measured in ohms. And likewise every capacitor is

**Dave Jones:** going to have a reactance also in ohms. But when we're talking about complex AC circuits which are going to have resistors, inductors, capacitors, and remember every element of a circuit has resistance, inductance, and capacitance as well. The wires in your circuit, they

**Dave Jones:** have little tiny inductors in them. The internal resistance of your battery, little and the contacts in your battery, for example, your power source, little tiny inductors in them. The inductor itself actually has inductance in its connective leads. And it's got

**Dave Jones:** capacitance in there between the windings and your resistor, that's actually got some inductance in it as well, tiny amounts. We're talking about equivalent components here. They all have inductance, resistance, and capacitance. So, there's no such thing as just a purely inductive

**Dave Jones:** circuit. Doesn't exist. So, every complex circuit, as it's called, cuz remember we've done a video on complex numbers. When you start talking AC signals, you start talking complex numbers, complex impedances, where the voltage and the current can be out of

**Dave Jones:** phase, and you can have that phase relationship. Anyway, we won't go over all the details, it's in part four. So, basically, in any complex circuit like this, we're going to have an equivalent resistance, it's called. And that equivalent resistance is the impedance Z

**Dave Jones:** in ohms. But then we have to break it down. We've got a resistive component, and we've just got, in this case, a purely conductive component here. And that in that inductor has an inductive reactance in ohms. So, the total

**Dave Jones:** impedance, the total equivalent resistance of this circuit, or this component, I guess you could call it, if you're talking about, say, the inductor with its internal resistance, you could be talking about that. So, the total equivalent resistance, or impedance,

**Dave Jones:** they're both in ohms, they're two resistors in series. So, a simple series circuit, it's the R in ohms, of course, plus remember it's complex now, so it's J XL, positive J XL, because if you remember part four, inductives is

**Dave Jones:** positive, capacitance is negative. That's why capacitive reactance over here is exactly the same except there's negative J XC. And remember, XL and XC are in ohms, so we're adding ohms to ohms to give you a total equivalent impedance of the circuit or equivalent

**Dave Jones:** AC resistance. So when you're talking about the total equivalent resistance of the circuit, the impedance of the circuit, you don't have the XLs and the XCs anymore, so you drop the L and you drop the C and it basically the

**Dave Jones:** impedance is Z equals R plus J X. It's just the reactance, not the capacitive reactance or inductive reactance. You don't care because, you know, it doesn't matter what that element is. It's just a reactance. So it just becomes R plus J X

**Dave Jones:** and it could actually be a negative in there as well if it just happens to work out that way with capacitance dominated by capacitance, for example. But that is in, remember we've done polar and rectangular forms. This is in

**Dave Jones:** rectangular form. Look at previous videos for how to convert polar and rectangular. And I know because you're keen, there's the formula for converting from the rectangular form to the polar form, which is Z angle theta in there. So I won't cover that again. We've

**Dave Jones:** already done that in the previous video, but you can have that in either form, whichever one is easier for you to work with later on. And once you've worked out your various impedances in your circuit, then your regular like resistive series

**Dave Jones:** parallel stuff applies. So if you've got three impedances in series like this, it's just the total impedance is Z1 + Z2 + Z3. That's it. Or if you've got them in parallel, it's 1 over ZT + 1 over Z1

**Dave Jones:** + 1 over Z2 + 1 over Z3. Easy. Exactly the same as what you'd use for resistors in DC. But, just remember these are in complex form, either rectangular or polar. They have a phase component to them. So, you will be doing complex

**Dave Jones:** number calculations when you add these up or do your divisions down here. So, depending on which form you want them in is going to be easier to do your calculations in the complex realm. And you might have heard me using the past

**Dave Jones:** the term characteristic impedance when I'm talking about coaxial cables, transmission, you know, PCB transmission lines and stuff like that. Don't confuse that with impedance. Impedance is basically talking about a circuit element that refers to the voltage and the current in the, you know, the total

**Dave Jones:** impedance of like a circuit element or a, you know, a bunch of elements in a circuit. Whereas, characteristic impedance is specifically a term used for distributed element transmission line. So, it's incorrect to say the impedance of that coaxial cable is 50

**Dave Jones:** ohms. It's not. It's the characteristic impedance. It's kind of different. So, yeah, just don't get them confused. And the characteristic impedance of a transmission line typically won't change with frequency. Whereas, something like this, it certainly does. It changes with

**Dave Jones:** every hertz, every millihertz frequency change, the impedance changes. But, the characteristic impedance the distributed characteristic impedance of a transmission line doesn't really change with frequency. It'll have a roll off at the end, but generally speaking, it doesn't change. So, they're essentially

**Dave Jones:** two different things. Even though they're both impedances in ohms, they're just talking about different systems. So, don't be confused. So, just remember the difference between reactance and impedance, even though they're both in ohms, is that reactance is purely the

**Dave Jones:** complex part. Uh it doesn't include any real component at all, which is what the resistor is here. So, the impedance equals the real component plus the imaginary component, which is the reactance. And that's the difference between, even though they're both in

**Dave Jones:** ohms, there is a difference. Impedance is a different term, which encompasses both the real and the imaginary. And remember, there's no such thing as like imaginary doesn't mean it doesn't exist. You have to watch the previous videos. It's the imaginary or complex part of

**Dave Jones:** it. Real plus complex. Next term we're going to take a look at is conductance. And its symbol is G. So, if you see G in any electronics uh thing, you're talking about not gigohms, it's not a unit. G is the

**Dave Jones:** symbol, and its units are siemens or S. And you could have nanosiemens, for example, which I'll show you in a minute. And the conductance is really easy. And you can think of it as the ease of current flow through a circuit

**Dave Jones:** or a component. How easily does the current flow? And you might think, well, that's resistance, isn't it? And yeah, it basically is, but it's the opposite. Hence why the conductance is one on the resistance. And we're talking the real

**Dave Jones:** resistance here. We'll talk about that in a minute. It's the inverse of resistance, because resistance is not how easily a current flows through the circuit, like conductance is. It's how much resistance it provides, hence the term resistance. Um but G, you can think

**Dave Jones:** of it as the ease of current flow. It's just one on R. That's it. But why would you want to use this? Well, several reasons. The most obvious one is when you're dealing with circuit elements that have a lot of resistances in

**Dave Jones:** parallel, then you saw that formula before, the parallel resistance formula, especially if you've got more than two items, is one on R equals uh one on R1 plus one on R2 plus one on R3 and so forth. So, you got all of these inverses

**Dave Jones:** in there. Well, it's easier if you just invert them all to begin with. I know it's kind of like a trivial thing, but it really makes difference if you're trying to do lots of like parallel system or circuit equations. It's just

**Dave Jones:** easier to convert them into conductance in siemens. And once you've done that, you can simply add them up. And if you happen to have conductances in series like this, well, you guessed it. It's instead of just adding them up like you

**Dave Jones:** would with resistance, you get the parallel resistor equation. In this case, it's for conductances. One on the conductance total is one on G1 plus one on G2 plus one on G3. So, really if you have conductances in series, you

**Dave Jones:** probably should just convert them to resistances and it's easier to deal with. And conductance isn't just useful in electronics. It's used in physics and semiconductors and it's used in material science. If you've got some sort of material like how easy is it for the

**Dave Jones:** electrons to flow through the various materials you got in all sorts of material science and things like that. So, it's not just electronics, but it's also used in like semiconductors and things like that. So, you might have heard of transconductance in transistors

**Dave Jones:** for example. That is conductance. It uses the same units, siemens. It's got a G as well, but it's called transconductance because it's more of a like dynamic component than like just a fixed sort of like real component we

**Dave Jones:** have here. So, that's used a transconductance used a lot in like transistors and other semiconductors. Just check out a data sheet. And if you want to see conductance in the real world, take the venerable Fluke 875 multimeter. It actually measures

**Dave Jones:** conductance. You switch to ohms mode here. I'll zoom in and if you go into manual range here and you press it again, bingo, it's got a reading in nS. That's nano siemens. So, unless you want to work in siemens, well, you take the

**Dave Jones:** reading directly. Otherwise, if you want resistance, you've got to get your confuser out and you've got to invert that value to give you ohms. And that's used for a very high resistance stuff. Hence, like if for material science and

**Dave Jones:** things like that as well. You know, you're talking about, you know, like really leakage stuff. You're talking about dielectrics as well in PCB materials and things like that. Really high values of resistances are often dealt with as conductance in siemens.

**Dave Jones:** And I mentioned before that conductance is always a real component. There's no complex imaginary mathematical part to it. It's all That's why it's one on R. It's not one on impedance. It's one on the real resistance that we actually saw

**Dave Jones:** before. So, that brings us to susceptance and admittance. These are the complex part of conductance, basically. And once again, they're in siemens and you'll see why in the end when we tie it together. Um so, siemens in S and susceptance is uses the symbol

**Dave Jones:** B and it's simply one on X, which is the reactance that we saw before, that complex reactance, whether it's capacitive or inductive. And just like we did before, we can break down the reactance into inductive reactance. So, B L is just one on XL and likewise, BC,

**Dave Jones:** the capacitive susceptance is one on XC, the capacitive reactance. It's simply the inverse of reactance. That's it. That's your susceptance. So, the term susceptance, say that three times quickly, is related only to the reactive part, the reactants part of your complex AC

**Dave Jones:** circuit element. But, admittance includes both the real conductance part and the susceptance part, and its symbol is Y, and it's simply one on the impedance. Cuz remember, impedance before was the real plus the imaginary, and that's what admittance is. It's one

**Dave Jones:** on the impedance with units, once again, in siemens. So, if we tie this whole video together, why our admittance is equal to the real component, which is conductance in G, it's equal to G, plus J, because it's a complex component, JB,

**Dave Jones:** like this. Just like we had before, the impedance is equal to the real part, which is the resistance. And remember, G is just uh basically, these are the inverse. It's exactly the same formula, except everything's one on. It's

**Dave Jones:** topsy-turvy, upside down. Uh impedance equals the real component and the real resistance plus uh the complex reactance. Likewise, the admittance Y is equal to the real part, which is the conductance G, plus the complex part, which is the susceptance over here.

**Dave Jones:** Simple. So, we've tied it all together. Impedance, conductance, susce- susceptance, and admittance. Beauty. So, as I said, impedance is the one that you're going to use most often, but conductance, susceptance, and admittance are also important, not only in electronics, especially if you get

**Dave Jones:** into uh some, you know, more complex circuit analysis, it's just easier to use. And as I said, in materials science, if you're dealing with like electrolyte or an electrochemist or something like that, as Mrs. E V blogger, she's an electrochemist, um

**Dave Jones:** she'll know all about conductance, um because that's what you'll be typically using um, instead of resistances and things like that. So, um, I hope you enjoyed that. It's not something that you'll typically have to deal with in practical electronics unless you're

**Dave Jones:** solving like complex uh, circuits and you know, in various ways and things like that. But, impedance you'll be using all the time and occasionally conductance. It might even be on your multimeter. Check it out. Anyway, hope you found that video useful. If you did,

**Dave Jones:** please give it a big thumbs up and as always discuss down below and check out all the other parts in this series as well. Catch you next time.
