---
video_id: i54YDHeU4ww
title: EEVblog 1660 - AC Basics Tutorial Part 4: Resistors, Capacitors, Inductors
url: https://www.youtube.com/watch?v=i54YDHeU4ww
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 26, "3": 43, "4": 57, "5": 70, "6": 84, "7": 101, "8": 117, "9": 131, "10": 145, "11": 160, "12": 175, "13": 190, "14": 205, "15": 217, "16": 230, "17": 246, "18": 259, "19": 272, "20": 287, "21": 303, "22": 318, "23": 333, "24": 347, "25": 362, "26": 377, "27": 391, "28": 402, "29": 416, "30": 434, "31": 448, "32": 465, "33": 478, "34": 490, "35": 506, "36": 524, "37": 537, "38": 557, "39": 575, "40": 587, "41": 603, "42": 617, "43": 630, "44": 646, "45": 659, "46": 676, "47": 693, "48": 709, "49": 722, "50": 740, "51": 754, "52": 770, "53": 781, "54": 798, "55": 814, "56": 829, "57": 844, "58": 858, "59": 870, "60": 883, "61": 895, "62": 912, "63": 927, "64": 943, "65": 961, "66": 976, "67": 991, "68": 1006, "69": 1024, "70": 1040, "71": 1052, "72": 1065}
---

**Dave Jones:** Hi, this is part four in the AC tutorial series. Previously we've taken a look at what AC is and how it's formed and uh phases and also complex numbers as well. And now we have to go back to Ohm's law

**Dave Jones:** because yes, Ohm's law applies to AC just as well as it does to DC and it's basically exactly the same. You don't really have to learn any new formulas but you have to be aware of new concepts. So let's take a look at AC in

**Dave Jones:** resistor, inductor, and capacitor circuits. Uh let's start out with resistors here. Now of course you've got a voltage source here which is AC instead of DC hence why we've got this like generator type symbol with the AC waveform. We've got a resistor here and

**Dave Jones:** current flows through your your circuit. It's the most basic circuit you're going to get and Ohm's law still applies. I equals V on R and rearrange that however you want. But instead of a DC voltage which is just continuous, it never uh

**Dave Jones:** changes although we have had a look at our stepped uh DC responses in uh the previous DC uh tutorial series. So take a look at that one but DC is basically one fixed steady state. But in AC of

**Dave Jones:** course you have a voltage which changes over time like this and given that you've got a circuit with current flowing, if your voltage changes, your current also changes. Ohm's law for AC is exactly the same for DC. I equals V

**Dave Jones:** on R but there's this word instantaneous here. So this is where uh it differs from DC cuz as I said we've got a changing voltage and changing current. So technically Ohm's law only applies for one instantaneous value of time.

**Dave Jones:** That should be T there. So we'll take the case of course of a sinusoidal waveform here. Now this formula here is interesting. V equals Vmax times Vmax being the maximum value of the you know like peak value of the waveform V peak,

**Dave Jones:** if you want. Uh V max times uh sine omega t. And you remember that w is not a w, it's an omega symbol. And remember, that's not the uppercase omega symbol, which is the ohm symbol. Uh this is

**Dave Jones:** omega is actually the Greek lowercase symbol for omega. And what omega is is simply 2 * pi * f, which is uh the frequency you're talking about, and then multiply by time. So, uh v = v max sine

**Dave Jones:** omega t. What does this mean? Well, you might notice that this v is smaller than this v here. And sometimes you write it as like an italicized uh v. This means the instantaneous voltage over here. And also, you will

**Dave Jones:** have an instantaneous current. That's why we've got like a little v here and a little i here, cuz they mean instantaneous values at one single point in time. So, I guess you could call that the instantaneous formula for the

**Dave Jones:** voltage source here. So, uh the Ohm's law simply applies. At any one instant in time, the current equals the instantaneous current equals the instantaneous voltage divided by the resistance. It's just basic Ohm's law. But, the great thing about resistors is

**Dave Jones:** that they don't affect your current relationship to your voltage. They're a linear component. They have no phase shift whatsoever. This is why we've drawn the current waveform exactly synchronized with the voltage, because when you put a resistor in an AC

**Dave Jones:** circuit, it doesn't change the phase of your waveform current at all. But, because it's a resistor, it does normal resistory things. And when you put a voltage across it, there'll be a current that flows through it. And you have a

**Dave Jones:** heat dissipated in the resistor. So, yeah, exactly the same as DC, except you're just dealing at every instant in time instead of just oh, it's a constant DC value. So, unless you need to, you can actually forget about all this

**Dave Jones:** instantaneous stuff, and you can just simply um apply Ohm's law, AC Ohm's law, the I the maximum current is equal to the maximum voltage divided by R. Simple. Or the I or if you're talking in terms of RMS, root mean squared, the RMS

**Dave Jones:** current is exactly the same as the RMS voltage divided by a resistor. It's basic Ohm's law stuff. So, I just spent 5 minutes explaining it's exactly the same as DC. What's the problem? Well, you have to get into your mind that when

**Dave Jones:** you're dealing with AC, you're dealing in terms of phases, and you're dealing in terms of instantaneous values. But, you remember how we learned about phases in a previous video? Well, phases apply here. It's an AC circuit, and the value

**Dave Jones:** is continuously changing. We're going to have a phase angle. It's just that in this case, the phasor representation is because the resistor is completely linear and doesn't impact the phase at all. It doesn't change the phase phase at all. Our phasor diagram is simply

**Dave Jones:** like this. It's the 0° here because we've got 0° phase angle. So, the current at at 0° phase angle is the same is voltage at 0° phase angle divided by the resistance here, and that's our phasor diagram cuz it's at 0°, not 90,

**Dave Jones:** not anywhere. It's simply at 0°. So, it's very simple and rather trivial, but you have to understand you're dealing with AC now, so set phases to stun. So, moving on to inductors, how does it work? Well, very similar to resistors.

**Dave Jones:** Almost the same, actually, with one subtle difference, which you might or have already guessed from watching previous videos in the series. So, our circuit is exactly the same. We've got our voltage generator here with the instantaneous value V max sin omega t

**Dave Jones:** here. We've got a current flowing, and we've got an inductor instead of a resistor. But, look at the waveforms. They're now out of phase. So, you remember from a previous video, I like to use the term civil. There are other

**Dave Jones:** ways to remember whether or not a current is lagging or leading in a capacitor and resistor circuit, but I like using civil cuz what this basically means C is a capacitor, L is inductor, V is the voltage. So with

**Dave Jones:** reference to the voltage, so the voltage is kind of used as like the reference point and I is the current. So for inductors, it's just handy to remember that the voltage leads the current or you can say that the

**Dave Jones:** current lags the voltage like this. And likewise for a capacitor, the current leads the voltage or the voltage lags the current. It's just a nice visual representation. I like that, but leave it in the comments down below if you've

**Dave Jones:** got a different way to remember that or you just simply remember that in a capacitor, oh yeah, current leads the voltage in an inductor, oh yeah, voltage leads the current. So you can see that visually here at zero time point here,

**Dave Jones:** you can see that the voltage is effectively leading the current cuz the voltage is already high when the current is low like this. So just like up here, the voltage leads the current like that. So they're 90° phase shifted. And for a

**Dave Jones:** purely inductive circuit, this current is going to lag the voltage by precisely 90°. So now we have a voltage current relationship so to speak so a or a volt-amps relationship, it's often called. And this is how it's expressed

**Dave Jones:** inside an inductor. And here's where we need to do that pesky calculus stuff again, which is not hard. Done in a previous video. Calculus is really easy. This dI dT term here is a derivative. And derivative just means basically a

**Dave Jones:** rate of change. In this particular case, amps per second. So the instantaneous voltage in time V is equal to the inductance in henries, of course, multiplied by the rate of change of the current over time in amps per second.

**Dave Jones:** So, it's just a rate of change. It's basically saying how many amps does this current, if this is current, how much what is the rate of change? I mean, what is the slope of that value? I know we're

**Dave Jones:** dealing with the linear slope and this is a sinusoidal, but you know, a a rate of change can apply to any shape waveform. So, the steeper that waveform, if it went like that, that would be a higher rate of change. be a greater

**Dave Jones:** derivative there. But anyway, that is the volt-amp relationship for an inductor. So, simply the voltage on the inductor is related to the inductance of the coil multiplied by the rate of change of the current. So, that is the

**Dave Jones:** relationship there. That's really got nothing to do with Ohm's law over here. Now, there is actually a volt-amp relationship in resistors as well, but it's instantaneous and linear. So, it that's why you don't really discuss it at all because it just resistors don't

**Dave Jones:** impact your AC circuit, but inductors and capacitors, they do. That's why you need to know this relationship. So, from our instantaneous value for our voltage over here, you can derive, I won't go through it, but you can derive that the

**Dave Jones:** instantaneous current is equal to Vmax divided by omega L here multiplied by the sine omega t minus 90° cuz we have that minus 90° relationship. And that leads to Ohm's law for inductors over here. Imax on omega L and I

**Dave Jones:** likewise just multiply by 0.707, Irms equals Vrms over omega L. You'll notice that it's exactly the same as resistors, current equals voltage divided by resistance, current equals voltage divided by inductance, but you need to add that omega 2 pi f relationship in

**Dave Jones:** here. Otherwise, it's not going to work. And yes, we have to talk phases again. So, I equals I max sine omega t minus 90. I won't derive get into that. But from there, we can take the voltage we

**Dave Jones:** can give that the reference value of zero cuz there's got to be a reference point somewhere. And in that in in that particular case, which is zero degrees, so our polar diagram is going to be there's our phaser for V with zero angle

**Dave Jones:** cuz there's zero angle like that. And our current is going to be minus 90 degrees like that because the current lags the voltage. You remember? The current lags the voltage over here for an inductor. So, that's all pretty

**Dave Jones:** simple for a pure inductive circuit. Just remember that we now have to include the omega term, which we didn't have to do for resistors. And now we get on to one of the most important concepts of AC when it applies to inductors.

**Dave Jones:** An inductor will have an AC resistance called an inductive reactance. So, it's measured in ohms just like it was for a resistor, but a resistor is a purely purely resistive element. It has no complex relationship with the voltage

**Dave Jones:** and current. But inductors and capacitors do. So, XL is what we use to represent this AC resistance or inductive reactance here. And XL or the magnitude of XL, that's what those two lines mean. It means you strip out the

**Dave Jones:** sign part of it. It's neither positive nor negative. It's just the pure magnitude is equal to omega L in ohms. And because omega will have a specific frequency, it's 2 pi f. So, at say 1 kilohertz for example, an inductor

**Dave Jones:** with a given Henry's will have a an AC resistance in ohms or an inductive reactance of 2 pi f times the inductance in Henry's. So, once again, just like regular Ohm's law, voltage on current equals the resistance or in this case

**Dave Jones:** the inductive reactance which is omega L in polar form or phasor form phasor notation 90 degrees because of that relationship down here. But generally speaking we don't tend to use the phasor notation like this. It's more common to

**Dave Jones:** refer it to you remember the complex numbers video I'll link that in if you haven't seen it you shouldn't be watching this before you watch that and of course we can convert polar to rectangular form which is J omega L. So

**Dave Jones:** the AC resistance or inductive reactance formula you usually remember for inductors is XL. Notice that it's not the magnitude anymore because it includes it can include a negative component is J omega L. So that is the inductive reactance which is just

**Dave Jones:** measured in ohms just like a resistance which is why you know you can actually treat an inductor in a circuit like a resistor if you don't if you're not worried about the phase relationship. It does actually have an AC resistance. And

**Dave Jones:** just like regular Ohm's law voltage on current equals resistance or in this case the AC resistance XL. Easy. So if you're not worried about the phase component that I eat the complex component which is J here XL can be just

**Dave Jones:** omega L or 2 pi f L and that's how it's often represented cuz it's easy to understand a lot of people still don't quite get the omega thing. It's just 2 pi it's just short hand way of writing 2

**Dave Jones:** pi f. So 2 times pi times a frequency times the inductance in henries. So just like a resistor the higher the resistance the greater the the impedance to the current in the circuit. Same thing with the inductor here. The higher the frequency therefore

**Dave Jones:** a given inductor so as your frequency goes up your AC your AC resistance or inductive reactance goes up and impedes the flow of current in the circuit. Simple. And capacitance, exactly the same as inductance, except everything's sort of turned on its head. Once again,

**Dave Jones:** we can go back to our civil acronym visual acronym here, and in for a capacitance, the inductance leads the voltage, or the voltage lags. Then so that's what we get on our waveform down here. If the voltage is we start as as a

**Dave Jones:** reference like this, you can see that the current is already leading that current is leading the voltage there in terms of phase. Circuit's still the same. The instantaneous formula is still exactly the same as what we had before,

**Dave Jones:** except we've got a capacitor, pure capacitance, as we talked about pure inductance. We're just talking about a pure capacitance in series. And I've covered capacitance in other videos, but of course, when you initially put and try to put a current through a capacitor,

**Dave Jones:** the current will flow because it's a basically a short circuit when you first switch it on. The current will flow and only then will the voltage sort of lag behind that. And that's what you see here. As soon as you turn it on at time

**Dave Jones:** zero, the current goes to absolute maximum here, but the voltage is zero and it hasn't had time to rise up yet. That's why it's lagging. Because you need time to build the voltage up on the plates as the current flows through the

**Dave Jones:** capacitor. I've done a whole video on that through. And you remember how I said everything's turned on its head compared to the inductance? Well, that includes our rate of change here. Our rate of change, remember it was voltage

**Dave Jones:** equals inductance times the rate of change of current with time, but now it's current equals the capacitance times the rate of change of voltage, not the current. Everything's flipped on its head. And of course, that rate of change is no longer

**Dave Jones:** amps per second, it's volts per second. And you'll notice our equation for the instantaneous current has also changed. It used to be Vmax on omega L. Well, now it's there's no division there, it's multiplication omega C times V max sine

**Dave Jones:** of omega T and it was minus 90 degrees before, but because we've shifted in the opposite direction, it's now positive 90 degrees. And likewise, that leads to a flip in our equation here. Our I max before was V max on omega L. Well, now

**Dave Jones:** it's omega C times V max and likewise, the RMS current is omega C volts RMS. And just like inductive reactance, we have capacitive reactance once again in ohms. Once again, it's an AC resistance and our magnitude of XC is now 1 over

**Dave Jones:** omega C in ohms. And from that, it follows that the voltage on the current here, which of course, voltage on current is is ohms exactly there. It's 1 on omega C with an angle of 90 degrees here. And it's a positive 90 degrees

**Dave Jones:** just like we had up here, but if we take that angular component out from under there, it then becomes from positive to negative 90 degrees over there. And then we get our final equation for our capacitive reactance XC. It's called is

**Dave Jones:** 1 on J omega C. So, we have to So, we've converted from polar to rectangular form again. And if you take the complex J part out like that, it becomes minus J 1 on omega C. And that is your capacitive

**Dave Jones:** reactance formula. Whereas, the capacitive inductance we saw was J omega L. And of course, voltage divided by current equals your AC resistance or your capacitive reactance. Easy. It's just sort of flipped on its head compared to inductors. And yes, we can

**Dave Jones:** have a phasor diagram for that instead of the inductance going negative 90 degrees like this, our pure capacitive circuit goes positive 90 degrees like that because the current leads the voltage over here. So, that is basic AC circuit theory for resistors, inductors,

**Dave Jones:** and capacitors. It's not too hard at all. Remember, you get a capacitive reactance and then inductive reactance. That's different to impedance. I'll have to do that in another video. So, I hope you found that video useful. If you did,

**Dave Jones:** please give it a big thumbs up. And as always, you can discuss down below in the comments or over on the EVblog forum. And check out my new merch store over on Teepublic. I've got new design t-shirts, hats, stickers, all sorts of

**Dave Jones:** stuff down in the merch store. Check it out. Catch you next time.
