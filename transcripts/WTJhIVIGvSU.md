---
video_id: WTJhIVIGvSU
title: EEVblog #609 - Condenser Microphone Design Tutorial
url: https://www.youtube.com/watch?v=WTJhIVIGvSU
source: youtube-asr
timestamps: {"0": 11, "1": 24, "2": 40, "3": 56, "4": 73, "5": 84, "6": 100, "7": 117, "8": 131, "9": 143, "10": 153, "11": 171, "12": 189, "13": 204, "14": 231, "15": 245, "16": 258, "17": 268, "18": 278, "19": 295, "20": 317, "21": 328, "22": 344, "23": 356, "24": 372, "25": 384, "26": 410, "27": 423, "28": 439, "29": 459, "30": 474, "31": 497, "32": 514, "33": 529, "34": 544, "35": 559, "36": 570, "37": 588, "38": 608, "39": 622, "40": 633, "41": 649, "42": 666, "43": 681, "44": 693, "45": 707, "46": 725, "47": 735, "48": 753, "49": 768, "50": 788, "51": 807, "52": 819, "53": 834, "54": 853, "55": 868, "56": 887, "57": 903, "58": 915, "59": 926, "60": 936, "61": 949, "62": 959, "63": 971, "64": 980, "65": 994, "66": 1004, "67": 1015, "68": 1039, "69": 1051, "70": 1065, "71": 1082, "72": 1094, "73": 1105, "74": 1114, "75": 1131, "76": 1148, "77": 1173, "78": 1185, "79": 1200, "80": 1209, "81": 1233, "82": 1243, "83": 1268, "84": 1284, "85": 1309, "86": 1326, "87": 1348, "88": 1362, "89": 1379, "90": 1399, "91": 1419, "92": 1431}
---

**Dave Jones:** I think the next bit I'll talk about is the basic operation of a condenser microphone. Let's do it. Mhm. Um Let's just say we've got a fixed electrode here Mhm.

**Dave Jones:** and we've got a flappy electrode here. And just for the hell of it Mhm. what we're going to do is we're going to ground that one. Yep. And we're going to polarize that one with a polarizing voltage.

**Dave Jones:** We'll call it positive for the moment. Yep. And we'll feed that onto there via a high value resistor. Mhm. How high? How high? Really high. Hundreds of megs. Um quite often gigohms.

**Dave Jones:** Gigohms? Yep. Reason being the capacitance between that flappy electrode and that one there is of the order well for a for a little electret microphone and obviously this is not an electret microphone because we're externally polarizing it.

**Dave Jones:** It might be about five puff. Right. Maybe seven puff, maybe four puff, that order of magnitude. For a larger studio microphone it might be between 50 puff and 100 puff.

**Dave Jones:** Mhm. Low capacitances. Yep. And we need a high resistance here for reasons to be explained in a second. All right. What we've done here is let Let's say that's about 100 volts.

**Dave Jones:** In a measurement microphone such as a Brüel & Kjær microphone Yep. uh which is externally polarized, they would typically use a 200 volt polarizing voltage. The uh studio condenser capsule which we had a little look at.

**Dave Jones:** Uh you might polarize it with somewhere around about the 60 V maybe even 90 V mark. Okay. The amount of charge varies, but the whole point is we've got a capacitor here that we've put charge onto.

**Dave Jones:** Yep. It'll charge up over a period of some seconds because we've got gigohms there and a few picofarads there. So, it'll charge up. of seconds after power on? Yeah.

**Dave Jones:** Uh so, somebody out there can calculate the time constant between Well, no, bugger it. Let's do it here. Uh let's say we've got 10 of the 9 ohms there.

**Dave Jones:** Yep. And let's say we've got 50 * 10 ^ -12 F there. Okay, that comes to about 50 * 10 ^ -3 seconds, I think. Oh, yeah. Sounds about right.

**Dave Jones:** Reasonable. So, 50 ms time constant. Mhm. Uh incidentally, that's an un That that that would be an unrealistically low value, but it's some that all the microphone manufacturers use.

**Dave Jones:** So, we've got a 50 ms charge time constant there. Mhm. Uh which incidentally will wind up corresponding to an electrical roll-off pole there of 20 Hz about 6 Hz.

**Dave Jones:** Okay. That's 50 ms time constant. Yep. Uh 1 over 50 ms is 20 Hz. Mhm. And uh well, actually, the with a 20 with a 20 Hz time constant the actual -3 dB frequency would be two two pi lower than that, which is about 3 Hz.

**Dave Jones:** Got it. Yeah, fairly typical. Anyway, charges up. We've got a charge there. What happens when we come along with a pressure wave onto that diaphragm? It decreases the distance between the plates, increases the capacitance.

**Dave Jones:** Yep. Now, the thing is charge on that capacitor has to be preserved. There's no way for the charge to go in a hurry. So, charge is preserved. If we've increased the capacitance, Mhm.

**Dave Jones:** the voltage has to fall to keep the same energy. And indeed, that's exactly what happens. If we get a pressure wave coming there, the voltage will go negative Mhm.

**Dave Jones:** if we have a rarefaction, the voltage will increase above the bias level. Yep. And those are the voltages that we're interested in gathering and amplifying as those AC voltages.

**Dave Jones:** They they respond to they they correspond to audio. Yep. The other thing to keep in mind is a positive pressure wave here results in a decrease, a negative going voltage.

**Dave Jones:** Mhm. Something to keep in mind. Okay. Uh you can reverse that incidentally by putting a negative polarizing voltage there. Yep. In which case, if we have a negative polarizing voltage on the capsule, then a positive pressure wave will indeed respond to a positive going change in the output voltage.

**Dave Jones:** Yes. So, that's one way of getting the polarity the right way around if you really want to. Any other practical difference to the polarity? Mhm. No. No, none. None whatsoever.

**Dave Jones:** And uh the other interesting thing is it doesn't matter whether you connect it as shown or Right. Let's put that over onto there and ground that. Still the same thing.

**Dave Jones:** Mhm. The signal on there because the capacitance is reducing will follow exactly that path. Yep. Okay, a positive going pressure wave results in a decrease in voltage. Negative pressure, increase.

**Dave Jones:** Got it. So, it doesn't matter What about noise on our What about noise on our bias voltage? Oh, we'll get into noise. Oh, we'll get into noise. Hey, actually the fascinating thing is high frequency noise Uh-huh.

**Dave Jones:** coming out of here Yeah, yeah. is low-pass filtered. Got it. Yes. Yes. With a uh the the response of that low-pass filter is, of course, flat to 3 hertz and we've got a 3 hertz corner frequency.

**Dave Jones:** So, it's a 3 hertz corner 20 hertz divided by 2 pi. Nice. I like it. So, we do in fact get a a noise reduction technique there. Having said that, any sane designer of polarizing supplies for these microphones would make bloody sure that it was as noise-free as they could get.

**Dave Jones:** Absolutely. So, Okay, that's the basics of how you run an externally polarized microphone. Yes. And the difference with an electric microphone, just to cover it again, is that you don't apply an external charge.

**Dave Jones:** The charge is embedded in the material. Either on Yep. the wobbly bit or on the fixed electrode. It doesn't matter. Usually in a bit of Teflon or something like that cuz they hold charge really well.

**Dave Jones:** Yes. Same principles apply though. A incoming positive pressure wave increases the capacitance and causes a decrease in voltage. Excellent. All right. What do we do with them? Well, as we saw, we need to load these with a really, really high impedance buffer.

**Dave Jones:** Uh-huh. If you don't have a hugely high impedance, uh you're not going to get much out of them. And where do you get a high impedance from? Well, you can either use Actually, there's there's two classes of components you can use.

**Dave Jones:** You can either use JFETs Yep. or JFETs with pilot lights. Right. JFETs as in tubes. Tubes. Tubes. Tubes. Yanks. All right. Incidentally, if we get old school about this Let's look at an externally polarized capsule studio microphone type stuff.

**Dave Jones:** Okay, so we're looking at one of those without the electric material. Okay. do do do do We're feeding that beastie from a polarizing supply and a really, really high im- impedance resistor.

**Dave Jones:** Probably about 1 gig. Yep. And that's going to be grounded. Okay, that's where our audio's occurring, but we need to Why does it non sequitur? Why does it have to be such high voltage?

**Dave Jones:** Uh if it uh the the amount of charge Mhm. there determines the sensitivity of the microphone. Got it. But you can't make it arbitrarily high and arbitrarily No, in- indeed, you get some problems.

**Dave Jones:** All right. The higher you make that voltage Mhm. a couple of things happen. First of all because that's positive and that's negative, they attract. So Yeah. Yeah. You'll get that diaphragm trying to bow in.

**Dave Jones:** Pop. Yeah. Well, actually, you get two different phenomena. All right. Phenomenon number one is that gets so close to that that it decides to arc over. Yep. Now, let's face it.

**Dave Jones:** When when it arcs over, you get a massive transient there. Whack in the say in whatever system you're listening to. Not not pretty. And then all of a sudden, of course, once that's discharged, it kind of springs back to where it was before and just sucks in and whack and oscillate.

**Dave Jones:** Yeah, yeah, yeah. Re- relaxation oscillator. Yeah. Brilliant. The In- Incidentally, that's about the nastiest thing that can happen. A much more benign scenario is when that gets attracted so far it gets so close, and you've still got that same voltage there.

**Dave Jones:** That it actually just decides to just go stick, and pretty much right across the surface of that diaphragm Yep. it sticks. And it won't unstick until you remove the polarizing voltage by turning off the microphone.

**Dave Jones:** All right. And of course, when it sticks, it can't vibrate. So, the microphone just goes deaf. Yep. So, it doesn't Does it physically damage them, though? Uh generally Generally, no.

**Dave Jones:** No, really? The reason be grossly exaggerated the ratio of that diameter to that distance. Got it. We're looking at typical diaphragm to plate distances of maybe 10 microns, something 10 micrometers.

**Dave Jones:** All right. So, it's really close. That deformation uh doesn't hurt that much. Got it. Or it shouldn't. Okay. Uh so, that's a couple of the perils. However, prior to that occurring, you can go for your life and you can turn up the bias voltage.

**Dave Jones:** Mhm. Because the the How do you put it? The sensitivity of the system in pressure to voltage is linearly dependent on that bias voltage. Yep. So, turn it up until it sparks or cracks.

**Dave Jones:** Right. There you go. Interesting. Actually, turn it up until it sparks or cracks at the highest SPL you're going to be using it at. Yes. Because that will end to some movement.

**Dave Jones:** So, is that typically an adjustable Um voltage that you could tweak in your system? Uh Or you generally wouldn't touch it? You would generally not touch it. Uh Yeah.

**Dave Jones:** If you were clever enough to dive into a microphone and start mucking about with the bias voltage, yes, you could tweak it. It's uh generally not that adjustable though because Uh Well, back in the good old days, that voltage there was simply derived from the same power supply that was used to drive your tubes.

**Dave Jones:** Got it. And decreasing it would be easy. Just use a pot. Increasing it, well, you'd have to have the voltage there to increase it in the first place. Yeah.

**Dave Jones:** Uh In later times, uh various designs involving uh oscillators and step-up transformers were involved. Uh the method that I tended to use when I was at Rode Microphones was a CMOS oscillator.

**Dave Jones:** Really, really dumb uh Yeah. CMOS oscillator, you know, usual usual resistor resistor capacitor type arrangement. Yep. Just so that you got a fairly well-determined frequency of oscillation. Whack that through another couple of stages of that.

**Dave Jones:** And then feed that into a modified variant of a uh voltage multiplier. Yes. And the thing is, you can actually go two-phase on there if you You can. You can be sneaky about it.

**Dave Jones:** Yeah, because we've got alternate phases on that output and that that output. Something might have there. Keep on going. And I'd typically use uh a number of stages of multiplication there to step, say, 12 or 15 DC supply to these 4000 series CMOS.

**Dave Jones:** Mhm. Up to 60 volts, 90 volts, whatever. And how would you clean that up? Oh, by the time you come out here It's remember, what's what's the actual current consumption out of there?

**Dave Jones:** It's zero. It's zero, of course. So, in principle, it requires absolutely no clean up at all. But, uh, let's face it. Uh, 1 meg of resistance and a couple of nanofarad capacitance And bingo, Bob's your uncle.

**Dave Jones:** all that's required. Yep. So, Nice. it's intrinsic In fact, the only real source of noise over there would be any uh, relatively low frequency variation to the DC supply there because that will cause that to wander and that represents a noise source.

**Dave Jones:** or it might be temperature dependent or something like that. Uh, we zeners. Bloody zeners. Quite often this will be a zener derived Yeah. supply. Right. Okay, from a higher voltage.

**Dave Jones:** You crude bastard. Yeah, absolutely. Well, you you you wouldn't chuck a regulator in there because actually regulators are probably going to be noisier than a wood zener. Cool. And the issue here is if you've got a zener with a soft knee, it's actually going to be quieter than a hard knee one.

**Dave Jones:** And, uh, by knee, I'm talking about if we're talking about, uh, I can't remember let's call that uh, current versus voltage. Uh, a soft knee zener would look a bit like that.

**Dave Jones:** Mhm. So, that's your regulated voltage there. Yep. A hard knee zener would be much more likely to be like that. Mhm. The hard knee low impedance ones seem to be way noisier than the soft knee ones.

**Dave Jones:** Well, that's what we found at the time. Right. After we got some, uh, hard knee zeners inadvertently, put them in and discover that they are noisy, noisy, noisy brute.

**Dave Jones:** There you go. They didn't make them in a production, did they? Uh actually, they made it in we did about 100 and then kind of realized, "Hang on, these aren't passing muster on noise."

**Dave Jones:** Because we were testing for noise. "What the hell's going on? Why are these different to the last ones?" And got it down to the zeners. So, still because the hard knee zeners have a lower impedance Mhm.

**Dave Jones:** than lower impedance than the soft knee ones, it doesn't matter how much capacitance you put across them, you you're not going to really going to shut them up because you've got a low impedance Exactly.

**Dave Jones:** and that capacitor and it just doesn't clean up. Yeah. The soft knee ones clean up beautifully. Mhm. Meh, go figure. go. Eh, so that was simply a a lesson learned along the way in low noise electronics.

**Dave Jones:** Uh if you're going to zener regulate pick something that's got a fairly soft knee. And the other thing is if you're going to filter your zener don't filter it there.

**Dave Jones:** Yes. Duh. That's a low impedance point. Add some impedance and decouple it over here where you can actually form an RC Absolutely. low pass filter that de-noise it. Yeah.

**Dave Jones:** Cuz that CMOS uh CMOS oscillator is going to take bugger all anyway. Yeah, that's right. So Yeah. So, you can use kiloohms there. know. You can use a couple of K.

**Dave Jones:** It just sits there and boogies. Excellent. Yeah. So, that was a typical circuit inside a road production? Yeah. Yeah. And still used to this day, to the best of my knowledge.

**Dave Jones:** Right. When I first came there though, they were not based on this kind of CMOS oscillator. They were a transistor oscillator with three discrete inductors hung around it and basically relied on getting a 12 or 15 V supply and look, I actually can't remember the circuit topology for this oscillator, but it was a real nasty thing and not at all deterministic.

**Dave Jones:** There you go. And it required on the particular transistor having a fairly specific gain and VCE and So there are Production is going to be all over the shop.

**Dave Jones:** Well, and what varies as a result? Mhm. The sensitivity of the microphone. Ah. It's the one thing you don't want to vary. It's the sensitivity of the mic. Ay ay ay.

**Dave Jones:** Oh, boy. Alrighty, so we're back to this microphone circuit where we've created some audio superimposed on DC there. Right. What are we going to do with that? Of course, we're going to capacitor couple it out to our amplifier.

**Dave Jones:** Mhm. Which also needs to have its bias conditions set by a resistor going to whatever bias voltage we want. Yep. That might be ground. Might be a few volts.

**Dave Jones:** It depends. Whatever, depends on what supply you got in your amp and whatnot. Yeah. Yeah. Things to remember, that capacitor has to be yeah, way larger than that capacitance there.

**Dave Jones:** Mhm. Talking a couple hundred nano or something. A few nano A few nano. given that that's say around about 50 puff. Puff. Yep. A nanofarad would be just fine.

**Dave Jones:** And typically 1 to 10 nanofarads is what you'd see there. Yep. What value does that need to be? Well, It's at least the same order of magnitude as that because as far as audio there is concerned, that thing and that thing appear in parallel.

**Dave Jones:** They do. And back in the good old days of valve microphones and not a lot of knowledge, uh typical resistances there might have only been about 100 megohms. Yep.

**Dave Jones:** Okay, that order of magnitude. The amplifier here might have been uh a tube? Yep. And that would go to supply output transformer. And that goes off to the rest of the system.

**Dave Jones:** And in fact, the very first microphone that I designed at Rode Microphones was a tube microphone. It actually had a had a tube in there. Yeah. J- JFET with a pilot light.

**Dave Jones:** Yeah. Right. Yeah. Stuck in the end of the Yeah. Incidentally, there there are real advantages in in having a valve, a tube, up in the head with the microphone.

**Dave Jones:** Why is that? Why? Because you're providing it with filament power, and it's the filament power that makes that thing warm. Yep. And it's that warmth that keeps the whole thing dehumidified.

**Dave Jones:** Ah. You're dealing with high impedances here, so you really want to keep it dry, not humid. You want to discourage Mhm. side benefit. And indeed, when I think that this might be an anecdote going back to maybe the '60s or '70s when Brüel & Kjær decided to go solid state instead of valve, they discovered that they were having all kinds of problems in their measurement mics with

**Dave Jones:** humidity build-up. So, they because they'd taken out the tube. So, Tube. they actually had to put heater resistors in there. They put a resistor in the heater. Nice. Oh, terrific.

**Dave Jones:** One of the ugly things about this kind of circuit is the fact that the output impedance of valves is really quite high. Mhm. That means that whatever load you put over here, you know, whatever your mixer console or whatever whatever it is that you're using over there, its load impedance will change the gain of the whole thing.

**Dave Jones:** And if you've got a load over here that's non-linear with frequency, for example, if it's you know heavily capacitive or something like that, your frequency response is going to droop because it's being fed by quite a significant impedance.

**Dave Jones:** In this first mic that I designed at Rode, the Classic II, I was heretical. I was a bad, bad boy. First of all, do that, then do that. called it.

**Dave Jones:** Then capacitor couple that into your transformer. And guess what? You get a nice low impedance drive point. cuz it's an emitter follower. And it it doesn't do anything to interfere with the tubeish linearities or non-linearities of that.

**Dave Jones:** It's just a dumb voltage follower. Did you get And tube sound? Oh, yes. Yes. Excellent. Interestingly enough, on this particular microphone, part of the what I reckon everybody called the tube sound was created by the fact that in be instead of being a skinny little runt of a microphone like this, damn thing was about that kind of diameter.

**Dave Jones:** It was hugely meaty. And had this quite large uh mesh covering over the capsule. So, you were you were never up close and personal the capsule even if you were crooner.

**Dave Jones:** Uh you were always kind of at least the the radius of this shell away from it. And it made it sound all spacey and airy. And yeah. And that was just the physical construction of the mic forcing people not to Yeah.

**Dave Jones:** They couldn't get their gobs up to it, so it sounded more better. Brilliant. Incidentally, that follower there also allowed me to put some filter circuitry in there, so we could either get it flat as possible or below pass filtering or a bit more uh sorry, high high pass filtering.

**Dave Jones:** So it's switchable high pass filtering. Yeah. Yeah. But uh yeah, the fact that I had a bit of bipolarity in there was heretical. Yes. Absolutely. Oh, unbelievable. Incidentally, uh transistor just uh I think it was a uh a 2N5401 or one of those 120 V 150 V class transistors Mhm.

**Dave Jones:** because the supply was only about 120 to 150 V. Yep. So we could get away with uh a fairly high gain, fairly low noise transistor there and yeah, it just worked a treat.

**Dave Jones:** Brilliant. Mhm.
