---
video_id: 4yosozyeIP4
title: EEVblog 1491 - The MacGyver Project - Part 1
url: https://www.youtube.com/watch?v=4yosozyeIP4
source: youtube-asr
timestamps: {"0": 0, "1": 24, "2": 36, "3": 50, "4": 66, "5": 81, "6": 92, "7": 105, "8": 115, "9": 127, "10": 141, "11": 150, "12": 161, "13": 172, "14": 186, "15": 195, "16": 210, "17": 222, "18": 238, "19": 247, "20": 259, "21": 275, "22": 287, "23": 305, "24": 319, "25": 332, "26": 347, "27": 368, "28": 379, "29": 400, "30": 415, "31": 427, "32": 444, "33": 457, "34": 464, "35": 476, "36": 494, "37": 507, "38": 520, "39": 536, "40": 546, "41": 558, "42": 570, "43": 581, "44": 590, "45": 604, "46": 615, "47": 629, "48": 647, "49": 659, "50": 671, "51": 680, "52": 700, "53": 711, "54": 725, "55": 736, "56": 760, "57": 773, "58": 786, "59": 801, "60": 812, "61": 823, "62": 837, "63": 853, "64": 863, "65": 880, "66": 895, "67": 905, "68": 930, "69": 947, "70": 955, "71": 966, "72": 980, "73": 996, "74": 1013, "75": 1026, "76": 1038, "77": 1049, "78": 1061, "79": 1070, "80": 1085, "81": 1098, "82": 1109, "83": 1126, "84": 1144, "85": 1152, "86": 1165, "87": 1175, "88": 1185, "89": 1196, "90": 1205, "91": 1219, "92": 1229, "93": 1239, "94": 1250, "95": 1267, "96": 1278, "97": 1293, "98": 1303, "99": 1311, "100": 1321, "101": 1329, "102": 1341, "103": 1355, "104": 1362, "105": 1374, "106": 1390, "107": 1402, "108": 1413, "109": 1425, "110": 1440, "111": 1452, "112": 1461, "113": 1479, "114": 1491, "115": 1499, "116": 1508, "117": 1523, "118": 1537, "119": 1544, "120": 1553, "121": 1560, "122": 1569, "123": 1581, "124": 1591, "125": 1600, "126": 1615, "127": 1624, "128": 1638, "129": 1651, "130": 1658, "131": 1678, "132": 1693}
---

**Dave Jones:** Yeah, the timer is set to tilt the dish with the mercury. 4 and 1/2 minutes. Yeah, we got to get inside and stop that timer. Hi, quite a lot of people wanted me to do a follow-up video to this gas leaky jar detector teardown, which got a lot of views.

**Dave Jones:** And I asked in the comments there if you'd like me to see me actually doing a project, actually getting this display in here, this five-digit seven-segment LED display to light up.

**Dave Jones:** And well, I'm not going to use the magic bomb word because that could get detected by the YouTube algorithm and demonetize me. So, anyway, I'm That's This is what I'm going to do.

**Dave Jones:** We're going to do a project, actually driving this display and seeing if we can have some fun having it like a countdown timer. And there were a lot of really good suggestions in there for all sorts of stuff like, you know, if you try and move it or whatever, movement sensor, it counts down quicker and stuff like that.

**Dave Jones:** And it ticks and does all sorts of weird and wonderful things. So, yeah, we can call it the MacGyver project, I guess at this stage. But if you've got a better name, leave it in the comments down below for this a better name that's not going to get me flagged on the YouTube algorithm.

**Dave Jones:** So, anyway, this is part one where we're going to reverse engineer the board in here and see what the interface is because we might as well reuse the board.

**Dave Jones:** Like, I could design a new board that goes in there, but what's the point? Like, we've already got the board, it's already done and dusted. So, we can just design a board that actually plugs into here, but we need to know what the pinout here is and like how to actually drive this thing.

**Dave Jones:** So, that's the point of this video and it just sits in here. And we've already got like this nice little foam surround here like this. We've got an infrared a and infrared receiver as well.

**Dave Jones:** so we can actually control this remotely. And, of course, there's tons of room in here for like a huge amount, like a big large primary back battery. None of that rechargeable rubbish.

**Dave Jones:** Even though they're LED displays, if you got a large primary battery pack in there, it'll last for like, well, a decade. Well, anyway, we can measure the current. That'll be another video, and you know, just seeing how much power this thing's actually going to take.

**Dave Jones:** But, we got a five-digit seven-segment LED display there. This is part one of video. We're going to look at reverse engineering this. You can see due to the shine on the board.

**Dave Jones:** That means it's conformally coated. Anyway, I'm going to whack this in the do-it-yourself light box, which I'll link in up here and down below. If you haven't seen it, and we'll get some high-res photos of this, and then we'll do some reverse engineering.

**Dave Jones:** Let's go. Okay, so we got the board out here, and as it so happens, this is actually the second time I'm recording this, cuz I recorded a full 50-minute version of this video.

**Dave Jones:** I was going to release it, but I thought maybe it's too long, cuz there's probably two types of people who are watching this video. One is those that want to see like my process actually reverse engineering this, and that's what's in that 50-minute video.

**Dave Jones:** And there's quite a few surprises in here, actually, and I'll talk briefly about them here. But, if you want to fully see the full reverse engineering 50-minute video, I'm going to release that on my EEVblog 2 channel.

**Dave Jones:** So, that'll be linked in down below and up here. Go and check it out. And I'm releasing a ton of content recently on EEVblog 2. So, if you're not subscribed over there, I've already passed 100,000 subscribers, but there's a ton of content over there you're missing out on.

**Dave Jones:** Anyway, here is the board here. There we go. Isn't it cute? And we're going to drive this sucker. So, we need to reverse engineer and get the pin out for this connector up here, which is a 10-pin flat flex jobby.

**Dave Jones:** And as you can see here, each seven-segment display here gets its own driver chip. And these are 74HC164s. These are classic jelly bean serial shift registers. So, these are not latched as we'll go into in a minute.

**Dave Jones:** So, each one of those is dedicated to a seven segment display plus the decimal point. So, where it was we need eight outputs and this is an 8-bit shift register.

**Dave Jones:** So, you feed data in and actually this is the data input pin over here, pin one and two on the chip. And then, you can see that it actually cascades out to the next So, from the previous chip out to here.

**Dave Jones:** So, you have to feed in serially eight bits into here and then shift it, shift it. So, if you want to turn on eight segments over here, you've got to feed in your eight bits into this chip and then clock it all the way through until it gets over to here.

**Dave Jones:** And there's no output latches, so you have to blank the display, which we'll talk about shortly. But anyway, um so, there's not much on here. So, this connector basically has clock and data for uh these five driver chips here.

**Dave Jones:** And uh we've got an infrared uh receiver here and an infrared transmitter LED here. This here is just one of those uh modules, so it's got the modulation circuitry or demodulation circuitry and everything built in and it's just a single data line um out of that thing.

**Dave Jones:** And we've got some uh filtering here. This is filtering for the digital rail. This is filtering for the uh receiver. And this is uh just some decoupling filtering for the uh LED drive cuz they actually have separate supplies and we might go into it.

**Dave Jones:** Then we've got a driver there, which just drives the um infrared uh transmitter LED here. And Bob's your uncle, right? So, it's very simple. Now, and all this shiny stuff here, this is actually conformal coating.

**Dave Jones:** And you'll see in the other video had a bit of problem actually uh probing these. You need really sharp probes to pierce through the conformal coating. Otherwise, you can actually get chemicals to actually um you know, strip it away either selectively or the entire board, but just sharp probes to get through.

**Dave Jones:** So, you can come a cropper there um if you don't really, you know, you could miss probing points when you're reverse engineering something like this. So, a brief look at what we've got here, the 74HC164 classic jelly bean 8-bit serial shift register, and it does not have an output latch like you might get on say the 595 for example, which is much better.

**Dave Jones:** So, as you can see here, we've just got two data inputs here that AND gate just helps it for various circuit configurations, but in this particular case, you saw it there, the two pins were tied together.

**Dave Jones:** And the data just gets shifted through from the D input to the Q output on this flip-floppy here every time your clock pulse goes positive. And you can tell, you don't even have to look up the table above here, which is the state table here, to actually get this because the clock pulse input, there's no knots on there, there's no knot on there.

**Dave Jones:** A knot is a that little circle with an inverter like you can see here on the MR, and the master reset pin here. So, you know if there's no, it's just buffering straight through into the clock, it's positive edge triggered.

**Dave Jones:** So, on the positive edge, the data on the input pins one and two here get shifted to Q0, and then you do another clock pulse, it gets then whatever is on Q0 here gets shifted through to Q1 and so forth.

**Dave Jones:** It just gets shifted through and through until you get to the output. Now, the problem with this, of course, is that when we actually want to drive this thing, when you're shifting data through, if you've got this connected to your LED display and it's on, then you're going to see this data shift through.

**Dave Jones:** Now, of course, you can actually shift it through like really quickly like in a millisecond, and then you could like have it displayed for 999 milliseconds for example, and then shift it through again, you know, however quickly you want to update the data in the display.

**Dave Jones:** Oh, you can only update when it's changing. But yeah, technically, you will actually see that data shifting. So, you want to actually do some sort of a display blanking, usually.

**Dave Jones:** And the seven-segment displays, for those playing along at home, are some old HP jobbies, HDSP-U113. And if we go over to here, we can actually see that Here we go.

**Dave Jones:** Here's the data sheet. These are HP ones, and we've got the U113, which is this one here, like this. They're common cathode, right-hand decimal, black surface, and sure enough, yep, right-hand decimal, black surface.

**Dave Jones:** That's exactly what we've got. Now, of course, the one thing you won't find on this board are any dropper resistors for the LED display. And here is one of the first quirks with this design and interfacing with this, cuz we want to design a board that just, you know, interfaces over here.

**Dave Jones:** But, it's not that simple. There's no LED dropper resistors in here. Look, there's none. So, it's connected directly up to the chip. And spoiler alert, here is the schematic.

**Dave Jones:** Ta-da! Well, you know, it's it's the pinout for this finished board here. So, this is the 10-pin connector here, pin one here, pin 10 over here. And we've got VCC, data, and clock and ground here on two, three, and four.

**Dave Jones:** So, they all go to the VCC goes to the rail of the chip. I don't know whether or not it's 3.3 or 5. We'll talk about that in a minute, cuz it's going to make a difference how we actually power this thing.

**Dave Jones:** So, this isn't a full schematic. What I haven't shown here is that the infrared transmitter has got its own VCC. It's got its own VCC pin, and then that's actually filtered.

**Dave Jones:** That's got one of these filter cap. I think it's that one there, and that 47-ohm resistor there is the filter for the infrared transmitter. And then that we get the data back on pin six here.

**Dave Jones:** So, that's the infrared data coming back in like this. Actually, that should be IRTX on there. So, what happens here? Here's here's my original one which you'll see in the other 50-minute video here.

**Dave Jones:** They've actually this is the driver transistor over here Q1, okay, and they're driving that. I don't know why they have a pull down resistor there. It's kind of redundant.

**Dave Jones:** But yeah, pin one up here is actually supplying the power separate power to the infrared LED up here. So maybe they're actually driving those at their 5-V rails and the digital chip is the VCC.

**Dave Jones:** The VCC here is 3.3. I don't know. I haven't actually measured the main board which we've got here. So anyway, and I also didn't draw the common cathode pin there.

**Dave Jones:** So the common cathode pin, these are all joined together, okay? So all the displays from the common cathode pins, they're all joined together on the five displays and they're going back to pin eight here which is the common cathode LED.

**Dave Jones:** So there's no dropper resistors at all on this board. So So if we supplied our VCC and our ground and we did clock and data, we'll be able to shift data into here and and the displays will light up.

**Dave Jones:** They could be a bit bright or a bit dim depending on how many segments we actually have turned on because in a good design you want you would have an individual LED dropper resistor on here.

**Dave Jones:** And I they've got room on this board. They could have added a LED dropper resistor on there. I don't know why they didn't. They've got SMD here. They could have added like little SMD dropper resistor arrays and stuff.

**Dave Jones:** Like you know, price is no object for this product as you've seen in the teardown. So yeah, so that's really piss-poor design by not adding the LED dropper resistors in there.

**Dave Jones:** And then you could have had one LED dropper in, you know, it's not that uncommon to find just one dropper resistor in series with each display. So you could have had like if you didn't want 40 resistors on there, you could have had just five resistors and just had one series LED dropper on here.

**Dave Jones:** But, the thing is depends on how many segments you turn on here as to how many segments turn on. And if you've got the one dropper resistor, well, the current has to be shared between the different segments.

**Dave Jones:** So, if you turn all eight segments on including the decimal point, then you're going to get 1/8 of effectively 1/8 of the current that you get if you just turn on one segment because like they're all essentially the same voltage drop.

**Dave Jones:** So, the series resistor would be calculated on the voltage drop and the supply voltage and any RDS on on the output MOSFETs inside here. But, so you could do it that way, but they haven't even done that.

**Dave Jones:** They've got no They've just connected all the common cathodes together and taken them back here. And what they've done over here, very briefly, more detail on the other video, is this They've got an NPN NPN transistor here, right, which goes down to ground and then they've just got a series base resistor there and that's on the common cathode pin.

**Dave Jones:** I don't know what that part number is, what that part is. Anyway, it's basically an NPN transistor that goes down to ground with a base resistor on there. And yeah, you could actually bias that so it's like partially on.

**Dave Jones:** So, in theory, you could actually you know, control It's not constant current, okay? It's This is not a constant current circuit, but you could actually control the current. But, as I said, all that current is shared between all five displays on here.

**Dave Jones:** 40 5 * 8 = 40. 40 different LED segments have to be shared through that one transistor there. So, yeah, and this is supposed to be an outdoor readable display as well.

**Dave Jones:** So, you would think that they want, you know, a decently high current. So, I don't know how the heck they're doing it. But, anyway, because this is under software control, you can actually uh pulse width modulate uh this thing.

**Dave Jones:** So, they could be doing some sort of PWM-ing, but you would have to blanket when you actually um shift the data in. The problem with the HC1664 is you can see the Q output here, it just goes to the output buffer.

**Dave Jones:** This is not designed This chip's not designed for um have a cascadeable output, okay? Which some good uh shift registers that are designed to be cascaded They They will actually have and that pin will go out to another pin, so it's buffered.

**Dave Jones:** Um so, it'll go out and you know, cascade to other chips. But, in this case, no, we have to take the output from Q7. So, what we have to do here is the data has to be tapped off here for the next chip and then so on for the next chip.

**Dave Jones:** But, if you're driving current out of this segment here, then you're going to get a voltage drop on there, um which could impact the data that's being read by the next chip.

**Dave Jones:** So, you want to be careful with that. So, what is the output uh resistance output resistance of the uh output high-side MOSFET um inside these things? Well, data sheets like this uh for 74 series logic, they won't give you a 4,000 or whatever it is.

**Dave Jones:** They won't give you an RDS on because that's just not a thing. These are not designed to draw a significant amount of uh current, but you can actually calculate it um using VOH, which is the high-level output voltage here.

**Dave Jones:** And if we go, say take 4.5 V here for example, okay? Why don't they give you five? It's really annoying. Um anyway, if if we got a 4.5 V supply voltage, okay?

**Dave Jones:** The typical output here, we could actually take worst case of 3.98, but let's let's actually take the typical figure of 4.32 V. So, we can actually get our confuser out and we can go 4.5 V, which is the supply voltage, minus 4.32, which is 180 millivolts, 0.18 volts, and then divided by 4 milliamps, which is our output drive, which is specified for, and that's 45 ohms.

**Dave Jones:** So, um yeah, it's 45 ohms effective output uh resistance at 4 milliamps drive like this. But, this can change depending on how many uh outputs are being driven and at what current it's being driven and all sorts of things.

**Dave Jones:** So, you know, as So, as I said, like at at worst case, if you want to take worst case, it's you know, almost for you 4 1/2 volts is dropped, half a volt to 4 volts here.

**Dave Jones:** Um and the thing is, here's another trap for young players, okay? If uh you might look at your data sheet and go, "Oh, look at this continuous output current.

**Dave Jones:** I can drive plus minus 25 milliamps. I can have I can drive these LEDs on here. I can drive 25 milliamps per LED." Whoa, that yeah, we'll really see those in daytime.

**Dave Jones:** Doesn't work like that. Yeah, one single output can supply 25 milliamps. Um but what's the continuous current? Next line here, continuous current through VCC, 50 milliamps. Uh what what what what?

**Dave Jones:** You can only drive two outputs at the full rated IO current there. You can't drive all eight. So, that's really annoying. Okay. So, uh to So, when we drive this thing, okay, we have to um keep in mind how much current we're taking per pin.

**Dave Jones:** And the entire the like the whole chip can only take 50 milliamps. That's its absolute absolute maximum ratings. So, if you exceed those, you can come a gutser. Don't do it.

**Dave Jones:** So, yeah, they're the things that we have to consider now that we've got our pin out and been able to uh drive this thing. We have to decide what we're going to do with the constant current uh LED drive here, um how we're going to actually do that?

**Dave Jones:** As I said, you can't just hook up like a constant current circuit because well, that's fine if you want to draw one LED, but then if you turn all 40 LEDs on, let's say you have a constant current at 20 milliamps, okay?

**Dave Jones:** Not as bright LED, right? No worries. You turn on all 40 of them, that current has to be shared. Kirchhoff's law must be obeyed. Kirchhoff's current law must be obeyed.

**Dave Jones:** I've done a video on that. So, that 20 milliamps gets divided by 40. And suddenly, you've got half a milliamp per segment and and they're just piss weak output.

**Dave Jones:** So, honestly, I don't know how in this actual original Banshee ultrasonic gas leak detector design, how they're actually getting like the all five displays on for like at at an outdoor brightness level.

**Dave Jones:** Like, you know, you'd want to be driving these at like at least 10 milliamps or something per segment. And if they like you just can't even PWM-ing isn't going to save your bacon.

**Dave Jones:** If you've got all those segments on, you could easily exceed the maximum current of your 164 chips. So, yeah, this is this is a really bad design. This is really piss poor.

**Dave Jones:** Like, at the very least, you would have had one dropper resistor per uh you know, segment, right? So, like you'd have five resistors on there. For the sake for the sake of five resistors, I don't know what drove them to I'm here awake.

**Dave Jones:** What drove them to implement it this way? It's it's just nuts. So, we can actually get the specs here for the LED here and you can see it 20 milliamps there, the voltage drop is 1.8 volts and that goes down to 1.6 volts forward voltage drop at lousy 1 milliamp here.

**Dave Jones:** So, if we go over to what we've actually got here, as I said, we've got the five displays like this which go up to the output pins of the 164s, okay?

**Dave Jones:** And they go directly to VCC. So, let's just ignore that, you know, on resistance kind of thing, right? Let Let's just assume that, you know, the nice and crunchy output drive and it's going to give us exactly 5 V or 3.3 V output, right?

**Dave Jones:** And we've got 1.8 V and they have a 20 mA down to 1.8 goes down a little bit with current. And but they've tied all of these pins together like this.

**Dave Jones:** And so, we've only got the one pin output that we can do something with. And you just like And this is what they've got on the board here is just they don't even have this this resistor here, okay?

**Dave Jones:** They've just got this. And of course, I'm you know, if you want to shift the data, this can be used as a blanking. So, you switch the transistor off, pull this low, it's not turned on, and then the displays don't display anything.

**Dave Jones:** So, you've got your blank in there, so you can shift in your data and Bob's your uncle, right? But as I said, you've got 40 segments, eight LEDs in each one times five, 40 of them.

**Dave Jones:** And as you saw in the data sheet, you can only have 25 mA maximum output. So, let's say 20, right? To make the numbers easy. So, you can have your 20 mA here, okay?

**Dave Jones:** You've got because you've got to like worst case, okay? You can't exceed that one pin worst case up here, okay? The one pin can It can drive more, okay?

**Dave Jones:** It's not It's not a hard and fast limit. But look, you know, come on, right? Let's just say it's 20 mA. So, let's just say you're going to the magic smoke's going to be released if you go over 20 mA.

**Dave Jones:** So, you can't have more than 20 mA coming out of one pin. And if you decide that you want to turn all the segments on at once, then that 20 mA has to be shared between 40 pins.

**Dave Jones:** So, they can stand a half a mA. There's no way around it. And then you've got to rely on the matching of the the matching of the voltage drop cuz you've got no current sharing resistors in there, even although you're you're effectively do.

**Dave Jones:** It's called the output on resistance now, you know. So, the output on resistance of the 164's is kind of like an acting like a like a ballast resistor, as it's called, a series ballast resistor, which helps uh share the current.

**Dave Jones:** You know, as a general rule, it's naughty to put just LEDs in parallel because they don't share current evenly. They have to be matched at the semiconductor level, and there can be differences in the doping and all sorts of, you know, semiconductor physics physicsy things.

**Dave Jones:** Um but, if you get them from the same batch, they you reasonably matched and stuff like that. But, yeah, generally, you want a series resistor in there, a ballast resistor, to at least help share the current evenly between the LEDs.

**Dave Jones:** But, yeah, like like there's no way around it. If you want to turn them all on at once, then uh yeah, you're down a half a milliamp per segment.

**Dave Jones:** Um it doesn't matter what you PWM here. You can't just go, "Oh, I'm going to PWM and drive these at, you know, hundreds of milliamps." You know, okay, you want to blow the output of your 164?

**Dave Jones:** Go for it. And even if you do some constant current circuit like this, you know, constant current dummy load, I've done the video on that, it's very popular, everyone's almost certainly seen it.

**Dave Jones:** Even if you do constant current, it makes no difference. I mean, it's it's just there's nothing going on here. Now, it might help, of course, to power the 161's from 3.3 V instead of 5 V cuz they can work HC series can work down to 2 V, so no worries there.

**Dave Jones:** So, what value uh do you have to like a dropper resistor down here for one segment, just one? If you power it from uh 3.3 V here, then you've got the ballast resistor up here, but let's just ignore that.

**Dave Jones:** Let's say you've got 3.3 V supply as a 1. So, 3.3 V supply minus your 1.8 V on your LED. So, what does this resistor here have to be?

**Dave Jones:** Well, let's say you want 20 milliamps uh current flow, then divide uh 20 milliamps and get your confuser out, uh work out that, and that's equal to 75 ohms like that.

**Dave Jones:** So, yeah, you know, so you want a 75 ohm resistor in there to give you that uh nominal 20 milliamps at 3.3 volts ignoring any drop in your 161, but, um, then as I said you start turning on the other segments and the current must be shared, Kirchhoff's current law.

**Dave Jones:** Yeah, so this kind of like really sucks. We're sort of like stuck with a meh um, display. So, I don't know. Like the only other way to do it would be, well, not turn on all 40 segments at once.

**Dave Jones:** They might actually be multiplexing the displays. You could actually multiplex them. You might go, um, well, okay, let's multiplex one display at a time and then you're just constantly shifting stuff all the time.

**Dave Jones:** You blank, shift, blank, shift, blank, shift. And then, uh, you know, and then turn on, you know, you might turn on each one of these for 100 milliseconds or something like that, you know, 200 milliseconds, uh, for example.

**Dave Jones:** You might turn on each one of these digits and then shift in the data real quick. So, I think, um, that's really the only way where the only way forward, really, is to like like multiplex these displays to ensure we don't have all 40 on at once.

**Dave Jones:** And to like if we can limit it to one, uh, like one segment, one display at a time, then we've, uh, reduced our our complexity our, uh, in problems by a factor of five.

**Dave Jones:** So, you know, one one fifth the problem. So, then we could easily, you know, but yeah, if you just have them all at once with 40, you're you're you're screwed.

**Dave Jones:** I mean, there's nothing we can do, really. So, yeah, um, so if we want to use this actual display unless we redesign it or a budget in with proper resistors or whatever, um, then, yeah, I I think we're probably going to have to drive, you know, for one decent brightness out of it, going to have to drive like one entire segment and then multiplex it.

**Dave Jones:** That makes it more complex and interesting, I guess, um, especially if you're doing it with, uh, discrete logic. But, yeah, cool, huh? So, anyway, um, we want to do a project reusing this board.

**Dave Jones:** So, yeah, we we we we have to deal with this thing. So, So, to decide how we're going to do that. Leave it in the comments uh down below how you think we should best approach this.

**Dave Jones:** I know there's people that say just read it re-spin this board. Just re-spin it. What's what's the big deal? I I think it's the principle of the thing um that we want to reuse it.

**Dave Jones:** Anyway, thoughts and comments down below, please. And I want to know uh which direction you want me to take this project. Uh we're just talking about this on the Amp Hour this morning with uh Chris Gamell, and we can go several directions.

**Dave Jones:** In fact, we don't have to pick one. We can do multiple projects. You can have one project over here, which um is all all discrete. We can drive this discretely using discrete 74 series logic.

**Dave Jones:** Or we could uh well, well, that's option one. We can do option two, which is uh use a PLD or an FPGA or something like that to actually drive it.

**Dave Jones:** Once again, you're using discrete gates to actually do that. Um option three is just a micro and throw any Joe Blog's microcontroller. Do you want to see the 3-cent milk?

**Dave Jones:** Do you want to see a bloody um thingamabob? Do you want to see a PIC? Do you want to see an AVR? What do you What do you want to see?

**Dave Jones:** Um and and interesting fourth one, which was brought up on the Amp Hour uh today, was that uh we could do like a that Raspberry Pi microcontroller uh that new jobby.

**Dave Jones:** Not not the Raspberry Pi itself, but the microcontroller version was the RP2040 something. I think And that's actually got um logic output um like a little configurable thing of logic output.

**Dave Jones:** So, maybe this might be an interesting project for something like that. Um so, it's not just entirely software-driven. We're kind of like you were doing a little hardware output thing.

**Dave Jones:** Let me check the data sheet on it. Yeah, here it is here. Um there are two identical PIO blocks. Each PIO block has dedicated connections in the bus fabric.

**Dave Jones:** Um so, yeah. Okay, so we've got like state machine zero. So, they've got little state machines here. Looks like they've got four state machines, and then you can map those over to um GPIO, just your regular IO outputs, you know?

**Dave Jones:** So, maybe, you know, maybe we could do something like that. I don't know. Anyway, leave it in the comments down below how you want me to take this project.

**Dave Jones:** I may, of course, decide to ignore the crowd and just do my own thing, which ever interests me, but please leave it in the comments down below. If you got any Where do you think like if everyone says I should take it in a, you know, yeah, discrete, yeah, 74 series logic, yeah.

**Dave Jones:** Um, and we can just drive it with 74 series logic or yeah, I, you know, and no, no internet of things wankery, please, no freaking Wi-Fi either. No, none of that rubbish, right?

**Dave Jones:** I I just want to drive this thing and maybe have a couple of, you know, interesting things like a tilt thing if it, you know, counts how fast if you tilt it or rock it.

**Dave Jones:** Anyway, leave your ideas down below what I can do with this thing. So, anyway, hope you liked that video. As I said, there's a 50-minute version of this which basically is me going through reverse engineering this and going through a bit more detail in the data sheets and other design aspects and stuff like that cuz this was interesting.

**Dave Jones:** When when I found it like I assumed that this thing was designed a certain way and it and it wasn't. Like I I did not see this coming like that it would have common cathode, you know, all this and then be driven over here and it's just, yeah, very interesting.

**Dave Jones:** Anyway, you like it, give it a big thumbs up. As always, discuss down below. Catch you next time.
