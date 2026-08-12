---
video_id: F-ZDiGmLvTs
title: EEVblog #306 - Jim Williams Pulse Generator
url: https://www.youtube.com/watch?v=F-ZDiGmLvTs
source: youtube-asr
---

**Dave Jones:** Hi. Now, this is a bit of a follow-on from my mailbag uh segment. Decided to make this as a separate video. We're actually using a uh pulse generator here from Minoot. Thank you very much, Minoot, who uh sent me this, and I'll

**Dave Jones:** provide uh links to uh his uh uh schematic and uh design and things like that. But, he sent that's powered from a 1.5-V battery. So, see the mailbag uh segment for that one. And uh but, I just decided that we'd uh do a separate video

**Dave Jones:** here. If using a uh pulse generator, and uh see what the bandwidth of my uh Agilent MSOX3054A oscilloscope is. It claims it's 500 MHz analog bandwidth. That'll be um nominally uh of course, the bandwidth of an oscilloscope is minus 3 dB down at

**Dave Jones:** that frequency. So, the frequency is not actually, you know, it doesn't give you a flat response to 500 MHz. Should be 3 dB down, but using one of these pulse generators, we can actually calculate the real bandwidth. I've got a little uh

**Dave Jones:** Dave Cad note here to explain the rise time versus the bandwidth. Now, the rise there's actually a direct relationship between the rise time you see on the oscilloscope, assuming a perfect input um you know, a pulse which has a perfect

**Dave Jones:** input, and the actual analog bandwidth of the scope. And for traditional Gaussian response scopes, they're your old uh like, you know, your basic analog uh CRT oscilloscopes, these non- digital types. It uses the classic formula, the rise time

**Dave Jones:** is equal to 0.35 on the bandwidth of the scope. It's as simple as that. But, uh these more modern scopes, uh digital scopes, don't necessarily use a have a Gaussian response on their analog input channels. They'll have what's called a

**Dave Jones:** maximally flat response, but even that will depend on you know, what kind of roll-off they're actually using on the the filtering of the analog uh front end. So, uh basically, it's, you know, it's a little bit higher generally, but

**Dave Jones:** it's roughly around about 0.4 on the bandwidth. So, slightly different variations, but assuming that we've got one of these, which generates an absolutely perfect pulse with zero rise time, like zero femtoseconds rise time, well, zero seconds or zero femtoseconds, same

**Dave Jones:** thing, but assuming it's absolutely perfect, then uh this formula will apply. We can If we know the rise If we we can measure the rise time on the oscilloscope, we can calculate the bandwidth, and it's not necessarily that

**Dave Jones:** same 500 MHz quoted. It's usually better than that. But, of course, these pulse generators never give you a perfect rise time. Um this one at best is going to be probably, you know, 350 picoseconds, 300, 400 picoseconds, or something like

**Dave Jones:** that. It's not perfect. So, it is actually going to have contribute It's going to have an effect on and contribute to the rise time you see on the oscilloscope here. But, as a rough rule of thumb, if it's five times better

**Dave Jones:** than what you need, then it's not really going to affect it much. Now, in the case of this 500 MHz uh bandwidth, using the formula of 0.4, we can calculate the rise time in theory of this oscilloscope is going to be uh 0.4

**Dave Jones:** divided by 500 MHz. That's 800 picoseconds. So, this one, although we don't actually know uh we did you know, we haven't actually measured the absolute rise time of this thing, so we don't know what it is, but we know it's going to be in the order

**Dave Jones:** of, you know, 300 picoseconds or thereabouts. It's, you know, it's only like three times, just on maybe three times as good as the oscilloscope. So, it's it's Yeah, it may you know, it's going to contribute a little bit bit.

**Dave Jones:** Ideally, you're going to want five times better, but this will certainly do the job for most bandwidth that most oscilloscopes up to say, you know, 500 MHz bandwidth. And of course, to measure the true performance of this thing, we

**Dave Jones:** need a really high-end sampling scope. You know, the type that you mortgage your house for, you know, $50,000, $100,000 scope, something like that that has, you know, 10 GHz, 20 GHz bandwidth, something like that. We need something really good so that the bandwidth of the

**Dave Jones:** oscilloscope, um you know, is basically so high, it doesn't matter. We're measuring the true performance of the rise and fall time of this thing. So, I'm going to have to try and get access to a better scope for that to actually

**Dave Jones:** measure this circuit here. But anyway, we can figure out from this what uh actual bandwidth we're getting on the scope. And I bet you it's better than 500 MHz. And as you can see, this uh pulse generator is pretty good. The rise

**Dave Jones:** and fall times are essentially identical. 520 picoseconds, 530 picoseconds. And of course, we can simply uh swap these two terms, the rise time and the bandwidth, here uh to because if we know it, we're measuring our rise time, we can calculate the

**Dave Jones:** bandwidth. So, if we go 0.4 divided by our rise time of 520 picoseconds here, that gives us about 769 MHz. So, there you go. The bandwidth of this scope is at least um as good as that because, you know, we've

**Dave Jones:** got uh things like the uh you know, we've got the coax, a meter of coax cable on the uh end of this thing, which is, you know, it might contribute a little something. And uh and of course, we've got the uh contribution of the uh

**Dave Jones:** unknown rise time of this thing, but we can say it's at least that good. It's much better than uh what you would think at minus 3 dB down at 500 MHz. So, this thing's pretty much kicking ass. And just in case

**Dave Jones:** you're wondering what the other channels are, I've chosen channel three here, and we're basically getting identical 520 530 picoseconds. And you can see that our signal integrity is not perfect here. We have a little bit of a little

**Dave Jones:** dip there just before it starts, and of course some undershoot and ringing at the end of it here. Ideally, it should be better than that. That's probably due to our coax cable. It would have been nicer if we had a direct connection, or

**Dave Jones:** if this connector here wasn't this socket type, but was actually a plug type. We could plug that directly into the BNC on the front of our scope here. That would have been the ideal case to you know, cuz we're using a meter of

**Dave Jones:** RG59 cable here. So, that's probably causing you know, that that sort of ringing there in the waveform. I doubt it would be the layout cuz the layout is taken is really stitched the the front and the back ground planes

**Dave Jones:** together really nice. So, you know, I'm sure it's really nice short pass there directly from the transistor there, and it's working quite nice. So, I think it's mostly the coax doing that, but check out this interesting uh phenomenon. If I touch the can here,

**Dave Jones:** it disappears. Look at that. It just absolutely vanishes. Let's turn the uh Let's turn the averaging off there. And so, we're getting all of our signals there. We're getting our jitter. That gets wider as as it goes out. It's quite

**Dave Jones:** a bit of jitter in that signal, but as you can see, if I put my finger on that, it slightly gets wider, gets a little bit bigger as you as I'm not quite touching that and you can see it start to expand there

**Dave Jones:** as the capacitive coupling between my finger and that can really kicks in, but I can just completely kill that. So, that's the 50 hertz obviously pick up um from my from my body there just absolutely swamping that uh oscillator

**Dave Jones:** circuit in the avalanche breakdown of this uh transistor in here. So, really, you know, that's that's absolutely killing that. Ideally, you want this thing in a proper shielded box. But, hey, even with a bare board like this with no shield at all using a big meter

**Dave Jones:** long uh you know, crusty bit of coax cable, you can at least get, you know, a decent measurement on the bandwidth of your scope. I like it. I'd recommend you build one of these suckers up. They're very handy. And as it so happens, I'll

**Dave Jones:** be getting this scope upgraded to the 1 GHz bandwidth model um in the not too distant future. So, I'll take this along with me uh down to Melbourne. Going down there to get the scope upgraded and uh we'll be able to check the performance

**Dave Jones:** before and after. And here's before, 630 picoseconds. And uh of course, we're only got 1 ns maximum uh time base there. That's the fastest time base we've got. The 1 GHz version should go a bit quicker than that, but it'll be

**Dave Jones:** interesting to see um what we get on the 1 GHz version. So, thanks to Minut for uh this little board. That's excellent, brilliant. Saves me having to build my own. I was going to build up that classic Jim Williams uh circuit as many

**Dave Jones:** people have and I highly recommend you do it. It's good fun and you can learn all about the avalanche behavior of uh transistor um avalanche breakdown. It's terrific and get a very handy, extremely fast rise and fall time

**Dave Jones:** pulse generator. And as you can see, it's, you know, 1 2 3 4 5 6, almost 7 volts uh you know, 6 and 1/2 volt uh pulse there at, you know, at least uh uh 530 picoseconds. It's likely a lot better

**Dave Jones:** than that. So, pretty neat. Now, let's take a look at the application note from Linear Technology AN-47. Classic application note. It's massive. It written by uh the late great Jim Williams, of course. Very famous app note. It's got a lot more in it than

**Dave Jones:** just this uh pulse generator circuit. So, I highly recommend that you uh have some bedtime reading here. AN-47. Classic. Anyway, um this is a circuit design for measuring the probe oscilloscope uh response. It's a classic circuit. Um a few people have done

**Dave Jones:** something better using like garden variety uh parts, but figure D1 is the one we want, which is the circuit that uh Minut used here. And it basically provides a 1-nanosecond pulse with rise and fall times of approximately 350

**Dave Jones:** picoseconds. But, they're going to depend upon the uh uh selection, the specific hand selection of the uh transistor, the avalanche transistor that we're uh using to generate this pulse. And here's the circuit here. And it's basically uh just a single-cell

**Dave Jones:** converter to generate for the 90 V required to uh break down, avalanche breakdown, the transistor, which is a 2N uh 2369. And that's the exact same transistor that Minut is using here. And it's got the metal TO-5 uh package, of course. Uh

**Dave Jones:** it still comes in that. But, uh you really have to uh hand select this. And it says, "See text there for a reason." So, let's go up and take a look at that. And here it is. "Q1 may require

**Dave Jones:** selection to get avalanche behavior. Such behavior, while characteristic of the device specified, is not guaranteed by the manufacturer. Sample of 50 Motorola uh 2N2369 spread over a 12-year date code span yielded an 82% result. So, some of them aren't even going to

**Dave Jones:** work at all, presumably, but uh this one does. It's been hand-selected by Minuit. I'm sure he's uh tested it to make sure it works before he sent it to me. And uh and they Jim Williams claims all the

**Dave Jones:** good devices switched in less than 650 picoseconds. So um uh our one is clearly getting better than that because it's at least uh 500 and uh something, but uh you know, I think it's probably going to be around that, you know, rough 350

**Dave Jones:** picosecond figure uh wouldn't surprise me cuz you have to combine that 350 picoseconds with the uh rise time of the oscilloscope and stuff like that, but I think we need access to a better scope to measure this thing.

**Dave Jones:** And here's the result that uh Jim Williams gotten. As you can see, the construction of his is basically, you know, he's got it in a metal box like this, just a rat's nest construction like that. It looks messy, but that's,

**Dave Jones:** you know, the absolute lowest um you know, impe lowest inductance sort of uh build you can get. And of course uses a uh plug directly on here, which plugs directly in the oscilloscope, so there's no coax cable at all. It it works a

**Dave Jones:** treat. And that's of course why he's getting no very little ringing. There's a little bit of ringing at the tail end there, but it's tiny as opposed to uh the one which me we measured, which is probably due to the uh long coax used on

**Dave Jones:** that thing cuz that's going to have some inductance. Sure, it's working like a transmission line, but it can only go so far. So uh really, you need the utmost in signaling integrity. So if you're going to build one of these things, not

**Dave Jones:** only do you need to shield it, as you saw, the 50 Hz just uh swamped the thing. And of course he's even got the battery box uh shielded here. Do not drop me. Do not drop me. And there you

**Dave Jones:** go. I love it. So that's a classic build from Jim Williams. And of course this is a very elegant circuit. As you can see, it's effectively just a high-voltage source. It's effectively only uh four parts, pretty much. There's three

**Dave Jones:** resistors in here and one to Well, uh sorry, five parts. Uh three resistors, a a capacitor, and transistor, and that forms an avalanche breakdown uh pulse generator or an oscillator um that is, you know, the breakdowns determined on

**Dave Jones:** the individual transistor and the component values. And uh let's have a look at how uh Jim Williams explains it. The regulator's 90-V output is applied to Q1 via the 1-meg 2-pF combination. Q1 is a 40-V breakdown device for the

**Dave Jones:** 2N2369. So, it breaks down at 40 V, and then if you go above that, it non-destructively avalanches when C1 charges to a high enough voltage. So, it'll You apply 90 V here, it charges up via the 1 meg, and then it breaks down

**Dave Jones:** because, of course, the base here is tied to ground. So, there's nothing driving uh the base of this transistor. So, this transistor switched off. It's effectively, you know, it's switched off, not doing anything, but once it reaches that maximum breakdown voltage,

**Dave Jones:** roughly 40 V for this device, bang, then it avalanches. The result is a quickly rising very fast pulse across the 50-Ω output. That's why you have to terminate it in 50 Ω on your oscilloscope as well. And then, of course, uh

**Dave Jones:** there we go. C1 discharges, Q1's collector voltage falls, and the breakdown ceases, and bingo, C1 charges back up, and it free runs at about uh 200 kHz, and there's the figure that shows the output pulse, which is pretty much

**Dave Jones:** exactly what we've got with a little bit more uh ringing on the output. But apart from that, it's a very elegant, very simple circuit, and that's a Jim Williams classic. And as always, if you want to discuss this video, jump on over

**Dave Jones:** to the EEVblog forum, where there'll be a special thread to discuss this particular one, and uh this Jim Williams circuit. And, if you like the video, please give it a big thumbs up. Catch you next time.
