---
video_id: bX8IIjf15qY
title: EEVblog #272 - Manson 9400 40A 3-15V Switchmode PSU Teardown
url: https://www.youtube.com/watch?v=bX8IIjf15qY
source: youtube-asr
---

**Dave Jones:** Hi, it's teardown Tuesday time again. Quite a few people have been asking for this one for quite some time. So, eventually got around to doing it. It's the Jaycar MP3090 40 amp 15 volt bench power supply. Um, it's okay it's also re-badged as the BK

**Dave Jones:** Precision 1692 and under a whole different One Hung Low names on the market. So, um, you can pick him pick it up pretty much anywhere. It's not a cheap power supply. It's about 340 bucks Australian and US I

**Dave Jones:** think if you get the BK Precision one. But, it's main claim to fame 40 volts 40 amps, sorry, output at 3 to 15 volts variable. Only a single turn pot, not that exciting. Voltage and current displays, there's no current limiting.

**Dave Jones:** Um, it does have the capability to have a fixed 13.8 volt output for ham radio gear and stuff like that. But, yeah, on off switch, adjustable voltage and that's it. But, huge current. And, the thing only weighs about 3 and 1/2 or 4

**Dave Jones:** kilos tops. So, um, for all that current and power, you if it was a linear supply of course, it would weigh a ton. But, this one's not. It's switch mode. So, let's crack it open. See what's inside because, well, it's just a high current

**Dave Jones:** switch mode power supply. Could be interesting or it could be boring as bad We'll find out. And of course its specs aren't going to set the world on fire. 10 million volts output noise like over 200 millivolts load regulation,

**Dave Jones:** things like that. But, it does have that 40 amps. And if it does do 40 amps at 15 volts, I'm not entirely sure if it does over the full range like that. But, certainly 40 volts at lower voltages we're

**Dave Jones:** talking, you know, 600 odd watts capability from this thing. It's not bad at all. But, yeah, I know PC power supplies do that sort of thing, but um this one I expect to be a bit better built than your average um you know, PC

**Dave Jones:** power supply. But, only one way to find out. Take it apart. All right, what are we expecting inside this thing? Well, uh as is typical with uh PC uh power supplies and most uh power supplies in general, really,

**Dave Jones:** they're uh pretty much going to use a single-sided PCB. So, I expect to expect a big single-sided uh PC switch mode uh PCB with some uh heatsinks on it or through-hole construction, of course. Couple of front uh front panel boards for the display

**Dave Jones:** and stuff like that. So, let's check it out. Oh, what have we got here? Wait, yep, there we go. Bingo. The first thing you notice is it looks well-built and well-constructed for a a typical uh single-sided switch mode power supply. I

**Dave Jones:** like it. But, what I found down here in this little section down here is the manufacturer and the manufacturer's model number. Hmm. And there it is, Manson. Uh 4520 doesn't seem to mean much, but uh if you Google Manson 8400,

**Dave Jones:** you also get the Manson uh 9400, and I was able to pull up a full service manual for it. You little ripper. So, I hadn't heard of Manson before, but it turns out they're a Hong Kong uh based pa- company who specialize in

**Dave Jones:** power supplies. So, it looks like um this is a reasonably uh well-designed. It's not a slapped-together beta of kit. And in the service manual, not only uh has it got instructions for how to calibrate and test it, it's got a

**Dave Jones:** complete component overlay, matching bill of materials, and most importantly, the schematic. Awesome. So, inside this thing, the basic operation, uh we'll look at all the individual components in more detail in a sec, but uh let's uh the basic flow here is mains input here.

**Dave Jones:** We've got some filtering here. We've got it going over to the uh front panel main switch here. Comes in here. We've got some more filtering there by the looks of it. We've got a bridge rectifier under there. And uh got

**Dave Jones:** a couple of more caps, and then we've got a couple of uh transformers which couple over into the low-voltage circuitry over here. And then we've got our main uh switching transformer here. We've got a big inductor up here. You

**Dave Jones:** can tell cuz it's only got the two wires coming out of it. Another big fat inductor here. Couple of diodes on this heat sink for the output. Um and output filtering, and Bob's your uncle. So, let's take a look at uh each section in

**Dave Jones:** a bit more detail. And here's our IEC mains input here. There is no uh voltage switching. It's uh 240. It's specifically designed for 240 V. We've got a uh MOV here. It's actually uh heat shrunk in a bit of uh heat shrinking.

**Dave Jones:** Excellent. Right on the terminals. Exactly where it should be. This, interestingly, goes into a little board holding nothing more than uh the uh 1 microfarad input uh filter cap. Once again, it's got all the necessary uh UL and all the markings on them. Check them

**Dave Jones:** out. There's a million of them. And uh there's a bleeder resistor in there, a tiny little one, in parallel. And that uses a connector. It's actually glued down. You may not be able to uh see that in detail there, but it but it is

**Dave Jones:** actually uh stuck in place. It's excellent. We've got heat shrink uh heat shrink over the terminals. Heat shrink tubing. We've got heat shrink tubing over the um uh earth uh terminal here and the earth terminal goes down to a um shake-proof washer

**Dave Jones:** down on the chassis down there. Excellent. And then it is again, interestingly, goes into a filter can here and we'll take a look at the uh circuit for that. That'll just be a pretty standard uh mains common mode uh

**Dave Jones:** filter. And the output from that, of course, they've got um earth coming out as well separately on the output side. Once again, heat shrunk, cable tied, brilliant. And the output from the filter, once again, it's heat shrunk all

**Dave Jones:** the way over. That goes into your double pole uh main switch on the front panel. It's got a real clunking main switch um once again, properly heat shrunk, cable tied, going over to some uh PCB uh spade terminals over here. Once again, heat

**Dave Jones:** shrunk, beautiful. And here we've got an NTC thermistor, more filtering here, another huge uh filter cap. Once again, they really haven't skimped on the components. We've got a common mode uh filter here, going over into the bridge rectifier. And there's the bridge

**Dave Jones:** rectifier. They've put a little heat heat sink on top. I love it. Little tiny plate. They uh obviously decided that they needed a little just a little bit more uh thermal dissipation there. I love it. Uh 3.3 microfarad high voltage caps, 400

**Dave Jones:** V. Haven't skimped at all. Now, I was wondering what this transformer here is and and this uh little bit of circuitry here until I checked the uh chip against uh the schematic and I found out that this is a power factor correction. It uh

**Dave Jones:** uses an MC Motorola um MC 34262 power factor correction device and that's uh part of the transformer and the circuitry used for that power factor correction. So, they've gone to the effort to actually do that. I think that's brilliant. And check out the

**Dave Jones:** copper strapping shield on there, and it's around the transformer, and they've got those on the other transformers inside as well. Nice attention to detail. They've gone to town to ensure that this design is actually going to meet EMC requirements and things like

**Dave Jones:** that. Now, let's actually take a look at the schematic and follow the circuit up until up until this point because I don't want to get that carried away and then show you the circuit later. So, we'll do it step by step, I guess. And

**Dave Jones:** there it is, Manson Engineering Industrial Co. It dates from 2002, rev 1.6. Now, this is for the 9400 model, but apparently the 8400 model that I've got here, well, presumably is exactly the same, but even the 9400 model the service manual shows it's

**Dave Jones:** branded 8400 on the on the overlay diagram. There it is there. So, go figure. Like, 8400, and that matches that number matches my PCB precisely. But anyway, here's our input here. Here's our MOV. There's our parallel bleeder resistor. You remember the that

**Dave Jones:** cap and that resistor were on the board. The MOV was on the IC input connector. There's another NTC there, and there's the inside the filter that filter can which we saw inside the unit there. And that brings us to our mains power

**Dave Jones:** switch on the front panel. There it is there once again, another bleeder resistor, two inductors, a mains rated filter cap. There's our common mode choke there, another filter cap, and there's our full wave bridge rectifier that we saw that had the heat sink on

**Dave Jones:** it. And that brings us on to our MC34262 power factor correction circuit we saw. And there's the big transformer we saw there. It's a little eight-pin dip chip, and all that does power factor correction. And then it goes through

**Dave Jones:** this diode here into the main filter caps. And as we saw in the previous Xantrex teardown video, we also have these are series caps like this, once again with the voltage sharing resistors across there. So, we get our high voltage DC across

**Dave Jones:** here and here, which actually goes down to you follow those wires down in there, it goes down to our main switching transformer down in here, which we'll take a look at. But, of course, we need a little power supply here to power the

**Dave Jones:** circuitry on our main board, and that's what TR2, this transformer here, does. That just powers VCC. There it is there through some filtering and small rectification, filtering and an inductor, and another filter cap. That's a VCC for our circuit. So, if we take a

**Dave Jones:** look at our board, we'll be able to find TR2, and that will be bridging the high voltage part of the circuit with the low voltage part of the circuit. And that's pretty easy to find. There it is there,

**Dave Jones:** cuz you see this black line going through here. They've got this black line on the silk screen, which actually separates the high voltage and the low voltage part of the board. And it's got a high voltage warning. Not sure if you

**Dave Jones:** can read that, but there it is. High voltage section. So, all the stuff in here is no touchy, really. And you can't see the black line, but it goes in between there, and there's our There's some switching transistors in there.

**Dave Jones:** But, that is There it is, TR2, and that separates See, the one side here is on the high voltage section and the other side is on the low voltage section and there's another transformer which does a similar thing here, bridges high voltage side

**Dave Jones:** with the low voltage side. And that transformer I just showed you is TR3 here and that actually comes that's is actually the driver for the PWM controller and it's a Texas Instruments TL494 PWM controller IC and that drives the

**Dave Jones:** two switching MOSFETs here, Q12 and Q13 here to drive the main transformer which then gives us our DC our main you know 40 amp DC volts out. And if we take a look at the TL494 pulse width modulator control chip just

**Dave Jones:** very quickly, it is actually a PWM controller fairly generic one. It's not actually a switch mode voltage regulator controller as such. It's you can use it for quite a few things but it is one of its primary uses

**Dave Jones:** is for a switch mode power supply application. And if we go down here and take a look at the functional block diagram here, you can see that there's not much in there at all. There's a voltage reference down

**Dave Jones:** here, an internal reference, there's a couple of error amplifiers that are summed there, there's an internal oscillator switching oscillator, there's a dead band controller and there's a steering flip flop and and some outputs and some uncommitted output transistors

**Dave Jones:** so you could use them in various configurations if you needed to. So there's really not much in there at all. So it is fairly generic and you would have to look at the greater operation in terms of the actual schematic for this

**Dave Jones:** device to see how it's better used and there's a typical application circuit and as you can see they don't tell you what the outputs go to because you can have your own configurations and use them in various configurations and as

**Dave Jones:** you can see it changes its pulse width to actually match the various waveforms dependent upon the threshold voltage and the feedback on couple of pins there there it is DTC and feedback and that's pretty much all there is to it. So if you want to do

**Dave Jones:** I go through it you would have to have a look at the main power supply schematic and see how it integrates with this pulse width modulator controller and the driver transformer and things like that. Well worth looking into. So Q12 and Q13 there

**Dave Jones:** they're our driving MOSFETs and they're on a big heatsink in there which I'll show you in a second and as I said it comes from the high voltage DC section up here. So here and ground of course it

**Dave Jones:** looks like there's a second but there's a second wire coming from the center tap of these caps here and interestingly that goes through is AC coupled here through to the other side of the transformer like that. So it's switching

**Dave Jones:** between the positive rail here and the negative rail and the center tap on the for this side of the of the winding on the transformer and the other side of the winding on the transformer is connected AC coupled

**Dave Jones:** through to the center tap of those two main DC filter caps. So this here TR4 it's the biggest it's the big transformer so it'll be the biggest transformer in this box and we'll find it in a second and

**Dave Jones:** it's what transfers all of our power across. These other transformers we saw like the driver transformer here is only a small fry. It's only uh transferring control signals and what and the other one we saw up here um is only doing um

**Dave Jones:** sort of you know low current stuff to power the low voltage circuitry, but this is the big beast where all the power gets transferred and then we get rectified over here, filtered, and it goes through to our output which we'll

**Dave Jones:** take a look at. But, let's try and find these uh big power devices on the board. We've got a bit of Chinglish happening here. Caution, warning Will Robinson, touching may hurt you by high voltage. Exclamation mark. This one may be a bit

**Dave Jones:** hard to see, but there's the two switching MOSFETs uh Q12 and Q13 down in there on their own heat sink. So, I've actually got three heat sinks in this thing. Here's Q12 and Q13, the driving uh MOSFETs down in here. That's that uh

**Dave Jones:** the smallest start heat sink in the bunch. This big thing here is we'll take a look at as the output uh output uh rectifier diodes, and then this one up here is the uh MOSFETs for the power factor correction circuitry

**Dave Jones:** which we saw before with the power factor correction uh transformer and the controller chip hidden in behind there. And you can see those side on output uh rectifier diodes, uh drive transistor MOSFETs, and power factor correction MOSFETs. And I don't think I actually

**Dave Jones:** showed those before. There's the uh two Q1 and Q2, the power factor correction MOSFETs there. And I stand corrected, there is a fourth uh heat sink in here which is uh the diode D2 here because it uh does uh transfer effectively uh

**Dave Jones:** all of the current through it for the entire supply. So, that is inside here somewhere. Where is it? There it is. Tiny little puppy down in there. And I just thought I'd mention the uh fan driver. Yes, it is temperature

**Dave Jones:** controlled, and there's the LM324 uh control circuitry used to drive that. And as part of the PWM circuitry, they got some dedicated over voltage protection as well. That's just to stop the output voltage going berserk if there's any uh component failure inside

**Dave Jones:** this thing. And I almost forgot to point out our steamed main switching transformer there. What is it? It's the biggest transformer in the thing. Here's the uh switching MOSFETs on their heatsink down in here, and uh that drives the output, as you can see.

**Dave Jones:** Fairly thin wires uh going in relative to the high-current output huge big thick red and black ones there going into the output uh diode, and uh these two inductors, which we'll take a closer look at. So, how does our output uh

**Dave Jones:** rectification and filtering work? Well, it's pretty basic, and you'll no doubt recognize this. There's a few extra components in there, but the basic uh topology is a um center-tapped uh full-wave rectifier output. Here's the center tap, which goes through to

**Dave Jones:** ground. Just ignore all those resistors. That actually goes through the grounded output. The current sense. We'll get into those, but there's our center-tapped ground output and our two diodes here and here. But, there's actually four of them. There's actually

**Dave Jones:** two in parallel there and two in parallel down here. And of course, they're carrying the full 40-amp uh output current, so they need to be heat heatsinked. And we've had a look at them, but we'll take another uh closer

**Dave Jones:** look. They've got some uh caps across those. We've got an output uh filter inductor here, an output capacitor, another output filter inductor. And once again, these two inductors need uh carrying the uh full 40-amp uh output current, so they need to be big

**Dave Jones:** beasties, and they'll stand out like dog's balls on the PCB. Well, you've probably already seen them there. And we've got our output filter in here, some caps in parallel, and we've got 12 0.1 ohm resistors all in parallel here.

**Dave Jones:** It looks a bit weird, but they're actually flip this up to here, and that one's in parallel with that one, that's in parallel with that, etc. So, there's actually 12 total 0.1 ohm resistors in parallel, and that's our current sense,

**Dave Jones:** which is actually tapped off tapped off here and goes up to our current meter here and off to some other circuitry over there. And we've got some extra caps in parallel here. They'll be on the separate output connector, and they go

**Dave Jones:** to chassis earth ground. You'll note the earth the chassis ground symbol as opposed to circuit ground. Chassis ground and circuit ground aren't necessarily the same thing, and that will be for extra RFI compliance and filtering. And the main output filter in there,

**Dave Jones:** they're not skimping here. They've got two 1,000 microfarads in parallel and different values here once again for filtering the different frequencies. These will have different ESR at different frequencies. And we've got a 1 kV cap here and a 330 ohm 1 W bleeder

**Dave Jones:** resistor. So, when you switch this thing off, it drains the voltage or bleeds the voltage off the output filter caps very quickly. It's a nice touch, and it's things like that which separate the cheapy supplies from the good ones.

**Dave Jones:** So, here's our main switching transformer up here, and you'll see the huge big thick heavy red and black wires coming out of here soldered on to the main board down in here. And here's our two a rectifier diodes in here and here's

**Dave Jones:** that big um output inductor which you saw before. But where's the other output inductor I hear you ask? Well, it's this sucker over here. Look at the beast. And once again, it's uh strapped for shielding as well. Beautiful. And once

**Dave Jones:** again, here because it's got to carry the 40 amps, huge big thick cabling. Once again, heat shrunk, done it very professionally. I love it. Now, this here may look a bit dodgy these uh terminations, but they're not. That's a

**Dave Jones:** reasonably common. They'll be like a little uh splayed uh terminal under there uh mounted on onto the board which then they soldered directly onto the top. So, it looks dodgy and blobby, but it's not that bad at all. And here's our

**Dave Jones:** output current sense resistors here which uh allows us to read the output current. And if you're wondering what these big metal things are, they're huge big um jumper links effectively. That's uh what they are cuz they can't rely on

**Dave Jones:** just the PCB to uh transfer all of the huge current from this side all the way over to our output wiring here, they use these big thick uh metal shunts to transfer all the current so it doesn't have to flow through the

**Dave Jones:** copper on the board. Other small touches in here, this capacitor is actually glued down as are all the other main capacitors in here. And the same can be said for some of the uh inductors here, the common mode chokes and these caps,

**Dave Jones:** they're actually gunked or glued down as well to stop uh vibration um during uh transport and use for uh these things actually uh shaking loose and breaking off. Nice touch. They've put, you know, a lot of effort into actually

**Dave Jones:** designing this thing properly, not just uh designing the circuitry, but actually the physical build as well which will which is what will set a good quality supply apart from low quality one which you know this one might last 10 years and another one on

**Dave Jones:** low brand will be dead after a year on a trolley being wheeled around in a production environment or something like that. Another small attention to detail the main inductor output inductor here is actually got these metal plates to

**Dave Jones:** hold it down as well as the main transformer. They haven't relied on just the transformer itself. They've gone to the effort to put a plate there bolt and bolt through and a shake proof washer on the underside of the housing. And

**Dave Jones:** there's our 40 amp output wiring going over to huge probably going to have to work it out to have to get a different angle on this one but it goes over to the big spade terminals mounted on the front

**Dave Jones:** panel. I've had to go handheld for this one but you can see the huge big 40 amp red wire there going into the big crimp terminal onto the big nut and washer there on the front panel and there are

**Dave Jones:** the two you can see the black one as well. They're the two front panel output terminals. And you should be able to just see those two disc ceramic caps under that heat sink there. They're on the there the filtering on directly on

**Dave Jones:** the front panel PCB. They've actually got a small PCB there that mounts those two output uh binding posts and terminal lugs. And really there's not much else doing on the front panel. There's the single turn voltage pot on the front

**Dave Jones:** panel. It's got its own board our output display voltage and current display with its own regulator there. Once again it's glued down to the top board there. That's a little bit dodgy it's at a different angle. I think they they kind

**Dave Jones:** of maybe didn't have enough room left over it sort of seems to be wedged in there like that. Uh but apart from that, there's not much else doing on the front panel. There's another tiny little board over here for the LED indicator on the

**Dave Jones:** front panel, but that's about it. But there is one thing left on the front panel, and you'll see that high voltage cap there connecting the uh circuit uh common output through to the chassis ground. And as far as the main PCB goes, you've

**Dave Jones:** got a couple of uh single-turn trimmer caps in there for uh tweaking this thing. And you'll notice that there's a switch here, switch two, which actually is uh inverted, and it goes through to the switch on the back panel, which is

**Dave Jones:** the uh selectable uh 13.8 V fixed output. And it's warning you if the 13.8 V is selected, the front panel voltage control is disabled. Well, duh. Course you'd expect that, but warning. So, overall, what have we got here?

**Dave Jones:** Well, we've got our 240-V mains input here, some filtering, full-wave bridge rectification here. We've got our power factor correction magic happening here. We've got our main high-voltage uh filtering that uh branches off into over to here, which uh powers uh via a

**Dave Jones:** isolation transformer powers some low-voltage um uh circuitry like all of the low-voltage uh circuitry, basically. And it branches off down into here, like well, this. Here we go. And it also taps off down into here into the main

**Dave Jones:** uh conversion transformer here, which is controlled by this uh driver transformer here, which is controlled by this pulse-width modulation uh controller, which actually uh controls um uh the output voltage of this transformer. And then we've got our, uh,

**Dave Jones:** full wave output, uh, bridge rectifier here. We've got some, well, we've got, uh, some, uh, filtering there with the inductors. And then we've got our main output filtering going off to our output terminals over here. And that's pretty much all there is to it.

**Dave Jones:** There's some reference type circuitry stuff up here and over voltage protection and fan control and then some other stuff happening around here. Yeah, but that's the basic concept of it. Check out that squiggle. It's got to mean something, surely. Hmm.

**Dave Jones:** So, there you go. There's the PowerTech Jae Car MP3090 or BK Precision 1692 or whatever brand or it's actually manufactured by, uh, Manson in Hong Kong. It's the, um, SPS, uh, 8400/9400, uh, 40 amp, 3 to 15 volt switch mode

**Dave Jones:** power supply. And it's really well built. I was thoroughly impressed with that. I couldn't really fault the thing. It's got everything you would want in a switch mode power supply. A lot of attention to detail. Very well built. I

**Dave Jones:** love it. Highly recommend this thing. Uh, but it's on the pricey side, you know. As I said, it's, uh, well over the, uh, $300 mark. Maybe you can pick it up, uh, cheaper than that, uh, on the street. But, yeah, it's built really

**Dave Jones:** well, really well designed. And I'll have the, uh, service manual with the, uh, schematic, um, and the parts list and everything else, uh, linked in the video there. So, I highly recommend, uh, checking that out and, uh, also those, uh, data sheets

**Dave Jones:** as well. So, for the main, uh, controls, cuz these are fascinating things how they work. So, it's, uh, definitely worth some bedtime reading there. So, there you go. That's tear down Tuesday. If you like it, please give the video a

**Dave Jones:** big thumbs up on YouTube cuz it really helps a lot. And uh you can as always, you can discuss this in the EEVblog forum. Catch you next time.
