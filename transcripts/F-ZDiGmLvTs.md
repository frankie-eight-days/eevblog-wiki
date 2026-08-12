---
video_id: F-ZDiGmLvTs
title: EEVblog #306 - Jim Williams Pulse Generator
url: https://www.youtube.com/watch?v=F-ZDiGmLvTs
source: youtube-asr
timestamps: {"0": 0, "1": 9, "2": 20, "3": 37, "4": 50, "5": 63, "6": 80, "7": 97, "8": 120, "9": 150, "10": 158, "11": 176, "12": 184, "13": 206, "14": 224, "15": 236, "16": 251, "17": 261, "18": 272, "19": 286, "20": 297, "21": 308, "22": 336, "23": 344, "24": 362, "25": 375, "26": 390, "27": 401, "28": 417, "29": 433, "30": 448, "31": 472, "32": 486, "33": 508, "34": 518, "35": 526, "36": 541, "37": 554, "38": 566, "39": 578, "40": 592, "41": 600, "42": 617, "43": 638, "44": 654, "45": 664, "46": 676, "47": 690, "48": 698, "49": 725, "50": 742, "51": 757, "52": 775, "53": 788, "54": 798, "55": 812, "56": 826, "57": 842, "58": 860, "59": 876, "60": 890, "61": 910, "62": 930}
---

**Dave Jones:** Hi. Now, this is a bit of a follow-on from my mailbag uh segment. Decided to make this as a separate video. We're actually using a uh pulse generator here from Minoot.

**Dave Jones:** Thank you very much, Minoot, who uh sent me this, and I'll provide uh links to uh his uh uh schematic and uh design and things like that. But, he sent that's powered from a 1.5-V battery.

**Dave Jones:** So, see the mailbag uh segment for that one. And uh but, I just decided that we'd uh do a separate video here. If using a uh pulse generator, and uh see what the bandwidth of my uh Agilent MSOX3054A oscilloscope is.

**Dave Jones:** It claims it's 500 MHz analog bandwidth. That'll be um nominally uh of course, the bandwidth of an oscilloscope is minus 3 dB down at that frequency. So, the frequency is not actually, you know, it doesn't give you a flat response to 500 MHz.

**Dave Jones:** Should be 3 dB down, but using one of these pulse generators, we can actually calculate the real bandwidth. I've got a little uh Dave Cad note here to explain the rise time versus the bandwidth.

**Dave Jones:** Now, the rise there's actually a direct relationship between the rise time you see on the oscilloscope, assuming a perfect input um you know, a pulse which has a perfect input, and the actual analog bandwidth of the scope.

**Dave Jones:** And for traditional Gaussian response scopes, they're your old uh like, you know, your basic analog uh CRT oscilloscopes, these non- digital types. It uses the classic formula, the rise time is equal to 0.35 on the bandwidth of the scope.

**Dave Jones:** It's as simple as that. But, uh these more modern scopes, uh digital scopes, don't necessarily use a have a Gaussian response on their analog input channels. They'll have what's called a maximally flat response, but even that will depend on you know, what kind of roll-off they're actually using on the the filtering of the analog uh front end.

**Dave Jones:** So, uh basically, it's, you know, it's a little bit higher generally, but it's roughly around about 0.4 on the bandwidth. So, slightly different variations, but assuming that we've got one of these, which generates an absolutely perfect pulse with zero rise time, like zero femtoseconds rise time, well, zero seconds or zero femtoseconds, same thing, but assuming it's absolutely perfect, then uh this formula will apply.

**Dave Jones:** We can If we know the rise If we we can measure the rise time on the oscilloscope, we can calculate the bandwidth, and it's not necessarily that same 500 MHz quoted.

**Dave Jones:** It's usually better than that. But, of course, these pulse generators never give you a perfect rise time. Um this one at best is going to be probably, you know, 350 picoseconds, 300, 400 picoseconds, or something like that.

**Dave Jones:** It's not perfect. So, it is actually going to have contribute It's going to have an effect on and contribute to the rise time you see on the oscilloscope here.

**Dave Jones:** But, as a rough rule of thumb, if it's five times better than what you need, then it's not really going to affect it much. Now, in the case of this 500 MHz uh bandwidth, using the formula of 0.4, we can calculate the rise time in theory of this oscilloscope is going to be uh 0.4 divided by 500 MHz.

**Dave Jones:** That's 800 picoseconds. So, this one, although we don't actually know uh we did you know, we haven't actually measured the absolute rise time of this thing, so we don't know what it is, but we know it's going to be in the order of, you know, 300 picoseconds or thereabouts.

**Dave Jones:** It's, you know, it's only like three times, just on maybe three times as good as the oscilloscope. So, it's it's Yeah, it may you know, it's going to contribute a little bit bit.

**Dave Jones:** Ideally, you're going to want five times better, but this will certainly do the job for most bandwidth that most oscilloscopes up to say, you know, 500 MHz bandwidth. And of course, to measure the true performance of this thing, we need a really high-end sampling scope.

**Dave Jones:** You know, the type that you mortgage your house for, you know, $50,000, $100,000 scope, something like that that has, you know, 10 GHz, 20 GHz bandwidth, something like that.

**Dave Jones:** We need something really good so that the bandwidth of the oscilloscope, um you know, is basically so high, it doesn't matter. We're measuring the true performance of the rise and fall time of this thing.

**Dave Jones:** So, I'm going to have to try and get access to a better scope for that to actually measure this circuit here. But anyway, we can figure out from this what uh actual bandwidth we're getting on the scope.

**Dave Jones:** And I bet you it's better than 500 MHz. And as you can see, this uh pulse generator is pretty good. The rise and fall times are essentially identical. 520 picoseconds, 530 picoseconds.

**Dave Jones:** And of course, we can simply uh swap these two terms, the rise time and the bandwidth, here uh to because if we know it, we're measuring our rise time, we can calculate the bandwidth.

**Dave Jones:** So, if we go 0.4 divided by our rise time of 520 picoseconds here, that gives us about 769 MHz. So, there you go. The bandwidth of this scope is at least um as good as that because, you know, we've got uh things like the uh you know, we've got the coax, a meter of coax cable on the uh end of this thing, which is, you know, it might contribute a

**Dave Jones:** little something. And uh and of course, we've got the uh contribution of the uh unknown rise time of this thing, but we can say it's at least that good.

**Dave Jones:** It's much better than uh what you would think at minus 3 dB down at 500 MHz. So, this thing's pretty much kicking ass. And just in case you're wondering what the other channels are, I've chosen channel three here, and we're basically getting identical 520 530 picoseconds.

**Dave Jones:** And you can see that our signal integrity is not perfect here. We have a little bit of a little dip there just before it starts, and of course some undershoot and ringing at the end of it here.

**Dave Jones:** Ideally, it should be better than that. That's probably due to our coax cable. It would have been nicer if we had a direct connection, or if this connector here wasn't this socket type, but was actually a plug type.

**Dave Jones:** We could plug that directly into the BNC on the front of our scope here. That would have been the ideal case to you know, cuz we're using a meter of RG59 cable here.

**Dave Jones:** So, that's probably causing you know, that that sort of ringing there in the waveform. I doubt it would be the layout cuz the layout is taken is really stitched the the front and the back ground planes together really nice.

**Dave Jones:** So, you know, I'm sure it's really nice short pass there directly from the transistor there, and it's working quite nice. So, I think it's mostly the coax doing that, but check out this interesting uh phenomenon.

**Dave Jones:** If I touch the can here, it disappears. Look at that. It just absolutely vanishes. Let's turn the uh Let's turn the averaging off there. And so, we're getting all of our signals there.

**Dave Jones:** We're getting our jitter. That gets wider as as it goes out. It's quite a bit of jitter in that signal, but as you can see, if I put my finger on that, it slightly gets wider, gets a little bit bigger as you as I'm not quite touching that and you can see it start to expand there as the capacitive coupling between my finger and that can really kicks in, but I can just

**Dave Jones:** completely kill that. So, that's the 50 hertz obviously pick up um from my from my body there just absolutely swamping that uh oscillator circuit in the avalanche breakdown of this uh transistor in here.

**Dave Jones:** So, really, you know, that's that's absolutely killing that. Ideally, you want this thing in a proper shielded box. But, hey, even with a bare board like this with no shield at all using a big meter long uh you know, crusty bit of coax cable, you can at least get, you know, a decent measurement on the bandwidth of your scope.

**Dave Jones:** I like it. I'd recommend you build one of these suckers up. They're very handy. And as it so happens, I'll be getting this scope upgraded to the 1 GHz bandwidth model um in the not too distant future.

**Dave Jones:** So, I'll take this along with me uh down to Melbourne. Going down there to get the scope upgraded and uh we'll be able to check the performance before and after.

**Dave Jones:** And here's before, 630 picoseconds. And uh of course, we're only got 1 ns maximum uh time base there. That's the fastest time base we've got. The 1 GHz version should go a bit quicker than that, but it'll be interesting to see um what we get on the 1 GHz version.

**Dave Jones:** So, thanks to Minut for uh this little board. That's excellent, brilliant. Saves me having to build my own. I was going to build up that classic Jim Williams uh circuit as many people have and I highly recommend you do it.

**Dave Jones:** It's good fun and you can learn all about the avalanche behavior of uh transistor um avalanche breakdown. It's terrific and get a very handy, extremely fast rise and fall time pulse generator.

**Dave Jones:** And as you can see, it's, you know, 1 2 3 4 5 6, almost 7 volts uh you know, 6 and 1/2 volt uh pulse there at, you know, at least uh uh 530 picoseconds.

**Dave Jones:** It's likely a lot better than that. So, pretty neat. Now, let's take a look at the application note from Linear Technology AN-47. Classic application note. It's massive. It written by uh the late great Jim Williams, of course.

**Dave Jones:** Very famous app note. It's got a lot more in it than just this uh pulse generator circuit. So, I highly recommend that you uh have some bedtime reading here.

**Dave Jones:** AN-47. Classic. Anyway, um this is a circuit design for measuring the probe oscilloscope uh response. It's a classic circuit. Um a few people have done something better using like garden variety uh parts, but figure D1 is the one we want, which is the circuit that uh Minut used here.

**Dave Jones:** And it basically provides a 1-nanosecond pulse with rise and fall times of approximately 350 picoseconds. But, they're going to depend upon the uh uh selection, the specific hand selection of the uh transistor, the avalanche transistor that we're uh using to generate this pulse.

**Dave Jones:** And here's the circuit here. And it's basically uh just a single-cell converter to generate for the 90 V required to uh break down, avalanche breakdown, the transistor, which is a 2N uh 2369.

**Dave Jones:** And that's the exact same transistor that Minut is using here. And it's got the metal TO-5 uh package, of course. Uh it still comes in that. But, uh you really have to uh hand select this.

**Dave Jones:** And it says, "See text there for a reason." So, let's go up and take a look at that. And here it is. "Q1 may require selection to get avalanche behavior.

**Dave Jones:** Such behavior, while characteristic of the device specified, is not guaranteed by the manufacturer. Sample of 50 Motorola uh 2N2369 spread over a 12-year date code span yielded an 82% result.

**Dave Jones:** So, some of them aren't even going to work at all, presumably, but uh this one does. It's been hand-selected by Minuit. I'm sure he's uh tested it to make sure it works before he sent it to me.

**Dave Jones:** And uh and they Jim Williams claims all the good devices switched in less than 650 picoseconds. So um uh our one is clearly getting better than that because it's at least uh 500 and uh something, but uh you know, I think it's probably going to be around that, you know, rough 350 picosecond figure uh wouldn't surprise me cuz you have to combine that 350 picoseconds with the uh rise time of the

**Dave Jones:** oscilloscope and stuff like that, but I think we need access to a better scope to measure this thing. And here's the result that uh Jim Williams gotten. As you can see, the construction of his is basically, you know, he's got it in a metal box like this, just a rat's nest construction like that.

**Dave Jones:** It looks messy, but that's, you know, the absolute lowest um you know, impe lowest inductance sort of uh build you can get. And of course uses a uh plug directly on here, which plugs directly in the oscilloscope, so there's no coax cable at all.

**Dave Jones:** It it works a treat. And that's of course why he's getting no very little ringing. There's a little bit of ringing at the tail end there, but it's tiny as opposed to uh the one which me we measured, which is probably due to the uh long coax used on that thing cuz that's going to have some inductance.

**Dave Jones:** Sure, it's working like a transmission line, but it can only go so far. So uh really, you need the utmost in signaling integrity. So if you're going to build one of these things, not only do you need to shield it, as you saw, the 50 Hz just uh swamped the thing.

**Dave Jones:** And of course he's even got the battery box uh shielded here. Do not drop me. Do not drop me. And there you go. I love it. So that's a classic build from Jim Williams.

**Dave Jones:** And of course this is a very elegant circuit. As you can see, it's effectively just a high-voltage source. It's effectively only uh four parts, pretty much. There's three resistors in here and one to Well, uh sorry, five parts.

**Dave Jones:** Uh three resistors, a a capacitor, and transistor, and that forms an avalanche breakdown uh pulse generator or an oscillator um that is, you know, the breakdowns determined on the individual transistor and the component values.

**Dave Jones:** And uh let's have a look at how uh Jim Williams explains it. The regulator's 90-V output is applied to Q1 via the 1-meg 2-pF combination. Q1 is a 40-V breakdown device for the 2N2369.

**Dave Jones:** So, it breaks down at 40 V, and then if you go above that, it non-destructively avalanches when C1 charges to a high enough voltage. So, it'll You apply 90 V here, it charges up via the 1 meg, and then it breaks down because, of course, the base here is tied to ground.

**Dave Jones:** So, there's nothing driving uh the base of this transistor. So, this transistor switched off. It's effectively, you know, it's switched off, not doing anything, but once it reaches that maximum breakdown voltage, roughly 40 V for this device, bang, then it avalanches.

**Dave Jones:** The result is a quickly rising very fast pulse across the 50-Ω output. That's why you have to terminate it in 50 Ω on your oscilloscope as well. And then, of course, uh there we go.

**Dave Jones:** C1 discharges, Q1's collector voltage falls, and the breakdown ceases, and bingo, C1 charges back up, and it free runs at about uh 200 kHz, and there's the figure that shows the output pulse, which is pretty much exactly what we've got with a little bit more uh ringing on the output.

**Dave Jones:** But apart from that, it's a very elegant, very simple circuit, and that's a Jim Williams classic. And as always, if you want to discuss this video, jump on over to the EEVblog forum, where there'll be a special thread to discuss this particular one, and uh this Jim Williams circuit.

**Dave Jones:** And, if you like the video, please give it a big thumbs up. Catch you next time.
