---
video_id: sUG_sjS67K4
title: EEVblog #14 - An unusual oscilloscope phenomenon!
url: https://www.youtube.com/watch?v=sUG_sjS67K4
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 32, "3": 56, "4": 70, "5": 87, "6": 102, "7": 125, "8": 142, "9": 156, "10": 174, "11": 188, "12": 204, "13": 216, "14": 226, "15": 238, "16": 258, "17": 280, "18": 298, "19": 311, "20": 328, "21": 355, "22": 374, "23": 389, "24": 410, "25": 432, "26": 453, "27": 477, "28": 496, "29": 512, "30": 526, "31": 541, "32": 557, "33": 570, "34": 585}
---

**Dave Jones:** EEVblog, I'm your host, Dave Jones, and this is episode number 14. First up, I've got a rather interesting phenomenon I bet you haven't seen before. It's quite unusual and involves an oscilloscope again. We had an oscilloscope special last week, so

**Dave Jones:** I thought I'd show you a really interesting phenomenon. Now, what you need is an oscilloscope, digital storage oscilloscope, 100 MHz bandwidth, the higher the better, but you can do it using a 100 MHz bandwidth scope. So, I've got a TDS 220.

**Dave Jones:** You need a standard times 10 crow pro and short the input just like that. And set your scope up to single shot capture, 10 nanoseconds per division, and maybe 1 V um per division vertical. But, you can go a bit lower than that if

**Dave Jones:** you can't get the phenomenon as easily as I'm about to show you. I'll explain it all later. So, I'm going to put the oscilloscope down here on the bench and I'll show you a close-up of it later.

**Dave Jones:** And put the probe on the bench. Remember, the probe is still shorted. Okay? Probe is completely shorted. It's going to sit on the bench. I'm going to set it to trigger at about the 1 V level. And let's go run.

**Dave Jones:** And what I'm going to do since it's about to trigger, I'll show you the waveform in a minute. And I'm just going to stand up like that and bingo, we've captured something. And check out whoops, that was a screwdriver falling

**Dave Jones:** on the ground. Check out what we've captured. Isn't that cool? That's 1 V per division. Right? And that is a very nice sinusoidal type uh impulse with a very sinusoidal, as you can see, at about 100 MHz. It's a beautiful, um

**Dave Jones:** burst It's a beautiful sinusoidal burst. And there you go. Check it out. Isn't it groovy? I'll explain how you actually get this and what's actually happening here. Now, I know what you're thinking. This must be some kind of trick, right? I'm

**Dave Jones:** trying to you. I can guarantee you I'm not. You can do this exact same thing at home and get the exact same response I did or similar to what I did by simply standing up off a chair. And you can do it using a

**Dave Jones:** shorted crowbar, right? This is a crowbar, a proper, you know, a good quality crowbar that is shorted. And, um, so therefore, you shouldn't be able to get any input at all to your oscilloscope, right? That's what you'd think. And all I did was stand up off

**Dave Jones:** the chair. Can you figure out what's happening? I'll tell you in a sec. Now, before I tell you what's actually happening here, I'll give you a background story about how I actually found this phenomenon. And, uh, I was

**Dave Jones:** also, um, work I was, uh, debugging a, um, complex digital design. This was quite a few years ago. And I was, um, I had my scope, um, set up. The, uh, the complex circuit I was working on, it

**Dave Jones:** was, um, it was actually, uh, it was getting glitches every couple of days and it was crashing and doing all sorts of weird things. So, I set up this oscilloscope, uh, to actually monitor the, uh, digital signal, some clocks and

**Dave Jones:** other things. And, um I would sit there and wait for it to trigger. I'd set the trigger to about, you know, a volt or a volt and a half or 2 V, you know, sort of center scale on

**Dave Jones:** a, uh, 3.3 V digital signal. And I was getting all these little glitch captures every now and then. I was capturing all these little glitches and I thought, "Aha, I found you know, I found it and I found a problem. I'm getting these

**Dave Jones:** glitches on a digital rail." And I'd zoom in and what I was actually seeing was, you know, like this. It was a sinusoidal type burst at, you know, roughly 100 MHz or thereabouts. And it was it's got the

**Dave Jones:** classic tank circuit type shape to it. So, I thought, "Aha, there's some sort of, you know, weird ground capacitive tank circuit thing happening in my design somewhere. Something's it's getting a burst of energy and it's oscillating or it's some DC-to-DC

**Dave Jones:** converter in there playing up pumping energy into a weird ground capacitive configuration or something like that." And well, no. After some investigation, it turned out there was nothing wrong with the circuit at all. It was actually the oscilloscope and the

**Dave Jones:** crowbar and and that that was actually at fault. And I proved this by doing exactly what I did just here. I shorted out my crowbar. I couldn't believe what I was what was happening in the circuit. So, I shorted just as a sanity check.

**Dave Jones:** Shorted out my crowbar and sure enough, I could reproduce this and it wasn't connected to my circuit at all. So, I knew there was nothing wrong. And there's actually something very interesting happening here. Now, there are two things that make this phenomenon

**Dave Jones:** possible. What Well, three things actually. One is the inductance of a coax cable used in oscilloscope probes like this and the input capacitance of the oscilloscope and um, what that does, that forms an LC tank circuit. And the key to, uh, what's happening here,

**Dave Jones:** though, is when I stand up from the chair, I'm generating static electricity. Broadband energy, which is a static electricity, uh, is a bunch of broadband energy, which is picked up by the coax cable, and it, uh, resonates the input to the oscilloscope based on

**Dave Jones:** the inductance of the cable and the input capacitance of the oscilloscope and a few other factors, distributed capacitance and, you know, all sorts of other stuff, but it basically forms an LC tank circuit, and that's why you get

**Dave Jones:** a response that's perfectly sinusoidal like that, because the broadband energy being injected into the cable, it resonates at the frequency of that LC circuit. Right, so I'll just do a quick illustration of what's actually happening here. Now, your crow probe is

**Dave Jones:** actually a 9 meg resistor in parallel with a small cap, and then you've got your cable, okay? This is your coax cable, which is actually inductive. So, we can represent an inductor in there, and you've got the input to your oscilloscope, which is

**Dave Jones:** capacitive and also 1 meg as well, and that's ground. And then if you This is the probe tip. If you ground that as well, okay? Your system's all, uh, grounded. It's closed loop, but when you inject broadband energy via static electricity

**Dave Jones:** into the coax cable, the whole system resonates and you get out your sinusoidal energy pulse like that. And that's exactly what you see on the oscilloscope. It's not magic. It's It's It isn't a trick. It's just a phenomenon of uh LC tank circuits formed

**Dave Jones:** by the very low um inductance of the scope probe. And if you actually do the um calculations, uh you know, the um resonant um formula is 1 over 2 pi square root LC, and that's um generate and that's your formula for your uh

**Dave Jones:** resonant tank circuit. And um there's there's quite a few complex factors involved in here, but if you do some just basic back-of-the-envelope calculations, it turns out that sure enough, based on the inductance of a typical uh coax cable and input

**Dave Jones:** capacitance of a scope, it's um pretty much always going to resonate at around about the 100, you know, 120 MHz mark or thereabouts. And you can do this on practically any scope and any probe, and you'll pretty much get a very similar

**Dave Jones:** result. Now, you can also get this uh phenomenon to happen on a uh times one uh probe as well, and also just a regular uh coax cable, too, if you're lucky. And um yeah, it it really doesn't discriminate too much.

**Dave Jones:** So, what's the moral of this neat little phenomenon? Well, it's uh really you should be careful when you're uh probing stuff because you can actually get um glitches in your uh coax input that has nothing to do with

**Dave Jones:** your circuit, and it looks like uh you can have something wrong with your circuit. So, just be careful when you're actually probing this. Now, I've actually had this uh phenomenon happen with me in a full lab coat um with a,

**Dave Jones:** you know, ESD uh bench as well, but still somehow the static gets through and it impulses into the probe and we are talking very low signal levels here. We're talking, you know, volts in some cases. So, I hope you learned something

**Dave Jones:** new there. That's definitely something you'll never learn in school. And just in case you're wondering, I actually got that to work on the very first take. I didn't have to refill it. It's easy. Try it yourself. Go have fun.
