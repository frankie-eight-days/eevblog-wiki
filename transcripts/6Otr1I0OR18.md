---
video_id: 6Otr1I0OR18
title: EEVblog #222 - Lab Power Supply Design - Part 2
url: https://www.youtube.com/watch?v=6Otr1I0OR18
source: youtube-asr
timestamps: {"0": 8, "1": 24, "2": 39, "3": 55, "4": 71, "5": 87, "6": 103, "7": 119, "8": 137, "9": 152, "10": 167, "11": 185, "12": 201, "13": 214, "14": 227, "15": 241, "16": 259, "17": 274, "18": 287, "19": 300, "20": 314, "21": 328, "22": 342, "23": 358, "24": 370, "25": 385, "26": 405, "27": 422, "28": 438, "29": 452, "30": 466, "31": 483, "32": 497, "33": 512, "34": 524, "35": 536, "36": 552, "37": 570, "38": 580, "39": 592, "40": 606, "41": 618, "42": 631, "43": 649, "44": 663, "45": 678, "46": 692, "47": 710, "48": 726, "49": 738, "50": 749, "51": 764, "52": 779, "53": 794, "54": 812, "55": 830, "56": 842, "57": 861, "58": 876, "59": 889, "60": 905, "61": 917, "62": 929, "63": 943, "64": 956, "65": 970, "66": 983, "67": 997, "68": 1011, "69": 1026, "70": 1038, "71": 1053, "72": 1068, "73": 1083, "74": 1100, "75": 1112, "76": 1128, "77": 1142, "78": 1158, "79": 1177, "80": 1191, "81": 1205, "82": 1219, "83": 1235, "84": 1246, "85": 1264, "86": 1278, "87": 1294, "88": 1308, "89": 1324, "90": 1337, "91": 1352, "92": 1370, "93": 1384, "94": 1397, "95": 1410, "96": 1422, "97": 1439, "98": 1456, "99": 1472, "100": 1486, "101": 1503, "102": 1520, "103": 1538, "104": 1554, "105": 1571, "106": 1590, "107": 1601, "108": 1616, "109": 1633, "110": 1648, "111": 1662, "112": 1677, "113": 1693, "114": 1702, "115": 1718, "116": 1734, "117": 1747, "118": 1763, "119": 1780, "120": 1798, "121": 1814, "122": 1829, "123": 1843, "124": 1855, "125": 1868, "126": 1885, "127": 1896, "128": 1913, "129": 1925, "130": 1936, "131": 1948, "132": 1961, "133": 1974, "134": 1987, "135": 2002, "136": 2013, "137": 2025, "138": 2036, "139": 2050, "140": 2064, "141": 2077, "142": 2094, "143": 2112, "144": 2124, "145": 2137, "146": 2149, "147": 2162, "148": 2176, "149": 2188, "150": 2202, "151": 2219, "152": 2234, "153": 2248, "154": 2263, "155": 2276}
---

**Dave Jones:** Now, let's take a look at the LT 3080 data sheet because we might find some practical considerations in here. In fact, I guarantee we'll find some practical considerations in here that we have to take care of in if we want to actually build this thing

**Dave Jones:** as opposed to just doing a conceptual type top-level design schematic that we've been doing up until now. And I really like this device because it does just exactly what we want. Now, let's have a look at some of the specs.

**Dave Jones:** Our output current up to 1.1 amp. So, I'm going to use the TO220 package of this that's available in many different packages, a DFN, a DPAK, and a SOT-223 version, which is really nice, or an MSOP package, but we'll use

**Dave Jones:** the TO220. It's a really neat 1% initial accuracy on the set current. That's not bad at all. And one of the neat things about this is that a single resistor programs the output voltage, although we're not going to use that today, but we might have to

**Dave Jones:** take aspects of that into account, as you'll see. But, it's really neat as like the unlike the LM317 where you got to do use two resistors to actually set the output voltage. This one only needs one. We'll go into why. Low output

**Dave Jones:** voltage noise is only 40 microvolts RMS through in that bandwidth. And it's got it supports input voltages up to 36 volts. Terrific. We're not going to go that high today, but hey, if you're into high voltage power supplies, it can do it. And the

**Dave Jones:** dropout voltage that will be at full load is only 350 millivolts, but we can check the curves on that one as you'll have to. Less than 1 millivolt load regulation. Line regulation's awesome. Now, one thing, minimum load current,

**Dave Jones:** there it is. 0.5 milliamps, we have to worry about that. And it's stable with 2.2 mic ceramic output capacitors. That's all we need to make this thing stable and then it's guaranteed over any loads you like. Terrific. And it's course it's got full

**Dave Jones:** back current limiting and over temperature, so it's pretty bulletproof just like the LM317. And there's the typical application which we've just spent a long time talking about. You've got a series pass transistor, the error amp connected straight through,

**Dave Jones:** but instead of having an internal voltage reference like the LM317, it's got an internal constant current generator which is actually 10 10 microamps. And it it tells you that over here. Here's the distribution graph and you'll notice, you know, we've been

**Dave Jones:** talking about bell curves recently. Well, there it is again. And that is 10 microamps constant current down through there. Now, although it doesn't tell you this in the data sheet, it basically it implies that because this is only 10 microamps, this constant

**Dave Jones:** current generator is pretty darn wimpy, right? You can force a voltage into the set pin just like you can on the LM317 and it's and it's going to be no big deal at all. But got to remember there's an extra 10

**Dave Jones:** microamps which has to flow out through there and we'll see that that matters later. And we'll just have a quick browse through the characteristic spec table here and see if there's anything that takes our fancy, shall we? Now, set

**Dave Jones:** pin current as we've said is 10 microamps. We don't necessarily need to know about the min max values of that because we we're driving it. We're not using an external external resistance. We're just driving that pin hard. So,

**Dave Jones:** really all we care about is that typical figure which we'll use later in a simple calculation. Now, let's take a look at the output offset voltage. And what this is is Vout minus Vset. What that means is the actual output voltage, the real

**Dave Jones:** output voltage minus what you've actually set. What you're you've set on your adjustment pot or what your software has set and what you're driving into that Vset pin in this case. Now, these specs are for a a control voltage of Vin of 1 V with an

**Dave Jones:** output current of 1 1 mA. Now, it could be your actual value may be plus minus 2 mV. Look at that. So, it may not be spot on to it if you put exactly 1 V on that Vset pin. If you're driving that

**Dave Jones:** Vsin at 1 V, then it could be 2 mV either side of that. Not a problem in the case of this power supply. 2 mV, that's neither here nor there. But, if you're designing precision really precision applications or

**Dave Jones:** precision power supplies, then this sort of this thing can matter. And you've got to take it into account. Now, you notice this dot next to it. There's it's actually wider than that over the full temperature range. It tells you up

**Dave Jones:** here. Bingo. Little trap. The other spec there is only for an ambient temperature of 25° C. And remember, this is not the ambient temperature. It's going to be the junction temperature of the device itself. So, it's dissipating all that

**Dave Jones:** power and your heat sink's gone up to 60°. Well, your your lab might be 25°, but your heat sink and your device is at 60°. So, just be aware. And you'll notice that there's two different specs here depending on the different packages. And

**Dave Jones:** the reason that they have these is because the die used, the silicon die, is going to be different in these smaller packages as they have a larger die used in these larger power type packages. And the spec gets worse, plus

**Dave Jones:** minus 5 mV. Man, terrible. Or plus minus 6 millivolts over temperature. Who cares for our case, but you know, you got to be aware of that sort of stuff. Thing the output offset voltage is fairly critical for is when you

**Dave Jones:** parallel devices up and this is how you going to increase the output current cuz this device is only rated to just over an amp. What if you want 2 amps or 3 amps or something like that? Well, you

**Dave Jones:** can parallel devices up like this and all you've got to do is include a series ballast resistor like this and you can do these do this to any similar type of voltage regulator as well. Now, there is an alternative device, the

**Dave Jones:** LT1080-1. I think it's a bit rarer to get, but it actually includes a built-in ballast resistor in there and the output offset voltage, a small one like the plus minus 2 millivolts you see here quoted for this one or at least that nominal at

**Dave Jones:** at room temp. It's if it's tight like plus minus 2 millivolts, it means that your output ballast resistor only has to be very small. In this case, they recommend 10 milliohms output resistance and it's still going to share you know, 80 to 90%

**Dave Jones:** of the current between two devices or even better than that typically and so you don't even have to actually buy a resistor for that. It's good enough to actually use a PCB trace for that. And they actually tell you to they actually

**Dave Jones:** recommend that a 10 10 mil width or a 10 thou width trace on a PCB, 20 thou width trace typical, 1 oz or 2 oz copper. 1 oz is your normal weight copper or if you're designing heavy duty power supplies, you

**Dave Jones:** might have ordered a 2 oz copper PCB, but you can get your ballast resistors. You don't actually have to buy one. There's no bill of extra bill of materials on them, and cost. You just include it with a PCB trace. Brilliant.

**Dave Jones:** And as long as that value is high enough, then you can share the current between the two devices adequately without one device heating up much more than the other device. But, you can't make it too high cuz then you get a

**Dave Jones:** voltage drop. And in this case, let's say you got a 2-A output, and our two ballast resistors are 10 mΩ. Well, it's a total of 5 mΩ cuz they're actually in parallel. So, essentially what they are. So, that's 5 mΩ

**Dave Jones:** ballast resistance or output resistance there at 2 A is going to give us a 10 mV drop on the output. And that's not too bad. At 1 V, that's only 1%. So, the neat thing about parallel devices like

**Dave Jones:** this is that you can actually leave one of the footprints unpopulated or multiple footprints on your board if you're designing a power supply like this and you want to save a bit of cost to begin with or you're designing a kit

**Dave Jones:** or something. Save a bit of cost, you only have one device. Or if you want two or three or four or more, you can actually parallel them up and you can just solder in the individual devices as you need them. Load regulation is going

**Dave Jones:** to be excellent from 1 mA up to it's fully specified from 1 mA up to 1 A, no problems. Line regulation up to 25 V input, not a problem at one it's specified at 1 mA load. Oh, no, don't need to worry about that.

**Dave Jones:** Minimum load current. Now, here we go. Minimum load current, very, very important. We need to take that maximum figure there, 500 microamps or half a milliamp, as our minimum load current. If we don't do that, it doesn't tell you what's going

**Dave Jones:** to happen. There's a couple of notes here, which we'll read, but it doesn't tell you. Just assume that's not going to be stable or it's going to have a larger dropout voltage, or uh sorry, it's not going to allow you to go down

**Dave Jones:** to a as low a voltage as it could, or whatever. There's a whole bunch of different uh reasons not to If you don't meet that, a whole bunch of bad things can happen and ruin your day. So, we

**Dave Jones:** have to somehow um get a minimum load current over uh our uh minimum load current of 1/2 a mA over our entire voltage range. And it's only specified at a VIN range of 10 V. If you go higher, it needs 1 mA

**Dave Jones:** minimum. And there it is, note three, minimum load current, yada yada, quiescent current. Uh it's the minimum load current required to maintain regulation. If you don't meet it, it ain't going to regulate, and that defeats the whole purpose of a power

**Dave Jones:** supply. Now, the dropout voltage of this part is interesting cuz it specifies it in two different ways. There's V control pin dropout voltage and VIN dropout voltage. So, if you look back to the circuit here, it's got VIN and V

**Dave Jones:** control. Normally, you tie these two together, and we will in our application here today, but uh if you want a really low dropout voltage of this part, like a low input voltage, and a minimum input uh dropout voltage between the input and

**Dave Jones:** the output, but you happen to have in your circuit somewhere a higher control voltage, then you can take advantage of that and get a lower dropout voltage from into out by tying V control up to a higher voltage up there like that. But,

**Dave Jones:** we're going to tie them together. And also, not all parts uh have the extra V control pin. Some of the Some of Some of the packages actually um will tie those two pins internally. So, you don't have it actually have it available. So, um

**Dave Jones:** we need to take the worst-case version of that because we're tying them together, which will be There it is, 1.2 V, or at full That's at 100 mA, so at full current, which you have to take into account it could be as bad as 1.6.

**Dave Jones:** So, our input voltage has to be at least 1.6 V above our output voltage. And that's this voltage here, not over here. So, if our output voltage is 5 V here, we need to have at least 6.6 V or 1.6 V

**Dave Jones:** higher here. And if we are using a 1-ohm resistor and we're drawing an amp, you're going to get an extra volt. And so, you need 7.6 V here minimum for a 5-V output. And the current limit here or a maximum output voltage,

**Dave Jones:** typical 1.4 amps. But, you might Well, you might be able to push it that far, and you probably can. But, when you're designing and you want to set your maximum figure, the lowest one here is what you're going to use as opposed to

**Dave Jones:** say the minimum load current, you'd use the highest value. In this case, you want to be conservative and use the lowest. So, depending on the parameter, you either have to choose the maximum value or the minimum value. We'll choose

**Dave Jones:** 1.1 amps. That's what our circuit will be capable of. Now, as far as the output noise goes, most linear regulators are pretty darn good, and this one's no exception. 40 microvolts RMS for the error amplifier noise. Now, if we have a look at the

**Dave Jones:** error amplifier here, all of the noise, assuming that the input voltage is perfect and there's nothing No noise coming in there, then all of the noise is going to be generated by the internal current source and the error amplifier.

**Dave Jones:** So, that's basically all the noise internally is going to be that 40 microvolts RMS. So, even if we feed force in an absolutely perfect voltage onto here with no noise at all, we're still going to get 40 microvolts or

**Dave Jones:** thereabouts worst case RS output noise. But, as you can see, the set, because this is a direct feedback loop and whatever voltage you put on here comes out here, any noise that you put on this set pin is going to come out here as

**Dave Jones:** well within limits of bandwidth and all sorts of other things like that. So, really the noise limit will depend on this. Now, if you're driving your circuit with a pot like this and you've got this fed to you know a voltage reference or

**Dave Jones:** something like that say a 2.5 volt voltage reference you know a really quiet low noise voltage reference then your noise is going to and you're driving that pin directly then the noise is going to be pretty good. But, if

**Dave Jones:** you're doing a PWM signal and you're feeding that through your RC filter like that and then you're driving that with a buffer obviously and you're driving that into the set pin like that then um your noise then any noise that you

**Dave Jones:** haven't filtered out here any noise on there is going to make it through to here and it's going to make it through to your output. So, filtering if you're using microcontroller control filtering of your pulse width modulation modulated signal is important. But, you

**Dave Jones:** can really up these values. You can you know up them as high as you want to really you know absolutely slaughter any noise and just kill it dead. It's not that hard. You just need to choose high values. And if you want to care about

**Dave Jones:** the ripple rejection then you have to figure out what 75 dB is for your various input ripple which is specified at half a volt peak to peak. If you're powering this thing from a transformer and a bridge rectifier and

**Dave Jones:** a and a filter cap you're going to get 100 you know this is a full wave one cuz it's double 60 hertz so it's 120 hertz ripple there it's specified. You know that's pretty good and you can calculate

**Dave Jones:** that if you're using um, a you know a noisy input and you've got a ripple, but if you're using say a battery input or something like that, then you don't have to worry about that at all. But if you actually want

**Dave Jones:** some real figures, you can plug those in for 75 uh dB there at the nominal uh half volt peak-to-peak and that's going to give you an output uh noise of less than 100 microvolts. So, 100 microvolts doesn't uh sound like much and it's not.

**Dave Jones:** It's you know, it's down in the noise. Although, once again, if you've got a really uh low noise, very high spec uh power supply system, then it could matter. But just for a lab power supply like us, more than good enough. Order of

**Dave Jones:** magnitude good enough. But that's only at 120 Hz. That's for ripple AC mains ripple. If you're powering this thing from an AC mains input. What if you um got a a switching frequency of 10 kHz or 1 MHz? Well, where would you get that

**Dave Jones:** from? Well, if you're powering this regulator, if this regulator is being uh the LT3080 is being powered from a DC-to-DC converter, well, that's going to have a switching frequency and that's going to have output noise and a very

**Dave Jones:** high efficiency uh switching regulator might be up near a megahertz or something like that. And in that case, look at the uh look at the rejection there at 1 MHz. It's down to only 20 dB. That's a huge

**Dave Jones:** drop from 75 dB at 120 Hz. And if we calculate what 20 dB is, just like 75 dB there, is you know the formula, you've seen it before. dB equals 20 log. In this case, it's going to be uh V out or

**Dave Jones:** our noise or ripple output voltage over our V in, in this case, which is uh given as uh 0.5 V. And if you calculate that and if you change the formula around because dB's already known and you work out what your

**Dave Jones:** uh output uh ripple or output noise is going to be, then it's going to be 1/10 of your input noise. So, if your input is 0.5 V, you're going to get 50 mV output noise. So, it's not down in the

**Dave Jones:** microvolts region anymore. It's in the tens of millivolts. And that can ruin your day if you're designing precision apps, and you've got and you haven't adequately filtered your input noise like that. Now, if you were actually using this in its traditional

**Dave Jones:** configuration with the external resistor, and you were relying upon the uh pin uh set current at 10 microamps, you'll see that that's only nominal at 25° C. When you actually go up or even down in temperature like this, it does

**Dave Jones:** vary a bit. You know, if you go right up to your 100° and go up an extra 50 uh 50 nanovolts. Woohoo! But, that could be significant. And remember, when you're looking at these curves, don't fall into the trap of thinking that your product

**Dave Jones:** is only operating at ambient temperature at 25°. It's not. This is the junction temperature of the actual uh device itself, the die temperature. And because this is a power supply and it's dissipating power, that junction temperature could easily get up to 100°,

**Dave Jones:** depending on how you do your thermal design. So, if you're designing really precision uh power supplies, you need to take that sort of thing or any power system that dissipates power, you got to take these thermal graphs into

**Dave Jones:** consideration. And the offset voltage, once again, doesn't really matter for our application because it um this is versus load current. So, the output offset voltage in millivolts is actually going to uh drop based on the output load current. So, if the output load

**Dave Jones:** current's 1 amp here at ambient uh temperature or C, it tells you here TG junction, the temperature of the junction, not just the ambient uh temperature, because ambient temperature makes no difference to it at all. All it cares about is temperature. Anyway,

**Dave Jones:** you're almost going to be uh 0.5 millivolts offset there. And if your junction's up to 125, 0.75 millivolts uh offset. And if you're designing precision applications, that could matter. Take it into consideration. Now, looking at the minimum load current,

**Dave Jones:** which is quite important as we said, cuz we have to take this into consideration, then at a input to output differential of 1.5 volts, then you know, your your minimum load current only needs to be 0.3 milliamps, then. But when it does rises

**Dave Jones:** your input to output differential rises to a much bigger voltage, then your minimum load current needs to be higher. So, you might put in half a milliamp. That would be That's what it tells you in the top level specs, but you might say

**Dave Jones:** design it for a milliamp just to be on the safe side if you didn't care about wasting that extra half a milliamp. Now, this load transient response here, we do want to consider this because this tells us our typical performance when you

**Dave Jones:** change your load like this. Here's the output load current in hundreds of milliamps. So, we're doing a 200 milliamp jump in the load current. It goes from 50 milliamps up to 250 milliamps and then back down. And you

**Dave Jones:** can see what the output voltage, how it deviates because these regulators aren't perfect, okay? They have a transient response when your output current suddenly changes. And this is the transient response you'll get if you've only got 2.2 microfarad ceramic cap. You

**Dave Jones:** can expect it to change by 50 millivolts output. You can expect it to droop down like that and then they recover like that. And if you use a 10 microfarad ceramic, you can see that it takes a bit

**Dave Jones:** longer to recover and the droop isn't Well, in this case, the rise isn't quite as much. So, there you go. But that's at a nominal 1.5 volts output, but the greater the your output the greater the output capacitance on your regulator, the

**Dave Jones:** better your load transient response can become. But just be careful. You don't want to put a massive amount of capacitance on the output of a constant current power supply like this, because that capacitor can store a lot of

**Dave Jones:** energy. You know, if you put in a "I'm going to put in a big 2200 microfarad capacitor. That'll really, you know, give it lots of transient performance." Well, there's a downside to doing that, and that's when this thing switches into constant

**Dave Jones:** current mode, then can't react, cuz it's still got all this energy in the cap that can get dumped high current into your load, because it's not current regulating. So, you want to keep in a lab power supply like this with a

**Dave Jones:** constant current circuit like this, you want to keep the output output capacitance as low as possible just to ensure stability in your regulator. Although, I guess you could say, "Oh, okay, you might determine transient response is a more

**Dave Jones:** important thing than uh switch it over into constant current." But, generally, you kind of want to keep that thing the output capacitance low. So, we're probably going to want it just, you know, the same value or uh twice the

**Dave Jones:** recommended uh value just to be on the safe side that it recommends for stability of this particular regulator. And just for a bit of completeness there, you've also got line transient response. Generally, not important in a power supply design like this, because

**Dave Jones:** our input um basically, this means uh line transient line means your input voltage coming into your voltage regulator as opposed to uh load transient response, which is changing uh current on your um output. So, um input line transient, you

**Dave Jones:** the the power supply that's powering your power supply is generally going to be pretty stable, and it's not going to change by this sort of current like this uh, this sort of voltage. This is in this case it's got a 3-V step in your

**Dave Jones:** input voltage to your voltage regulator. You can see the that the output gives a, uh, droop like that of 25 mV. So, THERE YOU GO. NOT IMPORTANT, BUT JUST THOUGHT I'd mention it. Another thing to consider is the turn-on

**Dave Jones:** response of the, uh, regulator. And that's what happens to the output voltage here when your input voltage ramps up. You don't want it to overshoot by a massive amount cuz that can damage your circuitry if it's already hooked up

**Dave Jones:** to the power supply. So, this one looks pretty good. It looks pretty well-behaved. And we'll actually, uh, when we build this thing up, we'll actually check that. Now, here's an interesting graph. You don't normally, uh, see these. Uh, this is a bit rare.

**Dave Jones:** It's the residual output voltage with less than minimum load. So, it's basically telling you, um, implying how this device is going to perform if you don't meet that minimum load current requirement. And you know that one of the big banner specs, one of the big

**Dave Jones:** highlight banner specs of this, um, of this voltage regulator is how low the output voltage can go. Uh, it can go all the way down to zero. That's what it claims, but only with a minimum amount of output current. And that's what it's,

**Dave Jones:** um, basically, uh, saying. And this is your test resistance here. So, as your test resistance gets lower and the output current increases, then, let's say you've got a test resistance up here of 2k, okay? Let's say 5 V.

**Dave Jones:** There we go. 5 V at 2k. And if you've got a 2k output resistor with an input voltage of 5 V here, when it's trying to set, you see the set pin is, uh, grounded here. So, it's trying to set

**Dave Jones:** 0-V output, but you don't get 0 V. You get There you go. 0.55 V or something like that. Terrible. So, you really So, that big banner spec that it shows on the front page here, you know, it claims, "Oh, output adjustable down to 0

**Dave Jones:** V." Fantastic. Yeah, here's the devil in the detail. It only goes down to 0 V if you've got a 0 ohm output resistor, effectively. So, if you've got a 1 K output resistor nominal on there, you're only going to be able to go down to

**Dave Jones:** about, you know, 0.25 V or something like that. And herein lies the trap. How do we get a minimum output load current here on an adjustable power supply? Because if we just Well, sure, we could just stick a resistor here on our

**Dave Jones:** circuit down to ground, make that 1 K, no worries. We're easily going to meet our minimum load requirement. Let's say it's 1 V. It even at 1 V, we're going to get 1 mA. That easily meets our minimum load

**Dave Jones:** requirement of 1/2 mA. And we can probably go down to 0.5 V output. We're going to get 0.5 mA. Great. Okay, that sounds like a good solution. BUT WHAT IF OUR OUTPUT voltage is 10 V? Well, we've got 10 mA. And we're effectively

**Dave Jones:** pissing away 10 mA there just on that output resistor. And aha, here's the thing to consider. If you're trying to get milliamp accuracy over here with your with your constant current setting. Let's say you want to adjust it in 1

**Dave Jones:** mA steps, you know, your input voltage down here 0 to 1 V. You want to adjust it with your micro in 1 mA steps. Well, jeez, you've got 10 mA at 10 V. In fact, you've got an output

**Dave Jones:** current which flow which is a which changes based on the output voltage. So, your microcontroller over here that's driving all this thing will have to be smart and know well, it knows what the output voltage is cuz it's setting it

**Dave Jones:** through here. So, it will have to know that loads 1K and then take that into account and then compensate by driving instead of driving let's say you wanted to you know, adjust this to 5 milli amps and that'll be 5 millivolts. Well, if

**Dave Jones:** you're drawing an extra 10 milliamps out of here, you've got to actually make because you want 5 milliamps only 5 milliamps max to go into your load. So, you know that you're going to at say at 10 volts output, you're going

**Dave Jones:** to have 10 volts coming out of 10 volts on here 10 milliamps going down here, you have to actually compensate and set this one to 15 millivolts to know and it gets really it all gets quite ugly. So, if

**Dave Jones:** you use a fixed resistor like that, I that's not a very elegant solution. I don't necessarily like it on a variable power supply like this. And by the way, another little trick, if you're if you really care about how much current this

**Dave Jones:** whole thing draws, you might want to add an LED in there like that and that could be your power LED and so you get a two for the price of one. So, instead of wasting your LED current just lighting up a power LED, you might

**Dave Jones:** get it from the output and you can use it as an output LED or something like that. But then it doesn't work down at low voltages if this thing goes down to you know, 0 volts or 1 volt or you know,

**Dave Jones:** it it's ugly. Anyway, uh we're going to I reckon we need to find a better solution than the fixed resistor. So, what do we use for that output current? Well, I can't think of anything better than the classic LM334

**Dave Jones:** constant current source. It's a single resistor. It's available in TO-92 package. It's not bad. Goes down to very low currents up to 10 milliamps maximum. and so I reckon we set this sucker for a value of 1 milliamp.

**Dave Jones:** Now the LM334 has been around since pretty much the dawn of time. It's one of those classic devices that is still incredibly useful today. It operates from 1 volt up to 40 volts. It's got good current regulation. You can program

**Dave Jones:** a current from 1 microamp to 10 milliamps, two terminal operation, 3% initial accuracy if you actually care about the you know the absolute accuracy. We're not that fussy at all. It could be 10%. We couldn't care less. And and it's available in you know a

**Dave Jones:** TO-92 package or an SO8. So very very usable, cheap as chips. I love it. One thing we do care about though is its minimum operating voltage of typically 0.9 volts up to 1 milliamp. So we plan to operate it at 1 milliamp or

**Dave Jones:** thereabouts or half a milliamp maybe. So it's unfortunately it's only going to operate down to about 0.9 maybe 0.8. But hey, 0.8 milliamp if we can get our power supply to operate down to say 0.8 or 0.9 volts that's a lot better than the 1.25

**Dave Jones:** volts you might get on an LM317. And then you can go right down to zero if you want. But then you're reliant upon the load actually providing the minimum current. Then you can't use like a high impedance load actually below 0.9

**Dave Jones:** volts or or 0.8 volts or thereabouts. So 0.8 volts is a nice figure. 0.9 is nice because for a power supply to go down to is because the a single cell battery a single cell you know D cell or double A

**Dave Jones:** alkaline or something like that will be basically pretty much dead from 0.9 down to 0.8 volts or 0.9 volts. So a power supply that can go down that low is pretty good. And it can go lower but depend on the load. Hey, that's good

**Dave Jones:** enough for me. I like it. And it's really easy to use. It's only a three-pin device and you just have a single set resistor like this, voltage in like this, I set. This will be connected to ground down here and this

**Dave Jones:** will be our output voltage and we'll have a single resistor like this. At what value does it need to be? Well, you can go through all sorts of uh formulas and take into account bias currents and stuff like that, but uh we can cheat and

**Dave Jones:** uh do the um Look at this uh graph here. Uh set 68 ohms and bingo, look, it settles at 1 milliamp. So, it looks like it's 68 ohms will give us 1 milliamp. 68 ohms is a nice E12 resistor value. I love it. And

**Dave Jones:** as you can see it it operates down to uh 0.8 volts, no problems. It drops off a little bit. Um it should probably drop to yeah, it probably dies at half at 0.8 volts. That's as probably as low as it's

**Dave Jones:** going to go because um uh we are uh operating uh this thing at um uh well, sorry, we want a minimum uh load current of half a milliamp. So, really, it's going to operate down to you know, there it is, half a milliamp

**Dave Jones:** is somewhere in there, round about 0.8 ON THE GRAPH. SO, if we set it to one, hey, we're going to be happy. You know, we could go up to here and then get some extra voltage margin, you know, if we uh

**Dave Jones:** set was up there at, you know, 5 milliamps. We can set it higher like that, but and get a bit more margin for our output voltage, but I don't think we need to do that. And if your output

**Dave Jones:** current doesn't happen to fall on one of these characteristic uh curves on this graph, you know, if you were 2 milliamps or something, you will have to use these formulas and you'll have to take the bias current ratio into account, which

**Dave Jones:** changes with your output current and that's the ratio that you can plug into various formulas down here to calculate your resistor value. Now, you remember this 10 microamps current we've talked about quite a few times from this set

**Dave Jones:** pin on this LT3080. It doesn't just magically disappear when you drive that pin. It's got to flow out of there. It's a constant current generator. So, it's got to flow out of that pin into that resistor and assuming that we're in

**Dave Jones:** constant voltage mode, all this stuff has vanished. It's got to go flow out of here as well. And if we got say trying to set 1 V on our input here, sure, we'll get a volt here, but then it's

**Dave Jones:** going to be there's going to be an offset error there due to that 10 microamps current. It doesn't sound like much, but Ohm's law, do the math. 10 microamps through 2K there is 20 mV. Once again, doesn't sound like much, but if you're trying to

**Dave Jones:** set 1 V on the output there, that's a 2% error. It's horrible. Don't want that. So, what do we do about it? Now, there's two things we can do about it. First one, the obvious one of course, is to

**Dave Jones:** lower these values until it gets to a point where you don't care more, and that's a perfectly reasonable design technique. But, in this case, well, we don't want to lower it too far. You know, we could lower it half of it down

**Dave Jones:** to four use 470 ohms or 220 ohms or something like that. But, ultimately, when you short out this op amp at high voltages, you're going to have a lot of excess current flowing out of there. And you're just wasting pissing that current

**Dave Jones:** away. So, I don't really like that solution at all. So, the next way to do it is to put it in the feedback loop of this op amp and compensate for it. And the way you do that is to break into

**Dave Jones:** here. So, instead of that output going directly to the buffer there, it's a pretty standard technique if you want to increase the output impedance of your buffer or your amplifier or whatever, is to simply stick that in the feedback

**Dave Jones:** loop there like that. Bingo. You've instantly gotten rid of that resistor, and And op amp compensates for it. Remember, due to op amp action, this voltage here will be equal to this voltage here. It'll do whatever it needs

**Dave Jones:** on the output to make that voltage the same. So, you've effectively eliminated the output voltage drop across that resistor, but you still have the advantage that it's protecting the output. So, when you short this, you're not going to short directly the output

**Dave Jones:** transistors of this op amp. Beautiful. But, that still leaves this resistor up here. Well, we can Turns out we can actually extend that. You can put all of this inside that feedback loop up here. So, we can connect that directly

**Dave Jones:** to the source pin. So, effectively, uh the voltage, once again, due to op amp action, that if you set 1 V here, you're going to get 1 V there and 1 V on that pin, and it's going to compensate

**Dave Jones:** for the drop through these resistors. So, these resistors can now be almost any value you like within certain limits, of course. Uh and it doesn't matter. The op amp is going to take care of it for you. Magic. So, that's what

**Dave Jones:** we're GOING TO DO. AND uh because you may This voltage uh set here is going to come from a reference uh voltage. You may want to use a 2.5 V reference voltage or something like that to match your op amps of your um

**Dave Jones:** uh microcontroller or something like that. So, you may not be using, like I say, a 10 V reference. So, you're probably going to need Uh can't get rid of that. There we go. Probably going to need some gain in

**Dave Jones:** there as well. No problems at all. It works exactly the same, not just in the buffer configuration, but also in the gain configuration, too. You put all your stuff you want to get rid of in your feedback loop.

**Dave Jones:** Beautiful. Woo. So, there you have it. After all that design effort, I'm pretty darn happy with this design. I think it's going to be the one I probably build up. Once again, you can uh add in a second device

**Dave Jones:** up here, parallel them like that we've mentioned stuff like that to uh increase your output current. And uh I might do that. And another thing you might want to do is uh replace this uh crusty differential amp here with a proper

**Dave Jones:** instrumentation amplifier like I mentioned before, like an AD620. All right, that's pretty expensive. An AD the low-cost AD623 or one of the uh high-side current monitor uh chips, monitor amplifier chips you can get specifically for high-side current sensing like this because it's going to

**Dave Jones:** be okay at 1 ohm uh like that, you know, just using a a fairly uh jelly bean uh sort of low-end precision uh op-amp that has, you know, 500 800 microvolts or something like that. You can get down to milliamp

**Dave Jones:** uh accuracy on this type of thing. But uh if you go down if you drop that uh if you want to reduce your voltage drop across there and use 0.1 ohms or something like that, uh your general-purpose op-amps, even

**Dave Jones:** your precision ones, aren't going to cut the mustard too much. And you may as well go to a proper uh instrumentation amp or something like that. Um now, you can uh do low-side current sensing as well. But as as I mentioned before,

**Dave Jones:** you're going to get voltage drop across there. If we include the resistor on the ground return path, the current shunt resistor on that ground return path from the output, you get the voltage drop there. There are ways around that, but

**Dave Jones:** uh it's dicky. I don't like it. Stick with the high-side current monitor, and we're sweet. So, I like that. Let's build it up. Said that last time, but this time I think I really mean it.
