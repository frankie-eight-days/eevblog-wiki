---
video_id: wopmEyZKnYo
title: EEVBlog #1116 - How to Remove Power Supply Ripple
url: https://www.youtube.com/watch?v=wopmEyZKnYo
source: youtube-asr
timestamps: {"0": 1, "1": 11, "2": 25, "3": 38, "4": 47, "5": 73, "6": 84, "7": 101, "8": 121, "9": 136, "10": 146, "11": 155, "12": 172, "13": 183, "14": 195, "15": 209, "16": 235, "17": 257, "18": 267, "19": 280, "20": 292, "21": 306, "22": 317, "23": 329, "24": 341, "25": 373, "26": 388, "27": 397, "28": 417, "29": 425, "30": 436, "31": 449, "32": 456, "33": 475, "34": 484, "35": 503, "36": 517, "37": 540, "38": 552, "39": 567, "40": 580, "41": 597, "42": 612, "43": 626, "44": 658, "45": 671, "46": 690, "47": 702, "48": 724, "49": 739, "50": 756, "51": 771, "52": 780, "53": 792, "54": 809, "55": 822, "56": 835, "57": 847, "58": 867, "59": 881, "60": 890, "61": 899, "62": 917, "63": 930, "64": 943, "65": 959, "66": 976, "67": 989, "68": 1000, "69": 1013, "70": 1024, "71": 1041, "72": 1054, "73": 1070, "74": 1086, "75": 1095, "76": 1113, "77": 1129, "78": 1138, "79": 1148, "80": 1169, "81": 1184, "82": 1203, "83": 1215, "84": 1236, "85": 1246, "86": 1265, "87": 1278, "88": 1290, "89": 1309, "90": 1322, "91": 1337, "92": 1355, "93": 1370, "94": 1392, "95": 1409, "96": 1427, "97": 1447, "98": 1461, "99": 1477, "100": 1492, "101": 1509, "102": 1537, "103": 1551, "104": 1569, "105": 1583, "106": 1624}
---

**Dave Jones:** Hi, welcome to another fundamentals building block video. Today we're going to take a look at the capacitance multiplier and its name is a little bit weird, but we'll get into why it's called that shortly.

**Dave Jones:** And this is a bit of a follow-on to my previous video which I'll link in down below and at the end about the 7660 voltage inverter which we looked at which had we talked about the output ripple of such a voltage inverter.

**Dave Jones:** So let's take a look at ripple in like typical power supplies and how to get rid of it because using a capacitance multiplier is one of the ways you can do it and it's really effective.

**Dave Jones:** It's better than a voltage regulator. So let's take a look at a couple of scenarios where you might get ripple. Now you might have say a mains transformer like this.

**Dave Jones:** You might go into a bridge rectifier like this. Of course you're familiar with this and then you might have the an output capacitor like this of course and you're going to get some like ripple on there and this is very common for example if you're building an audio amplifier for example you want to generate you know positive and negative rails and you want them to be really clean especially for like

**Dave Jones:** class A amplifiers and stuff like that. So really you know you want to get rid of that sort of ripple and you can increase the capacitance and to do that but really you might want to add some post regulation to that.

**Dave Jones:** Another one might be well you've just got a DC to DC converter like this so you've got just a positive voltage in and you might have either a higher if it's a boost converter or a lower voltage output like this.

**Dave Jones:** So you know this is like V out and once again you might add some capacitance onto there but you're going to get some you know high frequency ripple out because these things typically might be you know tens of kilohertz hundreds of kilohertz even up into the megahertz region but you're going get, you know, tens of millivolts might be typical or even hundreds of millivolts ripple.

**Dave Jones:** Or as per the previous video, the classic 7660 charge pump converter, which basically, you know, has some charge which switches in capacitors in there. And of course, you have an output capacitors like this.

**Dave Jones:** So, you've got V plus going in and you've got V out like this. But once again, it's going to have some ripple on it. And it can be quite high.

**Dave Jones:** It can be tens of millivolts might be reasonably low for a charge pump converter like this, for example. Or as we saw before, could even be a couple of hundred millivolts.

**Dave Jones:** You know, can really ruin your day. Especially if you're actually using this 7660 to go from say plus 5 volts to minus 5 volts, you're inverting that rail so that you can power your op-amp from plus 5 and minus 5 volts like that.

**Dave Jones:** Having a 5-volt rail is fine, but if you've got a couple of hundred millivolts or even tens of millivolts ripple, it's not very good ripple, but that's ripple, on your rail, then that can really ruin your day.

**Dave Jones:** So, you want to clean up ripple in, you know, any of these sorts of cases or, you know, other cases as well. How do you do that? Well, typically, you might just go, "Well, that's easy, Dave.

**Dave Jones:** I'll just whack in a regulator." So, you know, you might have your minus 5 volts here and you might say have a minus 4-volt regulator there. Just a low drop-out regulator.

**Dave Jones:** That'll be super clean, right? End your problems. Uh-uh. As it turns out, your voltage regulators, which are used everywhere to give you like a supposedly clean regulated, hence their name, regulated output voltage, are actually quite poor at uh attenuating large amounts of input ripple.

**Dave Jones:** Yes, they regulate well. It'll give you your precise minus 4 volts or 3.3 volts or whatever voltage you actually uh set your regulator to. But, if you've got tens or hundreds of millivolts of input ripple that you're trying to get rid of, LDOs can be a poor way to do it because the amount of attenuation of the ripple from input to output depends on uh not only the type

**Dave Jones:** of regulator, it depends on the input to output or the dropout voltage of the regulator. As you get lower, it can potentially get worse. Here's a graph uh which can show you a typical uh result of that.

**Dave Jones:** And it depends on the amount of current on the output as well. The higher the output current, the uh the less effective it the regulator's going to be at actually attenuating the ripple.

**Dave Jones:** If you don't believe me, if you don't believe it's actually a problem, let's go to the bench. I'll show you. Let's have a look at a typical LDO regulator.

**Dave Jones:** In this case, I've got a little uh SOT-23 Microchip MCP1700. It's a 3.3 volt low dropout regulator. I've just got an input filter cap, an input uh an output filter cap, and no load.

**Dave Jones:** But, let's actually see what happens if we add some ripple, like a lot of ripple, to the input here. Let's actually add uh 500 mV of ripple, right? Look what happens to the output.

**Dave Jones:** This is 10 mV per division. That ripple is coming through to the output like that. But, look what happens if we add a load. 270 ohm resistor on there.

**Dave Jones:** So, it's about uh what's that about? 13 mA or something like that. Look at the amount of ripple on here. Check that out. It's absolutely terrible. We're at 10 mV per division.

**Dave Jones:** 10 20 30 40 50 60 mV peak-to-peak for 500 mV ripple input, it's not doing a very good job, is it? And check it out, if we AC couple both channels, um the regulator's still regulating, by the way, still giving 3.3 V out, 50 mV per division, input ripple here at uh 330 odd mV, the output ripple in green is almost the same, there's virtually no attenuation of that ripple at all at 10

**Dave Jones:** kHz. It It's hopeless. So, as I demonstrate on the bench, voltage regulators, which are otherwise great for typical applications, are really not very good at getting rid of high amounts of ripple, especially at higher frequencies and higher load, you just saw it.

**Dave Jones:** Even at like, you know, the milliamp level, tens of milliamp level, which is not a very big load. If you take the example of the op-amp that I gave before, well, they can take a couple of milliamps easily.

**Dave Jones:** So, uh just a generating a negative voltage rail for an op-amp, especially from a charge pump like this that can have, you know, tens or hundreds of millivolts of ripple, and you really want a low amount of ripple on your rail for whatever particular reason it is, and there's going to be a whole, you know, dozens of different scenarios.

**Dave Jones:** Low ripple is good. Low ripple's generally a good thing. You generally don't want it, but in some cases it's absolutely critical, and you want to get rid of it.

**Dave Jones:** The voltage regulator just doesn't do it. Enter the capacitance multiplier. So, let's just consider all these uh scenarios the same. We've just got a ripple and we want to get rid of it.

**Dave Jones:** What's the easiest way to get rid of uh ripple? Well, that's easy. You have a resistor and you have a capacitor like this. So, this is in and this is out.

**Dave Jones:** And depending on the value of the R and the C, the larger you make the capacitance, the more ripple rejection you're going to get. It's going to attenuate your ripple.

**Dave Jones:** Even if you take the case of like a low value resistor, lowish, like 100 ohms for example, even with a small amount of current on the output, 10 milliamps, you kind of get a 1-V drop across that resistor at 10 milliamps.

**Dave Jones:** That's not terrific, especially if you're, you know, you're generating a -5-V rail and you need, say, a negative uh you know, almost near negative uh 5-V rail on the output or even -4.

**Dave Jones:** You can only get a lousy 10 milliamps there, and even with that low value of resistor, the lower value of resistor you go, so as you decrease the resistor value, you have to increase your capacitance value, often to absurdly high values, uh to get the ripple rejection that you'll actually want.

**Dave Jones:** And, of course, you can add a second stage on here. For example, you can add another 100 R, you can add another one, and that works, but you've doubled your amount of uh voltage drop across there for a given current.

**Dave Jones:** And, as you can see, an a typical RC filter, even a multi-stage one, is not very effective at all for anything but ridiculously low currents, pretty much. So, one scenario where an RC filter like this or a two-stage RC filter is fine is if you've got, say, a uh pulse-width modulator and you're you want to actually uh generate a DC voltage from that.

**Dave Jones:** Well, this is typically going to go into an op-amp over here like this, and the input uh impedance of the op-amp is very high, so you're drawing no current, so it's not really a problem.

**Dave Jones:** So, you can use, you know, reasonable values of, you know, 10s uh you know, 10 microfarad, a couple of mic in there, and, you know, hundreds of ohms or 1K resistor or something like that, and you can filter out uh your pulse-width modulator down to like bugger-all values.

**Dave Jones:** That's fine. But, we want to actually do this for, you know, 10s of milliamps, hundreds of milliamps, even like in the case of like several amps for a big audio amplifier, for example.

**Dave Jones:** So, how do we do this? Yeah, we can lower our resistor value down to 1 ohm or something like that, but then the capacitor has to be so ridiculously high in value up to the like farads range that when you are driving large output currents that it really becomes completely impractical.

**Dave Jones:** So, what if we could multiply the capacitance? What if we could use a small capacitor value and somehow multiply it to make it appear bigger? Hmm, we can do that.

**Dave Jones:** Let's take a look. We can actually use the same trick you can use with voltage regulators when your regulator just doesn't have enough uh current capability, you can put in what's put called a series pass transistor.

**Dave Jones:** On top of that, I'm sure I've mentioned that in a video somewhere. So, we can do the same thing here. We can actually go like this and go into a transistor, NPN in this particular case, and have it like that, and bingo, this can be our V out like this, and we can get large amounts of current that bypass this resistor like this, and we can use a smaller value of capacitor

**Dave Jones:** here. And you might have noticed this as it is a your classic uh transistor building block circuit, the emitter follower, because the um output is on the emitter of the transistor like that.

**Dave Jones:** So, basically what that does is any voltage here is matched on the output here. It's an emitter follower, it just follows this value. And because the input current of the transistor like this is relatively small because a transistor has current gain, okay?

**Dave Jones:** You've got a small, smaller amount of current flowing through this resistor. It's not zero because it's a BJT. It's a bipolar junction transistor. It needs some base current, but it has a gain.

**Dave Jones:** That transistor has a multiplying gain that multiplies the base current to give you a higher collector current. And that's where the multiplier comes in here. As it turns out, this simple configuration, which is basically an RC filter with an emitter follower, is what's called a capacitance multiplier.

**Dave Jones:** And some people don't call it that. It's just a basically an RC filter, which is a building block of its own, combined with a series pass transistor like this, which is again a building block topology circuit of its own.

**Dave Jones:** So, you combine those two, and it in effect, the capacitance value C here, it gives you an effective capacitance value of not just the C, but C times beta, which is the gain of the transistor.

**Dave Jones:** Hence the name multiplier. So, the amount of ripple that you get on the output here is equivalent to a capacitance value, which is the value you use. Let's say it's 1 microfarad times the gain of the transistor, which might be 100.

**Dave Jones:** So, you have an equivalent of 100 microfarads here. That's not a good example because, hey, you can just whack 100 microfarads isn't very big. You could whack it in there.

**Dave Jones:** But you can see that when you get to large amounts of current, it can be a really huge benefit. So, with this capacitance multiplier, you can use relatively large values of resistor like this.

**Dave Jones:** You can use, you know, in the order of kiloohms, tens of kiloohms, and, you know, relatively reasonable values of capacitance. And again, you can actually put in a second stage there, too, if you're are really you know a multiple stage one as well.

**Dave Jones:** Now of course you've only got the capacitance times the beta of the transistor. If you use a single bulb bipolar junction transistor, they don't particularly have high current gain.

**Dave Jones:** So yes, you guessed it. You can actually use once again another classic building block which is the Darlington pair whoop like this. There you go. That that's a Darlington transistor.

**Dave Jones:** You can even use like two separate transistors cuz you might have your favorite big high current pass transistor here for example and just a smaller signal one over here to feed in the base.

**Dave Jones:** And your Darlington pair actually has a much higher gain. So your capacitance multiplier factor is even bigger. So you can effectively have you know many farads of capacitance here easily like you know a Darlington pair might have a gain of a thousand or something like that.

**Dave Jones:** You can really ramp things up in this sort of scenario. So you can really reduce your ripple to almost negligible levels like half a bee's dick. But hey, you still might not want to use a BJT cuz you don't have enough gain.

**Dave Jones:** You know you really want a small value of capacitance here and really this resistor can't be too high otherwise it can starve the base current even of a Darlington pair like this.

**Dave Jones:** So you know if you want really small values of capacitance large values of resistor, you guessed it. You can get rid of that and you can use a MOSFET like this.

**Dave Jones:** No wackers whatsoever. But using a MOSFET you might have like a larger voltage drop or that. It depends on what parts you're choosing and things like that. But it means because it's a MOSFET, there is no gate in this particular case.

**Dave Jones:** It's not a gate. It's not a base. It's a gate. You've got no uh gate current here. So this value of resistor can be as high as you want, and that means you can use really seriously low values of capacitance to get your attenuation.

**Dave Jones:** And just like a regular uh Darlington transistor, you could replace it with a uh Sziklai pair here, it's called, which is a compound transistor. And I won't go into the advantages and disadvantages between those.

**Dave Jones:** Maybe that could be um another video, but basically you could either use a single BJT, a Darlington configuration BJT, a Sziklai pair, or a uh MOSFET uh configuration pass transistor, but it works basically the same thing.

**Dave Jones:** The capacitance value gets multiplied by the transistor gain, and you can reduce your ripple to practically nothing. It's awesome. So, I know what you're thinking. Well, if this uh capacitance multiplier is so magic, why don't they just build reg- voltage regulators like this?

**Dave Jones:** Well, you might notice here that there's no regulator element. There's no feedback coming back. There's no feedback loop, which maintains a regulated voltage. So, this is not a regulator.

**Dave Jones:** The output voltage will change with the input voltage, and then it'll change with like temperature of the transistor and all, you know, sorts of things if you're dealing with high power and stuff like that.

**Dave Jones:** Basically, it's only of use if you want to get rid of ripple. It's not good for regulation. So, you could get could use this circuit to get rid of the ripple, and then use a voltage regulator on the output of that.

**Dave Jones:** That's a winner. But, this to use as a voltage regulator doesn't really work. It's not the job of a capacitance multiplier. So, that's pretty cool. Let's go have some fun on the bench.

**Dave Jones:** See what happens. Let's build up our capacitor multiplier. We've got a BD137 uh power here, fairly typical sort of, you know, old school uh power transistor, not particularly high gain, anywhere from like 25 up to 100-ish.

**Dave Jones:** I've actually measured it at 100 and we'll do that in a minute. But, uh there you go, just an NPN power transistor, a 1K uh resistor here for R and the C uh capacitance here is uh 470 microfarads and we've got our 270 ohm load.

**Dave Jones:** So, as before, we've got uh about 4. uh 2-ish volts, 4.3 volts uh DC in here with a 500 mV uh peak-to-peak 10 kHz signal superimposed on that or ripple.

**Dave Jones:** So, 10 kHz ripple at a fairly horrible 500 mV. And here's our output. It is supposed to be a green waveform, but it's got cursors on it. Um so, it looks yellow, but there's our output, nice and clean.

**Dave Jones:** Look at that. And if we actually uh go over here and switch it to AC and we go right down, oh. Oh, we have the 500 microvolts per division.

**Dave Jones:** Look at that. It's still there, but wow, it's attenuated a lot. And that's just with a standard um you know, non-Darlington transistor. Winner, winner, chicken dinner. But, if we go back to our DC coupling, we're getting about a 3.3 volts output there.

**Dave Jones:** You can see that there's roughly about 1 volt uh drop due to the uh pass transistor there. But, as I mentioned, it's not regulated. Uh so, if we change our offset voltage like this, look how our output changes like that.

**Dave Jones:** So, it is not a regulator. It's just to get rid of your ripple. And the voltage drop here is going to be dependent upon your uh load that you've got.

**Dave Jones:** It's going to be dependent upon your base resistor, the type of transistor that you've got, and the gain as well. So, it's you know, it just happens to be around about a volt drop in this particular case.

**Dave Jones:** And if we change our base resistor here or our filter resistor from uh 1K to 10K for example, we'll find There you go. We've now got a larger drop like that, but uh of course, our corresponding AC ripple should go right down like that.

**Dave Jones:** But, we're basically just uh down in the noise now. Yeah, there's a lot of noise due to all sorts of uh crap, but you can see that there's basically no ripple that we had there when we had our 1K resistor in there.

**Dave Jones:** There you go. There's our 1K resistor, and you can see that. So, it's a trade-off. As you increase uh the resistor R here, it starves the transistor of base current, therefore you get a larger uh voltage drop across the pass transistor, but you uh increase the uh ripple attenuation due to the just the RC filter ratio.

**Dave Jones:** And if we go down really low to 100 Hz ripple here, you see we're 2 mV per division. It's still not much ripple, but of course, you can see it actually coming through.

**Dave Jones:** So, once again, we're back at the uh 1K resistor there. So, if we really even wanted to knock out the uh 2 mV peak-to-peak ripple here at 100 Hz, then we could uh change our single transistor to a Darlington pair for example that would have higher gain, and then we could use a larger value of resistor for a given capacitance, and then filter it out that way.

**Dave Jones:** Or, we could increase the capacitor value, but we've already got a pretty large 470 microfarad in there. So, you wouldn't want to go much larger than that unless you had like a big audio amplifier, you had plenty of room, and all that sort of jazz.

**Dave Jones:** But, here's a little twist at the end. Let's actually confirm that we can actually get a capacitor multiplier, in quote marks. Does it actually multiply this capacitance here, C, by the gain of this transistor, which I'm going to say is 100, and I've actually measured it as 100.

**Dave Jones:** Well, let's have a look. The The cutoff frequency, the minus 3 dB frequency, you should know it's one of the basic uh formulas, 1 over 2 pi RC. That's for your RC filter.

**Dave Jones:** So, for 1 K that we've got in circuit, and I've changed the capacitor now down to 100 nF here. So, for 1 K and 100 nF, our cutoff frequency should be 1.59 kHz.

**Dave Jones:** So, it should be 3 dB down at that frequency. But, because we have a beta or gain of this transistor of 100, so we should actually get a cutoff frequency of 1 kHz and equivalent to 100 times that 10 nF or 10 microfarads.

**Dave Jones:** So, our cutoff frequency should be 15.9 Hz. Well, what do we get? Let's actually turn it on. Look, I've got my input signal here. My input peak-to-peak ripple is 470 mV.

**Dave Jones:** I've got it at 1.59 kHz here. So, it should be way below that, right? Because if if it is actually a multiplier and it's equivalent to 10 microfarads, our cutoff frequency should be 15.9 Hz.

**Dave Jones:** So, we should get hardly any ripple at all. What do we get? Turn it on. What what what what about 310 mV or around about that 1.3 1.59 kHz frequency.

**Dave Jones:** Our minus 3 dB point. So, it's 470 times 0.707, which is about 330. Going to be near enough because we don't have much resolution in there. So, it's the end tolerance in the components, of course.

**Dave Jones:** The minus 3 dB frequency is not this expected uh multi-capacitor multiplier. It's exactly the same formula as the RC circuit. Why is it so? Well, as it turns out, this is why a lot of people don't like the name capacitor multiplier cuz it doesn't actually multiply this capacitance.

**Dave Jones:** It's not really 10 microfarads in terms of filtering like this. What it does is actually reduce the current through this resistor and hence the current that the capacitor has to smooth out by 100 times.

**Dave Jones:** So, instead of having the the whole load that we got there of 12 30 milliamps or whatever it is flowing through this resistor here, we've got 100 times less than that or about, you know, a couple of hundred microamps flowing through this resistor.

**Dave Jones:** But, in terms of calculating your cutoff frequency, the formula is actually the same as it is for a normal RC filter. It's just that the currents are reduced. The capacitor isn't actually multiplied, but I guess it depends on how you want to look at it.

**Dave Jones:** But, as far as calculating the frequency, no, it's exactly the same. So, capacitor multiplier, yeah, you either like that name or you don't. So, if we actually measure some of the voltages in here, we can actually find the gain of this transistor.

**Dave Jones:** Let's just, you know, not be too precise, but across our 270 ohm load resistor here, we've got about 3.4 volts or so. That's about, you know, 12 and 1/2 milliamps through this load.

**Dave Jones:** And that 12 and 1/2 milliamps is coming through the series pass transistor here. And if we measure across our 1K resistor there, it was about .12 volts or about 120 millivolts or thereabouts.

**Dave Jones:** So, therefore, 12 milliamps divided by 120, that gives us a gain of about 100 on our transistor here, which would be fairly typical. And of course, if we took put that into a Darlington pair, we might get, you know, an order of magnitude increase in that gain, so we might get 1,000 times instead of 100 times, for example.

**Dave Jones:** And of course, this is all going to be dependent upon the actual components used and you know, and the output load current as well. It's going to vary. Any data sheet for a power transistor will tell you that the gain varies with your collector but the good thing is is that we can just demonstrate that we can really reduce the ripple to, you know, basically negligible levels using this

**Dave Jones:** capacitor multiplier circuit or an RC filter with a series pass transistor, whatever you want to call it. And just for completeness, there is actually a variation in the capacitance multiplier that actually uses an op-amp instead of the series pass transistor.

**Dave Jones:** And it basically works the same way, but the thing with that is is that the op-amp can only drive a certain amount of current. There might be more stability like type issues and also you're going to be gain bandwidth limited as well.

**Dave Jones:** So, it's not a terrific solution. It's not designed for power applications like you get with a series pass transistor. So, I hope you found that video interesting. If you did, please give it a big thumbs up and as always, you can discuss in the comments down below or over on evblog.com.

**Dave Jones:** And thanks to all my patrons over on patreon.com, always linked in in the comments down below. They often get to see videos early before everyone else. Thanks. Catch you next time.

**Dave Jones:** Mhm.
