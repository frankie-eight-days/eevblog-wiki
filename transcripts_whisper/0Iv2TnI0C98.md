---
video_id: 0Iv2TnI0C98
title: EEVblog #983 - PART 2: Piezoelectric Oscilloscope Issue Followup
url: https://www.youtube.com/watch?v=0Iv2TnI0C98
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 19, "2": 39, "3": 52, "4": 73, "5": 86, "6": 98, "7": 113, "8": 139, "9": 147, "10": 169, "11": 181, "12": 195, "13": 207, "14": 233, "15": 249, "16": 265, "17": 281, "18": 301, "19": 313, "20": 333, "21": 349, "22": 361, "23": 377, "24": 397, "25": 421, "26": 441, "27": 457, "28": 469, "29": 485, "30": 505, "31": 521}
---

**Dave Jones:** Hi, just a very quick follow-up video to my previous one on the piezoelectric effect, or more microphonic effect, of multi-layer ceramic capacitors on the front end of oscilloscopes inside the PCB and how that, a tap on the top of the case can transfer a shock, either a low, lowish frequency one like that

**Dave Jones:** or a high frequency one like that with a little tap, through the PCB, through all the mechanical couplings into the capacitors, which are generally microphonic. You can get ones that are more immune to the microphonic effect. Murata and others make various caps. Anyway, almost every oscilloscope on the market

**Dave Jones:** suffers this effect from somewhat. But I thought it was quite ironic that if I tap the scope, tap the screen on a touchscreen thing, that it would couple through. And rightly so, a lot of people said, hey, that's not a realistic scenario, because the inputs are unloaded.

**Dave Jones:** And fair enough. So let's take a very quick look at this. Now, typically, the multi-layer ceramic capacitor, the culprit inside the front end here, is generally going to be on the input side of the input buffer. So if it was on the other side of, say, the JFET amplifier in there, for example

**Dave Jones:** then that would be a low impedance output. And the relatively high impedance MLCC capacitor and the low amplitude signal levels we're talking about here, if you load it down with any significant impedance it's just going to swamp it out and you're not going to see any impulse at all.

**Dave Jones:** And I'll be able to demonstrate this in a second. So a lot of people said, hey, you know, the effect vanishes if you plug in an actual probe in a real world scenario. Okay, well let's take a look at that. Which it does, by the way.

**Dave Jones:** And yes, if you turn on 50 ohms so let's actually go in here like this. And we can, I'll actually demo that. I forgot all about the 50 ohms. Where's the, oh no, this thing doesn't have a 50 ohm. Doesn't this thing have a 50 ohm input?

**Dave Jones:** No it doesn't. But if we whack a 50 ohm input terminator on there, then it completely vanishes. You won't see anything there at all. I don't have one handy. Do I? No, anyway, I'll be able to demo that in a second. So, what we're going to do is I'm going to plug in the actual probe which comes with the RTB2004 scope.

**Dave Jones:** And this is a problem across virtually all digital scopes. We'll have a look at the Rodin-Schwarz. I thought it was quite ironic just that, you know, you can tap a touch screen and it comes through. So let's plug in that. It's the RTZPO3.

**Dave Jones:** It's a switchable probe. So let's plug that in. And let's actually short out the input like this. And let's turn it to times one mode, shall we? Okay, so basically we are shorting that input. Just directly shorting that input. And sure enough, I'm triggering off a different channel here, number three.

**Dave Jones:** You can tell it's color-coded actually. So, which is quite a nice feature. And so I'm triggering off channel three. All the other channels are getting the impulse through the PCB. But you notice that channel one is just fine and dandy because we're shorting the input.

**Dave Jones:** So that shows that the offending capacitor inside this is on the front side of the input buffer. Because we're loading it down with the impedance. The impedance of that's going to be quite high. The impedance of this is zero. Well, you know, it's at the end of the line.

**Dave Jones:** Anyway, transmission line. We won't get into that detail. But let's have a look what happens if we switch it to times ten. I've still got it shorted, okay? But in the times ten mode, we've got a nine meg resistor in there, okay? So let's see if it's still a problem here.

**Dave Jones:** And yes it is, okay? Yes it's reduced in amplitude because you've got the nine meg resistor plus the cable capacitance, well, the transmission line. Anyway, right, you've got the nine meg resistor in here effectively across the forming an impedance load across the offending capacitor

**Dave Jones:** inside here. It's loading it down, so it's dampening the effect. But it's still not zero, okay? It's still not zero. And you can actually get it if you touch on the screen, okay? Even still touching on the screen, granted you've got to do it quite

**Dave Jones:** you know, viciously, but you can see that it still couples through, so it doesn't get rid of it completely, even with a completely shorted load with times ten. But granted, if you're doing low signal level measurements, you're generally using a low impedance source.

**Dave Jones:** Anyway, with a times one probe, you wouldn't be using a times ten. So, you know, there's fair enough merit to that, but there are cases where you're measuring high impedance, low signal amplitude level loads. I used to, sources, I used to do this

**Dave Jones:** with hydrophones, for example, in the seismic industry is an example. Photodiodes, another example, there's various examples of high output impedance, high impedance, low amplitude level sources. So, you know, it is possible. I just wanted to show that it still actually does come through.

**Dave Jones:** Yes, it is greatly diminished, but you can see that it does actually couple through. It's only because, like, it's the trigger point I'm trying to you know, trying to get there. But you can see, you know, I'm not even putting a huge amount of force onto that.

**Dave Jones:** It seems to but, see, even like, even little gentle taps like that depending on how you trigger it, you know, you do get a little bit, a little bit of something in there, but yes, it essentially vanishes. So I'm not saying that this is a big, that

**Dave Jones:** there's a big problem with this scope, or any other scope with this effect. Because in most practical cases, yes, it's going to be diminished or go away completely in a real probing situation, but not always. So there's always that one, you know, that one pain in the ass case

**Dave Jones:** you're going to get where, you know, you could get an impulse, a little impulse in there if you get low signal level measurements, you've got high res mode, you're doing you know, like, you're trying to see down in the noise. I just wanted to show

**Dave Jones:** that it's still actually possible to do that with a shorted probe input. And by the way I showed this in the previous video, and I've done a whole separate video on this a long, long time ago. There are also multi-layer ceramic capacitors inside these.

**Dave Jones:** They're either x10 probes either have them in here at the base, or they have them inside the probe here. And Daniel from Keysight actually just did a video where he was tapping the probe like this on the top causing an input, an impulse, and yes, that

**Dave Jones:** impulse is coming from the probe. So you can see the amplitude there is absolutely massive. Right? That, look at that, that's okay, what have we got there? That's 50 millivolts per division, because the capacitor inside that probe is causing that. So you don't want

**Dave Jones:** that is an order of magnitude worse, the ones inside here, because they're more directly coupled. Either inside here, or inside here, right? So, look, you can see that I'm still getting stuff coupled through, because that's coming through low, let's go back down, okay?

**Dave Jones:** There we go. That one, that one there, even though it doesn't do it when you short it out, so if I tap on there, right, there's nothing but if I tap it on the actual case of that, which has the ceramic microphonic capacitor in there, you can see that it's causing that impulse.

**Dave Jones:** So just be aware, I've done a separate video a long time ago on that effect that probe effect. And that's probably more important than, you know, tapping on the case or anything like that. So I hope you found that interesting, I just wanted to show that

**Dave Jones:** technically it's still possible, so by all means, don't avoid buying this because you think, you know, this is still you know, going to be like a major problem in everyday use. It's not, I just wanted to show in some cases of high impedance loads

**Dave Jones:** high impedance sources, that it can be an issue and if you're doing 50 ohm input termination off, forget it, you're never going to see this issue at all. Because those multilake ceramic capacitors are quite effectively a high impedance source, they're effectively a piezoelectric

**Dave Jones:** element. They're a hydrophone, that kind of same thing that I used to work on, basically, back in the day. And they, if you're working on a high impedance source with times one probe, it can be a problem. It doesn't vanish completely. Anyway, I hope you found that interesting.

**Dave Jones:** Catch you next time.
