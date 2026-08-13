---
video_id: myqytW9ecww
title: EEVblog #329 - Tracking Pre-Regulator LTspice Simulation Part 2
url: https://www.youtube.com/watch?v=myqytW9ecww
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 19, "2": 42, "3": 62, "4": 76, "5": 92, "6": 113, "7": 128, "8": 160, "9": 181, "10": 200, "11": 217, "12": 241, "13": 252, "14": 280, "15": 298, "16": 321, "17": 355, "18": 374, "19": 400, "20": 418, "21": 441, "22": 460, "23": 478, "24": 501, "25": 520, "26": 540, "27": 563, "28": 587, "29": 612, "30": 630, "31": 654, "32": 680, "33": 703, "34": 721, "35": 737, "36": 756, "37": 780, "38": 801, "39": 824, "40": 841, "41": 861, "42": 882, "43": 904, "44": 923}
---

**Dave Jones:** Hi, it's simulation time again. If you remember a previous video I did on a switching tracking pre-regulator for a linear voltage regulator. In this case it was a switching boost converter, can be any standard type of switching boost converter, followed by any type of linear

**Dave Jones:** regulator. In this case it was an LT3080 we were looking at, and we based that circuit on a P-channel MOSFET, which is M1 here, and that came from a recommendation in the LT3080 data sheet, and it had a few little issues with it, but as it turns out John Barnes has sent me

**Dave Jones:** an alternative circuit to that, so I thought we'd take a look at it. But if you haven't seen the previous video, click here and you'll be able to watch that first as a background. And in the previous video, with this P-channel MOSFET here, we had a few issues of choosing the correct type

**Dave Jones:** of MOSFET and some dropout issues, and we had to, if you wanted to increase the voltage, you have to put a diode in series with it or an LED or something like that to boost the voltage up, and it did work, but it wasn't the best circuit.

**Dave Jones:** So John has suggested a just as simple a circuit, but it uses a P-channel transistor here, and I thought we'd check it out and see how it compares. And if we take a look at it, it's pretty much identical almost to the MOSFET circuit.

**Dave Jones:** We've got our voltage input over here, which might be a battery. I've set it to 2.7 volts, which might be the low end of a single-cell lithium-ion battery, for example, and we're using an LT1935 boost converter here, but really it's just a standard boost converter.

**Dave Jones:** It can be practically any type which operates identically. There's, you know, hundreds of them, so there's nothing unusual there. It doesn't have to be a linear technology type. It can be any kind, and we're using that as the tracking pre-regulator for the LT3080 again.

**Dave Jones:** Once again, nothing special with the LT3080. It can be any linear regulator, a 7805, whatever, and we want this tracking pre-regulator voltage up here to be, in this case, around about 2 volts higher, always 2 volts higher than the output. And if we have a look at the circuit, as it turns out, R4 will be the resistor which controls,

**Dave Jones:** basically controls, the offset voltage here, and it should be fairly independent of the base current, and really we should have no issues at all with the particular type of transistor used, and our temperature coefficient for this circuit will basically be dependent only upon

**Dave Jones:** the temperature coefficient of the base emitter junction here. So let's try it and see what we get, and you can see that John's original circuit uses C1 here. That's obviously included for some sort of stability issue. I'm not convinced that we entirely need that, so we'll try it with and

**Dave Jones:** without that, but we can adjust a few parameters here, and we're going to use the parameter sweeping feature which I've done a video on before, so if you haven't seen that, click here and you'll be able to watch that video first, so you'll know exactly how we're doing this, and of course we're

**Dave Jones:** using LT SPICE again. It's a free circuit simulation tool, and it's probably one of the industry standard simulation tools now. It works really well, I highly recommend it. So let's run this thing and see what we get. So what I've got here is I've got V2, this voltage source here, which sets

**Dave Jones:** the output voltage, and I won't go into details of how it does that, you've got to watch previous videos, but I set it to 1 volt here, which means we'll get 1 volt on the output, so we're looking for 3 volts on our tracking pre-regulator input here.

**Dave Jones:** So let's run it, let's go into simulation, edit our simulation command, we're doing transient analysis, our stop time is 15 milliseconds, so let's just run that, pretty basic stuff, and you can see that there's some startup stuff there, around about 0.3 milliseconds or thereabouts, to start up the regulator, but that looks like

**Dave Jones:** it's working a treat. That's at about 2.9 volts or thereabouts, so let's have a look here, there's our output voltage, of course it's not stable at the start there, but once it gets there, it does stabilize out, and there you go, we're getting basically 1 volt out, and if we compare

**Dave Jones:** those side by side, it's pretty close to 2 volts offset like that. So that's working a treat, no problems at all. So I've changed R4 to 20k here, and let's run that now and give it a look, there it is, we're talking, what are we talking here, we're talking 4 volts or thereabouts,

**Dave Jones:** so that's 3 volts above our 1 volt output voltage there, so changing that R4 value from 10k to 20k, doubling that value has increased our voltage from 2 volts to 3 volts. Now if you're wondering why this simulation takes more time on the 20k one as it did on the 10k one, and we get this transient

**Dave Jones:** stuff on the input, it's because the DC to DC converter is now working, because we've only got a 3.3 volt input voltage here, let's stop that, so I've only got 3.3 volt input voltage, and before we're getting a 3 volt tracking pre-regulator, which means this is no longer operating as a boost

**Dave Jones:** converter, so when this voltage goes down, when our output set voltage is only 1 volt, and our configuration here is giving a 2 volts above that tracking pre-regulator, that's below the 3.3 volt input voltage, so if we up this, so if we increase this value again to say 5 volts,

**Dave Jones:** then you'll see that it will instant, so our input voltage is now 5 volts, and our tracking pre-regulator should be 4 volts, so it's below the V in input voltage, and let's run that again, and we should find that there's none of that transient stuff at the start, bang, and the

**Dave Jones:** simulation is instant, that is because that that DC to DC converter is no longer operating as a boost, and it's got less to analyze, it's going straight through, and bingo, we get our 4 volts offset voltage, or thereabouts, so what I've done now is I've gone and changed the output voltage to

**Dave Jones:** 5 volts, the input voltage is 3.3 volts, so we're always going to get this thing to work in that boost operation, our tracking pre-regulator should be 7 volts, because we've got our 10k value there, and we run it, and you can see that our output voltage in the green there is 2 volts above our

**Dave Jones:** output voltage of 5 volts, so it's tracking just fine, and you can see it stabilizes in you know 0.15 milliseconds, or thereabouts, so we don't need to run all that simulation time, because that actually, that'll take some time, so we can knock that down to, you know, let's say knock it down to

**Dave Jones:** 0.5 milliseconds, or thereabouts, so we can now run that again, and bingo, it just doesn't take us long, so now we can do some parameter sweeps of, let's try our base resistor R1 here, and see what effect that has on our tracking pre-regulator voltage, but before we do that,

**Dave Jones:** let's just have a look at C1 here, and this is the waveform, okay, 5 volts out, 7 volts tracking pre-reg, and we've got these wiggles here, that's with C1 in the circuit, let's get rid of C1, so let's go down here, delete C1, and let's run that again, and see what we get, much cleaner,

**Dave Jones:** start up there without C1, so I'm going to leave C1 out, and let's parameter sweep R1, and to do that is real easy, we go in here, instead of 22k, put in the curly brackets, which indicates to the simulator that it's a parameter, we'll call it RP, it's just a label,

**Dave Jones:** and then we can go up to our SPICE directive up here, we can add a SPICE directive, dot step command, parameter, and then the label we gave it, which was RP, and then the value we want to sweep over, well let's go from, say, oh I don't know, let's go 1000 ohms up to 20k

**Dave Jones:** in 1000 ohm steps, so that'll give us 20 waveforms, so we'll sweep through, let's put our parameter, our SPICE directive on the circuit there, and run it, so it'll sweep through, this R1 value will go from 1k to 20k in 1k increments, so we should get 20 different waveforms, let's run it,

**Dave Jones:** and there we go, and it's stopping, and bang, that's 1k, so that green one was 1k, this blue one will be 2k, red one will be 3k, looks like it's making absolutely no difference at all. Now let's do a parameter sweep on our output voltage, so Vout here, I've put, I've called it

**Dave Jones:** Vout, actually, and we're parameter sweeping, there it is, our dot step command, Vout from 1 volt to 10 volt in 1 volt increments, should be interesting, let's run this and see what we get, let's have a look at our output voltage, bang, so there's our green line 1 volt,

**Dave Jones:** blue line's 2 volts, red's 3, 4, 5, bang, look at that, and you'll see it takes longer to stabilize at the start, of course, the higher voltage you go, but it's drawing a very interesting parametric graph there for Vout, I like it, and if we have a look at our tracking pre-regulator

**Dave Jones:** voltage, that is tracking, you'll notice it's tracking 2 volts above each time, very nice, and we can just get that on its own, of course, and there it is, so we've got 3 volts, and then there'll be 4 volts, 5 volts, 6, 7, 8, 9, 10, 11, and 12 volts, it's working a treat,

**Dave Jones:** what I'm doing now is I've changed the transistor from a 32N3906 to a BC327, and once again, it's working just fine, not a problem, not a problem at all, so by now you're probably thinking this circuit is rather interesting, and exactly how does it work, because this base

**Dave Jones:** resistor here has no, effectively no effect, and doesn't set this pre-regulator voltage, and we can show that if we set it to, you know, 0.01 ohms, for example, and then run this thing, there's our output voltage, and there's our tracking pre-regulator voltage, 7 volts, 5 volts,

**Dave Jones:** it doesn't matter what that base resistor value is, it can be anywhere from a dead short, up to, you know, hundreds of K, and it's going to work just fine, so there's nothing, that base current is not setting the voltage, what is? Well, if you look down at the feedback pin

**Dave Jones:** down here, if we look at the voltage across R2, down here, let's go in, it is 1.25 volts, there it is, and that's no coincidence, because that is the bandgap voltage reference inside the DC to DC converter, and they're all the same, they're all going to be around that value,

**Dave Jones:** because that's the physical construction, the bandgap voltage reference in there, so that's effectively a constant current source through R2 there, R2, and because we've got a constant voltage across that, 1.25 volts, across 10 K, that sets a constant current, and we can actually look at that, if we run it, let's look at the current through R2,

**Dave Jones:** here we go, there it is, it's 125 microamps, no surprise, 1.25 volts on 10 K is 125 microamps, and you'll notice that if you look at R4, the current through R4 is exactly the same, there's the two of them laid on top of each other, because the base current does not contribute at all,

**Dave Jones:** so the current, so the pre-regulator voltage is equal to the constant current set through R2, which gives a constant voltage drop across R4 here, so let's shut that down, expand it, so the voltage pre-regulator voltage here is equal to the constant current through R4,

**Dave Jones:** and the voltage drop across that, plus the voltage drop of the base emitter junction here, and that's it, that's what sets the value of the pre-regulator voltage, so it depends on the constant current set up here, current through there, the voltage drop in the base emitter,

**Dave Jones:** so this circuit is going to be pretty darn good, and the only issue there's going to be with it is the temperature dependence of the base emitter junction here, so we can actually try that, I've set it back to a 2N3906 transistor, I've added the SPICE directive dot step temp,

**Dave Jones:** so we're going to step the circuit temperature from 0 to 50 degrees Celsius in 5 degrees C increments, so our base resistor is set back to 10k, not that it matters, and let's run that, and have a look at our tracking pre-regulator voltage with temperature, and here you go,

**Dave Jones:** it's, you know, there's not much in that at all, that's for 5 degree Celsius jumps there, I mean we're talking, you know, we're talking nothing really, there's very, very little in there, so really we're only talking about, you know, 100 millivolts or so there over that sort

**Dave Jones:** of temperature range of 50 degrees C, and that's not surprising because the typical base emitter junction temp code is going to be about 2 millivolts per degree C, so there you go, I quite like that circuit, so thank you very much John, I think I'm going to use that one, it's

**Dave Jones:** better than the MOSFET circuit recommended in the LT3080 data sheet, seems to work a treat, and if you want to discuss this, jump on over to the EEVblog forum, and if you like this type of video, please give it a big thumbs up, catch you next time!
