---
video_id: nWG_neR0CME
title: EEVblog #956 - Countersurveillance Monitor Teardown
url: https://www.youtube.com/watch?v=nWG_neR0CME
source: youtube-asr
---

**Dave Jones:** Hi, it's time for another random teardown from my mailbag shelf and this is a rather interesting bit of kit you don't get to see every day. This is a Research Electronics Inc. Inc. counter surveillance monitor. Yes, counter surveillance as in a bug detector. You

**Dave Jones:** know, in the spy movies when they sweep for bugs in rooms, this is exactly what they're using. This is the CPM 700 model. It's one of I believe one of the popular units on the market. It's fairly old. It dates from the 80s but it's

**Dave Jones:** still be a useful bit of kit today for bug detection and stuff like that. So, I thought we'd do a teardown of this thing. Now, I was hoping to actually show you this thing working and actually give you a bit of a demo in the lab here

**Dave Jones:** of actually finding some bugs cuz it does actually come with a little RF test transmitter and it also comes with a mains powered bug detector receiver. This is the Australian model. It's got the Australian plug on it and this is

**Dave Jones:** designed for detecting bugs that are on your power lines, power points cuz that's a common place to install your for you know, a spy is to install bugs is like on the back of a power point or something like

**Dave Jones:** that and it uses the mains power line to actually transmit and you might be able to pick it up in the next room, at the switchboard, whatever. And they're typically lower in frequency and it's got a transmitter, a test transmitter as

**Dave Jones:** well that you just plug into the mains and you can use this as you know, to make sure all your setups working correctly and you're able to detect the bugs but comes with an RF antenna. It was just

**Dave Jones:** one of these you know, telescopic rod antennas like this and it's got a frequency range from about 50 kilohertz up to about 3 gig. So, it uh detects over that entire frequency range. Now, these things aren't very complex

**Dave Jones:** devices. You might think, "Oh, they sweep over the entire frequency range and do all fancy stuff like that." No, inside these things, as you'll see when I tear down this thing and tear this thing down, I'm absolutely sure is that

**Dave Jones:** it's just going to have a wideband RF uh amplifier front end with a diode detector. Um that's basically as complicated as these things really get. But, um yeah, they're interesting bit of kit. So, it can detect any uh transmitter, be it an

**Dave Jones:** audio transmitter, video transmitter, whatever it is, uh over basically, you know, anything up to 3 gigs or thereabouts, which which would cover, you know, a good lot of uh stuff. So, real interesting bit of kit, but sadly, I've been trying to get this to work for

**Dave Jones:** some time, both with the uh test transmitter and with uh this uh test transmitter as well, and it does not work. So, there's obviously something wrong with it. So, sorry about that, but hey, we can still tear it down. And

**Dave Jones:** thanks to who sent this in, I couldn't find the mailbag episode that it was in, and I normally keep the notes. It came with the original uh padded bag and everything like that. And yes, we've got the original owner's guide as well,

**Dave Jones:** which tells you all about uh setting up and using this thing. And it also comes with an audio cassette training tape. I love this. Do not play this cassette in an area which may be a target for eavesdroppers. Choose a low-security

**Dave Jones:** area, and uh yeah, read through the owner's manual. Anyway, they've got uh lots of sage advice in the uh manual here on how to uh you know, how to establish in a game plan, make a sister time of entry, you know, you've

**Dave Jones:** got a uh uh do it during business hours so that bugs might be active cuz they might have timers on there, or you may have to actually uh, set up the ease dropper by sort of, uh uh, getting like actually

**Dave Jones:** making a plausible fake meeting, and then actually, uh, you know, maybe they're listening in, and then they go, "Oh, something's going to happen." and we'll switch on our bug or whatever, cuz they might be remote switched on bugs,

**Dave Jones:** and hence why you won't find them with a general sweep with one of these RF, uh, receivers. It's only when they activate it, uh, will they do that. So, you might have to bait them and stuff like that,

**Dave Jones:** and controlled leakages, and I don't know, sweep considerations. There's all sorts of cool, uh, advice in this manual. It's pretty neat. Anyway, um, yeah, from 50 kHz to 3 gig. So, the way one of these would generally work, you

**Dave Jones:** would switch it on like this, and then you'd, uh, set your input, uh, gain, and then you'd put it in, uh, search mode here. What are we in? We're at No, we're in manual, uh, monitor mode like that,

**Dave Jones:** where we set our threshold, but we're in search mode now, and uh, yeah, you can put filter off and on, and then we can basically turn up the gain. You should be able to hear that. Speaker coming out there. So, we've got

**Dave Jones:** our noise or whatever, and you would, uh, just go around. You'd have headphones on, of course, because you don't want it to feed back, and for the, uh, ease dropper to actually know that you've, uh, that you're actually

**Dave Jones:** sweeping for bugs and you're listening in and stuff like that. So, you go around, you know, under tables and under other gear, and you know, you'd sweep over things, and it's basically, uh, it works because it can detect Whoop.

**Dave Jones:** It can easily detect, uh, local transmitters. So, if you've got your transmitter and they've, you know, taped the wire under there, it's going to be really close. So, it's going to get a large RF signal on the thing, and

**Dave Jones:** they're dead easy to pick up, cuz they have to transmit. So, yeah, um, they're pretty simple devices. And we've also got the manual for this uh, test transmitter as well and it got built-in microphone so you can actually you know simulate a

**Dave Jones:** real audio bug or you can just set it to a tone which might be able to easy easier to detect. And look, it's just one of those FM transmitters. Nothing fancy, you know, just like one of those talking electronic ones. You know,

**Dave Jones:** what's this? A two transistor one? Oh, this one's fancy pantsy. We got a PN 35 63 RF transistor there they've used proper RF transistor instead of like a BC547 or whatever. But just a two transistor amplifier with a tank

**Dave Jones:** circuit. Here's which is formed with the coil there. Here's a typical schematic from Colin Mitchell from Talking Electronics fame who I've done a series of interviews which which are absolutely fascinating. Click here. I'll try and include one of

**Dave Jones:** those card things if you want to YouTube card thing pop-up thingos. If you want to watch those Colin Mitchell interviews where he talks about his FM bugs and all sorts of things. So yeah, that's a three transistor amp. So the first transistor

**Dave Jones:** would be used for the microphone gain and probably another one for the oscillator and one for the for the tone oscillator and one for the RF transmitter and that's all she wrote. Bob's your uncle. And this particular one works around 172 MHz. All right, so

**Dave Jones:** let's lift the hood on this thing and see if I am right. Ta-da! Yep, that doesn't look that complicated. Oh, check out the routing on that the square auto routed type layout. Oh my goodness, nobody's taken pride in that layout

**Dave Jones:** whatsoever. Oh, that's a bit of a shocker but you know, it works anyway. We've got a bunch of chips. Are those numbers? Hey, yep. Yep, I think they've rubbed some of the numbers on off. I'll get the macro lens up, but yeah, not much in

**Dave Jones:** this. Look, here's our here's our RF input here. Oop, there we go. What's down in there? Could be a surface mount budge. Anyway, we'll take a look at that. See a couple of diodes. We've got some diodes here.

**Dave Jones:** So, this is our RF front end by the looks of it. And of course, we've got a rubbed the numbers off the micro for this LCD here. Rubbed the numbers off these. Geez, these are only going to be

**Dave Jones:** like LCD drivers. Like give me a break. I mean, that's just that's ridiculous. Anyway, yeah, they've Anyway, it's a counter surveillance device. You know, serious professional job. You ain't got to rub the numbers off. Geez. Part of the business. All right, this is

**Dave Jones:** a little bit interesting. Here's our BNC input there. Comes right in there. AC coupled surface mount cap, but we've got ourselves a little Whoop. Little ferrite bead there. What's going on? Are we feeding in a DC signal perhaps

**Dave Jones:** to the BNC? Is there an amplifier in that antenna? Like a you know, a masthead type amplifier and they're feeding DC up there to power it. And then AC coupling again. We've got a couple of glass diodes in there. You can probably bet

**Dave Jones:** your bottom dollar they're germanium because you want the lowest drop possible. Very common to use germanium diodes in you know, RF detector type circuits. Then it buggers off down to the board down here and this switch down the bottom. You can't see it, but

**Dave Jones:** there's the switch down the bottom and then that rocks in the filter down here. So, it looks like that's what that chip there is doing. It's giving that filter. So, numbers are rubbed off. Can't get it. They've written, you know, their own

**Dave Jones:** number on there after rubbing the thing off. But, if anyone wants to have a crack at that, um actually reverse engineering that front end, by all means. We've got four diodes here. We've got ourselves a uh bridge there. I

**Dave Jones:** I don't think so. Something else is going on. Now, we'll just have a look at the under side here. There's no secret squirrel stuff going on there. But, oh, look at all the right angle traces. Oh, but yeah, that's, you know, somebody's

**Dave Jones:** laid out this board is not really, you know, a high-end professional PCB designer. It's pretty lazy. Anyway, uh right angle traces. All the electrons are just going to fly off the corner. Anyway, so there's no funny business going on there. 1988 vintage. And uh

**Dave Jones:** Ooh. Somebody scribbled some numbers in there. What's all that about, eh? Anyway, I just noticed this. Look at this this completely how you doing regulator. You can see that they had some holes down here to bolt the regulator. Oh, got a bit hot. Um so,

**Dave Jones:** just bodged in a heat sink like that. Oh, that is terrible, Muriel. Awful. And it looks like there's got a almost like a bodge resistor there. We've got another bodge resistor couple of bodge resistors there. What's going on there? But, yeah, like

**Dave Jones:** you can see there is not much in this thing at all. No, there is no like, you know, surface mount RF amp or anything on the back of that board. There's nothing uh down in there. So, it's not

**Dave Jones:** that. It's just going basically straight in. Yeah, they've rubbed the numbers off every single chip in this thing. But, as you can see, there's not much. So, sorry. It's probably taken some of the magic away. You might think, "Oh, you

**Dave Jones:** know, only the NSA can develop these bug detectors." And no, it's just an RF a wideband RF amp with a detector diode. Um and that's, you know, pretty much it. Then it's going to detect everything over the range because it's easy for

**Dave Jones:** these things. I mean, you've got the antenna. They only work when they're right next to the antenna. Hence, you have to go around and sweep the room. Um you don't sweep it in terms of frequency. I mean, it's just checking

**Dave Jones:** the entire frequency range at once. So, you don't sweep it in terms of the frequency range. You sweep it in terms of you physically go and sweep the antenna over and under and around every object in the room. And they've got to

**Dave Jones:** be transmitting something, you know, otherwise they would have to actually record something, for example, and then come back and physically get it later. That would be another method. But yeah, it's got to transmit. And if it's transmitted and it's within under 3 gig,

**Dave Jones:** this puppy is going to pick it up. No worries. And it doesn't matter whether it's encrypted or anything like that. You're just looking for any sort of RF transmission. Or in the case of the one for the mains here, this is fairly low

**Dave Jones:** frequency. The manual I've also got the manual for this thing. This one's actually 250 kHz plus minus 10. Thank you very much. Not exactly crystal controlled, is it? Hmm. Anyway, plug it into the mains and that would simulate a

**Dave Jones:** transmitter that a spy would install. You know, they'd just take out your unscrew your power point. They might pretend to be an electrician maintenance person coming in and detect unscrew the power point and whack a bug behind your

**Dave Jones:** power point. So, that's why you That's how you'd find these. You just plug this in and this just basically just couples that over into your RF front end. No worries. And sorry, but uh they've done a real good job rubbing these chips off

**Dave Jones:** and I've tried the usual uh techniques, putting spit on it and getting it under the mantis under different uh angles of light and stuff like that. And no, we're not getting the uh uh code back off those, I'm afraid, anytime

**Dave Jones:** soon. So, yeah, someone would have to uh reverse engineer the circuit there. Probably not hard. So, obviously, there's no uh you know, high-frequency RF stuff going on around here, I don't think. Um I wonder where that could be.

**Dave Jones:** Hm. And yep, I was on the money there. Look at that, active uh amplifier front-end. Bingo. So, that was uh they were feeding voltage up the clacker of that uh coax. And oh, we've got ourselves a tagged channel on them on the bottom there. And

**Dave Jones:** just a couple of little RF uh RF amps in there. They're not RF uh They they are uh specific um amplifier uh RF amplifier uh IC. So, they would be uh wideband, you can see. There's our antenna input, AC coupled

**Dave Jones:** straight in. And of course, we're coming uh feeding power into power and ground into these things. And then uh the output here. And you just couple the uh power off. You've just got little uh ferrite beads there and a couple of

**Dave Jones:** little resistors. And you just tap off the uh DC voltage. So, we've got one uh front-end amplifier there, AC coupled. So, we've got uh two-stage amplification here. The front-end, of course, would be a uh 3 gig Well, they're both going to

**Dave Jones:** be 3 gig uh bandwidth amps, but this one would uh be uh specifically for uh amplification of the front-end. And this one would be a uh cable driver for driving the uh coax over there. But that's about all she wrote. And I am

**Dave Jones:** actually able to get something out of this thing. Look, I've got my uh I've got the mic here. And there we go. We can get some feedback there. And got a tone. It's more of a buzz than a tone, but

**Dave Jones:** anyway, can definitely get the feedback there. So, and I can turn that off and on. So, that works, but uh yeah, it's like if it was just the RF uh front end in the probe that had failed, then um okay,

**Dave Jones:** I thought yeah, fair enough, but it doesn't work with this uh current uh transmitter either. So, it looks like there might be some damage in the uh other in the front end of this thing as well. So, yeah, it's

**Dave Jones:** yeah, I was hoping to do a real good interesting bug test, but not sorry. It's the best we're going to get some feedback.

**Dave Jones:** But, check this out. We do have the switching frequency of our uh LCD here. Da da da da da da. Um yeah, but the probe cannot pick up anything, so dead as a dodo. I just find this uh interesting that

**Dave Jones:** it's a very unsophisticated device for a very sophisticated market. Like, yeah, but anyway, anyone can go into the counter-surveillance business, I guess, but it's all about trust. People build up trust in this particular brand, model, stuff like that. Now,

**Dave Jones:** interestingly, we can actually have a look at a real NSA bug courtesy of Edward Snowden. Thank you very much, Ed. And this is available on the EFF, the Electronic Frontier Foundation website. I'll link it in uh down below. It's

**Dave Jones:** readily available. Everyone's published this thing. And uh let's There's one thing in here that we're interested in. And if we have a look down here, it's got all various products and stuff like that. And um uh these have been analyzed by all and

**Dave Jones:** sundry these days. But, what I'm interested in is this loud auto product here. Dates from 2009 and uh here it is. It's uh picks up speech in a standard office environment. It's just a regular um bug except that it works differently. It's

**Dave Jones:** not continuously RF uh transmitting. In this case, it uses very little power. Uh 15 microamps 3 V. So, basically a shelf life of the battery. So, you whack in the battery and it's going to last, you know, 5 or even 10 years or whatever

**Dave Jones:** depending on the battery, you know, shelf life of a lithium uh primary battery in there. So, now they tell you, you know, self-discharge is more of an issue uh basically. So, the concept of uh the operation though is not not just

**Dave Jones:** a regular RF um amplifier front end. By the way, just have a look at the hand soldering uh job on that. It looks like it's like a almost like a home-etched board with uh you know, really hacked together. Um

**Dave Jones:** so, that's really quite interesting. They've got a scale there. the interesting thing is is how it works. It uses a a uh pulse position uh modulation square wave running at a preset frequency. They don't tell you what. This square wave is used to turn

**Dave Jones:** on a FET. And when the unit, but this is the interesting part, when the unit is illuminated with a CW signal from a nearby radar unit, then then it actually amplitude modulates that with that particular square wave. So, essentially

**Dave Jones:** uh it's a re-radiator um just like an RFID tag and how other things like that work. So, the neat thing about this is that basically if you went in and did a sweep and nobody was illuminating the room to actually uh

**Dave Jones:** you know, the thing's still running, but it's not RF transmitting. So, it wouldn't be picked up with the type of RF uh bug detector that we've got here. It would uh you need um it would only do that if uh you know, you were being

**Dave Jones:** illuminated with the radar, you know, someone sitting in the black van outside with the you know, fiberglass fake side on it with their little you know, their RF, uh radar unit in there and demodulating that. So, that's, you know,

**Dave Jones:** it's a retro retroreflector. Very interesting technique, but these aren't new. These have been around for decades. In fact, many, many decades. I bring your attention to the thing, as it's called, which is a famous bug that was installed.

**Dave Jones:** It was given by the Soviets to the US ambassador to Moscow in 1945. So, it's a passive RFID type retroreflector, and it wasn't discovered until many decades later or something. I'll link in the article down below, but the

**Dave Jones:** interesting thing, the thing consisted of a tiny capacitive membrane connected to a quarter wavelength antenna. It had no active technology active electronics at all, no power supply. It was the capacitive membrane was just acting as a microphone modulating that quarter

**Dave Jones:** wavelength antenna. So, then this case it was around 330 MHz or so, and when you, you know, put a radar onto this thing, it'll modulate back. You get the tiny reflection coming back, and then it can listen to what was going in on inside

**Dave Jones:** the embassy. Anyway, this is brilliant bit of Soviet espionage technology here. Absolutely fantastic. Dates from 1945. Brilliant. So, there you go. I hope you enjoyed that quick look inside one of my random mailbag items, a counter surveillance monitor. Not

**Dave Jones:** something you get to see every day. It's not something, you know, Joe Average would generally get their hands on. Although, you know, they they do sell this particular model to, you know, paranoid business people and stuff like that. You can actually do sweeping

**Dave Jones:** yourself. This is one of the more popular or was one of the more popular models. I think it is still current, actually. I can still buy it at several thousand dollars to buy this. You're paying for you know, the niche market and the

**Dave Jones:** paranoia and stuff like that. I mean, you know, there's not much I mean, not much that goes into building this at all. It's the hardware is worth bugger all. There's no software or there's no, you know, fancy pantsy research going

**Dave Jones:** into this. It's just a wideband RF detector front end. That's it. And uh you know, but they can sell these for a couple of thousand dollars. No worries. And yeah, sorry it doesn't work. If anyone actually has a schematic or wants to

**Dave Jones:** reverse engineer that front end, but this is not going to be a repair uh video. Kind of a pain in the ass when you don't have a uh schematic. That'd be nice, but I'm sure there's no schematic released for this thing cuz they

**Dave Jones:** wouldn't want to reveal the magic of a RF detector. Anyway, hope you enjoyed it. If you did, please give it a big thumbs up. Catch you next time.
