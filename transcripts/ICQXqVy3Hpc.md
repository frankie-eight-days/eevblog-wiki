---
video_id: ICQXqVy3Hpc
title: EEVblog #158 - AVR ISP MK2 + LM317 Regulator Tutorial
url: https://www.youtube.com/watch?v=ICQXqVy3Hpc
source: youtube-asr
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, often when you're playing around with your microcontroller circuit, you build up your little board like this,

**Dave Jones:** and you just want to program it. And it usually doesn't draw all that much power, and you know that uh the 5-V USB port that powers your little programmer, your in-circuit programmer, can easily power your circuit. And it's just handy

**Dave Jones:** to be able to power the board and program it at the same time via the in-circuit programming adapter. This one's the AVR ISP mkII programmer. Now, the uh PICkit programmer for the PIC microcontrollers, that has the nice function of being able to generate an

**Dave Jones:** output voltage that comes on one of the in-circuit programming pins, and it can power your circuit under test, which is really handy when you just want to run the thing on your bench. You don't want to have to have a separate power supply

**Dave Jones:** to do it. But unfortunately, the AVRISP mkII doesn't have that capability, and I found that really annoying. So, I thought I'd do a very quick mod and show you uh how I converted this to generate an output voltage on here and power your

**Dave Jones:** board under test. And here's my modified AVRISP mkII main unit. And I've made two very simple mods to it. One is an on-off switch, which all it does is it applies um either 3.3 V or 5 V through to pin

**Dave Jones:** two of the uh six-pin in-circuit serial programming header. Now, normally pin two uh is actually an input. Well, it still is an input, but it uh it it reads normally on an unmodified unmodified unit, it reads the input voltage from

**Dave Jones:** your circuit, so uh which powers the input buffer on the thing, so it knows what uh signal level you're using. If you're using a 5-V circuit, it uses it it knows to use a 5-V input buffer, 3.3, or even lower than that, it can adjust

**Dave Jones:** to the level. And the beauty about that is that means, because it's pretty much an input, we can simply wire a voltage directly to uh pin two on the board in here, which can actually power your circuit. Now, my circuit my my little

**Dave Jones:** here only needed uh 5 V. It worked from 5 V, but I thought, "Ah, I'd go to the effort just to put in 3.3 V in case uh any future boards I design I'll be able to power those as well." So, let's take

**Dave Jones:** a look inside. Now, it's actually not a bad little design, this. It's got four little clips here on the back, and you just get a flat blade screwdriver in there and push them aside, and it just levers off and opens like that. And

**Dave Jones:** there's the main board in there, and they've also got two clips down the bottom here, which allows you to take out the main board. You can just uh apply just pull it back like that, and the board will lift out when you pull back

**Dave Jones:** on those connectors. And bingo, it just pops out, allows you to do mods really simply. I like it. Now, my modification is really simple. The on-off switch here just goes through is soldered to pin two on the ISP

**Dave Jones:** connector down there, and then the input to it goes to the 3.3 V or 5-V selection switch there. Um uh single pole double throw, and it just uh and I've just added an LM317 voltage regulator on there with some decoupling caps and some

**Dave Jones:** uh a couple of resistors to set the voltage, and that's pretty much it. And that's powered directly from the 5-V uh input from the USB. Now, unfortunately, Atmel don't actually uh give you the circuit for this Mark II uh programmer,

**Dave Jones:** and I couldn't find any circuits online. So, if you know of any, uh, please, uh, post the link so that everyone can take a look at it. So, I didn't really bother reverse-engineering the circuit to figure out how it works. I just knew

**Dave Jones:** that the, um, input, because it's, uh, it it's a voltage-buffer-based input, that I could just wire the voltage straight through the output, and it wouldn't do any harm because it's designed to read that input voltage. So, whether or not it comes from my voltage

**Dave Jones:** regulator here or the voltage comes from the connector on your board, it really makes no difference. So, I was 100% confident that, um, I was safe in doing that. Now, uh, if you just want to wire 5 V

**Dave Jones:** through to the output and not worry about adding the regulator with 3.3, you just tap off the 5 V pin, which is that furthest one with the, uh, large trace coming off it. Just wire that directly through the pin two, and that's all you

**Dave Jones:** have to do to mod this thing. Um, but I'd recommend putting on an on-off switch, of course. Uh, but you can the mod could be that simple if you just want to power 5 V circuits. And, of course, the USB is capable of

**Dave Jones:** supplying, uh, 500 mA at 5 V typically, or 2 and 1/2 W. I'm not sure how much, uh, power this board takes. I haven't actually measured it, but it's not that important. It wouldn't take all that much at all, really. So, there is, uh,

**Dave Jones:** there should be ample, uh, current to power your circuit under test, maybe, you know, 350, 400 mA, or something like that, should be readily available, but we'll check that later and see how that goes. And here's an up-close shot of my mod. And I've put

**Dave Jones:** the LM317 backwards here because, uh, it made sense to do that because the input pin here is on this side of the device, and I just bent that over and connected it directly to a capacitor. It's quite hard

**Dave Jones:** to see, sorry about that, but a a capacitor So directly connected through to that large trace, which is the 5-V input from the USB connector. So that goes directly into the LM317. Uh this one over here is the adjust pin.

**Dave Jones:** As you can see, I've got the resistor and the tab of the device is actually connected through to the center pin here, which is the output. So I could have soldered that wire directly onto the center pin, but I just thought it

**Dave Jones:** was uh nicer just to put it onto the uh tab at the back there. And this is one of the feedback resistors. And the other one, which is used to set the voltage, I've got two in series there,

**Dave Jones:** which will go into the circuit, but they uh these are the ones that set the output voltage. And this here is um just an input a 100 n uh input decoupling cap for the 5-V rail. So it goes 5 V and

**Dave Jones:** it's soldered down onto the tab of the um the the shield of the USB connector, which is I've checked, it is actually connected through to the ground point. Um and this here is the uh another um 100 n output capacitor. Oh, sorry, it's

**Dave Jones:** not 100 n, it's like um that. And uh yeah, I just picked the uh highest value I found in my junk box that fitted, and it's connected between the output and ground as well. And that's all there is

**Dave Jones:** to it. It's pretty simple. And the output just goes off to the 3.3 or the 5-V selector switch and then switches through to the on-off switch, which goes through to pin two. Simple. And it all seems to fit nicely. This um

**Dave Jones:** the actual voltage regulator isn't uh glued down or anything like that. It's just sitting there. So it's not the most robust solution in terms of vibration. So um yeah, I'm not sure how long it will last, but I didn't bother putting it

**Dave Jones:** down. It It'll be fairly rugged, but it can actually move there, but it's not a big deal for just a simple development device like this. And one thing you've got to be careful of there is just to drill the switch on the other side of

**Dave Jones:** this device. As you can see, I goofed it. I didn't have my head screwed on and I drilled the hole on the wrong side of the device, which without catering for the height of the device when it plugs

**Dave Jones:** in like that. So, it fouled on the top of the regulator and that wouldn't have been very good to short out to that to the switch. So, I just uh shifted that one over and put a label over it. No

**Dave Jones:** problems. Fixed. And let's have a quick look at the LM317 data sheet, shall we? This is the National Semiconductor one, which just so happens to be exactly the same as the one I'm using. And let's look down here

**Dave Jones:** at the typical application circuit. And this is basically what we have here, the LM317. We've got the input cap, 100 n, just for good measure because I'm not sure if there was actually one on the board. I didn't fully trace it out, but

**Dave Jones:** I wasn't actually sure of the input configuration on there. So, I added one just to be sure. I've got an output cap. Basically, 1 microfarad is a little bit overkill. That's a recommended value. You can use that. You can use 100 n as

**Dave Jones:** well if you want. And it's going to be perfectly stable. I used, I think it was a 470 n. I'm not sure. Uh and I've got a And it says it use a 240 ohm here. That's just a nominal value. I actually

**Dave Jones:** used a 220 ohm there and a variable value, which we have to calculate for our nominal output voltage of 3.3 V. So, let's do that. Here is the typical formula for a standard LM317. It doesn't matter which device you've actually got. But

**Dave Jones:** so, we know what our V out is. Our V out is 3.3 V. And we actually want to calculate R2 here. So, we know what R1 is. We're using 220 ohms for that. So, you have to rearrange the formula here. So, if you

**Dave Jones:** do that, R2 equals V out on 1.25, which is the voltage the internal voltage reference inside the device, and then you subtract one, and then you want to multiply that by R1. So, if you punch those numbers in, you will get a value

**Dave Jones:** for R2 for 3.3 volts. So, if we want 3.3 volts over 1.25 minus 1 times R1 is 220 ohms. That gives us an R2 of about 360 ohms. And because we've chosen E12 value here, we'll choose an E12 value here to make

**Dave Jones:** it nice. We'll actually choose a 330 ohm plus we'll make it a 33 ohm resistor to give us 363, which is more than near enough for our purposes. Now, I know what you're thinking. What about this term here? Why did I leave

**Dave Jones:** this I adjust times R2 out of the equation? Well, this is typically done because it's usually quite an insignificant term unless you've got quite high value resistors here for you for your feedback. But, because we've got quite low values, you'll see

**Dave Jones:** that it doesn't add up at all at much and too much at all. So, you can simply ignore it in most practical cases. So, the I adjust is actually the current required for the adjust pin here, which flows through R2. Hence, the output will

**Dave Jones:** be the adjust current times R2, which is Ohm's law, the voltage drop across that resistor, plus your value. So, that's why they they add that term plus I adjust times R2. Now, if you look at the data sheet for the device the other

**Dave Jones:** page, you have to look down here. Let's see if we can get it here. Adjustment pin current. There it is. And it's typical value is 50 microamps, but if you're doing these sort of calculations, you always take the worst case figure

**Dave Jones:** unless you know exactly what you're doing. So, we'll take the worst case figure of 100 microamps, and we'll multiply the 100 or 100 microamps times our 363 ohms, that's only equal to about 36 millivolts. So, instead of our nominal 3.3 or whatever

**Dave Jones:** value it works out to with those exact value resistors, it'll be instead of being 3.3, it'll be 3.336. And it's not really a big deal for our purposes, but it's something to be aware of if you are designing LM317

**Dave Jones:** circuits. Now, just in case you're wondering why they typically choose a value of 240 ohms here for the sense resistor here, it's pretty much because because of the error current from the adjust terminal. It it effectively sets like a minimum

**Dave Jones:** load current required for this device, which they typically specify in the data sheet here. If you take a look at a lot of the specs will actually show um like a minimum of like 10 milliamps. These specs will only be

**Dave Jones:** appropriate for a for an I out of 10 milliamps up here. So, if you go down and you take a look at a couple of these, they will actually have minimum values of 10 milliamps. There it is. Load load regulation, you

**Dave Jones:** got 10 milliamps I out up to I max. So, really having a low value for your sense resistor down here pretty much ensures that you're pretty much going to meet that minimum load current requirement. You can actually increase these values,

**Dave Jones:** but then the error term becomes significant, and you're not going to meet a lot of the data sheet's specs. So, you really should keep that to about 240 or well, you know, certainly under like 500 ohms or something like that to

**Dave Jones:** really keep the thing within spec. I typically use a 220 ohm. Now, the other trap with the LM317 is that it is not what's called a low dropout voltage regulator. It's a just a standard linear regulator with a high dropout voltage.

**Dave Jones:** That means the dropout voltage is the voltage differential between the input. So, the input must be X volts higher than the output, otherwise it drops out of voltage regulation, which I won't go into the details of how and why, but it

**Dave Jones:** basically means if you've got 5 volts out of your regulator, for example, well, you need typically for an LM317 as a rule of thumb at full current, it's taken as a 2-volt minimum drop, and we'll take a look at that in a sec. So,

**Dave Jones:** you would need a minimum of 7 volts input, otherwise your regulator will drop out of regulation. Now, here is, if you go through the data sheet, it'll it'll be the same for all voltage regulators like this. All linear

**Dave Jones:** voltage regulators will have a dropout voltage specification. You can get special low dropout types, which go down to several hundred millivolts or something like that. They can actually be quite low, but here is our parametric graph of the input to

**Dave Jones:** output differential voltage on the Y axis here from 1 volt up to 3 volts, and that's the dropout voltage, okay, on the Y axis versus temperature, cuz this effect does change with temperature. And as you can see, curiously, it has at

**Dave Jones:** different and these load lines are for different output load currents. This one up here, which curves like that, is for the maximum 1.5 amps output, and then 1 amp and 500 milliamps, 200 milliamps, and then the lowest load line they've got is 20

**Dave Jones:** milliamps here. So, let's take a look at the 20 milliamp one, and let's take basic room temperature here for our 20 milliamp minimum load current graph. So, at 25° C, which is room temperature, we've got a dropout voltage of about 1. 5 V. So, if we want

**Dave Jones:** 3.3 V output, that means we need an input voltage minimum of 3.3 V plus 1.5 V, which is 4.8 V, and technically our USB should give us that. Although USB is 5 V plus minus 5%. So, it could actually be,

**Dave Jones:** you know, it could actually be under that. It could technically be 4.75, but we're not too concerned with that. We will actually test it later, but that's at the minimum voltage. And let's say at our I out of 500 milliamps, which

**Dave Jones:** is the absolute maximum that the USB is going to give us at 25° room temperature, cuz typically this development board here in Australia is only going to be pretty much used at room temperature. So, I don't really have to worry about the extreme ends of

**Dave Jones:** the of the curve. Really, only if you're going up to some sort of industrial temperature, do you sort of have to worry about the differences in the temperature differential of the load line. So, at 500 milliamps, 25° C, we're

**Dave Jones:** looking at about 1.75 V or 1.8 V or thereabouts dropout voltage. And of course 3.3 V, our output voltage plus that nominal 1.8 V volts 500 milliamps, Uh, that's going to give us uh 5.1. So, we require a 5.1

**Dave Jones:** V input voltage, which our 5 V USB is uh well, 5 V nominal. So, we're pretty close to the margin if we're drawing In fact, we're technically over if we're drawing an I out of 500 milliamps. But, because I you know, this is circuit

**Dave Jones:** isn't going to go into production. It's only a development board, a development tool then. And I'm not going to be drawing 500 milliamps out of the thing. I'm only going to be drawing a couple of hundred. So, I might go down to the 200

**Dave Jones:** milliamp line here. It's only about um you know, 1.7 V or something like that. So, really you know, I think it's going to do the job. But, hey, let's test it. Now, I thought we'd just check the uh

**Dave Jones:** performance of this thing to see if it meets the data sheet specs. Because if you remember, I said that we're going to be pretty close to the limit of the dropout voltage of this LM317. Because ideally, I would have used a low

**Dave Jones:** dropout regulator in this application. But, I didn't have one left in my junk box. I just decided to use an LM317. And let's see if it matches the uh dropout voltage graph, shall we? Now, to do that, what we need is the

**Dave Jones:** input here powered from my bench supply uh over there. So, my variable bench supply. So, that's the 5 V input USB. I can adjust that. And you've seen this before. I've got my handy dandy constant current uh load. So, we can adjust the

**Dave Jones:** current to match the various curves on the graph and see what we get. And I've got two meters as always. Uh you need at least two uh on your bench to do serious work like this. So, I've got one the Metrahit

**Dave Jones:** extra here is measuring the input voltage to the voltage regulator. And the uh Fluke 87 is measuring the output voltage. Now, when you're probing the voltage like this, it has to be right on the input and output terminal. You've

**Dave Jones:** got to probe it right on there. Otherwise, you could get uh a a voltage drop due to current through your wires or or traces on your board or something like that. So, you have to probe it directly at the input and have the

**Dave Jones:** ground directly on the ground pin as well. And I won't go into it, but I've got it all hooked up down there and there it is. And it's a bit of a mess, but we should be able to measure the

**Dave Jones:** load current graphs. Let's try it. First one we're going to try and measure is 20 mA one down here because that's guaranteed to work. We should get just over 1.5 V there at 25°C And that's actually not the

**Dave Jones:** ambient temperature. That's actually the junction temperature. And if you're doing this seriously, then you'll actually want to get a probe onto the case of the device, but even that is not the true temperature of the junction. You will have to use the thermal data

**Dave Jones:** from the data sheet which shows the junction to case thermal resistance. You've got to take that into account to calculate the junction. Anyway, for the purposes of today's experiment, we just want to get a near enough value so we

**Dave Jones:** don't have to worry about that that sort of stuff because we're not going to draw too much current from this so the regulator's not going to heat up much. But, what we want is to measure the 20 mA

**Dave Jones:** load graph there at about 25°C we expect it just over 1.5 V drop out voltage. Now, the drop out voltage is defined as the delta V out or the change in V out or the drop in V out actually of 100 mV.

**Dave Jones:** So, what we want to do here is adjust our input voltage down until our output voltage drops by 100 mV. Now, as you can see it's 3.36 output voltage and if I adjust the input voltage here, way, that's a bit high.

**Dave Jones:** Oops, be careful with that. You can see that it it pretty much is regulated. There's no problem at all. So, the regulator's working just fine and we want to adjust that down until that gets down to 3.26. There we go, it's dropping. It could be

**Dave Jones:** a little bit tricky. Sorry, 3. Yeah, 3.26. So, there it is. I'm going to say that's near enough. So, 4.8 volts. All we've got to do is plug that into the calculator. 4.803. Let's put all the digits in. We don't

**Dave Jones:** have to. Minus 3. 2 Let's say 26 there and that is 1.54 volts drop out voltage. Bingo. It matches the graph there. 1. Yeah, 1.54. It's just over that point there on the graph. So, that matches up perfectly. Oh, by the way, I've set the

**Dave Jones:** current to 20 milliamps down here, the load current. And let's repeat that for the 200 milliamp load graph. So, I've got adjusted the output current to 200 milliamps there and we expect roughly let's have a look here. 1.5 or 1.65,

**Dave Jones:** 1.7 odd volts or thereabouts. So, let's see if we get that, shall we? Let's drop our input voltage until we get 3.26. There we go, pretty much spot on. So, it's 4.958 minus 3.264 equals 1.69 or 1.7 volts. So, it's spot on. It

**Dave Jones:** matches those graphs very precisely. Beauty. Now, if this was a production design, we would want to characterize the maximum output current we could take from this regulator under a worst-case input scenario. In this case, the it worst case would be 5% below the nominal

**Dave Jones:** 5-V USB input voltage or 4.75 V. So, you would adjust your input to 4.75 V, and then you would adjust your current up from zero until your regulator output voltage here got to 5% below your nominal 3.3-V output voltage. That's 165 mV below or

**Dave Jones:** 3.13 V. So, if we adjust our current here, okay, we adjust straight So, we're looking for 3.13 roughly. We've got Oh, I could tweak the input down a bit, but really we're we're just fluffing around the edges now. Um

**Dave Jones:** so, really we're looking at What have we got here? Very touchy on the old uh power supply voltage control there, but we're looking at 3.13 V there. So, really you're looking at um you know, at really 160-odd milliamps. There you go, 160 or

**Dave Jones:** thereabouts would be the worst case uh actually Well, it'd be the worst-case output current we could draw from our voltage regulator while we're still within spec at room temperature. And then, if you wanted to uh uh characterize it over different

**Dave Jones:** temperature ranges if it wasn't just going to be used in a basic uh lab environment like this, then you'd have to go to a lot more trouble. And that's what happens when you um when you're on the margin like this using an LM317

**Dave Jones:** voltage regula- regulator, a standard linear regulator instead of a low dropout one where we would have had plenty of margin. Um instead of having, you know, the 1.5 to 2 volts dropout voltage, which we get with the LM317, if

**Dave Jones:** you use an LDO, it might have .2 volts dropout voltage, and we'd have a ton of margin, and the output current would work right up to, you know, 500 milliamps, not a problem, and everything would be sweet. But, we're just trying

**Dave Jones:** to be really cheap and simple and nasty here and use an LM317. And if you're interested to know what the quiescent current is for just the AVR ISP Mark II programmer on its own, that's the input current for the USB,

**Dave Jones:** the 5-volt USB. It's around about 100 milliamps, and it's not doing anything. All it's doing is it's got an LED down there, which is flashing, and that's about it. And that's the quiescent. So, it really that means that we'd actually have out

**Dave Jones:** of our regulator a maximum of 400 milliamps to power our circuit under test. And I really like this. You can see the fast update rate of the bar graph here flashing in time with the LED. So, it's taking those pulses of current as the

**Dave Jones:** LED switches off and on. You can actually get an indication where it drops to about 90 milliamps there, or a little bit below, maybe about 85 milliamps up to like 110, but the average is about 100. And you can see the advantage that the

**Dave Jones:** Metrahit Xtra had on its expanded scale bar graph here, because the the Fluke isn't Well, it's not actually displaying the average as nice as the Metrahit Xtra did. It's jumping around like a jackrabbit, and the bar graph, as you

**Dave Jones:** can see, is really tiny. You can't really make out, you know, it's jumping just one segment where it there, whereas this was actually significantly jumping between two valid points, which you could actually see. And that's because the the Fluke is a

**Dave Jones:** has a six well, in this case a 600 count bar graph and we're down around 100 and based on the number of bar graph segments, you can see it's it's not nearly as useful as the Metrahit extra in this case, but that's going to vary

**Dave Jones:** between meters and between ranges. So, it just so happens the Metrahit extra was far superior in this case. But of course, that's where you put on your min max mode here. So, I've put on min max like this and it's you might

**Dave Jones:** hear an occasional beep there which means it's recorded a new value. So, you don't have to watch the display. Just put min max on there and bingo, we can just look at the maximum is well, in the because it's a negative current maximum

**Dave Jones:** was 92 odd and the positive was 112. Pretty much what we got on the but we could see that live on the bar graph here on the Metrahit extra. And I've done exactly the same min max thing here

**Dave Jones:** on the Metrahit extra and it's saying it's 87 milliamps and we're looking at 100. That's the sorry, that's captured minimum is 114 and 87. So, as you can see it really correlates to the actual bar graph display there live. So, I don't I'd have

**Dave Jones:** to I'd have to review the specs again, but looks like the Metrahit extra is actually capturing those peaks faster than the Fluke 87. And of course, we're not done yet. We still need to check the output noise of

**Dave Jones:** the regulator to see make sure it's not oscillating for a start and well, we know the noise performance as long as it's not oscillating and it's not dropping out, the noise performance is going to be good. So, I've got it set to

**Dave Jones:** 20 millivolts per division here and it's not, you know, a problem at all. It's it's quite nice. It's it hasn't dropped out. It's well within regulation and everything's fine, but watch what happens when I turn down the input

**Dave Jones:** voltage here and it starts to drop out. Boom, there we go. It's starting to Even though you haven't quite seen it on there, there you go. You can start Yeah, there you go. It's starting to drop. So, that's

**Dave Jones:** what happens when a regulator drops out of regulation there. Um different regulators perform in different ways. Some of them will actually perform quite nicely when they drop out. So, you they won't oscillate like this and do other weird stuff, but

**Dave Jones:** we're still talking about not a huge amount there, but if we keep dropping that input voltage say to 4.75 or we change the output current, it's going to change with the output current as well. But, as you can see, it does actually

**Dave Jones:** doesn't drop out as smoothly as you'd like, but that's the LM317. There are much better regulators out there. And if you're keen on the actual details of the circuit, there's not much to it. Here's the Dave CAD drawing of it. It's

**Dave Jones:** basically just a 5-V USB input. Any 3.3-V voltage regulator regulator you like. I used an LM317 cuz I didn't have anything else at the time. It's not that great. I'd recommend you use a low drop out an LDO voltage regulator. 3.3-V just a a

**Dave Jones:** selection switch to choose between them and an on-off switch and hook that up to pin two of the ISP connector and that's it. Bingo, you've got yourself a modified AVR ISP Mark II programmer. So, after all that, am I happy with

**Dave Jones:** this? Well, not not 100% No, it's There's a quite a limita- quite a few limitations. Really I'm limited to a maximum output current of Basically 150 milliamps, which is going to be okay for a lot of circuits I do, but really

**Dave Jones:** I think it was a it was a bit of a gamble to put in an LM317. I know I was going to be limited. I was hoping for a little bit better but and then than the data sheet performance figures, but they

**Dave Jones:** are pretty much spot on to the to the figures there. So, it's not that great. I think I might actually replace it with a low dropout voltage regulator and just a fixed voltage a fixed 3.3 volt one. So, you don't even need the

**Dave Jones:** adjustment adjustment resistors on there. All you need is the regulator and input and output cap. Problem solved. Huge amount of margin and well, there you go. That was just implementing simple LM317 on a design. I got a bit

**Dave Jones:** carried away here. I was just going to only show you the mod and that was it. It was going to be a quick 2-minute vlog, but I thought I'd just show you some stuff on some basic performance measurements on an LM317.

**Dave Jones:** I hope you liked it. See you.
