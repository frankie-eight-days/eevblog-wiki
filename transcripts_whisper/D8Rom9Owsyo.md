---
video_id: D8Rom9Owsyo
title: EEVblog #973 - Hioki Multimeter Review & Clamp Meter Teardown
url: https://www.youtube.com/watch?v=D8Rom9Owsyo
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 16, "2": 35, "3": 56, "4": 73, "5": 86, "6": 113, "7": 134, "8": 158, "9": 172, "10": 196, "11": 211, "12": 232, "13": 249, "14": 262, "15": 278, "16": 299, "17": 319, "18": 343, "19": 364, "20": 385, "21": 407, "22": 423, "23": 445, "24": 466, "25": 492, "26": 516, "27": 539, "28": 557, "29": 576, "30": 594, "31": 614, "32": 631, "33": 650, "34": 663, "35": 685, "36": 706, "37": 728, "38": 746, "39": 760, "40": 777, "41": 796, "42": 818, "43": 840, "44": 861, "45": 882, "46": 902, "47": 924, "48": 947, "49": 962, "50": 979, "51": 995, "52": 1013, "53": 1031, "54": 1048, "55": 1062, "56": 1082, "57": 1103, "58": 1122, "59": 1142, "60": 1157, "61": 1173, "62": 1191, "63": 1207, "64": 1231, "65": 1248, "66": 1266, "67": 1282, "68": 1300, "69": 1325, "70": 1345, "71": 1367, "72": 1386, "73": 1402, "74": 1418, "75": 1432, "76": 1449, "77": 1465, "78": 1487, "79": 1503, "80": 1520, "81": 1533, "82": 1549, "83": 1563, "84": 1577, "85": 1596, "86": 1612, "87": 1629, "88": 1643, "89": 1658, "90": 1676, "91": 1692, "92": 1707}
---

**Dave Jones:** Hi, we haven't seen any Japanese Hayauki brand equipment on the EEVblog before, so I thought it'd be interesting to take a look at it. These were sent in by Hayauki through their U.S. agent, teaequipment.net, who you might know, so thank you very much.

**Dave Jones:** Yes, made in Japan, all of this stuff's made in Japan, according to Marty McFly. So I thought we'd take a look at these, primarily the multimeter. I'm not really into big current AC clamp stuff. This is like 4200 amp, you know, clamp-type meter, but we'll do a simple teardown of that.

**Dave Jones:** I'm a bit more interested in the multimeter. This is not an electronics... well, what I don't call an electronics industry multimeter, it's an electrical multimeter. That's because it doesn't have, like, microamp range and the capacitance doesn't go down low enough and other stuff like that, but anyway, I thought we'd take a look at it.

**Dave Jones:** Could be interesting. Hmm, let's go. Optional comms, which I don't think they give, but hey, drop-proof, dual display, and supposed to be fast, and all that sort of stuff. Let's check it out. And that's what we get in the box. It's blue, all the best stuff comes in blue.

**Dave Jones:** Let's check that out. It's not quite EEVblog blue, but it's blue nonetheless. I don't know about the purple hold button there, that's a bit of an unusual choice, but anyway, that looks and feels quite neat. Well, let's give it a twist test. Actually, that's not...

**Dave Jones:** that's not the best I've felt. Hmm, range switch feels okay, positive detents on that. Looks like we've got four AAA batteries. Geez, I'd want to get good battery life. And the probes look and feel really nice, yes, flexible silicone insulation on them. Not the sharpest tool in the shed, but yeah, it does the job.

**Dave Jones:** Gold-plated, Hioki-branded probes, and they do have the slip-on cat4 thingamabob. And underwriter's lab-listed cable, thank you very much. And you know what we say here on the EEVblog, don't turn it on, take it apart. That looks like a sensor, like ambient light sensor or something, or is it a LED?

**Dave Jones:** It could be like a high-voltage LED, I don't know. Read the manual, RTFM. Speaking of which, the manual is all in English, and look at that, it's thick as! And it looks really quite jazzy, it's got all the requisite diagrams. Ooh, look at that, AC frequency response, oh that's the filter, hence why it's got a filter button on the front there,

**Dave Jones:** which is rather interesting, that's just the variable frequency, you know, the typical 1 kHz thing. 4 to 20 milliamps, nice manual. They've gone to town on that. Let's have a quick look at the back of it, there's our infrared comms serial interface, that just plugs in there.

**Dave Jones:** IR LEDs, very typical. Single screw, hopefully the battery compartment just comes out. Anyway, we are talking HRC fuses on both of those ranges, as you'd expect for a quality brand, you know, cat4 rated meter. No worries. What's under the hood? 4 AA batteries, just the one big HRC fuse there, 11 amps.

**Dave Jones:** That's only for there, they do milliamps on that as well. Obviously if they had microamps range, then they'd have to do that with only the 3 jacks, they'd have to almost certainly do it through there, and require another fuse on that, but nope, just there.

**Dave Jones:** Unfortunately it doesn't have microamps, so to my mind it's not usable as an... It's usable as an electronics meter, it just doesn't have your typical electronics meter microamp functionality. There's nice deep grooves around the side of that, so that should protect it. It's all in its own little enclosure there, the big HRC fuse, so if that releases the magic smoke,

**Dave Jones:** then it shouldn't do too much other damage, so that's very nice. And of course a machine-threaded screw as you'd expect, none of that self-tapping rubbish. Like I showed before, you get the... the holster comes off really well, it is quite thin and compact and lightweight without the batteries in it, but it does...

**Dave Jones:** I'm not sure if you see that, but I can feel it. There is quite... you know, a little bit of flex in that, although this... you know, once you put it in the holster, I have no doubt it's going to survive its 1 meter drop.

**Dave Jones:** On the concrete, it's just not the... it's not the most stable case I've seen. Alright, screws are out. Yes, they are self-tappers, but that's fine, because you never have to get into the thing. Oh, come on. Hang on. I must have a bloody clip somewhere.

**Dave Jones:** No, stupid me has to take the fuse out because they've got the plastic under there. That's actually... that's not bad at all. I think that's the first time I've seen that. Alright, one more time for the dummies. Let's lift that off. And we're in like Flynn, no wires going over to any buzzer or anything like that.

**Dave Jones:** Oh, I like the... look at the... First thing I noticed was the dual wipes on the battery contact. That is probably the best battery-to-PCB implementation I've seen. Big thumbs up for that, I'm very, very impressed. Wow, and nice big pads. Ah, it's all happening.

**Dave Jones:** That looks neat and tidy, doesn't it? Look at the input jacks. Geez, they're pretty good. Held down with... they would be metal-threaded inserts inside there. And going down to both sides, four solder points. Looks very robust. We've got ourselves the high-voltage isolation slots here.

**Dave Jones:** Very nice between the separate one over here and the two different input paths here. And from the fuse, wow, they know what they're doing. That is really very neat and tidy. I'm very impressed with that. Now at first I thought this glass job here must be like a gas discharge tube or something like that.

**Dave Jones:** But get it under the macro lens and you can see there's a couple of little contacts either side with what looks like a ceramic-type substrate in there. Wow! I don't think I've ever seen that before. Very unusual. What's going on there? Wow, look at that!

**Dave Jones:** Yeah, I think it's still some form of gas discharge tube, GDT-type thing, but it's using some ceramic former in there, and those black dots look like maybe a staged breakdown or something, and maybe, you know, like a controlled breakdown discharge tube or something like that.

**Dave Jones:** Wow, that is neat. That's a first. And the best part number I can get off that is CSB242M. So, yeah, like, you know, you Google that and you get like little fuse GDTs and stuff like that, but I can't find the exact one.

**Dave Jones:** If I can, I'll edit it in. But anyway, yes, it is open, so it's some form of, you know, high arcing GDT thing. Anyway, check out the beautiful guard tracing going back here to protect against surface leakage on the PCB. The center trace there is what they're guarding against.

**Dave Jones:** Very nice. The designers knew what they were doing here. There's our current shunt resistor, 10 milliohms, R010 is the dead giveaway there. That'd be our current front end, and that job there is the 74HC4052. I love it that even these days, like, just jelly bean,

**Dave Jones:** you know, 74HC4000 series type switching logic is still used. Wow. Geez, check out all the diode array there. They must be doing that for range switching. And under the shielded hood there, there's our Hioki branded chipset, the HAZ0105. I doubt they're spinning their own, but hey, I could be wrong,

**Dave Jones:** so it could be like a rebadged one of, you know, three main multimeter chipset manufacturers in there. And there's our two, there's our LED and our photo receiver there. And ta-da! For all you MSP430 fanboys, there you go. So it should be reasonably low power, MSP430, the choice of low power champions there.

**Dave Jones:** That'd be our programming interface for that. There's our little surface mount buzzer. And not a huge amount more around there, really. So that's about all she wrote. So that is certainly a very well-designed, neat and tidy, well-manufactured bit of kit. Thumbs up. And check out the really deep grooves they've got on there for blast protection around the outside.

**Dave Jones:** Yep, they're doing everything right. Fantastic. So as far as input protection goes, they haven't really gone overboard there. They've got the one PTC in series here, and they've got the one gas discharge tube, but that's it, no MOVs, but a GDT is exactly, performs the same function as a MOV.

**Dave Jones:** In fact, that looks like a really schmick, expensive jobby. But hey, you know, it's, I'm sure it is, no doubt meets the latest IEC, you know, CAT4 standard for this. If you have a look at the general specs here, they don't really tell you anything about that.

**Dave Jones:** It just says safety, it meets EN61010, which is, it doesn't say what version of the standard, doesn't say whether it's independently UL tested or anything like that. So, I mean, Hioki make quality bits of kit, so I'm sure it's more than capable, but yeah, there's no independent testing labels at all.

**Dave Jones:** And that goes for the back too, there's nothing there. And for all you mode-labeling fanboys, there you go. APS off, buzzer off, and auto backlight you can disable. Is it my imagination, or are they all held to skelter there? Like, not lined up, they're all angled.

**Dave Jones:** Not sure what's going on there, what the? Anyway, nice to be able to disable the backlight. And for those who desperately want to see the bottom, we've got another high voltage resistor string there, but that's about all she wrote. But that little thing on the front panel, that was either an ambient light sensor or a LED,

**Dave Jones:** I'm sure it's a LED, it's, oh, it'll be due with the voltage detection. OK, so when the voltage detection thing does its business, then yeah, it'll light up and flush the LED. And the range switch looks like a pretty standard implementation, with the little knobbly things on the side which go into the indents there.

**Dave Jones:** That should work a treat, should be pretty reliable. And the tilt and bail on it, nice and wide at the bottom, does the business. Doesn't fall over when you push the buttons. Yeah, once again, I can't help but feel, I mean, see if you can hear this.

**Dave Jones:** Here we go. You can just hear it, you know, like, it just does not feel like a brick, you know, which is what I want an industrial electrical multimeter to feel like. So I'm going to say that's, you know, the case is unfortunately quite flimsy,

**Dave Jones:** which is a real, which is a shame, because it's otherwise brilliantly designed and manufactured. But yeah, just a bit of a fail there. And unfortunately the LCD isn't the best contrast, or the biggest. I mean, it's a dual display, so you know, it's going to have a smaller display of course.

**Dave Jones:** I mean, the EEV log meter, that's as big as digits get on meters basically. So not so much the size, but yeah, just the contrast isn't terrific. But high up, it does the job at high angles though. And as far as backlights go, it's barely even noticeable.

**Dave Jones:** Hmm. If I turn the lights completely off, yeah, it's probably going to do the business, but it's certainly not bright. Hmm. Probably the weakest one I've seen, I think. Anyway, we switch it on, and dual display of course in AC mode is going to display the frequency up there.

**Dave Jones:** Got a nice little bar graph up there for the battery. That kind of makes me concerned about what the battery life is. It has to have a bar graph. Hmm. And it's actually in the specs. I like how they tell you what it actually goes down to.

**Dave Jones:** It's 1 volt per cell, because there's 4 AAA cells in there. So you're using up, you know, a good majority of the capacity in the batteries before it starts blinking. Now I like how it actually tells you the voltages in here, and it complete power shutdown at 4 volts,

**Dave Jones:** but it doesn't really tell you, like it's going to be blinking at you from 4 to 4.5. Presumably it's going to still meet its specs at the low voltage. So you get down to 1 volt per cell. So that's good. That's using, you know, a good majority of the energy in your AAA batteries,

**Dave Jones:** but unfortunately continuous operating time, 130 hours with backlight off. No, that's not what you want from 4 AAAs. You want a couple of hundred hours. I don't like it. It's good, like it's good enough, but it's not, no, it's not in the better class of meters, that's for sure.

**Dave Jones:** And whoa, yeah, 6 milliamps, you know, that's okay, that's reasonable, but yeah, it's just like on a non-datalogging, non-high functionality type meter, it's probably a bit too high for AAAs. Check this out, I really like that it's got a separate continuity switch position.

**Dave Jones:** No touching the buttons or any rubbish like that. Let's see how quick it is. Whoa! Oh yeah, that is latching and instant. That's one of the best there is. Check this out, it's also got visual alert. Why can't they latch that? Why can't they, like, when it, as soon as it buzzes they should latch that,

**Dave Jones:** rather than just have it continuously on. Like, they've gone to the effort to do that, but they haven't gilded the lily. I want my lily gilded, please. Auto-ranging response. That was quick. Oh, I don't like the beeping. It doesn't have an option to disable that.

**Dave Jones:** I find that really annoying, but geez, that's damn quick auto-ranging. Nice. And check this out, if you turn the min-max, like, turn it to average mode, like this, it just keeps beeping at you that it's, like, Oh, what? Give me a break, that is going to a new average.

**Dave Jones:** Oh, geez, lucky you can switch that off. But check this out, I do like how the secondary display actually displays the live reading, and the primary display displays your min-max and average. That's a real nice implementation. Thumbs up for that. Unfortunately, if you turn that beeper off by holding filter when you power it on,

**Dave Jones:** sure enough, it goes away, okay? Look, it's fine, it's now silent, but your continuity buzzer doesn't work. No, no, fail. Like, no. You always want your continuity buzzer to work. Like, no. And another reason why this isn't an electronics class meter as I would define it,

**Dave Jones:** it doesn't have a low capacitance range. The minimum is the one microfarad range. I've got to plug it in the right way, or the electrons will fall out. And there's my 10 nanofarad reference cap. Sure enough, but yeah, it's only designed for electrical applications,

**Dave Jones:** large motor, you know, run motor start capacitors, large values, things like that. So it's good enough for its purpose, it's just not an electronics class meter that can measure puff. And this is pretty disappointing. Diode test range, 1.5 volts maximum for your four AA batteries.

**Dave Jones:** Four of them, and they can only do 1.5 volts max, so that won't even light up a red LED. So, yeah, disappointing. And the lowest current measurement range, 60 milliamps. And, well, that's fine for electrical stuff. Once again, electronic stuff, eh, not good enough.

**Dave Jones:** And by the way, yes, this is a 6,000 count meter, 6,000 count primary and secondary. And the specs aren't going to set the world on fire. Typical 0.3 volts, that's, you know, good enough for a 6,000 count instrument. But this class, plus minus 5 digits, you've got to read the numbers anyway for the different models.

**Dave Jones:** Oh, it's a bit tighter for the model we've got. I think the 425356, yeah, I like a tighter spec meter. Plus minus 3 digits for our particular model. In your typical 10 megaohm input impedance. But, yeah, it's an electrical class meter. Not going to set the world on fire spec-wise.

**Dave Jones:** And the low Z mode here, there you go, it's got low Z up there. It's just like 900 odd K down at the, you know, 1.5 volts test voltage or whatever. That's going to decrease, of course, when you increase the voltage. But some meters, like the BM235, don't switch on at all.

**Dave Jones:** And they give you 10 meg, anything below 8 volts or something like that. So, yeah, anyway, low Z mode, it's going to work a treat. Unfortunately, no input warning jack alert when I plug it into amps. You saw that in the teardown when we have it in voltage mode.

**Dave Jones:** So that's something you want in an electrical meter. So that's a disappointing oversight. And it's bang on spec on the voltage, no worries there. Oh, yeah, yep, that's good enough. And, yep, it doesn't overshoot. Switches very nicely to the exact reading, nice. And it's bang on current too, no worries.

**Dave Jones:** And bang on resistance too. So there you go, that's the Hioki DT4256 electrical digital multimeter. And it's designed and built quite well. The only issues I had with it, you know, lack of little stuff like input jack alert, things like that, that annoying beep thing,

**Dave Jones:** and when you disable it, the continuity tester goes off. But it's fast and accurate, does the business. But, meh, in that case, it's just not the most robust thing around. But, yeah, designed and made very well by the looks of it. Not sure, of course, the certification and all that,

**Dave Jones:** not independently certified, or not that I can tell anyway. So T equipment have this for, well, listed at $199, but it's on clearance special for $159 or something. That's US Yankee dollars, of course. So it's a reasonable value for a top brand meter made in Japan.

**Dave Jones:** So, yeah, it's quality, it's just not as robust as it could be. And a few little things, but it's going to do the business. Battery life, not great, but it's not embarrassing either. So that's not a bad attempt at an electrical class meter.

**Dave Jones:** It's probably going to serve you quite well. Definitely compared to the cheapies, that's for sure. Whether or not it's good value in this range, I don't know. I haven't surveyed the electrical class range meters and stuff like that. I don't know. But if you've got a comment on this,

**Dave Jones:** whether or not you think it's good value, because it's certainly designed and produced quite well, leave it in the comments down below. Alright, now we've got the Hioki 328070-70F clamp meter. I wonder if it comes with both types of clamps. I rather like the flexible clamps like that.

**Dave Jones:** Anyway, this is like for big stuff. This is like 4200 amps, thank you very much. But it's got multimeter functionality in there with the separate probes. So, here we go. We've got ourselves a manual thick as, but it's got all of the languages.

**Dave Jones:** Anyway, ooh, that's smooth. Silky smooth. Let's open this puppy up. Oh, that's slim as. Wow, I like the slimness of that. Let's give that a twist test. Yeah, like there's no like holster or anything. Don't know if it's supposed to be drop-proof. I think, yeah, drop-proof.

**Dave Jones:** I assume like the one meter drop, I don't know, was straight onto the plastic or onto the clamps. I don't know, but clamp meters are vulnerable in that respect. But, jeez, I like how thin that is. That's really quite jazzy. You could almost slip that in a, if you had a pocket big enough.

**Dave Jones:** Hmm, not quite sure about that. Anyway, it's got like thumb rotating switch thing. Oh, sorry, I turned it on before I took it apart. But that's current and then AC voltage and then DC voltage. It's cat 3, 300 volts. Cat 2, 600 volts, which is not really what you want

**Dave Jones:** in an industrial meter that goes up to like, you know, a thousand amps or whatever. Really, you know, you want sort of like cat 4 type stuff, don't you? But I guess in this sort of form factor, you're not going to get that.

**Dave Jones:** Ooh, look at that, doesn't have standard. Um, banana jack's on the bottom. Ooh, and sure enough, the pros, once again, nice silicone leads on them, no worries whatsoever. But I've got to call that a fail for a custom lead interface. Your leads bust, you lose them, whatever,

**Dave Jones:** and they're not, they go in there, okay? But jeez, I don't know, it almost feels like a pocket clamp meter. Like not a proper, you know, not a proper real big man, rugged, you know, meter. So let's do the continuity mode. Nah, slow as a wet week.

**Dave Jones:** Nope, nope, fail. And it looks like it runs off a single CR2032 battery. That's nice, draws 15 milliwatts. So what's the battery life of that? I'll pop up a curve somewhere here, I'm sure. You bet we get the flexi probe with it. Beauty.

**Dave Jones:** Um, that's up to 4200 amps, because the main one here is only up to 1000 amps AC. But Cat4 rated 300 volts, and like, it's got CE, but no, like, independent, you know, type approvals on this. No independent testing. Hioki, I don't know, you know, why they're not going to be doing that.

**Dave Jones:** Maybe they think, oh, their own one is enough, and it is, but it's always nice to see, you know, independent UL or other type approval. Anyway, that plugs in like that. No worries. And this just pulls out. You don't have to twist it or anything like that.

**Dave Jones:** I believe it's got a magnet in there, because it kind of sort of sucks it in and holds it quite well. Rather like that implementation anyway. You just fold that around the cable you want to test, and Bob's your uncle. The problem here is that this is an AC clamp probe only,

**Dave Jones:** so not designed for DC, so it's not going to use that Hall effect sensor in there. So unfortunately, yeah, it's for AC only. It's a specific purpose. It's designed for a purpose. So if you need like a real thin, simple, you know, AC clamp meter,

**Dave Jones:** then it's going to do the business. But apart from that, no, it's not, you know, it's not DC, and it doesn't have standard banana jacks or anything like that, and the continuity test is pretty meh on it, and well, yeah, designed for a job.

**Dave Jones:** Of course, I should have seen that on the box, AC clamp meter. You know exactly what you're buying, so, you know. I'll just show you the difference in thickness between the Fluke AC wireless 3000 FC current clamp and this one. There's a huge difference there.

**Dave Jones:** Once again, this is an AC only current clamp, and yeah, this one's just tiny and lightweight compared to this thing. Alright, here we go. We've got four self-tapping screws on there. I like the little holder down in there. Oh, yep, no cables. There we go.

**Dave Jones:** We're in like Flynn. Once again, Hioki chipset, or Hioki branded chipset. It could be using an off-the-shelf. Oh, we've got that GDT again. Yep, we've got the exact same CSB242M, I believe it is. Once again, it's hard to see the numbers on there,

**Dave Jones:** but yeah, exactly the same. Oh, the through-hole ceramic cap just bent on the side there. It's a bit low rent. Didn't really expect that. They haven't gone to the effort to, you know, like make these PCB mountable or anything like that. They've just sort of wired them over.

**Dave Jones:** Granted, they've put little bits of insulation on there. You know, neat touch, but yeah. I'm not going to write home to my mother about it. Is that a 32 kilohertz watch crystal in there? Um, low power. You don't need, this doesn't need to have fast updating

**Dave Jones:** or the rest of it, so maybe they are operating the chipset at 32.768 kilohertz. Hmm, who knows, or it could have its own faster internal oscillator, but there'd be no reason for a real-time clock in something like this. Oh, is that a trimmer?

**Dave Jones:** Oh, I didn't want to see a trimmer in there. Gee, oh, there's another one! There's another one! Ah, trimmers all over the place. So as far as the multimeter side of this thing goes, you know, they've got the GDT in there, gas discharge tube for the overload, stuff like that,

**Dave Jones:** but no PTCs, you know, they've got the three high-voltage input resistors, this high-voltage input resistor here, but that's about it. You know, typical pocket multimeter type stuff. Nothing wrong with that. It's just is what it is. So yeah, there's really nothing else to see in there,

**Dave Jones:** apart from that, which is kind of fun. I don't know, I would have liked it. You know, it's sold as wired directly on the board, I don't know. Hmm, isn't it better to have a connector? Yeah, it would have been a nice touch, but I don't know.

**Dave Jones:** Yeah, it's reasonably neat and tidy. You know, it's reasonable for its functional, for its purpose, I guess. So yeah, there you go. That's inside the Hioki 328010F, little almost pocket-like AC clamp meter. It's probably as small as you can make a clamp meter,

**Dave Jones:** I think, you know, with external inputs. That's probably as small as you wouldn't want to see it made much smaller, really. But, you know, it's probably going to do the job. So yeah, I wouldn't go using, like, the multimeter functionality of this in, like, industrial applications, but it's probably just, you know,

**Dave Jones:** designed as, oh, it's got a handy little multimeter extra plug-in, you know, it's only cat 3, 300 volts, but hey, there's no current capability in this thing, which is exactly what you'd expect, so no worries there. So you don't have to worry about, you know, that sort of functionality.

**Dave Jones:** You've just got to worry about, you know, over-voltage surges and things like that. So yeah, I don't know. But as an AC clamp meter, sure, it works quite well. I'm not going to bother to go hook it up to AC wires and measure it.

**Dave Jones:** I don't know. Have a look at the specs. I'm sure it meets it. It's a proper brand, Hioke. It's going to do the business. What is it? AC. Oh yeah, 1.5 digits, minimum range, 42 amps. Eh, it's not my kettle of fish, but hey,

**Dave Jones:** for those in the AC, large current AC clamp field, it's probably not a bad pocket one. Are there any others this thin? I don't know. I don't know the market. Anyone? Bueller? Bueller? So there you go, that's a quick look at two bits of Japanese kit.

**Dave Jones:** An electrical multimeter and a pocket AC clamp meter. And they hold up reasonably well. Yeah, just a few little minor issues. They seem to do, you know, a reasonably respectable job for what they're designed for. So if you like the video, please give it a big thumbs up.

**Dave Jones:** If you like review videos, I do have a plan at the moment to get more into product review videos. So if you want more product review videos, definitely give it a big thumbs up. Leave it in the comments down below. And we'll see what we can do.

**Dave Jones:** Maybe I'll discuss it on the forum of what my plans are and things like that. Anyway, catch you next time. Thanks for watching.
