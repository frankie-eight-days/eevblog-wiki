---
video_id: JobJswHcnLE
title: eevBLAB #8 - New Tektronix AGO3000 Oscilloscope
url: https://www.youtube.com/watch?v=JobJswHcnLE
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 20, "2": 41, "3": 61, "4": 83, "5": 110, "6": 130, "7": 146, "8": 159, "9": 184, "10": 206, "11": 222, "12": 242, "13": 258, "14": 283, "15": 302, "16": 323, "17": 346, "18": 361, "19": 381, "20": 398, "21": 414, "22": 427, "23": 451, "24": 468, "25": 481, "26": 502}
---

**Dave Jones:** Hi, welcome to another EEVblab. This one should be reasonably quick. It comes from the forum yet again. The forum never ceases to amaze me. The manufacturers cannot hide anything from the forum members. They just find everything before they're released. It's fantastic. Awesome, guys.

**Dave Jones:** It turns out that Tektronix, it looks like they're releasing, I don't know when, but they're going to be releasing a new scope. It looks to be based on the MDO3000, which you've seen a lot of. It's called the AGO3000 series data sheet, and somebody on the EEVblog forum,

**Dave Jones:** sorry, I forget who it is, found the LinkedIn, the data sheet, or a pre-release draft data sheet to the new AGO3000 series. From what I can see in all the specs, it looks like it's basically exactly the same as an MDO3000 with one major difference, which we'll take a look at.

**Dave Jones:** Now, this isn't surprising because Agilent Keysight, never get used to Keysight, Keysight just released, of course, well, recently released their 3000T series, the touch one, which you've seen in a previous video. And that was kind of sort of a knee-jerk reaction response to Tektronix MDO3000.

**Dave Jones:** They tried to one-up them, and the manufacturers continually try to one-up each other. It's relentless, and it looks like Tektronix are going to respond to that soon. The new AGO3000 series scope is what's called a gravity compensated scope. And this one, I find interesting, because I did a video on this, I don't know, what was it,

**Dave Jones:** you know, 9 months, 12 months ago, I'll link it in down below, I might even maybe edit in a little thing-o from it, where gravity can have an effect on reference crystal oscillators. And I've got my, this is linked to the previous video, I'll do it in a bit more detail, but

**Dave Jones:** I've got my CSIRO rubidium frequency standard here, and I've got my Agilent frequency counter here, and what's it, sorry, I can't see, I can't see on the LCD. What's it displaying now? Okay, it's displaying 999, it's pretty close to the nominal 10 megahertz, okay?

**Dave Jones:** But if I, or 998 or whatever it was, put the tilting bail up like that, what do we get? We get 999. It actually changes when you tilt it, and it's going to change fairly drastically, well, drastically, if I turn it upside down.

**Dave Jones:** What's it reading now? There you go, 989. It's changed by 10 digits there. Look, hopefully you can see that. Alright, sorry, my leads aren't long enough here, but we turn that over, and ta-da! And that's, you should see it change by, I don't know,

**Dave Jones:** 10 least significant digits there, or, you know, .01 hertz, which is about one part per billion. If I've got my decimal places wrong, I often mix them up. Anyway, one part per billion, and that's, what this effect is, is called the 2G tip-over effect.

**Dave Jones:** And, as I said, done a previous video on it, so check it out. But it's interesting that tech are releasing a new scope that actually compensates for this well-known, well, not really well-known, but in the, you know, the industry I come from, seismic industry,

**Dave Jones:** very well-known that the orientation of crystal oscillators changes based on the gravitational field. That's what happens. It's a real phenomenon. It's not much. We're talking, like, typical in the order of, you know, 1 to 10 parts per billion. So you need, like, an 11 or 12 digit counter to actually see it.

**Dave Jones:** That's why it's not normally a problem in scopes. But what tech have done with this new one is the only difference I can see between the MDO3000 and the new AGO3000. What does AGO stand for? I don't know, Advanced Gravity Oscilloscope or something.

**Dave Jones:** Anyway, yeah, figure out your own name. They've added a TCXO reference oscillator because this is the other thing Keysight added. This is the thing Keysight added to their 3000 Touch series was a higher stability reference oscillator. And tech have obviously gone, well, we're going after that market, too, of the high stability oscillators.

**Dave Jones:** So they've not only whacked in a TCXO, which has, it's a real schmick one, 0.05 ppm, typical. Keysight went from, like, a 5 digit frequency counter to an 8 digit frequency counter. Seems like the new tech scope has a 12 digit frequency counter.

**Dave Jones:** Awesome. Everyone's one-upping themselves on the frequency counters. Fantastic. So, when you've got a 12 digit frequency counter like this, it matters. The orientation of the thing matters. Just doing the tilting bail like that matters. So, you know, major applications for this, like airborne applications when, you know,

**Dave Jones:** you're using a scope in a plane for military applications and stuff like that. The industry I come from, vibration is a big thing that can also affect your horizontal time base, which is derived from the internal reference in this thing. So it's all great to have a TC, temperature compensated crystal oscillator in there, and a real precise one.

**Dave Jones:** But if you tip the feet up and it's going to change, well, that can be a huge deal. So what they've got is, let me read all the wink, is proud to introduce the world's first oscillor capable of eliminating the effect of gravity

**Dave Jones:** through a patented electromechanical gravitational field sensor and extensive calibration. The gravitational field sensor detects the orientation of the scope's crystal, that's not rocket science, and then corrects for any errors. So they've obviously got some sort of look-up table which they programmed during the calibration.

**Dave Jones:** And it says that they have a nine-day factory calibration on this new AGO series scope, as opposed to a couple of hours which it takes them to calibrate the MDO3000. There you go. So unheard of levels of time base precision, blah, blah, blah.

**Dave Jones:** So it's a gravity compensated oscilloscope. Awesome! And well, oh, I can see everyone trying to one-up themselves. Keysight will probably go, oh, crap, we have to now release a gravity compensated scope. Rigol will probably figure out a cheap way to introduce it in there,

**Dave Jones:** because you could probably use it with a, you know, just a cheap MEMS accelerometer. You can probably do it with that. They're using some sort of electromechanical thing in this new scope. To go along with it, the specs here, which I'll link in.

**Dave Jones:** Gravity compensation, 0.01 parts per billion. You know how I told you that it's typically going to change by one part per billion? Or ten, one to ten, if you flip the scope or the frequency counter or your oscillator upside down. Well, they're claiming 0.01 parts per billion maximum for a plus minus 2.5 G range

**Dave Jones:** over a five to five hundred hertz vibration. So there you go. I have no idea when it's coming out. I'll try and get one, because I'd love to have a look at the gravitational, mechanical gravitational field sensor thingo in here. Awesome, Tektronix leading the field yet again.

**Dave Jones:** Gravity compensation, probably look out for gravity compensation in upcoming, you know, in the next year or two, Keysight and Rigol scopes too. So there you go. That's just quick blab. I think I waffled too much. As usual, I'll link in the data sheet down below.

**Dave Jones:** Check it out. I'm rather excited by gravity compensated scopes. I want extra precision in my scopes. You know, tilt and bail like that can affect your horizontal time base. No thanks. Give me gravity compensation. Anyway, I'll see if I can get one, and we'll do a teardown.

**Dave Jones:** Catch you next time.
