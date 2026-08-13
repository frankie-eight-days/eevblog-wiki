---
video_id: Aymumu3mYl8
title: EEVblog #692 - Digilent Analog Discovery Review
url: https://www.youtube.com/watch?v=Aymumu3mYl8
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 13, "2": 29, "3": 53, "4": 69, "5": 89, "6": 109, "7": 129, "8": 153, "9": 165, "10": 185, "11": 201, "12": 225, "13": 245, "14": 265, "15": 281, "16": 301, "17": 321, "18": 341, "19": 357, "20": 381, "21": 397, "22": 417, "23": 433, "24": 449, "25": 469, "26": 481, "27": 493, "28": 509, "29": 529, "30": 545, "31": 561, "32": 581, "33": 593, "34": 605, "35": 621, "36": 645, "37": 657, "38": 669, "39": 689, "40": 705, "41": 725, "42": 741, "43": 757, "44": 773, "45": 789, "46": 805, "47": 817, "48": 829, "49": 849, "50": 861, "51": 877, "52": 889, "53": 905, "54": 921, "55": 937, "56": 957, "57": 977, "58": 989, "59": 1005, "60": 1025, "61": 1045, "62": 1057, "63": 1073, "64": 1089, "65": 1105, "66": 1125, "67": 1141, "68": 1157, "69": 1169, "70": 1185, "71": 1205, "72": 1221, "73": 1237, "74": 1253, "75": 1269, "76": 1289, "77": 1301, "78": 1317, "79": 1333, "80": 1349, "81": 1365, "82": 1385, "83": 1401, "84": 1417, "85": 1433, "86": 1453, "87": 1469, "88": 1481, "89": 1497, "90": 1517, "91": 1533, "92": 1549, "93": 1561, "94": 1573, "95": 1593, "96": 1609, "97": 1629, "98": 1645, "99": 1665, "100": 1681, "101": 1705, "102": 1725, "103": 1737, "104": 1753, "105": 1773, "106": 1789, "107": 1801, "108": 1821, "109": 1845, "110": 1861, "111": 1877, "112": 1893, "113": 1909, "114": 1929, "115": 1945, "116": 1965, "117": 1981, "118": 1993, "119": 2005, "120": 2025, "121": 2045, "122": 2061, "123": 2077, "124": 2093, "125": 2109, "126": 2125, "127": 2141, "128": 2153, "129": 2177, "130": 2189, "131": 2209, "132": 2225, "133": 2241, "134": 2257, "135": 2277, "136": 2293, "137": 2305, "138": 2321, "139": 2341, "140": 2357, "141": 2373, "142": 2393, "143": 2413, "144": 2425, "145": 2445, "146": 2461, "147": 2481, "148": 2505, "149": 2529, "150": 2541, "151": 2561, "152": 2581, "153": 2601, "154": 2621, "155": 2641, "156": 2657, "157": 2673, "158": 2689, "159": 2705, "160": 2725, "161": 2741, "162": 2761, "163": 2781, "164": 2801, "165": 2821, "166": 2837, "167": 2857, "168": 2873, "169": 2889, "170": 2909, "171": 2921, "172": 2937, "173": 2953, "174": 2973, "175": 2993, "176": 3009, "177": 3029, "178": 3049, "179": 3061, "180": 3081, "181": 3097, "182": 3117, "183": 3133, "184": 3149, "185": 3157}
---

**Dave Jones:** Hi. There's a lot of people who've wanted me to take a look at this for quite a long time, and sorry it's taken me a long time to get around to it. It's been out for a long time, this thing. Anyway, it's the Analog Discovery from Digilent.

**Dave Jones:** And it's basically, as you can see, it's like a small little USB connected dual-channel oscilloscope, function gen, logic analyzer, power supply, and all sorts of things all built in. And if you have a look at some of the specs, the specs are reasonably impressive.

**Dave Jones:** It's got a 14-bit ADC and DAC, 100 meg samples per second, 16k sample channel memory, it's got fully differential inputs, but don't confuse differential inputs with floating inputs. They're entirely, you know, they are not the same thing. These are differential inputs. But they're still mains earth reference via

**Dave Jones:** the USB cable. Anyway, I've done a whole video on that. It's got 11 meg input, plus minus 20 volts, it does real-time FFTs and complex math and all sorts of weird and wonderful stuff. It's got 5 meg analog signal bandwidth, but not huge.

**Dave Jones:** But when you're talking about a 14-bit ADC, that's pretty darn impressive. So that's one of the big advantages of using a USB scope like this, 14-bit ADC. The function gen, once again, 100 meg samples per second, 14, matching 14-bit ADC, and it does arbitrary stuff, it does sweeps and modulations, we can do

**Dave Jones:** bode plots, fantastic with Nyquist and Nicholas plots and all sorts of weird and wonderful stuff, can drive 50 ohm loads, and it's got 16 digital I.O. channels, 100 meg samples per second, 4k channel memory, that's not much at all. It doesn't say that it actually does any signal compression at all.

**Dave Jones:** So 4k would be okay on a logic analyzer if it was doing compression, but it's not. So, you know, but anyway, it's got basic logic analyzer functionality, and it's got two very low current 50 milliamp power supplies designed for educational use. And this is pretty much what they, what it's geared

**Dave Jones:** towards, especially the pricing. It's $279 as the regular price, but that drops to $157 US academic pricing, or if you're a US student, $99 US, which is pretty impressive value for these sorts of specs. So you just get this with a bunch of interface

**Dave Jones:** cables, some pin headers, and a USB cable I've already taken out. So let's take a squiz at it. So like I said, it's designed to hook up to like a breadboard, and it's got like BNC breakout boards and breadboard kits, and all sorts of weird and wonderful stuff for educational use.

**Dave Jones:** And the software is geared around that with the examples and all sorts of things. Anyway, standard 0.1 inch pin header on the input here. We've got our dual differential inputs here, that down arrow symbol is actually ground. And then we've got our positive and negative supply rails.

**Dave Jones:** So they're plus minus 5 volts. Would have been nice if it had a 3.3 volt output as well, but well, can't have everything. Two waveform 1 and waveform 2, two signal generators, 14-bit DAC in there, you know, pretty powerful. Ground again, T1 and T2, no they're

**Dave Jones:** not temperature, they're actually trigger inputs, and then you've got your 16 digital inputs. And these are all mains earth reference of course. But as I said, the inputs are differential. But ultimately effectively mains earth referenced via the USB cable, which is standard micro USB, which I love, and it's got a headphone output as well.

**Dave Jones:** But that's basically all there is inside this sucker. And of course it uses all analog, or mostly all analog devices parts. They've basically sponsored this thing and Xilinx FPGA or CPLD in there as well. One little thing I don't like is that the silkscreen doesn't line up

**Dave Jones:** precisely with the pins on here. It like, meh, fail. They should have fixed that. Now I believe I've shown this before in a mailbag, but here's a little quick teardown. Nice looking layout here, we've got some input trimmers here, I don't know where my pointer is, sorry,

**Dave Jones:** using my Swiss Army knife. Yeah, all analog devices parts on the inputs. So this would be our dual channel scope here presumably. We've got our input MUX here, we'll go through the schematic for this in a minute. They provide all the schematics and really good technical

**Dave Jones:** documentation for this. The trimmer caps here are for input divider compensation. And this is one of the limitations, as we'll see, of these USB scopes. They don't have real input attenuators. As we'll see, this one only basically has a dual range. So you really need that kick-ass

**Dave Jones:** 14-bit analog to digital converter to get all your ranges. So effectively the ranges are all digital. They're not proper analog gained front-end, so all it selects is between two different dividers there. So that's pretty disappointing. And here's the heart of the beast, the AD90

**Dave Jones:** 648 14-bit dual channel 100 meg sample per second analog to digital converter. And if you're wondering why this thing could potentially be so expensive, well this chip alone in volume is like 70 bucks. And when you buy like 10,000 of them. So I know analog devices are sponsoring this

**Dave Jones:** thing, but it's still a bloody expensive chip. So you're getting some real high-end hardware, especially if you can get it for that $99 price. You're getting some awesomely high-end hardware here for your dollars. So there you go, that's our main ADC there. That's

**Dave Jones:** a dual channel, hence why the sucker has dual channels. So there we've just got our input switches there. We've got some amplification, then our ADC differential driver that drives that. And that's pretty much all for your ADC section of it. Then we've got an FTDI interface chip over here.

**Dave Jones:** FT232, as you're familiar with. Don't want to brick it, do we, with their firmware update? Be careful. Jeez. I'd be pretty confident this one would be genuine, but hey you never know what slips through. And then we've got ourselves the Xilinx part. What's that?

**Dave Jones:** A 6S LX10. So that's one of the smaller Spartan 6 series there. And you know, it's got some reasonable chops there. And clearly the interface from the FTDI there is parallel. You can see all the parallel tracers running over there, got to have that for

**Dave Jones:** the speed of course. And of course the FPGA there is doing all the logic analyzer stuff as well. Nothing fancy there, there's no voltage level threshold set triggering and all that sort of stuff. It's just really, you know, pretty dumbass logic analyzer functionality.

**Dave Jones:** And on the backside, you know, there's a whole bunch of miscellaneous there's our input protection there for our logic analyzer by the looks of it. I haven't looked at the schematic for that. There you go, there's our analog devices TX DAC part. Another expensive 14-bit

**Dave Jones:** DAC and all the miscellaneous circuitry and, you know, output amps to go along with that. It can drive a 50-ohm impedance output. So a pretty chock-a-block board. And if you can get this for $99, it represents pretty darn good value, let me tell you, on the hardware

**Dave Jones:** front, let alone the software. But with these things, it's all about the software. What is this thing capable of? It's got the hardware chops, let's go to the desktop and see if we can have a play around with the software. And here it is.

**Dave Jones:** I won't bore you with all the details of installing it, but no disk actually came with it, or maybe it didn't, I lost it a long time ago. But anyway, very simple and quick download from the website. You install it, no hassles whatsoever.

**Dave Jones:** And then you get your analog and digital functions with more instruments down here, which I'm particularly interested in. And if I plug it in to the USB, a device was detected, you bet your ass we wish to connect to it. And bingo, it enables all of your functionality.

**Dave Jones:** There it is, there's the serial number of the unit. No problems whatsoever. And if we go into the device here, we have a few settings to configure. And this is rather nice, look at the trigger setting for trigger channel 1. You can set it from the input pin, or you can set it from the scope or any of the

**Dave Jones:** wavegen or any one of the particular modules there. And same thing with trigger channel 2 as well. Audio output off on. Watchdog, this is interesting, disable the watchdog, keeps the device outputs enabled after it is disconnected from the PC. I haven't actually looked

**Dave Jones:** into that, but that's rather interesting. And overcurrent protection as well, as we'll see on the schematic. It has quite significant USB overcurrent protection and measurement as well, so very nice. And as we'll see, with everything to do with this, very customizable in most aspects.

**Dave Jones:** This is just the user interface options here, but yeah, very quite nice and flexible. But here we go, we've got our analog and digital instruments. I don't know why they have more instruments down here. Why not just like, well I guess because they're not analog or digital.

**Dave Jones:** Like for example, the one I'm particularly interested in here, the network analyzer. And the voltmeter, well the voltmeter is analog isn't it? You know, why? What's the difference between a voltmeter and voltage here and the spectrum analyzer? Well, you know, the spectrum analyzer is going to be analog isn't it?

**Dave Jones:** Why isn't it in there? I don't know, just seems a bit silly. Anyway, let's not muck around, let's see what we can do with this sucker. Alright, let's start out with a simple voltage here, and you think that's your voltmeter, but it's not.

**Dave Jones:** This is really annoying. This is the power supply that I told you about, the plus minus 50 milliamp hour output. You can turn those off and on here. Has a nice little bar graph to show you. Have stopped due to an overcurrent condition?

**Dave Jones:** What? What? I'm not powering anything! Are you kidding me? I haven't seen this before, this is ridiculous. What? I've got nothing connected to it. Unbelievable. That's got to be a bug. Not sure what's going on there. Oh, okay, not happy with that. Anyway, it's got this wanky little bar graph here that

**Dave Jones:** matches the current. It would have been nice if it could tell you what the actual current was. So this thing, voltage! Why is it labeled voltage? Why is it not labeled power supply? That's just ridiculous. If you want the voltmeter, you've got to go

**Dave Jones:** down here. And yes, you can switch all these devices on and have them open separately for example. Like if you want to run your wavegen and have your scope, hey, you can have them on separate screens or on the same screen or whatever.

**Dave Jones:** And then you can run multiple instruments at once. So it really is quite versatile. Here's our voltmeter, and it does DC, true RMS, and AC RMS as well. Presumably up to the full analog bandwidth of the thing, i.e. the 5 megahertz. Now here is what I told you about before, it only has two

**Dave Jones:** voltage ranges. 25 volts and 2.5 volts. That's it. And this doesn't just apply to the voltmeter, it also applies to the scope as well. So everything else, like for example your scope 10 millivolts per division range, is actually all done in software. It's all digital gain stuff.

**Dave Jones:** So to get your full 14-bit resolution out of this thing, you only get that on either the selectable 2.5 volts range or the 25 volt range. So eh, you know, but it's still good. I mean, you get that 14-bit resolution ADC up to

**Dave Jones:** full 5 megahertz bandwidth. Really very, very nice. So there you go, that's just a very simple voltmeter. Can't do anything else there at all except turn it off and on. And then you've just got some boring stuff here for the static I.O. You can turn each individual bit off or

**Dave Jones:** on, but you can have a 7-segment display. Look at that, you can actually configure that. So that's rather actually quite nice. You can have a slider here which generates a value, a digital value on the outside. You know, even though it's like just a basic

**Dave Jones:** I.O. interface, it really is quite neat. They've done nice work there on interfacing that. So great learning tool for just, you know, experimenting, mucking around with the digital outputs. So for each one of these, you can actually right-click on these and it can be an

**Dave Jones:** LED, you can have like a push button here. So look, that's really quite neat. You can have a push-pull switch, nice. A slider switch, 3-state switch, there we go. You can set high impedance as well. And an open source switch and an open drain switch.

**Dave Jones:** Wow! Really great learning tool, this thing. They've really thought about that. That is very neat. And then we've got our digital pattern generator here, and this is quite powerful and flexible as well. And yes, we can like go full screen on any of these instruments like this.

**Dave Jones:** So, you know, we'll show you that later in the much more versatile for the scope for example. But look, we can go in here and we can insert signals, we can insert bus signals. So we can go in here and say that digital pin 15,

**Dave Jones:** what type is it? Is it a constant value? Is it a clock? Is it a random signal? I mean, just fantastic. Here we go. And we can define the duty cycle of the clock and the frequency and the idle time and the output type.

**Dave Jones:** And it's just, yeah, fantastic. Very, very flexible. So what I've done here is I've just generated a clock signal there on pin 15. On pin 14 I've just generated a random frequency between the values 1 kHz and 10 kHz. So really flexible. You can

**Dave Jones:** set that up and we can run that. And then we can call up our logic analyzer instrument over here. It works a similar sort of way. We can insert all of our view, all of our signals here, and we can run that. And

**Dave Jones:** bingo, there's our clock and our waveform being generated out of these things. Absolutely fantastic on those pins. Because it's able to read back what it's outputting. So I didn't have to loop these back. I could have looped them back to channels 1 and 2 or something

**Dave Jones:** like that if I really wanted to. And then because they aren't triggered there, we can go in and we can say we want a trigger on the rising edge of that clock signal. Thank you very much. So now our clock signal is stable

**Dave Jones:** and there's just our random frequency between 1 kHz and 2 kHz on the second channel there. So that's terrific. And we can set up auto, normal mode, and we can do all sorts of regular set up your buffer size for example. And we can

**Dave Jones:** of course now see that I've actually stopped the digital pattern generator up here so we're getting nothing on our logic analyzer. So if we run our pattern generator, bingo, automatically shows up in our logic analyzer there. And of course we can go full screen on that so we can have all of our 16 channels set up

**Dave Jones:** there. And we can view lots of different stuff as well. So we can view data table for example. We can view events. We can view... well no, that's it. Or we can zoom in part of it. There we go, I've got a zoomed in

**Dave Jones:** screen right here. So now we're actually zooming in to that trigger edge signal there. And of course we can scroll this along, but we only have a small memory here. It's only using, as it says up here, 2048 samples at 200 kHz. That's what it's currently

**Dave Jones:** sampling at. So it does no sample compression that I'm aware of, and yeah. So it's a reasonably limited logic analyzer, but the amount of capability in here, just from the software side of things, yeah, very impressive. And of course everyone's going to want to know, can it decode buses as

**Dave Jones:** well? Well here we go. We can insert interpreter here, and we can actually set these up and define our signals. I don't have a bus hooked up at the moment, I could, but I'm not going to be actually bothering testing it. But there we go,

**Dave Jones:** we can do SPI, I squared C, and UART as well. So looks like it has all the functionality. There we go, we can get, oh, ones and twos complement. All sorts of weird and wonderful output formats there, and I squared C, and we can set up which channels we want those on, and UART

**Dave Jones:** as well. That'll go up to 230k board. Very, very nice. So there you go. It's got all that capability built in, so quite a useful logic analyzer apart from protocol decoder. I'm going to assume the protocol decoder works, so I'll give it the benefit of the doubt.

**Dave Jones:** And it's pretty good for the only limitation is the 4k sample memory, that's it. And about the only limitation in this pattern generator I'm not seeing here is it can't, looks like it can't generate, while it can do busses, and look you can set up B-endian, little-endian, that sort of jazz, it can't like simulate

**Dave Jones:** a, or generate an SPI or an I squared C buss by the looks of it. But I stand to be corrected if it is buried in there somewhere. And I'm keen to jump straight to that network analyzer. So, hey, let's hook up our microcurrent here.

**Dave Jones:** I've got the waveform output going to the input of my microcurrent. I've got it set to the 1 millivolt per nanoamp range, but we're basically not measuring current here, we're using it as a times 100 voltage amplifier. And the output going into the

**Dave Jones:** differential channel 1 there of the scope. So let's see if we can sweep this thing over its frequency range and get a bode plot of its frequency response. Alright, so let's do this. I'm going to jump straight into the good stuff, the network

**Dave Jones:** analyzer, because this is some powerful functionality. When you combine a function generator with a scope like this, especially at 14 bits for the generator and for the scope up front end. Absolutely fantastic. So this is the network analyzer screen. Let's go to full screen here.

**Dave Jones:** And by default we've got ourselves the magnitude and phase bode plot here. And no, for those who want to complain, I'm not going to say bode. Here in Australia it's bode, okay? I know the guys naming whatever languages pronounce bode, but no. In Australia, bode, okay?

**Dave Jones:** This is a bode plot. Don't want to hear another bloody word about it. Okay, so what we want to do is the bode scale up here, because we've got a times 100 amplifier here, what is that in dB, in voltage gain in dB?

**Dave Jones:** Well, for every 20 dB gain, that's times 10. So if it's times 100, it's double that, it's 40 dB. If it's times 10, it'd be 60 dB, and so on. That's just a good rule of thumb to remember. So we expect to get a flat

**Dave Jones:** response here of 40 dB, like this, and then roll off at I think it's 300 kHz or thereabouts, minus 3 dB down at 300 kHz is the bandwidth for the new microcurrent gold here. So we can set this the top part of the scale.

**Dave Jones:** I'm going to actually type in a value there, so I can type my own by the looks of it. And let's go down to say, yeah, 20 at the lowest. So here we go, it's scaled it from 45 dB over here to 25 dB here.

**Dave Jones:** And one thing I like is that you can just drag it like this, which is really quite usable. Anyway, our amplitude, because it's times 100 amplifier, we want a small signal scale output. So 1 millivolt sorry, 10 millivolt amplitude output will give us

**Dave Jones:** a 1 volt magnitude output. So that's really quite nice. We've got 100 steps here. And our frequency range, let's sweep it from say 10 Hz to 1 MHz, because we expect the bandwidth to go up to about 300 kHz. So that's what we've

**Dave Jones:** got here on our x-axis, 10 Hz to 1 MHz. So let's run it and see what we get. If I've hooked it up correctly, we should get a flat line at 40 dB rolling off at some point. And if I've turned it on, yep, there we go, look at that.

**Dave Jones:** 40 dB. The only thing I don't like about this, hang on, will it roll off? Will it roll off? It's rolling off! There we go, yay! So at 100 kHz here, it's just continuously going here, so I can stop that. You can do single shot or

**Dave Jones:** continuous run here. So yeah, it's rolled off at say 300 kHz there. There we go, 300 kHz, it's starting to drop down. You know, it's getting a bit better if you calculate 3 dB down there. It's getting a bit better than the claimed 300 kHz bandwidth there.

**Dave Jones:** So there you go, that's exactly what we expect. And one thing I like about this, you see how it's got all the little marker points there for each sample, because it's taken 100 of them. If we actually go out like that, if a smaller screen like that, it's smart enough not to crowd

**Dave Jones:** up the thing with all those sample little Xs. It turns them off. Just a really nice little touch there. Somebody was thinking. And we can get more resolution on that. I've changed it to 1000 steps here, so now it's going to take some time.

**Dave Jones:** It's very slow at these lower frequencies of course, but it should slowly speed up and get all the way across there. But this will be 1000 sample points across that entire frequency sweep. So it's generating at each point and it's then generating that fixed frequency.

**Dave Jones:** Like at the moment it's just about to hit 100 Hz, 80, 90 Hz, 100 Hz, boom, it generates 100 Hz and then takes the measurement. And we can go up and change those in the settings. If we go up here, here we go, our

**Dave Jones:** settle time, look at that, 10 milliseconds, we can change that minimum period. And of course our FFT window, we've got a whole bunch of all the usual suspects, the Blackman Harris and the Hamming and the Triangular, Rectangular, all sorts of stuff. So by default it's using Flattop here, I won't go into Windows

**Dave Jones:** but oh, it just stopped. Didn't like that. There you go. And here we go, we're getting there and you can see it's faster at the moment. All these little, you see how they're little jaggies like this? I'm going to presume that that's not my microcurrent.

**Dave Jones:** I've tested the microcurrent with really high end $30,000 gear and it's flat as a tack. So what that's going to be, just those little aberrations there, is going to be because we're generating this tiny little amplitude here, so let's stop that, tiny little amplitude of 10 mV here, so we're

**Dave Jones:** right down at the bottom end capability of what this function generator is capable of. Remember it was that fixed 2.5 V output scale, I believe it is. So yeah, we're trying to generate very small amplitude signals. So there's just going to be some error

**Dave Jones:** in the amplitude of the signal there, so that's why our waveform's a bit noisy right down at the low end. So this isn't the best low end tool, as we'll see on the scope as well. Yeah, it says it's got 500 mV per division capability, but nah, in practice

**Dave Jones:** it's going to be useless. And of course we can actually turn on the second channel as well, so we can actually get, well, it's the phase response of the second channel, and the second channel would actually show up on here as well, but it's way off scale.

**Dave Jones:** But yeah, of course it's a 2-channel scope, so we can use that to get our phase and magnitude responses there. So we can actually get this to see the output as well, and get the phase response. So there we go, if we hook up channel 2 to our input, so it's reading

**Dave Jones:** our 10 mV amplitude output signal here, then we can actually get the phase response here between the input and the output. And as you can see, it's 0 degrees, and then up it just starts to climb and climb and climb until we get right up past the

**Dave Jones:** minus 3 dB point, where it goes a bit silly. And then we can use it to check the performance of itself. So what I've got here is I've just fed the function generator waveform 1 output just through to channel 1. Just fed it right back in, and there we go.

**Dave Jones:** We set it over its maximum stop frequency range, so 10 Hz to 10 MHz here. And you remember how the spec said it's got a claimed 5 MHz bandwidth? Well, let's check it out here. That's 1 MHz, 2, 3, 4, 5, there it is.

**Dave Jones:** It's only like half a dB down, or 1 dB down at 5 MHz. So it's got better than its rated performance there. But yeah, anyway, that's just a quick and dirty way to check itself. And you know how I told you that this waveform here was just basically

**Dave Jones:** noise because we're down at the very low amplitude signal level there? Well, we should be able to prove that by increasing that to 1 volt here. You see how sort of jaggy it all is at the moment? Well, let's select 1 volt, it'll start again.

**Dave Jones:** And it should, if it's any good, be flat as a tack, and there we go. It's flattening up. Yep. Bingo! Little hump there, look at that. Little hump. Don't know what that is, but yeah. See? We're getting quite close there. We can change our scale

**Dave Jones:** in there to say 2 dB, or something like that, and change our scale to 5, so I can actually zoom in on that and see that hump a bit better. So I'm going to assume that the ADC's okay, and that's just a function

**Dave Jones:** of our siggen output. It's not completely rule of flat, but it's still within, you know, 0.1 dB or something. So it's, you know, it's pretty darn good, and there we go. It's, you know, at 3 dB down, it basically is 3 dB down at 10 MHz.

**Dave Jones:** So this entire system bandwidth, including DAC and ADC, effectively got a 10 MHz bandwidth here. Now about the only thing that I find lacking on this thing is measurement cursor capability. Like I expect to you know, as I move my cursor over here, I expect to be able to actually

**Dave Jones:** get some, we can add like a push pin and add notes and things like that, but you know, I expect some sort of measurement capability here. And really, we just don't get it. And by the way, here we go, here's the other views we can get.

**Dave Jones:** We can actually get the signal waveform as well. So the time, basically it's got time there, so they're basically saying the time domain signal there. And other advanced tools that it's got here are the views. Look at this, Nyquist plot. I won't go into what Nyquist plot is, it's for control

**Dave Jones:** theory, it has uses in control theory and stuff like that, so real and imaginary axes here. And also, as well, look at this, a Nichols plot as well. So once again this has applications in control theory measurements and things like that, so I won't go into detail.

**Dave Jones:** It's a whole other blog in its own right. But beautiful learning tool. Look at this, it's got the full network analyzer, the Nichols plot, the Nyquist view, and the time domain. Play to your heart's content with this thing, all at 14-bit resolution up to basically 10 MHz bandwidth.

**Dave Jones:** Fantastic. But hey, in my book, being able to get this Bode plot, this transfer function over frequency with 14-bit resolution up to 10 MHz, that alone is worth the price of entry on this tool. Even at the full $270, it's really quite decent performance for the price, really.

**Dave Jones:** But if you can score this for the $99 academic price, do yourself a favor. And yes, very powerful stuff. We can even export this data to CSV, tab-delimited format, fantastic. There's all our data there, there's our 100 sample points, and we can just extract that data so you can do further analysis

**Dave Jones:** on it. Terrific stuff. And you can save headers, comments, labels, yeah, it really is quite powerful functionality. And we can save the image as well, look at that! Oh, we can capture a PNG or a bitmap or whatever. Beautiful. And next up we have our wave gen tool

**Dave Jones:** here, and here we go. Bingo, we can go full screen on this, and we can choose our basic waveforms, but it's a full ARB generator as well, and I won't go into a huge amount of detail, but here we go. And once again, you've got some pretty advanced functionality here.

**Dave Jones:** Just for our basic sine wave, we can set our frequency, our amplitude, offset, and of course we've got two function generators, remember that, so we can stop. I was actually generating the signal there. We can set the symmetry of the waveform, we can set the phase as well.

**Dave Jones:** So this is for our basic stuff. So if we had our symmetry here, we could yeah, our square wave doesn't show, it just auto-scales this screen. But yeah, and then we can sweep, look at this, check it out, we can set our frequency, our amplitude, our offset, our

**Dave Jones:** symmetry, our phase, so we can sweep any of these things, any parameter over time. Oh man, beautiful. So we can just instantly call up our scope here for example, and we can run these, and as I said, we can dock them and do all sorts of

**Dave Jones:** or take them full screen. So our scope is running here, you might see the waveform updating over here, and then we can run our function gen over here, and bingo, we're not triggered properly on that signal, we can just drag our trigger level up and down like that.

**Dave Jones:** Of course this modulated signal is not particularly easy to trigger off, but you know, we can go basically, go into the basic sine wave down here, we're not triggered, and we should be able to trigger off that sucker, there we go. And that's the, you know, just because you've got dual channel

**Dave Jones:** function, arbitrary function gens up here, and a dual channel scope both at 14 bits. But as with all these USB digital scopes, they are no match for a proper, you know, a bench scope with knobs and things like that. It's just not even

**Dave Jones:** close to being the same usability and functionality on the thing. It's just not the same business. I mean, look, we can go in here, you know, we've got all our auto normal stuff, we've even got an auto set button up here, let's actually try that.

**Dave Jones:** And see if our auto set button works. Great for, well, you know, you can argue whether or not it's good for students, it's good for getting something up and running if you need to. And then we can type, then we can do our

**Dave Jones:** trigger source, channel one, or we can channel on the analyzer or the pattern or whatever, so we can actually do cross domain analysis, so we can do digital pattern analyzer for example and actually trigger off that. So very powerful mixed signal trigger capabilities on this thing.

**Dave Jones:** It's fantastic. And yeah, and we can measure all sorts of weird and wonderful things, we can turn measurements off and we can do all sorts of horizontal and vertical measurements here, I'm not sure if it's global, not sure if we can turn on

**Dave Jones:** all of them at once, just give me absolutely everything, but it's got all your usual suspects there in terms of measurement capabilities as well. Dynamic range, ADC bits, ooh, that's interesting. Look at that, dynamic range, resolution. Look, there you go. Hey, that's pretty neat.

**Dave Jones:** I like that. But in terms of actually basic scope functionality, there's no knob front panel interface, like if you want to go over here the time base, okay, here it is. But just to have to select from a menu like that, it doesn't cut the mustard.

**Dave Jones:** It's okay for a USB tool, but for an everyday use digital scope, no. If you want a scope, buy a proper scope. These things are fantastic measurement tools, high order resolution, 14-bit resolution, you can do, you know, for cheap as chips, for $99

**Dave Jones:** academic price, it's an absolute killer product. But for an everyday use scope, these USB scopes just do not cut it. And here's the thing I was telling you about, look, it can go down to 100 microvolts per division. That sounds very impressive, doesn't it folks?

**Dave Jones:** But let me actually disconnect the input there. Now here's the limitation of the analog front end I was telling you about. Look, we're at 1 millivolt per division. Look, it goes down to a ridiculous 100 microvolts per division, but even at 1 millivolt

**Dave Jones:** per division here, and here's where we can select our attenuation range. This is where our true input attenuation is. We've only got two ranges. Times 1 or times 10. So we're times 1, so we're getting the best resolution we can at the low end here.

**Dave Jones:** But you can see look at the bits here. Look, you can see the individual bits like that. It's just, you know, it's no good. If I have a 1 millivolt per division range like this, it's absolutely useless. But this is what this resolution

**Dave Jones:** here actually tells you. There you go, a 340 microvolts resolution. So each bit there is only 340 microvolts resolution, yet it lets you go down to 100 microvolts per division. What's the point when each bit is 340 microvolts? It doesn't show you anything.

**Dave Jones:** So, you know, it's just a bit silly. But at least hey, you do have that full 14-bit range over the 1 volt scale at least. And if we go in here and if we can see, let's change that to times 10. I haven't done this.

**Dave Jones:** But yeah, there we go. Changed it 3.4 millivolts per division. So now, where, you know, even at 10 millivolts per division, there we go, there's 3 bits there. So that's our noise floor. So it's just, you know, sort of like oscillating, flipping between those two bits.

**Dave Jones:** It can't really decide. And also, this function here, show noise band, that turns that noise, the expected noise band of this thing, off and on. So really great learning tool to be able to do this. But we're not done yet. Not by a long shot.

**Dave Jones:** Look at this, there's a whole bunch of other stuff we can view. We can go up to hit the data button here, we can view the actual data, we can view our current as well that we talked about before. Here's where we can change that audio output thing, so we can actually

**Dave Jones:** define that. I'm not sure about more advanced functionality on that, haven't looked into it yet. Yes, we can actually get our digital channels up here in the same window, so we combine our mixed signal analysis. We've got events view as well, and we've got a zoom

**Dave Jones:** view as well, so we can actually call that up. There it is. And look, it shows you where, and you can drag that around, and you can call that up, and you can have multiple zoom functions as well. There we go. You can have

**Dave Jones:** one, where's my other one gone? Oh, they're all over the shop. There we go. I can have two different zoom windows going all up. Yeah, I'd have to have them off screen or whatever on a separate screen. But yeah, you get the idea.

**Dave Jones:** It's pretty much the duck's guts. And then within that zoom view, let alone in the main screen, we can get histograms and FFTs as well, so we can set an FFT of just inside that particular window there. Absolutely brilliant. So yes, we can actually call up an FFT here of our signal,

**Dave Jones:** and there it is. It's all the way right down there. It's only a 1 kHz signal. I think it is frequency. There it is. It has our frequency counter up there. 1 kHz. So there you go, that's our noise floor down at like

**Dave Jones:** minus 90 dB or thereabouts, something like that. You can see some little spurious things happening there, but anyway, let's actually go and use the spectrum analyzer part of this and see if we can actually measure the purity of the signal gen. So here you go, in the waveform generator,

**Dave Jones:** I'm just generating a 100 kHz sine wave here, and that's the channel 1 there, the orange one. As you can see, there's our 100 kHz spike there. And you can see some harmonics down here, but you can also see, look at this, the crosstalk, the

**Dave Jones:** blue one, channel 2 there. There we go, look at that. We're just getting some. That's not surprising, I mean, that we're getting capacitive coupling over to the channel next to it. It's right on the pin header there, so you know, I can actually ground that input and watch that channel 2-1 vanish.

**Dave Jones:** Well there we go, it doesn't quite vanish. I've shorted the differential input of channel 2, and you can see how it's still there, but much lower than it was before when you short that input. Anyway, let's see if we can get some cursors up and measure

**Dave Jones:** this stuff and autoscale it, do all that sort of jazz. There's a few ways we can skin the measurement cat here. I mean, look at this, I've added some automatic measurements here, like the 2nd, 3rd, 4th, 5th harmonic, THD, sine add effective number of bits, signal-to-noise ratio, Spera's free dynamic range,

**Dave Jones:** all sorts of stuff. More than you can poke a stick at, you can add those into the measurement part of the screen here. And then of course we're doing averaging here. Here we go, on our trace, we're doing 100 averages, and you can see it just counting up there

**Dave Jones:** and getting better all the time. We can change that by going in here, and it's not entirely obvious at first glance, you do have to sort of poke around. We can go into trace 1, and here we go, linear RMS average. So we can just do regular sample like that, boom go.

**Dave Jones:** You know, it is quite fast updating, check that out, I don't know, what is that, 20 times a second or something? At least 10 times a second. Anyway, we can do all our different, all our regular culprits here in terms of our FFT

**Dave Jones:** windows, and then we can do all of our linear RMS averaging. As I said, there we go, we can set all that jazz up and we can do pretty much anything we like. Peak hold as well, so here we go. We can do peak hold, so there we go, that gives us our peak

**Dave Jones:** values. And anyway, and then I set up some manual measurement cursors down here, markers up here. So I've set marker 1 here, that's on our fundamental, and then on our harmonic down here, I've actually set that as a delta. So you can set that as normal

**Dave Jones:** and it tells you the actual value down there, there it is, it's actually minus 60, but that's not the difference between our fundamentals. So you can actually go in there and change that to the delta, and then that tells you, there you go, it's minus 57 dB relative

**Dave Jones:** to our marker 1 up there. So anyway, for a 100 kHz sine wave here, THD minus 59, you know, let's give it the benefit of doubt, say it's minus 60 dB or thereabouts, and you know, then we've got our fairly sizable spike down here at the 5th harmonic

**Dave Jones:** of our 100 kHz fundamental. So you know, it's not terrific, but still very very usable. We're now generating a 1 kHz signal here, and this is the there we go, we can set our markers there, and it's very similar to what we got before.

**Dave Jones:** And there's some clever stuff in here with the markers, like this one for example, you can just go, look, bingo, jump to the peak like that, and then this one, you know, jump to the trough down there, and you know, jump to the

**Dave Jones:** next one, and there we go. Beautiful. So there we go, we're getting about, you know, minus 60 dB THD there, so it's good to about 10 bits or thereabouts. And here's something a bit naughty I found, I've switched off my ArbGen so it's not running at all, and looky what we

**Dave Jones:** have here. At 39.4 kHz or thereabouts, look, we've got ourselves a nice little spike. That's got to be one of the internal switch mode power supplies. So oops, maybe they got a little bit of a layout issue there and it's coupling into the input.

**Dave Jones:** That's not great. Anyway, if we go in here and have a look at our waveforms with two shorted inputs, let's turn on the second trace actually. The second waveforms, second channel's a little bit better there. This is over our full range, our full, well, our highest frequency range, 10 MHz to 24

**Dave Jones:** kHz, let's go down a bit on that. And here we go. There we go. That's our noise floor. Effectively, you know, it's down around the 75, 74, minus 74 dBV mark, something like that. And you can see that channel 2 is picking up

**Dave Jones:** something else here. These are with the shorted inputs. And let's go to our lowest frequency range here. So there we go, there's our two channels there. Channel 1 at 39.4 kHz or thereabouts, channel 2 at 2.62. So looks at this, well, actually let's go take a quick look at the schematics now and the

**Dave Jones:** technical reference manual and we'll be able to see that this thing does have some switch mode, a couple of switch mode power supplies in it. So that's got to be where they're coming from. Here we go, we can have a quick squiz here, and this is

**Dave Jones:** actually very impressive. It tells you all about the hardware basically, architectural overview, the block diagram, here it is. Here's our FPGA, ties in our input divider and gain selection here, which as you'll see is very limited. We've got our ADC driver here, our ADC and DAC are 14 bits a pop.

**Dave Jones:** And our voltage reference, which is pretty darn good, it's 1% voltage reference as we'll see. And here we go, an important note, unlike traditional inexpensive scopes, they're fully differential. However a ground connection is still needed to provide a common stable mode voltage. And yeah, as we'll see, it is not a floating

**Dave Jones:** scope, it is still mains earth reference. So it's got standard 1 meg input impedance, let's go down here and have a look. They use analog devices ADG 612 quad switches, it tells you why, because it provides excellent impedance and bandwidth parameters. Well you know, this is basically, this whole project

**Dave Jones:** is one big ad for analog devices. They're heavily subsidizing the chips used in these things. So anyway, here's our front end schematic. So here's our positive and our negative input here. And as you can see, it is ground reference here, so the negative input here

**Dave Jones:** goes down to ground through this resistive divider. So you've already got this divider in here. So you've got some input protection by the fact that you've got this input 820k resistor here fixed. So that's how you can get the 50 volt range on this thing, because you've always got that

**Dave Jones:** divider there, you can't switch it off. So you can only choose, here's our MUX here, you can only choose two different ranges here and here. So that's it. As we saw in the software, times 1 or times 10 range. And here's one of those trimmer caps that we saw before, and then some

**Dave Jones:** fixed shunt range caps across the divider values there. So that's just an input MUX, so that just duplicates on the positive and negative. So you can see that they're both ground reference, which will that ground of course will go through to the USB port, which then goes through to the computer,

**Dave Jones:** and if you're not, unless you're using a battery-powered laptop, then it'll be mainzerfed referenced. So then our positive and negative inputs come in here, and then we're using AD8066s, here we go, and they explain the useful features. So this is a nice little

**Dave Jones:** design guide for students to go through and see why they pick these parts and how the specs are relevant. And I can see how you'd really use this in a classroom environment, a learning environment, a good design example. Anyway, we've got our cells, two separate amps

**Dave Jones:** there because we've got differential, and then our scope reference. Here we go, they use an ADR3412 micropower, 0.1 volts initial accuracy, 8 ppm. It's not a bad little part, especially for something like this. And they use an AD5643 14-bit DAC, and then some

**Dave Jones:** op-amps here. So here's our DAC, right, so these are our voltage output DAC, and then they've got various looks like ranges there which we can select. And not too concerned with the DAC, more concerned with how the ADC and scope front end works.

**Dave Jones:** Anyway, the precision oscillator, it's low jitter, all that sort of stuff. They go, look, they've even got phase noise plots, really quite nice. The total, there's the loop filter, really, you know, really quite jazzy. So then our scope ADC, here it is. So here is our

**Dave Jones:** scope ADC, but oh, right, so this is our ADC, these are our differential inputs for our ADC. We haven't actually got to the differential drivers yet. Or did we skip those? We must have skipped the differential analog drivers. Oh yeah, here they are, sorry.

**Dave Jones:** Scope driver. So these come from the output from the MUX, and then they've got differential drivers for driving the channels here. And then we've got some protection there by the looks of it. And that is pretty much all she wrote. And we've got some advanced

**Dave Jones:** stuff here on the scope signal scaling. This is really quite good, look. And we've got our usable windows here, and I won't go into details on those. No doubt there's some good explanatory text that goes along with that. Scope spectral characteristics here. And we can, there we go, they've used it to measure itself

**Dave Jones:** just like we were doing before. And there we go, there's the specs claimed. They span, you know, spurious free dynamic range up to the Nyquist frequency for a 1 MHz output, 84 dBc. Yeah, okay, we can go in and verify that. And at a maximum 10 MHz

**Dave Jones:** output, that drops down to 75. So there you go. And some stuff on the DAC, the voltage references, offsets, because yeah, we didn't, that's something we didn't play with was the offset in there in the arbitrary function gen. So got all the schematics for it, they've got all the

**Dave Jones:** formulas, everything, there's our audio output driver, and the spectral characteristics, here we go, and all sorts of and the calibration memory as well, which we didn't touch on. It is actually capable of doing and storing its own calibration stuff as well, which is fantastic.

**Dave Jones:** There's our digital inputs, there we go, we saw those clamping diodes there before. Input protection resistors, and that's about all she wrote. You don't need much more for the digital. And here we go, here's the USB power control. I think I mentioned this at the start, it is quite advanced.

**Dave Jones:** We've got a, once again, another ADM, well it's an ADM chip this time, which is a hot-swap controller for USB port, so it's, you know, capable of setting threshold as the value as we saw, you know, over current protection and things like that.

**Dave Jones:** Because there's our current shunt resistor in there, it can measure all that. And it's got like a 12 bit ADC. There we go, you know, it's pretty advanced stuff, and you can probably read that out there in the software somewhere, because we didn't touch on everything

**Dave Jones:** in the software, not at all. And user supplied controls as well, so we can actually measure the current. That's how we saw those, that little bar graph there. Not only for the analog discovery, but they've also got another board, another experimental board, which has like 1.5 amp

**Dave Jones:** power supply output capability with constant current control and all that sort of jazz. But that software is capable of talking to that board as well, but it doesn't, it's a bit limited on the analog discovery one we've got here. And there's our switch mode controllers, folks.

**Dave Jones:** Oh there's your problem! That's causing, we've got a couple of switch modes in there, and they're the ones that are no doubt causing those internal spikes there. There we go, there's quite a few switch modes in there. So they're the culprits, so maybe

**Dave Jones:** for the internal analog supplies and things like that, there we go. Yeah, it's got quite a few in there, so no doubt they've coupled those over. But anyway, it's still a very useful tool, but that 500 microvolts per division. Well this was actually a very lengthy look

**Dave Jones:** at this thing, and I'm sure I didn't, well I definitely know I didn't cover everything in this, but yeah, there's a few limitations to it, but damn, it's an impressive tool, especially if you can get it for the $99 US student price, or even $159

**Dave Jones:** US academic price. Absolute killer. Yes, they've got a Christmas special on, it looks like, but even at $279 like, you know, really just to get the transfer function capability, you know, the 14-bit generation, 14-bit measurement capability, up to, you know, the 5 or 10 megahertz

**Dave Jones:** bandwidth. Just, you know, fantastically versatile tool. So worth having in your kit, I think. And pretty much nails it in regard to capability for as a learning tool. And it can plug into MATLAB as well of course, which is big in the student, not only in the student environment, but in

**Dave Jones:** industry. So that's a huge deal. And as I said, they've got all these parts that go along with it. Here, this would be handy, this little BNC adapter board just to get your signals in and out. And shame it didn't come with any mini, like it should.

**Dave Jones:** They should have just included the adapter board and the mini grabbers and stuff like that. Anyway, they've also got, as I said, this Explorer board as well. And this one has, I believe, like a plus minus 1.5 amp power supply and stuff built in.

**Dave Jones:** So it's powered by this Waveform software that we've been actually playing with here. And the software is pretty much the bomb. It is very, very impressive. A lot of thought, a lot of detail has gone into it. I'm sure over many successive versions and user feedback and stuff like that.

**Dave Jones:** But yeah, they've pretty much nailed the software. So if you want one of these USB scope things just to do, you know, that's the advantage. Don't go out and buy one of these 8-bit USB scopes. You may as well just buy a regular bench scope.

**Dave Jones:** You're just wasting your time. But to get one of these things for its 14-bit capability, it's not going to be true 14-bit capability of course, it's a bit limited. But still, for that sub sort of a couple of megahertz range, it's an absolute

**Dave Jones:** killer. I highly recommend it. It's terrific. So there you go. A couple of little quirks and limitations in it, but geez. Big thumbs up I think to the Analog Discovery. Grab one. So I'll provide links down below to this if you want to

**Dave Jones:** check it out. And you can download the software on your own, but it might have a demo mode. I don't know if you want to play around with it, but you just watched me for an hour bum around with the thing. So there you go.

**Dave Jones:** If you want to discuss it, links down below to the EEVblog forum. I'll leave YouTube or blog comments or whatever. And as always, if you like it, please give it a big thumbs up on YouTube, because that helps a lot. Catch you next time.
