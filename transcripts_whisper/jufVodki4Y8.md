---
video_id: jufVodki4Y8
title: CleverScope USB Oscilloscope - EEVblog #207 (2 of 3)
url: https://www.youtube.com/watch?v=jufVodki4Y8
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 15, "2": 36, "3": 55, "4": 70, "5": 86, "6": 102, "7": 117, "8": 131, "9": 146, "10": 156, "11": 169, "12": 186, "13": 202, "14": 219, "15": 235, "16": 246, "17": 262, "18": 277, "19": 293, "20": 306, "21": 319, "22": 330, "23": 354, "24": 364, "25": 375, "26": 389, "27": 402, "28": 417, "29": 433, "30": 452, "31": 467, "32": 487, "33": 498, "34": 510, "35": 528, "36": 539, "37": 552, "38": 565, "39": 575}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. And I'm here with Bart from Cleverscope. He's the designer of that. Yeah, I make Cleverscopes and I love your blog, Dave.

**Dave Jones:** It's a beautiful blog. Thank you very much. It tells me a hell of a lot of good stuff. Well, we make Cleverscopes. Tell us about the Cleverscope. I can take one here and pull it out. And it's a little toy. It's a PC scope, so it's going against the Pico scope and all those other little scopes.

**Dave Jones:** This is what it looks like. It's a pretty average sort of plastic case, but hell, it works. If you open it, you can see inside. We have hardware. We have a teardown. Here we go. Here's inside. Teardown at Dave's blog, live at electronics.

**Dave Jones:** You betcha. And that's inside the Cleverscope. I assume there would have been several generations? There have been a few generations. Cleverscope? Yep, there have been. And this is the current one. Except that one's probably a bit bodgy because it's got development stuff inside it, I suspect.

**Dave Jones:** Right, okay. No, it's not too bad. This is the Ethernet version. So you can see there's the Ethernet board. Hang on, let's put it down on the table over here. There we go. And tell us about the hardware. I'll zoom in on that.

**Dave Jones:** We can do that, yeah. So this is the digitizer. And we do them in 10, 12, and 14 bits. So this is a 14-bit digitizer. This is all the analog stuff. And over here we have DC offset, which is so that we can look at just a small chunk of range,

**Dave Jones:** like 2.1 to 2.2 volts, and digitize across just that chunk. Right. Over here we have our mixed signal input, the eight digital ins. Yep. Not too many PCs got to do that. Yep. And over here is an Altera Cyclone. Magnificent device. That's where all the magic's running.

**Dave Jones:** It's all the magic, and we can change it. Yep. And people can go and upgrade their hardware in the field later on. Fantastic. Memory. Yep. SD RAM. Yes. It's got a couple of, what is it, eight? It's got eight megs. Eight meg of sample memory.

**Dave Jones:** But it's not high sample rate, this one. It's only 100 meg samples. 100 meg samples. So it's pretty slow, but when you've got a 14-bit converter, that's the magic. Plus, you've got a trigger that can capture almost anything. Excellent. I reckon, anyway. Wow, yes.

**Dave Jones:** Not that you're biased or anything. No, no. That's right. All right, but you've got to talk up your own product. Ethernet interface. Magnificent device. That's the WizNet chip. I don't know if you've come across those. Oh, you've heard of it? Hardware, hardware Ethernet.

**Dave Jones:** Yep. And then here's the SIGGEN, which is a little, using a little analog devices DDS chip. Right. Just shoots us down to the ground. As you can see, there's a bit of power supply. Yep. That's Bob's uncle. Aluminium case to stop the stuff, bad stuff getting in.

**Dave Jones:** Shielded? We have it. Excellent. Thank you for the teardown. The interface is LabVIEW. It's LabVIEW. It's all built in LabVIEW. You can see the LabVIEW he sort of controls. Yep. But, you know, we have lots of windows here. One of these, this one over here, is actually not one of ours.

**Dave Jones:** It belongs to MATLAB. Right. That's because we were piping through stuff to MATLAB until I pulled the kinescope off the rack and stopped it from working. We had mixed signal, as I say. Yes. And we can decode protocols. Well, we can. Yep. Not today, we can't.

**Dave Jones:** It's waiting for something. Right. That's all right. I'm sure it does. Hang a sec. Hang a sec. Why is it happening? Anyway, I buggered it up. Yep. So, yeah, we've got this graph here, this waveform display, which is mixed signal and it can

**Dave Jones:** decode protocols in real time, usually. Yep. And we have a maths graph, which you can scan the maths equation to. Yep. It's very complicated. Does that do serial decoding in the hardware? Yes, it does. It does. It does. Right. In the FPGA. In the FPGA.

**Dave Jones:** Excellent. So that means you can do triggering and stuff like that, which is what you want. Excellent. Okay. You have some signal information. We can do spectra. Yep. And lots of other things. Lots of other stuff. So the cleviscope is pretty clever. Moderately.

**Dave Jones:** All right. I think I love this stuff. Tell us about the history. Okay, the history. I'm an engineer. Engineers love scopes. Crows. I think you call them crows, don't they? Crow. Cathode ray. That's right. We call them that. Well, you see, the problem is that I wanted to make a crow like almost anyone else out

**Dave Jones:** there who wants to make a crow, and I noticed that the cell phone business that generated all these really fast analog-to-digital converters and FPGAs, those two together, magic. You've got a scope. That's what you have to do, don't you? Well, what else was I going to do?

**Dave Jones:** I made a scope. I designed my own scope back in 1993, got it published in Electronics Australia. It was extremely popular. Pretty good. Digital storage scope. You know, because back then you could design your own scope. It was worthwhile. You could, yeah, you could.

**Dave Jones:** Before the market was flooded with all the Chinese. Yeah, well, they've come along. That's right. So you started a business? Yeah. Just from home? Was it a side business at the time? Yeah, it was a side business, yeah. A side business? You had a real day job?

**Dave Jones:** I had a real day job, which was quite tough, and after a while I decided I've done enough in that now, you know. Ten years, whatever it was, I'm going to do a new thing. So this came along on the side. So how long did it take from when you started it to do a side business?

**Dave Jones:** How long did it take? About a year. About a year. Then you went full-time? Then we went full-time and got a few other guys, and now we're selling scopes all over the world. How many scopes have you sold, do you know? About 8,000.

**Dave Jones:** About 8,000? Yeah, something like that. Nice. Out of New Zealand? Out of New Zealand. New Zealand. Can you say six? Six. Six. So there's been several... There's been several generations, that's right. We had an earlier one, which was USB-1 based, and had an older FPGA.

**Dave Jones:** It was a bit slow and we couldn't fit enough stuff into it, so of course we had to make a new one. Right. And yeah, so we've got a new one coming after this, but it's not released yet, but it might get there eventually.

**Dave Jones:** Okay. So you've still only got the one... Have you got one model, or have you got several models? We really only have one model. You know, we make variations on it, but there's one model. Choice is too hard. It is. It's much too hard, yeah.

**Dave Jones:** There's just one, that's... Yeah. But the next one, that will have lots of variation. Okay. In detail? Yeah, well, digitally it's isolated channels. Isolated, okay. I don't know if that interests you at all. Yes, isolation is big between individual channels. Between individual channels.

**Dave Jones:** As well as the PC. Absolutely. So once you've got the individual channels, you don't need the... Or is the USB isolated as well? On here, the USB is not isolated. It's not isolated. And on the next one, the USB is also not isolated, because it's USB 3.

**Dave Jones:** Right. And USB 3 is even harder to isolate than USB 2. Are you running that at the full USB 3 throughput? Yes. What's the speed of it? Five gigabits per second. Five gigabits per second. It's going pretty fast. Nice. Yeah. So you've got that prototype?

**Dave Jones:** Yeah, yeah. We're getting, we're coming along. Right. So, but the isolation is aimed at people who want to make motor control drives and UPSs and power supplies and all that sort of stuff. How many channels is that going to be? Four. Four, yes.

**Dave Jones:** I was going to say, when you go isolated... Yeah, you need four. That's right. People typically want to monitor quite a few items. So that's awesome. Yeah. Is that going to be reasonably... Priced? Does it up the price? It does up the price a lot because you've then got to somehow isolate all that data

**Dave Jones:** and have a clock that gets its way around the place. Yeah, it ups the price. What's the sample? Sample rate of that? That will be, we're doing it in two versions. The lower version is 250 mega samples. Still pretty slow. 16 bits though.

**Dave Jones:** 16 bit converter. 16 bits. Fantastic. Keep going. And 25 kV per microsecond common mode noise. Yep. Which is right. And the other one is five gigabits per second based on that E2V converter. Right. Five. Excellent. But you've got the high that you're using the USB 3 to get the data throughput you need.

**Dave Jones:** Yes. So even though it's only a couple of meg samples, by a couple of hundred, it's only in the order of hundreds of meg samples. Yeah, we want USB 3 because we want to increase, we can currently stream at one and a half

**Dave Jones:** mega samples or three mega samples per second and we'd like to stream faster than that to hard disk. How fast can you possibly, how fast will you be able to stream in Pinkover? I have no idea. That's an experimental sort of thing, you know.

**Dave Jones:** Hard drives themselves have speed limits. Yeah, well because, and it won't be a consistent latency either, will it, with USB 3? No, no. Like Firewire gives you a consistent latency. Basically it's packetized and so as long as your average packet rate is suitable, you're

**Dave Jones:** okay. Keep up, right. Yeah, yeah, yeah. Do you think they should be stored into hard drives these days? Would you need a sold state? You would need a, if you want to go really fast, you will need one of them. You will. That's right, yes.

**Dave Jones:** I mean the one in my little laptop here, I think it can only handle about 40 megabytes per second. 40 megabytes per second. It's not that much really. Exactly. No. Oh, excellent. So we've got some interesting. We have got lots of interesting stuff coming.

**Dave Jones:** And how many people do you employ now? It's not large. Right, no. Exactly. I didn't mention that. It's sort of a six man company. Oh, that's decent size. Yeah, it's pretty good. Yeah. Doing well. And where's it made? Oh, it's made in Auckland.

**Dave Jones:** It's made in Auckland. Of course. New Zealand. New Zealand. But we'll claim it to be Australian because that's what we do. That's what you do. Russell Crowe. That's what we Australian do. Everything good that comes out of New Zealand we claim is Australian.

**Dave Jones:** Have over. So it's from Australia. Brilliant. Yeah. It's from Australia.
