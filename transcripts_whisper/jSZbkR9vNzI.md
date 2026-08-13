---
video_id: jSZbkR9vNzI
title: EEVblog #163 - Solder Paste Porn
url: https://www.youtube.com/watch?v=jSZbkR9vNzI
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 41, "3": 62, "4": 76, "5": 97, "6": 122, "7": 139, "8": 155, "9": 172, "10": 195, "11": 209, "12": 232, "13": 252, "14": 268, "15": 288, "16": 302, "17": 324, "18": 343, "19": 362, "20": 387, "21": 410, "22": 427, "23": 453, "24": 482, "25": 501, "26": 530, "27": 570, "28": 593, "29": 619, "30": 633}
---

**Dave Jones:** Hi, welcome to the EEVblog. An electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, I thought we'd quickly check out a solder paste dispensing machine. It's an automated dispenser. Don't confuse it with a pick and place machine, which is totally different.

**Dave Jones:** This doesn't place components. All it does is place solder paste, paste, place, solder paste onto a board. Now, if you check it out here, this is the jig. It's a Martin brand. It's made in Germany. And these are the fixed test jigs. But the board can basically be any size which fits in here.

**Dave Jones:** And you'll see that these little clamps are just magnetic clamps like that, that you can actually set your board onto in any position, any position you like, really, on this panel. And then it's got control software over here, and you set up the reference points based on the fiducials on the board,

**Dave Jones:** which that's why you put fiducials on there, not only for the pick and place, but if you've got a machine like this which automatically dispenses the paste, then you've got to have those fiducial marks, so you set usually two opposite corners like that,

**Dave Jones:** and then it knows where the reference is, and it knows you import the paste file, and it knows where to dispense the paste. Now here, we've got a standard, and that's actually a camera. It's a USB interface camera, so it treats it as a USB camera device, and that's what it uses to find the fiducials and actually visually align stuff.

**Dave Jones:** And then we've got the paste tube here, which has different size attachment nozzles for it, and there's an air hose system which, over here, which is used to actually dispense it, and it comes with, over here, a companion, what is this? Maybe it's a, it's like a compressor kind of thing, or a compressor, a pressure regulator controller,

**Dave Jones:** and because this is only a temporary setup, we don't have a factory air system, we're actually using just an air compressor here, running off the main. So it gets quite noisy when it's actually running, but this is what you need. You need a compressed air source to actually control this thing.

**Dave Jones:** Now, it's actually, if you look at the mechanicals, Oh, there it goes. See, it's pretty noisy. But if you look at the mechanicals here, it really is quite simple. It's just an XY, XY dispenser, and the paste can actually move up and down as well,

**Dave Jones:** but it just, basically just an XY plotter table with a paste dispenser. Pretty darn simple, but this, if you have to ask the price, you probably can't afford it. And if we just take a close-up look at the machine here, you can see the nice,

**Dave Jones:** there's the stepper motor for that direction there, and around here is one of these flexible cable guides that travels with this arm up here, and there's the other stepper motor up there, and it's pretty simple. There's a valve regulator there for the pressure, it's got a control board up the top there,

**Dave Jones:** but as you can see, there's not really much to it. There's another stepper motor down there, and there's not much to it at all. The only thing that comes out is the paste itself. You just lift that out, it's got a little O-ring, and there's the air hose.

**Dave Jones:** You want to do that for me? Can we take that out? Awesome, there we go, and there's our little paste tube, and you've got different size attachment nozzles. They come in little jars here like this, but... See that one? Yep. That's the type 6, which is the finest one you can get.

**Dave Jones:** Oh, that's the finest paste. OK, so they come in different grades of solder paste. Yeah, on the bottom you can see the size of the paste. 5 to 15 microns. Awesome. They're the little individual solder balls, I guess, of 5 to 15 microns each.

**Dave Jones:** Fantastic. But apart from that, it's a pretty simple device, really. Your board can be placed on there, it's got a couple of these fixed locations, but if you wanted to, I guess you could drill custom jigs in there, and stuff like that. But these little magnetic board holders are really quite neat.

**Dave Jones:** And, pretty simplistic machine, but it works, and it's very high precision, very well engineered. And, of course, it's important to store the paste in a fridge. So, we've got a companion fridge to it as well, and these are the individual paste tubes, which then you attach, and you have to clean the nozzles as well.

**Dave Jones:** But these must stay in the fridge, they must be kept at a constant temperature, otherwise they will go off. And I think they probably have to stand on their end too, I'm not too sure. But, yeah, that's an important part of any pick-and-place machine,

**Dave Jones:** or any reflow solder process. And it actually comes with CAM software, as well as the solder paste control software and alignment software. And this is where, it's like a Gerber CAM actual software, and that loads your board in like that. That loads in your Gerber paste file,

**Dave Jones:** which your PCB package will actually output that, and you load it into this. And you can either do individual boards like we did here, or you can do the entire panel. But it's pretty flexible software, but that's what you get when you, flexible and powerful software,

**Dave Jones:** you get when you buy these really high-priced paste dispensing machines, or a pick-and-place machine. And of course the application, it can read in the paste file directly from Altium Designer, or any other program, but you need to convert it into its own format up there,

**Dave Jones:** its own file format. It's a .Liner data file, and that actually converts it into its own format, so it can control the machine. So even though this machine is pretty simple, it is quite expensive and high-end, because the resolution is very large. They claim it can actually go down to 0105 components,

**Dave Jones:** not just 0402, which is what we're using on our board, they're the size of the 0402s, it can do 0105 or 0201s, and that's the resolution that it's actually capable of doing. So even though it's incredibly simple, but there's also a problem when the components are too close on the board,

**Dave Jones:** if they're actually spaced too close together, even though it's capable of that sort of resolution, you will have problems on your board, and, well, you might have to clean it and start again, or it may just not be possible to actually solder paste dispense that board at all,

**Dave Jones:** and you may have to use a traditional solder paste stencil approach to doing the paste. But there's an automated paste dispensing machine for you. OK, that's the camera on the screen. That's the camera looking down at the board, down there. This little, there's a little USB camera on the side.

**Dave Jones:** It's just a USB device, and there's the paste dispenser, and we're just aligning it up, ready to dispense the paste. If you use the mouse controller, click on that, you can see the step size has been changed. Got it. You can move to...

**Dave Jones:** All right, so we've chosen that pad down there. Normally we'd choose a fiducial mark on the board, but we've just decided to use a pad for the purposes of today's experiment, and we'll select that as the reference point, and let's go. And we're going to select the second reference point up there,

**Dave Jones:** which is LED number two. Do it. OK. Set our reference points. There we go, it's just doing a test, and it's dispensing the paste onto the board. It's hard to see, sorry, I can't focus in any better than that with this camera, but trust me, it is putting the paste onto each individual pad,

**Dave Jones:** and then you can place components and put them in the reflow oven. Neat. There we go, now we're doing the BGA. That's the fun part. There we go, you can clearly see the paste being dispensed. It's pretty noisy when the compressor's running. There you go, you can clearly see the paste being dispensed onto each BGA pad.

**Dave Jones:** Isn't that neat? I love it. And correspondingly, you can see on the screen here, the ones that have already been done are in purple, and it's in process until it completes the board. I like it, it's really neat. And you can see the paste, which is only, we stopped it halfway through,

**Dave Jones:** and you can see the paste is dispensed onto those pads there, on the BGA pads and the individual ones as well, but they're a bit harder to see. They're 0402 components on that board, so pretty darn small. And there you go, we've got our board with our solder paste dispensed onto the individual pads.

**Dave Jones:** Now, all we need to do now is take this to our pick-and-place machine. You've got to do that pretty quick, probably under an hour, otherwise the paste just dries up or does whatever, and it's no good anymore. So you've got to rush this over to the pick-and-place machine,

**Dave Jones:** which is already pre-loaded, pre-programmed, and you just need to set the reference, Interesting. See ya.
