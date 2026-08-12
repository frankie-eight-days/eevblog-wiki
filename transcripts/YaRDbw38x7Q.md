---
video_id: YaRDbw38x7Q
title: EEVblog #225 - Lab Power Supply Design Part 4 - PWM Control
url: https://www.youtube.com/watch?v=YaRDbw38x7Q
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 29, "3": 45, "4": 63, "5": 76, "6": 89, "7": 103, "8": 119, "9": 131, "10": 144, "11": 157, "12": 173, "13": 188, "14": 203, "15": 217, "16": 230, "17": 248, "18": 263, "19": 278, "20": 295, "21": 313, "22": 326, "23": 342, "24": 362, "25": 379, "26": 398, "27": 413, "28": 430, "29": 444, "30": 464, "31": 484, "32": 503, "33": 520, "34": 536, "35": 549, "36": 570, "37": 589, "38": 606, "39": 623, "40": 636, "41": 657, "42": 673, "43": 688, "44": 702, "45": 715, "46": 732, "47": 747, "48": 761, "49": 777, "50": 793, "51": 809, "52": 823, "53": 839, "54": 856, "55": 872, "56": 884, "57": 901, "58": 917, "59": 934, "60": 948, "61": 963, "62": 979, "63": 993, "64": 1012, "65": 1024, "66": 1040, "67": 1054, "68": 1071, "69": 1091, "70": 1108, "71": 1129, "72": 1144, "73": 1162, "74": 1178, "75": 1194, "76": 1212, "77": 1229, "78": 1244, "79": 1259, "80": 1271, "81": 1286, "82": 1300, "83": 1314, "84": 1330, "85": 1343, "86": 1358, "87": 1373, "88": 1388, "89": 1405, "90": 1420, "91": 1434, "92": 1447, "93": 1465, "94": 1478, "95": 1490, "96": 1507, "97": 1521, "98": 1538, "99": 1554, "100": 1569, "101": 1584, "102": 1601, "103": 1617, "104": 1632, "105": 1647, "106": 1659, "107": 1676, "108": 1693, "109": 1706, "110": 1721, "111": 1734, "112": 1752, "113": 1768, "114": 1783, "115": 1800, "116": 1814, "117": 1828, "118": 1844, "119": 1862, "120": 1876, "121": 1893, "122": 1906, "123": 1923, "124": 1941, "125": 1956, "126": 1972, "127": 1988, "128": 2005, "129": 2019, "130": 2033, "131": 2046, "132": 2064, "133": 2078, "134": 2095, "135": 2113, "136": 2128, "137": 2146, "138": 2160, "139": 2180, "140": 2198, "141": 2209, "142": 2221, "143": 2237, "144": 2253, "145": 2265, "146": 2280, "147": 2299, "148": 2312, "149": 2326, "150": 2342, "151": 2352, "152": 2367, "153": 2379}
---

**Dave Jones:** Hi. Now, after the last three videos on the power supply design, I've had a few people ask, "How do you do the PWM or the pulse width modulation voltage control instead of the 10-turn pot?" Well, it's a good question, so let's

**Dave Jones:** take a look at it. Now, when it comes to controlling a power supply like this, you've got three main options. The first one is the 10-turn pot, which I've been talking about, but they're quite expensive. They're about five to 10 bucks or even

**Dave Jones:** more each, depending on where you buy them from. The second one is to use a digital-to-analog converter. It puts out You put a digital signal in from your microcontroller, it gives you a voltage output, exactly like the pot, but I don't know, you're going

**Dave Jones:** to pay two bucks plus for a digital-to-analog converter. Not many microcontrollers have a DAC actually built in, so what you do is you use the third option, which is pulse width modulation, and it's effectively free. Most uh decent

**Dave Jones:** microcontrollers these days have a couple of PWM modules in them, pulse width modulator modules, and all you need It's not quite free. You've got to pay for a resistor and a capacitor, but gee, you know, they don't cost much at

**Dave Jones:** all. So, let's take a look at these. And there's a 10-turn pot, and they're very, very nice. And if you just build in a just a a linear uh power supply or uh even a switch mode one, and it's no

**Dave Jones:** intelligent microcontroller control in there at all, then I highly recommend just use a 10-turn pot. You can use regular uh pots, but then you've got to You've probably seen those power supplies that have coarse and fine adjustment. You That's probably a dead

**Dave Jones:** giveaway that they're not using a high-quality, expensive 10-turn pot, and they're dicky. Trust me, uh just the fine and coarse controls, they're hopeless. Get a decent 10-turn pot, but they're five, 10 plus dollars each, and you need one for voltage and current.

**Dave Jones:** Wow, there's like 10 to 20 bucks just for your supply right there. Doesn't include the knobs. And if you going for digital control, then what you're going to use instead of a pot because you're still going to have

**Dave Jones:** a knob on the front panel unless you use switches, uh then you're going to use one of these rotary encoders, and they're pretty cheap. They're only about 50 cents each or something like that, under a dollar. And you just put a little cheap knob on

**Dave Jones:** the top, and then you've got complete control. That is more than 10 turns. That's infinite number of turns. So, these uh rotary encoders are great. They're easy to encode in software, and you can use this to drive via your

**Dave Jones:** microcontroller either a digital-to-analog converter or a pulse width modulator. And the goal for all three of these things is exactly the same. You want a voltage output. If you've got a 0-to-10-V supply, then you want 0 V to

**Dave Jones:** 10 V output to drive uh whatever you're actually control your voltage regulator. And these do exactly the same thing. You turn a knob on these two here. You turn a knob, but a microcontroller generates the voltage. Now, in terms of the DAC uh

**Dave Jones:** here, you know about digital-to-analog converters, or if you don't, look them up. I won't go into them here, but basically, they're a dedicated device. You feed a digital signal in via usually, you know, like a serial input these days, an SPI or an I²C interface,

**Dave Jones:** or if they're built into the micro, they could do that, and they give you a direct voltage out. You don't have to do anything else with it. They're magic. But, a pulse width modulator is exactly the same as a DAC. It works It It well,

**Dave Jones:** it works differently, but it gives you the same result. It gives you a voltage output just like a DAC, and the resolutions are exactly the same as well. Because if you're working with a 10-bit or a 12-bit DAC, it's going to be

**Dave Jones:** give you exactly the same voltage resolution as a 10 to 12-bit PWM. So, let's take a look at how the PWM actually works. Now, uh you can get PWM hardware modules, dedicated hardware block inside your microcontroller that does all this for

**Dave Jones:** you independent of the software. The the microcontroller software can be off doing whatever it else it likes, and the PWM module in the micro will take care of generating the PWM waveform. And I highly recommend you use those if you

**Dave Jones:** have them available. But, you can do it using just a any generic IO pin, and you can do it in software because all it is is a digital waveform with a varying duty cycle. Now, what we have here, what a PWM signal is

**Dave Jones:** in this case, is just it's a a fixed frequency, say 10 kHz or something like that might be a typical PWM frequency. So, this waveform just repeats at at frequency of 10 kHz. Now, what changes though is the

**Dave Jones:** duty cycle or what's called the on time from 0 to 100% or what amount of time in that period that that waveform is high. And it can be anywhere from 0 0, of course, 0% would be it doesn't go high

**Dave Jones:** at all. It just stays low. Your output pin just stays forever low. And of course, you're going to get 0 V output. It's just low. It's a DC signal. But, let's say it goes high for X amount of

**Dave Jones:** time Let's say it goes high for 10% of the time, then 10% of the time it stays low for 90% of the time. What do you get out? Well, you don't get out anything. It's a digital signal. But, if you pass it

**Dave Jones:** through a low-pass filter, an RC filter, first-order filter like this, you will actually magically, as long as you got the filter values right, magically convert this PWM signal into a DC voltage from 0 to 5 volts because, let's

**Dave Jones:** say we've got a 5 volt microcontroller and that's what its output voltage is going to be, either 0 or 5 volts. Well, when you pass it through the RC filter like this, it averages out that duty cycle or on time value to a direct

**Dave Jones:** linear proportion linearly proportional voltage from 0 to 100% or 0 to 5 volts. So, if it's on 10% of the time and off 90% of the time, you'll get out 1/10 of 5 volts or half a volt out of your

**Dave Jones:** RC filter down here. Magic. So, you can see why it is actually a DAC. digital to analog converter. It works just like a DAC. You feed in a value, in this case, instead of outputting it into a digital

**Dave Jones:** to analog converter, you put it you the value that you put in from 0 to 100% gets converted into a duty cycle or on time from 0 to 100% and it generates an output voltage proportional to the digital signal or the digital number

**Dave Jones:** that you put in. Now, uh resolution plays a big part in these digital to analog converters and pulse width modulator circuits. And I said before, they're exactly the same. The resolution of a DAC is the same as the

**Dave Jones:** resolution of a pulse width modulator. Now, uh based DAC. That's sometimes what it's called. It's a PWM based DAC, basically, because it is a digital to analog converter, except it uses the PWM technique. Now, the resolution, let's take a pretty meager, pretty low-end

**Dave Jones:** 8-bit resolution and most really cheap budget low-end microcontrollers, you know, the 50 cent ones, might have these 8-bit PWM outputs like this. Now, of course, 8 bits represents there's 256 different levels. Now, that means that we can set

**Dave Jones:** this resolution in here in steps that there can be 256 different steps in there from 0 to 100%. So, what does that mean? It means that 100% divided by 256, it's each step we can get a resolution of 0.39%

**Dave Jones:** of our maximum voltage, which is 5 volts. So, in this case, 5 volts divided by 256, 19.5 millivolt steps. And if you're designing a 5-volt power supply, for example, then you would with an 8-bit resolution PWM module, you'd be able to

**Dave Jones:** get you'd be able to adjust that in almost 20 millivolt steps. That's not too bad for a generic lab supply, but let's say you doubled that to 10 volts. You multiplied it by two and you wanted a 0 to 10 volt output DC supply. Then

**Dave Jones:** you've got it then your steps would be 40 millivolts. You know, it's getting a bit crusty. You might want to up that to 10-bit resolution. If you have a look at 10-bit and 12-bit resolution PWM modules in the

**Dave Jones:** same case as 5 volts output, then divided by 1024 because it's 10 bits, 4.8 millivolt almost 5 millivolt steps. Not bad. 12-bit one. Hey, we're getting serious now. 4096 steps in 12 bits. So, we're talking a resolution of 1.22 millivolt steps.

**Dave Jones:** Fantastic. Now, here comes that tricky thing to do with the difference between resolution and accuracy. Just like you get in multimeters and a whole bunch of other stuff. Yes, a 12-bit uh digital-to-analog converter, be it PWM-based or other type of uh DAC-based

**Dave Jones:** uh system, then you will get almost 1 mV, just over 1 mV resolution or steps from 0 to 5 V. And uh it's And you do actually get that. You can control that output. You can jump it up by 1.22 mV.

**Dave Jones:** Bang, bang, bang. Or drop it down like that. You've got that fine control. But, the absolute value or the absolute accuracy, well, if you feed in completely 100%, are you going to get exactly 5 V out? Well, that depends on

**Dave Jones:** how you power or how you power your uh microcontroller here because the good thing about modern microcontrollers is that they're all CMOS. They're CMOS outputs. So, they use FET switching on the output. So, that means that they can

**Dave Jones:** get incredibly close, ridiculously close, to their input voltage rail up here on their output switching. So, if you're powering your PIC from precisely 5 V, 5.00000 V, then you can pretty much expect close to that absolute accuracy on the output

**Dave Jones:** of your PWM here. As a you know, uh there might be a millivolt drop or something like that. It's going to be very, very close. Okay? With these FET outputs. Now, if you just power your PIC or AVR from like a 7805, they're only 5%

**Dave Jones:** accurate. So, the output of your pulse-width modulator here is going to be 5% accurate absolute as well. And that's really not much good if you've got a uh bench a precision bench power supply. Now, you can compensate for that

**Dave Jones:** in software or uh parts with uh further gain stages or something like that, you can actually calibrate it and tweak it, but yeah, that's a bit nasty. But uh so sometimes you might want to actually power your microcontroller instead of

**Dave Jones:** from a regular voltage regulator, you can actually power them from a voltage reference. One of those precision uh you you know, 2 and 1/2 V voltage references if your micro goes down that low or a 3.3 V voltage reference or a 5 V voltage

**Dave Jones:** reference. And you can get those in like 0.1% or something like that, 0.2% for a dollar or so. So um you can actually power your microcontroller from that provided that your microcontroller and the other circuitry you're powering from

**Dave Jones:** it doesn't take more than its maximum allowable current. But you can actually do that. So when you're designing power supplies like this, don't be afraid to actually power your microcontroller from a precision voltage reference. It can work and it can be very handy. And in

**Dave Jones:** the previous videos, I actually used an LT109 voltage reference in the build, but you can use the LM336 and there's hundreds or thousands of other voltage references and some of them might have, you know, 40, 50 milliamps output capability and

**Dave Jones:** that's a decent amount of current for powering a a microcontroller. But just be careful if you're driving loads like LEDs and stuff directly from the microcontroller, then that current's got to come from the micro power rail, which comes from the voltage reference. But as

**Dave Jones:** long as you don't exceed that, you can get excellent absolute output accuracy as well as resolution on a PWM. So as you saw, if we have 10% on, 90% off during our period here, then we're going to get this RC filter is going to

**Dave Jones:** average that value out to 0.5 V. But it's not just going to be completely DC, there's going to be some noise on that. Okay? There's going to be noise superimposed on there depending upon the values you pick down here and

**Dave Jones:** how effective this filter is. So, we really need to take a look at it in depth at the filter and what values you need to get rid of, say, a 10 kHz might be a, you know, a very typical

**Dave Jones:** frequency. Let's take a look at what RC filter you need to get a decent low noise output from this, which then, usually, you want it lower than your resolution. So, if your resolution is 12 bits, you don't want the noise to be any

**Dave Jones:** more than one bit resolution or 1.22 mV. Now, what we're going to take a look at is a filter simulation program here. I'm using Filter Lab. It's from Microchip. It's an old program. It It does an okay job. There's one another one from TI and

**Dave Jones:** from various other people. Linear Technology do one as well. And and they're all pretty old, but they give you a good feel for how filters work. In this case, we've just got our simple RC filter here uh with

**Dave Jones:** the buffer and that's called a single pole filter. And we can change the filter up here. That's this number one up here. That's So, if we go to a second, what's called a second pole filter, you've added some extra

**Dave Jones:** components. And third, a three pole filter and a four pole filter. This is called a Sallen-Key configuration. There's There's different configurations you can do, but basically, the order of the filter, the higher the order, the greater the attenuation

**Dave Jones:** of those higher frequencies. Now, let's take a look. Let's go to the first-order filter. Now, I've set the filter to have a roll-off, a nominal roll-off, or a filter cut frequency of 1,000 Hz. So, you can see that here.

**Dave Jones:** It's 1 kHz. And what that means, you've seen that probably seen that formula before. It's 1/2 pi RC, and that gives you the cutoff frequency of your filter. Now, that it's not a brick wall cutoff, okay? What we've got on the X axis here

**Dave Jones:** is our frequency, okay? Now, this is a logarithmic scale, so it's in decades, so it doesn't go linearly from say 100 Hz to 1,000 Hz here. It goes That's 100 Hz, that's 200, then 300, 4, 5, 6, 7, 8,

**Dave Jones:** 9, and then 1,000 Hz like that. Now, the reason um we use a log scale like this is because it actually gives us a linear slope like this. It converts our logarithmic um response into a linear slope, which will

**Dave Jones:** become um it's just easier to do, and it's easier to fit um wide frequency spans into the one graph like this. So, that's why we're using a decade logarithmic response on the X axis. Now, the Y axis here is the magnitude in dB.

**Dave Jones:** So, right down here at 100 Hz, it's got 0 dB attenuation. That's the attenuation of the filter. So, you're feeding your signal, and what you get out you at at at 100 Hz, you're feeding exactly what you get out. There's 0 dB

**Dave Jones:** attenuation. Now, the uh the filter cut frequency, that formula 1 over 2 pi RC, that gives you your what's called minus 3 dB uh cutoff frequency of that filter. So, as you can see, in uh that that filter there, I've got it

**Dave Jones:** on the Y axis there, it's about minus 3 dB, and it's spot on 1,000 Hz on the X axis, cuz that's where that's what we've designed it for. And then it rolls off after that. Now, you remember we've been

**Dave Jones:** talking about filtering out a 10 kHz frequency. Well, let's go down to 10 kHz. Here it is. How much is our that filter attenuating our 10 kHz signal by? Well, if you take that over to the x um

**Dave Jones:** sorry to the y axis over there it's minus 20 dB. And if you know your dB's a minus 20 dB drop in amplitude is 1/10 or an order of magnitude. So if we're feeding in 1 V we're going to get out

**Dave Jones:** 0.1 V. Now the thing about dB's is that once you step down to if you go down to so in multiples of 20 that's an order of magnitude drop. So minus 20 dB is 1/10, minus 40 dB is 1/100, minus 60 dB is

**Dave Jones:** 1/1000, and minus 80 dB is 1/10000 of your input voltage. Now if we increase our pole down number of poles or the sharpness of our filter you'll see that it gets steeper and steeper as we go off. Now the roll off which is is

**Dave Jones:** specified in dB's per decade can be specified in other things too but in this case it'll be dB per decade and it it gets just sharper and sharper. And as you can see if we used a five pole

**Dave Jones:** filter our 10 kHz signal would be attenuated by minus 100 dB. That is absolutely phenomenal okay but if we use our first order filter which we've got our RC filter it's only attenuated by 1/10. So we're not going to filter out if if we

**Dave Jones:** set our cut off at 1000 Hz. So if you're trying to filter out a 10 kHz frequency PWM signal with a 1 kHz filter it's going to do a pretty darn poor job of it. It's only going to attenuate that 10

**Dave Jones:** kHz signal by one or the 10 kHz ripple by 1/10. It's hopeless. It's like you know, 10% unbelievably hopeless. Now, what I've done here is to set the filter to 10 Hz. So, there's the minus 3 dB cutoff

**Dave Jones:** frequency at 10 Hz. And you'll notice that at 100 Hz, it's 20 dB down. And at 1 kHz there, it's 40 dB down. So, if you measure the difference actually between the 100 Once it gets on this linear part

**Dave Jones:** of the curve here, if you measure the difference between the 100 Hz frequency at minus 20 dB and the 1,000 Hz frequency at minus 40 dB, that's what's called 20 dB per decade. So, that filter rolls off at 20

**Dave Jones:** You get 20 dB attenuation per decade in frequency. So, if we extended that graph out even further there, where to 10 kHz, we'd find that it'd be down to minus 60 dB. So, if we set our filter at 10 Hz, at 10

**Dave Jones:** kHz, we will be We'll have minus 60 dB attenuation of that 10 kHz fundamental frequency. And remember when I said it drops an order of magnitude or 10 times per 20 dB, then at 10 kHz, we'd be at minus 60

**Dave Jones:** dB. Sorry, it's off the graph. I haven't got enough decades to show it here, but it's minus 60 dB at 10 kHz. So, that's 1 1,000th. That's the attenuation. So, you feed in 1 V, then you're only going to get 1 mV out.

**Dave Jones:** Now, just to be clear, that 1 mV I'm talking about there, and these are levels I'm talking about, are they only apply to a sine wave at 10 kHz. So, basically, all this filter talk we've been talking about doesn't actually

**Dave Jones:** apply directly those amplitudes to the PWM. It gets more complicated when you start talking to PWM signal. And in practice, it's actually going to be uh lower than that, but let's uh use a ballpark. Let's say you did actually get

**Dave Jones:** 1 mV of ripple out. Assuming it transferred to your output through the regulator then, and there wasn't any extra further uh filtering, then, you know, that that might be okay, but generally you'd want to shoot for better than that. But, with a filter cutoff of

**Dave Jones:** 10 Hz, you know, that means you're not going to be able to um change your output voltage really quickly. And, on a DC power supply, if you're manually turning a knob, it's not a problem, you know, you can't turn that knob very

**Dave Jones:** quickly at all. You're going to turn it only, you know, effectively, you know, a 5 or 10 Hz at most or something like that. Okay, you're not going to get huge big step changes on your power supply because it's filtered out. All right,

**Dave Jones:** now we're actually going to do some real circuit simulation here with a PWM uh signal and with our LC uh one-pole LC filter and see what we actually get out. Now, I've set up this uh voltage um it

**Dave Jones:** looks like a voltage source, but it's actually a uh pulse source. I'm using LTSpice um here, which is a free uh circuit simulation tool. I highly recommend you get it. It's pretty darn good. And, basically, what I've set here

**Dave Jones:** is I set the pulse width modulation um uh voltage level uh from uh um to 1 V. So, it's going to uh switch between 0 and 1 V. Now, you know, uh it it won't do that if you're using a

**Dave Jones:** microcontroller that's say a 3.3-V voltage rail, you'll get 3.3, but we'll set it to 1 here just to make our uh math nice and easy today. Now, the period down here I've set to 100 microseconds, and that's equivalent to

**Dave Jones:** 10 kHz. So, we're going to get a 10-kHz repetition rate on our PWM signal. And then, I can set my on time. I've set it to 1/10 of that. So, I'm setting it to 10% on time or 10% duty cycle. It's 10

**Dave Jones:** microseconds out of that 100 microseconds total. Okay, so what I'm doing is I'm going to go into the simulation command here. We're doing transient analysis. And I've set my stop time to 1 millisecond and I've set my time step so

**Dave Jones:** it effectively samples or simulates the circuit every 0.1 microseconds. And if we hit that, then and we run it up here, bang, there we go. And I told it so we're only going to get it stops when it once it got to that 1

**Dave Jones:** millisecond period. And what we're doing is we're measuring this point here. You can see the little red probe down there on the circuit and we're probing that point right there, which is the PWM input. And as you can see, it is 10% and

**Dave Jones:** you can go in there and actually measure that precisely, but trust me, it's going to be 10%. So, our on time is 10%. So, we expect if we're feeding in 1 volt here, 1 volt peak-to-peak, there it is

**Dave Jones:** over on the Y axis here from 0 to 1 volt PWM signal, we expect 10% on time, we expect 1/10 voltage on here. Do we get it? Well, not quite and we'll see why. Now, the reason is is that is actually

**Dave Jones:** slowly ramping up because there's an RC time constant. We started the simulation from zero. So, we're going to have to go in here and we're going to have to extend that time period. Let's say set it to 100 milliseconds like that. Let's

**Dave Jones:** leave it at 0.1. It could take a bit of a while to simulate that, but let's try that again, shall we? Now, it's going to be hard to see that if we zoom in. So, let's click on the circuit here. Bang!

**Dave Jones:** Look at this. And you can actually see that window there. Let's uh zoom to fit. Okay? And bingo, you can see it rise up like that. That's our RC time constant that it takes when you first switch on the supply or change the

**Dave Jones:** voltage or whatever. It doesn't respond instantly, but it eventually settles down to bingo. What does it settle down to? Go across here, exactly 100 mV average. Trust me, if you drew a line straight through there, it would go right through

**Dave Jones:** the average point of that waveform. So, there's our 1 10th. It's worked. Our 10% duty cycle has translated to uh 1/10 of that or 100 mV output voltage. And if you look at the output on the op-amp over here, you can see

**Dave Jones:** that that takes a little bit of time, but it it responds to the same value. But, there's a little bit of an offset there. That's going to be due to the offset voltage, but anyway, what we really care about here is this noise.

**Dave Jones:** Look at the ripple. You can see that the switching frequency because um the RC filter we're using is not uh low enough in value to filter out all that noise. Who wants a power supply when you're trying to output 100 mV? It's got, you

**Dave Jones:** know, what's it got? 10 mV of ripple on that. Ah, hopeless. And that's with a filter frequency down here of 159 Hz because if you do the math, use that formula, 1 over 2πRC, that's that the 3dB cutoff point of that

**Dave Jones:** filter is 159 Hz. And we're trying to fil- filter out uh 10 kHz. So, as you can see, it's not terribly effective at all. But, let's try that again. If we actually change that to 1 microfarad, you'll find that this

**Dave Jones:** ripple here will decrease. We're increasing the capacitance by a factor of 10, so our filter frequency will go from 159 Hz to 15.9 Hz. And you'll find that because this is all order of magnitude, the ripple will also drop by

**Dave Jones:** an order of magnitude. So, let's resimulate that. So, it's about 10 millivolts at the moment. Let's resimulate that, and bang, it's slightly ramping up. It's ramping up, but as you can see, it's taking longer. It's taking much longer

**Dave Jones:** to actually get up to frequency there cuz we've changed the RC time constant. So, you can see that's taken 54 milliseconds before it even, you know, 50 odd milliseconds before it even sort of starts to level out like that, and

**Dave Jones:** that's not too bad, actually. Now, let's go in there and have a look at the ripple. We'll zoom right into this window here, and bingo, you can see it. There it is. That's only about one Well, what's that? Half a millivolt

**Dave Jones:** even. It's only half a millivolt ripple. Fantastic. So, as you saw there, there was really quite a trade-off between the response time and the uh and the filter effectiveness or the filter attenuation. Now, to do that uh to get around that,

**Dave Jones:** we can add a second stage RC filter like we've done here. Exactly the same. So, we've gone back to our original 10K and 100N here. So, that's 159 hertz nominal uh 3DB cutoff. We've added another identical one here, 10K and 100N, and we

**Dave Jones:** could do it with the op-amp and use, you know, various configurations like a Sallen-Key configuration and all that sort of stuff, but let's just start keep it simple and put two um RC filters in series like this. And if you run it,

**Dave Jones:** this is what you get. The green line there is the value on here like the exactly what we saw before. Okay, that's got our like 10 millivolts of ripple on it. It's huge, but our second one here after that, that

**Dave Jones:** is the blue line there. And check it out. That is Let's put both on there, and as you can see, it's it's beautiful. It And if we zoom in on that, let's zoom in on that part of it there.

**Dave Jones:** Look at that. The blue one, smooth as a baby's butt. There's hardly any ripple on that at all. We're talking, uh, .1 mV, .2 mV or something. It's tiny. So, that's just an easy way that you can get, uh, extra filtering on your

**Dave Jones:** PWM. Just add a second RC filter stage. I mean, sure you can up these values here, okay? These, uh, 10k, uh, this 10k and 100n, you know, you can up those, but then your response time gets low. So, it's better to add this, uh, second

**Dave Jones:** stage here, and then you can keep your response time fairly quick at 10 ms or something like that. But, um, it has much greater attenuation. So, you know, we're down in the hundreds of microvolts there now just by having a

**Dave Jones:** simple 10k and 100n like that, a two-stage RC filter. Beautiful. Now, what happens if your PWM signal is, say, 5 V out? Now, let's change it back to 5 V here, but let's say because you're got a 5 V rail on your microcontroller, but

**Dave Jones:** you don't want to get 0 to 5 V out. You only want 0 to 1 V or something like that. Well, what can you do? It's easy. You can add a resistor in here to actually attenuate that. So, let's add

**Dave Jones:** that in and see what we get. So, let's run it again with that. We've got our 5 V signal here, okay? There's our 0 to 5 V PWM signal at 10%. So, what do we expect out? We expect half a volt,

**Dave Jones:** 500 mV here. That was before we added this 10k, though. So, now we expect to halve that again, or .25 V, 250 mV. Let's see if we get it. Bingo, we do. There's our 250 mV, but it's got the ripple. But, if we

**Dave Jones:** look on the output here, then bang! There it is. Our blue line our blue trace there, that's 250 mV. So, let's run it again with that. We've got our 5-V signal here. Okay, there's our 0 to 5-V PWM signal at 10%. So, what do we

**Dave Jones:** expect out? We expect half a volt, 500 mV here. That was before we added this 10K, though. So, now we expect to have that again, or 0.25 V 250 mV. Let's see if we get it. Bingo! We do. There's our

**Dave Jones:** 250-mV, but it's got the ripple. But, if we look on the output here, then bang! There it is. Our blue line our blue trace there, that's 250 mV. Now, here's an interesting thing I just wanted to show you quickly. We've got an LT1014

**Dave Jones:** op-amp here. I just chose this generically just so we could get something working from the library. Now, it just so happens that this is a fairly, you know, good precision op-amp. It's only got a couple hundred microvolts offset voltage, and you pay a

**Dave Jones:** bit of coin for this thing. So, you'd expect it to work out quite well at low values. So, let's actually try that. Now, I've changed my PWM here to 0.1 microseconds compared to 100 microseconds period. So, that's 1/1000

**Dave Jones:** of our 5-V maximum PWM voltage there. So, if we're getting 5-V here with 1/1000 on time, we expect 5 mV out of our filter. And if we run it, bingo! That's exactly what we get. There's our 5 mV, and that's the input

**Dave Jones:** to the Well, that's the first stage of filter, second stage filter input to the op-amp, 5 mV. Well, let's also add on the output of the op-amp. What? Look at that, 35 mV. What's going on? Well, it turns out that this If you look at the

**Dave Jones:** data sheet for the LT1014, it turns out that you can't actually go down to 0 V unless you have a decent load on there. It's not a rail-to-rail op amp. So, just be careful if you're actually when you're choosing an op amp

**Dave Jones:** like this in this grounded configuration and you don't have a negative supply voltage for that op amp, just make sure that it's actually capable of 0 V on its output. Otherwise, if you use this fairly high precision op amp, we'd

**Dave Jones:** get a 35 mV output offset. Terrible. So, you might think that the solution to this PWM thing and the trade-off versus the the response time versus the attenuation and the ripple and all that sort of stuff is to just up the

**Dave Jones:** frequency of your PWM signal. Well, yeah, in theory, that's great. The higher the PWM frequency you use, the easier it is to filter out with better response time. But, the microcontroller is going to have a limit to how high a

**Dave Jones:** PWM frequency it can go based on the resolution. And generally, you can change the resolution of these things. You might be able to use the a 10-bit resolution PWM. You might be able to use it as an 8-bit one, or as a

**Dave Jones:** 10-bit one, for example. And it's going to have a maximum upper frequency. You have to read the data sheets very carefully to get that sort of info. But, generally, you want to run them as fast as possible. All right, enough of the

**Dave Jones:** simulation stuff. Let's actually feed it into our circuit a PWM signal to replace the pot which we used before in the previous videos. That's exactly what I've done. I'm using the function generator output of my Agilent scope here to actually replace the pot.

**Dave Jones:** And I'm feeding it in via a single RC filter, which is what we've looked at. And this is what I've got here. Instead of the voltage control pot, we've we've disconnected that and we're taking it down to a 10K and a 100N low-pass filter

**Dave Jones:** just as we looked at. And the frequency I've got set, as you can see here, if you go in here, you can see I've got 100 kHz frequency and our amplitude is 3.3 V. So, we're simulating a microcontroller generating that PWM

**Dave Jones:** signal with a 3.3 V rail. The offset voltage because it the function gen that's got to be halfway in between. We've got a 50% duty cycle or 50% on time. So, if we're feeding in 3.3 V and by the way, I've also changed

**Dave Jones:** this feedback resistor here just to make the math easy, changed it to 10K. So, we'll have a gain of times two in this amplifier control loop here. So, if we're feeding in 3.3 V that we've got here, we should

**Dave Jones:** get some ripple out of here, of course, because it's not that great this filter on its own. And so, and at 50% duty cycle, we'd expect to get 1.65 V out of here multiplied by two, we expect to get our 3.3 V out of

**Dave Jones:** here. Exactly what and let's actually see if we get it. Well, if you have a look here, let's zoom out. There it is. There's our output voltage. It's pretty close. There's going to be some error in here. This isn't perfect, but if we

**Dave Jones:** was to use more more precision function gen and stuff, you'd get exactly 3.3. So, we're getting out exactly what we expect. And this the green signal here which I'm triggering off, there's our 3.3 V 10 kHz PWM signal and the yellow trace here is

**Dave Jones:** the AC coupled output on that RC filter there. So, on the RC RC filter right there, that's our yellow waveform there. As you can see, that yellow waveform 100 mV per division, we're getting 100 mV ripple on there. And

**Dave Jones:** let's probe the output and see what we get. And this is our output. I've just in the output of our power supply, our 3.3 V output. And as you can see, it's there's not much on there at all. We're

**Dave Jones:** still at 100 mV per division, but if we turn that up, you can actually see you can actually see the ripple on there now down at 10 mV per division. We're getting about 5 mV, you know, 8 mV worth

**Dave Jones:** of ripple or something like that. And look at these little high-frequency stuff in here like that. Bit of ringing there, that's probably due to our probing and stuff like that, but you really want to get rid of this sort of stuff. So, that's not

**Dave Jones:** adequate ripple. If we just used that 159 Hz filter there, that's that's really no good at all. I like that one bit. Now, you're probably asking, why did that output actually Why did that output ripple drop from 100 mV to under

**Dave Jones:** 10 mV? It shouldn't have have all just If we were getting that here, shouldn't have all just passed through that straight to the output? Well, no, not really. Remember these caps we got here? They're going to do some filtering as

**Dave Jones:** well. And that's what you get if you you replace the 22 microfarad cap here down to 100 n. Bingo. And it turns out that I still had 47 microfarad of capacitance on the output there. So, I took that

**Dave Jones:** off, and what do you get? Magic. Look at that. Wham! That's an absolute shocker. And bingo, it's back to 100 mV. There you go. So, it's actually now made its way all the way through. So, all of our

**Dave Jones:** noise, all of our ripple that we had on our filter here has gone all the way through cuz now we don't have adequately adequate filtering on the output or the or the input to the set pin here. And

**Dave Jones:** what happens if we add in a second RC filter in here once again 10K and a 100N. Bang! There's our output voltage exactly the same scale as before but our ripple has dropped very very significantly and once again that's with

**Dave Jones:** no practically no output filtering or no filtering on the set pin. And if we replace our filtering back our 22 mic here and our big capacitance on the output, bang! There's our noise. It's suddenly vanished. These little spikes

**Dave Jones:** in here are going to be due due to ground bounce and stuff like that. You can actually see the bounce in there is to do with probing and things like that. So don't worry about that but the output

**Dave Jones:** noise there, look at that. Beautiful. And what happens if we adjust the duty cycle here? Well, let's give it a go, shall we? Let's drop it down to say 10%. Wait. Of course, silly function gen only allows us to go down to 20% but

**Dave Jones:** there you go. That's the expected 1.3 volts or 20% of that 6.6 volts cuz we've got a times two amp in there. There you go. It works fine and if you drop that if you did drop that duty cycle down to

**Dave Jones:** 1% or 0.1% you'll find that the output voltage would follow. So there you go. That's a practical demonstration of how to replace your control part with the PWM output or a DAC output of a microcontroller. Piece of cake. Catch you next time.
