---
video_id: 4n7iE7pw_WQ
title: EEVblog #1172 - TRIAC Testing (WEP Meltdown Part 2)
url: https://www.youtube.com/watch?v=4n7iE7pw_WQ
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 27, "3": 54, "4": 63, "5": 86, "6": 108, "7": 118, "8": 140, "9": 149, "10": 162, "11": 174, "12": 188, "13": 197, "14": 217, "15": 245, "16": 265, "17": 276, "18": 284, "19": 295, "20": 313, "21": 338, "22": 349, "23": 357, "24": 370, "25": 389, "26": 403, "27": 419, "28": 430, "29": 449, "30": 458, "31": 480, "32": 494, "33": 518, "34": 543, "35": 554, "36": 568, "37": 586, "38": 611, "39": 621, "40": 633, "41": 643, "42": 658, "43": 671, "44": 690, "45": 704, "46": 718, "47": 741, "48": 750, "49": 763, "50": 774, "51": 790, "52": 820, "53": 836, "54": 853, "55": 861, "56": 874, "57": 888, "58": 900, "59": 915, "60": 926, "61": 941, "62": 953, "63": 970}
---

**Dave Jones:** Hi, just a quick follow-up video to this web/yihua 898D plus soldering station that melted down. This SMD rework station I'll link to the previous video if you haven't seen it.

**Dave Jones:** And we sort of came to the conclusion that it was probably this fan failed cuz it has actually failed. We can measure that and then maybe something happened to the control loop or or something.

**Dave Jones:** It couldn't detect the temperature increase in this and didn't shut off the heat on. Now, one theory is that okay, the fan blew so there was no air blowing over this element anymore and here's a little thermistor in here that measures the temperature and this is a ceramic insulator for the heating element here and because there was no fan air blowing over it anymore, then the thermistor was

**Dave Jones:** detecting the wrong temperature and it kept pumping in the power but it's kind of near enough to still get radiant heat there. It's all covered in metal and everything else.

**Dave Jones:** So, I don't think that was a real issue. But anyway, a lot of people in the comments for the previous video said, "Aha, it is the SCR sorry, the triac in this thing which is here and it's a BTA16 / 600V triac and pretty decent one from ST designed for you know, medium power applications.

**Dave Jones:** Here's the data sheet and it looks like to be a genuine one not some knock-off or anything and a lot of people said, "The triac failed short." And sure enough, if the triac actually failed short, then there's nothing that the processor on this thing could actually do via the gate control optocoupler here.

**Dave Jones:** It couldn't switch it off. Which could certainly be a fire mode and a lot of people have said that oh, they've seen other Yihua/Web stations fail because of the triac.

**Dave Jones:** But, I actually measured the anodes on the triac here, and it's not shorted. So, we'll actually test this in a minute. And, it was kind of like too much of a coincidence to me that the fan also failed cuz I I can't think of a mechanism that if the triac failed short, yeah, the heating element will go up, but how does that really kill the fan?

**Dave Jones:** Okay, it could have melted it down, it could have melted the coil inside something like that, or a broken connection, something like that. But, the fan is like I can't see that happening.

**Dave Jones:** And, likewise, I it's kind of hard to see how a fan failure would cause a failure in the triac, like a short in the triac, I guess. Maybe it's possible in some weird scenario, but anyway.

**Dave Jones:** So, I've measured the triac, and it hasn't failed short. In fact, it seems to work just fine, and that's what we're going to have a look at today. We're actually going to test this, and spoiler alert, look, it's working.

**Dave Jones:** So, it's not actually the triac, and I've physically removed the snubber network down here. I've removed the optocoupler drive and everything. So, I'm just basically connecting up to the leads of the triac in here.

**Dave Jones:** And, this is basically what we've the setup that we've got in DaveCAD, which you can download, by the way, on GitHub. I might have to link that in down below.

**Dave Jones:** You can get the official DaveCAD. Anyway, got an AC mains transformer that I'll show you. It's like a nominal 6 and 1/2 volts or whatever. We've got a 50 ohm load here going into our triac, the two anode pins of our triac, and the gate's going off to a pot here that we can control the turn on turn off time for each AC cycle.

**Dave Jones:** And, if you're wondering what a triac is, this requires a whole different video cuz you can really go down the rabbit hole on these things. But, a triac is basically two SCRs back-to-back, and an SCR is a silicon controlled rectifier, also known as a thyristor, but once again, you can if you want to go down the rabbit hole and thyristor and SCR technically aren't the same thing, but you know, for most

**Dave Jones:** purposes you can say an SCR is a thyristor and vice versa and you can say that a triac is a bidirectional thyristor as well. So, you'll see a lot of these terms interchange, you know, they'll people will say thyristor in when they mean SCR or vice versa or they might say a bidirectional thyristor when they really mean, you know, when it's actually a triac and all that sort of

**Dave Jones:** stuff. The terms for these things are actually rather confusing, but basically two SCRs back to back like this and an SCR is basically a diode like this with a gate.

**Dave Jones:** So, we'll just look at one SCR like this and I'll just go over very crudely how it works. It's basically as the name suggests, it's a silicon controlled rectifier.

**Dave Jones:** So, it's basically a diode like this that allows current to pass through, but only when you get enough gate current in here and these aren't voltage operational devices, they're actually current.

**Dave Jones:** So, you need a minimum gate current to flow in here and then it latches on. It works like a latch and once you provide that gate current, you you can actually have a switch in here like going up to the positive thing and you can provide that gate current through there and this SCR will actually latch on.

**Dave Jones:** So, you can just a momentary button switch, you can press there and it'll latch on this SCR and the SCR won't turn off until such time as the holding current through here depends on the load and everything else, but when it'll keep maintaining that latch position until a minimum holding current where it'll actually just unlatch and then you can restart it again.

**Dave Jones:** So, quickly in a bit more detail how an SCR works and hence how a triac works cuz the triac's just two SCRs back to back works on AC. We've got the equivalent circuit in this case for a a triac.

**Dave Jones:** It's working in one what's called one quadrant of the triac, but just think of this is the equivalent circuit for the SCR. I just got this from Wikipedia here.

**Dave Jones:** And basically, two regular bipolar transistor regular bipolar transistors PNP and NPN. And hopefully you can see that so the base current just flows through here like a normal NPN transistor like that.

**Dave Jones:** And once you provide enough gate current, of course, then current starts to flow through the NPN transistor. Basic you know transistor operation. And then, of course, because you got the PNP up here, it can conduct through its base like that.

**Dave Jones:** And you know, it's a bit confusing that we've got bases here when we're talking about NPN transistors and gates when we're talking about thyristors. Not to be confused with gates on MOSFETs, which are voltage you know, driven devices.

**Dave Jones:** This is still current driven. So it ends up flowing through like that, but once it does that, of course, it switches on this PNP transistor so that some current can now flow through here into the base to keep this thing switched on.

**Dave Jones:** So it latches on with this PNP transistor like this. So you only need to provide a little short burst of gate current in here to latch this this two transistor circuit on.

**Dave Jones:** And that's what an SCR does. It actually latches on. And I've sure I've done a video way, way back on SCR latch-up, which is a phenomenon in semiconductor structures inside ICs, like a regular logic ICs, where they will act as an SCR and they'll latch up.

**Dave Jones:** A similar sort of, you know, a thing happens with the output structure of transistors in logic circuits. I'll link that in at the end, up here somewhere. Check it out.

**Dave Jones:** Anyway, that's how an SCR works and latches on. And you can see that in this case, if when the polarity reverses in an AC configuration, the current can't flow through here anymore, so one SCR inside the dual back-to-back TRIAC, um it switches off and then the other one can start to conduct in the opposite direction.

**Dave Jones:** Hopefully that makes sense. So, they're very cool devices, SCRs and TRIACs, and as I said, a very big deep rabbit hole if you want to go into the dynamic uh operation of these sorts of things, and it really gets a bit complicated.

**Dave Jones:** And the thing about a TRIAC is when you have two of these back-to-back in reverse orientation like this, you can use them for AC stuff, and that's why heaters like this, so just imagine this is the heater here, connected up to your 240-V mains here, a TRIAC, you can actually control the on and off cycles of that, and every time that the AC waveform swaps polarity like

**Dave Jones:** that, you can actually it you get the minimum hold off, it drops below the minimum hold off current, and it switches on and off. So, you can actually uh by adjusting the current going in through to the gate pin here on both cycles, that's why on a TRIAC with AC, you have it connected across the AC source like this, you can actually vary the on and off duty cycle, and you can

**Dave Jones:** control your load. So, this is useful for all sorts of, you know, dimming applications for lamps, for motor control, and heating elements, you can vary the amount of power that goes to it.

**Dave Jones:** So, let's have a look at the uh setup we've got here very quickly. I won't go through all the details, but I've got a uh little AC transformer here that I built when I was oh god, I don't know, I was 10 or something when I built that.

**Dave Jones:** It's It's actually very, very old, and it's just got a mains transformer in there, and I can select the different taps. I will just use the minimum 6.3 V AC and I'm using two to decade resistance boxes here just to simulate the upper half and the lower half to that cuz I just didn't bother with a pot.

**Dave Jones:** So, we'll use those two and I've got the scope. The ground is actually up here cuz it's floating. I can do that. Beware, I've done a whole video on how not to blow up your oscilloscope and channel one, which we'll see which is the yellow waveform, is measuring the voltage across the load resistor here, which is essentially the current flowing through the triac like this and the

**Dave Jones:** channel two, which is green waveform, is just the AC input signal, which we're triggering off. So, as you can see, ta-da! So, as you can see, it works a treat.

**Dave Jones:** So, this is the input AC signal that we're actually triggering off and this is the current through the triac and you can see that our duty cycle is like, you know, it's it's somewhere in the middle.

**Dave Jones:** And if I adjust these resistors here, we can see that duty cycle actually change like that. So, we can actually control the turn on and turn off time of this triac.

**Dave Jones:** So, it seems to work and you can actually just see a little current pulse in there when it actually switches. There you go. Look at that. Neat. But anyway, there there doesn't seem to be anything wrong with this triac.

**Dave Jones:** Yes, it could certainly fail at like high voltage. There could be some, you know, high voltage related issue that we don't know about, but it definitely hasn't failed short and it does actually work as a triac.

**Dave Jones:** So, in this particular case, yeah, that's not the failure mode. So, I my money's still kind of on that the fan failed and then something to do with the algorithm inside this thing or the measurement or whatever, it just it couldn't cope or whatever, I don't know, and it's melted down.

**Dave Jones:** But a lot of people have actually reported um uh similar units from uh Yihua or whatnot actually melting down as well. Um just yeah, completely going like white-hot, just like uh this one uh David's one here, and just melting down.

**Dave Jones:** So, they just tossed it in the bin. So, whoop, what fell? Something fell. Something in the lab fell down. Oops. Any happens. Anyway, so there you go. Um we've got some sort of failure mode there.

**Dave Jones:** The triac is okay at basic testing. By the way, I did actually try to measure the triac with my little um M tester here, which does actually measure triacs, but it couldn't do it because this only I believe this only gives out like a couple of milliamps gate current effect and couple of milliamps test current.

**Dave Jones:** So, that's not enough current to actually turn on this particular uh triac here. This one I think needs uh 10 or 50 milliamps depending on what particular uh part it is or whatnot.

**Dave Jones:** So, yeah, this um as cool as these little um and this is capable of testing triacs, by the way. Um you can like it has a I don't have another one here, but it can show it can show up with like the triac symbol and everything else.

**Dave Jones:** So, it can do it, but it can't do it unfortunately if you've got a triac that needs more than the base current um base current gate current. It's not an NPN rubbish.

**Dave Jones:** This is a triac gate current uh required. So, yeah, in this case just doesn't have the juice required. And for those who want to see the little uh blower fan here, I've just taken the uh uh top cover off here, and it 24 volts, it uh certainly doesn't work.

**Dave Jones:** It's cactus. There we go. Bonus teardown. If you haven't seen it, it's got the uh four coils with the permanent magnets around there, and then inside there just got the ring of permanent magnets so that they can control the magnetic field and make that the well and alternate the magnetic field in a circular fashion and make the motor spin.

**Dave Jones:** And there it is. I had to pry that out of the back of the case and it is ridiculously simplistic. Look at this. There's There's nothing in there except Oh, there's one cap.

**Dave Jones:** There is it a cap? Looks like there's one cap there and what else? We just got our driver IC up there. Can we get a number on that? It's going to be some weird thing you probably can't get a data sheet on, I'm sure.

**Dave Jones:** There you go. Ha, what do you know? You can get a data sheet for this thing. This is actually pretty cool. Um, BCD, but I got it from Diodes Inc.

**Dave Jones:** So, I guess they were bought by Diodes Inc. And it's an on-chip hall sensor as well, which of course, you know, to know the position of the thing. It's really cool.

**Dave Jones:** I like it. It's for dual coil brushless DC motor, brushless DC fan, revolution counting, speed measurement, all that sort of stuff. So, it's got an onboard driver. That's it.

**Dave Jones:** Fairly crude but cool device in that it has a and there's the magnet, you know, you've got to mount it in the right orientation, of course, trap for young players if you're using the hall effects sensor in it.

**Dave Jones:** And there's the magnetic flux density curves for all you uh magnetic aficionados. And that's all there is. Like two coils. So, they must have opposite side coils as two coils.

**Dave Jones:** So, that's how they're configuring this. Neat. And of course, for this low-cost fan, And went, "Ah, we don't need this diode rubbish. We don't need these in this RC these RC filters down here on that.

**Dave Jones:** Nah, don't worry about that. She'll be right. Just hook it up to the coil. Bob's your uncle." So, that's just crazy simplistic. I ones I've seen before are much more complicated than that in terms of all the drive.

**Dave Jones:** But, I guess okay, just do it in one chip. It's, you know, ultra low cost. But, anyway, that puppy has failed and whether or not it's the that was the cause of the issue or whether or not I don't know if something else went wrong on the board and killed it.

**Dave Jones:** I I don't know. I think it's just likely to have like just failed somehow just mechanically or electrically failed. Anyway, I hope you found that video useful and please let us know in the comments what you think about, you know, how this thing failed or whatever.

**Dave Jones:** Hope you liked it. If you did, give it a big thumbs up. As always, discuss down below in the EV comments, YouTube comments, or EV blog forum. Catch you next time.
