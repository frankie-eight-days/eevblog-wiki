---
video_id: U4JFeU-o2kc
title: EEVblog #26 - Multimeter Tutorial - Counts, Accuracy, Resolution & Calibration
url: https://www.youtube.com/watch?v=U4JFeU-o2kc
source: youtube-asr
timestamps: {"0": 0, "1": 21, "2": 32, "3": 49, "4": 69, "5": 81, "6": 99, "7": 113, "8": 124, "9": 133, "10": 152, "11": 174, "12": 189, "13": 216, "14": 228, "15": 241, "16": 255, "17": 267, "18": 288, "19": 302, "20": 319, "21": 331, "22": 349, "23": 365, "24": 386, "25": 405, "26": 425, "27": 452, "28": 468, "29": 486, "30": 498, "31": 510, "32": 523, "33": 537, "34": 557, "35": 570, "36": 580, "37": 590}
---

**Dave Jones:** Hi, welcome to the EE Vblog. I'm your host, Dave Jones, and this is episode number 26. There was a comment on one of my earlier blogs from someone called Walter, and he had a question about multimeters and the counts, like you know, 4,000 count multimeter, and how that what are counts and how that relates to multimeter accuracy.

**Dave Jones:** And I thought that's a pretty good question. It's something a lot of people don't really understand all that well, so let's you know, I thought I'd clear it up.

**Dave Jones:** A three and a half digit meter can actually display plus or minus 1,999. The half in the the half actually means that the most significant digit can only go to one.

**Dave Jones:** It can only be zero or one. So a three and a half digit meter can go up to 1999. A four and a half digit meter can go to plus minus advertising them as three and three quarter digits or three and two thirds digits, and that's where it gets a bit confusing.

**Dave Jones:** There's no real standard for that, but typically if it if it's got like two thirds or three quarters or something like that, they really mean that it can go a bit further than one.

**Dave Jones:** So it might be 3999 or it might be 2999 or even 4999 or something like that. Now, because it started becoming quite confusing, manufacturers started talking in terms of the number of counts, and I think this is a much better way to do it.

**Dave Jones:** So a a three and a half digit multimeter at plus minus 1999 is actually a 2,000 count meter, because it counts up to plus minus 2,000. And likewise, a four and a half digit meter is actually a 20,000 count.

**Dave Jones:** You can use these terms interchangeably. Now, how does this relate to accuracy? Well, it actually doesn't relate at all. It has nothing to do with accuracy. So, let's talk about this.

**Dave Jones:** Now, accuracy is a term when it comes to multimeters, people get it wrong all the time. And I'm I'm guilty of saying it too through sheer laziness or, you know, habit.

**Dave Jones:** It's wrong to say that this meter has an accuracy of four and a half digits or an accuracy of 10,000 counts. That is completely wrong. The counts, the number of digits, is the resolution.

**Dave Jones:** So, it's You should say that this meter has a 10,000 count resolution, not a 10,000 count accuracy. And if you, you know, if you say the wrong thing, it can make you seem like a bit of a dunce, especially if you're in a job interview or something and they ask the question, it can make you look like you don't know what you're talking about.

**Dave Jones:** Okay, now let's take a look at three typical multimeters and how the the number of digits or the resolution affects the usability of these meters. Now, I've got a Fluke 79 Series II here.

**Dave Jones:** Now, this is a 4,000 count or a three and three quarter digit meter. I've got the MeterMan 37 XR here and this one is a 10,000 count meter. The Fluke 87 V here is a the four and a half digit meter, but I've got it in it's actually got a mode that is actually 6,000 count mode.

**Dave Jones:** Okay, now I'm feeding the same voltage into all three meters and you can see they all read fairly similar. They, you know, there's there's slight differences there, but let's have a look what happens when I turn the voltage up here.

**Dave Jones:** Okay? Now, if I had a three and a half digit meter here, which I don't, it would have actually dropped down to two decimal places because it would have been over the 1999 limit, but none of them have reached that yet.

**Dave Jones:** So, let's keep turning this up, okay, and see which one actually drops its range first. And I'm sure you can guess which one it's going to be. Bingo, there it is.

**Dave Jones:** The Fluke 79 Series II because this is a 4,000 count meter, we're over that 4,000, we're basically over four, so it's got to go up to the next highest range.

**Dave Jones:** So, we lose one digit of resolution, okay? Not accuracy. Now, if we keep turning this up, we'll find that the Fluke 87V here is a 6,000 count, so as soon as it gets to six, or just slightly over, bang, it's changed upper range, also.

**Dave Jones:** So, I this is uh now, these are giving the same resolution, okay? This is a much more expensive meter um at 6,000 count, okay? But, it's but they've got the same resolution.

**Dave Jones:** Now, this Meterman 37XR at 10,000 count, you're still getting the extra digit of resolution, and this won't change ranges until you go right up to until you pass that 9999 limit, and bingo, there it is.

**Dave Jones:** Half digits, they're all back on an even playing field. But, let's switch the Fluke 87V to four-and-a-half digit mode, okay? Now, we've got this extra digit of resolution here, not accuracy, resolution.

**Dave Jones:** Now, you'll find that this 87V four-and-a-half digit meter is useful until once again, we get up to Once again, we get up to 20 odd volts and bingo, it's gone back.

**Dave Jones:** So, you can say that the 4 and 1/2 digit meter only has more resolution for 20% of its range over the 10,000 count meter. I said before that resolution, the number of digits on the display has nothing to do with accuracy.

**Dave Jones:** And that's true, okay? Accuracy of the meter is based on the percentage of the actual reading, not a full scale. So, a meter's accuracy will be specified as the percentage of the reading plus counts.

**Dave Jones:** Now, a typical like a good meter might have point an accuracy of 0.1% plus two counts. Now, what that means is if you're measuring 1 volt, okay? You will have an It will have an uncertainty of plus or minus 1 millivolt.

**Dave Jones:** 0.1% of 1 volt is 1 millivolt. But, you have to add on two counts to that plus or minus two counts to that displayed value. So, it will be if it's actually reading exactly 1 volt, okay?

**Dave Jones:** 1.000, then it can actually be 1.00 0 3 or plus minus or 0.997. So, that's resolution and accuracy. Now, let's talk about calibration. Everyone knows that uh you know, you should get your meter calibrated.

**Dave Jones:** What does that actually mean? What it means is that the meter has been checked. It's been It doesn't Calibration does not mean adjustment of your meter. When you send this away for calibration, it's They usually don't adjust it.

**Dave Jones:** What they will do is they'll measure it against a reference standard, and they will give you a test report for this, um giving you the actual typically giving you the actual figure, and um you know, and the error against that absolute reference or that transfer standard.

**Dave Jones:** And what you do with that calibration information determines how this multimeter is going to be used within your company, what applications it's going to use for, and how often you're going to calibrate it.

**Dave Jones:** Now, just because a meter has been calibrated yesterday does not mean it's going to be within spec today. It's uh It's all about Calibration is about the history of this meter, tracing.

**Dave Jones:** It's about traceability. You need to trace uh the calibration of this meter. You need a historical record of it over time, and then you build up confidence in this meter that it's not drifting.

**Dave Jones:** This is why some companies and some industries will actually uh uh you know, you have to actually use two multimeters to take a measurement just in case one of them has, you know, is is actually out.

**Dave Jones:** And they will, you know, anyone serious about electronics will actually have two multimeters. They won't rely on just one. They'll have two so that you can cross-check each other, and you can actually use a good known multimeter as a as a bit of a transfer standard to uh check and measure other instruments.

**Dave Jones:** And if you've got a bunch of multimeters, you can all cross-measure themselves, and you get more confidence that your meter is within specification. Usually, you'll follow the manufacturer's recommendation, which might be, say, every 12 months.

**Dave Jones:** But when you first get an instrument, you might want to calibrate it more often so that you build up more of that reference that historical reference data so you can track it.

**Dave Jones:** And once you know this meter is not, you know, it's really stable and it's not drifting at all, then you might actually widen your uh period of calibration 12 months.

**Dave Jones:** Then, you know, it still hasn't drifted at all, you might actually change it to two years.
