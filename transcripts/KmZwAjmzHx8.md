---
video_id: KmZwAjmzHx8
title: EEVblog #647 - Agilent 53131A Frequency Counter Oven Upgrade
url: https://www.youtube.com/watch?v=KmZwAjmzHx8
source: youtube-asr
timestamps: {"0": 0, "1": 11, "2": 24, "3": 40, "4": 51, "5": 64, "6": 75, "7": 92, "8": 109, "9": 124, "10": 133, "11": 146, "12": 157, "13": 169, "14": 179, "15": 198, "16": 212, "17": 228, "18": 237, "19": 248, "20": 263, "21": 278, "22": 288, "23": 296, "24": 307, "25": 317, "26": 335, "27": 347, "28": 360, "29": 370, "30": 386, "31": 403, "32": 419, "33": 433, "34": 453, "35": 473, "36": 490, "37": 506, "38": 518, "39": 539, "40": 555, "41": 564, "42": 578, "43": 590, "44": 610, "45": 619, "46": 640, "47": 658, "48": 667, "49": 678, "50": 691, "51": 706, "52": 714, "53": 723, "54": 739, "55": 753, "56": 774, "57": 800, "58": 814, "59": 825, "60": 837, "61": 856, "62": 867, "63": 875, "64": 885, "65": 895, "66": 913, "67": 925, "68": 939, "69": 952, "70": 962, "71": 973, "72": 981, "73": 1006, "74": 1020, "75": 1032, "76": 1041, "77": 1054, "78": 1063, "79": 1074, "80": 1082, "81": 1097, "82": 1114, "83": 1128, "84": 1147, "85": 1171, "86": 1185, "87": 1202, "88": 1217, "89": 1229, "90": 1248, "91": 1263, "92": 1280, "93": 1294, "94": 1306, "95": 1318, "96": 1328, "97": 1342, "98": 1356, "99": 1368, "100": 1386, "101": 1400, "102": 1413, "103": 1424, "104": 1435, "105": 1451, "106": 1462, "107": 1471, "108": 1482}
---

**Dave Jones:** Hi. Now, you've probably seen this before. This is my Agilent 53131A universal counter, frequency counter. And it's a very good unit. Highly recommend it if you can pick one up on eBay.

**Dave Jones:** It's an older model. They've got a newer model out now, but it's a really nice instrument. And I've done a couple of previous videos on this. I got it from an auction score, really dirt cheap, basically along with my rubidium frequency standard.

**Dave Jones:** So, click here if you want to watch the previous videos. I've showed actually calibrating this thing or the internal oscillator in this thing, hence today's video. While this is a really good frequency counter, its standard oscillator building is horrible.

**Dave Jones:** It is practically a joke. It's like, you know, I've just a 5 ppm SC cut crystal or whatever it is with a dicky little pot on the back that you got to adjust.

**Dave Jones:** It's It's worthless. So, to make this thing usable, you've either got to put an external reference in from a rubidium oscillator or anything like that, or get one of the higher stability internal options.

**Dave Jones:** And they're normally very expensive, of course. But, I found this on eBay, and this is one of these This is a high stability oven based oscillator. And this is what you need for one of these things.

**Dave Jones:** Sure, I've got myself a rubidium frequency standard from the CSIRO, no less. It is was the main frequency standard at the Commonwealth Scientific Research Institute here in Australia, whatever it is stands for.

**Dave Jones:** Research organization. And it was good enough for them, it should be good enough for us. It actually uses a Stanford Research PRS 10 rubidium oscillator in it that's GPS locked, and it's got backup power supplies and all that sort of jazz.

**Dave Jones:** Anyway, that's fine and dandy. And I've got this super accurate rubidium standard here in the lab that I can hook up, and my frequency counter is really accurate, but hey, you don't always have it available, and well, you know, convenient anyway, always hooked up.

**Dave Jones:** So, I thought it'd be nice just to upgrade this puppy with this oven oscillator, so it can be used standalone, and it's going to be pretty accurate. So, this thing only cost me I think it was $70 delivered on eBay.

**Dave Jones:** So, let's take a look at it, fit it inside, and see if we can check out its performance. Now, here are the various time base options for this HP frequency counter, HP Agilent.

**Dave Jones:** What is it now? I think it maybe they've officially changed their name now to Keysight. Oh, I don't know. I don't care. Jesus, it's always going to be HP, or at least Agilent.

**Dave Jones:** Anyway, yeah, the standard oscillator 5 ppm temperature stability, it's just it's just garbage. Like, you know, it is absolutely useless. It really is. Don't even bother using the frequency counter with the building oscillator.

**Dave Jones:** Anyway, you can get option 001 with the medium oven. You know, 2 * 10 ^ 7, not bad. Then you can jump up 2.5 * 10 ^ -9 for the high stability oven.

**Dave Jones:** And then they got the ultra high stability oven, which doesn't look a huge in terms of temperature stability, but it just has better aging. So, if you are buying one of these things on eBay, by the way, that's only for that model, the higher up model, not for the one that I've got, but yeah, you know, so we've got a replacement oscillator.

**Dave Jones:** Let's see if its specs are at least as good as this. And if you are going to pick these up on eBay, then the photos and description carefully. If you can get one with at least the medium oven in there, then that's what you want.

**Dave Jones:** But if you can't, hey, look, 70 bucks on eBay, brilliant. So, this is from a company called Chungo, if I'm pronouncing it correctly, Information Communication Co. Limited. And it's the STP 4 2145A 10 MHz reference.

**Dave Jones:** Operates at 12 V. Not all of them operate at the same voltage, so if buying one of these, just uh be aware. Anyway, I'm I don't know who actually uh designed this board.

**Dave Jones:** A few people have uh designed their own options. It's got a trim pot here, and it's got a jumper link, which allows you to uh adjust This one's currently set to adjust from the trim pot here.

**Dave Jones:** And if you have a look at the bottom of the board here, there it's actually missing some circuitry. And this is actually a digital-to-analog converter, which is what the uh real one inside the uh Agilent one has inside uh the Agilent if you get that option.

**Dave Jones:** So, the software There's calibration software Well, calibration routines inside the uh frequency counter itself to actually calibrate this thing. So, this one just doesn't have it. Presumably, I could populate the parts on there, get the schematic, which is readily available, and do that.

**Dave Jones:** And let let the software in the unit calibrate itself. But, uh I don't need to do that. Anyway, I'm just uh happy to uh set the trim pot and uh see what happens.

**Dave Jones:** Now, it'll be interesting to see whether or not this has spot-on this thing is uh coming from this eBay uh seller, which I'll provide the link in uh down below.

**Dave Jones:** Hopefully, they're still available by the time you watch this. Now, I've actually got the data sheet for this thing. Uh presumably, I couldn't get it from the uh manufacturer itself, so I presume this is the same manufacturer.

**Dave Jones:** But, anyway, it's exactly the same part number, so I'm going to run with that. Um this is a really pretty schmick ovenized oscillator. Uh you can get them in different frequency ranges.

**Dave Jones:** This is a 10 MHz one, of course, but uh very high stability. We're talking about uh you know, 5 * 10 ^ -11. That's very impressive. And I think we'll have a look at uh it's pretty comparable with my um Stanford Research PRS 10 rubidium oscillator, as well.

**Dave Jones:** Now, it does come in different grades here. And um this MV89, I can't find this part number on here. So, I'm not sure if it's exactly the same That's why I'm just maybe a bit skeptical.

**Dave Jones:** It's not exactly the same data sheet. Anyway, it does have different grades available if you are buying these sorts of things. They do come in different Well, not initial tolerance grades, but stability grades.

**Dave Jones:** But really, these things are designed to be calibrated after they're adjusted after they're installed. They have a frequency adjust pins, hence the pot going into a pin on the unit.

**Dave Jones:** You can actually adjust the frequency over a range. So, that's why in these data sheets, you won't actually find an absolute specification for its frequency. It's not there. Don't confuse this aging spec up this high this stability or aging spec up here with the absolute accuracy.

**Dave Jones:** It is not the same thing. Now, if you compare its specs here to my standard research PRS 10, which is used in my rubidium oscillator, which is the actual rubidium unit itself inside my CSIRO unit, which has been absolutely adjusted by the way.

**Dave Jones:** It's a similar sort of thing. You have to actually adjust it and calibrate it. My one has cuz it's a former CSIRO standard for the Australian Defense Force. So, hey, it's good enough to calibrate the Australian Defense Force here, it's good enough for us.

**Dave Jones:** Anyway, look at this. This oven oscillator pretty darn good. Look at the short-term stability like over 1 second, which is the Allan deviation. We're talking about less than 2 * 10 ^ -12 over the 1 second.

**Dave Jones:** And where it is. Here we go. On the rubidium one, it's basically an order magnitude better. We've only got less than 2 * 10 ^ -11. So, in terms of the Allan deviation there over 1 second, this ovenized oscillator is better order magnitude better than that rubidium reference standard I've got.

**Dave Jones:** Awesome. But in terms of actual long-term aging, which is kind of like, you know, more important when you're using it for a reference in most cases. Look, the ovenized oscillator over here, we're only talking about, you know, depends on what grade you get, of course, but even the best grade here, 5 * 10 ^ -9 per year.

**Dave Jones:** So, look at the rubidium one over here, where we're talking about Here we go, aging yearly, 5 * 10 ^ -10. So, now the rubidium oscillator is actually an order of magnitude better than the ovenized oscillator over the span of a year.

**Dave Jones:** And if you've got one of the lower grade rubidiums here, which I'm not sure what this one is cuz can't find an exact data sheet, but anyway, yeah, it could be the rubidium could be like two orders better stability than the ovenized oscillator.

**Dave Jones:** And then the rubidium oscillator is going to be like an order of magnitude better again. Look, voltage sensitivity here too. Basically, that's the sensitivity to the power supply change of 1-V difference in your power supply voltage, 2 * 10 ^ -11.

**Dave Jones:** And we're only talking about, you know, 10 ^ -10 over here for the same thing on the oven oscillator. And the oven oscillator actually warms up pretty good to spec, less than 15 minutes to get 5 * 10 ^ -8, which is more than good enough as a oven standard for this thing, but I'll let it warm up for more than that.

**Dave Jones:** And the phase noise as well for this thing, basically the same as the rubidium oscillator, which is a super low noise rubidium one at 10 Hz -130 dBc per hertz, and exactly the same spec here on the rubidium.

**Dave Jones:** Now, I've actually seen inside this thing before, so I won't bore you with the details, but basically there's a huge cutout in here, and it's got the three mounting holes there for the internal oven.

**Dave Jones:** Also, I mean, sure enough, this is actually designed as a, you know, a proper upgrade compatible clone of the Agilent unit, apart from the aforementioned digital-to-analog converter circuitry on there.

**Dave Jones:** So, yes, it looks like the uh the it does line up with the uh holes on there and uh comes with standoffs and screws and everything. So, I'm just going to screw that in and uh whack it right on over here to the headers and it should be good to go.

**Dave Jones:** Now, just one little interesting aside and a trap for young players with uh oscillators uh any sort of crystal oscillator like this, if you're really talking, you know, if you're really critical about your measurements on this thing, don't just have it sitting out here like this, plug it in, and then uh you know, adjust your trim pot out here.

**Dave Jones:** Why? Well, it's not because of thermal effects or anything like that, because this is an oven, it's going to stabilize its own temperature. So, that shouldn't be a problem.

**Dave Jones:** But, uh crystal oscillators are actually susceptible to orientation like that. Extremely slightly uh subject to orientation is due to gravity, that pesky thing. You can't beat gravity due to the uh microstructure in the mount of the crystal inside there, you can actually get very subtle frequency differences in this thing.

**Dave Jones:** So, you want to actually calibrate it in that particular orientation, preferably screwed into there. And uh sometimes, if you know, just the act of uh putting the moving up the tilting bail on this thing can actually affect the frequency just a smidgen.

**Dave Jones:** Might be hard to measure, but in theory, it can do it. And that mounted in there very nicely, perfect. And uh the header cable just goes on over. Now, I'll power it up.

**Dave Jones:** I'll uh before I when I do the calibration, I'll put the uh cover on and uh stuff like that. But, for the moment, I will just stick the power in.

**Dave Jones:** Really annoying aspect of this, the fan always stays on. But, uh it's powering up and uh self-test. Is there an indicator on the screen that we have an internal oven?

**Dave Jones:** Nope. Now, this thing actually has a LED on it to indicate that the oven is on, but maybe that's the oven is actually uh stabilized to temperature. So, it might take you know that recommended 15 minutes or whatever for that LED to come on.

**Dave Jones:** So, I'll just leave it for a little while with the case off see if that LED comes on. And by the way, with this oven installed, it's drawing 33 W or hereabouts.

**Dave Jones:** It I expect it to take a fair bit of power. So, let me just disconnect that and we'll measure it again. Yeah, there we go. 26.51. So, significantly less power.

**Dave Jones:** So, that thing's sucking what seven odd watts or thereabouts. And by the way, if you're wondering what these sort of aging figures mean here like plus minus 1 * 10 ^ -8 per year, what does that minus eight mean?

**Dave Jones:** Well, when you talk about this sort of stuff, you're always talking in terms of PPM or parts per million. So, for a 10 MHz reference oscillator like this, one parts per million is 1 * 10 ^ -6 * 10 MHz is gives you 10 Hz here.

**Dave Jones:** So, that's 10 ^ -6 and then you go down by an order of magnitude or get better by an order of magnitude looking at 0.1 PPM 10 ^ -7 or you're going to have a 1 Hz error or 1 Hz drift basically maximum plus minus 1 Hz drift over well, sorry.

**Dave Jones:** Let's go down. 0.01 PPM 1 * 10 ^ -8. So, if you had that oscillator there that had a an aging characteristic of you know, that spec of plus minus 1 * 10 ^ -8 per year, you're looking at you could say that this is a 0.01 PPM stability oscillator over a year and it's going to drift plus minus 0.1 Hz.

**Dave Jones:** And these other specs here, you treat those exactly the same. So, the warm-up time accuracy, so after 15 minutes, it's going to be stable or accurate to where you previously set it to plus minus 5 * 10 ^ of minus eight.

**Dave Jones:** So, not point basically not point plus minus not point five hertz within 15 minutes. And yes, the LED finally come on. I forgot to time that, but yeah, it was probably 10 minutes 15 tops something like that.

**Dave Jones:** So, yeah, well within spec. So, that is a thermostat lock. Now, of course, the interesting thing to note is that once you got the power on, I've switched this thing off.

**Dave Jones:** You'll notice there's no display, but as I said, the fan always continuously runs because this internal oven oscillator is always powered up. And really, if you're serious about your standards and your oscillators, you're just going to leave this sucker running, and it's going to draw 17 watts by the way on standby.

**Dave Jones:** What a shocker. I'm just looking at my power meter now. 17 watts just to keep this sucker running. But anyway, as we saw before, there was no indication on the front panel that it was actually working.

**Dave Jones:** But as I said, we can actually enter the calibration menu on this thing, which if this thing did have the DAC on it, we just hold down this button and cal secure.

**Dave Jones:** Oops. Okay. This can be secure or unsecure. Now, the manual, I think, gives you a code for this. So, you have to press this again, and cal count is six.

**Dave Jones:** So, this thing has been calibrated six times. There you go. Okay, I've held that down, and presumably it's going to be the factory code, which I think is 53131A.

**Dave Jones:** I won't bore you with the details. I'll see if it works. 53131 cal unsecure. We're in like Flynn. Beauty. Aha, no. I thought this would actually give us the option, but of course, dull, it doesn't because this module doesn't have that DAC on it.

**Dave Jones:** So, obviously, it's detected that, and normally, it would give you the option in here to uh, the timebase by supplying an external 10 MHz reference. So, we don't have that.

**Dave Jones:** So, unfortunately, um, we don't really know, um, if this thing's using the internal oscillator unless we actually, uh, play around with the, uh, well, feeding the signal in and measuring the output and checking the output frequency for drift and all that sort of jazz.

**Dave Jones:** Now, just as a very quick indicator here, I've got it connected to my other, uh, uh, counter here, my Rigol DG4162. It's got a external counter and I've got the reference for this hooked up to my 10 MHz rubidium.

**Dave Jones:** Um, and you can see I've just powered this thing, uh, back on. I've moved it, um, so the oven's switched off and now you can see it's actually drifting up like that and that's exactly what I expect.

**Dave Jones:** Now, um, unfortunately, the only bad thing about having the oven oscillator in this is that you that LED indication, you don't have it unless you actually wire that LED indication out to the front or the rear panel or something.

**Dave Jones:** You wouldn't know that that thermostat's locked in. So, you just got to trust it and, you know, wait 15 minutes after it powers up or whatever, but, uh, that's okay.

**Dave Jones:** And the interesting thing is, look, it's actually counting back down now. So, it's sort of overshot maybe in temperature and now it's coming back down. So, yeah, it'd be interesting to actually, uh, graph that, uh, switch on, but unfortunately, um, I tried to get, uh, some software for this Rigol cuz it's got, you know, Ethernet and a USB interfaces and try and actually get the data out and actually plot that, but it

**Dave Jones:** looks like no bloody software comes with the Rigol that allows you to do that. Uh! It's really annoying. It's got like the drivers and everything, so you could, yeah, write a LabVIEW thing for it or, you know, some other thing or use some other, uh, software to do it, but anyway, it was rather annoying.

**Dave Jones:** So, yeah, jeez, mango. And the other annoying thing is is I also wanted to get data out of this thing and it I don't have a GPIB, uh, board or cable.

**Dave Jones:** Um, and but it had a serial port on the back, so I thought, "Beauty." So, I I finally got a uh, managed to find a serial uh, cable here, a rare, I don't know.

**Dave Jones:** I lost the damn thing if you're following my tweets. But, uh it turns out that the serial port on this is not for communications like data extraction. Uh it's only for connecting to a serial printer.

**Dave Jones:** Oh. So, yeah, I can't extract data from this. I'm going to have a hard time extracting data from this. So, please excuse me that I'm not going to actually be able to log this stuff and actually get a graph of the frequency.

**Dave Jones:** I couldn't be bothered. So, I'm going to increase the gate time here to 1 second. So, that'll update the uh display here at 1 second. And look at that.

**Dave Jones:** That's not bad at all. Now, I'm This is much better than what it was before. So, straight off the bat, look at this. We're pretty not bad at all.

**Dave Jones:** Of course, uh it's now running on the internal ovenized oscillator on this thing, which has It's not been 15 minutes yet. It hasn't uh locked in at all. And I'm feeding the output from my rubidium oscillator over here.

**Dave Jones:** So, and this frequency is uh the rubidium locked or the rubidium uh referenced frequency of the output of this ovenized oscillator. Or I believe it is. I believe it automatically switches the ovenized oscillator through to the output instead of the internal one.

**Dave Jones:** It should be. Now, I've shown this in a previous video, which I'll link in, which I won't bore you with the details. But, this is a way that you can visually compare the uh drift or the uh or you can calibrate or trim these oscillators.

**Dave Jones:** Channel 1 here, the yellow one, is my 10 MHz uh reference signal from my rubidium uh reference standard. And I'm triggering from that channel. And this blue one down here, channel 2, is the 10 MHz output from the ovenized oscillator from the output terminal on the uh 53131A counter.

**Dave Jones:** You can see it's slightly drifting like that, very slowly. And if I start my stopwatch there at that point and time how long it takes to go all the way through a full cycle like that, then we'll see an interesting effect on the interesting comparison to the frequency displayed on the front panel.

**Dave Jones:** And I timed that at 40.8 seconds. And if we put 40.8 seconds into here, well, 40.8, and we invert that, we get .024 Hz. What do we get on here?

**Dave Jones:** .02 Well, it was .024. There we go, .024 Hz. Bingo. That is the direct error compared to our rubidium reference standard. And I've actually left this for some time now, and yes, the LED's been on for ages.

**Dave Jones:** So, I don't think it's going to age, you know, like it's going to warm up and come into spec a huge amount more than what we've already got. So, I might get in there now and just trim that pot at the right tongue angle, of course.

**Dave Jones:** It's all about the tongue angle. And see if I can zero that thing out compared to my rubidium oscillator. But as it stands, as I got this thing from eBay, is that How warm is that?

**Dave Jones:** Oh, yeah, it's fairly warm. It's certainly not too hot to touch. Anyway, as I got this from eBay, they must be like trimming them before they send them. But like, you know, .026 Hz there, we're only talking, you know, point you know, 2.7 * 10 ^ -9, is it?

**Dave Jones:** Yeah, it's not much at all. It's not out by much. So, anyway, you can see the slight drift on that. I'm going to get in there. Tongue is at the correct extended correct angle.

**Dave Jones:** Can tell I was talking. And here we go. Oh, yeah. Look, we're just ah slightest tweak on that and it drifts back. I mean, jeez, you barely touch that.

**Dave Jones:** It's not much travel range in that at all. Wow. I'm like I'm I'm just lightly touching that thing. And ah yeah, there's nothing in it. There's nothing in it.

**Dave Jones:** So, the uh trim range of this thing is very, very slight. But, anyway, look at that. Beautiful. And if I go up to 10 seconds uh gate time there, then we'll get an extra digit on our display.

**Dave Jones:** And uh you know, this isn't This waveform method isn't a bad way to do it. I've shown in previous video, which I'll link in, I've shown different ways to actually do this.

**Dave Jones:** There's a couple of ways, but there we go. We've gained ourselves an extra digit there. And uh yeah, that's not too bad at all. I might tweak it a little bit back.

**Dave Jones:** Unfortunately, with the display like this the thing is like you've got a gate time of 10 seconds here, so it makes it hard to adjust this. But, if you do the waveforms here, but as you can see, when you get down to this sort of level, it's really hard to see the drift in there.

**Dave Jones:** Look at that. I mean, you know, can you see that drift with your eye? It's you know, it's practically impossible. Yet, we're out. And there you go. I basically don't think I'm going to be able to get it any better than that.

**Dave Jones:** Look at that. I mean, you know, just the slightest hair touch on that pot. And of course, there is going to be some drift over time. And you can set up our data logging and stuff to actually do that in comparison with the rubidium oscillator.

**Dave Jones:** And even you know, GPS lock the thing. And ah you can do all sorts of weird and wonderful things and spend weeks and weeks characterizing something like this. But, this thing we've just improved the accuracy and stability of this thing by a couple of orders of magnitude with a 70 buck aftermarket add-on there.

**Dave Jones:** So, if you can if you've got one of these or you're looking at getting a frequency counter, then you can pick one up pretty cheap, especially because if it might have the the cheap ass standard crystal oscillator in it, then get one of these aftermarket add-ons.

**Dave Jones:** They work really well. I don't know sort of the comparison between the one with the where if you add the extra circuitry for the D to A converter, you'd have to, you know, figure out which one's more stable, the D to A converter or the pot adjustment.

**Dave Jones:** And I don't know that they've got that trim range cuz that's a 10 turn trimmer. And this thing was just so delicate. So, I haven't actually looked into the circuit details there.

**Dave Jones:** We probably have to adjust the series resistor in that from the wiper into that thing to adjust the range to narrow the range down or something like that. So, anyway, I'm pretty darn happy with that.

**Dave Jones:** That is a Bobby dazzler. It really is. This oscillator, um this rubanized oscillator is a really good, quite a high spec one. It's awesome. And for a 70 bucks assembled and tested, yeah, it's not a brand new oscillator.

**Dave Jones:** It's probably salvaged from somewhere, something like that as these things typically are. You can buy them just separately on eBay. And I believe a couple of people out there have actually designed boards.

**Dave Jones:** They're probably like open source hardware or something, designed boards that I think fit different types of oscillators on the market and things like that. So, yeah, well worth doing, but I just bought this one.

**Dave Jones:** It was just no fuss. It was already assembled and and it looks like it was already trimmed to frequency cuz it was pretty darn close to spot on, almost as good as you can get it.

**Dave Jones:** So, it's drifted a little bit there since I've been yapping on, but anyway, that's an absolute beauty. So, hope you found that interesting. Catch you next time. Ah.
