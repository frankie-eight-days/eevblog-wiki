---
video_id: Lg6oYFerUlA
title: EEVblog #232 - Lab Power Supply Design Part 5
url: https://www.youtube.com/watch?v=Lg6oYFerUlA
source: youtube-asr
---

**Dave Jones:** Hi, it's time for the next part in the power supply series. I've been designing this cute little power supply and I thought we'd take a look at the final schematic. Let's go. And if you remember the previous videos,

**Dave Jones:** here's the existing circuit we already had, which I breadboarded up. We pretty much developed this from scratch. Now, the the final schematic we're going to go through today is essentially exactly the same configuration as this, but I've gilded the lily again, added a few

**Dave Jones:** niceties and put some system engineering into it, I guess you could say, and tada, here it is. Here's the final schematic. Now, it might look a bit complicated. That's cuz I've put it all sort of crammed it all onto an A4

**Dave Jones:** sheet here. It's not terribly modular, but stick with me. We'll go through it and you'll see that it's not that hard at all. It's very simple. First of all, if you take away all the other circuitry there, you'll find that this circuitry

**Dave Jones:** in here is pretty much identical to our existing circuit here. So, let's take a look at that part of it first and the current shunt that current shunt amplifier and resistor, which I've changed up here. But before we do that,

**Dave Jones:** let's just take a look at the thing from a block diagram level, shall we? This is exactly the same circuit we had before. I've added a microcontroller down here. It's an ATmega168. It could be an ATmega328 or whatever.

**Dave Jones:** Any of those are 28-pin ATmegas. It's going to be Arduino compatible because the software will be written in the Arduino software environment. I've added external ADC and external ADC here around here with some voltage followers and an external DAC as well. Now, you

**Dave Jones:** know how I did the video on the pulse width modulation output and how you can control the output voltage and current with PWM. I was originally going to do that cuz most microcontrollers are only 10-bit resolution 80Cs. So, I don't

**Dave Jones:** know. I decided to gild the lily a bit. I wanted a bit more resolution, so I'm using external 12-bit DAC and an external 12-bit ADC, which we'll go into later. Uh up here we've got the LCD cuz we've got

**Dave Jones:** to have an LCD display to display the voltage and current and all sorts of other stuff. It's a nice squared C one. We'll go into that. Some push button switches, rotary encoders down here, two of them, one for voltage, one for

**Dave Jones:** current. I decided not to use the more expensive uh 10-turn pots. Um up here I've added a 5-V USB um output connector on the front panel with some um iPod kind of compatible uh things in there so it can uh tell an iPod that it's a

**Dave Jones:** genuine charger just so that you can uh power 5-V USB devices directly. There's a couple of voltage regulators up here. And here I've added I've really gilded the lily here. I've added what is essentially one of my microcurrent

**Dave Jones:** devices into the design here. So, I think this is probably one of the first uh power supplies bench power supplies on the market that I'm aware of anyway that can measure down to microamp output current. So, I can do a massive range uh

**Dave Jones:** from anywhere from a couple of microamps all the way up to a couple of amps with full resolution and full accuracy. So, that's a little nicety I've uh gone to the trouble to add there. We'll take a look at that, but that's the basic block

**Dave Jones:** diagram. In the previous design, we used a a very uh crude uh differential amplifier here for the current shunt, and that's not very accurate at high resolution stuff, 10- or 12-bits, which we're trying to do here. It's It'd be okay for 8-bit or

**Dave Jones:** something like that, but so I've decided to add a uh Maxim uh uh current sense amplifier specifically current sense amplifier specifically designed for the task and it does a really nice job. It's only a dollar or a dollar fifty or something like that. So,

**Dave Jones:** it's you know, it's a reasonable price, but it's very accurate and does a really good job. The current shunt resistor here, I've actually made up. Um I've Well, when I've laid out my board, I've put in uh 10 half watt half watt

**Dave Jones:** resistor um footprints in there so that uh you can basically get better than your uh 1% uh typical tolerance because it's quite difficult to get an accurate precision current shunt resistor like half a percent or point one percent or point

**Dave Jones:** two or something. It's very difficult to actually get those. They're very difficult and expensive to source. So, I've put 10 resistors uh in parallel. So, hopefully, if you see my previous videos on the Gaussian resistor response, we should get better than the

**Dave Jones:** typical 1% resistors we're using the tolerance there. Now, because we've got an intelligent controller over here, we don't really need technically need um a high precision accurate resistors in all of this power supply design because we can all we can calibrate the thing and

**Dave Jones:** compensate for that in software, but I that's just not nice. I didn't want to have to do that. So, I've made this overall design fairly high precision. So, I've used a 0.1% um high side current sense amplifier here. I've used

**Dave Jones:** 0.1% resistors elsewhere in the circuit down here as we'll see. Um and the current sense resistor, well, we'll see what we can get when we actually build the thing up, but I'm going to try and get it as accurate as possible.

**Dave Jones:** Now, you notice on my schematics that I've added these uh notes in various uh places here and I love doing that sort of thing cuz it just uh put formulas and things like that in little uh boxes next

**Dave Jones:** to uh the next to the actual pin that you're actually uh talking about and it just helps explain the schematic and when you come and look at it later, all the formulas are there, and you don't have to do the calculations. It's all

**Dave Jones:** done, and little notes and things, you know, you might add a star ground over here, so you put little notes and current values and things like that. That's just a nice touch to add to any schematic that you're actually doing.

**Dave Jones:** So, we're using a maximum 4080F high-side current sense amplifier, and that's got a fixed gain of five. It's basically a differential amplifier, and so it measures the differential voltage across a high-side current shunt resistor we've got here, and it

**Dave Jones:** multiplies by five, and it gives you a direct voltage output referenced to ground, and that's all it is. Very simple device, and this is a quite a precise one, and it's 0.1%, so with a gain of five, we can do various

**Dave Jones:** calculations up here for various current shunt resistor values. Now, I'll just mention that I'm actually using a 2.048 voltage reference here. It happens to be an ISL2107 over, but it can be any one on the market, really. It's, you know, it's not

**Dave Jones:** too bad. It's 30 ppm plus minus 0.25 0.25%. Now, why I'm using 2.048 V instead of the more traditional 2.5 V voltage reference is because then the values that we're going to get out of our analog-to-digital converter are going to

**Dave Jones:** be spot on. We don't have to fudge them or do anything like that. Now, I'll give you an example of that. Let's say we use a 2.5 V voltage reference, okay? And we're using a 12-bit analog-to-digital converter. There's

**Dave Jones:** going to be 2 to the power of 12 or 4,096 different steps in that analog-to-digital converter. Now, if we divide our 2.5 V maximum input to our analog-to-digital converter, cuz we're using a 2.5 V voltage reference, divide that by 4,096

**Dave Jones:** steps, you end up with some weird-ass value here of 610 or thereabouts microvolts per bit resolution on your analog-to-digital converter. And that's well, that's hopeless, you know, if you feed in 100, you know, if you're measuring 100 bits

**Dave Jones:** out of something that represents a voltage of, you know, 61.035 millivolts. It's not a nice round number. It sucks. So, uh and you have to compensate for that in software. You've got to actually do some math in software. It's

**Dave Jones:** not that bad, but there's a reason they make these voltage references which correspond to the like a power of two to match your analog-to-digital converter. In this case, 2.048 volts, but you can get 4.096 volt voltage reference. But, 2.04 volts is more

**Dave Jones:** common. So, we're going to use that. So, look what happens if you're using 2.048 volts, okay, on maximum ADC value and you divide that by your 4,096 bits, bingo, you've got a nice round number of 500 microvolts per bit. And if you have a look up here

**Dave Jones:** of when you translate this into your current shunt values, you end up with a very nice round 500 microamps per bit resolution. Or if you use different values, you can have 1 milliamp per bit resolution precisely from the output of

**Dave Jones:** your analog-to-digital converter. And that works out really nice in your software. I love it, and that's why I've used it. If we take a look at our current shunt resistor here, let's take a value of 2 ohms. If

**Dave Jones:** you put 10 in parallel, you're going to get 0.2 ohms current shunt resistor. Now, I put up here for a gain of five in this MAX4080. Remember, it's built-in gain of five. You can get different versions uh gain of 20 or I think a gain of 60, but

**Dave Jones:** we're going to use a gain of five and I'll tell you why in a minute. And uh that out for a that will give us because it's a gain of five, okay, 0.2 ohms. Let's say an amp uh through it is 0.2

**Dave Jones:** volts multiplied by gain of five is 1 volt. So, you're going to get out of your uh current shunt your uh current sense amplifier right here, you're going to get out 1 volt per amp output. And of course, that will give you a range

**Dave Jones:** because you're using a reference voltage on your analog-to-digital converter, it's going to give you a range a usable measurable range of 0 to 2.048 amps. And that translates to 500 microamps per bit resolution. And you can go through Let's say you wanted to

**Dave Jones:** use a uh 3-amp version of this LT3080, the LT3083, then uh you could say set it for a 4-amp current range and you'd get what still get an excellent resolution of 1 mV per bit. Awesome. And because you've used 10 resistors in

**Dave Jones:** parallel like this, say at half of what each are, you might have a 1-W resistor in there, then you might have 5 W or 10 W dissipation capability in your current shunt resistor there, and that's plenty. So, this current shunt resistor isn't

**Dave Jones:** going to heat up at all, so you can use um you know, fairly low-grade ones and they're going to work quite well. They're not going to change much with temperature because they don't heat up much. Let's take the example of the 2-ohm

**Dave Jones:** resistor here. If we've got 2 amps flowing through it, I squared R, 2 squared is 4 and * 0.2 ohms, we're only going to dissipate 0.8 W in all of those resistors. And we've got if we've got 5

**Dave Jones:** W total capability or 10 W, not a problem whatsoever. It's not going to heat up much at all. Now, of course, the value of your current shunt resistor is going to determine how much voltage drop you get across there, and depending on

**Dave Jones:** your input voltage over here, depending on what you power it from, that may be an issue. In this case, if we use a 0.1 ohms, then we're only Well, in either of these two cases up here, we're only talking

**Dave Jones:** about a 0.4 volts maximum drop, which really isn't that bad at all. And you don't want to make it too low and use like a gain of 20 here or a gain of 60, because then you can start getting right

**Dave Jones:** down into the noise, and you can get errors and issues like that. So, you really don't want to go there. You want to tolerate You want to get as maximum voltage drop across your current shunt resistor as you can tolerate and the

**Dave Jones:** lowest gain here, so you minimize your errors. So, how much error can you tolerate in this amplifier here? What's the minimum? Well, it depends on your specs and what you're willing to whether or not you're willing to compensate for

**Dave Jones:** it in software, which I don't really want to do. I want to try and get the maximum uh uh possible absolute accuracy out of this thing. So, the input offset error of this amplifier is going to matter. So, you can't make this resistor

**Dave Jones:** shunt resistor arbitrarily small, because then the voltage drop's going to be so small, it's going to be swamped by the input offset voltage of this op amp of this amplifier here. So, what's the minimum that we can tolerate? Well, it's

**Dave Jones:** a basic rule of thumb is that well, you don't want it to be any more than one bit resolution on your analog-to-digital converter. You want to be able to measure accurately down to your last bit. Why not? So, in this case, we've

**Dave Jones:** got a 500 microamps per bit. So, 500 microamps is the minimum we can measure. So, if we do 500 microamps here times our 0.2 ohm resistor there, we're basically going to get 100 microvolts drop across this resistor here. So,

**Dave Jones:** that's the minimum that we're going to get 100 uh microvolts. So, let's go over to our data sheet here for our MAX uh 4080 device. And what's its input offset voltage? Huh, what a coincidence. It's 100 microvolts. Typical, you could go

**Dave Jones:** into there. Uh but it's going to be 100 micro microvolts input offset voltage. So, as you can see, the MAX4080 is almost ideal for this. Its input offset voltage is exactly the same as uh our minimum voltage on our input

**Dave Jones:** here. That's pretty good. I mean, ideally, you know, if you're designing a really high precision thing, you'd want it to be uh maybe an order of magnitude lower, you know, uh order of magnitude lower or something like that. But in

**Dave Jones:** this case, perfect. Good enough. We're happy for a one-bit uh error there. And of course, the input offset voltage is just that. It's relative to the input. So, this amplifier has a gain. So, the actual um output uh uh the area going to get on the

**Dave Jones:** output is the input offset voltage times five, which is 500 microvolts um error on the output. But because um it scales up five, we're still only talking about one bit uh error there caused by our input offset voltage. Beautiful. And as

**Dave Jones:** I said, you just can't make that resistor arbitrarily low cuz not only is there input offset voltages, but then you get um uh noise and things like that causing issues. So, there you go. That's almost perfect, that device.

**Dave Jones:** And just to get rid of any noise, I've added just a little um RC low-pass filter there, which then goes down into our existing circuit, which we've seen before, our um our uh constant current um comparator down the bottom here.

**Dave Jones:** And not only that, if you look at the net name there, it also goes over to our uh analog-to-digital converter over here, one of the channels. There it is, ADC I out. Now, speaking of the ADC, we've used a

**Dave Jones:** four-channel one here, and so it's going to measure Not only does it measure the outputs current via here, it also measures the output current from this micro amp circuit over here. So, I can measure the current two different ways,

**Dave Jones:** either in series with the output like that. Well, they're both in series with the output. I'll explain this one later. But, it measures the output from the micro current, and it can also measure the output voltage, which we'll take a

**Dave Jones:** look at there, and also the ADC input, the voltage input as well, coming from your source. So, then your software is able to determine whether or not it's got adequate voltage and whether or not this regulator is going to actually drop

**Dave Jones:** out. So, our 2.048 voltage reference here goes into the DAC over here, the 12-bit DAC, and it also goes over to our 12-bit analog-to-digital converter here, and both of those are devices from Microchip. This is The DAC is an

**Dave Jones:** MCP4922, and the ADC is an MCP3204. So, why did I choose this specific analog-to-digital converter and DAC? Well, let's find out. Let's go and do a parametric search in Digi-Key here. Let's search for ADC, and we'll go down

**Dave Jones:** here to analog-to-digital converters, ADC. There we go, almost 12, 13,000 of them. Can you believe it? And here we go. Here's our parameters. We want a 12-bit converter only. There's no point searching for all the others, so let's

**Dave Jones:** drill that down. Bingo, we're still got 4,434 different converters. Well, because this is a kit, we only want through-hole, so we'll select through-hole over here, and we apply the filter, and bingo, we're down to 439 ADCs. So, from these particular

**Dave Jones:** manufacturers, Microchip, I like them, National, Texas, you know, all the biggies are there, Linear, Analog Devices. But, uh let's sort by price because, well, really, I uh I do care about uh I do care about price. So, let's search for that. Let's say we're

**Dave Jones:** going to make 100 kits. Let's sort by price based on 100. And uh bingo, what comes up first? Not terribly surprising, Microchip. They make pretty cheap uh analog parts. People think they People mostly know them for their uh

**Dave Jones:** uh PIC microcontrollers and stuff like that, but they make some uh pretty cheap analog stuff. I'm finding I'm using more and more of them uh lately. So, basically, uh let's have a look at the number of converters. It's only got one.

**Dave Jones:** Bang. Uh not too happy with that. We want uh Basically, we want something with at least four channels in there. So, let's select that. Hey, what's going on? No, I pretty sure there's a Microchip one in there. So, something's happened

**Dave Jones:** to that Digi-Key search. I don't know what's what's gone wrong there. Something horrible. But, uh here No, here we go. Uh look, they've Digi-Key's got it wrong. Here's my converter. It's a four-channel. It's only got one number of converters, one. Wow, fail. Okay, so

**Dave Jones:** much for that. But, there you go. The cheapest device is there. Um these are single-channel, dual-channel. And the cheapest uh device, four-channel ADC we can get, is a Microchip MCP3204. And bingo, that's the one I used purely because it was the cheapest in quantity.

**Dave Jones:** It's $2.40 in 100 of quantity, which is, you know, expensive, but it is a 12-bit uh converter. The next uh nearest brand is um Analog Device Sorry, Texas Instruments ADS7822. Um but, that that won't be a four-channel in an eight-pin

**Dave Jones:** package. So, really, you know, there's no competition. The prices start going up and up and up. So, that's why I chose the Microchip, and I did exactly the same thing for the DAC, and the matching Microchip DAC, unsurprisingly, I guess,

**Dave Jones:** came up as the cheapest again. So, that's why I used them. That's parametric search. And if you're wondering why I just didn't use a microcontroller with a 12-bit analog-to-digital converter and PWM in it, well, let's take a look. I've gone

**Dave Jones:** through and selected all the DIP devices here. You can't select through holes, so I've just one DIP microcontrollers. I'm searching through the 32,000 microcontrollers available from Digi-Key, any brand, any manufacturer. So, let's take a look over here, ADC at

**Dave Jones:** 12 bits. 12 bits, 12 bits. It's It's a bit tedious. You have to go through and select your 12-bit ones in here. But, if we do that, and then if we go through and select just the ones in here with 12-bit ADCs,

**Dave Jones:** let's not worry about the PWM at the moment, cuz that's harder to find, but let's just, as a first pass, find ones with 12-bit analog-to-digital converters. What have we got? We've got Freescale, and we've got Microchip. That's it. So, all you Atmel fanboys out

**Dave Jones:** there, don't come running why I didn't use some Atmel thing, or some or if you're a TI fanboy, why I didn't use those? Because they're not available with a 12-bit ADC in a DIP package. So, there you go. And if we go along here,

**Dave Jones:** and we probably search for, say, the uh best price over here, let's 100 of quantity. Let's have a look. It happens to be the Freescale, the HCS08. Time That's a going to be a tiny a tiny little device. That's only a

**Dave Jones:** 16-pin DIP. Not enough pins, 28-pin DIP. Um may or may not be enough. You know, it's just I don't know. And then you get into the PIC devices here, and there are quite a few PIC devices available with

**Dave Jones:** 12-bit analog-to-digital converters. But if you want one with a decent number of pins, and then you'd have to go through and look at the ones that actually have a 12-bit capable pulse-width modulation output, it just gets trickier and trickier. And well,

**Dave Jones:** it was just all too hard. So, I just decided, simply decided to use an external ADC and DAC. And generally, anyway, you're going to get better performance with an external ADC and DAC. The ones built into microcontrollers, they're great. So,

**Dave Jones:** when you start trying to push 12 bits inside a microcontroller, you know, you're probably better off going to external. 10, that's why most of them only have 10 bits cuz that's generally all they're good up to. Now, you see that I've got a couple of

**Dave Jones:** voltage buffers down here driving the ADC like this. Now, there's a reason I've actually got that is because when you got a successive-approximation ADC like this, you can't have an arbitrarily high input impedance. So, in this case, ADC V out is coming from over

**Dave Jones:** here. Look at these 10k resistors, okay? We've got a relatively high input impedance driving this um analog-to-digital converter. And this has sample and holds in here, and it can cause you all sorts of problems. So, it's good practice to actually buffer

**Dave Jones:** that so it provides a low-impedance drive to your analog-to-digital converter. These ones here don't need it because it's coming directly from the output of the op amp here through three a little low-pass filter of 330 ohms here. Not a

**Dave Jones:** problem, that's low enough not to cause an issue. And the other comes from the ADC I out, which is the current we looked at before. And once again, it's 330 ohms, low enough not to cause an issue. And as always, read the data sheet.

**Dave Jones:** Here's the ADC, the MCP3204, which is the four-channel version. Also available in eight-channel version. It actually warns you about high input impedances. And here's the equivalent circuit of the analog-to-digital converter. And as you can see, it's got an inbuilt sampling switch here with an

**Dave Jones:** internal series resistance of 1K. And then it's got a 20 pF sampling capacitor on here. And basically, your input impedance, which I just talked about over here, here's your input pin. So, this is all inside of the all inside of the analog-to-digital

**Dave Jones:** converter chip. So, your external impedance here will actually affect the time that this capacitor takes to charge up. So, that's charge up to the value. And if you've got a 12-bit converter, it's got to get very close to the

**Dave Jones:** nominal value not to introduce any additional errors into your analog-to-digital converter. And if you take a look down here, they actually provide you a graph here. So, that actually shows you the input resistance in ohms, 10K here, 1K here, down to 100 ohms down

**Dave Jones:** here. And the maximum clock rate in megahertz at different voltages. And as you can see, if you're operating in a low voltage, we're operating at 3.3 volts. So, it's going to be like in there somewhere. It's going to be

**Dave Jones:** another curve which goes in there and down like that. As you can see, if you've got a 10K input impedance, it's useless to you can't get a 0.1% least significant bit deviation on this thing. So, the input impedance matters. In

**Dave Jones:** practice, we may not um, need these op amps down here. And if we don't need them, well, we can just not insert it and then just short out pins two and three and five and six there. Not a problem. But good practice

**Dave Jones:** to put it in if you need it based on your input resistance cuz that can affect your maximum sampling rate. And by the way, it's not just specific to this analog-to-digital converter, either. If you use the one inside your

**Dave Jones:** microcontroller, you would have the same issue. Just be aware. Now, I've actually used a really cheap garden variety, uh, op amp here. It's an NMJ, uh, 14558. It's a variation on the, um, very common 4558 op amp. And this one has, um, five

**Dave Jones:** a nominal, uh, value, not a maximum value, but nominal of 500, uh, 500 microvolts, um, input offset voltage. So, that should be good enough for our circuit, but as always, it's a standard pinout. If we need to put, uh, really,

**Dave Jones:** um, better precision op amps in there, we just drop them in. And as for our 12-bit DAC over here, well, it's pretty darn boring. There's some digital input lines here. It's an SPI, so we've got a clock, a chip select, and, uh, data

**Dave Jones:** input, a voltage reference input, bypass cap, and it just outputs two different voltages. It's a dual channel 12-bit DAC, this one. It's quite nice. Uh, well, for the price, it's really cheap. And, uh, and so, that just generates our voltage Vset and Iset

**Dave Jones:** exactly as we would if we hooked a pot onto here like we've seen in the previous videos. Or we use a pulse width modulation output from our digital, uh, or from our microcontroller here. We could also drive it. Um, but a nice,

**Dave Jones:** good 12-bit resolution DAC, that gives us some great resolution on the output. And as for our current resolution, well, we've already looked at that. We can actually set, um, the current limit in steps of 500 microamps. Brilliant. Over

**Dave Jones:** the whole range of 500 microamps to 2 amps. Fantastic. That's the advantage you get with the 12-bit analog 12-bit DAC. If we used a 10-bit DAC, you'd be looking at 2 milliamps per bit. Not as good, but still, you know, might

**Dave Jones:** be certainly adequate. So, I've just gilded the lily here. You could have just used the microcontroller for sure. Depends on your requirements. Now, as for our voltage output, well, our DAC is going to give out 0 to 2.048 V cuz

**Dave Jones:** that's our voltage reference coming in here. So, 0 to 2.048 V. I've put in a gain of five here in this amplifier set by these two resistors here. Exactly the same circuit you've seen before. The tap actually comes from

**Dave Jones:** here, so it compensates for these series resistances here. But, that circuit has a gain of five. So, once again, I've put an engineering note in there, and there it is. Gain equals five, 0 to 2.048 V input, which gives a 0 to 10.24 V

**Dave Jones:** output with 2.5 mV resolution for our 12-bit analog-to-digital converter. So, we can set our output our voltage output up here on the supply in steps of 2.5 mV. Awesome. And of course, if you used a 10-bit DAC or a 10-bit PWM in your

**Dave Jones:** microcontroller, you would get a 10-mV resolution output. Once again, that's still adequate for most purposes. I'm just gilding the lily. Some of you might be asking, "Why have I put two resistors in parallel here and two resistors in series?" Well, if

**Dave Jones:** you'll note, they're both they're all 10 K. I've tried to basically optimize my design to reuse existing values on my sheets here. So, I've got you know, 10 K up there, 0.1% cuz these resistors are fairly, you know, fairly expensive cuz

**Dave Jones:** they're 0.1% tolerance. So, I've just used them. It's better I think it's better to use them and reduce more of them and reduce your bill of materials than it is to have all these different values. And over here, which we'll look

**Dave Jones:** at later, I've also used 10K there as well and 10K here. So, I bought, you know, you can buy a whole bunch of those, so you can consolidate your bill of materials and you only have to buy the one item. That's not bad. So, I've

**Dave Jones:** done that up here, like for this last time you'll notice that I set my current um fixed current output here, the LM 334, to 1 mA, but that required an oddball value resistor here I'm not using elsewhere on my circuit. So, I

**Dave Jones:** decided to use a 100 ohm I am using elsewhere in the circuit, and it's still good enough, 677 microamps, good enough for a minimum load on our LT3080. Component consolidation is one of those steps you should do in any good design.

**Dave Jones:** So, you'll see not only the resistors I've done that, but also elsewhere on the circuit I've done that for the capacitors as well. If I needed 4.7 microfarads, and I don't use it anywhere else, well, but I've used 10 microfarads

**Dave Jones:** somewhere else, well, I'm going to use a 10 microfarad in there instead of the 4.7. And for output protection, I've got a big nice 5 amp reverse Schottky diode there. Now, this is the output I'm going to have a load switch external to the

**Dave Jones:** board, it's not actually mounted on the board, and that's why it's not shown here. And you'll note that I'm this is my sense line that senses the output voltage goes back to the analog-to-digital converter down here. This net here goes down to the ADC. Now,

**Dave Jones:** the reason I'm doing that is because some people like to have the sense line directly on the output, so that it still reads the voltage when the switch the load switch is open. Others prefer it the other way around. They'd like to

**Dave Jones:** know what the output voltage is going to be before they or or what the output voltage actually is regardless of the load switch position. So, um this just having a separate sense line gives people the flexibility to wire it up

**Dave Jones:** anyway they like. And once again, I've just got some voltage divider resistors here, and that will give me a certain voltage into my analog-to-digital converter scaled down to meet my 2.04 V voltage reference. And more than that, it is precisely the voltage here is

**Dave Jones:** precisely 1/5 of the output voltage. And coincidentally, remember I had a * 5 gain over here. So, once again, my that scales perfectly. My If my max output voltage is 10.24 V / 5, the max input to my ADC is going to be 2.048

**Dave Jones:** V or that the output voltage divided by 5. So, it's perfect. I'm using the full maximum range of my analog-to-digital converter to measure my output. And that's what you want. You don't want to piss away any bits. Now, as for the current limit LED

**Dave Jones:** indicator over here, you know how I used this convoluted op amp before. I just wanted to show you that you could actually do that as a spare op amp, but that's not the nicest way. It's better to actually use a second transistor here

**Dave Jones:** and drive it direct. And that's exactly what I've done on the circuit here. Here's my current my current limit comparator down here. And as well as driving the as well as driving the set pin as per normal, it also drives a separate second

**Dave Jones:** transistor here because we're already used them. Same type, very cheap, you already got them. And that current limit goes into your microcontroller over here. It doesn't go directly to a LED. I decided to put input pin, and then you

**Dave Jones:** can the software can do intelligent stuff with the LED. It can blink it and do all sorts of things depending on various modes. So, there you go. And you don't need a pull-up resistor on there because you can program a pull-up

**Dave Jones:** resistor directly on your microcontroller here. And you'll notice the same with the optical rotary encoders. They got two outputs here. They go directly into the microcontroller. Normally, they need pull-up resistors on there, but do it inside the micro. No problems. Save a

**Dave Jones:** couple of resistors, save some board space. Now, let's take a look at this effectively a microcurrent circuit here, which allows us to measure if your if this lab power supply is powering your little microcontroller circuit and goes into sleep mode, well,

**Dave Jones:** you don't have to use your multimeter. This sucker, this power supply will be able to actually measure low values. Not as good as the microcurrent. It only goes down to a maximum of 2.5 microamps per bit, as we'll go into, but still, I

**Dave Jones:** don't know any other power supply that can measure the output current down to 2.5 microamps. And the way it does that is it basically this circuit doesn't operate all the time. This circuit will only effectively be in use when you want

**Dave Jones:** to measure and you want to measure low values and your microcontroller knows that the values are very low, it can switch this circuit in. And it does that with this MOSFET here. I can switch on this and effectively insert another load because

**Dave Jones:** our output voltage is here's our output voltage here, but the ground, here's our output, our negative output terminal. Instead of going directly to ground, it goes through a current shunt resistor here, a what's called a low-side as opposed to

**Dave Jones:** the high-side current shunt resistor we have up here. We have an additional low-side one. And normally, I don't like doing that because then it introduces an offset voltage error here from ground and depending upon your output current. That's why at very high output currents,

**Dave Jones:** we don't want to go through this resistor here. We want to shunt that Excuse the pun. We want to shunt that through a much lower value MOSFET here so we don't get any errors introduced on our low side. It's going to be

**Dave Jones:** effectively ground. So, let's say we want to only tolerate one bit resolution error on this output. What value do we need? Well, our output voltage is maximum output voltage is 10.25 V, 2.4 V, sorry, divided by 4096. We've got a 12-bit converter. So, 2.5

**Dave Jones:** mV. So, basically, our ADC down here can measure our output voltage to 2.5 mV resolution. So, it'd be nice if this circuit here only dropped 2.5 mV or one bit or less. So, pretty much, we want 2.5 mV maximum drop across this MOSFET

**Dave Jones:** here when it's switched on and all this circuit is disconnected on our high current range. Our maximum resistance there is going to be 2.5 mV divided by the 2 A maximum current there, 1.25 mΩ. So, our FET there needs one bit error is going

**Dave Jones:** to need 1.25 mΩ. So, that's actually a very low value for a MOSFET. If you actually want to meet that, you need a really, really beefy MOSFET. I've decided to use one of these. It's cheap, readily available, in

**Dave Jones:** a nice package. I like it. And it's going to be near enough. It's got a rated maximum RDS on or a maximum maximum resistance of 8.4 mΩ, but that's going to be at the maximum current. It's going to be better than that at the lower

**Dave Jones:** current and at higher VGSs as well or higher gate source voltages. So, in any case, that MOSFET should give us a a very insignificant error at our maximum range of 2 amps. So, as I said, the software is capable of switching this MOSFET on

**Dave Jones:** and to do that, I've actually to get a higher um gate source voltage, I've actually used, rather than drive it directly from the microcontroller, which would only be a 0 to 3.3 V output, that's not really good enough for this

**Dave Jones:** MOSFET. I really want it a nice high value. So, I'm going to tie it to V+ here and I'm going to use an external transistor to turn it off and on. So, the gate voltage is going to go between

**Dave Jones:** 0 and V+, which is our input all the way over here. So, we're getting a nice high gate source voltage because the higher the gate source voltage, the lower the turn-on resistance for this MOSFET. So, you want it as low as possible. And

**Dave Jones:** during that 2 amp range, this circuit isn't used at all. It's still measuring. It's trying to measure something, but we don't read it at all. The micro doesn't read it. We're doing our measurement based on this high side

**Dave Jones:** uh current shunt resistor. So, we've effectively got two different current measurement ranges. So, let's have a look at the low value current measurement when this circuit is active. Now, what we've got here is we've got four resistors here, 1 ohm, and they're

**Dave Jones:** in series parallel combination giving a total shunt resistor here, low side shunt resistor value of 1 ohm. Now, the reason I'm using four like that is, well, not only to get a little bit extra accuracy like we did with the high side

**Dave Jones:** current shunt resistor, but a bit of margin for error in case this software selects the wrong range when it's when there's actually a high output current. So, in this case, let's say it was 2 amps maximum like that.

**Dave Jones:** Then, in theory, if the software accidentally turned this transistor off instead of on, then all that current would try and flow through the would flow through these resistors here and we would get a power dissipation in those resistors

**Dave Jones:** of 4 watts. So, really, you know, if you put a tiny little resistor single resistor in there, you might burn it out accidentally. You don't want that to happen. So, a couple of extra resistors it's, you know, it's going to survive

**Dave Jones:** anyway. It's still not going to be great. It's going to be very, very hot, but at least survive and it won't blow those resistors. So, if we've got a 1 amp current shunt resistor here and 1 milliamp flows

**Dave Jones:** through there, we're going to have 1 millivolt across here. This op amp, the MAX4238 you've seen in my micro current, it's exactly the same. It's got a gain set by these two resistors here of 200. It's quite a high gain. And so, if we've got

**Dave Jones:** 1 millivolt drop across the shunt resistor, we'll get 0.2 volts output. So, my little engineering note here says it again, the 200 the Vout equals 0.2 volts per milliamp flowing through here. And that can from that we can determine

**Dave Jones:** our maximum range cuz our ADC down here, remember it's only 2.048 volts maximum. So, we can only tolerate that voltage or it can only read that voltage maximum. So, we can have 10 times that or roughly 10 milliamps or if you want to round it

**Dave Jones:** off, 10.24 milliamps maximum is what this circuit is capable of measuring. So, the microcontroller, when it when it measures over here on this shunt resistor that the current drops below 10 milliamps or you can do it under manual control with one of the

**Dave Jones:** switches here. It can automatically, if it wants, switch on, disconnect this MOSFET, and then start reading from this circuit over here. So, if you're Let's say your circuit's powering your microcontroller, but this power supply is powering your microcontroller circuit that's just gone

**Dave Jones:** into sleep mode, the software of this power supply can detect that, and it can switch on this circuit and measure that sleep current accurately. I think that's brilliant. Why can't all power supplies have a feature like that? So, just like

**Dave Jones:** the high-side current sense amplifier, what is the maximum input offset voltage we can tolerate here before we start getting errors? Well, if our maximum output is 2.048 V, okay, we divide that by our 4,096, we're getting 500 µV

**Dave Jones:** is our minimum on the output here. So, we're going to read a 500 µV per bit, one bit resolution here, but we've got a gain of 200. So, let's divide that by 200, okay? And it can tolerate and that

**Dave Jones:** translates to 2.5 µV is our minimum per bit value across here. And of course, the only way that you're going to get an input offset a voltage error pretty much of two point down in the order of 2.5

**Dave Jones:** µV, as you've seen in my microcurrent, is to use a is to use a chopper amplifier and auto-zeroing amplifier, which is exactly what the MAX4238 is. And what is its value? An ultra-low 0.1 V µV offset voltage. More than an

**Dave Jones:** order of magnitude more than what we need, but that's typical. But its maximum at ambient temperature, or even over the full temperature range, is about 2.5 µV. So, over the full temperature range, we're only going to get one bit error. Fantastic. More than

**Dave Jones:** what we need. A little bit overkill, but hell, I already used that in the micro current, so we're going to use it here again. Now, because I wanted to make this design into a kit, I wanted all the

**Dave Jones:** components to be through hole, and I tried as hard as I could to make everything through hole, but unfortunately, the MAX 4238 is only in an SO8 package, and likewise, the MAX 480 is only in an SO8 package,

**Dave Jones:** and the voltage reference, although I can get ones in like a TO92 package, they're cheaper and more readily available, especially in the 2.848 V version, in a SO23. So, they're the only three surface mount parts on the entire design.

**Dave Jones:** Everything else is through hole, and I pretty much optimized I chose parts based on through hole availability. There were maybe one or two others on the market for the current sense amp, but they weren't quite right and didn't have the right gain, and it

**Dave Jones:** didn't work out the values, and it just wasn't nice. I was pretty much forced to use an SO8 there, and pretty much an SO8 over here, and because I've used the chip before, ah well, you can't have everything. You

**Dave Jones:** have to if you go on build this thing up, you're going to have to solder a couple of SO8 packages. Sorry. And I've got a little MAXIM MCP1700 3.3 V voltage regulator. They're they're quite nice devices. They're actually got very

**Dave Jones:** high very close output tolerance of a percent or less, or half a percent. They're really really quite nice neat. You can actually use those almost as a voltage reference at an ambient temperature. I think I've mentioned that before, but anyway, I've got a standard

**Dave Jones:** LM7805 to give our 5 V out from our US for our USB output connector over here. And because I've This is the heat sink. I'm actually using it's from Altronics here in Australia. I don't think you can buy it anywhere

**Dave Jones:** else. I think it is specific to them. It's a PCB mount one. It's got PCB pins. It's upside down there cuz it was in my breadboard before, but it's got an extra hole here so I can mount both devices on

**Dave Jones:** the same heat sink. But, uh-huh, just be careful. You don't want to put them directly on there like that because then you'll short out the tabs which are connected through to the center pin and in this case it'll be

**Dave Jones:** ground and output which you'd be shorting. So, if you put this um uh, package here on if you put both these packages on the same heat sink, you'd actually be shorting the output of your LT3080. So, oops, you don't want that.

**Dave Jones:** Make sure you put some mica washers or some seal pad in there to isolate them from the heat sink. Now, as you'll see down here with the micro, I've actually used every available pin, every single one of them. And I probably goofed up

**Dave Jones:** here. I think I'm actually going to change it because I thought I could get away with using the 8 MHz internal oscillator in here and it'd be good enough to do my external serial RS232 comms, but to do RS232 as a rule of thumb you need

**Dave Jones:** a 1% tolerance frequency error or better and the oscillator in this thing can be trimmed to 1% or better in that software. You can actually software trim it, but it's not as good as the PIC one. I've done this on the PIC before and they

**Dave Jones:** come factory trimmed to 1% or better. So, out of the factory over temperature you can actually fairly reliably do RS232, but I don't think that's the case for the Atmel. So, probably going to have to use I'm going to have to free up these

**Dave Jones:** two pins down the bottom and put a oscillator on there, the external 8 MHz oscillator on there or 16 or whatever you want to use, which is Arduino compatible. You can use either and change it, but I'll probably use a

**Dave Jones:** ceramic resonator. They're at 8 MHz. So, I've got to free up two extra lines here so I can get that precision RS-232 serial comms out of here, I think. It's just You know, it's good practice. One of those ceramic resonators, you'll

**Dave Jones:** get, you know, easily get to half a percent tolerance on those, so more than good enough for RS-232. Now, the reason I've added a separate serial port here, it'll be a separate board, because really I want it to be able to do a

**Dave Jones:** whole bunch of things, be it just a standard, you know, 9-pin RS-232, you know, have an RS-232 chip or a 9-pin serial interface, or you can have electrically isolated. Because of a power supply, you can get major problems

**Dave Jones:** if you if you your connectors on the back are referenced to the computer, which is referenced to mains earth. That can be a big problem. So, electrical isolation can be a big issue. So, you can build a separate board with a USB to an isolated

**Dave Jones:** USB interface to RS-232 if you wanted to, or you could use one of those XBee wireless boards or something like that. So, this could be a wireless controlled power supply. That'd be awesome. There's no reason why you can't do that at all.

**Dave Jones:** That'd be fantastic. So, to free up these pins, basically, my DAC up here and my ADC over here, they're both SPI input devices, and because I had enough pins available, I just drove them separately. But, what I'm going to

**Dave Jones:** have to do is actually combine the clock pin on both. So, instead of having a separate clock pin coming from the micro, I'll have the same clock pin and I'll have the same data input pin as well. They can be shared and I'll just

**Dave Jones:** have a separate chip select pin for each separate chip select for each for the ADC and DAC. And that should do it. Bingo, I free up two pins so I can put the ceramic resonator and we're all sweet for our RS232

**Dave Jones:** and Arduino compatibility. And I've got the external AVR ISP interface here so you can program the chip in circuit and download your hex code to it. No problems. For the LCD display up here, I've chosen a Newhaven display. I rather

**Dave Jones:** like them and they're one of the LCD manufacturers that I like. Their displays are quite neat. And what it is is it's an I squared C interface. There it is, SCL and SDA. That requires less pins on your microcontroller so I freed

**Dave Jones:** up pins here rather than using the standard parallel or full bit interface one. I can get away with just well, three lines actually. There's an LCD reset line as well but that wasn't the only reason. Here it is.

**Dave Jones:** It just so happened that this LCD fits nicely into the case that I'm using. It was exactly the right dimensions and it's a 20 character by two line because I figured 16 by two probably wouldn't give be able to give

**Dave Jones:** the status displays that I actually wanted. So it's a 20 by two line display, I squared C compatible input. It's only about eight or 10 bucks or something. It is the most expensive component in the whole in this entire power supply project but

**Dave Jones:** you've got to have a decent display. This is actually an RGB backlight one. I didn't want that but that's the only one that they had in stock for a couple of months. So I'm I'm using the backlight. It'll just be standard, but there you

**Dave Jones:** go. I pretty much a lot of my design design decisions for this entire project were actually built around the case the actual case I'm going to build this in and another aspect I haven't talked about the project which you'll find

**Dave Jones:** about out about in another video. And so I'll talk about that next time I think how to actually how I engineered this thing to fit into this case cuz that's really a very important decision and that drove a lot of the design

**Dave Jones:** requirements in terms of how many switches I use to fit on my front panel whether or not I had room for a USB output connector, you know, the type of heatsink I used the maximum power dissipation all sorts of stuff the

**Dave Jones:** room I had for the LCD for the controls how big I could make those the knobs how big they could be whether or not I could use 10 turn pots and everything just sort of you know pretty much revolved around the case I'm

**Dave Jones:** using. So this video's been long enough. I'll have to make that a separate video and I've already designed the PCB for this thing. I've got some time lapse video of me doing that. So there'll be a couple of

**Dave Jones:** more videos coming up. In fact, probably more than two or three coming up to finish off this power supply project. So thanks. See you next time.
