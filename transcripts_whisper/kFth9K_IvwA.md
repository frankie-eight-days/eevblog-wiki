---
video_id: kFth9K_IvwA
title: EEVblog #713 - Voice Recognition - 1980's Style
url: https://www.youtube.com/watch?v=kFth9K_IvwA
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 36, "3": 51, "4": 76, "5": 96, "6": 116, "7": 136, "8": 156, "9": 171, "10": 186, "11": 201, "12": 221, "13": 236, "14": 261, "15": 276, "16": 291, "17": 306, "18": 326, "19": 341, "20": 356, "21": 371, "22": 391, "23": 406, "24": 426, "25": 446, "26": 466, "27": 476, "28": 496, "29": 511, "30": 526, "31": 541, "32": 556, "33": 581, "34": 596, "35": 611, "36": 631, "37": 646, "38": 666, "39": 681, "40": 696, "41": 711, "42": 731, "43": 746, "44": 766, "45": 781, "46": 796, "47": 811, "48": 836, "49": 846, "50": 866, "51": 876, "52": 896, "53": 911, "54": 931, "55": 951, "56": 971, "57": 1006, "58": 1036, "59": 1061, "60": 1086, "61": 1101, "62": 1121, "63": 1171, "64": 1211, "65": 1231, "66": 1266, "67": 1281, "68": 1301, "69": 1316, "70": 1331, "71": 1351, "72": 1371, "73": 1406, "74": 1421, "75": 1436, "76": 1456, "77": 1476, "78": 1496, "79": 1511, "80": 1536, "81": 1551, "82": 1571, "83": 1596, "84": 1611, "85": 1626, "86": 1651, "87": 1666, "88": 1691, "89": 1716, "90": 1736, "91": 1756, "92": 1776, "93": 1801, "94": 1816, "95": 1831, "96": 1846, "97": 1851}
---

**Dave Jones:** Hi. In a previous video about the downfall of RadioShack slash Tandy, I showed this VCP200 voice recognition IC. Dates from 1988, and Tandy used to sell this, Tandy as it's called here in Australia, at the local store. And I picked it up way back

**Dave Jones:** in the 80s. And it comes with the data sheet inside and everything. The plastic has yellowed over time due to the bromide in there, so yeah, it's seen better days. But anyway, I thought we would take this out. Oh, look at that. Beautiful.

**Dave Jones:** I thought we'd take it out and see if it still works after all this time. 27 years, 1988 vintage. Let's check it out. Now, even though it's got Motorola on there, this comes from a company called Voice Control Products, Inc. Hence the VCP.

**Dave Jones:** I don't know what the VCP1 on there, but the part number is VCP200 copyright 1988. And the reason it has Motorola on there is because this is a Motorola mask ROM microcontroller. A 6804 to be precise. So really old school stuff. So no, it is not a custom ASIC,

**Dave Jones:** but obviously they've got the magic firmware in there to do voice recognition. And the way you do that, of course, is to break speech up into individual phonemes, they're called. Each language has a unique set of phonemes. They can be like a different

**Dave Jones:** set of frequencies for a specific time period, all that sort of jazz. I won't go into phonemes, but that's how you do basic voice recognition. And in this case, this is a speaker independent voice recognition chip, i.e. it doesn't matter who you are, and in theory what your accent is, it should be able to

**Dave Jones:** recognize your words. It's got only a very limited subset of words in here, just some basic voice commands to operate a robot, you know, left turn, stop, reverse, go, all that sort of stuff. Or five, there's five particular words it can recognize, and then another mode where it can only recognize

**Dave Jones:** yes, no, or on, off. So it's very basic stuff, but it is speaker independent. So you don't have to train this thing at all, it should just work. Will it work after 27 years? I don't know, let's give it a go. By the way, I looked up the company

**Dave Jones:** and it looks like they're still listed, but I couldn't find a web page or anything like that. They're in New Jersey. I had a look at the Google Street View and it was like a laundromat or something. So yeah, I'm not sure what's going on there, but if anyone knows any

**Dave Jones:** details on who actually formed voice control products or where they are or what happened to them, then please leave it in the comments, because that might be a fascinating story. This might have been their one and only product. Wouldn't surprise me if this was like a little start-up

**Dave Jones:** spin-off from some PhD research paper or something like that. Perhaps that's how a lot of these things start up. They do their PhD thesis on voice recognition and they come up with some algorithms and tables and stuff like that, and bingo! They go into business and outpost this chip.

**Dave Jones:** Well, anyway, at least they sold them to Tandy. Everyone knew this thing back in the day and it was, yeah, they must have sold at least tens of thousands. And check it out, we've got ourselves the original data sheet with this thing. It's not actually, it's a more, you know, it's more

**Dave Jones:** like an application note than an actual data sheet, because all the proprietary stuff they've programmed into here, well, they don't want anyone to know about. So it's basically how to use the thing. And here it is, copyright 1988, Tandy Corporation, All Roads to Archer and Radio Shack are registered trademarks of Tandy Corporation.

**Dave Jones:** Archer. Ah, brings back so many memories. Anyway, as you'd expect with a voice recognition chip, it breaks things up and recognizes phonemes. So in this case we've got some predetermined stuff here. So it performs, well, claims it performs a spectral analysis of the incoming speech signal over 300 hertz

**Dave Jones:** to 5500 hertz bandwidth. Then it determines the membership of the phoneme classes based on spectral shape. That sounds complex. And then it forms strings of these classes and compares the strings to the stored listings of selected commands. And there you go. And it's basically got two modes.

**Dave Jones:** You can set with the pin strap up here, pin 19, you can set it to the command mode where it recognizes go, stop, left, right, and reverse for, you know, operating a robot, clearly, or just a basic yes, no, or on, off type command.

**Dave Jones:** And it tells you here it was designed for a relatively quiet environment, constant background noise such as fans, air con, or motors are usually accompanied by adjusting the input amplifier gain so the output signal does not exceed 1 volt peak-to-peak with speech input.

**Dave Jones:** So there you go. You've got to really tweak this thing. So intermittent noises such as slamming doors, loud music, or construction sounds are harder to deal with. A close-talking noise-canceling microphone helps so the occasional misrecognition might still occur. Occasional? I think it's, yeah, it's not going to be as great as it sounds.

**Dave Jones:** Hmm. And it claims it can get good performance up to 2 feet in quiet areas. Well, we'll test that. But ultimately what it comes down to, it's only designed to discriminate against words that it knows. So if, you know, it's not designed for use

**Dave Jones:** in an ambient environment where I'm just talking like this, for example, even though I didn't use any of the key phrases, it's just going to recognize them and pop it up. It's not that great. It is a very crude speech recognition device, only designed for

**Dave Jones:** the commands spoken to it. And they give you some application information here, how to do it, and a base, a little bit of a theory of operation here. And look! Printed circuit board pattern, or should I call it printed wiring board pattern. Oh, look at that.

**Dave Jones:** You used to photocopy these and then put them and then expose the negative film and then transfer that over and, oh goodness, those were the days. And we've got ourselves a basic schematic. And parts list here which, as I said, we'll scan all this in, put it down below, but this schematic is not

**Dave Jones:** very good. Look, they've done it like a chip-based thing, that's an LM324 op-amp. So I will redraw that and we'll go through it. So exactly what is this chip? Is it a custom ASIC? Well, no! It is just a mask ROM microcontroller, that's all it is.

**Dave Jones:** And in this case, it's a Motorola 6804. I don't know if it's a HC04, the high-speed CMOS version, or whether or not it's just the regular 6804. Anyway, this was the only data sheet I could find, the HC version. It's going to be exactly identical, you know, like functionality

**Dave Jones:** wise. And it's mask ROM micro, and not a very good one! It's an 8-bit job, it's got, look, it's got 1.6k of user program ROM, or barely that, or basically 1k. It's got 30 bytes of RAM, and basically, oh, it's got an on-chip clock generator,

**Dave Jones:** oh, fancy-pansy. And it's got a one 8-bit timer with a 7-bit pre-scaler, woo-hoo! And 72 bytes of user data ROM, so there's not much in here at all. It's very, very basic. And you'll notice, no, there is no analog-to-digital converter in here, so it has to

**Dave Jones:** accept a digital import. And we'll see on the schematic in a minute how it does that. So with basically like 1.5k of memory in there, of course this is all going to be written in Assembler. I don't know how they're fitting all this in.

**Dave Jones:** I mean, clearly, that, you know, they talk about doing, getting frequency spectrums and binning stuff and things like that. Obviously they're not doing that in real time in this process. So what they've done is that they've done all the theory and the math behind this and everything else,

**Dave Jones:** and they've come up with just a, like, just a basic lookup table. And that's, like, pretty much that's all it is. It's probably just working as a state machine, and just looking and comparing the input signals with a table, something like that. That's really

**Dave Jones:** all you can do in, like, 1k or 1.5k of memory, even in Assembler. There's just, you know, and it doesn't have the power to do any sort of, like, grunty real-time processing. So I'm pretty sure that's how it works, although they never released, as far as I'm aware, never

**Dave Jones:** released any of the algorithms or info for this thing. It was all proprietary. And I found this article, which I'll link in down below, which has some info on using the VCP-200 in a little project. This was in Radio Electronics magazine back in April

**Dave Jones:** 1991 by Daniel B. Cooper. G'day Daniel, I wonder if he watches. I wonder what he's doing these days. There you go. Not that long ago, 1991. Jeez, what was I doing in 91? I was working at Pacific Communications, I think. Yeah. So we've got a basic block diagram of what's going on here.

**Dave Jones:** We'll show you the schematic in a minute. Microphone, a big high-gain amp with a bandpass filter, and a comparator into the VCP-200. And he's got a schematic here which is practically identical to the Tandy application note there, just a couple of very minor value differences, things like that.

**Dave Jones:** But I don't think it's as well-drawn as it could be, so I'm going to redraw that and we'll go through it. And let's have a look at the DaveCAD drawing. I've redrawn it. It is basically identical to what we've got in sight in the Tandy one or in the other project.

**Dave Jones:** They're almost identical. But I've redrawn this part down here just to make it a bit simpler to understand. Obviously we've got the microphone over here. I've done videos on microphones before. This is a standard electric microphone input, so you need to bias it high

**Dave Jones:** with a 2K2 is by far the most common typical value to do that. And then they AC couple that, and they've got that going into an inverting amplifier here. You should recognize that if you put that down to ground. Of course, right there, if that was a ground symbol, you'd go, aha, that's an inverting amplifier, just because

**Dave Jones:** it's all hooked down here and all around the place here. Eh, just don't look behind the curtain there. It's fine, it's just confusing you. Just imagine that's at ground and that is an inverting amplifier. Now, we've got some filtering happening here. What's going on?

**Dave Jones:** When you've got a capacitor in parallel with a resistor like this here and here, this means that you're going to have some sort of high-pass filtering, i.e. as the frequency goes up, the AC resistance or the impedance of the capacitor goes down and reduces

**Dave Jones:** these values here and reduces the gain. So we're going to have some high-frequency roll-off there. But because, look, we've also got a coupling capacitor in here and over here on the second stage, any time you see a capacitor in series with a resistor

**Dave Jones:** like this, you go, aha, that is a high-pass filter because at DC, nothing's going to get through a series capacitor, is it? Look at the symbol. I mean, nothing's going to get through there at all. So it's going to have some sort of, based

**Dave Jones:** on the values here, the RC values, some sort of low-frequency roll-off there. In this case, for this circuit, I think it's about 500 Hz. I haven't actually checked the values or calculated anything, but that's what they say it is, so I believe them.

**Dave Jones:** And the upper frequency limit of this thing is around about 5 or 6 K or something like that, 5 or 6 kHz. So anyway, that's our first stage there. Then we've got a second stage here that's basically an identical stage where AC coupling that again, so we're going to have some more low-frequency

**Dave Jones:** roll-off and also some high-frequency. This is an optional capacitor. I have not fitted it in this case, but, you know, it should be fine. And if you wanted to increase the gain of this circuit, i.e. be able to recognize speech from a greater distance away, then you would increase the value of this resistor here.

**Dave Jones:** You could do both if you wanted to, but yeah, you'd probably just do this one here. And that would increase the gain and allow, you know, a greater distance between the microphone. The problem with that, of course, is that it picks up all the ambient background noise.

**Dave Jones:** So it's going to be a big trade-off between how loud somebody talks, how close they are to the microphone, and all these gain values in here. So they say the gain of this is around about 500 to 800. So I mentioned this thing here might have been a bit

**Dave Jones:** confusing. So once again, if you assume that's a ground, that's a ground, well you've got yourself a two-stage inverting amplifier, inverting amplifier with some high and low-pass filtering, i.e. it becomes a band-pass filter. So it attenuates at the low end and the high end, which is exactly what we want here.

**Dave Jones:** But what are they doing? Well, I actually forgot to put in the positive and the negative rail there, but we're powering this from a single 5-volt supply. This is an LM324, by the way. So we have to actually bias these up. If we had these at ground, it wouldn't work.

**Dave Jones:** It'd be clipping. We'd need a split supply. So what do we do? Well, we just raise this value up by some DC level, i.e. we're shifting the waveform up. We're adding a DC offset in there instead of ground. We're going up to a value set by this resistor divider here.

**Dave Jones:** So we've got our voltage supply, and that's going to be at some value, you know, like 2 thirds the supply value or whatever it happens to be, or half the supply value. And then they've got just some filtering on there to make sure it's a nice DC signal.

**Dave Jones:** So that shifts all of our waveform up into the operation, the center operational window of our op-amp there. Now, what's this puppy doing here? Well, because we've got ourselves a microcontroller here with no analog-to-digital converter, we can only feed in digital signals, i.e.

**Dave Jones:** a 1 or a 0, into the microcontroller. So if we just got our amplified waveform out of here, well that's an analog signal. We can't just feed that in a micro, that's going to be really ugly, it's not going to know what to do with it.

**Dave Jones:** So we need to square it up, i.e. clip the signals. So this is what we've got this for, this is a comparator. And you should recognize that instead of having negative feedback, like here, we've now got positive feedback. Positive feedback is a comparator.

**Dave Jones:** So they've got the 10 meg resistor here in combination with this adds a bit of hysteresis there, and we're also setting this offset here. And it's important to have this threshold value actually lower than our offset value there. So that's all that does.

**Dave Jones:** It squares up the signal, feeds it in there. It's not going to be a perfect square wave, but it's going to be good enough for the purposes here. So we're just using another 1 quarter of our LM324 op-amp as a crude comparator. Ideally you shouldn't use op-amps as comparators,

**Dave Jones:** they're very poor in that respect, but hey, it's good enough for something like this. What are you doing, Sagan? Show us. I'm putting on green LED and red LED. I found some green ones. See? Are you going to put some dropper resistors on there as well?

**Dave Jones:** Yeah, I'm putting them on right now. LED. Which colour? Red. What are we building up, Sagan? A circuit. What type of circuit? This. Yeah, a voice recognition circuit. Yeah. It's going to recognise voice, so you'll be able to tell it to start and stop.

**Dave Jones:** These are jumper links, aren't they? And you've got these too. Yeah, they're capacitors. We've got lots of mixed capacitors. These are ceramic ones. What are these? They are metal film. So I'm going to stick these on. Yes, I'm following it. You're following the circuit, are you?

**Dave Jones:** Yeah, I'm following it. And how old are you, Sagan? I'm three. You're three? Yeah. And you're pretty good at circuits, aren't you? Yeah. What is that? That's a breadboard. A breadboard. And these are pliers. Side cutters. That's right, show us. You want to show the camera the side cutters?

**Dave Jones:** Yeah, they're good, aren't they? And what's this, Sagan? A multimeter. Are you going to measure something? Yes. What are you going to measure? I'm going to measure these LEDs. Are you going to light up an LED? Yeah. You can do it. Are you going to use the Bryman instead of the Fluke, are you, Sagan?

**Dave Jones:** Yes. Why? Because this one is even better. You think it's better than the Fluke? Really? You think the Bryman is better than the Fluke? You want to stick that one in? Show me the tilting bail on it. It holds the meter up. It does hold the meter up, doesn't it?

**Dave Jones:** Is that a good one? Is that a good tilting bail, you think? Yes. It's got a good angle on it? And I can set this one up too. And what's this one? A Fluke. It's a Fluke, isn't it? A Fluke. Set them up.

**Dave Jones:** Here we go. And how many multimeters have you got? Two. Give us a thumbs up, Sagan. That's a finger. Show us a thumb. I just like a finger. You like the finger. Give us a thumb. You ready? Hold your hand out like that and raise your thumb.

**Dave Jones:** Yeah. Wave. Bye bye. Bye. Alright, we've built this sucker up. Let's see if she works. Left turn. Stop. Reverse. Turn right. Go. Reverse. Stop. Left turn. Turn right. Reverse. Go. Beauty. Bobby Dazzler. Bloody Ripper. Works a treat. No worries. And it's also got a second mode here, which is the basically just

**Dave Jones:** yes, no, on, off. So you just change the jumper link here and let's give it a whirl. Power on. Yes. No. Bloody oath. What a ripper. Not sure. Yes. No. On. Off. On. On. On. Off. Off. Off. Off. Yes. Off. Off. Off. Off, dammit.

**Dave Jones:** Off. There we go. And it actually seems to work a fair good distance from the mic as well. I can get up close like this and go. Go. Go. Turn right. Reverse. Stop. Left turn. So, but I can get like I'm one metre away.

**Dave Jones:** Go. Turn right. Turn right. Reverse. Nah, that's too far. Maybe 30 centimetres away. Go. Turn right. Reverse. Stop. Left turn. Eh, it's not bad. So it really is quite a, it's very touchy. It's designed not to have like an ambient room mic, it's designed to like have one of those

**Dave Jones:** push to talk type mics, you know, so you actually push to talk, talk into it, that sort of stuff. But it does work from like, you know, a good 30 centimetres away or so, so it's not too bad at all. But of course it's only designed to

**Dave Jones:** actually discriminate between the particular words that are being programmed in there. So everything else can just come up. Like I'm just talking normally here and it's just going to randomly flash LED's and things like that. So any other words, it's not designed to be like constantly listening to the ambient environment.

**Dave Jones:** As I said, one of those push to talk mics, you know, the old fashioned CB radio, you push to talk mic and go. And so you give it an instruction like that. So that's the limitation of this thing, but it actually does a pretty good job.

**Dave Jones:** So it's going to depend on your accent a little bit, but in general English, you can pretty much rely on that the phonemes are going to be broken up. And these are going to be reasonably identifiable, but I've found like if I speak too

**Dave Jones:** slowly or I speak too quickly, you've got to, you know, it won't actually register. You've got to speak with exactly the right, you know, timing, length. You can't speak too slow, too fast, you can't sort of shorten words or things like that. So it really is quite limiting technology, but it does basically work.

**Dave Jones:** So I think the particular algorithm they've programmed into here, it's designed for like a faster kind of speech pattern. So look, for example, left turn, stop, reverse, turn right, go. But if I go turn right, left turn. See, it's too slow, it doesn't get left turn.

**Dave Jones:** Left turn. Left turn. It did when I speak faster, so stop. Stop. Still gets it. Reverse. Doesn't get reverse really slow. Turn right. See, it turned it on before I'd even finished speaking the word right. Left turn. Turn right. It got it. Go.

**Dave Jones:** Go. See, it couldn't get a slow go. Eh, all right, I know you're going to want to see some waveforms, so let's just have a little poke around here, shall we? And I should be able to see my voice on the screen eventually.

**Dave Jones:** Let's have a poke at the, just out of the microphone now. Of course we've got it biased there with the 2K2, the electric microphone insert, AC coupled, of course, to couple that off, and that's going to be a very low signal level. Hence all this gain here.

**Dave Jones:** So let's have a look. I'm probing that point there, and check. Hello? There we go. If I speak really loudly, you can just see it. But it's pretty low level, so we need to gain that up with these two stages here. All right, so let's probe the output of this first stage

**Dave Jones:** here, pin 1. Here we go, you can see me talk into this thing. And let's give it a whistle, let's see what frequency I've got. And if we have a look at pin 7 here, the output of here, it's going to be a bit higher amplitude.

**Dave Jones:** Check, check, check, one, two, but there you go, you can see my voice very nicely on that, on the scope trace there. And the DC offset here of course is set by this value here with this resistive divider down here. So it's just setting a DC offset and shifting

**Dave Jones:** it up. But because we don't have any analog to digital converter in this little PCM micro, we have to convert it into a, we have to square it up and convert it into a digital signal which we can actually send into the micro.

**Dave Jones:** And that's what this does here. We've got ourselves a comparator. And so let's probe the output of pin 8, shall we? That was pin 7 we just had. There we go, there's pin 8. Ta da! Check, check. Now you can see how it's actually not perfect here, I mean there is still

**Dave Jones:** so if I speak softly like that, you can still see some crap in there because it hasn't actually gained that up as much. We've got a bit of hysteresis here with the 10 meg feedback. But if I get up close like this, here we go, left turn

**Dave Jones:** stop, reverse, turn right, go. So you can see how it's squared up the signal there which then goes into the micro and, well, it can discriminate against any other crap. But you can like, you know, you've got to tweak all these values. All these values are pretty critical depending on

**Dave Jones:** the signal level from the microphone and how close somebody is talking to it and all that sort of, and how naturally, how loud they talk. I'm a naturally loud talker, but... see I can we've definitely squared up our signal there. So that's good enough, obviously, to get into the micro and allow the micro to actually

**Dave Jones:** discriminate the individual words. And of course once you've got the signal into a digital form like that it's easy to just get... get the frequency of it and the time periods in there and match that against known patterns and then hence how they can actually decode the individual words.

**Dave Jones:** You just need enough discrimination in your analog circuit here. I mean, if we really gained it up, it'd probably be too much. You don't want to over-saturate your gain and like it picks up all crap, sort of crap ambient noise and stuff like that.

**Dave Jones:** So you know, it's fairly critical. I mean it's reasonably quiet here in the lab, well it's effectively a very quiet room, all it's picking up is this, but you know, if I tap on that, or if I yeah, if there was background, if there were people talking, like if I go like a couple of metres away

**Dave Jones:** whoop, hello, I'm a couple of metres away now, and check, I'm at the other side of the room, you probably can't hear me very well, but yeah I'm a good 4, 5 metres away now, and you can see it's just picking up all sorts of crap, so it probably doesn't know what to do with that.

**Dave Jones:** And of course based on the TTL input threshold levels of the micro, of course, then it's got to actually, you know, whether or not it's a 1 or a 0, it's going to be a bit iffy. So you've got to get the analogue portion of this just right and suited to your particular application and tweak.

**Dave Jones:** So it's a little bit messy, but hey, as you can see, it works. Left turn, stop, stop, left turn, stop, reverse, reverse, reverse, dammit! So what I've done here is increased the gain of this second stage, and this is our comparator output now, and as you can see, when it's just quiet here, we're getting

**Dave Jones:** crap out of there. If we have a look at the output, which is pin 7, there, let's have a look. See? We're just getting crap out without me talking at all. And obviously if you do that, so clearly it's not going to work anymore.

**Dave Jones:** Go, go, turn right, reverse, stop. It's just, nah, it's just got too much garbage there, so you can't have too high a gain, and you can't have too little a gain either, otherwise you're not going to get within the comparator threshold there and it's going to miss things

**Dave Jones:** and, well, it just won't be able to match it. So I hope you enjoyed that look at some really old school voice recognition, speaker independent voice recognition, and yeah, it does actually work. It doesn't do such a bad job at all. Go, turn right, reverse,

**Dave Jones:** stop, left turn, come on! Go, you little beauty! Go, you ripper, come on! No. Anyway. It's not too bad. Quite frankly, it's amazing what they achieved in this. I mean, it's a, you know, like 1.5k or maybe even 1k mask ROM microcontroller, and they're able to put speaker independent

**Dave Jones:** speech recognition into it. It's just, oh, absolutely fantastic. I mean, there weren't too many other options back in 1988 for doing stuff like that. You know, this was a probably a pretty good darn, you know, micro back in the day. So yeah, they squeezed it all in.

**Dave Jones:** Absolutely remarkable. Must be doing it with some sort of really highly optimized lookup table and state machine. That'd be my best guess anyway, how they're actually implementing that in there. Because there's no other way to do it, really, I think. So ah, fantastic.

**Dave Jones:** Hats off to them. It works. And still works after 27 years. Of course you'd expect it to. It's just a mask ROM micro. So if it can recognize strine, then, you know, it's pretty darn good. Don't mind that at all. Hope you enjoyed it.

**Dave Jones:** If you want to discuss it, jump on over to the EEVblog forum, link's down below. And if you liked it, please give it a big thumbs up on YouTube, because that helps a lot. I don't know, which direction is the thumb on YouTube?

**Dave Jones:** Is it that way or is it that way? I'm not sure. I think it might be that way. Anyway, catch you next time.
