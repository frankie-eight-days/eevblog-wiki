---
video_id: MWn3kaUeqRw
title: EEVblog #967 - Mystery Teardown
url: https://www.youtube.com/watch?v=MWn3kaUeqRw
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 37, "3": 57, "4": 73, "5": 93, "6": 113, "7": 129, "8": 149, "9": 169, "10": 189, "11": 205, "12": 221, "13": 237, "14": 257, "15": 273, "16": 289, "17": 309, "18": 329, "19": 349, "20": 373, "21": 389, "22": 401, "23": 421, "24": 437, "25": 453, "26": 473, "27": 493, "28": 513, "29": 533, "30": 553, "31": 573, "32": 585, "33": 605, "34": 633, "35": 653, "36": 677, "37": 693, "38": 709, "39": 725, "40": 737, "41": 753, "42": 773, "43": 793, "44": 813, "45": 833, "46": 849, "47": 865, "48": 881, "49": 901, "50": 917, "51": 941, "52": 965, "53": 981, "54": 1001, "55": 1017, "56": 1045, "57": 1061, "58": 1077, "59": 1093, "60": 1109, "61": 1129, "62": 1145, "63": 1169, "64": 1189, "65": 1205, "66": 1221, "67": 1245, "68": 1265, "69": 1281, "70": 1297, "71": 1317, "72": 1333, "73": 1354, "74": 1382, "75": 1406, "76": 1426, "77": 1446, "78": 1466, "79": 1478}
---

**Dave Jones:** Hi, welcome to a mystery teardown. What the hell is this thing? It's not an Illudium Q36 space modulator. Let's check it out. Yes, we're going old school, and thanks to Charles at Trio Test, we've got ourselves a Philips PM5639 colour analyser for those

**Dave Jones:** playing along at home. And this is an old school bit of test kit. Comes in the original carry case. Fantastic. And let's take a look at it. What have we got? We've got ourselves the detector, which is designed to plug on the front

**Dave Jones:** of our CRT monitors, and as the name suggests it analyses the colour to see if all the colours are accurate, and the spectrums are right. It's got a nice sexy little control unit that comes with it, and it looks like we've got ourselves the original brochure.

**Dave Jones:** Is it? No, well, it's part of it. There we go. CRT colour analyser. These would have been the ducks guts at TV stations back in the day for calibrating all their studio monitors and stuff like that. Maybe they still use them? You know, some old school places.

**Dave Jones:** Philips used to make a whole range of, you know, various audio and video analysers and all sorts of stuff for, you know, setting up production, measurement, test, all that sort of stuff. The old analog composite waveform monitor. Check it out. Loudspeaker powered audio monitor.

**Dave Jones:** It's pretty fancy. It looks like they've, you know, this is fairly modern stuff in the scheme of things, but yeah, I'm not sure when this colour analyser dates from, but yeah, it's basically no one would use it anymore, but it's probably still worth a pretty penny to someone who, you know,

**Dave Jones:** absolutely still needs it. But there we go. There's our operating manual. Hi to all my Danish viewers. Beauty. Made in Denmark, is it? But all the original manuals. There it is. I mean, that's an old check out the old CRT TV that they're actually

**Dave Jones:** monitor that they're testing there. That is hilarious. Oh my goodness. To our customers, on January 23, 1998, Philips TV test equipment has changed its name to Pro Television Technologies, or PTV. Who knew that? Yeah, I guess they, yeah, looked to sell it off for pennies on the dollar

**Dave Jones:** for what it used to be worth. Good day. Moritz von Toll. Good on ya. There you go. Check it out. Wow. Copyright 2000. It says recent printed in Denmark too. Thank you very much for playing. So this is actually surprisingly recent, although the model

**Dave Jones:** dates back to, you know, god, that's got to date back to the early 80's I would imagine. And maybe early to late 80's. But they were still selling this in 2000. Now, I used to work at Keycorp back in 1994, I think it was, and working on

**Dave Jones:** LCD monitors and things like that. So they're just starting to take over. You know, 640x480 was, you know, 800x600 was absolute state of the art, and it was real difficult. But 2000? I mean, yeah, okay, people still had, I still had a CRT TV

**Dave Jones:** in 2000. I'm pretty sure I did. Geez, I mean, how long did it last after that? Not very long. I wonder if they're still going. Check it out, we even have the calibration data for our CRT color sensor. CRT matrix, what does all this mean?

**Dave Jones:** I have no idea. Protected data, is that the data that's stored in the internal e-squared PROM, I would imagine? It's traceable to NIST. No wuckers. So this is a rather intimidating bit of kit. I mean, look at that. That is fantastic. It's got the suction cup to stick on there.

**Dave Jones:** Some sort of photo sensor in there, which is of course, you know, carefully, I'm sure it's very expensive, and it's quite expensive to get it calibrated as well. But there's not a, probably a huge amount more in there. It was last calibrated in 2002, but you'd stick that up

**Dave Jones:** and stick it on the CRT monitor and get an accurate, to see the spectrum and your color values so that you could get in there with your tongue at the right angle and tweak your RGB values to get your monitor the right color.

**Dave Jones:** I used to work with a guy way back at Pacific Communications back in the day who had calibrated eyesight. I kid you not. The job was to, they would be certified, their eyesight would be certified to actually look at colors on the CRTs and know that they're accurate.

**Dave Jones:** It's got the correct color, the hue, the saturation, and all the brightness or whatever, you know, and they could basically do it by eye. But this is a basically, you know, pretty much replaced people with those calibrated eyesights, I think. And yeah, you know, you have a numeric value that you could

**Dave Jones:** get with this thing. So let's actually try and before we, we'll violate the rule and we'll turn it on before we take it apart. Shall we? It comes with a little plug pack with a weird-ass attachment. It uses a rechargeable NICAD nickel metal hydride battery pack, but let's try and switch it on.

**Dave Jones:** Initializing, and bingo, there you go. There's your RGB values. I've got that sitting up. I'll stick it on the, whoop, there we go. Yeah, I've got it face down now, so it's not receiving any light at all. And we can get our, look, candelas per

**Dave Jones:** square meter. Believe that you can't use this on like a modern LCD panel, it wouldn't work, it hasn't got the right color attributes and everything else. It's designed for CRTs, I believe they did have versions for LCD monitors. They probably still do to test the color, because you know, you get one of those professional

**Dave Jones:** color monitors these days, I'm talking about the multi-thousand dollar professional monitors that are all color balanced, color matched and things like that. Well they've got to test that, and you know, presumably they stick on something similar. So if I point this up to my lights up here,

**Dave Jones:** my studio lights, there are nominal 6000 Kelvin color temperature. RGB's fairly well matched, I mean I could, you know, a spectrometer's much better, I could get my spectrometer and hook it up. I did that in a previous video, didn't I? There we go.

**Dave Jones:** Temperature around about that 6000 Kelvin, so that's, yeah, that's pretty spot on. Ensuring a high standard of picture quality has become even more important with the increasing interchange of program material from different sources such as TV studios and production houses. The Philips color

**Dave Jones:** analyzer assists in this process by meeting the demand for easy control and adjustment of the color white and the brightness on any color monitor. Beauty uses an adaptive system to establish the correct measurement independent of the field rate. The instrument works with four field rates, HD

**Dave Jones:** TV systems, progressive and interlaced systems. Bobby does that. The main application is to align the color of white and brightness color monitors in studios, OB vans, outside broadcast van for those not in the know, post-production, etc. Measuring monitors, surveillance monitors, RGB computer monitors, consumer TVs.

**Dave Jones:** And here's our XYY measuring mode here. This is plotted on a chromaticity diagram, it's a mouthful, and the X and Y values and the luminance value Y and the color error CIE love, hence why it's called CIE, are shown in the numerical display.

**Dave Jones:** User can select a preferred measuring unit of luminance, candelas per square meter, nits, I like the nits, or the foot lambert, oh, all you foot lambert fanboys, come on, admit it, who's a foot lambert fanboy? Now if you're wondering how this works, you can actually set up

**Dave Jones:** this box, you can have pre-programmed different setups, specs that you want, and this box, you actually want your dot to be inside that box, inside the RGB matrix with the luminance and the XY value, so it's got to match your pre-programmed one, so I can stick it up there to the lights, and boom,

**Dave Jones:** bingo, we are inside the box there. Smack bang in the middle, so that's, you know, whatever we've got it programmed up to, yeah, we're certainly meeting it. Inspect, ship it, and here's an interesting characteristic curve, we've got a portion of the CIE 1931 XY chromaticity diagram

**Dave Jones:** showing the daylight locus, the Planckian locus, importantly, with a few iso-temperature lines. Obviously, it makes perfect sense. So the field of colour imaging spectrum and luminance and all sorts of stuff is actually quite complex when you get into the physics of it, and I've done

**Dave Jones:** several videos on that before, touching on that sort of stuff, so yeah, it's a rather interesting field, and of course it all comes down to physics, there's our battery pack. Anyway, yeah, that's enough, I won't pretend I know all about colour television, you know, reference

**Dave Jones:** checking and stuff like that, but let's have a look what's inside this thing. Won't be a huge amount, this will have a micro in it, be interesting to see which one, and this will probably just be a sensor and some driver sensor electronics,

**Dave Jones:** something like that. And you bet we're going to break the warranty void if not removed sticker. Here we go, let's get in there, and will we be in like Flynn? Oh, no we have a spring, OK, we have a spring in there for the trigger.

**Dave Jones:** Ah, that could end badly. Ah, yeah. We're off, yeah. There's a little bit of stuff in there. Oop, yep, the trigger is... yeah, what's going on there? Hmm, yep, broke it. Oh! Brittle plastic, it's old. So let's have a squiz inside here. Of course it's all in the calibration of

**Dave Jones:** this thing. No, that's, that comes off, ooh, actually that's rather interesting. Ta-da! We have three separate ones, RGB, it makes sense, does it not? That you would have separate RGB ones with different filters down there, look at that. Oh, get a close-up on that.

**Dave Jones:** Now I'm going to guess that these photo sensors are all identical and the way that they of course, one's for R, one's for G, and one's for B and the way they do that is to have the filter in there. There you go.

**Dave Jones:** And you can see that they are actually different. They would be the RGB yeah, so that'd be the red, that'd be the green, and that'd be the blue, even though they don't necessarily look 100% like it on here. But yeah, that's how they're doing it.

**Dave Jones:** With these little lenses I won't bother taking, I could, I don't think there's anything else under there really, but hey, why not? And if you're wondering why they're all angled like that, it's obviously so that they focus in one point in the center like that.

**Dave Jones:** I don't know what the actual field spot size would be. Maybe it's in the specs, I don't know. But yeah, it's designed to focus on one little spot there, because there's no point if you're aiming, you know, one here, one here, one here,

**Dave Jones:** that's, you know, too far apart. You've got to aim for the correct space on the CRT itself that you want to measure. So it's a spot measurement thing. There you go, that's a better look at the filter lenses for those playing along at home.

**Dave Jones:** This is what faces the CRT, and they're the red, green, blue lenses, aren't they beautiful? They're probably worth you know, a pretty penny I would say. That'd be a very specialized bit of kit. I wonder what the, like the spectrum bandwidth of those are.

**Dave Jones:** I don't know. Does anyone know? Does anyone want to hazard a guess as to you know, how narrow the filtering is on these things? But anyway, they are. They do look really jazzy. I love that. And on top of that, in case you were wondering, is just

**Dave Jones:** what looks like. I'm sure this is kind of special too. I'm not sure what's going on there. Looks like something's happened to that. Hmm, I don't know. But yeah, that looks kind of sort of special as well. And maybe the front part of that as well.

**Dave Jones:** So yeah, there's lots of spectrum-y magic happening through these three layers here. Well it turns out we don't have to wonder, because I've got a spectrometer! So let's actually use my spectrometer to measure this. We've got our filters here, our red, green, and blue filters.

**Dave Jones:** I've taken the front part of that off, but we can measure that separately. And you've seen this spectrometer before on the blog, and here we go. I've got my little torch here, just to make a broadband sort of source. It's not, you know, this is

**Dave Jones:** not completely scientific. This is not the best thing, but you know, we're getting a reasonable coverage there. It's going up into the red as well. You know, it's peaky, but it'll do the job. So let's actually hook this up. Well actually, I'll show you.

**Dave Jones:** You can see that's red filter. There's the blue filter. Maybe it's not going to show up well on the webcam, but that's blue. And that's green. Fantastic! Alright, so yeah, that actually did show up. So let's actually shine our torch through. Here we go.

**Dave Jones:** What have we got here? Blue. Okay? So if we hook up, you'll notice that we're getting absolutely nothing when I point it away. So I've got the gain set so that there we go. Bingo! That's the bandwidth of our blue filter. Now I'm not sure what I was expecting.

**Dave Jones:** There may be something a little sharper than that. So you know, it's going from 400 to 550 nanometers, or thereabouts. And of course if you put it back through like that, it's more broadband than that. There's still content below 400, but you know, like you've got to

**Dave Jones:** get the gains right and everything else. I'm just mucking around here. So it's not certainly not the best science, scientific experiment, but you'll be able to see the bandwidth. And likewise for the green one. Bingo! There we go. It's chopping out, you know,

**Dave Jones:** from four, well mostly from say 500 to sort of 700, 650, or thereabouts. Certainly in that green spectrum there. And of course we are clipping a little bit of course. It's hard to... there we go. Anyway, you can see. So the green is a bit wider in terms of bandwidth than the blue one.

**Dave Jones:** I'd say. No, maybe not when you include that little aqua hump in there. Aqua hump, word of the day. Let's try the red one. And that, hello, that is surprising. The red one, there's still, well there's yellow content there I guess, but what is the blue doing?

**Dave Jones:** The blue is almost the same, well it's not almost the same, but you know, it's getting up there towards the green peak. So why it's letting through blue in the red filter at like 450 nanometers there, I don't know. That is quite strange.

**Dave Jones:** And then it's, you know, its main peak is about 580 nanometers in the green spectrum. Basically where we you know, not far off where we... yeah, basically the same where we were before. So I'm not sure what the deal is with that red filter.

**Dave Jones:** That is very unusual. If anyone knows what's going on there, I'd have to look into the physics behind that. Think about it a lot more, but anyway, that's interesting. So the bandwidth, now let's take this filter material, and look at that. There we go.

**Dave Jones:** That filter material is taking out all the red. What the? Why? I mean this is a red, green, blue, what? Give me a break. That's just ridiculous. Now that's whoa, there we go. Hang on, so wow, okay. That's the similar sort of response to what we saw with the red.

**Dave Jones:** And with that, and this just... it's giving the same response. What the? Oh no, no, no. Okay, no, no, there we go. That's our white. So that's our spectrum. Maybe, yeah, this lead isn't the best. I think maybe that's what's going on there.

**Dave Jones:** We don't have enough... yeah, because it's auto-gaining, we didn't really have anything in the red to begin with. Like there's some there, but because of the gain and everything else, no, we need a better light source. But why it was passing that blue through

**Dave Jones:** fascinating. So there you go, but they're the filters that we've got inside this thing, and you can really saw, like the blue one for example, and blue and green, very nice bandpass performance on this thing. So there you go, that's the filters. Neat.

**Dave Jones:** Ooh, wonder if you can still get the service manual for it. And for those who just can't get enough of the specs of this sort of thing, the measurement range, there you go, accuracy, and look, there's the repeatability, the luminance, RGB bars, better than 1%.

**Dave Jones:** Ah, terrific stuff. And it even has a learn mode if you don't know what particular phosphor of the monitor that you're actually testing, because that's important. So do that, the filters inside here actually parallel the colour response of the human eye as defined by, say,

**Dave Jones:** 1931 standard observer curves. That's probably what they're attempting to do here, because that's the thing, what do us humans actually see this monitor as? I mean, that's the important thing, you can do all the measurements you want, but you know, if we think it's out,

**Dave Jones:** then it's out. And just to clarify, and just a close-up there for those playing along at home. Psychedelic, man. And we have hot snot, thank you very much. And what have we got over here on the board? That is, we're going to have to get our knife out for that,

**Dave Jones:** aren't we? Have we got a little Philips, probably, you know, like an 8051 or something. Do we have an 8051? Come on, let's cheer, do we have it? 87C51, I called it! What else would you find in this puppy? But apart from that,

**Dave Jones:** and looks like they're a fan of some Maxim parts there. They'd be line drivers of course, dead giveaway right near there. I don't know why they put the vertical resistors in there like that, that's rather hilarious. Ooh, hang on, what's on the bottom

**Dave Jones:** of that resistor? It's weird. It's got a purple thing. What? Wow, they've actually gone to the effort to put a sleeve on the bottom of that. I am doubting that's a resistor now, I think that puppy's an inductor. And of course, you've got to hot snot your sensor in place,

**Dave Jones:** don't you? Can we get a part number? Nice little plastic holder for that, but I don't see a part number on there, do you? No. Bummer. Anyway, if anyone can identify that, quite a large sensor die in there, isn't it? Just got the one bond wire, you can see going over there,

**Dave Jones:** and that is really interesting. Like I said, all of those would be identical, and all the filtering is of course happening on the front. So they would be, you know, wideband, you know, photo sensors of some description, and of course they'd be doing all that filtering

**Dave Jones:** with those front lenses, however wide the bandwidth is for the RG and B. But that's pretty much all she wrote for the sensor board. It's got a fair bit more than I expected in there, so it's obviously digitizing all that. 8051, was there a little ADC on there?

**Dave Jones:** Oh, there might be somewhere a Philips ADC. Come on. Wow, yep, there it is. They've got some serious business happening here. This is a TC500A. That's not the microchip symbol, but I pulled up, when I googled that, pulled up a microchip data sheet.

**Dave Jones:** This is an analog to digital front end. It's an entire front end, up to 17-bit ADC with, you know, pretty much the whole shebang inside that thing. So that's an interesting bit of kit. Date code, 17th week 97. So let's open the main controller here.

**Dave Jones:** Hopefully I've got it all out. We had an 8051 before. Heh, look at the contacts with the battery just soldered directly onto the back there. We've been mooned! We've been mooned, we've got to get it out. So we had a had an 8051 before, but that's all you needed just to

**Dave Jones:** send that, you know, packetize that ADC, control that ADC and stuff, read those values, send it over the serial line. They were getting power over that line of course. So let's oh, got a board-to-board there, yep. Single in-line, I love single in-line board-to-board stuff.

**Dave Jones:** And we're in Like Flynn. Have we there we go. Ta-da! We're in Like Flynn. There's our LCD stuff. Oh, a Toshiba, I was going to say, probably sharp jobby, but it's not. That's a Toshiba, and what have we got down here? Good old-fashioned micro, because we've got ourselves

**Dave Jones:** a ROM, and all the best stuff's made in Japan. What on earth is that? SED 1330. Hmm. Aha, there we have it. Philips PCF80C31. Basically the same as the 8051, except there's no ROM built in. Hence, well, we've got a separate ROM there.

**Dave Jones:** Checksum, 7900. Seems too even to me. Sure enough, that's SED 1330, you googly that one. And it's an LCD graphic controller of course, because you know, this is just for driving the segments. So you've got to have the actual controller itself, so this is

**Dave Jones:** you know, pretty old-school stuff. I'd love to know where this design originated from. You know, it would be maybe early 90s, it could be the late 80s perhaps, but obviously they were making this into the 2000s. And I'd like to know when they discontinued it as well.

**Dave Jones:** So there you have it. That's the Philips PM5639 Color Analyzer. Thanks to Charles for donating this one. It was just going to get cost. It's like so old, you can't find anyone to really who wants this sort of thing anymore. But hey, the

**Dave Jones:** technology would still exist for modern, calibrating modern LCD monitors and stuff like that, I'm sure. But yeah, CRT's gone a little bit the way of the Dodo, but I don't know. If you're still using one of these, or when was the last time you used one of these?

**Dave Jones:** Let us know. Leave it in the comments. Anyway, I hope you found that mystery teardown interesting. I certainly did! Hope you enjoyed it, and if you did, please give it a big thumbs up. Catch you next time.
