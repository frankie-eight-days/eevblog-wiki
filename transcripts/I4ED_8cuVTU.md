---
video_id: I4ED_8cuVTU
title: EEVBlog #473 - Microcontroller Voltage Doubler
url: https://www.youtube.com/watch?v=I4ED_8cuVTU
source: youtube-asr
---

**Dave Jones:** Hi, welcome to Fundamentals Friday. This one's a follow-on from the Cockcroft-Walton voltage multiplier we looked at a couple of weeks back. And once again, it's a little useful circuit building block for all sorts of applications. We're going to choose one

**Dave Jones:** typical application today where it may be useful. And that's in the case of a microcontroller, for example, or your circuit widget, whatever it is, powered from, say, for argument's sake, a little 3-V coin cell battery, CR2032, or a

**Dave Jones:** couple of double A's, or a couple of triple A's, or whatever, 3-V supply. And let's say you actually wanted to power something that needs a 5-V rail, like one of those um LCDs, a typical LCD module. You can get 3.3-V ones, but much

**Dave Jones:** more common and much cheaper to get and much more wider availability of 5-V versions. So, how do you actually hook that up? Well, there's a couple of ways to do it. We're going to look at one way. And the building block we're going

**Dave Jones:** to look at is called the Dickson voltage doubler. Some common times called a Dickson multiplier, sometimes called a Dickson charge pump, all sorts of things, or just a charge pump. Doesn't have to have the name Dickson in it. And

**Dave Jones:** what it is, it takes us back to the circuit we looked at with the Cockcroft-Walton multiplier. And in this case, the Green Acre circuit that we looked at. If we had a transformer with a 3-V peak-to-peak input signal, it

**Dave Jones:** actually level shifted that up and gave us 6-V DC out. If you haven't seen that video, I'll link it in down below. Explains all this. And we're going to use this basic circuit again. Once again, a little rearrangement again, and

**Dave Jones:** it'll create our Dickson voltage doubler. And we can do exactly the same thing, because like in the case of this product here, we've got our microcontroller. We don't want a transformer. We don't want all sorts of things. I mean, there's various options

**Dave Jones:** you You you know, up here you can, if you wanted to double your voltage from 3 volts to 6 volts, you could use a 7660 charge pump chip. And that's a classic jelly bean building block part. It's a

**Dave Jones:** capacitor voltage doubler, voltage inverter. You can use it in various configurations, but it's, you know, it might cost a dollar a chip or something like that. And well, you know, you want to keep your bill of materials cost low

**Dave Jones:** as you do in a lot of projects. For a one-off, might not be a problem. There's various ways to do it, but let's try and lower the cost here by doing it with diodes and capacitors cuz you've already

**Dave Jones:** got likely diodes and capacitors in your bill of materials anyway. And well, in any case, even if you don't have the diodes, for example, they're incredibly cheap to add to your circuit. So, we can replace a 7660 voltage charge pump voltage doubler with

**Dave Jones:** a Dickson voltage doubler. So, how do we do that? Well, first of all, let's get rid of the transformer. We don't need a transformer. That's only useful for high voltage generation. We're not talking high voltage generation here. We're

**Dave Jones:** talking low voltage, and that's where this Dickson voltage doubler comes in the play. An absolute perfect example is the case we've got here. We want to double 3 volts into roughly 5 volts to power our LCD. Ideally, you know, you'd have 6 volts

**Dave Jones:** and then you could voltage regulate it down and all that sort of stuff. But we won't really go into that. Now, how do we do it? Well, a quick rearrangement. Take our classic Greinacher circuit there and erase that and put our diode

**Dave Jones:** in series like that and a capacitor down like that, but let's not have it go into ground. Shall we? Let's have it another input here. So, we've got two inputs coming in here like this. And what do we have in our design

**Dave Jones:** up here. Well, we've got 3 volts DC and we've got a microcontroller. What can microcontrollers do? They can generate clocks, PWM signals. So, we can actually use the microcontroller to generate a clock signal. So, what we're going to do

**Dave Jones:** here is we've got two inputs like this and this one will actually put to 3 volts DC. So, we'll tie that to our voltage level and then we'll feed in a clock into this input down here and magic

**Dave Jones:** happens, which I'll explain in a minute. We're going to get 6 volts DC out. And if you've seen the Cockcroft-Walton multi-voltage multiplier video, you'll see how that works. We've effectively level shifted that up, feeding in the clock, which we're getting from the

**Dave Jones:** transformer in the other configuration, and this circuit configuration is now a Dickson voltage doubler. We'll get 6 volts DC out of that with nothing more than a single pin on our microcontroller generating a PWM signal. Beauty. Now, if you were paying

**Dave Jones:** attention when I swapped these components around here, I didn't actually do anything at all. This circuit configuration is actually exactly the same as the Greinacher voltage doubler, except that we're now um we don't have like an an AC signal

**Dave Jones:** source from a transformer or something like that. We've just got a a a 3-volt voltage source or our DC source plus a clock, but it's exactly the same thing essentially. You can switch those around and then this is waveform up here, 3

**Dave Jones:** volts down there, the anode of the diodes down there, series diode there. It's exactly the same circuit. Haven't changed anything. So, a Dickson voltage doubler is a bit of a con. It's actually a Greinacher doubler. There's really essentially no difference. And the

**Dave Jones:** waveform and how it operates is exactly the same as before. So, let's have a look at the operation of this thing. Now, once again, we're going to assume that we've got ideal diodes. We'll get into the practical uh considerations in

**Dave Jones:** there later. But, ideal diodes, let's assume also that the circuit's reached a steady state and the capacitor is charged up and we've got no load on this thing, okay? So, this point number one here is uh 3 V DC here. It's charged up

**Dave Jones:** to 3 V. Well, there's 3 V across that capacitor there. So, when this um is uh low, when waveform two down here is low, then our point up here, number one, is going to be 3 V above there. But, when

**Dave Jones:** this waveform goes high, there's already 3 V across our capacitor, so then it's going to double up to 6 V at that point. And it can't flow back through the diode, it's going to prevent that. So, what do we end up with at this point

**Dave Jones:** number one? We end up with this shifted, once again, waveform shifted like that uh above this bias reference voltage, which happens to be our battery voltage or our supply voltage. It could be 3 V, 5 V, whatever your DC supply voltage is.

**Dave Jones:** And bingo, it's shifted that waveform up like that. And this point here is the red waveform there like that. And of course, we've just got our basic rectifier here with the diode and the cap, which then smooths that out

**Dave Jones:** to our fixed 6 V DC out. Bingo, we've doubled our voltage with just a single pin on our microcontroller. Or the clock could come from somewhere else in your circuit. Usually, you're going to have it coming from a micro though. And

**Dave Jones:** that's all there is to it. It's just a Greinacher doubler. But, yeah, it's called a Dickson doubler. Whatever. And the reason these things are sometimes called charge pumps as well is because the capacitor charges up and then you're

**Dave Jones:** So, it's already charged up and then you're pumping more into it. You're utilizing the charge that's already on the capacitor to boost that voltage up. And that's essentially what we're doing. We're essentially just level shifting. Again, once again, we're not actually

**Dave Jones:** doubling. You know, there's no doubling here. This waveform here doesn't get twice as big as this one. It's just shifted it up like that. And we're utilizing that DC reference level to do And the diode steering to do that. But unlike our high voltage

**Dave Jones:** DC generation, these low voltage charge pumps or doublers usually have to drive at least some little load. You're driving like an LCD which might take, you know, 1 or 2 milliamps or something like that. But for, you know, a couple

**Dave Jones:** of milliamps, it's going to be good enough using typical, you know, fairly low value caps in here, like 10 microfarads or something like that. Can easily probably do a couple of milliamps. If you want in the order of

**Dave Jones:** hundreds of milliamps, uh you're not really going to get it from one of these capacitor charge pumps. But of course, you can do an awful lot with a milliamp. You can fly to the moon on a milliamp or

**Dave Jones:** drive an LCD or drive an op amp or something like that. You could even regulate, use one of those low power low dropout voltage regulators if you wanted to regulate the output because when you start putting a load on here, as we saw

**Dave Jones:** last time, even if it's a small load, you know, a drawing a milliamp or two, then you're going to start to see, well, you're Let's draw in the blue waveform. It's not going to look perfect like that anymore.

**Dave Jones:** Sorry about the red one going there. It's going to start drooping like this. And then it'll kick it back up, and it'll droop down again, and it'll kick it back up. And you're going to get ripple on this DC output here. And

**Dave Jones:** sometimes that's not desirable if you're, you know, powering some analog stuff or something. But you might be able to say, have a voltage regulator, a 5-V voltage regulator in there. Once again, we're assuming ideal diodes. We're not actually going to get 6 V out

**Dave Jones:** of this thing when we build it up, obviously, because, you know, a diode loss, you know, 0.3 V for a Schottky or something like that. But, um you know, the theory remains the same. You could have a low voltage dropout in

**Dave Jones:** there. You base these capacitors based on the discharge rate of your load, and bingo, you can get a nice, clean, regulated output for your little project. Great. So, sometimes that's a lot more simpler and cost-effective than changing the battery solution for your

**Dave Jones:** product. Like, for example, I used this in my little micro watch uh project, my scientific calculator watch, right? I powered it from a single 3-V CR2032 coin cell battery. I couldn't really put a a higher voltage battery in there. It

**Dave Jones:** just didn't suit the system design of the calculator watch. So, it was much more beneficial to use one of these Dickson voltage doublers than it was to re-engineer, or, you know, uh change my battery solution for this thing. And at

**Dave Jones:** this stage, you should be thinking, "Aha, can we use that multi-stage configuration like we did on the Cockcroft-Walton multiplier?" Well, yes, of course we can. It's exactly the same circuit. It's just sort of in a different usage um configuration here.

**Dave Jones:** So, we've added another stage here to this so we can multiply our 3-V DC up to 9-V DC. Beauty. How does it work? Exactly the same uh configuration. Imagine this, that is still our same circuit as before, okay? Uh but, we've

**Dave Jones:** now got a 6-V DC reference here, point up here instead of a 3-V DC reference point here. So, we've just shifted that waveform up again. I won't go through all the details. It's the same as I explained in the Cockcroft-Walton

**Dave Jones:** voltage multiplier video. So, that 3 volts peak-to-peak from our microcontroller here, and it will be 3 volts peak-to-peak, of course, from a CMOS microcontroller, then it just shifts it from 6 up to 9. So, 0.3 here, the green waveform, is exactly the same,

**Dave Jones:** it's just shift shifted it up. This point This point here gets shifted up again, and then we've got 9 volts, and then we've got our final rectifier on the output, which gives us 9 volts DC on the output. But, of course, once you

**Dave Jones:** put a load on, it's going to sag like that, but uh there you go. Then, we could certainly whack in our 5-volt voltage regulator and have heaps of margin. You wouldn't even need a low dropout type. Beauty. And in case you're wondering, yes, this

**Dave Jones:** is the new Teespring crowdfunded triple 5 timer t-shirt. If you missed out on it, uh well, I might run another one soon. We'll see. But, top quality. I love it. And next up, we have Dave, looking trendy and smart in a nice little

**Dave Jones:** Teespring number. He looks equally at home in the dumpster as he does on the workbench. And to the breadboard we go. Deja vu, folks, we've been here before. Nothing new at all. It's exactly what we looked at the other week. But, we'll go through

**Dave Jones:** the motions again. Here it is, Dave Cadbury. We've got our 3-volt DC supply, which will come from our bench supply. We've got 3 volts DC coming from the function gen, and yes, it's shifted up to 1.5 volts, so it's

**Dave Jones:** not AC, so it's 0 to 3 volts, so it simulates our the signal coming from our microcontroller. And then we have our multi-stage doubler. There's our first stage there, and there's our second stage there. And we should get 9 volts

**Dave Jones:** out of here. And these are the um the on this oscilloscope, channel 1, channel two, channel three, channel four. And it's exactly the same as what we had last time as well on the scope screen. All four channels are ground referenced

**Dave Jones:** down here on that bottom graticule down there, 2 V per division on all the channels there, and we've got our peak voltage of each of the channels. So, let's have a look. Here on the circuit, our point one here is actually There it

**Dave Jones:** is, 6 V. Uh so, we've got our 3 V input. By the way, our square wave amplitude there is 3 V. I haven't shown the square wave actually coming in because it's exactly the same as that. And it's 6 V,

**Dave Jones:** and then the top of point two here, notice that we've got our diode loss between there and there, but with no load at the moment, so it's it's very small. And then the top of the next point, channel three up here, 8.2 V, and

**Dave Jones:** that's actually the uh blue waveform up there. So, point three is the blue waveform. Sorry. Point one is the yellow waveform there. Point two is the green waveform there, which is your DC value across there, and because that AC signal

**Dave Jones:** gets converted into DC, that's our 6 V DC reference, and then it gets pumped up again, shifted up by the blue waveform there, channel three, up to Well, in this case, 8.1 V peak, and then our final DC output is the purple one there.

**Dave Jones:** And bingo, 8.1 V. And what happens if I shift my 3 V signal here? Well, let's adjust our bench supply. There we go. As we move it up and down, all the waveforms Oh, we just lost our trigger

**Dave Jones:** there. Of course, once we get to that point, but we can boost that up there, and there you go. It just shifts that waveform up and down. So, with precisely 3 V DC input and our 3 V peak-to-peak square wave, which we can

**Dave Jones:** generate with a microcontroller, we can get a final output voltage here of 8 V. There it is. And this is using just bog standard 1N914 or 4148 diodes, not even the Schottky type. Now, let's have a look what

**Dave Jones:** happens if we put a lousy little 10-k load on this thing. So, our final output DC voltage of 8 V here divided by 10 k, assuming it stays at 8 V of course, divided by 10 k, 800 microamps. So,

**Dave Jones:** we're drawing less than a milliamp. Here we go. Let's connect it up. And bingo, look. You'll see it drop. And you'll notice that I can probably boost all the channels up like that. You can notice the ripple starting to appear on

**Dave Jones:** channel two there, which is our second point, which is our supposedly our DC reference in there. It was a straight line before, but now you can see the ripple in there due to the fact that we're drawing a 10-k load. And by the

**Dave Jones:** way, I didn't put values on here. These are actually 0.47 microfarad. And let's drop that load by an order of magnitude from 10 k down to 1 k. Here we go. There we go. Look at that. So, look, it's practically useless now. 3.2

**Dave Jones:** V top value of our final output. As you can see, it's absolutely useless when we try and power a 1-k load there. Our 3-V, we're still getting our 3-V both of our 3-V signals going in, but it's just it

**Dave Jones:** doesn't work anymore. It's useless. And we'll bump that up to 2 k. And as you can see, significantly improved there. There we go. And 3 k, 4 k, 5 k. And you can see the progression in that. But of course,

**Dave Jones:** we're not using Schottky diodes here. In practice, you'd almost always use a Schottky diode in this configuration unless you had really low current and you really didn't care. Generally, you're not going to use your little jelly bean 1N 4148s. You're going to use

**Dave Jones:** some sort of Schottky diode. They're, you know, practically the same price anyway. So, let's assume that we just had the single stage configuration here like this and here's our final output voltage, 4.62 V at This is a 10k load, half a microfarad

**Dave Jones:** cap on there. And by the way, frequency is 10 kHz here, a typical frequency that you might get out typical PWM frequency you might get out of your microcontroller, for example. And we're only getting a DC output voltage of 4.62

**Dave Jones:** V there, but that's probably going to be good enough. Only talking like So, you know, 4.62 V / 10k. So, we're only talking half a milliamp. Some LCDs can go down that low, but not all of them, but you know, potentially, we could

**Dave Jones:** actually, you know, almost power one of those little LCD modules because they are fairly tolerant of the supply voltage. We'd be able to power it with just a single stage circuit with even crappy, you know, 4148 diodes in there and a low

**Dave Jones:** value of capacitance. So, what happens if we replace this cap, half a microfarad, with say 47 microfarads? Fairly big step up in value. Well, let's do that. I'm going to rip that out there and I'm going to stick in a

**Dave Jones:** 470 microfarad cap. Aha, look at that. We now jumped up to about 4.8 V or thereabouts. So, what's our frequency going to do? Well, of course, it's going to change the discharge curve of this cap. So, of course, this is still our 47

**Dave Jones:** microfarads in here, but our second stage one up there, you'll be able to you can just see the ripple on there at the moment, but let's increase the frequency, shall we? So, here we go. Oh, well well, we can drop well we we

**Dave Jones:** can increase it, of course, and of course, we just get better, you know, there's you can't see any ripple on there now, but if we lower that frequency down significantly, aha, look at that. You can start seeing 4 kHz,

**Dave Jones:** three, you can start seeing the ripple appearing and the droop there. If we go down to 1 kHz, you know, ah, pretty bad. So, you don't want to be operating these things at 1 kHz. 10 kHz, reasonably good rule of thumb. Now, what

**Dave Jones:** happens if we change all of these caps to 47 microfarads, pretty beefy value. Bingo, here it is. This is with our 1K load. And the amazing thing is, that's still at 1 kHz, as you can see. So, it

**Dave Jones:** is possible to use a value like that, but uh you have a frequency like that, but you have to go um uh much higher in your capacitor's values, and that's with a 1K load. So, um our There we go. We're drawing 6

**Dave Jones:** milliamps from this circuit, just over 6 volts on our second stage output there. So, 6 milliamps this thing is taking with even 1N4148 diodes, but of course, that is a uh two-stage one to get our 6 volts. So,

**Dave Jones:** we're getting nothing near our 9 volts we expect, but uh good enough. But even that single-stage one, 4.7 volts there, is enough to drive, like you know, four or five milliamps, even at 1 kHz. Not a problem. And because there's no ripple,

**Dave Jones:** we're not going to actually see any uh benefit there by going up in frequency, as you can see. Frequency is only going to matter once you start drooping. And if we take our frequency down 81 Hz, look at that. Because we're

**Dave Jones:** using such large value caps, our switching frequency can actually be relatively low, you know, in the order of 100 Hz or so. And we're still going to get a good enough DC voltage out that we could use to power an LCD or

**Dave Jones:** something else perhaps, especially if we decide to put an extra linear regulator after that. But of course, generally speaking, you know, you're not going to be using 47 mic caps in there for example. They're just more expensive, you know,

**Dave Jones:** and they're larger and you know, you're going to use little ceramics that you've already got in the circuit. Typically, you know, if you're doing an SMD design, you might have 1 micro Farad caps in there for example might be very typical

**Dave Jones:** or something like that. All the 470 ends that I was using before, 0.47 micro Farads. And as you can see here, we couldn't get the several milliamps out of there even at the higher frequencies. So as you can see, it's all going to be

**Dave Jones:** a trade-off here of the value of the capacitance versus your load versus your diode the type of diode you got, the diode drops. I won't go into putting Schottky's in there as well. If we put Schottky's in there, we'll find that

**Dave Jones:** these waveforms will all be shifted up or have lower diode losses and stuff like that. So, you know, by all means build this thing up and experiment with it and it's a great circuit to use next time you need a simple voltage doubler

**Dave Jones:** or to get, you know, a higher value rail out of your project that's powered from a couple of batteries or something like that. You don't have to re-engineer your battery solution. You can just use one of these doublers or in

**Dave Jones:** this case, a tripler. Now let's look at a practical configuration of this. In this case, it's my microwatch project. Here it is. Here's the schematic for it. You can download it from my microwatch website if you really want to, but it's

**Dave Jones:** a microcontroller. Well, here's the actual thing powered from a single CR2032 battery here. Let's switch it on. It's in power saving mode at the moment. Haven't set the time or anything like that, but there you go. It's the world's

**Dave Jones:** only do-it-yourself scientific calculator watch. Now, uh, the interesting thing about this is that I've used Well, there's two interesting things. One's One is that I've used two Dickson doublers here. Might look a bit unusual, but trust me, I've got one for

**Dave Jones:** the LCD here that powers the 5-V LCD. It's not a 3.3-V one or 3-V one, so it, uh, needs 5-V, so I've got a Dickson doubler in there. And I've got another one for the LED backlight as well. I

**Dave Jones:** think it had like, uh, two LEDs in series. That's why I had to actually, uh, do that this particular module. Anyway, so I've got two Dickson doublers in there. The configuration is basically exactly like this. Of course, we've got

**Dave Jones:** a fixed DC voltage here, in this case 3 V from the battery. We've got our, uh, 3-V, uh, square wave coming from our PIC microcontroller in there. But in this case, of course, we're only using a single-stage doubler here, so ignore the

**Dave Jones:** rest of that. There we go. That's basically what we've got here. Now, it might look a bit unusual in that Well, why aren't these diodes here going to 3 V like this? Why are they going to a pin on the microcontroller? Aha, that's

**Dave Jones:** actually a feature. It allows the microcontroller to actually switch the output off and on under software control. So, if the output here, instead of tying this to 3 V, you tie it to a pin on the microcontroller, when that's

**Dave Jones:** high, 3 V, you apply your PWM signal, uh, well, in there, then it switches your LCD voltage on or whatever it else you want to power. If you set that low and switch off your PWM signal, bingo, your output voltage goes down to zero.

**Dave Jones:** And I can do that for both the LCD backlight and voltage on the LCD. And in this case, I've got, uh, a Schottky, of course, a standard bat 54, really a jelly bean um stuff in there, super cheap SM standard SMD type. I've got

**Dave Jones:** only a lousy 100 in in there, and I've got 10 micro farads there. On the output I actually forget what value I'm switching it at. I don't know. It's a, you know, 5 kHz or something like that, 10 kHz. Don't exactly remember, but so

**Dave Jones:** there you go. There's a real world example of uh two different reasons why you want to use it, the LCD and the back light. Uh, of course, because I was forced to use this LCD, 53 by 20 mm, and it had a

**Dave Jones:** certain type of back light, and it had to be a certain type. I couldn't use anything else. Couldn't just start substitute it for anything. So, really, um you know, I had to do this. This was my only choice apart from using a like a

**Dave Jones:** as I said before, like a 7460 uh voltage uh doubler uh charge pump voltage doubler or something like that. Eh, it's more expensive, so I just decided to go with the diode and capacitor solution. Piece of cake. And then I

**Dave Jones:** added in the bonus feature of being able to switch off the LCD, as you've seen. It goes into a power down mode that actually disables the uh voltage to the LCD, so it doesn't uh draw any current at all, and this thing can actually get

**Dave Jones:** a reasonably long battery life cuz it's only powering the microcontroller. The LCD I can completely switch off. And of course, the back light voltage, I can switch that off and on. There it is. It's gone into low power state. It's

**Dave Jones:** only drawing, you know, microamps instead of, you know, a milliamp or two. And you switch it on, draws a couple of milliamps, operates for a few minutes, then auto switches off. Real world practical example of a tricked up, I

**Dave Jones:** guess, uh Dickson doubler here with on off capability. So, there you go. I hope you enjoyed that follow up to the Cockcroft-Walton voltage multiplier. This is the Dickson doubler or uh charge pump doubler, diode doubler, whatever you want to call it. It's an interesting

**Dave Jones:** little and useful little building block circuit. And remember, if you like our Fundamentals Friday, please give it a big thumbs up. Dual thumbs up. And if you want to discuss it, jump on over to the EEVblog forum. Catch you next time.

**Dave Jones:** Gentlemen, I wouldn't trust this overgrown pile of microchips any further than I could throw it.
