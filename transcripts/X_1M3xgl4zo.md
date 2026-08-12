---
video_id: X_1M3xgl4zo
title: EEVblog 1448 - Convert a Fluke 77 IV to True RMS for 10 CENTS!*
url: https://www.youtube.com/watch?v=X_1M3xgl4zo
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 38, "3": 55, "4": 72, "5": 89, "6": 102, "7": 116, "8": 131, "9": 149, "10": 163, "11": 175, "12": 188, "13": 202, "14": 214, "15": 225, "16": 236, "17": 259, "18": 275, "19": 295, "20": 309, "21": 322, "22": 340, "23": 352, "24": 364, "25": 380, "26": 397, "27": 413, "28": 433, "29": 446, "30": 459, "31": 475, "32": 487, "33": 501, "34": 513, "35": 527, "36": 540, "37": 559, "38": 573, "39": 589, "40": 598, "41": 612, "42": 631, "43": 644, "44": 658, "45": 674, "46": 690, "47": 703, "48": 717, "49": 730, "50": 744, "51": 760, "52": 779, "53": 793, "54": 809, "55": 820, "56": 835, "57": 849, "58": 868, "59": 882, "60": 896, "61": 915, "62": 933, "63": 954, "64": 972, "65": 984, "66": 996, "67": 1013, "68": 1031, "69": 1046, "70": 1056, "71": 1070, "72": 1082, "73": 1093, "74": 1107, "75": 1121, "76": 1134, "77": 1147, "78": 1160, "79": 1173, "80": 1189, "81": 1202, "82": 1220, "83": 1235, "84": 1251, "85": 1267, "86": 1282, "87": 1299, "88": 1313, "89": 1324, "90": 1338, "91": 1352, "92": 1364, "93": 1372, "94": 1384}
---

**Dave Jones:** Hi, in the previous video I did a teardown of the Fluke 77-4 and compared it with the Brymen BM786 meter and I noticed something really interesting in this. So, in a minute I'm going to show you how to turn an average

**Dave Jones:** responding Fluke 77-4 into a true RMS Fluke 177 and do it for about 10 cents. Stick around. But, curiously here on the website, I didn't actually know, but I think Fluke have technically discontinued the 70 series. The venerable 70 series. I think it's

**Dave Jones:** actually been discontinued cuz if you go to their digital multimeter page here, there is no Fluke 70 series anymore. They've got the 170 series. They've got 175, 177, and 179, but that's it. There is no 70 7. Like, it's still there on

**Dave Jones:** the site if you actually search for it, but I think as I talked about in the video previous to that about why Flukes are so expensive in that yeah, this is appealing to legacy customers only cuz the Fluke 70 series were average

**Dave Jones:** responding meters. They were not true RMS meters. So, a slight bit of history here. The Fluke 79 series 3, that actually was true RMS, but they don't sell the 79 anymore. That was replaced by the 179 or the 170 series. In fact,

**Dave Jones:** the entire 70 series has been replaced by the 170 series true RMS, but there are customers who still want average responding meters instead of true RMS. As I said, they have these built the readings for these average responding

**Dave Jones:** meters built into test procedures in the military and government and organization. They don't want to change all their test procedures. They want an average responding meter. So, Fluke will still sell you one, but basically nobody buys the 70 series anymore. You buy the

**Dave Jones:** 170 series. So, you buy the 177 and it's exactly the same meter as the 77 four except it's true RMS. Now, when they actually moved over to the 170 series, this was about 2001 and they dropped the uh you know, the

**Dave Jones:** slash like the mark four and everything from it. And so, the 177 you buy today is still the same 177 from 2001. So, it's a 20-year-old model now. There is no 177 mark two or whatever. It's still the 177. So, 20-year-old model now, but

**Dave Jones:** they kept selling these uh 70 series they the mark three was the first series Fluke that actually looked uh like this with the new overmolded design and that's where uh the 170 series stem from. And then when they moved to the

**Dave Jones:** mark four, the only one you could get was the 77 mark four. They just didn't bother with the previous versions cuz they knew they were phasing it out. They wanted to go to push everyone to the 170 series true RMS, but they kept one model

**Dave Jones:** in the 70 line as an average responding, but I think it's gone cuz like it's just not on their main page. Wow. Anyway, I actually forget how long these like the 170 series has been around for 20 years

**Dave Jones:** now. That is absolutely incredible. Anyway, during the teardown video of the 77 four, I noticed something interesting in the chips here. And uh this is my um high-res photo available on my Flickr account. I put all my high-res photos on

**Dave Jones:** my Flickr account. Go check that out. Anyway, um if you want to know how I get these excellent uh PCB uh photos, uh head on over. It's actually on my second channel. I did a part three to my PCB uh

**Dave Jones:** photography light box and this is how I get the excellent photos. So, I tell you how to make one in there. Anyway, um yeah, I noticed something really interesting. We've got our MSP 430 processor over here. We've got a uh

**Dave Jones:** 20-bit delta sigma uh converter in here. The reference is in there somewhere. We've got the Fluke multimeter chip so which by the way, if you search the number here, you can actually still find and you can actually looks like you can

**Dave Jones:** buy this chip from third-party vendors. Absolutely amazing. Anyway, the interesting thing is up here. This is an AD737. That's a true RMS converter chip used in like a ton of multimeters on the market. What's it doing in a Fluke 77

**Dave Jones:** that is an average responding meter? Why does it have the chip there? Now, as I noted in my teardown video, the PCB actually is the Fluke 170 series. There it is, Fluke 170X up there. It's exactly the same PCB. And sure enough, I just

**Dave Jones:** looked for some teardown photos, found them on the EVBlog forum. Everything's on the EVBlog forum. And sure enough, the 170 and the 79 have the exact same components. Except one. And sure enough, the AD737, it's a true RMS to DC converter used in

**Dave Jones:** multimeters. So, what gives? Why would they go to the expense to put this chip in an average responding meter? Well, consistency in build is one thing. Of course, Fluke make a quite a decent margin on these things. So, maybe the

**Dave Jones:** cost of a 737 is not a big deal. They just have the same build. But remember when I said there is actually one component build difference between the 77 and the 177. This is where you go to the features over here. Look at this.

**Dave Jones:** Computes true RMS, average rectified value, and absolute value. It's actually got three different modes, this chip. It can actually do average responding multimeter functionality itself. Of course, most average responding meters on the market, the real cheap ones, they

**Dave Jones:** do this inside the multimeter chip set itself. But the Fluke chip set obviously doesn't do that. In fact, we can have a look at the block diagram in a minute, but what they're doing in the 77 and other model Flukes, as we'll look at,

**Dave Jones:** they're actually using this RMS converter chip in the average responding mode. So, I won't go into huge detail how this works. I'll link in the data sheet down below if you want to have a read for yourself, but basically, so

**Dave Jones:** what we've got here, this is our input signal here and this is our input FET, a buffer, and that goes into effectively what is a full wave bridge rectifier and that gives you an absolute value. It takes any negative stuff and puts it and

**Dave Jones:** flips the negative half up to the positive half. And then that goes into then there's an RMS core down here and that's what does the true RMS conversion part using an averaging capacitor down here. And then up here, you can choose

**Dave Jones:** either AC or DC feedback path here. So, if you bypass this RMS circuit down here, then you'll get a DC average response just like any DC average responding meter. And of course, you should know your peak to RMS conversion

**Dave Jones:** factors and of course, RMS is .707 and your average is .636. That's the DC average of the peak value. So, what they do is they calculate a scale factor in here of in this case 1.11, which is .707 / .636.

**Dave Jones:** Of course, all it does is basically it squares the signal, it takes the average, and then contains the square root, RMS, root mean square. And any RMS converter will have a maximum crest factor it can actually tolerate. And you

**Dave Jones:** know, like a pulse like a very narrow pulse down here, like an extreme crest factor and your true RMS multimeter probably can't handle that sort of thing. But anyway, you can actually get errors. But what happens in your side

**Dave Jones:** your multimeter, if you've got an average responding meter, they it's actually calibrated to match the average to give you an average responding for a perfect sine wave. So, here it is, undistorted sine wave. So, perfect sine wave, if you've got a true RMS meter, it

**Dave Jones:** gives you 0.707 of the peak value, and an average responding meter will also give you 0.707. There's no error whatsoever, and they give you the error over here, zero. But, you put in any other wave form, a square wave, a

**Dave Jones:** triangle wave, noise, rect- a pulse wave, you know, SCR switching wave form, which is like a switching thing, and then no, it's not a sine wave, so you're going to get an error on your average responding meter, and that

**Dave Jones:** can be some of these errors can be pretty high, right? You know, it's it's not a huge amount. If you're talking about, say, a triangle wave or something like that, like 3.8%, it's not much, but the further away it gets from that ideal

**Dave Jones:** sine wave, the more error you're going to get. This is why people use true RMS meters, and they're pretty much a standard these days, except on really low-cost meters. Because most multimeters that need true RMS function, they have to spend more in their bill of

**Dave Jones:** materials to get this AD737 chip, but Fluke, because their meters are so high-priced, and they design it in, a they're just using the chip anyway, and they're using it in average mode. So, how do you do that? Well, it's real

**Dave Jones:** simple. You simply remove the averaging capacitor. And if you do that, it basically passes straight through, and you get the average mode. So, surprise surprise, what do we find in our average responding Fluke 77? Yep, a capacitor right there, missing. The 33 microfarad

**Dave Jones:** capacitor, and that is the only difference between a Fluke 77 and a Fluke 170 series. But, it's not the only meter that does this. Check out the Fluke 87. We've actually got the service manual here, and I'll link it in down below, and we've

**Dave Jones:** got the full schematics. Check this out. Whoa, beautiful. Back when you could get schematics. I cannot find a Fluke 77 schematic or a 170 series schematic, but it's going to be very similar to this. And there's that Fluke custom ASIC I

**Dave Jones:** showed you before. And yeah, I think you can actually buy this on the market. So, yeah, yeah, I don't know if you can buy it from Fluke, but other suppliers have it by the looks of it. Now, the good

**Dave Jones:** thing about the schematic is that they tell you, "Look, for the model 87 only, they do this. This is it looks like that's doing locate near the V terminal. They are using that as a temperature sensor. Yeah, yeah, thermal compensation

**Dave Jones:** there. And there's an 800 Hz filter here, which is specific to the model 87 only. And then model 83 only here. But bingo, same thing happens here. There is your averaging capacitor on your AD737 model 87 only 33 micro Farads. So,

**Dave Jones:** that's what's missing from our Fluke 77 to turn it into a Fluke 177. And I haven't checked, but I'm willing to bet this is also the same on the Fluke 27 series 2 as well, cuz that's an average

**Dave Jones:** responding version of the Fluke 28. I bet you they're doing exactly the same thing, a missing capacitor. That's it. They're designed for different markets. All right, let's do a test before we do modification here. I've got three different meters, the true RMS Fluke

**Dave Jones:** 87V, the 77IV we're going to modify, and the 17B here. And both of these are average responding meters. They are calibrated for an average response of a sine wave. So, these should read the same. And they might have different like

**Dave Jones:** upper frequency limits and stuff, but at a reasonable frequency, I'm going to use 88 Hz here. Why not? So, that is well within the specifications of these meters. So, I'm feeding in a 1 V RMS sine wave here into all three of them in

**Dave Jones:** parallel. As you can see, they all read identically. 17B is a bit lower cuz this is not a very super duper accurate meter, and these are within one least significant digit count. So, that's for a sine wave, and that's what, even

**Dave Jones:** though these are average responding meters, and we are not going to get an average response of the sine wave of zero because that's a mathematical average. The how the averaging response in these works is, we saw before, the

**Dave Jones:** full wave bridge rectifier, and then it's calibrated um to give you the the average result based on a sine wave. But, what happens when you don't use a sine wave? Well, we have the handy table here from uh the data sheet. You can

**Dave Jones:** actually um calculate these yourself. So, for an undistorted or uh perfect sine wave here, um we should, of course, get exactly the same value. There's 0% error between an RMS meter and an average responding meter cuz these are

**Dave Jones:** calibrated for a sine wave. So, you get 0% error. But, if we change this to a symmetrical square wave, i.e., 50/50 uh duty cycle square wave, then we should get an error of plus 11%. And sine to square, it should stay at 1 V RMS. This

**Dave Jones:** remains the same. Bingo. There's our 11% error, very close to it. So, a triangle wave, we're looking at a minus 3.8% error. So, it should be negative. Uh yep, that's about a uh negative uh 3.8 percent error, is it not? Now, a lot of

**Dave Jones:** people actually make the mistake of thinking that a perfect sine wave actually has a crest factor of one. Now, of course, the crest factor is uh the peak value divided by the RMS value. The biggest the peak to RMS value um is, of

**Dave Jones:** course, 1.414. You should know that for your uh peak to RMS conversions. Only a square wave actually has a perfect crest factor. Um a good data sheet for a meter will actually have and specify the maximum uh crest factor for its true RMS

**Dave Jones:** measurement chip. Let's play around with some other waveforms here. Let's do a PRBS, which is a pseudo random Yeah, we're not going to bother to calculate it, but both are reading the same and it's reading high. So, we'll see what

**Dave Jones:** that measures after the modification. And I've got a pulse here, which is set to 1 ms pulse time. And as you can see, even the Fluke 87V can't handle that horrible crest factor there. So, it's 0.565, but the average responding meter

**Dave Jones:** is even worse. It'll be interesting to see after modification if this goes up to match the true RMS meter. So, let's solder in the capacitor onto the handy pad, which we have down here. It's even marked. Fantastic. Look at this.

**Dave Jones:** Positive on this side. Got to my AVX tantalum sample kit. Very handy. Now, the Fluke 87V schematic and parts list says it's a 33 mic, same as the Analog Devices data sheet. It says it's a 16 V 300 m. The best I've got down here

**Dave Jones:** that's not a biggie is this 33 mic. That's a B case and that's only 10 V. But considering that this is a 9 V battery, it'll be good enough for Australia, I think. So, I don't know what the ESR of this is. I don't think

**Dave Jones:** it's going to matter. So, let's use one of those. All right, let's get some freshy on there, shall we? I think that's that could be an A. But anyway, got the polarity correct there. No worries. She'll be right

**Dave Jones:** because tantalums, unlike electrolytic capacitors, they have the mark up there for the anode, not the cathode. So, the positive. Whereas electrolytic caps have it have the black mark on the on the negative. So, that's rather annoying, but there we go. No worries.

**Dave Jones:** All right, we have our brand new Fluke 177 meter here. However, But that I think about it, before I cross my fingers and power this up, I don't think we're going to get away with this without recalibrating this meter. Because even though it's

**Dave Jones:** calibrated with a sine wave, the internal scale factor of the conversion is going to be different. So I reckon we're going to end up with the scale factor of for the RMF 0.7 which is 0.707 divided by the yeah, divided by the DC

**Dave Jones:** average which is 0.636. So I reckon we're going to end up with an error of 1.1. Have I got that in the right direction? I think so. I think we're going to be should read up by 11%. Yeah, same as it does with a square

**Dave Jones:** wave, isn't it? So let's power this sucker on. Of course it's going to work. It doesn't say 177. That'd be nice. Um so yeah, I don't know. Maybe we can mod the firmware, something like that. Anyway, and if you mod the firmware by

**Dave Jones:** the way, we could turn this into a 179 by adding temperature measurement cuz I think it's all in there but yeah, it's just the firmware you pay extra for. Anyway, yeah, let's plug it in. Here we go. I've got my leads.

**Dave Jones:** Bingo. 1.11. So yeah, before I just measure the other stuff, I'll go to the calibration manual and we'll have to enter the cal mode on the back and we'll have to recalibrate. Now to do this, you got to

**Dave Jones:** switch it to millivolts over here and then you got to probe in the backside. Oh, yep. There we go. Got it. Ta-da, we're in. Now unfortunately, the steps we want the AC volt steps here six and seven and

**Dave Jones:** also of course amps as well. So you've got AC down here for the 400 milliamps and the 6-A range as well. Now, I'm hoping that we can actually bypass these other steps cuz I don't want to have to actually calibrate

**Dave Jones:** all the other ranges. I just want to be able to calibrate that one. Um yeah, I'm going to see if I can like bypass this and only calibrate the ranges we want. I bet you Murphy says we can't do that.

**Dave Jones:** Yeah, okay. Right. So, this reads the live reading on the input. It's uncalibrated, okay? So, press and hold this button to display the required input min max. So, there you go. So, it's telling us we have to feed in 600

**Dave Jones:** mV DC. Great. But, it says press the yellow button to store the calibration and advance to the next step. This button is also used to exit calibration mode. Can we just like think I'm going to be forced to actually calibrate this

**Dave Jones:** entire meter, damn it. Now, I've got nothing plugged into it, and if I press that to go to the next one, it just double beeps at me. So, it's smart enough to know, "No, you idiot. Um you haven't got anything plugged in."

**Dave Jones:** And if I maybe try and hold that down, does that do anything? Nope. Does range do anything? Nope. Ah, no. No, I'm I'm forced into it. I don't know. Backlight? Yeah, the backlight's still independently works. Um no. No, I'm forced to calibrate this

**Dave Jones:** whole damn thing, damn it. So, anyway, lucky I have my calibrators over here, AC and DC, and well, I've got various ohms-y things. And like, you know, this is not a high-spec meter. And of course, I can compare it against my 7 and 1/2

**Dave Jones:** digit jobbies over here. The bar graph actually it still works. It does the business. So, there you go. So, I'm feeding in 600 mV. That's what we have to feed in, and that's what we're live reading at the moment. But, there is

**Dave Jones:** course it's uncalibrated. It says it goes into uncalibrated mode when it shows you that live reading. But, we know we're feeding in the precise value. In that well, there it is over on there. That's good enough for Australia,

**Dave Jones:** definitely. So, I whack that in, and boom. We got a step two. Anyway, I'm up to the 60 V step and uh well, that only goes up to 10 V, so yeah, I'm going to have to use some of

**Dave Jones:** my other standards over here, high voltage uh supply. So, I'm up to step six. I switched over to my AC volts uh standard here and I can generate both required 600 mV at 60 Hz and also 600 V

**Dave Jones:** at 60 Hz. And not everyone, unfortunately, is going to have um this bit of kit. And likewise here, we have 660 V live, but I'm feeding in 600, so I'm going to calibrate that sucker. And we're up to ohms-y. Well, dumb ass Dave

**Dave Jones:** tried to cheat, didn't he? And I exited that cal procedure thinking it would have stored all those previous steps in the E-squared prom and Bob's your uncle, right? I wouldn't have to I could just like get a quick result just to show

**Dave Jones:** that it worked and I could do the current range later. Um it yeah, nah. Oh, winner winner, chicken dinner. I got it. Um it was not easy getting uh the AC current source uh particularly the 6 amp AC

**Dave Jones:** uh at 60 Hz current source, but I was able to uh cobble it together here in the lab and I got it. Um and here it is. It's a true RMS. There you go, 1 V RMS. Um it's recalibrated. You see how it was

**Dave Jones:** off before? It's now recalibrated. So now, we can fiddle around to see if it matches this. So, let's go waveform. Let's go our square wave. Oh, look at that. Like a bought one. Like a bought one, true RMS, none of that average

**Dave Jones:** responding rubbish. Ramp. Look at that. It was matching this before. Now, it's matching this. Oh, Bobby dazzler. Triangle wave we're getting before. How about that pseudo random binary sequence we got before? That's not to I'm I'm still going to call that. I mean, this

**Dave Jones:** might have a different response to this, perhaps, but it's certainly not um higher like we're getting before. So, that's all right. There we go. I've got an exponential rise function there. Um yeah, just the first uh one that I came off the rank. And um

**Dave Jones:** yeah, sure enough, there's that 1 ms pulse we had before. That's not too shabby. So, there you go. I I did it. I converted a Fluke 77 Series 4 into a Fluke 177. I don't think there's any other differences, really. I think it's

**Dave Jones:** just that the 170 All of the 170 series, every model, is uh true RMS, whereas the original 70 series was average responding, but it has the true RMS capable chip in it. Don't recommend doing this at home unless you have the

**Dave Jones:** ability to calibrate all those ranges. So, if you know of a way to skip those steps in there, cuz that's annoying. Cuz sometimes you might just have like one range that's out, and you just want to fix that one range. In this case, that

**Dave Jones:** would have been really nice. That being said, it's not easy to get uh 6 amps, 50 hertz, you know, you have to like budge something with a uh transformer and a you know, big variable resistor load or something like that. Um which is

**Dave Jones:** basically how I got it. I used my um variable frequency um AC, and it it was 4 amps maximum um on the name plate, but I managed to get 6 amps out of it. And I just put it into a 2 ohm load, and I

**Dave Jones:** just adjusted the output voltage until I um got the, you know, near enough. And it measured on the 7.5 digit meter, and Bob's your uncle. I was like, "How do you get it?" But yeah, you got to complete every single step. And then it

**Dave Jones:** says end uh on the end of it. And then you press the yellow button, and then it just boop, it goes back to normal. And it doesn't So, you can't just go halfway through or do an individual step. If you

**Dave Jones:** know how, leave it in the comments. And you should be able to do that, I think, with the uh 80 series and probably the uh 20 series as well, the 2728. So, yeah, if you do know, uh let us know in

**Dave Jones:** the comments down below. But, hope you found that interesting and useful. If you did, please give it a big thumbs up. As always, comment down below. Catch you next time.
