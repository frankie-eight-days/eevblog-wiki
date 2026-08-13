---
video_id: -mavHYV-H6o
title: EEVblog #38 2of2 - Seismic Survey Boats & Relay Matrix Insulation Resistance Measurement
url: https://www.youtube.com/watch?v=-mavHYV-H6o
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 26, "2": 45, "3": 61, "4": 79, "5": 96, "6": 115, "7": 139, "8": 156, "9": 172, "10": 187, "11": 205, "12": 221, "13": 235, "14": 253, "15": 275}
---

**Dave Jones:** Now, what seismic survey cables are, they're used for oil exploration, and I used to work for a company that manufactures them, and what they basically are is they're called a streamer. They're about this diameter, about 60mm diameter, and they're about 100 or 150

**Dave Jones:** metres long. So you have to actually have a factory 100 or 150 metres long to manufacture and test these things. And what they do is they contain, it's basically like a 100 or 150 metre section, and it contains a whole bunch, like 100 or so, of these hydrophones.

**Dave Jones:** A hydrophone is just an underwater acoustic microphone. That's basically what it is. And it's just got a whole bunch of wiring inside, and it's got some fibre optics too in some of them, twisted pairs and power wires. And you join these 100 or 150 metre sections together

**Dave Jones:** like this, and you can form what's called a streamer up to 6 or 8 or even sometimes 10 kilometres in length. And they're towed behind a huge seismic survey vessel out in the middle of the ocean. And they actually float just below the surface, like 5 metres

**Dave Jones:** or such, just below the surface. And the boat actually has these acoustic sounders on it. They're basically big air guns that just go BAM! BAM! And they generate wideband acoustic noise into the water, which bounces off the ocean floor and through the rock strata

**Dave Jones:** in the ocean floor, and it returns. And all these thousands of hydrophones, there's literally thousands in these whole arrays, pick up the signal and then they use huge Cray supercomputers to measure the, to actually map what's under the ocean and find oil. And it's quite a complicated

**Dave Jones:** and expensive business. Now, it's worth talking quickly about the relay matrix, because as I said, this product needs to measure insulation resistance, high values, in the order of like 100 megohms or even more. In fact, 100 megohms was our spec, so it had to go that high.

**Dave Jones:** And this is where it comes in. This is where the relay matrix and the choice of those really high quality, best brand on the market, Reed Relays, was so important. Because if you look at the spec for them, they've got an insulation resistance, they might say it's 10 gig.

**Dave Jones:** And that sounds huge. Oh, it's 10 gig. Okay. But it's also 10 gig between the relay coils like this. This is a little thing, and it gives you a total of 6.6 gigs. And you might think, okay, that's still pretty high. That's huge.

**Dave Jones:** Not a problem. Uh-huh. But when you put it into a relay matrix like this, they're effectively in series, and you got, you might have 48 of them in series and parallel combination, and that'll give you a total value. It comes down to 250 meg.

**Dave Jones:** And you might think, okay, that's still not too bad. Yeah, but it varies with temperature, time, someone farting across the other side of the factory. It just varies all over the shop. It's terrible. It wanders over the space of minutes and seconds and

**Dave Jones:** things like that. It's pretty horrible. So to get around that, what you do is you have a fixed value resistor inside the box, which you can disable the matrix with some more relays. And it's a fixed 100 megohm resistor in this instance. And the IR meter takes a

**Dave Jones:** compensation measurement. It measures that 100 megohm resistance. And then it quickly switches in the matrix, and it measures the value. And from the parallel, it does it a few times to get some averages. And then the parallel value using standard parallel resistance formula gives you your result.

**Dave Jones:** And, but the errors are pretty horrible in systems like this. There's all sorts of things due to capacitive charging of 100 meter long cables. And, oh, it's pretty awful. But if you actually analyze the error, you'll get a graph like this, which quickly spirals into, you know, this is the percentage error.

**Dave Jones:** Okay. And yes, this is not a mistake. A thousand percent error. A hundred percent error when it gets to somewhere like a gig or 800 meg or something like that. The errors are just massive. And a lot of people, managers, for instance, couldn't really understand why our measurements were wandering all over

**Dave Jones:** the place. Well, we're measuring a 100 meter long antenna with these tiny little currents trying to measure 100 megohms. It was crazy. But in the end, it did the job. And, well, there you go. Interesting.
