---
video_id: UhG83WS51q8
title: EEVblog #611 - Electret Microphone Design
url: https://www.youtube.com/watch?v=UhG83WS51q8
source: youtube-asr
---

**Dave Jones:** Okay, we're up as far as describing a a typical old style valve microphone. Yep. With uh modern edition in the clay case of the classic two. Let's go back to basic electric mics. Yep. As found everywhere, which don't have

**Dave Jones:** bias, which don't have tube amplifiers. They do actually have buffers, but they don't have output transformers. Nope. None of that rubbish. Yep. And in fact, I'll So, these are our little 10 cent mics that we find in uh

**Dave Jones:** Yeah. everything. So, we'll uh do Uh now, the the solid back electrode might be a ground, or it might be the actual uh hot electrode, if you like. Right. The diaphragm might be at ground, or it might be the hot. We don't know.

**Dave Jones:** The electret to polarize the electret mic mic might be on the diaphragm, or it might be on the back plate. Doesn't particularly matter. We'll just draw it that way for convenience. And what we've got there is a thing

**Dave Jones:** where when we talk at it, we get volts out of it. Yep. But as transducers go What type of level we talking? Uh Let me think. Typically, they're around about minus, let's call it minus 45 dBV per Pascal.

**Dave Jones:** Which translates to, let me see, minus 40 is 10 millivolts, so minus 45 is probably about, oh, I don't know, 4 millivolts or something like that. So, maybe 4 millivolts. Get it right, lad. 4 mV at 94 dB

**Dave Jones:** SPL. Right. that could be minus 35, could be minus 50. Got it. Okay, so if it was say minus 40, that would be 10 mV at 94 dB. 94 dB corresponding to 1 Pascal. Incidentally, that's the usual format

**Dave Jones:** for mic manufacturers to specify sensitivities. So, you have to do the translation of that to there, and that to there. Yep. Me. Okay.

**Dave Jones:** What can you do with a transducer that's putting out, well, 10 mi- 10 mV with a source capacitance of maybe about 5 pF? Huh. Well, let's kick off by sticking it in with a JFET because that's what everybody does.

**Dave Jones:** That's what they do. So, Stick them right in the back there. Yep. So, JFET. And that's pretty much all. That's just about it. Yeah. Now, in the good old days, we'd actually see a discrete bias resistor there to hold the gate

**Dave Jones:** near zero. Yep. That would be a gigohmish resistor. Right. There are, well, how do you put it? Two different basic electrical styles of electret mic. In one of the styles, that that and that are all brought out as separate

**Dave Jones:** electrodes. Yep. The idea being that you can put a voltage on there, hang a load resistor off there, Mhm. and there's your AC voltage with some DC superimposed coming off there. Sure. Rarely done, even though generally that particular

**Dave Jones:** topology offers better linearity and higher SPL handling and all of that kind of stuff. Usually not what happens. Usually what you get is Are they using electret mics in any pro applications? Yes. Yes. Whereabouts? Uh there are a few stage microphones

**Dave Jones:** which are uh back electret types. Mhm. Uh even companies like Sennheiser and AKG are offering uh stage and recording microphones which are electret. Yeah. Uh To what advantage? Um The I think the main advantage is they're cheaper to manufacture.

**Dave Jones:** There's less electronics in there to go wrong. Yep. You know, the bias circuitry, etc. Uh and you can use them over a wider range of uh uh incoming DC supply voltages. Got it. Uh one of one of the areas where you'll

**Dave Jones:** see lots of electrets used in preference to uh externally polarized is whenever you see a skinny gooseneck with a little head on it as used in uh courtrooms, Right. uh panels, uh parliament, that kind of thing. They're all going to be electret.

**Dave Jones:** Yep. And the usual players such as Shure and Sennheiser and AKG, they're all going to be manufacturing that style of thing. Right. Most of these look like that. Yep. That beastie there, JFET, uh becomes a voltage to current

**Dave Jones:** transducer. So, it's a transconductance device. Yep. So, all of a sudden now, what you're seeing here is uh not a given number of uh volts per pressure. It's um current modulation per pressure. That only gets turned back into a

**Dave Jones:** voltage once you add a load resistor. Then work with that. Correct. And then you always see a couple of that. Yeah. Yeah. And In fact, for some reason, one of the standards is to when they're specifying the sensitivity of these mics,

**Dave Jones:** uh their standard is to use a 2K resistor. noticed that. Mhm. Uh simply because it forms a common base for everybody. Yeah. With a 5-V supply. Yeah. And it just gives everybody a a common a common basis, a common platform from

**Dave Jones:** which to work. Although you can operate them much lower. Supply voltage. Yeah. Now, let's have a look at this. 1.5 V. Yeah. With caveat, with caveat. I've got one right here in my pocket. Runs off a single single coin cell.

**Dave Jones:** Mhm. That's it. Oh, mind you, one 1.5 or 3.something V. No, 1.5. Okay. 1.5 V. There you go. Much depends on the characteristics of the FET. Yeah. Let's have a look at the current versus current versus voltage characteristics of a JFET. Measured

**Dave Jones:** voltage there, Mhm. current through there, zero bias on the gate. Right. Uh most of them will have a characteristic that looks like that. Once you get above a certain voltage, about there, that thing produces a constant current source.

**Dave Jones:** Right. And it's in this region here that you want to operate the FET. Yeah. Why? Because as soon as you start coming down into this part of their characteristics, the gain, the transconductance of that just goes to party.

**Dave Jones:** to shop. Now, went through a stage of measuring rather a lot of different electret mics. That gain reduction point uh varied from FET to FET. From FET type to FET type. Uh Most of them were good down to around about 1.1 or

**Dave Jones:** 1.2 V and would then plummet. There were some better FETs that would come down to maybe 0.8 V before they started rolling off in gain. run those off a single alkaline cell until they're dead? Yes. Practically. So for example,

**Dave Jones:** let's take a typical JFET that might have a constant current region where it draws about 350 microamps. And that's a very, very, very typical figure It is. for the JFETs used in electric mics. Let's say up here we've got a

**Dave Jones:** single cell at 1.5 V volts. And let's say that that particular FET would maintain its gain down to say 1 V. Just make the numbers easy. Yep. Okay? What value of resistance can we reasonably put there in order to get those conditions?

**Dave Jones:** Well, we've got half a volt across it. We've got 350 microamps through it. Uh R equals 0.5 V over 0.35 milliamp. And at a rough guess, that's probably going to be about 1.4 K. So something like that? So you might actually toss in a 1 K

**Dave Jones:** resistor. Which means that that battery can be depleted to 1 V plus 0.35 V volts Yep. before it starts losing gain. Got it. Or you'd pick a FET that instead of having a knee point at 1 V went down to

**Dave Jones:** say 0.8 V volts and maybe drew less current. Mhm. Now, you can make that resistor smaller. Mhm. That will allow you to flatten the battery further before you get gain roll off. Yep. Penalty, the lower the resistor there,

**Dave Jones:** the lower the signal gain to that point there. Of course. So, it's all a compromise. And of course, if you've got a few more volts available, beauty. You don't have any problems anymore. Absolutely. But, any I guess anybody who's using an

**Dave Jones:** electret mic in a new piece of equipment needs to know what voltage they've got available so they can plan what resistor they use. Yep. So, for example, if you've got a piece of kit with a 5-V supply, okay, let's just do this again, but this

**Dave Jones:** time with a 5-V supply. Tons of headroom. You've got a ton of headroom with caveats. You might want to maximize the gain out of that circuit there so you don't have to have as much processing or so that you can maximize

**Dave Jones:** the dynamic range of your ADC that follows. So, you might think, "Okay, let's make that resistor as big as we possibly can." Okay, 5 V 1 V, we've got 4 V across there. 4 V / 0.35 is probably about

**Dave Jones:** 12 K. Vaguely speaking. Okay, beauty. So, you go to print with that circuit. Yep. All of a sudden, you come along with, you know, most of your microphones are sitting there at 350 microamps. You come along and you've got a fitting there

**Dave Jones:** that draws 400 microamps. Guess what? That's trying to suck 4.8 V across that. Okay, 400 * 12 4.8 V. Insufficient voltage there, so instead of getting all of that lovely gain, it goes Yeah, bonk. Oh, okay, I'll cover my ass instead of

**Dave Jones:** putting in 12 K, I'll put in 1 K. Well, you can do that. Yeah. And it'll cover all of those. Yeah. But you've robbed yourself of so much gain. Yeah. So, maybe pick a resistor that allows the typical voltage there to

**Dave Jones:** sit at about half of your rail. This almost goes back to good old bias theory where you can try and bias things at half rail. Half rail. That's it. Not only will it give you the best dynamic range as far as signal excursion

**Dave Jones:** goes. Duh. Yeah. But it also allows for production variations in that fit current. And you want the flattest battery chemical chemistry possible as well. Now, the voltage rating of those fits is generally about 10 volts. Mhm. So, if you were using a say 12-V or 15-V

**Dave Jones:** supply, Mhm. you might want to either regulate it down a bit or resistively drop it down a bit. Yeah. Or do something to ensure that the voltage there stays below around about that 10-V level. Mhm. Cuz otherwise they can start avalanching

**Dave Jones:** or getting noisy or undesirable effects. And this is how uh this is like the phantom voltage applied on like a PC microphone input. Yes. like that. They will they will have that voltage superimposed on there and you're supposed to hook up

**Dave Jones:** and just the Yeah. two wire Not only that, they have the voltage which is usually around about 3 and 1/2 to 5 volts and they have the resistor built in. Yes. Okay. So, they've done that bit inside the box.

**Dave Jones:** Inside the PC. They only want you to plug that much in. Yeah. Now, there's yet another caveat that you have to be aware of. Okay. How which is noise on this rail here. Yeah. If this thing if if this JFET is within

**Dave Jones:** that working within that constant current region, it's presenting a very high impedance there. Mhm. Which means that any noise there gets presented immediately to Absolutely. So, anybody who's using these from anything that might have a bit of noise

**Dave Jones:** there, like a PC. No, they're quiet. Uh make sure you decouple the hell out of it. Yep. That's why PC mic inputs are so crap. They really are. They're pretty god awful. Yeah, and sometimes it seemed to be cuz

**Dave Jones:** that ground is not at a quiet place. Absolutely. Yeah. Yeah. Okay, so that's care and feeding electrically of um electric mics. Electret mics. It's It It's easy. Yep. Get the manufacturer's spec on the mic to find out roughly what the quiescent

**Dave Jones:** current is going to be. Mhm. Plan your resistor around that and your supply rail. Too easy. Yeah. Bob's your uncle. Not rocket science. No, not at all. Too easy. It's not unusual these days to see electric mics that don't have that

**Dave Jones:** resistor at all. Mhm. How do you How do they work without being biased? I'm not quite sure. I I I still haven't tested this myself. I've got a suspicion that they're actually relying on things like PCB leakage, Ew.

**Dave Jones:** which is up in the tens of gigohms, hundreds of gigohms, who cares. It vaguely maintains that somewhere within hailing distance is zero. This is like trying to have an a uh op amp like this and trying to AC

**Dave Jones:** couple into your Yes. the bias? And the the only real sources of bias there A leakage. Well, ac- actually there's a couple of sources. First of all, there's leakage down through the gate there. yep. And that, in fact, is a source of noise

**Dave Jones:** as well as bias corruption. Now, typically, if you've got a little fit with little junctions and low capacitance, you're looking at pico amp Right. leakages. Yeah. Mind you, something to keep in mind about uh JFETs is that leakage current

**Dave Jones:** will increase around about at the rate of about a decade per 10° rise. Oh, okay. So, when temperatures get high, FETs get leaky. Yep. But uh it's not unusual to be talking about pico amps there. So, if you can

**Dave Jones:** arrange for uh tens or hundreds of pico amps leakage to ground there by having soggy circuit board or I don't know what to do. Yeah.

**Dave Jones:** Then you can maintain the DC voltage there somewhere within hailing distance of zero. Yeah. Uh the other thing to watch out for, of course, is that's at zero. We've got signal excursions either side of zero due to that.

**Dave Jones:** The negative going ones see a high impedance. Yeah. Any positive going signal greater than maybe 10, 20, 30 millivolts starts to see a forward diode junction down there, and once I've been non-linearly clipped, Ouch. So, the larger signal,

**Dave Jones:** the worse it clips there. Mhm. So, that we're discussing about headroom is a headroom limitation. Right. Now, the other downside of leakage is it's a noise source. Mhm. Uh I can't remember the the equation off the top of my head for

**Dave Jones:** uh noise current, but basically every dribble of electrons that goes down through that gate unit of measure. Yeah. A dribble's worth. Uh every electron that jumps that barrier Yeah. represents an impulse. It does? And uh the thing is, if you got zillions of

**Dave Jones:** them going at once, they kind of iron out, uh which is why the noise of a DC current is proportional to the square root of the current. Mhm. Double the number of electrons flying through there, and the noise part of all

**Dave Jones:** of that those rushing ball bearings, and it increases by a factor of root two. Right. Uh so, it's a noise source. Mhm. That current gets converted to a noise voltage by the impedance at the gate, which consists of that capacitance,

**Dave Jones:** Mhm. that capacitance, that resistance. Yep. Which will change with frequency. Yeah, it is. But by far and away, generally the most important part of the noise is that resistor or pseudo resistor. Yep. Interesting thing, the higher the value

**Dave Jones:** of that resistor, not the higher the noise, the lower the noise. That is counterintuitive. Counterintuitive. And the reason for that is, okay, let's plot noise voltage versus frequency. Mhm. For a resistor, it's basically flat. Yep. Okay, equal noise voltage per unit frequency.

**Dave Jones:** Yes. Okay, if we double the value of resistance, we increase the noise by root two or 3 dB. Right. Okay, wait, that's 3 dB. Okay, why? Because noise voltage equals root of KTRB. Yep. So, KTR. So, it's the fact that it's proportional

**Dave Jones:** to root resistance. Mhm. Okay, double the resistance, increase by 3 dB only. Okay, but here we've got our resistor in series with its noise voltage source. Okay, and that voltage there increases by 3 dB added to there, but

**Dave Jones:** it's got this low pass filter attached to it. So, that will only be true up to a cutoff frequency, a corner frequency determined by the value of that resistor and the value of the capacitor. So, let's just say this

**Dave Jones:** one, okay, cutoff there. Okay, so its corner frequency is there. When we double the value of resistance, we shift that down to half of what it was. So, all of a sudden our noise profile looks like that. Guess what? 3 dB lower.

**Dave Jones:** So, as long as we are only looking at frequencies significantly above that corner frequency, whenever we double that resistor, we knock 3 dB off the noise because we're in this roll off region. Very nice. And that's part of the secret to making

**Dave Jones:** a low noise mic is make any resistance as high as you possibly can, and make the capsule capacitance as high as you reasonably can. Totally counterintuitive. Who would have thought? Yeah, so high resistances equal lower noise. Lower noise? It's a bombshell, folks.

**Dave Jones:** And that's why Rode Microphones I think I was the first one to go from 100 meg type resistances up to 5 gig type resistances, and it really paid off in making low noise preamps. Awesome. The other thing to watch out for is that

**Dave Jones:** noise current, which as I said, noise current appears across those impedances as a noise voltage. Those impedances, well, guess what? The The impedance looks like a resistor in parallel with a capacitor. The lower you can pull that down,

**Dave Jones:** Yep. the happier everybody is. And the smaller you can make that uh noise current, the happier everybody is as far as keeping the noise down as concerned.
