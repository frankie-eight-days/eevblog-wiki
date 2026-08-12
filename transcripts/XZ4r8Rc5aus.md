---
video_id: XZ4r8Rc5aus
title: EEVblog#160 - 555 Timer Easter Egg?
url: https://www.youtube.com/watch?v=XZ4r8Rc5aus
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 29, "3": 41, "4": 53, "5": 68, "6": 83, "7": 97, "8": 116, "9": 130, "10": 145, "11": 160, "12": 175, "13": 189, "14": 199, "15": 213, "16": 226, "17": 237, "18": 254, "19": 272, "20": 288, "21": 308, "22": 324, "23": 344, "24": 358, "25": 375, "26": 396, "27": 408, "28": 431, "29": 445, "30": 469, "31": 486, "32": 502, "33": 519, "34": 537, "35": 556, "36": 572, "37": 592, "38": 616, "39": 627, "40": 648, "41": 664, "42": 681, "43": 698, "44": 709, "45": 720, "46": 736, "47": 755, "48": 774, "49": 788}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, as you may know, I've been involved a little bit in the 555 design contest that

**Dave Jones:** Chris Gamell and Jeri Ellsworth put together because I'm judging the Australian aspect. There's an Australian prize which I'm giving and I'm going to be judging that. So, I couldn't really enter the contest. I'm too close to it. So,

**Dave Jones:** I tweeted some time back that I was actually going to do my own 555 timer circuit just for fun, you know, enter it and make a good blog anyway, I thought. So, yeah, I go ahead with it. I

**Dave Jones:** was playing around with the damn thing and it it was just playing up on me. I found this weird quirk and I it took me ages to track the damn thing down and I've finally done it and let me show you

**Dave Jones:** what I found. It's really interesting. As you may know, the 555 timer was designed by a guy called Hans Camenzind and he's famous for it as well as other stuff as well and he's actually judging the 555 design contest which is totally

**Dave Jones:** cool. But, he's always publicly said that the that the number 555, 555, not this triple nickel rubbish, has was just an arbitrarily assigned number. But, if you look at the internal circuit and I just so happen to have it here on my

**Dave Jones:** t-shirt, there are famously five resistors in there in the standard version. It isn't the same in the CMOS version, but anyway, there's a 5K, 5K and 5K and it's publicly claimed it's not, you know, it's just a random

**Dave Jones:** randomly assigned number. But, everyone in the business knows that's complete Now, there's also been I heard a rumor like decades ago that he added something else in the chip as well as a little mark for the 555, but nobody's ever found it and

**Dave Jones:** you know, he's denied that as well, but I I'm not sure. I'm not going to claim it, but possibly I might have found something, and it needs to explain it. Let's Let's have a look at it. Now, here's the circuit I built up on

**Dave Jones:** breadboard. It actually took me some time to actually do this. I'll show you up close in a minute, but here's the DaveCAD drawing of what I've actually got here on the breadboard. I'll show you up close, but it's you'll recognize it's a

**Dave Jones:** standard astable 555 timer circuit. You know, pins eight and four up there, one to ground, and it's just a standard configuration, but I've added an adjustable pot up here so I can adjust the frequency, and I've tweaked this

**Dave Jones:** value with a couple of parallel series and parallel resistors in there just to tweak it to get to the exact frequency, which you'll find out actually matters. And, one of the key things is I haven't got a capacitor going to ground on pin

**Dave Jones:** five. Now, that is a recommended configuration. They recommend like a 10 nF capacitor to on pin five to ground, but my circuit that I was playing around with didn't have that, and I realized that you that is the key one of the keys

**Dave Jones:** to this. There are two keys to this, which you'll find out, and I just added a low pass filter to the output so that I can see some stuff, as you'll see later. But, let's check out the circuit on the

**Dave Jones:** board. And, here it is, wired up exactly as per that DaveCAD drawing. Here's my adjustable pot up here, which I'll use to adjust the oscillator frequency. That's my low pass filter there, and I've got a bypass cap on there, but as

**Dave Jones:** you will see that won't have any impact on this. Now, let's take a look at the problem and see what we get. As you can see, I'm probing the output here. This is the pin three output, and I'm also

**Dave Jones:** probing the output of the low pass filter here, and you'll note that there's no bypass cap on pin five, and as you'll see later, that's pretty key to this whole thing or it's one of the keys. There's a couple of keys to this,

**Dave Jones:** but let's see. And I'm measuring the output now, and as you can see, it's about 55.2 kHz, okay? Just over 55 kHz. Now, I'll see if I can get all this in the shot here. Sorry, it's hard to get the frequency and pot and

**Dave Jones:** everything, but let's see if we can recreate the problem I've been having. I've got my adjustment pot here, and let's wind up the wick on this thing. Let's Is that in shot? Yep. Okay, let's wind up the wick on this and see

**Dave Jones:** Watch the frequency over here. Once it gets to 55.5 Hz, you'll see something rather remarkable. I've got some averaging turned on here just to stabilize it because the 555 is not the most stable beast. And as you see,

**Dave Jones:** it's starting to get a bit wobbly. Now, as you can see, it Once it hits 55. 5 Bingo! Look at that. It's jumping around. And if we go past that, if we go past it, okay?

**Dave Jones:** We're we're out. So, let's go back down to that. There we go. That what That Have we got it? Have we got it? I think we've got it. All right. And look, it's modulating. It's something. Look, it's it's wobbling all over the place. That's

**Dave Jones:** because of the averaging. So, if you turn the averaging off, okay, let's turn the averaging off and look at Look at this thing, okay? Look. Look, there's modulation on there at 55.5 kHz. 5 5 5. I you you know,

**Dave Jones:** what can you say? I don't know. We I need to investigate this a bit more, but let's actually do this. What I've got is the low-pass filter up here. Okay, so let's we have to go trigger off channel two

**Dave Jones:** here. So let's trigger off our second channel up the top and look at that. Look. Look at what we've got. That that filter, that low-pass filter down in the circuit down here is just taking out effectively taking out the 55.5 kHz

**Dave Jones:** carrier frequency as you know, to want of a better term and it's it look at the output here and that's on frequency two. Look, it is 55. I'm not kidding you. It is 55 .5 Hz modulation. We can turn the

**Dave Jones:** averaging up a bit more here. Let's Oh, sorry. That that that is no averaging. Let's turn the averaging on. Okay, and you'll see that the other whoop, sorry. You'll see that the other waveform disappears of course because we're now

**Dave Jones:** averaging and check it out. Look, the frequency of that channel the modulation is 55.5 Hz at um at 55.5 damn kilohertz in this circuit. What the hell is going on? It's nuts. Okay, so what I'm going to do now is

**Dave Jones:** I've got a 10 nanofarad cap and I'm going to put that as per the application notes on pin five of the chip and see how much it where where where still modulating here. Look, it's still I haven't I haven't

**Dave Jones:** adjusted that pot any further. So let's let's whack this on here at um where is it? Whoop. Hang on. Hang on. I'm going to have to uh pin five.

**Dave Jones:** And check it out. Look, there is no more modulation. It's It's nuts. What's going on? And right, if you Well, that's for the application though. It's probably not, you know, cuz that's how you're supposed to use the device. And that's why

**Dave Jones:** probably no one has ever found this thing. But, look, if you if you physically remove that cap, look, the the modulation just It It comes back. It's nuts. Now, if you're thinking like I was that maybe it's got something to

**Dave Jones:** do with my external 5-V external bench supply I'm using here. But, um and maybe it's some weird uh decoupling effect because the frequency of the triple five um can actually be Well, you know, it can be sensitive to your power very

**Dave Jones:** sensitive to your power supply rails. But, let me So, I thought like it was the decoupling cap, but let's physically remove the decoupling cap off here. Well, and it still doesn't. I mean, there's the extra ringing, right? Because there's no decoupling on there,

**Dave Jones:** but the modulation still remains. It's still doing exactly the same thing. And if we uh and if we change that, if we go trigger off uh channel two again, and if we boop boop boop, we've still got that 55.5

**Dave Jones:** Hz modulation. It's crazy even with the decoupling cap gone. Yeah, I know what you're thinking, that wasn't good enough for me, either. So, what I've done is I've um uh I'm powering it now from a battery pack. I've completely disabled these uh

**Dave Jones:** inputs in my external uh supply. And um look, it it it's exactly the same. Exactly the same modulation. And I'm it's just nuts. If we go in and we trigger off channel two again, and we sweep it down, and there it is. It is

**Dave Jones:** still 55.5 hertz modulation when you hit 55 uh, .5 kilohertz. And of course, with that uh, battery circuit, because the battery will actually change the um, the battery would actually physically change the frequency uh, because it is it's not spot on five, it's about 5.3.

**Dave Jones:** I've got a couple of alkalines and some rechargeables in there. It's about 5.3. So, I had to re-tweak the pot, but that's all I had to do to get it to do exactly the same thing as what we had

**Dave Jones:** before. Now, I want to know how the bloody hell it's doing that when there's just, you know, it it's the um, there's it's just a standard S astable 555 timer circuit with uh, without the control um, modulation capacitor on uh, pin five to

**Dave Jones:** actually um, stop any uh, modulation or oscillation or stuff like that. And you still get the 55 hertz output. You whack that cap on and it just vanishes. That's per the application note. But, yeah, sure, I was trying to use the thing outside of its

**Dave Jones:** application note specification, but I found something really, really interesting here. And in case you're wondering what uh, chip I'm actually using, it is a National Semiconductor uh, chip. It's sorry, it's hard to it's hard to really get chips. You've got to get the light

**Dave Jones:** right, but I've actually tried um, a TI brand chip, and it's exactly the same. It's exactly do same thing. So, it's not just uh the National uh Instruments device. It It seems to be Well, it's at least across two brands.

**Dave Jones:** So, if other people can try out other brands and see if it does exactly the same thing, we'll see if this is across the board on all triple fives. So, there you go. That's the most bizarre thing I've ever seen. I came

**Dave Jones:** across this when I was breadboarding my little vero board uh circuit. I was getting all sorts of little funny things cuz I was trying to do something weird with it for the contest. So, I wasn't using the um

**Dave Jones:** I didn't have the standard bypass cap uh to ground on the control pin. And I was getting And it took me ages to narrow this damn thing down to 55.5 kHz, and then the damn thing modulates. And I've tried two different devices

**Dave Jones:** from different manufacturers. It does exactly the same thing. It only happens at 55.5 kHz, and it only happens if you have the uh control pin uh not connected at all, and you get the 55.5 Hz modulation. It can't be a

**Dave Jones:** coincidence. Surely. This is a triple five timer. IT'S FAMOUSLY GOT THE 555 RESISTOR in it at 55 kHz, 55.5 Hz modulation. It can't be. So, I've got to uh get in contact with Hans and find out uh what's going on here because

**Dave Jones:** I don't know, but something smells fishy. SO, I DON'T have the CMOS triple five to try out um or other brands. These are the two I had in stock here. So, build it up and let us know. Take a video. Let us

**Dave Jones:** know if you can actually get confirm this the same thing is happening. Catch you later.
