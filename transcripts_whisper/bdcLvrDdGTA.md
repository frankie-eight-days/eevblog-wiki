---
video_id: bdcLvrDdGTA
title: EEVblog #48 - Solar Power Hope
url: https://www.youtube.com/watch?v=bdcLvrDdGTA
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 20, "2": 36, "3": 58, "4": 70, "5": 96, "6": 113, "7": 134, "8": 145, "9": 172, "10": 185, "11": 206, "12": 218, "13": 233, "14": 251, "15": 276, "16": 290, "17": 313, "18": 335, "19": 362, "20": 382, "21": 403, "22": 422, "23": 436, "24": 458, "25": 478, "26": 491, "27": 512, "28": 533, "29": 557, "30": 572, "31": 594, "32": 613, "33": 626, "34": 642, "35": 659, "36": 676}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. I started work on a cool little project recently. It's a credit card-sized scientific calculator slash computer and, you know, I thought

**Dave Jones:** I'd have a go at it just for fun and I was originally going to have it battery-powered but then I thought, wouldn't it be cool to have it solar-powered? Completely self-contained, solar-powered. So I knew that solar cell, you know, you can get solar-powered calculators,

**Dave Jones:** you can get solar-powered credit card calculators. They've been around for like 20 years, you know, there's nothing new there. But the problem with these solar-powered calculators that have been on the market for 20 years is that they're really, they're tiny-powered. The solar cells generate virtually no current at all and they've got extremely low-power custom ASICs

**Dave Jones:** in there, application-specific integrated circuit, that allow them to get the really low power consumption. They only operate at tens of kilohertz. But my new project, I was going to have a full dot matrix LCD on it, like a 132 by 32 dot matrix display.

**Dave Jones:** And the module I was looking at using took around about 100 microamps at about 2.4 volts and upwards. So, you know, it's not a huge amount of power, but I knew that for a solar-powered design, especially something as small as a credit card, was going to be a challenge.

**Dave Jones:** But I thought, maybe it's possible. So I thought I'd have a go at it. Now, last time I worked on a solar-powered design, I think it was like, oh, the 1990s or something like that. So it's been a long time. And everyone knows that

**Dave Jones:** there's been massive progress in the efficiency and design of solar cells in the last 10, 20 years. You know, a massive advance. So I knew I couldn't really get that sort of current or power out of just a typical little calculator solar cell, but I thought I'd try and have a look at what's

**Dave Jones:** available on the market and get the best available on the market. You know, price wasn't really an object. So I thought I'd get one of these. It's an IXYS. I think that's how you pronounce it. An I-X-Y-S branded monocrystalline solar cell surface mount.

**Dave Jones:** They're really cool little devices. They're designed for applications like charging mobile phones and charging PDAs and other type portable devices. So they're monocrystalline. So they're the highest efficiency you can get. I think they're like 15-16% efficient or something like that. So they're really top class.

**Dave Jones:** And they're not cheap. They're like $5 each. And these put out about one and a half each. Well, this one's got three cells in it. Puts out about one and a half volts at up to 12 milliamps in full sun. And you can fly to the moon on 12 milliamps.

**Dave Jones:** It's a huge amount of power. So I thought, uh-huh, these might be suitable for my project. All I need is 100 microamps or so. Is it possible? And I just, I didn't do any calculations on paper. I just did a few rough numbers and, you know, I thought

**Dave Jones:** maybe, maybe it's possible. But, you know, I'm a practical guy. So I got some and I tried to measure them to see what I could get. Now a regular solar power calculator like this Casio, as you can see, this one's, it's got an internal battery but it's dead.

**Dave Jones:** But it, uh, see, it works on the solar cell just in the very poorly lit EEVblog lab here. But, you know, it works. I can sort of half cover that thing, you know, I half cover it and it really, they are really quite remarkable.

**Dave Jones:** And these don't use monocrystalline cells. They typically use amorphous solar cells which are only about, you know, five, six percent efficient as opposed to these monocrystalline ones I planned on using which were, you know, the super-duper latest technology which are much more efficient.

**Dave Jones:** So here it is. I've got three of these in series which if I hook it up to, let's do some things. And as you can see this is the, in the lab here, and I'm getting out 3.4 volts. Yeah, no worries, great. But if I,

**Dave Jones:** let's measure the current of this thing, this short circuit current, you can actually do this with solar cells. It's actually quite valid to measure the short circuit current. So you just hook it straight up to your meter in current mode, shorts it out, but you can get a really good

**Dave Jones:** indication of its operational current capability by just shorting it out. So as you can see, not, that's AC. Bloody fluke multimeter that defaults to AC, it's crap. Anyway, here you go, 30-odd microamps. Okay, that's its short circuit current. But, you know, if I lay it down on the bench here,

**Dave Jones:** it's about 25 microamps, and if I put my hand over the cell a bit, it drops down. So, you know, really I'm only getting, under typical conditions in like an inside environment here, where these, you know, these really ultra-low power calculators work just fine, this thing's

**Dave Jones:** only given me, you know, tens of microamps. So, really, that sort of, you know, very disappointed. My project just wasn't really viable, because the LCD alone would take 100 microamps. So, project scrapped right there. I was pretty disappointed. Not, not terribly surprised though, I guess, because, really, when you actually think about it, and you look at the

**Dave Jones:** figures, and you go through the math, I really didn't have to try this in practice to know that it really wasn't going to work. But, you know, I was hopeful. I thought that, you know, hope could overcome engineering, but no, afraid not. Okay, I know what you're thinking, maybe all the data sheet

**Dave Jones:** values were just bullshit. Does it actually give out 12 milliamps in, you know, in under ideal conditions? Well, I'm outside, let's find out. It's about, um, almost 6.30 at night at the moment, but, uh, as you can see, I've got the, got it pointed towards the sun, and sure enough, there it is, 11 milliamps.

**Dave Jones:** So, it can actually get close to that 12 milliamp figure, no problems at all. So, there you go, these things aren't bullshit. The data sheet is, is right on the money. These are top quality cells, they give out 12 milliamps at their rated voltage of 1.5 volts, or something like that, so they really are

**Dave Jones:** quite remarkable. Uh, they're, so you really could, you know, charge a mobile phone in full sun with one of these little things easily. So, why doesn't it work inside? Why doesn't it work indoors? Well, the answer's really obvious with a couple of seconds thought.

**Dave Jones:** It's about dynamic range, and dynamic range of these things. The human eye has a massive dynamic range. It spreads, it's about, uh, 90 dB, or something like that. It's a huge range. That's why you can go outside, you know, on a fully sunlit day, and you can

**Dave Jones:** see things perfectly, and, and yet, yet you can just walk inside, and your eyes adjust fairly quickly. It takes, the response time is an instant, but it adjusts, and then you can go outside at night, under, under moonlight, and see things. So that's a huge dynamic range, in the order of 90 dB.

**Dave Jones:** Okay, so let's take a look at some figures here. Now, a 90 dB range is approximately, it's a bit over, but it's approximately 30,000 to 1 ratio, which, which your eye is capable of seeing over, and so you perceive anything within that range to be, you know, fairly similar, I guess you could say.

**Dave Jones:** Now, the sun, when you're outside, is about 300,000 lumens. Let's round it down to that. I think it's a bit more, but let's say it's 300,000 lumens. Now, indoor lighting, uh, might be around about 300 lumens. Say, I've got two, uh, fluro tubes in here, and in the lab here, and that's, and that's about it.

**Dave Jones:** So I, I don't actually have a lux meter to actually measure it, but, you know, it's going to be around about in the order of 300 lumens. So the ratio of that to that is, of course, a thousand. Now, if I'm getting, say,

**Dave Jones:** 10 milliamps at, in full sun, okay, that's, uh, then you can divide that by this thousand, ratio of a thousand, and bingo, I'm only going to get 10 microamps indoors, and sure enough, that's what I measure. And so, you know, really, it's, it's fairly obvious, uh, when you go through the math, that, you know, do some

**Dave Jones:** simple calculations, that it's not really possible. But I was hoping that it was possible, because, you know, I thought, oh, you know, you can put them in parallel as well. You can put them in series and parallel combinations. So maybe if I got enough of them in parallel, I can only fit a certain number

**Dave Jones:** on my product. But if I got enough, it might be able to work indoors, but really, no. So the project, so the idea of powering my project from solar cells is really pretty much a no-go, unless I used a, uh, seven segment display LCD instead of those dot matrix ones, then I could probably get around, then I

**Dave Jones:** could probably do it. I could use a low-power processor, like an MSP430, or a microchip nanowatt XLP, or something like that, and, uh, with a seven segment display run at 32 kilohertz, it's still possible. But that's, that's not really as cool as, as the full dot matrix display I wanted

**Dave Jones:** to use. So, oh well. Yeah, I know I'm talking in terms of just current and things like that, when I should be really talking about power, but these are just sort of, you know, ballpark, uh, calculations, really, that, um, you know, it's, it's, it's really going to be of the same order.

**Dave Jones:** So it's, you know, you can just, for a rough back of the envelope, calculations for a design such as this, it's, it's perfectly all right, just to measure the short circuit current, and if you're working at low enough voltages, it's not, it's not

**Dave Jones:** really an issue. So what's the moral of the story? Well, you can't just hope your next project's going to work. You know, if you're trying to do something like this, you have to, you have to really look at the facts and figures carefully, uh, before you think something's possible, and get your hopes up.

**Dave Jones:** Because really, you know, a couple of simple measurements, or, or just some, uh, thinking about it up front, really can show that a project is not possible. And, you know, I know that kind of sucks, but you know, because really, you know, as Doc Brown said, if you put your mind to it, you can

**Dave Jones:** accomplish anything. But sometimes, you can't. Ah well.
