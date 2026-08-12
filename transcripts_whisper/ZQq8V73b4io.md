---
video_id: ZQq8V73b4io
title: EEVblog #1207 - ARM Dev Boards Falling From The Sky!
url: https://www.youtube.com/watch?v=ZQq8V73b4io
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 18, "2": 42, "3": 62, "4": 76, "5": 96, "6": 118, "7": 132, "8": 155, "9": 168, "10": 184, "11": 203, "12": 215, "13": 233, "14": 242, "15": 263, "16": 280, "17": 298, "18": 312, "19": 327, "20": 342, "21": 359, "22": 388, "23": 400, "24": 416, "25": 435, "26": 460, "27": 469, "28": 490, "29": 509, "30": 532, "31": 551, "32": 568, "33": 578, "34": 594, "35": 601, "36": 624, "37": 641, "38": 660, "39": 683, "40": 705, "41": 714, "42": 735, "43": 746, "44": 765, "45": 784, "46": 794, "47": 811, "48": 824, "49": 844, "50": 854, "51": 854, "52": 884, "53": 884, "54": 914, "55": 944, "56": 953, "57": 974, "58": 1004, "59": 1028, "60": 1047, "61": 1068, "62": 1086, "63": 1099, "64": 1118, "65": 1132, "66": 1144, "67": 1163, "68": 1182}
---

**Dave Jones:** Hi, this one was actually sent in to the mailbag, but it was, I think it should be so interesting that I'm going to do a dedicated video on it. It is a Radiosonde, check that out, and we've seen Radiosondes in the mailbag before and I hope to do a

**Dave Jones:** future EEVDiscover video on Radiosondes, so I'm hoping I can pull that one off. Anyway, we'll see. It is literally an STM32 dev board falling from the sky. This is what these Radiosondes do, they go up, eventually they come down. If you don't know, these are used for our weather observations at airports and

**Dave Jones:** other things that require daily weather observations and thousands of these things go up in the air on little balloons every single day and you're not aware of it, and they fall back down in random locations and it looks like Sondhub.org, where I assume Michael is from, they track these things and

**Dave Jones:** they go and pick them up because they're still transmitting when they come down. So you can, people outfit their cars with a array of antennas, direction finding equipment, and they go hunt these things down. It's really quite cool, so thank you very much Michael.

**Dave Jones:** Apparently this one is an STM32. So literally, is it, oh yep, I made the mistake. It's one of those stupid crud-filled bags. Anyway, oh that looks very similar, doesn't it? And oh, that one looks different. Cool, Australian Bureau of Meteorology. Radiosonde, there you go, do not burn or incinerate.

**Dave Jones:** Yeah, it's Vesala as well, I think they own the market. Anyway, cool, let's check it out. All right, let's take a look at these two new Vesala Radiosondes. As you can see, these are all practically identical to the one we've seen in the previous, but they look almost identical, except this one weighs a lot more.

**Dave Jones:** Maybe this one doesn't, oh, the sun's a bit loosey-goosey inside there. How about that one? No, that one's light as. Sensor probe up here, it looks, this one looks significantly different. I'll show you that in detail at the moment. These are basically temperature and humidity, as well as a GPS location, of course.

**Dave Jones:** That's basically all they do. And a helical antenna on these ones, but no visible helical antenna on that one, unless it's inside. You'll notice that the other difference between this is that this one has a little red button on the top. I'm sure the batteries are worn out, so it's not

**Dave Jones:** going to do anything. So let's have a squeeze inside. And they do have external ports down here, which look to be identical on both of them. So a little card edge jobby there. Yep, almost the same model, except this one's A. Could that be like analog?

**Dave Jones:** And this one's D. Could that be digital? Hmm, we'll find out. And it's pretty obvious what the weight difference is. This one has batteries and this one doesn't. Look, of course, it's in styrofoam because you want to temperature protect the batteries. And look at them.

**Dave Jones:** They've just taken standard Panasonic AA's and just welded those together. So they've just made their own custom packs and they've glued them. They probably just buy them like that, do they? Hmm. And both of them included, well, actually, this one included two by the looks of it.

**Dave Jones:** These little liquid bottles. There's some sort of liquid in there. I assume that's water. Is that, do they, maybe that like keeps the batteries warm. Maybe they like actually warm these things up. First, I would assume, like it wouldn't be like an icebreak.

**Dave Jones:** There'd be no point doing that, I guess. It's already cold enough up there. So I assume that they're keeping the batteries warm with these things. So they keep those in the thermal chamber. And then once they're, you know, moments before they're about to go out, they're going to go out and they're going to go

**Dave Jones:** out and they're about to launch. They whack the battery pack in there, check it all out and have their little heat brink, brick, I assume. So that would like go either side of the battery because they're molded to go around the battery like that.

**Dave Jones:** So yeah, that looks like to be a custom solution. That's neat. And those two look absolutely identical. I don't think I can spot a difference between those at all. This is the old one and this is the old one in quote marks. This is the new one.

**Dave Jones:** Sorry, this didn't have, we've been promised, an STM32 dev kit falling from the sky. But I don't see that as an STM32. It's actually got Vassala branded on it. So maybe it is an STM32. It makes sense. They wouldn't roll their own custom ASIC for this.

**Dave Jones:** That makes absolutely no sense at all. So it wouldn't surprise me if that is an STM32. And of course, if you buy any chip, you can, practically any manufacturer will custom silkscreen your chips for you if you order enough. You order, you know,

**Dave Jones:** 10,000 or 100,000 of them, they'll go, yeah, no worries. We'll silkscreen anything you want on there. You want like a platypus on there? Not a problem. We'll just put a platypus. I've just got some boring voltage regulation around there. Don't need much. Just a,

**Dave Jones:** you know, a 3.3 volt, whatever that jobby is. In this section down here, it's hooked up to the helical antenna here. And well, is that our GPS receiver? Let's have a look at that chippy there. I can't see it on my camcorder, but I'm shooting this in 4K, so I can

**Dave Jones:** zoom right in. Thank you very much. Okay, from the GPS antenna, I've got a couple of filters there, and a whole bunch of amplifier parts or whatnot. It seems to be a surprising amount of external circuitry there. And then we get to a UNAV 8021C chipset.

**Dave Jones:** And this is actually a GPS front end, but it doesn't do any of the processing. It's, as its name says, it's just a front end receiver, basically. And it's designed to match with a UNAV receiver. I think it's the 8031. And we don't see that anywhere.

**Dave Jones:** So I can only presume that they're going to be doing the GPS processing also in the processor up here, which is the DSP-1C, the Vesala branded micro. So yeah, they're doing the DSP, implies digital signal, processing. Looks like we've got a little, that looks like an E-squared prom, and not much else.

**Dave Jones:** We've just got a test and/or programming interface. And then it looks like this might actually be the transmitter down here after all. Let's have a squiz. Let's get this can off. We've got a big ass metal can on there. Geez, they're serious about strapping that down.

**Dave Jones:** Look at that. So they've got a copper tab on there, and they've got shielding. You can actually see the, yeah, it's like a metal coated, like a Mylar polyester-y strip kind of thing going up to the sensor elements. Well, they're really serious about shielding on this.

**Dave Jones:** So take off the outer shield, and we can get two more inner shields here. We've got one for all the sensor elements. So that'd be probably ADCs and signal conditioning under there, whether or not they're using external ADC, or whether or not it's just signal conditioning or whatever.

**Dave Jones:** And the micro is actually doing the ADC in. I'm not actually sure, but is that like our transmitter can or something? Well, there's only one way to find out. And sometimes if you don't want these again, I find it's often easier just to cut the shields off rather than trying to de-solder, like, almost all of it right

**Dave Jones:** around the edge like that. And good thing about these is that you can just wiggle, wiggle, wiggle, yeah, and you can break them off. Just get in there with a pair of cutters and snips. There we have our transmitter. Aliens confirmed. There we go.

**Dave Jones:** And I'm sure all the RF people are going, "Oh, yeah, I know what the heck that is. That's a doof-a-winkle topology." And if we flip it over, there's our transmitter and another Vesala-branded chip. It could, of course, be an off-the-shelf chip. I don't know what the protocol here,

**Dave Jones:** apart from saying it's a synthesized transmitter on 400.15 to 406 megahertz. Transmitter range up to 350 kilometers, frequency stability plus/minus two kilohertz, deviation 4.8 kilohertz, blah, blah, blah. Output power minimum 60 milliwatts. And it uses GFSK modulation at a downlink rate of 4,800 bits per second.

**Dave Jones:** So they're using, yeah, some sort of custom transmitter there. Like, it's only low power. Like, 60 milliwatts is not an awful lot. Let's just add in a teeny, tiny little bit of inductance down there. Just wiggle, wiggle. Yeah, AC coupling cap. And then that looks like it,

**Dave Jones:** I presume, pops out to the... Why are there two Vs there? What's going on? I need to get under there. So this is actually surprisingly well-engineered, or I'm not going to say it's not over-engineered, but you know, there's a lot of parts and a lot of effort that goes into designing something that is

**Dave Jones:** literally disposable. They use it once and they throw it away. Yeah. Like, they just pollute the environment with these things. And granted, I'm guilty of that before. I worked in the Sonoboy industry designing Sonoboys that they deploy those once and they work for like, you

**Dave Jones:** know, 10, 12 hours or whatever. And then they actually burn through a resistor on the flotation bag that sinks them to the, literally sinks them to the bottom of the ocean. Um, so that the Russian trawlers couldn't come along and pick them up anyway.

**Dave Jones:** That was the, yeah. But these things just drift anywhere. And of course, they tell anyone who, if this lands in your back, uh, yard, they tell you what it does. Um, it is expendable and may be disposed of as may be convenient. Do not burn or incinerate.

**Dave Jones:** That's because of the batteries. If you want to know how much use they'll get out of these, well, the other one, which we're going to take a look at in a minute, it's got a, uh, nominal operating time of 240 minutes. So that's it.

**Dave Jones:** And it's Gonski. Anyway, if you're wondering how these sensor probes work, well, this one up here, this is a platinum resistance wire, and this is the temperature sensor. Uh, believe it or not, uh, resolution of 0.01 degrees C, response time of half a second,

**Dave Jones:** and a nominal accuracy of, uh, point calibrated of 0.1%. Although the combined uncertainty after ground preparation is 0.2, then it goes up. Combined uncertainty in sounding at less than 16 kilometers is 0.3 degrees, and above 16 kilometers is a different spec. Oh, lousy 0.4%.

**Dave Jones:** But yeah, very nice. And the accuracy also changes with the, uh, pressure as well. Less than a hundred, uh, hectopascals is 0.15 degrees C, that's the reproducibility, and less than a hundred hectopas- hectopascally things is 0.3 degrees. Interesting. And then over here we have the, uh, humidity sensor.

**Dave Jones:** Why they've got two, I don't know. But anyway, this is a, a thin film, uh, capacitor. Anyway, that is the sensor, and you can really, really see that down in there. Look at the detail in that. That, I believe they're identical. There's some sort of, maybe it's some sort of differential thing.

**Dave Jones:** Not entirely sure. Anyway, the temperature sensor is apparently, uh, designed, uh, to prevent solar radiation error, because, you know, you're up high, you're getting a lot of, uh, solar radiation. So that could actually heat up and affect your sensor. Hence why I guess it's so thin and tiny, and it's, you know, separated by the big

**Dave Jones:** air gap, I guess. You know, it'd be a surface area thing, most likely. And that'd all tie in with the, uh, response rate of the, uh, sensor as well, because you want to be able to record, you know, like, fairly fast, uh, fluctuations in the voltage.

**Dave Jones:** And it's also designed to, uh, minimize, uh, evaporative cooling as well. When, like, it goes through clouds, of course, it's going to get all moisture on it or whatnot, because, well, it's a cloud. It's got water in it. Um, then it's, you could have, um, errors caused by, uh,

**Dave Jones:** the evaporation. So, yeah, they're, I'm sure that's very, uh, carefully designed temperature sensor. And I do believe the humidity sensor in there might actually have a little resistive heater in it as well. So that's just, uh, going to act like as a de-icing kind of thing.

**Dave Jones:** And you've got to remember, these are extreme conditions that these things are being asked to operate in. Now let's have a look at this RS-41 model, and apparently this is the popular one with the, uh, ham radio operators and radios on trackers. Cause these ones can actually be hacked.

**Dave Jones:** Apparently they do contain an STM32 processor and they can be hacked and repurposed to actually be used as a ham radio transmitter. So there you go. That will have to be the subject of a second video, but let's take a squeeze inside. As I said, this one is much

**Dave Jones:** lighter than the others. It's got a different, uh, designed sensor element, which we'll take a look at, but it's going to be temperature and humidity, uh, in the same way. And, um, this one's got a fancy-pantsy lead on it. Oh, there you go.

**Dave Jones:** This is a very different, uh, construction to the previous one. But once again, we see the, uh, styrofoam in there. I guess there's nothing really better than cheaper and simpler than, uh, you know, styrofoam for thermal insulation. But we have our board inside here.

**Dave Jones:** That's just going to, yep, that's just going to pop out. So there you go. It's just two halves of the case. And, oh, look at that. Look at that battery holder. Isn't that sex on a stick? Oh, that's just beautiful. Thing of beauty.

**Dave Jones:** It's a joy forever. Look at that. And this one would use, uh, 2AA. This is, uh, classed as, uh, being suitable for 2AA lithium batteries for a nominal 240 minutes, uh, of operation. But this is kind of more like what I would, you know, think like

**Dave Jones:** a disposable one might be. Although, you know, there's lots of fancy-pantsy in the plastic battery holder, but you've got to have that. But it seems to have much more minimalized, uh, power. And, uh, it's got a little bit of a, uh, circuitry on here.

**Dave Jones:** So let's have a squiz. And check this out. None of this tinted VIA rubbish. Look at all the VIAs on here. They're all gold-exposed pads. And that's great for hacking, because you can just, like, uh, get a mod wire and solder it directly on there.

**Dave Jones:** You don't have to scrape anything. Oh, yeah. It's, it's so much better. Ta-da! There's our STM. Processor 32F100C. 8T6B for those playing along at home. And 24 megahertz. Jeez, that's screaming, isn't it? Jeez, you wouldn't think you'd, you know, need that sort of grunt, really.

**Dave Jones:** But, uh, maybe just a switching converter down in there. A couple of local regulators. You can tell they're surrounded by a bypass cap down in there. And it looks like some voltage-set resistors, perhaps. Off-the-shelf connector there for our interface. And, oh, a routed-out slot there.

**Dave Jones:** What that would be for onboard temperature sensor. And this is a common technique that I've, uh, discussed over the years in, uh, several videos, I'm sure. Is that you route out a slot like that, because it prevents, uh, any thermal expansion in the, uh, PCB from actually stressing the, uh, through the leads of your, uh, temperature sensor here through the leads in there.

**Dave Jones:** And then getting onto the die. And that can actually affect the stability of your, uh, temperature reference or voltage reference or whatever it is. So, um, yeah, that's just a common technique for that. And on the bottom, HCUO4. Got to have some 7-4 series in there.

**Dave Jones:** Fantastic. Uh, just got a lot of, uh, other analog-y stuff. Not much else happening there at all. And that there is our transmitter. It's upside down, so all the electrons have already fallen out. But, uh, yeah, you can see that. That's what I want in a trans- that's what I expect to see in a disposable transmitter.

**Dave Jones:** Just a single chip. Not much else. A few passes. Bob's your uncle. And, oh, it looks like I've got some sort of, uh, matching network there or something. And that just goes off to your, uh, just your, uh, like, you know, quarter-wavelength, uh, antenna.

**Dave Jones:** We'll just wire antenna. Just flapping around in the breeze. And that coil there. Hang on. It's not the GPS. It's located near the transmitter. Where's that little via popping out to? Aha! There you go. Look at that. Wow. Got ourselves a, uh, a totem pole driver pair there of output transmitters.

**Dave Jones:** Okay. What's doin'? So, we've got the U-Block's, uh, GPS engine there. You might be wondering, well, where's the antenna? Oh, that's gotta be it right there. Tiny little surface mount patch jobby. What? Like, is it patch or is it some sort of weird fractally thing?

**Dave Jones:** Oh, yeah. Yeah, it's just some sort of patch job. Okay. Oh. Um, good enough for Australia. And there is the humidity sensor on the RS-41. I believe one of those is gonna be the power resistor. Probably that one down there. You could actually get in there and measure that.

**Dave Jones:** And that would be for the power, power resistor in quote marks. That would be for the, uh, de-icing of that. And, as you can see, they've got a different arrangement here. But, surely, that's gotta be the same. That is definitely the, uh... Platinum Resistor Temperature Sensor in there.

**Dave Jones:** Just, so, yeah, it's a totally different, uh, construction to the previous model. Now, unfortunately, I've, uh, powered this up, and, uh, we've got our green flashing light there. Apparently, it flashes that when it's, uh, looking for a connection. Once it's got a GPS, uh, connection, I believe it goes solid green.

**Dave Jones:** And I've checked all the pins on the connector there, and I'm getting no data out of this at all when it powers up or... Anything. So, I don't know if it needs a, uh, GPS lock before it, uh, outputs anything. So, I, I don't know.

**Dave Jones:** I expected to see something there, at least. Anyway, you can, uh, reflash this via this serial port, um, and with an STM32, uh, ST-Link, uh, programmer. And then you can get it to, uh, change frequencies and, and transmit on different frequencies and do everything.

**Dave Jones:** And somebody's reverse-engineered it and, uh, rewritten the software, the firmware from scratch. So, hats off to whoever, uh, figured out how to do that. That's awesome, but, uh, yeah, maybe I'll do that in a second video. But I was hoping to get some sort of data out of this.

**Dave Jones:** Unfortunately, like, there's just nothing there. Can't see it. And yes, I have hooked it up to a terminal program and tried to, like, uh, just input various characters into it to see if I can prompt it, uh, to do something. But, nah, zippity-doo-dah.

**Dave Jones:** So, that's disappointing. Alright, I had to come outside, and what do you know? Yep, it has locked in. Like, it only took, like, two minutes. Tens of seconds to lock in once it has, uh, proper GPS reception. But, unfortunately, um, even with the portable, uh, scope, got the nice, uh, Mixig out here.

**Dave Jones:** The screen isn't the best. Uh, let, like, if I tilt it like that, it's Gonski. But, anyway, the tilt stand is nice. Can still read it. Um, it's, once you get, like, on the high angle like that. Anyway, uh, yeah, I can't find any, there's no signals at all on that output connector.

**Dave Jones:** So, yeah. Yeah, Bama.
