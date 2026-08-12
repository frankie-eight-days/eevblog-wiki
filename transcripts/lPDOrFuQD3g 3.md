---
video_id: lPDOrFuQD3g
title: EEVblog #858 - Red Pitaya
url: https://www.youtube.com/watch?v=lPDOrFuQD3g
source: youtube-asr
timestamps: {"0": 1, "1": 16, "2": 61, "3": 99, "4": 130, "5": 168, "6": 195, "7": 224, "8": 256, "9": 288, "10": 318, "11": 339, "12": 363, "13": 378, "14": 396, "15": 410, "16": 436, "17": 464, "18": 493, "19": 526, "20": 560, "21": 581, "22": 595, "23": 625, "24": 644, "25": 679, "26": 700, "27": 715, "28": 744, "29": 767, "30": 788, "31": 822, "32": 855, "33": 871, "34": 889, "35": 904, "36": 932, "37": 966, "38": 984, "39": 1002, "40": 1030, "41": 1059, "42": 1081, "43": 1101, "44": 1120, "45": 1140, "46": 1164, "47": 1188, "48": 1214, "49": 1245, "50": 1253, "51": 1288, "52": 1305, "53": 1338, "54": 1369, "55": 1406, "56": 1442, "57": 1463, "58": 1498, "59": 1507, "60": 1528, "61": 1563, "62": 1592, "63": 1608, "64": 1621, "65": 1648, "66": 1683, "67": 1711, "68": 1733, "69": 1763, "70": 1791, "71": 1822, "72": 1854, "73": 1871, "74": 1902, "75": 1938, "76": 1964, "77": 2001, "78": 2024, "79": 2056, "80": 2078, "81": 2104, "82": 2130, "83": 2151, "84": 2191, "85": 2205, "86": 2226, "87": 2255, "88": 2275, "89": 2290, "90": 2324, "91": 2339, "92": 2370, "93": 2408, "94": 2428, "95": 2454, "96": 2485, "97": 2508, "98": 2525, "99": 2544, "100": 2566}
---

**Dave Jones:** Hi, we're going to take a look at the Red Pitaya, a roughly $240 not quite a USB oscilloscope. It's more of like a high-performance data acquisition system. Thank you very much for Red Pitaya for sending this one in.

**Dave Jones:** I actually got this in the mailbag a little while back along with an Analog Discovery. And I thought I'd do a video actually comparing the two, but I've already done like a fairly in-depth video on the Analog Discovery board and it's very similar to the Red Pitaya. So, I thought we'd just have a play around with the Red Pit sexy indeed. And we've got a bunch of high-end hardware in here and we'll take a close look, but of course the main grunt in this thing is provided by a

**Dave Jones:** Xilinx Zynq. This is a This is the 7010 system on chip series and the Zynq processor/FPGAs cuz that's what they are. They're fairly unique in that they have not only a ARM Cortex A9 in there plus Xilinx Artix FPGA fabric as well. Incredibly powerful beast. These are not cheap devices and this is actually running embedded Linux on this thing. I'm not sure what particular flavor. But we've got 4 gigabit of DDR3 DRAM here. Basically, we've got 1 gig Ethernet over here. We've got a micro SD

**Dave Jones:** card. We've got USB and we've got two USB connectors on the bottom as well. One's for power and one's for serial command type interface. And we've got a bunch of LEDs along here. There's a JTAG port and we've got a bunch of user IO as as which if you use the aluminum case, unfortunately, you can't access, but there's like another clear case version where you can access these. And there's an additional uh 12-bit, I think, 100 uh K sample per second multi-channel ADC in here and various IO. So, you can control

**Dave Jones:** everything. And this is basically not just a USB oscilloscope. It's much, much more than that, just like the Analog uh Discovery one. It is uh basically a complete uh DAC, a DAQ, a data acquisition system, basically, with dual channel uh 14-bit 125 meg sample uh per second converters, uh dual data 14-bit DACs as well, and a whole bunch of IO, and running embedded Linux, Ethernet. You can basically, yes, you could use it as an Internet of Things in {quote} marks uh device. And it's basically a uh programming system, kind

**Dave Jones:** of like the you know, like the Raspberry Pi kind of thing. It's got a visual programming environment, which we won't really take a look at in this thing, but it's got uh you can do FPGA development on it inside the uh Xilinx Zynq. And you can just use it as a uh generic USB oscilloscope if you want. You can use it as a frequency um spectrum analyzer. You can use it as a network analyzer. You can use it as a software-defined radio, cuz it's got a

**Dave Jones:** like a 50 MHz analog uh bandwidth, so anything up to 15 MHz at 14-bit uh conversion. Yeah, it's going to make a decent uh software-defined radio. Uh it's web-based interface, so either uh it can't might My one actually came with a Wi-Fi dongle on it, or you can use the uh Ethernet. You can uh program and operate this thing remotely from anywhere in the world. You can script it. You can do all sorts of things. And apparently, it's open source, at least open source software. It's the uh 7010

**Dave Jones:** series uh system on chip. This is not a cheap part at all, um especially in one-off uh quantity. Here's our um analog inputs here. So, here's our ADC. It's an LTC uh 2145. This is not a cheap part. It's almost the same price as the uh Xilinx Zynq. It's like 50 bucks. Um and one-off uh you know, Digikey type uh price for that puppy. And the performance is absolutely stellar. I'll link in the data sheet down below if you want to check it out. So, that's a dual channel

**Dave Jones:** uh 14-bit 125 megasamples per second. Uh the DAC here, um here's the two DAC outputs. Also 125 megasamples per second, 14 bits as well. That's about half the cost. That's about 25 bucks. So, if you're wondering why this thing is so expensive, well, there's a fair bit of expensive chips in it. And unless you manufacture a thousand of these or 10,000, you know, it's going to cost a bit. And for those who want to see the bottom, there we go. Peekaboo. We've got all our bypassing on the bottom of the

**Dave Jones:** Zynq there. Tiny. They're little 0402 jobbies by the looks of it. Absolutely tiny. We've got some uh line termination uh stuff here and a few miscellaneous things. There's our USB. We've got some protection on the USB uh power input there. Looks like we've got a uh a poly switch. And it looks like we've got a programmable attenuator on the front end here. And we've got uh two well, SATA well, they look like SATA connectors and they are SATA connectors, but they're not designed for SATA. These

**Dave Jones:** are synchronization connectors and I haven't looked into the details, but presumably you can sync up the acquisition for big um between boards for like daisy chain them for big uh multi-channel stuff, but that's just a guess. I haven't even looked. So, that's the Red Pitaya hardware. And yes, it is red solder mask. I love it. Beautiful.

**Dave Jones:** One of my favorite solder mask colors, red. Makes it go faster. Hmm. Anyway, let's take a look at the software. See if we can get this puppy up and running. See if we have any grief or whether it's just going to work like a treat out of the box.

**Dave Jones:** All right, let's see if we can make this red Pitaya do something useful. Now, I've come to the website here. This is my first time using the thing. I don't have any instructions, didn't come with it, at least my one didn't. Anyway, it's just the brick itself and the website.

**Dave Jones:** So, let's take a look. Now, I have actually had a look at the website and it actually confused me for some time exactly what's going on here. I mean, you you play the video here and it tells you all about this visual programming.

**Dave Jones:** You know, visual programming system and things like that. So, you know, like I don't want to program this thing. I just want to use it as an scope, you know, as a network analyzer. Get a bode plot or something like that.

**Dave Jones:** So, how do you do that? Well, like you know, I couldn't immediately like we can browse some apps here and we can do some other stuff and application marketplace and it has all this, you know, weird and wonderful stuff, but I it actually took me a little bit maybe cuz I'm a bit dumb. You go up to the start here and you can go to the quick start. So, this is actually a nice step-by-step process. It's look, step number one, prepare the SD card. Mine already came with an SD card, so I

**Dave Jones:** presume that they are pre-loaded and everything for me. I don't know if the one that you will buy will actually come with a pre-loaded SD card or not, but look you can download the image. It's got instructions for Windows and for Linux and everything else. So, you know, you just download it and it creates a bootable disk image that contains Linux and everything else. Fantastic. And how would you like to connect? The cable connection or wireless connection or direct wireless connection. Um I'm going to go

**Dave Jones:** for broke here and I'm going to go for the wireless. I'm going to plug the Wi-Fi dongle I got in here. And here it is, enter your wireless information and download the configuration file. Now it doesn't tell me, like I presume wireless network information, I'm presuming that's the name of my wireless network and that's the password. So, I'm going to give that a go and it then I it generates a file and you can download, you put it on the SD card and presumably Bob's your uncle and it should blink at

**Dave Jones:** you when we're done. Let's give it a go. All right, so I downloaded and copied my file. There are two USB connectors on here. You have to plug it into the power one, not the con size in, that's console like a serial console type thing. So, I've copied the file. I've got my USB, sorry, my Wi-Fi dongle plugged in. It came with it, so I'm not sure which one you need and there's a There's an LED on there and it's flashing and it's supposed to after 30

**Dave Jones:** seconds or so. So, we're going to have to wait. Uh it should eventually be green and flash red. And I can kind of see up, there it is. Dut dut. Dut dut. It's like a heartbeat. I think we have a winner. So, here we go. Step number three, connect to your Red Pitaya and make sure it's connected to the internet. How can I make sure? I don't know. That's another fact thing which I don't want to read yet unless something goes horribly Oh, no. Look.

**Dave Jones:** No. No, I don't want to do command pings. No, bugger that. I just want to input my MAC address and go. Let's start. Ah. Got to create an account. Thumbs down. I guess that one could be useful cuz then you can access it from anywhere and I don't know. Anyway.

**Dave Jones:** And bingo, we're in like Flynn. Check it out. I just registered. It didn't have to make me verify my email, so beauty. It just took me straight in. Said, "Thank you for registering." And I put in the MAC address and the EV login.

**Dave Jones:** There it is. There's my LAN IP address that I can go go directly to it. Presumably, unlocked applications oscilloscope plus signal generator and spectrum analyzer visual programming license. I don't have a license for this visual programming thing. I don't want to You won't see me do that in this video. I'm not really interested in that. I just want to use it as a you know, spectrum analyzer, oscilloscope, everything else. So, yeah. We're in like Flynn. Unlock apps.

**Dave Jones:** Can we have a look at unlock? I don't know. Unlock code. Got no idea. It should just connect to the browser. Remember, this is Wi-Fi. Um So, I'm not connected to the ethernet at all. There it is. And that's my telephone. Well, what what what what? That didn't work.

**Dave Jones:** Not directly to the IP address anyway. So, anyway, let's just hit start. No. It doesn't like it. What? Fail. Geez, this like a Wi-Fi like access. I mean, it can see it. Oh, it Right, it can see it. Tells me my LAN IP address, everything. Like if I have to go in and I need create gateways or some other crap. I don't know. I'm not some network penguin guru. Um Yeah, no, it just doesn't work.

**Dave Jones:** Uh, fail. See? Stuff like this just really you know, it leaves a bad taste in your mouth. Doesn't inspire confidence at all. It might have just worked if I plugged into the ethernet. I'll try that. So, there we have it. Got my ethernet plugged in. We've got that red heartbeat double flashy thing. So, yep.

**Dave Jones:** I'll go through the process yet again. And it wouldn't let me add a second device because the MAC address already existed. And I just clicked on the IP address here. Presumably do the same thing if you do start. Yes, it is. Start button is the same as that. And tada!

**Dave Jones:** We're in like Flynn. So, sorry. I have no idea what happened to the Wi-Fi thing. Some DHCP thing or something maybe. I don't know. Everyone who knows all about networking is probably screaming at me and they're all that's obvious. But hey, you know, it didn't work for me. So, what am I supposed to say, right? Didn't work out you know, didn't work off the bat. So, not impressed at all with uh that Wi-Fi setup. So, anyway, works with the ethernet. So, beauty.

**Dave Jones:** Um visual programming um which I yeah, I don't want to do that in this oscilloscope pro and spectrum analyzer pro. And we can get more applications. We can either do a demo or we can run it um like run the real application on the real hardware here. So, here's more this Tesla meter. Two channel time domain signal visualization system.

**Dave Jones:** Um cool. Oh, PID controller and a oscilloscope. Look at this. Okay, frequency response analyzer. Very very nice. AKA well, it's a bode analyzer. Well, you know, frequency response sort of bode bode plot. Um and impedance um analyzer requires a shunt resistor. There you go.

**Dave Jones:** It's even got a link to a guide available for that country. Okay, so these are the official Red Pitaya apps. And then we've got contributed apps because that's a whole thing about this. It's open source hardware. You can actually um it's you know, it's all available. You can write your own apps and everything like that. So, these are community uh developed apps. It's got an SDR transmitter. Um fanta- it's SDR transceiver. Sorry, because it's got a signal generator and a uh oscilloscope {slash} receiver as well. And like it's

**Dave Jones:** it's a full 50 MHz up to 50 MHz or so, I believe is the bandwidth um SDR or uh software defined uh radio. So, there you go. Good on your Pavel Demin. Um and LTIDSP workbench. Ooh, that's interesting. Um it's another spectrum analyzer SDR transceiver, another uh SDR app. Um yeah, I think this thing could be, you know, a fairly big and uh useful uh device for the SDR community at least up to uh 50 MHz or so, you know, if you're up to the you know, the real um

**Dave Jones:** the high frequency stuff, then it's no good, obviously, but uh anything below 50 meg, it's probably going to do the business and do it really well. Uh at least it has the hardware to do it. So, it all comes down to the apps. Calibrate upgraded with DC offset calibration.

**Dave Jones:** Ooh, you can calibrate your thing. Anyway, I'm going to install a bode plotter. Here we go. How it does it work? Spinning around, spinning its little gear wheel there. I assume it um downloads the app to the Red Pitaya.

**Dave Jones:** And uh cuz obviously it's got to run on the hardware um itself cuz it's got to utilize the um the FPGA and uh stuff like that. So, it's got to uh it's got to program things in there. So, yep. Okay, it's installed.

**Dave Jones:** I'm going to install them all. So, I haven't actually used it yet, but I I'll tell you what, I'm liking this um you know, a web-based um app model interface. It It looks like it's it's you know, it's really jazzy doing the business here. So, uh quite impressed by that. It's their bizarre. So, it's the you know, the apps are available at the bizarre. There you go. So, how do we get back to our IP address?

**Dave Jones:** Ta-da! There you go. There's all our apps which we didn't have before. Awesome. Look at that. So, our impedance analyzer, that's a basically an LCR as it says on the icon there, um, LCR meter and we can, um, obviously we won't see anything here. I need to make up a little jig with a, a shunt resistor in there cuz it basically measures, um, the voltage, uh, from the generator and then the voltage across the device under test in series with a shunt resistor and from those two voltages you can, uh,

**Dave Jones:** calculate, um, the impedance and everything else. You can calculate capacitance, inductance, resistance, everything else. You can draw, uh, the response and do the whole thing. I've done a video on that if you want to, uh, know how to actually calculate, um, those sort of things way, way back like episode 30 or something crazy like that.

**Dave Jones:** Anyway, so we can go in and this is all web-based interface. I'm liking this. It's quite neat. All right. The oscilloscope pro is, uh, the one that we, uh, is the one that came with it. I'm not sure why they wouldn't install all the official ones as, um, standard.

**Dave Jones:** Um, I guess maybe they don't want to confuse people. They just want to, you know, here's an oscilloscope, here's a spectrum analyzer. Um, that's it. Um, just fair enough and here's our scope. We're in like Flynn. And one thing to note, this thing actually does get quite warm during operation. I'm not actually doing anything, not sampling, well, I guess I'm running the, uh, scope app, but, uh, yeah, you know, it gets reasonably warm, not overly hot. So, as you saw, it's got the, uh, heat sink there on the, uh, top

**Dave Jones:** of the case which goes down presses against the, uh, Xilinx Zynq uh, processor inside this thing which is a really powerful beast running Linux high efficiency as well. It's fairly high efficiency, but still it's doing a lot in there. But yeah, so it's getting reasonably warm, but still, you know, in the scheme of things it's drawing like bugger all power for, you know, a ridiculously powerful instrument like this. That you probably couldn't even dream of getting 5 years ago, by the way. Absolutely amazing. Now, I'm

**Dave Jones:** not sure what's going on here. I went in channel on, but I had the channel there before, and now it's gone. And I was playing around with the output, and here we go. I can select various output waveforms from the generator. And like it's I don't know. I tried tried to type in a higher frequency here, press enter, and everything my waveform seemed to vanish.

**Dave Jones:** So, unshow, it's like stop run. I don't know. Like something's like auto scale, nothing. My waveforms have gone. Not sure what's going on. Hmm.

**Dave Jones:** No, but it's still got Can we drag that? Oh, we can drag the offset. That's nice. All right, but that's, you know, it's exactly what you'd expect. So, let's turn our sig gen on. There we go. Bingo. I've got a uh I've got an input output cable connected between channel 1 and 2. We're in like Flynn. There we go. What's the green?

**Dave Jones:** Oh, the green is the second input channel. We don't really want that. How do we turn off the second channel? See, like it's stopped updating. What's going on? Like it's worked. It's captured something. Right? But then it it it's just Hey, there we go. Look, it's gone.

**Dave Jones:** What the Select my not something is There it is. Something has gone wrong. Is there a problem with the server? I don't know. What server? I just got a router. I've plugged in box into the router here. And um which is the same router that my uh PC here I'm using is plugged into. So, you know, it's not like it has to go halfway across the world or anything.

**Dave Jones:** I I got no idea what the photons going on. And uh we're at 1 V per division at the moment. I don't like this control over here which adjust your thing. I'd rather have like a separate knob or buttons for each channel and stuff like that. So, anyway, if we increase that, look, 500 mV per division, okay? So, we're going down, so that's all hunky-dory, but it froze last time I did this.

**Dave Jones:** It actually froze. So, we can change our time base, too, 2 ms per division. There we go. What are we picking up there? That's interesting. Because that's our channel one and that is That's fascinating, actually, because I've just connected, as you saw, the output of the sig gen to the input of this, and it's um the sig gen is turned off.

**Dave Jones:** So, yeah. Quite strange. Anyway, we can turn our sig gen on. There it is. Hey. Got some alias in there. Doesn't like that. Um it seems to be more stable now. It seems to be doing the business. So, I don't know. Um it's fairly It's fairly responsive. There's a little slight delay when I click that button, but not much. It's It's pretty good. And the uh the waveform quality is is brilliant, as you'd expect with a 14-bit converter. It just It looks like it's doing the business. Now, here we go.

**Dave Jones:** Here's a worry. I'm going to select channel one, and I'm going to go auto scale.

**Dave Jones:** It works. Yes. Beauty. Um channel two, we uh can turn off channel two. Yeah, like there's plenty of room on the screen here to have all these settings, right? All all of these settings here all on the screen and all the controls. Why I've got to actually select number two and then go into a a setup icon thing. It's no, dumb. No, that's just poor user interface design. Sorry. Anyway, look, it's frozen again.

**Dave Jones:** Something like this. Someone with network experience to go, "Oh, yeah, I'll just go in and use my penguin skills and go into the command line and, you know, um try and figure out what's going on here, but I've got, see, no idea. Dummy user like me, it just freezes on me.

**Dave Jones:** You know? What am I supposed to think, right? It's not a good impression at all. Anyway, here we go. We're generating a 10 MHz sine wave now with the SigGen here. And as you can see, our sampled waveform in yellow there is well, not that great because this is Well, it's 125 megasamples per second. So, we're getting our 10 samples per division, but there's no um sine presumably no sine doesn't look like any sine x on x interpolation here. It's just got linear interpolation. So, and there's jitter.

**Dave Jones:** The you know, we're getting uh uh so, our trigger is currently set to channel one input. Yeah, I mean, we could probably um external input. Actually, where is the external input on this? It might be on one of the internal expansion headers or uh something like that. I did not show you this cuz I had my uh position thing um this is the thing I was talking about before for the uh our vertical and horizontal control down here. Oh, down here. Um yeah, I don't like the control. As I said, like all

**Dave Jones:** this wasted space around here. Look on the left-hand side, on the right-hand side, and we've got this dinky little, you know, gear setup icon thing. No. No. Just no. Fail. No. There's plenty of room in here to put everything you need. So, I think they really need to um update the uh uh user interface with that thing. Anyway, um settings can do calibration. I haven't tried that. Anyway, that's kind of what I would expect. Um of course, we're seeing that single sample uh jitter there. So, you know, I

**Dave Jones:** don't think we have any other options in there to actually uh display to change our uh interpolation, do averaging, or nothing or anything like that. So, it's a very basic um oscilloscope. Now, here's the thing actually. Uh the Red Pitaya is supposed to be open source. They're, you know, promoting open source, blah blah blah, open source software. Yeah, but not open source hardware, by the looks of things. And I actually I couldn't find any schematic on their uh web page at all. And when I um actually Googled

**Dave Jones:** it, the first hit was actually the uh Red Pitaya schematic. It was actually the EEVblog forum. And somebody um London Dock is very disappointed in the refusal to release full electrical schematics for the supposedly open source project. My guess is they want to keep imitators from generating similar products. I Yeah.

**Dave Jones:** Um yeah, fail. So, yes, if that's genuinely the case, that is a big thumbs down for not releasing the schematic. I presume that they've got all of the source code for the ARM processor plus the FPGA and stuff like that, cuz you can actually do FPGA development on this thing. Not only is it designed as a general-purpose oscilloscope, it's designed as a coding tool and things like that. Um but it's also designed for FPGA development, cuz it has that Xilinx uh Zynq FPGA in it. And you can

**Dave Jones:** do that. They actually ask you uh when you register, what do you want to use it for? Do you want to use it for, you know, as an oscilloscope? Do you want to use it for FPGA development or whatever?

**Dave Jones:** So, um yeah, presumably they've got that. I don't know. I haven't looked into the source code and uh everything else. But yeah, you can do remote control using uh MATLAB, Python, LabVIEW, SciLab. It's got, you know, if you really want to get down to the nitty-gritty of integrating this uh integrating a uh scope or a DAC, that's effectively what this is.

**Dave Jones:** It's a data acquisition um you know, module. Then uh yeah, this is, you know, it's this thing could be the duck's guts uh for doing that. If you, you know, if it suits all your hardware um hardware specs. It's got uh dual uh converters in it. Uh synchronous sampling, that's how they can do the uh LCR module, the impedance analyzer module. They actually sample them at the same time, otherwise you got issues. So, um it's got dual sampler in there. It's got a a secondary uh sampler on the IO

**Dave Jones:** uh headers internally on the thing. Uh 100k samples per second at 12-bit, so that's not too shabby. You can do some useful uh stuff with that as well. And they're trying to compare it to the Raspberry Pi and the Arduino Uno. Not really the same thing. But as I said, they're trying to uh sell this thing as like a programming platform, hence all the visual programming stuff that they're actually uh talking about here. Make your own web-based apps and all sorts of weird and wonderful things.

**Dave Jones:** But anyway, visual programming. There it is. Buy now. Do I have to buy the visual programming interface? Um that's a bit disappointing, but I guess they've got to make their money somehow. Um although they I'm not sure how much they're making on this uh board. I haven't done a bomb costing.

**Dave Jones:** Um but it's not a uh cheap board by any stretch of the imagination. Oh, they've got an LCR meter extension board. Ah, I wish they would have sent me one of those. I'm going to have to, uh, build for 300 bucks?

**Dave Jones:** No, sorry, 300 euros? Wow, will be available in 30 days. It's on back order. 300 euros? What's on it? It's just got a pic. That looks like a That looks like a pic with some shunt resistors and some relays. They look like little Pickering relays. Um, if they are, very nice. I'm a bit of a Pickering relay fanboy. Um, I like the fact that they're red. I've never seen them in red before. Wow, they're little, um, compact, uh, single in-line ones.

**Dave Jones:** They're probably magnetically shielded as well. You can get magnetically shielded options in the Pickering relays. Anyway, very nice relays. Have extensive experience with those. Um, jeez, 300 euros for an LCR meter board? Wow. Jeez, that's pretty rich. Anyway, while we're here, let's take a look at, uh, some other stuff. The aluminum case, which I've got, which I highly recommend it. Yeah, it's that's available for 39 euros. That's an optional extra cuz normally it's just a, uh, bare board. Clear acrylic, uh, case.

**Dave Jones:** That's a cheaper one. I don't know. I like the, uh, Is that a Oh, no, that's just a vent hole. Oh, a fan. Okay, it looks like you can screw a fan on the top of this thing. Um, nah, the aluminum If you're going to spend spend the extra 10 bucks and get the aluminum case. So, the Red Potato board itself, by the way, is 199, uh, euros or Yankee bucks, 238 Yankee bucks. Um, you know, it might sound expensive for just a board, but the Zynq

**Dave Jones:** Zynq processor in it is not cheap. I think if you go cost that one off, it's probably like 100 bucks for the chip or something. I'm not Don't quote me on that, but, you know, it it's not a cheap, uh, chip. Now, you get a lot of bang for buck in this thing. I It's Yeah, I think I think it's it's worth the money. It is worth the money. I like the app concept and things like that.

**Dave Jones:** It's shame it's not fully open source so or it doesn't appear to be. That's a real bummer, but yeah, I mean you can develop all your own apps so all the SDK and everything the programming all the source code and everything is available, but why not give us the hardware? Geez. And they won't allow the six US dollars for the visual programming system. Oh, free and you can get a free trial for 7 days play with it. Not sure why they bother selling it at you know

**Dave Jones:** at 5 euros a pop for why it's not included, but I can understand it's probably a lot of effort to develop a visual programming interface and it kind of looks all jazzy and but yeah, I don't know. I might have to save that for a separate thing, but if you're really into programming and getting apps up and running real quickly. The problem with these visual programming interfaces is that they're non-standard. So, you know, yeah, here it is like do repeat loops. Here we go and you know, put

**Dave Jones:** command rotary LED so you can do various things, you know, really easy for getting apps up and running real quick, but ultimately useless like skill to learn if you want to you know, actually program something else. So, but allows you to you know, it's kind of like National Instruments LabVIEW for example, you know, really incredibly powerful programming visual programming environment, but it's a skill if you learn that that's it like it doesn't translate to any other product at all.

**Dave Jones:** It's why I like you know, bench oscilloscope plug it in turn it on works, you know, but granted this is not a replacement. I keep saying this USB oscilloscopes are not replacements for bench oscilloscopes. They have their niche uses. In this case, it's not really just a USB scope. If you just want a USB scope, go buy just a USB scope. You probably wouldn't just buy this. It's more useful as you know, when you want to do, you know, really clever stuff with it. You want to automate something. You want to

**Dave Jones:** design, you know, an automated web, you know, interface that'll, you know, tweet when you signal goes out, you know, when you get a signal or something like that or do whatever, you know, you can interface digital stuff to this. You can do all sorts of things, program it. Fantastic.

**Dave Jones:** You want to use it as a software learning tool, an FPGA learning tool, that's what it's good for. If you're just using it as a USB scope, obviously, you've seen it, right? You've seen the interface. It's no good. It is like that's a hopeless USB oscilloscope. It works, but, you know, it doesn't offer you any, you know, bells and whistles at all. Okay, if we go in here and run another app, the frequency response analyzer, they all these apps are pretty basic. I've got to admit.

**Dave Jones:** I'm not terribly um not terribly impressed with them. Here we go. Now, um this one I haven't actually plugged the thing in. So, let's actually plug it in. This is showing the response over the full range. So, if I plug that in, there we go. That's pretty horrible, which is what why we have to calibrate the thing. Um let's turn channel two off. There's channel one. Look at that. Wow. Why it's that horrible it's it's by default it's going from 0 to 60 MHz. It'll be

**Dave Jones:** sweeping over that um range and we can calibrate. So, if we hit the calibrate button, yeah, okay. It's reasonably flat, but look. Uh-uh. It's all over the shop. What the What the photon? Look at this. You see it rolling off there at the end, but what like this is like gain. Like, you know, a couple of dB here.

**Dave Jones:** Like, it's horrible. What's going on? I don't get it. How can it be that bad? Yeah, so that's a real dinky app. I mean, all you can do error while sending data E3. What the restart? What the Like, come on. What Wow, this thing is flaky. Is it just me or is anyone else having issues? I mean, like wow, why this needs to be why it's out by that much over the over the frequency range. I've got no idea. Anyway, it's it really is quite dinky. I mean, you can zoom in on parts

**Dave Jones:** like that. Okay, that's fairly good, but that's basically all you can you know, that's basically all you can do. You can reset the zoom. Oh, no. How do you reset the frequency? We can scroll with the frequency, but like it's a real like really basic app. No, applica- application not loaded. What the What is wrong with this thing?

**Dave Jones:** Anyway, if we go back, wow, it's not like I'm over Wi-Fi with some dodgy connection or something. I'm connecting directly with Ethernet with this thing. Anyway, go into the bode plotter app and um This is very spartan as well. I I had a quick play with this before and it's like range settings. Um measurement settings. Look, amplitude like if I want to go point you know, if I want that like 10 mV amplitude, if I want to get a you know, generate that.

**Dave Jones:** Like, what the like like what? Start measurement. Blah blah blah, measuring measuring measuring. And like it's just a real dinky app. Don't like it. And here's the other uh, oscilloscope app instead of the oscilloscope pro. Um, this one can do averaging. Look at that. Uh, no wackers.

**Dave Jones:** Um, but yeah, like no, the user interface just no. No. No. Don't like it at all. Why should I have to scroll that list? Why can't it make use of, once again, user interface make use of all the screen, just have the links there. Like, you know, why it even has to be fancy like this. Why this can't be like a text link or something, you know, like a basic HTML page or something. Why it has to be all fancy pantsy like this.

**Dave Jones:** Um, I don't know. Whatever. Spectrum analyzer, there we go. We haven't had a look at the spectrum analyzer yet. Let's go in have a squeeze. That's really quick updating there. Um, how do we set all of our How, where are our settings? Frequency, we can have our frequency range, but like where is our number of bi- you know, where can we set the number of bins? Where can we set the window in?

**Dave Jones:** Where can we set I I see auto scale. I see reset zoom. I see an incredibly basic app. Wow. Wow. No. No. No, that doesn't cut the way. No. How do you set that up? You can probably zoom in. Okay.

**Dave Jones:** Whoop-dee-doo. No, where's all the settings? What do you want me to say about that, really? I mean, yeah. No, generator and oscilloscope. That's the thing I wanted to test, like how can you set the generator running, for example, in the background and then go use your oscilloscope app, uh, for example. Is that possible? Or do you need an app like this one which has generator and oscilloscope built in? Now, this looks like the oscilloscope app we had before, but it's got the extra signal generator down below. So, there you go. We can

**Dave Jones:** uh looks like in file you can upload files. So, arbitrary wave wave gen, but yeah, this is not No, the apps are not impressive. The hardware I really like this sort of the way that they've done it with the web base thing and the apps and everything.

**Dave Jones:** I do like it, but the apps leave so much to be desired. Let's hit the auto button. Hey, there we go. Popped up. That's our gen. That's a dinky toy interface, that is. There we go. I can use the mouse wheel. That's pretty good. No, I'm not impressed with these apps. Not impressed at all. Sorry, Red Pitaya.

**Dave Jones:** No, more work required. And of course, one of the things I really wanted to do with this thing is get a bode plot of my micro current like I did with the analog discovery before with great ease, but like this bode analyzer here, it's just like Look, it's not even Look, uh starting frequency 1 kHz. There it is, but the actual graph here starts at like 0 Hz. There's 1 Hz, 10 Hz, 100 Hz.

**Dave Jones:** What? Like it's just Ah, it's just ridiculous. And why is this like the amplitude? I want to set 10 mV because micro current has a gain of 100. I can do this easily on the analog discovery. It works a treat. This thing's just hopeless. Start measurement. Like it should go do do sample or sample sample.

**Dave Jones:** It should draw your bode plot like that as it sweeps the frequency. But no, I mean I've set it to start at 1 kHz. Yet what is it starting at zero? 1 Hz? What? This thing doesn't work at all.

**Dave Jones:** It's useless. There you go. It's just sitting there locking up. Surely I can't be the only one having issues with this thing. Oops, silly me. With the spectrum analyzer before, I was not in the spectrum analyzer pro. I was in just in the regular spectrum analyzer. So, that's it. Um but once again, look, right, it's not generating a signal. Like I had used the the generator app before to actually generate a signal and now it's gone. Like you change the app and it like I don't know, reconfigures the FPGA

**Dave Jones:** hardware in there and it's it's gone. Like unless you specifically I guess specifically right now which has both functionalities built in and I don't I don't like that at all. Um but once again, this is supposed to be the pro spectrum analyzer.

**Dave Jones:** Okay? Where where are all the settings? Where's your number of FFT bins? Where's like where is it? Where is it? There's nothing there. It's bare-bones. It's performance is actually probably going to be quite reasonable with the 14 125 megasamples per second 14-bit converter. Um I have no doubt that it would be reasonable, but the app this is the pro app.

**Dave Jones:** Right? This is the pro app. Where are the settings? Nothing. So much for pro. That's just nah that doesn't cut it. I'm sorry. It's you've got to have impressive uh default apps for something like this for people to use. I know it's more of a you know, it's probably you know more of a programming learning type tool than it is, you know, like a real off-the-shelf useful tool. Um like out out of the box experience. A better out of the box experience by far is the um

**Dave Jones:** analog discovery uh one which I've done a video on and people have uh asked about uh before. And then that can the out of the box experience of that one completely uh blows this one away. Um But this but the Red Pitaya is inherently more powerful in terms of stuff it can do and things like that.

**Dave Jones:** Not that impressive. Sorry, Red Pitaya. It has great potential. I think it's really good if you want to go to the effort to write the app and things like that. I think it could be a incredibly powerful tool and a big winner um for you. And I like the app interface and I like the way that they've done it, the quick start thing. It all seemed to work apart from the Wi-Fi thing. Very disappointing. I don't know why it's locking up, but it seems to be working

**Dave Jones:** now. And issues with it, but the apps just don't cut the mustard as an off-the-shelf tool. Sorry. Um Nope. Not hugely So, impressed with some things, not hugely impressed with others. So, you're going to have to weigh up whether or not it's the tool for you. If you want an out-of-the-box experience with you know, a good USB scope and spectrum analyzer and everything like that, uh the Red Pitaya is probably not for you. I'd recommend if you want out-of-the-box, I would go for the Analog Discovery, which is a similar

**Dave Jones:** price. I think it might be a little bit cheaper, but it's not as powerful as um this. I think the specs of the Red Pitaya are superior. So, there you go. That's a quick look. I will no doubt play with it some more. I want to do the LCR meter functionality, which I um didn't uh get to look at. Where was it?

**Dave Jones:** Impedance analyzer. I didn't uh Yeah, plot settings. I'm going to have to build up a little um It's not hard. Just a 50-ohm resistor in series with a device under test, things like that. Um but I'll try and do that as a separate uh video cuz that could be quite useful.

**Dave Jones:** I want to you know, get um impedance responses of various components, you know, capacitors for bypass applications, inductors, things like that. Um so, that could be uh quite useful as for, you know, network analyzer stuff. So, I'll have to do a separate video on that one.

**Dave Jones:** But, there you have it. That's the Red Pitaya. Just kind of sort of working for me. Um yeah, might have to get on the forum. Anyway, hope you like that uh first look, I guess first impressions, cuz this is just me first playing around with this thing. Um and I think it has potential, but uh yeah, it needs a bit of work.

**Dave Jones:** Catch you next time.
