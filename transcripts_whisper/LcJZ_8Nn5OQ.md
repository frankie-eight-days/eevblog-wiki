---
video_id: LcJZ_8Nn5OQ
title: EEVblog #275 - PIR Sensor Teardown & Tutorial
url: https://www.youtube.com/watch?v=LcJZ_8Nn5OQ
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 41, "3": 57, "4": 77, "5": 93, "6": 109, "7": 125, "8": 141, "9": 161, "10": 177, "11": 193, "12": 209, "13": 225, "14": 237, "15": 253, "16": 273, "17": 293, "18": 309, "19": 329, "20": 345, "21": 365, "22": 389, "23": 405, "24": 421, "25": 437, "26": 457, "27": 473, "28": 493, "29": 513, "30": 529, "31": 549, "32": 565, "33": 585, "34": 601, "35": 625, "36": 641, "37": 661, "38": 681, "39": 705, "40": 725, "41": 749, "42": 765, "43": 785, "44": 797, "45": 817, "46": 837, "47": 853, "48": 865, "49": 885, "50": 905, "51": 925, "52": 941, "53": 961, "54": 981, "55": 997, "56": 1021, "57": 1041, "58": 1057, "59": 1077, "60": 1093, "61": 1109, "62": 1129, "63": 1149, "64": 1165, "65": 1181, "66": 1197, "67": 1217, "68": 1233, "69": 1245, "70": 1265, "71": 1281, "72": 1297, "73": 1317, "74": 1333, "75": 1353, "76": 1369, "77": 1389, "78": 1409, "79": 1425, "80": 1441, "81": 1457, "82": 1473, "83": 1489, "84": 1509, "85": 1525, "86": 1573, "87": 1597, "88": 1617, "89": 1637, "90": 1653}
---

**Dave Jones:** Hi, it's Teardown Tuesday again. Today we've got one of these per-sensors, or passive infrared, or sometimes known as pyroelectric sensors. You've seen them before, they're used in home alarms, and they sit up in the corner of your room and whenever somebody walks into the room, the red light flashes

**Dave Jones:** and if your house alarm is armed, then it triggers the alarm. And basically they are movement sensors although what they're detecting, they are detecting movement, but they're also detecting heat as well. In particular, body heat. So it's not just humans that set them off, it's pets and things like that as well.

**Dave Jones:** And they're rather clever little things, so there's not much circuitry in them, so I thought I'd tear one down, reverse-engineer it, see what's inside, and play around with it a bit. Should be interesting. Let's go. Now the one I've got here today is a NES brand,

**Dave Jones:** NES, they're actually an Australian company, designed and built in Australia, more specifically here in Sydney. So this is the quantum sensor, and it is, you know, a basic per-sensor. It's not one of those, you can get like a dual wavelength types that have an additional microwave

**Dave Jones:** sensor in addition to a passive infrared detector, but this one just has the passive infrared detector. And if we open them up, they're pretty easy to open up, there's not much in them at all, it's the quantum EXP actually. And there's our board in there.

**Dave Jones:** There's not much in that at all. And they're very nicely designed, you can just pop out the board, look I love that screw down in there, little screw holder, and you just pop that out like that, and bang! That's it. There's our PCB.

**Dave Jones:** They've got three chips on there, let's check it out. So what have we got on the board here? Well it's pretty simple, we've got our 12 volt power in, because almost every alarm system I've ever seen uses 12 volt to power all of the sensors

**Dave Jones:** and all the other peripherals and things like that. We've got our alarm, which is a normally closed output, and because you want it to be normally closed, and then when the alarm goes off it actually breaks that and triggers the alarm. And it's got

**Dave Jones:** a tamper switch output as well, which is also normally closed when the power is off. And there's the tamper switch right there. And if you take a look, you'll see that the case up here has this matching tab here, so that when it clips on there like that and goes in, this

**Dave Jones:** actually depresses that switch down, and if anyone tries to sneak in under the sensor and then pry it open and try and disable it that way, bingo, it sets off the alarm as well. But that's optional, you don't actually have to wire in

**Dave Jones:** the tamper switch if you don't want to. But you can certainly do that, that's why you'll get multiple pair alarm cables going to a sensor, because not only do they provide power, but there's the sensor output as well, but for a tamper switch.

**Dave Jones:** So you might get a four pair alarm cable or something like that, typically wired in. Anyway, we have our purr sensor here, which we'll take a look at in detail I'm sure. We have our relay over here, which we'll also take a look

**Dave Jones:** in detail, because the relay's actually quite important, believe it or not. We've got a couple of jumper switches here, one is to disable the LED, there's the LED if you don't want it to come on, it just shines through the front of the case here with the Fresnel lens, which

**Dave Jones:** is basically, you know, it's not transparent, but the LED will, you will get a nice dim glow sort of, you know, around there. You might get a dim circle on there, we'll power it up later and see that. But the LED can shine through here.

**Dave Jones:** We've got a link for the number of pulse counts. So if you're getting issues with things accidentally setting off the sensor, you can change the number of pulse counts from one to two, or three to four pulses required to set off the alarm.

**Dave Jones:** And we'll go into those pulses later. We've got a couple of electrolytic caps here, and the circuitry on the bottom. Interestingly, if you have a look here at the electrolytic caps these orange ones are rated at 105 degrees C. Why? Well probably for reliability, because

**Dave Jones:** the higher temperature rated ones have a longer lifespan at any given specific temperature, and reliability in these things, as we'll go into with the Reed relay, is incredibly important. And these ones here are only 85 degrees C. I'm not sure why they decided

**Dave Jones:** to do that. They're the same brand, they're a Hatano brand. Not one of the biggest, but certainly not really a one-hung low either. And the circuitry on the back here is all analog, I love it. We've got the power supply here, which is an LM7805

**Dave Jones:** you'd be familiar with that, 5 volt voltage regulator. We've got an LM339 quad comparator, we've got an LM324 dual op amp, and we've got a driving transistor over here for the relay. And that's and a whole bunch of passives of course, resistors and capacitors.

**Dave Jones:** But that's all there is to it. And the normally closed nature of these relays is quite smart of course because then most of the time, you know, if you're not home or something like that, there's no movement. So why energize the relay and waste the power?

**Dave Jones:** Especially if the power's been lost or something like that, and your alarm's operating from the battery backup. Anyway, you don't want to chew the power unless it detects movement. So they have a normally closed contact there. Now the relay used in this one actually doesn't have

**Dave Jones:** any brand, and it does have numbers marked on it, but you know, you google those and I can't find a damn thing. But anyway, this will be an ultra-high reliability, hermetically sealed, read relay. Because these things need a massive switch in life in the order of many millions.

**Dave Jones:** One of these relays might typically be rated for 5 or 10 million, or at least a million operations. Why? Well, you do the math. Every time you see, if you've got an alarm sensor at home and you can sit there all day and count the number of times every time that LED

**Dave Jones:** turns on, well that relay means it's detected motion and the relay is switching. So you know, if you do that, it'll be many hundreds of times. If you're in the kitchen or something, you're moving around, you're cooking, you've got the alarm sensor up in the corner, and it's just going flash

**Dave Jones:** flash flash flash flash, and it might do that many hundreds of times. Maybe even thousands of times per day. But let's take a figure of say 500 per day, multiply that by 365 days in a year, and you know, you're over 180,000 relay operations per year.

**Dave Jones:** And these sort of sensors need, or are designed, for a very long installed lifespan, typically 10 years plus. So you're talking, you know, over 10 years, that might be 1.8 million operations or over a million operations. So really, you're going to need that relay

**Dave Jones:** to have like a million operations minimum. So a lot of the cost in this thing, most of the cost in this thing, is probably the PUR sensor itself, maybe the Fresnel lens, although you can probably churn those out cheaply, we'll have a look at that, and the reed relay.

**Dave Jones:** Now I think traditionally they've used mercury-wetted contacts in this, but this one specifically is advertised in the data sheet for this product as having a dry contact relay, so we know it's not a mercury-wetted type. And if we have a close-up look at our PUR sensor here, you can see it's a

**Dave Jones:** PKI ink LHI 968. PKI ink is Perkins Elmer, so let's go check out the data sheet for this thing. And here it is, the Perkins Elmer LHI 968. And this is definitely not a one-hung low brand sensor, this is one of the best

**Dave Jones:** ones on the market. And because it comes from this alarm sensor comes from Ness, it's a quality manufacturer, and they put the best sensors into this thing. It's designed for, here it is, intrusion alarms, high-end motion sensors, not the cheapos. It's a TO5 metal

**Dave Jones:** can housing, which is what we see. It's got improved EMI protection, and it's also got optional white light improvement as well. It says they grade it for lower white light sensitivity for interference from sunlight coming through the window, and things like that if you're using an alarm scenario.

**Dave Jones:** Anyway, this is what is inside one of these things. There's an optical filter up here, and of course that's the front filter. It's actually dual windows, as we'll see over here. If you look at the diagram of this thing, it's got two little windows in there.

**Dave Jones:** And we'll take a look at why that's important in a second. Now it's got two different windows and two separate sensor elements inside. And they're placed in series, and you'll notice that the polarity is back-to-back. Positive on the top, positive on the bottom, and this one's positive on the top, negative

**Dave Jones:** on the bottom. And that means that they can cancel each other out. So if it's in a room that there's no movement at all and they're all at thermal equilibrium and stuff like that, the sensors receive the same amount of heat energy, and they cancel each other out.

**Dave Jones:** And there's no voltage generated. But when the heat source, i.e. the human being, walks across, then the reason they have two different sensor elements, because then you can actually detect movement from one through to the other, or vice versa, and it can generate

**Dave Jones:** that positive or negative voltage depending on which way it actually, you know, the direction of the movement. If it's down like this, it'll generate a voltage in one direction. If it moves up through these sensors, it'll generate a voltage in the other direction.

**Dave Jones:** And there's a gate resistor on here, there's a JFET here, and it's just a source follower, that's all it is. There's a built-in resistor, and the external circuit as we'll take a look at, will have a pull-up resistor on the drain, and the source, because it's a source follower, the voltage

**Dave Jones:** input will equal the voltage output, but it's converting the very high impedance sensor voltage into a low impedance output, and that will go into the op amp amplifier. And that's all there is to it. There's some pyroelectric element sensors which are sensitive to a specific

**Dave Jones:** wavelength, a specific heat wavelength, and a JFET. And the data sheet has some basic information on how these infrared or pyroelectric sensors work. And we've got some infrared basics here, and we'll take a quick look at it, but basically every thing, every body emits infrared radiation, or

**Dave Jones:** heat radiation. And they give an example here, a human body of a surface temperature of approximately 35 degrees C, or 308 degrees Kelvin. You know, scientists like to work in Kelvin on this degree C rubbish. Gives a peak wavelength of 9.4 micrometers. And a cat at 38 degrees, pesky little

**Dave Jones:** cats, urgh, I hate cats. Sorry, dog person. Temperature gives, they give out a wavelength of 9.3 micrometers. So according to Planck, they've got a, they're going to have a radiated emission which is quite broad over the spectrum. So you can't really detect between

**Dave Jones:** a cat or a dog or a pet or something like that, and a human with these sensors. Although some of these human, some of these sensors, sorry, have been tweaked to be pet aware. And if you have a look at this graph of radiated

**Dave Jones:** energy on the y-axis versus the wavelength on the x-axis, you can see the curves for different types of things. There's 32 degree human skin is the, is that green one in there, and you can see how broad it is. So if you're going, and let's say, well, you know, something,

**Dave Jones:** an object that's at 10 degrees Celsius, for example, like the room itself, if it, you know, in the middle of winter it gets down quite low, there's the brown one down there. But as you can see, it's quite a broad curve like that.

**Dave Jones:** So the infrared filter you use to actually get a narrow band of energy into your sensor, because the sensor, you can't just have it absorbing, actually detecting all spectrum, all wavelengths of radiation. Otherwise you'd be getting noise left, right, and center caused by all sorts of stuff.

**Dave Jones:** So you want an infrared filter on the front to try and get that, you know, a narrow band in there which is going to detect human movement. And of course that infrared filter is pretty critical to the white light immunity that this sensor has.

**Dave Jones:** Or, you know, most of these good sensors should actually have, because you don't want them picking up the white light which comes in the window from the sun. If you go out, set your alarm, if it left your window open, you didn't close your curtains,

**Dave Jones:** as the sun goes across the sky, it might trigger at, say, 2pm every day because it got just the right angle, and boom, it picked it up. It'd be going off, you know, all day, every day. It'd be hopeless. So you've got to have the infrared filter in there.

**Dave Jones:** They tell you, like, a long range pyrometric filter like is used in this one is going to have a very narrow window of 9 to 14 micrometers. And here they tell us exactly how a pyroelectric detector actually works, or their ones actually work.

**Dave Jones:** And they use a property of the ferroelectric dielectric material that they actually use and basically when you apply thermal energy to it it changes the electrical polarization and with that you can actually get a charge displacement and you get a voltage generated and you can convert that.

**Dave Jones:** Basically what the pyroelectric material does is it forms a capacitor and that's why down in the circuit down here you can see that the sensor element is actually the symbol for a capacitor with the dielectric material in there. And it's, you know, x number of picofarads or

**Dave Jones:** whatever, and that actually generates a voltage when you apply a specific thermal energy to it. And of course there's a gate resistor in here and an RC, that will form an RC time constant of approximately, in this particular, these particular sensors, of about 1 second.

**Dave Jones:** So they only detect very slow changing thermal energy, and that's what you want. You don't want to be picking up a very wide bandwidth, because people only move very slowly in front of these sensors. And here in the detector construction part it actually hints that these things are fairly sensitive to thermal

**Dave Jones:** and mechanical noises and issues. So they mount the sensor inside in a special way that it avoids thermal, that it provides thermal and mechanical isolation from the case, which is then hard mounted onto your PCB and things like that. So if you hard mount the sensor onto your PCB

**Dave Jones:** and then your PCB is hard mounted to the case and the case is mounted to the wall and you get vibration on the wall, well, you know, you want to your alarm sensor to be immune to that. So these sensors they're constructed in a special way where that doesn't happen.

**Dave Jones:** Now if we look at another aspect of these sensors is the responsivity. And that actually shows a bandpass characteristic here. And the y-axis is the response in kilovolts per watt of infrared energy coming in, versus frequency on the x-axis here. And you can see down at 10 millihertz

**Dave Jones:** there, it peaks at around about .15 hertz or thereabouts, but it has a response a reasonable response there from 10 millihertz up to a couple of hertz. But it still has, you know, it drops off below the one point there, down to, you know,

**Dave Jones:** 10 hertz. So they're going to be used within that sort of range. And really that's what you're talking about. You're talking about detecting human movement through these sensors. So that's why if you've seen like the Mythbusters episode where they test these sensors and how slowly

**Dave Jones:** you have to move through them not to be detected by them, it's next to impossible because they've got a bandwidth which goes right down to, you know, 0.01 hertz and beyond that. I don't know whether or not I would presume that would drop off, you know, fairly slowly like that

**Dave Jones:** on the other side. But you would have to move incredibly slowly through these things not to be detected. And also if you remember the circuit for this thing, it has a high-value resistor from the gate down to ground. And of course high-value resistors, what do they

**Dave Jones:** generate? They generate thermal noise, or what's called Johnson noise. And that can be a real issue. So they also have another graph here which is the responsivity of noise versus frequency. And it's got the noise in microvolts RMS per square root of hertz.

**Dave Jones:** And that actually rolls off at the high frequencies, and it has a natural roll-off at the high frequencies as well. And that's designed so that, you know, there's a delicate balance in there so that the noise introduced from not only the sensor and the FET itself, but also

**Dave Jones:** that resistor on the input doesn't cause false triggering. And just as an aside, Perkins-Elmer also do what's called a digipyro. And that's a, instead of being an analog pyroelectric sensor, it's actually a complete digital one. It's got the pyro elements down here just as we've seen, but it's got

**Dave Jones:** an analog-to-digital converter, it's got a decimator, and a serial interface which goes off to a microcontroller, and a voltage reference of course, and an oscillator. So these are completely digital paths, but they're totally different systems to what we're looking at here today. We're looking at the

**Dave Jones:** one which is analog only. And if you have a look at the rest of the specs on the table here for the LHI968, you can see the responsivity we've mentioned, the minimum, the typical figure, matching between the two different sensors, 10% and the noise we've talked about,

**Dave Jones:** the spectral detectivity, and all sorts of fun stuff you can get into if you want some good bedtime reading. Look up exactly, you know, the physics behind how all these sorts of things work. And also, it's got a field of view also of 100 degrees.

**Dave Jones:** So that's, you know, it's not huge, but it's reasonably wide. And that allows our Fresnel lens to focus into these things. So let's take a look at the Fresnel lens. And if we have a look at a website called Glowlab.com, they've got some interesting information on how

**Dave Jones:** the infrared motion detectors work, and they've got some really good diagrams. So we'll take a look at these quickly. We've got the typical configuration here, which we've seen before. We've got our IR per sensor here, dual elements inside there, it's got the IR filter on the front

**Dave Jones:** as we've seen, it's got the JFET, it's got the gate resistor to ground, and then it's got an amplifier and a comparator. And there's a Fresnel lens in front of that to actually focus various streams of energy. We'll take a look at that, and the thermal energy coming in.

**Dave Jones:** And here's a nice little diagram. We've got ourselves an animal here, I don't know what that is, it's got little antlers there, isn't it cute? And basically we've got the two detector windows on our pyroelectric per sensor here, and that effectively gives you two different

**Dave Jones:** zones. And when your animal or your human walks through these different zones, you get two, well they call them infrared source movements. The first one there, when it moves through the first one, it'll generate a positive output, and you remember the other one was

**Dave Jones:** in series, but it was opposite polarity, so you'll get a negative going output like that. And when it detects one of these, it can actually detect that as a pulse count, and we saw that jumper link in there for pulse counts, and it can detect x number of

**Dave Jones:** pulse counts due to the Fresnel lens effect. And bingo! It triggers the relay and your alarm goes off. Wah, wah, wah, intruder. It's got antlers. And here you go, it explains that a Fresnel lens, they pronounce it Fresnel, I don't know, I always call it Fresnel, is a

**Dave Jones:** plano-convex lens. If you know your lenses and your optics and things like that, you're probably going berserk right about now. And a Fresnel lens has the same properties as this, but it's compressed into a thinner shape like this. So it retains the optical characteristics,

**Dave Jones:** but it's smaller in thickness, and then it doesn't have the absorption losses of a huge big round lens like that. And basically a Fresnel lens, an alarm sensor lens, will actually have multiple Fresnel lens in it focusing different zones onto the IR element.

**Dave Jones:** So let's actually take a look at the lens in our NES sensor. Now this might be a bit hard to see, but if you take a look inside the front surface of this sensor case, you can see the individual concentric circle Fresnel lenses in there.

**Dave Jones:** And these are all different zones, and they've got two of them, and they will be focused on the different two different sensors inside your purse sensor. And that will give you coverage right across the room spanning from one side to the other, and you'll have two different

**Dave Jones:** focused sensors at each point in the room. It's rather quite neat and novel, I love it. So this lens here actually has multiple concentric circle Fresnel lenses all the way across in patterns across this lens like this. So that's why it detects those different

**Dave Jones:** zones actually coming out of the sensor like that, and as you walk across, bang, you go from one zone to the other, and it can more readily detect that, and that helps the sensor work a lot. So these things really, the Fresnel lens

**Dave Jones:** is one of the keys to making these things work. Sure, you've got your individual sensor per in there, but without a good Fresnel lens to detect all those zones, you don't get that whole room, very difficult to get that whole room coverage, which these things, these

**Dave Jones:** per element sensors do really well. And this particular NESS sensor will do like 12 metres by 12 metres square area coverage. It's quite large. And you can see that on the data sheet for the NESS quantum EX sensor here. It's got 12 metres by 12 metres

**Dave Jones:** coverage range, and you can see that the different you can see that there's dual lines here, and that would represent the dual sensors in all these zones which go across in patterns like this. So you can walk through this one over here, bang, it detects you.

**Dave Jones:** You can walk through this little zone over here, bang, it detects you. So you don't actually have to walk from one side all the way to the other side of the sensor to actually be caught by this thing. You only have to walk through

**Dave Jones:** one of these little individual zones here. So it's rather quite clever how these things work. I love it. And of course you've got different angles as well. You also have different angles on the lenses and different mounting angles for the sensor that allow coverage over a certain depth with all these zones.

**Dave Jones:** So really that's why they're almost impossible to avoid these things, regardless of, you know, you might have a door over here for example and you walk through the door and you get detected. It's not because you're walking into the sensor, it's because there's slight differences between

**Dave Jones:** these two zones. And it'll catch you anywhere in any one of these zones. Look out! Well, I think it's about time we reverse-engineered this circuit and see how it works. ... ... ... ... ... ... And bingo! Here's the circuit I reverse-engineered. And yes, it's a bit of a mess, because that's what happens when you do this

**Dave Jones:** kind of thing. I'd have to redraw this to make it a bit more understandable. But the front end here is actually identical to the circuit on the glowlab.com website. So it looks like they're all very similar circuits here. We've got our PIR sensor with a pull-down resistor, a filter

**Dave Jones:** here, and we've got some comparators with some more filtering here, going into a dual monostable. Well, we don't have this in which the monostable then drives transistor, which drives the relay. Well, on this one we don't have a dual monostable at all. We don't have any sort of monostable,

**Dave Jones:** but they're using four of the comparators, they're using all four comparators inside. Once again, there's a window detector there. So yeah, it is slightly different on the second half of the circuit here. This second half of the circuit here is slightly different, but the front end is pretty much

**Dave Jones:** the same. And yeah, I won't go into details, I think I'll leave that for another video where we might possibly probe some waveforms and things like that. So there you go. I hope you enjoyed Teardown Tuesday. And remember, if you like Teardown Tuesday, give it a big

**Dave Jones:** thumbs up on YouTube, that really helps a lot. Catch you next time.
