---
video_id: AUwbtG6z6pI
title: EEVblog #1 - Rigol DS1052E Oscilloscope Review
url: https://www.youtube.com/watch?v=AUwbtG6z6pI
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 31, "3": 49, "4": 71, "5": 93, "6": 112, "7": 129, "8": 146, "9": 168, "10": 184, "11": 198, "12": 215, "13": 236, "14": 257, "15": 269, "16": 284, "17": 301, "18": 322, "19": 338, "20": 353, "21": 378, "22": 400, "23": 417, "24": 436, "25": 453, "26": 473, "27": 491, "28": 504, "29": 520, "30": 535, "31": 552, "32": 566, "33": 584}
---

**Dave Jones:** Hi, I'm Dave Jones. I was speaking to a colleague the other day and we were talking about video blogs and you know, all that online stuff. And he said, "Why isn't there a blog for engineers like us?" And

**Dave Jones:** well, I did know of like text blogs and things like that, but I had a look around and there are no video blogs. Something that we can watch every week. So, he suggested, "Why don't I do one? Do a video blog about engineering."

**Dave Jones:** And I thought, "Well, why not? I'll give anything a go." So, here it is, my first very first video blog about electronics engineering for guys like me. I came up with a couple of ideas. We can have book reviews,

**Dave Jones:** equipment reviews, mhm. And general news, I guess. Uh inform about what cool new parts are on the market. And anything else I can think of. Let's try a book review. And I'm not talking like nerdy sci-fi books or anything like

**Dave Jones:** that. Talking about books that should be of interest to electronics engineers. So, my first one is iWoz by Steve Wozniak. Now, if you don't know who Steve Wozniak is, then well, yeah, you shouldn't be watching this video blogger yet. Um

**Dave Jones:** it's his autobiography. It's his autobiography about how he uh uh started Apple, of course, and um came up with the first Apple I and the Apple II and uh the cream soda computer and uh all these practical jokes he used to do

**Dave Jones:** and all that sort of stuff. And it's got lots of info in here about his methods of design, his methods of minimization, circuit minimization, and it's it's just a really good read, and I'd highly recommend it. There's also an audio book

**Dave Jones:** version. Um I haven't fully read through that one, but unfortunately, it's not actually um spoken by Steve himself. So, I much prefer audio books that are spoken by the original author. Um but yeah, I highly recommend it. Get

**Dave Jones:** it. I was. And today's chip is the Linear Technology LT3085. And it's advertised as a low dropout 500 milliamp voltage uh regulator. Nothing unusual there. Uh but it's got two useful characteristics. The first one is that the output voltage

**Dave Jones:** is set by a single resistor, which is really handy to lower your parts count, better than the traditional dual resistor approach. But uh secondly, and most importantly, the output voltage is uh the output voltage can go down to

**Dave Jones:** zero volts, which is very unusual. Uh there's not uh many voltage regs on the market that can actually go down to zero volts, and that's really quite handy for many applications. And the way it works is unlike a

**Dave Jones:** traditional voltage regulator, this one is it's actually really simple. It's a band gap current source with a op-amp voltage follower and a series pass transistor, and that's basically all it is. Um it's really simple, but because it's all in the one

**Dave Jones:** package, and it's available in tiny surface mount packages, it's a real handy device and quite unusual. So, check it out. The Linear Technology LT3085. I came across a very interesting concept recently. It's called hacker spaces. Um basically, what a hacker space is is

**Dave Jones:** a communal uh hardware lab, so to speak, where uh engineers, hackers, nerds, geeks get together, and they work on just interesting and cool projects. They build them. They They disassemble things, do teardowns, um and just generally just hack around

**Dave Jones:** on stuff. And uh I do believe there's a a monthly fee or something like that involved, but basically, if if you join, you can turn up and use all the facilities and associate with all the other people there and

**Dave Jones:** and it sounds like a really good concept. Um and they're setting up all over the world, basically. There's a whole bunch in the US, Europe. There's a couple trying to be formed in Australia here in in various cities. Um

**Dave Jones:** So, but it sounds like a great concept. So, check it out. It's at hackerspaces.org. There was some news just the other week from Atmel, who make, you know, the AVR range of microcontrollers amongst other things. And the big news was that they've come out

**Dave Jones:** with this new ATtiny AVR microcontroller that supposedly operates down to 0.7 V, which wow, you know, sounds fantastic. It's uh means you can run an app from a single cell, um a single double A alkaline cell. Um and it sounds sounds like really good. I

**Dave Jones:** thought, "Oh, great. They've come out with some new uh process technology that allows the micro to operate down to 0.7 V." But no, as usual, there's always a catch. And uh basically, it's just a regular AVR ATtiny micro with a built-in boost

**Dave Jones:** converter. So, you need all the usual external parts. You need an inductor and a diode and some caps. And um I I guess it's handy for uh uh some people to lower their parts count in some apps, but really it was a

**Dave Jones:** bit of bit of a disappointment, so good try, but yeah, marketing. Some other big news this week uh concerns the CSIRO, the Australian research uh Commonwealth owned company. And they've just won a patent lawsuit against Hewlett-Packard, actually. Hewlett-Packard um settled out of court,

**Dave Jones:** I think. And basically, it um involved uh Hewlett-Packard among many other companies infringing on the CSIRO's patent for uh Wi-Fi. Uh not many people know that, but the CSIRO actually developed Wi-Fi, the 802.11 standard, uh what led to the 802.11

**Dave Jones:** standard. And they've been suing everyone left, right, and center to try and uh keep those patents, and it looks like they actually won. They beat Hewlett-Packard, so I guess all the other companies who make 802.11 gear are shaking in their boots and

**Dave Jones:** probably have to pay up royalties as well, otherwise they're going to get hauled off to court, too. Good on the CSIRO, yes. Okay, let's review some really cool equipment. What I've got today is the Rigol 1000 E series oscilloscope. It's a pretty new

**Dave Jones:** series, not to be confused with the 1000 B series or the 1000 A series. They're all different. So, just be careful, it's a bit confusing. This is the This is the DS1052E, the 50 MHz uh version. Bottom of the range, but

**Dave Jones:** it's really low cost. It's incredibly low cost. I got mine for 679 Australian dollars delivered. Um for you Yankee folk, that's less than 500 US dollars. Um, so it's it's really a remarkable price breakthrough. Even though they're they're uh cheaper oscilloscopes,

**Dave Jones:** they're really high quality. This one's uh really quite amazing. It just feels like a quality scope. Um, all the uh button indents are really quite high quality. The button presses, the screen The screen is really good. Um, it's a 320 by 240 quarter VGA, which

**Dave Jones:** is pretty standard in this price bracket. Um, but it's got a nice bright LED backlight. It's It's almost too bright, really. And it's a It's a big step up from their previous series. Um, other things are a really nice uh

**Dave Jones:** carry handle, which locks into place. You've got um some really nice sturdy feet, which snap out into position like that. Uh it's got a USB host. Uh very important. Allows you to plug in a memory stick, get screen captures.

**Dave Jones:** And it takes a few seconds to boot up. One of the um I guess really the main annoying aspect with it I have is that it does actually have a fan. Uh it's not too loud, but it's uh it's it's certainly not like a a

**Dave Jones:** fanless unit like the TDS 210. Now, its big selling point, of course, is that it's got a 1 meg point memory. Um, and 1 gig sample per second sampling. Now, Rigol were one of the first Asian manufacturers to roll their

**Dave Jones:** own 1 gig sample per second uh front end, which is what they've actually refined and they've finally used in these units. And it works quite well. The firmware is really stable, and um and of course uh Rigol uh design and

**Dave Jones:** manufacture Agilent's or HP's low-end um scopes as well. So, if it's good enough for HP, it's good enough for me. Definitely thumbs up the Rigol 1000 E series. So, that's it for my first electronics engineering video blog. I

**Dave Jones:** hope you liked it and I'm after feedback. So, actually I'm after a really cool name for it. So, if you got any ideas for a name for the blog, let me know. Thanks. See you next time, I hope.
