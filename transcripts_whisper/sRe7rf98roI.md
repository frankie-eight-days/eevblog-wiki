---
video_id: sRe7rf98roI
title: EEVblog #15 Part 2 of 2 - Fluke 189/289 multimeter review
url: https://www.youtube.com/watch?v=sRe7rf98roI
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 19, "2": 39, "3": 46, "4": 72, "5": 88, "6": 101, "7": 117, "8": 130, "9": 145, "10": 165, "11": 182, "12": 199, "13": 215, "14": 230, "15": 248, "16": 262, "17": 281, "18": 299, "19": 324, "20": 342, "21": 362, "22": 382, "23": 409, "24": 438, "25": 449, "26": 470, "27": 488}
---

**Dave Jones:** Now, my friend who loaned me the meter also gave me a whole bunch of Fluke probes. And I'm not sure if they actually come standard with it. Maybe they came bundled as a kit or something. But, what I really love are these little babies that came with the meter.

**Dave Jones:** I'm not sure if they actually come with the one you buy, but check them out. These are brilliant. They are tiny. These things are sex on a stick. Really, these are porn for engineers. Unbelievable. They're tiny, okay, little rubber probes. They're rated to 3 amp, 1000 volt, Cat 3.

**Dave Jones:** And they're genuine Fluke. I'm not sure of the model number. But check out the point. I'm not sure if you're actually going to be able to focus on that. But it's a tiny, it's a needle point and it's actually sharp as a needle.

**Dave Jones:** It's brilliant. These tiny little probes, very thin cords on them and, of course, the insulated things. But these are great for probing today's, you know, very dense surface mount circuitry. There's streets ahead of regular probes. And I highly recommend you pick some of these up separately to go with your Fluke.

**Dave Jones:** I'm not sure how much they cost. They probably cost a fortune. But, wow, sex on a stick, really. Now, the main selling feature, of course, with these meters are the data logging capabilities. And, you know, it has, you know, tens of thousands of samples, you know, built in.

**Dave Jones:** And you can actually sample the data in here, out in the field or something. And you can bring it back and you can upload it to the PC later and analyze it. Or you can actually display it on the screen as a graph and analyze the data on the screen.

**Dave Jones:** And that's really cool. It's a great feature. Now, it actually took a fair bit of figuring out how to actually do this. It wasn't obvious at first and I didn't have the manual. But I finally figured it out. Now, I've got it on volts DC.

**Dave Jones:** And let's say we want to log something. You've got your basic menu options here. And what you have to do is you have to press save of all things. You know, go figure. You have to press save to get into the data logging mode, you know.

**Dave Jones:** Anyway, it comes up with multiple options. And one of them is save and one of them is record. Now, you can scroll through with the menus. And you need to go down to record. And you've got to press the record button. And then it comes up with a bunch of options.

**Dave Jones:** You can set the duration in days and hours and minutes. Or you can actually set the sample interval. And I've actually set it up for one second. So it'll sample at one second intervals here. And of course, it's got edit. And if you hit start, it'll actually start.

**Dave Jones:** And yes, it's actually logging at 3, 4, 5. It's actually take and I'm not sure if you can see it. But the power button will actually pulse showing you that you're in data logging mode. And that's really quite cool. Now, you can even let it go all the way through.

**Dave Jones:** And it's showing that it's got 2 hours and 40 minutes of sample time left. So, you know, that's quite a lot. So we'll actually stop it. And then it comes up with either save or trend. So you can save it for future upload to the PC.

**Dave Jones:** But I'll hit the trend button. And if you hit the trend button, bingo. There it is. There's the data which we just captured. And of course, there's a noise there. It's zoomed right in. It's actually auto scaled vertically. And that's plus minus .001 volts.

**Dave Jones:** Plus minus 1 hilly volt. It's, you know, it's really zoomed right in. And then you can use the cursor keys to, you know, scroll through. And you can expand the display. And, you know, you can do all sorts of data analysis thing. Oh, there's a summary button.

**Dave Jones:** Ah, that just gets you back to the normal one. But there it is. It's the, it's really cool. It's on screen data logging capabilities. And it seems to work quite well. I like it. Beauty. Now, unfortunately, because my friend loaned me this and it is freshly cowed,

**Dave Jones:** he didn't want me to take it apart. So, unfortunately, I'm not going to be able to show you inside it. But, you know, you can pretty much be assured it's the excellent Fluke made in USA quality. And it's well designed. And it uses prime spec parts and all the rest of the stuff.

**Dave Jones:** Yada yada. Best in the business, really, construction wise. But I do have the service manual. Now, one of the first things you notice when you look through the schematics for this thing is that it basically doesn't rely on Fluke proprietary chipsets. Well, there is a, you know, there is a Fluke proprietary chip.

**Dave Jones:** At least one in, there's one in here. But it's only got some input switching and some filtering and a comparator and a buffer. And, you know, current source. And it hasn't really got, hasn't really got much else. Now, one of the most interesting things about this meter is that it uses standard off the shelf parts

**Dave Jones:** from Linear Technology and Analog Devices. The main converter is a LTC2415 Delta Sigma converter. And it's designed for, you know, high spec meters. And it's basically standard reference design. And Fluke just copied that. Same with the True RMS converter. It's the LTC1968 device.

**Dave Jones:** And there's a couple of op amps and things in there. But it's actually, overall, the actual designer of this thing is a really nice reference example of how to design a top end multimeter using off the shelf parts. Processors. It's actually got two processors.

**Dave Jones:** One is a MSP430. A TI, you know, the famous very ultra low power TI MSP430 processor. And that's really cool. But that's really kind of surprising why this thing draws so much current. You know, it's only got, you know, 100 hours supply on six AA's.

**Dave Jones:** And it uses the, you know, the famously low power MSP430. So I don't know where all the power's going. Maybe it's driving the display or something like that. But the other processor is a Motorola MC9328 Go figure. And that's got external memory and external flash and things like that.

**Dave Jones:** Presumably the external memory is the storage memory. I'm not entirely sure. But yeah, it's a dual processor thing. It doesn't rely on an actual proprietary processor at all. And it's got a whole bunch of standard DC to DC converters to generate the various power rails and the plus 20 volts for the LCD and stuff like that.

**Dave Jones:** So yeah, it's really quite, you know, pretty much it's a good reference design for a high-end multimeter using off-the-shelf parts. I like it. And there's another interesting aspect to this meter that's different to the 875. This one appears to use input opto. This appears to use optocouplers to actually detect whether or not the probe is plugged into the wrong jack.

**Dave Jones:** So if you're set to volts mode and you try and plug it into the amps jack, it beeps at you. Now on the 875, they actually do that using some sort of, I don't know, plug-in detection. It detects, you know, AC field or something.

**Dave Jones:** I don't know. But this one actually looks like it uses an opto, you know, a led or a phototransistor to actually detect that you physically plugged the probe in, which is quite different to the 875. So my verdict on the Fluke 289 meter, you've probably already guessed.

**Dave Jones:** It's definitely thumbs up. It's worth every cent. But, of course, there are some things I don't like about it. You know, as I've mentioned, for everyday use, it's too big, too heavy, and there's, you know, annoying usability aspects with it for every day-to-day use.

**Dave Jones:** So for just general bench use, I'd much prefer a Fluke 70 or a Fluke 80 series. But, you know, this has some really neat features, and it's super accurate, and it is worth every cent. As usual, Fluke pretty much always gets the thumbs up.
