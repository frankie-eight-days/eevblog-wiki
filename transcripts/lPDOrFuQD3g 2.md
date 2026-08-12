---
video_id: lPDOrFuQD3g
title: EEVblog #858 - Red Pitaya
url: https://www.youtube.com/watch?v=lPDOrFuQD3g
source: youtube-asr
timestamps: {"0": 1, "1": 16, "2": 31, "3": 59, "4": 74, "5": 91, "6": 107, "7": 120, "8": 137, "9": 153, "10": 168, "11": 182, "12": 195, "13": 209, "14": 221, "15": 239, "16": 254, "17": 269, "18": 282, "19": 298, "20": 312, "21": 327, "22": 340, "23": 350, "24": 374, "25": 389, "26": 405, "27": 419, "28": 428, "29": 440, "30": 451, "31": 465, "32": 481, "33": 493, "34": 507, "35": 523, "36": 543, "37": 558, "38": 574, "39": 591, "40": 606, "41": 618, "42": 634, "43": 652, "44": 671, "45": 690, "46": 703, "47": 718, "48": 733, "49": 749, "50": 765, "51": 786, "52": 801, "53": 817, "54": 831, "55": 849, "56": 859, "57": 872, "58": 891, "59": 906, "60": 922, "61": 938, "62": 952, "63": 968, "64": 981, "65": 997, "66": 1011, "67": 1026, "68": 1037, "69": 1050, "70": 1063, "71": 1079, "72": 1101, "73": 1114, "74": 1125, "75": 1145, "76": 1160, "77": 1172, "78": 1184, "79": 1200, "80": 1217, "81": 1232, "82": 1245, "83": 1253, "84": 1271, "85": 1290, "86": 1303, "87": 1320, "88": 1333, "89": 1350, "90": 1362, "91": 1376, "92": 1396, "93": 1408, "94": 1425, "95": 1442, "96": 1458, "97": 1477, "98": 1490, "99": 1503, "100": 1514, "101": 1531, "102": 1545, "103": 1559, "104": 1573, "105": 1589, "106": 1602, "107": 1613, "108": 1628, "109": 1642, "110": 1656, "111": 1676, "112": 1690, "113": 1700, "114": 1715, "115": 1725, "116": 1740, "117": 1754, "118": 1768, "119": 1779, "120": 1793, "121": 1809, "122": 1827, "123": 1841, "124": 1854, "125": 1868, "126": 1881, "127": 1897, "128": 1916, "129": 1933, "130": 1954, "131": 1970, "132": 1986, "133": 2001, "134": 2016, "135": 2033, "136": 2051, "137": 2071, "138": 2087, "139": 2098, "140": 2111, "141": 2126, "142": 2148, "143": 2157, "144": 2172, "145": 2187, "146": 2202, "147": 2215, "148": 2231, "149": 2247, "150": 2262, "151": 2277, "152": 2294, "153": 2309, "154": 2324, "155": 2338, "156": 2359, "157": 2377, "158": 2397, "159": 2413, "160": 2428, "161": 2441, "162": 2453, "163": 2468, "164": 2481, "165": 2497, "166": 2512, "167": 2523, "168": 2538, "169": 2554}
---

**Dave Jones:** Hi, we're going to take a look at the Red Pitaya, a roughly $240 not quite a USB oscilloscope. It's more of like a high-performance data acquisition system. Thank you very much for Red Pitaya for sending this one in.

**Dave Jones:** I actually got this in the mailbag a little while back along with an Analog Discovery. And I thought I'd do a video actually comparing the two, but I've already done like a fairly in-depth video on the Analog Discovery board and

**Dave Jones:** it's very similar to the Red Pitaya. So, I thought we'd just have a play around with the Red Pit sexy indeed. And we've got a bunch of high-end hardware in here and we'll take a close look, but of course the main

**Dave Jones:** grunt in this thing is provided by a Xilinx Zynq. This is a This is the 7010 system on chip series and the Zynq processor/FPGAs cuz that's what they are. They're fairly unique in that they have not only a

**Dave Jones:** ARM Cortex A9 in there plus Xilinx Artix FPGA fabric as well. Incredibly powerful beast. These are not cheap devices and this is actually running embedded Linux on this thing. I'm not sure what particular flavor. But we've got 4

**Dave Jones:** gigabit of DDR3 DRAM here. Basically, we've got 1 gig Ethernet over here. We've got a micro SD card. We've got USB and we've got two USB connectors on the bottom as well. One's for power and one's for serial

**Dave Jones:** command type interface. And we've got a bunch of LEDs along here. There's a JTAG port and we've got a bunch of user IO as as which if you use the aluminum case, unfortunately, you can't access, but there's like another clear case version

**Dave Jones:** where you can access these. And there's an additional uh 12-bit, I think, 100 uh K sample per second multi-channel ADC in here and various IO. So, you can control everything. And this is basically not just a USB oscilloscope. It's much, much

**Dave Jones:** more than that, just like the Analog uh Discovery one. It is uh basically a complete uh DAC, a DAQ, a data acquisition system, basically, with dual channel uh 14-bit 125 meg sample uh per second converters, uh dual data

**Dave Jones:** 14-bit DACs as well, and a whole bunch of IO, and running embedded Linux, Ethernet. You can basically, yes, you could use it as an Internet of Things in {quote} marks uh device. And it's basically a uh programming system, kind

**Dave Jones:** of like the you know, like the Raspberry Pi kind of thing. It's got a visual programming environment, which we won't really take a look at in this thing, but it's got uh you can do FPGA development on it inside the uh Xilinx Zynq. And you

**Dave Jones:** can just use it as a uh generic USB oscilloscope if you want. You can use it as a frequency um spectrum analyzer. You can use it as a network analyzer. You can use it as a software-defined radio, cuz it's got a

**Dave Jones:** like a 50 MHz analog uh bandwidth, so anything up to 15 MHz at 14-bit uh conversion. Yeah, it's going to make a decent uh software-defined radio. Uh it's web-based interface, so either uh it can't might My one actually came with

**Dave Jones:** a Wi-Fi dongle on it, or you can use the uh Ethernet. You can uh program and operate this thing remotely from anywhere in the world. You can script it. You can do all sorts of things. And apparently, it's open source, at least

**Dave Jones:** open source software. It's the uh 7010 series uh system on chip. This is not a cheap part at all, um especially in one-off uh quantity. Here's our um analog inputs here. So, here's our ADC. It's an LTC uh 2145. This is not a cheap part. It's

**Dave Jones:** almost the same price as the uh Xilinx Zynq. It's like 50 bucks. Um and one-off uh you know, Digikey type uh price for that puppy. And the performance is absolutely stellar. I'll link in the data sheet down below if you want to

**Dave Jones:** check it out. So, that's a dual channel uh 14-bit 125 megasamples per second. Uh the DAC here, um here's the two DAC outputs. Also 125 megasamples per second, 14 bits as well. That's about half the cost. That's about 25 bucks.

**Dave Jones:** So, if you're wondering why this thing is so expensive, well, there's a fair bit of expensive chips in it. And unless you manufacture a thousand of these or 10,000, you know, it's going to cost a bit. And for those who want to see the

**Dave Jones:** bottom, there we go. Peekaboo. We've got all our bypassing on the bottom of the Zynq there. Tiny. They're little 0402 jobbies by the looks of it. Absolutely tiny. We've got some uh line termination uh stuff here and a few

**Dave Jones:** miscellaneous things. There's our USB. We've got some protection on the USB uh power input there. Looks like we've got a uh a poly switch. And it looks like we've got a programmable attenuator on the front end here. And we've got uh two

**Dave Jones:** well, SATA well, they look like SATA connectors and they are SATA connectors, but they're not designed for SATA. These are synchronization connectors and I haven't looked into the details, but presumably you can sync up the acquisition for big um between boards

**Dave Jones:** for like daisy chain them for big uh multi-channel stuff, but that's just a guess. I haven't even looked. So, that's the Red Pitaya hardware. And yes, it is red solder mask. I love it. Beautiful. One of my favorite solder mask colors,

**Dave Jones:** red. Makes it go faster. Hmm. Anyway, let's take a look at the software. See if we can get this puppy up and running. See if we have any grief or whether it's just going to work like a treat out of

**Dave Jones:** the box. All right, let's see if we can make this red Pitaya do something useful. Now, I've come to the website here. This is my first time using the thing. I don't have any instructions, didn't come with it, at least my one didn't. Anyway, it's

**Dave Jones:** just the brick itself and the website. So, let's take a look. Now, I have actually had a look at the website and it actually confused me for some time exactly what's going on here. I mean, you you play the

**Dave Jones:** video here and it tells you all about this visual programming. You know, visual programming system and things like that. So, you know, like I don't want to program this thing. I just want to use it as an scope, you know, as

**Dave Jones:** a network analyzer. Get a bode plot or something like that. So, how do you do that? Well, like you know, I couldn't immediately like we can browse some apps here and we can do some other stuff and application

**Dave Jones:** marketplace and it has all this, you know, weird and wonderful stuff, but I it actually took me a little bit maybe cuz I'm a bit dumb. You go up to the start here and you can go to the quick

**Dave Jones:** start. So, this is actually a nice step-by-step process. It's look, step number one, prepare the SD card. Mine already came with an SD card, so I presume that they are pre-loaded and everything for me. I don't know if the

**Dave Jones:** one that you will buy will actually come with a pre-loaded SD card or not, but look you can download the image. It's got instructions for Windows and for Linux and everything else. So, you know, you just download it and it creates a

**Dave Jones:** bootable disk image that contains Linux and everything else. Fantastic. And how would you like to connect? The cable connection or wireless connection or direct wireless connection. Um I'm going to go for broke here and I'm going to go for

**Dave Jones:** the wireless. I'm going to plug the Wi-Fi dongle I got in here. And here it is, enter your wireless information and download the configuration file. Now it doesn't tell me, like I presume wireless network information, I'm presuming that's the name of my wireless network

**Dave Jones:** and that's the password. So, I'm going to give that a go and it then I it generates a file and you can download, you put it on the SD card and presumably Bob's your uncle and it should blink at

**Dave Jones:** you when we're done. Let's give it a go. All right, so I downloaded and copied my file. There are two USB connectors on here. You have to plug it into the power one, not the con size in, that's console

**Dave Jones:** like a serial console type thing. So, I've copied the file. I've got my USB, sorry, my Wi-Fi dongle plugged in. It came with it, so I'm not sure which one you need and there's a There's an LED on there and it's

**Dave Jones:** flashing and it's supposed to after 30 seconds or so. So, we're going to have to wait. Uh it should eventually be green and flash red. And I can kind of see up, there it is. Dut dut. Dut dut. It's like a heartbeat.

**Dave Jones:** I think we have a winner. So, here we go. Step number three, connect to your Red Pitaya and make sure it's connected to the internet. How can I make sure? I don't know. That's another fact thing which I don't want to read yet unless

**Dave Jones:** something goes horribly Oh, no. Look. No. No, I don't want to do command pings. No, bugger that. I just want to input my MAC address and go. Let's start. Ah. Got to create an account. Thumbs down. I guess that one could be

**Dave Jones:** useful cuz then you can access it from anywhere and I don't know. Anyway. And bingo, we're in like Flynn. Check it out. I just registered. It didn't have to make me verify my email, so beauty. It just took me straight in.

**Dave Jones:** Said, "Thank you for registering." And I put in the MAC address and the EV login. There it is. There's my LAN IP address that I can go go directly to it. Presumably, unlocked applications oscilloscope plus signal generator and

**Dave Jones:** spectrum analyzer visual programming license. I don't have a license for this visual programming thing. I don't want to You won't see me do that in this video. I'm not really interested in that. I just want to use it as a you

**Dave Jones:** know, spectrum analyzer, oscilloscope, everything else. So, yeah. We're in like Flynn. Unlock apps. Can we have a look at unlock? I don't know. Unlock code. Got no idea. It should just connect to the browser. Remember, this is Wi-Fi.

**Dave Jones:** Um So, I'm not connected to the ethernet at all. There it is. And that's my telephone. Well, what what what what? That didn't work. Not directly to the IP address anyway. So, anyway, let's just hit start. No. It doesn't like it.

**Dave Jones:** What? Fail. Geez, this like a Wi-Fi like access. I mean, it can see it. Oh, it Right, it can see it. Tells me my LAN IP address, everything. Like if I have to go in and I need create gateways or some other crap. I

**Dave Jones:** don't know. I'm not some network penguin guru. Um Yeah, no, it just doesn't work. Uh, fail. See? Stuff like this just really you know, it leaves a bad taste in your mouth. Doesn't inspire confidence at all. It might have just worked if I

**Dave Jones:** plugged into the ethernet. I'll try that. So, there we have it. Got my ethernet plugged in. We've got that red heartbeat double flashy thing. So, yep. I'll go through the process yet again. And it wouldn't let me add a second

**Dave Jones:** device because the MAC address already existed. And I just clicked on the IP address here. Presumably do the same thing if you do start. Yes, it is. Start button is the same as that. And tada! We're in like Flynn. So, sorry. I have

**Dave Jones:** no idea what happened to the Wi-Fi thing. Some DHCP thing or something maybe. I don't know. Everyone who knows all about networking is probably screaming at me and they're all that's obvious. But hey, you know, it didn't work for me. So, what am I supposed to

**Dave Jones:** say, right? Didn't work out you know, didn't work off the bat. So, not impressed at all with uh that Wi-Fi setup. So, anyway, works with the ethernet. So, beauty. Um visual programming um which I yeah, I don't want to do that in this

**Dave Jones:** oscilloscope pro and spectrum analyzer pro. And we can get more applications. We can either do a demo or we can run it um like run the real application on the real hardware here. So, here's more this Tesla meter. Two channel time domain

**Dave Jones:** signal visualization system. Um cool. Oh, PID controller and a oscilloscope. Look at this. Okay, frequency response analyzer. Very very nice. AKA well, it's a bode analyzer. Well, you know, frequency response sort of bode bode plot. Um and impedance um analyzer

**Dave Jones:** requires a shunt resistor. There you go. It's even got a link to a guide available for that country. Okay, so these are the official Red Pitaya apps. And then we've got contributed apps because that's a whole thing about this. It's open source

**Dave Jones:** hardware. You can actually um it's you know, it's all available. You can write your own apps and everything like that. So, these are community uh developed apps. It's got an SDR transmitter. Um fanta- it's SDR transceiver. Sorry, because it's got a

**Dave Jones:** signal generator and a uh oscilloscope {slash} receiver as well. And like it's it's a full 50 MHz up to 50 MHz or so, I believe is the bandwidth um SDR or uh software defined uh radio. So, there you

**Dave Jones:** go. Good on your Pavel Demin. Um and LTIDSP workbench. Ooh, that's interesting. Um it's another spectrum analyzer SDR transceiver, another uh SDR app. Um yeah, I think this thing could be, you know, a fairly big and uh useful

**Dave Jones:** uh device for the SDR community at least up to uh 50 MHz or so, you know, if you're up to the you know, the real um the high frequency stuff, then it's no good, obviously, but uh anything below

**Dave Jones:** 50 meg, it's probably going to do the business and do it really well. Uh at least it has the hardware to do it. So, it all comes down to the apps. Calibrate upgraded with DC offset calibration. Ooh, you can calibrate your thing.

**Dave Jones:** Anyway, I'm going to install a bode plotter. Here we go. How it does it work? Spinning around, spinning its little gear wheel there. I assume it um downloads the app to the Red Pitaya. And uh cuz obviously it's got to run on

**Dave Jones:** the hardware um itself cuz it's got to utilize the um the FPGA and uh stuff like that. So, it's got to uh it's got to program things in there. So, yep. Okay, it's installed. I'm going to install them all.

**Dave Jones:** So, I haven't actually used it yet, but I I'll tell you what, I'm liking this um you know, a web-based um app model interface. It It looks like it's it's you know, it's really jazzy doing the business here. So, uh quite impressed by

**Dave Jones:** that. It's their bizarre. So, it's the you know, the apps are available at the bizarre. There you go. So, how do we get back to our IP address? Ta-da! There you go. There's all our apps which we didn't have before.

**Dave Jones:** Awesome. Look at that. So, our impedance analyzer, that's a basically an LCR as it says on the icon there, um, LCR meter and we can, um, obviously we won't see anything here. I need to make up a little jig with a, a

**Dave Jones:** shunt resistor in there cuz it basically measures, um, the voltage, uh, from the generator and then the voltage across the device under test in series with a shunt resistor and from those two voltages you can, uh, calculate, um, the impedance and

**Dave Jones:** everything else. You can calculate capacitance, inductance, resistance, everything else. You can draw, uh, the response and do the whole thing. I've done a video on that if you want to, uh, know how to actually calculate, um, those sort of things way, way back like

**Dave Jones:** episode 30 or something crazy like that. Anyway, so we can go in and this is all web-based interface. I'm liking this. It's quite neat. All right. The oscilloscope pro is, uh, the one that we, uh, is the one that came with it.

**Dave Jones:** I'm not sure why they wouldn't install all the official ones as, um, standard. Um, I guess maybe they don't want to confuse people. They just want to, you know, here's an oscilloscope, here's a spectrum analyzer. Um, that's it. Um, just fair enough and

**Dave Jones:** here's our scope. We're in like Flynn. And one thing to note, this thing actually does get quite warm during operation. I'm not actually doing anything, not sampling, well, I guess I'm running the, uh, scope app, but, uh, yeah, you know, it gets reasonably warm,

**Dave Jones:** not overly hot. So, as you saw, it's got the, uh, heat sink there on the, uh, top of the case which goes down presses against the, uh, Xilinx Zynq uh, processor inside this thing which is a really powerful

**Dave Jones:** beast running Linux high efficiency as well. It's fairly high efficiency, but still it's doing a lot in there. But yeah, so it's getting reasonably warm, but still, you know, in the scheme of things it's drawing like bugger all power for, you

**Dave Jones:** know, a ridiculously powerful instrument like this. That you probably couldn't even dream of getting 5 years ago, by the way. Absolutely amazing. Now, I'm not sure what's going on here. I went in channel on, but I had the channel there

**Dave Jones:** before, and now it's gone. And I was playing around with the output, and here we go. I can select various output waveforms from the generator. And like it's I don't know. I tried tried to type in a higher frequency here, press enter, and

**Dave Jones:** everything my waveform seemed to vanish. So, unshow, it's like stop run. I don't know. Like something's like auto scale, nothing. My waveforms have gone. Not sure what's going on. Hmm.

**Dave Jones:** No, but it's still got Can we drag that? Oh, we can drag the offset. That's nice. All right, but that's, you know, it's exactly what you'd expect. So, let's turn our sig gen on. There we go. Bingo. I've got a uh

**Dave Jones:** I've got an input output cable connected between channel 1 and 2. We're in like Flynn. There we go. What's the green? Oh, the green is the second input channel. We don't really want that. How do we turn off the second channel? See,

**Dave Jones:** like it's stopped updating. What's going on? Like it's worked. It's captured something. Right? But then it it it's just Hey, there we go. Look, it's gone. What the Select my not something is There it is. Something has gone wrong.

**Dave Jones:** Is there a problem with the server? I don't know. What server? I just got a router. I've plugged in box into the router here. And um which is the same router that my uh PC here I'm using is plugged into. So,

**Dave Jones:** you know, it's not like it has to go halfway across the world or anything. I I got no idea what the photons going on. And uh we're at 1 V per division at the moment. I don't like this control

**Dave Jones:** over here which adjust your thing. I'd rather have like a separate knob or buttons for each channel and stuff like that. So, anyway, if we increase that, look, 500 mV per division, okay? So, we're going down, so that's all

**Dave Jones:** hunky-dory, but it froze last time I did this. It actually froze. So, we can change our time base, too, 2 ms per division. There we go. What are we picking up there? That's interesting. Because that's our channel one and that

**Dave Jones:** is That's fascinating, actually, because I've just connected, as you saw, the output of the sig gen to the input of this, and it's um the sig gen is turned off. So, yeah. Quite strange. Anyway, we can turn our

**Dave Jones:** sig gen on. There it is. Hey. Got some alias in there. Doesn't like that. Um it seems to be more stable now. It seems to be doing the business. So, I don't know. Um it's fairly It's fairly responsive. There's a little

**Dave Jones:** slight delay when I click that button, but not much. It's It's pretty good. And the uh the waveform quality is is brilliant, as you'd expect with a 14-bit converter. It just It looks like it's doing the business. Now, here we go.

**Dave Jones:** Here's a worry. I'm going to select channel one, and I'm going to go auto scale.

**Dave Jones:** It works. Yes. Beauty. Um channel two, we uh can turn off channel two. Yeah, like there's plenty of room on the screen here to have all these settings, right? All all of these settings here all on the screen and all

**Dave Jones:** the controls. Why I've got to actually select number two and then go into a a setup icon thing. It's no, dumb. No, that's just poor user interface design. Sorry. Anyway, look, it's frozen again. Something like this. Someone with

**Dave Jones:** network experience to go, "Oh, yeah, I'll just go in and use my penguin skills and go into the command line and, you know, um try and figure out what's going on here, but I've got, see, no idea. Dummy user like

**Dave Jones:** me, it just freezes on me. You know? What am I supposed to think, right? It's not a good impression at all. Anyway, here we go. We're generating a 10 MHz sine wave now with the SigGen here. And as you can see, our sampled waveform in

**Dave Jones:** yellow there is well, not that great because this is Well, it's 125 megasamples per second. So, we're getting our 10 samples per division, but there's no um sine presumably no sine doesn't look like any sine x on x

**Dave Jones:** interpolation here. It's just got linear interpolation. So, and there's jitter. The you know, we're getting uh uh so, our trigger is currently set to channel one input. Yeah, I mean, we could probably um external input. Actually, where is the external input on

**Dave Jones:** this? It might be on one of the internal expansion headers or uh something like that. I did not show you this cuz I had my uh position thing um this is the thing I was talking about before for the uh our

**Dave Jones:** vertical and horizontal control down here. Oh, down here. Um yeah, I don't like the control. As I said, like all this wasted space around here. Look on the left-hand side, on the right-hand side, and we've got this dinky little,

**Dave Jones:** you know, gear setup icon thing. No. No. Just no. Fail. No. There's plenty of room in here to put everything you need. So, I think they really need to um update the uh uh user interface with that thing. Anyway,

**Dave Jones:** um settings can do calibration. I haven't tried that. Anyway, that's kind of what I would expect. Um of course, we're seeing that single sample uh jitter there. So, you know, I don't think we have any other options in

**Dave Jones:** there to actually uh display to change our uh interpolation, do averaging, or nothing or anything like that. So, it's a very basic um oscilloscope. Now, here's the thing actually. Uh the Red Pitaya is supposed to be open source. They're, you

**Dave Jones:** know, promoting open source, blah blah blah, open source software. Yeah, but not open source hardware, by the looks of things. And I actually I couldn't find any schematic on their uh web page at all. And when I um actually Googled

**Dave Jones:** it, the first hit was actually the uh Red Pitaya schematic. It was actually the EEVblog forum. And somebody um London Dock is very disappointed in the refusal to release full electrical schematics for the supposedly open source project. My guess is they want to

**Dave Jones:** keep imitators from generating similar products. I Yeah. Um yeah, fail. So, yes, if that's genuinely the case, that is a big thumbs down for not releasing the schematic. I presume that they've got all of the source code for the ARM processor plus

**Dave Jones:** the FPGA and stuff like that, cuz you can actually do FPGA development on this thing. Not only is it designed as a general-purpose oscilloscope, it's designed as a coding tool and things like that. Um but it's also designed for

**Dave Jones:** FPGA development, cuz it has that Xilinx uh Zynq FPGA in it. And you can do that. They actually ask you uh when you register, what do you want to use it for? Do you want to use it for, you

**Dave Jones:** know, as an oscilloscope? Do you want to use it for FPGA development or whatever? So, um yeah, presumably they've got that. I don't know. I haven't looked into the source code and uh everything else. But yeah, you can do remote

**Dave Jones:** control using uh MATLAB, Python, LabVIEW, SciLab. It's got, you know, if you really want to get down to the nitty-gritty of integrating this uh integrating a uh scope or a DAC, that's effectively what this is. It's a data acquisition

**Dave Jones:** um you know, module. Then uh yeah, this is, you know, it's this thing could be the duck's guts uh for doing that. If you, you know, if it suits all your hardware um hardware specs. It's got uh dual uh

**Dave Jones:** converters in it. Uh synchronous sampling, that's how they can do the uh LCR module, the impedance analyzer module. They actually sample them at the same time, otherwise you got issues. So, um it's got dual sampler in there. It's

**Dave Jones:** got a a secondary uh sampler on the IO uh headers internally on the thing. Uh 100k samples per second at 12-bit, so that's not too shabby. You can do some useful uh stuff with that as well. And they're trying to compare

**Dave Jones:** it to the Raspberry Pi and the Arduino Uno. Not really the same thing. But as I said, they're trying to uh sell this thing as like a programming platform, hence all the visual programming stuff that they're actually uh talking about

**Dave Jones:** here. Make your own web-based apps and all sorts of weird and wonderful things. But anyway, visual programming. There it is. Buy now. Do I have to buy the visual programming interface? Um that's a bit disappointing, but I guess they've got to make their money

**Dave Jones:** somehow. Um although they I'm not sure how much they're making on this uh board. I haven't done a bomb costing. Um but it's not a uh cheap board by any stretch of the imagination. Oh, they've got an LCR

**Dave Jones:** meter extension board. Ah, I wish they would have sent me one of those. I'm going to have to, uh, build for 300 bucks? No, sorry, 300 euros? Wow, will be available in 30 days. It's on back order. 300 euros? What's on it?

**Dave Jones:** It's just got a pic. That looks like a That looks like a pic with some shunt resistors and some relays. They look like little Pickering relays. Um, if they are, very nice. I'm a bit of a Pickering relay fanboy. Um, I like the

**Dave Jones:** fact that they're red. I've never seen them in red before. Wow, they're little, um, compact, uh, single in-line ones. They're probably magnetically shielded as well. You can get magnetically shielded options in the Pickering relays. Anyway, very nice relays. Have

**Dave Jones:** extensive experience with those. Um, jeez, 300 euros for an LCR meter board? Wow. Jeez, that's pretty rich. Anyway, while we're here, let's take a look at, uh, some other stuff. The aluminum case, which I've got, which I highly recommend it. Yeah, it's that's

**Dave Jones:** available for 39 euros. That's an optional extra cuz normally it's just a, uh, bare board. Clear acrylic, uh, case. That's a cheaper one. I don't know. I like the, uh, Is that a Oh, no, that's just a vent hole. Oh, a fan. Okay, it

**Dave Jones:** looks like you can screw a fan on the top of this thing. Um, nah, the aluminum If you're going to spend spend the extra 10 bucks and get the aluminum case. So, the Red Potato board itself, by the way,

**Dave Jones:** is 199, uh, euros or Yankee bucks, 238 Yankee bucks. Um, you know, it might sound expensive for just a board, but the Zynq Zynq processor in it is not cheap. I think if you go cost that one off, it's

**Dave Jones:** probably like 100 bucks for the chip or something. I'm not Don't quote me on that, but, you know, it it's not a cheap, uh, chip. Now, you get a lot of bang for buck in this thing. I It's

**Dave Jones:** Yeah, I think I think it's it's worth the money. It is worth the money. I like the app concept and things like that. It's shame it's not fully open source so or it doesn't appear to be. That's a real bummer, but

**Dave Jones:** yeah, I mean you can develop all your own apps so all the SDK and everything the programming all the source code and everything is available, but why not give us the hardware? Geez. And they won't allow the six US dollars for the

**Dave Jones:** visual programming system. Oh, free and you can get a free trial for 7 days play with it. Not sure why they bother selling it at you know at 5 euros a pop for why it's not included, but I can understand it's

**Dave Jones:** probably a lot of effort to develop a visual programming interface and it kind of looks all jazzy and but yeah, I don't know. I might have to save that for a separate thing, but if you're really into programming and getting apps up and

**Dave Jones:** running real quickly. The problem with these visual programming interfaces is that they're non-standard. So, you know, yeah, here it is like do repeat loops. Here we go and you know, put command rotary LED so you can do various

**Dave Jones:** things, you know, really easy for getting apps up and running real quick, but ultimately useless like skill to learn if you want to you know, actually program something else. So, but allows you to you know, it's kind of like National Instruments

**Dave Jones:** LabVIEW for example, you know, really incredibly powerful programming visual programming environment, but it's a skill if you learn that that's it like it doesn't translate to any other product at all. It's why I like you know, bench oscilloscope plug it in turn it on

**Dave Jones:** works, you know, but granted this is not a replacement. I keep saying this USB oscilloscopes are not replacements for bench oscilloscopes. They have their niche uses. In this case, it's not really just a USB scope. If you just

**Dave Jones:** want a USB scope, go buy just a USB scope. You probably wouldn't just buy this. It's more useful as you know, when you want to do, you know, really clever stuff with it. You want to automate something. You want to

**Dave Jones:** design, you know, an automated web, you know, interface that'll, you know, tweet when you signal goes out, you know, when you get a signal or something like that or do whatever, you know, you can interface digital stuff to this. You can do all

**Dave Jones:** sorts of things, program it. Fantastic. You want to use it as a software learning tool, an FPGA learning tool, that's what it's good for. If you're just using it as a USB scope, obviously, you've seen it, right? You've seen the

**Dave Jones:** interface. It's no good. It is like that's a hopeless USB oscilloscope. It works, but, you know, it doesn't offer you any, you know, bells and whistles at all. Okay, if we go in here and run another app, the frequency response

**Dave Jones:** analyzer, they all these apps are pretty basic. I've got to admit. I'm not terribly um not terribly impressed with them. Here we go. Now, um this one I haven't actually plugged the thing in. So, let's actually plug it in. This is showing the response

**Dave Jones:** over the full range. So, if I plug that in, there we go. That's pretty horrible, which is what why we have to calibrate the thing. Um let's turn channel two off. There's channel one. Look at that. Wow. Why it's

**Dave Jones:** that horrible it's it's by default it's going from 0 to 60 MHz. It'll be sweeping over that um range and we can calibrate. So, if we hit the calibrate button, yeah, okay. It's reasonably flat, but look. Uh-uh. It's all over the shop. What the

**Dave Jones:** What the photon? Look at this. You see it rolling off there at the end, but what like this is like gain. Like, you know, a couple of dB here. Like, it's horrible. What's going on? I don't get it.

**Dave Jones:** How can it be that bad? Yeah, so that's a real dinky app. I mean, all you can do error while sending data E3. What the restart? What the Like, come on. What Wow, this thing is flaky. Is it just me

**Dave Jones:** or is anyone else having issues? I mean, like wow, why this needs to be why it's out by that much over the over the frequency range. I've got no idea. Anyway, it's it really is quite dinky. I mean, you can zoom in on parts

**Dave Jones:** like that. Okay, that's fairly good, but that's basically all you can you know, that's basically all you can do. You can reset the zoom. Oh, no. How do you reset the frequency? We can scroll with the frequency, but like it's a real

**Dave Jones:** like really basic app. No, applica- application not loaded. What the What is wrong with this thing? Anyway, if we go back, wow, it's not like I'm over Wi-Fi with some dodgy connection or something. I'm connecting directly with Ethernet with

**Dave Jones:** this thing. Anyway, go into the bode plotter app and um This is very spartan as well. I I had a quick play with this before and it's like range settings. Um measurement settings. Look, amplitude like if I want to go point you know, if

**Dave Jones:** I want that like 10 mV amplitude, if I want to get a you know, generate that. Like, what the like like what? Start measurement. Blah blah blah, measuring measuring measuring. And like it's just a real dinky app. Don't like it. And here's the other uh,

**Dave Jones:** oscilloscope app instead of the oscilloscope pro. Um, this one can do averaging. Look at that. Uh, no wackers. Um, but yeah, like no, the user interface just no. No. No. Don't like it at all. Why should I have to scroll that list?

**Dave Jones:** Why can't it make use of, once again, user interface make use of all the screen, just have the links there. Like, you know, why it even has to be fancy like this. Why this can't be like a text

**Dave Jones:** link or something, you know, like a basic HTML page or something. Why it has to be all fancy pantsy like this. Um, I don't know. Whatever. Spectrum analyzer, there we go. We haven't had a look at the spectrum analyzer yet.

**Dave Jones:** Let's go in have a squeeze. That's really quick updating there. Um, how do we set all of our How, where are our settings? Frequency, we can have our frequency range, but like where is our number of bi- you

**Dave Jones:** know, where can we set the number of bins? Where can we set the window in? Where can we set I I see auto scale. I see reset zoom. I see an incredibly basic app. Wow. Wow. No. No. No, that doesn't cut the way. No. How do

**Dave Jones:** you set that up? You can probably zoom in. Okay. Whoop-dee-doo. No, where's all the settings?

**Dave Jones:** What do you want me to say about that, really? I mean, yeah. No, generator and oscilloscope. That's the thing I wanted to test, like how can you set the generator running, for example, in the background and then go use your

**Dave Jones:** oscilloscope app, uh, for example. Is that possible? Or do you need an app like this one which has generator and oscilloscope built in? Now, this looks like the oscilloscope app we had before, but it's got the extra signal generator

**Dave Jones:** down below. So, there you go. We can uh looks like in file you can upload files. So, arbitrary wave wave gen, but yeah, this is not No, the apps are not impressive. The hardware I really like this sort of the

**Dave Jones:** way that they've done it with the web base thing and the apps and everything. I do like it, but the apps leave so much to be desired. Let's hit the auto button. Hey, there we go. Popped up. That's our gen. That's a

**Dave Jones:** dinky toy interface, that is. There we go. I can use the mouse wheel. That's pretty good. No, I'm not impressed with these apps. Not impressed at all. Sorry, Red Pitaya. No, more work required. And of course, one of the things I really wanted to do

**Dave Jones:** with this thing is get a bode plot of my micro current like I did with the analog discovery before with great ease, but like this bode analyzer here, it's just like Look, it's not even Look, uh starting frequency

**Dave Jones:** 1 kHz. There it is, but the actual graph here starts at like 0 Hz. There's 1 Hz, 10 Hz, 100 Hz. What? Like it's just Ah, it's just ridiculous. And why is this like the amplitude? I want to set

**Dave Jones:** 10 mV because micro current has a gain of 100. I can do this easily on the analog discovery. It works a treat. This thing's just hopeless. Start measurement. Like it should go do do sample or sample sample. It should draw your bode plot like that

**Dave Jones:** as it sweeps the frequency. But no, I mean I've set it to start at 1 kHz. Yet what is it starting at zero? 1 Hz? What? This thing doesn't work at all. It's useless. There you go. It's just sitting there

**Dave Jones:** locking up. Surely I can't be the only one having issues with this thing. Oops, silly me. With the spectrum analyzer before, I was not in the spectrum analyzer pro. I was in just in the regular spectrum analyzer. So, that's

**Dave Jones:** it. Um but once again, look, right, it's not generating a signal. Like I had used the the generator app before to actually generate a signal and now it's gone. Like you change the app and it like I don't know, reconfigures the FPGA

**Dave Jones:** hardware in there and it's it's gone. Like unless you specifically I guess specifically right now which has both functionalities built in and I don't I don't like that at all. Um but once again, this is supposed to be the pro

**Dave Jones:** spectrum analyzer. Okay? Where where are all the settings? Where's your number of FFT bins? Where's like where is it? Where is it? There's nothing there. It's bare-bones. It's performance is actually probably going to be quite reasonable with the 14

**Dave Jones:** 125 megasamples per second 14-bit converter. Um I have no doubt that it would be reasonable, but the app this is the pro app. Right? This is the pro app. Where are the settings? Nothing. So much for pro. That's just

**Dave Jones:** nah that doesn't cut it. I'm sorry. It's you've got to have impressive uh default apps for something like this for people to use. I know it's more of a you know, it's probably you know more of a programming learning type tool

**Dave Jones:** than it is, you know, like a real off-the-shelf useful tool. Um like out out of the box experience. A better out of the box experience by far is the um analog discovery uh one which I've done a video on and people have uh asked

**Dave Jones:** about uh before. And then that can the out of the box experience of that one completely uh blows this one away. Um But this but the Red Pitaya is inherently more powerful in terms of stuff it can do and things like that.

**Dave Jones:** Not that impressive. Sorry, Red Pitaya. It has great potential. I think it's really good if you want to go to the effort to write the app and things like that. I think it could be a incredibly powerful tool and a big

**Dave Jones:** winner um for you. And I like the app interface and I like the way that they've done it, the quick start thing. It all seemed to work apart from the Wi-Fi thing. Very disappointing. I don't know why it's

**Dave Jones:** locking up, but it seems to be working now. And issues with it, but the apps just don't cut the mustard as an off-the-shelf tool. Sorry. Um Nope. Not hugely So, impressed with some things, not hugely impressed with others. So, you're going to have to

**Dave Jones:** weigh up whether or not it's the tool for you. If you want an out-of-the-box experience with you know, a good USB scope and spectrum analyzer and everything like that, uh the Red Pitaya is probably not for you. I'd recommend if you want

**Dave Jones:** out-of-the-box, I would go for the Analog Discovery, which is a similar price. I think it might be a little bit cheaper, but it's not as powerful as um this. I think the specs of the Red Pitaya are superior. So,

**Dave Jones:** there you go. That's a quick look. I will no doubt play with it some more. I want to do the LCR meter functionality, which I um didn't uh get to look at. Where was it? Impedance analyzer. I didn't uh

**Dave Jones:** Yeah, plot settings. I'm going to have to build up a little um It's not hard. Just a 50-ohm resistor in series with a device under test, things like that. Um but I'll try and do that as a separate

**Dave Jones:** uh video cuz that could be quite useful. I want to you know, get um impedance responses of various components, you know, capacitors for bypass applications, inductors, things like that. Um so, that could be uh quite useful as for, you know, network

**Dave Jones:** analyzer stuff. So, I'll have to do a separate video on that one. But, there you have it. That's the Red Pitaya. Just kind of sort of working for me. Um yeah, might have to get on the forum. Anyway,

**Dave Jones:** hope you like that uh first look, I guess first impressions, cuz this is just me first playing around with this thing. Um and I think it has potential, but uh yeah, it needs a bit of work. Catch you next time.
