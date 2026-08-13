---
video_id: P8s3Xjeg0sk
title: EEVblog #55 - RCA Airnergy WiFi Charging Free Energy Harvesting Marketing BS
url: https://www.youtube.com/watch?v=P8s3Xjeg0sk
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 21, "2": 37, "3": 65, "4": 87, "5": 107, "6": 126, "7": 143, "8": 157, "9": 182, "10": 208, "11": 231, "12": 257, "13": 281, "14": 300, "15": 312, "16": 345, "17": 368, "18": 401, "19": 417, "20": 436, "21": 452, "22": 471, "23": 490, "24": 508, "25": 530, "26": 549, "27": 570, "28": 587, "29": 604, "30": 623, "31": 641, "32": 657}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, there's been a lot of talk recently about a product that RCA have demoed at the recent CES Consumer Electronics Show and

**Dave Jones:** what it is, it's called the Energy, as in A-I-R, Energy, Energy, as in it gets energy from the air, get it? Marketing, yeah, good one, alright, but here's a photo of it and I'll also post a link to a YouTube video of people on the stand, of the RCA stand at the show, talking about it.

**Dave Jones:** And it's to do, it's just an energy harvesting device and energy harvesting is all the rage in the last couple of years. Everyone's talking about it, you can get chips to harness all sorts of, you know, residual energy that's out there, light, motion, vibration and electro, maybe waves and all sorts

**Dave Jones:** of things, right? So this one is designed to capture energy from Wi-Fi, 2.4 gigahertz Wi-Fi signals, which are all around us, pretty much, and charge an internal lithium-ion battery that then can be, in turn, plugged into your mobile phone and charge your mobile phone up quickly.

**Dave Jones:** It sounds terrific, it sounds like the greatest thing since sliced bread and RCA reckon they've come up with some fantastic new technology that can make it work. Well, I smell bullshit! Yeah, bullshit. Now there's a YouTube video of some guy on the RCA stand claiming that they

**Dave Jones:** charged a BlackBerry phone from 30% to full in around 90 minutes and, of course, all the geeks, they all went apeshit. They think this is fantastic, this is going to be the greatest thing since sliced bread, if it works. But really, it's obvious that that's just not

**Dave Jones:** possible. That charge rate is coming from the internal lithium-ion battery. It assumes that that battery is already full and you plug that full battery from this energy device into your phone and it'll charge it. I'm sure it will charge it in that time, there's no problem at all,

**Dave Jones:** nothing special about that. You can get a couple of AA batteries, stick them in a box and have a little 5-volt generator and charge your phone. Nothing new there, but I thought I'd do some calculations and see just how much bullshit this actually is.

**Dave Jones:** Okay, here we go. Let's do some back-of-the-envelope calculations, real rough stuff, to see, to sort this out, is it bullshit or not? Here we go. Let's say that we have a home Wi-Fi router, okay, here it is, it's a little antenna and a typical output power of a Wi-Fi router is 0.1 watts or 100 milliwatts, okay,

**Dave Jones:** there it is there. Now, let's be pretty generous and say that our little energy receiver is going to be one meter away, okay. Now, if you know your basic math, the area, now let's assume that this antenna is a perfect ideal, what's called an isotropic, okay, isotropic antenna, all right,

**Dave Jones:** that means that the energy is pretty much evenly spread out around a perfect sphere, okay, real antennas aren't like that, but let's be generous, okay, and let's say that, you know, just for rough measurements, that that's what it is, a sphere. Now, the area of a sphere is 4 pi r squared, okay,

**Dave Jones:** now in this case the radius, we're one meter away, okay, so it's 4 pi 1 squared and that equals 12.6 square meters, okay, that's the surface area of our sphere, simple. Now, let's work out the energy density at that sphere, okay, if we've got 0.1 watts, okay, divided by 12.6

**Dave Jones:** square meters, okay, we're looking at a figure of 8 milliwatts per square meter, all right, and that's the energy density in that field at one meter away, simple. Now, you can see where this is headed, it's already starting to smell like bullshit, look, 8 milliwatts we're talking about per square

**Dave Jones:** meter at one, at a pretty, you know, a pretty decent one meter away from it, that's very generous, but let's keep going, shall we? Now, let's assume that this is our little energy device here, and let's say it's 10 centimeters by 10 centimeters, that's the capture, effective capture area of the

**Dave Jones:** antenna, you know, it doesn't matter what the actual figure is, but, you know, it's going to be around about that order, okay, so that's 0.01 square meters, we've got 8 milliwatts, and if it's one meter away, we've got 8 milliwatts per square meter, so what's that?

**Dave Jones:** Well, it's 8 milliwatts per square meter times 0.01, bingo, 0.08 milliwatts, whoop, milliwatts, and that's what we get, 0.08, it's like 80 microwatts, that's what we're going to get in that antenna, it's just crap, 80 microwatts, but I know what you're thinking, right, this thing's designed to sit there for a long time

**Dave Jones:** and charge up, well, let's see how much charge we need, let's take my Nokia E71 battery as a typical example, this is a pretty high capacity one, but we use it, okay, this has a capacity of 5.6 watt hours, now let's see what it takes, okay, 5.6 watt hours, okay, now let's divide that by

**Dave Jones:** 0.08 milliwatts, okay, 0.08 milliwatts, okay, that, to charge a 5.6 watt hour battery at 0.08 milliwatts is going to take roughly 70,000, 70,000 hours, that's 8 years, you've got to be kidding me, 8 years, see, it's absolute and utter bullshit, this thing's just not going to work, yeah, I know

**Dave Jones:** what you're thinking, you know, I haven't done this, I haven't taken this into account, and that, and antenna radiation patterns, and things, and the receiver, and the antenna's sensitivity and gain, and all sorts of crap, it doesn't matter, these are ballpark figures that are going to remain

**Dave Jones:** pretty much constant regardless of how you fiddle with the rest of it, it's, you know, it's just not going to work, okay, so, you know, people will claim that, oh, okay, that's just one Wi-Fi router, what if you've got 10 of them, you know, if you're in a building, there's 10 Wi-Fi routers around,

**Dave Jones:** well, go through the math again, and you're not going to be a metre away from the damn thing, you're going to be 10, 20 metres away from it, or something like that, or more, 50, 100 metres away, it's just, it doesn't matter how many you've got, it's not going to work, and it doesn't matter what

**Dave Jones:** type of antenna RCA, what type of technology in the antenna design RCA have got in this thing, because some whiz-bang fractal antenna manufactured by nude virgins in the marketing department, well, it doesn't matter, it's still not going to work, it's bullshit, I'm calling it out,

**Dave Jones:** the energy device, the RCA energy device is marketing bullshit, you simply can't beat the inverse square law, which says that the power drops as a square of the distance, so, if you double the distance, your power from the antenna, your power drops by four times, and, well, you're

**Dave Jones:** seeing the results at just a metre, it's hopeless, god, and of course, I'm not taking into account, you know, losses in the battery, and conversion, and all sorts of, all sorts of things, you know, loss over capacity, loss over time, and god knows what, there's so many things that go into this,

**Dave Jones:** and it just, it just doesn't add up, there is no way that you're going to harness enough energy from usable Wi-Fi signals to charge that internal battery in the energy device, so that you can charge, you know, a two, three, or four, five watt hour mobile phone battery, it's just, it's just not

**Dave Jones:** going to happen, and I bet you they end up supplying it with a plug pack too, just in case there's not enough Wi-Fi energy in your particular area, you know, just in case you might have to plug it into the PowerPoint, and actually charge it up, and that'll take a few hours, and, well, isn't that just

**Dave Jones:** easier to do that, oh, it's useless, it's a complete and utter gimmick, but geeks will buy it, because it's got a cool name, and it looks funky, so how can they get away with releasing a product like this, or even proposing a product like this, that clearly just is a gimmick, it doesn't work, well, it not only

**Dave Jones:** doesn't come down to marketing, but it comes down to future funding as well, because as you see in the clips, they're also trying to market a little, a little battery version of it too, that is integrated into a mobile phone battery, and to get funding to do something like that, they have to

**Dave Jones:** produce this energy device, and, and sell it, and market it, and hype it up, and sell it, just so that they can get the extra funding for doing something else, and of course, RCA, they're, you know, you might think they're a big, you know, huge corporation, big reputation, been around a long time, no, they're,

**Dave Jones:** they're just a, it's just a shell name now, it has been for a long time, they're just a, you know, who knows who's actually behind this, when slapping the RCA name on it, to give it some credibility, and the thing is, the engineers, they will design this thing, okay, they design this energy device,

**Dave Jones:** and they will write a report for it, and it says, oh, you know, even under best ideal case conditions, it might take 50 or 100 days to, to charge, you know, and the marketing department and managers, they look at that, and they go, oh, that can't be right, well, what happens if you only want to

**Dave Jones:** get down to say, if you only want to charge a battery 10%, that'll help, won't it, so bingo, and they focus on that one figure, they might focus on that 10% instead of whether or not the product is actually overall useful, and the engineers, well, you know, they just want to keep

**Dave Jones:** their job, so they mumble and agree, and go, oh, yeah, kinda, you know, and then they'll, you know, walk away with their deal, but ties up back to their cubicle, and, and well, it's, you know, that's how big companies operate, what can you do?
