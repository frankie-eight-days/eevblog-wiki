---
video_id: g94mpom2Ahs
title: EEVblog #314 - Korad KA3005P PSU Teardown
url: https://www.youtube.com/watch?v=g94mpom2Ahs
source: youtube-asr
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. We've got a power supply for you. It's a Korad. I hadn't heard of Korad before either. So, no surprises, but apparently they've been around for a quite some time and they make some high-end

**Dave Jones:** specialized power supplies, but this is one of their bottom of the range low-end programmable ones. It's the KA3005P 30 V 5 A programmable power supply and uh it's really cheap. So, I don't know. When they're really cheap like this, you got to wonder what's

**Dave Jones:** inside of them. So, let's take a look. And thanks to Charles at Trio Smart Power, who are the Australian distributors for this thing. They just got it in. It's new. They loaned me one, so we're going to take a quick look at

**Dave Jones:** it. You know what we say here on the EEVblog, don't turn it on, take it apart. And we'll have a quick peruse of the outside here. It's a single output supply, of course, 30 V 5 A. It's got uh programmable memories.

**Dave Jones:** It's got uh it's a floating output, of course, plus your uh ground terminal here. It's got your optical encoder knob here, voltage current control, overvoltage, overcurrent protection, output on-off switch, lock-in, um memory recalls, various uh status indicator LEDs, and separate voltage and

**Dave Jones:** current readout displays. It's got everything happening. And uh you it you can tell it's a linear supply uh by the weight of it, trust me. And there's a big uh whopping transformer in there. You can probably see the uh

**Dave Jones:** yellow tape around the core. Let's have a look at the back here. We've got um standard IEC mains input connector. It's only uh 220 / 240 V. There is no selection switch. There might be one inside or there might be a transformer

**Dave Jones:** tap or something like that, but certainly uh it's uh not going to work off the bat with 110 volts as you'd expect with a linear supply. It needs those transformer taps and we've got presumably RS232 serial and USB

**Dave Jones:** interface. So, there it is and we've got a fan as well and that's about it. So, let's crack this thing open. Few screws on the side. It's a you know, a reasonably thick metal chassis. It feels you know,

**Dave Jones:** it certainly doesn't uh feel cheap and tinny like some of the others I've looked at. So, uh let's try and get these screws out and see what we've got.

**Dave Jones:** All right, I'm not expecting a a huge amount inside this. I'm expecting a large amount of empty space, a big transformer, maybe a board here and a board over here and uh that's about it. There'll be control board, maybe uh the

**Dave Jones:** power board and there'll probably be a display board as well. So, let's get this thing off. And ta-da! And let's look at the chassis first. Of course, it's your traditional just your bent folded metal frame like this. They've just you know, folded at

**Dave Jones:** the sides and then pinched it and fold the edges fold over and they got these support bars on the top like this and rather interestingly, they've got another um plate across here which doesn't really seem to do anything in terms of

**Dave Jones:** you know, maybe you know, electrically sort of you know, a bit of shielding perhaps from the rear side to the front but gee, I don't know. It's more like it's a more like it's a you know, a cross brace

**Dave Jones:** support really or basically a dual function there but as it stands, the thing does, you know, it's reasonably rigid, I guess, for a for a folded metal case like this. So, it's not too bad. And at first glance, it's a nice and

**Dave Jones:** neat and tidy. I guess the only thing I'm going to really complain about here is that this stiffener bar up the top goes into a plastic surround. It doesn't go into like the you know, a a metal part of the folded front panel. So, it's

**Dave Jones:** not a complete metal frame, just plastic, but you know, it it feels solid enough though. So, I don't think too many problems. And if my eyes don't deceive me, this top bar here actually slopes down. This is not

**Dave Jones:** square. It may not I may not be able to capture that with the wide-angle lens, so I'll go back here and see if I can zoom in like that. And this seems like it should have been mounted flush or on top of this plastic

**Dave Jones:** support here. It's just not not square. It just looks funny. And I don't know what's going on there. I think they really kind of goofed, sort of rushed the design of the case there and sort of goofed and went, "Whoops, we'll have to

**Dave Jones:** sort of mount it on the bottom side of this plastic standoff." Weird. And let's have a look at the mains wiring here. We've got our fused IEC mains connector over here. It's solidly connected down to the case there

**Dave Jones:** with a uh like a standoff on the case, but there's no shake-proof washer on that that I can see, but it's certainly is very tightly done up. It's all heat shrunk. And there is no 120-V tap on this thing. In fact, it's

**Dave Jones:** up marked 240 230 V 5 A. So, it looks like, um, yeah, just be careful where you buy this thing from. It is not switched at all. And of course, we've got, uh, a real power switch, clunking power switch on the

**Dave Jones:** front, which actually switches in the, uh, mains primary like that. And, uh, it, you know, it's all, uh, neat and tidy. It's all heat shrunk. I like it. But for holding down the transformer onto the base there, it does look like it uses

**Dave Jones:** some form of, uh, shake-proof washer under there. So, thumbs up to that. Now, system design-wise, basically it's got a separate, um, USB, uh, control board down there. We'll take a closer look at all these boards in a minute. But a

**Dave Jones:** separate USB, uh, control interface, which then goes over via this cable in up here, up, it's cable tied up here, and goes over to a, uh, some sort of, uh, processor and, uh, display, uh, type board. There's the display, the actual

**Dave Jones:** seven-segment display board is on the front. Then there's another processor board here, which would be the, uh, digital control. And that's probably like a serial, uh, interface over to there. So, it maybe that's just a, uh, the USB board is just a, you know, USB

**Dave Jones:** to, uh, RS-232, uh, serial. And, uh, then we've got a separate, uh, power board over here with a separate heat sink on the back, bolted onto the fan, which, um, I don't think I've seen that particular, uh, construction before. But it's actually

**Dave Jones:** quite clever. And we'll take a better look at that, uh, in detail. We've got a separate little board down there on the front panel, binding posts. So, let's take a look at each board in detail. Now, just interestingly here, uh, just

**Dave Jones:** above the processor board, they've got a cutout for a big, uh, D25, by the looks of it. So, they didn't, uh, go ahead with that. Um, they've gone for the D9, uh, plus the USB. Now, this is interesting. On the USB

**Dave Jones:** board here, you'll note this big whopping earth wire here. Huge, uh, you know, mains rated, uh, cable. So, we're talking, you know, 10 amp rated cable soldered directly onto the top case of the USB connector going down to a

**Dave Jones:** chassis, um, standoff down in there. And of course, which of course, uh, goes through the chassis and over to the back to the, uh, mains IC input connector. So, that means, most definitely, the, uh, USB connector is very well and

**Dave Jones:** truly, uh, mains earth connected. Why have they done that? So that you don't have any issues with connecting this to mains, uh, with to your PC, which will also be mains earth referenced. And you can see some optocouplers on here. So, this is

**Dave Jones:** actually an opto, um, isolated, uh, USB/RS232 interface. Brilliant. So, it's mains earth on the USB and the serial side, presumably, but, uh, it's not but then it's isolated, which goes over to the main connectors. Brilliant. They've done this properly. I like it. And of course,

**Dave Jones:** to power this board, you could, uh, of course, uh, power it from the 5 volt, uh, USB. But if you're just using the RS232 there, then, you know, you're not going to you have to get, uh, power to

**Dave Jones:** the board. So, they've got a separate, uh, tap on the transformer here with a Look what looks like, um, there's a round device in there, which is, uh, most probably some sort of, uh, MOV, uh, I would, uh, guess. And that's, uh,

**Dave Jones:** and that's powering the board. You can see the bridge rectifier in there and, uh, some large filter caps as well. No, I think I'm going to revise my estimate on that one. I think it's, uh, some sort of choke. You can feel the

**Dave Jones:** windings in there around a, uh, around a little toroid or something like that. So, they've yeah, they've decided that they need that in line with the output of the transformer tap. And here's the USB board in some detail.

**Dave Jones:** And of course, the first thing you notice is that the bastards have scratched the number off the chip. Give me a break. Idiots, why bother? It's just ridiculous. It really is. Anyway, a couple of 4N25 optocouplers there. There's the

**Dave Jones:** bridge rectifier. We've got two filter caps, which are ZH brand. Never heard of them. But they are 105 rated. And a couple of little power devices there. Probably some sort of regulator there, U1. And another power D-pack up there.

**Dave Jones:** Crystal, which isn't isn't glued down at all. And a another 32 kHz or presumably 32 kHz watch crystal also just floating in mid-air there. That's That's not good. I don't like that at all. That's a bit of a

**Dave Jones:** fail. They should stick that one down properly. But you can see the big earth connection to the USB. And apart from that, there's you know, it's pretty mediocre. They've got a budge cap on the input there. That's a 470

**Dave Jones:** nanofarad 100 volt job. And yeah, there's not much else doing there. So, let's get a bit of spit, put it on that, see if we can Yeah, well and surely rub that off, I think. Yeah, I'm not seeing

**Dave Jones:** anything there that's uh that's familiar. So, your guess is as good as mine. Now, let's take a look at the power board here, how it's actually mounted. And as I said, I rather like this. It's um you know, it's there's the power

**Dave Jones:** devices down in there, presumably the uh power transistors. And they're mounted directly onto that heat sink, and then the board's mounted onto that, directly mounted onto the back of the fan. It's a rather efficient um kind of arrangement. I really like it.

**Dave Jones:** You can see all the uh all the heat sink compound all smeared down in there behind the devices, but that's that's really quite neat. And of course, that should uh keep most of the heat away from the main

**Dave Jones:** filter cap here. It should you know, it it it should be a reasonably efficient system to actually remove the heat directly from that heat sink. And the main filter cap's a 63-V 6800 microfarad. Um it's got a vent, of

**Dave Jones:** course, big vent written on there, but uh I don't recognize that uh brand. So, um I'm not going to bother to go look it up. I you know, it's only 85° C rated, not that terrific. Um is held down with

**Dave Jones:** some uh hot snot here, some hot melt glue. Um So, they've at least uh done that job. Uh the uh the connector here, more hot snot. There's generally uh the power supply uh uh companies love to use hot snot. They just fill, you know,

**Dave Jones:** they just apply it everywhere inside these supplies. So, it's not uncommon when you open them to get maybe maybe you can see it there, just a little leftover sort of strands of hot snot all over the all over the unit. This

**Dave Jones:** one's uh not too bad. I've pulled out a couple of little uh stringies in there, but not too much at all. Now, as for the uh system architecture in terms of the, uh, power cabling, of course, we've got our main taps out of

**Dave Jones:** the transformer here, and they go down into the power board down in the bottom here, and then the output, uh, from the power board, there's a couple of relays on there, we'll take a look at that. Output from

**Dave Jones:** the power board goes directly into this main board, which we'll also take a look at, which is, uh, clearly the control board, and then it jumps on over, it goes, uh, through this, uh, current shunt here, through to an output here,

**Dave Jones:** which then goes, jumps down to the output binding post there. So, that is the, uh, that is the power part, the main power path in this design. Now, offhand, I don't know what these, uh, connectors are rated at, but, you know,

**Dave Jones:** 5 amps, uh, you know, they they they could have done better. It's probably just, uh, barely adequate for the task or the power wiring in here, uh, stuff like that, you know. But, I guess you're sort of limited in this, uh, compact,

**Dave Jones:** um, thin form factor like this to to exactly how you can, uh, lay out the board and stuff like that. Maybe if they use move the transformer to the back, but then the weight's not centered nicely. They've put it in the center, so

**Dave Jones:** it's all nicely weighted, but if you had the power board directly up near the binding, you know, sitting on the bottom directly near the binding post, that may have been better, and then you could have avoided, um, you know, having to do

**Dave Jones:** all of this wiring, jumping over to this processor board, and then down to there, but ah, well, that's the way they decided to do it. Now, as is, uh, par for the course with these, uh, type of, uh, 30 V linear uh,

**Dave Jones:** supplies, they've got multiple, uh, taps from the transformer here. They've got three different, uh, taps, and they've got, uh, two relays here, and, uh, they switch in the taps when you get to a certain uh, voltage to reduce the power

**Dave Jones:** dissipation in the heatsink cuz because this isn't, you know, a very big heatsink in the scheme of things for a 30 V 5 amp power supply. So, they need the software needs to know exactly when to switch those things in. So, as you

**Dave Jones:** turn the optical encoder knob and I get to a certain voltage, you'll hear those relays clicking in and out. And if we take a look over here, clearly the heatsink contains a bridge rectifier there. You can see the see the symbol there. So,

**Dave Jones:** that's mounted on the bottom of the board and then that's mounted up under there, wedged between the heatsink and the board. And then you've got your couple of power transistors there down in here. Like that. There they are. I'm probably

**Dave Jones:** not going to take this board out. I'm not going to bother. I'm not that interested to find out exactly what those power transistors are. Not very interesting. And a free standing TO-220 device here. Not a big fan of those. I'd rather it be strapped

**Dave Jones:** down, but get that all the time. Now, taking out the main control panel PCB here. We'll take a look at the front side components. There's two board-to-board headers here. Why they've got a male and female there, I don't quite know, but

**Dave Jones:** this bottom part is rather interesting and deserves some looking at. And if you take a look at this, this is clearly the power part where I showed before how the power comes in here. And oh, sorry, it comes

**Dave Jones:** in here and goes out over here down to the front panel binding post. So, this comes from the power board input and down there. And you can see note the tinning on the traces through the solder mask there. They've deliberately left off

**Dave Jones:** some solder mask and they've put tin in there. presumably to increase the current handling capacity of the traces because there's you know there's two ways to increase the current handling on a PCB. One is to use well, three ways. One is to use wider

**Dave Jones:** copper traces of course, but you've only got you know you've only got so much room in here. They can only be so thick. Another is to increase the copper thickness. A standard board might be 1 oz, but you might go for say 2 oz or

**Dave Jones:** even more thick copper, but that costs money. You know copper's expensive. They want to keep the cost down. So, a third option is to just start tin it cuz they've got to solder they've got to wave solder this thing anyway, so why

**Dave Jones:** not leave some solder mask off, apply the tin in there, and that effectively is a cheap way to get yourself extra current handling on your traces there, and that's clearly what they've done. Um it's all a bit it's all a bit dodgy

**Dave Jones:** around here, but all these holes you notice all these slots here. These are uh presumably um they look like sort of you know high voltage uh isolation slots, but look at you know why go to all this trouble when you got

**Dave Jones:** these tiny little traces snaking through to here. That's going off to a connector somewhere. I'm not actually sure what it's doing. At first glance I've got a whole bunch of Are these holes around here for uh for air flow over the heat

**Dave Jones:** sink? The heat sink's on the other side of that board. So, they've got some heat flow there, and you know that looks like it's a high voltage isolation slot, that one as well, but yeah, once again I don't quite understand it when the trace

**Dave Jones:** is up there right next to I don't know. Weird. Maybe it's all just you know air flow. And if we have a look at the main board here, as I said uh power comes in here from the power board. We've got our

**Dave Jones:** current shunt here, which is you know just a dodgy coiled uh bit of current sense wire. There's a diode down there, couple of filter caps, and power just comes out here to the front panel. Binding post, and then we've got a uh

**Dave Jones:** power device in there. We'll take a look at that. That's a 7812. So, that's just a 12-V voltage regulator on a tiny little heat sink. We've got a buzzer, another couple of power devices down in there, SOT223s, one of my favorite

**Dave Jones:** packages. And one interesting feature which we'll take a look at is a whole bunch of 74HC595s with all these resistors here. And it's rather curious because there's not enough output connections for all of these resistors. We'll take a

**Dave Jones:** look at that. Another processor. Idiots, they've rubbed the number off again. Another device down here, they've rubbed the number off. Ah, nuts. Anyway, that's clearly some, you know, some sort of microcontroller, some little 8-bit microcontroller, probably. Nothing fancy at all. Probably a few

**Dave Jones:** comparators over here. Let's take a closer look. And we've got three TL082s there, little bit of a budge solder bridge there. I think that's done on purpose. Otherwise, it most likely wouldn't work. And the odd component left off there,

**Dave Jones:** but that's probably something to do with, you know, the overvoltage overcurrent protection uh stuff. And they're too cheap to fit a zero ohm resistor there, so yeah, just bridge it out. And this one's a real hoot. Take a look

**Dave Jones:** at C14 there. That's the weirdest capacitor I've ever seen. Is that 1 K farads? Microfarads? Picofarads? Puff? What is it? And then we have a classic ULN2003 Darlington driver. And there's an Atmel 74HC564 E squared external E squared prom there.

**Dave Jones:** So, uh whatever microcontroller they're using, um obviously, doesn't have any uh built-in E squared prom because, you know, this thing doesn't need to hold a whole lot unless it's uh doing uh data logging which then uploads to the PC, but I didn't think it did

**Dave Jones:** that. I thought it would uh just uh upload data in real time, but yeah, they scratched the bloody numbers off again, [ __ ] Now, this resistor network here with the 74HC595s, this is one of the most unexpected

**Dave Jones:** things in here and it looks all the world like it's a pro it this is the DAC. It's a programmable resistor ladder DAC of some description. I could go through and, you know, uh actually uh reverse engineer it and

**Dave Jones:** figure out exactly what they're doing there, but I believe that's what it is. Go figure. I guess uh three 74HC595s and a whole bunch of resistors is cheaper than a real DAC. And behind the main uh processor board here is a

**Dave Jones:** single-sided board. See a couple of jumper links here. That's for the soft buttons uh on the front. And they've gone to a bit of trouble to do the optical rotary uh encoder over here on its own little board on its own little

**Dave Jones:** uh standoffs which then goes through this header onto the uh soft button board which then goes through this header back to the main processor board. Go figure. And the processor board is actually straddling uh the display board as well. So,

**Dave Jones:** there's the other header up here which plugs into the display board and then this header down here which plugs into the um soft button rotary encoder board. So, that's a, you know, uh they've gone to a bit of uh trouble there to make sure all

**Dave Jones:** that stuff lines up across all these different boards. And we've got a budge wire there. Oops. And down on the binding post board, there's not much doing here. You can see the 1 kV caps connecting earth through to the

**Dave Jones:** negative output there. Standard practice. They've got shake-proof washers on the nuts and behind the nuts for the binding post there. Nice. They've only got a small amount of output capacitance because on a on a constant current power supply, of

**Dave Jones:** course, you don't want a massive amount of output capacitance because then that energy can be dumped into your circuit when you don't want it to be. And then we've got the the main inputs out here, of course, coming from the output of the

**Dave Jones:** current sense resistor on the processor board. And then it looks like they've got a another little sense cable which senses the voltage directly at the output terminals. Nice. So, there you have it. The Korad KA3005P programmable DC power supply. Eh, what

**Dave Jones:** can you say? It's a cheap Chinese power supply and it's I guess you can say it's not bad for the cost. It's pretty much what you'd expect, par for the course, but the cleanliness of the PCB and the

**Dave Jones:** solder joints leaves a lot to be desired. Doesn't instill a lot of confidence, quite frankly, but for the money, eh, it's not too bad. What do you expect? But anyway, if you want to discuss it, jump on over to the EVblog

**Dave Jones:** forum. And if you like teardown Tuesday, please give it a big thumbs up cuz that helps a lot. Catch you next time.
