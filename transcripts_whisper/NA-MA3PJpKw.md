---
video_id: NA-MA3PJpKw
title: EEVblog #184 - Open Hardware Multimeter Concept
url: https://www.youtube.com/watch?v=NA-MA3PJpKw
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 19, "2": 36, "3": 53, "4": 71, "5": 83, "6": 101, "7": 125, "8": 143, "9": 162, "10": 180, "11": 192, "12": 215, "13": 236, "14": 255, "15": 275, "16": 289, "17": 309, "18": 326, "19": 350, "20": 368, "21": 388, "22": 401, "23": 421, "24": 441, "25": 457, "26": 478, "27": 493, "28": 511, "29": 539, "30": 563, "31": 580, "32": 597, "33": 611, "34": 623, "35": 644, "36": 656, "37": 673, "38": 697, "39": 714, "40": 726, "41": 749, "42": 769, "43": 784, "44": 802, "45": 819, "46": 835, "47": 846, "48": 867, "49": 883, "50": 900, "51": 912, "52": 939, "53": 958, "54": 974, "55": 986, "56": 1004, "57": 1021, "58": 1039}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it's a bit of a random one today and it comes from the EEVblog forum. I saw a post a couple of hours ago from a viewer by the name of

**Dave Jones:** house91320 and he posted some photos of an open source hardware project he's working on. Cool, I love open source hardware projects, but what piqued my interest was that it was an open source hardware multimeter. And, you know, I love multimeters. I love talking about multimeters,

**Dave Jones:** I love talking about multimeter design, so I couldn't help but be interested and come up with a few ideas of my own. So, I thought we'd take a look at it. I've done some quick doodles in DaveCAD here. Let's check it out. Now, here's some photos of house's open source hardware multimeter mockup.

**Dave Jones:** It's just a, you know, a first pass mockup and it's not bad at all, but I saw it and I went, well, you know, it's just a multimeter. It's a regular looking multimeter, it's got a graphic display though, it's got a range switch, and it's got volts, ohms, and amps, jacks, and well,

**Dave Jones:** that's pretty much it. It's got USB interface to a PC, okay, but yeah, it's just a multimeter. I got to thinking, well, you know, there's just so many multimeters on the market that just have all those features, so why really do an open source hardware one?

**Dave Jones:** So, I thought, well, it's got to have something novel. It's got to have something interesting that other, nothing else on the market has. It's got to have that compelling feature or a combination of compelling features to make it worthwhile. So, I spent five minutes, did some doodles, came up with some ideas.

**Dave Jones:** So, I started off thinking about multimeters, and well, quick thought, what do they all have in common? Well, it's pretty obvious. They all are basically a single measurement type device. They've got a common jack, they've got a volts, ohms, amps, well, volts and ohms jack, and they've got an amps jack,

**Dave Jones:** and well, really, there's very few on the market that actually do more than that, and I figured, if you're going to actually design your own multimeter, why not make it do more than the standard multimeter? Add some novel capability to it, and one of my favorite multimeters is the

**Dave Jones:** Metrihit Energy, and it measures volts and amps. It's still only got the three input jacks here, but it measures volts and amps at the same time, and it's got a triple display, and it displays power, among other things. It's got data logging and stuff like that, and there are another novel

**Dave Jones:** multimeter on the market is the Fluke 233, which has the removable display on it, so it got me starting to think, well, maybe if you could do more than just measure power like this, and more than just having a removable display or something like that, sure, there's a lot, you know, there's

**Dave Jones:** multimeters out there, they've got graphic screens, data logging, USB interface, all sorts of stuff, but they all pretty much come down to they're basically a single input function. They can't log or measure more than one thing at a time, so that's where I started from.

**Dave Jones:** As you may know, I've mentioned on here before that any good lab should have more than one multimeter. In fact, I've shown a case or two where you really need four multimeters for measuring the input power of a product and the output power at the same time, so that got me thinking, well, what if you could

**Dave Jones:** replace that with one multimeter? That'd be awesome. So let's take a quick look at my DaveCAD drawing, see what I've come up with. So I present to you Dave's kinda novel multimeter concept. This is what I came up with very quickly. I don't know, I haven't slept on it, but I just thought I'd come

**Dave Jones:** up with something different. What have we got here? Well, you'll notice one of the main things is we've got multiple input jacks here. In fact, we've got four separate channels, all with their own separate grounds. So it's basically a totally isolated, by the way, so it's a four-channel

**Dave Jones:** isolated multimeter. Now, when I first came up with the idea, I thought, oh, wouldn't it be great to have ground volts and amps and then have three or four channels of those? And then I thought, well, you know, it's a bit overkill, so I sort of limited myself a little bit just to two voltage

**Dave Jones:** channels and two amps channels. Now, one of the input channels has all your standard functions. Most of the time you might use this as a single channel multimeter. You plug your leads in here and you can do your volts, ohms, caps, diode, continuity, whatever you want.

**Dave Jones:** That works like a regular multimeter, but at the same time you have the capability to have a second voltage channel here at the same time and a first and a second amps channel. So you can combine, just like on the Gossen energy multimeter, you can combine volts and amps.

**Dave Jones:** That's why I've labeled them channel one here. You don't have to worry too much about the semantics of how all this works, you know, it varies. It's just a concept. But you can take, say, if you're talking power, you can take channel one, volts times amps, and it can display power.

**Dave Jones:** Likewise on the second channel, volts and amps displays power. And I've got a secondary function here which is an output, which I originally was going to have this as another separate output, but I decided that it was a bit too many connectors already, so I thought, well, I'll just integrate it into

**Dave Jones:** the existing amps jack. Now the beauty of this is that it's not common ground. It is tight, they are all totally electrically isolated channels. And I don't think there's probably any general purpose multimeter on the market that actually has that. And I've shown this in one of

**Dave Jones:** my videos where, because the Gossen-Metrihit energy actually shares a ground terminal, I really wasn't able to take really precise measurements of some battery consumption and things like that. I'll have to link the video in there to show you what the actual issue was,

**Dave Jones:** but you can get around that by having two totally isolated channels like this. And what have we got on the rest of it? Well, let's take a look at the overall concept. I've got these nice little wanky hand sort of grips in here, I kind of like that sort of concept.

**Dave Jones:** Please excuse the crudity of the model, I didn't have time to build it to scale or to paint it, to quote Back to the Future, but my CAD drawings kind of suck. But hopefully you can get the concept. Now I'm a big fan

**Dave Jones:** of big seven-segment displays. I think any multimeter's got to have big seven-segment displays. Now House's design just had the one big graphic display, and it was color, and it was backlit TFT. Ugh! Chew power like there's no tomorrow! No! No! Please give me,

**Dave Jones:** on my multimeter, I want big seven-segment displays. Now the Gossen-Metrihit energy, for example, has three displays so that you can display voltage and current and power at the same time. But I thought, well yeah, that'd be nice if I could have triple or even quadruple display,

**Dave Jones:** I thought about, so you can display the actual parameter from each channel. But it gets messy when you start talking about the design of this LCD. If you've got three or four displays on there, all with 50,000 counter, all five-digit displays like this, it really gets quite complicated when

**Dave Jones:** you can get down to the design details of it. So I decided to have two big five-digit displays, and a separate, just as a bonus, a separate, say for example, 256 by 64 mono graphic LCD display. And that can be used for, say, soft buttons.

**Dave Jones:** You could have four or five soft buttons under there. You could have a menu-based system. You know I hate menus on multimeters, but when it has this much functionality, you really can't get away with it, frankly. So you've got to have some sort of menu capability.

**Dave Jones:** And the graphic display can display not only menus, but it could display data login and simple graphs and things like that, login stuff. And of course, it's got an SD card down here. Now, what multimeter on the market's got an SD card? Now, the reason I chose the SD card over a USB interface, in my mind, the SD card actually

**Dave Jones:** negates the need for a USB input terminal, because USB input requires isolation. It's a real pain in the butt. And well, I just like the idea of being able to log standalone to an SD card. And you can upgrade firmware by there, and you can do all sorts of stuff when you integrate an SD card into a

**Dave Jones:** login multimeter like this. You can log voltage current across all four channels, power, all sorts of things, and log it to the internal memory, and then dump it to the SD card if you want to save power and stuff like that. There's all sorts of smaller details like that when you actually get

**Dave Jones:** down to it. But I reckon you can do away with USB, save yourself a lot of design effort and hassle by trying to isolate the USB input, and use an SD card. Now, you'll notice I haven't put a RAIN switch on here. I haven't really decided the concept for that, whether or not you actually need

**Dave Jones:** a a traditional rotary switch on a design like this. Maybe not. I'm not hard set on that. So it could be like a, you know, there could be like, I don't know, 10 buttons, big, large, easy to press, soft buttons, things like that.

**Dave Jones:** So maybe you can go for a full button interface. I don't know. I haven't sorted out the user interface details to be determined, absolutely. And let's take a look at some of my notes up here. As we've mentioned, we've got four isolated channels.

**Dave Jones:** Two voltage, two current, just for the sake of simplicity. I don't think you need probably any more than that. It's just nice to have two voltage channels and two current channels, I think. Maybe you could argue that the current one should be dual purpose voltage inputs as well,

**Dave Jones:** so you could have a four channel voltage data logger. I haven't gotten that far into it. Anyway, now the output jack down here, this one I talked about, it could actually be separate. It could actually go on the side here. It could even go on the top of the multimeter up here.

**Dave Jones:** Now, what I want to use that for is, I've talked about this before, is I want a programmable constant current feature. So you can test LEDs at a specified current. Or you can have like a function gen. A lot of multimeters have got a function generator output.

**Dave Jones:** You can define the frequency, whatever. It could even have not just a digital signal output, but actually a proper function generator with a sine triangle as well, possibly. And I think what would be real handy is a little power supply output. You could adjust from say zero to, I don't know,

**Dave Jones:** six volts or something like that, and you could power your project. Sure, you're going to suck your batteries dry if it takes a fair amount of current, but there's so many projects these days that require small amounts of power. And why not have your multimeter supply that power once again

**Dave Jones:** isolated to your project? I think that would be terrific. Now, we talked about the SD card negating the need for the isolated USB there and logging, so I don't need to talk about that anymore. Now, here's where I got to thinking about the Fluke 233 with the removable display.

**Dave Jones:** I originally had a first rough sketch of this. It would actually have three removable displays that you could actually take out, because I had three channels at the time, and then I thought about four. It's just, I don't know, it's all very mechanically hard to actually integrate a

**Dave Jones:** removable display into this. So just build. I mean, you don't need to have a removable display on a multimeter. It's handy. You just have, but you can just have a separate one and wireless. So you integrate Bluetooth, Zigbee, whatever, for a second display, or it could be for a PC or iPhone interface

**Dave Jones:** or something like that. And then, if people want to, if they need that capability, they can just buy a second display that all it does is contain the actual display which links to the meter and and, you know, it's got a magnet on the back, its own battery power, all that sort of thing.

**Dave Jones:** Just like the Fluke 233, except it's not removable, which then lowers your system complexity designing this multimeter. It's just another thing to goof up, quite frankly. Now, I've got two five-digit displays here. We talked about that, and I haven't really worked out details of

**Dave Jones:** how you would actually display. One might display volts and amps, how the combinations work with power and then voltage. It'd be nice if we had the triple display like on the Gossen, but I don't know. I think I'd probably limit it to two, just the sheer complexity of it, really.

**Dave Jones:** Now, I talked about the graphic display before. Now, a key to it is it's got to be a low power. Now, you can get these tiny displays that only take a milliamp or two, so they don't take a huge amount. And really, you could even have a feature that disabled that if you weren't actually using

**Dave Jones:** it. So you can get away, you know, forget color, forget backlighting and all that. You can have backlighting but only switch it on when you need to. None of this color TFT rubbish. Just get a nice reflective monochrome display. Thank you very much.

**Dave Jones:** Super low power. And of course, the meter should do LCR type and ESR functionality was mentioned on the forum as well for houses design. I think ESR would be a nice feature as well. LCR, I don't know. How complicated is it? Well, you know,

**Dave Jones:** the whole thing's complicated. So, well, you may as well add those sort of features. As we've talked about, power display, power factor, and all the other stuff which goes along with it, like on the Gossen energy. And I kind of like the idea of possibly having a voice output so that it could

**Dave Jones:** speak the voltage or something like that. Or maybe even just say, high voltage warning, Will Robinson, something like that. You could possibly have, instead of actually having the samples actually stuck in the memory in there and the processor needs lots of grunt to do it, just use one of

**Dave Jones:** those voice recorder chips maybe. You could have a microphone in there perhaps and you could record your own, you know, overload or continuity or, you know, under 10 ohms or something like that. Warning, high voltage or nothing connected or something like that. I don't know.

**Dave Jones:** Voice output might be novel, might be a wank, who knows. And what I've added up here is an often lacked function on multimeters is a good temperature capability. You know, I guess all good multimeters these days will have temperature capability, but they're all single channel and often, so often,

**Dave Jones:** I've needed to measure multiple channels. So I reckon have two separate multiple temperature inputs. Use the blade type thermocouple, standard thermocouple inputs at the top, two or even three perhaps, depending on your requirements and space at the top and things like that. And then you can

**Dave Jones:** log not only, so it effectively turns your multimeter into a six channel thing. You can still do your two volts and your two amps channels, but you can measure two temperatures at the same time. Imagine the logging capabilities. That'd be awesome. You just plug the thermocouple straight

**Dave Jones:** in. That's better than wasting your inputs here with those thermocouple adapters on the input. Why not just whack them straight on the case up the top? Not a problem. And of course, I'm a huge fan of big battery life on multimeters, so really double A's are the go.

**Dave Jones:** If you start talking bigger than that, you start talking C or D size, and they're really quite, you know, they're huge beasts. I don't know how you'd get away with that, but just four double A's would be nice. I'd shoot 500 hours plus.

**Dave Jones:** 300 hours is typically taken as a decent amount of battery life for a meter. Once again, those sort of hours would only be for like a standard, you know, just your standard multimeter functions. Data logging is going to take more and other functions are going to take

**Dave Jones:** more of course, and there's the power supply and current outputs that are built in and things like that. But anyway, there's my basic concept for a novel multimeter. I might wake up tomorrow and decide this is complete and utter crap, but anyway, let me know what you think, and let me know what

**Dave Jones:** you'd like to see in your own multimeters. Come up with your own sketches, video response if you want. Thanks. See ya.
