---
video_id: ETCOhzU1O5A
title: EEVblog #703 - Rigol DS1054Z Oscilloscope Review Summary
url: https://www.youtube.com/watch?v=ETCOhzU1O5A
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 34, "3": 49, "4": 62, "5": 76, "6": 90, "7": 106, "8": 120, "9": 136, "10": 145, "11": 162, "12": 176, "13": 187, "14": 199, "15": 216, "16": 228, "17": 243, "18": 255, "19": 269, "20": 281, "21": 296, "22": 308, "23": 325, "24": 341, "25": 354, "26": 366, "27": 382, "28": 395, "29": 410, "30": 426, "31": 435, "32": 451, "33": 464, "34": 477, "35": 491, "36": 504, "37": 517, "38": 529, "39": 542, "40": 555, "41": 569, "42": 587, "43": 603, "44": 619, "45": 634, "46": 647, "47": 660, "48": 672, "49": 689, "50": 706, "51": 717}
---

**Dave Jones:** Hi, it's product review time. Now, for the last 6 years or so, the Rigol DS1052E here has been pretty much the benchmark standard for entry-level scopes. It couldn't be beat for quite a long time, and there's quite a lot of competition

**Dave Jones:** to this now, but Rigol have released the new DS1054Z, and it's a four-channel scope, still 50 MHz entry-level bandwidth, but it's got more memory, it's got a bigger screen, it's got all sorts of bells and whistles built in. It's an absolutely killer

**Dave Jones:** scope for $399 US, or even less than that, and different prices depending on which country you're in. So, I've done quite a few videos on this already. This is going to be the summary review video, a bit different to how I normally do

**Dave Jones:** reviews. This will be about 10 minutes, just direct overview of, you know, pros and cons of this scope. If you want more detailed stuff, I've linked in videos down below. I've linked teardown video, which has additional information. I've

**Dave Jones:** linked in videos to firmware issues and firmware fixes in this thing. I've linked in a reverse engineering version of this thing to see if it's actually got the 100 MHz bandwidth built in, and yes, it does. This is a summary review

**Dave Jones:** video. Let's go. First of all, it's a very small and compact scope, much smaller than what you would think. There it is compared to the size of my hand, but it is quite hefty, and really feels like it's a real quality

**Dave Jones:** uh designed and manufactured unit. Feels really good. All the buttons are pushable, which is excellent, so you get the additional functionality in there. Unfortunately, one downside is that the rotary encoders sometimes skip uh the occasional menu item or overshoot or

**Dave Jones:** something like that. So, just a little bit touchy on the encoders. Huge selling point is that it's four channels. Awesome, but unfortunately, it doesn't come with auto probe interface around here, so it can't automatically detect the times 10 probe when you plug it in.

**Dave Jones:** You've got to select that manually here, but no big deal. And because it's four channels like this, and it's a very narrow and really compact scope, unfortunately, you have to share the vertical controls here between all four channels, but that's the price you pay

**Dave Jones:** for such a small scope. And this really is a great scope for the beginner. Big green help button on the front. You hit that, and then you can just choose any of the button which you need help with.

**Dave Jones:** Rise time, for example, it explains with waveforms exactly what the measurement function is for. Terrific stuff. Although the screen is relatively large and high res for this particular size unit, unfortunately, these menus on the left and right side here are fixed. You

**Dave Jones:** can't turn them off like you can on the 2000 series to expand the waveform to the full screen. Unfortunately, that's just a disadvantage of this particular model. And also, the fonts on these can be very, very small. So, if you got bad

**Dave Jones:** eyesight, that could be a real issue. And the screen is reasonably well laid out. You've always got whether or not you're triggered or you're waiting for a trigger up here. You've got your horizontal time base always displayed. You've got your

**Dave Jones:** vertical controls always down here, which you can select. It shows which one is highlighted and grays out the others. It always shows you the sample rate and the memory depth, so you always know where you stand with the scope. Very

**Dave Jones:** nice. The pretty much standard waveform zoom display there. It always shows you delayed offset of your waveform. Just a crazy thing like 000 picoseconds. That's just nuts. Little firmware issue. And it always shows your trigger level up here. And

**Dave Jones:** your waveform window here does actually shift up if you turn on these measurement capability down the bottom here. And you can change the font size of these as well, so it's not overlaying your waveform data. That's quite smart.

**Dave Jones:** And even though it does have a nice big high resolution 800 by 480 wide screen on here with 12 divisions, which is excellent. It is not the brightest thing on the market and the angle is not that terrific, but it's

**Dave Jones:** adequate for the job. It takes about 22-23 seconds to start up, little bit annoying, but pretty much par for the course on these sort of scopes these days. Now, the fan is unfortunately a little bit on the loud side, not the

**Dave Jones:** loudest I've heard, but fairly distracting in a very quiet room. But anyway, you could get in there and retrofit a silent one in there. This is a basic bandwidth of 50 MHz, which is pretty good and it's a reasonable 1 gig

**Dave Jones:** sample per second, but that is only for single channel like this. If you turn on a second channel like that, it halves to 500 meg and if you turn on a third or a fourth, it drops down to 250 meg samples

**Dave Jones:** per second. And if you buy the 100 MHz model, then 250 meg samples across all four channels is not the best. So, don't expect the full 100 MHz bandwidth when you got all four channels turned on. And the great thing

**Dave Jones:** is you get a lot of memory with this thing, 12 meg standard or if you got the upgraded model, 24 meg memory. That's a huge deep memory, but once again, if you turn on the multiple channels, you do

**Dave Jones:** actually lose some of that unfortunately. It really has very nice serial decoding and trigger capability. You can do SPI, I squared C and RS232 and parallel, but unfortunately, this is an optional extra. And it really does have an amazing range of measurement and

**Dave Jones:** statistics capability. It's absolutely phenomenal for a low-end scope like this, fantastic. And it's got your basic FFT functionality as you'd expect on a modern scope. And when you turn on the measurements and the statistics and the FFT math and everything else, it is

**Dave Jones:** still a reasonably responsive scope, doesn't slow down a huge amount. It's still usable. And it's got all the mathematical operators you could possibly want. Terrific stuff in a low-end scope. And it does have a USB host on the front. You can just plug a

**Dave Jones:** key in, and then you can just uh store uh either the waveforms, the actual data all the data itself you can analyze later, or you can uh get screen captures really easy. And it comes standard on the back with a trigger out and

**Dave Jones:** pass/fail uh output as well for mass testing. Yes, it does have full mass testing built in. And it does have uh LXI LAN capability built in as standard. Fantastic until you realize that Rigol software is just crap. It basically does

**Dave Jones:** not come with any software. Comes with really annoying drivers. Fortunately, some people have written some decent third-party uh apps to uh talk to this thing and analyze data and operate it remotely. But Rigol, they don't provide anything. And one of the best things

**Dave Jones:** about this scope, and absolutely incredible for the price, it has one of the best intensity-graded displays on the market. Look at that. It's got 64 uh shaded levels. Not as good as the Rigol 2000 series, but still very impressive,

**Dave Jones:** very analog-like display, and very fast updating as well, especially for uh the price of uh up to 30,000 waveforms per second. So, I it's This is one of the best intensity-graded displays on the market. Can't be beat. Fantastic. Very

**Dave Jones:** analog-like if you're coming from an analog scope. And it does go down to 1 mV per division. In fact, if you get the hack for the thing, it does go down to 500 µV, but the hardware doesn't really

**Dave Jones:** support it properly, so don't bother. But it's got uh normal, uh peak, average, and high-resolution mode as well, which works really nice. It's a reasonably low-noise scope. And it's got a built-in hardware frequency counter as well. Fantastic. Unfortunately, it

**Dave Jones:** doesn't have any uh software or hardware filtering in it on your input signal. So, no low-pass or high-pass filters, unfortunately. And the dual-screen uh delayed time base works exactly as you'd expect and with the very deep memory on

**Dave Jones:** this thing, it's a very powerful tool. And if you go into triggering here, there is a ridiculous amount of triggering options, even run pulses and everything else and you can trigger off the serial ones as well, but these are

**Dave Jones:** optional extra, they're not standard. And these are all the all the various options that you can get all the triggering ones, the decoders, the memory depth up to 24 meg, the recorder, which is the segmented memory feature and the bandwidth up to 100 megahertz.

**Dave Jones:** So you can buy these and yes, the scope is hackable because the 100 megahertz bandwidth is actually physically built into the hardware and the software options as well. So if you're into that sort of thing, it is possible at the

**Dave Jones:** moment. Unfortunately, some of the menu options in here can be a bit convoluted. You have to go you know, to a secondary menu like this and it shows you these little dots here show you which menu you're on and it can

**Dave Jones:** just be a little bit intimidating and convoluted for the beginner until you get used to the thing. You got and you got to realize that all of your measurement capability over here, all your buttons and all these menus are all

**Dave Jones:** dedicated so you can go horizontal and vertical and all these measurement functions down here. It's ridiculously powerful the amount of measurement capability, but it is very nice to actually have all these dedicated buttons here. You know, this side of the

**Dave Jones:** scope is just for measurements. But as I said, it does take up some permanent screen area. And things like the segmented memory, they're buried away in the utility menu here and it's called record. So it's not as good as the 2000

**Dave Jones:** series Rigol with its dedicated segmented memory control on the front. So it's basically a record replay feature and as I said, this is optional, but it allows you to extend the already deep memory to actually capture a ton of

**Dave Jones:** data that's not possible with any regular scope. And you get these RP2200 switchable times 1 times 10 passive probes with it. 150 MHz bandwidth, which is a pretty good. They're reasonable quality. I'm not going to write home about them, but you do get four of them.

**Dave Jones:** Awesome. Did I mention it's a four-channel scope for 399 bucks? So, there you have it. That's a summary of the Rigol DS1054Z. What's my verdict? Huge thumbs up. Seriously, if you're in the market for an entry-level scope under, say,

**Dave Jones:** anywhere under 500 bucks or something like that, possibly anywhere under 1,000, just go and buy this. Don't bother buying anything else. It simply cannot be touched. Unless, of course, you got a very specific requirement like the font's too small or or something

**Dave Jones:** like that. But, it's a well-made scope and it does still have a few little design issues, maybe a few quirks and things like that. But, the price-per-performance, the bang per buck you get with this thing for $399, the

**Dave Jones:** four channels, the um all the great measurement capability. Yes, it is hackable if you want to do that sort of thing at the moment. And just the amount of analysis capability built in, it's just oh, the intensity graded

**Dave Jones:** analog-like display is one of the best on the market. And you get all this and it's pretty fast updating as well. And you get all this for under 400 bucks. Unbelievable. The market's completely changed. So, seriously, I cannot see

**Dave Jones:** another scope that offers the same bang per buck as this. It at the moment it cannot be beat. The equation might change. It's the start of 2015 now. The equation might change in a year's time. If you're still watching this video in

**Dave Jones:** 2016 or 2017, this Rigol DS1052E hung around for like 6 years. It it led the market for like 4 and 1/2 5 years, probably. Um and this one might do the same. That remains to be seen, but just go out and buy it if you're in

**Dave Jones:** there. Just don't worry. Just get this. That's it. Easy. Make your decision easy. It's a great scope. It really is. It's the best entry level scope on the market. You can't go wrong. Unbelievable. Anyway, lots of other videos I've linked in for this

**Dave Jones:** scope as well. And so be sure to watch those. They'll all be linked in after this. They'll have fancy little pretty rolly things on it. And if you like the review, please give it a big thumbs up. And

**Dave Jones:** yeah, comment, rate, all that sort of stuff. And EEVblog forums linked down below if you want that. Hope you enjoyed it. Catch you next time.
