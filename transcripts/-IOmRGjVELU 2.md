---
video_id: -IOmRGjVELU
title: EEVblog #1000 - Fundamental Mailbag Retro Teardown Shootouts are Bullshit
url: https://www.youtube.com/watch?v=-IOmRGjVELU
source: youtube-asr
timestamps: {"0": 1, "1": 15, "2": 34, "3": 45, "4": 61, "5": 74, "6": 85, "7": 98, "8": 112, "9": 126, "10": 135, "11": 146, "12": 161, "13": 176, "14": 190, "15": 200, "16": 209, "17": 221, "18": 238, "19": 250, "20": 269, "21": 286, "22": 299, "23": 313, "24": 322, "25": 334, "26": 350, "27": 367, "28": 376, "29": 397, "30": 408, "31": 421, "32": 436, "33": 452, "34": 463, "35": 475, "36": 488, "37": 500, "38": 511, "39": 522, "40": 539, "41": 554, "42": 565, "43": 581, "44": 592, "45": 610, "46": 623, "47": 645, "48": 661, "49": 670, "50": 683, "51": 693, "52": 708, "53": 726, "54": 740, "55": 753, "56": 765, "57": 780, "58": 802, "59": 829, "60": 843, "61": 857, "62": 870, "63": 881, "64": 896, "65": 910, "66": 923, "67": 939, "68": 959, "69": 973, "70": 988, "71": 1003, "72": 1013, "73": 1020, "74": 1033, "75": 1054, "76": 1065, "77": 1076, "78": 1089, "79": 1105, "80": 1121, "81": 1130, "82": 1142, "83": 1152, "84": 1173, "85": 1185, "86": 1198, "87": 1215, "88": 1228, "89": 1238, "90": 1254, "91": 1269, "92": 1280, "93": 1291, "94": 1301, "95": 1321, "96": 1335, "97": 1347, "98": 1366, "99": 1377, "100": 1400, "101": 1409, "102": 1426, "103": 1435, "104": 1448, "105": 1458, "106": 1474, "107": 1491, "108": 1502, "109": 1513, "110": 1525, "111": 1540, "112": 1550, "113": 1562, "114": 1573, "115": 1582, "116": 1609, "117": 1625, "118": 1646, "119": 1655, "120": 1676, "121": 1689, "122": 1705, "123": 1716}
---

**Dave Jones:** Hi, welcome to everyone's favorite segment, mailbag. Let's get straight into it. This one is from Emmett L. Brown. No idea who Emmett L. Brown is. So, let's uh Let's give it a go.

**Dave Jones:** Everyone loves mailbag. So, jeez, not packed very well. What the hell? What a T-shirt. We'll check out. And what the is this? It's a Microsoft Surface tablet. Um with some young-looking dude on there doing a piece to camera.

**Dave Jones:** What the Hi, I'm Dave Jones. I was speaking to a colleague the other day and we were talking about video blogs. Video blogs? Bloody is No future in video blogging?

**Dave Jones:** What are you doing? There's absolutely no future in video blogging. That's crazy. Like a quality scope. Shut up. Shut up. Can't shut this guy up. Can't shut this guy up.

**Dave Jones:** He is now shut up. Yes, April 4th, 2009. I was going to insert a joke about Doc Brown falling off a toilet, but David said that no one would get it.

**Dave Jones:** So, no. There is no falling off a toilet joke with Doc Brown. Anyway, this is the 1,000th episode and I thought we'd do a medley of stuff that people like, different segments.

**Dave Jones:** So, got to be brief. Let's get to it, shall we? Everyone loves a tutorial. Let's get to it. Come on. Transistor as a clamping Zener. Here's one you may not have seen before.

**Dave Jones:** You probably won't find it in any textbook, really, or pretty much information on this anywhere. And it's a bit of a naughty circuit. We're going to use transistors the way you shouldn't use them, but there's a reason for it and it's it does actually work from a big-name manufacturer.

**Dave Jones:** Let's look at bipolar junction transistors, how we can turn those into a clamping Zener diode, a bipolar clamping Zener diode that can use in either direction to clamp impulses and overloads and ESD and all sorts of other stuff.

**Dave Jones:** So, let's take a look at it. Uh this is a configuration here. The two collectors joined, the two bases joined, and we've got emitters either side. It's really weird.

**Dave Jones:** They're both NPNs, but one's flipped up the other way. So, you might think, "How can this conduct?" Well, we'll find out. Now, don't take a look at this. Let's go straight over to the equivalent circuit here.

**Dave Jones:** Base, collector, emitter of an NPN BJT bipolar junction transistor. You probably won't see this configuration uh in your usual explanations of the equivalent circuit of a transistor. But, because we're using it in a certain overload mode, it becomes relevant.

**Dave Jones:** There's actually a bipolar junction transistor that can be modeled as uh basically two Zeners inside. There's one Zener from base to emitter. In fact, because it's forward-biased like that, it's actually uh working as a diode.

**Dave Jones:** But, it's in its reverse configuration. If you look at the data sheet, V EBO uh or the voltage, sometimes called V uh BR BR for breakdown, is the emitter base breakdown voltage.

**Dave Jones:** In reverse, it'll break down and act like a Zener at about 5 to 10 V. I did a whole video on Zener diodes. It's really cool, detailed down below.

**Dave Jones:** Check it out. It's typically, for most BJTs, can be higher, but typically 5 to 10 V. It's actually an avalanche breakdown. Anything under 5 V is actually a Zener.

**Dave Jones:** I explained that in the other video, linked in down below. And base to collector, we've got what's called VCBO. And you'll usually find VEBO and VCBO in the absolute specs of a data sheet.

**Dave Jones:** Like, don't exceed these. Magic smoke will escape. Warning, Will Robinson. Um so, usually we don't want to operate, but today we are. We're going to be pretty naughty. So, in the reverse configuration here, because of the construction of the BJT, it has a much higher Zener voltage, typically 20 to 100 volts, something like that.

**Dave Jones:** Can be higher, but we'll run with these. So, how does this work? Well, your base-emitter junction like this, if you've got a positive voltage here and a negative voltage here, base-emitter is just your diode drop.

**Dave Jones:** It's just a diode. It's a Zener diode, but in the forward configuration. So, 0.6 volts, near enough. Then, our reverse, because we're actually using base emitter base, positive negative, it's acting like a Zener to give us a roughly, we'll call it 6-volt drop.

**Dave Jones:** So, anything over 6.6 volts here will cause this to conduct and clamp. So, in if you've got a series resistor on the input, it clamps everything. Fantastic. And likewise in the other direction, negative and positive, bidirectional, 0.6 volts and 6 volts.

**Dave Jones:** So, it'll clamp at plus minus um 6.6 volts or thereabouts. Let's go to the bench and check it out. Here's the same configuration that we had before. We've basically got our Zeners.

**Dave Jones:** I've got PN2222s, voltage Zener, input uh series resistor here, and uh the voltage of the supply input here, the voltage of the Zener across here, and the current flowing through the circuit here.

**Dave Jones:** So, you can see at 1 volt, for example, um there's no current flowing through there, and it's just it it's a as if this isn't there, because it's not clamped yet.

**Dave Jones:** But as soon as we reach the threshold voltage, you'll know notice that there's basically no uh current there, okay? But if we start might start to conduct a little wee bit, cuz these aren't great transistors.

**Dave Jones:** But let's take it up to 10 volts. Bingo, it clamps at 8.26 volts. And we can actually go up higher. Let's go up to 20 volts. It still clamps at 8.3 volts and because it's bipolar, it works in the other direction.

**Dave Jones:** Negative. There we go. I just inverted the input voltage minus 20 volts. It still clamps at 8.3. Fan-freaking-tastic. And these are quite fast clamps. Great use for overloads. Now we can actually show the AC configuration of this.

**Dave Jones:** So let's plug it in. I've got a couple of diff probes here. Don't really need it. Not really high voltage. But check that out. We can see how one waveform, there we go.

**Dave Jones:** It's actually clamped it like that. There we go. If we actually turn it down like that, there's actually two waveforms in there. You'll see. Because it's not clamped. So they're equal, but once you actually go up in voltage, then you'll find that it clamps.

**Dave Jones:** There we go. And we'll go up. Up. You see it start to clamp. Fantastic. So it's a bidirectional clamp. I love it. Where's it Where's this thing used? Typically in Fluke multimeters.

**Dave Jones:** They use this circuit all the time. The classic Fluke 87 here. Check out this. I don't have my poker, but there is your couple of transistors down in there.

**Dave Jones:** So they actually use that for the CAT III input clamping. Okay, let's have a look at another one. The Fluke 3000 meter. Flip that open and over and ta-da, check it out.

**Dave Jones:** This actually has two parallel configurations of those for extra power dissipation. But this is quite handy to use these. A very fast impulse clamping response and used for the 1000 volt CAT III, which I believe is 8 kilovolt impulses.

**Dave Jones:** So it clamps those quite nicely. A short sharp. They're not high power dissipation, but they're okay. And you might reuse these elsewhere in your bill of materials. So, very handy to reuse parts.

**Dave Jones:** So, there you go. That's a common use for those. So, I hope you enjoyed that tutorial. Now, let's get back. It wouldn't be a thousand video if we didn't have a whole bunch of scopes.

**Dave Jones:** So, what I'm going to do here, I'm actually generating Let's do a quick review comparison. I'm generating a 500 microvolt RMS signal and we've got the classic Tektronix 2225 analog scope with 500 microvolt per division range.

**Dave Jones:** And there's the input signal. Now, let's actually compare this. So, we're comparing the noise across several different scopes. Now, I've actually frozen and captured this. Let's have a look at Keysight 3000 here.

**Dave Jones:** You'll notice this is not a true 1 mV per division scope. So, we're getting a whole bunch of quant horrible quantization noise on there. That is just absolutely awful.

**Dave Jones:** You wouldn't want to use this scope if you were doing low signal work at all. The Tektronix MDO 3000, this one is a real worry. Look at the amount of noise on there.

**Dave Jones:** Look at it. Um you'll see that other scopes are much better. So, this is only 1 mV per division minimum, but there's a lot Oh, by the way, this is a 1 MHz sine wave and all the scopes are set to 20 MHz bandwidth limit and the same memory depth of 1 meg.

**Dave Jones:** There's no averaging or anything else turned on. So, yeah, the Tektronix MDO 3000, really noisy. I don't know where that's coming from. And you'll see that in the contrast of this Rohde & Schwarz RTB2004.

**Dave Jones:** Check it out. This is 1 mV per division, but and this is a 10-bit ADC, but look how nice that waveform is. Absolutely beautiful low noise. Awesome work, Rohde & Schwarz.

**Dave Jones:** The Hameg one up here, 1 mV per division, and that one's got a little bit of noise on it, but otherwise a reasonably clean result on the Hameg/Rohde & Schwarz, the new Keysight 1000X series scope.

**Dave Jones:** Um this actually is supposed to have a better 1 mV range, but as you can see, it's very similar to the Tektronix. So, there's a ton of noise on there.

**Dave Jones:** Not a great result at all. The Rigol 2000 series, let's have a look. Once again, there's some higher frequency stuff on there. This has a supposedly a No, it doesn't have a true 500 mV range because you can see some quantization amplification on there.

**Dave Jones:** Like you can actually see just not as bad as the Keysight, but still bad. Anyway, uh the Teledyne LeCroy 1 mV per division, not a bad response there. Fairly clean waveform.

**Dave Jones:** Everyone's favorite, the Rigol 1054Z or not. It's a 1 mV per division range, very very noisy. Not the noisiest as we'll see, but still not a great result. And then the new Siglent 1000X series at supposedly has a true 500 microvolt per division range, and it's a pretty good result.

**Dave Jones:** Fairly clean. Look at that. You can see some noisy details on there, but that's an excellent excellent result for low noise measurement with a true 500 microvolt range. And then this GW Instek, this is the worst of the bunch.

**Dave Jones:** Look at that. That's just horrid. Like let's just not even go there. And the 01 has a 12 14-bit converter, but it's actually only 12 bits at the moment.

**Dave Jones:** And what we're looking at, this is 12-bit. The 8-bit is a little bit doesn't show the detail in there, but it's still pretty clean. So, that's actually an excellent result on the 01.

**Dave Jones:** Very nice, but it's only got 1 mV per division. So, there you go. That's just a quick comparison of all these different scopes. Hope you like that, and I'll leave that set up and do some more tests on that in the future.

**Dave Jones:** Now, everyone loves teardowns on the EVblog, and I got something special. Let's check it out. Woohoo! You might have seen this on a previous video, which I'll link in down below where I did the Channel 7 TV transmitter teardown.

**Dave Jones:** This is the 300-W amplifier that transmitted the analog TV signal in Sydney for about 20 years. This one 300 W as I said, this one was the preamplifier, a 300-W preamplifier for the video signal, and also they use the same one, might have even been this one, for the audio.

**Dave Jones:** So, the audio went out at 300 W, the video went out at several hundred kilowatts. It's got a phase shift input here so that you can parallel these things up and tweak them for the same phase so that they load equally.

**Dave Jones:** But, it's just an input, output, and overload indicator. So, let's take a look inside this baby, and yes, we have the schematics. You ready for it? Oh, yeah. The RF aficionados are wetting their pants right now.

**Dave Jones:** Look at this thing. I'll have to do a detailed teardown. This will be very short, but look at all the rigid coax lines here. Look at that little stargates inside.

**Dave Jones:** Look Look little rigid coax penetrators. Here's the power supply. It operates off 28 V DC system supply, and let's take a look at the topology used in this thing, shall we?

**Dave Jones:** And I'll take you briefly through. Oh, by the way, I do have the schematic. I'll link it in down below for those playing along at home. Now, the input signal comes in down here, and it goes into a limiter circuit cuz you don't want some [ __ ] feeding in some input signal that then blows up your amplifier and a, you know, a couple of million people in Sydney can't watch

**Dave Jones:** their TV signal. So, it just clips and limits the input a so it doesn't damage anything else, and there's a phase adjust. Now, it goes into a circulator which I'll explain shortly and then there's a couple of preamplifier transistors over here and then that leads up into another circulator which then goes into two circulators which basically split the signal out like this into two separate channels.

**Dave Jones:** So, there's actually two power amplifiers in here, two complete separate stages like this. I believe they do this for redundancy so that if one blows, the other one still goes and they can't affect each other.

**Dave Jones:** It recombines in a circulator and then comes out down here. That's tapped off for an overload indicator display like that. Beautiful. Now, I promised to briefly mention circulators. So, let's give that a go.

**Dave Jones:** Let's have a look at these circulators down here. What a circulator does, it's a passive device that uses ferrites and it basically does RF power protection. So, it basically circulates the power through to a dummy load here.

**Dave Jones:** So, if some idiot shorts the output of the antenna here, then what it will do is automatically dump all the energy into the load like this. The load is internal.

**Dave Jones:** Well, no, this might be external but it it dumps it into the load instead of blowing up your transistors over here. Very, very nice and you can probably see the power resistor is going to be under there near the output circulators for combining.

**Dave Jones:** There you go. That is very, very nice bit of kit and I'll have to do a more detailed teardown on that. So, hope you enjoyed that. Now, one that we all like on the EV blog hopefully is debunking.

**Dave Jones:** So, let's have a look at a debunk, shall we? Ta-da! Right, which product is going to win the [ __ ] product of the century award cuz century's only 17 years old.

**Dave Jones:** So, well, there's a lot of contenders, isn't there? You know, Batterizer, Solar freaking Roadways, and all sorts of stuff, but this one I think takes the cake. The sheer number of uh the dollars that have been invested in this and just the sheer ridiculousness of the idea.

**Dave Jones:** Let's take a look, shall we? The winner is, drum roll, Ubeam. Now, if you haven't uh seen it, I've done a blog post 2 years ago uh debunking the Ubeam uh concept as have many others, including the uh former vice president of engineering at Ubeam has even debunked it.

**Dave Jones:** This is how bad it is. Okay? Now, if you don't know what it is, it is uh ultrasonic wireless power transfer. It's like Wi-Fi for charging. Woo! That gets all the investors juiced up, doesn't it?

**Dave Jones:** Yeah. It's going to be the energy infrastructure of the future. Oh, by the way, 28 million bucks they sucked out of the investors for this boondoggle. Unbelievable. They reckon it's safe.

**Dave Jones:** They They reckon it can be used in buses, trains, planes, cafes, gyms, hotels, and stadiums. You can sit in a stadium, if I had my phone, here it is, sit in a stadium and big huge stadium and your phone magically charges.

**Dave Jones:** What's that? Yeah, [ __ ] Unbelievable. And it will power TVs without wires. You can sit TVs in the middle of the room and they just magically work. Woo!

**Dave Jones:** Pixie dust. Um now, they were very secretive for a couple of years and then they finally revealed some stats. They've been working on this for like 5 years, okay?

**Dave Jones:** And they finally said, "Oh, we can do a 4-m radius and at and we can charge a phone at 1.5 W." Yeah, it's not nearly as good as USB can do, especially USB-C these days.

**Dave Jones:** You can wonder why anyone needs wireless charging at all, really, with how fast modern chargers can actually go. And they released their specs for how much what their transmit power is, 145 dB to 155 dB at 60 kHz SPL, sound pressure level.

**Dave Jones:** Now, we'll talk about that in a minute. Now, look, the power with ultrasound in air, different mediums have different things, it drops off with a square of the distance, approximately.

**Dave Jones:** You know, um 3 dB per meter. Nice round number. That's actually what it kind of is in air. So, it even if you're a 1 m away, just with the air alone, no other losses, you lose 50%.

**Dave Jones:** It's only 50% efficient. And so, at 2 m, the efficiency is already 25% right off the bat, before you start including. And that's assuming 100% efficient transducers, no nonlinearities, 100% focused.

**Dave Jones:** By the way, um if you have if they've got an array like this, it's actually slightly bigger bit bigger than this, then they can actually turn on only parts of it and get a smaller aperture size, and that will have an a better natural a different natural focus distance.

**Dave Jones:** And I believe with roughly the size of the transmitter they've got, it's about maybe a meter and a half guestimate is the natural focus distance. So, that is beam forming as well, so they can do electronic beam forming to follow your phone.

**Dave Jones:** So, they've got some very cool tech, actually, to locate where your phone is, and then beam form. It's about a half second lag, which you can see in their video of phone.

**Dave Jones:** It's a Granted, they've got some cool tech. Um but, let's just look at I mean and well, actually, let's not. This has to be short. I could go into the numbers here.

**Dave Jones:** 145 dB to 155 SPL is like uh gives we can basically get maybe my estimate at a meter, you know, 2 m you might Yeah, you can get that 1 and 1/2 watts.

**Dave Jones:** It's not a problem. And there's two ways to analyze this. One is with a continuous a fixed transmit power, and the other one is with a variable transmit power where they change the size of that transmit aperture and pump more energy in to maintain 1.5 watts at every distance, for example.

**Dave Jones:** That's their figure. If they could charge quicker, they'd be boasting about it, but that's the best they could boast. 1.5 watts. It's It's getting down towards trickle charging, and it drops off with square of distance, but it doesn't matter.

**Dave Jones:** This thing? No. It does not violate the laws of physics. Yeah, and yes, it does work. This thing can work. You can charge a mobile phone using ultrasound at several meters.

**Dave Jones:** It is possible, but the efficiency is down in the single-digit percentage, and in practice, it's going to be possibly sub 1% efficient because things it's affected by temperature, pressure, which is altitude, humidity.

**Dave Jones:** There's non-linear effects. There's saturation in the air because you're pumping in so much pressure sound pressure level that the atoms just the molecules just go and they can't do it like that that they just die.

**Dave Jones:** They saturate, poor little things. And you know, you can't get you reach a saturation point. Anyway, we could go through the result It doesn't matter. The numbers do not matter with this.

**Dave Jones:** I'll show you a whole bunch of stuff on another whiteboard where I've got some major points that just blow this thing right out of the water. Let's go. And by the way, I'll link in a video of the CEO of Ubeam.

**Dave Jones:** I challenge you to try and sit through all 15 minutes of it. It's really bad. Take it away, Meredith. For each technological hurdle deemed insurmountable by the experts, I would spend just a few hours thinking about the problem from a variety of approaches.

**Dave Jones:** So, I was able to solve problems when the PhD experts couldn't with just a few hours of really simple research. Every single argument over why the technology couldn't work has been indisputably wrong.

**Dave Jones:** This taught me to be skeptical of experts, that expertise represented a narrow way of looking at things. Engineers are inherently linear thinkers and tend to take a very binary approach to solving problems.

**Dave Jones:** As a non-expert, I had an advantage because I could look at a problem from different angles because I just didn't know what was possible. By thinking outside the box, by thinking around corners, you can out-think the top thinkers.

**Dave Jones:** And now, 8 months later, I have four of the top ultrasonic engineers in the world working for me or working with me. It's going to work and it's going to be awesome, and I can't wait to give the middle finger and smile to all the engineers that criticized the crap out of me.

**Dave Jones:** This is why UBeam it will never work or any ultrasonic charging technology, why it's not practical. Let's go to number one, the efficiency. It's going to be bad. As I said, if it's 1% I'll eat my tin foil hat at 4 m.

**Dave Jones:** Like, give me a break. It's the worst efficiency charging technology by an order of magnitude on the market. Um and remember, it's going to be very bad for the planet.

**Dave Jones:** If everyone implemented this, the planet would be screwed. Energy usage and energy consumption is one of the biggest problems we have on this planet. You might know of the Energy Star legislation where it's actually uh against the law to sell products in some countries that have aren't very efficient chargers, mobile phones and things like that.

**Dave Jones:** They need a certain standby power, they need a certain efficiency, otherwise you're not allowed to sell them. The MEPS regulations, all that sort of stuff. So, right there off the bat, this thing shouldn't have even made it past the first concept.

**Dave Jones:** It's just the efficiency. Who's going to want this? It's just ridiculous for the planet. Unbelievable. Anyway, cost. The cost, you need hundreds of these transducers that can do the 145 to 155 dB SPL in this thing and for the transmitter, hundreds and hundreds of them and you need maybe 100 of them for a phone size thing.

**Dave Jones:** If we've got like 100 of these things on the back of a phone and these are already sold in massive volume at several in for the automotive industry. They're several dollars each.

**Dave Jones:** Yeah, you might be able to pick them up on AliExpress for like 50 cents or something, but there's no way that Willy Wonka's transducer factory is going to churn out transducers of this uh you know capability and efficiency for anywhere near a practical consumer cost.

**Dave Jones:** It's just ridiculous. You need so many of them. Uh and then we'll compare that with the competition in a minute. Size, how thin can you make these things really?

**Dave Jones:** You can't. Look at their design. They've spent 5 years on this tens of millions of dollars in development and they've got a brick, an actual a big brick which um they you know you have to hold in a certain direction.

**Dave Jones:** Like it's got to be flat on to the thing. There's a reason they hold it like that. Crazy. Nobody's going to want that. There's no way it's ever going to get thin enough thinner than a Qi charger that we'll look at.

**Dave Jones:** It's just right off the bat there. Uh it's gone and safety and legality. Let's have a look at that. They on their website, it's all about safety and uh but most countries actually have either legislation or recommended uh safe levels of 110 dB SPL.

**Dave Jones:** So Ubeam is up to 3,000 times higher than what almost every country recommends as a safe limit for ultrasonics. And like it's ridiculous. Don't let them convince you otherwise on the website.

**Dave Jones:** It's just [ __ ] and waffle. Now, five and this is the face palm. This is where it should never have made it off the bloody napkin. You come up with the idea of ultrasonic phone charging.

**Dave Jones:** Okay, let's run the back of a napkin. Let's see how pretty feasible this is. People put and use phones face up on a surface. So, you've got all your receiver transducers on the back.

**Dave Jones:** Eh, in a cafe, which is one of their big usage scenarios, things not going to charge at all, zero. It's ridiculous. And people hold them in their hands at odd angles like that.

**Dave Jones:** Once you tilt it like that, you'll notice that they hold them in their demo perfectly like that with their fingers. Wow, of course it's going to work. But when you people hold them like that at angles and when their hands on the back, you've lost half your transducer area anyway.

**Dave Jones:** It's ridiculous. And people store them in their bloody pockets. Bloody modern huge phones barely fits in my pocket. But they store them in their pockets, their bags, where it's absolutely useless.

**Dave Jones:** There is right there off the bat it should not have been funded or made it off the back of a bloody napkin. It's just not a practical uh charging environment.

**Dave Jones:** Let's compare it with the competition, the Qi charger. My phone has a Qi charger already built in. Wireless charging. It's already built in to most a good lot of them phones on the market.

**Dave Jones:** It's called uh Qi and it's already built in and it's very efficient. Upwards of 50% efficient. Pretty good. Order of magnitude better than Ubeam will ever be at its best.

**Dave Jones:** Uh and it's cheap. You can buy one of the charging pads for five bucks on eBay delivered. Delivered to your home. Like it's There is no competition. There's no way that Willy Wonka's transducer factory is going to churn out these things for anywhere near the cost of what the Qi charger and the thinness of a Qi charger with the coil in there, a tiny little slither of a coil, and uh

**Dave Jones:** just the controller charger a to go with it? You've been there and it's just every one of these points is a showstopper. It's just dumbest idea ever. Anyway, that wins the [ __ ] product of the century, decade, year, whatever.

**Dave Jones:** It's pretty dumb. Anyway, let's wrap it up. So, that's it. That's 1,000 episodes. Hope you enjoyed it. That was pretty much done in It was done in a single take.

**Dave Jones:** And that was the idea, bit of a medley on everyone's favorite segments. I could have done it in more detail. I'll play around with those scopes a bit more.

**Dave Jones:** That amplifier teardown is a bloody a ripper. It's a Bobby Dazzler, so needs more detail on that. But, thank you for everyone who has uh supported me from day dot when I uploaded um just a silly little idea I had um for a video blog onto my personal YouTube channel, posted on Oz Electronics, and I don't know.

**Dave Jones:** I thought maybe 1,000 people would watch it, but I got 1,000 in the first week or two. And uh it's been grow Two years later, this, sitting in a lab, off the cuff, doing this sort of crap is my full-time job.

**Dave Jones:** Has been for 6 years. So, thank you to everyone who's sub- subscribed, viewed me. Some have viewed every video from day one. Awesome work. And everyone on the forum, and everyone uh all my advertisers who've kept me a financially afloat and all that sort of jazz.

**Dave Jones:** And yeah, this is probably video 998 officially numbered and 1,100. I don't know. I've done a crap load of videos. It's got 1,000 in the title. It's pretty official.

**Dave Jones:** So, there you go. That wraps it up. Thank you very much, and hope you enjoyed it. Catch you next time. IS IT DONE? WOO! WOO! Single take. Yes! Yeah.
