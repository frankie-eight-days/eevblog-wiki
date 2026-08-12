---
video_id: 0AEVilxXAAo
title: EEVblog #1325 - OPAMP Shootout - Datasheet Deep Dive
url: https://www.youtube.com/watch?v=0AEVilxXAAo
source: youtube-asr
timestamps: {"0": 0, "1": 19, "2": 29, "3": 43, "4": 57, "5": 72, "6": 85, "7": 93, "8": 104, "9": 120, "10": 130, "11": 144, "12": 167, "13": 179, "14": 193, "15": 208, "16": 220, "17": 235, "18": 251, "19": 259, "20": 277, "21": 284, "22": 302, "23": 310, "24": 324, "25": 338, "26": 357, "27": 366, "28": 375, "29": 387, "30": 401, "31": 417, "32": 435, "33": 454, "34": 465, "35": 479, "36": 490, "37": 501, "38": 513, "39": 526, "40": 547, "41": 561, "42": 577, "43": 596, "44": 604, "45": 617, "46": 626, "47": 634, "48": 646, "49": 655, "50": 669, "51": 682, "52": 694, "53": 708, "54": 718, "55": 734, "56": 743, "57": 754, "58": 767, "59": 782, "60": 792, "61": 810, "62": 821, "63": 834, "64": 858, "65": 870, "66": 892, "67": 904, "68": 925, "69": 943, "70": 958, "71": 971, "72": 985, "73": 1000, "74": 1019, "75": 1034, "76": 1047, "77": 1057, "78": 1076, "79": 1086, "80": 1098, "81": 1111, "82": 1123, "83": 1133, "84": 1154, "85": 1169, "86": 1181, "87": 1195, "88": 1224, "89": 1233, "90": 1245, "91": 1257, "92": 1268, "93": 1288, "94": 1297, "95": 1308, "96": 1320, "97": 1327, "98": 1343, "99": 1363, "100": 1381, "101": 1394, "102": 1408, "103": 1420, "104": 1433, "105": 1444, "106": 1456, "107": 1475, "108": 1495, "109": 1503, "110": 1519, "111": 1535, "112": 1553, "113": 1567, "114": 1575, "115": 1584, "116": 1594, "117": 1603, "118": 1613, "119": 1621, "120": 1633, "121": 1651, "122": 1665, "123": 1677, "124": 1693, "125": 1708, "126": 1717, "127": 1724}
---

**Dave Jones:** Hi, in a previous video, linked in down below and at the end, if you haven't seen it, where we looked at finding potentially any modern, more modern, higher performance replacement for the MAX4238/4239 used in the microcurrent, which is like a 12, 13-year-old design, at least.

**Dave Jones:** Something like that. And well, we looked at a few chips on the market and really just like superficial top end look, but I wanted to actually have a more comprehensive look.

**Dave Jones:** And actually, one of the chips that we covered and looked at in the previous video, even though I sort of dismissed it based on like some top level specs, this video, we're going to have a shootout between these two particular chips.

**Dave Jones:** We're going to go deeper into the data sheets on both of these and look and see how they compare, cuz we might have a winner winner chicken dinner here that is a better op-amp than the MAX4238/4239.

**Dave Jones:** So, let's take a look at it. The one we're going to take a look at today is the OPA189. It's actually and also 2189. So, it's available in the single one and the OPA2189 is a dual version.

**Dave Jones:** And it's available in SOIC package, a SOT23 and a VSSOP package as well. So, choose your flavor. Here we go. I'll whack the Dave head up the top for you.

**Dave Jones:** I know there's a lot of floating Dave head aficionados out there and yes, I have flipped my image now so that if I look over on the right-hand side here, it's going to be right.

**Dave Jones:** If I look over on the left-hand side here, my eyes actually follow. So, let me know if you like floating Dave head up the top or you like it down the bottom.

**Dave Jones:** Yeah, we looked at this and it had a few interesting things in that it was it had mux-friendly inputs. I mean, it didn't have any clamping anti-parallel clamping diodes in it, which means that it doesn't interrupt your your mux you know, switching and things like that.

**Dave Jones:** So, yeah, it's got mux friendly inputs here and also RFI EMI filtered inputs. That's always good. And it's actually got a wide supply voltage range 4.5 to 36 volts.

**Dave Jones:** And that's one of the first things we need to look at because if you compare that to the max 4239, this one is only 2.7 to 5.5 volts supply there.

**Dave Jones:** So, your maximum dynamic range can only be 5.5 volts and dynamic range is important when you're talking about a current shunt amplifier like the microcurrent. It's one of the the major things because when you're measuring a device that switches between say a sleep mode and a and a higher power mode like this, then you know, it wakes up and it transmits via Wi-Fi or does you know,

**Dave Jones:** some processing and then shuts back down. That's you know, the dynamic range you're trying to measure and if you don't have a sufficient voltage range there, you're it limits the dynamic range and you might have to range switch and things like that.

**Dave Jones:** So, this is essentially part two of designing a better microcurrent by the way and I'm going to do future videos on this. So, the OPA189 wins out on supply voltage range, dynamic range goes up to 36 volts.

**Dave Jones:** It's actually quite remarkable. Now, of course, one of the major requirements is offset voltage of the op-amp and the max 4239 of course is famously like no ultra low 0.1 volts offset which is I can't really control my mouse very well, can I?

**Dave Jones:** 0.1 volts offset voltage there and that's incredibly low. There's basically nothing else on the market that can really match it, but as we saw last time, the devil is in the detail.

**Dave Jones:** You need to go down here and let's have a look at this graph here, input offset distribution. And they don't tell you how many different parts, but basically this is the production test uh of they you know take hundreds of different chips.

**Dave Jones:** They measure them and they basically bin them in a in this case uh it looks like a 0.3 microvolt bin here. So, you can see that 40% of the chips here are within plus minus 1.15 microvolts.

**Dave Jones:** And that's you know that's pretty tight. Of course, this is going to be a like a production bell curve. Geez, I'm not very good at drawing a bell curve, am I?

**Dave Jones:** The mouse isn't very good for this sort of thing. I need one of those huge big tablet-y things that I can you know write on. Anyway, I do have my Microsoft Surface, but uh so yeah, you can see it basically extends out uh pretty much to uh plus minus 1 microvolt here.

**Dave Jones:** And of course, if you look at the actual um specs, they are actually higher than that. Uh we need to never look at these top level uh specs, by the way.

**Dave Jones:** So, let's actually go down and have a look at the real input offset voltage note one. Typically, 0.1 max of two microvolts here. Now, this is where the the maximum value of the 189 is not going to be as good, but let's look at note number one.

**Dave Jones:** Always look at the notes, see what they have to say for themselves. There it is. Uh guaranteed by design thermocouple and leakage effects uh preclude measurement of this parameter during production.

**Dave Jones:** So, basically, they they don't production test every uh unit, but they screen during production test to eliminate defective units that are outside that maximum 2.5 microvolt input offset volt.

**Dave Jones:** Hang on. Why is this one two microvolts here and it's 2.5 here? What's different? Uh voltage range 2.7 volts to 5.5 common mode equals V ground common mode V V output VCC on two for V out.

**Dave Jones:** Aha, this is over the full temperature range. There you go. Whereas this table, this electrical characteristics table here is over only the 20 like at nominally 25°. So, they've got two different tables.

**Dave Jones:** So, you know, trap for young players there. Don't necessarily take, you know, this table for granted because, you know, you might go, "Ooh, it's 2 microvolts maximum here. That's beauty."

**Dave Jones:** But, who knows? The next table over here it could have been 20 microvolts. You just never know. But, it's fairly tight, you know, it's almost tight, not quite tight as a nun's nasty, but pretty close.

**Dave Jones:** 2.5 microvolts there over the full operating temperature range. Now, the 189, uh I don't believe is as good as that. So, top level here, yeah, 3 microvolts maximum. It's, you know, it's getting pretty close.

**Dave Jones:** So, let's go down to information, electrical characteristics. This one's at nominally uh 25°. Offset voltage here, see, it's not as tight on the typical. In fact, it's like it's four times worse.

**Dave Jones:** Right? So, you might think that this particular chip is like, "Oh, it's four times worse, not nearly as good. Won't even consider it." Okay, this is where you need to dive deeper into the data sheets and have a second look at these sort of things, which is what I was always going to do.

**Dave Jones:** And the maximum isn't that much more than the plus minus two. But, technically, this is a worse chip in offset voltage, but that's not an absolute showstopper if it has advantages in other areas, be it other performance like bandwidth and noise and other things which we're going to look at in this video.

**Dave Jones:** Or be it price. If this was like 10 times cheaper, you'd go, "Ooh, yeah. Oh, you know, happily live where you know, you might happily trade off." You might not, but you might decide, "Yeah, I'll happily trade off, you know, four times worse typical input offset voltage for, you know, half the price or 1/10 the price." I don't know.

**Dave Jones:** I think the price is quite similar between these chips, by the way. So, yes, here's an example where data sheets can differ. The maximum one we saw had completely different tables for different voltages.

**Dave Jones:** This one is ambient typical around ambient of 25, but they include a separate line item here for the full range. So there you go, plus minus four. We had plus minus two and a half on the Maxim unit.

**Dave Jones:** So not as good, but may not be a showstopper. So here's the devil in the detail. Let's go down to our production yield down here and see what we get.

**Dave Jones:** Aha. Offset voltage production distribution. Once again, they are number of units. There you go, they tell you. Excellent. Yeah, they give you, you know, you statisticians out there. There you go.

**Dave Jones:** You can look at all that. But look, it's, you know, once again, it's that bell shape bell shaped curve. You're going to get that on practically any production type yield parameter, not just input offset voltage.

**Dave Jones:** You'll get that on almost everything. Let's take say 40%. You know, there's three up here at around 10 12%. So let's take three or four of those, right? Which is equivalent to the one bar we saw on the Maxim, and it's within it's not as tight, right?

**Dave Jones:** So four of these, you extend that down, it's like plus minus .25. So it's a little bit worse, but not a huge amount. But look at the Maxim. You remember when the Maxim one it extended down to minus one here and plus one here?

**Dave Jones:** It's basically the same yield. It's not as tight. The Maxim one was like tighter, like that. This one's a little bit wider, but the maximums of plus minus one microvolt here, they aren't like too dissimilar.

**Dave Jones:** It's almost an identical chip. And it's pretty usually not wise to design your products around the fact that it's got a nice tight production curve like this, cuz that could vary over time and production processes and all sorts of things.

**Dave Jones:** So, this is only a typical thing. This is not a guaranteed. They will only guarantee you, you know, what was it? Three? Yes, it was plus minus four. And by the way, the dual version, the 2189, actually has a higher offset voltage.

**Dave Jones:** So, just be aware of that. Some of the parameters in here, if you go deep enough, they will change for the dual part or a quad part or whatever as opposed to a single.

**Dave Jones:** So, there can be advantages, even though it'll cost you more to use that single chip part. They can actually be performance advantages there. So, anyway, and this is at a VS of plus minus 18 volts.

**Dave Jones:** Once again, they don't want they won't give you the offset voltage for lower voltages. It could change at lower voltages. That's something you might have to measure in your design, for example.

**Dave Jones:** But anyway, they measured lots of parts here, and it's it's basically the same, you know, plus minus one. But as I said, it could be plus minus four over here.

**Dave Jones:** So, that's what they guarantee. But when they go measure them, look, you know, bang on. So, they're going to tweak their production process, so it's They're They're always going to tweak it, so it's pretty much in the center like this.

**Dave Jones:** It might shift a little bit, but, you know, not a huge amount. But the actual yield, you know, could get bigger, something like that. But they would have to change something for that to happen.

**Dave Jones:** So, yeah, interesting, huh? And also, the 189 has um the same yield for input bias uh distributions and input offset uh current as well, if you're interested in those sort of things.

**Dave Jones:** Which, if you're down in your picoamps, you know, you're really, you know, could care about that sort of thing. Um so, yeah, they've got the yields for that. So, I'm going to call those practically equivalent on input offset voltage, or at least good enough for Australia, anyway.

**Dave Jones:** So, let's go back to the maximum. What's the next thing we need to care about here? Well, it's going to be our gain bandwidth product. Look at this, the MAX4239, that's the uh which with the minimum gain of five by the way to get that.

**Dave Jones:** Um 6.5 MHz gain bandwidth product. And I've done an entire video on uh cascading amplifiers for gain bandwidth products, and I'll have to link that one in cuz it is an excellent video.

**Dave Jones:** But once again, never take the top level spec for granted, always go to the table. The gain bandwidth product here uh with a load of 10 K 100 puff measured at 100 kHz.

**Dave Jones:** With it doesn't tell you what gain that's measured at those. Some data sheets will tell you that. But yeah, normally 6.5 MHz, okay? So, is the 189 better? Well, let's go to the videotape.

**Dave Jones:** 14 MHz. Let's go check it out. And the slew rate by the way, might check that out in a second, but so gain bandwidth product and they actually specify the unity gain bandwidth here.

**Dave Jones:** The unity gain bandwidth is already bigger. It's 8 MHz. Um but the gain bandwidth product at gain of 1,000, as I said, and some data sheets do tell you that, it's 14 MHz.

**Dave Jones:** So, this is a wider bandwidth op amp. So, that's a win for the 189. It's higher bandwidth. And of course, bandwidth is uh one of the important criteria of a shunt amplifier like the microcurrent.

**Dave Jones:** So, anyway, slew rate 20 V per microsecond. And of course, because it's got a lower bandwidth, the maximum is only one maximum is only 1.6 V per microsecond. So, like more than an order of magnitude better slew rate.

**Dave Jones:** Huh. I'm going to have to start writing a list of actual parameters here and which one wins. All right, what's the next thing we care about? Well, we do care about uh supply current.

**Dave Jones:** So, let's have a look here. The maximum uh device 600 microamps supply current per amplifier cuz we got multiple amplifiers. It does add up. If we go down here, we're talking about like a a of 900 microamps, but you know, I'll take them at their word of the 600 microamps.

**Dave Jones:** We don't care about shut down cuz we're never shutting it down. And the 189, 1.3 milliamps. So, it consumes twice the current. So, that's a win for the MAX4239.

**Dave Jones:** But, you might be willing to trade off and I'm certainly willing to trade off in this design supply current for bandwidth, noise, and other performance parameters. Okay, next thing, let's just go short circuit current.

**Dave Jones:** You know, what can this uh sucker drive? Plus minus 65 milliamps for the 189 and 40 milliamps for the Maxim. So, that's a win to the 189. Now, of course, it's important it could be an absolute show stopper if you don't get your ground sensing input and rail-to-rail uh performance cuz well, you may not care about these things in this uh particular case.

**Dave Jones:** Yes, we do have to sense uh to ground. If you do it in the single uh unipolar supply configuration, do it in the bipolar supply uh configuration, doesn't matter.

**Dave Jones:** But, yep, rail-to-rail output includes negative rail, so they both get a tick. Now, another one of the biggies is actually noise here uh because I've actually done a whole video, which is excellent by the way, not that I like to toot my own horn, but I think it's really uh quite a great video where I talk about uh measuring noise of op-amps and I actually demonstrate it on the bench with a

**Dave Jones:** dynamic signal analyzer how to measure the performance. And I'm going to be buying these chips and actually uh comparing these two chips in a future video in terms of like their noise floor and response and uh stuff like that.

**Dave Jones:** Anyway, low noise, 1.5 microvolts from DC to 10 hertz. Well, let's go and check the video tape. Now, I won't go into the differences between noise cuz I've done a whole video on that, but basically uh there's two ways you can measure either peak-to-peak uh noise like this in voltage or you can talk about noise density like this, which is over a given bandwidth.

**Dave Jones:** Um it's you know, spectral density uh pretty much. And that's in uh nanovolts per root hertz, capital N. Volts per root hertz, oops. Somebody give that Look, they've used nanovolts up here, and they've used capital N volts down here, oops.

**Dave Jones:** Yeah, great stuff. Anyway, uh for 1 kHz bandwidth, which is a typical uh specification, 30 nanovolts per root hertz for the MAX4239. So, you basically have to multiply this factor by the bandwidth.

**Dave Jones:** It's not divide, you actually multiply it by the bandwidth, and that'll be your total um output noise basically. But, they give us a figure like this, but that's only low end if you care about uh that sort of stuff.

**Dave Jones:** We don't necessarily care about that. So, anyway, 30 nanovolts per root hertz. Dave head's got to go down to the bottom for this. Uh 17 nanovolts RMS. They actually uh noise, if it's in volts is always RMS uh noise by the way.

**Dave Jones:** Um so, that's uh up to 10 hertz. So, 0.1 microvolts uh peak to peak. Wow, that's more than an order of magnitude better. The MAX4239 was 1.5 microvolts peak to peak.

**Dave Jones:** This is 0.1. WOW, that's over the 10 hertz range. And nanovolts uh per root hertz, the same 1 kHz bandwidth here, 5.2 versus 30 for the maximum. Wow, six times lower.

**Dave Jones:** So, this is a substantially lower noise op-amp than the MAX uh the MAX4239, which you kind of expect cuz it's drawing like what uh three times the current, three, four times the current, or something like that.

**Dave Jones:** So, you'd expect that. Um it's you know, usually you're going to trade our supply current for noise. That's one of the typical uh things. But, if you're willing, if you're happy to do that, then wow, this is a substantially lower noise op-amp.

**Dave Jones:** And of course, noise gets multiplied by the gain as well, which hopefully we'll um show this in future videos when we build these up and actually compare them. But, that is a huge tick um for the 189.

**Dave Jones:** That could be one of your most important parameters. Um, cuz the micro current is not exactly a low noise device. So, yeah, this could have huge advantages. And things like input common mode voltage range V ground minus one, that's going to be the same.

**Dave Jones:** Uh common mode voltage range, yeah, I'm not not too concerned about that. Let's have a look at the common mode rejection ratio. Not really uh important for the micro current, but worth a squeeze.

**Dave Jones:** Typical 140 uh down at the 2.25 V. So, yeah, there you go. So, at the lowest voltage, 140 dB. And they don't note one down here. Oh, they don't test it.

**Dave Jones:** That's the same. Yeah, 140 dB. Floating head David again. Input uh bias current. This is important because uh you need a low input uh current due to the topology measuring across a 10 K source impedance on the nano amp uh range.

**Dave Jones:** So, you know, you don't want to sort of uh you want a decently low bias uh current there. We'll read the note in a second, but basically one puff, one pico amp there.

**Dave Jones:** Um, input offset current is two pico amps. This is for the maximum. What does note two have to say for itself? In plus and in minus uh gates to CMOS transistors, typical input bias currents of one pico amp.

**Dave Jones:** CMOS leakage is so small it's impractical to test in guarantee in production. They're screened uh to eliminate defective units. So, they basically have a go no go for input uh bias current, but it's basically so one pico amp is like so low you don't need to worry about unless you're in some ridiculously ultra critical design uh where yeah, it would matter and then you're going to pay 10

**Dave Jones:** bucks for an op-amp that's specifically, you know, test every unit for input offset current. Oh, here we go. Input bias current the 189 Oh, it's 70 times worse. That's a lot.

**Dave Jones:** So, big tick for the 4239 there and it's the same for the dual part as well. I'm surprised it's not a little bit different there but and the input offset current as well.

**Dave Jones:** 140 picoamps. So, so once again, that's you know, hugely more than the Maxim device. But in this particular case, I'd have to run through the numbers but I I think we're okay there.

**Dave Jones:** 70 picoamps is you know, it's it's worth considering and looking at but it's probably not a show stopper. So, input bias current, you know, you wouldn't throw this chip out just because of that unless you really needed you know, ultra-critical type stuff which we don't necessarily need because as I said, I'm happy to trade off supply current like and accuracy and stuff like that if you get higher bandwidth and lower noise

**Dave Jones:** and other advantages. So, yeah, it's yeah, I wouldn't rule that out. Okay, and we don't really care about crosstalk or total harmonic distortion. What wonder what it is. Look at this.

**Dave Jones:** Oh, you audio fools. Look at this. Point double O double O six percent. Wow, but you know, they can still hear that. Yeah. Does Maxim even have total harmonic distortion?

**Dave Jones:** I don't think they do. Couldn't give a rat's ass. I don't blame them. Okay, another thing we probably want to have a look at here is overload recovery time because if you drive the probably done a video on this.

**Dave Jones:** If you drive the input to an op-amp hard and make it saturate, it actually takes time like milliseconds like which is quite significant time for the signal to recover.

**Dave Jones:** And for a device like the Microchip account that's designed to measure like really fast changes in like sleep and wake up currents and things like that. If you especially if you auto range and you don't if you're outside the dynamic range and then you're forced to auto range, you're saturating the op amp unless you take measures to clamp it and things like that and prevent it.

**Dave Jones:** You're but then you need extra parts and extra design tweaking. We won't go into that for this video. But that can really impact what you're going to see on the scope and things like that.

**Dave Jones:** You may see this like decay curve like this. You might think, "Oh, that's what my my product's actually doing that." No, that's the settling of the you know settling time of the op amp doing it.

**Dave Jones:** Anyway, overload recovery time here, let's have a look. Once again, this is nice. It gives you in different number of bits like 0.1% which which equates to like a 10-bit analog-to-digital converter.

**Dave Jones:** So, it's nice of them to put that in there. It was a nice touch. It just means that you don't have to get out your confuser here and actually calculate things.

**Dave Jones:** You can just go, "Okay, I've got a 12-bit ADC that I'm using, you know, so yeah, what roughly 0.025% is 4.1 milliseconds." Anyway, let's take the 0.1% cuz that is a typical recovery time.

**Dave Jones:** A 3.3 milliseconds for the maximum. And overload recovery time for the 189, 320 nanoseconds. We're down in the nanoseconds not these milliseconds rubbish or microseconds. 320 nanoseconds. How many orders of magnitude is that better than the maximum?

**Dave Jones:** That's really incredible. So, like recovery, huge tick for the 189. And that's a it can be a huge massive advantage in a product like this. So, a winner. And let's look at the settling time as well to not 0.1% 0.8 microseconds there.

**Dave Jones:** Once again, that's like 800 nanoseconds. We're down in the nanosecond region for a 10 V step. Wow. And over here, the settling time, you know, 0.5 milliseconds. So, 500.

**Dave Jones:** So, wow. The the 189 just blows it out of the park. All right. So, what's actually left? We're getting getting down to the dregs, really. Maximum closed-loop gain, not too concerned about.

**Dave Jones:** Well, if you want to run typically 1,000 here, I don't know if the 189's going to have that. I don't think they have a maximum closed-loop gain there, but we only want a closed-loop gain of 100.

**Dave Jones:** I'm sure it's going to do the 1,000. We've got open-loop gain there, but it won't tell us the maximum closed-loop, and that's fine. Maximum output impedance here, 380 ohms.

**Dave Jones:** Do we care? No, the maximum's not even going to tell us that. Okay, I'm struggling to think of anything else. Input offset, long-term offset drift. Like, we're not really concerned with offset drift.

**Dave Jones:** 50 nanovolts per 1,000 hours. Like, you know, you really have to be squabbling over details there. Yeah, I don't think the TI's going to tell us the drift there.

**Dave Jones:** Oh. No, they specify this as zero drift. It's It's specifically zero drift. So, yeah, I can't see how this 189 is not a winner. Over the MAX4239. There might be a showstopper in there depending on your design.

**Dave Jones:** And once again, we like we could go and quibble over the graphs and things like that. But, I think we've covered almost everything we care about. Offset voltage, supply voltage, gain bandwidth product, supply current, input short circuit current, rail-to-rail stuff, noise, bias and recovery times and slew rates.

**Dave Jones:** And yeah, positive overload recoveries and things like that. And we've got the, you know, there's the step response, and we're down in like nanoseconds, hundreds of nanoseconds per division.

**Dave Jones:** Absolutely brilliant. Uh can drive uh overshoot with uh and versus capacitive loads and things like that. Like, you know, you can go into lots of little intricate details like this, but I uh there's the output impedance uh versus frequency.

**Dave Jones:** That's kind of groovy. But, yeah, really um we've seen more than enough that warrants us to buy some of these chips and try them out and actually do some AB comparisons uh like in terms of uh you know, bandwidth, noise particularly, um offset voltage, and things like that versus the uh MAX42 39.

**Dave Jones:** And here's the internal block diagram here. As I said before, this is like a zero drift or uh chopper amplifier. There are differences between the uh zero drift architecture provides ultra-low offset voltage, near zero input offset voltage over temperature and time.

**Dave Jones:** Uh choice factor chip also offers outstanding IC performance, ultra-low broadband noise. Yeah, really interested to actually compare the two. Zero flicker noise. I've done I think I've never done flicker noise in my noise uh tutorial and I went operating below the chopper frequency.

**Dave Jones:** But, yeah, basically it's got internal clocks, which uh usually they're a divided uh clock, so it's not a one fixed uh frequency, so which can help or it depends.

**Dave Jones:** Sometimes you want to like filter that out. You want it to be exact, so you can notch filter it out or something like that. But, anyway, we don't uh care about that.

**Dave Jones:** ripple reduction feedback loop. Anyway, it's it it's a chopper amp. Uh slew boost circuit. Well, that's how we get our fast bandwidth. Beauty. But, anyway, um I'll link these data sheets down below.

**Dave Jones:** I'm This video is long enough, but you can go in here, and it's got EMI rejection stuff, which is really great, and things like that. And always, don't just look at the tables, of course.

**Dave Jones:** Go in and actually have a thorough read of uh the text in here, cuz they can, you know, alert you to some things that you may not have picked up in the tables and things like that.

**Dave Jones:** So, I won't go through and read stuff like that read all these things. The video's been long Oh, I love the equations. Look at that. Beautiful. There you go.

**Dave Jones:** Low-side current monitor. That's what we're doing. There's our 100 million shunt. We use a 10 million shunt, 10 ohms, and 10k in the case of the current microcurrent design.

**Dave Jones:** Anyway, driver for a 24-bit delta-sigma converter. Stuff like that. The layout tips and things like that. Nice. I'm going to call it. This is a winner winner chicken dinner or at the very least it's absolutely worthy of I'm going to go out and buy some of these chips and we're going to do a direct AB comparisons with the 4239.

**Dave Jones:** So, hopefully we'll have that in an upcoming video. So, there you go. Don't always take these top-level specs or one particular thing like you know three are the Maxim's 0.1 microvolts.

**Dave Jones:** This one's three microvolts. Oh, that's horrible. You know, and so yeah, it's worth digging into the details because check this out. Focus you bastard. So, there you have it.

**Dave Jones:** Switch off the Dave head mode. You can see that the 189 wins in lots of categories and sometimes wins hugely. The only one where the 4239 really one out hugely was the input bias current.

**Dave Jones:** So, 189 very worthy of being considered for a new design. Microcurrent. There you go. But, hey subject to actually getting some chips, soldering them, and doing some real-world measurements especially like noise.

**Dave Jones:** I'm very interested in the noise measurements and stuff like that. Anyway, hope you like that video. I'll link in all those other videos down below measuring noise and stuff like that.

**Dave Jones:** And I hope you found that useful. If you did, please give it a big thumbs up. As always, discuss it down below. So, hopefully this is like part two of a multi-part series.

**Dave Jones:** I don't want to specifically say it's a proper design series, but I'll be doing videos from time to time on this. So, yeah. Catch you next time.
