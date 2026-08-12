---
video_id: UhG83WS51q8
title: EEVblog #611 - Electret Microphone Design
url: https://www.youtube.com/watch?v=UhG83WS51q8
source: youtube-asr
timestamps: {"0": 10, "1": 25, "2": 38, "3": 59, "4": 72, "5": 85, "6": 109, "7": 135, "8": 154, "9": 173, "10": 190, "11": 210, "12": 223, "13": 244, "14": 263, "15": 276, "16": 305, "17": 318, "18": 342, "19": 354, "20": 369, "21": 383, "22": 395, "23": 408, "24": 429, "25": 445, "26": 461, "27": 478, "28": 490, "29": 505, "30": 522, "31": 535, "32": 549, "33": 563, "34": 575, "35": 589, "36": 611, "37": 626, "38": 643, "39": 659, "40": 669, "41": 688, "42": 696, "43": 712, "44": 726, "45": 743, "46": 755, "47": 770, "48": 784, "49": 798, "50": 813, "51": 828, "52": 849, "53": 867, "54": 883, "55": 898, "56": 916, "57": 926, "58": 941, "59": 951, "60": 971, "61": 982, "62": 1002, "63": 1017, "64": 1030, "65": 1054, "66": 1064, "67": 1080, "68": 1099, "69": 1118, "70": 1138, "71": 1152, "72": 1176, "73": 1192, "74": 1214, "75": 1229, "76": 1252, "77": 1263}
---

**Dave Jones:** Okay, we're up as far as describing a a typical old style valve microphone. Yep. With uh modern edition in the clay case of the classic two. Let's go back to basic electric mics.

**Dave Jones:** Yep. As found everywhere, which don't have bias, which don't have tube amplifiers. They do actually have buffers, but they don't have output transformers. Nope. None of that rubbish. Yep.

**Dave Jones:** And in fact, I'll So, these are our little 10 cent mics that we find in uh Yeah. everything. So, we'll uh do Uh now, the the solid back electrode might be a ground, or it might be the actual uh hot electrode, if you like.

**Dave Jones:** Right. The diaphragm might be at ground, or it might be the hot. We don't know. The electret to polarize the electret mic mic might be on the diaphragm, or it might be on the back plate.

**Dave Jones:** Doesn't particularly matter. We'll just draw it that way for convenience. And what we've got there is a thing where when we talk at it, we get volts out of it.

**Dave Jones:** Yep. But as transducers go What type of level we talking? Uh Let me think. Typically, they're around about minus, let's call it minus 45 dBV per Pascal. Which translates to, let me see, minus 40 is 10 millivolts, so minus 45 is probably about, oh, I don't know, 4 millivolts or something like that.

**Dave Jones:** So, maybe 4 millivolts. Get it right, lad. 4 mV at 94 dB SPL. Right. that could be minus 35, could be minus 50. Got it. Okay, so if it was say minus 40, that would be 10 mV at 94 dB.

**Dave Jones:** 94 dB corresponding to 1 Pascal. Incidentally, that's the usual format for mic manufacturers to specify sensitivities. So, you have to do the translation of that to there, and that to there.

**Dave Jones:** Yep. Me. Okay. What can you do with a transducer that's putting out, well, 10 mi- 10 mV with a source capacitance of maybe about 5 pF? Huh. Well, let's kick off by sticking it in with a JFET because that's what everybody does.

**Dave Jones:** That's what they do. So, Stick them right in the back there. Yep. So, JFET. And that's pretty much all. That's just about it. Yeah. Now, in the good old days, we'd actually see a discrete bias resistor there to hold the gate near zero.

**Dave Jones:** Yep. That would be a gigohmish resistor. Right. There are, well, how do you put it? Two different basic electrical styles of electret mic. In one of the styles, that that and that are all brought out as separate electrodes.

**Dave Jones:** Yep. The idea being that you can put a voltage on there, hang a load resistor off there, Mhm. and there's your AC voltage with some DC superimposed coming off there.

**Dave Jones:** Sure. Rarely done, even though generally that particular topology offers better linearity and higher SPL handling and all of that kind of stuff. Usually not what happens. Usually what you get is Are they using electret mics in any pro applications?

**Dave Jones:** Yes. Yes. Whereabouts? Uh there are a few stage microphones which are uh back electret types. Mhm. Uh even companies like Sennheiser and AKG are offering uh stage and recording microphones which are electret.

**Dave Jones:** Yeah. Uh To what advantage? Um The I think the main advantage is they're cheaper to manufacture. There's less electronics in there to go wrong. Yep. You know, the bias circuitry, etc.

**Dave Jones:** Uh and you can use them over a wider range of uh uh incoming DC supply voltages. Got it. Uh one of one of the areas where you'll see lots of electrets used in preference to uh externally polarized is whenever you see a skinny gooseneck with a little head on it as used in uh courtrooms, Right.

**Dave Jones:** uh panels, uh parliament, that kind of thing. They're all going to be electret. Yep. And the usual players such as Shure and Sennheiser and AKG, they're all going to be manufacturing that style of thing.

**Dave Jones:** Right. Most of these look like that. Yep. That beastie there, JFET, uh becomes a voltage to current transducer. So, it's a transconductance device. Yep. So, all of a sudden now, what you're seeing here is uh not a given number of uh volts per pressure.

**Dave Jones:** It's um current modulation per pressure. That only gets turned back into a voltage once you add a load resistor. Then work with that. Correct. And then you always see a couple of that.

**Dave Jones:** Yeah. Yeah. And In fact, for some reason, one of the standards is to when they're specifying the sensitivity of these mics, uh their standard is to use a 2K resistor.

**Dave Jones:** noticed that. Mhm. Uh simply because it forms a common base for everybody. Yeah. With a 5-V supply. Yeah. And it just gives everybody a a common a common basis, a common platform from which to work.

**Dave Jones:** Although you can operate them much lower. Supply voltage. Yeah. Now, let's have a look at this. 1.5 V. Yeah. With caveat, with caveat. I've got one right here in my pocket.

**Dave Jones:** Runs off a single single coin cell. Mhm. That's it. Oh, mind you, one 1.5 or 3.something V. No, 1.5. Okay. 1.5 V. There you go. Much depends on the characteristics of the FET.

**Dave Jones:** Yeah. Let's have a look at the current versus current versus voltage characteristics of a JFET. Measured voltage there, Mhm. current through there, zero bias on the gate. Right. Uh most of them will have a characteristic that looks like that.

**Dave Jones:** Once you get above a certain voltage, about there, that thing produces a constant current source. Right. And it's in this region here that you want to operate the FET.

**Dave Jones:** Yeah. Why? Because as soon as you start coming down into this part of their characteristics, the gain, the transconductance of that just goes to party. to shop. Now, went through a stage of measuring rather a lot of different electret mics.

**Dave Jones:** That gain reduction point uh varied from FET to FET. From FET type to FET type. Uh Most of them were good down to around about 1.1 or 1.2 V and would then plummet.

**Dave Jones:** There were some better FETs that would come down to maybe 0.8 V before they started rolling off in gain. run those off a single alkaline cell until they're dead?

**Dave Jones:** Yes. Practically. So for example, let's take a typical JFET that might have a constant current region where it draws about 350 microamps. And that's a very, very, very typical figure It is.

**Dave Jones:** for the JFETs used in electric mics. Let's say up here we've got a single cell at 1.5 V volts. And let's say that that particular FET would maintain its gain down to say 1 V.

**Dave Jones:** Just make the numbers easy. Yep. Okay? What value of resistance can we reasonably put there in order to get those conditions? Well, we've got half a volt across it.

**Dave Jones:** We've got 350 microamps through it. Uh R equals 0.5 V over 0.35 milliamp. And at a rough guess, that's probably going to be about 1.4 K. So something like that?

**Dave Jones:** So you might actually toss in a 1 K resistor. Which means that that battery can be depleted to 1 V plus 0.35 V volts Yep. before it starts losing gain.

**Dave Jones:** Got it. Or you'd pick a FET that instead of having a knee point at 1 V went down to say 0.8 V volts and maybe drew less current. Mhm.

**Dave Jones:** Now, you can make that resistor smaller. Mhm. That will allow you to flatten the battery further before you get gain roll off. Yep. Penalty, the lower the resistor there, the lower the signal gain to that point there.

**Dave Jones:** Of course. So, it's all a compromise. And of course, if you've got a few more volts available, beauty. You don't have any problems anymore. Absolutely. But, any I guess anybody who's using an electret mic in a new piece of equipment needs to know what voltage they've got available so they can plan what resistor they use.

**Dave Jones:** Yep. So, for example, if you've got a piece of kit with a 5-V supply, okay, let's just do this again, but this time with a 5-V supply. Tons of headroom.

**Dave Jones:** You've got a ton of headroom with caveats. You might want to maximize the gain out of that circuit there so you don't have to have as much processing or so that you can maximize the dynamic range of your ADC that follows.

**Dave Jones:** So, you might think, "Okay, let's make that resistor as big as we possibly can." Okay, 5 V 1 V, we've got 4 V across there. 4 V / 0.35 is probably about 12 K.

**Dave Jones:** Vaguely speaking. Okay, beauty. So, you go to print with that circuit. Yep. All of a sudden, you come along with, you know, most of your microphones are sitting there at 350 microamps.

**Dave Jones:** You come along and you've got a fitting there that draws 400 microamps. Guess what? That's trying to suck 4.8 V across that. Okay, 400 * 12 4.8 V. Insufficient voltage there, so instead of getting all of that lovely gain, it goes Yeah, bonk.

**Dave Jones:** Oh, okay, I'll cover my ass instead of putting in 12 K, I'll put in 1 K. Well, you can do that. Yeah. And it'll cover all of those. Yeah.

**Dave Jones:** But you've robbed yourself of so much gain. Yeah. So, maybe pick a resistor that allows the typical voltage there to sit at about half of your rail. This almost goes back to good old bias theory where you can try and bias things at half rail.

**Dave Jones:** Half rail. That's it. Not only will it give you the best dynamic range as far as signal excursion goes. Duh. Yeah. But it also allows for production variations in that fit current.

**Dave Jones:** And you want the flattest battery chemical chemistry possible as well. Now, the voltage rating of those fits is generally about 10 volts. Mhm. So, if you were using a say 12-V or 15-V supply, Mhm.

**Dave Jones:** you might want to either regulate it down a bit or resistively drop it down a bit. Yeah. Or do something to ensure that the voltage there stays below around about that 10-V level.

**Dave Jones:** Mhm. Cuz otherwise they can start avalanching or getting noisy or undesirable effects. And this is how uh this is like the phantom voltage applied on like a PC microphone input.

**Dave Jones:** Yes. like that. They will they will have that voltage superimposed on there and you're supposed to hook up and just the Yeah. two wire Not only that, they have the voltage which is usually around about 3 and 1/2 to 5 volts and they have the resistor built in.

**Dave Jones:** Yes. Okay. So, they've done that bit inside the box. Inside the PC. They only want you to plug that much in. Yeah. Now, there's yet another caveat that you have to be aware of.

**Dave Jones:** Okay. How which is noise on this rail here. Yeah. If this thing if if this JFET is within that working within that constant current region, it's presenting a very high impedance there.

**Dave Jones:** Mhm. Which means that any noise there gets presented immediately to Absolutely. So, anybody who's using these from anything that might have a bit of noise there, like a PC.

**Dave Jones:** No, they're quiet. Uh make sure you decouple the hell out of it. Yep. That's why PC mic inputs are so crap. They really are. They're pretty god awful. Yeah, and sometimes it seemed to be cuz that ground is not at a quiet place.

**Dave Jones:** Absolutely. Yeah. Yeah. Okay, so that's care and feeding electrically of um electric mics. Electret mics. It's It It's easy. Yep. Get the manufacturer's spec on the mic to find out roughly what the quiescent current is going to be.

**Dave Jones:** Mhm. Plan your resistor around that and your supply rail. Too easy. Yeah. Bob's your uncle. Not rocket science. No, not at all. Too easy. It's not unusual these days to see electric mics that don't have that resistor at all.

**Dave Jones:** Mhm. How do you How do they work without being biased? I'm not quite sure. I I I still haven't tested this myself. I've got a suspicion that they're actually relying on things like PCB leakage, Ew.

**Dave Jones:** which is up in the tens of gigohms, hundreds of gigohms, who cares. It vaguely maintains that somewhere within hailing distance is zero. This is like trying to have an a uh op amp like this and trying to AC couple into your Yes.

**Dave Jones:** the bias? And the the only real sources of bias there A leakage. Well, ac- actually there's a couple of sources. First of all, there's leakage down through the gate there.

**Dave Jones:** yep. And that, in fact, is a source of noise as well as bias corruption. Now, typically, if you've got a little fit with little junctions and low capacitance, you're looking at pico amp Right.

**Dave Jones:** leakages. Yeah. Mind you, something to keep in mind about uh JFETs is that leakage current will increase around about at the rate of about a decade per 10° rise.

**Dave Jones:** Oh, okay. So, when temperatures get high, FETs get leaky. Yep. But uh it's not unusual to be talking about pico amps there. So, if you can arrange for uh tens or hundreds of pico amps leakage to ground there by having soggy circuit board or I don't know what to do.

**Dave Jones:** Yeah. Then you can maintain the DC voltage there somewhere within hailing distance of zero. Yeah. Uh the other thing to watch out for, of course, is that's at zero.

**Dave Jones:** We've got signal excursions either side of zero due to that. The negative going ones see a high impedance. Yeah. Any positive going signal greater than maybe 10, 20, 30 millivolts starts to see a forward diode junction down there, and once I've been non-linearly clipped, Ouch.

**Dave Jones:** So, the larger signal, the worse it clips there. Mhm. So, that we're discussing about headroom is a headroom limitation. Right. Now, the other downside of leakage is it's a noise source.

**Dave Jones:** Mhm. Uh I can't remember the the equation off the top of my head for uh noise current, but basically every dribble of electrons that goes down through that gate unit of measure.

**Dave Jones:** Yeah. A dribble's worth. Uh every electron that jumps that barrier Yeah. represents an impulse. It does? And uh the thing is, if you got zillions of them going at once, they kind of iron out, uh which is why the noise of a DC current is proportional to the square root of the current.

**Dave Jones:** Mhm. Double the number of electrons flying through there, and the noise part of all of that those rushing ball bearings, and it increases by a factor of root two.

**Dave Jones:** Right. Uh so, it's a noise source. Mhm. That current gets converted to a noise voltage by the impedance at the gate, which consists of that capacitance, Mhm. that capacitance, that resistance.

**Dave Jones:** Yep. Which will change with frequency. Yeah, it is. But by far and away, generally the most important part of the noise is that resistor or pseudo resistor. Yep. Interesting thing, the higher the value of that resistor, not the higher the noise, the lower the noise.

**Dave Jones:** That is counterintuitive. Counterintuitive. And the reason for that is, okay, let's plot noise voltage versus frequency. Mhm. For a resistor, it's basically flat. Yep. Okay, equal noise voltage per unit frequency.

**Dave Jones:** Yes. Okay, if we double the value of resistance, we increase the noise by root two or 3 dB. Right. Okay, wait, that's 3 dB. Okay, why? Because noise voltage equals root of KTRB.

**Dave Jones:** Yep. So, KTR. So, it's the fact that it's proportional to root resistance. Mhm. Okay, double the resistance, increase by 3 dB only. Okay, but here we've got our resistor in series with its noise voltage source.

**Dave Jones:** Okay, and that voltage there increases by 3 dB added to there, but it's got this low pass filter attached to it. So, that will only be true up to a cutoff frequency, a corner frequency determined by the value of that resistor and the value of the capacitor.

**Dave Jones:** So, let's just say this one, okay, cutoff there. Okay, so its corner frequency is there. When we double the value of resistance, we shift that down to half of what it was.

**Dave Jones:** So, all of a sudden our noise profile looks like that. Guess what? 3 dB lower. So, as long as we are only looking at frequencies significantly above that corner frequency, whenever we double that resistor, we knock 3 dB off the noise because we're in this roll off region.

**Dave Jones:** Very nice. And that's part of the secret to making a low noise mic is make any resistance as high as you possibly can, and make the capsule capacitance as high as you reasonably can.

**Dave Jones:** Totally counterintuitive. Who would have thought? Yeah, so high resistances equal lower noise. Lower noise? It's a bombshell, folks. And that's why Rode Microphones I think I was the first one to go from 100 meg type resistances up to 5 gig type resistances, and it really paid off in making low noise preamps.

**Dave Jones:** Awesome. The other thing to watch out for is that noise current, which as I said, noise current appears across those impedances as a noise voltage. Those impedances, well, guess what?

**Dave Jones:** The The impedance looks like a resistor in parallel with a capacitor. The lower you can pull that down, Yep. the happier everybody is. And the smaller you can make that uh noise current, the happier everybody is as far as keeping the noise down as concerned.
