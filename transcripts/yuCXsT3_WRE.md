---
video_id: yuCXsT3_WRE
title: EEVblog #853 - How A Multimeter Works
url: https://www.youtube.com/watch?v=yuCXsT3_WRE
source: youtube-asr
---

**Dave Jones:** Hi. In a previous video, I showed that my Fluke 17B multimeter, which I basically have had just had sitting in a box here on the shelf, uh because it's not, you know, it's not something I typically uh use every day. I've got uh

**Dave Jones:** better, nicer meters than this one. But, anyway, um it looks like it is like died. It I don't know what has gone wrong with it. It's just been sitting in the box. Check it out. I mean, you know, it

**Dave Jones:** obviously like the uh the chip set's working, you know, the display comes on. It seems to do all, you know, it appears to work when you actually turn the thing on. But, like nothing. Look, zippity do da. And no,

**Dave Jones:** it's not the test leads. I've tried various functions. It just does not recognize anything at all. Has the input blown or something like that? I have no idea. As far as I know, I haven't used it for, you know, anything uh serious

**Dave Jones:** uh since I got it in uh a mailbag way, way back uh quite a few years ago now. And um yeah, I I think I did a uh quick teardown on it once, but that was like it. So, anyway, let's crack this sucker

**Dave Jones:** open and uh have a look. And of course, yes, this is the made-in-China Fluke. Um it's just like the original. This actually reminds me of the Fluke 19, which was Fluke's uh first uh foray into the Chinese-made multimeter market just

**Dave Jones:** to test the waters here. It was uh the Fluke 19 was uh here's a photo of it I grabbed from uh the internet. I don't have mine anymore, but I bought quite a few of these for work cuz at the time

**Dave Jones:** they were a big deal. They came out. It was like I think it was sub $100. And for a Fluke, that was absolutely incredible. You could buy it in the local Tricky Dick uh store, and it was Fluke's first entry into, you know, they

**Dave Jones:** were just testing the market to see if people would uh want or like a Chinese uh made Fluke. And they only sold it in Australia, a couple of other Asia Pacific countries and that was it as far as I know and it was a complete and

**Dave Jones:** utter failure. Oh, almost every one of them like died. They had this fault where the chipset would get killed. I can't remember the details but every one of the ones I had died. I've got tons of reports of them dead.

**Dave Jones:** They were at the time and this was probably back in the late 90s perhaps I think. It was a long time ago in a galaxy far far away but yeah, it was a miserable failure Fluke 90 M but

**Dave Jones:** obviously well, yeah, they did a second suck of the seven. Hey, we can still do this the Fluke 17 B. Just started out as the 17 then it went to the 17 B. I'm not sure. Anyway, let's crack this thing open and um

**Dave Jones:** see if we can find out what's wrong with it. And yes, the good thing is we have the schematic. Awesome. So, if you still got a working Fluke 19 B, well, you're one of the real lucky ones. You've got a rare instrument there

**Dave Jones:** because I think most of them on the market died. I'd love to find out the exact reason. It was something to do with the chipset ESD sensitivity or something weird like that. Anyway, this one failing just sitting on the shelf

**Dave Jones:** there does not instill a lot of confidence in me. Now, I don't know about you but that non-standard spacing on the amps jack there gives me the heebie-jeebies. All right, let's crack this thing open. Two AA batteries, lots of Chinese

**Dave Jones:** writing on there. Thankfully, you can understand the fuse ratings and uh let's whip it open. See if there's anything obvious in here. Give it the smell test. Nope, nothing smells burnt and nothing right off the bat. OH! OH!

**Dave Jones:** OH! D'OH! LOOK. Can you see what I see? Or don't see? D'oh! Well, there is your problem.

**Dave Jones:** That is hilarious. The screws are not on there. I think this is a massive PEBKAC. Um I've As I said, I think I've done a teardown on this before, and obviously, I did not put the screws back in.

**Dave Jones:** D'oh! Well, there it is. I fixed it. And I'm pretty sure it'll now work again. Yep. No worries. Well, I could have just deleted this video, but what fun's that? I've got a schematic. I can salvage this. I can salvage any video, no matter

**Dave Jones:** how tragic it is. All right, let's just I don't know. Have a look at things. Why not? Meh. And I just checked, and yep, I have actually done a full teardown video of this, episode number 344 to be precise. No wonder I don't

**Dave Jones:** remember it. I'm going to do this one day. I'm actually going to, you know, produce the exact same video I've done like 5 years ago or something, and I won't even realize. Anyway, um yeah, so I won't go into huge

**Dave Jones:** detail about the construction of this thing. I've done that in the previous teardown, I'm sure. Suffice it to say that that's one of the wimpiest 10 amp current shunts I've ever seen. Look at it. This little and neebic

**Dave Jones:** thing. And the other thing that strikes me about this is, of course, these adjustment pots. Look at them. 1 2 3 4 5 6. Is there Have I missed one? 7 8. Eight adjustment pots in this thing. They're adjusting for everything. Why

**Dave Jones:** are they doing that? Well, you know, like every modern multimeter, you know, no longer has They're all closed ca- what's called closed case calibration. I You don't have There's no pots inside to actually trim. But, this thing has

**Dave Jones:** trimming for almost everything. Why is that the case? Well, it's just using a single chipset here. We'll have a look at the actual chipset itself in a minute. But, so it's just a regular like off-the-shelf multimeter chipset. There's no secondary processor that

**Dave Jones:** actually cuz basically multimeters can come in two varieties. Well, probably three varieties, actually. One is just like this one, as simple as it gets. One multimeter specifically purpose-designed multimeter chipset. There's, you know, three or four manufacturers on the

**Dave Jones:** market who make these things, and it does everything. It does all the multimeter range switching functionality, measurement, ADC. It drives the LCD, everything else. Does the whole shebang. The second one is to use a multimeter, which is probably more popular these

**Dave Jones:** days, especially in the mid to high-range meters, is to use a specific multimeter chipset, but it's only a front-end chipset. So, it only does the measurement hardware, you know, the front end, the range switching, the ADC, and, you know,

**Dave Jones:** various generators and all that sort of stuff. And that is just a front end. It can't actually do anything itself. It's not really a processor. Can't drive an LCD. Can't do anything else. Usually a serial output, which then goes to a

**Dave Jones:** secondary processor, which then drives the LCD and everything else. Now, we can actually do a comparison with the new EEVblog meter, the BM235 here, and have a look at this one. And you'll notice this one actually uses two chipsets

**Dave Jones:** here. But, this one is a little bit unusual. Usually, when you see two chipsets like this, you'll have just a multimeter front-end uh like this, which doesn't contain a processor. It's just, as I said before, like the range

**Dave Jones:** switching, everything else, the ADC, all that all the stuff, you know, the true RMS converter, every you know, everything else, all the other functionality required for a multimeter chipset. I'll put a typical uh data sheet over here of a uh chipset, which

**Dave Jones:** is uh fairly common, for example. Now, this one, you would think that that's the case, and it interfaces with the processor over here for the serial. But, this one's a little bit unusual in that No, this one is actually a

**Dave Jones:** processor and does everything just like this one up here, but it obviously does uh it's designed for uh closed case calibration. It's got E-squared PROM built in, cuz it's got to store the uh contents, and it either has uh E-squared

**Dave Jones:** PROM built in for the uh to store the software calibration functions, or it can use external uh E-squared PROM. But, this one actually is this secondary chipset here. I'll link in the data sheet here, and uh it's actually just an

**Dave Jones:** LCD controller chipset. So, obviously, couldn't get enough pins on this thing. They needed uh even though it's a complete multimeter chipset with processor and everything built in, requires external LCD controller. So, that this one's a little bit unusual in

**Dave Jones:** that respect, but it's more common to find a multimeter chipset and then a uh secondary processor. Now, there's nothing stopping a single chipset multimeter like this one up here from having closed case software calibration. But, the the the actual uh processor

**Dave Jones:** inside here is not designed that for that. It's bare-bones. It's designed uh not to have any of that closed case um calibration, i.e., you know, E-squared PROM built in, so I can store uh you know, calibration uh settings and things

**Dave Jones:** like that and compensate. It's designed to use these external trim pots around here. So, in that case, it's a it's a poor choice by Fluke in a modern multimeter to have to require pots like this to trim. It's just from a

**Dave Jones:** long-term, you know, drift characteristic and everything else. It's It's poor form. Not when, you know, modern processes can handle these sorts of things. But, hey, that's typical of these really cheap-ass low-end chipsets like this. They require these external pots. And for those who

**Dave Jones:** want to know what the front-end multimeter chipset on the EEVblog meter is, sorry. Secret squirrel. So, anyway, I think that's pretty poor having these trim pots on a modern multimeter. Just, yeah, fail. Anyway, now, let's take a look at the schematic. Now, I'll link in

**Dave Jones:** the complete schematic down below. It seems to be the official one. So, I'm not sure proprietary. Sorry, Fluke, but once it's on the internet, it's on the internet. So, yeah, there you go. 2009 it was generated. Anyway, yeah, so

**Dave Jones:** it looks to be a genuine. It's not like a reverse engineered or anything like that. And I'll link in the PDF down below. Now, the chipset in this thing they've mangled somehow. I don't know when they convert to PDF, they mangled

**Dave Jones:** that. But, it's actually an FS 9721 the LP3 version. And I'll link in the data sheet for this puppy down below. And yeah, it's a complete multimeter chipset. Fortune FS is Fortune Semiconductor. They're one of, you know, three or four different makers of

**Dave Jones:** multimeter chipsets that are still around. They specialist chipsets. And And as you can see, you know, it pretty much handles everything. It is a single chipset. One chip to rule them all. And there's miscellaneous stuff around. So, let's actually just have a quick look at

**Dave Jones:** the schematic. See what we can see here. First of all, take a look at the current jacks here. And I have done a separate video on multimeter input protection. So, if you want to know all about fuses and how they do things in this diode

**Dave Jones:** bridge here and things like that, which by the way is just clamping. That's basically what they're doing there, clamping the voltage. Then I'll link that one in as well if you haven't seen it. It's well worth a look. And look,

**Dave Jones:** they're actually trimming. These are the shunt resistors, okay? So, this is the Here's the 10 amp input here. Here's our common jack, okay? So, our 10 amp goes through through our HRC fuse, of course, into our typical 10 milliohm shunt

**Dave Jones:** resistor. That's that real wimpy. Look at it. It's real wimpy. Look. Sorry, I've got fixed contrast fixed exposure on the camera here. That's why it's all dark. It's very difficult when you're doing white paper like this. You've You've got

**Dave Jones:** to set manual exposure on the camera. Anyway, 10 milliohm current shunt, which is all fine and dandy. And then they're doing a trim across that. So, typically, what which actually is Okay, you could probably argue that one's not that bad. So, they're doing a

**Dave Jones:** divider here. They're doing a voltage divider. There's a 100k resistor 47. They're actually trimming that. That's a large That's a large trim range. That's absolutely massive. So, yeah, I would have limited that. I think that's a bit of

**Dave Jones:** poor design work there. Anyway, usually they physically trim the the nichrome wire current shunt. Typically, it's made out of nichrome wire. The current shunt and they'll physically trim it either by taking a little chunk out of it or adding some

**Dave Jones:** solder, you know, getting some pliers on there and just giving it a little crimp or something. Just to you know, change the value by you know, half a bee's dick or something like that. So, they've decided to add a trim pot and that's

**Dave Jones:** rather unusual. Most companies just decide to trim it some other way or with the modern chipsets just software trim, of course. Okay, so on the milliamp range here, here's part of the range switch. They've got this range switch actually split all the way

**Dave Jones:** through the schematic as you'll see. And what this is showing, these are the physical contacts on the PCB. So, when you put it in the milliamp position down here, it's shorting out these two contacts. What does that do? Well, it

**Dave Jones:** shorts out this resistor up here. So, here's our milliamp input jack. So, if this resistor is shorted out, then this 1 ohm resistor here is going to be our uh current shunt resistor. Actually, it's 1 ohm plus this 10 milliohms down

**Dave Jones:** here. And you'll note that they've got another They've got a 1K resistor in parallel with that. So, they're just, you know, trimming that down slightly cuz they want to get it down cuz you um you want this This should be like 0.99

**Dave Jones:** ohms, really. So, that's what they're trying to trim it to because it's in series with this 10 milliohm 10 amp shunt down here. And then in the microamp range, this contact is moved from here up to the top. So, then we've

**Dave Jones:** got this 1K resistor in series here. And you'll notice this is 0.1%. This one here was only 1% tolerance for the milliamp current shunt. It didn't, you know, they Once again, it's all about the tempco. It's not about the absolute

**Dave Jones:** tolerance cuz this thing is actually trimmed. But you'll notice these ones are 0.1% here because there is no trimmer for the microamp range. So, that's why they're using precision resistors in here cuz it's actually not easy nor cheap to get a 10 milliohm

**Dave Jones:** current shunt resistor. My I do that. I use a 10 milliohm current shunt resistor on my microcurrent, for example, and it's an expensive resistor even in thousands and thousands of volumes, it's, you know, upwards of $4 per resistor, right? It is really expensive.

**Dave Jones:** So, um yeah, if you want the precision, you know, straight off the bat without having to trim the thing, you know, mine's uh What is it? Is it 0.05%? I can't remember. Yeah, I think it's about 0.05% or 0.1 No, 0.1% is it? Um yeah,

**Dave Jones:** that's actually a very expensive resistor. Hence, it's actually cheaper per unit to just have somebody trim this trim pot here. Yeah, uh labor takes time, but labor's not that expensive compared to a $4 resistor. It just depends on which way you want to do it.

**Dave Jones:** So, yeah, they've decided no, we don't want to trim up for that because the 1K ones, these low values, one um these low values of 1 ohm and 10 milliohms, they're expensive to get in real precision values. But, 1K is not.

**Dave Jones:** Like, you can get those for 10 cents in volume or something like that. Right? Real fairly cheap, right? Compared to these. So, they're able to use precision resistors for those and no trimmer. And you'll notice the sense voltage here is

**Dave Jones:** actually tapped off different position depends on whether we're in the amps range or whether they're the milliamp range. So, they've got another set of contacts on the range switch here which in the amps range, of course, it taps

**Dave Jones:** off from this voltage divider across this 10 milliamp current shunt resistor. In the milliamp and microamp range up here, it's same contact. Then, it taps off the top here. And when it's in milliamp range here, it actually taps

**Dave Jones:** through this resistor onto there. So, the current shunt resistor is 1K in parallel with 110 ohms, then in series with 1 ohm in series with the 10 milliohms there. But, it's actually strictly not true to say that there's no

**Dave Jones:** trimmer for the microamp range here. It's not for these resistors, but because it's still in series with this 1 ohm resistor in parallel with this 1K here, you actually have a look. If we briefly zoom in here, and we have a look

**Dave Jones:** what we've got, we've got 1K in parallel with 110 up here. So, that's 99.099 and 0999, but I'll leave the rest off. Anyway, it's that in series with, so plus one on the 1K here, but that 1K is

**Dave Jones:** a trimmer. Okay? So, that's actually 0.999 if it's just the 1K. Okay? If you haven't trimmed it lower than that. Plus the 10 milliamp current shunt resistor down here, that's a total value of maximum value, not including tolerance,

**Dave Jones:** of 100.108. So, these two down here uh don't this one down here it's it's way too small to affect. It's up in the 47k range cup, you know, orders and orders of magnitude higher than the 10 milli-ohm, so it

**Dave Jones:** doesn't affect it. It's only for when you're uh tapping off the amps range here. So, obviously they have to trim this 1k here. It's It's going to make a difference. They want that to be like bang on, okay? Cuz this has no uh

**Dave Jones:** software uh compensation at all. So, they want that to trim this value right down here to exactly bang on 100. So, that trim pot actually will fine actually affect both the milli-amp and the micro-amp ranges. And then they've

**Dave Jones:** just got two uh high-value input protection resistors here to because it's going directly into the chip set there just for some uh current limiting protection for the input pins here in case there's a slight possibility of overload.

**Dave Jones:** I can roll. And they don't have to be uh precision, of course, cuz this is high input impedance. That's why you've only got uh 1% tolerance there, just Joe Blog's resistors. Now, let's take a look at our volts and ohms input down here. This is

**Dave Jones:** our input jack, and then we've got five resistors in series like this, and they are these puppies in there. There they are. Why have they got five like that? I've explained that in the previous video. It's to get a

**Dave Jones:** high withstanding voltage. So, each resistor uh has a certain uh voltage uh you know, maximum voltage tolerance, so you whack five in series, and you can get a effectively a high voltage resistor there, and And cheaper. Five of

**Dave Jones:** those is cheaper than, you know, one big uh uh one, which you'll typically find by the way, ta-da, in the EEVblog meter. There you go. This is more expensive. You notice the isolation slot under there. That's a high compliant voltage ceramic

**Dave Jones:** resistor, much nicer than just the five. But, you know, they get away with it. I mean, you know, nothing inherently wrong with that. And you'll notice that they got 1.5 mm there and also here. Now, a real educated guess is that this is

**Dave Jones:** actually a design note to the PCB layout person to saying, "We need 1.5 mm minimum clearance on these things. That's what we need cuz these are the high voltage input, so isolate it from everything else." And this one here, 9

**Dave Jones:** mm input clearance. Thank you very much. So, assuming that we're in either the millivolts DC range, the ohms, or the capacitance range, then these two contacts on the PCB here are going to be shorted and we're going to be using

**Dave Jones:** these input five input resistors here for that particular mode. And if we follow the yellow brick road here, let's go over, let's go over another protection resistor here. We've just got some diode clamping here. What are they? Bev

**Dave Jones:** 199s are they? So, we've got some diode clamping and it's also fairly typical, especially in old Flukes. I'm not sure if Fluke pioneered it or not. And I was kind of going to maybe do a separate video on this. It's

**Dave Jones:** I'll try and find a another Fluke meter schematic here, which actually shows these. And yes, I actually found it. Here's a schematic from the Fluke 77 Series 3, which actually comes from way like even much earlier multimeters. I think the Fluke

**Dave Jones:** 45 had it. And, you know, all sorts of real old school Flukes have this dual transistor arrangement where it's basically they're configured as back-to-back diodes. So, it actually uses the um the breakdown voltage of the transistor to actually

**Dave Jones:** act as a Zener. And then having the two actually acts as a back to back uh Zener because one will have the uh forward drop and the other one will actually have the breakdown as the Zener depending on whether it's positive or

**Dave Jones:** negative input. And it's a rather unusual configuration, but very popular. So, I'm not into If anyone knows the history of that and whether or not Fluke actually pioneered that, then I'd love to I'd love to actually know details on

**Dave Jones:** that. Anyway, uh back to the 17B here. Um yeah, they've just decided to use some BAT54s. Yeah. Now, this part down here is rather interesting. It's It's a different configuration to what I was mentioning before with the back to back uh Zener

**Dave Jones:** clamp in there. But, uh look, if you put it in uh DC volts or AC volts mode, then it's basically shorting out this, right? So, there's nothing there uh effectively nothing there at all. But, what they're doing is actually tying VSS.

**Dave Jones:** Effectively, this is where they're coupling VSS into the common terminal. The common is actually the terminal over here. So, the battery negative VSS is actually the battery negative. If you go up here, there it is. So, it's They're

**Dave Jones:** not directly uh shorted together. They're tied through this 1 meg resistor here. And um on the base of this uh transistor Q1 here, they've actually just got a uh reverse biased uh diode there on the base of that thing. And they've got a

**Dave Jones:** PNP here. So, it's basically they're shorting out that. This goes up to You follow it up, yellow brick road again. It goes up to the bottom of our resistor divider here.

**Dave Jones:** Yeah, handled by uh multiplexing inside the chipset. And basically, the common of those is shorted down to ground when we're measuring AC and DC. But, when we're measuring ohms, it disconnects the ground, and it's you know, it's go it's

**Dave Jones:** activating this part on the lower end of this resistor network here in the ohms mode and the uh capacitance mode here. In the volts uh DC mode, they've got an AC coupling cap here. They actually and I and a series resistor, so it's almost

**Dave Jones:** like a little snubber. They're uh shorting that out, and uh then our input goes, by the way, through a PTC, positive temperature coefficient resistor, which will increase in value in uh overloads, and that's that puppy down in there. Sorry.

**Dave Jones:** Silly thing. There it is. There we go. There's our input uh PTC uh resistor. And then our big 1K Here we go. They This is where they have a note saying, "Install either one of these." So, install that or install that. So,

**Dave Jones:** they've got this 1K resistor here in series. That's very common input uh protection for you know, it pretty much handles This is how why you can put mains on the um ohms range, for example, because you've got the PT resistor here,

**Dave Jones:** which will increase in value with any overload. Got the big beefy 1K high voltage resistor here. And uh no worries whatsoever. And with our clamping and everything else inside here, then no worries whatsoever. Because when we're in the ohms range

**Dave Jones:** here, by the way, we're actually we need to force a current out into the uh into the positive jack out here. So, that's why it's switching this uh range switching is both used for uh DC and AC voltage ranges, plus the ohms

**Dave Jones:** range as well. It's rather quite quite clever. So, they're actually switching that in this particular circuit in here when they're generating the ohms. So, you know, it's like constant current type thing out for the ohms range. And likewise for the capacitor, too, because

**Dave Jones:** basically when you measure how they do the capacitance measurement, they just basically have a constant current output and then they just time chipset just times how long it takes to charge up. Bingo, you can work out the capacitance.

**Dave Jones:** And then of course the way that they're tapping that off, not only do they have to generate the constant current from here like this, but they also have to read back off as well. So, that's why in the ohms range here, also bingo, it's

**Dave Jones:** tapping off like that. So, that's the voltage sensing there and the chipset can actually measure the voltage across the resistor under test. So, I think they're attempting to do some sort of clamp in here in the ohms and the

**Dave Jones:** capacitance mode, but to what end? I'm not entirely sure cuz at low voltages this circuit is not going to engage. It's not going to do anything. So, you know, at a couple of volts that we're talking about when you're operating the

**Dave Jones:** ohms mode, then this is not going to do anything. But at higher voltages, yeah, it's going to start to conduct. So, yeah, presumably some sort of attempt at clamping. And this is not a true RMS multimeter, so there's no true RMS

**Dave Jones:** converter chip either. A separate analog device is one which is quite typical or the EEVblog meter, for example, is a true RMS multimeter. There it is, but you won't find your traditional analog devices true RMS converter chip in here because

**Dave Jones:** it does some clever stuff using external components in the main multimeter chipset. Might have to separate video on that one day. Anyway, this So, this one's an average responding meter and here's the AC average responding at control via the

**Dave Jones:** chip set here and bingo another trip another trimmer in there for the AC calibration. Bloody trimmers, dodgy as. And it looks like they've got a amplifier in here. Yep, OP that'd be op amp. So they've got some internal op amps in here. So you'd

**Dave Jones:** have to look at the data sheet to get the internal arrangement for this. But basically, so there are feedback resistors for our non-inverting op amp with a times 10 gain there. Now some multimeter chip sets though have a

**Dave Jones:** combination of standard op amps in there plus they might have a chopper amp in there as well that you can select with the internal mux in. So that's you know not uncommon because the chopper amp very precise you know no bugger all DC

**Dave Jones:** offset. So you might find those on say a higher end four and a half digit multimeter chip set. And there's our DC calibration trim pot. Looks like that's is that hooked up to two reference pins? We really need to look at the data sheet

**Dave Jones:** for this getting an internal block diagram to get more fancy pantsy. Speaking of fancy pantsy, look at this. This is quite unusual. You don't often see this in a multimeter. So thumbs up to this. We've got cold junction

**Dave Jones:** compensation and that's for the temperature mode. So you'll notice that when we select a temperature on the range switch here, bingo it goes up to here into this amp here but then that's offset with a cold junction compensation. I've done a

**Dave Jones:** video on cold junction compensation so I won't go over it again. But awesome, that's what high-end thermocouple amplifiers and thermometers look hang on I've got one here somewhere. Like this Fluke K type Fluke F 3000. I've done a teardown of

**Dave Jones:** this and various others and these have a cold junction compensation on the input pins here. They have a temperature sensor which takes into account the temperature of the dissimilar metals which can cause um offset errors in your temperature. So, they've actually added

**Dave Jones:** that in here and you'll notice, look, there it is, a temperature sensor. And uh once again, the uh the designer has put a note in here for the PCB person, um place near the inputs because it's got to be right near the

**Dave Jones:** input jacks. Brilliant. I don't know why they bothered doing that, but it's excellent. I mean, this thing's you know, it shows they've tried to build it down a cost, but hey, cold junction compensation, brilliant. And you'll notice, there it is, U4 down there.

**Dave Jones:** There's our little temperature sensor right down there, but really, you know, in this case it doesn't like matter. In your proper ones like that uh other Fluke uh thermocouple um meter I showed uh before, it actually physically couples the chip through to the metal of

**Dave Jones:** the input jacks. And this one's just physically close. It's not doing that. So, it's in you know, it's a little bit how you're doing, but it's I guess it's better than halfway up the meter, but yeah, in the

**Dave Jones:** scheme of things doesn't really matter here, but yeah, they've gone to that effort. So, I'm very, very surprised. And they've got a offset uh trim pot in there as well just for the temperature. So, they you know, they really did take

**Dave Jones:** this thing seriously. I guess maybe not surprising. I mean, it does have a specific, you know, maybe that was a big selling point they wanted to do. This thing does temperature and does it probably better and more accurately than

**Dave Jones:** your average multimeter. There's not much else doing here. We've got some miscellaneous, looks like some filter stuff maybe happening around here. Uh there's our main oscillator 4 MHz and uh direct LCD driver up here. And Bob's your uncle. That's about it. Um

**Dave Jones:** some extra range, you know, the buttons and things like some extra range uh stuff. And well, not much. Well, what have we got here? A mux. Yeah, there we go. 74HC148 priority encoder. So, they've basically got some pull-ups and pull-downs here.

**Dave Jones:** Just the range switching. So, they're basically just detecting which So, the chipset can detect which range is actually currently selected. So, there you go. I hope you enjoyed that. I Hopefully I managed to salvage this video. Was supposed to be a rip

**Dave Jones:** here of this thing and sorry, Fluke. I I thought this thing had come a gutser and failed on me. But oh, it was a PEBCAK screws when I previously put the thing after the teardown. Ah, these those things happen, you know.

**Dave Jones:** Jeez. So, that was better than deleting the video, I hope. Anyway, I hope you enjoyed it. If you did, please give it a big thumbs up. Catch you next time.
