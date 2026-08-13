---
video_id: lndRXed2ylk
title: AGL Energy Smart Meter DODGY?
url: https://www.youtube.com/watch?v=lndRXed2ylk
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 18, "2": 32, "3": 48, "4": 67, "5": 85, "6": 102, "7": 118, "8": 136, "9": 160, "10": 189, "11": 202, "12": 223, "13": 242, "14": 259, "15": 274, "16": 291, "17": 315, "18": 330, "19": 345, "20": 361, "21": 383, "22": 401, "23": 417, "24": 434, "25": 453, "26": 476, "27": 493, "28": 508, "29": 527, "30": 541, "31": 559, "32": 580}
---

**Dave Jones:** Hi, just a quick video on my new smart meter. Yes, I've got one of those newfangled smart meters. Link in the video if you haven't seen it. I used to have net metering, so import and export meters, but now it's been replaced by a smart meter which does the time of day usage.

**Dave Jones:** So, potentially I can now join other plans. Yes, I'm aware of other plans, but if you have links to I'm aware of OVO or whatever it is, if you know of any others, please let me know, that have favorable like EV battery charging plans or whatnot.

**Dave Jones:** Anyway, so it's new, like a time of day usage. Even though I'm not doing time of day, the meter is now capable, smart meter is capable of that. I'm still on a fixed rate plan. So, what is it? 31 cents per kilowatt hour or something like that.

**Dave Jones:** No, 28 or something like that. Anyway, I'm on a fixed rate. I've noticed something interesting here, though. I've now had it installed for 7 days, okay. So, here's my energy provider, and here is my new live results. It gets updated once per day, and sometimes there's a couple of days lag before the data updates or whatever.

**Dave Jones:** But anyway, I've got 7 days worth of data. So, before this, they just put in some flat generic value, which I don't know, was some calculated average or something. It doesn't matter. Anyway, I've had it for 7 days. Look, on the first day, so the blue one above, it means that I've imported energy from the grid.

**Dave Jones:** So, it means my solar power system and all my battery has not been able to provide that energy, okay. 2.08 kilowatt hours per day, but I exported 3.05. So, I exported more than I got, but I'm only getting paid 8 cents per kilowatt hour.

**Dave Jones:** So, I only got 21 cents back. But anyway, next day, I imported again 1.38 kilowatt hours, even though I exported a ton, which means that my battery would have been full very early on in the day there. And I was just, and we weren't using it for anything else.

**Dave Jones:** You know, we weren't charging the EV, we weren't doing whatever. And so, I had a ton of energy to export. So, I exported 15.8. But, you'll notice that I've got a little bit more energy. So, what? Okay. Good thing is I have a third-party energy monitoring thing, which is my solar analytics.

**Dave Jones:** But let's have a look at this day here, okay. 4th of September, where I exported all this ton of energy, but still didn't get paid for it. So, what? Okay. So, what? Okay. So, what? Okay. So, what? Okay. So, what? Okay. So, I exported all this ton of energy, but still imported 1.38 kilowatt hours.

**Dave Jones:** So, 4th of September, let's go over to here, okay. Let's go back to the 4th of September. And you can see that my produced, right, is equal to the consumed. So, what that means is that I'm not importing any energy whatsoever, right. Because my consumed is matching even at nighttime, which means my battery is providing that energy, right.

**Dave Jones:** So, my battery is actually providing that energy there. So, there's no, like, if we go back here, I can try and find, here we go. There's a small peak there where it produced more than it was taking. Let's see if there's another one.

**Dave Jones:** Here we go, right. The battery must have got full there. And so, it was like exporting all this stuff, right. So, it was producing more than it was consuming, or whatever, right. So, there you go. But we don't, but where, but when it matches, right, when there's no excess energy there, right,

**Dave Jones:** it means that the produced equals the consumed precisely. Now, the solar analytics only updates in 15-minute intervals. I can do live for, like, 5 minutes or whatever. But, anyway, it's 15-minute intervals that it logs this in. So, technically speaking, I could, you know, you could switch on, you know, massive loads for, like, 15 minutes

**Dave Jones:** and all of the less than 15 minutes that it might not show up on here, perhaps. And let me show you my battery, okay. This is from my solar assistant Raspberry Pi coming from my new DI inverter, right, which the battery's hooked up to, okay.

**Dave Jones:** Now, if we have a look at the state of charge of the battery, you notice that on none of these days did my battery deplete to 20%, which is what I've got this switch off done, right. So, this is the last 7 days here, okay.

**Dave Jones:** Last 7 days of my battery state of charge. So, my battery has easily taken care of all the nighttime loads. So, during the night, and, you know, it's only taken a couple hundred watts for some fridges and stuff, right, for some residual stuff.

**Dave Jones:** My battery has never discharged in the last week. So, why am I seeing that I am every one of those days, I'm import, according to this newfangled smart meter, I'm importing an average of, like, 1.8 kilowatt hours of energy. Why? So, if we turn everything off, right, you can see the consumed data, right.

**Dave Jones:** So, this is for my entire house, okay. So, this will capture everything, alright. So, yeah, you can see that, you know, the house is using over 8 kilowatts here, so that would exceed the battery 5 kilowatt, you know, maximum output of the battery.

**Dave Jones:** But that's during the day. So, the solar would take over the rest, okay. But just take a look at the scale over here, okay. At night, right, which is kind of what we're worried, more concerned about, because, you know, I could turn on a couple of major appliances at night,

**Dave Jones:** the oven and a couple of air cons or something, even though we haven't been using air cons. But, you know, we could turn on some major loads. I think we turned on the dryer one night or something, you know, something like that. So, yeah, but look, you can see that, you know, at nighttime here,

**Dave Jones:** just coming from the battery, right, like the battery can provide all of that energy, right. The battery can provide all of this. So, what? What? So, there's nothing at nighttime that's been, that would cause this. It should, the battery should be able to deliver all of that

**Dave Jones:** if it's 5 kilowatt power capability, right. And even during the day, there hasn't been, right. So, from the 3rd to the 9th is what we're looking at. Like, I'm only looking at peak powers, 9 kilowatts, briefly, 8 kilowatts, you know, 8.5, 9. Yeah, so we like, you know, the green one there,

**Dave Jones:** we're dumping some excess energy into the pool, for example, and then the heat pump, hot water system, the air cons not actually, the current plant's not hooked up, that's included in the consumed one here. But, like, what? And then we had the EV charger there for a bit with our zappy EV charger,

**Dave Jones:** just, you know, topping up the EV there. But, like, this was all during a period when the sun was, like, out. And you can see the battery peaks. Like, you know, yeah, we hit 5 kilowatts here on the 4th, so the battery was peaking here during the day.

**Dave Jones:** But once again, that's actually during the day, that's at 10 a.m., we should have, you know, a reasonable amount of solar by then, which can take up the difference. But, you know, there's only a couple of brief points where the battery actually maxed out in its 5 kilowatt production capability.

**Dave Jones:** And it never went, it never discharged, it never shut off. What? What? So what's going on here? What's going on? Why am I, I can't see, in my data, I can't see why I would be importing energy on any of these days. Yet it seems, you know, reasonably consistent,

**Dave Jones:** suspiciously consistent at, like, 1.8-ish average. That one's a bit low, 1.3. Like, why? Where is this residual coming from? I can understand maybe, you know, a couple of hundred watt-hours in, you know, error in current shunts or whatever or something like that, you know.

**Dave Jones:** But these are supposed to be calibrated, you know, officially certified meters and everything, right? So it's got to be accurate. But I'm just wondering where this residual's coming from. I don't see it. I don't see it in my data, is what I'm saying.

**Dave Jones:** Over the last seven days, I would have expected, you know, at least a few of those days to show zero imported energy. So I can leave it going for another week or two and I'll keep you updated, but is it going to magically fall to zero?

**Dave Jones:** Do we have to, like, actually go away, shut everything off, or go, you know, go away for the weekend or something and see if, like, we actually get a zero import day? I just don't get it. I just don't get it. If you've got any idea what's going on here,

**Dave Jones:** then please leave it in the comments down below. But I smell something. I smell some funny business going on here. I don't know what's up. But I expected, after a week, with, like, really good days and, like, not much in terms of, like, peak battery power

**Dave Jones:** and stuff like that, and easily going through the nights where the battery can easily handle all of the capacity. Battery's never stopped. Yet, I'm getting pinged for 2 kilowatt hour, 1.8 kilowatt hours on average or something, imported. I don't get it. If you've got any clue, leave it in the comments down below,

**Dave Jones:** but I'll keep you updated on this. I just thought that was interesting. Something's not right. Catch you next time.
