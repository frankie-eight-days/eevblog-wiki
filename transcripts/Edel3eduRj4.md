---
video_id: Edel3eduRj4
title: EEVblog #594 - How To Measure Power Supply Ripple & Noise
url: https://www.youtube.com/watch?v=Edel3eduRj4
source: youtube-asr
timestamps: {"0": 1, "1": 13, "2": 28, "3": 35, "4": 56, "5": 66, "6": 80, "7": 95, "8": 104, "9": 124, "10": 141, "11": 156, "12": 174, "13": 188, "14": 204, "15": 217, "16": 230, "17": 240, "18": 253, "19": 265, "20": 274, "21": 286, "22": 298, "23": 312, "24": 336, "25": 348, "26": 358, "27": 367, "28": 377, "29": 389, "30": 401, "31": 414, "32": 429, "33": 441, "34": 455, "35": 468, "36": 479, "37": 489, "38": 505, "39": 515, "40": 535, "41": 548, "42": 558, "43": 568, "44": 578, "45": 586, "46": 594, "47": 605, "48": 625, "49": 633, "50": 647, "51": 659, "52": 669, "53": 677, "54": 698, "55": 709, "56": 726, "57": 738, "58": 747, "59": 757, "60": 768, "61": 780, "62": 795, "63": 813, "64": 830, "65": 844, "66": 857, "67": 873, "68": 888, "69": 898, "70": 911, "71": 927, "72": 938, "73": 952, "74": 971, "75": 988, "76": 1004, "77": 1014, "78": 1031, "79": 1040, "80": 1051, "81": 1066, "82": 1085, "83": 1096, "84": 1110, "85": 1124, "86": 1131, "87": 1144, "88": 1158, "89": 1173, "90": 1188, "91": 1202, "92": 1218, "93": 1234, "94": 1250, "95": 1261, "96": 1277, "97": 1287, "98": 1302, "99": 1322, "100": 1331, "101": 1349, "102": 1360, "103": 1373, "104": 1392, "105": 1405, "106": 1418, "107": 1434, "108": 1449, "109": 1460, "110": 1469, "111": 1481, "112": 1489, "113": 1500, "114": 1509, "115": 1522, "116": 1530, "117": 1542, "118": 1553, "119": 1564, "120": 1572, "121": 1585, "122": 1594, "123": 1608, "124": 1618, "125": 1631, "126": 1645, "127": 1657, "128": 1673, "129": 1686, "130": 1698, "131": 1711, "132": 1726, "133": 1741, "134": 1751, "135": 1766, "136": 1775, "137": 1786, "138": 1798, "139": 1808, "140": 1820, "141": 1840, "142": 1854, "143": 1865, "144": 1877, "145": 1889, "146": 1903, "147": 1917, "148": 1933, "149": 1945, "150": 1956, "151": 1969, "152": 1984, "153": 1994, "154": 2004, "155": 2012, "156": 2021, "157": 2033, "158": 2043, "159": 2058, "160": 2068, "161": 2083, "162": 2102, "163": 2114, "164": 2134, "165": 2147, "166": 2165, "167": 2175, "168": 2183, "169": 2194, "170": 2208, "171": 2223, "172": 2232, "173": 2242}
---

**Dave Jones:** Hi, welcome to Fundamentals Friday. Today we're going to take a look at ripple and noise measurement and specifications. You're familiar with it. You've seen it on your power supply, your bench power supply that you've got lying around, no doubt.

**Dave Jones:** You see that ripple and noise measurement. They might give a typical value for a PSU like 1 mV RMS / 5 mV peak-to-peak ripple and noise. What exactly does that mean?

**Dave Jones:** What's ripple and what's noise? And how do you measure it? What are the traps for young players? Well, I'm glad you asked. So, what does it ripple mean? Let's take a look at that first.

**Dave Jones:** And you're almost certainly familiar with this term. You've seen it used in terms of linear power supply, for example, and we'll get into that. Now, it can be correctly described as the charge-discharge cycle of the storage element in whatever power supply you're actually using, be it linear or switch mode.

**Dave Jones:** There's a bit of confusion there. People think ripple only uh is 50-60 Hz mains hum, that sort of stuff out of your traditional linear supply that you're used to here.

**Dave Jones:** Half-wave Half-wave bridge rectifier, for example, and your capacitor. Then, well, you'll get that 50 Hz / 60 Hz, depends on where you are, ripple on the output. A full-wave bridge rectifier, you'll get double that frequency.

**Dave Jones:** And you've seen that. It's a basic uh building block thing. You've no doubt mucked around it with your scope if you're a beginner. But, that ripple uh the term ripple also applies to a switch-mode power supply, a DC-to-DC converter.

**Dave Jones:** Let's take, for example, this uh buck uh converter here, which, you know, converts a higher voltage down to a lower voltage. The storage element in this case is the inductor here.

**Dave Jones:** And the charge-discharge cycle of the inductor in the switch-mode converter. And that will give you, you know, it doesn't look at as smooth, usually, as your uh mains frequency, which is derived from the mains, which is of course a sine wave.

**Dave Jones:** You don't generally get a sine wave out. You might get something sort of funny-looking like that, but it's still going to be periodic and relatively low frequency. In terms of a switch-mode power supply, could be, you know, tens of kilohertz up to a couple of hundred kilohertz, maybe even a megahertz or two or something like that.

**Dave Jones:** But it's generally defined as that base frequency of the discharge and charging of your storage element, be it your rectifier here or your inductor, your DC-to-DC converter. So, that sort of base frequency.

**Dave Jones:** And well, what is noise? Easy. Noise is everything else. Pretty much mainly due to, in terms of a switch-mode power supply, for example, you generally won't get noise in just a linear power supply like this unless it's being coupled in via something else.

**Dave Jones:** But in a DC-to-DC converter, for example, you can get parasitic inductances all over the place, and they can cause some high-frequency noise or ringing when you've got large dIDT, technical term.

**Dave Jones:** It just means large changes in current over time, which you get charging and discharging your storage element. These parasitic inductances generally much lower inductive values, so therefore they're going to ring and generate noise at a higher frequency.

**Dave Jones:** So, you'll find that the noise typically will have sort of, you know, noise superimposed on there like that. I can't draw it in there, but you'll see that it'll have much more higher frequency content.

**Dave Jones:** And that's generally what noise is. And in terms of power supply specifications, well, they lump them all together and say it's ripple and noise. So, they combine the two, and they give you two figures.

**Dave Jones:** They give you a peak to peak value, of course, which is your value from there to there, your absolute maximum peak to your absolute minimum. And they also give you a value in RMS, as well.

**Dave Jones:** At least your good supplies do. You know, your cheaper supplies, they might just give you the RMS value because, well, marketing wank, right? The RMS value is always going to be lower than the peak to peak value.

**Dave Jones:** Now, I've done videos on noise before, and you should probably know from those that a noise figure is generally pretty useless unless you specify it over a particular bandwidth.

**Dave Jones:** And well, what is it in the case of power supplies? Well, a lot of manufacturers will not tell you. So, there's actually no real standard for it as such.

**Dave Jones:** Pretty much manufacturers will just throw a number out there, 1 mV RMS. They won't even give you the bandwidth. What does it mean? In fact, they won't even tell you what current it is at because the ripple and noise is going to change with your output current.

**Dave Jones:** The noise, for example, the parasitics in the inductors, the value of the change in current with time that I talked about there, well, that's going to vary with your output current.

**Dave Jones:** So, the voltage and noise figures, well, unless the manufacturer actually specifies it, you've actually got no clue. It's It's kind of almost meaningless, but there is a semi de facto standard for it, and that's 20 MHz bandwidth.

**Dave Jones:** So, generally, if it's not mentioned, that's what the manufacturer is really pretty much telling you that it should be over a 20 MHz bandwidth, both ripple and noise. Hence why your oscilloscope has that bandwidth button on it, and it's 20 MHz or vice versa, the bandwidth figure was taken from the fact that scopes actually had 20 MHz bandwidth limiting on.

**Dave Jones:** And your analog scopes for a long time had sort of like a base level 20 MHz bandwidth. So, really, I the number was just sort of picked out of the air pretty much.

**Dave Jones:** But, most scopes should have that 20-megahertz bandwidth limit on it. And if they don't, well, if you're using the wide bandwidth of your scope, you're going to get the wrong result.

**Dave Jones:** You're not measuring it properly. So, if your scope doesn't have that, hey, you might have to build up an external filter to put inside. And that's all there is to the theory, pretty much.

**Dave Jones:** In fact, I've probably spoken longer than I should. Let's go to the bench. So, let's take a look at two typical power supplies here. We've got this PowerTech MP3090.

**Dave Jones:** It's actually a Manson uh 9400. I've done a teardown of this before. It's just rebranded. And it's just a high-current switch-mode uh power supply, not really a bench uh power supply as such.

**Dave Jones:** And then you've got your higher-quality Rigol DP832 up here. Let's take a look at their data sheets. So, here's the Manson 9400. And well, look, it's pretty basic. Ripple and noise, 10 millivolts RMS.

**Dave Jones:** As I said, they're just too scared to put in the peak-to-peak figure in there. And they don't even specify a bandwidth or anything like that. And of course, they don't specify what output current it's over.

**Dave Jones:** But, almost no manufacturer actually specifies what output current it's actually at or different values for different output currents. So, it's generally taken the ripple and noise figure generally taken to mean at the maximum output current or maximum output uh power point.

**Dave Jones:** And here's the Rigol DP832. And look at this, much better. Here we go. Ripple and noise, and they specify the bandwidth, 20 hertz to 20 megahertz. There's the de facto industry standard there of 20 megahertz.

**Dave Jones:** But, hey, it may not always be. So, there you go. Normal voltage mode, here it is. Once again, they've lumped them together. Uh and we've got uh less than 350 microvolts RMS {slash} 2 millivolts peak-to-peak.

**Dave Jones:** So, that's a pretty low-noise power supply. So, which one actually means more to you, the RMS value or the peak-to-peak value? Well, actually that's up to you and your requirements for the circuit you're actually powering.

**Dave Jones:** But, generally speaking, the peak-to-peak value is really, you know, that's the one that's going to be a pain in the ass cuz you will get those peaky spikes out of it as we'll see on the scope.

**Dave Jones:** So, you might think it's pretty easy to measure the ripple and noise of your power supply. Just hook your oscilloscope probe up to the output like that and and measure it with or without a load on there.

**Dave Jones:** But, hey, that's rule number one is that generally the ripple and noise is going to be higher at higher loads. So, you generally want to test it at either the maximum output current or your intended output current for your circuit under test, for example.

**Dave Jones:** So, we've got a 5-V output here and I've got it connected up to my BK Precision constant current load up here and I've set it for 2 amps. So, there it is, it's drawing 2 amps.

**Dave Jones:** Let's go over to the scope and see how we set it up. And because power supply measurements are typically going to be low amplitude values, like in the terms of millivolts or even sub-millivolt, really you want the best scope you can get with the lowest noise front end with, if possible, you know, a good 1 mV per division range.

**Dave Jones:** Or in this case, the Rigol 2000 series scope has a 500 microvolt per division range. Fantastic. Ideal for testing power supply stuff like this. Or pretty much, as we'll get into.

**Dave Jones:** Anyway, the way you want to set it up is, well, here's channel one feeding our signaling. You always want AC coupling. You've got to remove that DC content, of course.

**Dave Jones:** Bandwidth limit, very important because we have to measure over the bandwidth. We can disable, well, we can go into say 100 MHz or turn it off and look at that.

**Dave Jones:** That is the difference between having your full bandwidth or your what the actual specification is over a 20 MHz bandwidth. So, if your scope doesn't have that, hey, you'll have to add a series filter in there.

**Dave Jones:** And I've set up normal mode manual triggering on this so I can adjust the trigger level. And well, look, I can get it to not trigger at all. Barely.

**Dave Jones:** Oh, yeah, we've got a big spike there. But barely because I'm adjusting the trigger level like that. It can be tricky to actually trigger on uh noise like this.

**Dave Jones:** So, generally you want your uh trigger threshold maybe on a noise peak like that, for example. So, anyway, um generally you don't want to use your auto trigger mode.

**Dave Jones:** Sometimes it's not going to work very good. Anyway, um what we've got is our RMS value. The scope can tell us the RMS value. Before scopes could calculate this sort of thing, you would typically use a wide bandwidth uh multimeter specifically for the task with a true RMS uh value mode to give you the RMS value.

**Dave Jones:** But these days your oscilloscopes can do it. And we've got, look, a current value of not sure if you can read that, but it's like 2.6 mV or something like that.

**Dave Jones:** And these are the statistics, average, and then the peak-to-peak. So, there's our two figures. We've got 20 you know, almost up to 20 mV peak-to-peak there. And of course, we can uh freeze that and actually take a look at the waveform which we're typically getting.

**Dave Jones:** It's pretty ugly, pretty noisy. But hey, we've got some basic figures there. But you might notice something here. I've used a times a fixed times 10 probe for this thing.

**Dave Jones:** Well, that's not so great when you're doing noise low-level measurements like this. You don't want to be using that divider probe, really. So, you want to stick in a times one probe.

**Dave Jones:** So, I've changed that to a times one probe and uh there it is. I've set it up as times one. We're basically getting similar to values to what we got before, similar waveform.

**Dave Jones:** But you're going to get uh better signal fidelity out of your times one probe because you're not dividing it down. But another trap is that with a times one probe, as you've seen in previous video I've done, is that a times what the bandwidth of the times one probe can actually be pretty low in the order of like 10 or 20 megahertz.

**Dave Jones:** So, just check the data sheet for your particular if you're going to use a scope probe like this, check your particular probe and what bandwidth cuz you may not be measuring over a 20 megahertz bandwidth anymore.

**Dave Jones:** You may actually be limited by the bandwidth of your scope probe. There you go. I'll link in the video for that down below if you haven't seen it. You've got an older scope with limited memory depth during regular sampling, then you might need to use peak detect mode.

**Dave Jones:** In fact, you probably should, you know, as a general rule be using peak detect mode so that it can actually detect the absolute peaks and you're not missing it based on your time base and your memory depth and stuff like that.

**Dave Jones:** So, if you want your true peak-to-peak reading, it should be in peak detect mode. That's what it's there for. And just to show you how that ripple and noise changes with load, well, that's with my 2 amp load.

**Dave Jones:** If I turn off my 2 amp load, bingo. Look at that. Big difference. So, yeah, make sure you know and specify at what load current you're testing it at.

**Dave Jones:** But, you guessed it, I've deliberately added a trap for young players here. The probing method that I've just shown you before is actually wrong. You shouldn't be doing it like this.

**Dave Jones:** And I'll show you why. It won't be a huge example. I could probably set up a better example, but you'll at least see the difference. At the moment, I've got my LED studio lights above me and they're pulse width modulated.

**Dave Jones:** And those things generate, you know, a whole bunch of noise which gets coupled into our test system here and our test leads and everything else. Absolutely horrible stuff. So, what happens if I turn off my lights here?

**Dave Jones:** Watch the waveform. You won't see a huge change, but you should see a difference. Ready? There we go. And if I switch them back on, there we go. You actually get a bit more noise and it can actually be a lot worse than that depending on the scenario and how it's actually being picked up.

**Dave Jones:** In fact, I'll show you a much better example of let let's hook it up to my Rigol 832 power supply. Exactly the same as before, 5 volts out. We're drawing 2 amps into our load over here and I've got my standard oscilloscope probe times one with our earth lead on there.

**Dave Jones:** Let's check this one out. And as you can see, totally different waveform, totally dominated by you know, high frequency noise content because this is a linear power supply as opposed to a switching power supply that we saw before.

**Dave Jones:** And we're down to 1 millivolt per division here. Let's That's with my lights on. Let's turn it off. Ready? Ta-da! Look at that. Huge difference. Let's switch IT BACK ON.

**Dave Jones:** WHOA! Look at all that. That is common mode noise being picked up by our piss-poor test connection. We didn't do it right. So, the next rule of power supply ripple and noise testing, don't use your big antenna earth lead like that.

**Dave Jones:** It's a huge inductor just picking up all sorts of crap. So, instead, what I'm going to get is a BNC adapter like that and I've got a banana plug to BNC like that and I'm just going to plug that into our power supply.

**Dave Jones:** Much better. So, we don't I mean, I can still leave this lead dangling off here. It's not doing anything anymore, but generally, you'd take that out and then we can plug it straight in.

**Dave Jones:** Nice low impedance, low inductance path through to our power supply connection right at the test connection. By the way, you always want to measure it right on the output and not way over here.

**Dave Jones:** You don't want to measure it over here because, well, that is just going to pick up all sorts of crap. Forget it. So, there we have it. Beautiful low inductance path directly in our load connected directly across there, probing via the BNC, fully shielded, no big inductive path.

**Dave Jones:** That's as good as we can possibly get for measuring the output of a bench power supply like this. And what does that give us? Look at that. And that's with my lights on.

**Dave Jones:** Look, I'll switch them off. And tada, look, it adds very little high-frequency noise to that. Where is it? 1 mV per division. We can actually go down to 500 µV per division cuz this scope is really, really good.

**Dave Jones:** And look, we really can't see those lights. Whoop, switch them on. Yeah, there we go. We've added a little bit more, but it's nothing like before. It's like, you know, half an order of magnitude less than what we're what we're getting before because we've got a proper low-inductance shielded test connection.

**Dave Jones:** But now the problem is with that what's called single-ended connection that we're testing with at the moment, that that's good. And you can do power supply testing like this, but it's not absolutely ideal cuz we still don't know where our noise sources are coming from.

**Dave Jones:** Look, we've got some spikes here. I could probably try and trigger off those, but you can see it drifting across like that. Are they being generated in by the supply or is it coming from something external, something, you know, and we're getting common mode coupling onto our cable?

**Dave Jones:** Well, I don't know. And for those curious to see what it looks like on a real old-fashioned analog which is still the best choice for something like this. Well, here's my Tektronix 2225.

**Dave Jones:** Once again, it's also very rare on the market. That's got a 500 µV per division vertical range. And see, you know, we can see a bit more detail in the high-frequency content in there, but we could also probably see that on our digital if we actually stopped and zoomed in and stuff like that.

**Dave Jones:** But there you go. We're seeing We're also seeing some of that noise which I'm not sure if that's still common mode noise common mode pick up from something or what.

**Dave Jones:** But there you go. Generally, basically exactly the same thing we're seeing before on our analog scope. And there you go. I've got that a bit better on the digital scope over here.

**Dave Jones:** I've triggered manually now, so I'm in there and I've got AC coupling. I've got some noise reject on as well. I don't think that matters a huge amount, but I've got it set to normal and I'm just holding my tongue at the right angle and tweaking that trigger level.

**Dave Jones:** And you know, pretty much we can capture that and of course then zoom in on any of the detail. We were sort of seeing that a bit clearer on the analog type stuff, but that is your high frequency noise and the rest of it is that low frequency content like that is your ripple.

**Dave Jones:** And of course we can trigger on that ripple because we can go into our source for our triggering and we can trigger off the AC line there. There we go.

**Dave Jones:** That's the 50 hertz. So there you go. It doesn't drift anymore so you know that is your ripple. But of course that sort of line triggering of course only works for a linear power supply where you're going to get that 50, 60 or 100, 120 hertz ripple on the thing.

**Dave Jones:** You're not going to be able to do that on a switch mode power supply which has a a free running frequency for its switching converter. Now this is our best possible single-ended test connection we can get for a bench power supply like this.

**Dave Jones:** Well, what happens if you want to measure your own design or measure one of these little brick converters or something like that? Let's take a quick look at that.

**Dave Jones:** So to measure your own supply or a a brick converter like this for example or something on any PCB switching be it switch converter or linear for example, you always take measure the output directly on the output filter capacitor like that.

**Dave Jones:** I'm not sure exactly which one in here is here. I'm presuming it's these and big ceramic capacitor here. So you'll put your scope probe directly across that capacitor with as low an inductance uh probing technique as possible.

**Dave Jones:** So, you might use one of your little uh low-inductance um ground uh spring clip adapters that you should have got with any uh decent set of scopes, and you would probe it directly across there like that.

**Dave Jones:** Or as I've shown in previous videos, you can actually uh solder a bit of uh you know, dedicated wire like a little hook and loop. So, you can basically uh make one of these out of a wire, solder directly on the board, and then stick your probe right in like that.

**Dave Jones:** You want the lowest inductance path possible. Forget about using this garbage. Uh, it's an antenna. Now, I said this was the best single-ended method possible. And well, by single-ended, your scope probe is a single-ended probe.

**Dave Jones:** I.e., it's got uh your input and a ground. Basically, that is a single-ended test connection. Well, that is not ideal cuz we still aren't 100% sure of the way of the no noise on our scope.

**Dave Jones:** Is it common mode noise, or is it actually coming out of the power supply? The only way to be absolutely sure and the best possible and recommended way to measure ripple and noise of any power supply is not to use a single-ended scope probe like this, but to use a differential probe.

**Dave Jones:** Now, you might be familiar with a high-voltage differential probe like this LeCroy AP031. And these are fantastic to have and the tool for measuring high-voltage stuff because they have differential input like this.

**Dave Jones:** Yes, there's a positive and negative, but it's a differential input, not single-ended, and it can tolerate high common mode voltages on the input. But, and and it gives you a single-ended output.

**Dave Jones:** So, it converts differential to single-ended output that goes into your scope like this. But, this is actually useless for our task here because this is designed for high voltages, it's not low noise, and it only has 1/10 or 1/100 attenuation.

**Dave Jones:** So, no good at all. What you need is a proper differential probe and or differential probe with a preamplifier on the input. Now, the Duck's Guts is one of these.

**Dave Jones:** It's a Lecroy, has very high bandwidth, higher than the 20 MHz required, but hey, it costs thousands and thousands of dollars. So, pretty much there's not much on the market in terms of proper differential probing for doing power supply measurements like this.

**Dave Jones:** Now, there's a poor man's way to do this, but it actually works kind of reasonably well and gives you a good ballpark indication of whether or not you've got common mode noise or not, and that's to use a the old technique of having using the dual channel of your scope and getting a differential measurement that way.

**Dave Jones:** You'll notice I got the two scope probes here, but there is no connection at all. It's just the center connection on both the positive and negative of our power supply.

**Dave Jones:** So, the grounds are not connected at all. Our oscilloscope, of course, is mains earth reference, so we're going to get all sorts of crap coming from each channel, but when you subtract one channel from the other, bingo, it should get rid of all that crap and give you a true differential measurement across there.

**Dave Jones:** Now, the way to do this on an old-fashioned analog scope, and a digital as well, but I'll show you analog first, uh we've got both our inputs here. Must both must be AC coupled.

**Dave Jones:** Both must be set to the exact same vertical attenuation range. In this case, I've got 5 mV per division. I've pulled out my times five times 10 magnifier, so we're 500 µV per division, channel one and channel two.

**Dave Jones:** We're displaying We've got both channels active and we're inverting channel two. That's important because an analog oscilloscope doesn't have a subtract function. It's only got an add function. But, if you have channel one plus the inverse of channel two, that gives you subtraction.

**Dave Jones:** So, there we go. We're on add mode. We're channel two invert. And as I said, it's important that these two are exactly the same range. Otherwise, if you're got that cal, make sure your cal's adjusted correctly.

**Dave Jones:** Otherwise, it's going to be completely out of the shop. And of course, this is a big reason why this isn't a very good technique. You don't get good common mode rejection ratio using these.

**Dave Jones:** No common mode rejection using this technique, but it's good enough. But, look. What What the hell is this? What is this? It's hopeless. It doesn't work at all. Well, the reason is that we've got no ground connection between the scope and our system under test.

**Dave Jones:** So, it's picking up a whole bunch of common mode garbage on both these channels, and it can't deal with it. So, we have to really knock that common mode stuff on the head by adding a couple of 50 ohm terminators on the input.

**Dave Jones:** If your scope has 50 ohm termination, turn it on. So, let's plug both our channels back in with I've got a series 50 ohm terminator on each one. And bingo, look at that.

**Dave Jones:** We're now in subtract mode. As I said, if you muck around with any of the vertical settings, if they're not completely matched like that, you're just It's just not going to happen.

**Dave Jones:** And of course, if you don't invert channel two, you're screwed. You're just looking at that. And bingo, we're getting bugger all there. And you expect it to be bugger all because well, the Rigol is a very good power supply.

**Dave Jones:** Let's go over to a better example, much higher noise. You know, we can't go any further on a vertical. Let's go back to that horrible Manson switching power supply.

**Dave Jones:** So, there you go. That's the test connection back on our Manson supply there. Exactly the same load we had before. And bingo, look at that. There we go. There's our Manson power supply output.

**Dave Jones:** There's some of the high frequency stuff in there. We can actually turn our alt zoom on and we can actually see the zoomed value of that a zoomed part of that noise in there.

**Dave Jones:** Look at that. So, there's our ripple and there's our noise using our differential measurement on our analog scope like that and we should get exactly the same on the digital.

**Dave Jones:** Let's go back and try that. And we're back on our Rigol here. Here's our channel one, channel two input and I've got the math operator on A minus B there.

**Dave Jones:** And as you can see, it's a bit slow updating on the screen there, but we're basically getting exactly the same waveform we get before with some high frequency content in there we weren't seeing on our analog scope.

**Dave Jones:** So, what we'll do is we'll just expand that out a bit. We'll go to our acquire menu here and we're in normal acquisition at the moment. We'll change that to our high-res mode with our boxcar averaging.

**Dave Jones:** And bingo, look at that. There we go. We're getting exactly the same waveform we're getting on that analog scope there on our digital scope. But the waveform updating, uh, little bit slow.

**Dave Jones:** And that's one of the problems with the Rigol scope and a lot of other scopes on the market. They will do all that math function in, you know, processing in software.

**Dave Jones:** So, it takes actually time when you turn those math functions on. That's why they're slow updating. If we go to our Agilent 3000 series scope here, it does all the math stuff and in direct hardware on the ASIC.

**Dave Jones:** So, it is much better, much quicker updating. But the problem is this scope only goes down to 1 mV per division, but it really only has a true 2 mV per division.

**Dave Jones:** The 1 mV is actually just a software tweak. So, we don't get the greatest fidelity out of our waveform here. So, in that respect, the Rigol scope with its true low noise 500 microvolt front end much better for this purpose.

**Dave Jones:** And here's an interesting thing to note. What I'll do is I'll adjust the gain here on the well the scale of our math function. We're currently at 1 mV per division there.

**Dave Jones:** So, I'll tweak that down here and you'll notice look at that. You start if I go up one to 500 microvolts per division, you start seeing the individual bits in there of the math calculation.

**Dave Jones:** So, this is uh you know, one of the disadvantages of a digital scope and one of the advantages of the analog. Once you get down to with large differences and dynamic range, you've only got that 8-bit converter in there to play with.

**Dave Jones:** So, really, you know, look you can start to see the individual individual bits there. Just crazy. Look at that. But, hey, at least we can see our waveform. So, that's pretty good.

**Dave Jones:** And that value is going to change with our scale here. If we turn our vertical uh up, of course, we get increased fidelity and resolution in that uh calculated math value because it's only got eight bits to work with or more if it's the high-res mode.

**Dave Jones:** But, let's take it down to say 5 mV per division on both channels. Look at that. Totally blocky because the signal the amplitude is down in the noise. So, it can only calculate Look, we've only got a couple of bits down in there.

**Dave Jones:** Ah, it's bugger all. So, when you're using a digital scope, just make sure you maximize the uh use of your dynamic range of your front end by using the lowest uh vertical scale possible.

**Dave Jones:** And here's another trap for digital scopes as well. There's our waveform. What happens if we move our one of our channels off outside the range of the ADC. So, it's clipping.

**Dave Jones:** Look. Look at that. Our calculated math value just goes to complete garbage. That's one of the advantages of analog scopes. Digital Uh look at that. That's awful. Real trap if you don't know what you're looking for.

**Dave Jones:** But, if you're observing, you would have noticed that our amplitude here that we're getting is much lower than what we were getting our differential uh waveform here is much lower in value in amplitude than we're getting with that single-ended connection.

**Dave Jones:** Why? We're still using times one probes here. Nothing's really changed. We're subtracting one signal from the other. We should get the same value, but we're not. Remember, look at our scale.

**Dave Jones:** It's 500 microvolts per division here, and it's basically I can uh go in there into the math function and adjust the tweak that up. It's like, you know, two divisions sort of peak to peak there.

**Dave Jones:** What we're getting before, we're getting what, about 10 millivolts peak to peak, about 10 times more. So, what I've set up here in parallel is our single-ended connection as well.

**Dave Jones:** Yeah, you can do this. Ordinarily, you wouldn't, but we're going to get away with it here. So, we're got a single-ended and our differential probing it as well. So, I've got the yeah, the proper high-frequency connection there.

**Dave Jones:** It's going that third channel now single-ended is going to our Agilent scope because our Rigol scope is only two channels. So, let's have a look. So, there's the single-ended measurement on our Agilent scope.

**Dave Jones:** Look, two millivolts per division. You know, two, four, you know, it's almost six, sort of, you know, something like that. Hey, yeah, let's not dick around with the triggering.

**Dave Jones:** And if we go up here and have a look at our differential measurement, then, as we said, we're 500 microvolts per division, so we're barely even 1 millivolt there peak to peak.

**Dave Jones:** So, there's about a six odd times difference. Where is that coming from? Well, if you remember a previous video I've done, which I'll uh link in, in that um the how these uh oscilloscope probes work, the coax cable isn't just a direct connection straight through.

**Dave Jones:** It actually uses a lossy coax, which means it has a resistance in it. And we can actually measure that. Look, let's get our multimeter here. Here we go, and measure our center conductor, which you'd expect to be a dead short.

**Dave Jones:** It's not. It's about 330 ohms. Aha! We've got a 50 ohm terminator on our scope to get rid of all that crap, and bingo, we've got a voltage divider.

**Dave Jones:** So, if you work out how much the signal's being divided time by Well, it's roughly 7 and 1/2 times with that 330 ohms and the 50 in there. So, that's why our amplitude on our differential measurement is so low.

**Dave Jones:** So, to get the true value that you're actually measuring, you have to multiply that by the measured probe. But in this case, well, you wouldn't be using scope probes for this measurement.

**Dave Jones:** So, I've actually Another trap for young players is when you're doing this sort of stuff, you wouldn't be using a scope probe like this. It's good enough to get an indication like this to see if there's any uh you know, get rid of any common mode noise or something like that.

**Dave Jones:** But, hey, in this case, it is not the correct method. You should be using direct coax 50 ohm loaded. So, what we get down to is the ultimate correct method to do differential probing like this.

**Dave Jones:** If you don't have a proper, you know, really expensive high impedance differential probe, this is how you would do it. You'd have your coax from the scope, of course, 50 ohm terminated on the end here, and you would have a 50 ohm source resistance in here as well.

**Dave Jones:** And just to get rid of any DC out of there, you would have AC coupling in both lines, and that is that becomes your differential probe. But, with the two 50 ohms in there, you've still got an attenuator.

**Dave Jones:** So, your final value that you're measuring, hey, you've still got to multiply it by two. So, there you go. But, that is how you would do proper differential measurement with a scope or with a preamplifier.

**Dave Jones:** Usually, you would you know, use a differential measurement into a preamplifier, especially for doing something like the Rigol scope here which has noise. We can't really measure, you know, with even with our 500 microvolts per division here.

**Dave Jones:** It's just not really doable. So, you would typically, you know, whack in a times 10 preamplifier or something like that in there. Yes, you could do this with two single-ended preamplifiers if you wanted to with your scope and stuff like that.

**Dave Jones:** And you know, that is still work, but a proper differential amplifier like that Lecroy one, that's the one you want. So, there's no absolute requirement for actually having the 50 ohm termination here.

**Dave Jones:** If you got a proper differential preamplifier, they usually are high impedance. You know, they'll be 1 meg or 100 meg or, you know, really high impedance and you don't have to do that.

**Dave Jones:** But if you are going to turn them turn terminate them like this like you do for a scope, then well, you're basically looking at, you know, transmission line stuff.

**Dave Jones:** You're supposed to match source and load impedances so you don't get reflections and things like that. So, if you are doing that, yeah, proper 50 ohm source impedance and 50 ohm load over there is the way to do it.

**Dave Jones:** And if you were doing this with the home brew probe approach, of course, you would keep absolute minimum these passing here. You wouldn't have anything exposed. So, you'd have your coax and something like that.

**Dave Jones:** You'd have your 50 ohm in series. They'd be nicely heat shrunk and you'd have your tiny capacitor and you'd connect it directly across your bypass cap of your power supply to be measured.

**Dave Jones:** But you know, really that's just a do-it-yourself sort of a custom hack if you need to. As I said, by far the best way to do it is to use a proper differential probe, preferably with a preamp for measuring low noise power supplies like the Rigol one we just did.

**Dave Jones:** And here's the money shot. You know how I told you that the reason we're doing this differential measurement is so that we can see if this noise that we're getting I'm single-ended probing on back to my Rigol supply here.

**Dave Jones:** So, we get that really horrible noise on there, those spikes. We wanted to know if those spikes were actually coming out of our power supply. Well, if we go up here and take a look at our differential measurement, look, we're probing the exact same point.

**Dave Jones:** No, look, they're gone. With the differential measurement, they're not there at all. So, that noise is not coming from the power supply. But, if you're using that single-ended probing technique, then hey, you could be easily fooled into thinking that power supply was a lot noisier than what it actually is.

**Dave Jones:** And if you're curious to know the frequency of that noise, well, it's around about 142 odd hertz between those with two spikes there and there. So, that's being picked up somewhere from something in this room.

**Dave Jones:** Aha, I found the culprit. It's part of the test setup. Check it out. That's the waveform we're getting now. And but, look what I've done. I've disconnected my electronic load and I've got connected just a resistive dummy load here.

**Dave Jones:** Similar amount of current, we're taking 2 and 1/2 amps instead of 2 amps, but it's vanished. Bingo, it's only when I use connect up my electronic load, it's adding that switching there at 142 hertz.

**Dave Jones:** It's coming from this damn load. So, you've got to be careful of your test setup like this and where your noise is coming from. And if we didn't use our differential probing here to actually confirm that, we would have thought for sure that it was coming from this Rigol power supply, but it wasn't.

**Dave Jones:** This thing's clean as a whistle and this thing is a culprit adding, you know, normally not an issue, but when it's coupled in like this, well, it causes all sorts of stuff, common mode.

**Dave Jones:** So, that's to do with the, you know, the design of it. Who knows where it's picking it up internally, but it's definitely coming out of here and interfering with our test setup.

**Dave Jones:** Ta-da! So, there you go. That's the basics of ripple and noise measurement for a power supply or maybe even one of these brick converters or your circuit or whatever like that.

**Dave Jones:** And we've looked at single-ended probing, we've looked at common mode noise, we've looked at differential probing, we've looked at uh you know, secret attenuation in your crow probe crow cathode ray oscilloscope probe, that's what we call them here in Australia anyway.

**Dave Jones:** Um yeah, your scope probe. And well, there's lots of traps for young players. There's a lot of art which goes into actually getting a real proper measurements on these things and knowing exactly what you're doing and not being fooled especially by common mode noise.

**Dave Jones:** Just because you see it on your scope doesn't mean it's actually coming from your device under test. So, anyway, I probably there's some stuff I haven't covered in there as well.

**Dave Jones:** And yeah, there's there's a lot of around to try and do this right, but hope you learned something there. And if you liked the video, please give it a big thumbs up.

**Dave Jones:** Beauty. And if you want to discuss it, jump on over to the EEVblog forum. That's the place to do it. Linky's down below. Catch you next time.
