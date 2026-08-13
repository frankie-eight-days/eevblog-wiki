---
video_id: gVfJTZG6h9o
title: EEVblog #972 - Operating Chips Outside Their Spec
url: https://www.youtube.com/watch?v=gVfJTZG6h9o
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 29, "2": 53, "3": 77, "4": 98, "5": 116, "6": 138, "7": 158, "8": 176, "9": 194, "10": 206, "11": 222, "12": 236, "13": 253, "14": 272, "15": 291, "16": 312, "17": 331, "18": 349, "19": 364, "20": 380, "21": 398, "22": 426, "23": 441, "24": 457, "25": 471, "26": 491, "27": 507, "28": 527, "29": 542, "30": 557, "31": 575, "32": 590, "33": 608, "34": 623, "35": 638, "36": 656, "37": 677, "38": 692, "39": 713, "40": 725, "41": 746, "42": 761, "43": 785, "44": 800, "45": 818, "46": 836, "47": 854, "48": 869, "49": 884, "50": 899, "51": 911, "52": 929, "53": 944, "54": 956, "55": 971, "56": 993, "57": 1008, "58": 1026, "59": 1044, "60": 1062, "61": 1077, "62": 1092, "63": 1110, "64": 1125, "65": 1143, "66": 1161, "67": 1179, "68": 1194}
---

**Dave Jones:** Hi, I was just doing some experiments on the new EEVblog 121 GW multimeter and, hey, I thought this might make an interesting video. It's to do with the true RMS converter chip used inside this thing. It's the Analog Devices AD8436. Now, it's a relatively new chip compared to the ancient AD5366 it is that's been used in, you know, every true RMS multimeter since like the late 1970s,

**Dave Jones:** I think it is, that chip came out crazy. Anyway, it's a very popular true RMS converter chip that's used inside all sorts of modern multimeters, and we're using it inside this one to get decent true RMS performance of this thing. But, hey, there's some little limitations that I wanted to test out, and we're actually going to be doing something a little bit naughty with this chip.

**Dave Jones:** We're actually going to be using it outside of its nominal operational voltage range specified in the data sheet. And normally, you know, you wouldn't do this in a bit of production kit like this new multimeter, but we have actually confirmed with Analog Devices that it will actually operate properly outside of this range,

**Dave Jones:** and the company who's doing this multimeter with me there doing some testing, and I thought, hey, I'd just check it out as well. So it's all hunky-dory, even though it's outside of its nominal voltage range. So you can actually do this, you know, as long as you've either characterized it, fully characterized it yourself to be, you know,

**Dave Jones:** fairly sure that it's going to give you the results you want in production, and or you've cleared it with the manufacturer, because sometimes they're very conservative on the data sheets, and it does actually operate outside of whatever performance spec it is just fine,

**Dave Jones:** but, hey, they didn't want to put in the data sheet for, well, insert reason here, right? They didn't want to push the limits or whatever. So I thought we'd just do some testing of that here and see what's happening. Now the AD8436, I'll put the data sheet in here, operates or has a minimum operational voltage of plus minus 2.4 volt supply rail,

**Dave Jones:** or in a single-ended configuration, which we're basically going to be doing inside here. That's 4.8 volts minimum, but, hey, this multimeter actually uses four AA batteries to power this thing. So four AA batteries gives us a nominal battery supply voltage of 6 volts.

**Dave Jones:** But, of course, when you're designing a battery-powered product, you want to actually maximize the usable capacity in that battery. So you want to have the cutoff voltage of your battery as low as possible. Now, in this case, of course, if we dropped it out at 4.8 volts,

**Dave Jones:** that'd be wasting probably half of the capacity in the batteries. I haven't checked, but it'd be a horribly high cutoff voltage of 1.2 volts per cell, and that doesn't include the dropout voltage of the regulator. But, hey, this chip, you could actually run it directly off the batteries.

**Dave Jones:** But, of course, if you've got a nice stable supply, you can guarantee the performance is not going to change over the supply range. So 4.8 volts is like, we don't want to piss away half the capacity in our batteries, or whatever it is.

**Dave Jones:** Look up the characteristic curve for the batteries, I've done many videos on that. So we need to operate this thing down lower. Preferably, a nominal cutoff voltage might be, you know, a decent one might be, say, 1 volt per cell. So we're looking at working down to 4 volts.

**Dave Jones:** So that's 0.8 volts lower than the data sheet value of this chip. But we actually want to operate it lower than that. We actually want to put in a 3.6 volt voltage regulator, because we've got a 3.6 volt voltage regulator for other stuff,

**Dave Jones:** and we want to operate it down that low. And we talked to Analog Devices and they said, yep, you know, it will actually operate down at 3.6 volts, instead of the minimum 4.8 volts in the data sheet. So what I'm going to do here today is I've got it powered from an external supply here.

**Dave Jones:** I've actually taken the back cover off. I won't show you too much, but back cover off there. And normally you need to spring the batteries in the back, and the spring terminals actually, you know, go down on that. So I've just soldered some wires in there that allow us to hook up an external power supply there.

**Dave Jones:** And we can adjust that and operate our meter down to any voltage we like. So that allows us to adjust our power supply and check its performance over any particular range. So I've got the Siglent SIGGEN here. That allows us to generate some AC signals.

**Dave Jones:** And I've got the Keysight 34470A, which is a beast of a 7.5 digit multimeter. So we're going to use that to compare the readings. And basically, you know, if we adjust the different waveforms and our 121 GW varies from our reference Keysight here,

**Dave Jones:** then, you know, we know to investigate further. But basically, if we change the voltage range right down and we test various waveforms, and it matches something like the Keysight here, hey, no worries. Now the AD8436 inside here is actually powered from a low dropout voltage regulator in this case.

**Dave Jones:** So rather than, like, butcher the circuit and everything else and bypass that and put the existing 3.6 volt voltage regulator on there, I thought I'd just drop the battery supply like this and actually let the voltage regulator drop out, and then we can lower the voltage.

**Dave Jones:** But of course, LDOs are famous for oscillating. If you get them below that dropout voltage, it might be, say, 0.1 volts for, say, a 5 volt voltage regulator. So I'm just going to hook the scope up here to the rail, AC couple it there.

**Dave Jones:** I'm only on 200 millivolts per division should do it. Actually, let's go down to 100, something like that, to see. And I'll just drop it below its dropout voltage and just make sure it doesn't oscillate. And then that's just an easy way to do it.

**Dave Jones:** There it is. You saw it jump up because when I change the rail like this, you should probably see it jump around a little bit. There we go. So I'm dropping out, regulator's dropping out now, and it's following, it's basically tracking that voltage rail down.

**Dave Jones:** So, whoop, 3.4, okay, I've got it to 3.6 volts now on the battery input here, and the output, so here's our input. What have we got? There we go, we've got 3.6 volts, and then the output of the regulator, 3.57. So there's just a little drop there, there's not much current, there's a bit of drop,

**Dave Jones:** but it's basically tracked that down very nicely. So we can get away with doing that, the oscillation's not going to affect anything. But that's worth checking, and if you thought that was a problem, hey, maybe in real performance measurements you wouldn't do that,

**Dave Jones:** you would go to the effort to bypass, but I don't want to butcher the meter. So, eh, that's going to be good enough for today. So what I've got here is a 400 hertz waveform generating, that's a typical figure, a nominal specification figure for a multimeter,

**Dave Jones:** we could use a kilohertz or whatever, or the frequency range of this, you know, is going to go up to many, many tens of kilohertz. I think the AD8436 is like capable of a megahertz, if you optimize, it's not going to be that high in this particular case,

**Dave Jones:** it's going to be sub-100k or something like that, I believe. So I'm generating a 1 volt RMS signal, and ta-da! We have 1 volt RMS, so it's actually working just fine, down at that 3.6 volts, no worries, at that nominal frequency. So, you know, as a first-order pass, that's working just fine,

**Dave Jones:** and of course if I adjust it, it's going to take time, to settle down, you know, when you're adjusting the supply, you expect things to jump around because the averaging caps and everything else have to settle, you're changing the whole upset in the apple cart there, but there we go,

**Dave Jones:** that's basically nominal 6 volts, although that's voltage regulating there, but yeah, we can take that down to 3.6 volts, no worries, and, you know, it's a little bit lower than what it was before, but that's just a calibration thing, basically. So that is well within specification,

**Dave Jones:** so it's already looking very promising. But hey, what we want to do is actually check it at full scale here, and it's basically bang on to the Keysight, because this is a 50,000 count meter, so we want to test it at its full range there,

**Dave Jones:** full scale range, no worries, I mean, that's practically bang on, and then if we check it down at 0.1 volts, and then if we check it down at 0.1 volts, so we're getting right down there at the lowest signal levels on the same range, then it's basically

**Dave Jones:** pretty much bang on as well, so beauty, it's looking good. But of course we're using a pure sine wave here, and that's a relatively low crest factor waveform. Now the crest factor is actually defined as a ratio, and it's a ratio of the peak value, whoops, shouldn't have touched it,

**Dave Jones:** it's a ratio of the peak value, bloody touchscreens, the peak value of the waveform, which is the peak value of the sine wave, divided by the RMS value of the sine wave. So a sine wave actually doesn't have a crest factor of 1, it's actually got a crest factor of,

**Dave Jones:** you guessed it, that 1.414, that you're, a figure that you're actually used to, which is the peak ratio. So, in fact, if you put a square wave into this thing, a square wave is actually a crest factor of 1, because its peak value,

**Dave Jones:** it stays at that peak all the time, so the peak divided by the RMS is actually the value, it's a definition of a perfect crest factor. So you might think, oh, square waves are bad for true RMS converters, they're actually not, they're really, you know,

**Dave Jones:** as good as you get in terms of crest factor. And depending on the true RMS converter chip used, you might, you know, you typically have a crest factor limitation that might tell you the maximum crest factor is 4, or you might read the

**Dave Jones:** datasheet of a multimeter and it tells you, hey, the RMS values are only guaranteed for this spec up to a crest factor of 4 or 8 or something like that. The AD8436 is specified, its specifications are given up to, nominal specs are given up to

**Dave Jones:** a crest factor of anything up to 10. So, you know, that's pretty horrific type crest factor, so we'll try something with just a little bit more oomph, shall we? So we'll go into waveforms here, we'll go into, I mean we can put noise is a pretty bad one, but we'll go into ARB here

**Dave Jones:** and we'll actually do a sine x on x which, you know, it's mostly low for most of the period, then it's got a big spike, so like switch mode power supplies are a common example of this, that'll have bad crest factor waveforms and stuff like that, and incidentally

**Dave Jones:** the AD8436 actually has a specific pin to add an additional averaging capacitor, like a higher frequency averaging capacitor for those shorter peaks, as well as having a larger average capacitor value. So this is a pretty neat chip, that's why it handles crest factors quite well, and certainly the EEV

**Dave Jones:** log meter has both of those caps built in to handle the higher crest factor waveforms, so this is going to be a reasonably high crest factor waveform, you might typically get, you know, overshoots like that, and you know, spikes and things like that.

**Dave Jones:** So, hey, look right down already, look at that! Look at that, 22 point, we're basically bang on let's go back up to our amplitude here, and go 1 volt oh, we can only do peak to peak here, okay, we can't do the RMS anymore

**Dave Jones:** but yeah, it's tracking that, no worries at all. And if we go up to 10 volts peak to peak there it's, look, it's pretty, you know, it's not quite bang on, but it's pretty darn close, it's well within spec so it's operating quite well with large crest factor

**Dave Jones:** signals, down at a 3.6 volt chip supply limit, well under that data sheet value of 4.8, so this chip is very conservatively specified, and by the way, 3.6 volts will be the highest operational voltage part inside this meter, so this allows us to set our dropout voltage

**Dave Jones:** our low battery detector voltage not much above that 3.6, so you might set it to, have to look at the data sheet for the regulators, the low dropout regulators used in this, but you know, it might be typically 50 millivolts, 100 millivolts, not much above that

**Dave Jones:** so 3.6 volts nominal would give a low battery warning indicator of 0.9 volts per cell, and that's pretty darn good, you're using up you know, vast majority of the energy inside those 4 AA batteries, so that's quite good design you don't want to be, you know, pissing away

**Dave Jones:** that battery capacity. And of course we can, you know, select all sorts of other waveforms here, what is that? Exponential rise, there we go, doesn't matter what, ARB type built in, this has got all sorts of built in math functions, and you know, you can have engines

**Dave Jones:** so if you like a cardiac pulse, there you go we can choose a cardiac pulse and bingo, there we go, so it measures a cardiac pulse no problems at all, seems to be working very well basically the only variable left really, that would be a concern, would be

**Dave Jones:** temperature really, because you know, power from batteries, low dropout, voltage regulator, everything else you wouldn't worry about, you know, power supply rejection ratio and you know, other system stuff like that's not really relevant here, so probably temperatures, the performance over temp would probably be the only one left.

**Dave Jones:** So how does it perform over temperature? I'm glad you asked, we've got the old thermal chamber here which we haven't seen in quite some time, and I'll just like ramp it, you know 10, 15, or maybe 20 degrees if I can, and basically

**Dave Jones:** just see if it matches, so we'll give it a boil I'll come back, because it's pretty boring to watch. So at the moment we've got a value of 0.777, let's call it whatever, 7777, and which is fairly close to the key site there

**Dave Jones:** and of course the key site's out of the chamber, so that's our control, it's not going to change, and we'll see if there's any effect with increased temperature. But of course here we're not concerned whether it's an increase or decrease in temperature, we're just concerned

**Dave Jones:** with the temperature delta, i.e. delta just means change, the change in temperature. So you know, it doesn't matter, we just want to get a measurement on the multimeter at two different temperature points, you know, 5 degrees might tell you, you know 10 starts to be reasonable, you know, a 10 degree C

**Dave Jones:** change might be a standard control or something like that so we'll ramp it up at least 10 and see if there's a difference if not then I wouldn't be too concerned, I mean this is not some ultra full-on professional testing that'd take weeks and weeks and weeks where we'd fully characterize it

**Dave Jones:** over the entire operating temperature range and everything else, I just want to see if it makes a difference. Because I trust that the people at Analog Devices, when they say it works at 3.6 volts, we just don't put that on the data sheet

**Dave Jones:** then, you know, I trust them that they know their part very well and they know it's going to perform at that. So one other thing we've got to test for is frequency range as well, so I've taken it up to 5 kHz here, we're down at, sorry this is a bit complicated, we're down at

**Dave Jones:** 3.6 volts again, and we're getting 1.005 there, so we can take it up higher in frequency, 10 kHz 20, there we go, the by the way, the Keysight one's got 300 kHz or something 20, we're still hanging in there but now we're starting to get, you know, a few

**Dave Jones:** a couple of percent out, you know, we're starting to get a few percent, that's 36 kHz 37, I mean if you want to talk about the minus 3 dB point, then it's going to be massive you know, so we're up at 65 kHz

**Dave Jones:** now, but anyway, that's not the point, OK so what we're going to do is, there we go you can probably go down to the 0.707 point at 120 odd kHz or something like that but what we want, what I'll do is I'll just tweak it to 1 volt precisely

**Dave Jones:** on there and just use that frequency point as a ballpark, what do you think? Sounds good. There you go 17 kHz, now time to ramp the temperature up and we're up to 39 degrees and on the AC performance at 39 degrees C we're looking at, you know, 0.3

**Dave Jones:** ish percent change or something like that, so yeah, not much and if we change it back down to the 5 kHz reference it's almost spot on, isn't it? It's basically ramped up to 38 degrees now, which is a good 15 degree differential on there and

**Dave Jones:** by the way, the back is still off, so the air flow is going directly over the chip, it's going to there's little thermal mass inside there in terms of the chip, so it's going to change almost in real time with the chamber basically, and it

**Dave Jones:** hasn't drifted at all, I'm not sure if you can see that glare on there, yeah, 0.77, almost double 7, it hasn't changed a smidgen in 15 degrees, so I'm going to call that a win so there you go, I hope you found that video interesting

**Dave Jones:** in using a chip in a commercial application outside of its nominal specification, and ordinarily, as I said, you wouldn't do this but there's good reasons why we're doing it, because we want to get that low dropout, you know, voltage on the batteries and everything else, so you know, it's pretty important

**Dave Jones:** and that's the chip that we want to use in that application yeah, there are other options maybe, but you know, that's the chip that we're going to be using here, and it works just hunky-dory, so I'm pretty darn happy with that I'm going to do some more testing

**Dave Jones:** but that's basically confirmed that no problem whatsoever, yep, no worries no problem in using that in this particular application now that doesn't mean that the chip is fully characterized down to 3.6 volts, you know, at higher signal amplitudes, which we may not be seeing in this

**Dave Jones:** you know, it's full operational range, which we're not using over and stuff like that, it could, you know, there could be traps in there for that, but you know, for the particular application that we've got here at full scale input voltage and at the low end, so we measured full scale and at the low

**Dave Jones:** signal level as well, no problems whatsoever, no problems over temperature, no problems with crest factor so I'll just do some more experimentation but yeah, that seems pretty solid so analog devices were right when they say this thing works down to 3.7, 3.6 instead of the

**Dave Jones:** nominal 4.8 in the datasheet, but yeah, you know, don't try this at home make sure you stick to the datasheets unless you're absolutely have to go outside, you have a very good reason to do it. Lots of traps for young players doing that

**Dave Jones:** but anyway, hope you found it interesting, catch you next time Thanks for watching!
