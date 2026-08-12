---
video_id: HZ21DX9kA7c
title: Mobile Cell Phone Radiation SAR Testing - EEVblog #201
url: https://www.youtube.com/watch?v=HZ21DX9kA7c
source: youtube-asr
timestamps: {"0": 0, "1": 20, "2": 34, "3": 49, "4": 67, "5": 87, "6": 100, "7": 121, "8": 142, "9": 175, "10": 195, "11": 222, "12": 234, "13": 259, "14": 270, "15": 286, "16": 301, "17": 311, "18": 325, "19": 338, "20": 356, "21": 370, "22": 388, "23": 409, "24": 421, "25": 444, "26": 468, "27": 484}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones.

**Dave Jones:** I'm here with Jason. What have we got? What is this cool looking robot arm? I love it. This is our SAR measurement system. SAR, what's that? Uh specific absorption rate. Right. It's the amount of energy that's absorbed by the human body from wireless devices.

**Dave Jones:** Cool. Mobile phones, that's the big one. That's the big one everyone cares about, right? All right, what does it do? How does it work? Uh this is an E-field probe. Um essentially we dip this probe in this liquid here.

**Dave Jones:** Yep. Uh the liquid's got similar dielectric parameters to uh the human tissue. Right. Uh so we dip the probe probe in there, we put the phone underneath here. Yep. And uh we measure the field inside the liquid. Fantastic. So that's just like a regular That's just water with a bit of bit of sugar and a bit of salt.

**Dave Jones:** Bit of sugar and salt, and that's actually similar to brain tissue, apparently. That's right. That's to say, yeah. And the the idea is to heat is to measure the heat How much it heats up by? a Well, the idea is yeah, to measure the heat, but because uh the heat the temperature changes are too small for accurate measurements, we measure the E-field.

**Dave Jones:** Right. And then using the dielectric parameters of the liquid, we can calculate what the SAR is. Fantastic. So you just put this at a specific height, is that where and then you scan over it? That's right. So 2 mm from the surface, we do a 2D scan.

**Dave Jones:** 2 2 mm, okay. Exactly. nice. It's pretty great. And uh we do a 2D scan, find the find the peak, and then do a 3D scan around that to find the penetration depth. Right. The specially average value. So this is like Does this rotate at This This This is a this is manually rotates, right?

**Dave Jones:** Yeah, this is This is this is all made of plastic and fiber glass. There's no metal parts in here cuz and same with this frame there's no metal parts cuz there's any metal parts can distort the field. Okay, right. And yeah, this is a designed so that we can get the angles exactly right. We've actually Great up close.

**Dave Jones:** Let's have a look. So, this thing was actually used for body testing and a flat phantom. Um Right. Over here we've got the head phantom which you'll see is Oh, right. Okay, so that's a human head. Yeah, that's a They they came up with these dimensions after measuring the a thousand heads from the US Army. This is this is the average head of a American That's the average US soldier's head. That's right, yes. I like it. And yes, so we put the phone under here and we we line it up.

**Dave Jones:** We've got we've got little stickers to to help us line it up. The standards are pretty specific in the angles that we test. Right. Okay. And so that's where that's really where one of those holders comes in handy. Okay, so you just move the holder over to this bench here and then Fantastic. I love it.

**Dave Jones:** And that's just filled with the same same Very similar, yeah. I mean slightly different dielectric parameters cuz this is the brain tissue and this is muscle tissue. Oh, got it. Okay. So, this is it in your pocket. Okay, right. And and you have to keep the room at a certain temperature, is that right? Yeah, the test have to be done sort of between 18 and 25 degrees, but once we start a test it's not allowed to change by more than plus or minus 1 degree. Okay, right. So, it's it

**Dave Jones:** has to be has to remain fairly accurate. Yeah, cuz the dielectric parameters of the liquid changes with temperature. So, so if we measure it in the morning and then, you know, it's 5 degrees warmer in the afternoon we're we're not calculating the correct SAR.

**Dave Jones:** Right. Got it. And how how long does it take to scan? It takes about half an hour, so about 15 minutes for the 2D scan, and then another 15 minutes to do the fine sort of 3D scan. Right. So, you build up So, you go over it once with the 2D and build up a 2D map of it, Yeah. Yeah. It's a coarse sort of 2D map around it sort of maps the field, and then once we found where the peak is, then we'll do quite a fine sort of 3D

**Dave Jones:** Right. um scan of And how do you do that? You just move it move the move the probe It's all run by software. All right. Okay. So, but but to build up a 3D map, the probe physically moves upwards. Is that right?

**Dave Jones:** Yeah. Right. And that Excellent. 7 by 7 by 7 points. Um Fantastic. I love it. That's great. That's fantastic. What a cool bit of kit. How much does something like that cost? Uh about a million dollars. About a million bucks.

**Dave Jones:** Yeah. About a million dollars. That's just the robot, and then we've got the Yep. base station simulators with the Okay. So, this is the Yeah. So, this is the um test This generates the uh simulates the Yeah, this this actually simulates the phone. That's right.

**Dave Jones:** Because we're in a shielded Faraday cage here, so we can't get inside. So, that generates into a SIM. Yeah. It just calls up a SIM, and you put the SIM inside the phone, inside the phone. That's right. Yeah.

**Dave Jones:** Fantastic. we've got full control over the power that's being output by the phone and the frequency and all that. So, it's a controlled environment. So, these other um tables, they've got different sort of Yeah, it's it's it's the same setup.

**Dave Jones:** It's just um it's originally from back in the day the the dual band mobile phone at the 900 and the 1800 MHz. So, we have the 1800 MHz liquid in here and here, and the 900 in there and there.

**Dave Jones:** Um Nowadays with 3G and seem to be 4G, there's a lot of different frequencies, and Yeah. you've got Wi-Fi as well, so we end up having to change um liquids quite a lot, which is what's at the back there. There's Oh, okay. You got all the different types of liquids and Right, so you can actually test Wi-Fi products here as well.

**Dave Jones:** Right. What sort of RF ranges can you do? Like, the power output levels can you test, do you know? Um I'm not sure about the power output levels. I mean, And mobile phones like a 1 or 2 W peak, isn't it? Peak when it's transmitting.

**Dave Jones:** the average I think is around 250 mW. Uh we've we've measured 10 W transmitters in here. Okay. And that wasn't quite getting to the to the peak of it yet. And it measures It's got a huge dynamic range, actually. It's all fiber optic, so there's not much noise.

**Dave Jones:** Okay. All right. It's very It's quite expensive equipment, so you'd expect pretty good specs from it. Yeah. And um yeah. So, are you going to hazard a guess as to whether or not mobile phone causes any problems? Do you use it 5 hours a day with I don't use it 5 hours a day.

**Dave Jones:** Okay. I I think if you use a mobile phone sensibly Sensibly, yeah. you're fairly safe. I think that's that's the go. All right. And what else? These are just They're They're the controls on the back? Uh these are RF amplifiers.

**Dave Jones:** Oh, RF amps, yep. Yeah, we've got that set up. Before any measurements we do, at the start of each day we'll do a sort of a measurement of a known source. Got it. All right. So, just put a um sine wave at 250 mW, the frequency that we're planning to measure, and measure the SAR of that to make sure it's sort of where we expect, so that the system's working okay.

**Dave Jones:** Got it. Do a confidence check before we start. All right. So, how do you calibrate? How do Do you have a ref So, just a reference standard as your calibration or what? yeah. Well, all this equipment gets calibrated once a year in Switzerland. And then we we get the reports back, and then before we start a test we'll do the same thing and confirm that our results are within 10% and that's just a confidence check to make sure the system Okay. Yeah. Cuz you really wouldn't need

**Dave Jones:** to be terribly accurate with this thing, would you? Is it it's probably a relative A lot of it would might be relative. No, it's it's actually an absolute value. Okay. It's the amount of it's definitely it's it's measured in watts per kilogram. So it's it's it's Okay.

**Dave Jones:** Yeah. Got it. Fantastic. Thank you very much. That's all right.
