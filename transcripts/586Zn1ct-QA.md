---
video_id: 586Zn1ct-QA
title: EEVblog 1547 (Part 1) - Contacting the Voyager 2 Space Probe
url: https://www.youtube.com/watch?v=586Zn1ct-QA
source: youtube-asr
timestamps: {"0": 1, "1": 19, "2": 47, "3": 66, "4": 85, "5": 102, "6": 119, "7": 133, "8": 152, "9": 171, "10": 188, "11": 204, "12": 220, "13": 236, "14": 252, "15": 267, "16": 283, "17": 298, "18": 315, "19": 334, "20": 350, "21": 366, "22": 382, "23": 405, "24": 419, "25": 435, "26": 448, "27": 462, "28": 477, "29": 490, "30": 508, "31": 521, "32": 537, "33": 551, "34": 568, "35": 585, "36": 597, "37": 611, "38": 625, "39": 639, "40": 651, "41": 667, "42": 681, "43": 697, "44": 714, "45": 730, "46": 745, "47": 765, "48": 780, "49": 790, "50": 803, "51": 821, "52": 837, "53": 854, "54": 874, "55": 889, "56": 907, "57": 922, "58": 939, "59": 956, "60": 971, "61": 985, "62": 999, "63": 1013, "64": 1029, "65": 1046, "66": 1062, "67": 1078, "68": 1093, "69": 1106, "70": 1119, "71": 1131, "72": 1143, "73": 1155, "74": 1164, "75": 1176}
---

**Dave Jones:** Hi, currently the furthest man-made objects from Earth are the Voyager space probes launched in 1977. Voyager 2 is currently 17 billion kilometers from Earth. That's like going to Pluto and back and then back to Pluto again at roughly. And we can still contact it.

**Dave Jones:** How? Let's find out. So, what does it take to track Voyager 2? A big antenna. So, in the case of this 70-m deep space station 43, so we can track on smaller antennas. We have a couple of beam wave guides that

**Dave Jones:** are 34 m. But if you want a nice signal with a lot of margin, you pick a big antenna. So, looking at it, you got 8,000 tons, 4,000 below the bearing. Essentially, 4,000 tons at swivel. It's all hydraulic. 43 is a hydraulic antenna

**Dave Jones:** and it uses a unique platform called a hydrostatic bearing. So, there's no friction. So, it the whole antenna that moves rides on a film of oil 7,000th of an inch thick. Pressurized 2,500 PSI, it just lifts it a tiny amount and it slews around. At

**Dave Jones:** the moment, we are looking at Voyager 2 we're tracking now. The beam width of the antenna on X-ray band 30 millidegrees. So, so we deviate any further side to side, we lose it. So, in fact, it's not just the antenna

**Dave Jones:** pointing that's the important thing, it's the sub reflector as well. Uh the sub reflector sort of moves on all axis and we actually have calibration tables that so as the antenna goes down, we have a squint factor. Where essentially the antenna will sag

**Dave Jones:** and it has to be compensated for as well. Now, that's just the antenna side. So, we have obviously that has to be extremely accurate. Then we also have the RF side. And that's where the interesting stuff comes in.

**Dave Jones:** The antenna's pointing up. Surface of the dish, classic parabolic. Classic Cassegrain. Where it bounces off the dish surface, hits the subreflector, and then is reflected down into the cones. Now, low noise amplification is important. So, we certainly don't want to introduce

**Dave Jones:** any more noise than the sky is giving us. So, we we cool it. And all our LNAs are cryogenically cooled. About a tropical 4 and 1/2 Kelvin. So, you get rid of the the noise effect there. In fact, the whole system noise

**Dave Jones:** temperature of one of our antennas, if you look at from the cone to the the receiver itself is probably no more than 19 Kelvin. So, when you're looking for very small signals in essentially a field of noise, yeah, you don't want to be introducing

**Dave Jones:** any any further noise. If you look at what we are receiving, strangely enough, Voyager isn't the weakest signals you expect it to be because it's so far and and it's it's our weakest signal, but it doesn't really work like that. Voyager

**Dave Jones:** is weak. We so probably have around about -158 dBm. But we do have lower. Voyager has a nice big high gain antenna. So, we all have a number of missions and I'll I'll give you an example. So, we

**Dave Jones:** have Kepler, which is literally just outside of our atmosphere and it's looking for exoplanets. While it's looking for exoplanets, so it's configured to talk to us on its low gain antenna. And we can be receiving in the mid neg

**Dave Jones:** 160s. So, it's even lower again. Maven, we have around Mars again, so not very far away at all, relatively speaking. Uh so, and you know, we can be picking up a neg 170 DBM on Maven. And that's because it's

**Dave Jones:** high gain antenna is oriented towards a towards Mars. It's actually so transmitting its housekeeping, which is essentially all it is. It's 20 bits per second. It's It's a tiny bit rate. Uh so, just to allow us to know that

**Dave Jones:** everything's cool, everything is operating fine, and the spacecraft health is is good. -158 about we receive. So, what does that give us as far as telemetry? Telemetry on Voyager is a huge 160 bits. So, it's been that for quite a while,

**Dave Jones:** and we're hoping we won't have to go any lower. Uh we have the margin on the 70-m. So, Voyager we actually receive 160 bits. Uh the symbol to noise ratio on on this antenna here is around about 6 and

**Dave Jones:** 1/2 7 dB. Uh that's the symbol noise ratio, so the bit rate is 160 bits, as I said, but we actually use a an encoding method called the multi-convolutional encoding. Same thing you have in your ADSL modems. And what that does is a fact it's a it's

**Dave Jones:** a form of forward error correction. Uh so, you transmit 320 symbols to get your 160 bits of data, but it gives you a 3-dB improvement. It doubles the symbol SNR. We now have a bit SNR of double that, or should I say 3 dB, not

**Dave Jones:** double as in numbers. You're looking at 34-m, so obviously it takes about three and a bit 34-m to to be the equivalent 70-m. We're hovering around zero on the symbol to to noise ratio. So, you can tell if we have a a a a little bit

**Dave Jones:** of rain on a 34-m it wipes Voyager out. When we go below probably 30° and you start getting the the ground noise coming up, it wipes out Voyager. So, what if we don't have a 70-m available during that period, what we'll do we'll

**Dave Jones:** array two 34-m. So, not the equivalent of a 70-m, but it gets us past that hard so I suppose a little bit more of a margin so we can serve ride that weather out and we can get a little bit lower on the horizon.

**Dave Jones:** As far as transmit, Voyager has essentially different requirements for its transmit. Uh we have a BLF where we transmit a series of ramps and this is to try and characterize uh a failed capacitor that happened eons ago and we've we've we've handled that

**Dave Jones:** all the way up to today. So, this is their secondary receiver, so the first one is dead. So, and if you think of Voyager 2, it's it's a very 1977 and you think of the technology around at the time.

**Dave Jones:** Uh and yeah, so and it was just a failed a failed component. So, unfortunately the the backup had already died. So, whoever designed it came up with this clever idea of if I don't talk to it within a certain time, then obviously

**Dave Jones:** the spacecraft thinks there's something wrong and then it goes into a safing mode where it's get grabs its star scanner and starts scanning around making sure it's orientated towards Earth. So, another method had to be thought of to actually get into the

**Dave Jones:** receiver that was failing. So, that's where we had to categorize the best lock frequency or the rest frequency of uh the receiver and we'll do almost on a weekly basis a best lock frequency characterization where we just transmit

**Dave Jones:** a ramp. And then 30 hours later, we see the receiver status. So, we'll get a lock status and we'll have a speed. And we'll know then that when we have to transmit later on commands to it, we know exactly

**Dave Jones:** the the frequency that we need to transmit on. You know, so you look at radios and and then you look at the DSN. And if we're more than a couple of hertz out over 15 billion kilometers, we're doing something wrong.

**Dave Jones:** So, it's it's a you know, to put into perspective so uh subcarrier loop bandwidth is half a hertz. Half a hertz. So, so so they're all really tight tolerances so and and all the spacecraft that we do support, including Voyager,

**Dave Jones:** are certainly well characterized as well. Uh and also we have a wonderful system. Voyager doesn't use it where uh the spacecraft will turn a a signal round at a fixed ratio as well. So, we actually have a predicted

**Dave Jones:** frequency that arrives back on Earth because it's referenced to our frequency of within .02 of a hertz. Again, so these things can travel billions of kilometers as well. Uh so, we we uplink. So, we have an 18 kilowatts and that allows us to send a

**Dave Jones:** no up command. So, every now and again we'll send a series of commands which are essentially just commands saying you're happy. Just reset that timer and we'll talk to you another time. Uh and we compensate from the failed

**Dave Jones:** capacitor by just retransmitting that same command. As we start ramping those frequencies, we'll just keep on transmitting it. If one gets in, that's all we need. With uplinking commands as far as a sequence where we're actually telling it to do a mag roll

**Dave Jones:** or some other form of calibration, we can't we can't rely on luck. So, what we'll do then is we'll characterize the best lock frequency, but we'll transmit 75 kW. We'll get that margin into the spacecraft, so that receiver can hang on just that little

**Dave Jones:** bit further. And so so far, so it seems to be a successful method, and it has been for the last 20 years. If you look at weather, the impact of weather, which is really the a good way of characterizing where we

**Dave Jones:** drop it off. And you talk about system noise temperature. So normally I say we're about 19°. If we get a rain shower, that signal uh sorry, the the SNT, the system noise temperature can raise to round about 90 K,

**Dave Jones:** and and above. And we all see that 7 dB SNR just disappear to zero. Right. So rain is is a big factor here. I should point out with Voyager as well, it has two frequencies. So we receive on

**Dave Jones:** X, but we transmit S. So completely different systems. In fact of one thing you can't see is we have two separate cones. And so and you'll see we have an S band cone and an X band. And you go, well

**Dave Jones:** hang on, so how do we focus on both cones at the same time? Well we use a dichroic mirror. Think of a a band pass filter. So it's a piece of a hardware. So what we have is we have the S and X

**Dave Jones:** signals coming down and a dichroic plate. I'm trying to get you on there. A dichroic plate, which is has perforations, which have been drilled to allow X band through at that wavelength, but reflect the big chunky Sierra bands,

**Dave Jones:** which are reflected to a little umbrella mirror, and then down into the the cone. So it follows the same path all the way to the dichroic, and from there they're actually separated out. Think of not so much signal level, I think of Kelvin. It

**Dave Jones:** probably adds two or three Kelvin. Right. So it does introduce a little bit of noise, and it does attenuate ever so slightly, but it's marginal. When we start looking at some of the even Mars Reconnaissance Orbiter and so of Mars Odyssey and they're

**Dave Jones:** pumping down 3 megabits. They're using either a turbo 16 or an MCD 16. So essentially out of 6 bits only one's good but we can get down to a minus 6 symbol SNR. So you're you're looking so proportionally more noise than signal.

**Dave Jones:** So and you go, "Okay, well how do you pick the signal out of that?" And fortunately noise is random. It is. Where hopefully the signal isn't. So we're able to from that minus 6 symbol SNR we can actually get a positive

**Dave Jones:** 5 or 6 bit SNR. So using that encoding method. So a lot of projects what they'll do is they'll sacrifice symbol SNR. So for essentially so of knowing that they'll get the better so of bit SNR at the end of it after

**Dave Jones:** they use a coding. Sierra band on 43 is 400 kilowatts. Uh we've used it probably twice since I started here 30 years ago. Uh S band is a funny frequency now. So we've the the Deep Space Network has tried to

**Dave Jones:** move out of the Sierra band and now Sierra band is uh to the moon. All right. But after that we we like X and now K. KA. So KA is coming in into it as well about 32 gigs.

**Dave Jones:** Uh so as far as weather is concerned the KA is a real pain. S band is really robust. I mean you and I suppose you look at the the size of a raindrop and the you know the size of a

**Dave Jones:** an X band bandwidth well it's about so big. So yeah there's obviously a fair amount of attenuation in that raindrop. You're talking about S band. Right. So it's it's far more robust. So So it's the physical size of the water

**Dave Jones:** drop that does the damage. Exactly right. So we also have the physical issues of water on We actually use a a cap con window. Uh so, which is so essentially a a film a plastic film that goes over the cones. Uh nitrogen

**Dave Jones:** pumped to keep it moist keep the moisture out. It blows them out. Uh and RF is transparent. So, if we get water beading on that, we actually have attenuation as well. So, so we we've got a a retro fitted vacuum cleaner set to

**Dave Jones:** reverse. So, that that's continuously blowing that blowing that water off and I'll stopping it from settling as well. We try to use uh essentially commercial power as much as possible. Obviously, it's cheaper. Uh we have recently gone to a 3-MW

**Dave Jones:** uh so, up system which can take us to 3 minutes. So, it can deliver deliver 3 MW for 3 minutes. But, in in that 3 minutes, hopefully our diesels have started kicking in. So, we have uh four 3/4 of a MW

**Dave Jones:** so, of Caterpillars in there on one station and four in another. So, we can provide oodles of power. Uh but but yeah, we try to use commercial uh and on that 3-minute ups and uh but we always have the backup with the

**Dave Jones:** diesel. In fact, so when we go to level ones and for us a level one is anything that involves uh encounters, uh landings. So, for instance, when MSL hit Mars, well, gently, not like Beagle. That hit Mars. So, uh then then the site would have

**Dave Jones:** been on on on diesel power. So, and so so, regardless of what the commercial power does, we've got a guaranteed power supply. If you look at the DSN, you know, we're here to essentially to to establish that connection

**Dave Jones:** between the the project and and the spacecraft. Voyager was launched in 1977. Uh the Deep Space Network has supported it so from launch. So, you know, it's um I I still have colleagues who who can remember that launch now. So,

**Dave Jones:** I'm a relative newcomer at 30 years. So, we actually have a a guy who's 15 years and he's said to be here dog watch. So, and he was he was he was the last recruit. So, so uh Voyager's a special spacecraft for the

**Dave Jones:** entire DSN. Uh the fact that Canberra has the only visibility makes it even more special. Uh we do have sight of Voyager 1 and every time we go down on Voyager 1, it's like it feels that we're poaching.

**Dave Jones:** Right. So, because nobody can see our our Voyager 2. So, Voy- Voyager 2 is definitely a southern hemisphere spacecraft that's really so belongs to Canberra. Uh so, we have a vested interest to make sure that it lasts. And whereas Voyager

**Dave Jones:** 1 has has exited into interstellar space, Voyager 2 has isn't there yet. So, we're still waiting for that milestone as well. So, so there's with Voyager 2, there's still an element of anticipation. So, and you know, you think of a spacecraft just

**Dave Jones:** going out and out and out doing nothing. It's not. It's still an active spacecraft. You know, so on a regular basis, it's doing calibrations that we're monitoring on Earth. So, you know, when it it calibrates its uh magnetometer in what they refer to as a

**Dave Jones:** mag roll where they spin the gyros up a couple of days before and they rotate the entire magneto- uh spheric antenna around and then they'll do it again. And we actually see that variation on the downlink as well. So, and here we

**Dave Jones:** are 15 billion kilometers away and you really do feel a part of it. So, even though you're separated by an awful lot of space. Uh what we have for the future, Voyager was launched with an RTG and as far as a power source, uh which

**Dave Jones:** means it has little pellets of pluto- plutonium that uh have a half-life of a fair way, I think it's 70 odd years, I think for for plutonium. Uh unfortunately, the RTG themselves are starting to break down, so it's not the

**Dave Jones:** plutonium that's the issue, it's essentially the uh the transducers. Uh so, we can't see us tracking Voyager beyond say 2025, which is still a fair number of years. And we're still hoping that it'll hit interstellar space sometime within the

**Dave Jones:** I'd I'd I'd hate it to lose it and then so suddenly it found it. And 160 bits, we can still go further down. Right. We can still go down to 40 bits. 40 bits per second? 40 bits per second. So, in fact, it does

**Dave Jones:** that now, so when it does uh so changes on board, so and it does equipment swaps, it will go down to an engineering 40 bits. And we're talking about the paint drying. Uh so, 160 bits takes probably about 3 or 4

**Dave Jones:** minutes to lock. So, 40 40 bits, you know, you're you're pushing it out a little bit further. As you talked about Maven, the 20 bits, it can be anything up to 14 minutes to lock. After 13 minutes, you find there's some some issue with

**Dave Jones:** configuration. It's a It's a long wait to get to that second frame. So, so that can be an issue as well. So, so now Voyager uh is is quite special for the Deep Space Network and so you know,

**Dave Jones:** other spacecraft will come and go, but that's the one that's going to endure. Did they design it to last that long? Did they think it would? I suppose uh by its nature, uh the fact that it had the RTG meant it could.

**Dave Jones:** Right. Uh I honestly don't believe they thought it would. You know, you look at the primary missions that they had, you know, Saturn Jupiter. After that, it was all it was like, "Woohoo!" Yeah, bonus. So, it was. And the fact that they

**Dave Jones:** actually got one shooting out to the south and one shooting out to the north of the ecliptic, so gave a little bit of diversity as well. And so, you know, not so much for Voyager 1, but Voyager 2 had

**Dave Jones:** the the secondary encounters. And and they just kept on going. Sad thing we went in the wrong right part of the space to do Pluto. Right. But, so you know, so uh the Uranus Neptune sort of encounters were quite

**Dave Jones:** special as well.
