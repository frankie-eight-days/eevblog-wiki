---
video_id: Uds-wLoaZmA
title: EEVblog 1474 - Can You Measure Capacitors IN Circuit?
url: https://www.youtube.com/watch?v=Uds-wLoaZmA
source: youtube-asr
timestamps: {"0": 0, "1": 19, "2": 34, "3": 44, "4": 54, "5": 63, "6": 74, "7": 84, "8": 97, "9": 110, "10": 121, "11": 136, "12": 148, "13": 160, "14": 171, "15": 181, "16": 194, "17": 209, "18": 228, "19": 241, "20": 254, "21": 266, "22": 284, "23": 291, "24": 299, "25": 309, "26": 325, "27": 343, "28": 358, "29": 374, "30": 385, "31": 396, "32": 412, "33": 424, "34": 438, "35": 453, "36": 468, "37": 488, "38": 496, "39": 511, "40": 520, "41": 532, "42": 547, "43": 557, "44": 569, "45": 582, "46": 593, "47": 607, "48": 618, "49": 627, "50": 642, "51": 660, "52": 670, "53": 686, "54": 699, "55": 710, "56": 718, "57": 729, "58": 740, "59": 749, "60": 763, "61": 778, "62": 786, "63": 809, "64": 821, "65": 832, "66": 856, "67": 866, "68": 878, "69": 890, "70": 900, "71": 910, "72": 926, "73": 941, "74": 955, "75": 967, "76": 977, "77": 987, "78": 998, "79": 1007, "80": 1023, "81": 1037, "82": 1047, "83": 1057, "84": 1071, "85": 1078, "86": 1088, "87": 1101, "88": 1108, "89": 1122, "90": 1132, "91": 1142, "92": 1156, "93": 1174, "94": 1189, "95": 1201, "96": 1214, "97": 1240, "98": 1255, "99": 1266, "100": 1285, "101": 1311, "102": 1321, "103": 1331, "104": 1348, "105": 1365, "106": 1383, "107": 1393}
---

**Dave Jones:** Hi, here's an interesting question for you. Can you actually use your LCR meter to measure capacitors in circuit? Because if you could, that'd be really handy, right? You can have like all these uh electrolytic uh caps and things, you can go in there and you'd be able to test them in circuit to troubleshooting a PCB.

**Dave Jones:** Cuz everyone knows one of the major failure modes for products, if you've seen a lot of my repair videos, a lot of them, especially like, you know, TV repairs or something like that, it'll just be like a blown cap in the power supply, a blown wet electrolytic uh capacitor.

**Dave Jones:** And not all of them can be identified with like, you know, it's burst out, it's leaking, or whatever, leaking capacitors. You have to actually uh test them. Is the capacitor that's good?

**Dave Jones:** Is the ESR or equivalent series resistance good? Well, can you actually measure them in circuit? And the answer is, surprisingly, yes, you can do a pretty decent job of it.

**Dave Jones:** But, as always, there's traps for young players. Let's take a look at it. Right, so let's just try and measure a capacitor in circuit. Got my uh LCR meter here.

**Dave Jones:** It's just set to auto uh mode, so it'll determine whether it's capacitor, inductor, resistive, whatever it is. Uh measuring at uh 1 kHz. That's a fairly nominal uh test frequency.

**Dave Jones:** And let's measure this big bad boy here, shall we? What do we get? Will it auto detect it? Oh, oh, resistance. Oh, it's 1 it's 1 ohm. It's 1 ohm.

**Dave Jones:** Oh, we've come a cropper. Well, let's actually force it into capacitance mode and try it again. There we go. That's more like it. Look at that. 1,000 mic. And what is the value of this capacitor?

**Dave Jones:** Sure enough, it's 1,000 mic. We measured that in circuit, no worries whatsoever. It's practically bang on. And we can measure the equivalent series resistance of that capacitor as well, cuz that's very important for high frequency ripple applications.

**Dave Jones:** You can come a cropper that way. So, let's put it in ESR mode here. Now, uh you measure that at 100 kHz if your meter can do 100 kHz cuz that's the uh general industry specification for ESR.

**Dave Jones:** Whoop. There we go. ESR mode. So, we have to short the leads together cuz these are like really long. So, I'm going to null that out there. And unfortunately, it looks like I can't null out in ESR mode on this Agilent meter.

**Dave Jones:** Anyway, let's let's let's call that an ohm. So, so we now measure that in circuit. There you go. 1.02 ohms, something like that. So, we're talking under 0.2 ohms.

**Dave Jones:** Um that sounds pretty good for a 1,000 mic cap ESR. We'll compare I'll whack up a data sheet here for a Rubicon, um which is the brand of this one, and that's probably going to be very close.

**Dave Jones:** Let's try another popular um LCR meter. This is the DE-5000. This is IET One, but uh you can get these for about 100 bucks. They're pretty darn good bang for buck.

**Dave Jones:** Let's give this one a go. Can it do it? Uh nope. It's coming at ya. But if you put that on manual range, there it is. Well, just uh yeah, pretty close to 1,000 mic there.

**Dave Jones:** Uh 0.91 ohms there. So, that's not too far off the other meter. But we did have to manual range it. So, at 1 kHz there, we measure pretty much bang on to 1,000 microfarads.

**Dave Jones:** Let's change the frequency. At 10 kHz, huh, 6 uh 700 nanofarads. What? 100 kHz? 1,600 nanofarads? And at 100 Hz, we're actually up to 1,200 microfarads. Hmm, what's going on?

**Dave Jones:** So, what does this actually measure if we desolder it uh from the circuit without any of the other uh components actually affecting it? Well, it's actually uh 855 microfarads at 100 Hz, and 120 Hz it's not going to be much different because that's the same frequency.

**Dave Jones:** 1 kHz, 820. And at 10 kHz, it's basically measuring well, that's not actually open. That's like basically short. That's what happens when you short circuit a on a capacitance meter.

**Dave Jones:** It measures OL like that. Otherwise, it'd be measuring like picofarads if it was actually open. And at 100 kHz, 1,700 nanofarads. So, it's all over the shop. Now, of course, this is a very large value cap, 1,000 microfarads.

**Dave Jones:** So, one of the things that you're supposed to know when you're using LCR meters like this is that for large value capacitors like this, you're supposed to use the lower frequency, like 100 Hz, 120 Hz.

**Dave Jones:** And that really gives us our capacitance value. So, if you were to give me this cap and say measure it, right, I'd put it on the 100 the lowest frequency mode, 100 Hz, and that will give us the greatest resolution, and we'll as we'll talk about different range resistors in a minute.

**Dave Jones:** But, yeah, that's going to give us the best value. And the ESR, 1.3 ohms. So, basically, our ESR was pretty much bang on to where we were where before.

**Dave Jones:** Of course, we have to subtract the 1 ohm of the leads here. So, you know, we did a fairly good job measuring the ESR of that capacitor in circuit.

**Dave Jones:** And we'll repeat the same measurement on the other LCR meter using the proper short lead measurement interface like this. So, you know, this is going to be this is going to be the real deal.

**Dave Jones:** At 100 Hz there, 848. 120 Hz, 843, basically the same. And at 1 kHz, as you can see, we've lost some resolution here. So, it's not 761 microfarads. And at 10 kHz, it's going nope, that is too big a capacitor.

**Dave Jones:** I can't measure that. Thank you very much. And it's going to tell us the same at 100 kHz as well. Hi, brief whiteboard interlude. I actually started shooting how an LCR meter works, and I ended up like shooting 20 minutes worth of footage.

**Dave Jones:** So, Uh, yeah, that was just made this video too long. So, at insert at this point, I would say go watch that previous video which I've already released on how LCR meters work, and it explains everything I'm going to be talking about later on in this video.

**Dave Jones:** So, you definitely should watch this. Link it down below and up there. So, if we actually go back to this board and measure uh what's actually on the board after we remove the cap, we can see uh well, at least the parameters of what uh we had actually in circuit surrounding that capacitor.

**Dave Jones:** And I don't know. I haven't like traced this out or anything. I've got no idea uh what it's doing, what it's a bulk for. Obviously, it's a bulk cap for, you know, some sort of uh supply or something like that.

**Dave Jones:** But, if we probe that, we can see well, it's it thought it was a 1 microfarad or something. Now, it's 4.8 ohms at 1 kHz. So, that's a you know, it's fairly low impedance around there.

**Dave Jones:** Now, at 100 kHz, it thinks it's an inductor. That is low impedance. So, that's why actually uh you know, we had a little bit of trouble uh with different meters actually measuring such a large value cap, and you can only do it at low frequencies.

**Dave Jones:** So, let's measure this cap in circuit, 470 microfarads. Um it's looks like it's same type and everything. So, let's measure that at 100 Hz in uh fixed capacitance mode, and 422 microfarads.

**Dave Jones:** So, we can actually measure that in circuit. But, one of the um extra tricks of measuring uh in circuit is that uh not only uh to manually um select the capacitance mode or the inductance mode if you're measuring inductors, but also swap the leads like that.

**Dave Jones:** And aha! Well, well, there we go. It still might have some residual charge in there. You might have to leave it. But, if you swap the polarity, you can get extra in circuit parameters that can actually change depending upon uh the polarity that you've got there.

**Dave Jones:** And you can see that's only 690 nanofarads. And there we go. Let's put it in that direction. You saw that it was 690 nanofarads before. It was nanofarads. So now we had to actually like clear that and do it again.

**Dave Jones:** Oh, I thought it was nano. Nano, nano, nope, nope, nope, nope. 690 nanofarads, what's going on? Right? It's playing silly buggers. It really doesn't like that at all. So we'll range this deliberately to microfarads like this so it's not going to get confused at all.

**Dave Jones:** Oh, yeah, 420 microfarads. And we can measure it that way as well. But you can see how if you let the meters auto range, well, you can really come a gutser.

**Dave Jones:** And it turns out for most large value capacitors, we can actually go around in circuit and actually measure them. Here's another thousand mic jobbie. There it is there. 1,100, no wackers.

**Dave Jones:** There you go. 979. We can do 10 microfarads. There it is there. It's practically bang on. Here's a 100 microfarads down here. See? We can actually get reasonably close.

**Dave Jones:** And I've tried this on dozens of different boards and hundreds of different types of caps in various circuits. I've got a whole bunch of them up there. And it generally just works pretty fine.

**Dave Jones:** But then you do again eventually get ones that are so low impedance around them that well, you can't measure diddly squat because it's basically a short circuit. If you measure resistance like that, there we go.

**Dave Jones:** Like 33 ohms. It's just like way too low impedance. Whatever is around that cap there, it's like on the output of this little transformer thing here. Like who knows what's going on there.

**Dave Jones:** But you know, there are some that you can't measure. But a good lot of caps in circuit, you can actually measure not too badly at all and measure the ESR as well.

**Dave Jones:** But of course, capacitors in circuit actually have active components usually around them. They could be voltage regulators, they can be like I mentioned before a this could be like the reset pin of a micro or something.

**Dave Jones:** You might have some like RC you know startup thing, you know, something like this or something like that and you want to measure that cap in circuit to see if it's still any good or gone bust and stuff like that.

**Dave Jones:** And inside the chip, you can have ESD protection diodes like this and you can have active parts. So effectively you've got like a diode and the power supply can act as a short circuit at a frequency like really low impedance.

**Dave Jones:** So effectively you can have like one or two diodes in parallel with the capacitor that you're trying to measure. And well, if you've got too high a test voltage, that's going to clip it.

**Dave Jones:** Let's go to the scope. So you should actually test this for your LCR meter. You should really get to know the output signal levels of your LCR meter here.

**Dave Jones:** So let's just do the Agilent jobby here. I've got my capacitance substitution box here and across it I've actually got two parallel diodes like that to simulate some active circuitry that you might get on a PCB.

**Dave Jones:** So I've got it disconnected here and you can see that we're getting like a selected 100 hertz there and we're getting two volts peak-to-peak. And of course that is more than enough to clamp it on these two silicon back-to-back diodes.

**Dave Jones:** And at the moment it thinks it's 15 nanofarads cuz I've got it going into the scope and everything. But don't worry about that. Okay? Let's plug it in and you can see that our signal levels dropped.

**Dave Jones:** You can see though it has not clipped. It's still a sine wave. So it's actually dropped to about 220 millivolts peak-to-peak which is not enough to clip these. I've got a 100 micro sorry a 10 microfarad capacitor in there.

**Dave Jones:** So with the 10 microfarad capacitor at 100 hertz with the particular range resistor that uh, the LCR meter has chosen, the signal level is not enough to actually turn on any active devices in circuit.

**Dave Jones:** So, if we're actually trying to measure a 10 microfarad cap in circuit, we're not going to be switching on at least any active elements, and that helps a lot with in-circuit measurements.

**Dave Jones:** And you'll notice that this is the same 150 220 mic. I can go up to the highest one I've got to 1,000 mic. There you go, we're down in the noise.

**Dave Jones:** We're getting some common mode noise on there because we're using a single um, ended scope here. And let's see if we can get this to clamp, right? At Well, there we go, it's starting to distort a little bit.

**Dave Jones:** So, at 1 V peak-to-peak there, you can see and that's at 15 microfarads. So, if we go down to 10, you can see it starts to get a little bit distorted.

**Dave Jones:** And now, as we go down, I'm now at 1 microfarad. We're trying to measure a 1 microfarad cap, and you can see that it is clamped. And I'm down to like 100 nanofarads there now.

**Dave Jones:** We've got absolutely no chance of measuring in this particular case a 100 nanofarad cap using this particular range resistor in circuit that has active diodes and other, you know, elements, active silicon elements in them.

**Dave Jones:** We've just got no chance of measuring that accurately. But large values of caps, yeah, because it drops all the way down. But you can't just like increase the frequency to do this cuz it actually gets worse, as I said, because of the large capacitor's value.

**Dave Jones:** And you'll see uh, it Well, at 120 Hz, you might have saw it drop a little bit. At 1 kHz, yep. Look at our signal level now. It's tiny tot.

**Dave Jones:** It's absolutely tiny tot. We're getting the common mode noise and everything, right? Pretty horrible stuff. And at 10 kHz, forget it. Because what you're doing is trying to measure a large value of capacitance at a large frequency, and you can't do that because it's your signal level is going to be too low even for any range resistor you try and select in there.

**Dave Jones:** Doesn't matter. But, at 100 Hz, of course, um we can measure that there's 220 micro Farads. I'm measuring that, no problems whatsoever. 33 micro Farads, you know, it's measuring 28 cuz this is these aren't exact values, right?

**Dave Jones:** But, we're measuring that in circuit with those diodes across it. It's only once we get to those low values, or we can go down even lower. I'm now in the nano Farad range.

**Dave Jones:** That's 1.5 nano Farads. And you can see that all of the That's 10 pico Farads, right? We we just cannot measure that, okay? Because the based on the frequency that we're using, the uh low and the low value capacitance, the the reactance that impedance is very high, and doesn't matter what range resistor we use, we just can't do it.

**Dave Jones:** It's only those large value caps. So, coincidentally though, this the caps you usually want to measure in circuit are like your large value electrolytics. And you can actually do it.

**Dave Jones:** It works fairly well. And I've repeated this with other LCR meters, and uh yeah, pretty much um all the ones that I've tested, they were able to give you a low enough uh signal level that actually doesn't clip.

**Dave Jones:** And you can experiment with your own LCR meter and some caps. And in this case, it starts clipping about oh 15 micro Farads. Let's call it 10 micro Farads at 100 Hz.

**Dave Jones:** Even though it's clipping, it can can actually still measure them. I'm going 2.2 micro Farads. Now it starts to get a bit off, right? It can't measure it anymore.

**Dave Jones:** 1 micro Farad, right? And it's measuring 7.2. It just na na It just can't do it. And right down at 100 nano Farads, it's showing 16 micro Farads, right?

**Dave Jones:** It's completely off. But, anything above 10 micro Farads, yeah, no worries. You can measure that in circuit with other active elements in there. But, that doesn't mean you won't get other, you know, low impedance stuff uh like, you know, transformers or other things which act as low impedances.

**Dave Jones:** And then that can ruin your day, but yeah, it actually works pretty well. And for this particular LCR meter, if I manually range it, there's really not many spots where it actually hits the sweet spot of being able to measure.

**Dave Jones:** There we go, it can measure it like this is 15 nanofarads here, measuring 15.8 there, but you can see that the waveform's a little bit distorted. Um yeah, it's not it's not good and it's over-ranged at that point where the actual signal level's low enough not to clip.

**Dave Jones:** And you'll see that we've got a clipped waveform here, 470 picofarads, it's way off. And if we actually range it there, you can see how it's different with the different ranges.

**Dave Jones:** And if we go down to the picofarad range, yeah, we can get values like 6.8 nanofarads that don't clip, but they're well over-range that it can't measure them on that range.

**Dave Jones:** But as I said, it works remarkably well for the high value caps. In this particular case, over 10 microfarads. But every LCR meter is going to be different depending on the range resistors and whatnot.

**Dave Jones:** So you've got to really test your own LCR meter to see what its limits are. And this IET meter, it goes down to like one microfarad before it starts to clip there.

**Dave Jones:** But anything above that, it's going to be super duper accurate in circuit. It just it the signal level's low enough for it not to clip. That's 150 mic, and there it is.

**Dave Jones:** Even though our signal level's very small, so we'll have to gain that up, but of course it it does that internally. So if I actually remove the diode here, this is 100 microfarads, and you'll see it has no impact at all on the measurement.

**Dave Jones:** It's not doing anything cuz it's not really conducting. But now, let's actually put a resistor in parallel and see what that does. Actually, I have to use this resistance box cuz this one only does high values in fixed and variable, I won't know what I've got.

**Dave Jones:** So, anyway, so there it is, right? So, there's there's a 100 microfarad capacitor. It's reading a bit low, okay? No worries. And if we disconnect the oscilloscope, that actually doesn't make any difference.

**Dave Jones:** So, that's really essentially no load on there, as you'd expect. Actually, let's change that frequency back to 100 Hz there. Okay? So, let's now put a 100 K resistor in parallel with that.

**Dave Jones:** You can see, it makes no difference whatsoever. Let's go to 10 K. Makes no difference whatsoever. Let's go down to 1 K. Makes no difference whatsoever. Let's go down to 100 ohms.

**Dave Jones:** Okay, it's starting to make a little bit of a difference. Let's go down to 10 ohms. Okay? And yeah, 10 ohms, we start to have a problem in circuit.

**Dave Jones:** But, that's 10 ohms. It's like really low impedance um stuff. You saw in previously, we measured like 30 ohms and stuff like that. Um so, it was obviously able to handle that.

**Dave Jones:** So, why does a parallel impedance, if it's a pure resistor, make no really no difference unless it's so low that it actually kills the amplitude down like this, okay?

**Dave Jones:** Um because which is a function of the uh it's going to be a function of uh with the range you're choosing, the range resistor in there in combination with this.

**Dave Jones:** It's because it's a pure resistor. Just like we talked about on the whiteboard in the other video, it's just effectively a uh parallel resistance across the capacitance. It doesn't really, because it's a pure resistor, it doesn't change the phase angle at all.

**Dave Jones:** And because uh there's not much else uh series resistance in there to actually get a voltage divider um type thing, the the source from the LCR meter is able to actually drive that capacitance.

**Dave Jones:** It doesn't You can have, you know, look, 100 ohms in parallel and still measure it exactly the same as 1 K or anything else. And you might think 100 ohms, no way it's going to measure that.

**Dave Jones:** But, yep, whack it in parallel, and that's why you can effectively measure like high-value capacitors at a low frequency like 100 hertz, in in circuit, relatively easily. It actually works fairly well.

**Dave Jones:** So, unless you've got like the waveform clipping or a really low impedance, like you know, tens of ohms or something like that. Once again, every LCR meter is going to be slightly different depending on what range resistor you've got in there, well, which is effectively the source impedance of your voltage source inside here, your AC voltage source.

**Dave Jones:** But, yeah, it's actually going to do a pretty decent job for large value caps. So, try it with your LCR meter and see what it's like. I've tried several LCR meters here, the ones that I've got, and they all, you know, work in a similar sort of way for measuring high value caps.

**Dave Jones:** It's like it's rather surprising. And I thought going into this video that I would actually find more of examples of in circuit where it actually clips, but I just couldn't find them.

**Dave Jones:** And this is why some LCR meters like this Global Specialties LCR 58 here, they have different voltage test levels. There it is there. See? 0.5 volts RMS, of course, that's RMS.

**Dave Jones:** So, that is will actually turn on diodes. But, we can actually switch that to a 0.1 volt RMS, so 100 millivolt test signal. And the reason, the specific reason that they have this functionality is so that diodes in circuit, any active elements inside chips, inside regulators or whatever, any active elements at all, bridge rectifiers, whatever it is, um, this won't turn them on.

**Dave Jones:** But, here's the funny thing. This video was originally not supposed to be a whiteboard tutorial on how LCR meters work. It was supposed to show you this exact thing where you can get in circuit things that screw up, active elements that screw up your in circuit capacitance measurements.

**Dave Jones:** And I thought I'd be able to find really good examples, but I've tried hundreds of capacitors across like dozens of different boards, and I can't actually find one example.

**Dave Jones:** Bloody Murphy's Law. Could not find one example where the voltage actually made a difference for large value capacitors. I can only get it to do it on the box if I use like lower value caps, but all large value electrolytics that I measured in all sorts of different boards, I couldn't get it to do it.

**Dave Jones:** But anyway, LCR meters, some do actually have a specific low voltage mode specifically to avoid uh active elements. So, there you go. I hope you found that video interesting even if it wasn't the video I originally intended uh to make, and I did waffle on the whiteboard there, but hopefully you now get a good understanding of how LCR meters work and some tips that you can use for measuring in circuit uh

**Dave Jones:** capacitors. Make sure you manually set the function, the capacitance of the inductance that you uh want to do uh so that you don't confuse the uh auto ranging algorithm or the auto uh selection algorithm in there.

**Dave Jones:** And for large values of capacitors, which is typically what you want to use in circuit, you measure them at uh the lowest frequency possible, 100 Hz or 120 Hz.

**Dave Jones:** And then also, um don't forget to swap your probes around as well just to uh make sure that you're getting the same reading in both directions, and then you can or at least similar reading in both directions, then you can be more confident uh that you're actually measuring an accurate capacitance value in circuit.

**Dave Jones:** And then, of course, if you're measuring the uh ESR, measure it at 100 uh kHz. You want to measure that at high frequency, and generally that works pretty well um in circuit, but just compensate for your test lead resistance cuz these long thin leads like this, they'll have like an ohm or something like that.

**Dave Jones:** And yeah, you want to take that out if you're measuring uh ESR. And then, get to know your LCR meter by measuring its signal level. And if you are measuring uh in circuit and your uh LCR meter does actually have the ability uh to set the voltage level, then you definitely want to set it on the lower level.

**Dave Jones:** Even though I could not find a single silly example of this thing. If I do, I'll celebrate and whack the video on the second channel. Anyway, I hope you enjoyed that.

**Dave Jones:** If you did and found it useful, please give it a big thumbs up. As always, discuss down below. Catch you next time.
