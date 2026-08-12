---
video_id: rrPtvYYJ2-g
title: EEVblog 1417 - AC Basics Tutorial Part 1: Alternating Current
url: https://www.youtube.com/watch?v=rrPtvYYJ2-g
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 27, "3": 43, "4": 61, "5": 76, "6": 92, "7": 109, "8": 126, "9": 142, "10": 160, "11": 174, "12": 192, "13": 210, "14": 227, "15": 242, "16": 255, "17": 272, "18": 282, "19": 295, "20": 309, "21": 320, "22": 334, "23": 350, "24": 365, "25": 383, "26": 398, "27": 413, "28": 430, "29": 447, "30": 464, "31": 479, "32": 491, "33": 504, "34": 521, "35": 538, "36": 554, "37": 570, "38": 588, "39": 604, "40": 622, "41": 643, "42": 661, "43": 675, "44": 693, "45": 706, "46": 721, "47": 736, "48": 747, "49": 765, "50": 781, "51": 799, "52": 812, "53": 830, "54": 844, "55": 863, "56": 879, "57": 892, "58": 907, "59": 921, "60": 936, "61": 950, "62": 963, "63": 978, "64": 991, "65": 1005, "66": 1016, "67": 1029, "68": 1040, "69": 1052, "70": 1063, "71": 1076, "72": 1088, "73": 1101, "74": 1112, "75": 1124, "76": 1137, "77": 1152, "78": 1164, "79": 1178, "80": 1194, "81": 1209, "82": 1222, "83": 1235, "84": 1251, "85": 1263, "86": 1275, "87": 1290, "88": 1306, "89": 1322, "90": 1338, "91": 1357, "92": 1373, "93": 1387, "94": 1407, "95": 1422, "96": 1437, "97": 1454, "98": 1469, "99": 1483, "100": 1497, "101": 1507, "102": 1525, "103": 1541, "104": 1557, "105": 1577, "106": 1591, "107": 1604, "108": 1619, "109": 1635, "110": 1654, "111": 1681, "112": 1698, "113": 1711, "114": 1724, "115": 1741, "116": 1755, "117": 1771, "118": 1785, "119": 1798, "120": 1813, "121": 1825, "122": 1841, "123": 1857, "124": 1874, "125": 1891, "126": 1910, "127": 1925, "128": 1937, "129": 1949, "130": 1963, "131": 1984, "132": 2002, "133": 2018, "134": 2031, "135": 2042, "136": 2054, "137": 2067, "138": 2081, "139": 2095, "140": 2111, "141": 2122, "142": 2134, "143": 2148, "144": 2163, "145": 2179, "146": 2192, "147": 2205, "148": 2219, "149": 2227, "150": 2240, "151": 2253, "152": 2267, "153": 2280, "154": 2295, "155": 2310, "156": 2321, "157": 2335}
---

**Dave Jones:** Hi, in previous series we took a look at DC circuit fundamentals and there was quite a few videos and we covered lots of stuff including inductors and capacitors and transient circuit analysis as well which you a lot of

**Dave Jones:** people might have thought was actual AC circuit theory but it's not it's DC transient circuit theory cuz as we're going to look at today we're going to do an acadaca and we've got to look at alternating current basics. So now we

**Dave Jones:** have to move on to AC circuit theory and that includes AC signal generation, the importance of sinusoidal waveforms as we'll see in this video and then on to AC circuit theory which can actually be pretty much identical to DC circuit

**Dave Jones:** theory the AC Ohm's law as we'll look at in future videos but it can also be surprisingly different in many ways. So let's have a look at alternating current basics. So what is alternating current compared to DC or direct current? Well,

**Dave Jones:** it's obvious it alternates polarity. If we've got our waveform like this DC would just be like this is zero volts, this is one volt or wait got current here. So let's say zero amps one amp up here DC direct current would be just a

**Dave Jones:** straight line like that. It would just be one amp but alternating current it changes direction. It's positive up here in this case positive one amp and then it goes negative one amp like this. It physically changes direction in the wire

**Dave Jones:** like that. The current the electron flow actually changes direction. And that's pretty much the definition of AC or alternating current which is confusing cuz you can go AC voltage and it's like or alternating current voltage that doesn't make sense but that's the

**Dave Jones:** terminology AC voltage. You'll find lots of stuff like that in engineering but and And pretty much the definition of AC. Is it really has to change polarity like this. If you've just got DC up here, which might have some ripple on it

**Dave Jones:** like this, that might look like alternating current, but it's still direct current with ripple. And yeah, flame wars in the comments down below the difference between is this actually AC and is it DC? Anyway, we'll get into the details of

**Dave Jones:** this, but suffice it to say for this video, we're talking about alternating current that's physical current physically changing direction. And this is super important theory because most of our power generation and our telecommunications RF signal transmission, this all happens

**Dave Jones:** in the AC domain. And this all happens with the sinusoidal wave like this. And there's actually something very special about the sinusoidal wave as we'll go through in a minute. Now, the sinusoidal wave shape like this comes about

**Dave Jones:** naturally in rotating magnetic fields like you get in generators, which is used for most of our power generation, be it wind turbine generators, hydropower generators, steam power generators, which are also nuclear nuclear energy just heats up steam basically, which

**Dave Jones:** then drives a a turbine which drives a generator like this. And that generates always a sinusoidal output. Actually, you want as close to a perfect sinusoidal output like this as possible on a generator for reasons that we're going to get into.

**Dave Jones:** So, we're going to look at how a basic generator here works. And this brings us back to a formula you've seen before in even DC fundamentals when we talked about inductors. Faraday's law of electromagnetic induction. The induced voltage in volts is negative the change

**Dave Jones:** which is Lenz's law, won't go into details, watch previous videos. The change in the magnetic flux in Weber's per second. So, basically, the phi dt here just means the change of magnetic flux over time in Weber's per second.

**Dave Jones:** And that's it. And then I won't derive how we actually get down to here, but basically, this formula here you should pretty much remember along with Faraday's law. This is the formula for the induced voltage in a conductor in a

**Dave Jones:** magnetic field and it's equal to the flux density in Teslas B multiplied by the length of the conductor at 90° to the magnetic field in meters multiplied by the velocity of the conductor through the magnetic field in meters per second.

**Dave Jones:** Simple. And of course, we've got all that stuff inside a generator like this. So, let's have a look. We've got a north pole of a magnet, south pole of a magnet like this. We've got a shaft in there

**Dave Jones:** like that which contains a core and that red part around there is just a single turn coil. Of course, it could be multiple turns. You wouldn't have a single turn coil in there. Not very efficient. But we'll run with a single turn for today.

**Dave Jones:** And the wires come out here like this. Now, I won't get into details of how the power actually gets out of there. I won't go into like the mechanical slip rings and everything like that. Doesn't matter, okay? Basically, voltage current comes out of

**Dave Jones:** the coil like this as it rotates in a magnetic field. And if we have a look down here, this is like a side cross section of this 3D model up here. Please excuse the crudity of model. have time

**Dave Jones:** to build to scale or to paint it. North and south pole here. We've got a uniform magnetic field through here. Let's just assume that it's a uniform magnetic field. And then we've got our coil here and here like this. And the

**Dave Jones:** coil will rotate through the magnetic field like that and go around and around and around. And this will actually produce a sinusoidal wave shape. How does it do that? Basic trigonometry. You learn in uh school. If we uh take like

**Dave Jones:** the vertical axis like this as the the angle of the coil like this is theta here, and theta is the angle. And of course, you know your basic trig trigonometry, it's just sine theta is the angle through that field. So, as it

**Dave Jones:** goes through, it actually naturally develops, assuming you've got a uniform magnetic field and everything's hunky-dory, you get a sinusoidal wave shape out like that. And when the coil is right in in the horizontal position like this, this is the actual maximum

**Dave Jones:** uh velocity through the magnetic field like this. It's at its highest velocity at this point. So, at 90° like that, this is when you'll generate your peak voltage here and here like this, depending on which orientation it is.

**Dave Jones:** Depends on which whether it's positive or negative peak. But when it's up right at 90° like this, it's not There's basically no movement through the magnetic field. The velocity drops to zero cuz it's not going through the magnetic field. The

**Dave Jones:** magnetic field's going in this direction. It's basically It reaches a point where it's it's zero. So, here here here, it's basically generating nothing when the coil is vertical like that. Pretty simple. But that's your basically basic formula for

**Dave Jones:** induced voltage in a magnetic field. So, basically our maximum voltage here, our peak voltage we're going to get is B * L * V. So, the instantaneous voltage here, so let's Well, this could be E. Voltage here, the instantaneous

**Dave Jones:** voltage at any point in time here equals E max, which is the maximum, assuming it's like one up there, multiplied by sine theta, the angle of the coil in the magnetic field. So, therefore, you end up with that sinusoidal shape. Simple.

**Dave Jones:** So, in basic maths, when you're talking about sinusoidal waves and cosine and and tangents and everything else, you might talk in terms of degrees like this. So, 0°, 90°, 180°, 360°. And in electronics, we do uh talk about and in

**Dave Jones:** engineering, we talk about uh degrees in terms of phase difference. So, if you have two waveforms and they shift like this, we generally talk in terms of uh degrees. But, what's more helpful to use when it comes to talking

**Dave Jones:** about AC stuff is to talk in what's called angular frequency. So, we use W to represent that, which is actually uh omega in the Greek alphabet. It's not just the ohm symbol, it's also the little W thingy. Anyway, Greek alphabet

**Dave Jones:** rubbish. Anyway, equals 2 pi f. So, we talk about this in terms of pi. So, 90° is actually pi on two. 180° is just pi. And 270° is 3 pi on two or however you want to represent that. And 2 pi is

**Dave Jones:** 360°. I.e. a full cycle of an AC waveform like this. Because one thing I actually didn't point out before is like another definition of AC or something that it needs to include this to be like deemed to be AC. And this is what

**Dave Jones:** differentiates it from uh the transient analysis in DC. You just have a single transient like this. AC actually has to have a frequency. It's got to have a period. And it's got to uh basically repeat that for infinity or X amount of

**Dave Jones:** time to really be considered AC AC in quote marks. So, yeah, it's it's got to be more than just If it's one cycle, hmm. If a tree falls in a forest, do you hear it? And if you've only got one cycle, is

**Dave Jones:** it still AC? Comment down below. Anyway, the angular frequency is 2 pi f and you'll find this 2 pi everywhere in electronics and 2 pi f is very important and in this case we're talking about angular frequency like this instead of

**Dave Jones:** degrees. Anyway, this is in units of radians per second. So we can do once again the instantaneous voltage e equals e max times c sine omega t like this and then if you run it through the wash t

**Dave Jones:** equals 1 on f and with t being your time period like this and well that's one of the most fundamental equations in all of electronics. How I convert time into frequency. It's just inverse and this by the way is why your computer

**Dave Jones:** here almost certainly has a degrees and radians and gradients button. Gradients some weird French thing that surveyors might still use. I don't know. Degrees and radians mode. Your calculator's got it. Guarantee it. That's what it's for. So that's what it's for on your calculator.

**Dave Jones:** Degrees, radians or gradients which is like 400 gradients for one one time period, one t, one turn of your generator is 400 gradients. Meh. Anyway, radians. Beauty. So if we do pi on our calculator in radians mode like this and

**Dave Jones:** get the sign of that it's zero because it's in the middle of the wave that we saw there. But if we do pi divided by two equals and then sign, it's one cuz that's when our wave form peaks right up

**Dave Jones:** there. Beauty. And then three times pi divided by two equals sign minus one. The maths works. And once again with all this stuff you can really go down the rabbit hole to the physics side of things and advanced mathematics of it

**Dave Jones:** and everything, and it's like, nah. But anyway, let's get on to the importance of the sine wave and more circuit theory related stuff, cuz I know that like motors and generators might be boring, but it's important that you know where

**Dave Jones:** that sinusoidal wave shape can come from physically. And it does in the real world. You know, probably a majority of the power that comes out of your power point was generated with a with an AC generator like this. So, I mentioned before

**Dave Jones:** specific benefits of sinusoidal AC. So, let's take a look at them. And this basically applies to sinusoidal shape ACs, cuz it's the ideal AC waveform. Sure, you can get square waves, which are AC, and you can get triangular

**Dave Jones:** waves, you can get all sorts of, you know, pulse width modulator waveforms, which can be AC and all sorts of stuff. But in particular, sinusoidal ones have specific benefits. Let's take a look at them. It's easy to physically produce

**Dave Jones:** high powers, as we looked at. Those generators. This is how the vast majority, probably, of the power that you're using is generated using perfect sinusoidal AC from a generator. Sure, of course, these days solar's a big thing, and it generates

**Dave Jones:** DC, but you know, still the majority is probably going to be coming from some sort of AC generator, be it wind, hydro, coal, nuclear, whatever it is. And because the sinusoidal waveform is only one frequency, you know, I'll talk about

**Dave Jones:** that more about that in a minute. It's easy to efficiently transform and isolate these voltages using transformers. So, so you go from like 500,000 V, 500 kV, or even 700 kV, I think, these days. AC transmission lines, these

**Dave Jones:** huge ones, they're easy to step down, and you can do that very efficiently using AC, sinusoidal AC, in transformers. They're incredibly efficient and you can use those at the signal level as well if you're designing circuits, audio and other

**Dave Jones:** telecommunications type stuff can be isolated using transformers. Easy peasy. Because a transformer's just a coil of wire and like a piece of ferrite, it's really simple stuff. And it's what's used for all basically all RF and communications technology. Is basically

**Dave Jones:** you can't just put DC on an antenna and have it transmit something. It's got to oscillate. And if it oscillates using a sine wave, that is one pure frequency. Because don't want to go into in this video, but you've probably heard me

**Dave Jones:** mention Fourier before. And Fourier's theorem or Fourier transforms if you've heard about FFTs in basically oscilloscopes, this is how like a spectrum analyzer works in your oscilloscope, Fourier transforms. Fourier theorem basically says that any wave shape at all is made up of sine

**Dave Jones:** waves. So, if you've got a square wave like this, it's actually made up of sine waves at lots of different frequencies. So, when you plot a frequency spectrum instead of time and that's F. That's supposed to be F there,

**Dave Jones:** trust me. Frequency like this, if you've got a sine wave, it's just one line on your spectrum analyzer. Say that's 1 kHz or something like that. And then you might have another line here at harmonic multiples of that, things like that. But

**Dave Jones:** any waveform, doesn't matter what it is, sine, square, triangle, wiggly piggly, your heart uh you know, cardiac waveform or whatever, it can be made up, as long as it's periodic, can be made up of sine waves. And if you've only got one sine

**Dave Jones:** wave, then you can actually transmit exactly on that frequency. There's no other harmonics either side of it. So, you can fit a lot more different bits of information in the same bandwidth using different frequencies. And that comes down here,

**Dave Jones:** they can be sharply filtered as well. So, that allows all sorts of RF and you know, telecommunications magic to actually happen. All done with sine waves. And as we've seen, sine waves are naturally produced in generators, but they're also produced in oscillator

**Dave Jones:** circuits as well. Wien bridge oscillators, Colpitts oscillators, you know, phase shift oscillators or whatever. And also when you filter stuff, what comes out of it? If you've got a simple RC filter and you feed a square wave into it, it could be LC RC,

**Dave Jones:** it could be an active filter, whatever it is. Feed into a filter, what comes out? Hopefully, a perfect sine wave. The better the filter, the more perfect a sine wave comes out. And this is a really interesting point. The sinusoidal

**Dave Jones:** wave shape is the only wave shape that is not distorted by when it passes through capacitors and inductors because well, that's what magically comes out. So, if you feed in a sine wave, you're going to get a sine wave out of a filter

**Dave Jones:** even though the filter's made up of inductors and capacitors and well, that's an inductor there. Little hairy resistor. Is it an inductor? Who knew that? Anyway, you feed that in and it's not you can filter them out, but the

**Dave Jones:** actual wave shape is not distorted by those components. Whereas if you looked in the previous videos of DC fundamentals where we looked at transient circuits in capacitors and inductors, yeah, they it actually distorts them. And yes, I know if you

**Dave Jones:** feed a square wave through a series capacitor like that with no load, then you're going to get a square wave on the output except that if this is DC here, the DC will now be it DC will be removed

**Dave Jones:** cuz it's an AC coupling capacitor. It removes all the DC. But anyway, once you start trying to drive that into a load and actually passing like a large current through that, yeah, you're going to come a cropper. Also, sinusoidal AC

**Dave Jones:** is great for motor drives and things like that. get multi three phase or multi phase motor drives and stuff like that. Really efficient stuff. Anyway, but some of the problems with AC, of course, well, you can't store it, of

**Dave Jones:** course, like you can in batteries. It just sits as electrochemistry inside a battery. And it's not actually not that easy to measure, as we'll look at in a minute. You basically have to let rectified in order to measure the value

**Dave Jones:** of it, unless you do it in this other ways you can do it. But anyways, it's actually not as easy to measure as DC. And basically, AC is not a thing and even can be a problem for like much of

**Dave Jones:** the electronics out there. All your digital stuff and all the other things, like your DC power supply, you want a rock solid 3.3 volts or 5 volt supply. If, as we saw before, like it has some ripple on you know, if it's got some

**Dave Jones:** ripple on there, if you got some 50 hertz ripple from your transformer power supply or something like that, that can ruin your day. You don't want that. You want to get rid of AC from any sort you know, it's a much of modern electronics.

**Dave Jones:** But it's useful for a whole range of stuff. So, there's tons of benefits to sinusoidal AC, and that's why it's a pretty much the ducks guts in this sort of like high power and RF stuff and things like that. You just can't do the

**Dave Jones:** same sort of stuff you can with DC, at least not easily. And yes, you can actually transmit power using DC high voltage transmission. I've actually done a video. I'll link it in down below and up here. It's very interesting about

**Dave Jones:** high voltage DC transmission. It's over on my EV log 2 channel, so check that out. But basically, yes, you can use DC to like transfer large amounts of power over transmission lines and stuff like that. But then ultimately, you've got to

**Dave Jones:** like chop it up and do some DC stuff to DC to AC conversion to actually convert it, and then basically convert it back to DC. So, you're never going to escape AC. And all of your DC to DC converters,

**Dave Jones:** all your switch mode power supplies and things like that you're so used to using in modern electronics, well, it's DC. It's chopped up. It becomes AC, basically. And that's what you're feeding through the transformer. And this brings us to some really important

**Dave Jones:** terminology you use all the time in electronics and it can be used for both voltage and current. So, we're just going to use voltage here. So, we've got our original waveform like this doesn't have to be sinusoidal. We'll get into

**Dave Jones:** that. So, basically got four different ways to define the voltage of this waveform. As I said, it's actually not that easy to measure let alone be able to communicate what the actual value is to somebody else. So, what we've got is

**Dave Jones:** four different ones. We've got peak, peak to peak, average, and RMS or what's called root mean square. So, a peak, the voltage peak here is from zero or a reference point. Doesn't necessarily have to be zero, but it's defined as the

**Dave Jones:** reference point of the waveform and because it's AC, it'll go negative as well. So, the peak value is simply the value where it reaches absolute maximum in one direction like that relative to the reference. In this case, it's one

**Dave Jones:** volt. So, you might say one volt peak and it'll be usually represented by either PK or just P. If you just see P on its own, you know that's peak. But, the peak to peak voltage as it's called

**Dave Jones:** is the value from the negative excursion bottom down here to the positive excursion up here like that. That is your peak to peak voltage and if you got a symmetrical waveform, the peak to peak voltage is going to be twice the peak

**Dave Jones:** voltage, obviously. Now, one of the downsides about peak and peak peak voltages while they're very commonly used, they don't actually tell you anything any information at all about the way the actual waveform shape. It doesn't actually care. This could be a

**Dave Jones:** perfect sine wave, could be a triangle wave, a square wave, it doesn't matter what this waveform is. If it goes to plus one up here and minus one down here, it it doesn't matter. It could have a tiny little spike like this, tiny

**Dave Jones:** little spike down here. It could be like a you know, that could be a very poor power factor as we've looked at. Way means way form or something. The peak-to-peak, it doesn't matter what the wave form is. The peak-to-peak is just

**Dave Jones:** the actual instantaneous peak value like that. But average and RMS, they're different. They actually take into account the actual wave form itself. Now, the average value is defined as this. And there's several different ways to sort of explain it, but this is the

**Dave Jones:** way I'll do it. It's the total area under the wave form divided by the period of the wave form. So, the total area under the wave form, that means all this area under here like this like to the axes. You got to have it like to a

**Dave Jones:** reference axes. So, all the area under there, but we've also got all this area under here. And this one's positive, and this one's negative. And because it's a perfect sinusoidal wave form, or it could be a perfect square wave

**Dave Jones:** for example, it doesn't actually matter if the area above the axes here is equal to the area below the axes here, and they're both the same amplitude like this, the average value will actually come out at zero. So, if you feed an AC

**Dave Jones:** voltage, a perfect AC voltage with no DC offset, into your DC multimeter, which reads average value, it'll read zero. And also for multimeters that aren't true RMS multimeters, that'll have true RMS written on them, usually they will actually be what's called an average

**Dave Jones:** responding multimeter for AC. So, what that means is that it assumes that the wave form you're measuring in AC voltage mode or AC current mode on your multimeter is a perfect sine wave. If it's not a perfect sine wave, it's going

**Dave Jones:** to give you an error. It's not going to be accurate. Because the multimeter has only been calibrated to assume a perfect sine wave. To give you another example from digital electronics you might be familiar with if you've got a

**Dave Jones:** V here so that that goes up to 1 V there. This is time and if you've got a pulse width modulated square wave that is like this let's say that this is 10% of the time this and it's zero 90% of the time like this.

**Dave Jones:** What is the average value going to be? Well, our axis is zero volts down here like this. Everything's above the axis it's not actually an AC waveform it doesn't go negative but this can actually apply to it doesn't matter

**Dave Jones:** where the reference point is. Our reference point in this case is zero okay? The total area under the waveform so the period from here to here it'll be 1 V for 10% of the time multiplied by 90 V

**Dave Jones:** for 95% of the time. So therefore it'll actually equal 1/10 of that or 0.1 V will be your average value over the period of one waveform. So let's analyze a half-wave rectified sine wave and you'll be familiar with this if you've

**Dave Jones:** done made any do-it-yourself basic power supply from a transformer. So this is how AC transformer just got a single diode in there and just driving a load there's no filter capacitor because that smooths it out and ruins your day. So

**Dave Jones:** we've got a waveform that looks like this. It's here's our total period here from zero to 2 pi or zero to 360 degrees and it's as its name suggests is a half-wave rectified. It only rectifies the positive half. The other half of the

**Dave Jones:** waveform down here when it goes negative the diode is reverse biased so it doesn't conduct at all so you just get zero. So you get this half-wave rectified waveform. Now we'll analyze this waveform using our formula here and

**Dave Jones:** several different ways to look at it, but because it's a sine wave, what I'm going to do is like this half of the sine wave from here is identical to this half here. So, what I'm going to do is

**Dave Jones:** just split it into quadrants like this. So, I just assume that there's like four different areas that we're calculating here for our one waveform from zero to 2 pi. So, it's the area of A here plus the area of B plus the area of C plus the

**Dave Jones:** area of D. You remember it's the total area under the waveform divided by the period of the waveform, which is 2 pi. So, area A plus B plus C plus D divided by 2 pi. Now, we'll just normalize the area to one. We'll just

**Dave Jones:** call it one cuz we're not talking about any actual absolute value here. So, we'll just normalize it to say that area A is one. Area B is identical to area A, obviously. It's a perfect sine wave. So, 1 plus 1 and then area C and D are of

**Dave Jones:** course zero. There's nothing there. So, it's 1 plus 1 plus 0 plus 0 or 2 divided by 2 pi is equal to 0.318. Not 0.318 V. 0.318 is the factor that you then multiply by your peak value up here. But, that is

**Dave Jones:** just a factor that you multiply by the peak value up here to give you your actual average voltage for a half-wave rectified waveform. And, that's a common number. You'll actually see that a lot and especially when it's to do with like

**Dave Jones:** half-wave stuff. If you see that number, you go, "Oh, yeah, that's half-wave." And, we'll now look at a full-wave bridge rectifier. I haven't bothered to draw it, but basically um familiar with the full I'll put up the circuit here. Here it is. Now, uh this

**Dave Jones:** will give us a waveform that then looks now like this. So, we'll get two humps cuz it does the positive and the negative cycle as well. But, because that's now identical and we've doubled our frequency, say it's 50 hertz here in

**Dave Jones:** Australia, not any of that 60 hertz Yankee rubbish. If it's 50 hertz, and then it actually becomes 100 hertz now because the waveform is repeated. So, our period is not 2 pi anymore, it's just pi like this. So, it's 1 + 1 area

**Dave Jones:** of A + area of B divided by pi, which is 0.636. wait. No, that's Isn't that meant to be 637? Yeah, say again. I 637. Yeah. Why why would it be 637? Because when you go into the calculator

**Dave Jones:** here, if you go 2 / pi equals equals 0.6366. So, you reckon Rounded it up to 0.637. Seven. Well, I'm going to say that it's 636 because that's kind of like symmetrical. And it's double 0.318 that I rounded before.

**Dave Jones:** So, I'm sticking with 636. You reckon 637. I like I'm the type of person who likes symmetrical and all, but Yep. 637. Okay, leave it in the comments down below. Thanks, Sagan. Yeah. Now, the thing about peak peak to peak

**Dave Jones:** and average voltages is that their amps and currents is they're useless for measuring power. You'll get the wrong value. In fact, you'll get zero, cuz let's just assume that this is a current waveform, okay? And you've got it

**Dave Jones:** dissipating power into a resistor. The there's going to be power dissipated in the resistor on the positive half like this. There's going to be power dissipated in the resistor on the negative part of this, cuz power doesn't care whether the voltage is positive or

**Dave Jones:** negative. It's just the power dissipated in the resistor or the load, then well, you're But if you measure the average current, the average current is going to be zero and zero times that P is I squared R, zero squared times R is zero.

**Dave Jones:** So, you got zero power dissipation. Uh-uh. Go try it. Put an AC waveform into a resistor, you're going to dissipate power. So, it doesn't work. In this particular case, we have to use RMS. So, RMS stands for it's right in

**Dave Jones:** the name, the root mean squared. Where does the squared bit come from? Well, power equals I squared R. There's a squared factor in there. And then when you square that, that is the mean squared. So, if we have a look at the

**Dave Jones:** waveform over here for current, we've got our regular AC current waveform, we'll call that IAC here. Then if we square that current, we square it like take every single point on this waveform and square it, the number any negative

**Dave Jones:** numbers, they're going to go positive like this. So, it's going to be squared, so it's going to be much larger like this and it's all going to be shifted up on the positive half of the reference axis like this. So, we'll call

**Dave Jones:** that I squared AC. So, that's where our squared factor comes from. So, what you do is you actually work backwards. You take the square first, then you take the mean, and then you take the root, the square root. So,

**Dave Jones:** we've done our squared business. Let's now take the mean. We've looked at the mean before, the mean is the average, okay? It's just another word for average. The mean, the the average is smack in the middle like that because

**Dave Jones:** it's a perfect sinusoidal waveform. Squaring it doesn't change the wave shape. It simply shifts it up and changes the amplitude like this. So, we'll call that I squared AC average like that. That's our average value. So, we've done our squaring

**Dave Jones:** business, we've done our mean or average business. Now, we need to take the square root of that average value. But, what is that average value? Well, it's pretty easy as we looked at before. This is the peak-to-peak value.

**Dave Jones:** Well, it's the peak-to-peak value of the waveform. It's now the peak value of the waveform. I squared AC is also I squared peak. It's the peak value of the waveform and the mean value is going to be the peak divided by two. It's smack

**Dave Jones:** in the middle. Simple. So, this is I squared max as we'll call it over here. Now, let's actually go through and derive the actual answer for our RMS. And you might be familiar 0.707. We're getting there. Now, the DC power must

**Dave Jones:** equal the AC power cuz that's the basically the definition of RMS is that it's the equivalent heating in a resistor for the same for the equivalent value of DC. So, that's what the RMS value actually is. So, how we derive this is well,

**Dave Jones:** power in DC is I squared R. We learned that back in day one. And the power AC here is actually the average value here. Now that we've squared it, it's no longer zero. It's right up there. It's going to be the average value times the

**Dave Jones:** times the resistance in the load. So, it's of course that average value is going to be half of the peak value I max. So, you can put average in there if you want like AC average in there if you

**Dave Jones:** want, but we'll put half I squared R max. Now, because we've got R on both sides of the equations, we can actually take that out and IDC is equal to the square root cuz we had square here, so

**Dave Jones:** we have to bring it over and now it becomes square root half times that I squared max. And then you can just rearrange that again to be I max on the square root of two. And well, if you say

**Dave Jones:** I max is one, then it's 0.707. That's your answer. But the this is the this is the formula for RMS value is 0.707 times the maximum current there. So anytime you see 0.707 in electronics, you know you're talking about one on

**Dave Jones:** square root of two. And it's basically RMS. And this also applies to voltage as well. So V RMS, the RMS voltage is equal to 0.707 times V max, which is actually V peak to peak. So the equation that you have to

**Dave Jones:** remember is volts RMS equals volts peak divided by the square root of two. Or you can remember the 0.707 if you want, but square root of two will give you a more precise answer. So uh and that, if you just rearrange

**Dave Jones:** that formula, V peak peak voltage equals the RMS voltage times the square root of two. Easy. And there's other formulas which derive, you know, you can go directly from volts RMS to peak to peak or peak to peak to RMS or whatever, you

**Dave Jones:** know, there's various combinations of these. But if you just remember well, if you remember one of them, you can derive the other and then you can derive the peak to peak from the peak, etc. etc. Now, we've only looked at ideal

**Dave Jones:** sinusoidal waveforms, but what if you've got I don't know, a sawtooth waveform like this or you've got like a a high crest factor, we might go into that. Um a waveform like, you know, a current waveform like this. How do you get that?

**Dave Jones:** Well, we start looking at integrals and this is where you get a little bit more advanced uh calculus, which we don't really want to go into here. So the average value one on T the integral from zero to T and then the function of that.

**Dave Jones:** And we won't go into the details. You can do this yourself, but it's basically um an integral is just the area under the curve. And I've done a practical video, I believe, showing this somewhere. I'll try and link it in on on an

**Dave Jones:** oscilloscope. Um the integral is just the area under the curve. So, it's exactly what we did before, but you can actually do the average uh derive you can derive the average formula we did before using integrals and stuff. But anyway, it's

**Dave Jones:** that and the RMS version of it is simply the square root with the squared in there. That's exactly the the it's the squared factor, the mean uh factor, and then the square root in there. So, anyway, we won't go into details. It's

**Dave Jones:** basically just getting the area under the curve. So, you just have to get this area under the curve here, and you can do that using graphical methods if it's just like a sawtooth waveform or something like that, or even uh you

**Dave Jones:** know, a pulse current uh waveform like that, like a poor like power factor on a DC to DC converter. You'll get a waveform like that. I showed that in previous videos. You can do these actually using uh graphical methods, or

**Dave Jones:** you can do it using uh differential calculus. Now, the absolute last thing we're going to look at, I swear for this video anyway, uh just to round this off, is what's called crest factor. And this is important for uh RMS true

**Dave Jones:** RMS uh measurement you might get on your multimeter, for example. This is also known as peak factor as well. And the crest factor or peak factor is Vpeak on VRMS. So, if we've got our waveform here, obviously we've got our peak value

**Dave Jones:** up like this, uh easy, and our RMS value is going to be 0.707 times uh the peak there that we've seen. And that gives a crest factor of 0.414. Beauty. No worries. But if you've got a horrible waveform

**Dave Jones:** like this, like the sine wave is like this, but you've seen this in videos where you might have a uh a non-power factor corrected uh mains power supply, for example, current peaks could be up like this. And if you're trying to

**Dave Jones:** measure, say, with your multimeter using your true RMS converter in your multimeter of this waveform like this, if it has a too high a too high a crest factor like this, your true RMS converter won't be able to handle it.

**Dave Jones:** And you'll often find the maximum crest factor value in the data sheet for your meter or your true RMS converter chip measurement system, whatever it is. So, there's a maximum, you know, they can't tolerate an infinitely small pulse like

**Dave Jones:** this. There's going to be a point where they come a cropper and just go, "I'm going to give the you know, I'm not going to give an accurate value. I'm going to read low." So, you can see that

**Dave Jones:** the in this particular case the the peak value might be absolutely identical, say it's one between the two of them, but because it's much shorter like this, the RMS value, of course, is going to be much lower. It's not going to be 0.707

**Dave Jones:** anymore cuz it's no longer a perfect sine wave. So, it could be could be, you know, 0.2 or something volts or something like that. So, it's going to be one divided by 0.2, for example. It's going to be a crest factor of five. And

**Dave Jones:** that that starts getting up there towards where, you know, your true RMS converter multimeter, cuz there's different methods for RMS conversion, which we won't go into. Maybe I've done that in another video. Don't know. Done so many videos. And yeah, that's

**Dave Jones:** getting, you know, that's getting pretty high. So, once this gets narrower and narrower and narrower or the, you know, the ratio, it doesn't like the waveform could be different. It type of waveform, but the crest factor V peak on V RMS if

**Dave Jones:** that's too high, then yeah, screws up your RMS calculations. And you need, basically, you know, better, faster sampling hardware for your RMS converter chip to actually measure it. Or you might have to go to some method that there's RMS converter chips that

**Dave Jones:** actually measure the heat in in the resistor. So, they don't actually, you know, do it sampling-wise. They actually like physically measure how much power's dissipated in a resistor. That's old school. 1960s, 70s stuff. So, I hope you found that introduction to AC useful. I

**Dave Jones:** know it's very long and there's lots of stuff to cover. I could have broken it up maybe into smaller videos, but there's a lot more to come. We haven't even gotten into other stuff like, you know, transformers and circuit theory

**Dave Jones:** and all sorts of other stuff and AC Ohm's law and all the rest of it, but yeah, and complex numbers and things start coming next, but this will all be in part of the AC circuit theories a circuit theory series. There you go. If

**Dave Jones:** you liked it, give it a big thumbs up. As always, discuss down below. Catch you next time.
