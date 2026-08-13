---
video_id: liXaHJLn6Ps
title: EEVblog #1051 - 121GW Multimeter Mass Turbulence
url: https://www.youtube.com/watch?v=liXaHJLn6Ps
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 20, "2": 38, "3": 63, "4": 86, "5": 110, "6": 135, "7": 150, "8": 187, "9": 214, "10": 229, "11": 244, "12": 268, "13": 297, "14": 317, "15": 340, "16": 359, "17": 377, "18": 399, "19": 419, "20": 441, "21": 462, "22": 483, "23": 503, "24": 528, "25": 544, "26": 569}
---

**Dave Jones:** Hi. Very excited. We finally got in the 121 GW multimeters. They've been a long time coming, let me tell you. And they were supposed to come in like mid-December or something when I took pre-orders on the website for supporters and things like that.

**Dave Jones:** Sorry, they've been waiting for these things. As, of course, all the people on Kickstarter, the early backers. But, we finally got them this morning after a few little delays at the port. So, let's open them up. This is a box of 32 per box.

**Dave Jones:** So, we're just going to open one box and do some cow stuff. Ta-da! Here we go, look at this. This is actually the first time I've gotten more than one or two like, sort of, you know, production or pre-prototype units. And it's the first time I've seen the box and everything finished.

**Dave Jones:** There it is. Made in Korea. The EEVBlog No Bullshit Packaging for the 121 GW Multimeter. And, oh look, it's got a little product hanger on it. Didn't know about that. Let's open it up. And, ta-da! The very first. The very first. All we've got in there is a thermocouple and a statement of calibration.

**Dave Jones:** No, it's not a cow certificate. So, let's have a look. Ta-da! The very first one. Oh, thing of beauty. Joy forever. Still got the screen protector on there. Look at that. And, hey, we got the serial number label. There we go. That one's number 127.

**Dave Jones:** Oh, winner, winner, chicken dinner. So, let's switch it on. Version 1.01. And, beautiful. So now I'm going to take 32 of them and I'm going to put them side by side and just check them out. Let's go. I don't know why, but it's just immensely satisfying to see 32 metres lined up like that.

**Dave Jones:** I just love tweaking all the knobs. Look at it. It's a thing of beauty. Joy forever. Alright, time to check these puppies. Please excuse the camera angle. I've got to do this for the time lapse, but there you go. I've got my 5 volt reference.

**Dave Jones:** It's bang on. 5 volts, good enough for Australia. And, let's go through them. Oh, this is the fun part. Very therapeutic. And there's the results for a nominal 5 volts input, which, by the way, is not the point where it's actually calibrated. It's actually calibrated at 4.5 volts,

**Dave Jones:** or, you know, 45,000 count on almost all the ranges except the oddball one. So, yeah, it's full scale, basically. And, I think the only one, the biggest outlier was this one here, 4.9994 and 5.0001 here. So that's a total spread of 7 counts there.

**Dave Jones:** Pretty darn happy with that. If I probably left that one a bit longer, it might have settled up a digit or two or something like that. So, yeah, pretty happy with that. 7 digit spread max, nice. And a bunch of them have auto turned off,

**Dave Jones:** and they'll slowly, you'll probably start to see the odd one do it now, because I think the timing should be pretty precise on it, so you'll see them cascade. Well, I won't leave it. But, oh, it's very therapeutic to switch them back on.

**Dave Jones:** So, yeah, you can switch off the auto turn off in software, but, oh, oh, just love pushing buttons. Whoa, magic. And what's even more satisfying than that? Oh, changing the ranges. Oh, oh, oh. I'll just check a few more ranges. I'll check the 500 millivolt range.

**Dave Jones:** There we go. And bang on so far. In theory, the 500 millivolt range should be a bit tighter than the 5 volts, because you're not relying on the divider resistors, but because they're all calibrated, individually calibrated ranges, eh, you know, it's arguable. And sure enough, yep, that's a bit tighter.

**Dave Jones:** I think 0.03 was the highest there, and 0.98, so a total spread of 5 digits. So a little bit tighter than here. Okay, it's Wicom resistance standard time. This is like a $4000 resistance standard. It's more than good enough for our purposes here.

**Dave Jones:** And there we go, 10.000. Beauty. Okay, for our 10k here, it looks like our worst case is 10.002. There are a few of those, and 9.999. So we've got a total spread of 3 counts. That's not much at all. And by the way, of course, 10k is well under the calibre,

**Dave Jones:** very similar to what we've got here. So we've got a total spread of 3 counts. That's not much at all. And by the way, of course, 10k is well under the calibre, very significantly different from the 4 point, well, no, sorry, in this case 45k for this range calibration value

**Dave Jones:** that it would have been called at. So the rest of it's the linearity of the ADC and whatnot. And on the AC volt range, I just did 5 volts at 60 hertz, and the spread is much larger as you'd expect on any AC meter, basically,

**Dave Jones:** because it uses the separate true RMS converter chip. It's got an inherently larger number of counts and everything. And the tone, I think the worst case was 5.003244.9942 or something. It's in there. Anyway, for a total spread of 0.2%, what's it in counts?

**Dave Jones:** 60, 90 counts or thereabouts. Somewhere just under 100 counts spread across all units. I think that's quite reasonable. And as for currents, sorry, I don't have enough leads to hook them all up at once, but there you go, I've got, what, 14 or something of them hooked up.

**Dave Jones:** There you go. I think we've got, like, 5 counts or something between them, maximum. Not too shabby. And as for capacitance, I can't bloody well find my reference capacitor, can I? So I'm just going to have to use a crap little thing, but I have adjusted it for, bang on, 10 nanofarads,

**Dave Jones:** and we are getting 10 nanofarads. Doesn't have a great resolution there, but there you go. That's pretty tight. Or is that a coinkydink? Come on. Oh, no. That's tight. Tight as a nun's nasty. And for those playing along at home, they're shipping with four Duracells,

**Dave Jones:** and they're shipping with a little fuse, a FLU11A 11-amp fuse, and the ASTM HV610, which is the one that I use on the BM235. Beauty. And an 8-gigabyte SD card, because these things are probably, like, a dime a dozen in Korea. And because you want to see inside it,

**Dave Jones:** and technically I haven't seen inside an actual production meter yet. There you go. I have had a look under the Mantis microscope, and the soldering looks no worries whatsoever. I'll just get the macro lens out on that for those who do like to play along at home.

**Dave Jones:** There you go. Beautiful. Nice fillets. No worries. All hunky-dory. Beautiful. Bob's your uncle. So I haven't actually run the spread numbers on these things yet, but I'll do that, and I'll include it as an overlay here. So there you go. I think I'll call it quits at that.

**Dave Jones:** I don't want to test absolutely every range and every function on these things. I just want to spot-check that there's nothing seriously wrong here, and it seems all hunky-dory. So anyway, I hope you found that interesting. I've got to go pack and ship these things now,

**Dave Jones:** and unfortunately I got them out of the box in the wrong, like I just scattered the boxes, and the boxes have the serial number card which matches the particular meter. So I've got to put them back together, match them up. D'oh! Catch you next time.

**Dave Jones:** Thanks for watching.
