---
video_id: gG6rta4PuSM
title: EEVblog #35 - Inside the Varta 15 minute NiMH Battery Charger
url: https://www.youtube.com/watch?v=gG6rta4PuSM
source: youtube-asr
timestamps: {"0": 10, "1": 47, "2": 83, "3": 126, "4": 175, "5": 195, "6": 228, "7": 254, "8": 282, "9": 318, "10": 352, "11": 377, "12": 411, "13": 434, "14": 450, "15": 480}
---

**Dave Jones:** Hi, today we're going to talk about battery chargers. Why? Well, I was at work the other day and we needed to power something from some rechargeable batteries and we needed a solution really quick and we didn't have anything so I went down to the local shop and I found this. It was the Varta 15-minute battery charger. Yes, you heard that right, 15 minutes. It claims it can charge these things and supports four double A's and it comes with these Varta rechargeable ready-to-go, they're called, Varta ready-to-go 2100 milliamp

**Dave Jones:** double A rechargeable batteries and they're similar, these batteries are supposedly similar to the Sanyo eneloop ones where they actually hold um they charge for a long time. These ones are rated at something like they can hold they still hold 80% of their charge after 12 months. So very similar to the Sanyo eneloops. So I thought I'd give it a go and because they come charged straight out of the pack, that's what we needed and they did actually work straight out of the pack by the way. But I figure 15 minutes you can

**Dave Jones:** charge. Is there something dodgy going on here or is this some marvelous new technology? Well, let's check it out. Let's start by looking at the charge rate. Now the Varta batteries have a capacity, a rated capacity of 2100 milliamp hours. Now a standard fast charging rate for these type of batteries is what's called a 1C charge rate. That's one times the battery capacity. So it's 2100 milliamps for 1 hour. Okay, so it's 2.1 amps, 2100 milliamps, for 1 hour. All right? Now, that's the 1 C rate, but you can have

**Dave Jones:** other charge rates as well. You can have, say, 0.1 C, or often called C on 10, and this will be 1/10 that uh current. So, it'll be 210 milliamps uh for 10 hours. So, let's figure out this C rate for this Varta one. It claims it can charge a 2100 milliamp hour nickel-metal hydride battery in 15 minutes. Okay? 15 minutes is uh 1/4 of an hour. So, that means uh you have to charge it at four times its uh rated capacity. So, 2.1 * 4 is 8.4 amps for 15

**Dave Jones:** minutes, and that is a an effective uh C rate of four, what's called 4 C. And that's absolutely incredible. Check out the claim on the packet. Charges up to 1,000 cycles, and all at this 15-minute 4 C charge rate. That's what they claim.

**Dave Jones:** Four times more than anyone else, any other manufacturer's rate. Now, they got must have some fantastic new technology in here. Because if they can do that, if you can get 1,000 decent cycles out of these, I'll eat this damn battery. I reckon it's marketing But if it can do it, then must be using dilithium crystals or something. Or heck, all the Chinese have figured out how to put a zero-point module in here. Wow, you know, the the Gould or the Replicators are invading Earth. We can recharge the Antarctic

**Dave Jones:** defense outposts in 15 minutes. Woohoo! And yes, you guessed it. We're going to open this sucker up and take a look at what's inside. But but I can tell you up front, I know what's going to be inside here because just this massive charging rate dictates several design options with this thing. It's got to have individual charging for each battery.

**Dave Jones:** There's no way they are in series and because it's got four leads that indicates that. But and it's got to have There's no way it's just a timer base system. It's got to have an individual temperature sensor on each one. And because there's a huge fan in there, it's it can't just have the temperature sensor like inside the case like some cheaper lesser slower chargers do. It's got to sense the It's very critical and we'll talk about this later, but it's very critical that senses the battery

**Dave Jones:** temperature. So I can guarantee you it's going to have an individual temperature sensor on one on these on each one of these terminals or maybe inside these little springy things here. Maybe it's inside there, but I I guarantee you there's an individual temperature sensor for each battery direct contact. And because we're talking about 8 amps at least minimum 8 amps 9 amps even per battery to meet their specifications, this thing's going to have some heavy duty wiring per channel and it's going to have some really beefy

**Dave Jones:** transistors, MOSFETs, you know, solid state relays, something like that to actually get the individual control to each battery. And it's going to have one heavy duty power supply in there as well to cater for all that. This thing requires a lot of power. Check this out. The plug pack that comes with it, it's a 15 volt 4.7 amp 70 watts. It's actually a 70 watt plug pack. So this thing is going actually even if it's reasonably efficient, it's still going to get quite hot during charging. So,

**Dave Jones:** that's that's one decent plug back. All right, here we go. I've just popped the back cover off. It's got three screws on it. And as you can see, this is pretty much what I expected up front. Definitely, these are the output MOSFETs or um what are they? Hang on. I think they're a can't really get the part number there, but um I'll have a look at that later.

**Dave Jones:** And there's obviously a micro of some sort. Um I can't make out the number there, but um that's a obviously a microcontroller. There's got It's got some cable running over here to this back board. And as you can see, I'll turn on the light here and see if I can get in there. Bingo, there it is. There's the internal um sensor. There's the temperature individual temperature sensor on each of these um uh contacts. So, it looks like it's just a little um silicon diode or something

**Dave Jones:** like that, which which is probably uh good enough for temperature sensing. But there you go, each of those contacts has a little temperature sensor, as you'd expect. And you've got um it looks like there's two of these um uh output MOSFETs or relays per uh channel. And they've got these beefy strap wiring across here like this. And that's pretty much what you'd expect.

**Dave Jones:** Okay, I've prized the uh top board open. And as you can see, here's the high current uh switch-mode supply. That one's got to be supplying the four times uh 8 amps at least minimum required for the batteries. And this is interesting.

**Dave Jones:** The um If you can see just in here, that that little spring type contact. I'm not sure if you can Yeah, I'll try and make that better. There you go, there's a little contact spring which comes down there, and that um when you push in this contact here, it pushes down and actually enables that uh channel. So, that's actually quite neat. I really like that. Okay, now what I've done here is I've actually desoldered one of the uh channels here, and I've installed a battery on the back

**Dave Jones:** there. I've got it powered up, and I'm going to measure the actual um current. And let's what let's turn it on and Yep, the fan's going, and bingo, 7.6 amps I saw there, 7.6, and it's just cut out. So, it looks like it was giving about 7.6 amp pulses. So, that kind of matches with the uh figures that we thought we should get for a 15-minute charge.
