---
video_id: qdgXvFbgjQU
title: EEVblog2 #858 - Red Pitaya Extended Cut
url: https://www.youtube.com/watch?v=qdgXvFbgjQU
source: youtube-asr
---

**Dave Jones:** Hi, we're going to take a look at the Red Pate, a roughly $240 US, not quite a USB oscilloscope. It's more of like a high performance data acquisition uh system. Thank you very much for Red Potato for sending this one

**Dave Jones:** in. I actually got this in the mailbag a little while back um along with an analog uh discovery. And I thought I'd do a video actually comparing the two, but I've already done like a fairly in-depth uh video on the analog uh

**Dave Jones:** discovery uh board. And it's very similar to the red potato. So, I thought we'd just have a play around with the Red Paya uh today and see what we can do with it. See if we can get a bode plot

**Dave Jones:** and uh just um basically set it up and use the thing. And here it is inside the optional um aluminium case. I highly recommend the aluminium case. It is very sexy indeed. And we've got a bunch of high-end hardware in here. And we'll

**Dave Jones:** take a close look. But of course, uh the main grunting this thing is provided by a XYlink Zinc. This is a um this is the 7010 system on chip series and the zinc uh processors/ FPGAAS cuz that's what

**Dave Jones:** they are. They're fairly unique in that they have not only a um ARM Cortex A9 in there, but they have a dual ARM Cortex A9. So, two processors plus um Rex uh XYLink RTX FPGA fabric as well. Incredibly powerful beast. These are not

**Dave Jones:** uh cheap devices. And this is actually running uh embedded Linux on this thing. I'm not sure what uh particular flavor, but we've got 4 GB of DDR3 uh DRAM here. Basically, um we've got 1 gig uh Ethernet over here. We've got a micro SD

**Dave Jones:** card. We've got USB and we've got uh two USB connectors on the bottom as well. One's for power and one's for serial uh command type interface. And we've got a bunch of leads along here. Uh there's a JAG port. And we've got a bunch of um

**Dave Jones:** user IO as well, which if you use the aluminium case, unfortunately, you can't access, but there's like another clear case version where you can access these. And there's an additional uh 12bit I think 100 uh K sample per second multi-

**Dave Jones:** channelannel ADC in here and various IO so you can control everything. And this is basically not just a USB oscilloscope. It's much much more than that. Just like the analog uh discovery one, it is uh basically a complete DAC a

**Dave Jones:** DAQ or data acquisition system basically with dual channel uh 14bit 125 meg sample uh per second converters uh dual d 14bit DAX as well and a whole bunch of IO and running embedded Linux Ethernet. You can basically, yes, you could use it

**Dave Jones:** as an internet of things in quote marks uh device and it's basically a uh programming system kind of like, you know, like the Raspberry Pi kind of thing. It's got a visual programming environment, which we won't really take

**Dave Jones:** a look at in this thing, but it's got uh you can do FPGA development on it inside the XYlink Zinc. And you can just use it as a uh generic USB oscilloscope if you want. You can use it as a frequency um

**Dave Jones:** spectrum analyzer. You can use it as a network analyzer. You can use it as a softwaredefined radio cuz it's got a like a 50 MHz analog uh bandwidth. So anything up to 15 MHz at 14 bit uh conversion, it's going to make a decent

**Dave Jones:** uh softwaredefined radio. Uh it's webbased interface, so either uh it my one actually came with a Wi-Fi dongle on it or you can use the uh Ethernet. You can uh program and operate this thing remotely from anywhere in the world. You

**Dave Jones:** can script it. You can do all sorts of things. And apparently it's open source, at least open- source software. And here's a closer look at the hardware used. It's a zinc. Uh they come in many different varieties. Anyway, it's the uh

**Dave Jones:** 7010 series uh system on chip. This is not a cheap part at all. Um especially in oneoff uh quantity. Here's our um analog inputs here. So here's our ADC. It's an LTC uh 2145. This is not a cheap

**Dave Jones:** part. It's almost the same price as the Xylink zinc. It's like 50 bucks. Um oneoff uh you know Digi Key type uh price for that puppy. And but the performance is absolutely stellar. I'll link in the data sheet down below if you

**Dave Jones:** want to check it out. And uh the dual um so that's dual channel uh 14 bit 125 meg samples per second. uh the DACK here. Um here's the two DAC outputs. Also 125 meg samples per second, 14 bits as well.

**Dave Jones:** That's about half the cost. That's about 25 bucks. So if you're wondering why this thing is so expensive, well, there's a fair bit of expensive chips in it. And unless you manufacture a thousand of these or 10,000, you know,

**Dave Jones:** it's going to cost a bit. And for those who want to see the bottom, there we go. Peekaboo. We've got all our bypassing on the bottom of the zinc there. tiny. They're little 0402 jobbies by the looks of it. Absolutely tiny. We've got some

**Dave Jones:** uh uh line termination uh stuff here and a few miscellaneous things. There's our USB we got some protection on the USB uh power input there. Looks like we've got a uh a poly switch. And it looks like we

**Dave Jones:** got a programmable attenuator on the front end here. And we've got uh two well Sart well they look like Sarda connectors and they are Sarta connectors but they're not designed for Sarda. These are synchronization connectors and I haven't looked into the details but

**Dave Jones:** presumably you can uh sync up the acquisition for big um between boards for like daisy chain them for big uh multi- channelannel stuff. But that's just a guess. I haven't even looked. So that's the red Paya hardware and yes it

**Dave Jones:** is a red solder mask. I love it. Beautiful. One of my favorite solder mask colors. Red makes it go faster. H. Anyway, let's take a look at the software. See if we can get this puppy up and running. See if we have any grief

**Dave Jones:** or whether it's just going to work like a treat out of the box. All right, let's see if we can make this red potato do something useful. Now, I've come to the website here. This is my first time

**Dave Jones:** using the thing. I don't have any instructions. Didn't come with it. At least my one uh didn't anyway. It's just the brick itself and uh the website. So, let's uh take a look. Now I have actually had a look at the website and

**Dave Jones:** it actually confused me uh for some time exactly what's uh going on here. I mean you you play the video here and it tells you all about uh this visual um programming you know visual programming system and things like that. So you know like I

**Dave Jones:** don't want to program this thing. I just want to use it as an oscilloscope you know as a network analyzer. uh you know get a bode plot or something like that. So how do you do that? Well, it actually you know kind of hints at it

**Dave Jones:** down here. It's here we go. Ready to use open-source webbased test and measurement instrument. So it does actually have a web interface in it. Now this thing runs uh Linux on it and you can connect via via Ethernet or you can

**Dave Jones:** connect via your uh via the Wi-Fi module. My one came with a little Wi-Fi uh dongle on the thing. So, it's not really entirely obvious like how to run the thing. It's different from your traditional more traditional USB scope

**Dave Jones:** like you plug it into your USB, you download the application for Windows or Linux or whatever and you run it and it talks to it and Bob's your uncle. No, this thing's a bit different. It is web- based. I know it's probably obvious to,

**Dave Jones:** you know, people who are familiar uh, you know, really into the programming side of things, the Linux side of things, the command line, uh, side of things and the networking side of things and things like that. but it wasn't

**Dave Jones:** immediately obvious to me anyway. Perhaps I am a dummy. Anyway, it tells you down here um the access is via Wi-Fi, LAN, and USB. Well, I haven't tried I'm not going to try the USB one. I'm more interested in the Wi-Fi and the

**Dave Jones:** LAN and uh so uh like you know I couldn't immediately like we can browse some apps here and we can do some other stuff and application marketplace and it has all this you know weird and wonderful stuff but I it actually took

**Dave Jones:** me a little bit maybe because I'm a bit dumb. You go up to the start here and you can go to the quick start. So this is actually a nice stepby-step process. It's uh look step number one prepare the

**Dave Jones:** SD card. Mine already came with an SD card, so I presume that they are preloaded and everything for me. I don't know if the one that you will buy will actually come with a pre-loaded SD uh card or not, but look, you can download

**Dave Jones:** the image. It's got instructions for Windows and for Linux and uh everything else. So, you know, you just download it and it creates a bootable disc image that contains Linux and everything else. Fantastic. because it's a bit scary

**Dave Jones:** because you go to the uh front page here, you know, and it's going well, you know, example like like download the source code and that sort of like freaked me out at the start cuz you know, I'm not a fan of, you know, like

**Dave Jones:** as soon as I see source code, it's like no fail, you know? So, like download the source code and it'll take you to the GitHub page and no thank you. I don't want to see the GitHub page at all. I

**Dave Jones:** just want to use my instrument. Thankfully, you don't have to. is go to this quick start thing here. Very, very nice. And so I'm presuming that mine already has that. And how would you like to connect the cable connection uh or

**Dave Jones:** wireless connection or direct wireless connection? Um I'm going to go for broke here and I'm going to go for the wireless. I'm going to plug the uh Wi-Fi dongle I got in here. And here it is. Enter your wireless information and

**Dave Jones:** download the configuration file. And that was the first trap. Of course, if you get it in your very sexy case like this, um the MAC address which you need is actually inside the thing. You got to take the rubber feet off. Um so I

**Dave Jones:** actually uh put my uh MAC address on the back here just on a little layer. So I took it apart and printed a little label for future use so I don't have to take it apart again. Um now it doesn't tell

**Dave Jones:** me like I presume wireless networking information. I'm presuming that's the name of my wireless network and that's the password. So, I'm going to give that a go. And it then I it generates a uh file and you can download you put it on

**Dave Jones:** the SD card and presumably Bob's your uncle and it should blink at you when we're done. Let's give it a go. All right. So, I downloaded and copied uh my file. There are uh two um USB connectors on here. You have to plug it into the

**Dave Jones:** power one, not the uh cons. I assume that's console. Um like a serial uh console type thing. So, I've copied the file. I've got my uh USB uh sorry, my Wi-Fi um dongle plugged in. It came with it, so I'm not sure which one you need.

**Dave Jones:** And there's a there's an LED on there, and it's flashing. And it's supposed to after 30 seconds or so. So, we're going to have to wait. Uh it should eventually be green and flash red. And I can kind of see Oh, there it is.

**Dave Jones:** D. It's like a heartbeat. I think we have a winner. So, here we go. Step number three. Connect to your red potato and make sure it's connected to the internet. How can I make sure? I don't know. That's another fack thing which I

**Dave Jones:** don't want to read yet, unless something goes horribly. Oh, no. Look, no, no, I don't want to do command pings. No bugger that. I just want to input my MAC address and go, let's start. Oh, got to create an

**Dave Jones:** account. Thumbs down. I guess that one could be useful cuz then you can access it from anywhere. And I don't know. Anyway, and bingo. We're in like Flynn. Check it out. I just uh registered. It didn't uh have to make me verify my

**Dave Jones:** email. So, beauty. Um it just took me straight in. Said, "Thank you for registering." And I put in the MAC address and the AEV login blog. And there it is. There's my uh LAN IP address that I can go go directly uh to

**Dave Jones:** it presumably unlocked applications oscilloscope plus signal generator and spectrum analyzer visual programming license. I don't have a license for this visual programming uh thing. I don't want to you won't see me do that in uh this video. I'm not really interested in

**Dave Jones:** that. I just want to use it as a you know spectrum analyzer oscilloscope everything else. So um yeah we're in like unlock apps. Can we have a look at unlock? I don't know. Unlock code. I got no idea. Anyway, start. We can either

**Dave Jones:** start it or we could go directly to the IP address presumably and it should just work. It should just connect to the browser. Remember, this is Wi-Fi. Um, so I'm not connected to the Ethernet at all. There it is. And that's my

**Dave Jones:** telephone. Well, that didn't work. um not directly to the IP address anyway. So anyway, let's just hit start. Um I have seen where you can actually access it from the main page. So let's actually go back and have a look uh EV blog. I thought I

**Dave Jones:** saw somewhere once that it uh my There we go. My repetitay. You can just hit that. There you go. And it takes us straight to there. That's that's kind of cool. Once you're uh once you're logged in is not available. No, it doesn't like

**Dave Jones:** it. Fail. Geez. Is this like a Wi-Fi like access? I mean, it it can see it. It right. It can see it. Tells me my LAN IP address, everything. Like, if I have to go in and bloody create gateways or some

**Dave Jones:** other crap, I don't know. I'm not some network penguin guru. Um, yeah. No, it just doesn't work. H fail. See, stuff like this just really, you know, leaves a bad taste in your mouth. Doesn't inspire uh confidence at all. It might have just

**Dave Jones:** worked if I plugged into the Ethernet. I'll try that. So, there we have it. Got my Ethernet plugged in. We've got that uh red heartbeat uh double flashy thing. So, yep. I'll go through the process yet again. And it wouldn't let me add a

**Dave Jones:** second device because the MAC address already existed. And I just clicked on the uh IP address here. Presumably do the same thing if you do start. Yes, it is. Start button is the same as that. And tada. We're in Lake Flynn. So,

**Dave Jones:** sorry. I have no idea what happened to the uh Wi-Fi thing. Some DHCP thing or something maybe. I don't know. Everyone who knows all about networking is probably screaming at me. Oh, that's obvious. But hey, you know, it didn't

**Dave Jones:** work for me. So, what am I supposed to say, right? didn't work out, you know, didn't work off the bat. So, not impressed at all with uh that Wi-Fi setup. So, anyway, works with the Ethernet. So, beauty um visual

**Dave Jones:** programming um which I yeah, I don't want to do that in this oscilloscope pro and spectrum analyzer pro. And we can get more uh applications. We can either do a demo or we can run it um like run

**Dave Jones:** the real application on the real hardware here. So, here's more. Uh, look at this Tesla meter. Two channel time domain signal visualization system. Um, cool. Ah, PD controller and oscilloscope. Look at this. Okay. Frequency response analyzer. Very very

**Dave Jones:** nice. Aka uh well, it's a it's a Bode analyzer. Well, you know, frequency response sort of blo plot. Um, and impedance um analyzer requires a shunt resistor. There you go. It's even got a link to a guide available for that

**Dave Jones:** contri. Okay, so these are the official uh Red Pate apps and then we've got contributed apps because that's a whole thing about this. It's open source hardware. You can actually um it's you know it's all available. You write your

**Dave Jones:** own apps and everything like that. So these are community uh developed apps. It's got an SDR uh transmitter. Um, fant S SDR transceiver, sorry. Because it's got a signal generator and a uh and a oscilloscope/receiver as well. And like

**Dave Jones:** it's it's a full uh 50 mehz up to 50 meghertz or so I believe is the bandwidth um SDR or softwaredefined uh radio. So there you go. Good on you. Pavel demon. Um and LTI DSP workbench. Oh, that's interesting. Um, another

**Dave Jones:** spectrum analyzer, SDR transceiver, another uh SDR app. Um, yeah, I think this thing could be, you know, a fairly big and uh useful uh device for the SDR community. At least up to 50 meghz or so. You know, if you're up to the, you

**Dave Jones:** know, the real um the high frequency stuff, then it's no good, obviously. But, uh, anything below 50 meg, it's probably going to do the business and do it really well. Uh, at least it has the hardware to do it. So, it all comes down

**Dave Jones:** to the apps. calibrate upgraded with DC offset calibration. Oh, you can calibrate your thing. Anyway, I'm going to install a Bode Plotter. Here we go. How does it work? It's spinning around, spinning its little gear wheel there. And

**Dave Jones:** uh I assume it um downloads the app to the red Paya and uh cuz obviously it's got to run on the hardware um itself cuz it's got to utilize the um the FPGA and uh stuff like that. So it's got to uh

**Dave Jones:** it's got to program things in there. So yep. Okay, it's installed. I'm going to install them all. So, I haven't actually used it yet, but I I'll tell you what, I'm liking this um you know, webbased um app model interface. It it looks like

**Dave Jones:** it's it's, you know, it's really jazzy doing the business here. So, uh quite impressed by that. It's their bazaar. So, it's you know, the apps are available at the bazaar. There you go. So, how do we get back? How do we get

**Dave Jones:** back? I guess we just go to our IP address. Tada. There you go. There's all our apps which we didn't have before. Awesome. Look at that. So, our impedance analyzer, that's a basically an LC, well, as it says on the icon there, um

**Dave Jones:** LCR meter. And we can um obviously won't see anything here. Here, I need to make up a little jig with a uh a shunt resistor in there cuz it basically measures um the voltage uh from the generator and then the voltage across

**Dave Jones:** the device under test in series with a shunt resistor. And from those two voltages, you can uh calculate um the impedance and everything else. You can calculate capacitance, inductance, resistance, everything else. You can draw uh the response and do the whole

**Dave Jones:** thing. I've done a video on that if you want to uh know how to actually calculate um those sort of things way way back like episode 30 or something crazy like that. Anyway, so we can go in and this is all web-based interface. I'm

**Dave Jones:** liking this. It's quite neat. All right. Oscilloscope Pro is uh the one that we uh is the one that came with it. I'm not sure why they wouldn't install all the official ones as um standard. Um, I guess maybe they don't want to confuse

**Dave Jones:** people. They just want to, you know, here's an oscilloscope. Here's a spectrum analyzer. That's it. Um, just fair enough. And here's our scope. We're in like Flynn. And one thing to note, this thing actually does get quite warm

**Dave Jones:** during operation. I'm not actually doing anything, not sampling. Well, I guess I'm running the scope app, but uh yeah, you know, it gets reasonably warm. Not overly hot, but of course. Uh so as you saw it's got the uh heat sink there on

**Dave Jones:** the uh top of the case which goes down presses against the uh XYlink zinc processor inside this thing which is a really powerful beast combination FPGA and um ARM something or other processor and uh running Linux really you know

**Dave Jones:** high-end um powerful beast a reasonably low well high efficiency as well it's fairly high efficiency but still it's doing a lot in there but uh yeah so it's getting reasonably warm but still you know in the scheme things that's drawn

**Dave Jones:** like bugger or pow for you know a ridiculously powerful instrument like this that you probably couldn't even dream of getting 5 years ago by the way absolutely amazing now I'm not sure what's going on here I went in uh I

**Dave Jones:** don't mind this interface like you can turn the um uh channel on but I had the channel there before and now it's gone and I was playing around with the output and here we go I can select uh various

**Dave Jones:** um output uh waveforms from the uh generator And like it's I don't know. I tried to type in a higher frequency here. Press enter and everything. My waveforms seem to have vanished. Show unshow. It's like stop run. I don't

**Dave Jones:** know. Like something's like auto scale. Nothing. My waveforms have gone. Not sure what's going on. H. Well, it's the old Have you tried turn the power off and on again? Well, instead of that, I just went back a page and uh

**Dave Jones:** opened up my scope gen um pro application again and my waveform's back. So, here you go. Um if we like let's just try and select that auto scale. Can we can we do anything there? No. No. But it's still got Can we drag

**Dave Jones:** that? Oh, we can drag the offset. That's nice. All right. But that's you know, it's exactly what you'd expect. So, let's turn our sig gen on. There we go. Bingo. I've got a uh I've got an input output cable connected between channel

**Dave Jones:** one and two. We're in like Flynn. There we go. What's the green? Oh, the green is the second uh input channel. We don't really want that. So, can we No, I don't know how we Oh, there we go.

**Dave Jones:** Show. No. How do we turn off the second channel? See, like it's stopped updating. What's going on? Like, it's worked. It's captured something, right? But then it it's just Hey, there we go. Look, it's gone. What the Okay, watch this.

**Dave Jones:** Right, I go back and I select my oscilloscope. Okay, and I run it. And everything seems to be hunky dory, right? So, let's um now go into our output here. Let's turn our output on. Okay, everything's fine and it's frozen. And I actually

**Dave Jones:** look if I go back here and I go back, I don't even have to turn the um function gen on. Why it's taking its time to look. Get back. No, something's something's horribly wrong with this thing. I don't know what don't

**Dave Jones:** know what I'm doing. I can't select my No, something. There it is. Something has gone wrong. Is there a problem with the server? What server? I just got a router. I've plugged my box into the router here. And um which is the same

**Dave Jones:** router that my uh PC here I'm using is plugged into. So, you know, it's not like it has to go halfway across the world or anything. And what I I got no idea what the photons going on. fail.

**Dave Jones:** Wow. Wow. Okay. Yeah, we're back. And uh we're at one volt per division at the moment. I don't like this control over here which adjust your thing. I'd rather have like a separate knob or buttons for each channel and stuff like that. So

**Dave Jones:** anyway, if we increase that look, 500 millolts per division. Okay, so we're going down. So that's all hunky dory. But it froze last time I did this. It actually froze. So, we can change our time base, too. 2 milliseconds per

**Dave Jones:** division. There we go. What are we picking up there? That's interesting because that's our channel one. And that is that's fascinating actually because I've just connected, as you saw, the output of the SIG gen to the input of this and it's um the SIG

**Dave Jones:** gen is turned off. So yeah, quite strange. Anyway, we can turn our sig gen on. There it is. Hey, got some alias in there. Doesn't like that. Um, it seems to be more stable now. It seems to be

**Dave Jones:** doing the business. So, I don't know. Um, it's fairly it's fairly responsive. There's a slight delay when I click that button, but not much. It's It's pretty good. And the uh the waveform quality is is brilliant, as you'd expect with a 14-bit

**Dave Jones:** converter. It just it looks like it's doing the business. Now, here we go. Here's a worry. I'm going to select channel one and I'm going to go auto scale. It works. Yes. Beauty. Um, channel two. We uh can turn off channel

**Dave Jones:** two. Yeah. Like there's plenty of room on the screen here to have all these settings, right? all all of these settings here all on the screen and all the controls. Why I've got to actually select number two and then go into a

**Dave Jones:** setup icon thing. It's no dumb. No, that's just poor user interface uh design. Sorry. Anyway, look, it's frozen again. I don't know. I might go back to scratch because I I use the SD card that came with this thing and it's I they

**Dave Jones:** sent it to me like a month or might even be a month or two back uh now. So maybe there might be, you know, a latest version. I think I might nuke the SD card and actually download uh from

**Dave Jones:** scratch following their instructions cuz I didn't do that. I just used the SD card that came with it. So maybe I don't know. I wouldn't know how to begin to troubleshoot something something like this. um someone with network experience

**Dave Jones:** that go oh yeah I'll just go in with my penguin skills and go into the command line and you know um try and figure out what's going on here but I've got see no idea dummy user like me it just freezes

**Dave Jones:** on me you know what am I supposed to think right it's not a good impression at all well scratch that idea I'm using build 549 uh version 94 and that's exactly what the current version is.94. Um, RC22 doesn't say that there, but I looks

**Dave Jones:** like I am using the correct version from the 21st of December. And I'm pretty sure they sent it to me after that. So, yeah, it's not the image file. Well, I'll tell you what, I've switched browsers. I'm now using Firefox instead

**Dave Jones:** of Chrome. Uh, and it is holding up. So, um, yeah, I don't know. Chrome is their recommended browser. It says so right on their page that and they link to it. Um so I've got Yeah, I got no idea. But it

**Dave Jones:** seems to be much more stable now. I haven't had it crash once on me yet. So that's pretty good. All right. All right. I'll chalk that up to a browser issue. I'm pretty sure I got the latest version of Chrome installed or whatever,

**Dave Jones:** but yeah, I don't know. Anyway, here we go. We're generating a 10 megahertz uh sine wave now with the uh sig gen here. And as you can see, our sampled waveform in yellow there is well not that great

**Dave Jones:** because this is well it's 125 meg samples per second. So we're getting our 10 samples per division, but there's no um sign presumably no s doesn't look like any sign xonx uh interpolation here. It's just got linear interpolation. So, and there's jitter

**Dave Jones:** the, you know, we're getting uh uh So, our trigger is currently set to channel one input. Yeah, I mean, we could probably um external input actually. Where is the external input on this? It might be on uh one of the internal

**Dave Jones:** expansion headers or uh something like that cuz there's not an external uh header thing on here. So, there you go. Oh, by the way, I did not show you this cuz I had my uh position thing, my waveform position thing. Sorry. Um, this

**Dave Jones:** is the thing I was talking about before for the uh our vertical and horizontal control down here. Down here. There we go. Wrong screen. It's weird having two things happening here. I got my preview window open with XSplit and my real one

**Dave Jones:** over here. So, um, yeah, I don't like the control. As I said, like all this wasted space around here. Look on the left hand side. On the right hand side, and we've got this dinky little, you know, gear setup icon thing. No. No.

**Dave Jones:** Just no. Fail. No. There's plenty of room in here to put everything you need. So, I think they really need to um update the uh uh user interface with that thing. Anyway, um settings. We can do calibration. Haven't tried that. Anyway,

**Dave Jones:** that's kind of what I would expect. Um, of course, we're seeing single sample uh jitter there. So, you know, I don't think we have any other options in there to actually uh display to change our interpolation, do averaging or nothing

**Dave Jones:** or anything like that. So, it's a very basic um oscilloscope. Now, here's the thing actually. Uh the red potato is supposed to be open source. They're, you know, promoting open- source blah blah blah, open- source software. Yeah. But

**Dave Jones:** not open-source hardware by the looks of things. And I actually I couldn't find any schematic on their uh web page at all. And when I um actually Googled it, the first hit was actually the uh red potato schematic was actually the EEV

**Dave Jones:** blog forum. And somebody um London doc is very disappointed the refusal to release full electrical schematics for the supposedly open-source project. My guess is they want to keep imitators from generating similar products. I Yeah. Um yeah, fail. But anyway, I

**Dave Jones:** actually somebody has actually done it, I think. So I think either somebody got the schematic or they reverse engineered it or something. I think it's in here somewhere. I can go into here and maybe we can actually e times inexpensive

**Dave Jones:** portable test tool. There we go. Is that No, that's not it. H. So, yes, if that's genuinely the case, that is a big thumbs down for not releasing the schematic. I presume that they've got all of the source code for the ARM processor plus

**Dave Jones:** the FPGA and stuff like that because you can actually do FPGA development on this thing. Not only is it designed as a general purpose oscilloscope, designed as a coding tool and things like that, um, but it's also designed for FPGA

**Dave Jones:** development because it has that uh, XYlinks zinc FPGA in it. And you can do that. They actually ask you uh, when you register, what do you want to use it for? Do you want to use it for, you

**Dave Jones:** know, as an oscilloscope? Do you want to use it for FPGA development or whatever? So, um, yeah, presumably they've got that. I don't know. I haven't looked into the source code and uh everything else but yeah you can do remote control

**Dave Jones:** using mat lab python lab view silab it's got you know if you really want to get down to the nitty-gritty of integrating this uh integrating a scope or a DAC it's effectively what this is a data acquisition um you know module then uh yeah this you

**Dave Jones:** know this thing could be the duck's guts uh for doing that if you you know if it suits all your hardware um hardware specs by the way we can go in there and ta there it is dual core arm A9 that's

**Dave Jones:** the XYlink zinc uh processor as I said 125 meg sample per second 14 bit converters dual uh converters in it uh synchronous sampling that's how they can do the uh LCR module the impedance analyzer module they actually sample

**Dave Jones:** them at the same time otherwise you got issues. So, um it's got dual sampler in there. It's got a a secondary uh sampler on the IO uh headers internally on the thing. Uh 100k samples per second at 12

**Dave Jones:** bits. So, that's not too shabby. You can do some useful uh stuff with that as well. And they're trying to compare it to the Raspberry Pi and the Arduino Uno. Not really the same thing, but as I said, they're trying to uh sell this

**Dave Jones:** thing as like a programming platform, hence all the visual programming stuff that they're actually uh talking about here. Download the source code. No, we've looked at that, but uh and where is it? Where's that visual programming thing? Compile

**Dave Jones:** sources. Oh, boy. You make your own web-based apps and all sorts of weird and wonderful things. But anyway, visual programming. There it is. buy now. Do I have to buy the visual programming interface? Um, that's a bit disappointing, but I guess they got to

**Dave Jones:** make their money somehow. Um, although they I'm not sure how much they're making on this uh board. I haven't done a bomb costing. Um, but it's not a uh cheap board by any stretch of the imagination. Oh, they've got an LCR

**Dave Jones:** meter extension board. A I wish they would have sent me one of those. I'm going to have to uh build for 300 bucks. Sorry, 300. Wow. will be available in 30 days. It's on back order. €300. What's on it?

**Dave Jones:** It's just got a pick. That looks like a That looks like a pick. And uh sorry, I'll just drag this uh drag this window back here. And it's it's Is it a pick with some shunt resistors and some

**Dave Jones:** relays? They look like little Pickerin relays. Um if they are, very nice. I'm a bit of a Pickering relay fanboy. Um I like the fact that they're red. I've never seen them in red before. Wow, they're little um compact singlein line

**Dave Jones:** ones. They're probably magnetically shielded as well. You can get magnetically shielded options in the Pickerine relays. Anyway, very nice relays. Have extensive experience with those. Um Jeez, 300 euros for an LCR meter board. Wow. Jeez, that's pretty rich. Anyway,

**Dave Jones:** while we're here, let's take a look at uh some other stuff. the aluminum case which I've got which I highly recommend it. It really is, you know, it's just very sexy, very sexy case. Um, yeah, it's that's available for €39. That's an

**Dave Jones:** optional extra cuz normally it's just a bare board. Uh, what else they got? Oh, there looks like they've got a um like a is that like a 3D printed like or an a clear acrylic uh case? That's a cheaper

**Dave Jones:** one. I don't know. I like the uh Is that a Oh, no. That's just a vent hole. Oh, a fan. Okay. It looks like you can screw a fan on the top of this thing. Um no, the aluminium. If you're going to spend

**Dave Jones:** spend the extra 10 bucks and get the aluminum case, definitely. Uh calibrated diagnostic kit. What What's included in the calibrated diagnostic kit? Um I This is actually what I got. I think I believe this is what I got cuz I got a

**Dave Jones:** couple of probes with mine and I got the SMA adapters and uh Tpieces and things like that. Uh so, yep. I don't know whether or not uh well calibrated. I guess they mean calibration and calibrate the probes. I guess what

**Dave Jones:** they're talking about there. So, we should actually run the calibration anyway. Let's have a look what else they got. So, the red potato board itself, by the way, is €199 or Yankee bucks. 238 Yankee bucks. Um, you know, it might sound expensive

**Dave Jones:** for just a board, but the XYlink zinc processor in it is not cheap. I think if you go cost that one off, it's probably like a hundred bucks for the chip or something. I'm not, don't quote me on

**Dave Jones:** that, but you know, it it's not a cheap uh chip. It's got dual um Cortex A9 plus the FPGA in there. Incredibly powerful chip. So, uh, very expensive, but no, you get a lot of bang per buck in this

**Dave Jones:** thing. I It's Yeah, I I think it's it's worth the money. It is worth the money. I like the, uh, app, uh, concept and things like that. It's shame it's not fully open source, though, or it doesn't appear to be. That's a real bummer. But

**Dave Jones:** uh yeah, I mean you can develop all your own apps. So all the SDK and everything, the programming, all the source code and everything's available, but why not give us the hardware? Jeez. And they want a lousy $6 US for the visual programming

**Dave Jones:** um system. Oh, free. And you can get a free trial for 7 days. Play with it. Not sure why they bother selling it at um you know at 5 a pop for why it's not included but I can understand it's

**Dave Jones:** probably a lot of effort to develop a visual programming interface and it kind of looks all jazzy and but yeah I don't know I might have to save that for a separate thing but if you're really into programming and getting apps up and

**Dave Jones:** running real quickly the problem with these visual programming interfaces is that they're non-standard so you know yeah here it is like do repeat uh loops here we and you know put command rotary le so you can do various things you know

**Dave Jones:** really easy for getting apps up and running real quick but ultimately useless um like skill to learn if you want to you know actually program something else so but allows you to you know it's kind of like uh national

**Dave Jones:** instruments lab view for example you know really incredibly powerful programming visual programming environment but it's a skill if you learn that that's it like It doesn't translate to any other product at all. So, um yeah, similar thing here. What do you know?

**Dave Jones:** N fail. No, Firefox is also locked up as well. That's just it's just ridiculous. I What can I say? No, you know, is it just me? It's probably just me, right, Murphy? there's something weird with my configuration of my PC or something like

**Dave Jones:** that and everyone else and nobody will have problems or anything like that. I don't know. Anyway, looks like I might have to actually make uh use of their forum. I might jump on the forum and go, "Hey, what the hell is going on?" You

**Dave Jones:** know, thing locks up. Well, that's probably in the frequently asked questions. Although, if it has to be in the frequently asked questions, why does your, you know, red potato always lock up? um then well it shouldn't have to be in the fact

**Dave Jones:** um but it's probably not. Anyway, they've got support down here and a frequently asked question. So maybe no connectivity problems. No, no, I'm having reliability problems, not connectivity problems. No, it all connected just fine. H except for the

**Dave Jones:** Wi-Fi. Still haven't figured that out yet. So I don't know. Bloody these tools. Uh, it's why I like, you know, bench oscilloscope. Plug it in, turn it on, works, you know. But granted, this is not a replacement. I keep saying this.

**Dave Jones:** USB oscilloscopes are not replacements for bench oscilloscopes. They have their niche uses. In this case, it's not really just a USB scope. If you just want a USB scope, go buy just a USB scope. You probably wouldn't just buy

**Dave Jones:** this. It's more useful at, you know, when you want to do, you know, really clever stuff with it. You want to automate something, you want to uh design, you know, an automated uh web, you know, interface that'll, you know,

**Dave Jones:** tweet when you signal goes out, you know, when you get a signal or something like that or or do whatever, you know, you can interface um digital stuff to this. You can do all sorts of things. Program it. Fantastic. If you want to

**Dave Jones:** use this software learning tool, an FPGA learning tool, that's what it's uh good for. If you're just using it as a USB scope, obviously you've seen it, right? You've seen the interface. It's no good. It is like that's a hopeless USB oscilloscope.

**Dave Jones:** It works, but you know, it doesn't offer you any, you know, bells and whistles at all. Okay, if we go in here and run another app, the frequency response analyzer, the all these apps are pretty basic, I've got to admit. Um, not

**Dave Jones:** terribly um not terribly impressed with them. Here we go. Now, um, this one I haven't actually, uh, plugged the thing in. So, let's actually plug it in. This is showing the response over the full range. So, if I plug that in. There we

**Dave Jones:** go. That's pretty horrible, which is why we have to calibrate the thing. Um, let's turn channel two off. There's channel one. Look at that. Wow. Why it's that horrible? It's it's by default it's going from 0 to 60 megahertz. It'll be

**Dave Jones:** sweeping over that um range and we can calibrate. So if we hit the calibrate button. Yeah. Okay. It's reasonably flat. But look. Uh-uh. It's all over the shop. What the what the photon? Look at this. You see it rolling off there at

**Dave Jones:** the end. What? Like this is like gain like you know a couple of dB here. Like it's horrible. What's going on? I don't get it. How can it be that bad? Yeah. So that's a real dinky app. I mean all you

**Dave Jones:** can do Oh, error while sending data. E3. What the restart? What the? Like come on. What? Wow. This thing is flaky. Is it just me or is anyone else having issues? I mean like wow why this needs to be why

**Dave Jones:** it's out by that much over the over the frequency range. I got no idea anyway. It's it really is quite dinky. I mean you can zoom in on parts like that. Okay, that's fairly good. But that's basically all you can you know that's

**Dave Jones:** basically all you can do. You can reset the zoom. Oh no. How do you reset the frequency? We can scroll with the frequency. Like it's a real like really basic app. No. Applica application not loaded. What the What is

**Dave Jones:** wrong with this thing? Anyway, if we go back. Wow. It's not like I'm over Wi-Fi with some dodgy connection or something. I'm connecting directly with Ethernet with this thing. Anyway, go into uh the Bode Plotter app. And um this is very Spartan as well. Like I

**Dave Jones:** I had a quick play with this before and it's like range settings um measurement settings look amplitude like if I want to go point you know if I want like 10 millolts amplitude if I want to get a

**Dave Jones:** you know generate that like what the like like what start measurement blah blah blah measuring measuring measuring and like it's just a real dinky app don't like it and here's the other Oscilloscope app instead of the oscilloscope pro. Um, this one can do

**Dave Jones:** averaging. Look at that. No workers. Um, but yeah, like no, the user interface just No, no, no. Don't like it at all. No fail. Um, so don't really care for that at all. Let's We haven't had a look

**Dave Jones:** at the um It's bit dicky to frequency response analyze. Why should I have to scroll that list? Why can't it make use of once again user interface make use of all the screen just have the links there like you know why it even has to be

**Dave Jones:** fancy like this why this can't be like a text link or some you know like a basic HTML page or something why it has to be all fancy pancy like this um I don't know whatever anyway oh no didn't want

**Dave Jones:** the frequency response analyzer I wanted the spectrum analyzer. There we go. We haven't had a look at the spectrum analyzer yet. Let's go in have a squeeze. That's really quick updating there. Um, and how do we set all of

**Dave Jones:** our how where are our settings? Frequency. We can have our frequency range, but like where is our number of bit, you know, where can we set number of bins? Where can we set the window in? Where can we set? I I see autoscale. I

**Dave Jones:** see reset zoom. I see an incredibly basic app. Wow. Wow. No. No. No. That doesn't cut the where? No. How do you set up? You can probably zoom in. Okay. Whoopde-doo. No. Where's all the settings? What do you want me to say

**Dave Jones:** about that? Really? I mean, no generator and oscilloscope. That's the thing I wanted to test like how can you set the generator running for example in the background and then go use your oscilloscope app uh for example is that

**Dave Jones:** possible or do you need an app like this one which has generator and oscilloscope built in. Now this looks like the oscilloscope app we had before but it's got the extra signal generator down below. So there you go. We can uh looks

**Dave Jones:** like you can file you can upload files. So arbitrary wave wave gen. But yeah, this is not no the apps are not impressive. The hardware I really like the sort of the way that they've done it with the

**Dave Jones:** web-based thing and the apps and everything. I do like it, but the apps leave so much to be desired. Um 0.01 volts peak to peak low level. Okay, let's go. One. There we go. We're in like Flynn. Auto. Let's hit the auto button. Hey,

**Dave Jones:** there we go. It popped up. That's our gen. That's a dinky toy interface. That is That is very dinky toy. Oh, no. Sorry. Channel one. Sorry. Channel one is the blue. I thought channel one was the um that was the wave signal

**Dave Jones:** generator waveform. It's not. My apologies. It's the um actual sample waveform. Um, but yeah, like it's I don't know. There we go. I can use the mouse wheel. That's pretty good. And uh Oh, can save image. Yeah, I can drag. I can zoom, do

**Dave Jones:** all that sort of jazz. But yeah, I'm no I'm not impressed with these apps. Not impressed at all. Sorry, Red Paya. No, more work required. And of course, one of the things I really wanted to do with this thing is get a Bode plot of my

**Dave Jones:** microcurrent like I did with the analog discovery uh before with great ease. But like this Bode analyzer here, it's just like look, it's not even look starting frequency uh 1 kHz. There it is. But the actual graph here starts at like zero

**Dave Jones:** hertz. There's one hertz, 10 hertz, 100 htz. Like what? Like it's just ah it's just ridiculous. And why is this like the amplitude I want to set 10 millolts because microcurren has a gain of 100. I can do this easily on the analog

**Dave Jones:** discovery. It works a treat. Um you know it's a little bit inaccurate down at 10 millolts when it's trying to generate you know a 10 millolt signal but it gets the job done um fairly well. And this thing's just hopeless. Start

**Dave Jones:** measurement. Like it should go d sample sample sample. It should draw your bode plot like that as it sweeps the frequency. But no, I mean I've set it to start at 1 kHz. Yet what is it? Starting at zero one hertz.

**Dave Jones:** What? This thing doesn't work at all. It's useless. There you go. It's just sitting there locking up. Surely I can't be the only one having issues with this thing. I mean, really. I wow. And this has been this is version

**Dave Jones:** 1.1. It's been out for a while since they did the original uh Kickstarter thing. I think it's been quite a long time. I can't remember when they did the original Kickstarter, but geez. Um, no. This is something seriously wrong here. I It

**Dave Jones:** can't be a Pebbak surely. Oops. Silly me. uh with the spectrum analyzer before I was not in the spectrum analyzer pro I was in just in the regular spectrum analyzer so that's it um but once again look right it's not generating a signal

**Dave Jones:** like I had used the the generator app before to actually generate a signal and now it's gone like you change the app and it like I don't know reconfigures the FPGA hardware in there and it's it's gone like unless you're specific I guess

**Dave Jones:** specifically right nap which has both functionalities built in and I don't I don't like that at all. Um but once again this is supposed to be the prospectrum analyzer. Okay. Where where are all the settings? Where's your number of FFT bins? Where's

**Dave Jones:** like where is it? Where is it? There's nothing there. That's barebones. that is as barebones as you can get. You know, it it's it's probably going to its performance is actually probably going to be quite reasonable with the 14 125

**Dave Jones:** meg sample per second 14 bit converter. Um I have no doubt that it would be reasonable, but the app, this is the pro app, right? This is the pro app. Where are the settings? Nothing. So much for pro.

**Dave Jones:** That's just nah. It that doesn't cut it. I'm sorry. It's, you know, you've got to have impressive uh default apps for something like this for people to use. I know it's more of a, you know, it's probably, you know,

**Dave Jones:** more of a programming learning type tool than it is, you know, like a real off-the-shelf useful tool. Um, like out out of the box experience. A better out of the box experience by far is the um analog discovery uh one which I've done

**Dave Jones:** a video on and people have uh asked about uh before and that the out of the box experience of that one completely uh blows this one away. Um but this but the red potato is inherently more powerful in terms of uh stuff it can do and

**Dave Jones:** things like that. So I I don't know. I think I give up. That's all for this video. I'm There you go. That's the red potato. I'm Yeah, I'm headed home. What is it now? 6:44 p.m. Yep. Um, not that impressive. Sorry, Red

**Dave Jones:** Paya. It has great potential. I think it's really good if you want to go to the effort to write the app and things like that. I think it could be a uh incredibly powerful tool and a big winner

**Dave Jones:** um for you. And I like the app interface and I like the way that they've done it. The quick start thing, it all seemed to work apart from the Wi-Fi thing. Very disappointing. I don't know why it's locking up, but it seems to be working

**Dave Jones:** now. And issues with it, but the apps just don't cut the mustard as an offthe-shelf tool. Sorry. Um, nope. Not hugely. So, impressed with some things, not hugely impressed with others. So, you're going to have to weigh up whether

**Dave Jones:** or not uh it's the tool for you. If you want an out of the box experience uh with, you know, a good USB scope and spectrum analyzer and everything like that, uh the Red Paya is probably not for you. I'd recommend if you want out

**Dave Jones:** of the box, I would go for the uh analog discovery, uh which is a similar price. I think it might be a little bit cheaper, but it's not as powerful as um this. I think the specs of the Red Paya

**Dave Jones:** are superior. So there you go. That's a quick look. I will no doubt play with this some more. I want to do the LCR meter uh functionality which I um didn't uh get to look at. Where was it?

**Dave Jones:** Impedance analyzer. I didn't uh yeah plot settings. I'm going to have to build up a little um it's not hard. Just a 50 ohm resistor in series with a device under test, things like that. Um but I'll try and do that as a separate

**Dave Jones:** uh video because that could be quite useful. or I want to you know uh get um impedance responses of various components you know capacitors for bypass applications inductors things like that um so that could be uh quite useful as for you know network analyzer

**Dave Jones:** stuff so I'll have to do a separate video on that one but there you have it that's the red paya which is kind of sort of working for me um yeah might have to get on the forum anyway hope you

**Dave Jones:** like that. Uh first look, I guess first impressions cuz this is just me first playing around with this thing. Um and I think it has potential, but uh yeah, it needs a bit of work. Catch you next time.
