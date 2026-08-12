---
video_id: sUG_sjS67K4
title: EEVblog #14 - An unusual oscilloscope phenomenon!
url: https://www.youtube.com/watch?v=sUG_sjS67K4
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 28, "3": 54, "4": 70, "5": 84, "6": 98, "7": 121, "8": 138, "9": 154, "10": 169, "11": 185, "12": 200, "13": 209, "14": 220, "15": 226, "16": 237, "17": 255, "18": 273, "19": 287, "20": 301, "21": 311, "22": 323, "23": 348, "24": 381, "25": 403, "26": 420, "27": 439, "28": 465, "29": 480, "30": 496, "31": 519, "32": 537, "33": 561, "34": 581, "35": 591}
---

**Dave Jones:** EEVblog, I'm your host, Dave Jones, and this is episode number 14. First up, I've got a rather interesting phenomenon I bet you haven't seen before. It's quite unusual and involves an oscilloscope again.

**Dave Jones:** We had an oscilloscope special last week, so I thought I'd show you a really interesting phenomenon. Now, what you need is an oscilloscope, digital storage oscilloscope, 100 MHz bandwidth, the higher the better, but you can do it using a 100 MHz bandwidth scope.

**Dave Jones:** So, I've got a TDS 220. You need a standard times 10 crow pro and short the input just like that. And set your scope up to single shot capture, 10 nanoseconds per division, and maybe 1 V um per division vertical.

**Dave Jones:** But, you can go a bit lower than that if you can't get the phenomenon as easily as I'm about to show you. I'll explain it all later. So, I'm going to put the oscilloscope down here on the bench and I'll show you a close-up of it later.

**Dave Jones:** And put the probe on the bench. Remember, the probe is still shorted. Okay? Probe is completely shorted. It's going to sit on the bench. I'm going to set it to trigger at about the 1 V level.

**Dave Jones:** And let's go run. And what I'm going to do since it's about to trigger, I'll show you the waveform in a minute. And I'm just going to stand up like that and bingo, we've captured something.

**Dave Jones:** And check out whoops, that was a screwdriver falling on the ground. Check out what we've captured. Isn't that cool? That's 1 V per division. Right? And that is a very nice sinusoidal type uh impulse with a very sinusoidal, as you can see, at about 100 MHz.

**Dave Jones:** It's a beautiful, um burst It's a beautiful sinusoidal burst. And there you go. Check it out. Isn't it groovy? I'll explain how you actually get this and what's actually happening here.

**Dave Jones:** Now, I know what you're thinking. This must be some kind of trick, right? I'm trying to you. I can guarantee you I'm not. You can do this exact same thing at home and get the exact same response I did or similar to what I did by simply standing up off a chair.

**Dave Jones:** And you can do it using a shorted crowbar, right? This is a crowbar, a proper, you know, a good quality crowbar that is shorted. And, um, so therefore, you shouldn't be able to get any input at all to your oscilloscope, right?

**Dave Jones:** That's what you'd think. And all I did was stand up off the chair. Can you figure out what's happening? I'll tell you in a sec. Now, before I tell you what's actually happening here, I'll give you a background story about how I actually found this phenomenon.

**Dave Jones:** And, uh, I was also, um, work I was, uh, debugging a, um, complex digital design. This was quite a few years ago. And I was, um, I had my scope, um, set up.

**Dave Jones:** The, uh, the complex circuit I was working on, it was, um, it was actually, uh, it was getting glitches every couple of days and it was crashing and doing all sorts of weird things.

**Dave Jones:** So, I set up this oscilloscope, uh, to actually monitor the, uh, digital signal, some clocks and other things. And, um I would sit there and wait for it to trigger.

**Dave Jones:** I'd set the trigger to about, you know, a volt or a volt and a half or 2 V, you know, sort of center scale on a, uh, 3.3 V digital signal.

**Dave Jones:** And I was getting all these little glitch captures every now and then. I was capturing all these little glitches and I thought, "Aha, I found you know, I found it and I found a problem.

**Dave Jones:** I'm getting these glitches on a digital rail." And I'd zoom in and what I was actually seeing was, you know, like this. It was a sinusoidal type burst at, you know, roughly 100 MHz or thereabouts.

**Dave Jones:** And it was it's got the classic tank circuit type shape to it. So, I thought, "Aha, there's some sort of, you know, weird ground capacitive tank circuit thing happening in my design somewhere.

**Dave Jones:** Something's it's getting a burst of energy and it's oscillating or it's some DC-to-DC converter in there playing up pumping energy into a weird ground capacitive configuration or something like that." And well, no.

**Dave Jones:** After some investigation, it turned out there was nothing wrong with the circuit at all. It was actually the oscilloscope and the crowbar and and that that was actually at fault.

**Dave Jones:** And I proved this by doing exactly what I did just here. I shorted out my crowbar. I couldn't believe what I was what was happening in the circuit. So, I shorted just as a sanity check.

**Dave Jones:** Shorted out my crowbar and sure enough, I could reproduce this and it wasn't connected to my circuit at all. So, I knew there was nothing wrong. And there's actually something very interesting happening here.

**Dave Jones:** Now, there are two things that make this phenomenon possible. What Well, three things actually. One is the inductance of a coax cable used in oscilloscope probes like this and the input capacitance of the oscilloscope and um, what that does, that forms an LC tank circuit.

**Dave Jones:** And the key to, uh, what's happening here, though, is when I stand up from the chair, I'm generating static electricity. Broadband energy, which is a static electricity, uh, is a bunch of broadband energy, which is picked up by the coax cable, and it, uh, resonates the input to the oscilloscope based on the inductance of the cable and the input capacitance of the oscilloscope and a few other factors, distributed

**Dave Jones:** capacitance and, you know, all sorts of other stuff, but it basically forms an LC tank circuit, and that's why you get a response that's perfectly sinusoidal like that, because the broadband energy being injected into the cable, it resonates at the frequency of that LC circuit.

**Dave Jones:** Right, so I'll just do a quick illustration of what's actually happening here. Now, your crow probe is actually a 9 meg resistor in parallel with a small cap, and then you've got your cable, okay?

**Dave Jones:** This is your coax cable, which is actually inductive. So, we can represent an inductor in there, and you've got the input to your oscilloscope, which is capacitive and also 1 meg as well, and that's ground.

**Dave Jones:** And then if you This is the probe tip. If you ground that as well, okay? Your system's all, uh, grounded. It's closed loop, but when you inject broadband energy via static electricity into the coax cable, the whole system resonates and you get out your sinusoidal energy pulse like that.

**Dave Jones:** And that's exactly what you see on the oscilloscope. It's not magic. It's It's It isn't a trick. It's just a phenomenon of uh LC tank circuits formed by the very low um inductance of the scope probe.

**Dave Jones:** And if you actually do the um calculations, uh you know, the um resonant um formula is 1 over 2 pi square root LC, and that's um generate and that's your formula for your uh resonant tank circuit.

**Dave Jones:** And um there's there's quite a few complex factors involved in here, but if you do some just basic back-of-the-envelope calculations, it turns out that sure enough, based on the inductance of a typical uh coax cable and input capacitance of a scope, it's um pretty much always going to resonate at around about the 100, you know, 120 MHz mark or thereabouts.

**Dave Jones:** And you can do this on practically any scope and any probe, and you'll pretty much get a very similar result. Now, you can also get this uh phenomenon to happen on a uh times one uh probe as well, and also just a regular uh coax cable, too, if you're lucky.

**Dave Jones:** And um yeah, it it really doesn't discriminate too much. So, what's the moral of this neat little phenomenon? Well, it's uh really you should be careful when you're uh probing stuff because you can actually get um glitches in your uh coax input that has nothing to do with your circuit, and it looks like uh you can have something wrong with your circuit.

**Dave Jones:** So, just be careful when you're actually probing this. Now, I've actually had this uh phenomenon happen with me in a full lab coat um with a, you know, ESD uh bench as well, but still somehow the static gets through and it impulses into the probe and we are talking very low signal levels here.

**Dave Jones:** We're talking, you know, volts in some cases. So, I hope you learned something new there. That's definitely something you'll never learn in school. And just in case you're wondering, I actually got that to work on the very first take.

**Dave Jones:** I didn't have to refill it. It's easy. Try it yourself. Go have fun.
