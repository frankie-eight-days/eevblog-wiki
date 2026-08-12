---
video_id: tSzem8xshxk
title: EEVblog #576 - Advantest R6142 Current Voltage Generator
url: https://www.youtube.com/watch?v=tSzem8xshxk
source: youtube-asr
timestamps: {"0": 1, "1": 13, "2": 22, "3": 36, "4": 47, "5": 62, "6": 75, "7": 88, "8": 106, "9": 116, "10": 141, "11": 154, "12": 166, "13": 183, "14": 211, "15": 219, "16": 234, "17": 245, "18": 261, "19": 271, "20": 292, "21": 311, "22": 326, "23": 336, "24": 348, "25": 362, "26": 371, "27": 386, "28": 397, "29": 410, "30": 424, "31": 435, "32": 452, "33": 463, "34": 475, "35": 483, "36": 501, "37": 512, "38": 537, "39": 553, "40": 570, "41": 600, "42": 615, "43": 629, "44": 647, "45": 662, "46": 678, "47": 687, "48": 696, "49": 705, "50": 716, "51": 730, "52": 741, "53": 752, "54": 768, "55": 777, "56": 796, "57": 809, "58": 828, "59": 838, "60": 848, "61": 867, "62": 881, "63": 898, "64": 913, "65": 929, "66": 944, "67": 955, "68": 966, "69": 982, "70": 1004, "71": 1015, "72": 1036, "73": 1044, "74": 1056, "75": 1067, "76": 1086, "77": 1102, "78": 1119, "79": 1134, "80": 1148, "81": 1155, "82": 1169, "83": 1178, "84": 1197, "85": 1206}
---

**Dave Jones:** Hi, just a quick video to show you what I'm playing around with at the moment. I just scored this very nice Advantest uh R6142 programmable DC voltage current generator.

**Dave Jones:** In fact, it's it's almost like a voltage and current standard. It specs are uh pretty darn uh good as we'll take a look at. And I scored this on eBay for about 300 bucks.

**Dave Jones:** And if you're not aware of Advantest, they are a huge Japanese company who primarily make automated test gear for like the semiconductor uh you know, fabrication industry and stuff like that.

**Dave Jones:** You know, they're a multi-billion dollar company make real high-end high-spec gear, but they also make some you know, some reasonably well for them uh sort of low-end gear like this.

**Dave Jones:** And they do spectrum analyzers and a whole bunch of other stuff. And this is a real nice bit of kit. And we'll take a quick look at it and I'll show you what I'm doing here cuz I've just done some uh a couple of days worth of uh data logging on this thing.

**Dave Jones:** And you would have seen the a couple of updates on my Twitter uh feed for this if you're following along at home. And I just wanted to see like how accurate and stable it was for generating in this case a 1 milliamp uh current over time.

**Dave Jones:** And not only for absolute accuracy, but for drift as well. And you may have just heard that my air con just turned off here. And I've been doing some uh that's where I turned the air con on this morning when I came in and it ramped up.

**Dave Jones:** So, I've sort of like had the air con off and on. And we'll take a look at what this data actually uh means and see how you know, see how good this is for uh calibrating my microcurrent for example cuz there's not too many really precise current generators on the market.

**Dave Jones:** And this is certainly one of them. And uh yeah, so is it good enough to um program a microcurrent at normally 0.05%. So, it's got to be better than that.

**Dave Jones:** You notice my battery LED is flashing there. That's a feature of course the the battery is um of course uh low. So what it does that's just the ESR of the battery uh there when it turns on the LED of course it draws more current which then drops under the voltage threshold of the uh comparator there really uh quite a neat little um you know unintended uh side effect there but

**Dave Jones:** I like that feature. So we'll take a quick look at the data sheet and uh this is basically the data sheet's all I can find at the moment. I haven't been able to find a uh user a full user manual for the thing let alone a uh service manual.

**Dave Jones:** So if you do have those uh please leave a link in the comments. Uh large capacity up to uh 32 volts 160 milliamps. I would have liked it to go up to 1 amp and on the low side as well but uh well you can't have everything.

**Dave Jones:** High accuracy uh .03% high stability low noise 3 millivolts peak 50 milliseconds settling time and uh here it is. The um unit precision voltage and current generator is ideal for evaluation of precision circuits and parts as well as cal- calibration of temperature controls.

**Dave Jones:** Unit uses a time sharing D to A conversion circuit which provides excellent linearity and stability. There you go. So it's um and it does um it's also got uh you can it's programmable as well hence you know because they're really into automated uh test functionality and things like that so so it's got a 160 uh step memory and uh it's 6 month uh guaranteed accuracy .03% for voltage and .035%

**Dave Jones:** for current and that 3 millivolt noise is 1/5 of their previous model. I don't know what the previous model is and there's probably another model after this as well.

**Dave Jones:** I'm not sure of the age of this thing it might have a date code on the back. I forget off the top of my head. We'll check it out but anyway um and the Advantest stuff you know like a lot of the high end manufacturers over engineered so that point 03% is going to be very conservative.

**Dave Jones:** So, we're going to get I think well within side that sort of accuracy. In fact, if we go over here and have a look at some of the specs, we're looking at voltage generation.

**Dave Jones:** There are the ranges. It's only got three current ranges. As I said, I'm a bit disappointed that it's only got 10 milliamps and 100 milliamp ranges. So, you know, I would have liked to you know, generate microamps or something like that.

**Dave Jones:** But, this isn't designed for low current. You know, you'd have to get like a Keithley current source or something. Although, I'm sure Advantest, if you pay big dollars, will sell you a low current source generator most likely.

**Dave Jones:** But, you know, overall accuracy we're talking you know, point 03% there plus you know, five plus a small percentage plus a small range error there. And point 035%. But, if you're talking you know, 24-hour stability, it goes down to point 01% which is pretty darn good.

**Dave Jones:** So, these specs are essentially and because it's likely over engineered, good enough for calibrating a point 05% microcurrent. And the temperature coefficient here, I E the parts per million per degree C is in the order of 20 odd ppm per degree C.

**Dave Jones:** Not bad. Although, my HP34461A here I'm using has a nominal five ppm per degree C. So, it's like at least four times better than that. And we won't worry about the plus offsets on the amp will.

**Dave Jones:** Just you know, keep things a bit simple for today. And on DC current though, my Agilent meter which we're using actually does go up to about 20 on the current.

**Dave Jones:** So, it's going to be for so for the current measurement here, the drift of my Agilent meter is you know, about roughly equivalent to this Advantest unit or at least these are going to be worst case figures.

**Dave Jones:** Now, let's have a look at what the data up here means that I've been getting. You'll notice I've been logging for almost 1 day and 20 hours and 11 minutes.

**Dave Jones:** So, I've been going for quite some time and I've been here. I've turned the aircon. This is where I like came in and turned the aircon on and I turned the aircon on again this morning.

**Dave Jones:** It's you know, ramped back up. So, the temperature in the lab does change by, you know, like maybe up to 5° C variation depends on whether or not I've got the aircon when I leave the aircon on or off or not.

**Dave Jones:** When I've got the aircon on, I've actually measured the aircon in the the temperature in the room to be stable within plus minus 0.5° C. So, that's what the aircon cycles through.

**Dave Jones:** There's about a 5-minute cycle time between when it switches on and off to maintain the temperature here in the room. Anyway, um this looks like a Oh, you can probably see some of the multiplexing on the display there.

**Dave Jones:** You can probably see a bit of bit of flicker there. At least I can on my LCD screen. Now, if we have a look at the data here on my Agilent meter and I'm going to assume that my Agilent meter is like spot on.

**Dave Jones:** You know, it is my reference standard and I have actually confirmed that with my other reference gear. It is pretty darn good. It's way better than spec. It's you know, way better than it's calibrated spec.

**Dave Jones:** It's 24-hour spec. It's actually better than that absolute. So, I'm pretty damn confident in this Agilent meter. It really is kick ass. Now, you can see that there's a lot of noise in here and this looks like a huge variation, right?

**Dave Jones:** But, it's not really and I'll show you that in a second. And now, this So, this is the total data over that almost 2-day period there. And so, so we've got it set to all.

**Dave Jones:** Now, if I set it to recent, you can actually see the little tiny amount of noise. You can actually see the individual bit changes almost within that, uh, you know, within the sampling limit there.

**Dave Jones:** And as I've said in the review for this Agilent meter, its resolution is actually better than its nominal 6 and 1/2 digits when you're in this, uh, trend display mode.

**Dave Jones:** So, I I forget the exact figure, but it's like at least like 7 and 1/2 digits or something like that. So, it's pretty darn good. That's why I love the logging mode on this thing cuz you can get some excellent resolution better than what you get if you actually go into the, you know, pure number display like that.

**Dave Jones:** And that's how far we're off, um, in terms of I can actually jump between these things. Trend chart, there it is. So, we'll go back to all here, but that's like I've auto scaled that.

**Dave Jones:** So, they're the figures up there, and that's the, uh, real-time display up the top here. So, let's look at what these figures here actually represent. So, what I'm going to do is actually go into the, uh, vertical range, and I'm going to change the scale here to represent the, uh, 0.05% accuracy around the nominal 1 V that I would expect for my micro current.

**Dave Jones:** So, I can go in here. So, 0.05% of 1 V is 999. 0 5 0. And I'll do that for the high side as well, and you'll see how it's going to change.

**Dave Jones:** So, what we're going to do is 1 * 0.05 % there, and then we want to add that on, of course. And 1.0005. So, we want to get in here and change the scale to 1.0005.

**Dave Jones:** Oh, 000. 5 Bingo. 1.0005 milliamps. So, that range there now from 999.5 to 1.0005, that represents the nominal .05% range of my micro current here. And you can see how it's well within that window, not in terms of not only in terms of absolute accuracy.

**Dave Jones:** It's only, you know, a smidgen like, you know, half a bees dick under the nominal one microamp, but it's, you know, in terms of drift as well. You can see that the drift is actually pretty insignificant.

**Dave Jones:** It's well within that. So, I'm very happy with that. This Advantest unit on the 1 milliamp range more than accurate enough, better than its spec. And if you remember back here at the data sheet, it's one day stability spec.

**Dave Jones:** Spec. That's just a stability, let alone its absolute overall accuracy, which is up here. If we program in the .01% into there, bingo. This is what we get. .0 plus minus .01% around the nominal.

**Dave Jones:** So, it's still within side the .01% including the absolute value and the drift with in this case probably a 5° C three four or five maybe degrees C overall change here in the lab.

**Dave Jones:** So, that's brilliant. So, I'm really stoked with this unit. Absolute bargain, I think, for for 300 bucks a precision voltage and current generator that's good enough to calibrate any, you know, at least any four and a half digit meter.

**Dave Jones:** So, you know, it really is awesome and its specs are better than the data sheet. You know, it's made performance is measuring better than the data sheet. So, anyway, I've finished my data logging.

**Dave Jones:** I don't really need to, you know, save it. Not a huge deal. I got a video record here. That's good enough for me. And so, let's go back to the um Oops, sorry.

**Dave Jones:** Let's go back to the uh number display here, and let's uh play around with it. So, I'm going to screw up my data logging here, and uh let's see what happens.

**Dave Jones:** Uh like you can switch the polarity of the output. Let's So, let's see what happens when I go to positive and negative. Uh it's 0.9994. You know, let's take say 4 0 there.

**Dave Jones:** Look at that. It's not far off. It's changed by Well, bugger all, really. Um you know, well within well within the spec. So, that's pretty darn good. And let's see what happens when we go up one digit at a time.

**Dave Jones:** It's only a five-digit uh display, but it's still very good. Now, when I first uh got this thing, I thought, "Oh, you type in the number." cuz it's got like a number keypad here, and you type in the number, but it doesn't actually work like that.

**Dave Jones:** The These two uh are up-down buttons for this digit. These are up-down buttons for that digit, and so on. So, it's really quite weird. So, here we go. 999.4.

**Dave Jones:** Let's see if we go up one uh digit here. I We're going up uh 100 0.1 microamp there. Let's see if that jumps to uh in is still has exactly the same offset.

**Dave Jones:** Yeah, look at that. It jumped up, and it's still 41 there. And we can go up one, and we're increasing that digit. Look at that. Look at that. That is fantastic.

**Dave Jones:** So, that offset there is stays the same, but the jumps are precisely to that least significant digit there. I love it. Or actually beyond that. So, that is really, you know, quite impressive.

**Dave Jones:** I like that a lot. That is great. And of course, uh it's it goes up to 1.119, I think, is its maximum uh on all ranges like that. So, now let's check out the other ranges.

**Dave Jones:** The 1 mA of course is its maximum range minimum range there. I mean, you know, I can actually go down and generate, you know, 100 microamps or even 1 microamp or even 0.1 microamps, but then we're right down, you know, we're really quite right down in the noise.

**Dave Jones:** So, I'm not going to really, you know, it's so it's not the best for generating low value currents like that. I mean, look, you know, we're we're just around there, right?

**Dave Jones:** We're down at the least significant digit. Your accuracy is way out the window cuz you're not near the full scale there. So, whoop, let's go down. And let's go up a range.

**Dave Jones:** Let's go to 10 mA. Look at that. Still well within spec. Calculated that 0.002% absolute. Fantastic. I mean, that's within inside the spec of this Agilent unit. And on the 100 mA range, well, we're looking, you know, it's well within spec again.

**Dave Jones:** In this case, cuz it's 100, it's going to be this is going to be 0.005 or, you know, 0.004 % basically off from absolute. Once again, assuming that our Agilent unit here is absolutely bang on.

**Dave Jones:** But hey, these two units being like, you know, almost bang on together gives you a really good confidence that, you know, both units are working, you know, and well within specification, that's for sure.

**Dave Jones:** And of course, as I said, I've got other transfer standards which I can use to actually test precision voltage sources, precision resistors, and stuff that I can use to verify and sort of, you know, calibrate in quote marks my Agilent 34461A here.

**Dave Jones:** And I know it's well within specification, as I said. So, very, very confident about this puppy. So, I'm sure I'd bet money that if I took this to a standards cal lab, it would be well within spec, exactly what I'm measuring here.

**Dave Jones:** And we go negative on that. Look at that. Fantastic. All right, let's play around with the voltage mode, shall we? I'm still in that current mode, so we're getting a maximum output voltage of 13.4 volts there, but let's switch on over to volts.

**Dave Jones:** So, we're in we're generating 1 volt. I've got to press the operate button. That's the you know, and that's the output on off button. And check that out. Look at that.

**Dave Jones:** Bang on, of course, because we've got our four decimal places there. So, not a problem. Let's go up one digit. Look at that. Once again, completely spot on with the jumps.

**Dave Jones:** There's only that offset at the end. The point, you know, the point 0072 offset there. So, that is incredible. So, what does that work out to in percentage? Well, let's do a quick calculation.

**Dave Jones:** 1.000074 minus 1 is that times 100. There it goes. Bang. Look at that. 0.0074%. Awesome. And 10 volts. Not a problem. And it's lowest range, of course. Oh, no, it's lowest range There's 100.

**Dave Jones:** Sorry, it's lowest range is 10 millivolts. So, that one is a little bit out. There we go. Least significant digit there. Oh, no. Oh, no. We have four least significant digits.

**Dave Jones:** But even right down on the 10 millivolt range, we're still under 0.05%. Beauty. And it's got a four-wire input that sense, too. Although, I haven't actually been able to get that to work, cuz I put it on four-wire, and I don't attach anything to here, and it's still displaying the current just fine.

**Dave Jones:** So, you know, I'm not sure what's actually going on there, whether or not it's got a measurement. I don't think it's got a true measurement mode to read back.

**Dave Jones:** It's just, you know, it's just actually a generator. Um, but anyway, um, probably need a user manual for that. It's got adjustable current limit set so you don't damage anything.

**Dave Jones:** There's just a pot in there, you can just turn it so, you know, the operator can't come around and, you know, bang a few buttons and and blow up your uh uh you know, real expensive semiconductor under test or something like that.

**Dave Jones:** And they're very likely very high-quality tellurium copper contacts. No doubt. They sort of have that sort of tinge to them that you probably can't see it on camera, but it, you know, you can sort of tell those high-quality tellurium copper contacts when you see them.

**Dave Jones:** And if we take a random micro current here, whack in our 1 milliamp, assuming it's spot on, we knew it was actually a bit uh low. Anyway, it's still 0.012% out from that nominal, well within spec.

**Dave Jones:** And the milliamps range there at 100 milliamps test current, we're only 0.03% out. That's better than its nominal spec of 0.1%. And there's the back of the unit. It's got GPIB interface, trigger and ready trigger input, ready output, operator hold.

**Dave Jones:** I guess you can turn that off so the operator can't do anything stupid. Calibration uh button, which I'm not going to mess with. Of course, uh selectable mains voltage so you can safely buy this gear anywhere in the world, like here in Australia, and just switch it over.

**Dave Jones:** And some, looks like some BCD inputs as well for test systems and stuff like that. And a voltage limit pot on the back. Manufactured by Advantest in Tokyo in Japan.

**Dave Jones:** Brilliant. Japanese made. Unfortunately, no date code. We'll have to crack it open and have a look. And I can confirm after popping off the lid that this is about a '94 vintage.

**Dave Jones:** So, there you go, about 20 years old, but still very nice little bit of kit. And no, I'm not going to show you inside because I said this would be a quick video, and it won't be if I do a teardown.

**Dave Jones:** And I can't just blow my wad on one video, can I? So, yes, if you want me to if you want to see a teardown inside this thing, please let me know in the comments.

**Dave Jones:** Although, I probably will anyway, so there you go. I hope you enjoyed that little look at this Advantest R4142 programmable DC voltage current generator. And I reckon Advantest is a nice little search term to whack into eBay to try and find some good bargains.

**Dave Jones:** But, their stuff usually goes for a price premium, but I got this at quite a decent price, I think. So, if you like the video, please give it a big thumbs up.

**Dave Jones:** And if you want to discuss it, jump on over to the EVBlog forum. Catch you next time.
