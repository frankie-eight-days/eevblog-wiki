---
video_id: ep3D_LC2UzU
title: EEVblog #469 - Cockcroft-Walton Multiplier
url: https://www.youtube.com/watch?v=ep3D_LC2UzU
source: youtube-asr
timestamps: {"0": 1, "1": 14, "2": 29, "3": 37, "4": 46, "5": 60, "6": 73, "7": 89, "8": 102, "9": 114, "10": 127, "11": 138, "12": 152, "13": 167, "14": 183, "15": 199, "16": 213, "17": 222, "18": 231, "19": 243, "20": 256, "21": 272, "22": 287, "23": 298, "24": 318, "25": 339, "26": 354, "27": 366, "28": 377, "29": 393, "30": 409, "31": 428, "32": 448, "33": 456, "34": 465, "35": 478, "36": 488, "37": 512, "38": 531, "39": 544, "40": 555, "41": 564, "42": 579, "43": 590, "44": 604, "45": 615, "46": 634, "47": 646, "48": 653, "49": 682, "50": 697, "51": 707, "52": 717, "53": 732, "54": 746, "55": 757, "56": 771, "57": 786, "58": 803, "59": 826, "60": 836, "61": 850, "62": 864, "63": 877, "64": 890, "65": 906, "66": 923, "67": 947, "68": 962, "69": 969, "70": 990, "71": 1000, "72": 1011, "73": 1020, "74": 1033, "75": 1045, "76": 1058, "77": 1070, "78": 1079, "79": 1091, "80": 1105, "81": 1118, "82": 1126, "83": 1139, "84": 1152, "85": 1165, "86": 1178, "87": 1191, "88": 1208, "89": 1221, "90": 1238, "91": 1256, "92": 1266, "93": 1275, "94": 1288, "95": 1298, "96": 1314, "97": 1330, "98": 1342, "99": 1354, "100": 1366, "101": 1377, "102": 1386, "103": 1396, "104": 1409, "105": 1426, "106": 1436, "107": 1450, "108": 1464, "109": 1472, "110": 1482, "111": 1496}
---

**Dave Jones:** Hi, welcome to Fundamentals Friday. Hopefully, a regular segment, although don't hold me to it, where I explain just a little snippet of something to do with electronics. Some little, you know, a little building block circuit or something like that.

**Dave Jones:** Today, we're going to do high voltage DC generation. Like this is a follow-up from the Uni-T video I just did. If you haven't seen it, it'll be linked down below, where it generated 5 kilovolts DC inside.

**Dave Jones:** And we had a quick look at the circuit and I said I'd explain it further. So, that's what we're going to do here. Now, my aim with this segment is to keep it relatively short.

**Dave Jones:** I know I always say that. This is just a quick video. I'll try and keep it to like 10, 15 minutes, something like that. Uh, we'll give it a go.

**Dave Jones:** If I'm doing half hour tutorials, I think I'm doing it wrong. So, anyway, let's take a look at high voltage DC generation. Now, let's have a look here. You've seen uh, your traditional transformer here.

**Dave Jones:** Let's say it has the one-to-one winding ratio. So, we're feeding in 1 volt AC and we're getting out 1 volt. Now, you've seen your regular half-wave rectifier like this with your diode there and your capacitor.

**Dave Jones:** Right, everyone's familiar with that circuit. Okay, it rectifies the AC, but some magic happens if you swap the diode and the capacitor there. There's our capacitor and there's our diode like that.

**Dave Jones:** It has to be in that direction like that. This becomes what's called a Villard voltage doubler. And this is how it works. Now, as the blue waveform here, okay, we've got ground here.

**Dave Jones:** This is it's not ground, it's just a circuit reference point. So, G and that's at 0 volts. It's an AC signal we're getting out of the transformer. So, the voltage at point A there is this AC square wave.

**Dave Jones:** No, it doesn't have to be a sine wave. In fact, in most cases, it is actually a square wave, okay? And B, in the uh green waveform here, will be our output waveform.

**Dave Jones:** And as you can see it you end up with a voltage doubled signal. So, how does it do it? Well, it's actually very easy. Let me take you through step by step.

**Dave Jones:** Now, let's assume that our reference point here is 0 V and we're on the positive cycle here. So, this point here is 1 V. Now, we have to assume that the capacitor is already charged up and the circuit's reached that steady state.

**Dave Jones:** Let's not go into capacitor charging and uh all that sort of stuff. We've got no load, so the capacitor's going to charge pretty darn quick. Now, uh what we've got here 0 V 1 V at this point here, but the capacitor is already charged up.

**Dave Jones:** Just assume follow me here. It's already charged up to 1 V. Okay? So, we have 1 V across our capacitor there, like that. 1 V positive, negative. But, we've also got 1 V here as well.

**Dave Jones:** You add them up. 1 V plus 1 V relative to this point here gives us 2 V on our output. That's all there is to it. And that's why the green B here, the green signal, is at 2 V when the input signal here is on its positive peak at 1 V.

**Dave Jones:** We've just doubled our voltage. Brilliant. But, now what happens when our input signal, the blue waveform here, goes negative? Well, the voltage on this capacitor is always going to stay the same.

**Dave Jones:** Remember, there is no load here, okay? So, the charge is not going to drain off that capacitor. It's going to stay charged up to 1 V all the time.

**Dave Jones:** So, now we have minus 1 V on the input here cuz our blue waveform is now gone negative like this. And once again, we add up those two voltages.

**Dave Jones:** -1 V +1 V is 0 V. So, instead of 2 V we had before, it now drops down to 0 V on the output, and that's exactly what the green waveform here shows.

**Dave Jones:** It now drops down when this blue waveform transitions down, the green output waveform also transitions down to 0 V. So, it's converted You'll see that they're the same amplitude.

**Dave Jones:** The blue waveform has just been effectively shifted up like that, and that gives us our voltage doubled signal. It's all there is to it. It's real easy. Yes, it changes once you put a load on and the capacitor discharges and all that, but we're not going to cover that today.

**Dave Jones:** That's our voltage doubler. But, I know what you're thinking. This is not DC. It's AC. Look at it. This green waveform, it's Yeah, it's it's not going negative, but well, it's a pulse you know, it's a pulsating DC signal.

**Dave Jones:** Okay, yes, it does not go negative, so technically it's not AC, but that's not really, you know, proper flat DC. We want 2 V DC. So, how do you do it?

**Dave Jones:** Very easy. You just add in another diode like this, and another capacitor going down like that. And of course, that will You can think of it as a rectifier, same as what we showed right at the beginning, but it's actually like a peak detector.

**Dave Jones:** So, now the output waveform here, I'll show it in black down here, will now be like that, and we get our steady 2 V. Ignoring the diode voltage drop, cuz these things usually work at quite high voltages, and you can ignore the 0.6 V or whatever in your diode.

**Dave Jones:** In this case, we're just going to assume an ideal diode. So, that's all there is to it. We now get out 2 V DC and this circuit configuration here is no longer a Villard doubler, it becomes a Greinacher doubler.

**Dave Jones:** Now I actually didn't mention the operation of the diode here. I sort of left that out of my previous explanation and of course yes, it is needed. Doesn't work without it.

**Dave Jones:** So let's have a look. In the case when you've got 1 V here and you've got your positive waveform, then you've got 1 V and the two voltages add up and the diode's reverse biased because it's zero here and 2 V here.

**Dave Jones:** So the diode doesn't conduct, might as well not even be there. But on the negative cycle, of course, it is required. So when you go to minus 1 V down here, then this diode then allows this point to go to 0 V because then it's forward biased.

**Dave Jones:** So that's why that junction there can now drop down to 0 V. If you didn't have the diode there, wouldn't work. All right. So now we have our voltage doubler, but that's hardly high voltage DC generation.

**Dave Jones:** Where's our high voltage? We want to multiply this voltage up to high voltages. How do we do it? Well, we can take our standard Greinacher doubler or more commonly known as the Cockcroft Walton doubler or Cockcroft Walton multiplier, as we'll see why it's called a multiplier in a minute.

**Dave Jones:** And we can take this basic building block circuit and we can actually cascade this along to generate higher voltages. And that's why it's often referred to as a Cockcroft Walton cascade or sometimes a Greinacher cascade or even sometimes incorrectly a Villard cascade or something like that.

**Dave Jones:** Lots of interchangeable terms here. Let's not argue over it, but what we're going to do is take this doubler circuit which we've got here and I've just redrawn it.

**Dave Jones:** Nothing tricky going on here at all. There's the cap, there's the diode. I've just put it on an angle like that. There's the other diode, I've just put it going on another angle down like that.

**Dave Jones:** And there's the cap being returned to there. Exactly the same circuit. So, let's take a look at it. If we've got our 1 V peak here, I forgot to mention it's peak voltage I was dealing with here before.

**Dave Jones:** So, I've got our 1 V peak here. We've got our ground reference point down here. And as you saw before, we got our filtered 2 V DC at this point.

**Dave Jones:** So, this point here is 2 V DC. Now, what happens if we put an identical circuit in here like this, a duplicated, and then actually have that diode coming back like that, and then another diode going down here, you'll see that I've completely duplicated that circuit.

**Dave Jones:** I've added what's called another stage. So, that is a two-stage Cockcroft-Walton multiplier. And let's have a look what happens. We've got our 1 V peak signal here, and we've got our But now, instead of having our ground reference over here, 0 V, we now have shifted that reference point up to 2 V.

**Dave Jones:** So, now we're working on that same We've still got that same AC waveform here. We've still got that switching waveform there, and we've got a ground reference point here.

**Dave Jones:** So, it's like we've just shifted this across. We've got the exact same amplitude waveform here as what we had before, but now we've shifted that reference point. So, what do we end up here?

**Dave Jones:** We end up with a if I dot that along, we end up with another shifted waveform there, but it's shifted up by 2 V relative to this point back here.

**Dave Jones:** And that's important. It's going to be relative to this ground point. That'll come important later. And then, this point here will now be 4 V DC filtered out. That's a two-stage Cockcroft-Walton multiplier.

**Dave Jones:** All right, so we have two stages there and we went from 1 volt to 2 volts and 2 volts to 4 volts. So, we doubled and then we doubled again.

**Dave Jones:** What happens if we add another stage? Are we going to go from 4 volts to 8 volts? Well, let's see. Hmm. Let's add our cap in. And let's add our diode back here, of course.

**Dave Jones:** And then we'll put in our diode over here. Boom. And we're in like that. Now, what do we get at this point? Remember the AC level is still exactly the same as before.

**Dave Jones:** It was 1 volt here peak. Sorry, 2 volts peak to peak, 1 volt peak. It's also the same level here. Well, it's going to be exactly the same level again at this point except it's going to you you guessed it.

**Dave Jones:** It's going to be shifted up by another 2 volts. So, this point doesn't become 8 volts, unfortunately. It's not a doubler a doubler a doubler a doubler a doubler as you go on.

**Dave Jones:** No free lunch there, I'm afraid, folks. But, it does go up by two. So, it goes up by 2 4 6 and you guessed it if we keep adding stages 8 10 12 14 etc.

**Dave Jones:** etc. So, that is why it's called a Cockcroft-Walton multiplier and it's no longer a just a doubler a doubler a doubler a doubler multiplier. Remember that one. But, you can still generate really high voltages because let's say out of the transformer here, our transformer was giving out 1,000 volts, for example, then well, we get 2,000 4,000 6,000 8,000 10 kilovolts and so on.

**Dave Jones:** You can get quite high voltages based on your transformer tap. So, I've gone in and I've added an extra stage here, so we now have a four-stage Cockcroft-Walton multiplier, and we're getting 8 V DC out.

**Dave Jones:** But, 8 V DC relative to where? Well, it's not It's not just across this cap here, because that would be a differential voltage. You could use that if you really wanted to.

**Dave Jones:** Um you could use that as a reference point there, but really then you're only getting the 2 V out, or your 200 V or your 2 kV or what whatever your input voltage happens to be.

**Dave Jones:** So, the reference point you remember we said the reference point was always back at this point. So, that is where your reference point is. So, that now becomes your positive negative output voltage.

**Dave Jones:** That is your final DC output voltage from this multiplier, and you can see these points. So, basically, the top of this network here, these are all AC points like this, and these ones down the bottom here are all DC points.

**Dave Jones:** That's why you can get your 8 V or 8 kV or 800 kV out of this circuit. So, what do our components need to be rated at for this circuit?

**Dave Jones:** Well, if you look at these waveforms here, they're the exact same amplitude. It's the same amplitude AC signal as our input 1 V peak, 2 V peak-to-peak or whatever or RMS or whatever your input signal happens to be.

**Dave Jones:** So, these points along here are still the same voltage. So, the relative voltage across each capacitor and diode stage is still the same as your input voltage here. So, even though we're up to Let's say it's 8 kV.

**Dave Jones:** Let's say we're feeding in 1 kV out of the transformer, we're getting 8 kV out. You don't need 8 kV rated diodes and capacitors across here. You only need ones that are rated to the input voltage or two times the input voltage depends on how you look at it.

**Dave Jones:** So, these components in here have don't have to be rated at the full output voltage and that's a neat part of this Cockcroft-Walton multiplier. And if you look inside one that's actually built in a commercial product, that's why you'll find standard, you know, a thousand volt diodes or something inside something that can give out five or ten kilovolts because they don't need to be rated that high.

**Dave Jones:** Brilliant. So, let's take a look at the waveform view of this and what we're getting. I've got point one, two, three and four here and that corresponds to the waveforms over here, one, two, three, four.

**Dave Jones:** And as you saw here, we're getting By the way, I've changed it to two volts peak to peak input, not peak anymore, just to avoid confusion. So, two volts peak to peak is going to give us two volts DC out here.

**Dave Jones:** So, on the vertical axis here is just volts, two, four, six, eight volts and that represents the voltage peak. You can see that there, two volts peak to peak and the next waveform is shifted up by that two volts because you remember our reference point down here is two volts, so it's shifted up.

**Dave Jones:** And the next one is then shifted two volts above that, four, six, eight until the final waveform here, this red one, this one here is raised up at the reference level of six volts.

**Dave Jones:** But, you can see that the amplitude in there of each of these waveforms is still the same as your original two volts peak to peak input, but it's multiplied up like that, four stages multiplied four times.

**Dave Jones:** And of course, this is assuming ideal diodes, of course. If you have especially when you're operating down at eight volts, your diodes will have a huge effect. But, as I mentioned before, this is assuming that there's no load on here at all.

**Dave Jones:** So, these capacitors aren't really getting a chance to discharge at all, but there is a practical limit where to how long you can make this thing. You can't just make it arbitrarily long because there is going to be some AC resistance, some impedance in here due to the components.

**Dave Jones:** And then, of course, it depends on the switching frequency as well. So, when you're driving a load, uh for example, or you know, even a tiny little load, the frequency is going to matter, the value of the capacitors is going to matter, and effectively, you can get the output voltages um sagging because, let's say we had the waveform at at this point here, it's going to drop.

**Dave Jones:** It's not going to be a square wave like that. It's going to drop off like that. So, it's going to drop off, and then the reference and then the uh peak value that's fed through to the next stage is going to be lower than in this case with the peak value with no load.

**Dave Jones:** So, and then this one is going to roll off like that, and then this one's going to roll off like that, and you won't have as high a multiplication at each stage.

**Dave Jones:** So, when you start loading this thing down, then you're effectively going to lower your output voltage due to the nature of the discharge of the caps and the AC impedance, and it gets all complicated, and the response curve can actually end up looking something like that if you uh end up going too far.

**Dave Jones:** It can actually be, you know, higher back at this point than it was on your output, and all sorts of weird things can happen cuz you've got this huge uh cascaded network.

**Dave Jones:** But, we won't go into that. But, that's what can happen when you load these things down. So, these are primarily designed for essentially no load applications, electrostatic driving, and you know, uh stuff like that.

**Dave Jones:** So, when you put a load on, it can get a bit complicated. Whack this into the simulator, or even better, build it up for yourself, and see for yourself.

**Dave Jones:** Now, it would be remiss of me if I didn't mention a variation on this and how you can overcome some of the limitations due to the uh half-wave rectified nature of this standard Cockcroft-Walton multiplier that we've looked at.

**Dave Jones:** And you should be familiar with your full-wave and half-wave rectifiers in your linear power supplies as we showed back at the very start. This was only a half wave rectified and this one is a half wave rectified Cockcroft-Walton multiplier.

**Dave Jones:** But, just like your linear supply, you can do a full wave rectified version. You just mirror that circuit down and duplicate it like that. You have your extra tap on the transformer exactly like your linear supply.

**Dave Jones:** And just like that, it doubles the frequency so you get less sag on your capacitors and greater output you know, a capability to drive a load just like a linear supply.

**Dave Jones:** So, what we're going to do today is we're not going to build up that full one. We're just going to build up the half wave rectified one and have a very quick play with it.

**Dave Jones:** To the breadboard. Very, very quick build up of this just to show you some waveforms on the scope. My Dave CAD drawing here, we've got a four stage Cockcroft-Walton multiplier.

**Dave Jones:** I'm only feeding in 2 volts peak to peak and the good thing is at this low voltage we can see the effect of the diodes as well. So, now I've got that exact arrangement there built up here and I've got four channels probed at these points.

**Dave Jones:** Channel 1, Channel 2, Channel 3, Channel 4. Let's go to the oscilloscope. All right, now as you can see we've got a 1 kHz signal going in here. As I said, 2 volts peak to peak.

**Dave Jones:** As you can see there if I actually it's one all all four channels are 1 volt per division. If I move that up, you can actually see that it's there but we'll move it right down there.

**Dave Jones:** So, that's our 0 volt reference. That first graticule line there is our 0 volt reference. So, all of our channels will be ground referenced around that point or DC coupled, of course.

**Dave Jones:** So, as you can see we're not quite getting our 2 volts out of there. In fact, we're getting 1.67 volts. We've got some diode losses there. You see how it actually pulls it negative like that.

**Dave Jones:** That's that reverse bias diode in action which we saw on the circuit there. So, well, that's this one here when it comes into play. That's that one there when it comes into play.

**Dave Jones:** So, it pulls it a little bit low like that. Now, let's switch on channel two and see what we get. Now, the top voltage up there, which is effectively our DC output voltage, is two sorry three volts.

**Dave Jones:** So, you know, we expected to get four volts out of this thing. So, you can see how the diode voltages are already accumulating those diode losses. So, let's switch on channel three and that's that third point there.

**Dave Jones:** And we're now getting 4.43. And we'll turn on the fourth channel and we're getting 5.83. So, you can see that our diode losses have accumulated very quickly here. We expected two volts top voltage there and then four and then six and then eight.

**Dave Jones:** But we're only getting 5.83 volts out because each time you cascade through that stage, you're getting those diode losses accumulating until your top voltage there is you know, 5.83 instead of the eight you expect.

**Dave Jones:** Ah, death, taxes, and diode losses. Now, if we actually drop our input voltage down here instead of two volts peak-to-peak, let's drop it down to one volts peak-to-peak and we'll be able to see that our input then we'll be able to see the discharge on our caps.

**Dave Jones:** Watch this. It takes actually some time for those to drop down like that. And once again, if you look at the losses in there, it's absolutely huge. You know, we're expecting one volt, two volts, three volts, and four volts and we're only 2.19 volts.

**Dave Jones:** So, that discharge there was due to our scope input resistance. So, let's this is at 1 kilohertz by the way. So, let's jump that back up and you'll see it'll almost jump back up instantly.

**Dave Jones:** So, we'll go back to 2 volts peak to peak and bang, it jumps straight back up. Now, if we up that to 20 volts peak to peak input, then what do we get?

**Dave Jones:** Look, there it is, 19.7 volts, the top voltage of the first waveform, 38.7. We expected 40 there, so we're getting a couple of diode losses in there, and then 58 volts, and then 76.5.

**Dave Jones:** So, you know, even at you know, those sort of high voltages, the diode losses still add up. We're getting a 3 and 1/2 volts less than our expected 80 volts.

**Dave Jones:** So, that's our AC waveforms 1, 2, 3, and 4 there. What about our DC voltages down here? Well, of course, we are still on 20 volts peak to peak input, so I expect zero here, that's our reference point, and then 20, 40, 60, and then 80 volts.

**Dave Jones:** And what do we get? Well, we get a couple of diode losses there, zero, and then down here, there's our 19 volts because we're getting that extra diode loss in there, whereas you saw before it was 19.7 volts peak because we've got that now, that extra diode loss in there.

**Dave Jones:** So, that was 19.7, so we're getting our diode loss across here, and that one now becomes 19 volts, of course. And this one over here is 37.8, whereas we were getting 38.7 before.

**Dave Jones:** And then, once again, one diode volt less, we were 58 before, now we're 56.7, and it all adds up and accumulates. Now, finally, our output voltage is 75.4 volts there.

**Dave Jones:** But, as we said before, the voltage rating of these components doesn't need to be that full 80 volts. I've only got 63 volt caps in here, and these are only 75 volt rated diodes.

**Dave Jones:** But, let's look at the voltage across that final cap there, and it'll be that differential voltage. It should be 20 volts, but because of losses there, we're getting 19.1 volts difference there.

**Dave Jones:** Now, let's have a look what happens when we whack a load on on thing. You can see the maximum top output voltage there, 76.5 volts. I've got a 20 megaohm load on this thing.

**Dave Jones:** Well, let's drop it down to even 10 meg. Look at that, it's dropped down to 75.6. Let's go down to you know, 1 meg. You would think that's a pretty low load on the thing and it is.

**Dave Jones:** It's dropped down to 70 volts. Um peak output voltage, of course, that'll be like 69.5 or something DC output volts. And you know, it's it's just crazy. So, you can and that's a shorted output, by the way.

**Dave Jones:** There's a 100k. It's just, you know, absolutely incredible. So, there's a 0 ohm output. So, that has completely shorted the thing. If we go down, there we go. That's completely shorted.

**Dave Jones:** That's at 2 volts per division. And what happens if we adjust our input offset voltage of our AC waveform here? At the moment, and for for all the stuff I've just been doing, it's been at 0 volts offset.

**Dave Jones:** So, it hasn't actually gone negative. So, let's actually change that offset there and we'll see our waveform. There's our negative point and you'll notice that it doesn't change at all.

**Dave Jones:** You can see our offset changing over there. Well, waveform jumps around a bit, of course, but once it settles, not a problem. That's because our uh Cockcroft-Walton multiplier is all AC coupled.

**Dave Jones:** So, there you have it. Took a bit longer than normal. That's a definitely over a 20-minute video, I think. Oops, try and keep it a bit shorter next time.

**Dave Jones:** And speaking of next time, next Fundamental Friday, I think I'll do a similar thing, but with a DC, like when you want to multiply your voltage or double your voltage.

**Dave Jones:** So, we'll look at a DC and doubler next time. Hope you enjoyed it. If you like Fundamentals Friday, please give it a big thumbs up and as always, discuss it on the EVblog forum.

**Dave Jones:** Catch you next time.
