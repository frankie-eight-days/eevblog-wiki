---
video_id: H9QONLaitWU
title: EEVblog #702 - Keysight 3000T Oscilloscope Teardown
url: https://www.youtube.com/watch?v=H9QONLaitWU
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 26, "2": 41, "3": 61, "4": 81, "5": 101, "6": 116, "7": 136, "8": 161, "9": 181, "10": 201, "11": 216, "12": 236, "13": 256, "14": 276, "15": 291, "16": 306, "17": 326, "18": 341, "19": 366, "20": 386, "21": 406, "22": 421, "23": 446, "24": 461, "25": 476, "26": 496, "27": 516, "28": 536, "29": 551, "30": 566, "31": 586, "32": 606, "33": 621, "34": 641, "35": 656}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. A lot of people wanted to see inside the new 3000T Agilent X-Series oscilloscope. Well, let's take a look. We'll compare it with the original 3000X series. I don't... 3000A X-Series, that'll be confusing. I don't expect a huge difference, if any difference at all, because it's still the same Megazoom 4 ASIC.

**Dave Jones:** It's still... I don't know. Have they upgraded the processor? Eh, or anything else? I doubt it. And my 3000A, by the way, is one of the first models released. So whether or not they've actually incrementally improved the hardware in the four years since my one was manufactured, I don't know.

**Dave Jones:** So the differences may not be... may have been incremental in those series. Anyway, let's have a look inside. You know what we say here on the EEVblog, don't turn it on, take it apart. And we've just got four screws on the back here, including a secret squirrel one

**Dave Jones:** inside the probe compartment there. And if we... that should be enough to... oh, no, oh! Gotta release the module. That should be enough to... ta-da! Pop the hood! And we should see exactly the same awesome build quality that we saw in the original 3000 series.

**Dave Jones:** And it's all shielded, of course. Very nice. Oops. Not sure what that is. Part of the plastic case is sort of broken off on the inside around that screw hole. Hmm. Someone tightened that screw up too tight and fractured the plastic or something?

**Dave Jones:** And we can try and play spot the difference. Exactly the same YSTech fan we had before. I don't think they're a huge brand name, but look at the rubber-compliant mount they've got on there. Exactly the same as the previous one, of course, but that's just to reduce the vibration.

**Dave Jones:** Very, very nice. Absolutely identical so far. And yes, that is my blood. There we go. This metal chassis is really quite sharp. This part of it anyway, this cover that goes over the power supply, this is not the first time I've done this.

**Dave Jones:** D'oh! And we've got exactly the same high-quality power supply from Lineage Power. Very nicely designed. Can't fold it at all. Beautiful riveting down in there on the insulated earth connector. Exactly the same as before. No difference. In fact, ta-da! Spot the difference. I don't think you can.

**Dave Jones:** Hmm. In fact, four years apart, both of them are still Rev-A. Same model number. And here we go, we've taken the front panel off. And that just came off with plastic clips on the side. So exactly as before. And ta-da! We're in like Flynn.

**Dave Jones:** Bob's your uncle, no worries. Well, there you have it. That's going to be a very quick teardown. In fact, that's probably the end of it almost, because it's identical to the 3000A. Eh, that's what I thought, and I wasn't surprised at all. Exactly the same.

**Dave Jones:** The only change is the addition of the touch screen shielded touch screen module. You can see that it's a bit of an afterthought just tacked on there. They've got an extra chip over here, and an extra connector with the cable going over there.

**Dave Jones:** But apart from that, it's exactly the same. And if you don't believe me, let's play spot the difference. Here we go. Can you? No, not really. Exactly the same. Well looky what we have here. Keysight couldn't even be bothered designing their own board

**Dave Jones:** they've just used. And off the shelf, by the looks of it, E-T-I what's that, an E-Galax? E-M-P-I-A Technology Inc touch screen, capacitive touch screen driver board. So yeah, they just went, oh, marketing have just gone, oh, we need something to compete. Come on, let's, you know

**Dave Jones:** the MD03000's out, let's do something, let's add FFT, let's add our zone trigger down from the 4000 series, and let's add touch as well, yay, she'll be right. We'll just whack that in. It's a bit disappointing. But ultimately, that's you know, practical engineering for you, you just tack things on like that, get the

**Dave Jones:** product to market, and, well, they did have to redesign the board a little bit I mean, they have tacked on this little puppy over here, they have relayed out the board, they've added that, they've added the connector, but that's basically the only difference I can see, really.

**Dave Jones:** I mean, I'll post the high-res photos down below in the links so that you can have a look at it yourself, but it's identical apart from that I believe, anyway, from my cursory glance. And check it out, if you take out all that

**Dave Jones:** metalwork, all they've done is actually reuse an existing mounting hole in the chassis putting on a longer screw, and screw it in, it's rather clever, well, it's a rather nicely executed retrofit, actually, to an existing design, and they've changed the silkscreen there, if you'll notice the other one, it doesn't say no screws, so it says

**Dave Jones:** no screw there, so when they're actually assembling it, you can see this one has the targets on them there, saying insert a screw, so, whereas the 3000A before, yeah, it had the same target in there, plus the screws, so, we haven't been screwed.

**Dave Jones:** But wait, hold on to your hats, I found a difference! Look, this is the 3000A, the original, this is the 3000T, they've changed the Spartan Xilinx Spartan FPGA here, it was a 3S1200 on the 3000A, it's now a 3S1600, so, bigger, it's the same series chip, just bigger, got more

**Dave Jones:** gates in it, whether or not they're doing, they did that because they want extra functionality, like that FFT stuff, perhaps that they're doing, that might be happening in there I'm guessing, because all the zone triggering stuff perhaps, or both but I think the MegaZoom ASIC 4 might be implementing the zone triggering

**Dave Jones:** over there, I can't remember offhand, but yeah, they have increased that just the capacity of that thing a reasonable amount. But apart from that, we've still got the same Spear 600 processor here, one of these applications processors, still exactly the same, that's an ST-ARM processor.

**Dave Jones:** And here I believe is the main 10MHz crystal oscillator in the old 3000A now this was, I think, 25ppm or something, they have drastically increased that by more than the order of magnitude in the new one, it's 1.6ppm, if memory serves me correctly, so let's go on over to the new one.

**Dave Jones:** And there you go, it has changed, they've actually put that, looks like they've put it on, or they've ordered it in a little ceramic hybrid type daughterboard, and they've sold it into the existing footprint, so maybe that was a late design afterthought perhaps from marketing, they said, oh what other

**Dave Jones:** differentiator can we do, oh can we whack in a better crystal, and they're going, oh no, we can't really get one in the same footprint, maybe it wasn't affordable, maybe they got a bargain on these ones, who knows? But yeah, that's the 1.6ppm main crystal and it's changed, and yeah

**Dave Jones:** squeezed into the existing footprint with a ceramic hybrid. Interesting. There you go, there's a better look at the puppy, and yeah, I don't recognize it offhand, but if anyone wants to decode that, go for it. Now I can't show you the 1 gig

**Dave Jones:** and unfortunately, because these shielding cans are soldered directly into the board, so yeah, it's a huge effort to get those out, probably damage the unit or the high likelihood but interesting thing to note, trust me, it is different to the 500MHz one I've got in the 3000A, but it'll be identical to the 1 gig version of the 3000A

**Dave Jones:** which is a different one again. They've got a metal can relay there whereas in the 500MHz one, it looks like they've got two plastic ones down in there, so yeah, that'd be a high frequency RF relay down in there, I'd be guessing. But they have certainly given the board

**Dave Jones:** an entirely different part number, this is the new one here, here it is, 75037 and the old 3000A is 75019 so that was actually up to REV5 by the time I got mine, which was one of the first release units. And likewise with this one, already up to REV4

**Dave Jones:** even though it's just released. And of course, they've changed their name from Agilent to Keysight Oh, goodness. So everything else is exactly the same except for the inclusion of the capacitive touchscreen, which you can see there with the cables going over to that module on the back.

**Dave Jones:** Apart from that, it's basically identical. And the front rotary encoder board here, it's almost identical, yes they have upgraded, they may have added a few extra buttons on there, I'm not going to bother to take all the knobs and everything off to see if there's any spare buttons.

**Dave Jones:** Eh, couldn't be bothered. I really do like the modular nature of the 3000 design, and I've said it before, the front panel just clips off like that, complete with all the knobs and everything else intact all the buttons, the membrane, keypad, and there's just a couple of

**Dave Jones:** cable looms and things like the flat flex here going to the LCD, just holding it together. Well, actually connecting the different modules together so it's really well designed from a systems engineering point of view. Always has been impressive. So I think this teardown's just been a tad over 10 minutes, very quick indeed.

**Dave Jones:** So thanks for Keysight for sending this in, the 3000T, we've done a review if you haven't seen the review, that'll be linked in here as well, check it out. And this teardown is exactly the same, no real surprises in there, just upgraded one FPGA by the looks of it.

**Dave Jones:** So the MegaZoom 4 A6 here, they're of course going to be exactly the same, the ADC A6 in here, going to be exactly the same you've got one ADC sharing two channels exactly like you did before. Everything's exactly the same, the same spear arm processor up here, but yeah, just a little bit

**Dave Jones:** more grunt for maybe the zone triggering and the FFT functions and whatever else maybe they've got in store in the future, who knows? Anyway, if you liked that video, please give it a big thumbs up, because I did draw some blood out of that one.

**Dave Jones:** And if you want to discuss it, EEVblog forum link is down below, and also the high-res teardown photos as always are linked in down below as well. Hope you enjoyed it. Catch you next time. Bye for now. Woohoo! Winner!
