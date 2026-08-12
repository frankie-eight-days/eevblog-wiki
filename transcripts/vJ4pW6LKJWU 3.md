---
video_id: vJ4pW6LKJWU
title: EEVblog 1482 - Mains Capacitor Zener Regulator Circuit
url: https://www.youtube.com/watch?v=vJ4pW6LKJWU
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 25, "3": 46, "4": 63, "5": 77, "6": 92, "7": 102, "8": 117, "9": 130, "10": 148, "11": 163, "12": 177, "13": 193, "14": 207, "15": 226, "16": 241, "17": 255, "18": 267, "19": 279, "20": 293, "21": 305, "22": 318, "23": 335, "24": 351, "25": 367, "26": 384, "27": 403, "28": 420, "29": 436, "30": 447, "31": 460, "32": 478, "33": 491, "34": 506, "35": 518, "36": 530, "37": 547, "38": 560, "39": 573, "40": 586, "41": 604, "42": 622, "43": 638, "44": 653, "45": 666, "46": 680, "47": 693, "48": 707, "49": 722, "50": 737, "51": 750, "52": 766, "53": 781, "54": 797, "55": 807, "56": 820, "57": 831, "58": 845, "59": 856, "60": 872, "61": 886, "62": 899, "63": 913, "64": 930, "65": 946, "66": 958, "67": 968, "68": 981, "69": 995, "70": 1009, "71": 1022, "72": 1037, "73": 1049, "74": 1061, "75": 1074, "76": 1090, "77": 1105, "78": 1118}
---

**Dave Jones:** Hi, in a previous video linked up here and down below if you haven't seen it, I repaired an Arlec space heater and I did a Dave CAD drawing of basically what was happening here for the power supply and

**Dave Jones:** well, I won't spoil it for you what the failure was. Just go and look at it. So, all I showed on my Dave CAD drawing was a 47 ohm resistor here, a bridge rectifier and then the AC capacitor down

**Dave Jones:** here with some bleeder resistors across there. And it basically generated the 24-V output from the bridge rectifier, 24-V to power the relay and the LED display control circuitry and stuff for the heater. And somebody asked me, "Well, how do you actually get 24-V out

**Dave Jones:** of the bridge rectifier?" They didn't quite understand and that's because yeah, I forgot to include the actual regulation side. So, we're actually going to look at a capacitive dropping mains Zener rectifier. Let's check it out. Now, this won't be an in-depth tutorial on Zener

**Dave Jones:** diodes cuz I've already done that, linked up here as well as down below. Check that out if you want to work out the intricacies of powering stuff with Zener diodes. Zener diodes use a current through them like this to actually

**Dave Jones:** regulate the voltage across them and when you include the load, the calculations can get a little bit tricky for Zener diodes. So, we won't cover that detail here. It's in my previous tutorial video which is quite extensive on the Zener diode topic. But basically,

**Dave Jones:** as you saw on the PCB, here's a photo of the PCB. The Zener diodes are actually on the top side. They're through-hole parts, but I've just photoshopped them onto the back side of the board so you can see what's happening. And you might

**Dave Jones:** think that they look like back-to-back Zener's, but if you actually trace out the circuit, which I've done here, not extensively, it's not a full reverse engineering, but we can actually see what's going on here because just the the rectifier on its own is not

**Dave Jones:** enough to regulate the voltage. You do actually need a regulation element. All the diode bridge rectifier is doing is current steering where the current needs to go because I've got to put it here. You've got 240 volts AC in which is 240

**Dave Jones:** volts here in Australia and the bridge rectifier you've seen you're used to this configuration of the bridge rectifier, but it's exactly the same as this. So let's assume that the AC waveforms on the positive part of the cycle here, then we're going to get

**Dave Jones:** the diode steering it like that and we're going to get another diode steering it like that. So then we can get current to flow in our circuit, but when this flips around negative to positive like that, then we're going to

**Dave Jones:** get a diode like that and get rid of that one and then that's going to jump over there like that and we get rid of that one and now the current can flow from positive through negative like that

**Dave Jones:** and each alternating cycle of the 50 hertz AC waveform, then it just gets the current always going in this direction like this. Never goes backwards. And that's the job of the bridge rectifier, but if you've got nothing here, then

**Dave Jones:** there's no load. It actually won't do anything. It you'll get no current flowing at all really apart from parasitic capacitances. Unfortunately, I don't have the PCB with me anymore so I can't actually measure it, but we were we're actually getting

**Dave Jones:** that 24 volts clamped over there and we saw that our input capacity here, it was an X2 class capacitor normally 220 nanofarads, but it had actually dropped in value to 100 nanofarads and this happens to AC capacitors like this when you get

**Dave Jones:** surges on them. The self-healing dielectric inside actually uh, plasma vaporizes tiny little holes and over every time you get a surge, the dielectric self-heals. It doesn't uh, short out, usually. Uh, that's his job. It heals itself by burning the little

**Dave Jones:** metal metallized plastic inside the uh, poly put the kettle on capacitor. When I say poly put the kettle on, it can can be polypropylene polycarbonate. There's various different types of poly material uh, used in capacitors. And uh, it's

**Dave Jones:** it's metallized on top metal layers. Then when you get a surge on there, it's sort of like punches through a tiny little hole. We're only talking micron uh, size stuff here. And then a little plasma arc forms and it just vaporizes

**Dave Jones:** the metal in there. And then just it forms an insulator again. So you've just got that hole uh, with the insulator. Here's a little graphic um, kind of showing what happens there. And this is why you generally use a self-healing

**Dave Jones:** capacitor in a circuit like this. But one of their problems is that over time they can lose capacitance due to uh, you know, main surges and stuff like that actually uh, causing uh, loss of capacitance due to all these little holes opening up on

**Dave Jones:** your capacitor. You've only got so much area on your capacitive uh, plates. Sooner or later, it's going to drop in value. So we saw a pretty drastic one here, you know, 220 down to 100 nanofarad. But that 100 nanofarads then

**Dave Jones:** caused our regulator to drop out of regulation and we weren't getting 24 volts across here. I think we're getting like 12 and a half 13 volts. We're getting roughly half the voltage out of our Zener diode. So why does that

**Dave Jones:** happen? Well, the effective uh, resistance of this uh, 220 nanofarad capacitor, it actually goes up in value. And the standard capacitive reactive formula XC is 1 on 2 pi FC. F is the frequency, 50 hertz here in Australia.

**Dave Jones:** Um, C is the capacitance. So if your capacitance value drops, then your resistance goes up. So that's called the capacitive reactance. Sometimes uh, you'll hear people call it impedance. And they kind of use interchangeably, but capacitive reactance is actually

**Dave Jones:** just the value of the capacitor itself. Impedance also means the capacitive reactance value itself just due to the capacitance plus the internal equivalent series resistance in there. So, like the total resistance, that's what's called impedance, but they're kind of used like

**Dave Jones:** interchangeably, impedance or reactance. But, strictly speaking, they are different terms. So, this impedance is what's known as the AC resistance of the capacitor, and this is basic AC circuit circuit theory. The effective resistance of a capacitor is going to change with

**Dave Jones:** frequency, but because we've got a fixed frequency, 50 Hz 240 V mains here, then we're always going to get about 14.5 K effective AC resistance of the capacitor. So, basically, that is our dropper resistor for our Zener diode here, cuz the Zener

**Dave Jones:** diode always needs a dropper resistor in here, but what is this 47 ohm resistor up here? Well, it's actually because it's very low, it's like 47 ohms compared to 14.5 K ohms, it's not the dropper resistor for the Zener here. It's actually inrush

**Dave Jones:** protection because when you first plug the appliance into the mains, if you've got a capacitor directly across it, which you effectively do with a capacitor and just assuming your load is like a very low value, then the capacitor appears as a short circuit.

**Dave Jones:** So, you want to actually have some inrush protection. So, that limits the surge current when you first turn it on, and in this particular case, it might I've actually drawn it with a fuse symbol in there because I don't know for

**Dave Jones:** certain, but it might be a fusible resistor, and that's quite common in this sort of application. So, if your capacitor does fail short circuit, then your resistor is going to pop. So, this is how you can actually get a power

**Dave Jones:** supply directly from the mains. It's a mains driven Zener diode voltage regulator, but the huge disadvantage of this is that everything in this circuit here is at mains potential, okay? It's not isolated. There's no isolation transformer, even though your circuit

**Dave Jones:** might be 24 volts or 3.3 volts to power your circuitry. You don't want to go around touching and probing in your circuit, especially with your oscilloscope. Done the whole video how not to blow up your oscilloscope. You don't want to be connecting your scope

**Dave Jones:** ground on here or anything like that. You don't want to be touching it with your wet finger. Cuz you really come a gutter. It's at some sort of mains potential. No touchy. But this sort of Zener regulation circuit directly from the mains is cheap

**Dave Jones:** and simple, and that's why it's used in tons of you know, you'll find them in light bulbs and all sorts of appliances like this cuz you don't need an isolation transformer and all that sort of stuff. That costs a huge amount

**Dave Jones:** extra. Real cheap ass designs even do away with the inrush protection. And you might have like a mob across here as well for like extra surge protection and stuff like that. This particular one didn't. So what you've got here is a

**Dave Jones:** basic AC resistor here, a 14.5 K, stays constant with the 50 hertz frequency, and a Zener diode here, and then you can have your resistor load on there. And we can actually work out roughly how much current we're going to get

**Dave Jones:** total including the Zener current and the load current cuz you have to separate them. That's in my Zener tutorial. And it's roughly 240 volt RMS here divided by 14.5 K. But I know what you're saying Dave, we also have to

**Dave Jones:** subtract the Zener voltage here. Well, in engineering when you're doing ballpark calculations like this, and that's all we're doing in this video is ballpark calculations because 24 volts is like an order of magnitude less than 240 volts. If something's like an order

**Dave Jones:** of magnitude Um, to what you're talking about, like if you have a resistor that's an order of magnitude higher in parallel with another resistor, you just like ignore it. And that's what we're going to ignore here. Just ignore the Zener

**Dave Jones:** voltage. So, 240 volts divided by 14.5k, around about 16 milliamps or so through the resistor here and through the Zener and/or load. But, because this load actually is a relay coil and here's the data sheet for it and you'll see that a

**Dave Jones:** 24-volt relay is actually a 50-milliamp coil current. So, oh, we're There's not much current left over to actually drive the Zener here. So, uh, it's kind of right on the border and this is why, um, the when our 220-nanofarad capacitor

**Dave Jones:** dropped in capacitance value and the resistance went up, there just wasn't the current available to maintain regulation in the Zener and the Zener voltage dropped and then we didn't have enough spoiler alert didn't have enough voltage to turn on the, uh, relay coil.

**Dave Jones:** We just didn't have the 24 volts and, uh, the actual coil current available because this value here went up in value, um, as the capacitance dropped due to the one over, uh, formula here. So, yeah, and that just starved the

**Dave Jones:** relay of current and it couldn't switch on. So, the simplest AC regulated, uh, supply that you can get is just basically a capacitor or a resistor. I'll talk about that in a second, uh, in series with a diode bridge and a, uh,

**Dave Jones:** and a Zener diode. And that's it. Bob's your uncle. You've got a regulated, um, whatever 24 volts, 3.3, 5 volts, whatever it is, uh, to power your circuit. But, as I said, it's a little bit dangerous. It's not isolated, no

**Dave Jones:** touchy. But, if you use it inside an enclosed product where, uh, the customer can't actually touch it, then, meh, it's good enough. So, why do they actually use a capacitor? It's It's nothing to do with, uh, AC coupling or anything. You

**Dave Jones:** could actually simply use a resistor in here. No worries whatsoever. You could put in a 14.5 K resistor instead of a cap. In fact, it's probably cheaper. Why don't they do that? Well, look at the calculations here, okay? So, let's

**Dave Jones:** calculate the power if we used an actual resistor up here. Power dissipated in that resistor. Um so, we'll call that PR and it's I squared R is the uh power uh formula. So, it's 16 milliamps squared because 240 volts divided by 14 and 1/2

**Dave Jones:** K, 16 milliamps squared times 14 and 1/2 K, it's 3.7 watts. Now, that's actually a fairly beefy resistor. That's a a lot of and it's a lot of power uh to waste away as well if you're doing a a

**Dave Jones:** low-power circuit or something like that. If you're driving, you know, some LED light or something like that, you you don't want to be pissing away 3.7 watts in the resistor. So, instead, you use a capacitor because there's no power

**Dave Jones:** loss, ideally, in an ideal capacitor, there's no power loss at all. The dissipation, even though it's equivalent resistance is 14.5 K, the power loss in this capacitor is effectively zero. Or, there'll be a tiny amount due to the

**Dave Jones:** equivalent series resistance in here, but that's really really really small. Now, of course, to understand this, you have to get into power factor and there's no free lunch here, okay? You still have to provide at the generator at the power station somewhere still has

**Dave Jones:** to provide the 3.7 watts, but because this is a mostly capacitive circuit, the power factor is going to be absolutely horrible. So, even though the power generator has to deliver the power, the actual uh load here does not dissipate

**Dave Jones:** any power because it's a capacitor. So, that's why they whack a capacitor in there. So, um you know, if you especially if it's a little compact device or something, you know, you don't want to be wasting. We're only talking

**Dave Jones:** like 16 milliamps here. It's not much current. You don't want to be wasting 3.7 watts to deliver your 15 milliamps. So, but it kind of like puts the problem back onto the grid, but the grid a kind of uh you know, sort of they try and

**Dave Jones:** balance it out with power factor correction and all the rest of it. And we won't go into that. I think probably done a video on that. If I have, I'll link it in. So, this circuit's a bit unusual. I kind of uh expected at first

**Dave Jones:** glance um that they would just use, you know, have the 24-V rail and Bob's your uncle, maybe a secondary regulator in there uh to power the 3.3 or 5-V uh digital logic. There's a little micro with a uh display and stuff

**Dave Jones:** like that. But, they've actually gone for this configuration here. I haven't drawn the micro in, but basically what it is, they've they've got a Zener diode up here and a smaller one down here. So, this is uh the high-voltage one and this

**Dave Jones:** capacitor's a 50-V one and this is a uh lower-voltage jobby down here. And I believe this lower uh Zener down here will be like 3.3 or 5-V, whatever is uh required for the uh digital logic uh circuitry. And here's the uh relay coil

**Dave Jones:** here and the PNP driver transistor up here. They've got a back EMF diode across that as well. So, that's across the top Zener, but then they're actually uh rather than then taking that 24 volts and then dropping it down again, they're

**Dave Jones:** actually using the return path here uh for the coil to go through this Zener here. So, basically uh the current's going through both and the load is being switched uh out of this one and then into this one down here. So, calculating

**Dave Jones:** the power of these two Zeners gets a bit complicated depending on whether the relay's on or off. Cuz as I said, the the relay is like uh the relay's nominally like 15 milliamps plus uh the whatever the LED circuit and your uh

**Dave Jones:** microcontroller takes, you know, another couple of milliamps there at least, you know, 5 milliamps or something uh there at at least. So, you know, it really doesn't uh leave um anything over for your Zener regulation. So, this at ballpark calculations seems to

**Dave Jones:** be a bit dodgy design, and that's why it was not tolerant to this value actually dropping in capacitance when a surge has caused that capacitor to self-heal and lose capacitance. And as I showed in my Zener tutorial video, choosing the power

**Dave Jones:** rating of your Zener diode here, you have to take into account your minimum and maximum loads. In this particular case, depending on whether the heat is on or off, it's going to be like 15 milliamps or whatever difference in the

**Dave Jones:** relay current. They might even be running it at a lower voltage. You know, you don't need exactly 24 volts to operate that. Relay is going to have a minimum latching voltage, minimum latching current. You'd have to look at

**Dave Jones:** the data sheet for that kind of thing. So, I think I think because there's hardly any margin in here at all for the extra current. So, I think that they this top one's not actually 24. It could be, you know, 20 or something like that

**Dave Jones:** because we measured 24 total across here. So, then they've got this NPN down here, and this is actually powered this is what's powered from the micro. So, the micro is powered from like the 3.3 or 5 volts here, and that switches on

**Dave Jones:** this NPN transistor, which then turns on the PNP. Then you've got a small base current across both these Zeners here, and then it switches on the relay, which then turns on the heater coil here. And we almost forgot about the bleeder

**Dave Jones:** resistors across the two 220 nanofarad capacitor here. This is for safety. So, when you pull the thing out, this capacitor could be charged up. You pull it out of the outlet, and you don't want to touch the pins because then you could get a

**Dave Jones:** zappy. So, you've got two high value resistors, 750 K each, and so 1.5 meg total across the 220, and that just bleeds the charge off that capacitor. So, then the user, if they accidentally touch the mains pins, they're not going

**Dave Jones:** to get a zap from it. And the reason that they use two resistors is in series physically here on the board, you can actually see the two there, is that the SMD resistors that they're using, they're only rated for about 200 volts

**Dave Jones:** each. So, they have to put two in series to get the voltage rating required. So, there you go. I hope you found that quick follow-up interesting. As I said, this is just ballpark stuff. More detailed calculations I'd actually have

**Dave Jones:** to get physically get the board back and do measurements and you know, you could go into more detailed stuff. But, please watch that Zener tutorial if you want to know all about using Zener diode circuits for regulation. But, that's what they're

**Dave Jones:** doing here. It's basically a capacitive It's This is not what's called a capacitive divider power supply, which is basically two capacitors two or more capacitors in circuit and then using that AC resistance to actually tap off a smaller voltage than

**Dave Jones:** the 240 V you're feeding in. They're basically This is just a Zener circuit here, which as I said, you could use a resistor here or you could use a capacitor. They use a capacitor cuz they want to get the power dissipation down and then

**Dave Jones:** force the problem off onto the power generator. So, if you found that video interesting, please give it a big thumbs up and as always discuss down below and check me out on my alternative platforms Odysee and Utreon as well. I've got like

**Dave Jones:** 65,000 subscribers over on Odysee as well as some exclusive content over there as well. Catch you next time.
