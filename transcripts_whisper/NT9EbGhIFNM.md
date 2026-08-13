---
video_id: NT9EbGhIFNM
title: EEVblog #5 - Maxim product marketing, Function Generator Review
url: https://www.youtube.com/watch?v=NT9EbGhIFNM
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 41, "3": 64, "4": 81, "5": 97, "6": 114, "7": 134, "8": 151, "9": 172, "10": 203, "11": 225, "12": 243, "13": 271, "14": 296, "15": 323, "16": 340, "17": 358, "18": 384, "19": 405, "20": 432, "21": 452, "22": 468, "23": 494, "24": 511, "25": 528, "26": 556, "27": 578}
---

**Dave Jones:** Hi, I'm your host, Dave Jones, and this is the EEVblog number... First up, something that ticks me off again. This time, it's Maxim. In fact, they've been ticking me off for a long time. Now, I like their parts. They make some of the greatest parts on the market, if you can get them.

**Dave Jones:** But that's another thing we need to talk about. But, yeah, it's to do with... what really bugs me is that... the way Maxim market their products. For ever since I can remember, it's always been, the world's greatest this, the world's greatest that. And there's always conditions to their claims.

**Dave Jones:** So they'll advertise parts as the world's lowest power, SOC 23-5 voltage regulator, with remote power down and under 10 cents. You know, it's like every part is the world's greatest, and the world's this and the world's that. And it's crazy. And lately, they seem to have, you know,

**Dave Jones:** the world's best has dropped out of favour, and they've got industry's best. You know, industry best. Industry best part that does this or does that. And there's five conditions on the end of it. It's nuts! Stop it! And, of course, the other thing Maxim are famous for is

**Dave Jones:** for having every one of their parts contain the rare element unobtainium. Because you just can't get Maxim parts. You know, they've got the best sample service in the business. You can get free samples, and it's fantastic. But you actually try and buy something in volume,

**Dave Jones:** and it's been next to impossible sometimes. So they lure you in with thousands of devices. They come out with, like, a thousand new devices per year or something. It's crazy. And, yeah, so they entice you with these new chips, and then you want to put them in your, you spec them into your product,

**Dave Jones:** and you find out, bang, I can't buy 10,000 of them. It's crazy. Well, they've got a 14-week lead time, 23 weeks. Unbelievable. They've actually publicly tried to counter this in recent times with, you know, the CEO or whoever coming out and saying, you know,

**Dave Jones:** oh, we, you know, care about, you know, supply availability. And it has gotten a lot better, I've got to admit. And you can buy them on the website too, which is quite handy. But it's never quite the temperature grade or some other grade

**Dave Jones:** or particular variation of a part you actually need if they've got it in stock. You know, Murphy's law of component supply. Now it's time for everyone's favourite part of the blog. Equipment review. This week, I've actually got something new again. And here it is.

**Dave Jones:** Ta-da! It's a function generator. Now, this one in particular is the Instek or Goodwill, as they're sometimes known. It's the very boringly titled GFG8219A 3MHz function generator. It's their sort of top-of-the-line model in this base series, if that makes sense. Now, there are two things you do when you get a new product like this.

**Dave Jones:** Number one, you take it out of the box and you... take in that new product smell. Step number two, don't turn it on, take it apart. Right, I've gone handheld this time, so let's take this sucker apart. There's one screw on the back here, which allows you to slide the case open,

**Dave Jones:** but it's got this tilt carry handle you have to take off. And in common with these handles, you have to get them to the right angle and then actually pull them out. Right, the handle's off, and we can just slide the case open like this,

**Dave Jones:** and let's have a look what's inside. Aha! We have a bunch of... discreet through-hole circuitry. It's all your traditional design. It's actually quite nice, I like it. It looks like it's going to be easy to repair, and it looks like it should be fairly reliable.

**Dave Jones:** Now, it looks like Instek have their own branded chip here. That's obviously the function genera... sorry, the frequency counter board, because it's hooked into the frequency counter display at the front here. What else do we have? These boards on top here look like they're the optional

**Dave Jones:** log linear sweep, or something like that perhaps, which are features not found on the base model units. And the circuitry is all fairly standard. It has an LM324. Pretty much recognise most of these parts. 7-4 series logic. Yeah, it's pretty good. Thumbs up to the internal construction.

**Dave Jones:** Now, at the back here, we have an internal and external counter switch, which is really nice. The 6-digit counter on the front you can actually use as a 150 MHz frequency counter. And it's got all the usual inputs. And it's got voltage selection, of course.

**Dave Jones:** And a little tiny fan, which isn't too loud at all. It's very quiet. OK, so we've turned it on and we've got it going, and... First thing I notice is that the waveform is jumping around like a jack-in-the-box. And you can see on the display as well,

**Dave Jones:** it's certainly not stable to any degree. So, obviously, there's instability right at the bottom end of the scale. Now that's really quite dodgy, I think. And that doesn't seem to be affected by range either. Now we're up on the 100 kHz range, and right at the bottom end of the frequency scale,

**Dave Jones:** it's doing the same thing. It's jumping around like a jack-in-the-box. And you go up to mid-scale, and it's nice and stable again. Now, this unit also has AM and FM modulation as well, which is set by this switch. So let's pull it out.

**Dave Jones:** Modulation on. And we can increase the level, and we can see that that's amplitude modulation. And we push it in for frequency modulation. So it all works as expected. And, of course, there's the usual duty cycle adjustment, so we'll just give that a go.

**Dave Jones:** And, yeah, it works. And probably from about 80% down to 20%, which is pretty usual. The things I like about it, though, is that it's got pretty much every bit of functionality you could want in a sort of mid- to low-end analog function generator.

**Dave Jones:** And the frequency display is really good in hand. You can use it as a frequency counter. Well, a low-end frequency counter, but, yeah, it's got pretty much all the basic functionality you need, plus a few nice extras. They cost around 300 US each,

**Dave Jones:** which is pretty much par for the course for this type of 2-3 MHz type analog generator. But, really, I'd much prefer the new digital DDS ones. They're much more stable, and they probably offer more bang per buck. So the verdict? Well, I think it's probably a thumbs sideways.

**Dave Jones:** I wouldn't give it a thumbs down or a thumbs up, because I really have concerns about the waveform stability at the low end of the frequency scale. Now, to be fair, this isn't the first time I've seen this in a mid-to-low-end analog function jet.

**Dave Jones:** It's not that uncommon a problem. But, still, this is probably one of the worst I've seen, perhaps, and it's just not that great. So you need to be wary of it, definitely. Now it's time for chip of the week. Once again, it's not just a chip.

**Dave Jones:** This week it's a whole bunch of analog products from, surprisingly, Microchip, the guys who do the PIC processors. Now, normally when you think you need a regulator or an op-amp or some other analog device, you turn to one of the major players, Maxim, TI, National, Analog, LT, guys like that.

**Dave Jones:** But lately I've found I've been turning more towards the analog products from Microchip. And they make ADCs and DACs and programmable gain amps and interface chips, and lately I've been finding I've been turning towards them a fair bit when I want an analog device.

**Dave Jones:** Because they're usually, most of them are really low power and they're cheap, they're really cheap, and they're available off the shelf, unlike Maxim products, for instance. Yeah, so next time you're in the market for an analog device, try Microchip.
