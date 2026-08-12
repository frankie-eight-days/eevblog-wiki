---
video_id: 2OHMNGi1RUY
title: EEVblog #457 - Oscillator Calibration Followup
url: https://www.youtube.com/watch?v=2OHMNGi1RUY
source: youtube-asr
timestamps: {"0": 1, "1": 18, "2": 36, "3": 54, "4": 71, "5": 87, "6": 101, "7": 113, "8": 127, "9": 140, "10": 155, "11": 174, "12": 187, "13": 200, "14": 211, "15": 226, "16": 241, "17": 260, "18": 274, "19": 287, "20": 299, "21": 311, "22": 335, "23": 352, "24": 369, "25": 383, "26": 399, "27": 417, "28": 431, "29": 445, "30": 458, "31": 469, "32": 485, "33": 501, "34": 515, "35": 531, "36": 548, "37": 564, "38": 577, "39": 598, "40": 613, "41": 631, "42": 647, "43": 663}
---

**Dave Jones:** Hi, just another very quick follow-up video from the previous one. If you haven't seen it, click here and you'll be able to watch that where I adjusted this Agilent frequency counter I've got that's just got its built-in 5 ppm standard. I adjusted the

**Dave Jones:** calibration pot on the back there to match my rubidium oscillator here and I did that with the frequency display on the front. But I just thought I'd show you another method and um someone mentioned you know does you know having one of these non

**Dave Jones:** conductive non metallic adjustment things matter? Well, let's take a look at it. What I've got here is got the scope set up. Channel one here that I'm triggering off that is the 10 megahertz reference output from my rubidium oscillator which is also which

**Dave Jones:** I've also got going into the front of the frequency counter which we'll take a look at in a minute. And then I've got the 10 megahertz output here from the internal 5 ppm you know crappy internal oscillator. That's going into channel

**Dave Jones:** two there and we can see and I'm triggering off a channel one here the rubidium oscillator and you can see that that's not bad at all. This you can see the 10 megahertz output from well the 10 megahertz oscillator

**Dave Jones:** inside the Agilent scope is not quite the same frequency. If they were exactly the same, of course, they would be completely locked. This second waveform would not be moving at all. And of course, we can you know we can trigger

**Dave Jones:** off our channel two if we want and then the other one will move. It doesn't matter. But we're going to trigger off our rubidium reference here and we're going to adjust this waveform and this is another way you can do it. I did it

**Dave Jones:** before using the frequency display on this, but this can actually be a better method. It's more analog uh like even though I'm using a digital scope. You can do it on an analog scope. Works exactly the same. So, watch this. Now,

**Dave Jones:** um I've already adjusted it so it was it's reasonably close. It's a as you can see it's scrolling past it maybe a couple of hertz. And this is actually a way that we can directly see the difference between these. Now, um what

**Dave Jones:** I've got what what I'll do first is I'll use this screwdriver here and I'll put this into the pot and I near the pot in there and I won't actually touch it. So, watch this. Well, look at that. Look at that. It's

**Dave Jones:** going berserk and then I'll just touch the pot inside and it's gone completely haywire. Look at that. But, if I do the same thing with this non conductive non metallic little adjustment pot, I can go near it and it will change a little bit.

**Dave Jones:** Will change a little bit and if I touch it, it's not nearly as bad as the other ones. So, there you go. That is why you use these because what the pot in there is not a resistive pot. It's an

**Dave Jones:** adjustable capacitor. And even with this plastic, it's acting as a dielectric even though you don't touch it and you get very close to it that you're going to have the dielectric of the air, then the dielectric material of

**Dave Jones:** the material and then your hand etc. So, you do actually change it a little bit just by going near it. I'll try and get it more spot-on so you can see that better in a second. And but of course

**Dave Jones:** the metal one that is much much worse. That one just goes crazy. So, when you're adjusting these things, you really do want one of these plastic adjustment pots. Now, let me see if I can trim this pot in.

**Dave Jones:** Oh, there we go. There we go. Yes, I do have my tongue at the right angle. So, that's not bad. Can I get it No, if I move it more in that direction, now it's very touchy. Oh, almost.

**Dave Jones:** Almost had it there. Just out of pure luck. It's uh you're real it is a bit of luck depending on where the sweet spot of the that the plates in that capacitor need to be as to where you can physically put them.

**Dave Jones:** But, that's you know, we're getting there. I have had it so it's very very close. And you know, that's not too bad. And that's maybe about 2 Hz out because if you follow the peaks it maybe it's like 2

**Dave Jones:** Hz. So, what we should see on this frequency counter, if we turn it around and have a look at the frequency, we should actually see that that frequency is about 2 Hz out. There we go. It's 2 Hz under

**Dave Jones:** because it's going in this direction. If it was going in the in that direction, then um it would be 2 Hz over. So, there you go. You can actually you don't have to you don't need a display like this to

**Dave Jones:** actually uh see that. You can just adjust it using a scope like this. So, if we make it go the other direction, oh oh look at that. I've got it almost bang on. It's just the act of touching

**Dave Jones:** it. My body extra capacitance in there is just making it go back in the other direction. So, this is just another technique. I think it's a better technique for adjusting these sorts of oscillators because it's uh you get direct visual feedback.

**Dave Jones:** It's much better than just watching some digital display flip over cuz you really get a feel for it, but uh this is this is It's really tricky now. If I take that off, there we go. We're maybe 1 Hz. See, it's taking 1 Oh, no, 1 Oh,

**Dave Jones:** just under a Hz. So, in the other direction, so it should just be now showing over almost a Hz on the display, and there it is. Spot on. So, that's just another way to adjust these pots. And of course, this thing

**Dave Jones:** will drift with time as well because it's, you know, it's not a very It's not an oven-controlled oscillator. So, when this thing warms up, you might find it will slowly stop and maybe drift back in the other direction like that. Given

**Dave Jones:** enough time. Like maybe if I blow on it, perhaps. No. But, certainly, if I uh bring some extra capacitance near there, what?

**Dave Jones:** You can get this reasonably spot on. I mean, we're talking like a one one one Hz. It's actually 0.1 ppm. So, and that's why on these ones with the stock oscillators, they put the calibration pot on the back because uh

**Dave Jones:** well, cuz the oscillators are so crap that really, you know, before any critical operation, you probably should adjust it against a standard. Really. And well, if you're doing anything serious, you shouldn't have a internal oscillator. If you've got a

**Dave Jones:** reference, then the silly thing there is if you've got a rubidium or a better oscillator to compare it against, well, you should be using that as the external input anyway. But, anyway, there you go. That's just another method to do that. And yes,

**Dave Jones:** these tools do actually make a difference. So, hope you like that. Oh. Almost 8 minutes' worth. So much for my quick video again. All right, here we go. I think it's going to reverse, folks. I think we're going to get it.

**Dave Jones:** We're going to get it reversing. There we go. OH, IT'S SPOT ON. LOOK. It's spot on, and it's going to drift backwards. There you go. That is the oscillator internal It was bang on for a second there. Well, at one point it was

**Dave Jones:** absolutely precisely the same as the rubidium clock. And there we go. It's drifting back. And if I put my thum- even just putting my thumb over that hole, you can see that should I can make that go faster.

**Dave Jones:** Maybe just a little bit. You can kind of sort of see it. So, yeah. Just any capacitive coupling near that thing at all, even half a bee's dick there of capacitance, 1/100th of a path or something, is just enough

**Dave Jones:** to make that sort of drift a little bit. So, yeah. Stock oscillators, hate them. As you can see, there's other oscillator options on this thing. You can get the uh uh uh I'm not sure I I I I assume that the

**Dave Jones:** uh US uh yeah, ultra-stable oven, I guess, is the best one. And there's a high-stability oven, and then there's the I guess I don't know MS medium-stability oven, I guess. But yeah, this doesn't have it. It's just got a regular, you know, SC cut crystal

**Dave Jones:** in there, and ah, whatever. Hopeless. And what do you know? This thing does have 12-digit capability. I thought this model didn't. What I did was go in there and selected the gate and set it permanently to the number of

**Dave Jones:** digits like that instead of a regular gate time. I forced it to a number of digits, and it actually goes up to allows you to go up to 15, actually, but it can't obviously display 15. There we go. Can't obviously display

**Dave Jones:** that many digits. It can only display 12, but maybe internally, I don't know, software-wise, you could read it out perhaps, but certainly does display 12 digits. I hope they're not dummy ones. I assume not. And I've actually done a

**Dave Jones:** video way, way back on this and drift of reference or oscillators crystal oscillators like this against GPS locked rubidium reference and how you can actually track the drift of this both positive and negative over time and then get data out of the thing. So, if you

**Dave Jones:** want to if you haven't seen that, it was many, many years ago and uh you can do that by clicking right here. Tada! The wonders of YouTube hyperlinking. Wow. And yes, okay, if you want to get all funky, you can just

**Dave Jones:** switch your scope into XY mode and do the famous Lissajous pattern here and you can do it way. There we go. Put my finger near it and I prefer the waveform. Like some people prefer um some people prefer this, but I certainly

**Dave Jones:** don't and you want to get a stable circuit. Uh, circle there. And the wobble rate, of course, is the same as the waveform drift rate. And there we go. We're almost bang on. So, you basically want your perfect

**Dave Jones:** Well, you want a stable circuit there and circle there that doesn't uh undulate, but nah, this thing's impossible to adjust, but ultimately, I don't think that's it, you know, it looks funkier, but it's not as useful as the waveform. I like the

**Dave Jones:** waveform. Catch you next time.
