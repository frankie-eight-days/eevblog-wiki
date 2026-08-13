---
video_id: el6CB-h9Lo0
title: NES on a 64Bit RISC-V Sipeed MAIX
url: https://www.youtube.com/watch?v=el6CB-h9Lo0
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 20, "2": 33, "3": 51, "4": 70, "5": 93, "6": 116, "7": 125, "8": 153, "9": 173, "10": 192, "11": 206, "12": 225, "13": 248, "14": 260, "15": 283, "16": 300, "17": 321, "18": 336, "19": 354, "20": 369, "21": 381, "22": 400, "23": 418, "24": 437, "25": 462, "26": 473, "27": 493, "28": 513, "29": 536}
---

**Dave Jones:** Hey, so here I have the Kendrite K210 development board, and it's basically this board that appeared on Indiegogo a few months ago, and it's a board targeted at AI development. It has some hardware for convolutional neural networks, which are great for image recognition

**Dave Jones:** and things like that, but today I'm not going to be really doing that. I'm just going to do a brief overview of what you can do with it, and with MicroPython. MicroPython is a language written by Damian George. It's basically just like Python, except designed for embedded

**Dave Jones:** systems. So, you know, it's somewhat cut back, but it's pretty damn similar, and someone who, if you are familiar with Python, you'll have no problem with MicroPython. It's based on Python C. So, sorry, C Python, whatever. So, here we have something I've made with

**Dave Jones:** it, and this video basically goes through how I made it, and it also gives, and I'm also going to demonstrate a few things the board comes with, like a Nintendo NES emulator. What? Yes, it has one, for some reason. Okay, so we're just going to look at the MicroPython

**Dave Jones:** kernel here. So, MicroPython is a language created by Damian George, 2014. It's been developed ever since. It's a version of Python which runs on microcontrollers, and in this case it's for the Cypede, MayX 1, and it's basically a pretty cut-down version of Python,

**Dave Jones:** although it does have more features than you'd think. So, you know, of course you've got standard Python things like that. You've got, you know, the syntax of Python is still around, and you can even use things like import os, os.listdir, and we can see what's on our,

**Dave Jones:** on our root directory. So, as you can see, I've got this thing called nova.nes, and that's a NES game. It's an open-source game. It's on GitHub, so all we need to do to run it is go import nes, nes.init0, and as you can see, there's Nova the squirrel.

**Dave Jones:** So, let's start the game. I'm pressing M, and, oh no, story mode. I don't want to do a story mode. And there we go. Okay, so as you can see, it can run things like NES the squirrel, and, you know, that's, that's not, that's not all this device can do.

**Dave Jones:** You can do plenty more than that if I could figure out how to bloody close the program. Okay, so let's just do a really basic program. I'm going to just render the camera to the screen and display the FPS over the top, and this is basically the same as one of the example documents,

**Dave Jones:** and it's really quite simple, and they've provided a fair bit of flexibility for you, although I would prefer their C library, C++ library work, but can't get it to compile. Got really strange errors because I was trying to get Doom to run, but I couldn't get their

**Dave Jones:** library to run, their FreeRTOS, or their standalone library, and that's kind of annoying. So RGB 565 is 5 bits for red, 6 bits for blue, 5 bits for green. Red, green, blue. So that's what the sensor outputs, so that's the format we're using.

**Dave Jones:** This is just setting the frame size. Think means the image size. Now the sensor's powered on, and I'm configuring it for 30 FPS. Let's loop forever. Now, we can get the system tick using clock.tick, and then we just, and we can draw the string on the screen in a similar way to printf.

**Dave Jones:** Now, these are the coordinates, and here we have the string format specifier here, so I want it to be printed with 2.1, floating point, and then after that it's going to say FPS. And then we're literally just going to hook in the FPS value.

**Dave Jones:** And that won't work, because that's not how you do that. And this is the color of the string, and I'm going to make it, I'm going to make super gray. Hopefully that doesn't blend in with everything. Probably will. Don't really know what scale does, I assume it just scales the text.

**Dave Jones:** It's probably the font size, but I don't know what the initial font size is, so that's not really useful, is it? Okay, so lcd.display image. So it does appear that the screen is flipped, so that's a bit annoying. So I've just ended the program, and there's probably some basic

**Dave Jones:** graphics commands. We just want some graphics commands. At the start, we issued this drawstring command, so image drawstring, so I'm guessing in the image library there's some other commands, like draw rectangle. Okay, so after fiddling around for a little while, I got it running

**Dave Jones:** a moving rectangle which changes color. Nice. Bounces off walls and things, and it also renders some text. So I'll show you the code now. This actually has an internal editor, a Python editor, which I believe is actually a Python script itself. So the editor can

**Dave Jones:** be opened just like this, and I'm opening the file called game.py. No, lol.py. That's not a good name. Okay, here it is. So I'll just go through what it does. So the first thing it does is import the image library, then the lcd library, then the time library,

**Dave Jones:** and the clock library, sensor, and the ability to create random values. It initializes the lcd, it initializes an instance of the clock class, and it sets up the camera. Why am I setting up the camera? Well, no reason other than I don't know how to create an image which

**Dave Jones:** is the same size as the screen, because I couldn't find a constructor that had width and height, so whatever. So I took a snapshot, and then I cleared it. That was redundant. And then I get these temporaries, the position in the X, then the Y, the width of the box,

**Dave Jones:** and the velocity of the box. And then I have this variable called redness, which actually is more like intensity of color. And then I create some temporaries which store the width and height of the lcd, and I have some debugging messages which just print what's

**Dave Jones:** going on. In this case it's printing while it's starting. Then the loop logic starts. This logic here handles the box bouncing off walls in the X direction. This logic here handles the box bouncing off walls in the Y direction. This increments the position

**Dave Jones:** of the object with the velocity, really simple. And this draws the rectangle, actually this draws the string bouncy rectangle, with the color defined by redness. It's basically how red the text is. Now that variable name falls apart when I put redness into the green component

**Dave Jones:** of this color. Yeah, I should change the name of that variable. But in this editor it's extremely tedious, so I didn't. So, and then it draws the rectangle at the position Px and Py, with the width Wx and Wy. And there we go, and we increment the redness, wrap it

**Dave Jones:** around the maximum color, and display the image on the screen. That is really all that is needed to do this. So, to run this, it's really simple too, os.listdir, do I have the files? Yes I do, with openlol.py as file. Now all of this is actually done on the micro

**Dave Jones:** itself, so I'm in putty talking over the serial port. So the interpreter here is actually handled by the micro. And there we go, we have a bouncy rectangle with a bouncy rectangle string printed up here, and as you can see it's a very bouncy rectangle.

**Dave Jones:** And the red's going up and down, and the green's going up and down, and it's just like it should be. Yay! And there we go, we've filled up the LCD with a completely pointless green blob. Anyway, so that's just a few things this module can do.

**Dave Jones:** It's really tailored towards machine learning and AI. It's got hardware dedicated to convolutional neural network things, which are great for image classification. So this process is actually pretty impressive. It is a 64-bit processor, which means you don't get such a hit for precision when you're

**Dave Jones:** using higher precision values, that's fantastic. And it's got hardware dedicated to machine vision, so things like convolutional neural networks have lower overhead in this type of device than they would ordinarily, and ordinarily they have a lot of overhead. And those type of things, convolutional neural networks, can be used for things like image

**Dave Jones:** classification, face detection, face tracking, all kinds of things like that. And yeah, it's pretty cool. Today, just for a quick look, I just did some pointless green square moving. Anyway, bye!
