---
video_id: oIAATOQe3to
title: EEVblog #1285 - How to do Design By Inspection
url: https://www.youtube.com/watch?v=oIAATOQe3to
source: youtube-asr
timestamps: {"0": 1, "1": 14, "2": 28, "3": 47, "4": 58, "5": 77, "6": 89, "7": 99, "8": 117, "9": 133, "10": 147, "11": 162, "12": 175, "13": 186, "14": 201, "15": 225, "16": 240, "17": 253, "18": 273, "19": 288, "20": 299, "21": 311, "22": 327, "23": 341, "24": 353, "25": 363, "26": 382, "27": 395, "28": 414, "29": 424, "30": 441, "31": 455, "32": 466, "33": 478, "34": 488, "35": 499, "36": 513, "37": 520, "38": 536, "39": 563, "40": 576, "41": 586, "42": 596, "43": 609, "44": 629, "45": 637, "46": 652, "47": 666, "48": 679, "49": 694, "50": 703, "51": 716, "52": 730, "53": 742, "54": 758, "55": 773, "56": 782, "57": 792, "58": 803, "59": 814, "60": 823, "61": 836, "62": 855, "63": 861, "64": 871, "65": 888, "66": 899, "67": 922, "68": 937, "69": 954, "70": 967, "71": 976, "72": 989, "73": 1002, "74": 1014, "75": 1027, "76": 1039, "77": 1047, "78": 1062, "79": 1071, "80": 1094, "81": 1099, "82": 1113, "83": 1125, "84": 1143, "85": 1155}
---

**Dave Jones:** Hi, in my previous video, a rather hyperbolic one in terms of bad product design in smoke alarms actually drawing like huge amounts of quiescent current over the battery-powered solution.

**Dave Jones:** I'll link it in if you haven't seen it. And yes, I will be doing a follow-up video on that hopefully about harmonic power factor, which is quite interesting and it answers a lot of the questions people had on this video.

**Dave Jones:** But anyway, what I wanted to talk about today is an interesting aspect of engineering, one that seems incredibly simple and obvious to any like experienced design engineer, but to beginners out there, it it it just may not be obvious.

**Dave Jones:** And it's a question on the forum. It comes from hacked fridge magnet, who's been on the forum for a while, super contributor. Thank you very much. You've got to be on the EEVblog forum, it's all happening.

**Dave Jones:** What hacked fridge magnet asked is nice for a video down the track if you could build up those other two solutions that I talked about, i.e. the the on semi high voltage regulator part, and also that specific Texas Instruments one, which is specifically designed for direct mains connection.

**Dave Jones:** It does active rectification and all sorts of stuff, really neat little chip for that low power solution. And then measure the difference between the three options, i.e. the smoke alarm that we looked at.

**Dave Jones:** The terrible design with the Zener, a very wasteful design. And Zeners are jeez, they went the way of the dodo in terms of doing regulation in the 70s, only for niche applications.

**Dave Jones:** There's the odd advantage to them. But anyway, comparing the three different solutions, four if I count the full bridge. And replied, "I don't think I'll go that far. It's obvious what results a HV regulator will give in terms of uh uh the Zener solution.

**Dave Jones:** No need to build and measure to prove that. And to me, as an experienced design engineer, it's just really obvious. Like it it I don't really need to build this up and then get measurements to verify that it's actually going to make a difference as I claimed it would.

**Dave Jones:** Not so obvious to me. I will try it myself if when I can. And I highly recommend, yes, you build it up. But what I wanted to talk about today is uh design by inspection, as I call it.

**Dave Jones:** It's sort of like an old term in the industry, and it does mean various things to various people. But to me, this is a classic case of design by inspection.

**Dave Jones:** And let me try and explain what I mean. This is the regulator that we're looking at. Of course, we had the Zener solution last time. Focus, you bastard. There's the Dave card reverse engineering Zener diode solution that we had last time.

**Dave Jones:** And it's a traditional Zener with your dropper resistor here. But it just uses a AC cap here for the mains. But it's basically it's wasting power in your resistor.

**Dave Jones:** You're wasting power in your Zener diodes just to get naff all current out of the back of that thing. And I just said, "Hey, why not replace it with this and you'll get orders of magnitude less current."

**Dave Jones:** But just with my knowledge of engineering, I know for a fact that simply changing it to this uh solution here using this regulator with just a half-wave a bridge rectifier and the cap and like 240 volts directly mains in and then the current out is going to be a vastly lower solution, probably several orders and many orders of magnitude smaller than the Zener solution.

**Dave Jones:** And this is just immediately obvious. Bang, off top of my head, I know for a fact it's going to work. How do I know that? Because A, my experience, but also because if you want to go through, you can build it up, of course, and measure it.

**Dave Jones:** But, of course, building it up and measuring things, while fun and often can find hidden problems, and we'll talk about that. But, really, if you want to verify something that's relatively simple like this, you can do it by inspection.

**Dave Jones:** And what that means is you can simply look at the circuit, look at the data sheet, calculate where currents flow and things like that, and be absolutely 100% guaranteed sure, bet your life on it, except for maybe the odd trap for young players like the regulator might oscillate, or you know, something like that.

**Dave Jones:** But, assuming it doesn't do that, but you're guaranteed to get the solution you want by doing design by inspection like this. Just, you know, uh thinking about it, just jotting down some numbers, back of the envelope calculations, if you want to uh call it like that.

**Dave Jones:** But, I kind of like uh the term by inspection. So, let's take a look at it. Okay, so please excuse the crudity of the model. I didn't have time to build it to scale or to paint it here, and I had to draw it freehand with my little moose.

**Dave Jones:** So, uh not using my tablet. Anyway, this is the Zener circuit. I've admitted the second uh Zener here and the mob protection. They don't matter. Anyway, we've got a 100-ohm series 240 V AC mains in.

**Dave Jones:** Uh we've got a Zener diode here, and then we've just got a back protection diode here, and just another uh cap, and that gives us our 5-A regulated 15 V, or the Zener voltage minus that .6 uh diode drop, whatever.

**Dave Jones:** Right, so in this circuit, as you saw, we actually measured uh the current through this thing, which goes down here, and then, of course, out uh back down the mains, because there's basically no current draw into the load over here.

**Dave Jones:** The load draws like 50 microamps. It's naff all. It's half of a bee's dick, right? So, you don't worry about all of the current and all that power is being wasted in the Zener diode.

**Dave Jones:** In this particular case, the current flowing in here we measured at just under 80 milliamps. So, there's 80 milliamps flowing flowing through the 100 ohm resistor there and also the Zener as well.

**Dave Jones:** So, that's why they're very wasteful. So, you've got to supply that 80 milliamps, you've got to waste that in heat in the resistor and in the Zener here. There's no real heat loss except for a tiny little bit of a series equivalent series resistance in the cap there, but basically two losses here and here.

**Dave Jones:** All that power, I think it was 1.36 watts we actually real power that we actually measured lost just to provide our little measly 50 microamps current over here, which is ridiculous.

**Dave Jones:** Now, they they were measured currents, you could actually inspect this by inspection as well or you could simulate it. For example, so what we're going to do is just have a look at this replacement circuit which I suggested and we'll do it design by inspection.

**Dave Jones:** Once again, got the 240 volts in, we've got a half-wave bridge rectifier here, got a 2.2 mic filter cap, and that's going to generate higher DC voltage in here.

**Dave Jones:** But, this is a 450-volt device. It can handle 450 volts DC. So, it can handle directly rectified 240-volt AC mains as well as 110 and it gives a fixed 15 volts out depending on the model you choose here.

**Dave Jones:** Now, why is this going to be lower solution? Because linear regulators standard building block and this is where the experience comes in or as you'll see in a minute we can look down in the data sheet to see this, okay?

**Dave Jones:** So, what we're going to get here, let's just ignore uh, voltage regulator for a minute and let's just look at the half wave, uh, bridge rectifier and the cap here.

**Dave Jones:** The waveform that we're going to get is going to look like this. Okay, let's uh, please excuse the crudity of the model. This is terrible, Muriel. Let's just say that you start from scratch.

**Dave Jones:** If you actually, uh, simulate this, you'll be able to, uh, see it. But, it's going to you're basically going to get like this and then it's going to drop to zero.

**Dave Jones:** It's going to be zero current and then maybe you'll get some little spikes in here every, uh, cycle. But, essentially, uh, draws nothing unless your load over here starts to draw something.

**Dave Jones:** So, really, there's not much in the way of, uh, quiescent current here. It's not absolutely perfect, but it's vastly better than the wastage we're going to get up here with this Zener circuit.

**Dave Jones:** Right, so you're going to find that it's going to initially charge up, uh, the cap here, but if you're talking like steady state, it's just going to do that.

**Dave Jones:** It's going to be doing naff all. So, already, by inspection, we can, uh, determine that, um, this is going to be used vastly less power than over here like this, which is continuous power wasted in the resistor and the Zener.

**Dave Jones:** Now, what about the currents actually flowing into the regulator here? Aha, this is where you have to understand, uh, voltage regulators and linear voltage regulators like this. How they work is that basically the current flowing in here, let's call that I in, this is I IQ, which is, uh, the quiescent current of the regulator and we'll have a look at that, uh, down at the minute cuz look

**Dave Jones:** at the box here, right? And and the regulator's physically only got three legs. So, current, if it's going to flow into the regulator at all, it can only flow out of here like this or out of this ground pin like this.

**Dave Jones:** So, this is going to be a quiescent current that is essentially the just the little bit of current that the regulator itself needs to use to do its function.

**Dave Jones:** And then of course the output current here there's going to be none down the cap unless you know there's transients and things, but don't worry about that. It's going to be nothing down the cap.

**Dave Jones:** It's an open circuit. That's why the cap has a symbol like that. It's an open circuit. So, the current out of the regulator is going to equal the load that you've got.

**Dave Jones:** And we've already measured that. Let's say it's 50 microamps. Okay? So, by inspection of this circuit and of course knowing that not only basic building blocks like this linear regulator, but also knowing standard DC circuit theorems like Kirchhoff's current laws, which I've done a video on.

**Dave Jones:** I'll have to link that in. How these two currents here and here have to equal this one here. You can say that I in equals I Q plus I out.

**Dave Jones:** That's 50 microamps there. It's it's easy. So, now we can look at the data sheet to find what I Q is. We know what I out is. Quiescent current.

**Dave Jones:** There it is right there for V in range of 25 volts to 450. So, the quiescent current is basically the same regardless of the input voltage cuz there's an internal constant current source.

**Dave Jones:** So, it doesn't actually it's it's not linear. It doesn't change with increased input voltage. 7.5 microamps could be as high as 14 microamps maximum and you might take that as a worst case cuz that will be over temperature.

**Dave Jones:** What do they say? Yeah, this is for these are typical figures for minus 40 to plus 85 for I out because the quiescent current here could change with the output current.

**Dave Jones:** So, they're going 100 microamps just so happens to be pretty close, even though it was double. That's like in engineering you talk in terms of orders of magnitude. It's not 10 times more.

**Dave Jones:** It's not 500 microamps. It's 100 microamps. So, it's only double. So, near enough in terms of doing these sorts of calculations. So, all these typical figures, we're going to get 7 and 1/2 microamps.

**Dave Jones:** And we can go back up here and plug these figures back in here. Total input current here equals 7.5 microamps plus 50 microamps 57.5 microamps. Worst case, like you know, 70 microamps or something like that.

**Dave Jones:** And that is our total consumption of this circuit not including any sort of little losses in here and stuff like that. But we're already down in the sub 80 microamp level.

**Dave Jones:** So, we're already we knew that this one up here was 80 milliamps. We're already down in 80 microamp territory. So, we're talking three orders of magnitude, I not times 10, not times 100, but times 1,000 to or divide by 1,000 in this case.

**Dave Jones:** Three orders of magnitude less, 1,000 times less quiescent current for this circuit here compared to the Zener solution up here. And to any experienced engineer in the industry, everyone knows that these Zener circuits are wasteful.

**Dave Jones:** They always have been. That's why once these linear regulators came along, everyone just switched over those. Although, the Zener solution, the reason that they use it is because it's cheap.

**Dave Jones:** A Zener is still going to be lower cost than linear regulator, especially a higher voltage linear regulator like this, even though it might be, you know, 20 cents in volume or something like that.

**Dave Jones:** So, bingo, that's design by inspection. And I you can bet your life that that's the quiescent current you're going to use. But as I said before, there can of course be traps.

**Dave Jones:** These linear regulators can actually uh oscillate if you don't get the output uh capacitance correct value, the correct type, the correct you know, placement distance from the regulator and things like that.

**Dave Jones:** So, there are little traps like that. I'm not saying that you can go out and build a million widgets without building this thing up. I'm not saying that at all.

**Dave Jones:** You would definitely build up, make sure, and measure it, make sure it works. But, there's really for me, there was no reason to do a video really actually measuring and comparing these two because I it just seems absolutely obvious that you can just do this by inspection.

**Dave Jones:** So, instead, I made a video about design by inspection. No, wait. I've come a cropper. Stop the video now and try and figure out the mistake I've made. It's not huge, but it's subtle and it could make a difference, but we'll see that in a second.

**Dave Jones:** So, thanks to a patron for pointing this out because if you're a patron, you often get to see the videos early and you can see me come a cropper like this.

**Dave Jones:** Anyway, it was just a test that to see if you were paying attention. So, stop it now, download the data sheet, have a quick squeeze, and see if you can figure it out.

**Dave Jones:** All right, you're back. You notice that we had 15 V here. It's 15 V out that we need to have here. I was using the 3.3 V out table and its parameters of a chip can actually vary slightly based on the output voltage.

**Dave Jones:** So, if we go down here, quiescent current is as I said 7.5 microamps. A typical 12 V have different tables for each voltage. Here we go, 15 V. That's what we're talking about.

**Dave Jones:** And here it is, quiescent current. It's actually jumped up. It's more than doubled. It's 18 microamps typical now with 22 microamps maximum, but that doesn't change anything, really. And this is the good thing about doing this sort of like back of the envelope type stuff is that it this thing here changes to 18.

**Dave Jones:** Whoop-dee-doo. It It doesn't matter. We're still three orders of magnitude lower than the Zener current here. And I said that there were two things. I didn't notice this because, you know, I I was too busy yapping away, and I should read the data sheet properly.

**Dave Jones:** Usually, this is called quiescent current, but um on semi seem to have also ground current here. And they've got a note seven, always read the notes. A proper heat sinking and or low duty cycle pulse techniques are used to operate the device within the safe operating area.

**Dave Jones:** That's about as clear as mud, but my guess is that that has to do with when you actually load the thing up. So, I think what on semi are doing here is actually splitting up the quiescent current spec.

**Dave Jones:** It's still quiescent current, but they're going to call it something different. It's like so it's quiescent current with a load, um so to speak. But, they they call it ground current.

**Dave Jones:** And you'll notice that um the quiescent current here is for I out of precisely zero. So, that's why it's for no load only. They just separate the specs out.

**Dave Jones:** It might be important for some reason, but technically speaking, you should use ground current. So, that's I out up to 10 milliamps here. And it's 25 microamps. They don't actually specify a typical figure.

**Dave Jones:** Designing for worst case, it should be 25 microamps up here for I cube. But, even then, we're still under that 80 microamps, which is a thousand times lower than this.

**Dave Jones:** So, yeah, it doesn't matter. By the way, at like lower voltage linear regulators, they can can be much higher, like several milliamps uh quiescent current. So, just be aware of that.

**Dave Jones:** So, I hope you found that useful. And there's uh many other ways examples of this design by inspection. You may not even call it this. It's just engineering knowledge, engineering intuition, or whatever it is, um back of the envelope calculations.

**Dave Jones:** Let us know if you actually use that terminology. Leave it in the comments. But, you know, like there's other things that we could go into and things like this.

**Dave Jones:** And we're not going to like look at power factor of this versus this. Like that's something that, you know, you might measure like build it. You can simulate it, of course, but you might actually want to build it up and actually measure it out in the real world.

**Dave Jones:** And because I've got a as I said, might have a video coming up on harmonic power factor. It's not just phase lead and lag. Harmonic is the, you know, is is the killer.

**Dave Jones:** So, there's differences in there in terms of apparent power, but as far as solving the real the real power, which is the power dissipated the actual heat dissipated in these components compared to these components here, yeah, it's going to be like three orders of magnitude guaranteed by the laws of engineering.

**Dave Jones:** So, there you go. I hope you found that quick video useful. If you did, please give it a big thumbs up. And as always, discuss in the comments down below.

**Dave Jones:** Tell us about your, you know, classic Have you goofed by doing a design by inspection, for example, and you've come a gutser? And as I said, I wouldn't build up a million of these and go straight into production without actually building up comparing.

**Dave Jones:** This one up here can because like Zener diodes are guaranteed, you know, it's just practically guaranteed to work. These are, you know, complex little chippies that can, you know, have little traps and police.

**Dave Jones:** So, there's more risk in going for, you know, a solution like this than this dumb solution up here. But, anyway, let us know if you've come a gutser. So, I hope you like the video and check out my new LBRY library channel over at direct link is EVblog.tv.

**Dave Jones:** It's easy to remember. I think I just surpassed Khan Academy in terms of subscribers. Woot! The EVblog audience trumps the Khan Khan Academy audience. Absolutely fantastic on library anyway.

**Dave Jones:** How many YouTube subscribers do they got? I don't know. Tens of millions. I Anyway. Hope you liked it. Catch you next time.
