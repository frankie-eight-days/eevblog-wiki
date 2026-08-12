---
video_id: Ht48vv0rQYk
title: EEVblog #941 - Schmitt Trigger Tutorial
url: https://www.youtube.com/watch?v=Ht48vv0rQYk
source: youtube-asr
timestamps: {"0": 1, "1": 14, "2": 27, "3": 42, "4": 51, "5": 61, "6": 75, "7": 86, "8": 101, "9": 111, "10": 122, "11": 138, "12": 148, "13": 169, "14": 183, "15": 193, "16": 214, "17": 232, "18": 246, "19": 267, "20": 279, "21": 305, "22": 314, "23": 333, "24": 344, "25": 353, "26": 360, "27": 373, "28": 389, "29": 400, "30": 413, "31": 423, "32": 435, "33": 446, "34": 458, "35": 471, "36": 487, "37": 500, "38": 513, "39": 533, "40": 552, "41": 569, "42": 582, "43": 593, "44": 607, "45": 617, "46": 632, "47": 659, "48": 671, "49": 687, "50": 696, "51": 713, "52": 723, "53": 736, "54": 752, "55": 762, "56": 772, "57": 788, "58": 800, "59": 811, "60": 822, "61": 844, "62": 859, "63": 879, "64": 896, "65": 920, "66": 935, "67": 947, "68": 963, "69": 978, "70": 998, "71": 1009, "72": 1028, "73": 1041, "74": 1054, "75": 1080, "76": 1096, "77": 1106, "78": 1121, "79": 1132, "80": 1150, "81": 1164, "82": 1182, "83": 1201, "84": 1211, "85": 1227, "86": 1239, "87": 1251, "88": 1264, "89": 1276, "90": 1304, "91": 1316, "92": 1327, "93": 1351, "94": 1363, "95": 1375, "96": 1391, "97": 1401, "98": 1420, "99": 1439, "100": 1448, "101": 1471, "102": 1483, "103": 1506, "104": 1519, "105": 1531, "106": 1545, "107": 1560, "108": 1574, "109": 1586, "110": 1596, "111": 1609, "112": 1616, "113": 1629, "114": 1641, "115": 1666, "116": 1674, "117": 1685, "118": 1700, "119": 1713, "120": 1725, "121": 1749, "122": 1765, "123": 1788, "124": 1804, "125": 1822, "126": 1836}
---

**Dave Jones:** Hi, there's a couple of annoying problems in electronics. One of them is slow rising input signals on uh digital circuitry and other stuff. And the other one is noise on comparator inputs and such like.

**Dave Jones:** So, we're going to take a look at these uh two problems today and how we can fix them. There's basically one solution for both. So, let's take a look at slow rising input signals and the problems they can cause with digital circuitry.

**Dave Jones:** Now, uh look at the Dave CAD drawing here. I've got a 74HC161 4-bit uh synchronous counter, jelly bean logic. I've got it wired up here and I've got the four LEDs on the output and I've just got like a 2-Hz input uh square wave and it's counting up in binary just fine.

**Dave Jones:** And by the way, don't worry about all these extra pins here. This is just a complicated uh chip with that has a data load input. I've just set them all loaded.

**Dave Jones:** Has various enables and uh stuff like that. So, I've just tied all those high. Basically, clock in, binary out. The settings for our input clock here, you can see it's uh 5-V uh peak-to-peak.

**Dave Jones:** So, from 0 to 5 V, it's just got an offset there. Duty cycle is 50% and the rise time of the uh positive edge is 30 ns. And if we go over to our scope here and have a look at our input signal, sure enough, there's our 50% duty cycle.

**Dave Jones:** It's just a regular uh clock all the way in and we can see that our rise time is about 45 ns. It's near enough. It's going to have uh you know, some delay due to the cables and other stuff.

**Dave Jones:** But, it's basically a nice sharp rising edge and it's working just fine, as you'd expect. So, what I've done is uh slowed it down a little bit to 500 ns for the rise time.

**Dave Jones:** This is a positive edge triggered uh clock and you can see the count is still just fine. We go up to 1 microsecond here, near enough, and it still seems to be working just fine.

**Dave Jones:** We're at 2 microseconds and it all still Well, yep, it all still looks good. Oh, there was no zero there. Do you notice that there was no zero? It did not go to zero.

**Dave Jones:** All the LEDs didn't turn off. You see that? It's starting to play up. That's at two microseconds. And if I go higher, four microseconds, whoops. Our first LED there is just stuck on.

**Dave Jones:** What's going on? This thing has completely failed. And you might think, "Look, this is a perfectly fine edge. There's no noise on it." Aha, trap for young players. Let's go to the data sheet.

**Dave Jones:** Now, I've got the data sheet here for the exact National Semiconductor chip that we use in the 74HC161, the exact same brand. Different brand logic families like this will vary slightly due to slightly different process technology and stuff like that, but basically, they're all pretty much identical among manufacturers.

**Dave Jones:** And it's got all sorts of specs in here for propagation delay and setup time and all sorts of stuff. And if you go right down to the bottom of the specs here, you'll find that there's a maximum input rise time.

**Dave Jones:** Aha. This one's actually maximum input rise and fall time as well. But we're only concerned with the rise time here for the positive clock edge. I haven't changed the fall time here at all.

**Dave Jones:** And you'll notice that it does actually change with voltage. So, at 2 V, it's 1,000 ns, 1 µs is the maximum rise time. But at the 4.5 or say 5 V we're using it at, then it the maximum rise time you can have is 500 ns.

**Dave Jones:** And where we saw that, you know, 1 or 2 µs, it started to play up. And sure enough, it's outside of the spec. It's not guaranteed. And if I take it right up to 50 µs here, look, it's just it's just flashing the two most significant digits.

**Dave Jones:** It's just gone crazy. But 50 microseconds, that's still a pretty fast or fastish input edge. If you actually look at your square wave here, you might think that's practically instantaneous, right?

**Dave Jones:** It's It's a super fast input edge, not nanoseconds, but hey, it's you know, tens of microseconds, so it should work, but it doesn't. And what's going on here is that the input is uh transitioning through the threshold voltages for your digital logic, and you might be familiar with this uh V in high and V in uh low for the digital logic.

**Dave Jones:** The data sheet has specs on this. And instead of a really fast transition through that, we've got a real slow transition through, and it's spending too much time in that um undefined region, and hence the gate might start to oscillate or do something weird.

**Dave Jones:** And you might think, well, what's the big deal here? Just make sure you have fast input uh edges. Well, this can be a problem. I'll say, for example, a reset pin of a microcontroller, for example, you might uh traditionally hook that up to an RC circuit on the input so that it uh shorts the pin when the uh power supply powers on and resets the chip for a certain amount of time, and

**Dave Jones:** the capacitor charges up, and then you've got a slow rising input signal. If you feed that into some digital logic, that can go into a metastable state and ruin your day.

**Dave Jones:** Or if you're designing a crude RC oscillator with some spare digital gates or something like that, mhm, that can ruin your day as well. So, a slow transition through this uh undefined threshold region can cause uh oscillation or some other weird effect inside unknown effect inside the gate.

**Dave Jones:** It's basically uh not guaranteed. That's why there's a maximum spec for that rise time. Now, this probably shouldn't be confused with metastability, which is something I'm sure I've mentioned in a previous uh video somewhere.

**Dave Jones:** I haven't done a specific video on it, maybe I'll will in the future, but metastability has a similar end result in that the gate can oscillate, do weird stuff like that.

**Dave Jones:** But, in the case of metastability in clocked uh systems, that has to do with uh setup and hold times and not the actual uh slew rate of the input signal being in the undefined region.

**Dave Jones:** But, some people might call this sort of uh oscillation caused by this uh input signal a metastable state. But, yeah, just don't confuse it with metastability, which is a different uh phenomenon.

**Dave Jones:** So, let's take a look at our next issue here, which is noise on comparators. Now, we've got a classic jelly bean uh comparator here, the LM311, and uh we've got a reference voltage on the non-inverting input here, which is uh just a resistor divider from our 5-V uh rail.

**Dave Jones:** So, two 1K resistors giving us 2.5 V reference voltage here, and the um inverting input is our input signal. Now, our input uh signal can be anything. It can be, say, a battery.

**Dave Jones:** This could be a classic uh low battery uh indicator. Uh for example, where you have a reference voltage, your battery drops below the uh reference voltage, and your LED turns on or it signals uh you know, uh the micro or something else.

**Dave Jones:** And here's our output LED. And if we turn that pot, there we go. We can turn our LED off and on. No worries whatsoever. This is working just fine.

**Dave Jones:** Or is it? Hmm. What if we try and get it right on the edge like that? It could be a hold-your-tongue at the right angle. You might Oh, well, can you see that LED?

**Dave Jones:** Flicker, flicker, flicker, flicker, flicker. What's going on? Let's take a look at the scope. Now, I've got my scope set up uh at a slowish uh time base. What is it?

**Dave Jones:** 500 ms per division uh in normal uh trigger mode, so that uh it doesn't keep auto sweeping across the screen, so it'll only um capture on the positive edge when we uh transition through there.

**Dave Jones:** So, here we go. I'll turn the pot. The LED should turn off, and bingo, it's captured it. No worries whatsoever, right? It looks fine. Mhm, let's actually zoom in here.

**Dave Jones:** What what what what What's going on there? Look, we've got some horrible oscillation there. Let's try that again, shall we? It'll auto reset. Oh, there we go, it captured the uh other edge there, but there we go.

**Dave Jones:** Bingo, we captured it again, and you can see that we've got some oscillation in there. Wow, look at that. That's horrible. And you can see that we're also going to get that when the LED switches from off to on as well on the negative edge.

**Dave Jones:** We're going to get the same sort of oscillation going on there. And well, this might be just fine and dandy if you uh you know, you just got a low battery LED circuit or something like that.

**Dave Jones:** Okay, you know, not a real uh issue, but hey, oscillations are undesirable. They can draw extra power, and uh the LED's drawing power, but hey, if you've got an ultra low power circuit, and that wasn't going to a LED, it was going off uh to some you know, triggering your micro or something like that, um an interrupt service routine, that could really ruin your day.

**Dave Jones:** Look, I'll turn it really fast, and it's sort of like narrow there, but if I turn it really slow, watch this. Boom, look how long that is. The slower I did it, and the just like before with the uh rise time, the slower I did it, the more oscillation that we actually got.

**Dave Jones:** So, what's Here we go, I'll go really slow again, and wow, look at that. Whereas if I go really fast, boom, look, there's not much of it, but there is still oscillation, and that could cause you no end of problems, depending on the uh circuit implementation you've got.

**Dave Jones:** Real trap, that one. So, there's the two problems, input slew rate, and also uh noise on comparator circuits. What's happening here and how do we fix it? Well, let's go to the whiteboard.

**Dave Jones:** So, we'll jump straight into the solution, the Schmitt trigger. You might have got it from the title of the video. And it's absolutely classic bit and building block. It's used everywhere, and you may not even have realized it's used in uh places.

**Dave Jones:** Now, I'll very briefly and very simplistically, it's important to realize what's happening in a CMOS uh digital circuit. You might have uh seen this if you saw the same in the internal circuitry inside a typical uh CMOS gate.

**Dave Jones:** In this case, it's a CMOS uh inverter. Then, you basically just got two MOSFETs like this. The gates are tied together. You've got a P-channel and N-channel MOSFET, and the output here.

**Dave Jones:** That's it. Now, we won't get into uh detailed characteristic curves of MOSFETs and how they work, but suffice it to say that when your input signal changes, cuz the two gates are tied together like this, one transistor's supposed to be on when the other one's off and vice versa.

**Dave Jones:** But, that's not always the case. If you have a slow-changing input signal, a you know, a slow slew rate like we saw like that, there's going to be a point where both of these transistors are on or partially on at the same time, and that can cause excess current and other uh issues in digital logic, especially when they've just got a non-Schmitt trigger input like this, a standard CMOS input, they

**Dave Jones:** don't like having slow input slew rates. They like having just to be switched incredibly fast so that either one transistor is on or the other one's off. So, let's get into Schmitt triggers.

**Dave Jones:** Now, you might have seen this symbol before inside an inverter gate or on a microcontroller data sheet or uh something like that on one of the digital inputs, like the reset uh pin of a micro, for example, might have in the internal block diagram, might actually have this little symbol here.

**Dave Jones:** And it could actually also be the other way around. It could also be like that as well, but it doesn't We won't get into details. It's the same thing.

**Dave Jones:** That means that this inverter or this particular part of the logic has a Schmitt trigger on the input. And shortly we'll see why this symbol is actually a good representation, visual representation of what actually happens in a Schmitt trigger.

**Dave Jones:** So, we'll start the solution by taking a look at our classic comparator circuit here. Now, I'm just like using an op-amp here, but it can be an op-amp or a comparator.

**Dave Jones:** Op-amps can be used as comparators as I've done in mentioned in my op-amp video, which will be linked in down below if you haven't seen that. So, we've got our input, we've got our output, positive and negative rail cuz that's going to make our just our theory and a little bit of math simpler.

**Dave Jones:** And our input is tied to ground like this. So, this is actually a zero crossing detector building block circuit. So, if you want to detect if your circuit wants to detect a zero crossing on an input signal, this is how you do it.

**Dave Jones:** You might have noticed that I flipped this around cuz I kind of goofed it. I wasn't thinking. Anyway, we'll see why in a second. Now, let's take the example of our zero crossing detector.

**Dave Jones:** Works exactly the same for the circuit that we saw on the breadboard before where the input where we had a single rail here, ground and 5 volts, and then our input was half rail at 2.5 volts.

**Dave Jones:** Works exactly the same way. So, you should know how a basic comparator works. If our input our non-inverting input is greater than in this case, if our input waveform goes high like this above 0 volts, if it's greater than our reference voltage on the non-inverting input, i.e.

**Dave Jones:** ground, then our output is going to swing negative because the negative input is more positive than the positive input, so it's going the output is just going to switch negative like this.

**Dave Jones:** Or if we had a grounded reference like we did in the previous example, it'd just go to ground. And likewise, once that input signal goes below the reference voltage, i.e.

**Dave Jones:** below 0 V here, boom, it switches the other way. And that's it. Simple. But, we didn't see that in our example. We saw that we had some oscillation on the transition here.

**Dave Jones:** So, it might be actually obvious what's going on here. In the real world, you get noise on signals. Nothing is absolutely perfect. And in the case of a comparator here, that input threshold, this input only needs to be a fraction, half a bee's dick, a smidgen above or below the reference voltage here, be it I don't know, a microvolt, a nanovolt, whatever.

**Dave Jones:** You don't actually know, but if think of it basically as practically zero. It just needs to be above by any ridiculously small amount, and it will switch. And of course, um your input signal is going to have noise on it.

**Dave Jones:** It always will. It's just a practical uh reality of real-world circuits. Now, I've greatly exaggerated the noise on our input sine wave here like this, and you'll notice that it actually transitions through the noise actually transitions through that ground there several times.

**Dave Jones:** So, in this case, if we take that down here, okay? This one's going negative, so it's going to go negative like this. But, then you notice that because it went above zero, so it's going to go negative, but then it transition because of noise briefly down below ground like this.

**Dave Jones:** So, it's going to switch boom like that because of that matching one there. Basically going to transition several times like that before it actually stays down like this. And likewise over here, it's going to transition a few times there due to noise.

**Dave Jones:** And that is what we saw on our practical circuit because there's no hysteresis or no Schmitt trigger action on our comparator here. So, our solution is to add what's called hysteresis otherwise known as a Schmitt trigger.

**Dave Jones:** A Schmitt trigger uses hysteresis to give you the Schmitt trigger action. You can think of them as basically the same thing. If a circuit has hysteresis, it's basically acting as a Schmitt trigger.

**Dave Jones:** And the way we do this is we will actually want to widen the margin on the input where this switches between positive and negative to prevent noise, any certain level of noise from actually giving us multiple oscillations, multiple transitions like that.

**Dave Jones:** And the way we do this is to use positive feedback as opposed to negative feedback which you're familiar with with amplifiers. Amplifiers use negative feedback to amplify things. What we're going to use positive feedback.

**Dave Jones:** Usually positive feedback is a bad thing in electronics. You usually don't want it, but in this case it's very very helpful because we can add Bingo, you might notice this looks somewhat like your negative feedback amplifier, but it goes back to the non-inverting input.

**Dave Jones:** So, it's positive feedback. So, what this positive feedback gives us, and I'll go through working out these values in a minute, is it gives us not just that 0 V threshold voltage and 0 V is it.

**Dave Jones:** Even if it's smidgen above or smidgen below, you get that oscillation. What we want to do is add two different threshold levels, the upper threshold level and the lower threshold level about that 0 V point or about 2.5 what we had in the circuit before.

**Dave Jones:** Doesn't matter. Then we can if we have these two thresholds like this, then the noise like this is not going to affect it. Let me show you. Now, in this case, the 0 V threshold doesn't exist, so we can ignore that.

**Dave Jones:** We've just got an upper and a lower one, which in this case I've just arbitrarily said +10 mV and -10 mV about ground, because let's say our noise in our system might be, you know, 5 mV or 1 mV or something like that.

**Dave Jones:** We want to avoid that level of noise causing our false triggering. So, in this case, well, let's just assume it's high. Like normally, we would have had the oscillation here if we just had that one 0 V level, but because we've got this upper threshold, it won't switch until it gets to that particular threshold right there, and then it will go negative just like before.

**Dave Jones:** The upper threshold works exactly the same way as our 0 V, but the key is because of the positive feedback action, and we'll see how it works in a second, it won't then transition back high until it actually until the signal goes back below the lower threshold.

**Dave Jones:** So, in this case, you see how it transitioned back down under the upper threshold there, it's not going to do anything. It only cares about the lower threshold before it switches back.

**Dave Jones:** So, this noise about here is not going to cause any problems whatsoever. It's only when it then it first goes through this lower threshold, will it actually boom, switch back like that.

**Dave Jones:** And then once again, even if it transitions multiple times because of noise through this lower threshold, it's not going to flip back until it reaches the upper threshold again.

**Dave Jones:** So, bingo, with by adding some hysteresis, which is the difference between the upper threshold voltage and lower threshold voltage, by Schmitt trigger action, we've added a margin in there that eliminates our noise problems, and we get a nice clean switching waveform.

**Dave Jones:** Beauty. So, let's take a quick look at how this would actually work using some typical values here. Let's say we had our plus minus rails here plus 10 volts minus 10 volts and our two resistors here with the 9k we'll call that R1 and 1k R2.

**Dave Jones:** You might realize why I've chosen 9k cuz it comes out as a nice round number. Now, the formula is and it's very simple math. The upper threshold voltage here is you might recognize this R2 over R1 R2 times V out maximum.

**Dave Jones:** That's a voltage that's the voltage divider formula. You already should already know that. So, it's basically the voltage divider. So, you put 9 1k over 10k total gives you 0.1 times V out which is the maximum voltage this particular comparator goes to.

**Dave Jones:** It may not always go to the rail, but let's assume it's ideal. It goes to the rail to 10 volts. Then UT in this particular case would be plus 1 volt.

**Dave Jones:** Easy. And likewise for the lower threshold voltage down here exactly the same way. LT equals minus 1 volt. So, in this case instead of 10 millivolt example we used before the example would be plus 1 volt and minus 1 volt.

**Dave Jones:** So, you could have half a volt of noise on there and it wouldn't cause a problem. So, what's the mechanism that makes this work? Well, it's fairly simple. Remember that we had ground here before.

**Dave Jones:** Well, ground is now here and the voltage the reference voltage here is the point on this voltage divider referenced to this ground here. This could be some other voltage could be 2 and 1/2 volts or whatever.

**Dave Jones:** Doesn't matter. The formula just gets a bit messier, but it works the same way. Right. So, let's take the case where our output is high. Okay? So, our output here is plus 10 volts.

**Dave Jones:** So, instead of our reference voltage being 0 volts like it was before cuz we had ground there, it's now that not plus 1 V because of this voltage divider action, this reference voltage is now plus 1 V.

**Dave Jones:** So, it won't um action, it won't do anything, it won't switch unless it gets to plus 1 V here. So, once that signal goes once, just once over, even a smidgen over, just like our uh our issue before with 0 V, even you know, a a microvolt, a nanovolt over, whatever it is, the first time it does that, it'll switch down like this and the output will then switch to minus 10

**Dave Jones:** V down here. What have we got in our voltage divider? Instead of having plus 1 V here, because we've got minus 10 V here, we're going to have minus 1 V here and our reference voltage is changed.

**Dave Jones:** You see how we had a fixed reference voltage before, but now we've got a reference voltage which toggles between two different values depending on our output state. It's clever.

**Dave Jones:** So, our reference comparator voltage here is immediately, let's just say instantaneously, switched from plus 1 V to minus 1 V like this, and bingo, that noise doesn't cause an issue anymore because it now needs to go through the lower threshold point down here, the minus 1 V, before it can switch back.

**Dave Jones:** Beautiful. And that is hysteresis, and that's the Schmitt trigger. So, why is it called a Schmitt trigger? Well, as common in electronics, it's named after the inventor, in this case, Otto Schmitt in 1934.

**Dave Jones:** And why is it called a trigger? Because, well, kind of warm fuzzy, because once it goes through this threshold, it triggers it into the next condition, something like that.

**Dave Jones:** It's a Schmitt trigger. So, I promised to tell you where the Schmitt trigger symbol came from. Well, you have to look at the transfer function and I won't go into details, but it's basically the output referred to the input in a graphical representation like this.

**Dave Jones:** And in this case, the output voltage switches between plus 10 volts and minus 10 volts and then the input voltage switches between plus and minus 1 volt like this.

**Dave Jones:** And you can see that if you invert it like that to scale on the input, bingo, that is what it looks like. So, you can see that our Schmitt symbol is actually, well, in this particular case, they put a slope on it like that and that is our Schmitt trigger.

**Dave Jones:** It can also go the opposite direction and that's supposed to imply a directionality, but it doesn't. Just draw it either way, fine. And sometimes it's drawn like sloped like that, either that way or that way slightly, or sometimes it's drawn with vertical lines like we get in this ideal representation here.

**Dave Jones:** Doesn't really matter. You get the idea. So, let's go back to our breadboard and actually fix this to see if our oscillation disappears when we add some positive feedback.

**Dave Jones:** Now, in this case, I won't go through the calculations cuz using the LM311 comparator that we've got, it's got an open collector output. We're driving a LED like this and it's like to add in a resistor going back like this, you know, it's either ground like this, but there's going to be some drop across there and it's not going to be quite ground and it's going to be a little bit

**Dave Jones:** tricky, but it it doesn't matter. We'll just whack a resistor in there, you know, 10K, 20K, something like that. See if it makes a difference. So, here's our original circuit with no hysteresis, no positive feedback whatsoever.

**Dave Jones:** In this case, we've got 1K, 1K resistor here. Now, I'm going to add a 15K resistor from the output here back to our non-inverting input. So, I've added some uh, feedback there and the calculation gets a little bit, uh, tricky with the voltage divider and, you know, everything else, but and the fact that we've got a LED and an open collector output, doesn't matter.

**Dave Jones:** 15k, it's just like order of magnitude bigger. I just happen to have a 15k line on the bench. So, um, it'll add some hysteresis to this and, uh, we should see a difference.

**Dave Jones:** So, this is before. Okay, I'll do this all in a single shot to show you that there's no funny business. Okay, there's our positive and negative thresholds. I've got that auto, um, sorry, normal triggering on the scope, so we can see that.

**Dave Jones:** I'm not going to change any settings and I've got my 15k resistor here. Let me plug it in. And, come on. In we go. And, bingo. Fixed. There we go.

**Dave Jones:** Look at that. Even if we go right in, we've only got the one transition. Winner, winner, chicken dinner. We just added some hysteresis to that and our noise problem is gone.

**Dave Jones:** Schmitt triggers. Beautiful. And as for fixing our dodgy clock input here, well, I won't bore you with the, uh, details, but suffice it to say, you just either use a counter that has a Schmitt trigger on the clock input, which most of them do.

**Dave Jones:** I chose the, uh, 74HC161 cuz it in particular didn't have a Schmitt trigger input or you can just add, you know, a 741, uh, a four Schmitt trigger inverter in there.

**Dave Jones:** No worries. It'll fix the problem. Try it yourself. Now, we saw how you can do an analog Schmitt trigger with the, uh, comparator and the feedback resistors, the positive feedback.

**Dave Jones:** That's all hunky-dory, but how do they do it inside, say, a 74HC14 Schmitt inverter or inside any other chip that has a CMOS, uh, digital chip that has a Schmitt trigger action on the input?

**Dave Jones:** Well, they can't have resistors in there and do it all analogically that you know, that just doesn't work in the process. They have to do it using discrete MOSFET transistors.

**Dave Jones:** And here's a shot of how they actually do it from Fairchild and it is rather clever. Look at the input here. It actually uses four stacked MOSFETs on the input.

**Dave Jones:** Two N-channel down the bottom, two P-channel up the top and this is different from the arrangement I showed on the whiteboard before with just the single transistor top and bottom.

**Dave Jones:** And then they've got additional two MOSFETs there, P3 and N3, which act as source followers. Actually going from the output feeding back the output, effectively feeding back the output signal back to the middle of either the upper or the lower totem segment up there on the input and that can be used as a Schmitt trigger action.

**Dave Jones:** It's fantastic. So, let's take a brief and simplistic look at how it works. If you've got zero volts on the input, then the upper two MOSFETs P1 and P2 are going to be on.

**Dave Jones:** P3's going to be off and N1 and N2 down the bottom of the pole totem pole there are going to be off. And and N3 is going to be on.

**Dave Jones:** But if we start to raise that input voltage by a little bit, let's just say 1 volt for argument's sake, then it sort of reaches a threshold where N1, which was off before, actually switches on and that forms a voltage divider between VCC and ground with N3.

**Dave Jones:** So, N1 and N3 are now forming that voltage divider similar to what the resistors were doing in that analog type configuration. And a similar sort of thing's happening here as that input voltage rises.

**Dave Jones:** And likewise, if you went down from 5 volts down to then the same mirror thing would happen with P1 and P3 at the top. They would act as a voltage dividers between VCC and ground.

**Dave Jones:** So, that voltage divider of M1 and N3 then biases uh the source of N2 there to a particular threshold level, which then when it transition and then if you raise the input voltage even more, it transitions through that and switches that on and boom it flips the trigger point over and and the mirror starts to happen with the P1 and P2 and P3 at the top.

**Dave Jones:** It's a very clever system. I love it. And then of course uh parts that on the output you'll see that out is in the middle there. Then the other two P4 and N4 there are just another inverter with a and then an output driver using P6 and N6.

**Dave Jones:** But, that's how you basically configure a Schmitt trigger inside any sort of modern CMOS digital logic. And I mentioned way back towards the start of this video that when you have both of the transistors on in a typical configuration a ramp that input slowly both transistors can partially turn on you can draw excess current and also if it oscillates you can draw excess current as well.

**Dave Jones:** Well, unfortunately the Schmitt trigger configuration doesn't give you a free lunch here. It doesn't let you escape that this if you have a slow changing input it still does actually increase the current but of course it doesn't oscillate and solves all that sort of problem.

**Dave Jones:** But, you can see here that this is the supply current in milliamps versus the input voltage in volts for a Schmitt trigger gate here. And you can see that at various threshold at the two threshold voltages there it sort of peaks at you know at much higher current.

**Dave Jones:** So, yeah if you ramp it through it can still cause little current spikes. So, yeah you don't completely get away with that unfortunately. So, there you go. I hope you enjoyed that look at the Schmitt trigger and hysteresis.

**Dave Jones:** Anyway, if you liked it please give it a big thumbs up and if you want to discuss it links down below or comments. Catch you next time.
