---
video_id: I4ED_8cuVTU
title: EEVBlog #473 - Microcontroller Voltage Doubler
url: https://www.youtube.com/watch?v=I4ED_8cuVTU
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 33, "3": 52, "4": 63, "5": 70, "6": 82, "7": 95, "8": 109, "9": 122, "10": 134, "11": 140, "12": 153, "13": 168, "14": 179, "15": 194, "16": 201, "17": 222, "18": 235, "19": 255, "20": 266, "21": 286, "22": 302, "23": 318, "24": 336, "25": 350, "26": 359, "27": 371, "28": 390, "29": 402, "30": 416, "31": 430, "32": 443, "33": 451, "34": 465, "35": 478, "36": 490, "37": 504, "38": 512, "39": 522, "40": 531, "41": 551, "42": 566, "43": 580, "44": 591, "45": 607, "46": 620, "47": 634, "48": 643, "49": 657, "50": 669, "51": 686, "52": 706, "53": 722, "54": 733, "55": 747, "56": 763, "57": 772, "58": 792, "59": 807, "60": 824, "61": 837, "62": 854, "63": 864, "64": 896, "65": 907, "66": 929, "67": 942, "68": 954, "69": 975, "70": 983, "71": 995, "72": 1008, "73": 1020, "74": 1034, "75": 1045, "76": 1064, "77": 1082, "78": 1104, "79": 1121, "80": 1129, "81": 1143, "82": 1154, "83": 1172, "84": 1183, "85": 1197, "86": 1215, "87": 1232, "88": 1245, "89": 1261, "90": 1272, "91": 1287, "92": 1301, "93": 1316, "94": 1330, "95": 1340, "96": 1356, "97": 1364, "98": 1376, "99": 1386, "100": 1400, "101": 1413, "102": 1423, "103": 1432, "104": 1443, "105": 1454, "106": 1467, "107": 1483, "108": 1491, "109": 1506, "110": 1516, "111": 1530, "112": 1549, "113": 1560, "114": 1571, "115": 1578, "116": 1587, "117": 1603, "118": 1616}
---

**Dave Jones:** Hi, welcome to Fundamentals Friday. This one's a follow-on from the Cockcroft-Walton voltage multiplier we looked at a couple of weeks back. And once again, it's a little useful circuit building block for all sorts of applications.

**Dave Jones:** We're going to choose one typical application today where it may be useful. And that's in the case of a microcontroller, for example, or your circuit widget, whatever it is, powered from, say, for argument's sake, a little 3-V coin cell battery, CR2032, or a couple of double A's, or a couple of triple A's, or whatever, 3-V supply.

**Dave Jones:** And let's say you actually wanted to power something that needs a 5-V rail, like one of those um LCDs, a typical LCD module. You can get 3.3-V ones, but much more common and much cheaper to get and much more wider availability of 5-V versions.

**Dave Jones:** So, how do you actually hook that up? Well, there's a couple of ways to do it. We're going to look at one way. And the building block we're going to look at is called the Dickson voltage doubler.

**Dave Jones:** Some common times called a Dickson multiplier, sometimes called a Dickson charge pump, all sorts of things, or just a charge pump. Doesn't have to have the name Dickson in it.

**Dave Jones:** And what it is, it takes us back to the circuit we looked at with the Cockcroft-Walton multiplier. And in this case, the Green Acre circuit that we looked at.

**Dave Jones:** If we had a transformer with a 3-V peak-to-peak input signal, it actually level shifted that up and gave us 6-V DC out. If you haven't seen that video, I'll link it in down below.

**Dave Jones:** Explains all this. And we're going to use this basic circuit again. Once again, a little rearrangement again, and it'll create our Dickson voltage doubler. And we can do exactly the same thing, because like in the case of this product here, we've got our microcontroller.

**Dave Jones:** We don't want a transformer. We don't want all sorts of things. I mean, there's various options you You you know, up here you can, if you wanted to double your voltage from 3 volts to 6 volts, you could use a 7660 charge pump chip.

**Dave Jones:** And that's a classic jelly bean building block part. It's a capacitor voltage doubler, voltage inverter. You can use it in various configurations, but it's, you know, it might cost a dollar a chip or something like that.

**Dave Jones:** And well, you know, you want to keep your bill of materials cost low as you do in a lot of projects. For a one-off, might not be a problem.

**Dave Jones:** There's various ways to do it, but let's try and lower the cost here by doing it with diodes and capacitors cuz you've already got likely diodes and capacitors in your bill of materials anyway.

**Dave Jones:** And well, in any case, even if you don't have the diodes, for example, they're incredibly cheap to add to your circuit. So, we can replace a 7660 voltage charge pump voltage doubler with a Dickson voltage doubler.

**Dave Jones:** So, how do we do that? Well, first of all, let's get rid of the transformer. We don't need a transformer. That's only useful for high voltage generation. We're not talking high voltage generation here.

**Dave Jones:** We're talking low voltage, and that's where this Dickson voltage doubler comes in the play. An absolute perfect example is the case we've got here. We want to double 3 volts into roughly 5 volts to power our LCD.

**Dave Jones:** Ideally, you know, you'd have 6 volts and then you could voltage regulate it down and all that sort of stuff. But we won't really go into that. Now, how do we do it?

**Dave Jones:** Well, a quick rearrangement. Take our classic Greinacher circuit there and erase that and put our diode in series like that and a capacitor down like that, but let's not have it go into ground.

**Dave Jones:** Shall we? Let's have it another input here. So, we've got two inputs coming in here like this. And what do we have in our design up here. Well, we've got 3 volts DC and we've got a microcontroller.

**Dave Jones:** What can microcontrollers do? They can generate clocks, PWM signals. So, we can actually use the microcontroller to generate a clock signal. So, what we're going to do here is we've got two inputs like this and this one will actually put to 3 volts DC.

**Dave Jones:** So, we'll tie that to our voltage level and then we'll feed in a clock into this input down here and magic happens, which I'll explain in a minute. We're going to get 6 volts DC out.

**Dave Jones:** And if you've seen the Cockcroft-Walton multi-voltage multiplier video, you'll see how that works. We've effectively level shifted that up, feeding in the clock, which we're getting from the transformer in the other configuration, and this circuit configuration is now a Dickson voltage doubler.

**Dave Jones:** We'll get 6 volts DC out of that with nothing more than a single pin on our microcontroller generating a PWM signal. Beauty. Now, if you were paying attention when I swapped these components around here, I didn't actually do anything at all.

**Dave Jones:** This circuit configuration is actually exactly the same as the Greinacher voltage doubler, except that we're now um we don't have like an an AC signal source from a transformer or something like that.

**Dave Jones:** We've just got a a a 3-volt voltage source or our DC source plus a clock, but it's exactly the same thing essentially. You can switch those around and then this is waveform up here, 3 volts down there, the anode of the diodes down there, series diode there.

**Dave Jones:** It's exactly the same circuit. Haven't changed anything. So, a Dickson voltage doubler is a bit of a con. It's actually a Greinacher doubler. There's really essentially no difference. And the waveform and how it operates is exactly the same as before.

**Dave Jones:** So, let's have a look at the operation of this thing. Now, once again, we're going to assume that we've got ideal diodes. We'll get into the practical uh considerations in there later.

**Dave Jones:** But, ideal diodes, let's assume also that the circuit's reached a steady state and the capacitor is charged up and we've got no load on this thing, okay? So, this point number one here is uh 3 V DC here.

**Dave Jones:** It's charged up to 3 V. Well, there's 3 V across that capacitor there. So, when this um is uh low, when waveform two down here is low, then our point up here, number one, is going to be 3 V above there.

**Dave Jones:** But, when this waveform goes high, there's already 3 V across our capacitor, so then it's going to double up to 6 V at that point. And it can't flow back through the diode, it's going to prevent that.

**Dave Jones:** So, what do we end up with at this point number one? We end up with this shifted, once again, waveform shifted like that uh above this bias reference voltage, which happens to be our battery voltage or our supply voltage.

**Dave Jones:** It could be 3 V, 5 V, whatever your DC supply voltage is. And bingo, it's shifted that waveform up like that. And this point here is the red waveform there like that.

**Dave Jones:** And of course, we've just got our basic rectifier here with the diode and the cap, which then smooths that out to our fixed 6 V DC out. Bingo, we've doubled our voltage with just a single pin on our microcontroller.

**Dave Jones:** Or the clock could come from somewhere else in your circuit. Usually, you're going to have it coming from a micro though. And that's all there is to it. It's just a Greinacher doubler.

**Dave Jones:** But, yeah, it's called a Dickson doubler. Whatever. And the reason these things are sometimes called charge pumps as well is because the capacitor charges up and then you're So, it's already charged up and then you're pumping more into it.

**Dave Jones:** You're utilizing the charge that's already on the capacitor to boost that voltage up. And that's essentially what we're doing. We're essentially just level shifting. Again, once again, we're not actually doubling.

**Dave Jones:** You know, there's no doubling here. This waveform here doesn't get twice as big as this one. It's just shifted it up like that. And we're utilizing that DC reference level to do And the diode steering to do that.

**Dave Jones:** But unlike our high voltage DC generation, these low voltage charge pumps or doublers usually have to drive at least some little load. You're driving like an LCD which might take, you know, 1 or 2 milliamps or something like that.

**Dave Jones:** But for, you know, a couple of milliamps, it's going to be good enough using typical, you know, fairly low value caps in here, like 10 microfarads or something like that.

**Dave Jones:** Can easily probably do a couple of milliamps. If you want in the order of hundreds of milliamps, uh you're not really going to get it from one of these capacitor charge pumps.

**Dave Jones:** But of course, you can do an awful lot with a milliamp. You can fly to the moon on a milliamp or drive an LCD or drive an op amp or something like that.

**Dave Jones:** You could even regulate, use one of those low power low dropout voltage regulators if you wanted to regulate the output because when you start putting a load on here, as we saw last time, even if it's a small load, you know, a drawing a milliamp or two, then you're going to start to see, well, you're Let's draw in the blue waveform.

**Dave Jones:** It's not going to look perfect like that anymore. Sorry about the red one going there. It's going to start drooping like this. And then it'll kick it back up, and it'll droop down again, and it'll kick it back up.

**Dave Jones:** And you're going to get ripple on this DC output here. And sometimes that's not desirable if you're, you know, powering some analog stuff or something. But you might be able to say, have a voltage regulator, a 5-V voltage regulator in there.

**Dave Jones:** Once again, we're assuming ideal diodes. We're not actually going to get 6 V out of this thing when we build it up, obviously, because, you know, a diode loss, you know, 0.3 V for a Schottky or something like that.

**Dave Jones:** But, um you know, the theory remains the same. You could have a low voltage dropout in there. You base these capacitors based on the discharge rate of your load, and bingo, you can get a nice, clean, regulated output for your little project.

**Dave Jones:** Great. So, sometimes that's a lot more simpler and cost-effective than changing the battery solution for your product. Like, for example, I used this in my little micro watch uh project, my scientific calculator watch, right?

**Dave Jones:** I powered it from a single 3-V CR2032 coin cell battery. I couldn't really put a a higher voltage battery in there. It just didn't suit the system design of the calculator watch.

**Dave Jones:** So, it was much more beneficial to use one of these Dickson voltage doublers than it was to re-engineer, or, you know, uh change my battery solution for this thing.

**Dave Jones:** And at this stage, you should be thinking, "Aha, can we use that multi-stage configuration like we did on the Cockcroft-Walton multiplier?" Well, yes, of course we can. It's exactly the same circuit.

**Dave Jones:** It's just sort of in a different usage um configuration here. So, we've added another stage here to this so we can multiply our 3-V DC up to 9-V DC.

**Dave Jones:** Beauty. How does it work? Exactly the same uh configuration. Imagine this, that is still our same circuit as before, okay? Uh but, we've now got a 6-V DC reference here, point up here instead of a 3-V DC reference point here.

**Dave Jones:** So, we've just shifted that waveform up again. I won't go through all the details. It's the same as I explained in the Cockcroft-Walton voltage multiplier video. So, that 3 volts peak-to-peak from our microcontroller here, and it will be 3 volts peak-to-peak, of course, from a CMOS microcontroller, then it just shifts it from 6 up to 9.

**Dave Jones:** So, 0.3 here, the green waveform, is exactly the same, it's just shift shifted it up. This point This point here gets shifted up again, and then we've got 9 volts, and then we've got our final rectifier on the output, which gives us 9 volts DC on the output.

**Dave Jones:** But, of course, once you put a load on, it's going to sag like that, but uh there you go. Then, we could certainly whack in our 5-volt voltage regulator and have heaps of margin.

**Dave Jones:** You wouldn't even need a low dropout type. Beauty. And in case you're wondering, yes, this is the new Teespring crowdfunded triple 5 timer t-shirt. If you missed out on it, uh well, I might run another one soon.

**Dave Jones:** We'll see. But, top quality. I love it. And next up, we have Dave, looking trendy and smart in a nice little Teespring number. He looks equally at home in the dumpster as he does on the workbench.

**Dave Jones:** And to the breadboard we go. Deja vu, folks, we've been here before. Nothing new at all. It's exactly what we looked at the other week. But, we'll go through the motions again.

**Dave Jones:** Here it is, Dave Cadbury. We've got our 3-volt DC supply, which will come from our bench supply. We've got 3 volts DC coming from the function gen, and yes, it's shifted up to 1.5 volts, so it's not AC, so it's 0 to 3 volts, so it simulates our the signal coming from our microcontroller.

**Dave Jones:** And then we have our multi-stage doubler. There's our first stage there, and there's our second stage there. And we should get 9 volts out of here. And these are the um the on this oscilloscope, channel 1, channel two, channel three, channel four.

**Dave Jones:** And it's exactly the same as what we had last time as well on the scope screen. All four channels are ground referenced down here on that bottom graticule down there, 2 V per division on all the channels there, and we've got our peak voltage of each of the channels.

**Dave Jones:** So, let's have a look. Here on the circuit, our point one here is actually There it is, 6 V. Uh so, we've got our 3 V input. By the way, our square wave amplitude there is 3 V.

**Dave Jones:** I haven't shown the square wave actually coming in because it's exactly the same as that. And it's 6 V, and then the top of point two here, notice that we've got our diode loss between there and there, but with no load at the moment, so it's it's very small.

**Dave Jones:** And then the top of the next point, channel three up here, 8.2 V, and that's actually the uh blue waveform up there. So, point three is the blue waveform.

**Dave Jones:** Sorry. Point one is the yellow waveform there. Point two is the green waveform there, which is your DC value across there, and because that AC signal gets converted into DC, that's our 6 V DC reference, and then it gets pumped up again, shifted up by the blue waveform there, channel three, up to Well, in this case, 8.1 V peak, and then our final DC output is the purple one there.

**Dave Jones:** And bingo, 8.1 V. And what happens if I shift my 3 V signal here? Well, let's adjust our bench supply. There we go. As we move it up and down, all the waveforms Oh, we just lost our trigger there.

**Dave Jones:** Of course, once we get to that point, but we can boost that up there, and there you go. It just shifts that waveform up and down. So, with precisely 3 V DC input and our 3 V peak-to-peak square wave, which we can generate with a microcontroller, we can get a final output voltage here of 8 V.

**Dave Jones:** There it is. And this is using just bog standard 1N914 or 4148 diodes, not even the Schottky type. Now, let's have a look what happens if we put a lousy little 10-k load on this thing.

**Dave Jones:** So, our final output DC voltage of 8 V here divided by 10 k, assuming it stays at 8 V of course, divided by 10 k, 800 microamps. So, we're drawing less than a milliamp.

**Dave Jones:** Here we go. Let's connect it up. And bingo, look. You'll see it drop. And you'll notice that I can probably boost all the channels up like that. You can notice the ripple starting to appear on channel two there, which is our second point, which is our supposedly our DC reference in there.

**Dave Jones:** It was a straight line before, but now you can see the ripple in there due to the fact that we're drawing a 10-k load. And by the way, I didn't put values on here.

**Dave Jones:** These are actually 0.47 microfarad. And let's drop that load by an order of magnitude from 10 k down to 1 k. Here we go. There we go. Look at that.

**Dave Jones:** So, look, it's practically useless now. 3.2 V top value of our final output. As you can see, it's absolutely useless when we try and power a 1-k load there.

**Dave Jones:** Our 3-V, we're still getting our 3-V both of our 3-V signals going in, but it's just it doesn't work anymore. It's useless. And we'll bump that up to 2 k.

**Dave Jones:** And as you can see, significantly improved there. There we go. And 3 k, 4 k, 5 k. And you can see the progression in that. But of course, we're not using Schottky diodes here.

**Dave Jones:** In practice, you'd almost always use a Schottky diode in this configuration unless you had really low current and you really didn't care. Generally, you're not going to use your little jelly bean 1N 4148s.

**Dave Jones:** You're going to use some sort of Schottky diode. They're, you know, practically the same price anyway. So, let's assume that we just had the single stage configuration here like this and here's our final output voltage, 4.62 V at This is a 10k load, half a microfarad cap on there.

**Dave Jones:** And by the way, frequency is 10 kHz here, a typical frequency that you might get out typical PWM frequency you might get out of your microcontroller, for example. And we're only getting a DC output voltage of 4.62 V there, but that's probably going to be good enough.

**Dave Jones:** Only talking like So, you know, 4.62 V / 10k. So, we're only talking half a milliamp. Some LCDs can go down that low, but not all of them, but you know, potentially, we could actually, you know, almost power one of those little LCD modules because they are fairly tolerant of the supply voltage.

**Dave Jones:** We'd be able to power it with just a single stage circuit with even crappy, you know, 4148 diodes in there and a low value of capacitance. So, what happens if we replace this cap, half a microfarad, with say 47 microfarads?

**Dave Jones:** Fairly big step up in value. Well, let's do that. I'm going to rip that out there and I'm going to stick in a 470 microfarad cap. Aha, look at that.

**Dave Jones:** We now jumped up to about 4.8 V or thereabouts. So, what's our frequency going to do? Well, of course, it's going to change the discharge curve of this cap.

**Dave Jones:** So, of course, this is still our 47 microfarads in here, but our second stage one up there, you'll be able to you can just see the ripple on there at the moment, but let's increase the frequency, shall we?

**Dave Jones:** So, here we go. Oh, well well, we can drop well we we can increase it, of course, and of course, we just get better, you know, there's you can't see any ripple on there now, but if we lower that frequency down significantly, aha, look at that.

**Dave Jones:** You can start seeing 4 kHz, three, you can start seeing the ripple appearing and the droop there. If we go down to 1 kHz, you know, ah, pretty bad.

**Dave Jones:** So, you don't want to be operating these things at 1 kHz. 10 kHz, reasonably good rule of thumb. Now, what happens if we change all of these caps to 47 microfarads, pretty beefy value.

**Dave Jones:** Bingo, here it is. This is with our 1K load. And the amazing thing is, that's still at 1 kHz, as you can see. So, it is possible to use a value like that, but uh you have a frequency like that, but you have to go um uh much higher in your capacitor's values, and that's with a 1K load.

**Dave Jones:** So, um our There we go. We're drawing 6 milliamps from this circuit, just over 6 volts on our second stage output there. So, 6 milliamps this thing is taking with even 1N4148 diodes, but of course, that is a uh two-stage one to get our 6 volts.

**Dave Jones:** So, we're getting nothing near our 9 volts we expect, but uh good enough. But even that single-stage one, 4.7 volts there, is enough to drive, like you know, four or five milliamps, even at 1 kHz.

**Dave Jones:** Not a problem. And because there's no ripple, we're not going to actually see any uh benefit there by going up in frequency, as you can see. Frequency is only going to matter once you start drooping.

**Dave Jones:** And if we take our frequency down 81 Hz, look at that. Because we're using such large value caps, our switching frequency can actually be relatively low, you know, in the order of 100 Hz or so.

**Dave Jones:** And we're still going to get a good enough DC voltage out that we could use to power an LCD or something else perhaps, especially if we decide to put an extra linear regulator after that.

**Dave Jones:** But of course, generally speaking, you know, you're not going to be using 47 mic caps in there for example. They're just more expensive, you know, and they're larger and you know, you're going to use little ceramics that you've already got in the circuit.

**Dave Jones:** Typically, you know, if you're doing an SMD design, you might have 1 micro Farad caps in there for example might be very typical or something like that. All the 470 ends that I was using before, 0.47 micro Farads.

**Dave Jones:** And as you can see here, we couldn't get the several milliamps out of there even at the higher frequencies. So as you can see, it's all going to be a trade-off here of the value of the capacitance versus your load versus your diode the type of diode you got, the diode drops.

**Dave Jones:** I won't go into putting Schottky's in there as well. If we put Schottky's in there, we'll find that these waveforms will all be shifted up or have lower diode losses and stuff like that.

**Dave Jones:** So, you know, by all means build this thing up and experiment with it and it's a great circuit to use next time you need a simple voltage doubler or to get, you know, a higher value rail out of your project that's powered from a couple of batteries or something like that.

**Dave Jones:** You don't have to re-engineer your battery solution. You can just use one of these doublers or in this case, a tripler. Now let's look at a practical configuration of this.

**Dave Jones:** In this case, it's my microwatch project. Here it is. Here's the schematic for it. You can download it from my microwatch website if you really want to, but it's a microcontroller.

**Dave Jones:** Well, here's the actual thing powered from a single CR2032 battery here. Let's switch it on. It's in power saving mode at the moment. Haven't set the time or anything like that, but there you go.

**Dave Jones:** It's the world's only do-it-yourself scientific calculator watch. Now, uh, the interesting thing about this is that I've used Well, there's two interesting things. One's One is that I've used two Dickson doublers here.

**Dave Jones:** Might look a bit unusual, but trust me, I've got one for the LCD here that powers the 5-V LCD. It's not a 3.3-V one or 3-V one, so it, uh, needs 5-V, so I've got a Dickson doubler in there.

**Dave Jones:** And I've got another one for the LED backlight as well. I think it had like, uh, two LEDs in series. That's why I had to actually, uh, do that this particular module.

**Dave Jones:** Anyway, so I've got two Dickson doublers in there. The configuration is basically exactly like this. Of course, we've got a fixed DC voltage here, in this case 3 V from the battery.

**Dave Jones:** We've got our, uh, 3-V, uh, square wave coming from our PIC microcontroller in there. But in this case, of course, we're only using a single-stage doubler here, so ignore the rest of that.

**Dave Jones:** There we go. That's basically what we've got here. Now, it might look a bit unusual in that Well, why aren't these diodes here going to 3 V like this?

**Dave Jones:** Why are they going to a pin on the microcontroller? Aha, that's actually a feature. It allows the microcontroller to actually switch the output off and on under software control.

**Dave Jones:** So, if the output here, instead of tying this to 3 V, you tie it to a pin on the microcontroller, when that's high, 3 V, you apply your PWM signal, uh, well, in there, then it switches your LCD voltage on or whatever it else you want to power.

**Dave Jones:** If you set that low and switch off your PWM signal, bingo, your output voltage goes down to zero. And I can do that for both the LCD backlight and voltage on the LCD.

**Dave Jones:** And in this case, I've got, uh, a Schottky, of course, a standard bat 54, really a jelly bean um stuff in there, super cheap SM standard SMD type. I've got only a lousy 100 in in there, and I've got 10 micro farads there.

**Dave Jones:** On the output I actually forget what value I'm switching it at. I don't know. It's a, you know, 5 kHz or something like that, 10 kHz. Don't exactly remember, but so there you go.

**Dave Jones:** There's a real world example of uh two different reasons why you want to use it, the LCD and the back light. Uh, of course, because I was forced to use this LCD, 53 by 20 mm, and it had a certain type of back light, and it had to be a certain type.

**Dave Jones:** I couldn't use anything else. Couldn't just start substitute it for anything. So, really, um you know, I had to do this. This was my only choice apart from using a like a as I said before, like a 7460 uh voltage uh doubler uh charge pump voltage doubler or something like that.

**Dave Jones:** Eh, it's more expensive, so I just decided to go with the diode and capacitor solution. Piece of cake. And then I added in the bonus feature of being able to switch off the LCD, as you've seen.

**Dave Jones:** It goes into a power down mode that actually disables the uh voltage to the LCD, so it doesn't uh draw any current at all, and this thing can actually get a reasonably long battery life cuz it's only powering the microcontroller.

**Dave Jones:** The LCD I can completely switch off. And of course, the back light voltage, I can switch that off and on. There it is. It's gone into low power state.

**Dave Jones:** It's only drawing, you know, microamps instead of, you know, a milliamp or two. And you switch it on, draws a couple of milliamps, operates for a few minutes, then auto switches off.

**Dave Jones:** Real world practical example of a tricked up, I guess, uh Dickson doubler here with on off capability. So, there you go. I hope you enjoyed that follow up to the Cockcroft-Walton voltage multiplier.

**Dave Jones:** This is the Dickson doubler or uh charge pump doubler, diode doubler, whatever you want to call it. It's an interesting little and useful little building block circuit. And remember, if you like our Fundamentals Friday, please give it a big thumbs up.

**Dave Jones:** Dual thumbs up. And if you want to discuss it, jump on over to the EEVblog forum. Catch you next time. Gentlemen, I wouldn't trust this overgrown pile of microchips any further than I could throw it.
