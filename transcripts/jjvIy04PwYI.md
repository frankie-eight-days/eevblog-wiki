---
video_id: jjvIy04PwYI
title: EEVblog #286 - Orders Of Magnitude
url: https://www.youtube.com/watch?v=jjvIy04PwYI
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 28, "3": 41, "4": 54, "5": 70, "6": 87, "7": 101, "8": 113, "9": 129, "10": 139, "11": 158, "12": 176, "13": 189, "14": 197, "15": 210, "16": 227, "17": 238, "18": 252, "19": 260, "20": 272, "21": 282, "22": 295, "23": 309, "24": 329, "25": 339, "26": 353, "27": 367, "28": 383, "29": 394, "30": 406, "31": 419, "32": 438, "33": 448, "34": 466, "35": 480, "36": 493, "37": 511, "38": 529, "39": 544, "40": 567, "41": 581, "42": 597, "43": 616, "44": 626, "45": 637, "46": 646, "47": 656, "48": 672, "49": 688, "50": 702, "51": 719, "52": 732, "53": 743, "54": 758, "55": 767, "56": 780, "57": 792, "58": 809, "59": 820, "60": 837, "61": 851, "62": 870, "63": 886, "64": 906, "65": 920, "66": 934, "67": 949}
---

**Dave Jones:** Hi, it's engineering terminology time. We're going to talk about orders of magnitude. And you hear me say it all the time, not just me, but it's a very common term in electronics and other engineering and science for that matter.

**Dave Jones:** Order of magnitude, what exactly what does it mean? You'll hear me use it in terms of ah, I was out by an order of magnitude or that was an order of magnitude bigger than I thought or it's dropped something's dropped by an order of magnitude something like that.

**Dave Jones:** What does it mean? It's pretty simple concept and it's easy to learn and easy to use incredibly easy in fact, but a lot of people don't really understand it or get it a little bit wrong.

**Dave Jones:** So, let's take a look at orders of magnitude. And here's a basic table you're going to be familiar with. What is an order of magnitude? An order of magnitude is just 10 times something.

**Dave Jones:** That's it. That's the entire concept. It's incredibly simple. And here's how it relates to numbers, decades, and the order of magnitude in increasing and decreasing value. So, what we've got here in the blue is the order of magnitude.

**Dave Jones:** So, this is one order of magnitude, two orders of magnitude, six orders of magnitude, and they've got something I've put down minus one order of magnitude, but in engineering nobody it's not very often used we say minus three orders of magnitude or something like that.

**Dave Jones:** Some people may, I personally don't do it. I'll say it's dropped by or it's down by three orders of magnitude. So, what does that mean? Well, if you're talking about the number one as your reference point, remember your reference point doesn't have to be one.

**Dave Jones:** Can be anything. Your reference point can be a thousand volts. And if it's an order of magnitude greater than your reference voltage of a thousand volts, then it's going to be ten thousand volts.

**Dave Jones:** One order is just ten times. So, even though I've used one as the reference point, it doesn't have to be, okay? So, it's simple. You know about decades in um uh engineering and uh scientific notation.

**Dave Jones:** And uh it's basically 10 ^ 1 is 10, 10 ^ 2 is 100, and so on up to a million, and it can go any as far as you like in any direction.

**Dave Jones:** So, these are common terminology to say something is you know, it's uh I've I'm an order of magnitude out, for example. I'll say that commonly in my videos. And that could mean if I'm out by an order of magnitude, it means I'm out by 10 times.

**Dave Jones:** If I say I'm out by three orders of magnitude, I'm out by 1,000 times in either direction, because I didn't actually say which direction I was out by. So, I'll you might use the common terminology something the voltage has dropped by an order of magnitude.

**Dave Jones:** It's dropped from 1 volt to 0.1 volts. And that's an order of magnitude. Or it's increased by 1 volt has increased by an order of magnitude. It's jump jumped from 1 volt up to 10 volts.

**Dave Jones:** Pretty simple. So, these are common terminologies you'll find in engineering. And just to be clear, when I say that reference point can be anything, it doesn't have to be a power of 10.

**Dave Jones:** I talked in terms of 1,000 volts and 1 volt, but it could easily be say 3.5 volts or something like that. And if something if 3.5 volts has increased by an order of magnitude, it's going to be roughly 35 volts.

**Dave Jones:** And that's the other thing, the big thing about orders of magnitude. It's a rough rule of thumb in engineering. It doesn't have to be exact. When you talk in terms of order of magnitude, you're talking about roughly, very roughly.

**Dave Jones:** To be oh, it's a couple of orders of magnitude bigger, or it's an order of magnitude bigger or it's an order of magnitude dropped by an order of magnitude dropped by roughly 10 times.

**Dave Jones:** Doesn't have to be exactly 10 times. It might be 11, 12, or something like that. And you can round up either way. But that's one of the advantages of talking in terms of order of magnitude.

**Dave Jones:** It's just a rough rule of thumb that gives you an indication that you're in the ballpark. And often a lot of practical electronics engineering, you just want to be in the ballpark.

**Dave Jones:** I want to choose a 1K resistor. That's, you know, it's going to be correct to the right order. That's another term. To the right order just means you're roughly within the ballpark.

**Dave Jones:** And that leads us to one of the big misconceptions and a thing which people get wrong with order of magnitude. Everyone knows that an order of magnitude is 10 times.

**Dave Jones:** That's basic. But some people have the incorrect assumption that two orders of magnitude is 20 times. And it's not. It is 100 times. It goes up by that decade each time.

**Dave Jones:** 10 to the power of. So don't make the mistake of thinking that two orders of magnitude is 20. It's not. It's 100. And there are some people who try and talk in terms of 1 and 1/2 orders of magnitude.

**Dave Jones:** And probably not technically incorrect, but it's not within the spirit of the order of magnitude. That rough rule of thumb in the ballpark kind of thing. So yeah, I wouldn't make the mistake of going, you know, try to make it more precise than what it actually is.

**Dave Jones:** So if your 1 volt has jumped up to 8 volts, don't say it's increased by 0.8 orders of magnitude. It hasn't. It's 1 order of magnitude. Round it up.

**Dave Jones:** Now let's take a look at engineering notation that we're familiar with in electronics. Powers of three, multiples of three. You're familiar with these. Kilo, mega, giga, tera, milli, micro, nano, pico in the negative direction.

**Dave Jones:** And it extends beyond that, but that's pretty much probably from giga down to pico, uh plus nine minus 12 orders of magnitude is the range you're typically going to encounter in electronics engineering.

**Dave Jones:** If you're working outside of that, you're working on some pretty extreme stuff. Now, let's take let's think about what these orders of magnitude mean. I mean, we can certainly measure down in the nano volt region and generate things down in pico amps and stuff like that.

**Dave Jones:** So, and we're able to get and generate, you know, there's like well, there's gigaohms and, you know, we're able to measure and work with these values practically. So, what does this entire range mean?

**Dave Jones:** If you're working from minus 12 pico, if that's your reference, so let's say you've got one pico volt, for example, that's your reference. How high is tera up here?

**Dave Jones:** It's 24 orders of magnitude greater than your one pico volt reference. So, that's what the typical engineering spectrum is going to involve, 24 orders of magnitude. Doesn't sound very impressive, right?

**Dave Jones:** 24, you know, it's a pretty low sort of number, but it's two It's sorry, it's 10 to the power of 24. And to give you a scale of how massive this range is that electronics engineers work over on a daily basis.

**Dave Jones:** So, let's use the example of how far Jupiter is from the sun. I'm always saying you can fly to Jupiter on a milliamp, right? So, let's actually see how far Jupiter is from the sun.

**Dave Jones:** If we take our reference point as 1 mm. That's 1/25 of an inch, roughly, for you uh Yanks out there. Now, Jupiter is roughly um is roughly uh 1 billion kilometers from the sun.

**Dave Jones:** Roughly. Why? Because we're talking orders of magnitude. It's actually around about 800 just over 800 uh million kilometers from the sun at its maximum um distance, but we're talking orders, so we round things.

**Dave Jones:** So, it's a billion kilometers from the sun. Well, what's that in meters? Well, it's a thousand billion and a millimeter it's a another thousand again. What's that in orders of magnitude?

**Dave Jones:** Count the zeros. 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15. It's only 15 orders of magnitude. From a millimeter uh uh a millimeter to the uh freaking Jupiter is only 15 orders of magnitude.

**Dave Jones:** Engineering works over 24 orders. Wow. How about Proxima Centauri, the nearest star to the sun? Approximately 4.2 light years. Well, what's one light year compared to our 1 millimeter reference?

**Dave Jones:** It's 10 to the power of 19. 19 orders of magnitude. Not there yet. Turns out we've got to go to the Andromeda galaxy at 2.5 million light years from the sun, which is roughly 10 to the power of 25 or 25 orders of magnitude.

**Dave Jones:** So, if in millimeters, the 1 millimeter reference. So, let's take it as a 10 millimeter reference, 1 centimeter. Bingo, you've got your 24 orders of magnitude. Incredible. That's how wide this sort of range is that engineers work over a daily basis.

**Dave Jones:** It's incredible when you think about it. The Andromeda galaxy, for goodness sake. And here's a practical example of some equipment I've got on my bench here. I've got a Keithley 260 nanovolt source and a 240A high voltage power supply.

**Dave Jones:** And with these two instruments here, I can generate a voltage anywhere from 0.01 nanovolt or 10 picovolts, 10 to the power of minus 11, to 1,000 volts, 10 to the power of three.

**Dave Jones:** And that's 14 orders of magnitude. Incredible. And one order of magnitude is important in electronics for lots of rules of thumb reason, measurement uncertainties, and things like that. Let's take an example of a multimeter measuring a resistor divider here.

**Dave Jones:** We've got two resistors here. One is a fixed 1 meg resistor, which we're measuring across with our digital multimeter. And as you should know, a digital multimeter doesn't have an infinite input impedance.

**Dave Jones:** It's going to be roughly 10 megaohms or thereabouts. Most of them are anyway. Now, when you put 10 megaohms across that 1 meg resistor, that's going to cause a measurement error.

**Dave Jones:** How much? Well, in this particular case, it depends on what value of R1 is. If R1's 100k, you're going to get roughly a 1% error caused by a multimeter.

**Dave Jones:** If it's a half If it's a half rail divider like this with a half volt in the middle and R1 is 1 meg here, you're going to get about a 5% error.

**Dave Jones:** And if it's much bigger and you're measuring a smaller voltage down here, you're going to get about a 9% error or thereabouts. And roughly, you're getting an order of magnitude error, worst case, due to that 10 meg resistor.

**Dave Jones:** And in a lot of cases, that's going to get you in the ballpark. It's good enough if you choose a value for measurement or something like that, you know, like a 1% error, for example, is not, you know, it's not a huge deal in most practical circuits.

**Dave Jones:** So, that's why you deal with just one order of magnitude. When you're talking about say measurement like this, you want a multimeter to at least be an order of magnitude above what you're trying to measure.

**Dave Jones:** Otherwise, you'll disturb it and your error will be too great. Now, a practical example in electronics where you're going to use this one order of magnitude rule of thumb is in a basic LED circuit like this where you don't have to do any You don't have to get your calculator out and actually do calculations and things like that.

**Dave Jones:** You can just choose a resistor that's going to work without having to do any You don't have to get into the nitty-gritty of the calculations cuz you're using rule of thumb, back of the envelope calculations.

**Dave Jones:** Now, let's take the example of We've got a 10-V power supply here and we've got a red LED. It's going to drop roughly 1.8 V or thereabouts over its uh, you know, over its current range.

**Dave Jones:** So, 1.8 V is roughly an order of magnitude lower than 10 V. So, as is common in electronics, if it's an order of magnitude lower or an order of magnitude higher, you can safely take it out of the equation.

**Dave Jones:** So, we're going to not worry about the voltage drop of that LED because it's an order of magnitude out. So, we're going to say 10 V divided by the resistance gives us the current.

**Dave Jones:** And we know that an LED is going to, you know, at least turn on anywhere from 1 mA up to, say, 20 mA maximum. Or let's go 10 mA like that without blowing the LED, just a bog-standard LED.

**Dave Jones:** So, what do we do that? We can calculate the values. 1 10 V divided by 10 mA gives us 1 K, and 10 V divided by 1 mA gives us 10 K.

**Dave Jones:** So, any value within that range is going to be of the right order. So, you can safely go to your parts bin and pick out a resistor anywhere within that range and you know you're going to get that LED to light up.

**Dave Jones:** And that's just a common example of how rough, you know, rough rules of thumb and order of magnitude calculations work in electronics. You're going to get this circuit working if you're within the right order.

**Dave Jones:** Another practical example of an order of magnitude is calibration. Let's say I wanted to calibrate my Fluke 87 multimeter here, and it's uh say, for example, it's 0.1% uh accurate, and I want to compare it against something else.

**Dave Jones:** Well, you want to have something that is an order of magnitude better or 10 times better. So, you'd want another meter which is 0.01% instead of 0.1%. So, comparing against another Fluke 87 is no good.

**Dave Jones:** I need a meter which is an order of magnitude or 10 times better than that to give you a test uncertainty ratio of 10. Like a I sort of the minimum figure that we use in the calibration industry might be a test uncertainty ratio of four, but ideally, that's that's a minimum.

**Dave Jones:** Ideally, you would really be shooting for something that's 10 times more accurate than the instrument you're trying to calibrate. So, you'll find that order of magnitude 10 times or 1/10 come up all the time in electronics engineering.

**Dave Jones:** It basically is just that rough figure where something sort of doesn't matter in a practical sense. If it's 10 times bigger or if it's 1/10, if you know, your leakage current is 1/10 of something else or if your phase is 1/10 of something else, order of magnitude out, it's practically not going to make a huge difference to a working circuit.

**Dave Jones:** So, you'll hear the term all the time, and it gets thrown around, and it's a very good term. If you're going if you're a you know, a graduate or whatever, and you're going for a job interview or something like that, there's some real choice terms you should throw in.

**Dave Jones:** Order of magnitude is one of them. Start talking in terms of orders of magnitude. Oh, yeah, it's an order of magnitude out a couple of orders. Yeah, you'll sound like you've been in the industry for 20 years and you know what you're talking about.

**Dave Jones:** It's like you're using dBs for everything. Start using orders and people will think you know what the hell you're on about. So, I hope that gave you a bit of an insight into and get a feel for orders of magnitude.

**Dave Jones:** Catch you next time. And that leads us to one of the biggest misconception misconception
