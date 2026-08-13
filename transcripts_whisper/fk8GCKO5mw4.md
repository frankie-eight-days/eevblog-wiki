---
video_id: fk8GCKO5mw4
title: EEVblog #130 - The µCalc Credit Card Scientific Calculator / Computer
url: https://www.youtube.com/watch?v=fk8GCKO5mw4
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 18, "2": 30, "3": 56, "4": 73, "5": 88, "6": 104, "7": 126, "8": 140, "9": 160, "10": 179, "11": 203, "12": 220, "13": 238, "14": 255, "15": 271, "16": 291, "17": 302, "18": 322, "19": 338, "20": 368, "21": 391, "22": 414, "23": 434, "24": 447, "25": 469, "26": 490, "27": 508, "28": 521, "29": 547, "30": 567, "31": 589, "32": 598, "33": 618, "34": 638, "35": 658, "36": 679, "37": 699, "38": 713, "39": 728, "40": 741, "41": 762, "42": 774, "43": 798, "44": 818, "45": 836, "46": 851, "47": 867, "48": 885, "49": 897, "50": 916, "51": 936, "52": 953, "53": 970, "54": 978, "55": 988, "56": 1010, "57": 1021, "58": 1040, "59": 1059, "60": 1073, "61": 1093, "62": 1112, "63": 1129, "64": 1146, "65": 1160, "66": 1170, "67": 1184, "68": 1204, "69": 1220, "70": 1237}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, this one comes from somebody in the forum who asked about my micro calc project, and I've touched on this before in

**Dave Jones:** one of the live shows. I think I explained a little bit about it, but I thought it probably deserves its own little short blog describing what the micro calc is, the project, and some of the design aspects that went into it, because it's rather interesting.

**Dave Jones:** So, let's go. And here's the micro calc project. This is what it looks like. Well, it's not finished, but we'll go into that. What it is, is it's basically the world's first and only credit card size programmable scientific calculator. It's got a dot matrix display on it, 128 by 32

**Dave Jones:** display. It's got touch-sensitive keypad, as you can see, with all the scientific legends directly on them, but it is fully programmable. It's got function keys up the top, and I called it the micro calc because I've already done the micro watch, which you've seen in another blog.

**Dave Jones:** So, it's basically a credit card thin scientific programmable scientific calculator. Why? Well, why not? I always wanted ... I used to use one of those credit card scientific calculators. You could just whack in your pocket, really small, and ... but you couldn't really get ...

**Dave Jones:** they came in solar power a lot of the time, but you couldn't really get a scientific version of them. There was one. Casio did make one back in the very early 80s, but it was pretty thick. I think it was about five, six millimeters, or something like that.

**Dave Jones:** So, I figured that I could design my own using off-the-shelf parts, and this is the result, the micro calc. Spec-wise, it's based on a microchip, a 24F series 16-bit microcontroller. It's got 256k of flash, 16k of SRAM, and, you know, it's quite a powerful little 16-bit micro.

**Dave Jones:** It's the same one as used in my micro watch project, but it's just got basically increased SRAM and increased flash memory as well. Now, a lot of thought went into what microcontroller to use for this. Should I use Atmel? Should I use microchip and ...

**Dave Jones:** or something else? A TI MSP? Because it's got to be low power. Everyone thinks, oh, use the TI MSP. Well, no. These microchip nanowatt XLP micros are pretty darn low power, so this was one of the most low power micros I can get.

**Dave Jones:** I considered the microchip 32-bit series as well, I considered all sorts of things, but lots of reasoning went back into choosing the microchip 16-bit part again. The other big decision which went into the microcontroller was pretty critical, because I couldn't put buttons on this thing.

**Dave Jones:** They're actually touch-sensitive, capacitive-sense buttons, which I'll also go into. Now, this microchip PIC chip actually had enough ... it's got the built-in capacitive sensing technology, so I didn't need an external chip. I was going to use one of the Atmel touch-sensitive chips to actually do that, but they were actually

**Dave Jones:** quite expensive, increases your parts count, yada, yada, yada. So to get it built into my microcontroller, that was awesome. So the number of keys on here were limited by size, finger size, and stuff like that, but also by the number of channels, capacitive-sense channels, available

**Dave Jones:** on the microchip part. But it had more than enough power to run, say, chess on here, which is a big thing for the microwatch. Some of the guys out there, the users, actually wrote a chess program. It's the world's only chess-playing watch. So I thought, OK, we can play chess on this one too.

**Dave Jones:** So that was the microcontroller choice. It's a little bit arbitrary, a little bit of thought went into it, but plenty of power, once again, to take into account not only the dot matrix LCD display on it, but the microSD card as well. One of the other major design aspects of this

**Dave Jones:** product was, how do you power it? Now, I originally wanted to solar power it, but I've already done a blog on that, on this particular design, and why that's not actually possible. So I won't go into it again. So I decided to use the standard lithium coin cell batteries, because I wanted them to be

**Dave Jones:** replaceable. I didn't want rechargeable. I hate rechargeable. They're a pain in the ass. You can get some really thin lithium-ion batteries these days, some, you know, under one millimeter thick, absolutely incredible. But yeah, I just, I just like the thought of using these disposable batteries,

**Dave Jones:** and I went through the battery life calculations, and these seem quite reasonable. Now, the good thing about button cells, OK, if you haven't actually seen them before, I'll go through it, OK? This is a CR2032. It's a standard battery, and you've probably seen them before, OK?

**Dave Jones:** You've heard about them before. Like a CR2032 is probably the world's most popular battery. But in case you didn't know, there's actually a reasoning behind these numbers. What the first two, so you can get all these different types, there's like, oh, there's about 20 of them or something, I think.

**Dave Jones:** There's heaps. So they come in all these different sizes and styles, and what the numbers mean are the first, the CR is just basically coin cell. That's just, I don't know where that comes from, actually. But the first two numbers mean something, and the last two numbers mean something.

**Dave Jones:** In this case, the first two numbers are the diameter of the battery in millimetres. So 16 is 16 millimetres diameter. So a CR2032 is 20 millimetres in diameter. Easy. And the second number is actually the thickness of the coin cell, like that, in, in, well, you've got to put a decimal point in there, directly in

**Dave Jones:** millimetres. So a CR1616 battery is 16 millimetres in diameter and 1.6 millimetres in thickness. It's great, and it's a standard. And you can choose all these different types of batteries. Now, if you give this a moment's thought, you'll notice, aha! 1.6 millimetres is the thickness of a standard

**Dave Jones:** FR4 PCB. That's important. You can also get 2 millimetre PCBs. You can get 3.2 millimetre PCBs as well, and you can probably get 2.5. I've never had to get one. But you can get those as well. Different thicknesses of actual FR4 material. Now, the reason that is important is because when

**Dave Jones:** you're designing something really thin, ultra-thin like this, you want to make it as thin as possible, obviously. Now, as it turns out, the maximum thickness component on my entire design, after a lot of searching and stuff like that, is the LCD. Now the LCD, and I'll go into this a bit more

**Dave Jones:** detail later, but the LCD is basically 2 millimetres thick. So what I can do, so that, okay, my entire design can't be less than 2 millimetres. It's got to be more, because it needs a top front panel and a back panel as well.

**Dave Jones:** But if you use a CR1620 battery, i.e. it's 2 millimetres thick, it can slide on there like that, and be wedged, sandwiched between the top layer and the bottom layer like that. I don't actually have the top board, because the project's not actually finished, but as you can

**Dave Jones:** see, whoop, nah, it's gone. There we go. All right, here it is. Here's the battery. The ultimate goal is you glue, you sandwich the two together, and you can slide in your coin cell like that. The coin cell will just slide in there and be held in place by the thickness of the board and just friction.

**Dave Jones:** And because the contact is, you can see I've actually got a large size contact like that, I'd have a matching one on the base board as well, but that means it can just slide in there and make good contact, and I've got two batteries just wide in parallel, so that you can actually replace one and

**Dave Jones:** not lose your contents, or if there's any flexing of the thing or something like that, you put it in your shirt pocket, your back pocket, and it flexes, then you've got two battery contacts to make, so that one just won't accidentally disconnect. So there you go.

**Dave Jones:** You can actually sandwich things. You don't need to buy a coin cell holder. You can just slide it right in. It's brilliant. Now here's the actual front panel PCB. It's got integrated into it the touch switches. I'll show that later on a 3D thing on the PC, and it's got the cutout for the LCD like that, and the LCD just solders

**Dave Jones:** directly into the back, and all the parts mount on there. No problems at all. Now, this board is actually 0.8 millimeters thick. Now, I could have made it, um, I could have made it 0.5 millimeters, which is probably about as small as you can get boards made without going ultra, ultra exotic, i.e.

**Dave Jones:** from, you know, you can get 0.5 millimeter boards cheap from PCB cart in, um, in China, and that's what I used for my, uh, the front panel on my MicroWatch project. I used a 0.5 millimeter front panel PCB. Now, I'm a big fan of using, I've mentioned this before, PCBs for front panels, because

**Dave Jones:** not only are they, you can get them machined easily, because they're just a PCB, you can get them from the manufacturer, but you can get them silk screened, you can get nice different colors, all sorts of things. So I integrated these really nice, um, touch switches into my PCB.

**Dave Jones:** So the front panel is not only the front panel with the buttons etched into it, and the nice silk screen on top, and you can put a logo there, and you can cut out windows and do all sorts of things, but it's the

**Dave Jones:** actual PCB on the bottom as well. Now, this entire design will need three PCBs. This one, which basically is the entire calculator, which mounts everything like that. Everything's mounted on there, and there will also be another back panel of the same thickness, or I could go for 0.5 millimeters

**Dave Jones:** if I wanted to really get the thickness down. So we're talking, uh, basically a maximum thickness of, um, 3.6 millimeters for the entire design, because I said the LCD in there's two millimeters. I'd use a CR1620 battery to slide in, so it's two millimeters plus 0.8 on the bottom,

**Dave Jones:** plus 0.8, uh, on the top, and that's, uh, 3.6 millimeters. In theory, I could probably get it down to three millimeters. Unbelievable, right? But, um, and if I found that all the solder joints might be a bit variable on the LCD, then choose a thicker, slightly thicker battery, the CR1625,

**Dave Jones:** or something like that. You've got 2.5 millimeters. Anyway, you need three boards. You need the base one, you need the back plate, which will just be a flat back plate. It'll also have the contact on it for the back, uh, battery, and the final board will be an inner board, which sits in the middle, basically.

**Dave Jones:** You just route everything out, and that acts as sort of like the central core, and you route out around all the components. As you can see, there's probably not going to be much room, but there'll be a big section here, just a little bit, so it'll be, like, completely routed out around all my

**Dave Jones:** components. So you do that last, after you've perfected your design, and, um, and, you know, it's, it's ready to go. Then you would design your inner PCB core, and then you just glue them all together. You use super glue, you use whatever, stick them all together, sandwich them,

**Dave Jones:** and you leave a couple of little slots on the outside to slide your batteries in, a slot on the side for your micro SD card to come in and out, and bingo! You've got a beautiful product without using a case at all. It just uses the FR4 PCBs as the case.

**Dave Jones:** I love it! Here's a really good close-up of the, of the main, uh, PCB, and as you can see, it's got the, uh, LCD mounting points here and here. These are actually mechanical ones. These are all the electrical mounting points, the micro SD card.

**Dave Jones:** This down here, in this actual connector interface down here, is the ICSP, the in-circuit serial programming, uh, system, and it's got, it's got a reset button up there, but as you can see, these are the two, uh, contacts for the two batteries which wedge between it.

**Dave Jones:** Now, as you can see, the LCD is mounted basically, um, sort of, you know, on the back. The, the pins are bent back. I'll actually show you this LCD when you get it. This is how you buy it. It's a standard DIP, uh, version LCD, so it's

**Dave Jones:** designed to just plug directly into a PCB, but there's nothing stopping you from bending those pins back on themselves and cutting them flush so that it, you utilize the full, uh, two millimeter, you utilize the two millimeter thickness of that LCD. So you might be able to get away with two

**Dave Jones:** millimeters if you trim each pin individually, um, or you might have to go to 2.5, as I mentioned, but you just bend the pins back and use the display, uh, inverse like that, pretty much. So instead of just, um, sticking it in DIP-wise, because then it's all exposed and it's just, uh, it's awful,

**Dave Jones:** you stick it in and you just bend the pins back like that. Real easy. This, um, LCD 128x32, it's actually a, get this, it's a Dog M, uh, graphic series from Electronic Assembly. There you go, that's the, uh, model number if you want to look it up and have a play with it.

**Dave Jones:** It's not a bad LCD at all. It's reasonably priced, um, and it's only two millimeters thick. I love it! And in case you're wondering what all these wires here are, I've mentioned this before, it was actually a silicon bug inside the PIC, uh, processor for the ICSP port.

**Dave Jones:** Didn't work. The bastards! Unbelievable. Um, but yeah, it's got a nice little, uh, reset switch, and if you're wondering what the hole up here is, uh, when I, when I was, uh, designing this, everyone, somebody said, oh, it'd be nice if it had, like, a hole to stick it onto a

**Dave Jones:** keyring or something like that. So, yep, not a problem. Just stick the hole in for the keyring. And you can actually see the tracks in here under the black solder mask. See? You can actually, you can actually see the pattern under there, and I think that really looks quite funky.

**Dave Jones:** You have to sort of get it in a certain light. If you get it in a different light, it just looks all black and everything, but I think it's, it's a really neat sort of high-tech look for that, and this is just a, um, this connector here is just temporary for, um, in-circuit, uh, testing and in-circuit

**Dave Jones:** prototyping and, and debugging as well. But there you go. That's the microCAP. It's not finished yet because, um, I never got around to actually doing the, uh, backplate and the inner core board as well, um, but it's a really neat little project, and it just goes to demonstrate how you can, uh, using a

**Dave Jones:** few novel techniques and a bit of thought, actually design something this small. Um, a lot of the major manufacturers would be struggling to actually, like a Casio or someone, would struggle to get something this thin in a, uh, credit card style thing. I can do it using off-the-shelf parts, easy.

**Dave Jones:** All it needs is a bit of thought, and if you adapt an LCD like that, bend its pins back, or you could even use, uh, Zebra connectors. You can get ones without the connector, those Zebra strips to join boards top and bottom. Um, and in case you're wondering how you get the power off the top board

**Dave Jones:** onto the bottom board, because you've only got the negative down here, the positive would be on the top board, for example. It would sort of, you know, it would sit like that. So you've got to get power from this board down to this board.

**Dave Jones:** There's two ways to do that. I chose the simple solution, which is just to put a pad there which wires up to the top board. So you just have a loose wire, and you wire it on, and then when you squeeze it together, the wire gets squeezed, and not a problem.

**Dave Jones:** But if you really wanted to be, uh, smart about it, but it's a bit risky, you could actually put, uh, vias all the way along the, say, the edge of the board, or somewhere in the board, top and bottom, and then, um, actually join them together, but then you've got to rely on the, just the physical

**Dave Jones:** pressed contact between the different boards. So that's not really a good approach. So the best approach, I think, the most reliable, is just a wire, top to bottom, and sandwich it like that. And here we are inside the PCB editor for the actual board, which I've just shown you.

**Dave Jones:** And it's actually a two-layer board. That's all I needed. Uh, two layers, top, bottom, and as I said, it's either 0.8 or 0.5 millimeters, uh, thick, depending on, uh, the ultimate thickness, and the rigidity, and the strength I need in the final design.

**Dave Jones:** And let's take a look at the individual layers. This is the, uh, silkscreen, and as you can see, this just has the logo, and all the buttons, and all the buttons you want. The, uh, silkscreen overlay, uh, goes, as you can see, it actually overlays the buttons on the red

**Dave Jones:** layer there. Um, and the red layer actually shows, here it is here, the red layer is the individual buttons. Now, these are capacitive, uh, touch buttons. They rely on the capacitor, or the, they rely on the finger, um, when you overlay the button.

**Dave Jones:** The finger will actually change the capacitance between the pads, and that can be detected by the microcontroller. Now, there's a whole art in designing these buttons, and there's, uh, a whole bunch of app notes on how to get it right. As you can see, there's ground in between the individual buttons, and there's a bit of, um,

**Dave Jones:** a bit of trial and error involved in actually determining what size pads to use for different finger widths, and button, uh, spacings, and things like that. So, you often won't get these capacitive buttons right the first time. So, one of the, uh, rules is the, uh, signal tracers, uh,

**Dave Jones:** need to avoid, uh, grounds and other, uh, objects, which is why you wouldn't flood fill these boards with the ground on the bottom. Here's the bottom layer here, and as you can see, I didn't, uh, flood fill anything, and you try to, um, keep the, the signal tracers away from other digital

**Dave Jones:** signal tracers, because that will detract from the, uh, sensitivity of the button. And, uh, and the microcontroller, also, you need algorithms to detect, um, to actually discriminate between individual buttons as well, so that, uh, you know, if you put your finger halfway between

**Dave Jones:** a button, for example, then, well, which button does it choose? So, there's a bit of, um, trial and error involved in that. Let's take a look at the 3D thing. As you can see, there's the cutout, uh, in here as well, and I've got the nice rounded edges and the logo up there,

**Dave Jones:** but this is what it looks like in the final design, and as you can see, it looks exactly what we got manufactured. Go figure! And this is the bottom, this is the base of it here, as you can see, and it all looks quite well.

**Dave Jones:** It shows the cutout. I love these 3D, uh, view modes, because it can actually show you exactly what you're going to get, and you can actually see the, um, the traces under there as well. You can change the transparency and all sorts of stuff

**Dave Jones:** in 3D mode. It's got the hole up there, but it really looks exactly like the finished product. So, that's the MicroCalc, the world's first and only credit card-sized scientific programmable calculator slash computer with dot matrix LCD. It's streets ahead of anything that's ever been

**Dave Jones:** developed or put on the market before, and it was real simple. It just had to be to put, uh, it just uses a few novel concepts, capacitive touch sensors, um, touch sense switching, uh, novel construction with the sandwich using the front panels as the PCBs and the back panels

**Dave Jones:** and the inner core. Just doing a few things like that, uh, you can come up with a, you know, a pretty good-looking, awesome-looking product like this incredibly simply, and I'm a big fan of using PCBs for front panels like this. A lot of my projects do it, and I highly recommend

**Dave Jones:** you give it some thought next time. See ya!
