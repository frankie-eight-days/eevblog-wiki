---
video_id: tSzem8xshxk
title: EEVblog #576 - Advantest R6142 Current Voltage Generator
url: https://www.youtube.com/watch?v=tSzem8xshxk
source: youtube-asr
---

**Dave Jones:** Hi, just a quick video to show you what I'm playing around with at the moment. I just scored this very nice Advantest uh R6142 programmable DC voltage current generator. In fact, it's it's almost like a voltage and current standard. It

**Dave Jones:** specs are uh pretty darn uh good as we'll take a look at. And I scored this on eBay for about 300 bucks. And if you're not aware of Advantest, they are a huge Japanese company who primarily make automated test gear for like the

**Dave Jones:** semiconductor uh you know, fabrication industry and stuff like that. You know, they're a multi-billion dollar company make real high-end high-spec gear, but they also make some you know, some reasonably well for them uh sort of low-end gear like this. And they do

**Dave Jones:** spectrum analyzers and a whole bunch of other stuff. And this is a real nice bit of kit. And we'll take a quick look at it and I'll show you what I'm doing here cuz I've just done some uh a couple of

**Dave Jones:** days worth of uh data logging on this thing. And you would have seen the a couple of updates on my Twitter uh feed for this if you're following along at home. And I just wanted to see like how

**Dave Jones:** accurate and stable it was for generating in this case a 1 milliamp uh current over time. And not only for absolute accuracy, but for drift as well. And you may have just heard that my air con just turned off here. And

**Dave Jones:** I've been doing some uh that's where I turned the air con on this morning when I came in and it ramped up. So, I've sort of like had the air con off and on. And we'll take a look at what this data actually uh means

**Dave Jones:** and see how you know, see how good this is for uh calibrating my microcurrent for example cuz there's not too many really precise current generators on the market. And this is certainly one of them. And uh yeah, so is it good enough

**Dave Jones:** to um program a microcurrent at normally 0.05%. So, it's got to be better than that. You notice my battery LED is flashing there. That's a feature of course the the battery is um of course uh low. So what it does that's just the ESR of

**Dave Jones:** the battery uh there when it turns on the LED of course it draws more current which then drops under the voltage threshold of the uh comparator there really uh quite a neat little um you know unintended uh side effect there but

**Dave Jones:** I like that feature. So we'll take a quick look at the data sheet and uh this is basically the data sheet's all I can find at the moment. I haven't been able to find a uh user a full user manual for

**Dave Jones:** the thing let alone a uh service manual. So if you do have those uh please leave a link in the comments. Uh large capacity up to uh 32 volts 160 milliamps. I would have liked it to go up to 1 amp and on the low side as well

**Dave Jones:** but uh well you can't have everything. High accuracy uh .03% high stability low noise 3 millivolts peak 50 milliseconds settling time and uh here it is. The um unit precision voltage and current generator is ideal for evaluation of

**Dave Jones:** precision circuits and parts as well as cal- calibration of temperature controls. Unit uses a time sharing D to A conversion circuit which provides excellent linearity and stability. There you go. So it's um and it does um it's also got uh you can it's

**Dave Jones:** programmable as well hence you know because they're really into automated uh test functionality and things like that so so it's got a 160 uh step memory and uh it's 6 month uh guaranteed accuracy .03% for voltage and .035%

**Dave Jones:** for current and that 3 millivolt noise is 1/5 of their previous model. I don't know what the previous model is and there's probably another model after this as well. I'm not sure of the age of this thing it might have a date code on

**Dave Jones:** the back. I forget off the top of my head. We'll check it out but anyway um and the Advantest stuff you know like a lot of the high end manufacturers over engineered so that point 03% is going to

**Dave Jones:** be very conservative. So, we're going to get I think well within side that sort of accuracy. In fact, if we go over here and have a look at some of the specs, we're looking at voltage generation. There are the

**Dave Jones:** ranges. It's only got three current ranges. As I said, I'm a bit disappointed that it's only got 10 milliamps and 100 milliamp ranges. So, you know, I would have liked to you know, generate microamps or something like that. But, this isn't

**Dave Jones:** designed for low current. You know, you'd have to get like a Keithley current source or something. Although, I'm sure Advantest, if you pay big dollars, will sell you a low current source generator most likely. But, you know, overall accuracy we're talking you

**Dave Jones:** know, point 03% there plus you know, five plus a small percentage plus a small range error there. And point 035%. But, if you're talking you know, 24-hour stability, it goes down to point 01% which is pretty darn good. So, these

**Dave Jones:** specs are essentially and because it's likely over engineered, good enough for calibrating a point 05% microcurrent. And the temperature coefficient here, I E the parts per million per degree C is in the order of 20 odd ppm per degree C. Not bad. Although, my

**Dave Jones:** HP34461A here I'm using has a nominal five ppm per degree C. So, it's like at least four times better than that. And we won't worry about the plus offsets on the amp will. Just you know, keep things a bit simple for today. And on DC

**Dave Jones:** current though, my Agilent meter which we're using actually does go up to about 20 on the current. So, it's going to be for so for the current measurement here, the drift of my Agilent meter is you know, about roughly equivalent to this

**Dave Jones:** Advantest unit or at least these are going to be worst case figures. Now, let's have a look at what the data up here means that I've been getting. You'll notice I've been logging for almost 1 day and 20 hours and 11

**Dave Jones:** minutes. So, I've been going for quite some time and I've been here. I've turned the aircon. This is where I like came in and turned the aircon on and I turned the aircon on again this morning. It's you know, ramped back up. So, the

**Dave Jones:** temperature in the lab does change by, you know, like maybe up to 5° C variation depends on whether or not I've got the aircon when I leave the aircon on or off or not. When I've got the aircon on, I've actually measured the

**Dave Jones:** aircon in the the temperature in the room to be stable within plus minus 0.5° C. So, that's what the aircon cycles through. There's about a 5-minute cycle time between when it switches on and off to maintain the temperature here in the

**Dave Jones:** room. Anyway, um this looks like a Oh, you can probably see some of the multiplexing on the display there. You can probably see a bit of bit of flicker there. At least I can on my LCD screen. Now, if we have a look at the data

**Dave Jones:** here on my Agilent meter and I'm going to assume that my Agilent meter is like spot on. You know, it is my reference standard and I have actually confirmed that with my other reference gear. It is pretty darn good. It's way better than

**Dave Jones:** spec. It's you know, way better than it's calibrated spec. It's 24-hour spec. It's actually better than that absolute. So, I'm pretty damn confident in this Agilent meter. It really is kick ass. Now, you can see that there's a lot of noise in here and

**Dave Jones:** this looks like a huge variation, right? But, it's not really and I'll show you that in a second. And now, this So, this is the total data over that almost 2-day period there. And so, so we've got it

**Dave Jones:** set to all. Now, if I set it to recent, you can actually see the little tiny amount of noise. You can actually see the individual bit changes almost within that, uh, you know, within the sampling limit there. And as I've said in the

**Dave Jones:** review for this Agilent meter, its resolution is actually better than its nominal 6 and 1/2 digits when you're in this, uh, trend display mode. So, I I forget the exact figure, but it's like at least like 7 and 1/2 digits or

**Dave Jones:** something like that. So, it's pretty darn good. That's why I love the logging mode on this thing cuz you can get some excellent resolution better than what you get if you actually go into the, you know, pure number display like that. And

**Dave Jones:** that's how far we're off, um, in terms of I can actually jump between these things. Trend chart, there it is. So, we'll go back to all here, but that's like I've auto scaled that. So, they're the figures up there, and that's the,

**Dave Jones:** uh, real-time display up the top here. So, let's look at what these figures here actually represent. So, what I'm going to do is actually go into the, uh, vertical range, and I'm going to change the scale here to represent the, uh,

**Dave Jones:** 0.05% accuracy around the nominal 1 V that I would expect for my micro current. So, I can go in here. So, 0.05% of 1 V is 999. 0 5 0. And I'll do that for the high side as

**Dave Jones:** well, and you'll see how it's going to change. So, what we're going to do is 1 * 0.05 % there, and then we want to add that on, of course. And 1.0005. So, we want to get in here and change

**Dave Jones:** the scale to 1.0005. Oh, 000. 5 Bingo. 1.0005 milliamps. So, that range there now from 999.5 to 1.0005, that represents the nominal .05% range of my micro current here. And you can see how it's well within that window, not in

**Dave Jones:** terms of not only in terms of absolute accuracy. It's only, you know, a smidgen like, you know, half a bees dick under the nominal one microamp, but it's, you know, in terms of drift as well. You can see that the drift is actually pretty

**Dave Jones:** insignificant. It's well within that. So, I'm very happy with that. This Advantest unit on the 1 milliamp range more than accurate enough, better than its spec. And if you remember back here at the data sheet, it's one day

**Dave Jones:** stability spec. Spec. That's just a stability, let alone its absolute overall accuracy, which is up here. If we program in the .01% into there, bingo. This is what we get. .0 plus minus .01% around the nominal. So, it's still within side the .01%

**Dave Jones:** including the absolute value and the drift with in this case probably a 5° C three four or five maybe degrees C overall change here in the lab. So, that's brilliant. So, I'm really stoked with this unit. Absolute bargain, I

**Dave Jones:** think, for for 300 bucks a precision voltage and current generator that's good enough to calibrate any, you know, at least any four and a half digit meter. So, you know, it really is awesome and its specs are better than

**Dave Jones:** the data sheet. You know, it's made performance is measuring better than the data sheet. So, anyway, I've finished my data logging. I don't really need to, you know, save it. Not a huge deal. I got a video record here. That's good

**Dave Jones:** enough for me. And so, let's go back to the um Oops, sorry. Let's go back to the uh number display here, and let's uh play around with it. So, I'm going to screw up my data logging here, and uh let's

**Dave Jones:** see what happens. Uh like you can switch the polarity of the output. Let's So, let's see what happens when I go to positive and negative. Uh it's 0.9994. You know, let's take say 4 0 there. Look at that. It's not far off. It's

**Dave Jones:** changed by Well, bugger all, really. Um you know, well within well within the spec. So, that's pretty darn good. And let's see what happens when we go up one digit at a time. It's only a five-digit uh display, but it's still very good.

**Dave Jones:** Now, when I first uh got this thing, I thought, "Oh, you type in the number." cuz it's got like a number keypad here, and you type in the number, but it doesn't actually work like that. The These two uh are up-down buttons for

**Dave Jones:** this digit. These are up-down buttons for that digit, and so on. So, it's really quite weird. So, here we go. 999.4. Let's see if we go up one uh digit here. I We're going up uh 100 0.1 microamp

**Dave Jones:** there. Let's see if that jumps to uh in is still has exactly the same offset. Yeah, look at that. It jumped up, and it's still 41 there. And we can go up one, and we're increasing that digit. Look at that.

**Dave Jones:** Look at that. That is fantastic. So, that offset there is stays the same, but the jumps are precisely to that least significant digit there. I love it. Or actually beyond that. So, that is really, you know, quite impressive.

**Dave Jones:** I like that a lot. That is great. And of course, uh it's it goes up to 1.119, I think, is its maximum uh on all ranges like that. So, now let's check out the other ranges. The 1 mA of course is its

**Dave Jones:** maximum range minimum range there. I mean, you know, I can actually go down and generate, you know, 100 microamps or even 1 microamp or even 0.1 microamps, but then we're right down, you know, we're really quite right down in the

**Dave Jones:** noise. So, I'm not going to really, you know, it's so it's not the best for generating low value currents like that. I mean, look, you know, we're we're just around there, right? We're down at the least significant digit. Your

**Dave Jones:** accuracy is way out the window cuz you're not near the full scale there. So, whoop, let's go down. And let's go up a range. Let's go to 10 mA. Look at that. Still well within spec. Calculated that 0.002%

**Dave Jones:** absolute. Fantastic. I mean, that's within inside the spec of this Agilent unit. And on the 100 mA range, well, we're looking, you know, it's well within spec again. In this case, cuz it's 100, it's going to be this is going

**Dave Jones:** to be 0.005 or, you know, 0.004 % basically off from absolute. Once again, assuming that our Agilent unit here is absolutely bang on. But hey, these two units being like, you know, almost bang on together gives you a really good

**Dave Jones:** confidence that, you know, both units are working, you know, and well within specification, that's for sure. And of course, as I said, I've got other transfer standards which I can use to actually test precision voltage sources, precision resistors, and stuff that I

**Dave Jones:** can use to verify and sort of, you know, calibrate in quote marks my Agilent 34461A here. And I know it's well within specification, as I said. So, very, very confident about this puppy. So, I'm sure I'd bet money that if I took this to a standards

**Dave Jones:** cal lab, it would be well within spec, exactly what I'm measuring here. And we go negative on that. Look at that. Fantastic. All right, let's play around with the voltage mode, shall we? I'm still in that current mode, so we're getting a maximum output

**Dave Jones:** voltage of 13.4 volts there, but let's switch on over to volts. So, we're in we're generating 1 volt. I've got to press the operate button. That's the you know, and that's the output on off button. And check that out.

**Dave Jones:** Look at that. Bang on, of course, because we've got our four decimal places there. So, not a problem. Let's go up one digit. Look at that. Once again, completely spot on with the jumps. There's only that offset at the end. The point, you know, the

**Dave Jones:** point 0072 offset there. So, that is incredible. So, what does that work out to in percentage? Well, let's do a quick calculation. 1.000074 minus 1 is that times 100. There it goes. Bang. Look at that. 0.0074%.

**Dave Jones:** Awesome. And 10 volts. Not a problem. And it's lowest range, of course. Oh, no, it's lowest range There's 100. Sorry, it's lowest range is 10 millivolts. So, that one is a little bit out. There we go. Least significant

**Dave Jones:** digit there. Oh, no. Oh, no. We have four least significant digits. But even right down on the 10 millivolt range, we're still under 0.05%. Beauty. And it's got a four-wire input that sense, too. Although, I haven't actually been able to get that to work,

**Dave Jones:** cuz I put it on four-wire, and I don't attach anything to here, and it's still displaying the current just fine. So, you know, I'm not sure what's actually going on there, whether or not it's got a measurement. I don't think it's got a

**Dave Jones:** true measurement mode to read back. It's just, you know, it's just actually a generator. Um, but anyway, um, probably need a user manual for that. It's got adjustable current limit set so you don't damage anything. There's just a

**Dave Jones:** pot in there, you can just turn it so, you know, the operator can't come around and, you know, bang a few buttons and and blow up your uh uh you know, real expensive semiconductor under test or something like that. And they're very

**Dave Jones:** likely very high-quality tellurium copper contacts. No doubt. They sort of have that sort of tinge to them that you probably can't see it on camera, but it, you know, you can sort of tell those high-quality tellurium copper contacts

**Dave Jones:** when you see them. And if we take a random micro current here, whack in our 1 milliamp, assuming it's spot on, we knew it was actually a bit uh low. Anyway, it's still 0.012% out from that nominal, well within spec.

**Dave Jones:** And the milliamps range there at 100 milliamps test current, we're only 0.03% out. That's better than its nominal spec of 0.1%. And there's the back of the unit. It's got GPIB interface, trigger and ready trigger input, ready output,

**Dave Jones:** operator hold. I guess you can turn that off so the operator can't do anything stupid. Calibration uh button, which I'm not going to mess with. Of course, uh selectable mains voltage so you can safely buy this gear anywhere in the

**Dave Jones:** world, like here in Australia, and just switch it over. And some, looks like some BCD inputs as well for test systems and stuff like that. And a voltage limit pot on the back. Manufactured by Advantest in Tokyo in

**Dave Jones:** Japan. Brilliant. Japanese made. Unfortunately, no date code. We'll have to crack it open and have a look. And I can confirm after popping off the lid that this is about a '94 vintage. So, there you go, about 20 years old, but

**Dave Jones:** still very nice little bit of kit. And no, I'm not going to show you inside because I said this would be a quick video, and it won't be if I do a teardown. And I can't just blow my wad

**Dave Jones:** on one video, can I? So, yes, if you want me to if you want to see a teardown inside this thing, please let me know in the comments. Although, I probably will anyway, so there you go. I hope you

**Dave Jones:** enjoyed that little look at this Advantest R4142 programmable DC voltage current generator. And I reckon Advantest is a nice little search term to whack into eBay to try and find some good bargains. But, their stuff usually goes for a price premium, but I

**Dave Jones:** got this at quite a decent price, I think. So, if you like the video, please give it a big thumbs up. And if you want to discuss it, jump on over to the EVBlog forum. Catch you next time.
