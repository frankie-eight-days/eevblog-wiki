---
video_id: lBycH31K-E8
title: Veritasium Electricity Video - Simulation Notes
url: https://www.youtube.com/watch?v=lBycH31K-E8
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 20, "2": 32, "3": 52, "4": 64, "5": 80, "6": 96, "7": 112, "8": 132, "9": 149, "10": 165, "11": 181, "12": 197, "13": 217, "14": 229, "15": 249, "16": 265, "17": 286, "18": 302, "19": 318, "20": 334, "21": 350, "22": 366, "23": 378, "24": 395, "25": 415, "26": 435, "27": 451, "28": 467, "29": 487, "30": 503, "31": 524, "32": 536, "33": 552}
---

**Dave Jones:** Hi. Just a quick follow-up video to my Veritasium video, which seems very popular, linked in on the main channel if you haven't seen. This is just going to be a quick video, just basically mentioning simulation of this thing. Now, of course, Derek, you know, proposed the question of

**Dave Jones:** the light year. Well, here it is. It's over here, okay? You've got the switch and the battery and the lamp, which is a resistive load, and then you've got this wire going all the way out for half a light second that way, half a light second that direction.

**Dave Jones:** And there's several ways that you can go about solving this problem where the answer is 1 meter on C seconds, that when you close this switch, 1 meter on C seconds, later, the lamp will light. Now, a lot of people have gone into the detail,

**Dave Jones:** oh, the lamp doesn't really light, it won't light in practice and stuff like that, and it'll only light a little bit and it's got to wait for the waves to travel back and steady state and all the rest of it, right? I've deliberately left that out of the video

**Dave Jones:** because that's not in spirit with the question. The spirit of the question was, assuming the lamp's ideal, it turns on instantly and it turns on at any current, then basically, at what point will it first turn on? It doesn't matter how brightly, it doesn't matter for how long,

**Dave Jones:** it doesn't matter, like, anything, right? It's just how quickly will it immediately turn on? And the answer is 1 meter on C seconds, because the distance between these wires here is 1 meter. And I think I forgot to mention in the video, too, that, yeah, it's not

**Dave Jones:** going to be instantaneous, it's going to be 1 meter on C seconds, because there's a meter here, right? So I chose this transmission line model, and the lumped element model here, just showing, like, the lumped elements of the simulation line, but the fact that it's a transmission line doesn't actually matter.

**Dave Jones:** I just wanted to note that it's the capacitance in here which is doing the magic. You can forget about the inductors and everything else. It's the cable capacitance in here that's the two wires are only a meter apart, and when you turn on that switch, it's a step function, and therefore

**Dave Jones:** the capacitors, no matter how small they are, will actually be effectively a short circuit. But it still takes time, it can only travel at the speed of light. The capacitors aren't magic, they won't instant, the charge won't instantly go, like, jump from the

**Dave Jones:** battery and the switch over to the lamp instantaneously because capacitors are magic and they go short circuit instantly like you see in the simulations. That's not how it works. It actually, it's physically a meter away. So it's going to take that, you know, it has to travel the meter at the speed of light

**Dave Jones:** assuming no dielectric or anything else, right? So this ideal lamp is going to light up no matter how briefly, just like 3.3 nanoseconds after you close the switch because that's the speed of light for a meter to complete the loop there through the capacitance of the cable.

**Dave Jones:** Now, a lot of people have tried to simulate this as like a transmission line, and I drew it as a transmission line because it effectively is. Let me explain that a bit better visually. So maybe this might make it a bit clearer. What I've overlaid here is

**Dave Jones:** like some old school 300 ohm twin flex cable here, and hopefully this is a bit of a better visual representation because that's effectively what you've got there going half light year out in either direction is basically a transmission line, but this is not a traditional transmission

**Dave Jones:** line simulation. Now, if we have a look over here, right? Like a model for a transmission line, for example, this is how I've done it like this, but you know, in most cases when people simulate transmission lines they'll do the generic model like down here.

**Dave Jones:** It'll just be like a common ground like this with the resistor and the inductor and the capacitor and a parallel resistance there which is the conductance of the cable, but we're not going to worry about that, okay? So you end up with a traditional simulation model

**Dave Jones:** like you get here, for example, but you can't actually simulate it like this. Why? Because in a traditional like LCR simulation, transmission line simulation like this, I'll run it in a second it's really interesting, you've got a source at one end and a load at the other end, right?

**Dave Jones:** But that's not what we've got here. That is not what we've got here at all. I'll just move these down here right, because I don't know how to make them transparent, and right, we don't have the source, it's not like we have the source here going into the transmission line and the load at the other end

**Dave Jones:** that's not what it is. We've effectively got like two transmission line stubs, right? We've got one stub here, it's shorted at the other end, okay? And we've got another stub here, which is shorted at the other end, and then the load is actually across the other end

**Dave Jones:** of that. So it's not your traditional single transmission line simulation. So if you're trying to do your single transmission line simulation I think you're probably doing it wrong, you might come out with an answer that's right, but basically you've got two stubs, either

**Dave Jones:** side. So hopefully that's pretty clear. Now let's have a look at your traditional LC simulation here. So what I've got is a source over here, which is a pulse, which is a step response, which is exactly what we're doing here by closing the switch, and

**Dave Jones:** let me set this to 10 ohms, which is the characteristic impedance of this cable. Cable, apparently, that we're simulating here. And let me run it. The cool thing about the Falstad simulation is that it shows like the electron flow and the reflections and everything else.

**Dave Jones:** Really cool, okay? So if I run it, watch this, you can see the green. You can see it propagating through, propagating through as it hits the load and then you can see maybe a little bit of red. That is the reflected signal. So over here, the green, this is the source,

**Dave Jones:** this is the pulse gen, and this is the resistor load here. And the pulse gen, the green signal there is the voltage, and the yellow one is the current. And you can see that everything's pretty hunky-dory, because the load matches we're getting really no reflections.

**Dave Jones:** Reflections aren't going off the load and then making it all the way back to the generator over here, okay? So it's good to go. But if we actually change the value of this resistor here, okay? Let's make it 1000, okay? And so it's really unmatched, okay?

**Dave Jones:** So it's almost open, right? And let's reset that. Let's run that again, okay? It goes through, it goes through, it goes through, it looks normal at the moment, but bam, it hits here. Look at the red reflection. Look, look, look, look, it's going way, it's going back, and boom!

**Dave Jones:** Boom! That's where the reflected wave hits. Back at the source over here. And then it just starts looking horrible. Right? Because you've got this horribly mismatched load at the end, right? So it doesn't match the transmission line. This is your basic transmission line simulation stuff.

**Dave Jones:** And you can see how it's that. And if we go in the other direction and we say like 0.1 ohms, okay? Let's stop that, reset, run again, okay? Nothing, everything's looking fine, everything's looking fine until it hits the end now, bam, and the red reflection starts coming back in

**Dave Jones:** about now. Whoop, it's gone up instead of down. It's the opposite polarity that we had before. Anyway, this is all basic transmission line stuff. So if you start trying to simulate like waves and, you know, propagating along the transmission line and stuff like that, just remember that it's not just one transmission line.

**Dave Jones:** You actually have like a stub thing here. And as I mentioned in the comments and on the EEVblog forum where there's much discussion as well, this is only one way to model this. You can actually model this in different ways. You know, like it's an antenna, for example.

**Dave Jones:** You can model that and you can go to the physics, the photons, and all the rest of it, right? And you can, but you'll come out with the same answer. Because like, it takes this is a meter gap. So regardless of which model you use to try and solve this, it's going to light up in one

**Dave Jones:** meter on C seconds. Because nothing can propagate faster than the speed of light here, right? And capacitors aren't magic, antennas aren't magic, nothing, wires aren't magic, nothing's magic. So yeah, that's your answer. But hopefully that gives you a better understanding how this is not just a simple transmission line simulation.

**Dave Jones:** Source and load. It doesn't quite work like that. It's a bit, it's a little bit mixed up. So yeah, I don't want to spend any more time trying to go in and simulate it, but I'm sure there are people who will do that

**Dave Jones:** and do like a really accurate simulation of this thing. But yeah, that's just something to remember. So I hope that gives you a bit of, a bit better visual representation there. I reckon it's two transmission line stubs like this, shorted out at the end,

**Dave Jones:** and going to the load between there. So there you go. I hope you found that interesting. Catch you next time.
