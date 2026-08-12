---
video_id: ZmyYYKFePz4
title: EEVblog #574 - NEC Analog TV IF Modulator Teardown
url: https://www.youtube.com/watch?v=ZmyYYKFePz4
source: youtube-asr
---

**Dave Jones:** Hi. Welcome to Teardown Tuesday. Yes, we're going to take a look at bit of historic gear here. I've done a previous video on this a tour of the old analog TV transmission facility at our time and here in Sydney and I scored this gear

**Dave Jones:** which was the actual gear used in the rack to transmit the Channel 7 TV signal over most parts or a good lot of Sydney here. So, really historic bit of gear and they switched it off. Of course, they moved entirely to digital and this

**Dave Jones:** is the original gear that transmitted it. Made in around 1981 and it's been in use since then. Not continuously, but cuz it gets switched in with backup gear and rotated through other gear, but this gear itself has, you know, a couple of hundred thousand

**Dave Jones:** hours use out of it. So, you know, really well-used gear and built like a brick dunny. It really is over-engineered. This sort of stuff very rarely fails. So, it should be a real interesting teardown, but unfortunately, I apologize up front. There's no way I

**Dave Jones:** can do justice to this thing. It doesn't matter how I try and explain things, how I tear things down. We've got the full manuals, the full theory of operation, the schematics, the service manuals, the whole works for this thing and there's

**Dave Jones:** no way that I can really do it justice in depth. So, unfortunately, all we're probably going to have to do is a basic overview of the stuff. Then we'll take it apart, have a look at the construction and all we'll cut might

**Dave Jones:** cover some basic operational block diagrams and things like that, but nothing more in depth. I'm sorry. I will try and scan the manuals or, you know, a good lot of it anyway. It could be quite an effort and I'll link those in if you

**Dave Jones:** really want the to go into the circuit detail and exactly how it all works. But, anyway, this is, you know, pretty much just a teardown. Let's pop the hood on these things and see what they're like. But the first thing we're going to

**Dave Jones:** check out is because this stuff is really interesting, the documentation. Hmm, let's see what documentation was like for a bit of really niche gear. I mean, they would have I think the serial number on this is like 200 and something like that.

**Dave Jones:** They wouldn't have manufactured these only in the hundreds, maybe even the low thousands or something like that worldwide over the lifetime of these actual units. So, really not this is the exact opposite of high volume consumer stuff. Really niche stuff made by NEC in

**Dave Jones:** Japan who still make a lot of the TV transmitters used around the world. So, it's going to be really interesting, especially the documentation, the amount of work and things they put into this just to you know, support these products

**Dave Jones:** which would have cost a fortune. I don't even know the price. And if you have to ask the price, you can't afford it. So, here we go. Let's take a look at the documentation. It comes in two binders here and so

**Dave Jones:** we'll take a look at volume one here cuz I don't think there's a huge amount in volume two that we're interested in. It's the PCN 1205AH VHF TV transmitter and this documentation is for the entire rack because this is the model number not

**Dave Jones:** just for any one of these bits of gear but for the entire rack which NEC sold as a complete system and this is all of the supporting documentation that went along with it. So, like I said, they had

**Dave Jones:** to compile this and write this back in the very early 80s. Probably you know, late 70s. A lot of it would have maybe been based on some earlier stuff perhaps but this is all around about that vintage. So, let's take a look at it and

**Dave Jones:** it has all sorts of different uh sections in it for um all of the different uh you know general overview and specs of like the rack and things like that in the overall system how it works, protection, and

**Dave Jones:** then we got into the maintenance operation, and then we got the individual modules down here which we'll take a look at, but ooh, here we go. I love this. Death on contact. Look at that. Whoa. You don't want to die doing

**Dave Jones:** this sort of stuff. Death on contact, high voltage, warning, Will Robinson, dangerous, dangerous. It looks like second edition. That one's been added later. CPR, all that sort of stuff. Because you know, this is serious business. I mean, this um and not the

**Dave Jones:** instruments we're looking at today. I mean, they're just you know regular 240 V um stuff, you know, a couple hundred watts uh output, things like that of the power amplifier, but in terms of the exciter and the really you know high-end

**Dave Jones:** uh high-power stuff in the rack that uh generated the uh couple of kilowatts, um going to the antenna, that's the real dangerous stuff. Anyway, look at this all uh you know, all uh type um all done on uh typewriter, as you can see. It's

**Dave Jones:** fantastic. All different sections, all done and somebody's had to put that in a typewriter and done it. And here we go. I won't go through all the uh details. I'll scan this as I said, and you can read through it to your

**Dave Jones:** heart's content. But here we go, the PCN 1200 series is what we got. Uh TV transmitters, the latest IF modulation type, the VHF TV transmitter. Solid state techniques are more and more used in TV transmitter. Uh solid state with solid state in

**Dave Jones:** exciter employed concurrent with IF modulation. Blah blah. Reduce uh use tube usage, enhance the reliability, and reduction of maintenance costs have been realized through uh full utilization of solid state technique. So, even back in the '80s here, it was a big deal to

**Dave Jones:** switch over to a solid state uh stuff. And of course, the final uh transmitter is a valve, but uh pretty much everything else is uh solid uh state in this thing. So, here we go. Composition. Ah. Use of newly developed steel rack. I

**Dave Jones:** love this. It shows great strength and superior earthquake-proof properties. Well, hey, Japanese company is probably a big deal, you know. Japan is a subject to earthquakes. Not so much here in Australia. Not a big deal, but hey, they've put thought into

**Dave Jones:** that that the uh transmitter still go during a massive earthquake natural disaster, that sort of thing. And here's an overview of the rack which you uh saw in the previous video, which will be linked in. If you haven't seen it,

**Dave Jones:** definitely watch that first. Uh that's the big uh three-door. All of the equipment we're looking at was in this one over here. And then, well, well, it'll get a breakdown. Here it is. Here we go. Here's the breakdown of the

**Dave Jones:** actual uh rack itself. So, we've got ourselves the um this is the gear we're going to look at. We don't have the TX control unit. Um I've told there's nothing really interesting in there, but we start with the uh modulation uh unit.

**Dave Jones:** We've got that. That one's going to be a big deal. Um the IF corrector we don't have. I'm told that's uh you know, pretty trivial, not really uh hugely anything interesting in there. And in a lot of cases, you may actually not need

**Dave Jones:** the IF corrector. It's um anyway, uh then we've got the VHF mixer, which we'll look at. Um that won't be hugely interesting because it's just a mixer. I mean, a lot of the analog magic for transmitting the modulating and ensuring

**Dave Jones:** that the TV signal and audio is high quality is all done in the modulation unit down in here. So, the mixer is just as it says, a mixer to mix the um IF frequency up to a um up to the carrier

**Dave Jones:** frequency of the transmitter. And then we've got the power amplifiers, of course, separate power amplifier for audio and video as we saw. And And then here is the big power amplifier. Oh, there we go. That one had the big uh

**Dave Jones:** huge multi-kilowatt uh valve in there. And then we got a send diplexer over here. And that's pretty much um what constitutes the Syntia rack system and what this documentation's all about. And they talk about the coaxial uh feeders,

**Dave Jones:** of course, the um RF uh coaxial at the cooling fair and the exhaust ducts and things like that. Woo, specifications. Here we go. This is uh rather interesting. The unit we're actually looking at here is the PCN 1205. Yeah, a

**Dave Jones:** little pissy little 5 kW unit. Ah, man, hopeless. They can make them This series went up to 25 kHz uh kHz 25 kW um uh transmitters. The carrier frequency stability, here we go. It tells you about the TCXO, uh plus

**Dave Jones:** minus 150 Hz over a period of 1 month. There you go. Um output impedance, input uh level for the video and the audio, AM noise, and uh all that sort of jazz. Linear distortion uh for those really into their uh video stuff. It's all

**Dave Jones:** exciting, terribly exciting. Specs for this thing. Uh group delay transmission, there we go. Non-linear distortion. And as we'll see in the modulator unit, all this sort of stuff is a big deal. There's lots of tweaks, lots of circuitry in there to actually

**Dave Jones:** ensure that the video uh signal the video and audio signals are of the highest quality and they're all tweaked to absolute perfection before they're transmitted out. Output power variation within 2%. The blanking level for the video. Um the

**Dave Jones:** Oh, man. What else have we got? Modulation capability, FM noise, AM noise, amplitude versus frequency response. It's you know, about a dB flat between that 30 Hz and 15 kHz, for example. Harmonic distortion, 0.5%. So, if you complain there's too much

**Dave Jones:** distortion coming out of your video signal, hey, um your TV signal, hey, somebody may have, you know, accidentally tweaked the pot on the front panel here. And they go with the various standards they try to meet. Step response here.

**Dave Jones:** Goodness. Power supply is 240 V or 384 415 V uh three phase. Voltage fluctuations allow allows 2%. Frequency fluctuation allows 2%. And power consumption, of course, for the model we've got, 5 kW. Go and figure. And there you go. Um

**Dave Jones:** ambient temperature range at minus 10 to plus 45. Operational power factor greater than 90% up to 95% relative humidity. And they can operate these up to 2,500 m above sea level, which could be important because, hey, uh you know, you want to mount mount

**Dave Jones:** these things on the top of mountains, pretty much. That's where they go. So, this is basic block overview of what we're looking at. We've got two of the items here today. As I said, we don't have the corrector here, but basically,

**Dave Jones:** we have got the audio and video input over here, which comes from the network, you know, channel 7 network headquarters or something. They microwave in the audio or these days, it used to be microwave, but in nowadays, it's sent

**Dave Jones:** via you know, fiber optic or the internet or some other connection, something like that. The raw, you know, what information they want to send on their TV channel comes from the network, goes into the modulator, which as I

**Dave Jones:** said, the modulator is the really interesting bit of kit here cuz it has all the circuitry that allows you to tweak almost every aspect of the audio and video to get it just as you require it. And then goes into the IF corrector,

**Dave Jones:** which corrects for phase and things like that based on the transmission output because we have multiple transmitters in parallel. That's why that can be a big deal when you got a parallel system, when you got a single transmitter

**Dave Jones:** system, I believe that one isn't all that hugely important. And then we have our VHF mixer, which as I said, is just really a you know, a mixer. There's not much else to it. And then then we have

**Dave Jones:** our IF output our visual uh uh VHF signal and audio. You'll notice that audio and video is always kept separate right throughout this entire process here. Let's take a look at the IF modulator, shall we? The video signal is

**Dave Jones:** first fed to the differential amplifier and prevents hum from being superimposed on the video signal by the hum current flowing through the ground line. Got to be careful. System grounding would be you know, super important in something in a complete system like this really

**Dave Jones:** would. So, they're using differential amps wherever they can. Then after level adjusted signal, which by the way, there are various adjustments on the front panel here, which we'll take a look at and even more adjustments on the top of

**Dave Jones:** the unit outside of the rack, which you know, wouldn't you know, you wouldn't sort of adjust those after the the thing's installed in the rack. It's directed through the BNC U link on the front panel and is applied to the

**Dave Jones:** video corrector. Here the video signal is subjected to various stuff, pedestal clamping, synchronizing, signal level control, and white clipping. For all you video aficionados who are familiar with video, you know, the PAL video standard. And it really gets meaty now. The video

**Dave Jones:** corrector output is subjected to quadrature distortion compensation at the quadrature detector, which is an optional circuit and then directly when no quadrature corrector is used, fed to the receiver equalizer. Now the video is signal is subjected to pre-correction of

**Dave Jones:** specified group delay for the receiver compensation. Huge amount of stuff going on here. At the next transmit equalization, the overall amplitude response of the transmitter and group delay are compensated again. In case of the transmitter with a sin diplexer, the

**Dave Jones:** TX EQ is mainly for the compensation of group delay caused by the sin diplexer. So, where this is all outside of the system now, like the sin diplexer, as we saw before, is a totally separate unit which gets

**Dave Jones:** um fed part of the signal gets fed here. After a level adjustment, the TX equalization is subjected more pedestal clamping, DC restoration is fed to the modulator. And then it goes through a balanced modulator and balanced modulators are

**Dave Jones:** pretty simple. They just consist of four diodes. There's not much going on there at all. As we'll see in the schematics, the IF modulated signal is subjected to level amplification and a surface acoustic wave saw filter having the

**Dave Jones:** characteristics of a bandpass filter concurrently forms a vestigial sideband and low pass characteristic limiting video bandwidth. The saw filter output is amplified and becomes the visual output of the modulator. The video corrector, quadrature corrector, and clamping at the modulator may be

**Dave Jones:** disconnected by means of available switches, applicable switches. Ah. Goodness. I You know, the amount of effort that goes into ensuring that the video uh signal is all good when it comes out of this thing is just absolutely phenomenal. And then we've got the audio

**Dave Jones:** uh one as well, which is a separate audio path to the video. As I said, all the way through this thing, completely separate audio and video. And there's the block diagram of the audio path of the system. Differential amp, of course.

**Dave Jones:** They got some pre-emphasis on there. Um looks like FET attenuation there. That's interesting. Um modulator oscillator VCO. Uh we got ourselves an output divider, phase detector, what's some PLL stuff going on there, and then there's a crystal main crystal oscillator input.

**Dave Jones:** There's a circuit diagram for our FM modulator there. As you can see, there's not much in these things. I mean, you know, single transistor. They do have some variable capacitance diodes, varicaps in there, but you know, there's not a huge amount, but of course the you

**Dave Jones:** know, the theory behind this sort of stuff working. Geez, you do whole separate videos on that. Then we have a very nice internal wiring diagram of here. Like here's all the stuff on the front panel, all of the connectors, all

**Dave Jones:** of the indicators on the front panel here, and this is all the rear panel stuff. And this is really There you go. So, we got multiple plug-in PCBs. So, that's what we can expect inside this thing. Separate power

**Dave Jones:** supply circuitry generating plus 12, plus 15, 10, and minus 10 as well. Modulation. So, we've got a video modulator board. That's what V mod stands for. We've got a color equalization board by the looks of it, and we have our video corrector board,

**Dave Jones:** and we have our audio modulator board. So, looks like we've got quite a few boards inside this thing when we crack it open. Then we can flick through other stuff like the IF corrector, which I don't have, but there was actually some

**Dave Jones:** reasonably interesting stuff in the IF corrector there. And if you want to take a look at that, of course I'll endeavor to scan this stuff in. And there's the internal block the wiring sort of block diagram for our mixer,

**Dave Jones:** which we'll take a look at. And then we've got our power amplifiers, which are all solid state power amplifiers, by the way. These weren't valve base power amps, so it'd be interesting There's the tetrode power amplifier. So, this is now we're getting into the

**Dave Jones:** other parts of the rack here. And as you can see, so all the different components which go into this, we've got filters and things a harmonic filter. There we go, we've got a 3DB coupler here. Each one of these has their own little

**Dave Jones:** um own little section. You know, we're talking about the blowers inside. So the main wire emergency stop button, all that sort of There's a tetrode power amplifier, the screen power amplifier, the bias screen power supply, sorry, the bias power supply,

**Dave Jones:** TX control unit which we don't have. And woo, look at this. Looks like we've got some sort of control sequence, yeah? Control sequence of the transmitter. There you go, how it all works. TX control off and on because

**Dave Jones:** this is woo no shortage of stuff in here, let me tell you. Unbelievable. This is great. You look at this sort of stuff all day. And then protection, we've got a whole separate section on all the mechanical and electrical interlocks inside this

**Dave Jones:** thing. Here we go, how to turn the play how it turns the plate off, emergency stop, screen grid screen circuit, plate circuit, all that sort of stuff, cylinder key, how the keys go in sequence as we saw in the previous

**Dave Jones:** video, and setting and adjustment of this thing. How you adjust it. Let's take a look. Look at all the work that went into installation. Here we go. Oh, yeah, look at the cabinet I got pulled out. These are all A3

**Dave Jones:** stuff here. So there we go. Look at this. All hand drawn, all hand done. NEC Nippon Electric Co. Somebody signed it, I don't know. Engineering checked, approved, all that sort of jazz. Look at that. Beautiful. And they had to go through and produce all

**Dave Jones:** this lovely documentation for, you know, a couple of thousand units, uh basically, sort of tops. There's the rack that we we've taken off. Nice three-dimensional drawings there, very nice. All the air filters. Oh my goodness. Assembly of the VHF

**Dave Jones:** transmitter. Look at that. That's the transmitter part of the rack. Oh. All the different parts of the rack. Fantastic. Fantastic. Fantastic. There's more than you can poke a stick at. Unbelievable. So, yeah, I won't bore you with the details. I've already bored you

**Dave Jones:** with enough details here. The plate power supply, for example. Power supply circuit. Uh frequency response, adjustment, how to Now we're getting into the video, the input signal level waveform modulation and voltages, things like that. Adjustment. Height of the tuning plate, length of

**Dave Jones:** the quarter resonance bar for the secondary tuning. Oh goodness. Operation. Here we go. Emergency control, stop, how it all works. Blah blah blah. Blah blah blah. Maintenance. And here's what we'll take a look at first, which is the IF

**Dave Jones:** modulator. And this will contain all of the circuit descriptions and the adjustments, how to adjust in detail, and the full circuit diagrams, and the parts layouts. It's all here. Fantastic. Oh, unbelievable. Uh it's roughly divided into a chassis and

**Dave Jones:** plugged-in type printed circuit boards. There we go. So, we know pretty much what we're going to get inside this thing. And uh the audio frequencies, the yeah. They're the IF frequencies, of course. That's the general uh block diagram

**Dave Jones:** operation of the board, similar to what we saw before. And uh video corrector. Here we go. Here's how the video corrector works. Look, block diagram of the APC loop, all going on there. Fantastic. You got the feed that you got

**Dave Jones:** the divider feedback, your phase detector PLL, a voltage controlled oscillator. So, you got it all happening there. Explains all how it works. This is interesting. Look at this. Examples of uh Is that on camera? Yeah, examples of predistortion curve for the TX

**Dave Jones:** equalization, predistortion curves for the RX equalization, the phase equalizer, all this sort of stuff vital to getting the you know, the highest quality video signal you can. And somebody, you know, some little old granny watches it on her old, you know,

**Dave Jones:** crusty old 34 cm analog TV filled with snow. And yet, you know, here's all the gear, you know, and somebody's, you know, all fussed over all the details of the exact, you know, getting the phase and the distortion of the video signal and

**Dave Jones:** everything else right, the levels and the uh man. And, you know, uh people just don't care, you know? This sort of all this sort of stuff is all designed for probably well over-engineered in terms of what was required for like a regular,

**Dave Jones:** uh you know, analog uh TV signal. Cuz it's, you know, it's not that great. Although, I guess it's hard to say what happens if you tweak one of those pots on the front panel, what the user would actually uh see if

**Dave Jones:** this thing was out of uh out of, you know, out of adjustment, really. So, uh uh Check that out. There's a block diagram of the generation and compensation of distortions in the transmitter and the receiver. Unbelievable. And there's the overview

**Dave Jones:** of how the double balanced mixer works. Fantastic stuff. Not much going on here, of course. You just got two transformers, you know, four diodes, and it does all the magic. But, the theory behind that, hey, that could take up a

**Dave Jones:** couple of fundamental Fridays. And it talks about the VSB filter, how it's double sideband modulated, and all that sort of jazz. And it's all in here, how the saw filter works. There we go. So, we'll probably be able to take a look at that when we

**Dave Jones:** open it up. Here's the alarm and metering circuitry, which is really quite interesting because, you know, it basically gives you a visual indication on the front panel that there's a fault in an individual circuit. So, they've got the signals

**Dave Jones:** coming over, and there there's not much going on in here. They're just buffering those, or actually, you know, doing a bit of level detection there in a comparator, and just, you know, switching. In this case, they're actually doing some relay

**Dave Jones:** switching. I guess that actually physically disables the output. Perhaps. I didn't know it actually did that. I thought it just indicated that something was wrong, but it looks like it may actually physically disable something. I don't know. That's

**Dave Jones:** very interesting. And here's all the adjustment pots available inside this thing. I mean, just incredible. Look, these are all That looks like the front Yeah, they're the front. So, that's the front panel. So, there's all these little adjustment pots on the front

**Dave Jones:** panel, as we'll see. And that looks like it's a top view. So, that's internal circuitry. They look Aha, different cards. So, when we open it up, we're going to see different cards. Looks like we've got our audio modulation, our

**Dave Jones:** video corrector, our color equalization, our video modulator, and our SPF there on the different And there's looks like a front panel board as well for adjusting stuff like that, and our power supply over here. So, that's what we're

**Dave Jones:** going to see when we I'm going to stuff open. And you're probably getting in quite sick of this by now. Adjusting the AM component stuff. Dave, show us the hardware. Shut up and show us the hardware. Yeah, yeah, I'm getting there.

**Dave Jones:** Keep your pants on. Total characteristics of the equalizer, phase equalizer, just in the color phase equalization. Uh, adjusting the visual modulator. Uh, frequency response. Unbelievable. Woohoo! Here we go. Have we got ourselves some schematics now? It looks like we do. Now, these are really

**Dave Jones:** interesting. Looks like we have one page per board, basically, but it's a block diagram level, which could maybe follow the functional layout. They may have laid out the board to functionally match this block diagram. That will be interesting to see when we physically

**Dave Jones:** take these boards out. So, I may actually come back to these diagrams and then show you these and then the different parts of the circuitry. Oh, yeah, there's our FET attenuator that we're talking about before. There we go.

**Dave Jones:** Um, yeah, I have to FET. I don't know if it's actually field effect transistor. I don't know. Um, maybe FET means something else. I don't know in, uh, this parlance. No idea. But, yeah, we may actually come back to this cuz

**Dave Jones:** this is interesting stuff. This is That was our audio corrector or audio modulator, by the way. Then we got our video corrector. And then, looks like we've got a color equalization. So, these are all of our different boards. I

**Dave Jones:** don't know if they'll actually have the block diagrams, you know, uh, on the silk screen of these boards or not. Here we go. Here's all our internal, uh, drawings for the front panel and all the internal stuff. But, yeah, um, maybe

**Dave Jones:** they'll actually have the all this sort of stuff, uh, silk screened on there, you know, like a the board. Oh, no, here we go. Here's our all of our, uh, block. Here's all of our component overlays. Not in sure if

**Dave Jones:** these boards have silk screens. Actually, they may not. That's why they actually provide uh component overlays for each board. But, you can see where all going to get all through-hole. Look at this, transistors everywhere. As far as the eye can see, little uh transform

**Dave Jones:** little inductors everywhere. Uh it's all going ICs. Look at this, in the old uh round metal can packages. Fantastic. That's what we're going to see inside this thing. Looks like we've got some uh coax uh semi-rigid coax on the boards. So,

**Dave Jones:** that'll be interesting to uh check out when we open them up. So, there you go. I've whet your appetite for what we're going to see inside the uh and next then we've got the IF corrector, which we don't have, and then

**Dave Jones:** we have the uh mixer, which we'll take a look at, and so forth and so on. Oh, look. Hey, look. Look at this. Somebody's photocopied this. And this is interesting. Look, got some notes here. Here we go. Jam?

**Dave Jones:** No, Sam, is it? Sam further through on Artamon transmitter excited switch a VHF mixer level maybe noise uh sufficient check must Tom. There you go. So, they've got the original uh notes in here of people who've actually worked on

**Dave Jones:** this gear and done stuff and maybe set it up cuz this is all the original documentation dating right back to 1981. Ooh. Ooh, look at this. The temperature-compensated crystal oscillators have which are done by a third-party company, I believe. They've

**Dave Jones:** uh they're marked on the front by a third-party company. They've got their own documentation including all of the uh the specs and we've got the schematic and everything else. This is really really juicy stuff. I love it. Here's the aging characteristics for our

**Dave Jones:** oscillator. Oh, brilliant. We'll come back to that, but check it out. There we go. There is our temperature compensated crystal oscillator circuits parts list. These are for all the different types cuz there's a couple used in all the gear here. Here we go.

**Dave Jones:** They're actually bolted onto the front panel. There you go. They're a Kikusui Lab, however you pronounce it. So, they're the main temperature compensated crystal oscillators in this thing. And lastly, in the back here, I wanted to show you that tada they've got

**Dave Jones:** semiconductor section. It's actually the data sheet section because hey, there was no internet back then, right? You couldn't just access the data sheets. You had to have the data sheets photocopied and put in the back. So, here's all the silicon rectifiers. You

**Dave Jones:** know, look at this. 250 amp silicon rectifier in there in a in a tab pin package that mounts on the panel. Man, unbelievable. Here we go. Transistors 2SC 1889 transistors. And then we'll get There we go. RF power transistor.

**Dave Jones:** Brilliant. 125 watt. There we go. That would be one of the RF power transistors used in the solid state power amplifier, which will end up taking look at. Positive rest 7912 voltage regulator and so on and so forth. All the Motorola stuff, which

**Dave Jones:** you'll recognize. And there's probably some NEC chips. Yep. NEC, you know, because NEC of course are a huge semiconductor manufacturer. So, they can certainly wideband general purpose amplifier. There we go. In a package. They just rolled their own stuff. Right? NEC,

**Dave Jones:** would you because this is the whole rack and systems designed by NEC solid state relays. Man, NEC did tons of semiconductors so they could just roll their own chips whenever they wanted. There's a juicy overall block diagram for the 3 5 kW in parallel

**Dave Jones:** transmitters. I love it with the combiner. That's the complete coaxial switching equipment and outside all the sins that we had a look at in the previous videos. So, the whole system level block diagram. Brilliant. So, I know I

**Dave Jones:** waffled on there and yet some people that may not have been interested but I find this sort of documentation fascinating. And look at it. That's just one of the manuals. I mean, that's just crazy. I mean, this doesn't even include

**Dave Jones:** the power amplifier example. That's in the second volume of this thing. It's just crazy. The amount of work, the amount of people that must have worked on this back in, you know, 1980 to produce all this for something that

**Dave Jones:** they're only going to sell, as I said, you know, a couple of thousand of these things was phenomenal. So, I don't know how many, you know, engineer years of work went into producing that but that's just awesome. You don't get that these

**Dave Jones:** days. So, let's take apart the HPA 3696 NEC IF TV modulator. And as I said, functionally I think this is the most interesting unit out of the lot because, you know, it it does all of the video and audio correction and tweaking and

**Dave Jones:** modulation and clamping and generating the waveform, you know, doing everything like that, doing the whole business and generating the IF frequencies which then go off onto the Um, and then out basically, you know, pretty much uh sent out to the transmitter. So, this does

**Dave Jones:** all the real interesting stuff. And uh as you can see, really nice block diagrams on the front, functional block diagrams, along with uh fault indicators, which they're it's not got fault, it's just got off. So, I guess this section is switched off. It's

**Dave Jones:** faulty, the little light up. And as I said, you can adjust uh little uh little adjustment pots. I don't know if they're 10 turn or uh single turn. We'll take a look at those. But uh you can adjust the modulation level, the white

**Dave Jones:** clip level, the sync level, the modulation level. Uh and then we've got a frequency uh check output for our uh audio crystal oscillator frequency check output for our video oscillator here. And then what have we got? Line, we've got input here,

**Dave Jones:** uh which comes from uh the inputs actually come from the rear. These are the two outputs here, which then go up to the uh IF corrector, and then go on to the uh mixer, and then we've got some

**Dave Jones:** a nice little uh panel meter here, which allows us to do some tests, you know, allows the um uh operator, you know, the technician to come along and sort of, you know, measure things, make sure everything's working hunky-dory. The power switch,

**Dave Jones:** for example, you can't accidentally uh do it, you know, and can't accidentally flick it off and kill everyone's TV all over Sydney, cuz that'll really ruin your day. So, it's one of those locking types, you have to pull it out, and

**Dave Jones:** that's the same across all this gear. It's designed so that you can't do anything really stupid to it. And then take a look at the top. I mean, these are obviously designed to be uh you know, tweaked sort of at the um

**Dave Jones:** installation setup level, and not actually uh tweaked, you know, not for the technician to just come along and uh you know, I don't think, you know, channel 7's looking a bit shitty today. I think I'll, you know, tweak the uh you

**Dave Jones:** know, the white clip level or something like that. So, anyway, I've got clamp receiver equalization, video correction, pre-emphasis. You can actually turn these off or on whether or not you actually want them in your system. Do you want video correction?

**Dave Jones:** No, I don't want it. Thank you very much. Just disable it. I guess, you know, it allows you better than just taking out the board. Maybe you can't the board has to actually be fitted. You can't just take out the video corrected

**Dave Jones:** board cuz it'll be part of all the uh signal path flowing through this whole thing. So, APC off and on transmit equalization, all that sort of stuff. You know, the setup stuff and adjustment pots as well all through this top. More

**Dave Jones:** adjustments that you can poke a screwdriver at. And on the back here, we've got a huge uh heat sink for the power supply, obviously. Uh anodized. We've got some power transistors with uh covers on the back there. We'll be able to take those

**Dave Jones:** covers off and have a look. And uh we've got our 240-V AC input over here. I've no idea what sort of connector that is. It's a, you know, a weird-ass looking uh three-pin connector. Audio uh control output, you know, your guess is as good

**Dave Jones:** as mine what that connector is. I don't know. Maybe it isn't industry standard connector, but hey, you know, I've never seen it before. And then, you know, we've got uh jumper links like this for example. And these things would have

**Dave Jones:** had to have been, you know, produced and supplied. Can we Oh, I got it. It popped apart. The seal on that was absolutely incredible. And uh you know, they would have had to have made these, engineered these to the

**Dave Jones:** precise length to to go on these. And these are all over this NEC year. There you go. Manufactured April 1981. There you go. It's 33 almost 33 years old. Serial number 344. So, they didn't make many of these

**Dave Jones:** things. And there you go, that's our video TCXO, and that's 38.9 MHz, which is the intermediate frequency that the video signal gets modulated up to, and which then finally gets uh subtracted from the local oscillator frequency in the mixer, which we'll see

**Dave Jones:** later. And here's the audio one. That is 8.3501 MHz. These are manufactured, both of them, in December 1980. So, there you go, they're relatively small units, actually, unless they extend a long way back into the input there. They're

**Dave Jones:** relatively small for a temperature compensated crystal oscillator. And what do we have here? What looks like some sort of weird-ass old-style lamp is actually if we rotate that, pull it out, tada, fuse holder, complete with O-ring. Look at that. Geez, they've gone to town. And

**Dave Jones:** look at what we have here, the top panel here looks like it's designed to be easily or come off for real easy servicing. And the way they've engineered that is to have a larger cutout there, so you don't have to take

**Dave Jones:** out the screw and then lose the screw. So, that's bad design for servicing. So, don't want that, so we undo the screw like that, and we undo them all, and then we can just slide our panel off. Brilliant. So, here we

**Dave Jones:** go, let's pop this sucker off, and uh whoa, look at that. We've got ourselves some nice felt in there to hold the boards in place. Look at that. First thing I am going to do, of course, is uh give it a smell. Yeah, that

**Dave Jones:** 30-year-old electronic smell. Beautiful. The other thing you have to remember is this has been operational in a rack for 30 years. And you know, it's not like it's been recently serviced and I don't see any dust at all in this.

**Dave Jones:** None. Zip. Beautiful. Looks like it was the day it was built. And this is lovely. Look at this. Multi-card construction with sliders with a big motherboard at the bottom, which I'll show you, but let's Can I just Yeah,

**Dave Jones:** these aren't These aren't screw knobs. These are just knobs to help you Oh. Pull out a board and tada! There's one of our boards and we'll take a look at each board. Oh, there we go. Shielded on the back. Look at that. Beautiful. All

**Dave Jones:** the uh transistors heat sink there. Lots of heat sink compound. Oh, lots of glue under the bottom hot snot under the bottom of that. Oh, that looks beautiful. Tada! There you have it inside our main rack here. All of the uh

**Dave Jones:** individual uh boards, they're all labeled. Check out all the uh all the connectors. Look at these huge big beefy card edge connectors. Really love them. I don't know who the manufacturer of those is, but oh, they're beautiful. So, big

**Dave Jones:** baseboard, it looks like I don't know, we might have some sort of I don't know, a relay or something over there perhaps, but look at all the uh wiring all loomed, cable tied, and stuff like that. Got a couple of uh components on the

**Dave Jones:** back there. Um some of that, but yeah, all that's all coax wiring all down there. Power supply over here obviously. Oh, there's so much to take a look at in here, but really, I mean, all of the wiring looms down in there, then the

**Dave Jones:** coaxials are terminated down to the bottom boards to the baseboard down there like that. Little uh standoffs there. All individually wired on. Very nice. We've got some rigid coax happening here, too. Check it out. There we go. Got some rigid coax just

**Dave Jones:** flowing from there to there. So, they you know, they're serious rigid coax flowing all the way around there, right down to the bottom, which we can't see, but ah beautiful. The amount of engineering that goes into this is huge. And this

**Dave Jones:** really, you know, it's hard to know if there's a budge or not, really, cuz it's all sort of, you know, it's not designed for high-volume production, high-volume manufacture. They really haven't taken that into account. They're not trying to

**Dave Jones:** shave cost off. They're just getting this job done and engineering it well, but not well for in terms of like high-volume production and automated assembly and all that sort of cost saving, all that sort of stuff, which you get in consumer gear. You're not

**Dave Jones:** going to find that here. So, you know, they don't care if somebody has to sit there all day and, you know, hand-wire all these cable looms. Hey, doesn't matter. And there's a front board, which is interesting in its own right. Ribbon

**Dave Jones:** cable, didn't really expect to see that in there, but obviously that's, you know, some logic sort of stuff going over to the front panel indicator board. Some relay action happening up here. Once again, I don't know. That's, you

**Dave Jones:** know, it's K112MC5107. Not actually sure what that is. No, it's an IC. It's got IC on it. So, yeah, not entirely sure there, but yeah, that drives all the indicators and has all the other pots on the front panel, but that's not all Oh,

**Dave Jones:** no, there's some high-frequency stuff there happening because we've got some rigid coax going across here and across the top there like that. So, yeah, that's all happening cuz that's all the modulation stuff. So, that's all that video or IF frequency. And then we've

**Dave Jones:** got some coax terminated going down to the baseboard down there. And there is the back of our, um, uh, TCXO's there. So, they didn't extend very far into here at all. They weren't very deep. I'm quite, uh, quite

**Dave Jones:** surprised at that. I expected them to be a fair bit bigger. All right, let's take a look at some individual boards. This is our, uh, audio uh, modulator board. There it is. I'm quite, uh, surprised to see some, uh, shielding cans on the

**Dave Jones:** audio modulator board here, which we don't see on, uh, some of the other some of the other boards, uh, for the video, for example, uh, you know, high frequency stuff don't have the shields on them. So, that's, uh, rather

**Dave Jones:** interesting. And we've got some rigid coax on here as well, going there. Now, my theory that the, uh, board would have followed, maybe the layout of the board would have followed the, uh, block diagram up here. No, not really. Uh,

**Dave Jones:** kind of the case. I mean, you know, there's our CMRR pot over there. There's our input level pot. So, these, you know, adjustment pots are in the positions of the switches up here. Oops, sorry. I don't think you can see the top

**Dave Jones:** of that, but sort of, you know, so they're in positions on the board, but, uh, whether or not the circuitry, I mean, your differential amplifier is probably going to be that beast there. It's going to be around there, you would

**Dave Jones:** expect. Um, then our the what's what they call a fit attenuator there, that's probably around that section there, perhaps. Um, the pre-emphasis is switched off and on here. Looks like we've got some regulation, perhaps. Um, but, you know, I mean, look, here's

**Dave Jones:** our phase detector and our divider. That's probably under here. I'm guessing a buffer amps. I don't know. Yeah, it doesn't doesn't hugely follow here. So, uh, so much for that. And for fans of rigid coax, there it is. Metal outer.

**Dave Jones:** There you go. And there's the there's the dielectric on the inside plus the inner conductor in there. Off to these nice little PCB standoffs here. Really a PCB like turrets. There's our gold plated edge connector. That would have been top quality

**Dave Jones:** gold plating of course, not some skimped one hung low thing you get these days. Yeah, that's interesting. Take a look at this resistor here which is mounted on some PCB pins there and there. Whether or not that's like a repair afterwards

**Dave Jones:** or whether or not they sort of, you know, assembled those at the factory. Still I still see some flux residue on that from the solder into that thing. Um They haven't and you can see it on the pins there as well. They haven't

**Dave Jones:** actually cleaned up some of the flux on there. That's a bit ugly but still ultra reliable. 30 years later, not a problem. This stuff was still operational. And notice the cleanliness of the board. As I said, there's no dust on this thing.

**Dave Jones:** Not a speck anywhere. But anyway, that's interesting why they decided to put that on there. Whether or not that was selected after they sent the value was selected after they assembled the board. I don't know exactly. And we have a

**Dave Jones:** budge. Look at this. We have a budge wire going over there. There's not many from a cursory glance of all these boards, there's not too many budges on here but that's certainly one. Check out the standoff for this IC here. What I

**Dave Jones:** originally thought at first glance might have been some oozing hot melt glue is actually a manufactured plastic standoff specifically for the pins to come out because the pin out of this thing is much larger. I'll show you a better one

**Dave Jones:** later where you can actually see the pins. In fact, this one's actually better. There you go. You can actually see the individual pins coming out of the package. NEC branded of course. All these ICs, most of them are going to be

**Dave Jones:** NEC branded parts, all the analog stuff. But, mounted on those interesting standoffs. So, they really didn't want to mount those things on the board. And the reason for that, well, the pins are probably too closely spaced on there.

**Dave Jones:** So, if they had the pins coming straight down and they mounted these, you know, directly onto the board in there, then the wave soldering our process of this thing going on the bottom probably would have shorted those pins out during

**Dave Jones:** manufacture. So, that's probably one of the reasons. There's, you know, this is not a very dense board at all. The components are very well spaced out. Look how they've cut and inserted little insulating sleeves on the base of these

**Dave Jones:** capacitors. Isn't that gorgeous? And check out the original axial capacitors, electrolytic capacitors on here. Once again, NEC branded. They're such a huge corporation. They did everything. And you'll notice like they're the original ones and they got plastic sleeve,

**Dave Jones:** they're, you know, like heat shrink tubing over those. So, these ones look suspiciously modern and the solder joints on there indicate that these suckers have been replaced at some point. So, this board has been repaired. And there's another pretty modern 220

**Dave Jones:** mic 10-V axial capacitor there. But, by modern, hey, this could have been repaired 10-15 years ago, but it's certainly not 1980s original. We've got ourselves some slug tuned inductors there and they've been sealed. You'll notice the gunk on there to hold those

**Dave Jones:** in place to make sure they don't come loose. Somebody's got their tongue at the right angle and tweak those. And the trim pots there are rather interesting. Haven't seen that exact type before. I'm not actually sure who manufactures

**Dave Jones:** those. Surprise, surprise, upon closer inspection NEC manufacture the pots as well. And there we go. I took those cans off and obviously they decided these two separate bits of circuitry were so critical here that they needed to put those inside those shielded cans.

**Dave Jones:** This looks like it's possibly the divider up here for the PLL, perhaps. I would be guessing at that. We'd have to have a look at the circuit diagram and block diagram and take a look at that, but and trust me, you're not missing

**Dave Jones:** anything under there. There's nothing going on on the bottom of these boards, so it's really not worth taking the bottom shield off these things. And well, here's the full schematic diagram for it, which I found in volume two and

**Dave Jones:** the overall block schematic diagram, which I found in volume one. So it is actually scattered around the place a bit and this is just the analog modulator board which we've got here. And yes, I did find the FET I was after,

**Dave Jones:** so that FET attenuator up there, I did find it. Well, I found a FET in there. There you go. I thought it was all discrete transistors. There's a There's a FET and we've got ourselves a Darlington there and

**Dave Jones:** all sorts of things happening. There's our divider circuitry. They've got some waveforms on here as well, which is really quite nice with signal levels, so great for troubleshooting stuff like that. All sorts of stuff all over the shop. So

**Dave Jones:** there's our See if I can see divide by 16, divide by 16, divide by eight. So there's our PLL. Yep, that's what was under that can that I showed you there. So they They're those chips there. So I was right. That

**Dave Jones:** was a good guess, the divider. You can tell because, you know, they're sort of You know, there's a bypass cap on each one. It's sort of a digital type configuration. There's not much analog circuitry surrounding that bit on the

**Dave Jones:** input here, bit on the output. So, that's all part of the phase lock loop. Dead giveaway. Aha, silly me. That FET we saw before was not our FET attenuator. It's over here, which matches our block diagram, of course.

**Dave Jones:** You remember that? There's our differential amp in. There's our FET attenuator there. And that's exactly what we've got up here. There's our differential amplifier there, discrete transistor differential amplifier, of course. And there's our FET attenuator over there. And that's just been

**Dave Jones:** amplified by an op-amp on the output. Bob's your uncle. So, all of this schematic does really match that overall block diagram very nicely. So, you can like put these one on top of the other, and you can go, "Right, here's our phase

**Dave Jones:** detector right here." And bingo, there's your phase detector going to be in there. And, you know, it really is So, there's your DC amp, your low-pass filters happening in there, all sorts of stuff. So, it really is quite easy to

**Dave Jones:** follow when you have the schematic and the block diagram here. It's beautiful servicing this thing. Must have been a dream. We've got ourselves an audio transformer here, 600 ohm output impedance. That's coming out of here. And that's going out to our audio

**Dave Jones:** output. So, all that work just for an audio modulator board. There's a lot that goes into that. I hope you appreciate the level of engineering which goes into transmitting your TV signal, cuz it's incredible. This is just the audio part. This is just one

**Dave Jones:** part. Well, they just modulate it. And well, I can't go through every board in minute detail. We'd just be here forever. We've already been here forever. But, take for example this video corrector board up here and you know, we've got similar stuff sort of

**Dave Jones:** you know, discrete amplifiers happening here all NEC branded and you know, pretty much traditional through-hole technology and it was right when I mentioned before that this sort of stuff you may have noticed it before on the other diagrams,

**Dave Jones:** but there you go. 9th of October 78 even though this was manufactured in 1980. I think yeah, 78 this was designed updated rev in 79. So this is potentially an older design which they've reused in a more modern system unit and there you

**Dave Jones:** go. If you're curious to know what was happening on that board that's got the pedestal clamp the sink level adjuster the white clipper once again a differential amp there video amp and a then the final video amp output. Oh,

**Dave Jones:** terribly monostable multivibrator. Then you got really jam-packed analog goodness like on this color equalization board. Look at that lots of trimmers in here because hence you know, equalization. You have to get in there and you got to trim everything out.

**Dave Jones:** Imagine how horrible it'd be to sit there and calibrate and adjust all these things. Once again, we've got some rigid coax happening here to take it from one side to the other. These boards are all just you know, double-sided board very

**Dave Jones:** coarse through-hole layout, but look, I mean you know, there's hardly any bodges on these boards at all. So really they did well to put these things together and then you know, architect it into the whole system design with the bus and

**Dave Jones:** everything else and wow. Then we've got our video modulator board. You know, not a huge amount happening on that that we've got some rigid coax. We've got another look at that mysterious device there, but check out that. We've got a thermistor right

**Dave Jones:** next to that, so there's some thermal compensation happening there. And check out those two transistors there. They've put a heat sink over both of them, but it may not be a heat sink. It may just be for for

**Dave Jones:** thermal equalization to try and match those pairs thermally. Oh, and by the way, the reason this one had so much stuff on it, there you go. It's got a phase equalizer, receiver and transmitter phase equalizer, and then four stages of pre-emphasis there before

**Dave Jones:** it gets to the final amplifier output. And look at all the lovely parts list inside this thing. That was for that video corrector. There's like 10 page parts list for that. Fantastic. So, really curious to know what that beastie

**Dave Jones:** is. This here looks like, there we go. That could be our balanced modulator. There's our four diodes and our transformers in and out. Let's see if we can find those on the circuit diagram. Yeah, I found it. There's our double

**Dave Jones:** balanced modulator with the four diodes and the two transformers there that we actually saw, and that's coupled into IC 507 there, which unfortunately, that's what that thing is. I'm rather disappointed. That's just an IC. MC5107. And but why it's in a package like that,

**Dave Jones:** that stands off on the board, and no, I couldn't find the data sheet for that thing in the data sheet pack in the back of the manual there, so it's just some sort of, you know, some sort of buffer, some sort

**Dave Jones:** of, you know, video power buffer, wide bandwidth buffer. And last we have our video sideband filter, and this one might be rather interesting. Not much in the block diagram here, but look at this, oven temperature controller, and there's our saw filter up there inside

**Dave Jones:** the oven. There you go, beautiful. So, they're pretty serious about that saw filter, that's for sure. And not much else, you know, frequency response compensator, another buffer, probably using the same one we just uh saw or so. There you go, that's interesting.

**Dave Jones:** And yeah, 1978. Good on you Good on you, T. Otami. And check it out. This is the most interesting thing we've seen so far. This they've got to uh mounted on a physically separate board here on standoffs is the oven controller, of

**Dave Jones:** course, and this, for all the world, looks like the power element to heat this thing up, and the uh saw filter, the surface acoustic wave filter, is inside there. So, inside this big aluminum block, this is obviously the uh

**Dave Jones:** temperature uh sensor, the the thermistor coming out, so we can, you know, they can keep the temperature of that loop um stable. But, there you go. So, that is rather interesting. And there you go, there's the big uh

**Dave Jones:** power resistor on top of this thing to actually keep this thing uh you know, to warm it up. That's rather interesting. It's sort of like a a ceramic um you know, laser uh trimmed uh you know, power resistor. It's it's

**Dave Jones:** really weird. I didn't sort of expect to see something like that in here, that's for sure. Now, unfortunately, to get a look at the uh saw filter inside this thing, then well, that might be might be destructive. It certainly has

**Dave Jones:** to be uh desoldered from the board, that's for sure, and it could be, you know, glued inside there or or something like that embedded in a potted even inside the aluminum. I don't like the look of it. But anyway, um yeah,

**Dave Jones:** exactly. I was right. They've got the exactly the same uh little power buffers there. Those motor Those um NEC manufactured but MC5107s. And what I've done is uh taken the screws off for the back panel. So, let's pop a look under the hood here and see

**Dave Jones:** if we can actually uh get that see if it is uh potted or something else. Hello. Hello. We've got ourselves some uh Oh. Oh. Shielding cans on the bottom. I shouldn't disturb that. Now I got to put it back in place. Um but that's

**Dave Jones:** interesting. But look. Here we go. Here's the back of the board. Aha. There's our saw filter. Look at that. Um huge number of ground pins but it's basically a huge dip package but looks like there's some screws for the

**Dave Jones:** aluminum block there. So, possibly we can get that off. Look at some of the solder joints there. Not terrific. I mean, this sort of stuff is uh the finish on the solder in there not that great. Obviously, anything

**Dave Jones:** that's uh hand soldered everything that's wave soldered is of course absolutely perfect but uh anything that's been repaired What is that? Maybe somebody's actually uh repaired these NEC or they they they they may have been hand soldered after the fact

**Dave Jones:** um after the uh wave soldering uh process potentially. So, yeah. Um that's probably why they're a bit dodgy. Here we go. I've undone the screws and now let's see if we can pop that off. Ah, tada. Look at that.

**Dave Jones:** There we go. It's just a It's just a brick basically. An NEC brick serial number 152. Look at that. So, there you go. It's a uh Yeah, it's a sealed ceramic package there. So, yeah, I would to get in there

**Dave Jones:** and show you the SAW filter the SAW element on there the surface acoustic wave filter. Yeah, we'd have to destructively take that apart and then hey, it may not be all that interesting anyway and I'm not going to

**Dave Jones:** do that cuz that would be an awful shame to actually ruin this thing. It's interesting you can see some like soot marks cuz that just rubs off coming up with following the air flow of this thing. Check it out. There we go. Coming up

**Dave Jones:** from here. So, obviously air is flowing up through there or something like that and capturing that soot. I don't know where it's getting it from but yeah, interesting. That's possibly the most interesting of the boards because why they've gone to the effort to

**Dave Jones:** temperature regulate that SAW filter. What is so special about it? Nothing else in this thing is you know, temperature compensated apart from the crystal oscillator of course which is pretty critical to have stability on the main frequency that you're using to

**Dave Jones:** transmit a TV frequency all over the city but yeah, for something like that filter and I just look back through the circuit description and it unfortunately it doesn't shed any light on why that is kept temperature stable. Presumably they

**Dave Jones:** chose a SAW filter for its performance to remove in this case it's a it removes the lower sideband frequency of 1.25 MHz and the upper sideband frequency of 5.5 MHz and maybe they they chose a SAW filter for its performance

**Dave Jones:** characteristics but you know, the technology of the time maybe dictated that well, you got the performance but to get that performance out of your saw filter, you had to keep a temperature stable. Maybe there was too much drift in there with the

**Dave Jones:** transducer with temperature. That's the only thing I can come up with cuz they've gone to quite a bit of effort there just for, you know, basic video filter, but it uses a saw technology. Maybe they couldn't get the roll off

**Dave Jones:** response of the filter they wanted electrically, so they have to do it essentially mechanically cuz a a surface acoustic saw filter is is you know, is essentially a mechanical filter. Basically, it's it's got a transducer on the input, a transducer on

**Dave Jones:** the output, and some coupling mechanism in between, and it's the physical characteristics of how the how the waves travel along the surface of of the device that they're the medium that they're actually using inside there that determines its filtering

**Dave Jones:** characteristics, but hey, so they chose it off I think that's the only logical explanation. Chose it for the performance and then had to deal with the consequences of that. In this case, temperature compensated. Now, it's time to have a peek inside this power supply,

**Dave Jones:** and I think this cage, two screws here, pretty darn easy. Even got some finger holes here to uh yep, lift that off and too easy. Huh. Look at that. Check out those Philips electrolytic caps here. We got three of

**Dave Jones:** them. Nice big screw terminals on them. 15,000 microfarads, 40 volts. And look, they've got I've never seen this sort of package before. They're not completely round. They're actually flattened, it looks like. I Originally when I looked at it, I thought, "Oh,

**Dave Jones:** somebody's crushed it." They've actually got the sides flattened down like that. So, it's like a a six-sided capacitor. I mean, it's round at the top, and then they've got a little ridge in there, but then these sides are are flat.

**Dave Jones:** It's rather interesting and they're all like that. And we've got some big ass through panel diodes there. Look at them. That's our diode bridge. Brilliant. No problem with heat sinking. So basically what we've got here is a big ass linear supply. We've got a dual

**Dave Jones:** bridge rectifier here with our four big diodes. We've got three big ass 15,000 mic 40 volt filter caps. It looks like there's a little relay board over there so I'm not sure what that's uh doing. That may maybe switch on the power after

**Dave Jones:** a power up delay or something like that. I don't know. Not going to look in the manuals. There's the back of the panel meter down in there. Nice big wafer switch down in there. That's that front panel selection for the

**Dave Jones:** for the panel meter where you know function to switch through to the panel meter and I have to flip the chassis around to get a look at the board on the back which is for our linear power supply here. Ta-da! 2SD357s

**Dave Jones:** manufactured by NEC. Who would have guessed? And there's not a huge amount interesting on that linear regulator board. I mean, you know, whatever. Couple of huge power resistors in there. Incidentally, there you go. Once again, they've got those standing

**Dave Jones:** off but no spacer. None of those fancy plastic spacers we saw on the other board. No way. Don't want to go to that expense on the power supply board. So I don't know why they did it on the others

**Dave Jones:** and not on this one. Who knows? Anyway, ancient stuff going on here. And we've got our big ass transformer in there. And well, that's about all she wrote. But the interesting thing to note about this is how everything is just spread out. I mean,

**Dave Jones:** they don't try and, you know, cram this stuff in. They've got the regulator circuitry right on the back where it needs to be near the past transistors down in there, transformer or the you can see the grill at the bottom there

**Dave Jones:** gets air flow through no problems at all. The caps are probably massively overrated in terms of capacitance and working voltage. Got nice big heat sinking on your bridge rectifier here it seems or your dual bridge rectifier seems much bigger than what you need but

**Dave Jones:** that's what you'd expect in a you know a high reliability instrument like this because the biggest thing which is always going to fail in these things is your power supply. So I'm not sure of the exact you know the full

**Dave Jones:** power consumption of this thing but it's not you know it's not going to be huge and this over engineered linear supply in terms of physical size and probably current and power dissipation and everything else then you know it's

**Dave Jones:** to be expected because to get a long life on these things you really need to over engineer your power supply. So no surprises for finding that they've done it. Remember this thing also has to live in a rack with all that other gear too.

**Dave Jones:** So just testing this thing on the bench isn't good enough. It's you know it's got to work within a system where the heat is always rising but hey these racks do have a forced air well actually no the rack doesn't have I

**Dave Jones:** don't think the rack has forced air going through it. The valve and everything else in part of the you know the real high power transmission stuff does. I'm not sure this side of the rack actually had any blowers in it. It maybe

**Dave Jones:** it does I don't know I'd have to check the documentation but anyway there is no dust inside this thing at all. It is a ridiculously clean considering that it has been in use basically since 1981. It's just unbelievable the condition

**Dave Jones:** this thing's in. It's it's almost as if, you know, it just rolled off the production line. And we've got one more thing left to crack open, the TCXO. Let's take a look. But, of course, as I showed before, we have the full

**Dave Jones:** schematics and everything for this thing, so we know what's inside. By the way, that's a lovely little uh custom module. You know, that would not be off the shelf. This would have been uh you know, a custom designed for NEC

**Dave Jones:** for use in these products, no doubt. And I was wondering how they would have fitted all that circuitry that we saw on the schematic in there before. And look at that. Very crude, sort of, you know, end-on construction. Very nice, though.

**Dave Jones:** I mean, they've individually heat shrunk all the leads. Look at that. Even color coded them blue and yellow. That's just beautiful. Um but, yeah, it's really incredibly old-school. Um and all we've got is this case here. So, that's going

**Dave Jones:** to have the uh crystal in it, and presumably a heater. But, you know, it doesn't really look like, you know, um like there's a lot of, you know, a thermal insulation there or anything like that. So, I, you know, I really expected

**Dave Jones:** something better out of uh you know, the main TCXO in uh you know, a TV transmitter like this. This is, you know, it's pretty crude. And if we have a look at the specs here, yeah, um you know, it's

**Dave Jones:** uh it's pretty ordinary. I mean, we're only talking uh you know, from 0 to 50. Here, we're talking 0.5 ppm there, you know, plus minus 5 * 10 ^ -7. That'd be 5 ppm. So, you go up a digit and you

**Dave Jones:** move the decimal place and you're 0.5 ppm. So, not really great at all. Uh pretty darn ordinary aging characteristics, uh 0.2 ppm. Uh there we go. Uh the internal uh trimmer has a range of uh 2 ppm. But,

**Dave Jones:** yeah. Uh not impressed. Now, it's interesting that uh the name Kensekiya. I mean, I've used Kenseki uh crystals before, and they make really good uh TC uh well, digitally temperature compensated uh crystal oscillators that I've used. And look,

**Dave Jones:** they've sort of added the SHA on the end. Uh Kensekiya Lab. Very interesting. So, yeah, uh Kenseki is still around today. And this is interesting. There we go. It says it uses a uh Gouriet-Clapp system ensuring maximum efficiency. Oh, they're very

**Dave Jones:** reliable and popular. Um I I've never heard of uh Gouriet-Clapp. I mean, I've heard of Clapp oscillator before, but uh apparently it was uh co- or you know, founded at the uh discovered at the same time by a Gouriet or something like

**Dave Jones:** that. And here you go, compensation. It's a poor man's uh TCXO. In this oscillator, temperature characteristics of crystal is compensated with two thermosensors and a varactor in there. Uh transistor in place of a diode. Uh there you go. In

**Dave Jones:** case of transistor characteristics, the crystal is compensated with the variation of impedance between base and collector by the thermosensor. So, it doesn't No wonder it looks so crude and un- TCXO-like is because well, it's not actually temperature controlled. It's just

**Dave Jones:** temperature compensated. And there's a circuit for those playing along at home. I won't go into details, that's for sure. And well, I guess that was uh obvious because TCXO does technically stand for temperature compensated crystal oscillator. It's If it was an oven uh

**Dave Jones:** controlled oscillator, it would be an OCXO, oven uh controlled crystal oscillator. But, hey, it's not. But that's sort of what I expected. I always imagined, you know, I heard about all the stability of the TV transmitters. In fact, you used

**Dave Jones:** to be able to There was a project way, way back in the old days where you could actually, you know, a frequency lock and get a frequency reference from the local TV transmitter or something like that. It's not that great. I mean, you know,

**Dave Jones:** 0.2 ppm. It's probably good in the 70s. So, there you have it. That's inside the NEC HPA 3696 IF TV modulator from the original one used by Channel 7 to transmit the TV signal here in Sydney. And it was rather

**Dave Jones:** interesting. I thought, yeah, it was as well engineered as I expected it to be. Rather fascinating. So, anyway, sorry, I do not have time, literally, because it's 8:30 p.m. I've got Tuesday. I got to get home and edit this video. And

**Dave Jones:** sorry, I still don't have time to scan these manuals, but that is the plan. I'm going to scan them, so they won't be available until Well, they won't be available when this video goes live. So, sorry about that. And I will follow on with the

**Dave Jones:** other two units that I've got in future videos. So, if you liked it, please give it a big thumbs up. And if you want to discuss it, jump on over to the EEVblog forum. The link is, as always, down

**Dave Jones:** below. Catch you next time.
