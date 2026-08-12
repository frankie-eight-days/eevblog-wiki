---
video_id: oibJUt6QkwI
title: EEVblog #24 - Chopper Operational Amplifiers
url: https://www.youtube.com/watch?v=oibJUt6QkwI
source: youtube-asr
timestamps: {"0": 0, "1": 41, "2": 72, "3": 102, "4": 133, "5": 154, "6": 190, "7": 209, "8": 225, "9": 269, "10": 295, "11": 337, "12": 374, "13": 417, "14": 453, "15": 485, "16": 524, "17": 539, "18": 580}
---

**Dave Jones:** Hi, welcome to the EEVblog. I'm your host, Dave Jones, and this is episode number 24. Right, this week I thought I'd talk about component which not many people are typically know about or use all that often. It's the chopper amplifier. The it's a standard op amp, but it's called a chopper amp or an often called an auto zero amp. And basically what these are are they're they just they work just like a standard op amp except they have ridiculously low offset voltages. Like crazy low. Like your standard op amp,

**Dave Jones:** you know, a standard general purpose op amp might have 10 millivolts offset, 1 millivolt offset, you know, 0.1 millivolts, you know, for a really good one. But, you know, often that's not good enough for very high precision DC and low frequency applications. And and you have to resort to one of these chopper amplifiers or auto zero amplifiers. So, they're really cool parts and I'll explain how they work.

**Dave Jones:** I've got the inside circuitry, the internal circuitry of a typical chopper or auto zero amplifier. And this is how it works. Okay, you've got your standard op amp here. It's called we'll we'll actually call it A. We'll call it op amp A. It's got two op amps in it, op amp A and op amp B. Op amp A is your standard is the actual standard amplifier used to, you know, used as a standard op amp.

**Dave Jones:** Now, these op amp, you know, a regular op amp has an offset voltage VOS. And as I said, you know, a typical op amp that might be a millivolt or something like that. You know, which is quite large for precision DC applications. Okay? Now, what we would do is we want to zero that out. We want to null that out. That's what these chopper or auto zero amplifiers do. And the way it does this, it's got um four internal switches. Okay, these are internal switches. It's got a second op

**Dave Jones:** amp which also has its own offset voltage, same as this one. So, it's really quite neat how it's actually going to offset not only this one, but its own. This second amplifier is called the nulling amplifier and you have to offset this voltage as well. And we'll see how it works. It's really neat.

**Dave Jones:** Now, it's also got two internal sampling capacitors as well. Okay, and these are used to store the um offset voltages for compensation. So, let's have a look how it works. Basically, there are two phases in um to a chopper amplifier. It It actually alternates between these two phases, phase A and phase B. Um and basically, they're just different positions of these switches, these four switches here. So, let's go phase A, we'll call it. Okay? Now, in phase A, I've already set the switches to what they're like. This one is closed. This

**Dave Jones:** one is open. This one's closed and this one here is open. Now, as you can see, basically what it's doing is um we are compensating for this offset voltage here on this nulling amplifier. So, basically, it's this input voltage here.

**Dave Jones:** This switch is closed, so it measures its own input voltage between the positive and negative input terminals. And it stores that value on capacitor C1 here. It actually stores it on that and then feeds it back and offsets itself.

**Dave Jones:** So, this um this amplifier is effectively nulling its its input offset voltage. It's It's actually storing that voltage on capacitor C1. Okay? Now, this amplifier isn't doing anything at at here at the moment, except it's being offset by the voltage which is stored on C2. Okay? But, because we haven't gotten to that phase yet, okay? There's Assume there's nothing on here. Now, okay. So, this amplifier B has stored the offset voltage on capacitor C1 here. And then, it goes into phase B. And what happens in phase B?

**Dave Jones:** Is that Let me rub those out. The switches alternate. So, that one's closed, that one's open, that's open, and that's closed. Okay? Now, what happens is the previously stored offset voltage here is um actually offsets this amplifier. So, this nulling amp- effectively, we've canceled out this input offset voltage.

**Dave Jones:** It's been canceled out. Now, what that does is now these switches here are changed, uh this nulling amplifier is now measuring the input offset voltage on this amplifier, cuz it's fed through. Okay? It's measuring the VOS of the main amplifier. And it's storing that output on capacitor C2 here. Okay? And then, that value is fed through like this, to the back to the amplifier, and it offsets its own VOS voltage. So, that's all it does. They're the two phases. So, all it does is it alternates between

**Dave Jones:** these two phases at a fixed frequency, but I'll talk about that later. It alternates between these two phases at a certain frequency, and bingo! it alternates between nulling the offset voltage of these two amplifiers. And that's that's basically how it works. It's not It's not hard or magic at all. It's just basically storing some charges on some capacitors and swapping between them. And the end result is that bingo, this um your main amplifier here, the offset voltage is completely canceled out or, you know, effectively canceled

**Dave Jones:** out. It's magic. And that's how these chopper or auto-zero amplifiers can get incredibly uh low offset voltages like, you know, 1 microvolt instead of a millivolt, 0.1 microvolts, you know, really incredibly small offset voltages. So, that's how an auto-zero chopper amplifier works. Um if you're trying to use a regular op-amp at uh DC, they're they're very noisy. And um And And that's a real problem for precision DC applications or, you know, low-frequency applications. It's a real issue. And basically these um a chopper or auto-zero amplifier, because it uh

**Dave Jones:** effectively nulls out um uh DC offsets and very low-frequency signals, 1/f, those high-noise content ones are effectively canceled out by um chopper amplifiers. They basically don't have any 1/f noise, and that's really cool. That's a huge advantage. They've They've got their own disadvantages as well. Um the main ones are really they don't have a high uh bandwidth. They only have, you know, a couple of kilohertz, uh something like that, because the chop frequency is typically, you know, 10-15 kilohertz um or, you know, somewhere around that

**Dave Jones:** figure. The other problem with uh chopper amps is that um when you overload them, their recovery time can be quite slow, you know, it can be you know, 5 milliseconds, 10 milliseconds or something of that order. The other thing you got to watch out for when you're designing with chopper amps is charge injection caused by the switches. Now, this can be reduced by lowering the input impedance and your feedback resistors. So, you really got to make them as low as possible to get the maximum performance out of a chopper

**Dave Jones:** amp. Now, I actually used a Maxim MAX42 39 chip in my little adapter I've shown you before before for measuring our current. It's called the micro current. And I'll actually show you now a plot. This is actually a plot of the total harmonic distortion versus frequency for this chip, for the MAX4239. Now, I actually measured this using an audio precision analyzer, a really high-end analyzer, and you can see it spike at at at several frequencies there. The main ones are at about, you know, 7 1/2

**Dave Jones:** kilohertz or something like that. And I'll show you on the scope here exactly what that looks like when you get to high THD. And that's about 5 kilohertz mark, and let's increase the frequency and see what we get.

**Dave Jones:** Now, if we take it to about 7 and 1/2, where we saw that big spike on the THD, um uh plot. Now, look at that. There we go. That is the That is the high THD caused by the pseudo random fragment pseudo random sampling frequency of the MAX42 39. It It actually uses a pseudo random technique because that helps prevent um intermodulation distortion and things like that. So, there you go. That's what it looks like when you decrease the frequency and there's no problem at all.

**Dave Jones:** It's, you know, it's it's really smooth. So, you've got to watch out for that on on you know, chopper amplifiers in general. So, there you go. That's all about chopper amps.
