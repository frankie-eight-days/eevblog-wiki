---
video_id: 586Zn1ct-QA
title: EEVblog 1547 (Part 1) - Contacting the Voyager 2 Space Probe
url: https://www.youtube.com/watch?v=586Zn1ct-QA
source: youtube-asr
timestamps: {"0": 1, "1": 19, "2": 49, "3": 78, "4": 100, "5": 117, "6": 133, "7": 158, "8": 195, "9": 216, "10": 233, "11": 264, "12": 281, "13": 299, "14": 317, "15": 354, "16": 382, "17": 419, "18": 450, "19": 483, "20": 498, "21": 519, "22": 548, "23": 573, "24": 603, "25": 616, "26": 634, "27": 650, "28": 673, "29": 699, "30": 714, "31": 738, "32": 757, "33": 776, "34": 798, "35": 813, "36": 843, "37": 864, "38": 898, "39": 917, "40": 948, "41": 971, "42": 990, "43": 1019, "44": 1037, "45": 1056, "46": 1074, "47": 1089, "48": 1118, "49": 1134, "50": 1150, "51": 1171}
---

**Dave Jones:** Hi, currently the furthest man-made objects from Earth are the Voyager space probes launched in 1977. Voyager 2 is currently 17 billion kilometers from Earth. That's like going to Pluto and back and then back to Pluto again at roughly. And we can still contact it.

**Dave Jones:** How? Let's find out. So, what does it take to track Voyager 2? A big antenna. So, in the case of this 70-m deep space station 43, so we can track on smaller antennas. We have a couple of beam wave guides that are 34 m.

**Dave Jones:** But if you want a nice signal with a lot of margin, you pick a big antenna. So, looking at it, you got 8,000 tons, 4,000 below the bearing. Essentially, 4,000 tons at swivel. It's all hydraulic. 43 is a hydraulic antenna and it uses a unique platform called a hydrostatic bearing. So, there's no friction. So, it the whole antenna that moves rides on a film of oil 7,000th of an inch thick.

**Dave Jones:** Pressurized 2,500 PSI, it just lifts it a tiny amount and it slews around. At the moment, we are looking at Voyager 2 we're tracking now. The beam width of the antenna on X-ray band 30 millidegrees. So, so we deviate any further side to side, we lose it.

**Dave Jones:** So, in fact, it's not just the antenna pointing that's the important thing, it's the sub reflector as well. Uh the sub reflector sort of moves on all axis and we actually have calibration tables that so as the antenna goes down, we have a squint factor.

**Dave Jones:** Where essentially the antenna will sag and it has to be compensated for as well. Now, that's just the antenna side. So, we have obviously that has to be extremely accurate. Then we also have the RF side. And that's where the interesting stuff comes in.

**Dave Jones:** The antenna's pointing up. Surface of the dish, classic parabolic. Classic Cassegrain. Where it bounces off the dish surface, hits the subreflector, and then is reflected down into the cones. Now, low noise amplification is important. So, we certainly don't want to introduce any more noise than the sky is giving us. So, we we cool it.

**Dave Jones:** And all our LNAs are cryogenically cooled. About a tropical 4 and 1/2 Kelvin. So, you get rid of the the noise effect there. In fact, the whole system noise temperature of one of our antennas, if you look at from the cone to the the receiver itself is probably no more than 19 Kelvin. So, when you're looking for very small signals in essentially a field of noise, yeah, you don't want to be introducing any any further noise. If you look at what we are receiving, strangely enough,

**Dave Jones:** Voyager isn't the weakest signals you expect it to be because it's so far and and it's it's our weakest signal, but it doesn't really work like that. Voyager is weak. We so probably have around about -158 dBm. But we do have lower. Voyager has a nice big high gain antenna.

**Dave Jones:** So, we all have a number of missions and I'll I'll give you an example. So, we have Kepler, which is literally just outside of our atmosphere and it's looking for exoplanets. While it's looking for exoplanets, so it's configured to talk to us on its low gain antenna.

**Dave Jones:** And we can be receiving in the mid neg 160s. So, it's even lower again. Maven, we have around Mars again, so not very far away at all, relatively speaking. Uh so, and you know, we can be picking up a neg 170 DBM on Maven. And that's because it's high gain antenna is oriented towards a towards Mars. It's actually so transmitting its housekeeping, which is essentially all it is. It's 20 bits per second. It's It's a tiny bit rate.

**Dave Jones:** Uh so, just to allow us to know that everything's cool, everything is operating fine, and the spacecraft health is is good. -158 about we receive. So, what does that give us as far as telemetry? Telemetry on Voyager is a huge 160 bits.

**Dave Jones:** So, it's been that for quite a while, and we're hoping we won't have to go any lower. Uh we have the margin on the 70-m. So, Voyager we actually receive 160 bits. Uh the symbol to noise ratio on on this antenna here is around about 6 and 1/2 7 dB.

**Dave Jones:** Uh that's the symbol noise ratio, so the bit rate is 160 bits, as I said, but we actually use a an encoding method called the multi-convolutional encoding. Same thing you have in your ADSL modems. And what that does is a fact it's a it's a form of forward error correction.

**Dave Jones:** Uh so, you transmit 320 symbols to get your 160 bits of data, but it gives you a 3-dB improvement. It doubles the symbol SNR. We now have a bit SNR of double that, or should I say 3 dB, not double as in numbers. You're looking at 34-m, so obviously it takes about three and a bit 34-m to to be the equivalent 70-m. We're hovering around zero on the symbol to to noise ratio. So, you can tell if we have a a a a little bit of rain on a 34-m it wipes Voyager out.

**Dave Jones:** When we go below probably 30° and you start getting the the ground noise coming up, it wipes out Voyager. So, what if we don't have a 70-m available during that period, what we'll do we'll array two 34-m. So, not the equivalent of a 70-m, but it gets us past that hard so I suppose a little bit more of a margin so we can serve ride that weather out and we can get a little bit lower on the horizon.

**Dave Jones:** As far as transmit, Voyager has essentially different requirements for its transmit. Uh we have a BLF where we transmit a series of ramps and this is to try and characterize uh a failed capacitor that happened eons ago and we've we've we've handled that all the way up to today. So, this is their secondary receiver, so the first one is dead. So, and if you think of Voyager 2, it's it's a very 1977 and you think of the technology around at the time.

**Dave Jones:** Uh and yeah, so and it was just a failed a failed component. So, unfortunately the the backup had already died. So, whoever designed it came up with this clever idea of if I don't talk to it within a certain time, then obviously the spacecraft thinks there's something wrong and then it goes into a safing mode where it's get grabs its star scanner and starts scanning around making sure it's orientated towards Earth. So, another method had to be thought of to actually get into the receiver that was failing. So, that's

**Dave Jones:** where we had to categorize the best lock frequency or the rest frequency of uh the receiver and we'll do almost on a weekly basis a best lock frequency characterization where we just transmit a ramp. And then 30 hours later, we see the receiver status. So, we'll get a lock status and we'll have a speed. And we'll know then that when we have to transmit later on commands to it, we know exactly the the frequency that we need to transmit on. You know, so you look at radios and and then you look

**Dave Jones:** at the DSN. And if we're more than a couple of hertz out over 15 billion kilometers, we're doing something wrong. So, it's it's a you know, to put into perspective so uh subcarrier loop bandwidth is half a hertz.

**Dave Jones:** Half a hertz. So, so so they're all really tight tolerances so and and all the spacecraft that we do support, including Voyager, are certainly well characterized as well. Uh and also we have a wonderful system. Voyager doesn't use it where uh the spacecraft will turn a a signal round at a fixed ratio as well.

**Dave Jones:** So, we actually have a predicted frequency that arrives back on Earth because it's referenced to our frequency of within .02 of a hertz. Again, so these things can travel billions of kilometers as well. Uh so, we we uplink. So, we have an 18 kilowatts and that allows us to send a no up command. So, every now and again we'll send a series of commands which are essentially just commands saying you're happy. Just reset that timer and we'll talk to you another time.

**Dave Jones:** Uh and we compensate from the failed capacitor by just retransmitting that same command. As we start ramping those frequencies, we'll just keep on transmitting it. If one gets in, that's all we need. With uplinking commands as far as a sequence where we're actually telling it to do a mag roll or some other form of calibration, we can't we can't rely on luck.

**Dave Jones:** So, what we'll do then is we'll characterize the best lock frequency, but we'll transmit 75 kW. We'll get that margin into the spacecraft, so that receiver can hang on just that little bit further. And so so far, so it seems to be a successful method, and it has been for the last 20 years. If you look at weather, the impact of weather, which is really the a good way of characterizing where we drop it off. And you talk about system noise temperature. So normally I say

**Dave Jones:** we're about 19°. If we get a rain shower, that signal uh sorry, the the SNT, the system noise temperature can raise to round about 90 K, and and above. And we all see that 7 dB SNR just disappear to zero.

**Dave Jones:** Right. So rain is is a big factor here. I should point out with Voyager as well, it has two frequencies. So we receive on X, but we transmit S. So completely different systems. In fact of one thing you can't see is we have two separate cones.

**Dave Jones:** And so and you'll see we have an S band cone and an X band. And you go, well hang on, so how do we focus on both cones at the same time? Well we use a dichroic mirror. Think of a a band pass filter. So it's a piece of a hardware.

**Dave Jones:** So what we have is we have the S and X signals coming down and a dichroic plate. I'm trying to get you on there. A dichroic plate, which is has perforations, which have been drilled to allow X band through at that wavelength, but reflect the big chunky Sierra bands, which are reflected to a little umbrella mirror, and then down into the the cone.

**Dave Jones:** So it follows the same path all the way to the dichroic, and from there they're actually separated out. Think of not so much signal level, I think of Kelvin. It probably adds two or three Kelvin. Right. So it does introduce a little bit of noise, and it does attenuate ever so slightly, but it's marginal. When we start looking at some of the even Mars Reconnaissance Orbiter and so of Mars Odyssey and they're pumping down 3 megabits.

**Dave Jones:** They're using either a turbo 16 or an MCD 16. So essentially out of 6 bits only one's good but we can get down to a minus 6 symbol SNR. So you're you're looking so proportionally more noise than signal.

**Dave Jones:** So and you go, "Okay, well how do you pick the signal out of that?" And fortunately noise is random. It is. Where hopefully the signal isn't. So we're able to from that minus 6 symbol SNR we can actually get a positive 5 or 6 bit SNR. So using that encoding method. So a lot of projects what they'll do is they'll sacrifice symbol SNR.

**Dave Jones:** So for essentially so of knowing that they'll get the better so of bit SNR at the end of it after they use a coding. Sierra band on 43 is 400 kilowatts. Uh we've used it probably twice since I started here 30 years ago.

**Dave Jones:** Uh S band is a funny frequency now. So we've the the Deep Space Network has tried to move out of the Sierra band and now Sierra band is uh to the moon. All right. But after that we we like X and now K.

**Dave Jones:** KA. So KA is coming in into it as well about 32 gigs. Uh so as far as weather is concerned the KA is a real pain. S band is really robust. I mean you and I suppose you look at the the size of a raindrop and the you know the size of a an X band bandwidth well it's about so big. So yeah there's obviously a fair amount of attenuation in that raindrop.

**Dave Jones:** You're talking about S band. Right. So it's it's far more robust. So So it's the physical size of the water drop that does the damage. Exactly right. So we also have the physical issues of water on We actually use a a cap con window.

**Dave Jones:** Uh so, which is so essentially a a film a plastic film that goes over the cones. Uh nitrogen pumped to keep it moist keep the moisture out. It blows them out. Uh and RF is transparent. So, if we get water beading on that, we actually have attenuation as well. So, so we we've got a a retro fitted vacuum cleaner set to reverse. So, that that's continuously blowing that blowing that water off and I'll stopping it from settling as well.

**Dave Jones:** We try to use uh essentially commercial power as much as possible. Obviously, it's cheaper. Uh we have recently gone to a 3-MW uh so, up system which can take us to 3 minutes. So, it can deliver deliver 3 MW for 3 minutes.

**Dave Jones:** But, in in that 3 minutes, hopefully our diesels have started kicking in. So, we have uh four 3/4 of a MW so, of Caterpillars in there on one station and four in another. So, we can provide oodles of power. Uh but but yeah, we try to use commercial uh and on that 3-minute ups and uh but we always have the backup with the diesel. In fact, so when we go to level ones and for us a level one is anything that involves uh encounters, uh landings. So, for instance, when MSL

**Dave Jones:** hit Mars, well, gently, not like Beagle. That hit Mars. So, uh then then the site would have been on on on diesel power. So, and so so, regardless of what the commercial power does, we've got a guaranteed power supply.

**Dave Jones:** If you look at the DSN, you know, we're here to essentially to to establish that connection between the the project and and the spacecraft. Voyager was launched in 1977. Uh the Deep Space Network has supported it so from launch. So, you know, it's um I I still have colleagues who who can remember that launch now. So, I'm a relative newcomer at 30 years. So, we actually have a a guy who's 15 years and he's said to be here dog watch.

**Dave Jones:** So, and he was he was he was the last recruit. So, so uh Voyager's a special spacecraft for the entire DSN. Uh the fact that Canberra has the only visibility makes it even more special. Uh we do have sight of Voyager 1 and every time we go down on Voyager 1, it's like it feels that we're poaching.

**Dave Jones:** Right. So, because nobody can see our our Voyager 2. So, Voy- Voyager 2 is definitely a southern hemisphere spacecraft that's really so belongs to Canberra. Uh so, we have a vested interest to make sure that it lasts. And whereas Voyager 1 has has exited into interstellar space, Voyager 2 has isn't there yet.

**Dave Jones:** So, we're still waiting for that milestone as well. So, so there's with Voyager 2, there's still an element of anticipation. So, and you know, you think of a spacecraft just going out and out and out doing nothing. It's not. It's still an active spacecraft. You know, so on a regular basis, it's doing calibrations that we're monitoring on Earth. So, you know, when it it calibrates its uh magnetometer in what they refer to as a mag roll where they spin the gyros up a couple of days before and they rotate

**Dave Jones:** the entire magneto- uh spheric antenna around and then they'll do it again. And we actually see that variation on the downlink as well. So, and here we are 15 billion kilometers away and you really do feel a part of it. So, even though you're separated by an awful lot of space.

**Dave Jones:** Uh what we have for the future, Voyager was launched with an RTG and as far as a power source, uh which means it has little pellets of pluto- plutonium that uh have a half-life of a fair way, I think it's 70 odd years, I think for for plutonium.

**Dave Jones:** Uh unfortunately, the RTG themselves are starting to break down, so it's not the plutonium that's the issue, it's essentially the uh the transducers. Uh so, we can't see us tracking Voyager beyond say 2025, which is still a fair number of years.

**Dave Jones:** And we're still hoping that it'll hit interstellar space sometime within the I'd I'd I'd hate it to lose it and then so suddenly it found it. And 160 bits, we can still go further down. Right. We can still go down to 40 bits.

**Dave Jones:** 40 bits per second? 40 bits per second. So, in fact, it does that now, so when it does uh so changes on board, so and it does equipment swaps, it will go down to an engineering 40 bits. And we're talking about the paint drying. Uh so, 160 bits takes probably about 3 or 4 minutes to lock. So, 40 40 bits, you know, you're you're pushing it out a little bit further. As you talked about Maven, the 20 bits, it can be anything up to 14 minutes to lock. After 13 minutes,

**Dave Jones:** you find there's some some issue with configuration. It's a It's a long wait to get to that second frame. So, so that can be an issue as well. So, so now Voyager uh is is quite special for the Deep Space Network and so you know, other spacecraft will come and go, but that's the one that's going to endure.

**Dave Jones:** Did they design it to last that long? Did they think it would? I suppose uh by its nature, uh the fact that it had the RTG meant it could. Right. Uh I honestly don't believe they thought it would. You know, you look at the primary missions that they had, you know, Saturn Jupiter.

**Dave Jones:** After that, it was all it was like, "Woohoo!" Yeah, bonus. So, it was. And the fact that they actually got one shooting out to the south and one shooting out to the north of the ecliptic, so gave a little bit of diversity as well. And so, you know, not so much for Voyager 1, but Voyager 2 had the the secondary encounters. And and they just kept on going. Sad thing we went in the wrong right part of the space to do Pluto.

**Dave Jones:** Right. But, so you know, so uh the Uranus Neptune sort of encounters were quite special as well.
