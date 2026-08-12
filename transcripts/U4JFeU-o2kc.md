---
video_id: U4JFeU-o2kc
title: EEVblog #26 - Multimeter Tutorial - Counts, Accuracy, Resolution & Calibration
url: https://www.youtube.com/watch?v=U4JFeU-o2kc
source: youtube-asr
---

**Dave Jones:** Hi, welcome to the EE Vblog. I'm your host, Dave Jones, and this is episode number 26. There was a comment on one of my earlier blogs from someone called Walter, and he had a question about multimeters and the counts, like you

**Dave Jones:** know, 4,000 count multimeter, and how that what are counts and how that relates to multimeter accuracy. And I thought that's a pretty good question. It's something a lot of people don't really understand all that well, so let's you know, I thought I'd clear it

**Dave Jones:** up. A three and a half digit meter can actually display plus or minus 1,999. The half in the the half actually means that the most significant digit can only go to one. It can only be zero or one.

**Dave Jones:** So a three and a half digit meter can go up to 1999. A four and a half digit meter can go to plus minus advertising them as three and three quarter digits or three and two thirds digits, and that's where it

**Dave Jones:** gets a bit confusing. There's no real standard for that, but typically if it if it's got like two thirds or three quarters or something like that, they really mean that it can go a bit further than one. So it might be

**Dave Jones:** 3999 or it might be 2999 or even 4999 or something like that. Now, because it started becoming quite confusing, manufacturers started talking in terms of the number of counts, and I think this is a much better way to do it. So a a

**Dave Jones:** three and a half digit multimeter at plus minus 1999 is actually a 2,000 count meter, because it counts up to plus minus 2,000. And likewise, a four and a half digit meter is actually a 20,000 count. You can use these terms

**Dave Jones:** interchangeably. Now, how does this relate to accuracy? Well, it actually doesn't relate at all. It has nothing to do with accuracy. So, let's talk about this. Now, accuracy is a term when it comes to multimeters, people get it wrong all the time. And

**Dave Jones:** I'm I'm guilty of saying it too through sheer laziness or, you know, habit. It's wrong to say that this meter has an accuracy of four and a half digits or an accuracy of 10,000 counts. That is completely wrong. The

**Dave Jones:** counts, the number of digits, is the resolution. So, it's You should say that this meter has a 10,000 count resolution, not a 10,000 count accuracy. And if you, you know, if you say the wrong thing, it can make you

**Dave Jones:** seem like a bit of a dunce, especially if you're in a job interview or something and they ask the question, it can make you look like you don't know what you're talking about. Okay, now let's take a look at three typical

**Dave Jones:** multimeters and how the the number of digits or the resolution affects the usability of these meters. Now, I've got a Fluke 79 Series II here. Now, this is a 4,000 count or a three and three quarter digit meter. I've got the MeterMan 37 XR

**Dave Jones:** here and this one is a 10,000 count meter. The Fluke 87 V here is a the four and a half digit meter, but I've got it in it's actually got a mode that is actually 6,000 count mode. Okay, now I'm feeding the same voltage

**Dave Jones:** into all three meters and you can see they all read fairly similar. They, you know, there's there's slight differences there, but let's have a look what happens when I turn the voltage up here. Okay? Now, if I had a three and a half

**Dave Jones:** digit meter here, which I don't, it would have actually dropped down to two decimal places because it would have been over the 1999 limit, but none of them have reached that yet. So, let's keep turning this up, okay, and see

**Dave Jones:** which one actually drops its range first. And I'm sure you can guess which one it's going to be. Bingo, there it is. The Fluke 79 Series II because this is a 4,000 count meter, we're over that 4,000, we're basically

**Dave Jones:** over four, so it's got to go up to the next highest range. So, we lose one digit of resolution, okay? Not accuracy. Now, if we keep turning this up, we'll find that the Fluke 87V here is a 6,000 count, so

**Dave Jones:** as soon as it gets to six, or just slightly over, bang, it's changed upper range, also. So, I this is uh now, these are giving the same resolution, okay? This is a much more expensive meter um at 6,000 count,

**Dave Jones:** okay? But, it's but they've got the same resolution. Now, this Meterman 37XR at 10,000 count, you're still getting the extra digit of resolution, and this won't change ranges until you go right up to until you pass that 9999 limit, and

**Dave Jones:** bingo, there it is. Half digits, they're all back on an even playing field. But, let's switch the Fluke 87V to four-and-a-half digit mode, okay? Now, we've got this extra digit of resolution here, not accuracy, resolution. Now, you'll find that this 87V

**Dave Jones:** four-and-a-half digit meter is useful until once again, we get up to Once again, we get up to 20 odd volts and bingo, it's gone back. So, you can say that the 4 and 1/2 digit meter only has more resolution for 20% of its range

**Dave Jones:** over the 10,000 count meter. I said before that resolution, the number of digits on the display has nothing to do with accuracy. And that's true, okay? Accuracy of the meter is based on the percentage of the actual reading, not a full scale. So, a meter's

**Dave Jones:** accuracy will be specified as the percentage of the reading plus counts. Now, a typical like a good meter might have point an accuracy of 0.1% plus two counts. Now, what that means is if you're measuring 1 volt, okay? You will

**Dave Jones:** have an It will have an uncertainty of plus or minus 1 millivolt. 0.1% of 1 volt is 1 millivolt. But, you have to add on two counts to that plus or minus two counts to that displayed value. So,

**Dave Jones:** it will be if it's actually reading exactly 1 volt, okay? 1.000, then it can actually be 1.00 0 3 or plus minus or 0.997.

**Dave Jones:** So, that's resolution and accuracy. Now, let's talk about calibration. Everyone knows that uh you know, you should get your meter calibrated. What does that actually mean? What it means is that the meter has been checked. It's been It doesn't

**Dave Jones:** Calibration does not mean adjustment of your meter. When you send this away for calibration, it's They usually don't adjust it. What they will do is they'll measure it against a reference standard, and they will give you a test report for

**Dave Jones:** this, um giving you the actual typically giving you the actual figure, and um you know, and the error against that absolute reference or that transfer standard. And what you do with that calibration information determines how this multimeter is going to be used

**Dave Jones:** within your company, what applications it's going to use for, and how often you're going to calibrate it. Now, just because a meter has been calibrated yesterday does not mean it's going to be within spec today. It's uh It's all

**Dave Jones:** about Calibration is about the history of this meter, tracing. It's about traceability. You need to trace uh the calibration of this meter. You need a historical record of it over time, and then you build up confidence in this

**Dave Jones:** meter that it's not drifting. This is why some companies and some industries will actually uh uh you know, you have to actually use two multimeters to take a measurement just in case one of them has, you know, is is actually out. And they will, you

**Dave Jones:** know, anyone serious about electronics will actually have two multimeters. They won't rely on just one. They'll have two so that you can cross-check each other, and you can actually use a good known multimeter as a as a bit of a transfer

**Dave Jones:** standard to uh check and measure other instruments. And if you've got a bunch of multimeters, you can all cross-measure themselves, and you get more confidence that your meter is within specification. Usually, you'll follow the manufacturer's recommendation, which might be, say,

**Dave Jones:** every 12 months. But when you first get an instrument, you might want to calibrate it more often so that you build up more of that reference that historical reference data so you can track it. And once you know this meter

**Dave Jones:** is not, you know, it's really stable and it's not drifting at all, then you might actually widen your uh period of calibration 12 months. Then, you know, it still hasn't drifted at all, you might actually change it to two years.
