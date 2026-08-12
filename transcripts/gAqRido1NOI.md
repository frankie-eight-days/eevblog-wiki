---
video_id: gAqRido1NOI
title: EEVblog #4 - Calculator Design, Mr Bean, & FPGA's
url: https://www.youtube.com/watch?v=gAqRido1NOI
source: youtube-asr
---

**Dave Jones:** Hi, I'm Dave Jones, and welcome to the EE Vblog number four. As you might know, I've got a bit of an interest in calculators, and sometime back I noticed that Hewlett-Packard, um, they actually released the HP 20b financial calculator.

**Dave Jones:** Now, I don't have much interest in financial calculators, but uh, one spec caught my eye, and that was the fact that it ran at 30 MHz. Now, that just seemed uh, you know, uh, quite high. I couldn't believe it. Wow,

**Dave Jones:** 30 MHz for a financial calculator? Unbelievable. So, I decided to check into it. Now, the HP 20b uses, uh, the new Atmel, um, ARM processor. It's the SAM7L series, and it's quite a nice nice device. It's really designed for

**Dave Jones:** low-power operation. It's got, uh, 0.5 mA per MHz, uh, power consumption, which is really quite low. Now, the, uh, Atmel ARM chip is actually quite smart. You can actually dynamically change its clock speed, um, as you're going. So, so the code can

**Dave Jones:** actually change the clock speed. So, what you can do in a calculator design is that, uh, when you need to, when you're actually performing the calculation, you can speed it up as fast as you want to help speed up the

**Dave Jones:** calculation. And then when it's sitting there idle, just waiting for a key press, you can drop it right down to 32 kHz or something. Now, if the chip can operate at 30 MHz, it kind of makes sense when you're doing

**Dave Jones:** the calculation to up it to its highest frequency possible. Uh, because everyone knows that, um, if you, uh, speed up something 10 times, it takes 1/10 the time to do that calculation, to perform that operation, as it does at a frequency 10 times less.

**Dave Jones:** So, why not just bump it up in speed? So, let's do some back-of-the-envelope calculation, shall we? Now, the HP 20B is powered from two standard CR2032 coin cell batteries, and they have a characteristic which looks something like this.

**Dave Jones:** This is the internal resistance in ohms, and this is time, and starts off and heads up like that. Now, it starts off around 15 ohms, and you know, it starts going off the scale at about 100 towards the end of the life. And at

**Dave Jones:** about half life, it's about 20 ohms or thereabouts. Now, let's have a look at what effect this has on our operation at higher frequencies. Right, so let's do a model of the calculator. We've got the coin cell battery.

**Dave Jones:** We've got an internal resistance. And we've got the calculator itself. Now, we've already said this is 15 ohms, but because they're using two in parallel, let's go 7.5 ohms. We have current I, and we want to know the power that's

**Dave Jones:** being wasted in this internal battery resistance. So, let's call that uh PR. Okay? Now, at 30 MHz, let's have a look at what loss we get in the internal battery resistance. PR is equal to 15 milliamps because we said the uh

**Dave Jones:** device has .5 milliamps per megahertz power consumption. So, if we're operating at 30 MHz, we're using 15 mA. Now, that's squared times uh 7.5 ohms. And that gives us an answer of roughly 1.7 mW loss in the battery resistance. Now,

**Dave Jones:** that doesn't sound like much, but let's compare it when it operates at 1/10 that frequency. So, let's do the same again, but this time at 3 MHz. Power in the resistor equals This time, it's uh only going to be 1.5 mA.

**Dave Jones:** Squared times 7.5 ohms. And that's going to be about 17 microwatts. But, I know what you're thinking. Because we're operating at 3 MHz, we need 10 times the uh 10 times the amount of time to actually do the same operation as we

**Dave Jones:** would at 30 MHz. So, let's multiply that by 10, and we get 170 microwatts for or what? Per second. Now, these two figures, you can see that at 3 MHz, it takes we have 1/10 the loss in the battery as we do at 30 MHz. So, what

**Dave Jones:** have we proven with this little calculation? Well, we've proven that it's the squared factor which gets you, the I squared factor in power consumption which really gets you. And you have to take into account the internal battery resistance in low-power

**Dave Jones:** designs like this if you're operating at high frequency. Because the 20B calculator is wasting at minimum uh 5% of its consumption is being taken up by the internal battery battery resistance and that's just going to get worse as the battery ages because of this

**Dave Jones:** curve here. It just gets worse with time. So, it's not too bad, you know, losing 5% in your internal batteries isn't too bad right down at this point, but when you get right up to here, it's you know, when you get towards the end

**Dave Jones:** of the battery life, it's getting quite severe and it's really just poor engineering. Not much thought has gone into it. They've just upped it to the highest possible frequency, 30 MHz, and really not given much thought to the internal

**Dave Jones:** battery resistance. So, just take it into account next time you're designing something like this. I came across a rather interesting fact the other day while I was searching another engineering blog site actually. It's was the Subversive Guide to

**Dave Jones:** Engineering site and they had a list of the top 10 uh famous people who were engineers. And one I had no idea about was Rowan Atkinson, Mr. Bean. Incredible. He actually has a degree in electronics engineering and also a

**Dave Jones:** master's from Oxford. Who knew? Mr. Bean. Can you imagine having Mr. Bean working on your project or Mr. Bean at your design review meeting? Awesome. Now it's time for another thing that really ticks me off. This time it's

**Dave Jones:** FPGAs, field programmable gate arrays. Now, I like FPGAs. I use them a lot, but one thing that's ticked me off over the years is that you've never really been able to get uh the high logic density devices in

**Dave Jones:** small packages, in ones that you can use for prototyping like, you know, a simple quad flat pack or something like that. Uh they all come in BGAs, and this was this was really bad uh 4 5 years ago. It

**Dave Jones:** was it was shocking. You couldn't get a single FPGA on the market that wasn't in a big BGA package. They uh the manufacturers seem obsessed with high pin count, high IO, and high number of IO devices. So, if you wanted a um

**Dave Jones:** uh you know, a couple hundred thousand logic element device, a really high density one, you're forced to use this thousand pin BGA package. It was crazy. It's uh it's actually getting a bit better these days. The manufacturers um

**Dave Jones:** are starting to release, you know, a little 44-pin quad flat pack devices, things like that. But, they're but they're still only a low density. So, you know, they actually have they have fairly limited use. Um so, really, I

**Dave Jones:** don't know what's stopping them. You know, a a couple hundred thousand gate high density device, you know, you know, a DIP-28. Beautiful. I get a lot of questions about my scientific calculator watch project, the Micro Watch. One of the most asked questions is,

**Dave Jones:** where do I get the little compact LCD display that I use in the watch from? The answer is I get it from Jaycar, but many people don't realize it's an industry standard size. It's 53 by 20 mm, which is really

**Dave Jones:** tiny. And it's a standard two-line by 16-character LCD display. It uses a standard LCD chipset, so it's compatible with your existing code. And they're just real handy. There's probably four, five, six different manufacturers out there that I'm aware

**Dave Jones:** of, at least, that make this exact uh one with the same mounting holes, the same dimensions, 53 by 20 mm. And they're really handy. So, look at specking one into your next project because they're just great for all sorts

**Dave Jones:** of apps.
