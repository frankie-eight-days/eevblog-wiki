---
video_id: ETCOhzU1O5A
title: EEVblog #703 - Rigol DS1054Z Oscilloscope Review Summary
url: https://www.youtube.com/watch?v=ETCOhzU1O5A
source: youtube-asr
timestamps: {"0": 0, "1": 30, "2": 42, "3": 55, "4": 65, "5": 76, "6": 90, "7": 106, "8": 120, "9": 136, "10": 145, "11": 160, "12": 173, "13": 184, "14": 194, "15": 204, "16": 214, "17": 226, "18": 243, "19": 260, "20": 271, "21": 281, "22": 294, "23": 309, "24": 326, "25": 344, "26": 353, "27": 363, "28": 376, "29": 392, "30": 402, "31": 419, "32": 429, "33": 442, "34": 456, "35": 467, "36": 478, "37": 491, "38": 504, "39": 522, "40": 534, "41": 542, "42": 552, "43": 570, "44": 587, "45": 607, "46": 627, "47": 640, "48": 651, "49": 663, "50": 677, "51": 689, "52": 699, "53": 712, "54": 721}
---

**Dave Jones:** Hi, it's product review time. Now, for the last 6 years or so, the Rigol DS1052E here has been pretty much the benchmark standard for entry-level scopes. It couldn't be beat for quite a long time, and there's quite a lot of competition to this now, but Rigol have released the new DS1054Z, and it's a four-channel scope, still 50 MHz entry-level bandwidth, but it's got more memory, it's got a bigger screen,

**Dave Jones:** it's got all sorts of bells and whistles built in. It's an absolutely killer scope for $399 US, or even less than that, and different prices depending on which country you're in.

**Dave Jones:** So, I've done quite a few videos on this already. This is going to be the summary review video, a bit different to how I normally do reviews. This will be about 10 minutes, just direct overview of, you know, pros and cons of this scope.

**Dave Jones:** If you want more detailed stuff, I've linked in videos down below. I've linked teardown video, which has additional information. I've linked in videos to firmware issues and firmware fixes in this thing.

**Dave Jones:** I've linked in a reverse engineering version of this thing to see if it's actually got the 100 MHz bandwidth built in, and yes, it does. This is a summary review video.

**Dave Jones:** Let's go. First of all, it's a very small and compact scope, much smaller than what you would think. There it is compared to the size of my hand, but it is quite hefty, and really feels like it's a real quality uh designed and manufactured unit.

**Dave Jones:** Feels really good. All the buttons are pushable, which is excellent, so you get the additional functionality in there. Unfortunately, one downside is that the rotary encoders sometimes skip uh the occasional menu item or overshoot or something like that.

**Dave Jones:** So, just a little bit touchy on the encoders. Huge selling point is that it's four channels. Awesome, but unfortunately, it doesn't come with auto probe interface around here, so it can't automatically detect the times 10 probe when you plug it in.

**Dave Jones:** You've got to select that manually here, but no big deal. And because it's four channels like this, and it's a very narrow and really compact scope, unfortunately, you have to share the vertical controls here between all four channels, but that's the price you pay for such a small scope.

**Dave Jones:** And this really is a great scope for the beginner. Big green help button on the front. You hit that, and then you can just choose any of the button which you need help with.

**Dave Jones:** Rise time, for example, it explains with waveforms exactly what the measurement function is for. Terrific stuff. Although the screen is relatively large and high res for this particular size unit, unfortunately, these menus on the left and right side here are fixed.

**Dave Jones:** You can't turn them off like you can on the 2000 series to expand the waveform to the full screen. Unfortunately, that's just a disadvantage of this particular model. And also, the fonts on these can be very, very small.

**Dave Jones:** So, if you got bad eyesight, that could be a real issue. And the screen is reasonably well laid out. You've always got whether or not you're triggered or you're waiting for a trigger up here.

**Dave Jones:** You've got your horizontal time base always displayed. You've got your vertical controls always down here, which you can select. It shows which one is highlighted and grays out the others.

**Dave Jones:** It always shows you the sample rate and the memory depth, so you always know where you stand with the scope. Very nice. The pretty much standard waveform zoom display there.

**Dave Jones:** It always shows you delayed offset of your waveform. Just a crazy thing like 000 picoseconds. That's just nuts. Little firmware issue. And it always shows your trigger level up here.

**Dave Jones:** And your waveform window here does actually shift up if you turn on these measurement capability down the bottom here. And you can change the font size of these as well, so it's not overlaying your waveform data.

**Dave Jones:** That's quite smart. And even though it does have a nice big high resolution 800 by 480 wide screen on here with 12 divisions, which is excellent. It is not the brightest thing on the market and the angle is not that terrific, but it's adequate for the job.

**Dave Jones:** It takes about 22-23 seconds to start up, little bit annoying, but pretty much par for the course on these sort of scopes these days. Now, the fan is unfortunately a little bit on the loud side, not the loudest I've heard, but fairly distracting in a very quiet room.

**Dave Jones:** But anyway, you could get in there and retrofit a silent one in there. This is a basic bandwidth of 50 MHz, which is pretty good and it's a reasonable 1 gig sample per second, but that is only for single channel like this.

**Dave Jones:** If you turn on a second channel like that, it halves to 500 meg and if you turn on a third or a fourth, it drops down to 250 meg samples per second.

**Dave Jones:** And if you buy the 100 MHz model, then 250 meg samples across all four channels is not the best. So, don't expect the full 100 MHz bandwidth when you got all four channels turned on.

**Dave Jones:** And the great thing is you get a lot of memory with this thing, 12 meg standard or if you got the upgraded model, 24 meg memory. That's a huge deep memory, but once again, if you turn on the multiple channels, you do actually lose some of that unfortunately.

**Dave Jones:** It really has very nice serial decoding and trigger capability. You can do SPI, I squared C and RS232 and parallel, but unfortunately, this is an optional extra. And it really does have an amazing range of measurement and statistics capability.

**Dave Jones:** It's absolutely phenomenal for a low-end scope like this, fantastic. And it's got your basic FFT functionality as you'd expect on a modern scope. And when you turn on the measurements and the statistics and the FFT math and everything else, it is still a reasonably responsive scope, doesn't slow down a huge amount.

**Dave Jones:** It's still usable. And it's got all the mathematical operators you could possibly want. Terrific stuff in a low-end scope. And it does have a USB host on the front.

**Dave Jones:** You can just plug a key in, and then you can just uh store uh either the waveforms, the actual data all the data itself you can analyze later, or you can uh get screen captures really easy.

**Dave Jones:** And it comes standard on the back with a trigger out and pass/fail uh output as well for mass testing. Yes, it does have full mass testing built in. And it does have uh LXI LAN capability built in as standard.

**Dave Jones:** Fantastic until you realize that Rigol software is just crap. It basically does not come with any software. Comes with really annoying drivers. Fortunately, some people have written some decent third-party uh apps to uh talk to this thing and analyze data and operate it remotely.

**Dave Jones:** But Rigol, they don't provide anything. And one of the best things about this scope, and absolutely incredible for the price, it has one of the best intensity-graded displays on the market.

**Dave Jones:** Look at that. It's got 64 uh shaded levels. Not as good as the Rigol 2000 series, but still very impressive, very analog-like display, and very fast updating as well, especially for uh the price of uh up to 30,000 waveforms per second.

**Dave Jones:** So, I it's This is one of the best intensity-graded displays on the market. Can't be beat. Fantastic. Very analog-like if you're coming from an analog scope. And it does go down to 1 mV per division.

**Dave Jones:** In fact, if you get the hack for the thing, it does go down to 500 µV, but the hardware doesn't really support it properly, so don't bother. But it's got uh normal, uh peak, average, and high-resolution mode as well, which works really nice.

**Dave Jones:** It's a reasonably low-noise scope. And it's got a built-in hardware frequency counter as well. Fantastic. Unfortunately, it doesn't have any uh software or hardware filtering in it on your input signal.

**Dave Jones:** So, no low-pass or high-pass filters, unfortunately. And the dual-screen uh delayed time base works exactly as you'd expect and with the very deep memory on this thing, it's a very powerful tool.

**Dave Jones:** And if you go into triggering here, there is a ridiculous amount of triggering options, even run pulses and everything else and you can trigger off the serial ones as well, but these are optional extra, they're not standard.

**Dave Jones:** And these are all the all the various options that you can get all the triggering ones, the decoders, the memory depth up to 24 meg, the recorder, which is the segmented memory feature and the bandwidth up to 100 megahertz.

**Dave Jones:** So you can buy these and yes, the scope is hackable because the 100 megahertz bandwidth is actually physically built into the hardware and the software options as well. So if you're into that sort of thing, it is possible at the moment.

**Dave Jones:** Unfortunately, some of the menu options in here can be a bit convoluted. You have to go you know, to a secondary menu like this and it shows you these little dots here show you which menu you're on and it can just be a little bit intimidating and convoluted for the beginner until you get used to the thing.

**Dave Jones:** You got and you got to realize that all of your measurement capability over here, all your buttons and all these menus are all dedicated so you can go horizontal and vertical and all these measurement functions down here.

**Dave Jones:** It's ridiculously powerful the amount of measurement capability, but it is very nice to actually have all these dedicated buttons here. You know, this side of the scope is just for measurements.

**Dave Jones:** But as I said, it does take up some permanent screen area. And things like the segmented memory, they're buried away in the utility menu here and it's called record.

**Dave Jones:** So it's not as good as the 2000 series Rigol with its dedicated segmented memory control on the front. So it's basically a record replay feature and as I said, this is optional, but it allows you to extend the already deep memory to actually capture a ton of data that's not possible with any regular scope.

**Dave Jones:** And you get these RP2200 switchable times 1 times 10 passive probes with it. 150 MHz bandwidth, which is a pretty good. They're reasonable quality. I'm not going to write home about them, but you do get four of them.

**Dave Jones:** Awesome. Did I mention it's a four-channel scope for 399 bucks? So, there you have it. That's a summary of the Rigol DS1054Z. What's my verdict? Huge thumbs up. Seriously, if you're in the market for an entry-level scope under, say, anywhere under 500 bucks or something like that, possibly anywhere under 1,000, just go and buy this.

**Dave Jones:** Don't bother buying anything else. It simply cannot be touched. Unless, of course, you got a very specific requirement like the font's too small or or something like that. But, it's a well-made scope and it does still have a few little design issues, maybe a few quirks and things like that.

**Dave Jones:** But, the price-per-performance, the bang per buck you get with this thing for $399, the four channels, the um all the great measurement capability. Yes, it is hackable if you want to do that sort of thing at the moment.

**Dave Jones:** And just the amount of analysis capability built in, it's just oh, the intensity graded analog-like display is one of the best on the market. And you get all this and it's pretty fast updating as well.

**Dave Jones:** And you get all this for under 400 bucks. Unbelievable. The market's completely changed. So, seriously, I cannot see another scope that offers the same bang per buck as this.

**Dave Jones:** It at the moment it cannot be beat. The equation might change. It's the start of 2015 now. The equation might change in a year's time. If you're still watching this video in 2016 or 2017, this Rigol DS1052E hung around for like 6 years.

**Dave Jones:** It it led the market for like 4 and 1/2 5 years, probably. Um and this one might do the same. That remains to be seen, but just go out and buy it if you're in there.

**Dave Jones:** Just don't worry. Just get this. That's it. Easy. Make your decision easy. It's a great scope. It really is. It's the best entry level scope on the market. You can't go wrong.

**Dave Jones:** Unbelievable. Anyway, lots of other videos I've linked in for this scope as well. And so be sure to watch those. They'll all be linked in after this. They'll have fancy little pretty rolly things on it.

**Dave Jones:** And if you like the review, please give it a big thumbs up. And yeah, comment, rate, all that sort of stuff. And EEVblog forums linked down below if you want that.

**Dave Jones:** Hope you enjoyed it. Catch you next time.
