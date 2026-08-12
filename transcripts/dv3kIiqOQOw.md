---
video_id: dv3kIiqOQOw
title: EEVblog 1693 - Uni-T UTE310 Power Meter Teardown & Practical Demo
url: https://www.youtube.com/watch?v=dv3kIiqOQOw
source: youtube-asr
---

**Dave Jones:** Hi, today we've got an interesting teardown of the Uni-T UT210 digital power meter. And this is not a bit of kit every lab is going to have, but if you're looking at doing product power measurements, then a digital power

**Dave Jones:** meter can be really handy. Yes, you can do it with your, you know, a couple of multimeters. Of course, you've got to have at least two multimeters in your lab, one for measuring voltage, one for measuring current, and then you can

**Dave Jones:** calculate the power, etc. But, to get a measurement of energy over the time, you've got to like accumulate. You've got to like integrate that. And you can can do all sorts of other energy measurements as well. And uh I'll link

**Dave Jones:** it in if you haven't seen it, but a long, long time ago in a blog far, far away, I did a teardown of the Voltech PM 300, which I've been using up until now. But, it's a really old design, but still

**Dave Jones:** a very interesting teardown. And that was quite crude, and you've seen that in a lot of videos where I like might measure sort of like mains power consumption or something like that. Um but, this thing can do a lot more than

**Dave Jones:** that. Um it's 600 V 20 A capable, so yes, I can easily do uh like, you know, energy measurements of mains power equipment, but it also has low current ranges down to like 5 mA maximum current range. So, can do really do low power

**Dave Jones:** stuff. And I might give you a demo of that at the end of this after we do the teardown. But, thank you very much, Uni-T, for sending this in. It's a real interesting and very incredibly useful bit of kit. And it's about 1,600

**Dave Jones:** uh Yankee bucks or something like that. Anyway, um prices could vary depending on where you are, but that's actually a bargain for a a comprehensive digital power meter like this. And you can see on the back here, we've got the big

**Dave Jones:** current terminals cuz this thing can do 20 A, so we've got massive terminals. And then you got the voltage sense terminals. We've got IO as well, so you can automate it into production testing. We've got RS232 and GPIB. We've got the ethernet, and

**Dave Jones:** we've got the USBs, and the whatnots, and it looks like we've got um an external uh triggery thing here, too. So, you know what we say here on the EV blog, don't turn it on, take it apart. So, as I mentioned, this can do uh

**Dave Jones:** integral uh energy measurement, but you can also do THD analysis, and uh all sorts of weird and wonderful things. I don't know if I had to take off the rubber baby buggy bumpers there. No, probably not. Uh And it's got a sampling

**Dave Jones:** rate of 1 MHz, which is really quick for this sort of uh you know, uh high resolution, high accuracy thing. Um hence why it's, you know, it's Some people might think it's it's reasonably expensive, but uh not for the capability

**Dave Jones:** that you actually get in this thing. Ooh, is that going to slide off? So, if you want to know the power consumption, the battery life of your new uh product, then something like this is I the tool you're going to use to

**Dave Jones:** measure that, rather than just guessing. And of course, uh you know, if your product changes into different modes and stuff like that, then uh yeah, this thing is going to help you uh do that, you know, analyze that. And you can uh

**Dave Jones:** get waveform uh measurements, as well. But, I haven't used the software on this thing, so I'm not sure what we can get out. But, look at that. That's a Bobby Dazzler. That's clean as a whistle. That's beautiful. Look at this one main

**Dave Jones:** one large main board directly in the center of like it's literally in the center like this. What's on the bottom? Oh, look at that. So, there's actually quite a lot of space inside this thing. Wow, look at that. Um unfortunately,

**Dave Jones:** some of the cans are soldered down, so um yeah, but interestingly, look at that up there. These are our input connections, which go directly over a giant cutout here. They're really serious about the layout of this thing. Wow, this is really something else.

**Dave Jones:** Well, brutal is probably the word I'd use to describe that input diode clamping up in there. This is the two current terminals here and the two back-to-back diodes. Look at those beasts. No fusing rubbish in there, so you're guaranteed not to get more than

**Dave Jones:** half a volt burden voltage across your current shunt resistor there. And they're of course coupled directly into these two relays here. This is basically your current switching, you know, when you're in the saw on the front panel, you tell it to, you know, switch on the

**Dave Jones:** load or whatever, clunk, the relays switch on and yeah, you're connecting those rear terminals through to no doubt the current shunt resistors under here. And they're going to be pretty schmick. And the voltage sense terminals on there, they go into these wires directly

**Dave Jones:** over to here and and they run across here after nice big ferrite clamp on there into this shielded um voltage amplifier here. So, this would be your multi-gain ADC and like an input amplifier as well. And that would be doing all your voltage

**Dave Jones:** ranging, but unfortunately we can't see that unless we desolder the thing. Oh, I didn't want to have to do that. And they've got isolation slots just everywhere. Look at this, right? I don't know why they've actually put that giant

**Dave Jones:** isolation slot in there. I because really, this is all really low impedance um stuff. You don't have to worry about any you know, leakage, creepage, anything like that. But you can see all this custom metal work here is just very

**Dave Jones:** impressive way to get to shunt. I'm here all week to carry the current from the relays over to the input resistors over here. And I've got a little board there. That's interesting. That's just like a four That's just like a vertical

**Dave Jones:** connection board, um which actually connects to whatever's um under that heat sink. So, you have your uh current sense amplifiers or shunt amplifiers are under here. And you can see right up there, there's a missing chippy. That'd be your uh GPIB there, and then you've

**Dave Jones:** got your pins for your uh right angle GPIB connector, which would poke out the back. But, we've got the RS232 option in this jobby. Um and yeah, that just goes straight into that little header there. And then we've got a whole

**Dave Jones:** bunch of digital isolation from basically uh the measurement um half of this thing over to the uh processing half of this thing. Arctic-7 uh FPGA there for those playing along at home. And uh nice isolation slots in here.

**Dave Jones:** Beautiful. They haven't put the um isolation uh capacitor across there. They um Yeah, it's part of the design, but they went "Nope, we don't need that." for whatever reason. I don't know. More isolation happening up here with your little uh switching converter.

**Dave Jones:** There's an isolation slot under there. They've got another one under here. And up Yeah, somebody's really had fun with this board. They really know what they're doing. It's very very nice. And power supply-wise, you don't need much uh to power a board like this because,

**Dave Jones:** well, there's nothing really happening here. It's just, you know, measurement of a 1 MHz high-resolution ADC and um some, you know, high-precision shunts and switching and gain switching and stuff like that. And that's And Bob's your uncle. Um so, yeah, we only need, I

**Dave Jones:** don't know, you know, 5 10 W uh coming in here. It's not uh much of a uh power supply at all. That'll just be um some third-party one. We could have a look at that if you're really interested. But,

**Dave Jones:** just measuring the power supply current there, it's about 580 600 milliamps, something like that at whatever voltage is coming out. 12 V. That's what I thought. So, my initial guess was about right. Yeah, that's like a 7 W power

**Dave Jones:** supply. Like, it's really low. Uh one big uh just digital IO going over to all the main front panel uh processing, which handles all the graphics and everything else. That'll have, you know, be running the Linuxes, the penguins, or

**Dave Jones:** whatever under there, I'm sure. But, yeah, the Artix-7 FPGA that'll be handling the 1 meg high-speed ADC and stuff. Oh, we've got an arm processor down there. Oh, and a Winbond jobbie. There's a memory. It's tied into the

**Dave Jones:** Artix-7 with a big bus. So, yeah. Actually, this is really quite interesting. We've got one arm processor here. It's an STM something. read that on the screen. But, it's an ST jobbie. And the one and the Artix-7 FPGA over

**Dave Jones:** here, as I said. But, also we almost practically duplicating that over here. We've got another processor. It looks identical. And another Winbond memory over here. We don't have another Artix-7 by the looks of it. I'd have to get that board out

**Dave Jones:** there. But, yeah, basically, we've got dual processor action happening here. The designers obviously Maybe they decided to offload uh voltage and current processing separately. Or maybe voltage and current in one and then like a dedicated real-time energy measurement

**Dave Jones:** in another one, perhaps. And that rear panel board there's just dedicated to your IO, that custom IO connector. We've just got a little isolated DC-to-DC converter to power that. And this is an ADP5052. And that's just a five-channel switching converter. You

**Dave Jones:** can tell it's a switching converter cuz hey, here's your DC input here. And we need to generate the various rails for the FPGAs and everything else. And yeah, we've got some little inductors around there. And some output caps. So, you can

**Dave Jones:** tell that's a little low-power switching reg there. But, you can see from the traces here that the isolated digital signals, these would be digital, coming out of here and going over to your Artix-7 FPGA, which doesn't have any

**Dave Jones:** analog capability. So, yeah, these are digital um isolated digital signals coming over. So, I'd be guessing these two here for your voltage measurement. Yes, cuz that's tied Here's your voltage input here. So, this would be your um high resolution ADC uh for

**Dave Jones:** your voltage input. And that's powered from this switching converter. And of course, you'd have a low noise uh linear regulator on the output of that as well. Cuz we're dealing with very low signal levels here. And this one here would be

**Dave Jones:** for your uh current ADC. So, yeah, we're going to find our voltage ADC under there and our current ADC under there somewhere. So, my guess would be that they're doing uh like real-time integration inside the uh Artix-7 there.

**Dave Jones:** So, that's you know, it's all hardware accelerated uh stuff. And then the ARM processor would be uh doing some auxiliary uh stuff like energy accumulation over time or uh you know, something like that. Um, but that that second ARM up there Oh, the second ARM

**Dave Jones:** up there could actually be um for like handling like IO and stuff like that. So, this could be a measurement uh processor. And this other one, which is identical ARM processor up there, could be used to handle um IO and um other

**Dave Jones:** stuff. And you know, serial comms and things like that. And then no doubt, your main processor uh up here is driving your user interface, your operating system, and uh you know, your screen and everything else. So, the giant cutout on the uh current input

**Dave Jones:** here um well, this is a 600-V capable unit. So, we're going to get some uh voltage isolation. And you can see how the You can see that the ground plane and that there's a huge gap in there between your

**Dave Jones:** current measurement here and your voltage measurement over here. And they've got two separate isolated uh paths here getting the data out for the voltage, getting the data out uh for the current. And then they're isol- then they're really isolating. You can see

**Dave Jones:** the isolation in the PCB there from um all the other uh processing side of it. Now, I got the heat sink off. Uh unfortunately, I can't see under there. The shunt resistor is soldered into these tabs and also soldered into that

**Dave Jones:** vertical PCB on the bottom and then clamped on with that. So, wow. They've really gone to town with that. That is just nuts. But anyway, we can measure it in circuit. Let's get 100 micro-ohms resolution here. Let's null out our

**Dave Jones:** leads. There you go. And it's not going to be absolutely precise. But There you go. I'd probably guess that that is actually a bang on to 10 milliohms. So, yeah, it's getting down there. The longer I leave it there and

**Dave Jones:** the more force I put on it, yeah, I think she's going to be a precision 10 milliohms shunt resistor. That's what I'd expect and it probably costs a fortune with bugger all tempco, of course. And of course, it's all about

**Dave Jones:** the tempco or temperature coefficient of the shunt resistor in here. You can have like a 10% accurate shunt resistor in here. It doesn't matter as long as its tempco is borderline zero, right? If you've got no like zero tempco, it

**Dave Jones:** doesn't matter what the accuracy of your shunt resistor is as long as it doesn't change with temperature or anything else like you know, a mechanical stress or anything else, then you can actually calibrate that out. You can calibrate

**Dave Jones:** that accuracy out in software. But when you're designing something like this, there are specialized manufacturers of resistors that will actually sell you a precise you know, 0.01% 10 milliohm resistor. And that four-terminal board there with the two inner ones

**Dave Jones:** pins are the tap going off from that precision resistor. So, yeah, I reckon they've got a real expensive jobbie in there. That's you know, probably like What's I don't know. I'd have to put this put up the spec of this thing. It's probably like

**Dave Jones:** half an order of magnitude or even an order of magnitude if you can get it more accurate than the best spec for this thing. So, all this mechanical complexity with the custom high current brackets here soldered directly onto the

**Dave Jones:** high current relay pins here and the vertical riser board for the current shunt resistor. That's all designed so that you can get the absolute best accuracy out of that precision shunt resistor. Yep, that's kind of like the effort you have to go to when you got

**Dave Jones:** this class of instrument. Anyway, the mains input here is pretty groovy. It's going down to the chassis down there. I think there's a shake-proof washer on there. It's all insulated nicely and and it looks like there might be a small

**Dave Jones:** filter inside that. Not sure. And I'll just power this on so that you can see the current mode up here, 5 milliamps. And I'm curious to know which Oh, it's got all these different current ranges. Of course, you can't do everything with

**Dave Jones:** your 10 milliohm resistor. Get your Ohm's law out and your confuser and figure out well, 5 milliamps across 10 milliohms. It ain't much voltage to read. Just saying. For those who couldn't be bothered getting your confuser out, that's 50 microvolts full

**Dave Jones:** scale. Full scale. So, if you got to read the resolution down in that, we're not going to be using 10 milliohm resistor. So, obviously, they must be switching other resistors. But anyway, let's listen for the big relay. We

**Dave Jones:** should be able to hear the big clunk. Clunk. There it is. Clunk. Clunk. So, 500 milliamps. Do we get another clunk? No. So, from 500 milliamps up to 20 amps, they're using that 10 milliohm shunt resistor. And for the other

**Dave Jones:** ranges, they're probably using like an ohm or something. I'm sure that LED there was flashing before. I thought I saw three flashy flashy LEDs. Anyway, there's three LEDs doing something. This is interesting. Just noticed that LED there flashed every

**Dave Jones:** time I was in the current menu and pushed that button. There it is. Beep. beep, beep, beep, beep, beep, beep. And when I change the voltage as well. Yeah, but it doesn't do it for other buttons. So, it's not like a button

**Dave Jones:** press. If I do the sideways buttons, it doesn't do anything. So, it's only when changing the voltage and current ranges up and down. So, yeah, my guess would be that that processor there is doing the real-time voltage and current

**Dave Jones:** measurements, but that's no surprise considering that the ASIC would be doing that and that processor there's handling. And this processor over here is, like I said, doing something else. And as for the sizing of this large heat sink for that 10 mli current shunt

**Dave Jones:** resistor there, at the maximum 20 amps here, we're only talking 4 W. But as you can see, there was supposed to be a fan in here, but they decided, "Nah, we don't need a fan. We'll just go with a

**Dave Jones:** really quite large." I mean, that's a really large heat sink for 4 4 W maximum power dissipation. But as I said, tempco is everything. So, you want to actually keep the temperature of that resistor down. You don't Yeah, okay, your

**Dave Jones:** resistor might be able to dissipate 4 W, but you don't want it to go from room temperature to 100° C at 4 W. So, just be aware of that with resistor ratings. Sure, okay, you've got your you've put

**Dave Jones:** your 1 W resistor in the circuit. It can dissipate 1 W, no worries. Yeah, but have a look at what temperature it's going to get to at 1 W. And when you got a critical precision current shunt resistor, yeah, you want to keep that

**Dave Jones:** thing as as cool as possible. I'll see if I can get the metal cans off without breaking anything. Um metal cans top and bottom. And here is under the two metal cans. There's nothing on the back side, just some

**Dave Jones:** miscellaneous stuff. We just got some diodes here on the That's on the current one and on the It looks like just Is that a regulator there? I'm not sure what that is, but anyway, yeah, there's not much doing.

**Dave Jones:** There's a whole bunch of unpopulated caps there on the bottom side of the voltage one, but anyway, let's have a look here. Now, I was wrong. I assumed that the ADC was going to be under these cans here. It ain't. It's just sitting

**Dave Jones:** out here. So, I zoom in and have a look. It's a linear technology jobby. Of course, it is. It's the 23 238016. And if we go to the video tape, and here it is, the LTC2380-16. It's a 16-bit 2 meg sample per second.

**Dave Jones:** The rating for this thing is 1 meg sample per second. So, I don't know why they're not pushing it to two. They can. Uh they're not multiplexing anything here cuz they've got separate ADCs for voltage and current. So, anyway, it's a

**Dave Jones:** successive approximation register or SAR converter, which is none of that flash conversion rubbish. So, good old school successive approximation converter. It looks pretty schmick. So, yeah, 16-bit jobby. And you know, look look at this. Low power battery operated

**Dave Jones:** instrumentation ATIs. That's exactly what we needed for. Ha, what a coinkidink. The given the signal-to-noise ratio on the THD, and you can go wild in the comments down below. But yeah, that's pretty schmick. So, they've got that outside of the

**Dave Jones:** metal can. Why? Because the metal can is the differential amplifiers in there, and it's really the low noise part of it. And once you amplify that signal up, then and of course drive it to the ADC, it's a low impedance path coming out of

**Dave Jones:** the can into the ADC like that. And once you've got a a relatively like line level voltage as it's called, and a low impedance path drive source impedance, then yeah, any interference is not going to matter in this part. So,

**Dave Jones:** it doesn't really need to be under the can. All the sensitive stuff is under the can because it's at sensitive higher impedance. Well, for the current, it's not very high impedance because you're like 10 milliohm resistor. It's a pretty

**Dave Jones:** low source impedance for your voltage coming across there. But you're talking about low signal levels, and you have have amplify them up. So, yeah, but once you've amplified them up, then Bob's your uncle. The voltage one over here is

**Dave Jones:** exactly the same. We've got our digital converters up there. I put up the data sheet of those before, and it's exactly the same successive approximation SAR converter here. And so, we'll have a look at the voltage one briefly here.

**Dave Jones:** We've got two Omron relays here. Unfortunately, look at this. China. Why can't I have a genuine Japanese Omron? Thank you very much. Anyway, the reason why that we've got all these resistors in series there, 1206 jobbies are they? The reason that

**Dave Jones:** we've got them all in series like this is because it's a high voltage string, and you can see the traces going like that. So, yes. And here's the bottom one. So, they're measuring the voltage across. That's just one big high voltage

**Dave Jones:** attenuation like that. So, yeah. Here it is. Here's our input connector. So, you remember this can measure up to 600 V. So, 600 V straight in, and then you know, 100 to 1 divider, whatever that is. In fact, they might tap off a couple

**Dave Jones:** of ranges there. But anyway, op 27, absolutely classic jelly bean precision op amp. And then, of course, yes, look at this. It's 74HC4052s. We've got some classic 74 series logic, but actually 4000 series logic. HC4053s. Classic triple analog muxes. These are

**Dave Jones:** your classic 4000 series muxes, but in the 7400 HCT series or HC. This is HC. This is HCT. So, this must be a TTL input threshold one. And anyway, they're analog switches. Classic analog switches, they do fine cuz once again,

**Dave Jones:** all the all the work's being done by these precision op amps. And this one, the OP1656, take a look at the video tape on this. It's a Burr-Brown jobby. Yes, all the Burr-Brown fanboys go wild before they were acquired by TI. Now, it's TI, but

**Dave Jones:** bloody Burr-Brown make the best stuff. Anyway, ultra low noise, low distortion FET input op amp. Look at this, point .000035 % distortion at 20 kHz. Ah, an audio fool's wet dream. Um and no, but they don't want really high

**Dave Jones:** precision stuff like this cuz they like the smell of their own farts and uh and the noise coming from their valves. So, you know, whatever. Anyway, um yeah, this is probably probably I don't know the best audio op amp on the market,

**Dave Jones:** perhaps? If you've got a better one, leave it in the comments down below, but yeah. DJ equipment, turntables. You've got your turntable. You put your points .000035% 20 kHz distortion in your turntable amplifier and yeah, okay, whatever. Anyway, fantastic. Probably, you know,

**Dave Jones:** if not the world's best op amp. Anyway, gain bandwidth product 53 MHz. Can easily do the 300 kHz bandwidth that we're looking at here. They're not gaining it up a lot, but very schmick. So, they've got three of those jobbies

**Dave Jones:** and yeah, that's it. And they're using that to drive the ADC. Now, the only other interesting thing here are these parts here. And there's a few of these in both the voltage and current. It's It's designator is RM8. So,

**Dave Jones:** this is like a resistor matched It's some sort of matched resistor array. Some sort of special secret squirrel matched resistor um array like dual resistors in it cuz they want them thermally bonded and thermally matched. They've got another

**Dave Jones:** three of those down here. So, these are like like just precision resistors, really. Um matched. I don't know. I don't know that package offhand. If you do know the manufacturer and if you notice that uh package if you recognize

**Dave Jones:** that package, then leave it in the comments down below, but yeah, some sort of matched resistor thing, not just, you know, your regular standard Joe Blog's resistors here. And as I said, this has got a linear reg out here. That's just

**Dave Jones:** an LM 7805 uh jobbie. And this will just be another low noise uh regulator just for powering the ADC here cuz that's important. So, yeah, cool bananas. And we'll go over here. And on the current amplifier side of things, look at this. Over here,

**Dave Jones:** I love how the the this is the uh this is the shunt resistor module version 1.00.000 because you never know when you have to get six uh you know, revision um decimal points in um to here in simple riser

**Dave Jones:** board for your shunt resistor. So, yeah, that's funny. Anyway, yep, so we have our lines coming out of here. We've got a Linear Technology 1037. Take a look at that. That's a low noise high speed precision op amp there. Yes, I'm not

**Dave Jones:** sure why they've chosen that particular one. Um anyway, you have sine wave generators here. Tape head amps, wide microphone preamps, strain gauge amps, microvolt s accuracy threshold detection. What's the offset voltage on this? This would have Yeah, guaranteed

**Dave Jones:** 0.6 microvolts max drift with temperature, 25 microvolts max offset voltage. So, it's not low. So, they're not using a chopping chopper amplifier uh like say we use in the microcard. I've done many uh videos on that. Um so,

**Dave Jones:** yeah, they're not they're not using that there. Um I would have expected a chopper configuration here actually because your offset voltage is going to matter when you've got a current sensing um shunt like this. Anyway, um we've got

**Dave Jones:** this um intercell jobbie. Uh let's take a look at that. And that's just a mux. So, looks like they needed a better mux than the uh 4000 series CMOS the 4053s and whatnot. So, yeah. And once again, we've got the 1656s here, 1560 56s. And

**Dave Jones:** they do actually have the 4053s here and here as well. And once again, we've got those little match resistor things there, those match resistor pairs. They got those all over the shop. So, yeah, that's interesting. Um but, yeah, I don't see a chopper amplifier

**Dave Jones:** here. So, that's surprising because you saw that we only change between two different shunt resistor values, the 10 mΩ one and whatever the higher one is. I actually I don't know where the higher shunt resistor is and on that board. No,

**Dave Jones:** it wouldn't be on that board, would it? Um might be on the riser board cuz I don't see a precision shunt resistor in here, really. Um you know, like a 1 Ω or 10 Ω or something like that. Anyway, like even

**Dave Jones:** with say the 10 mΩ one, it's great when you have like a full scale like half a volt drop across it or something like you know, several hundred millivolts drop maximum. But, when you're down in the resolution of your converter down in

**Dave Jones:** there, you've got like microvolts and then uh you know, this app op amp here had 25 microvolts offset voltage, for example. And then it's going to vary with temperature and stuff like that. Whereas a chopper amplifier is going to

**Dave Jones:** auto zero. It's called an auto zeroing amplifier. I've done videos on this and it's going to zero out that offset, basically. So, you get like, you know, 0.1 microvolts offset or something like that, you know, it's practically zero.

**Dave Jones:** Yeah, I'm not seeing any chopper package in here at all. So, that's interesting. Although, this you'll notice when I switch it on later, I'll show you that it does actually have a residual offset in it and it does actually

**Dave Jones:** put have that in the specs as well. So, they just didn't bother to put a chopper in there and make it better? I don't know. At this price point, another couple of bucks for a precision chopper amp. So,

**Dave Jones:** don't know what's going on there. LM393 dual op amp. Yeah, we've got another one of uh those low noise TL072 absolute classic jelly bean amplifier in there. That's not doing much to write home to your mum about. Um as and we've got some

**Dave Jones:** regulators here, but yeah, I expected a like really low offset chopper in there and we didn't get it. But yeah, they've got some pretty schmick op amps and they're using these what matched resistor dividers or something. So, we've got it back together and it seems

**Dave Jones:** to work. So, let's go into the current here and I'll tell I'll show you what I said about that offset there. Let's go down to the smallest current range that we actually can, 5 milliamps here and well, we can go down to the smallest

**Dave Jones:** voltage, but it's only got 15 volts up to 600 volts there, but anyway, we can go down to say 15 volts here and you see that we have a residual offset there of about 1.8 micro there and that is probably that

**Dave Jones:** that residual offset of that op amp that we actually looked at there. Because what I think they're doing there is they're actually trading off the ability to have lower offset here in the measurements with noise. So, they've opt

**Dave Jones:** they've decided we're going to prioritize like a lower noise floor on this thing rather than the offset down at the, you know, incredibly low values. Cuz this isn't designed to go down to, you know, nanoamps and stuff like that, but it's

**Dave Jones:** like it's really quite good as you can see, right? We've got like 100 nanoamps resolution on this thing. You can see it's changing by a single least significant digit is 100 nanoamps there, which is really great for most products

**Dave Jones:** unless you're really into ultra ultra low power stuff. So, but for most general product uses, this is really good, but they've decided to trade off just in that like lowest range there. And we should notice that doesn't really

**Dave Jones:** change except for the resolution there. So, there we go. It's now three microvolt three microamps offset there and they do actually include this in the spec. I'll try and put it up here. I can't remember offhand, but yeah, so it

**Dave Jones:** is in there and once we've lost that digit, boom, it goes away. Cuz as I said, when we go to the 200 milliamps maximum range for that 1 ohm or 10 ohm shunt resistor, whatever it is. When we

**Dave Jones:** switch to 500 milliamps, hear the relay click, clunk, like that, and then we restart the offset again. Um so, yeah, 500 milliamps, unfortunately, we've got the 0.33 milliamp offset. So, there we go, until you lose a digit and it

**Dave Jones:** vanishes. It's exactly the same. So, there's two current shunt resistors there, but unfortunately, that's the tyranny of ranging there. Unless you're going to have an entirely separate shunt resistor and amplifier for each one of those ranges, or at least shunt

**Dave Jones:** resistor, and then you can switch them using MOSFETs or whatever. Um but unless you like if you've only got the two shunt resistors, then yes, um on the slower on the lower ranges, um which is 5 milliamps and 500 milliamps here, uh

**Dave Jones:** you're going to get a greater effect of the offset uh voltage there. It's just going to beat the laws of physics, Captain. But as I said, if maybe if they used like a really, you know, best in industry uh chopper amp, they probably

**Dave Jones:** could have eliminated that. Um and you can do it with like manual tweaks and things like that, but then that's it just gets ugly, and well, you don't really want that. So, um yeah, cuz that adds adds a lot of time, and time is

**Dave Jones:** money, of course, when you're producing instruments like this. You don't want to be in there with some, you know, graybeard his tongue at the right angle uh trimming little uh trimmers in there, or even a software offsetting and stuff

**Dave Jones:** like that. So, you know. Let me show you a real-world measurement example here that I've been actually wanting to do. Uh this is the new Brymen/Eevblog BM787BT, the Bluetooth multimeter. I've done a video on that on the second channel. Uh

**Dave Jones:** if you haven't seen or a little bit of it, I'll be getting that fairly soon on the eevblog.store. Anyway, I want to measure, um, its battery power consumption when it's in Bluetooth mode, when it's actually transmitting data. So, I've got it hooked up here. I've got

**Dave Jones:** my, uh, power supply here generating 4 and 1/2 V, which is the nominal, uh, three, uh, AAA uh, battery thing here. And I've got the, uh, digital power meter connected to it. Let me show you how I've got that hooked up with the

**Dave Jones:** Dave card here. Uh, we've got our power supply here. Um, so our positive goes into the, uh, current shunt, the internal current shunt there. The positive side of the current shunt, you get that back to front, it'll be then

**Dave Jones:** your readouts will be negative. Then the output of the current shunt just goes into the positive input, uh, the battery terminal of the multimeter, and the ground is just connected to the ground. And this is the voltage sense, uh,

**Dave Jones:** terminals here. So, what I've done is I've put the voltage sense terminal actually on the negative side. So, any power that we're measuring is actually the current going into the device and the voltage across it. Now, uh, you can

**Dave Jones:** actually, uh, put this terminal on the positive side here across the power supply, and then you're actually measuring the true power supply source. But we won't go into reasons when you might want to do that and might not. But

**Dave Jones:** in this particular case, so we're just avoiding any power that's dissipated or power lost in the measurement shunt resistor inside this thing. But at these sorts of power levels, it doesn't really matter. Anyway, I've got it hooked up,

**Dave Jones:** and you can see I've just got the meter. It's it's not, um, transmitting anything, so data mode is not actually, uh, switched on. And you can see in AC voltage mode, we get our 4 and 1/2 V voltage there, U, not that V rubbish. U,

**Dave Jones:** hate it. Don't get me started, it's V, not U. Anyway, I can live with it. Um, and you can choose your different measurement parameters here for each of these, uh, four settings. So, we're we've just chosen the voltage, which is U, and the

**Dave Jones:** current, uh, I there. And you can see it's drawing 8 and 1/2 mA. And we're just multiplying those two together to give us the instantaneous power, 38 mW there. And I love this um, FU error cuz we're actually trying to measure Hz.

**Dave Jones:** I don't know. It was just there from default or whatever. So, that's why it's showing error because we're in DC mode up here. And you can watch that power change, okay? When I go into the different it should drop. Yeah, cuz AC

**Dave Jones:** is going to take more because it's doing more stuff. And millivolts there. So, it's round about 20 mW. Ohms keys is a bit less. And capacitance, more less again. Look at that. Temperature measurement mode, current. And other currents. So, yeah, the highest

**Dave Jones:** the highest mode here is your AC volts. But let's just put it in say DC volts. But watch what happens when we turn our data on here. I'll hold this on. And boom, we're in data mode there. And you

**Dave Jones:** see that's going that that kicked up there. That was very short, but anyway, we can adjust adjust the update, right? Let's do it 0.1 per second, shall we? So, there we go. It's updating really quick now. So, let's actually switch

**Dave Jones:** that data back off, okay? And bingo, we've got our 4.5 mA, okay? Watch this. Switch it on. Whoa, it was 20 something mA there. It's jumped up. And so, it's actually trying to negotiate hooking up with the shoe phone at the moment, the

**Dave Jones:** Bluetooth app. You might say it bright look, it's jumping up, right? 14 15. So, there's like a brief there's, you know, current spikes in there. And we can of course log this data. We're just viewing it on the screen at the moment. Okay?

**Dave Jones:** So, let's see if it'll log. Will it Come on. There we go. It's connected. Did that change? I wasn't watching the screen over here. But it could actually be consuming more current when it's actually like in in negotiation mode.

**Dave Jones:** And then I can and the channel here. And we can actually go into a real time logger here and we can actually log Oh, did it jump up there? Like seven, eight? I mean, we can turn on like average

**Dave Jones:** modes and stuff in here, right? So, we're we're just reading uh noise at the moment. So, it's just, you know, least significant digit there. No, I don't think there's anything in that. It's really hard to see there. We probably

**Dave Jones:** need to uh log this. And we can actually view the waveform here and we can see those spikes generated being generated there. Those those current spikes. And you can actually see that there's little modes in there where it actually

**Dave Jones:** increases. Now, not only is there that little uh transmit spike there where it's transmitting the packet, but it's I can't get it to sync there. You know, this is not as uh groovy as a proper scope for uh triggering wise, but

**Dave Jones:** you can see that we've got peak currents there of like 48, 49 milliamps there. So, you know, it's getting up there. And then, watch that waveform data if I switch off the transmit mode. There we go. And now,

**Dave Jones:** we've got peaks of like, you know, 3 milliamps. So, the answer is yes, of course, it's going to actually chew probably a significant amount of power extra um it when you're actually logging um Bluetooth data to your shoe phone.

**Dave Jones:** And nothing surprising there, you expect that, of course. Now, if we want to measure energy, which is basically our power with respect to time, then we want to use the integrate mode uh which basically it integrates the power to

**Dave Jones:** give us a watt-hour figure over time. So, I've got it in non-transmit mode and we can start our integrator and boom, it's going to get our milliwatt-hour figure and we can take this over, you know, we can leave it logging until the

**Dave Jones:** battery's run out um or, you know, for an hour as a benchmark or a day's worth of logging or something like that. And we can get an accumulated milliwatt-hour figure. But anyway, just use your noggin at the moment and

**Dave Jones:** look at how fast that's counting up. Maybe count that digit three, four, five, six, and well, actually, we'll do it live here. Ready? We'll turn on the data mode. Boom! It's now transmitting. And that's counting up significantly quicker now. So, we can get an

**Dave Jones:** accumulated milliwatt hour figure over time. And if we know the milliwatt hour capacity of our battery, for example, for a given cutoff voltage, I know it gets a bit complicated. We can start talking about cutoff voltages and things

**Dave Jones:** like that, but um yeah, we can we can use this tool to actually um get a like a nice battery consumption figure, uh a comparative battery consumption figure for our product that we're developing. So, it it's very cool. And it can do a

**Dave Jones:** lot more stuff, of course, you know, as I said like you can do harmonic analysis and stuff like that, but um yeah, and and of course, we can use the other stuff, right? We can go back into the

**Dave Jones:** data here live, and it's still integrating in the background. And that's that probably doing it inside that ASIC and the arm processor there. It's it's just doing that integration um with inside that, so you can operate the menus and do everything else while

**Dave Jones:** you're actually doing uh the long-term integration uh measurement, which is really cool. And we can get milliamp hours there if we didn't want uh milliwatt hours uh depending on what battery spec we're doing and stuff like that. So, a very comprehensive bit of

**Dave Jones:** kit. Now, of course, you can do this uh like with a you know, two multi two logging multimeters, but then you've got to have the software to actually you know, the data logger software to actually do that and accumulate that

**Dave Jones:** over time. This is like it just a nicety that you've got this built into the one bit of kit. And because this is doing integration in hardware, that's what that ASIC, no doubt what that ASIC is for, it's doing that in hardware. It at

**Dave Jones:** one meg sample per second for the voltage and current. It's doing it in a real time and really fast in the hardware, so it's not going to miss any of those transmit little transmit spikes and stuff like that. Whereas if you're

**Dave Jones:** doing this sort of measurement with your regular multimeters, they're slow as a wet week, right? Whereas this is like a precision voltage and current meter, but it's capable of 1 megasample per second. So you're not going to miss all

**Dave Jones:** of those little transmits. So you're going to end up with a true energy indication and you haven't missed any of these like fast spikes or you know, your processor is changing modes and doing things like that. Or in this particular

**Dave Jones:** case, they're doing a little RF transmission burst and things like that. So yeah, you really need a fast digital power meter in doing that integration in sampling and integration in real time in the hardware to capture all this. And

**Dave Jones:** that's what this thing can do. It's pretty cool. So I've switched off our load and you'll notice that our residual current there has shifted a bit because we've got the whole setup actually connected in the back. So if I

**Dave Jones:** disconnect, let's diddle the let's diddle the back here and boom. No, there you go. I've interesting. I thought that would go back, but that has actually drifted. The the residual offset has actually drifted. Anyway, we can actually calibrate that out.

**Dave Jones:** Unfortunately, I'd love to have it actually get it back to where it was before. Maybe I should turn it off for a while. So we can actually calibrate and zero that out with the cal function there. But yeah, I don't have to. But you can see

**Dave Jones:** that it does drift. So unfortunately, down at the least significant digits here, you are going to drift a bit. And you can calibrate it out, but then you might drift again due to temperature, whatever. I just actually repowered the

**Dave Jones:** thing and we're getting that negative point triple 0 5 there, but we can null that out. and what? Yeah, it gets a bit tricky but you can see so you could have eliminated the need to actually do that

**Dave Jones:** and you know, you can get like one LSB in digital or something offset if you really want to design that in but then that impacts the noise floor and the bandwidth as well. So this thing wants to be really fast.

**Dave Jones:** So yeah, we're we're sort of trading off a bit of that DC that absolute offset accuracy for bandwidth and noise floor really. And you can just do a whole bunch of stuff in the one instrument. So that's a very cool bit of

**Dave Jones:** kit. I like that. Yeah, sorry I can't give you a final result on this but yeah, we probably expect the battery life to maybe halve or go down by a third or something like that if you continuously log in

**Dave Jones:** the Bluetooth data. So anyway, I hope you enjoyed that video and look at this interesting bit of kit that a lot of labs don't have but if you're doing any sort of product development where you need any sort of energy or power

**Dave Jones:** measurement or something like that, having a dedicated digital power meter like this very cool bit of kit worth having. Anyway, thoughts and comments down below and if you like the video, please give it a big thumbs up cuz that helps with

**Dave Jones:** the engagement on YouTube. I'm trying to beat the bots. It's almost impossible these days. Anyway, yes the Bluetooth version of the multimeter will be available as soon on the EV blog store. It will cost a bit more than the regular 786 but I'll have

**Dave Jones:** it shortly. This is a prototype which just has like stickers on there and you can see it's just got the it's just got the stickers and no blue for the EV blog yet and no blue holster but anyway,

**Dave Jones:** it's coming. Anyway, hope you enjoyed that and found it useful. Catch you next time.
