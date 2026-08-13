---
video_id: 579SYLxORyw
title: EEVblog #575 - DIY 1970s Spectrum Analyser
url: https://www.youtube.com/watch?v=579SYLxORyw
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 32, "2": 51, "3": 66, "4": 96, "5": 119, "6": 137, "7": 161, "8": 187, "9": 208, "10": 229, "11": 248, "12": 266, "13": 291, "14": 312, "15": 330, "16": 353, "17": 372, "18": 394, "19": 411, "20": 436, "21": 458, "22": 476, "23": 497, "24": 516, "25": 533, "26": 550, "27": 572, "28": 598, "29": 622, "30": 642, "31": 658, "32": 680, "33": 700, "34": 721, "35": 740, "36": 755, "37": 775, "38": 789}
---

**Dave Jones:** All right, I'm here with Phil and your, what's your call sign? BK2BDF. BK2BDF? Yep. Excellent. And you're going to show us a really neat home-built spectrum analyzer. Spectrum analyzer. Tell us all about it. Very, very long time ago, when the radio club was first building the two-meter repeater,

**Dave Jones:** we were having terrible trouble getting the cavities working. Right. And we had very limited access to RF test equipment. Mm-hmm. I worked in a RF laboratory and had access to a spectrum analyzer. Yep. And I just wish I had one at home. Right.

**Dave Jones:** I decided there was no way I was ever going to be able to afford a Hewlett-Packard spectrum analyzer in those days. Yep. Late 70s, early 80s. So I decided to build one. Excellent. All right. And this is the result. And this is it.

**Dave Jones:** Wow. This device has been used to get the cavities working for the original two-meter repeater for the radio club. Mm-hmm. And several times since for EMC testing of various pieces of commercial equipment. Right. Probably the most recent and valuable was the traffic light controller I've been working on for many years.

**Dave Jones:** Mm-hmm. Had a leakage of 160-meg signal out of the microprocessors. Right. And you were able to track that down using this beast? We took the traffic light controller up to Colo, to the open-air test site. Yep. They failed it. Ha, ha, ha. And they said that signal's got to go down about 10 dBs.

**Dave Jones:** Yep. I brought it home and set up the traffic light controller in my carport, used the spectrum analyzer with a dipole antenna. Mm-hmm. And went through board by board until I found where the problem was. Nice. And fixed it, went back to Colo and got it passed.

**Dave Jones:** All right. Yeah, it's great. All right, so tell us how it's, tell us, explain all the sections in here and tell us how a homebrew spectrum analyzer works. Well, a spectrum analyzer is really just a radio receiver. Mm-hmm. Where the last detector stage is a logarithmic amplifier instead of a linear voice detector.

**Dave Jones:** Mm-hmm. It's very much like an AM receiver. There's no gain controls. It just runs flat out all the time. But the last stage, the detector, which is this last section here. Yep. Is a logarithmic amplifier. Right. That just takes a 10.7 MHz signal and rectifies it like an AM detector.

**Dave Jones:** Mm-hmm. But it's set up so that the output of the detector is logarithmically proportional to the input. Right. So it has, we were working out before, it has about 70 dBs of gain. Mm-hmm. So 60 dBs is 1,000 times in voltage. Yep. Another 10 is another three.

**Dave Jones:** So about 3,000 times in voltage. And that equates to the height of my screen. Mm-hmm. So these signals here, that's about 40 dBs down from the top of the screen. Right. So the noise floor is what, minus 70 or thereabouts, is it? Yeah, about 70.

**Dave Jones:** Yep. I'm not sure where the other signals are from. And what sweep range are we looking at there at the moment? That's the zero mark. Oh, right. OK. Up to 200 megs. 200 megs. 200, about, it tops out at about 200 megs. Yep.

**Dave Jones:** Right. Somewhere here will be the page and transmitters. There's somebody transmitting. Right. Somebody around us. Yeah. Yeah, everyone's got a transmitter around here, like on his belt there. Who's got a handheld? Can you key up your handheld? Handheld. Can you just key up your handheld?

**Dave Jones:** Key it. Can you frequency? Here we go. And? And? Here we go. Oh, there we go. Look at that. Wow. You've got to be kidding. You're allowed on the air with that? Oops. Wow. Thanks, Ben. All right. We might have momentarily overloaded the front end.

**Dave Jones:** Right. Anyway, that was him there. Yep. Yep. So that's 146 megs about there somewhere. Right. That'll be the 147 megs paging transmitters? Mm-hmm. Well, I'm not sure where 88 to 108 is gone. There was a... That's all the FM broadcast transmitters in there.

**Dave Jones:** Oh, it's on narrow. That's why I can't see it. There they are all there. Ah, there they are. They're the FM transmitters. Yep. There are the local FM stations. 88 to 108 megs? Yep. That's them. Spot on. So can you tell us about all the sections,

**Dave Jones:** starting from the antenna input? Oh, the antenna input. Yep. Comes down into the front-end mixer. Yep. Now, the mixer takes the RF signals, mixes it with the voltage-controlled oscillator. Mm-hmm. And that produces a 205 meg IF. Right. This receiver actually converts up rather than converts down like a traditional receiver.

**Dave Jones:** This can only work this way. Right. Right. Okay. Because we're trying to churn everywhere from zero frequency to 200 megs, you've got to take that and convert it up to a... And convert it up. ...to an IF that's higher than the signals you're trying to receive.

**Dave Jones:** Of course. Yep. So the first filter here is somewhere around 205 megs. Right. That comes down into a homemade double-balanced diode mixer. That does look like a double-balanced mixer. You can see the four diodes in there. Yeah, and the little toroids. And the little toroids because that's all that's in a double-balanced mixer.

**Dave Jones:** Yep. So this section here is just a crystal oscillator and multiplier. Yep. And that's mixing that 200 megs down to about 50 megs. Right. The frequencies are not terribly important. They're based on what crystals I had in my junk box at the time.

**Dave Jones:** Okay. The whole thing works that way. Right. So just a filter and then a bandpass filter of, I'll say, 56 megs. Right. And then another crystal oscillator, another double-balanced mixer. Mm-hmm. And that mixes down to 10.7 megs out through... Yeah, through that coax into here.

**Dave Jones:** Mm-hmm. And this is just a 10.7 meg IF amplifier. Right. Ceramic bandpass filter. There it is. Yeah, I can see it. Then it comes through into this section and then it splits two ways with a diode switch. It either goes straight through for wideband, wideband being 250 kilohertz.

**Dave Jones:** Yep. Or it goes across through those crystal filters for narrowband, which is 15 kilohertz. And that's the switch on the front. That's this one here, narrow-wide. Wide and narrowband, yep. Then just into some more amplifiers, which then feeds back into that logarithmic amplifier.

**Dave Jones:** At the end, yep. And that's our final output. The output of the logarithmic amplifier comes out into the crow. Yep. As the vertical input or video input to the crow. The oscillator is actually being swept from this oscilloscope, the horizontal time base. Oh, you're taking the horizontal time base out.

**Dave Jones:** Out. Ah! And it's fed back into this amplifier. Ah, right. Nice. And that drives the voltage-controlled oscillator. I got it. So that it can synchronize with it. The frequency is actually being swept. Swept on the... With the... Very clever. Yep. Very clever. But that's our spectrum analyzer.

**Dave Jones:** Yeah, but to integrate it with a scope like that is neat. Yeah, I could afford to buy the scope, but not a spectrum analyzer. Got it. And these are all hand-wound inductors? Yeah, little hand-wound chokes. Yep. But yeah, the thing's full of hand-wound coils.

**Dave Jones:** Yep. Nice. It's all built on... The base is a piece of little print circuit board. Yep. And then copper... Copper shield. Shielding around. Soldered in on top of it. Yep. And you don't need to shield the tops of them? Ah, well, there's the...

**Dave Jones:** Ah, well, okay, you've got shielded plates. There's the... Okay, yep. The lids. The lids. The lids. Not all the boxes ever got shielded. That was it. Yeah, right, okay. So the performance is still fairly adequate even without the shield? Yeah. We were actually looking at a signal before.

**Dave Jones:** Oh, yeah. There we go. Oh, yeah. That is both that one and that one. That's probably the crystal and that's... Yep, that looks like feeding back. So there's picking up near the crystal? Yep. So that's... Anyway, they look like they're double the frequency to me.

**Dave Jones:** Mm-hmm. So that's the second local oscillator being picked up by the system itself. Got it. But if you disconnect the antenna completely and put the shields on... That's your noise floor, yeah? That's not... No, there's not much left. Yeah. And, you know, that could actually be a signal.

**Dave Jones:** It could be sneaking in, yeah. Yeah, there's a couple down here. Yeah, there's not much there until you put the antenna on. Sure. Very nice. When I connect the spectrum analyzer up to my beam, I'm down at Beacon Hill. Yep. Down in the gully.

**Dave Jones:** I can get the receiver about S9. Mm-hmm. I can put the spectrum analyzer on the beam, key up the repeater, and actually see the repeater come back. Right. It just pops up here as a... Yep. It's only just popping out of the noise.

**Dave Jones:** Got it. That's the sort of sensitivity that the device has. Mm-hmm. It doesn't go down to, yeah, microvolts like a normal ham radio would. I'm not sure what the smaller signal is, but, yeah, 10 or 20 microvolts probably. Yep, something like that. So would you, if you were building a spectrum analyzer,

**Dave Jones:** a discrete spectrum analyzer, would you do it the same now? Or would you use similar styles? Pretty much. Yeah, similar components? When I first looked at it, the voltage-controlled oscillator was always going to be a problem. Right. And I rang up, I won't say who.

**Dave Jones:** Right, okay. The place up at Hornsby that sells all the fancy RF equipment and mini-circuits. Right. And I priced what's called a YIG oscillator, Y-I-G. It's an acronym for something, and I can't remember what it is. A YIG oscillator is a magnetically-tuned sphere oscillator.

**Dave Jones:** Nice. And it's the heart of a real spectrum analyzer. Mm-hmm. And I wanted one that tuned, you know, 2,000 to 3,000 megs. Yep. And it was $2,500. $2,500. This was back when? Long time ago. Late 70s, early 80s. Late 70s, early 80s. Yep.

**Dave Jones:** Nah, there's just no way I was going to spend that much money on a little oscillator in a box. Well, nowadays everyone's doing it with a software-defined radio these days. It's just not the same, is it? Yeah, it's not. It's not the same.

**Dave Jones:** There was some spectrum analyzer kits that came out years after this, where they actually used a TV tuner. I remember that. An electronically-tuned TV tuner, not turret tuners. Yep. But they had enough range that, yeah, you could build a half-reasonable spectrum analyzer out of a TV tuner.

**Dave Jones:** Okay. Would it have a decent noise floor in it? Well, you had to build all the back end of it. Yeah, right. Okay. Yep. So, yeah. But, yeah, $700, you can buy a spectrum analyzer that works better than this today. Yeah, of course.

**Dave Jones:** Of course. Yep. But still, that is very nice. It's a sort of dead bug-style construction, or as the Yanks call it, Manhattan-style construction. And it's just beautiful. Phil, that is awesome. Thank you. Well done. Thank you very much. You're welcome.
