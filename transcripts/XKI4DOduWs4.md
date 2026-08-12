---
video_id: XKI4DOduWs4
title: EEVblog 1560 - TIP: Use Your Arb Gen as a High Resolution DC Voltage Source!
url: https://www.youtube.com/watch?v=XKI4DOduWs4
source: youtube-asr
timestamps: {"0": 0, "1": 19, "2": 33, "3": 47, "4": 60, "5": 72, "6": 88, "7": 103, "8": 120, "9": 135, "10": 146, "11": 162, "12": 177, "13": 192, "14": 204, "15": 217, "16": 229, "17": 244, "18": 259, "19": 273, "20": 286, "21": 296, "22": 308, "23": 323, "24": 333, "25": 349, "26": 365, "27": 380, "28": 391, "29": 407, "30": 420, "31": 433, "32": 447, "33": 459, "34": 473, "35": 487, "36": 499}
---

**Dave Jones:** Hi, just a quick 2 minute tech tip video. Have you ever needed to generate a precisely changing voltage in like small little increment steps? Like ordinarily, okay, you might use your fancy pantsy modern digital power supply like this, but typically that can even

**Dave Jones:** on a like a Ducks Guts unit like this Rohde & Schwarz jobby here, you can only do 10 mV increments. And if you ever had a need for generating much smaller voltage increments like that. And sure, okay, you can put a voltage divider on

**Dave Jones:** the output of it and then get smaller potential voltage changes across it and stuff like that, but often you might be powering using your power supply to power your product. And of course, most labs aren't going to have calibration

**Dave Jones:** kit like this with six decades of voltage adjustment or like a nanovolt voltage source like this. If you don't have any of this and your power supply is being used, well, what can you use? Well, you might already

**Dave Jones:** have something. Any decently equipped lab these days you should have an arbitrary waveform generator. It doesn't have to be as quite advanced as this. You can get them quite cheap, whether it's, you know, it's the Siglent or the

**Dave Jones:** Rigol like this or one of just the cheap eBay jobbies. In most cases, you should actually be able to use your arbitrary function generator to generate precisely small stepped voltages. Let's take a look. Modern arbitrary waveform generators, they don't generate the

**Dave Jones:** signal analog like old school ones did. They generate them using typically a 16-bit digital-to-analog converter. And with that higher resolution analog-to-digital converter, you can actually get really nice steps on this. A lot of people don't know realize that

**Dave Jones:** their arbitrary waveform generator should have a DC option like this. Usually it might be called DC offset or something like that, but they can actually generate a DC voltage on the output which then can be precisely this one. You might think it goes 1 mV, but

**Dave Jones:** we can actually go over and generate 0.1 mV steps. So, that's two orders of magnitude better than the best power supply I've got in my lab here. Now, it's not magic, of course. There's a couple of issues which I'll go through.

**Dave Jones:** The first one is that usually they will have a DC offset. This one's not bad, so you can see it's a 25 microvolts offset if I set it to zero. But, it can be substantially higher than that. This

**Dave Jones:** Rigol over here, for example, set it to 0 V, you switch it on, and you can see that it's got like a 500 microvolt offset or a 0.5 mV offset. So, yeah, you can adjust it by 0.1 mV, but you just got to be aware

**Dave Jones:** you're going to have that offset there, or you might or might not, depending on, you know, how decent your signal generator is. But, the good news is is that you can actually adjust that by 0.1 mV increments. Look, 0.6, 0.7. So, you

**Dave Jones:** can actually jump up in those 0.1 mV increments. So, you do have the resolution there to actually do this. But, it is going to depend upon the voltage span, like the total voltage span, whether it's plus minus 10 V

**Dave Jones:** output, for example, and then the number of bits of your digital to analog converter, typically 16 bits. The next thing you have to be aware of is that the accuracy of like the voltage source in these things is not great. Cuz that's

**Dave Jones:** not their main purpose. Their main purpose is to generate waveforms. So, your typical accuracy of an arb gen like this in the order of like 1%, something like that. And when you're trying to make like very small changes, like 0.1

**Dave Jones:** mV, like we're doing here, then you talk start talking about the linearity of the digital to analog converter chip used in here. And I'll link in the teardown video for this. I can't remember what one it is, but I'll put it up in the

**Dave Jones:** overlay here. But, you can see this signal's pretty good. I can like 0.1 mV. IT'S ALMOST 0.2. LOOK, I CAN ADJUST AT 0.1 mV steps. Now, unfortunately, once you get to higher voltages like this, you won't be able to do like often the

**Dave Jones:** 0.1 mV offset like that. Whoop, that was just an error there, actually. Whoops. But, I can actually go up to plus minus 10 V on this particular thing. So, plus minus 10 V with a 16-bit digital-to-analog converter, you get

**Dave Jones:** pretty decent DC resolution on these things. It's great. And also, you might have temperature drifts as well, cuz these things don't have the absolute best voltage standards in them. So, you know, it But, but if you need to, you don't care

**Dave Jones:** about the absolute value, you know, if 1% is good enough for Australia, but you need to adjust and do fine adjust in DC voltages, you can use this signal gen to get an order of magnitude or or two

**Dave Jones:** orders of magnitude better than what you can get with a typical DC power supply. And as I said, you're probably using your power supply to power your project anyway. And I know you're going to ask about noise, so we've got it on the

**Dave Jones:** scope over here, and we can see that we're only talking about, you know, 220 microvolts here. But, of course, your mileage may vary with your particular arb gen, but let me adjust this in 1 mV steps. And you can see, boom, boom,

**Dave Jones:** boom, boom. We're getting nice 1 mV, but we can actually do 0.1 mV steps there. And look, you'll see that I you can hardly see that change, but I'm actually adjusting that. You know, doing my little changes there.

**Dave Jones:** Those bursts are coming like externally. Don't worry, it's not actually coming from the gen there. There's all sorts of things happening around me. I've done videos on common mode interference and stuff like that. But, there you go. You

**Dave Jones:** can actually adjust in like 0.1 mV or 1 mV steps, WAY BETTER THAN YOUR POWER SUPPLY. SO, that could come in real handy for, you know, all sorts of projects that you might need, a you know, I a nice, finely adjustable DC

**Dave Jones:** voltage. The other downside to this is that your output impedance of your function generator is going to be 50 ohms. So, it's like having your nice adjustable 16-bit, uh, you know, precision DC source, but with a 50-ohm resistor in series. And for those who

**Dave Jones:** are wondering, no, it makes no difference if you actually select the, um, output set up here, right? And we go into load if you have the high impedance or the 50 ohm. Watch it not change here. It doesn't change at all, okay? People

**Dave Jones:** think, well, it looks like it changed by a tiny little bit there. So, I don't know why it's doing that, some internal thing in here. But people think that when you select 50 ohms, uh, output impedance, then there's a relay in there

**Dave Jones:** that inserts that 50 ohm on the output. Sorry to tell you, it's always there. So, uh, the high impedance option just changes in software in your arb gen what your maximum voltage is. So, it basically doubles or halves it depending

**Dave Jones:** on what, uh, setting you're actually got here. So, I can show you that right now. We can put high impedance. I'll put my 50-ohm load on there, and bingo, it's halved. So, it makes no difference whether or not you have that 50-ohm

**Dave Jones:** setting on. It's only the maximum voltage that it, uh, well, the actual, uh, offset voltage that it actually puts. But when you're doing this, you want high impedance cuz you're usually putting, you're usually not going to put your nice adjustable little DC voltage

**Dave Jones:** into a 50-ohm load. So, yeah, make sure it's on high impedance, and then this figure will be accurate. Or reasonably accurate within the percentage tolerances of your arb gen. But anyway, I hope you found that little tip useful.

**Dave Jones:** Might have been slightly longer than 2 minutes. Uh, leave a big thumbs up down below if you like 2-minute tech tips, uh, like this. And hopefully you did, you realized something you didn't know before, or you'd forgotten, or you just

**Dave Jones:** didn't think, um, Um, that your arb gen, yeah, even the like the cheapies ones might use a 14-bit or even 16-bit converter in them. And you can get like really cheap as arb gens, you know, that are complete no-names.

**Dave Jones:** You can get them on eBay for like 100 bucks or something now. And they could actually be useful and might save your bacon one day if you need a nice fine adjustable DC voltage. And as I said, you can actually put it into a voltage

**Dave Jones:** divider as well. But just remember that 50 ohm series output resistance in there. You got to take that into account if you're using an external divider to make sure you get accurate voltages. So, if you need to adjust in, you know, 10

**Dave Jones:** microvolt steps or something, you can do that with an external divider. No worries. Anyway, thoughts and comments down below. If you liked it and found it useful, thumbs up. Catch you next time.
