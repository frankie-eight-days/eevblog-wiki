---
video_id: ne_Prn0eGQE
title: EEVblog #376 - Multimeter Fuse Diode Followup
url: https://www.youtube.com/watch?v=ne_Prn0eGQE
source: youtube-asr
---

**Dave Jones:** Hi, this is just a quick follow-up video to the multimeter input protection video I did before and I'll link to it uh down below if you haven't seen that. It won't make any sense otherwise. Now, a lot of

**Dave Jones:** people asked and I think rightly so because it is a little bit confusing. These this diode protection here, we're using the Fluke 27 as the example. This is the schematic I used on the whiteboard in the previous video, but

**Dave Jones:** this is the actual schematic from the Fluke 27 service manual. And this diode bridge here and these four diodes here, which give a 3.6V nominal voltage drop um across the current shunt resistor. In this case up here, it's say 5 ohms up there for the

**Dave Jones:** milliamp one for example. and they was uh asking how do the manufacturer Fluke in this case ensure that these diodes won't blow before the fuse blows here. I mean the fuse is designed between these here's the milliamps and micro amps jack here J2

**Dave Jones:** and then the fuse is in series with WP4 and WP5 there even though you can't see it just assume that the fuse is in there like that. Now, how do we ensure that these diodes do not blow before this

**Dave Jones:** fuse blows? Because the fuse has a thermal mass. It takes time to heat up. It takes time to blow. How? And so during that time that it blows, how do we ensure that these dodes don't go poof? The whole idea of this circuit of

**Dave Jones:** course is that the fuse is supposed to blow first and the diodes are supposed to just limit the voltage drop to protect the 5 ohm. in this case the 5 ohm uh milliamp uh current shut resistor up here and if you do basic ohms law V ^

**Dave Jones:** 2 on R in this case uh 3.6 6 V squared on 5 ohms is only 2 1/2 W. Okay. So let's assume that you apply a voltage across the input here. It goes through the fuse. A very low impedance source by

**Dave Jones:** the way that's capable of, you know, many tens of amps or even hundreds of amps or whatever. And and so you're effectively shorting out your input jack between J2 and J4. You've made a mistake. Measure uh volts on when you've

**Dave Jones:** got the multimeter lead plugged into the jacks amp. Oops. Something's going to blow here. Is it going to be the fuse first or is it going to be these diodes or this resistor? Now, ignoring the fuse for a second, the diode will limit that

**Dave Jones:** current and that voltage immediately to 3.6 volts across the current shunt resistor of uh nominally 5 ohms. So, that's only 2 1/2 watts. It's a 4 W resistor here. As you can see, it's going to handle it no problems at all.

**Dave Jones:** Now I mentioned that these diodes standard 1N47s here I mentioned that these are pretty slow types. They're not shocky types. Now that slow actually refers to the reverse recovery time of the diode. And in that case we don't really care

**Dave Jones:** about that. That's why you don't need shocky diodes here. All you care about is the switch on time. In which case these diodes are effectively going to switch on instantly regardless of whether or not they're shocky or not. So

**Dave Jones:** there's no issue with the turn on time of these diodes here. They will switch on immediately, limit that voltage to 3.6 volts across that 5 ohm resistor and we'll have many many amps flowing through this fuse as well pretty much as

**Dave Jones:** much current as the voltage source you've hooked it up to can provide. Now uh these diodes, they're only 1 amp diodes, one in 4007s. So, you might think, well, 1 amp, that's not much at all. But, uh-huh. We'll go into the data sheets and we'll

**Dave Jones:** take a look at that. Now, this fuse, we also need to know how long it takes this fuse to blow. So, let's go into the data sheet for a fuse, shall we? Let's have a look here. Here's a typical Busman DMM

**Dave Jones:** multimeter fuse. And these are the ones that Fluke uh use and recommend as well as we'll look at ones from Littlefuse as well, the FLU series. No surprises why it's called FLU. It's short for Fluke because these are designed for Fluke and

**Dave Jones:** other multimeters. It tells you designed for multimeters only. Okay. And this is the f actual fuse specified for the uh Fluke 27. It's a 44 on 100 or 450 milliamp fuse. HRC, high rupture capacity fuse. And notice that it is uh these are

**Dave Jones:** designed to here it is intended to carry 100% of the rated current indefinitely. So that's just a little heads up on these fuses. If it's rated to 440 milliamps, it's not going to blow at 440 milliamps. It's actually going to hold

**Dave Jones:** that current and never ever blow. It only blows when it's higher than that. And how much higher than that will determine how much time it takes. Now, if we go down here, we'll get some characteristic curves. And these will

**Dave Jones:** tell us. Now, on the y ais, we've got the time in seconds it takes to blow. So, here's 1 second. This is the 1 second mark. Here, this is 1/10enth of a second. This is 10 seconds. This is 100

**Dave Jones:** seconds. So let's actually this is the characteristic curve we want the 44 on 100 the 440 milliamp fuse let's not worry about the 11 amps it's going to be the same so this video will just concentrate on this 440 milliamp fuse on

**Dave Jones:** the milliamp range now it'll blow in 1 second here you go across and that's what the x axis here is this is the current in milliamps so this is 1 amp here this is 100 milliamps down here this is 10 amps here this is 100 and a

**Dave Jones:** th00and and so on. So let's see how long it takes this fuse to blow in 1 second. Time in seconds on the y axis here. Extrapolate that will go up there. There you go. At 1.5. There it is. 1.5

**Dave Jones:** amps. Uh if you've got 1.5 amps flowing through this fuse, it will blow in 1 second. There you go. Well, let's see what the lowest point on this characteristic curve is. is down here at let's say that's 2.4 amps or something.

**Dave Jones:** So if you've got 2.4 amps flowing through that 440 milliamp fuse, then it's going to blow in 0.01 of a second or 10 milliseconds. It doesn't tell you anything faster than that. But of course, you can see that the curve is

**Dave Jones:** slowly branching off like that. Okay? So it's just going to get quicker and quicker. So if there's a 100 amps flowing through that thing, it's going to blow, you know, practically instantaneously really. Okay. So there you go. That is the fastest, let's say,

**Dave Jones:** the fastest it's going to switch in 10 milliseconds or, you know, at 2 and 12 amps. But let's say we've got say 5 amps flowing through that fuse, which is might be a reasonably uh, you know, a good number to pick, a nice round number

**Dave Jones:** to pick. It's going to blow pretty quick, right under 10 milliseconds. way under 10 milliseconds. It might be 1 millisecond or you know 500 microsconds or something like that. So uhhuh is that faster than our diode at that particular

**Dave Jones:** current? Now let's take a look at our diode here. 1 47 in this case. We'll look at the bridge rectifier next. So we've got our 1N47 diode here. And yes, it is a bog standard 1 amp diode. 1 amp nom. Here it

**Dave Jones:** is. Average rectified output current at 75° C. 1 amp. That's how these dodes are specified at their average rectified output current. So, you might think this is absolutely useless. If we got 5 amps flowing through this thing or more and

**Dave Jones:** we're going to blow the ass out of this diode and well, you know, um, bye-bye diode. You have to repair your multimeter. You can't just change your fuse. Aha, look at this. It also has a spec for nonrepetitive peak forward surge current

**Dave Jones:** specified at 8.3 millisecond single half sine wave superimposed on rated uh load. This is a pretty standard terminology which means half a sine wave at it can handle 30 amps. So this little piss and you know weak 1 amp diode can actually

**Dave Jones:** handle 30 amps for 8.3 milliseconds without blowing. It can handle that single surge there. Not a problem. So easily handle 30 amps. And for 8.3 milliseconds we saw on our graph down here that even at 5 amps it's going to

**Dave Jones:** blow in well under 10 milliseconds. Even at 3 amps here, it's going to blow in well under that 8.3 milliseconds. Bingo. The fuse is going to blow first. And you can bet your bottom dollar when Fluke designed this multimeter. That's part of

**Dave Jones:** the design aspect, the good engineering work gone into this, they would have looked at that diode data sheet and they would have went, "Well, 30 amps, no problems. We're well, you know, we're an order of magnitude over where we need to

**Dave Jones:** be." Cuz 30 amps here, look. you extrapolate that graph, it's ah man, it's way down the bottom of the graph heaps quicker. So, that fuse is definitely going to blow. And we've only got a single figure there of 30 amps for

**Dave Jones:** a nonrepetitive uh single half sine wave. Well, what happens if you go over that? What if there's, you know, your AC source and you got multiple half sine waves there? It's it's it's certainly repetitive. What is the difference in the middle

**Dave Jones:** there? Well, you can go down to the characteristic curves down here. Here's the one we're interested at. This one here on the y-axis, we've got the peak forward surge current in amps. There's the 30 amps that we had before number

**Dave Jones:** and the x-axis is a number of cycles at 60 hertz, max non-repetitive forward peak surge current. And there's one 30 amp. So, we got the single figure, but that graph allows us to get more than that. So if you got a hundred cycles

**Dave Jones:** like that at 60 Hz, so well over a second, you're still talking 10, you know, almost 10 amps there, sort of at that uh sort of 1 second mark. So that diode for a second is still going to

**Dave Jones:** hold 10 amps. And it's a wimpy 1 amp diode, but aha, there's a diode bridge in there. Well, this happens to be the same diode bridge used in there. It's a DFO2. So let's have a look. Once again,

**Dave Jones:** it's a nominal 1 amp rated diode. You know, pretty pissweak kind of bog standard one you you'd use in your basic uh linear power supply. It's not a shocky type once again. But here you go. Look at this peak forward surge current

**Dave Jones:** single half sine wave 50 amps. It's even better than the one in 4007. And that's for the DFO2 which we're using here. Not a problem. 50 amps. We absolutely hit a home run there. This fuse is definitely going to blow first. And if we want some

**Dave Jones:** uh double check on that, here's the little fuse uh brand one, the FLU series, the Fluke series, of course. Once again, we've got our nice characteristic graph here. Let's have a look at it. This one only goes down to

**Dave Jones:** 10 milliseconds as well. Doesn't go any faster. the this one. Let's have a look at 1 amp, 2 amps, 3 amps, 4 amps, 5 amps. It's going to blow in 20 milliseconds there. Once again, if you were replacing this fuse and you weren't

**Dave Jones:** using the uh the recommended fuse replacement, you might want to actually look at this these sort of curves and see that, you know, is this fuse suitable for my particular multimeter? I've got diodes that can handle, you know, 50 amps for 8.3 milliseconds or

**Dave Jones:** something like that. Well, you look at these graphs, but pretty much all of these HRC fuses are going to be within the same ballpark in terms of their uh the average time versus current curve here. They're all going to be pretty

**Dave Jones:** much the same. So you can go through the same thing with the micro amp one and stuff like that because the uh 10 amp one pretty much isn't protected by this uh diode bridge here because as you can

**Dave Jones:** see the amps come ah sorry I can't really highlight this as I'm doing it but the current comes directly in there straight through there straight back out and really it's only the sense line which goes off there. So, this diab

**Dave Jones:** bridge is not applicable to the uh 10 amp current range, but there you have it. I mean, you've got other things that can blow in there, your PCB traces and stuff like that, your wiring and all that sort of stuff, but usually they're

**Dave Jones:** going to handle pretty beefy amounts of current unless the multimeter is poorly designed. So, there you go. I hope that uh cleared it up and it was interesting. And if you want to discuss the video, jump on over to the EV blog forum. And

**Dave Jones:** if you like it, please give it a big thumbs up. Catch you next time.

**Dave Jones:** [Music]
