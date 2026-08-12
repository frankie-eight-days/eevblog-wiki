---
video_id: Uds-wLoaZmA
title: EEVblog 1474 - Can You Measure Capacitors IN Circuit?
url: https://www.youtube.com/watch?v=Uds-wLoaZmA
source: youtube-asr
---

**Dave Jones:** Hi, here's an interesting question for you. Can you actually use your LCR meter to measure capacitors in circuit? Because if you could, that'd be really handy, right? You can have like all these uh electrolytic uh caps and things, you can go in there and you'd be

**Dave Jones:** able to test them in circuit to troubleshooting a PCB. Cuz everyone knows one of the major failure modes for products, if you've seen a lot of my repair videos, a lot of them, especially like, you know, TV repairs or something

**Dave Jones:** like that, it'll just be like a blown cap in the power supply, a blown wet electrolytic uh capacitor. And not all of them can be identified with like, you know, it's burst out, it's leaking, or whatever, leaking capacitors. You have

**Dave Jones:** to actually uh test them. Is the capacitor that's good? Is the ESR or equivalent series resistance good? Well, can you actually measure them in circuit? And the answer is, surprisingly, yes, you can do a pretty decent job of it. But, as always,

**Dave Jones:** there's traps for young players. Let's take a look at it. Right, so let's just try and measure a capacitor in circuit. Got my uh LCR meter here. It's just set to auto uh mode, so it'll determine whether it's capacitor, inductor,

**Dave Jones:** resistive, whatever it is. Uh measuring at uh 1 kHz. That's a fairly nominal uh test frequency. And let's measure this big bad boy here, shall we? What do we get? Will it auto detect it? Oh, oh, resistance. Oh, it's 1 it's 1

**Dave Jones:** ohm. It's 1 ohm. Oh, we've come a cropper. Well, let's actually force it into capacitance mode and try it again. There we go. That's more like it. Look at that. 1,000 mic. And what is the value of this capacitor?

**Dave Jones:** Sure enough, it's 1,000 mic. We measured that in circuit, no worries whatsoever. It's practically bang on. And we can measure the equivalent series resistance of that capacitor as well, cuz that's very important for high frequency ripple applications. You can come a cropper

**Dave Jones:** that way. So, let's put it in ESR mode here. Now, uh you measure that at 100 kHz if your meter can do 100 kHz cuz that's the uh general industry specification for ESR. Whoop. There we go. ESR mode. So, we have to

**Dave Jones:** short the leads together cuz these are like really long. So, I'm going to null that out there. And unfortunately, it looks like I can't null out in ESR mode on this Agilent meter. Anyway, let's let's let's call that an ohm. So, so we

**Dave Jones:** now measure that in circuit. There you go. 1.02 ohms, something like that. So, we're talking under 0.2 ohms. Um that sounds pretty good for a 1,000 mic cap ESR. We'll compare I'll whack up a data sheet here for a Rubicon, um which is the

**Dave Jones:** brand of this one, and that's probably going to be very close. Let's try another popular um LCR meter. This is the DE-5000. This is IET One, but uh you can get these for about 100 bucks. They're pretty darn good bang for buck.

**Dave Jones:** Let's give this one a go. Can it do it? Uh nope. It's coming at ya. But if you put that on manual range, there it is. Well, just uh yeah, pretty close to 1,000 mic there. Uh 0.91 ohms there. So, that's not too far off

**Dave Jones:** the other meter. But we did have to manual range it. So, at 1 kHz there, we measure pretty much bang on to 1,000 microfarads. Let's change the frequency. At 10 kHz, huh, 6 uh 700 nanofarads. What? 100 kHz?

**Dave Jones:** 1,600 nanofarads? And at 100 Hz, we're actually up to 1,200 microfarads. Hmm, what's going on? So, what does this actually measure if we desolder it uh from the circuit without any of the other uh components actually affecting it? Well, it's actually uh 855

**Dave Jones:** microfarads at 100 Hz, and 120 Hz it's not going to be much different because that's the same frequency. 1 kHz, 820. And at 10 kHz, it's basically measuring well, that's not actually open. That's like basically short. That's what

**Dave Jones:** happens when you short circuit a on a capacitance meter. It measures OL like that. Otherwise, it'd be measuring like picofarads if it was actually open. And at 100 kHz, 1,700 nanofarads. So, it's all over the shop. Now, of course, this

**Dave Jones:** is a very large value cap, 1,000 microfarads. So, one of the things that you're supposed to know when you're using LCR meters like this is that for large value capacitors like this, you're supposed to use the lower frequency, like 100 Hz,

**Dave Jones:** 120 Hz. And that really gives us our capacitance value. So, if you were to give me this cap and say measure it, right, I'd put it on the 100 the lowest frequency mode, 100 Hz, and that will give us the greatest resolution, and

**Dave Jones:** we'll as we'll talk about different range resistors in a minute. But, yeah, that's going to give us the best value. And the ESR, 1.3 ohms. So, basically, our ESR was pretty much bang on to where we were where before. Of

**Dave Jones:** course, we have to subtract the 1 ohm of the leads here. So, you know, we did a fairly good job measuring the ESR of that capacitor in circuit. And we'll repeat the same measurement on the other LCR meter using the proper short lead

**Dave Jones:** measurement interface like this. So, you know, this is going to be this is going to be the real deal. At 100 Hz there, 848. 120 Hz, 843, basically the same. And at 1 kHz, as you can see, we've lost

**Dave Jones:** some resolution here. So, it's not 761 microfarads. And at 10 kHz, it's going nope, that is too big a capacitor. I can't measure that. Thank you very much. And it's going to tell us the same at 100 kHz as well. Hi, brief whiteboard

**Dave Jones:** interlude. I actually started shooting how an LCR meter works, and I ended up like shooting 20 minutes worth of footage. So, Uh, yeah, that was just made this video too long. So, at insert at this point, I would say go watch that

**Dave Jones:** previous video which I've already released on how LCR meters work, and it explains everything I'm going to be talking about later on in this video. So, you definitely should watch this. Link it down below and up there. So, if

**Dave Jones:** we actually go back to this board and measure uh what's actually on the board after we remove the cap, we can see uh well, at least the parameters of what uh we had actually in circuit surrounding that capacitor. And I don't know. I

**Dave Jones:** haven't like traced this out or anything. I've got no idea uh what it's doing, what it's a bulk for. Obviously, it's a bulk cap for, you know, some sort of uh supply or something like that. But, if we probe that, we can see well,

**Dave Jones:** it's it thought it was a 1 microfarad or something. Now, it's 4.8 ohms at 1 kHz. So, that's a you know, it's fairly low impedance around there. Now, at 100 kHz, it thinks it's an inductor. That is low

**Dave Jones:** impedance. So, that's why actually uh you know, we had a little bit of trouble uh with different meters actually measuring such a large value cap, and you can only do it at low frequencies. So, let's measure this cap in circuit,

**Dave Jones:** 470 microfarads. Um it's looks like it's same type and everything. So, let's measure that at 100 Hz in uh fixed capacitance mode, and 422 microfarads. So, we can actually measure that in circuit. But, one of the um extra tricks

**Dave Jones:** of measuring uh in circuit is that uh not only uh to manually um select the capacitance mode or the inductance mode if you're measuring inductors, but also swap the leads like that. And aha! Well, well, there we go. It still might have

**Dave Jones:** some residual charge in there. You might have to leave it. But, if you swap the polarity, you can get extra in circuit parameters that can actually change depending upon uh the polarity that you've got there. And you can see that's

**Dave Jones:** only 690 nanofarads. And there we go. Let's put it in that direction. You saw that it was 690 nanofarads before. It was nanofarads. So now we had to actually like clear that and do it again. Oh, I thought it was nano. Nano, nano,

**Dave Jones:** nope, nope, nope, nope. 690 nanofarads, what's going on? Right? It's playing silly buggers. It really doesn't like that at all. So we'll range this deliberately to microfarads like this so it's not going to get confused at all. Oh, yeah, 420 microfarads. And we can

**Dave Jones:** measure it that way as well. But you can see how if you let the meters auto range, well, you can really come a gutser. And it turns out for most large value capacitors, we can actually go around in circuit and actually measure

**Dave Jones:** them. Here's another thousand mic jobbie. There it is there. 1,100, no wackers. There you go. 979. We can do 10 microfarads. There it is there. It's practically bang on. Here's a 100 microfarads down here. See? We can actually get reasonably close. And I've

**Dave Jones:** tried this on dozens of different boards and hundreds of different types of caps in various circuits. I've got a whole bunch of them up there. And it generally just works pretty fine. But then you do again eventually get ones that are so

**Dave Jones:** low impedance around them that well, you can't measure diddly squat because it's basically a short circuit. If you measure resistance like that, there we go. Like 33 ohms. It's just like way too low impedance. Whatever is around that

**Dave Jones:** cap there, it's like on the output of this little transformer thing here. Like who knows what's going on there. But you know, there are some that you can't measure. But a good lot of caps in circuit, you can actually measure not

**Dave Jones:** too badly at all and measure the ESR as well. But of course, capacitors in circuit actually have active components usually around them. They could be voltage regulators, they can be like I mentioned before a this could be like

**Dave Jones:** the reset pin of a micro or something. You might have some like RC you know startup thing, you know, something like this or something like that and you want to measure that cap in circuit to see if it's still any good or gone bust and

**Dave Jones:** stuff like that. And inside the chip, you can have ESD protection diodes like this and you can have active parts. So effectively you've got like a diode and the power supply can act as a short circuit at a frequency like really low

**Dave Jones:** impedance. So effectively you can have like one or two diodes in parallel with the capacitor that you're trying to measure. And well, if you've got too high a test voltage, that's going to clip it. Let's go to the scope. So you

**Dave Jones:** should actually test this for your LCR meter. You should really get to know the output signal levels of your LCR meter here. So let's just do the Agilent jobby here. I've got my capacitance substitution box here and across it I've

**Dave Jones:** actually got two parallel diodes like that to simulate some active circuitry that you might get on a PCB. So I've got it disconnected here and you can see that we're getting like a selected 100 hertz there and we're getting two volts

**Dave Jones:** peak-to-peak. And of course that is more than enough to clamp it on these two silicon back-to-back diodes. And at the moment it thinks it's 15 nanofarads cuz I've got it going into the scope and everything. But don't worry about that. Okay? Let's plug it in

**Dave Jones:** and you can see that our signal levels dropped. You can see though it has not clipped. It's still a sine wave. So it's actually dropped to about 220 millivolts peak-to-peak which is not enough to clip these. I've got a 100

**Dave Jones:** micro sorry a 10 microfarad capacitor in there. So with the 10 microfarad capacitor at 100 hertz with the particular range resistor that uh, the LCR meter has chosen, the signal level is not enough to actually turn on any

**Dave Jones:** active devices in circuit. So, if we're actually trying to measure a 10 microfarad cap in circuit, we're not going to be switching on at least any active elements, and that helps a lot with in-circuit measurements. And you'll notice that this is the same 150 220

**Dave Jones:** mic. I can go up to the highest one I've got to 1,000 mic. There you go, we're down in the noise. We're getting some common mode noise on there because we're using a single um, ended scope here. And

**Dave Jones:** let's see if we can get this to clamp, right? At Well, there we go, it's starting to distort a little bit. So, at 1 V peak-to-peak there, you can see and that's at 15 microfarads. So, if we go down to 10,

**Dave Jones:** you can see it starts to get a little bit distorted. And now, as we go down, I'm now at 1 microfarad. We're trying to measure a 1 microfarad cap, and you can see that it is clamped. And I'm down to

**Dave Jones:** like 100 nanofarads there now. We've got absolutely no chance of measuring in this particular case a 100 nanofarad cap using this particular range resistor in circuit that has active diodes and other, you know, elements, active silicon elements in them. We've just got

**Dave Jones:** no chance of measuring that accurately. But large values of caps, yeah, because it drops all the way down. But you can't just like increase the frequency to do this cuz it actually gets worse, as I said, because of the large capacitor's

**Dave Jones:** value. And you'll see uh, it Well, at 120 Hz, you might have saw it drop a little bit. At 1 kHz, yep. Look at our signal level now. It's tiny tot. It's absolutely tiny tot. We're getting the common mode noise and everything, right?

**Dave Jones:** Pretty horrible stuff. And at 10 kHz, forget it. Because what you're doing is trying to measure a large value of capacitance at a large frequency, and you can't do that because it's your signal level is going to be too low even

**Dave Jones:** for any range resistor you try and select in there. Doesn't matter. But, at 100 Hz, of course, um we can measure that there's 220 micro Farads. I'm measuring that, no problems whatsoever. 33 micro Farads, you know, it's measuring 28 cuz this is these aren't

**Dave Jones:** exact values, right? But, we're measuring that in circuit with those diodes across it. It's only once we get to those low values, or we can go down even lower. I'm now in the nano Farad range. That's 1.5 nano Farads. And you

**Dave Jones:** can see that all of the That's 10 pico Farads, right? We we just cannot measure that, okay? Because the based on the frequency that we're using, the uh low and the low value capacitance, the the reactance that impedance is very

**Dave Jones:** high, and doesn't matter what range resistor we use, we just can't do it. It's only those large value caps. So, coincidentally though, this the caps you usually want to measure in circuit are like your large value electrolytics. And

**Dave Jones:** you can actually do it. It works fairly well. And I've repeated this with other LCR meters, and uh yeah, pretty much um all the ones that I've tested, they were able to give you a low enough uh signal

**Dave Jones:** level that actually doesn't clip. And you can experiment with your own LCR meter and some caps. And in this case, it starts clipping about oh 15 micro Farads. Let's call it 10 micro Farads at 100 Hz. Even though it's clipping, it

**Dave Jones:** can can actually still measure them. I'm going 2.2 micro Farads. Now it starts to get a bit off, right? It can't measure it anymore. 1 micro Farad, right? And it's measuring 7.2. It just na na It just can't do it. And right down at 100

**Dave Jones:** nano Farads, it's showing 16 micro Farads, right? It's completely off. But, anything above 10 micro Farads, yeah, no worries. You can measure that in circuit with other active elements in there. But, that doesn't mean you won't get other, you know, low impedance stuff uh

**Dave Jones:** like, you know, transformers or other things which act as low impedances. And then that can ruin your day, but yeah, it actually works pretty well. And for this particular LCR meter, if I manually range it, there's really not many spots

**Dave Jones:** where it actually hits the sweet spot of being able to measure. There we go, it can measure it like this is 15 nanofarads here, measuring 15.8 there, but you can see that the waveform's a little bit distorted. Um yeah, it's not

**Dave Jones:** it's not good and it's over-ranged at that point where the actual signal level's low enough not to clip. And you'll see that we've got a clipped waveform here, 470 picofarads, it's way off. And if we actually range it there,

**Dave Jones:** you can see how it's different with the different ranges. And if we go down to the picofarad range, yeah, we can get values like 6.8 nanofarads that don't clip, but they're well over-range that it can't measure them on that

**Dave Jones:** range. But as I said, it works remarkably well for the high value caps. In this particular case, over 10 microfarads. But every LCR meter is going to be different depending on the range resistors and whatnot. So you've got to really test your own LCR meter to

**Dave Jones:** see what its limits are. And this IET meter, it goes down to like one microfarad before it starts to clip there. But anything above that, it's going to be super duper accurate in circuit. It just it the signal level's

**Dave Jones:** low enough for it not to clip. That's 150 mic, and there it is. Even though our signal level's very small, so we'll have to gain that up, but of course it it does that internally. So if I actually remove the diode here, this is

**Dave Jones:** 100 microfarads, and you'll see it has no impact at all on the measurement. It's not doing anything cuz it's not really conducting. But now, let's actually put a resistor in parallel and see what that does. Actually, I have to

**Dave Jones:** use this resistance box cuz this one only does high values in fixed and variable, I won't know what I've got. So, anyway, so there it is, right? So, there's there's a 100 microfarad capacitor. It's reading a bit low, okay?

**Dave Jones:** No worries. And if we disconnect the oscilloscope, that actually doesn't make any difference. So, that's really essentially no load on there, as you'd expect. Actually, let's change that frequency back to 100 Hz there. Okay? So, let's now put a 100 K resistor in

**Dave Jones:** parallel with that. You can see, it makes no difference whatsoever. Let's go to 10 K. Makes no difference whatsoever. Let's go down to 1 K. Makes no difference whatsoever. Let's go down to 100 ohms. Okay, it's starting to make a little bit

**Dave Jones:** of a difference. Let's go down to 10 ohms. Okay? And yeah, 10 ohms, we start to have a problem in circuit. But, that's 10 ohms. It's like really low impedance um stuff. You saw in previously, we measured like 30 ohms and

**Dave Jones:** stuff like that. Um so, it was obviously able to handle that. So, why does a parallel impedance, if it's a pure resistor, make no really no difference unless it's so low that it actually kills the amplitude down like this,

**Dave Jones:** okay? Um because which is a function of the uh it's going to be a function of uh with the range you're choosing, the range resistor in there in combination with this. It's because it's a pure resistor. Just like we talked about on the

**Dave Jones:** whiteboard in the other video, it's just effectively a uh parallel resistance across the capacitance. It doesn't really, because it's a pure resistor, it doesn't change the phase angle at all. And because uh there's not much else uh series resistance in there to actually

**Dave Jones:** get a voltage divider um type thing, the the source from the LCR meter is able to actually drive that capacitance. It doesn't You can have, you know, look, 100 ohms in parallel and still measure it exactly the same as 1 K or anything

**Dave Jones:** else. And you might think 100 ohms, no way it's going to measure that. But, yep, whack it in parallel, and that's why you can effectively measure like high-value capacitors at a low frequency like 100 hertz, in in circuit,

**Dave Jones:** relatively easily. It actually works fairly well. So, unless you've got like the waveform clipping or a really low impedance, like you know, tens of ohms or something like that. Once again, every LCR meter is going to be slightly

**Dave Jones:** different depending on what range resistor you've got in there, well, which is effectively the source impedance of your voltage source inside here, your AC voltage source. But, yeah, it's actually going to do a pretty decent job for large value caps. So, try

**Dave Jones:** it with your LCR meter and see what it's like. I've tried several LCR meters here, the ones that I've got, and they all, you know, work in a similar sort of way for measuring high value caps. It's like it's rather surprising. And I

**Dave Jones:** thought going into this video that I would actually find more of examples of in circuit where it actually clips, but I just couldn't find them. And this is why some LCR meters like this Global Specialties LCR 58 here, they have

**Dave Jones:** different voltage test levels. There it is there. See? 0.5 volts RMS, of course, that's RMS. So, that is will actually turn on diodes. But, we can actually switch that to a 0.1 volt RMS, so 100 millivolt test signal. And the reason,

**Dave Jones:** the specific reason that they have this functionality is so that diodes in circuit, any active elements inside chips, inside regulators or whatever, any active elements at all, bridge rectifiers, whatever it is, um, this won't turn them on. But, here's the

**Dave Jones:** funny thing. This video was originally not supposed to be a whiteboard tutorial on how LCR meters work. It was supposed to show you this exact thing where you can get in circuit things that screw up, active elements that screw up your in

**Dave Jones:** circuit capacitance measurements. And I thought I'd be able to find really good examples, but I've tried hundreds of capacitors across like dozens of different boards, and I can't actually find one example. Bloody Murphy's Law. Could not find one example where the

**Dave Jones:** voltage actually made a difference for large value capacitors. I can only get it to do it on the box if I use like lower value caps, but all large value electrolytics that I measured in all sorts of different boards, I couldn't

**Dave Jones:** get it to do it. But anyway, LCR meters, some do actually have a specific low voltage mode specifically to avoid uh active elements. So, there you go. I hope you found that video interesting even if it wasn't the video I originally

**Dave Jones:** intended uh to make, and I did waffle on the whiteboard there, but hopefully you now get a good understanding of how LCR meters work and some tips that you can use for measuring in circuit uh capacitors. Make sure you manually set

**Dave Jones:** the function, the capacitance of the inductance that you uh want to do uh so that you don't confuse the uh auto ranging algorithm or the auto uh selection algorithm in there. And for large values of capacitors, which is

**Dave Jones:** typically what you want to use in circuit, you measure them at uh the lowest frequency possible, 100 Hz or 120 Hz. And then also, um don't forget to swap your probes around as well just to uh make sure that you're getting the

**Dave Jones:** same reading in both directions, and then you can or at least similar reading in both directions, then you can be more confident uh that you're actually measuring an accurate capacitance value in circuit. And then, of course, if you're measuring the uh ESR, measure it

**Dave Jones:** at 100 uh kHz. You want to measure that at high frequency, and generally that works pretty well um in circuit, but just compensate for your test lead resistance cuz these long thin leads like this, they'll have like an ohm or

**Dave Jones:** something like that. And yeah, you want to take that out if you're measuring uh ESR. And then, get to know your LCR meter by measuring its signal level. And if you are measuring uh in circuit and your uh LCR meter does actually have the

**Dave Jones:** ability uh to set the voltage level, then you definitely want to set it on the lower level. Even though I could not find a single silly example of this thing. If I do, I'll celebrate and whack the video on the

**Dave Jones:** second channel. Anyway, I hope you enjoyed that. If you did and found it useful, please give it a big thumbs up. As always, discuss down below. Catch you next time.
