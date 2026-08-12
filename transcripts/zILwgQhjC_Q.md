---
video_id: zILwgQhjC_Q
title: EEVblog #646 - Gravity Detection Using A Frequency Counter!
url: https://www.youtube.com/watch?v=zILwgQhjC_Q
source: youtube-asr
timestamps: {"0": 1, "1": 18, "2": 38, "3": 57, "4": 71, "5": 87, "6": 101, "7": 115, "8": 132, "9": 152, "10": 169, "11": 183, "12": 200, "13": 214, "14": 228, "15": 245, "16": 263, "17": 280, "18": 295, "19": 309, "20": 324, "21": 340, "22": 355, "23": 371, "24": 383, "25": 396, "26": 410, "27": 424, "28": 440, "29": 458, "30": 474, "31": 488, "32": 503, "33": 515, "34": 531, "35": 543, "36": 560, "37": 574}
---

**Dave Jones:** Hi, here's something I bet you didn't know. Your humble frequency counter here can actually change frequency depending upon its orientation. Don't believe me? Let me show you. I've got my Agyant 53131A frequency counter here. An excellent frequency counter. It's got a built-in

**Dave Jones:** uh high stability ovened uh reference oscillator and it's measuring uh the 10 MHz reference frequency from my external uh CSRO rubidium frequency standard here. Watch what happens if I just increase the tilting bale. Put the tilting bale up. Look at that. It's

**Dave Jones:** changed. Magic. It's changed by uh 3 mill there. If I put it back, it's changed back to exactly where it was before. Why is it so? Well, the reason for this is that the internal uh quartz crystal oscillator in this thing,

**Dave Jones:** be it an ovenized one like this, which is kept at a stable temperature, or be it the uh generic internal one that you're familiar with with using as you know, your 10 MHz reference oscillator on your microcontroller, for example.

**Dave Jones:** They're all quartz crystal oscillators and they're susceptible to many different forms of uh environmental uh things like for example everyone knows there they change with temperature of course they'll have a certain temperature spec they'll drift with temperature they have an aging

**Dave Jones:** characteristic so every year they'll age by a certain amount and they have voltage dependency all sorts of things and not only that but also uh physical shock and vibration as well. Now, as it turns out, I've actually done some

**Dave Jones:** research on this at a former company I used to work for, and you can actually reset the drift characteristics of a typical quartz crystal oscillator by impacting it with a certain shock or vibration. So, what's going on here

**Dave Jones:** actually has nothing to do with shock or vibration or temperature, thermal gradients inside the other or anything like that. What it is is uh related to the shock and vibration in that the physical crystal inside vibrates and that is actually susceptible to gravity.

**Dave Jones:** Believe it or not, yes, gravity. You can't escape it. You can actually use your frequency counter to detect gravity. And by physically changing it like that, you're actually changing the vibration characteristics of the crystal because you're changing its orientation

**Dave Jones:** relative uh to the gravitational field. So if I turn it over like that, for example, we will see it change yet again. And look at this. You'll notice that it's changed by roughly uh 4 mz there. If I turn it all the way over, it

**Dave Jones:** should double. That difference should double. And yeah, it pretty much does. So, it went from 4 MHz above to basically 4 mill below or thereabouts cuz we don't have the resolution. We'd have to go to a greater gate time there

**Dave Jones:** to get better resolution. But you can see that we can actually detect gravity because when you turn a crystal upside down, you're changing its physical vibration properties relative to that gravitational field. So when you actually calibrate instruments like

**Dave Jones:** this, you've actually got to calibrate them in a specific orientation. And just changing that tilting bale like that, you think nothing of it, but you could do that. And if you're talking about serious measurement, look, I mean, we're

**Dave Jones:** easily we can get this frequency counter to go to another digit resolution after this. But that's the sort of impact you can that gravitational fields can have on quartz crystals. Who knew? And it turns out that your average quartz

**Dave Jones:** crystal has a gravitational change of roughly uh 1 * 10 - 9 per g. So that translates to on a 10 MHz uh signal, 10 MHz crystal like this, uh 0.01 hertz basically per G. So take your humble

**Dave Jones:** quartz crystal here and let's crack this thing open and actually see what's inside this thing. And after you carefully slice one open, ta, we're in like Flynn. And that is what's inside your typical quartz crystal that you're used to

**Dave Jones:** using. There's a a big circular slither of quartz there with a couple of electrodes on either side and that thing vibrates. And that's how crystal oscillators actually work. But as you can see by the orientation of that, if

**Dave Jones:** you orient it in that direction, gravity is going to have a different effect than if you orientate it in that direction. As very minor as that is, as very small as that gravitational effect is, it does actually make a difference. Now, you

**Dave Jones:** might be a bit puzzled as to what's actually going on here. Why does it make a difference if we suddenly like flip this axis of the crystal over like this, i.e. we go like that and we turn it over

**Dave Jones:** or whichever way you want to uh do it. isn't the force of gravity down towards the center of the earth for example like 1g it's still 1g pointing down on the crystal why does that make a difference well you got to remember that the

**Dave Jones:** crystal was measured i.e you know, calibrated cuz this is a frequency. It's a reference, for example. Uh, then that was actually calibrated with it in this orientation with 1g being applied to say this top surface here. So, you've got

**Dave Jones:** positive 1g coming down on this top surface. And when you flip it over like this, it was one frequency in that respect before, but now you've got one positive 1g on this surface. So you've effectively got negative 1g reference

**Dave Jones:** from the other side. So that's why you get a total difference figure a total frequency change of 2G when you flip it over. And hence why this phenomenon is called 2G tip over. And it's a very common thing. You flip a crystal over

**Dave Jones:** like this on a bench and you get a difference of 2G. Now as I said it does change with the cut, what's called the cut of the crystal as well. And a typical SC cut crystal is as I've said

**Dave Jones:** uh you know roughly uh 1 * 10 - 9 or one part per billion. But your say your at cut crystals they can be like an order of magnitude worse than that. Now what we've actually seen here is very low

**Dave Jones:** values of G. We're just basically changing the orientation like that. So it changes by 2G when you flip it over which is basically uh nothing really. The real problem with these things comes about when you start to move them. I.e.

**Dave Jones:** you're up in a plane or something like that or you're some other thing which is moving accelerating all over the place. Well, you can have really big problems with uh stability of your oscillator. So, it's a really huge deal. Now, you

**Dave Jones:** might be wondering, does this 2G tipover effect apply to atomic frequency standards like this rubidium uh frequency standard I've got here? uh does it have that same 2G tipover problem? Because if you know the uh block diagram of how a Rubinium

**Dave Jones:** frequency standard works, it basically has a regular quartz crystal in there which is then frequency locked to the atomic um physics package inside there. So 2G tipover will apply of course to the quartz crystal inside this thing. But because it's with inside a survey

**Dave Jones:** loop locked to the uh atomic rubidium frequency physics package inside there then it the frequency will change the output of the rubidium standard will change but it uh its frequency will be dependent upon how fast the servo loop

**Dave Jones:** can act and actually correct for that change. And there are other physical effects like if you that's if you just rotated the crystal inside there. But of course if you entire if rotated this entire package then the rubidium

**Dave Jones:** standard itself uh the actual rubidium inside the element in there can uh diffuse in a different way and you can get physical effects that way. Um but it's not the same 2G tip over effect that you get in the quartz crystals. So

**Dave Jones:** it can affect it. So certainly if you were, you know, if you're in a calibration standard lab and you had an a rubidium frequency standard like this, you wouldn't be going tipping the thing over. That's for sure. But really, it's

**Dave Jones:** not something you really have to worry about unless you're absolutely critical uh talking about your rubidium uh standards there. Certainly not in the same league as what we see here with our uh quartz crystal ovenized oscillator. Not even close. these things. Yeah, you

**Dave Jones:** can just measure it on your basic frequency counter and there is plenty of great research out here on this and it it does make fascinating bedtime reading if you're interested in this sort of thing. So, I hope you found that

**Dave Jones:** interesting and you've gained a new appreciation for what happens when you tilt your tilting bale like that little insignificant change to your instrument can have a significant impact upon your measurements. can even change the calibration of your instrument. There

**Dave Jones:** you go. Fascinating but true. And it can be a really big deal in uh some applications. As I said, when things start moving, we're just got a basic frequency counter on the bench here. And we can measure it easily. We can even

**Dave Jones:** measure it with more precision than this if we really want to. So there you go. Hope you found that interesting. If you did, please give it a big thumbs up. Catch you next time.
