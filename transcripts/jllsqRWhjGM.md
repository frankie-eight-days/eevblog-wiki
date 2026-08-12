---
video_id: jllsqRWhjGM
title: EEVblog #490 - Peak Detector Circuit
url: https://www.youtube.com/watch?v=jllsqRWhjGM
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 31, "3": 45, "4": 58, "5": 72, "6": 90, "7": 107, "8": 123, "9": 137, "10": 152, "11": 170, "12": 187, "13": 199, "14": 214, "15": 227, "16": 240, "17": 253, "18": 268, "19": 284, "20": 293, "21": 307, "22": 324, "23": 337, "24": 350, "25": 364, "26": 377, "27": 392, "28": 406, "29": 421, "30": 439, "31": 454, "32": 471, "33": 484, "34": 499, "35": 510, "36": 523, "37": 539, "38": 553, "39": 566, "40": 582, "41": 597, "42": 611, "43": 625, "44": 641, "45": 655, "46": 669, "47": 690, "48": 703, "49": 723, "50": 732, "51": 745, "52": 757, "53": 773, "54": 789, "55": 803, "56": 820, "57": 831, "58": 844, "59": 859, "60": 872, "61": 883, "62": 897, "63": 910, "64": 925, "65": 940, "66": 953, "67": 965, "68": 982, "69": 1000, "70": 1014, "71": 1030, "72": 1045, "73": 1060, "74": 1072, "75": 1085, "76": 1097, "77": 1117, "78": 1136, "79": 1148, "80": 1163, "81": 1178, "82": 1188, "83": 1202, "84": 1215, "85": 1228, "86": 1241, "87": 1256, "88": 1271, "89": 1283, "90": 1293, "91": 1310, "92": 1325, "93": 1341, "94": 1358, "95": 1376, "96": 1390, "97": 1407, "98": 1420, "99": 1436, "100": 1449, "101": 1463, "102": 1478, "103": 1493, "104": 1508, "105": 1525, "106": 1536, "107": 1551, "108": 1565, "109": 1580, "110": 1596, "111": 1615, "112": 1629, "113": 1644, "114": 1659, "115": 1677, "116": 1692, "117": 1711, "118": 1724, "119": 1741, "120": 1753, "121": 1763, "122": 1780, "123": 1796, "124": 1812, "125": 1830, "126": 1846, "127": 1862, "128": 1874, "129": 1890, "130": 1904, "131": 1918, "132": 1932, "133": 1944, "134": 1958, "135": 1975, "136": 1988, "137": 2002, "138": 2017, "139": 2031, "140": 2046, "141": 2062, "142": 2077}
---

**Dave Jones:** Hi, welcome to Fundamentals Friday. Today we're taking a look at a real basic building block circuit called the peak detector. Now, what a peak detector is, if you've got an analog input signal that you want to know what value

**Dave Jones:** it peaks at, as the name suggests. If you've got your it could be a voltage like that, you want the positive peak voltage on that or negative, but let's we're just going to look at the positive case today. And you want to detect that

**Dave Jones:** value and read it out. Now, why would you want to do that? Well, you know, there's many reasons in the audio field, for example, you want to sort of, you know, get a peak value and hold it there. You might want to drive a some

**Dave Jones:** sort of LED display or something like that. Lots of measurement scenarios as well, where you may want to get this peak detector value. Now, you know, you may think, well, you could throw sort of brute force at this and you can feed

**Dave Jones:** your analog input signal into an analog-to-digital converter and then you can read the values and you can get the maximum one. Well, yeah, you can do that sort of thing, but it's much easier to do it with two simple components. Turns

**Dave Jones:** out all you need to do for a peak detector is feed your input signal like this into a diode and a capacitor. That's it. So, what are we going to get out of a simple diode-capacitor peak detector circuit like this? Well, I've redrawn my

**Dave Jones:** input signal here and let's assume that your input signal starts out at zero like this and your capacitor is initially discharged. So, got zero volts on the capacitor. Well, the output voltage is going to follow the capacitor voltage like that and then

**Dave Jones:** it's going to go across here like this. Stick with me for a second. It's going to go up there like that and then it's going to jump up there and go like that. It's going to continually track the peak value of that signal. And why

**Dave Jones:** is it going to stay a DC signal like that? Well, a value on a charge on a capacitor, if it's if it can't discharge out that way, and it can't go backwards through the diode, because your diode would be reversed biased, you know,

**Dave Jones:** current can't flow through the backwards through a diode, that's why the diode symbol looks like that. There's an arrow pointing in that direction. Then the voltage, the charge on that capacitor stays there like that. And that is the basis of the

**Dave Jones:** diode capacitor peak detector circuit. Incredibly simple and incredibly useful in its own right. But of course, you're not fooled because you know that diodes aren't ideal, and they're going to have that diode drop. They're going to have that loss on there. So, the actual value

**Dave Jones:** you I hope this shows up on the video is actually going to be somewhere below your actual value. So, in there, there's actually going to be a difference of the of your diode voltage drop in there. So, it's not an ideal circuit, but it

**Dave Jones:** can still be useful in a practical sense for like a basic peak audio level detection or something like that, where you don't care about sort of half a volt. You just care sort of, you know, oh, it's near enough up the top, or you

**Dave Jones:** don't actually need the absolute value. You just need to hold uh sort of hold a particular value. And this circuit also effectively works as a very crude sort of sample and hold, as well as a peak detector. If, you know, sample is except

**Dave Jones:** it only samples it continually samples the maximum value, and then holds that maximum value for an indefinite period of time if there's no discharge on that capacitor. But of course, in practice, hey, there's always going to be some

**Dave Jones:** load on here. You're going to get self-discharge in the the due to leakage, and then you're going to get back leakage through the diode. There's leakage all over the place. So, this value is not going to hold. We'll get rid of

**Dave Jones:** the blue waveform. The value is not going to hold steady like that. It's just It's going to droop off like that, and eventually discharge all the way down until another the next peak and if another peak value came along, of

**Dave Jones:** course, like this, bam, it would, you know, top it top it back up like that. But, assuming that the input circuit the input signal dropped away, you'd eventually get droop on that capacitor. Yes, droop is a technical term, and it would eventually

**Dave Jones:** droop down to zero. Now, this particular scenario here is okay if you want to sample or measure your peak DC value at you know, a slow rate or something like that. But, then what happens when you want to reset the thing? Um you know,

**Dave Jones:** you've still got this capacitor charged. It can't flow back out there. It can't do this. Well, there's a couple of things you can do. You can either put A common way to do it is to put a resistor

**Dave Jones:** across here as well, and then that will, of course, cause it to droop much quicker, but you at least it gives you a known droop. So, then, instead of going drooping all the way like that, it may only hold that peak value for a small

**Dave Jones:** amount of time there, small amount of time, and then really drop off very quickly. So, it's effectively a sort of self-resetting uh circuit as long as you measure that peak value right at that time up there. Not a problem. It'll self uh discharge

**Dave Jones:** very quickly. It'll eventually get down to zero, and it effectively resets the peak detector circuit. But, if you're sort of doing uh like intelligent measurement on this thing, and you've got an analog-to-digital converter, it could be a microcontroller or something,

**Dave Jones:** reading the value out of this, then well, as soon as you've read your peak value, it makes sense to reset your peak detector detector signal straight away, and not just have to rely on a simple resistor to discharge the thing. So,

**Dave Jones:** what do you do? You replace the resistor with a MOSFET like that, and you can apply a signal to the gate and short out that capacitor. Bam! You've reset your peak detector circuit. So, peak detector circuits really quite useful. It, you

**Dave Jones:** know, a changing AC input waveform, if you only care about what the maximum value, either positive or negative, is, you can just use a couple of simple components and it gives you a DC value out that you can read. Great! Because

**Dave Jones:** it's much easier to, you know, and simpler to read a DC value out than it is to sample this waveform at, you know, a much faster rate than the highest frequency component in there, and then, you know, have a processor just

**Dave Jones:** churning away in the background trying to detect the positive and negative peaks. That brute force approach is pretty horrible. It's a pretty elegant, simplistic way to do it. So, that's your basic diode capacitor peak detector circuit, but of course, you're not, in

**Dave Jones:** practice, while the diode capacitor technique is quite common for very crude circuits, the absolute value doesn't matter. For any sort of like semi-precision or precision applications, especially where you've got an analog-to-digital converter on hooked on there and trying to read the

**Dave Jones:** real value, of course, you're not going to use a crusty diode in here. Diodes are horrible. They've got an unknown loss based on the current, which changes significantly with temperature. Really unprecision type components. So, what we actually need to solve this problem here

**Dave Jones:** is an ideal diode. If the If the diode's ideal, well, we can solve a lot of our problems right there. As it turns out, in practical electronics, you can actually build a an ideal diode, or what's called a precision diode, or

**Dave Jones:** sometimes known as a precision rectifier. How you do it? A basic op-amp with an existing crusty diode in it. And that forms a precision diode precision rectifier. So, how does this work? Well, it's a voltage follower. Look at it.

**Dave Jones:** You're familiar if we should short it out that diode, then we've just got a basic voltage follower. The output voltage equals the input voltage. Well, in this case, let's say we put a load on there like that down to ground, then

**Dave Jones:** what's our output voltage here going to be? Well, it's going to be equal to the input voltage for those positive values. You're feeding in a positive If you feed 1 V in here, for example, you're going to get 1 V out here. But once you start

**Dave Jones:** feed If you're feeding If this is a dual supply op-amp, you feed a negative voltage in here, the diode is going to be reverse biased, you're not going to get anything. All you're going to do, that may as well be open

**Dave Jones:** cuz no current can flow. Well, there's no current flow into the input pin, so that resistor your load pulls it down to ground, and bingo, you've got zero output volts. And if you want to see that on the graph here, then well, it's

**Dave Jones:** just like your regular diode rectifier that you're familiar with in linear supplies, except we our output voltage is precisely equal to V in because the op-amp does what it needs to to keep these value these input values the same.

**Dave Jones:** Remember, that's one of the golden rules of op-amps. So, the output voltage here Oh, sorry. Got to draw my diode back in there. Our output voltage here is actually going to compensate. The op-amp is going to drive this output voltage

**Dave Jones:** here to compensate for the loss in the diode, and it's going to do it in real time, and it's going to compensate for temperature and everything else, regardless of how that diode how crusty that diode is. You can even use a real

**Dave Jones:** crap one, the op-amp will compensate for it. And so, the out works just like a standard rectifier, except it's a precision rectifier cuz there's no diode loss here. Output voltage, if you feed in a AC signal on the input, which

**Dave Jones:** you know, it would have been down here if it was a Right? But, it cuts that bit off, and it rectifies that like that. Exactly like your regular rectifier. So, we've got exactly the same circuit as we had up here, except

**Dave Jones:** our diode is now an ideal, perfect diode, provided you operate it within the op-amp voltage range, but that's all a given. Now, you can do exactly the same thing. You can have the resistor load on the capacitor here, for example,

**Dave Jones:** or you can have your MOSFET there, your reset MOSFET there to short out the cap on the output, provided, of course, that your op-amp can handle that short circuit current, and it's not going to cause any damage. Usually not a problem.

**Dave Jones:** So, we've got now our perfect peak detector circuit. Or is it? You know, this sort of circuit is good enough for sort of, you know, ordinary everyday applications, where you want to get a relatively accurate, you know, quantized value of the peak

**Dave Jones:** value. You've got an ADC on here, and you want to accurately measure that peak voltage, and then reset it, however you want to reset it, and this circuit does a pretty darn good job, but it does have a few limitations. Now, the first

**Dave Jones:** limitation is, of course, the discharge on the cap. Now, if you're driving an ADC, for example, this isn't exactly the ideal circuit to be driving an ADC with, and I won't go into ADC details and stuff like that. Whole separate video,

**Dave Jones:** but for for suffice it to say that ADCs can actually take input current spikes when they're taking the measurement, in like in the case of a successive approximation analog-to-digital converter, like a typically used in microcontroller, for example. So, you don't want, you know, a

**Dave Jones:** a bit of current to be drawn out of your cap and then it droops and droops and droops. So, you don't want your capacitor to droop like that. So, during measurement because that's bad news. So, typically, you're going to follow that

**Dave Jones:** with another op-amp voltage follower, which is a proper low impedance source, very high impedance input here, and that can drive your ADC, not a problem at all. Now, the second problem here is the recovery of this op-amp because remember

**Dave Jones:** that this op-amp is going to do whatever it needs to to make this output follow the input. So, let's say we had our peak value go up there, very short, sharp, bang, it went up to peak, and then it

**Dave Jones:** dropped all the way down to zero. Well, this op-amp is going to try and force this output here to to zero. How is it going to to match the input signal of zero here? How's it going to do that?

**Dave Jones:** Well, this input uh uh sorry, the output signal of the op-amp here is Yeah, it's going to ramp up to the peak value, but then it's going to try and go It's going to try and instantly go low, and it's

**Dave Jones:** going to slam right hard against the negative rail. It's going to go, "Uh, I'm Send it low. Send this output signal low." But, of course, it's not going to go low because it the um diode is not going to allow that to happen because

**Dave Jones:** it's reverse biased. Once this voltage drops down, this output value here is zero, diode's reverse biased. Uh. It can't do anything. The op-amp has lost control over the ability to force this um value here back down low cuz the

**Dave Jones:** capacitor's going to hold it. So, the op-amp can't do anything but kick and scream and and pull this output right down low to try and do it. So, it's going to saturate right down to its negative rail, either negative rail or

**Dave Jones:** ground if you're using a single rail op-amp. So, what that means here is when the peak value is when another peak value comes along. If you have a nice fast peak value jumping up there, then this um op amp is going to of course go right

**Dave Jones:** back up, or it's going to try to, but it's going to take time to charge up this capacitor. So, you're going to have the slew rate of the op amp there. It's not going to go suddenly high like that.

**Dave Jones:** The output voltage here then won't go immediately up to the value. There's going to be some slew rate in there. And if you're working on fast signals, for example, the slew rate of the op amp is going to matter a lot. So, you've got

**Dave Jones:** that recovery time in there of this op amp. And that, for a lot of circuit applications, can be a real big deal. So, naturally that leads to a trade-off between how fast this op amp is and what value capacity here you use. You can't

**Dave Jones:** just arbitrarily choose a super Oh, I'm going to put a 1,000 microfarads in there. That'll hold the voltage forever. Fantastic. That'll solve all my problems. Well, no, it won't because the slew rate of your op amp to try and

**Dave Jones:** charge up that huge capacitance is going to be a real could could be a real big deal. So, there is a trade-off there between how much droop you want. So, you've got these conflicting requirements. You want to keep the

**Dave Jones:** capacitance value small because then uh so, the slew rate of the op amp and charging that capacitor will ensure higher speed and higher performance out of your peak detector circuit, but you also want to make it large so that your

**Dave Jones:** droop time is, you know, not going to affect the precision of your measurement. So, you know, it's a real trade-off there between choosing that right value and the choosing the uh right type of op amp. And, you know,

**Dave Jones:** that comes down to practical design and what your actual requirements are. Third problem is a bit of a sneaky one. Dielectric absorption in capacitors. Now, I won't go into it, but suffice it to say that uh capacitors can have a

**Dave Jones:** memory, so to speak, of the charge that was last on them. And as you saw, we can actually short out the cap here. Now, when you short out that cap, depending on the type of the dielectric material used in the capacitor, then that voltage

**Dave Jones:** may not stay at zero. It may actually rise back up due to dielectric the phenomenon called dielectric absorption. There's a whole bunch of deep physics in that to try and explain how that all works, and I won't go into it.

**Dave Jones:** But, that is a real problem for these for a precision peak detector circuit. Not for your just rough and ready ones up here. It's fine. But, if you're trying to do any sort of precision or ultra precision measurements, dielectric

**Dave Jones:** absorption and choosing the right type of capacitor dielectric can be a real big deal. Critical, in fact. So, you choose a low dielectric absorption cap like a traditional polystyrene or even better, uh the Teflon-based caps. So, that circuit's not bad for, you know,

**Dave Jones:** semi-precision or precision, uh most precision applications. But, what if you're after an ultra precision application? We're after the utmost in accuracy, and you can't afford any droop there at all on your capacitor. None. Nada. Zip. Well, this circuit, you know,

**Dave Jones:** may not cut the mustard. Because not only have you got input bias current in there, right? But, uh as I've done a whole video on, but of course you can choose an op amp with incredibly low, you know, femto amps input bias current.

**Dave Jones:** So, that's not a huge deal. But, the diode, uh-huh. Typically, in an ultra precision application circuit, the leakage of the diode, the reverse leakage, remember when this thing when this output voltage here drops down low like that, then this diode is

**Dave Jones:** effectively connected down to ground here. It's reverse biased. We're going to get some leakage current through that diode. And that's going to be that can be higher than you can get in a typical FET input, you know, really

**Dave Jones:** low bias op-amp. Now, this rather clever and elegant circuit does just that. Let's have a quick look at how it works. Now, what we've done is we've added in two diodes here instead of one. So, just ignore this op-amp and this feedback

**Dave Jones:** resistor here for a minute. It works exactly the same as before. It doesn't matter whether you have one diode in there or two or 10. Well, apart from your apart from the losses the op-amp's got to compensate for, doesn't really

**Dave Jones:** matter. So, let's start by assuming that this diode is not here. We've got our buffer. Then this output voltage, of course, equals the peak of the input voltage, the voltage across the capacitor. But when the input drops back

**Dave Jones:** low again, then this output the output of the op-amp's going to try and drag all that low. But not you know, and this diode is going to be reverse biased. But if we add this resistor in here, feeding

**Dave Jones:** back that peak output the the voltage on this side, effectively feeding that signal back to here, then the voltage across that capacitor, when it's at peak value, actually becomes zero. There's zero volts across that diode there. What happens when

**Dave Jones:** there's zero volts across that diode? Well, there's zero leakage current. You can't get any leakage current going back through that diode when it's zero like that. So, bingo. This clever little circuit has just eliminated the leakage current through that diode. Beauty. Now,

**Dave Jones:** if you want to get into the nitty-gritty detail of it, yeah, technically there's still reverse current flowing through this diode here because the output here is saturated low. It's gone boom, hard negative like that. So, and you've got a

**Dave Jones:** voltage here. So, you're still getting leakage through there, but it's not affecting the value on the capacitor. It's just flowing through this feedback resistor here, and it's going to be not worth worrying about, negligible. So, your input bias current on your op amps

**Dave Jones:** is now going to dominate cuz you've eliminated totally the leakage through that diode there. And of course, as we've seen in the tutorial previously on input bias currents, you can get very very low ones, you know, in the order of femtoamp

**Dave Jones:** op amps. And you're going to need two because not only do you have the bias current flowing in there like that, but you've also got the bias current flowing in there cuz that's connected in parallel across the cap. So, you're

**Dave Jones:** going to want want to choose two pretty schmick op amps in there. So, there you have it. That's the basic implementation of a peak detector. Got a fairly crude one up here, but still quite useful for a lot of practical non-precision

**Dave Jones:** applications. Then you've got a sort of a semi-precision to a precision type. And then you've got your ultra-precision down one here one down here, which sort of takes into account and eliminates your diode leakage in there. Brilliant. And you can also reverse these circuits

**Dave Jones:** and use them for the negative scenario down here as well, but we won't go into details. It works exactly the same way. And to the breadboard for a quick verification of that, I've just got a basic little diode cap one in here,

**Dave Jones:** crusty 4148 diode and just a 0.7 microfarad film cap. Let's take a look at the circuit. And I'm feeding in a sine C waveform here. You can see that. It's repetitive. It's at at about a kilohertz at a

**Dave Jones:** kilohertz actually. And you can channel one is of course the input waveform and channel two, the green waveform there, they're both centered about the middle. And uh there we go. We're getting our one diode drop in there. You can clearly

**Dave Jones:** see that around about that 0.6 volts where both 1 volt per division there. And there's no droop at all because there's basically very little load on our capacitor. The only load, of course, um the 10 meg input impedance of our

**Dave Jones:** scope probe. That's it. And if we drop the frequency down to 100 hertz, you can maybe just see a couple of pixels in there. The scope The resolution of the scope's not good enough. You see a little bit of a droop, little bit of a

**Dave Jones:** recovery. If we switch down to 10 hertz, we'll see it even more. There we go. We can start to see it. But, of course, we've got I've got a very small load on here and a reasonable value cap. I mean,

**Dave Jones:** 0.47 microfarads is no slouch. And if we drop that down to a 1 nanofarad cap, right back at 1 kilohertz, you can really see the droop now. There it is. Pretty horrible, but that's what you get from 1 nanofarad, even with a you know,

**Dave Jones:** a 10 meg input impedance from the scope probe. There's no load on there at all. So, look, you have very little time in there to actually reach your value before it starts to droop off and you get significant error pretty quickly.

**Dave Jones:** Now, what I've got here is a 100 nanofarad capacitor in parallel with a 10k cap. And you can see the droop or the decay in that. And if we have a look at the time period here, this is a 100 hertz

**Dave Jones:** signal, by the way, and it decays faster than that before it has time to recover. And it's with 2 milliseconds per division. So, it's taking about 500 milliseconds or sorry, 5 milliseconds or thereabouts to decay back down to zero.

**Dave Jones:** And that's really what you'd expect cuz the rule of thumb is about five times the RC time constant. So, five times RC. 100 nanofarads, 10k. There it is. It's about 5 milliseconds. So, that's your effective reset time of your signal.

**Dave Jones:** But, let's increase the frequency here, shall we? And you'll notice that once we get in here, I mean, it's fully reset. I mean, it's back down to ground. It can't go any lower than ground, of course. So, let's increase the frequency and you'll

**Dave Jones:** see that it can we can make it bump back up quicker like that because it's following that input signal like that. So, you can see how your reset time effectively by putting the parallel resistor across there is a compromise between the

**Dave Jones:** accuracy or how quick you're going to actually read out the value or how, you know, quickly you're going to use it and the effective reset time because it hasn't had time to reset before it boop, it's just, you know, jumped back up

**Dave Jones:** there. But anyway, let's get rid of this horrible diode drop in here. Let's go to our precision rectifier. Now, here's where we're going to really see the difference between how things should work on the whiteboard in theory and how they actually work in practice

**Dave Jones:** and how there's lots and lots of traps. Now, I could go on all day with this, but we're only going to keep this relatively quick. Now, what I've built up here is my precision rectifier. I'm using a just a bog standard 1N4148 diode

**Dave Jones:** here, nothing special. I've actually got no capacitor installed at the moment and my load is 1 meg in parallel with my 10 meg scope probe, but you know, let's say it's an order of magnitude bigger. Let's say it's a 1 meg load on here and we've

**Dave Jones:** got that precision rectifier configuration in there. I'm using a TS912 op amp. It's not a bad little rail-to-rail CMOS op amp. It can drive 40 milliamps. So, it's not bad at being able to charge up a decent value of cap

**Dave Jones:** in there. So, there's no cap at the moment. So, all we're doing is I've I'm powering it from plus minus 5 volt rails. I'm feeding in a 100 hertz sine wave, as you can see in there, at 1 volt RMS. So, we're well

**Dave Jones:** within our supply rails. Everything's going to work just fine. Now, channel one is connected to the input there, so that's the yellow waveform. You can see the sine wave in there, and channel two is the output of the op amp, which is

**Dave Jones:** going to be the green waveform here, and channel three is the blue waveform is our output voltage. Now, as you'd expect, here it is. The output voltage, the blue waveform, follows the input waveform precisely. That because there is no capacitor on

**Dave Jones:** here, otherwise it would store the voltage at the peak value on there. But, we'll have a look at that in a minute. So, it follows the input waveform exactly, and then it gets clipped because it's a precision rectifier, it

**Dave Jones:** gets clipped at that 0-V rail there. All three channels are 0-V in the center. But, you can see, as we said, the output of the op amp here, the green waveform, actually goes down there and saturates down at the bottom rail.

**Dave Jones:** That's actually a different voltage scale, 2 V per division. Maybe the others are 500 mV per division. So, 2 4, there's our negative rail, 5 V there. So, you can see that the op amp spends a lot of its time

**Dave Jones:** saturated down there, and then it's got it won't be able to ramp up instantly. You see that? It can't, you know, the op amp has a certain slew rate. It's got to charge the capacitance, in which case there's no capacitance at the moment.

**Dave Jones:** So, that's why, even with a 100-Hz waveform, as you can see, low frequencies, we kind of run into a few problems here. Now, let me install a 1-nF cap. I will Here we go. I'm going to put a 1-nF cap in there. I still got

**Dave Jones:** my load, okay? So, you can see how it's sort of, you know, it, you know, it's draining off pretty quick with that load on there, okay? So, the droop basically follows the input waveform, basically. So, let's remove the load resistor now. So, we'll take

**Dave Jones:** out the load the 1 meg load resistor and see if that improves it. Bingo. Look at that. We've just now So, we've got a 1 nF storage cap on here and you can see it drooping down and it droops down and

**Dave Jones:** when the input goes uh back up, it follows that and then stores that charge with a bit of droop there. And as you can see, the op-amp spends most of its time saturated down at the negative minus 5 V rail and

**Dave Jones:** only when it starts to when it needs to do work again, does it ramp back up and then follow that input. But, you'll notice that there's a bit of oscillation in there. Look at the output of that op-amp. There

**Dave Jones:** we go. It's oscillating a bit. Hmm, this could get even worse. Now, what I've done is actually installed a 1 100 nF cap here. So, 0.1 microfarads and as you can see, you know, there's not much droop. We've got no load at all

**Dave Jones:** on here. So, obviously, it stays pretty much at that peak value all the time. But, look at the output of this op-amp here. It's just dancing around like this and you'll notice that it's even skipped some here or it's got very

**Dave Jones:** low value pulses down in here because it skipped it because it's determined the circuit has determined that uh it hasn't drooped enough in order to warrant switching on that uh at the output of the op-amp again. But, say in

**Dave Jones:** this case over here, for example, this one here where it's you know, it's almost switched back on and it's well, it it has started, right? The output of this op-amp has started to go back up high, but it's determined, "Ah, I don't

**Dave Jones:** need to do that anymore." Boom, because its slew rate wasn't fast enough in order to charge up that cap again. So, you get this effect where you get these missing pulses in there like that. And now, if we install a 1

**Dave Jones:** meg resistor back in here with our 100 n cap, look at this. Now, we get two pulses in there, and this is rather interesting. If we go in and have a look at this, look at this. It's sort of, you know,

**Dave Jones:** there it is. Boom. It recovers once, it droops down again, it knows, and then the circuit goes, "Oh, I need to switch back on." Boom, to ramp back up, and there you go. So, you get Now, we get

**Dave Jones:** two pulses per waveform to try and charge it back up because we're getting that droop caused by that 1 meg resistor. And if we replace this 1 meg resistor with a 100 K resistor, look at that. We get even more

**Dave Jones:** peaks in there because it's got to charge up that cap more times. Isn't that fascinating? Look at that. And I'm going to start from 200 Hz here, and I'm actually going to wind the frequency down, and look at this. It

**Dave Jones:** just adds more and more pulses in there as we drop down in frequency because the frequency of our input waveform that it's trying to track, you'll see that it tracks more and more times in there because the uh input frequency, now

**Dave Jones:** we're down at 10 Hz, and our input frequency is much, much lower than the um how fast our op amp is. So, it's able to um slew fast enough to do all of Let's stop that. It's able to slew fast enough to do

**Dave Jones:** all of those little to sort of, you know, chop up and track that input waveform like that. And if you start getting up too high in frequency and you have too large a load on here with the uh discharge, then you can notice that

**Dave Jones:** we're actually getting some sort of overshoot on our output voltage here. Now, that's at 100 hertz. Where is it? Oh, I had it there. Yeah, there it is. 100 hertz. And if we bump that frequency up to 1 kilohertz, look at this. We're

**Dave Jones:** now starting to get some very large errors and overshoots on our output signal. But if we take off our hand and that's with a 100k by the way, but if we take off our 100k load, bingo, look at

**Dave Jones:** that. It's recovered. So, as you can see, you really do want to try and keep the value of this capacitance, you know, fairly low in order to get the performance that you're after, but then you need a real high impedance load over

**Dave Jones:** here. So, at the moment I've got a 100n in there and if I change that 100n back to Tada! There we go. That's a 1n. There we go. Then we're following that much more nicely and the op-amp is only going

**Dave Jones:** berserk at the start here and then it's, you know, then it's acting like you're really, really tracking the input very nicely around here. So, there you go. That's, you know, that's the sort of trade-off you're going to get and this

**Dave Jones:** is with no, effectively no load. Well, the load is my scope probe. It's the 10 meg of my scope probe because the input impedance of the input bias current on this op-amp is only 1 picoamp. It's a very low one. So, you know, there's

**Dave Jones:** nothing in there. There's going to be some diode leakage in there, but yeah, we've got our 10 meg scope probe. And in this case, the leakage of our 1n4148 diode, it's going to vary a hell of a lot with temperature, but at room

**Dave Jones:** temperature, you know, it's going to be in the order of like 25 nanoamps or something like that. So, that's like, you know, 1/4 of our 1 meg load or something like that. So, you know, it it does um, add up, but you know, so we

**Dave Jones:** should be using a better diode in here. And of course, in a precision, uh, you know, circuit, you would certainly use a better diode than a 1N, uh, jelly bean 1N4148. And of course, just remember that the, um, input impedance of your scope is not

**Dave Jones:** is not just going to be 10 meg. It's going to be 10 meg at DC, but as you go up in frequency, of course, the input capacitance on here is going to dominate that thing. So, uh, at at 100 hertz that

**Dave Jones:** we're talking about here with our, uh, 11 picofarads input cap of our, uh, times 10 probe, we're only talking about 144 meg. So, it's, you know, it's basically the, uh, DC resistance of the probe dominates at 10 meg. So, as you

**Dave Jones:** can see, there's lots of tricky AC behavior going on in the circuit, and you can really play around and tweak this thing uh, to get exactly the performance you want until the cows come home. And like, I could do a whole one

**Dave Jones:** or two hour video on just, you know, choosing the right op amps, different loads, and, uh, different types of diodes, and different values of cap, and different values of load, and all sorts of stuff. I you can go for hours and

**Dave Jones:** hours. There's a lot of traps involved in just a simple peak detector circuit like this. It doesn't always necessarily work exactly as you expect on paper, and over frequency range as well. There's all sorts of traps. So, they just be

**Dave Jones:** careful when you're building practical circuits like this. There can be a big difference between the, uh, whiteboard theory and what you get in practice. Anyway, this video's, uh, gone long enough. It's longer than my usual fundamental Friday. So, I'm going to

**Dave Jones:** leave it up to you to go and play around with a, um, peak detector circuit and precision rectifier like this, and try and learn exactly what's going on here by playing around with all the values and trying to understand how it all

**Dave Jones:** works. So, I hope you like that and if you do like Fundamentals Friday, please give it a big thumbs up. And if you want to discuss it, the EEVblog forum is the place to do it. Catch you next time.
