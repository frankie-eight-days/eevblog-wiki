---
video_id: 4pwI2NebT90
title: EEVblog #21 - The Unusual Oscilloscope Phenomenon - Part 3
url: https://www.youtube.com/watch?v=4pwI2NebT90
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 43, "3": 62, "4": 79, "5": 102, "6": 118, "7": 137, "8": 158, "9": 186, "10": 205, "11": 222, "12": 246, "13": 263, "14": 280, "15": 304, "16": 319, "17": 340, "18": 359, "19": 384, "20": 405, "21": 433, "22": 450, "23": 472, "24": 492, "25": 515, "26": 537, "27": 558, "28": 577, "29": 597}
---

**Dave Jones:** Welcome to the EEVblog. I'm your host, Dave Jones, and this is episode number 21. Yes, it's the unusual oscilloscope phenomenon. People can't get enough of this. I've had everyone from Edison to damn Elvis contact me saying, Dave, you've got to get to the bottom of this.

**Dave Jones:** It's too mysterious. We want to see more tests. We want to see, we want to do this, we want to do that. Well, okay, I'm happy to oblige, so here we go. There was a whole bunch of industry RF guys all claiming that it was the actual loop on the end here

**Dave Jones:** that was actually picking up the signal, and I got it all wrong. But I proved that wasn't the case in the second video. This has nothing to do with it. You can pick it up with just a coax, as I demonstrated, or just the probe, or the probe shorted right at the tip, a proper RF short with some alfoil.

**Dave Jones:** Now, I said I've seen this phenomenon not only in my own lab, but in all sorts of other labs over the years and all sorts of places with all sorts of different types of oscilloscopes. But people really don't want to, and also different types of probes,

**Dave Jones:** but people don't want to take my word for it. They want some more tests. They want me to use a real oscilloscope. They want me to use a real known probe under, you know, better conditions. So, that's it. I've got a Tektronix TDS3032B, a 300 MHz Tektronix scope.

**Dave Jones:** You know, it's not the top end, but it's a pretty decent scope. I'm sure everyone will agree. So, I hope I don't get any complaints this time. 300 MHz analog bandwidth, 2.5 gig samples per second, because some people think it might be some sampling artifacts or something like that,

**Dave Jones:** and people think that I won't get the, you know, the 120-odd MHz signal on here. Well, let's find out. There are also people who wanted more details on what oscilloscope probe I'm using. They want me to use a real one. So, okay, I've got the best name brand one I could get to hand.

**Dave Jones:** Sorry, it's a Tektronix P2200, a 200 MHz passive switchable probe. Okay, pretty standard bit of kit, and hopefully I don't get any complaints over this one. Right, here we go. I've set this up exactly the same as before. I've grounded it in the horrible non-RF kind of way just to give you a benchmark.

**Dave Jones:** Here we go. Sit this down here. Single-sequence trigger. Boing! Stand up, and there we go. Check it out. That's 0.5 volts per division, okay? That's not times 10 compensated, okay? So that's 0.5 volts per division. Okay, now if I bring up the cursors on that, you can see it's about 140 MHz, okay?

**Dave Jones:** Roughly 140 MHz for that impulse, and that's typically what I get regardless of the oscilloscope. It doesn't matter which oscilloscope it is. It doesn't matter which probe. It doesn't matter how I ground it. It's usually about 120 ± 20 MHz or something like that.

**Dave Jones:** It's always pretty much within that band. Okay, let's try it again, but this time I've got the alfoil short on top of the probe. Okay, so let's give it a go. Put the probe down. Trigger. I've changed the voltage scale because I know it's going to be lower amplitude this time.

**Dave Jones:** Okay, we're down to 50 mV per division, so let's try that. And bingo! We've got 50 mV per division and lower amplitude, but it's still there. And if you call up the cursors, once again it's roughly, it's the same time base, so roughly, there it is again.

**Dave Jones:** 140 odd MHz. Now, I know what you're thinking. A lot of people are going to say, Dave, you're not thinking fourth dimensionally. This scope has a 50 ohm input terminator option. Okay, let's turn that on and see what happens. And I've triggered, and let's try it again.

**Dave Jones:** Bingo! There we go. 50 ohm input terminator. And I know what you're going to say again. Dave, we want to see it with that coax cable, 50 ohm terminator at both ends, and the 50 ohm terminator on. Okay, let's do that. Okay, here we go.

**Dave Jones:** The standard 50 ohm coax again, 50 ohm terminator. The scope is terminating in 50 ohms as well. Let's give it a try. Trigger. Nope, didn't get it that time. Let's try it again. Bingo! There we go. There it is. Once again, this is a rather unusual shape again, but once again, there's an impulse there.

**Dave Jones:** And I know what you're thinking again. Dave, this is unrealistic. No one's going to generate this amount of static charge in their lab. You haven't taken proper ESD precautions. Now, I think I mentioned this in the first vlog. I've seen this with an antistatic coat.

**Dave Jones:** So, to prove it, antistatic coat. Let's give it a go. Okay, here we are. I've got my proper antistatic lab coat. This is a top quality lab coat. I've got my wrist strap. Okay, got my wrist strap. I'm going to actually, the oscilloscope actually has a grounding terminal on the front.

**Dave Jones:** I'm going to plug the wrist strap into the oscilloscope grounding terminal. And I'm using a proper Tektronix probe. I'm using a 300 megahertz Tektronix oscilloscope. Pretty good one. I've got a nice alfoil short on the end of the probe. Let's give it a go.

**Dave Jones:** Single shot. And bingo! Complete with antistatic coat and wrist strap. Check it out. You still don't believe this thing's an issue? That's 50 millivolts per division. There you go. Told ya. Now, a couple of people have mentioned that it could be something to do with the anti-ground,

**Dave Jones:** sorry, the, yeah, the anti-ground loop circuitry used inside some decent oscilloscopes, almost. Now, this could be the case. It could have a factor as well. And it's most likely an issue. So what we're going to do is we're going to 50 ohm input terminate the scope.

**Dave Jones:** And I'm just going to connect just a clip lead onto the case of that, which is the ground. And let's give that a try, shall we? Bingo! There it is. Check it out. Five, ten millivolts per division. Okay. There we go. Out of roughly that 140, no, let's, yeah, about 140 megahertz again.

**Dave Jones:** Now, I know people aren't going to be happy until I try it with a direct alfoil short on the input. So let's, let's see if we can get anything. We may not. So I'll turn the volts per division down, five millivolts per division.

**Dave Jones:** And let's give that a go. Bingo! Look at that! That is a direct alfoil short on the input. As you can see, five millivolts per division. But it's much higher in frequency this time. Much, much higher. Now, that's, um, you know, there's, there's something else happening there as well.

**Dave Jones:** There's something else going on, I think. So, but there you go. You can still get an input and impulse directly shorted on the input. Go figure. Yeah, I know what you're thinking. You know, five millivolts per division. It's not much. It's naffle. But, you know, if you're measuring your signals, you can get these impulses.

**Dave Jones:** That's the whole point of this blog, me, you know, talking about this oscilloscope phenomenon, is that when you're measuring circuits, you've got to be careful. Because you can get impulses on the input which are due to just, you know, um, you know, magnetic impulses or some other impulses directly into the test probe that can make it look like,

**Dave Jones:** you know, it's your signal at fault when it's not. So be careful of it. So I hope that's whet the appetite of the RF guys out there. I hope it gets them fired up again about exactly what's happening here. Because I'm not going to try and, uh, I'm not game enough to try and explain anti-ground input circuitry

**Dave Jones:** when I don't actually, you know, know exactly what's happening inside this particular unit. But it happens very similar across most oscilloscopes I've used. It doesn't discriminate. So there you go. More controversy. Go for it, guys. Right, now just as an extra bonus to show you what can happen on any oscilloscope,

**Dave Jones:** I'll give you another data point to work with, fellas. So here we go. I've got my Rigol DS1052E. It's only 50 MHz, but this sucker picks it up as well. Let's give it a go. There you go. Bingo. And the frequency is around about 120 MHz.

**Dave Jones:** Once again, magic with the Alfoil Shorted Probe. A lot of people have asked, what's this Crow Probe, Brisa? What does Crow mean? Crow is Cathode Ray Oscilloscope. It's what we Australians call an oscilloscope. So this is a Crow in Australia. This is a Crow Probe.

**Dave Jones:** So I hope I cleared that up.
