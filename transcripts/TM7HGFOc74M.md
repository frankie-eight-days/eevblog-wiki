---
video_id: TM7HGFOc74M
title: EEVblog #521 - Picoscope 5000 USB Oscilloscope Teardown
url: https://www.youtube.com/watch?v=TM7HGFOc74M
source: youtube-asr
---

**Dave Jones:** Impractical tear down time guys. We got the Pico scope 5000 series and we got Daniel on camera. And yeah, why not? We're here at the Mona stand and we thought we'd rip this sucker apart and have a look.

**Dave Jones:** Should have put my good mic on that camera. So it's probably going to be crap audio. Sorry about that. But uh I couldn't I normally I'd have my Swiss Army knife in my pocket but uh coming on the plane

**Dave Jones:** not allowed to bring it since 9/11. And uh I'm sure Pico won't mind me taking apart this scope.

**Dave Jones:** Actually this screwdriver is having a hard time fitting. And this is a 16-bit converter. Um it's got uh adjustable resolution from 8-bits to 16-bits.

**Dave Jones:** Here we go. And hopefully it should be pretty easy to take apart. No, hang on. Uh it's not a Phillips. It's one of those bloody annoying pozidrive pozidrive screw pozidrive whatever you call it. And just get in there. Got it. Got it.

**Dave Jones:** Got it. We're in. All right. We're in like Flynn. Oh, hang on. This is tricky. Okay, we've got rubber.

**Dave Jones:** All right, now it's coming. It's coming. Ta-da! There we go. John's going to be a bit upset if I break it. Oh, jeez. We've got an audience.

**Dave Jones:** Right, we've got the ass end of the board. We've got the bottom of the board. There we go. They've got uh So, dual side populated. They've got some shielding, surface mount shielding, Pico branded. Look at that. Wow, that's fancy pansy. And uh is that

**Dave Jones:** the main oscillator down there? 10 MHz? That looks like it would be. And uh Yeah. All right. So, obviously we've got our forefront. This is a four-channel, yep, four-channel scope with external trigger. And uh can't see any converter. We've got a BGA

**Dave Jones:** package there. You can see the see the via footprint on the bottom. And uh bit of flux residue on the hand soldering. They haven't cleaned that. So, on the BNC is the hand soldered stuff down there. And uh the DC power jack

**Dave Jones:** on the back. That's uh But, there's no shielding on that. They clearly don't need it. They're uh just happy with the shielding on the front end. I thought this would be quite trivial. I thought the top plastic cover

**Dave Jones:** would just pop off. Maybe it's not possible. Maybe I've got to unscrew the board. But, now we're getting serious. Which means I have to take the front and back panels off. I'm trying not to break the tabs. That's the

**Dave Jones:** That's the thing. I might have it. These things went deep into the plastic. And maybe Yeah, here we go. Here we go. Actually, let me put this back. Like that. And then we'll flip that out and we're in. Tada!

**Dave Jones:** They're kick cans. They've got cans on the front end. Love heart-shaped cans. And love heart-shaped They are. Look at that. Is that deliberate? What have they done that for? So, why have they got And they're Look at those BNCs.

**Dave Jones:** Maybe they knew you'd be opening it. Check out the BNCs. They They haven't seen Look, they're rounded. Look at those. They've got sexy little rounded ends on the back of them. That's unusual. Where do they get those from?

**Dave Jones:** Uh Spartan-6 FPGA. There you go. So, yeah. It's got some DRAM hooked on there. And I don't know, I'd have to get my macro lens out to look at the individual converters. But uh obviously got the trigger stuff around

**Dave Jones:** here. There's a reed relay. Yeah. You know, I'm pretty sure there are some 3D microscopes we There are plenty of 3D microscopes around here. We could take it over to the uh That would be interesting, wouldn't it? Yeah.

**Dave Jones:** We could take it over and uh have a look. How about we do that? We're heading off to find a microscope. I think we should be able to find one in the trade show area. Let's have a look.

**Dave Jones:** So, I could get my macro lens out, but that's not nearly as much fun. So, here we go. Uh found one.

**Dave Jones:** No, I I I really like this one here. All right. All right. This one's sexy. Can we You can You can buy it. Excellent.

**Dave Jones:** This one is great. This one is Check out this This is from a company called Tagarno. Tagarno. And it's a uh 44 uh 40 times zoom. And I've got foot pedal down here, which allows me to zoom in and out

**Dave Jones:** on that. And that's 40 times 40 times zoom. Look at that. Fantastic. And I can tilt this, too. Hang on. It will auto focus and come back. Supposedly. Hang on. I might have to turn the Oh, there we go. It's too much. Oh,

**Dave Jones:** there we go. It's too bright. So, that will There we go. And uh we can have a look at the main chip. So, what we've got Oh, hang on. Here we go. I'll tell you what I think's on here at

**Dave Jones:** first pass. All right. I've got my pointer here. Ha, look at this. This is great. It's a HDMI output by the way. And the working distance, check out the working distance on this. It's That's like 250 mm or

**Dave Jones:** something like that. Crazy. Do you know 250 250, I spot on. There you go. Good guess. All right. So, 250 mm. And uh we've got a Spartan 6 FPGA. Uh we don't have enough light. Maybe we can uh

**Dave Jones:** Oh, there we go. Oh, beautiful. Well done. All right. First time I've used this. All right. So, we've got ourselves a Spartan 6 FPGA with memory next to it. And obviously, this is the ADC because you can see four

**Dave Jones:** It's a four channel unit, so you can see four differential amps, I'm guessing. So, there are four amps, and that's What number is that? Turned around the right way. It's ASD5020. So, there's no manufacturer on that. But uh Well, we can Oh, there we go.

**Dave Jones:** Zoom in. You don't have to zoom in. It's There you go. So, that's the I presume that's the main ADC. So, and I love these foot pedals. You can just operate This is great. So, yeah, I'm assuming four

**Dave Jones:** amps coming out of four uh drivers for the uh ADC drivers. Unfortunately, we can't get out of the cans because they're all uh they're soldered on. But, uh that's beautiful armor. Don't know what it's doing with the uh love

**Dave Jones:** heart-shaped uh cutouts there because there's no adjustment pots underneath those. So, go figure. But, uh for those playing along at home, we have a Spartan 6 XC6S LX25. And there's a squared prom. And what do we got here? Cypress.

**Dave Jones:** CY I'm not sure what that'd be the uh USB driver, I'm assuming. Dead giveaway when the uh traces come out and uh go into your USB there. And that's our power supply from our DC input. I'm loving this microscope. I mean, look

**Dave Jones:** at the zoom we can get on this. This is ridiculous. 250 mm working distance and 40 times zoom. And the depth of field is pretty good, too. So, very impressed with this. More power supply around here. That's all your trigger stuff. They've

**Dave Jones:** got a TX DAC. There we go. So, that's setting your trigger level. Uh or is this uh one of those No, this is a signal gen. This is a This model unit actually has a signal gen. So, we've got an AD

**Dave Jones:** 9744 TX DAC generator. And uh there's our output buffer amp there. LT, what else? Yeah. Nothing doing there. That's your external trigger, so that'll be like a comparator, something like that. More comparators in there. There's probably another DAC.

**Dave Jones:** And uh well, that's it. Nothing else left. Unfortunately, we can't get inside the cans, but uh there you go. That's just an impromptu tear down. Back over here, Daniel. An impromptu tear down of the uh PicoScope 5443B. Beauty.

**Dave Jones:** Catch you next time. And yes, I'm back home from the trade show, and I thought I'd check out this ASD5020 uh ADC that we found in this PicoScope 5000. And this is what I love about tear downs. You get to often find uh

**Dave Jones:** companies and chips you didn't know exist before. And in this case, um check it out. ASD, Arctic Silicon Devices. I can't say I've ever uh heard of them before. And this is a preliminary product specification. I found this data

**Dave Jones:** sheet from uh Mouser. It was the first link actually that uh popped up. So, um but I can't actually find the part on Mouser, but the data sheet is on there, and I can't find any other suppliers. So, I dug a bit uh I also uh Googled

**Dave Jones:** Where is it? Here we go. Um Hittite Microwave Corporation actually back in 2011 So, like a couple of years back actually acquired Arctic Silicon Devices, a high-performance mixed-signal IC company for 12 million bucks in cash and equity. Um

**Dave Jones:** and it provides Hittite new IC design and verification capability, state-of-the-art product line of analog-to-digital converters. There you go. Who knew? They uh successfully designed and launched innovative multi-function low-power ADC products which target high-performance specifications, including ta-da, test and measurement systems and

**Dave Jones:** communications infrastructure. Fantastic. So, there you go. That's what we've got here. We've got ourselves, um, this ISD5020. I'm not sure if you can still buy it. I need to dig a bit deeper, but yeah, sure enough, it's got

**Dave Jones:** this, uh, multi, uh, mode converter. 12-bit mode, uh, 600 single channel mode, dual or quad. Of course, the sample rate seems to, uh, drop. Of course, uh, base basic that's a multiplex, um, analog-to-digital converter. But, 12-bit mode there and

**Dave Jones:** 8-bit mode there. Single channel mode up to, uh, 1,000 megasamples per second in single channel 8-bit mode. So, pretty darn impressive little chip. Only draws, uh, uh, half a watt at 640 megasamples per second. Only? Well, I, you know, that

**Dave Jones:** sounds pretty darn good to me. Um, integrated cross-point switches, instantaneous switching, internal low jitter programmable clock divider. Uh, internal reference circuitry. Course and fine gain control. So, there you go. Digital fine gain adjustment for each ADC. Very nice little chip. Runs off a

**Dave Jones:** 1.8 V supply utilizing time interleave to increase, uh, sampling rate. Integrated cross-point switches, dual channel mode. Woo. Excellent. I like it. Based on proprietary structure and employs internal reference circuitry, serial control, LVDS output data. Blah, blah, blah, blah, blah. Is designed to

**Dave Jones:** interface easily with field programmable FPGAs from several vendors. There you go. I really like it. It precision oscilloscopes. Tada. No kidding. Ultrasound, all sorts of applications like that. So, I'll, uh, include the link, um, down below if you want to, uh,

**Dave Jones:** check out the data sheet in depth. But, uh, you can get a precision mode one, which is, uh, 14-bit up to 105 megasamples per second, the HS type or the PM type. And you'll notice, of course, that, uh, there is no 16-bit

**Dave Jones:** option here. That is because it's actually a 12-bit converter. And to get the higher resolutions, for example, like to get all 14-bit. So, to get the greater resolution, they have to actually multiplex the channels together. So, if you want the full

**Dave Jones:** 16-bit resolution, your four-channel scope becomes a one-channel scope. And if you want 15-bit resolution, you can only use two channels, for example. So, but that is, you know, the flexibility of this thing that allows you to do that. You just tie

**Dave Jones:** the things together with this cross-point mux array on the input. And you're able to do all this, and then the FPGA can handle it and give you the desired resolution result. But even with utilizing that interleave sampling on the input channels, this thing is

**Dave Jones:** still capable of 500 meg samples per second at a full 12-bit. So, still a very impressive scope. If you look at the data sheet for the 5000 series, which is not a new product, by the way, then, you know, it talks about

**Dave Jones:** things like combined with that segmented memory allows you to capture events in rapid sequence. So, full segmented memory capability at the fastest time base, you can use rapid triggering there to collect 10,000 waveforms in under 20 milliseconds. And it's got mask limit

**Dave Jones:** testing as well. I'm not sure if that's done in hardware or that's done in the PicoScope software, by the way. But still, it's quite a versatile and powerful little USB scope. I really like it. And that's one of the advantages of a USB,

**Dave Jones:** generally speaking, a USB scope over a PC scope is that they're generally going to give you, in this case, much greater resolution than you would get on a traditional bench scope. In this case, up to 16 bits. It's got a pretty

**Dave Jones:** impressive amount of buffer memory down here. I mean, you know, we're talking up to 120 up to five some models up to 512 meg samples for 8-bit and 256 meg samples for a greater than 12-bit. So, that's pretty darn impressive. I'm not

**Dave Jones:** sure if you can continuously stream this data at a slower rate over USB. Maybe, maybe not. I haven't looked into the details, but often that's one of the advantages of the USB scope is that you can stream directly to

**Dave Jones:** the PC and essentially have unlimited memory. Noise down here, even though we weren't able to take a look at the front end. 8-bit mode, 120 microvolts RMS. Down at the 16-bit mode, they're claiming 70 microvolts RMS noise level.

**Dave Jones:** And interestingly, if we have a look at the Hittite website, Microwave Corporation, yeah, they've got you know, they've got a ton of stuff. Absolute ton of it. But, down here, well, they have data converters. There we go. ADCs.

**Dave Jones:** And once again, they feature pipeline architecture results from 8 to 14-bit. So, they still sort of carry these converters. But, if you have a look at their offerings down here, the 5020 doesn't seem to be available. I mean,

**Dave Jones:** look, 14-bit quad, it's the 1520 now. Yeah, they've changed the number in system. It's now the HMKAD 1520. So, the chip is still available. And yes, I checked the date code on the video there and you would have already

**Dave Jones:** noticed that if you were paying attention. Yeah, this the scope I actually tore down at the trade show there was actually a 3-year-old demo unit. So, there you go. 2010. That's why it has the old chip. So, presumably, the new one

**Dave Jones:** that PicoScope would sell would use the new uh uh and this particular part number, but uh pretty much it's it looks to be the identical chip. They've just integrated that uh line of chips into the Hittite uh numbering system and stuff like that.

**Dave Jones:** So, there you go. It was Arctic Silicon Devices. No longer. And that's the thing you got to be careful of as a uh designer. When you're designing something like this, if you use, you know, this is quite a novel uh chip. I

**Dave Jones:** really liked it, but, you know, Arctic Silicon Devices, they got bought out for $12 million. They're not exactly a huge player in the ADC uh market. They never were. So, the risk was when uh Hittite bought them out, they might have, you

**Dave Jones:** know, consolidated some of the product ranges and discontinued um the ASD5020. And PicoScope would have been left up the proverbial creek without a paddle. They would have had to uh either discontinue the product or find uh some way or some other

**Dave Jones:** equivalent chip, which I greatly doubt of uh re-engineering. I mean, this product was obviously, with the flexible sampling architecture, was pretty much uh you know, designed and modeled around the availability of this chip from Arctic uh Silicon Devices. I don't think

**Dave Jones:** anyone else probably has anything to uh match it on the market. So, yeah, if Hittite uh decide to just dis- discontinue the chip, PicoScope would have been uh faced with usually a uh last buy uh order. Usually, they don't

**Dave Jones:** just suddenly discontinue the chip. Sorry, they'll put out a notice saying, "Look, we're, you know, here's the last buy coming up. Uh we'll only make the chip for one more uh lot. Give us your maximum number you want to buy, and then

**Dave Jones:** that'll be it." So, uh if they did do that, PicoScope would have had to went, "Well, we're only going to buy a million of these things. I mean, how many of these scopes are we going to uh sell over the next years?"

**Dave Jones:** Or um they would have done that um to a certain number to keep it going for a while. But ultimately, uh they would have had to either discontinue it or really, um seriously re-engineer this thing from scratch, which

**Dave Jones:** really would have been a dog. So, there you go. Um that was rather interesting. I hope you enjoyed that little impromptu uh teardown. Sorry about the uh lack of audio and video quality and uh completeness as would have been in a normal teardown, but that

**Dave Jones:** was an impromptu one. Right at the last minute decided, "Oh, we're here. Why "shoot a teardown?" Yeah. Catch you next time.
