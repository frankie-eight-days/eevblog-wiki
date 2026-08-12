---
video_id: d8i125NSaqE
title: EEVblog #1056 - Digilent Open Scope MZ Review
url: https://www.youtube.com/watch?v=d8i125NSaqE
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 33, "3": 53, "4": 73, "5": 89, "6": 105, "7": 117, "8": 133, "9": 149, "10": 165, "11": 189, "12": 205, "13": 221, "14": 241, "15": 253, "16": 265, "17": 281, "18": 301, "19": 321, "20": 341, "21": 361, "22": 377, "23": 389, "24": 409, "25": 429, "26": 449, "27": 469, "28": 485, "29": 505, "30": 521, "31": 537, "32": 549, "33": 569, "34": 585, "35": 605, "36": 617, "37": 641, "38": 661, "39": 677, "40": 693, "41": 709, "42": 729, "43": 745, "44": 769, "45": 789, "46": 805, "47": 821, "48": 845, "49": 869, "50": 889, "51": 913, "52": 925, "53": 949, "54": 969, "55": 985, "56": 997, "57": 1013, "58": 1033, "59": 1053, "60": 1077, "61": 1093, "62": 1117, "63": 1149, "64": 1173, "65": 1197, "66": 1217, "67": 1237, "68": 1265, "69": 1281, "70": 1301, "71": 1317, "72": 1341, "73": 1361, "74": 1385, "75": 1409, "76": 1425, "77": 1449, "78": 1477, "79": 1493, "80": 1513, "81": 1533, "82": 1557, "83": 1577, "84": 1601, "85": 1621, "86": 1641, "87": 1669, "88": 1689, "89": 1705, "90": 1721, "91": 1745, "92": 1769, "93": 1785, "94": 1801, "95": 1825, "96": 1845, "97": 1861, "98": 1881, "99": 1901, "100": 1925, "101": 1941, "102": 1961, "103": 1977, "104": 1997, "105": 2017, "106": 2041, "107": 2061, "108": 2081, "109": 2109, "110": 2141, "111": 2157, "112": 2177, "113": 2193, "114": 2213, "115": 2233, "116": 2253, "117": 2269, "118": 2289, "119": 2313, "120": 2329, "121": 2349, "122": 2365, "123": 2385, "124": 2409, "125": 2425, "126": 2437, "127": 2453, "128": 2473, "129": 2493, "130": 2509, "131": 2529, "132": 2541, "133": 2557, "134": 2573, "135": 2589, "136": 2605, "137": 2617, "138": 2637, "139": 2649, "140": 2665, "141": 2681, "142": 2697}
---

**Dave Jones:** Hi, we're going to check out the Openscope MZ today from Digilent. Thank you very much, Digilent, for sending this one through. I didn't know they were going to do it, but it was a Kickstarter project which raised $107,000, I think, and they got just over

**Dave Jones:** 1,000 backers, and I guess this is one of the first production run. It's an open source, professional open source instrumentation for everyone. So let's check it out. Now, I have actually reviewed the analog Discovery before, which is an excellent little unit, and it's very

**Dave Jones:** popular, and rightly so, especially in, like, education sectors and stuff like that. It's more high-end than this one. This one is actually a 2-channel, 12-bit, 2 MHz bandwidth oscilloscope front-end. So, well, just an ADC. There's no actual, I don't believe there's any actual

**Dave Jones:** analog front-end circuitry on there. At 6.5 M samples per second, so that's good. That's good enough for the 2 MHz claimed bandwidth. And it's got 1 MHz bandwidth, 10 M sample per second generator, and it's got 10 GPIO pins on it that can be used as a

**Dave Jones:** 10-channel logic analyzer as well as output, and just general purpose stuff. And like the analog Discovery, it's got a PSU in there, power supply that can do 50 mA, plus minus 4 volts. I would have liked to have seen that go to 5, but, you know, meh, it is

**Dave Jones:** what it is. Obviously they've taken the 5 volts in from the USB and only giving plus minus 4 volts out, because they haven't put any boost or sepic converter in there or anything like that. And of course the differentiators. This one has Wi-Fi

**Dave Jones:** built into it, so that, you know, you can use it and couple it to your phone or whatnot if you're out in the field, or if you want to put this on like a portable device and then monitor remotely, that could be good.

**Dave Jones:** You just power it from the thing that you're mounting it onto so it could be very handy. Anyway, let's check it out, shall we? The Openscope MZ. It is $89, and by the way, that is a good price compared to the analog Discovery

**Dave Jones:** which is $279. It's not cheap, the analog Discovery. I'm not sure if they still have the educational discount for that, but it is, you know, it's worth it. Because the software, the Waveform software is very good. They have new software for this called Waveforms Lite, which you

**Dave Jones:** no doubt check out. Ta-da! We have our, just our probes, in quote mark. Good for logic analyzer, not any good for any sort of you know, oscilloscope type functionality. Hey, that's neat. Look at that. They've put a cutout in there just for the jumper.

**Dave Jones:** So there you go. That's all we get. That's all she wrote. And there we go. That's a neat looking board. Don't mind that at all. Purple. Oh, and of course the big thing about this Openscope, because it's supposedly open source, whereas the analog Discovery is not open source.

**Dave Jones:** So we'll check that out later. I don't see any open source logo on here at all. They're not using the regular gear logo or my gear logo, which I highly recommend. I might have to link it in at the end of this. Which is gaining some

**Dave Jones:** traction by the way. Some people are starting to use that. So we don't know the degree of openness. They're just calling it like open source. I don't know if it's full open source hardware or open source software or whatnot. We'll find out. And they promote this as a, you know, a portable

**Dave Jones:** instrument. A portable measurement instrument, but quite frankly with just these sort of interface leads, it's not really very good as a scope. I mean, at least the analog Discovery has the proper case around it and it's got the BNC expansion thing, so you can actually put

**Dave Jones:** regular probes on it and stuff like that. I don't, there is a 3D printed case for this, which is kind of cool. I guess you can just download the files and 3D print your own case. But like, you know, I don't know. With the

**Dave Jones:** 0.1 inch header interface and just the leads like this, I don't think it's hugely useful as a portable measurement tool. It's more like a bench type thing. So if you've got that, well why not just use the analog Discovery? Okay, well this one's a bit cheaper.

**Dave Jones:** But if you're using, you know, if you're out in the field doing measurements and you're using the WiFi or whatnot, then well, you want to be able to probe stuff. And it's just, anyway. I mean, I'm sure a lot of people will find it useful.

**Dave Jones:** But let's take a look at some of the chips on here. Now here's a change. They've actually gone for a PIC32MZ, a reasonably powerful little 32-bit processor. But why they've chosen that one, I don't know. The analog Discovery, of course, had, I think it was a Xilinx

**Dave Jones:** FPGA in it. Probably running some soft core thing, we just don't know, because it wasn't open like this one. But anyway, they've chosen PIC. And curiously, check this out. Microchip as well for the that's a lot of pins on there, for the WiFi

**Dave Jones:** module. I didn't know Microchip were rolling their own WiFi modules or whatnot. So they obviously maybe got a real good deal from Microchip to do that, perhaps. Anyway, so yes, they've changed the platform completely. So obviously it's not, well, it could be built on some of the

**Dave Jones:** same code, I guess, as the analog Discovery, but yeah, it's just like a different architecture. So maybe you can reuse some routines, but yeah. Totally different. And as far as the analog input circuitry goes, you won't find like the same differential capability that you'll get on the analog Discovery.

**Dave Jones:** So that's a bit of, that was actually quite nice. But this is lower performance. You wouldn't expect it. Single-ended. We've got a Microchip 10 MHz op-amp on here. There's one of those for each channel. There's another one on the bottom there. And they've just got various

**Dave Jones:** gain ranges with these muxes here. And here's the schematic. You can work it out for yourself. And there's various gain ranges that they've put into this thing. So yeah, it can go from a reasonable, I think a plus-minus 20 volt range, is it?

**Dave Jones:** Right down to a relatively low one. So that's alright. No worries. You don't really need on a portable thing like this 20 volts is plenty. Then you've got the old-fashioned LMV 324 in there. And that just goes. The analog the ADC, the 10-bit, sorry, the 12-bit

**Dave Jones:** 2 MHz ADC is built into the PIC32 there. So there's not much else. We've got an FT232 of course, classic for your USB interface. It looks like we have some power supply stuff up there. 3.3 volt low dropout reg. And well there's not much else.

**Dave Jones:** A couple of switches here. What is BTNP and BTNR? Huh? Don't get it. As for the function generator, the DAC for that is not built into the PIC32. They're actually, here's the schematic they're actually using an R2R ladder network to actually do that.

**Dave Jones:** That's a little bit how you're doing. I mean, maybe they were, right, are there any PIC32s with a DAC? Oh, and their schematic actually says plus minus 5 volt output on both of those dual channel power supplies. So, I don't know their marketing specs are a bit out there.

**Dave Jones:** Anyway, the hardware is very basic. Pretty much what you'd expect apart from the R2R ladder DAC there, which is a bit surprising. But it all comes down to, with this sort of thing, comes down to the software. So, let's have a look at how you can connect.

**Dave Jones:** You can connect either via the Wi-Fi or USB I believe. Why it'd be nice if it was backward compatible with the Waveforms software, but they've got this new software, presumably because they've got entirely new PIC32 in here. So it has to be its own

**Dave Jones:** product. That's a bit of a shame. I don't know why they couldn't have taken the Analog Discovery and got the price point of that one down a bit more by just using a different, you know, converter chip. You know, I think they used like a, yeah, they used a big

**Dave Jones:** 14-bit expensive one on the 100 meg samples per second 14-bit in the Analog Discovery. Why you wouldn't reuse all that good software that they'd already written and just get the price point down for this one? And just whack on the Wi-Fi. I don't know, strange.

**Dave Jones:** Alright, so let's actually plug this thing in and give it a burl shall we? On the product page here, it's actually, of course you can order the thing, but it's actually quite disappointing. Yes, they have a PDF schematic and a data sheet, but that's about all she wrote.

**Dave Jones:** For all the good stuff you've actually got to go to the resource center down here and you go, aha! Check it out! We've actually got everything. Look, it's got the FRITZ! in parts, the schematic REVF in PDF, the schematic changelog. Looks like it may not have the original schematic

**Dave Jones:** file, I'm not sure. That could be in the GitHub repro. But look, it's got a Thingiverse 3D printable case, the acrylic case, zip files, presumably the mechanical CAD package, whatever they use. All sorts of stuff. It's fantastic! And more than that, look at all the tutorials.

**Dave Jones:** Getting started with the OpenScopeMZ, the setup, and all sorts of jazz. Update the firmware, calibration, WiFi setup, which we'll try out all sorts of stuff. So there you go, we can go into the getting started but basically what we want is the setup here.

**Dave Jones:** So we'll go into the setup and basically if you want to run this on Windows or Mac or Linux, you've got to download this DigiLint agent, which I have downloaded and it sits in the bottom corner down here. And whoop, there it is, DigiLint agent.

**Dave Jones:** And as I said, the Waveforms Live, it looks like it's only available online, because if you go in here and you launch Waveforms Live, it simply takes you to a tab where you can add your device. Okay, well, great, but yeah, I much prefer a standalone program, because if the internet

**Dave Jones:** is dead, the interwebs is down, then your product is useless. Alright, let's see if this thing works. Let's plug it in, I've installed my DigiLint agent, plug it into the USB, we'll do the WiFi later. I heard a beep, and I guess Windows, I think it

**Dave Jones:** I believe it's a serial port, anyway, add a device, agent, local host, I believe that's what we do, and we just go plus, connect into, it's only one com three, so that's got to be it, because I don't think I'd ordinarily have a

**Dave Jones:** com. So I guess open, it's a bit clunky, retry emulator, firmware update required, now we take into the update firmware wizard. That's nice that it kind of, okay, so out of the box we're, what? Up to current firmware. Point, oh wow, we're way behind.

**Dave Jones:** Way behind. Alright, we'll update that, let's see if the firmware transfer in the hex file. It's all pretty seamless at the moment. Yeah, there we go. Lights are flashing, everything's hunky-dory. Reconnecting, of course it's got to reboot the firmware. Come on, you can do it.

**Dave Jones:** Done. Uncalibrate, your device is uncalibrated, you'll be now taken to the calibration wizard. Oh, I guess it's nice that it takes you through your wizard like this. Connect, oh, what? I've got to, why do I have to calibrate this thing? I mean, what are we

**Dave Jones:** actually calibrating? Like the R2R ladder network or something? I don't get it. Hang on. Alright, so I've got to connect the solid red wire to the solid orange, solid blue to solid white. Of course they don't include any, like little jumper pins or anything in the kit.

**Dave Jones:** All you get is the females, you don't get any male pins, so I had to get those. And ready to calibrate. So this must be calibrating the DC, the two DC power supplies. So anyway, let's go, let's begin. And, I don't know, it like, would have been much easier if you

**Dave Jones:** surely they could have designed it without needing calibration. Anyway, should take about 30 seconds. Come on. You can do it. That's a long time for a it's probably like stepping it all the way through or something like that. Would have been nice if it told you what it was actually doing

**Dave Jones:** and why it has to do it. Like, hey, it's important that we calibrate, sorry for the inconvenience, but it's important that we calibrate the here we go, source calibrated ideal 4, calibrated A, these are our percentage difference. Okay, so there we go. Okay, maybe they're just

**Dave Jones:** calibrating out a little bit of error there, just to get better. Specs, which is all hunky-dory, presumably all referenced back because I don't, I'm not sure if there was an external voltage reference chip on here, but they might be using the one built into the PIC32

**Dave Jones:** ADC. Done. I guess I can save that for, as being implied, the instrument was lost when powered down. What? What? Are they seriously telling me that they have to reload this calibration for every time you power this up? No way. That's an epic fail, if that's the case.

**Dave Jones:** That's just ridiculous. I've got a storage location, flash, okay, flash, so I've got to save it to the, I'm saving it to the built-in flash on there, and then, right. Done. Okay. Surely it won't require me to redo that. Hmm. Anyway, there you go.

**Dave Jones:** Okay, we can now set up Wi-Fi and all that sort of stuff, which we'll do later. I presumably can't set up the Wi-Fi, of course, without plugging in the USB. Calibration is done. It's stored in flash, surely. Can't be serious. Anyway, done. Alright, there you go.

**Dave Jones:** Host name, open scope. Can we just open it? Connect in. Yay! That's what we want. There you go. Millivolts, 500 millivolts per division. Thank you very much. And trigger in the middle. Beautiful. Alright. Wavegen. It's not an arbitrary waveform gen, which I believe the analog discovery

**Dave Jones:** was, so it's just a basic function gen. But you can go up to, looks like 3 volts peak-to-peak is the highest you can go. That's okay, you know, for a device like this, that's fine. You can offset in 100 millivolts steps up to plus minus one and a half.

**Dave Jones:** So that's pretty groovy. It's good to have the ability to DC offset. And the frequency is, can we I mean, presumably we can just type in 100. If we just type in 100, can we? No? Set wavegen, like 40 kilohertz. What? 100. Like I can't press enter and like 100k.

**Dave Jones:** Can I just press like, no. It would be nice if I could just type in 100k and then press enter. So what, I can only go up in steps? I can't do any finer steps? That's nuts. And there we go. We turned it off and on.

**Dave Jones:** Everything's on by default. So the wavegen's on by default. Is it? Is that, I assume that switches off the output. Hmm. Anyway, let me see if I can hook the function gen up to the scope and see what's what. Now one of the

**Dave Jones:** problems here is while all the wires are color coded, okay, great. You know, you're out in the field using this thing and you just want to hook it up you've got to remember what colors are what. I mean, there's no labels on there.

**Dave Jones:** You know, this sort of price bracket, I guess you wouldn't expect individually labeled, but yeah, you've got to know which one's what. Or you've got to label them yourself. So yeah, that's not terrific. Right, and if we scroll down here, they've got a pinout

**Dave Jones:** printout, but this is basically useless. It's not color coded, it doesn't really explain anything what any of these things do. So that's, I don't even know why they bother having that. But luckily down here, they have this nice color coded pinout. Anyway, we've got a, we've got the grounds here,

**Dave Jones:** the analog inputs, oscilloscope one, oh, arbitrary waveform gen, it is saying arbitrary. So we didn't see any arbitrary capability, maybe it is deeper inside there. Trigger and trigger out, which is nice, trigger external stuff, and then your 8 data well, 8? 7? I guess?

**Dave Jones:** Maybe the triggering can be used oh no, D09, okay, D1 to D10, and then they've just got looks like, you know, just dedicated pins on the micro. Like, that's a little bit confusing to people who don't know the microcontroller labeling and stuff like that, but they're just the microcontroller pins.

**Dave Jones:** Would have been nicer to extract that outer layer, but just a small thing. Right, so let's have a look here, I've got my ARB gen output yellow connected to channel 1 input, over here we've got our trigger settings, we want channel 1 trigger line level

**Dave Jones:** 500 millivolts, whatever, and oscilloscope channel 1, oscilloscope channel 2 which we can just switch, well, yeah, off, so we've got it doesn't switch the grid off, it just switches the waveform off, okay no worries. We've got 500 millivolts per division, so if we go like that, yep

**Dave Jones:** no worries, plus minus 25, and we go down to, oh, 2 millivolts per division, that's alright, anyway let's give that a little run, and see oh, single, okay where's the auto trigger? We're getting zippity-doo-dah oh, there we go, we're in like Flynn alright, we've got to turn our, see, I don't like that

**Dave Jones:** negative like that, that's just, argh, it's just wrong it's just wrong, and the horizontal here it is, there we go, so let's can we go single shot? It just takes forever run, where's our trigger point? Can I, like, I can't right click on here, I can drag across, okay, that's cool

**Dave Jones:** can't do anything with the right button, so but we can, and yeah, we can drag that window across there, okay, the distortion here we're seeing is of course sample distortion so abort, geez alright, level, well, let's go down to zero, we want to trigger on zero

**Dave Jones:** and run, right? why is it not, okay, if you zoom in far enough you actually get to see the sample points, it's kind of nice and you zoom out it gets rid of them of course just to avoid clutter, that's groovy we're armed, force trigger, there we go

**Dave Jones:** no, I've switched my, no wonder I've switched my oscillator off it's on now, sorry, it's, yeah, when it's blue it's on and you can't change stuff while it's on that's a bit annoying, okay, so let's single, there we go now we're talking, alright, that kind of makes sense

**Dave Jones:** and if we, woah, woah, look at all that sample distortion wow, what's going on there? did that, like, what? it's just armed and re-trigger wow, oi, there it is again, geez, that's a problem, isn't it? wow, that's glitchy as, that's ridiculous, you can't have

**Dave Jones:** that, that is so buggy nah, that's, that's an epic fail, right there will we get the sample distortion if we zoom right in like that, yeah, yeah you can see it in the top window, I like, you know, they have the typical magnified

**Dave Jones:** window up the top, but look, the amplitude was jumping, look, and that sample distortion, so we're not seeing that unless we go right out maybe we'll get it again, but geez, that's, yeah, look at that, that's ridiculous it's a terrible mural, so why the trigger level here

**Dave Jones:** doesn't have, oh god, it's horrible, why it doesn't, like, have the ability to go plus minus on the trigger level, and, like, you have to actually type that in, so, I don't know what's going on there anyway, I set my trigger level to 2 volts, and

**Dave Jones:** it's still triggering, why is it still triggering, single shot, idle, okay so it must have some sort of auto auto sample there, because then if I change that down to 1 volt it should, I've got to redo single do I, no, look, I'm going trigger level 1 volt, it should be

**Dave Jones:** it should trigger at that point there, at that one point, I like the little info there that comes up with the voltage and the time, relative to the 0 point, how do you get back to 0? how do you reset the horizontal back to 0?

**Dave Jones:** center view on trigger, ha, there we go, easy peasy lemon squeezy, okay, so it's triggering on 0 volts, 0.5 500 millivolts, it's triggering on 500, yeah, it's going to make an idiot out of me, I don't know why it wasn't triggering before, and then if we go 1.5

**Dave Jones:** should still trigger, just, yep but if we go 1.6, it shouldn't trigger should just sit there arming, yep, so that's all good, alright no wucker's got to abort that, run it armed no, there is no auto, so that's it okay, it's all pretty rudimentary, not happy that

**Dave Jones:** you can't adjust the wavegen in real time without switching it off, I mean that's just, it's an annoying limitation, it's not a showstopper but geez, it would have been nice to because if I run that, right, now it's not doing anything until I switch

**Dave Jones:** the wavegen on, and I can't modify anything I've got to stop it, triangle please and switch it on, go, there we go square wave please sir, oh that's sample corruption, how do you get sample corruption like that, that's remarkable, hang on, we haven't turned on the wave

**Dave Jones:** it's updating, it's updating, but we haven't turned on the wavegen, what the, and now it's stopped, what, it's like it's inverse what, oh yeah, sorry, because I just offsetted my, so the offset works but geez, what's going on wow, this is, no, no, it's pretty clunky

**Dave Jones:** not the least bit impressed, and the logic analyzer, well, what can we do here, geez, I'm on a full HD screen here, like a 1920x1080, and it can't fit all the stuff in there, I've got to do like a little slider, well, okay, granted

**Dave Jones:** if I got rid of my tab bar like my thing up there, or I went to full screen, it'd probably, you know I wouldn't have to do that, but eh, okay, but data corruption, wow, yeah, it shows you the sample rate, number of samples, like let's go

**Dave Jones:** 100 samples, there we go, look at that okay, so that works, it's just, I don't know, the UI is just a bit clunky, not impressed, ah, bode plotting, okay now we're talking, yep, let's, ah, got to calibrate okay, got to calibrate it first, solid

**Dave Jones:** orange to solid yellow, yep, calibrate so we've got to calibrate the bode plot and we're up, there we go frequency one hertz, okay, took a bit, ah, pretty big steps there in the end, goes up to one megahertz, okay start, back to your circuit, click start, well, my

**Dave Jones:** circuit is connected directly, so let's see the direct response, and of course it's scaled, that looks really bad, but it's not, look at the, um, it's actually really quite good look at the amplitude, the dB amplitude over here, it's just auto-scaling right in so it looks bad, but, ah, look, I can't, like

**Dave Jones:** right, like I can't click on that, like I can't control, shift, use my scroll wheel, anything anyway, that is, like, that, trust me, that's flat, if I was able to zoom out on the amplitude, on the Y steps, I can't even adjust export chart, calibrate, auto-scale

**Dave Jones:** yeah, whoa, I can auto-scale, I can't even adjust the amplitude over here, how do I do that? Doesn't seem to be there, that's crazy anyway, because it's so minute, like .005 dB there is like, it's nothing, right, so that's rule of flat if you had that set to like a, you know, a 60 dB scale or something

**Dave Jones:** like that, um, that'd be flat as a tack over the frequency range, so yeah, if we put an RC filter in there, we'd see the response, okay whoop-de-doo, ah, the number of steps, okay, we can do 100, and, there we go it's going to take a bit longer, but that's kind of cool, but

**Dave Jones:** very primitive though, um yeah, not terrific, but, you know, usable I guess, you know, for education stuff, although I still think that the analog discovery is a better educational tool than this, whoa, data corruption why is it, it's gone wow, that is incredible

**Dave Jones:** another one, I'm not touching it, I don't think I'm touching it so maybe that has something to do with the sample calibration problems that we had before, anyway, not really impressed by this, how do I stop, I can't stop it, I can't stop it

**Dave Jones:** once started, oh dear, oh dear I'll get back to you, right, I'm not sure if that locked up or just took forever, but I just had to like go up here to the URL and just reload the damn thing, and that worked, what I do like is that show

**Dave Jones:** device pinout is here, so that's quite nice, you can pop that up in the software someone there was thinking, so, what else have we got, reset device and reinitialize, like, but there's no multimeter thing like, you know, you could have had like multimeter functionality

**Dave Jones:** maybe that's on the Windows, sorry, the phone version I don't know, we can't click on the math thing down there, anyway you know, not hugely impressed, let's go over here settings, zoom on center, oh ok, mouse wheel zoom on mouse, control mouse wheel, ok, gives you the hotkeys

**Dave Jones:** ok, there you go, change volts per division, vertical pan shift plus click and drag, ok shift plus click and drag, there we go that's just moving that, but that's not vertical, that doesn't highlight area and zoom, but we don't, zoom on mouse wheel

**Dave Jones:** control mouse wheel, ok, and I'm just playing around with the simulated version of this, so you can actually try out the software yourself, you just choose the simulated version and if I actually hold down the shift key, I figured out how to do

**Dave Jones:** the vertical there, so hold down shift and use your scroll wheel and then I can just highlight the one I want and then drag that up and down, and then you can of course drag your trigger point here, so that's all ok, you know, all your stuff is not too bad, but the

**Dave Jones:** waveform generator is like really pretty basic, I mean I can't find a way to, is there a way to step that in smaller increments? I just you know, 501, nah bummer. And I can just hold down control and of course zoom that in and out, that's alright, and the

**Dave Jones:** mass functions here, we've got frequency, period, like nothing fancy, like you can't add in equations or do any cool stuff like that, it's just, you know, it's pretty basic, you can't even gate, you can't even highlight a section and then operate on that, it's just the entire

**Dave Jones:** memory or waveform, not sure if that's over the memory range or over the entire memory range or the waveform window range, I presume it's window based. Whoops. And I was actually going to go back in, I'm back at the office now, I don't have access

**Dave Jones:** to the unit so I'm running the simulator, and the bode plot can't work again because I don't have new firmware I don't even have the hardware attached. Oh, anyway it does have FFT capability, it looks pretty rudimentary, nothing to write home about there at all

**Dave Jones:** it's like 600 hertz, there you go, what? Oh, because I didn't change my, there we go, it was on 600, yep, so it's Johnny on the spot, but like rudimentary stuff, and it's got a data logger as well, but I can't check that now because I don't have the correct firmware

**Dave Jones:** on my simulated version. Oh dear. Alright, let's give the analyzer a try down here, I've turned on channel 1, channel 2 I've hooked up an I squared C signal, and I've just gone force like that because I haven't figured out how to trigger from the, I mean I'm

**Dave Jones:** triggering from the logic analyzer, but like where's the, like what source, what channel, what, like, I don't get it. Anyway, like here's our two signals, A1, A2 I'm not sure if you, oh yeah, can we expand, no we can move them, but we can't, can we expand them?

**Dave Jones:** Oh, anyway, we can hold down control and we can zoom in like that, that's alright so let's force, I don't like this, like why does the green oh, hang on, yeah, why does the green line go down like that in the middle, I don't like that at all, that's quite disturbing

**Dave Jones:** so anyway, there we go, we've got our I squared C, but like, there's no protocol analysis or anything by the looks of it, with C, and it's like no auto timing pops up and things like that, you know, I know this is early stage

**Dave Jones:** for the software and stuff like that, but it would have been nice to see it's really pretty rudimentary, you know, maybe it's good enough to see a signal, but I can't even see a way to trigger from the, like oh, hang on, if I turn off my, what if I turn off my scope

**Dave Jones:** here we go, okay, so we're now free running there we go, why that line is still down, that's our centre, is it? that looks like negative and positive, so that's our centre, it can't even go back to the centre, it can't even stay there, wow

**Dave Jones:** look, it's jumping back, that's terrible, Muriel alright, so, but how do we trigger from it source, logic analyser, but how do you choose? well, I went to the trigger section here, and it says any oscilloscope or logic analyser channel, but if I change the trigger source to logic analyser, I have more configuration options

**Dave Jones:** each channel in the logic analyser can be set to a rising edge aha, thought I had to watch the video, stop ah, sorry, that's when the configure comes up and you can choose your channel, okay, excellent and trigger mask, okay, so it's got rudimentary stuff, so rising edge

**Dave Jones:** of the first channel, our clock or whatever, alright, let's see if we can connect to the wifi, shall we, wifi status disconnected why? I want to connect, I've already set up my password for my SSID, which is the NSA, because we want to

**Dave Jones:** hack into the NSA's wifi, and it's not there, RTFM again, okay looks like we might have to re-enumerate up here ta-da, there we go, 192.168.1 129, and we don't want to save that alright, I think we're in like Flynn now, done we are wifi connected, okay, now we should be able to

**Dave Jones:** add a device, networked ah, I forgot what the IP was 129, okay are we in like Flynn, connect to device and navigate to the instrumentation connecting, ah, we're in we're in, analyzer yes, run, force ah, where's our stuff, forcing unlikely due to unarmed trigger

**Dave Jones:** ah, come on, I don't like this, like where's my analyzer gone, like it hasn't even popped up here with the channels I've got analyzer, that's the digital IO, um, I'm sure that works a treat but I've got, not sure how I got my channels

**Dave Jones:** up there before, and it's, and by the way I don't particularly like how it's overlaid on the wave, on the um, oscilloscope screen, I mean, like it's great if you're doing mixed signal analysis of course, the logic analyzer stuff, and the analog stuff as well at the same time, I mean you can time correlate everything, that's fantastic

**Dave Jones:** but if you just want to run the digital analyzer then you should just be able to run the digital analyzer. Now it's almost as if it hasn't connected, alright, well I downloaded and installed the waveform live ah, I was like number 100 to install, like 101 or something

**Dave Jones:** um, and sure enough, um, I can connect, ah, to it and connect into device, bingo, but ah, I cannot get this thing to actually run and do anything, I can't force it, I can't get a waveform up, I don't know what the deal is

**Dave Jones:** it just, cannot turn on the wavegen because the logic analyzer is running, so if you had dreams of being able to use the logic analyzer with the wavegen and the oscilloscope all at once it looks like it can't really do that alright, I got it, I had to actually repower the

**Dave Jones:** open scope itself, and wait a minute for it all to initialize again, I reconnected, and bingo, I've got ah, bleh, yeah, single shot, there we go, so yeah, I think I'm back I think I'm back in business, there you go, channel 1 channel 2, for your analyzer

**Dave Jones:** let's, can we actually try and trigger now maybe, pretty please, with Cherry on top um, it's really frustrating on a phone screen, it's not really I don't know if you can get rid of this panel, it doesn't look like you can get the waveform

**Dave Jones:** full screen, of course better on a tablet, um, or a phablet or one of those stupid newfangled things, um, but yeah on a phone it's pretty cramped, but you know, it's like, it's gonna work there we go, oh, it's tiny tot, like yeah we can zoom that way, okay

**Dave Jones:** oh my goodness, force, let's run force, force, how can I, like zoom in those waveforms, anyway, you've got like cursors down here and stuff like that, and they're not particularly fast, logic analyzer 1 logic analyzer 1, like, yeah type, time, track, voltage, you know, there we go

**Dave Jones:** we can track stuff, but, oh, is it stopped? Anyway, it kind of works, but absolutely useless on a phone, useless as tits on a bull I can't read that at all, I can't see any data on that whatsoever, and if I try and, like, pinch and, like

**Dave Jones:** I can't, can't do anything, I can move back and forth, and once again, that trigger thing that's not even the center of that waveform view, and there's no like trigger delay that I can actually set for this logic analyzer to allow me to, like, it's just triggering on that positive

**Dave Jones:** edge, um, so it's not like I can, you know, wait for a new packet or something like that to do that, um, so that's, you know it's pretty useless. I like how the, look at this waveform view down here is actually auto-scaled and zoomed in to show you the data, whereas this one

**Dave Jones:** over here is full screen if we go like that, should now match. Kind of like that. So that's pretty jazzy. There's significant offset there. There's a 40 millivolt offset Wow! Sorry, yeah, 40 millivolt offset. That's a lot. Is that inherent in the channel?

**Dave Jones:** I thought we calibrated this thing. Anyway, so that's not terrific, but yeah, I like how that auto-zooms in vertically, that's really quite nice. But yeah, there's no trigger hold-off or anything like that trigger delay to allow me to you know, reliably trigger on a

**Dave Jones:** packet after a dead space or anything like that. Nothing basic, and there looks to be no decoders in it, and the interface for the phone is exactly the same as the one you get on the web, which is kind of understandable. So yeah, it's just exactly the same as the

**Dave Jones:** Windows version, I don't know what else to tell you there. It kind of sort of does the job if you want to squint at it, but pretty useless for logic analyzer on a phone. So I think I'll call it quits there, I've pretty much

**Dave Jones:** seen enough. So the OpenScope MZ, what is it? 79 US dollars or something like that? I mean it's reasonable value if it suits your purposes, but it's got a few quirks and the software's missing. It does have the full open source in the GitHub

**Dave Jones:** I haven't really checked it out, but it all seems to be there. But I don't kind of get it when they had the excellent analog discovery and the more mature software involved in that. I don't know why they couldn't have just cost-cut this down to a cheaper version and utilize that software.

**Dave Jones:** Well I probably know the reason actually, it's because this is all closed source. This is not open source at all. Either the software I don't think is open source, or the FPGA and protocol and all the stuff inside of here. Whereas this is fully open source, presumably you can get the firmware for the

**Dave Jones:** network and everything and the software and the whole works. Here's a clip talking about what it's written in, I don't know. Might as well be written in Klingon. Our application software is called Waveforms Live, and it's developed using common web frameworks like Ionic 2 and Angular 2.

**Dave Jones:** Most of our code is written in TypeScript and JavaScript, and will be available on GitHub. When running Waveforms Live in the browser, you can connect to the OpenScope via USB or with Wi-Fi. If you connect with Wi-Fi, you can actually load Waveforms Live from the OpenScope itself.

**Dave Jones:** So yeah, I don't see that the open source nature of this adds a lot. I mean, you know, 99 plus percent of people are not going to care, or not going to well, utilize the open source. You know, it's a nice warm fuzzy

**Dave Jones:** marketing thing, and it's great. I fully support like open source, fantastic. But ultimately at the end of the day, people are just going to buy this and use it with the off-the-shelf software. But it does mean people can write their own software and do all that sort of stuff.

**Dave Jones:** I don't know, I just would have liked to see the cut-down price version of this even if it was closed source, I think. Could be more competitive and utilize all the more mature software that they've got written for this thing, and maybe add on like, of course this one's got the Wi-Fi.

**Dave Jones:** It does ultimately work, but yeah, like, not very good on a phone. They haven't optimized the interface for a phone. It'll work fine on a tablet, I'm sure. You know, if you had an 8 or a 10 inch tablet and a full HD screen, it'd just work like your desktop.

**Dave Jones:** But yeah, I don't know, I can't see a huge market for this one. I mean, this one's absolutely killing it in the educational space and even in the hobbyist market. Even like, this is like $270 I think. I don't think they have like the, I don't even think they have

**Dave Jones:** like the student discount for this anymore. Don't quote me on that. But yeah, anyway, this one is a bit pricey, but it's really quite a much nicer tool than this open source one. But it is only $79, so I don't know, make your own evaluation on that.

**Dave Jones:** But I find it hard to think that this is going to get a big market. It just needs more mature software and also, you know, like it doesn't have the nice differential input that this one had and other stuff. And you've got to dick around a bit with the calibration

**Dave Jones:** on here, which sort of, you know, took the excitement off a bit for this thing. And they don't, oh well, I guess you could design a matching interface just like Digilent. You could get this, which just plugs in there, and then you could get your standard B and C attachments.

**Dave Jones:** Nothing stopping you doing that for something like this. So yeah, can't really give that one a thumbs up at this stage. It might, you know, what are the competing ones with like an interface like this which does it all with a Wi-Fi interface offhand, I'm not sure.

**Dave Jones:** So really it would depend on the competition. If this is the only thing out there in this particular niche space for that sort of thing, then well, you know, it might be valuable to you. So it'd be interesting to compare with others on the market.

**Dave Jones:** But yeah, it needs a bit more maturity, I think. The OpenScope, it's getting there. There's some nice aspects to it I like, but there's just too many little fiddly negative things. Anyway, hope you found that useful. If you did, please give it a big

**Dave Jones:** thumbs up. And as always, discuss down below. Catch you next time. Thanks for watching.
