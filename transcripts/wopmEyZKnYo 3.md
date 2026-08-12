---
video_id: wopmEyZKnYo
title: EEVBlog #1116 - How to Remove Power Supply Ripple
url: https://www.youtube.com/watch?v=wopmEyZKnYo
source: youtube-asr
timestamps: {"0": 1, "1": 13, "2": 27, "3": 40, "4": 56, "5": 70, "6": 82, "7": 97, "8": 111, "9": 126, "10": 141, "11": 155, "12": 172, "13": 185, "14": 200, "15": 218, "16": 240, "17": 252, "18": 265, "19": 278, "20": 290, "21": 306, "22": 322, "23": 335, "24": 352, "25": 369, "26": 386, "27": 397, "28": 411, "29": 423, "30": 436, "31": 451, "32": 464, "33": 481, "34": 493, "35": 507, "36": 523, "37": 538, "38": 552, "39": 565, "40": 580, "41": 595, "42": 615, "43": 628, "44": 649, "45": 665, "46": 682, "47": 702, "48": 722, "49": 739, "50": 756, "51": 771, "52": 784, "53": 798, "54": 815, "55": 833, "56": 847, "57": 867, "58": 881, "59": 894, "60": 910, "61": 923, "62": 937, "63": 954, "64": 971, "65": 989, "66": 1000, "67": 1015, "68": 1028, "69": 1044, "70": 1062, "71": 1080, "72": 1095, "73": 1113, "74": 1129, "75": 1142, "76": 1156, "77": 1173, "78": 1188, "79": 1205, "80": 1219, "81": 1233, "82": 1244, "83": 1261, "84": 1274, "85": 1290, "86": 1308, "87": 1327, "88": 1342, "89": 1363, "90": 1383, "91": 1400, "92": 1417, "93": 1437, "94": 1454, "95": 1469, "96": 1488, "97": 1503, "98": 1516, "99": 1531, "100": 1549, "101": 1563, "102": 1579, "103": 1594}
---

**Dave Jones:** Hi, welcome to another fundamentals building block video. Today we're going to take a look at the capacitance multiplier and its name is a little bit weird, but we'll get into why it's called that shortly. And this is a bit

**Dave Jones:** of a follow-on to my previous video which I'll link in down below and at the end about the 7660 voltage inverter which we looked at which had we talked about the output ripple of such a voltage inverter. So

**Dave Jones:** let's take a look at ripple in like typical power supplies and how to get rid of it because using a capacitance multiplier is one of the ways you can do it and it's really effective. It's better than a voltage

**Dave Jones:** regulator. So let's take a look at a couple of scenarios where you might get ripple. Now you might have say a mains transformer like this. You might go into a bridge rectifier like this. Of course you're familiar with this and then you

**Dave Jones:** might have the an output capacitor like this of course and you're going to get some like ripple on there and this is very common for example if you're building an audio amplifier for example you want to generate you know positive

**Dave Jones:** and negative rails and you want them to be really clean especially for like class A amplifiers and stuff like that. So really you know you want to get rid of that sort of ripple and you can increase the capacitance and to do that

**Dave Jones:** but really you might want to add some post regulation to that. Another one might be well you've just got a DC to DC converter like this so you've got just a positive voltage in and you might have either a higher if it's a boost

**Dave Jones:** converter or a lower voltage output like this. So you know this is like V out and once again you might add some capacitance onto there but you're going to get some you know high frequency ripple out because these things

**Dave Jones:** typically might be you know tens of kilohertz hundreds of kilohertz even up into the megahertz region but you're going get, you know, tens of millivolts might be typical or even hundreds of millivolts ripple. Or as per the previous video, the classic 7660

**Dave Jones:** charge pump converter, which basically, you know, has some charge which switches in capacitors in there. And of course, you have an output capacitors like this. So, you've got V plus going in and you've got V out like this. But once

**Dave Jones:** again, it's going to have some ripple on it. And it can be quite high. It can be tens of millivolts might be reasonably low for a charge pump converter like this, for example. Or as we saw before, could even be a couple of

**Dave Jones:** hundred millivolts. You know, can really ruin your day. Especially if you're actually using this 7660 to go from say plus 5 volts to minus 5 volts, you're inverting that rail so that you can power your op-amp from plus 5 and minus

**Dave Jones:** 5 volts like that. Having a 5-volt rail is fine, but if you've got a couple of hundred millivolts or even tens of millivolts ripple, it's not very good ripple, but that's ripple, on your rail, then that can really ruin your day. So,

**Dave Jones:** you want to clean up ripple in, you know, any of these sorts of cases or, you know, other cases as well. How do you do that? Well, typically, you might just go, "Well, that's easy, Dave. I'll just whack in a

**Dave Jones:** regulator." So, you know, you might have your minus 5 volts here and you might say have a minus 4-volt regulator there. Just a low drop-out regulator. That'll be super clean, right? End your problems. Uh-uh. As it turns out, your voltage

**Dave Jones:** regulators, which are used everywhere to give you like a supposedly clean regulated, hence their name, regulated output voltage, are actually quite poor at uh attenuating large amounts of input ripple. Yes, they regulate well. It'll give you your precise minus 4 volts or

**Dave Jones:** 3.3 volts or whatever voltage you actually uh set your regulator to. But, if you've got tens or hundreds of millivolts of input ripple that you're trying to get rid of, LDOs can be a poor way to do it because the amount of

**Dave Jones:** attenuation of the ripple from input to output depends on uh not only the type of regulator, it depends on the input to output or the dropout voltage of the regulator. As you get lower, it can potentially get worse. Here's a graph uh

**Dave Jones:** which can show you a typical uh result of that. And it depends on the amount of current on the output as well. The higher the output current, the uh the less effective it the regulator's going to be at actually attenuating the

**Dave Jones:** ripple. If you don't believe me, if you don't believe it's actually a problem, let's go to the bench. I'll show you.

**Dave Jones:** Let's have a look at a typical LDO regulator. In this case, I've got a little uh SOT-23 Microchip MCP1700. It's a 3.3 volt low dropout regulator. I've just got an input filter cap, an input uh an output filter cap, and no

**Dave Jones:** load. But, let's actually see what happens if we add some ripple, like a lot of ripple, to the input here. Let's actually add uh 500 mV of ripple, right? Look what happens to the output. This is 10 mV per division. That ripple is

**Dave Jones:** coming through to the output like that. But, look what happens if we add a load. 270 ohm resistor on there. So, it's about uh what's that about? 13 mA or something like that. Look at the amount of ripple

**Dave Jones:** on here. Check that out. It's absolutely terrible. We're at 10 mV per division. 10 20 30 40 50 60 mV peak-to-peak for 500 mV ripple input, it's not doing a very good job, is it? And check it out,

**Dave Jones:** if we AC couple both channels, um the regulator's still regulating, by the way, still giving 3.3 V out, 50 mV per division, input ripple here at uh 330 odd mV, the output ripple in green is almost the same, there's virtually no

**Dave Jones:** attenuation of that ripple at all at 10 kHz. It It's hopeless. So, as I demonstrate on the bench, voltage regulators, which are otherwise great for typical applications, are really not very good at getting rid of high amounts of ripple, especially at higher

**Dave Jones:** frequencies and higher load, you just saw it. Even at like, you know, the milliamp level, tens of milliamp level, which is not a very big load. If you take the example of the op-amp that I gave before, well, they can take a

**Dave Jones:** couple of milliamps easily. So, uh just a generating a negative voltage rail for an op-amp, especially from a charge pump like this that can have, you know, tens or hundreds of millivolts of ripple, and you really want a low amount of ripple

**Dave Jones:** on your rail for whatever particular reason it is, and there's going to be a whole, you know, dozens of different scenarios. Low ripple is good. Low ripple's generally a good thing. You generally don't want it, but in some

**Dave Jones:** cases it's absolutely critical, and you want to get rid of it. The voltage regulator just doesn't do it. Enter the capacitance multiplier. So, let's just consider all these uh scenarios the same. We've just got a ripple and we want to get rid of it.

**Dave Jones:** What's the easiest way to get rid of uh ripple? Well, that's easy. You have a resistor and you have a capacitor like this. So, this is in and this is out. And depending on the value of the R and

**Dave Jones:** the C, the larger you make the capacitance, the more ripple rejection you're going to get. It's going to attenuate your ripple. Even if you take the case of like a low value resistor, lowish, like 100 ohms for example, even

**Dave Jones:** with a small amount of current on the output, 10 milliamps, you kind of get a 1-V drop across that resistor at 10 milliamps. That's not terrific, especially if you're, you know, you're generating a -5-V rail and you need, say, a negative

**Dave Jones:** uh you know, almost near negative uh 5-V rail on the output or even -4. You can only get a lousy 10 milliamps there, and even with that low value of resistor, the lower value of resistor you go, so

**Dave Jones:** as you decrease the resistor value, you have to increase your capacitance value, often to absurdly high values, uh to get the ripple rejection that you'll actually want. And, of course, you can add a second stage on here. For

**Dave Jones:** example, you can add another 100 R, you can add another one, and that works, but you've doubled your amount of uh voltage drop across there for a given current. And, as you can see, an a typical RC filter, even a multi-stage one, is not

**Dave Jones:** very effective at all for anything but ridiculously low currents, pretty much. So, one scenario where an RC filter like this or a two-stage RC filter is fine is if you've got, say, a uh pulse-width modulator and you're you want to

**Dave Jones:** actually uh generate a DC voltage from that. Well, this is typically going to go into an op-amp over here like this, and the input uh impedance of the op-amp is very high, so you're drawing no current, so it's not really a problem.

**Dave Jones:** So, you can use, you know, reasonable values of, you know, 10s uh you know, 10 microfarad, a couple of mic in there, and, you know, hundreds of ohms or 1K resistor or something like that, and you can filter out uh your pulse-width

**Dave Jones:** modulator down to like bugger-all values. That's fine. But, we want to actually do this for, you know, 10s of milliamps, hundreds of milliamps, even like in the case of like several amps for a big audio amplifier, for example.

**Dave Jones:** So, how do we do this? Yeah, we can lower our resistor value down to 1 ohm or something like that, but then the capacitor has to be so ridiculously high in value up to the like farads range that when you are driving large output

**Dave Jones:** currents that it really becomes completely impractical. So, what if we could multiply the capacitance? What if we could use a small capacitor value and somehow multiply it to make it appear bigger? Hmm, we can do that. Let's take a look.

**Dave Jones:** We can actually use the same trick you can use with voltage regulators when your regulator just doesn't have enough uh current capability, you can put in what's put called a series pass transistor. On top of that, I'm sure

**Dave Jones:** I've mentioned that in a video somewhere. So, we can do the same thing here. We can actually go like this and go into a transistor, NPN in this particular case, and have it like that, and bingo, this can be our V out like this, and we

**Dave Jones:** can get large amounts of current that bypass this resistor like this, and we can use a smaller value of capacitor here. And you might have noticed this as it is a your classic uh transistor building block circuit, the emitter

**Dave Jones:** follower, because the um output is on the emitter of the transistor like that. So, basically what that does is any voltage here is matched on the output here. It's an emitter follower, it just follows this value. And because the

**Dave Jones:** input current of the transistor like this is relatively small because a transistor has current gain, okay? You've got a small, smaller amount of current flowing through this resistor. It's not zero because it's a BJT. It's a bipolar junction transistor. It needs some base

**Dave Jones:** current, but it has a gain. That transistor has a multiplying gain that multiplies the base current to give you a higher collector current. And that's where the multiplier comes in here. As it turns out, this simple configuration, which is basically an RC filter with an

**Dave Jones:** emitter follower, is what's called a capacitance multiplier. And some people don't call it that. It's just a basically an RC filter, which is a building block of its own, combined with a series pass transistor like this, which is again a building block topology

**Dave Jones:** circuit of its own. So, you combine those two, and it in effect, the capacitance value C here, it gives you an effective capacitance value of not just the C, but C times beta, which is the gain of the

**Dave Jones:** transistor. Hence the name multiplier. So, the amount of ripple that you get on the output here is equivalent to a capacitance value, which is the value you use. Let's say it's 1 microfarad times the gain of the transistor, which

**Dave Jones:** might be 100. So, you have an equivalent of 100 microfarads here. That's not a good example because, hey, you can just whack 100 microfarads isn't very big. You could whack it in there. But you can see that when you get to large amounts

**Dave Jones:** of current, it can be a really huge benefit. So, with this capacitance multiplier, you can use relatively large values of resistor like this. You can use, you know, in the order of kiloohms, tens of kiloohms, and, you know,

**Dave Jones:** relatively reasonable values of capacitance. And again, you can actually put in a second stage there, too, if you're are really you know a multiple stage one as well. Now of course you've only got the capacitance times the beta

**Dave Jones:** of the transistor. If you use a single bulb bipolar junction transistor, they don't particularly have high current gain. So yes, you guessed it. You can actually use once again another classic building block which is the Darlington pair whoop like this.

**Dave Jones:** There you go. That that's a Darlington transistor. You can even use like two separate transistors cuz you might have your favorite big high current pass transistor here for example and just a smaller signal one over here to feed in

**Dave Jones:** the base. And your Darlington pair actually has a much higher gain. So your capacitance multiplier factor is even bigger. So you can effectively have you know many farads of capacitance here easily like you know a Darlington pair might have a gain of a thousand or

**Dave Jones:** something like that. You can really ramp things up in this sort of scenario. So you can really reduce your ripple to almost negligible levels like half a bee's dick. But hey, you still might not want to use a BJT cuz you don't have

**Dave Jones:** enough gain. You know you really want a small value of capacitance here and really this resistor can't be too high otherwise it can starve the base current even of a Darlington pair like this. So you know if you want really small values

**Dave Jones:** of capacitance large values of resistor, you guessed it. You can get rid of that and you can use a MOSFET like this. No wackers whatsoever. But using a MOSFET you might have like a larger voltage drop or that. It depends

**Dave Jones:** on what parts you're choosing and things like that. But it means because it's a MOSFET, there is no gate in this particular case. It's not a gate. It's not a base. It's a gate. You've got no uh gate current here. So this value of

**Dave Jones:** resistor can be as high as you want, and that means you can use really seriously low values of capacitance to get your attenuation. And just like a regular uh Darlington transistor, you could replace it with a uh Sziklai pair here, it's

**Dave Jones:** called, which is a compound transistor. And I won't go into the advantages and disadvantages between those. Maybe that could be um another video, but basically you could either use a single BJT, a Darlington configuration BJT, a Sziklai pair, or a

**Dave Jones:** uh MOSFET uh configuration pass transistor, but it works basically the same thing. The capacitance value gets multiplied by the transistor gain, and you can reduce your ripple to practically nothing. It's awesome. So, I know what you're thinking. Well, if this

**Dave Jones:** uh capacitance multiplier is so magic, why don't they just build reg- voltage regulators like this? Well, you might notice here that there's no regulator element. There's no feedback coming back. There's no feedback loop, which maintains a regulated voltage. So,

**Dave Jones:** this is not a regulator. The output voltage will change with the input voltage, and then it'll change with like temperature of the transistor and all, you know, sorts of things if you're dealing with high power and stuff like

**Dave Jones:** that. Basically, it's only of use if you want to get rid of ripple. It's not good for regulation. So, you could get could use this circuit to get rid of the ripple, and then use a voltage regulator on the output of that. That's a winner.

**Dave Jones:** But, this to use as a voltage regulator doesn't really work. It's not the job of a capacitance multiplier. So, that's pretty cool. Let's go have some fun on the bench. See what happens. Let's build up our capacitor multiplier.

**Dave Jones:** We've got a BD137 uh power here, fairly typical sort of, you know, old school uh power transistor, not particularly high gain, anywhere from like 25 up to 100-ish. I've actually measured it at 100 and we'll do that in a minute. But, uh there

**Dave Jones:** you go, just an NPN power transistor, a 1K uh resistor here for R and the C uh capacitance here is uh 470 microfarads and we've got our 270 ohm load. So, as before, we've got uh about 4. uh 2-ish

**Dave Jones:** volts, 4.3 volts uh DC in here with a 500 mV uh peak-to-peak 10 kHz signal superimposed on that or ripple. So, 10 kHz ripple at a fairly horrible 500 mV. And here's our output. It is supposed to be a green waveform, but it's got

**Dave Jones:** cursors on it. Um so, it looks yellow, but there's our output, nice and clean. Look at that. And if we actually uh go over here and switch it to AC and we go right down, oh. Oh, we have the 500

**Dave Jones:** microvolts per division. Look at that. It's still there, but wow, it's attenuated a lot. And that's just with a standard um you know, non-Darlington transistor. Winner, winner, chicken dinner. But, if we go back to our DC coupling, we're getting about a 3.3

**Dave Jones:** volts output there. You can see that there's roughly about 1 volt uh drop due to the uh pass transistor there. But, as I mentioned, it's not regulated. Uh so, if we change our offset voltage like this, look how our output changes like

**Dave Jones:** that. So, it is not a regulator. It's just to get rid of your ripple. And the voltage drop here is going to be dependent upon your uh load that you've got. It's going to be dependent upon your base resistor, the type of

**Dave Jones:** transistor that you've got, and the gain as well. So, it's you know, it just happens to be around about a volt drop in this particular case. And if we change our base resistor here or our filter resistor from uh 1K to 10K for

**Dave Jones:** example, we'll find There you go. We've now got a larger drop like that, but uh of course, our corresponding AC ripple should go right down like that. But, we're basically just uh down in the noise now. Yeah, there's a

**Dave Jones:** lot of noise due to all sorts of uh crap, but you can see that there's basically no ripple that we had there when we had our 1K resistor in there. There you go. There's our 1K resistor, and you can see that. So, it's a

**Dave Jones:** trade-off. As you increase uh the resistor R here, it starves the transistor of base current, therefore you get a larger uh voltage drop across the pass transistor, but you uh increase the uh ripple attenuation due to the just the RC filter ratio. And if we go

**Dave Jones:** down really low to 100 Hz ripple here, you see we're 2 mV per division. It's still not much ripple, but of course, you can see it actually coming through. So, once again, we're back at the uh 1K resistor there. So, if we really even

**Dave Jones:** wanted to knock out the uh 2 mV peak-to-peak ripple here at 100 Hz, then we could uh change our single transistor to a Darlington pair for example that would have higher gain, and then we could use a larger value of resistor for

**Dave Jones:** a given capacitance, and then filter it out that way. Or, we could increase the capacitor value, but we've already got a pretty large 470 microfarad in there. So, you wouldn't want to go much larger than that unless you had like a big

**Dave Jones:** audio amplifier, you had plenty of room, and all that sort of jazz. But, here's a little twist at the end. Let's actually confirm that we can actually get a capacitor multiplier, in quote marks. Does it actually multiply this capacitance here, C, by

**Dave Jones:** the gain of this transistor, which I'm going to say is 100, and I've actually measured it as 100. Well, let's have a look. The The cutoff frequency, the minus 3 dB frequency, you should know it's one of the basic uh formulas, 1

**Dave Jones:** over 2 pi RC. That's for your RC filter. So, for 1 K that we've got in circuit, and I've changed the capacitor now down to 100 nF here. So, for 1 K and 100 nF, our cutoff frequency should be 1.59

**Dave Jones:** kHz. So, it should be 3 dB down at that frequency. But, because we have a beta or gain of this transistor of 100, so we should actually get a cutoff frequency of 1 kHz and equivalent to 100 times

**Dave Jones:** that 10 nF or 10 microfarads. So, our cutoff frequency should be 15.9 Hz. Well, what do we get? Let's actually turn it on. Look, I've got my input signal here. My input peak-to-peak ripple is 470 mV. I've got it at 1.59

**Dave Jones:** kHz here. So, it should be way below that, right? Because if if it is actually a multiplier and it's equivalent to 10 microfarads, our cutoff frequency should be 15.9 Hz. So, we should get hardly any ripple at all.

**Dave Jones:** What do we get? Turn it on. What what what what about 310 mV or around about that 1.3 1.59 kHz frequency. Our minus 3 dB point. So, it's 470 times 0.707, which is about 330. Going to be near

**Dave Jones:** enough because we don't have much resolution in there. So, it's the end tolerance in the components, of course. The minus 3 dB frequency is not this expected uh multi-capacitor multiplier. It's exactly the same formula as the RC circuit.

**Dave Jones:** Why is it so? Well, as it turns out, this is why a lot of people don't like the name capacitor multiplier cuz it doesn't actually multiply this capacitance. It's not really 10 microfarads in terms of filtering like this. What it does is

**Dave Jones:** actually reduce the current through this resistor and hence the current that the capacitor has to smooth out by 100 times. So, instead of having the the whole load that we got there of 12 30 milliamps or whatever it is

**Dave Jones:** flowing through this resistor here, we've got 100 times less than that or about, you know, a couple of hundred microamps flowing through this resistor. But, in terms of calculating your cutoff frequency, the formula is actually the same as it is for a normal RC filter.

**Dave Jones:** It's just that the currents are reduced. The capacitor isn't actually multiplied, but I guess it depends on how you want to look at it. But, as far as calculating the frequency, no, it's exactly the same. So, capacitor multiplier,

**Dave Jones:** yeah, you either like that name or you don't. So, if we actually measure some of the voltages in here, we can actually find the gain of this transistor. Let's just, you know, not be too precise, but across our 270 ohm load resistor here,

**Dave Jones:** we've got about 3.4 volts or so. That's about, you know, 12 and 1/2 milliamps through this load. And that 12 and 1/2 milliamps is coming through the series pass transistor here. And if we measure across our 1K resistor there, it was

**Dave Jones:** about .12 volts or about 120 millivolts or thereabouts. So, therefore, 12 milliamps divided by 120, that gives us a gain of about 100 on our transistor here, which would be fairly typical. And of course, if we took put that into a

**Dave Jones:** Darlington pair, we might get, you know, an order of magnitude increase in that gain, so we might get 1,000 times instead of 100 times, for example. And of course, this is all going to be dependent upon the actual components

**Dave Jones:** used and you know, and the output load current as well. It's going to vary. Any data sheet for a power transistor will tell you that the gain varies with your collector but the good thing is is that we can just demonstrate that we can

**Dave Jones:** really reduce the ripple to, you know, basically negligible levels using this capacitor multiplier circuit or an RC filter with a series pass transistor, whatever you want to call it. And just for completeness, there is actually a variation in the capacitance multiplier

**Dave Jones:** that actually uses an op-amp instead of the series pass transistor. And it basically works the same way, but the thing with that is is that the op-amp can only drive a certain amount of current. There might be more stability

**Dave Jones:** like type issues and also you're going to be gain bandwidth limited as well. So, it's not a terrific solution. It's not designed for power applications like you get with a series pass transistor. So, I hope you found that video interesting. If you did,

**Dave Jones:** please give it a big thumbs up and as always, you can discuss in the comments down below or over on evblog.com. And thanks to all my patrons over on patreon.com, always linked in in the comments down below. They often get to see videos

**Dave Jones:** early before everyone else. Thanks. Catch you next time. Mhm.
