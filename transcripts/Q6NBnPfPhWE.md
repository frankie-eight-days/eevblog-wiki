---
video_id: Q6NBnPfPhWE
title: EEVblog #998 - How To Program ESP8266 WiFi With Arduino
url: https://www.youtube.com/watch?v=Q6NBnPfPhWE
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 29, "3": 41, "4": 59, "5": 74, "6": 82, "7": 94, "8": 105, "9": 120, "10": 128, "11": 143, "12": 157, "13": 165, "14": 196, "15": 212, "16": 237, "17": 245, "18": 263, "19": 275, "20": 287, "21": 308, "22": 322, "23": 334, "24": 347, "25": 359, "26": 372, "27": 385, "28": 398, "29": 410, "30": 428, "31": 440, "32": 455, "33": 463, "34": 476, "35": 491, "36": 507, "37": 522, "38": 553, "39": 565, "40": 578, "41": 592, "42": 605, "43": 616, "44": 639, "45": 652, "46": 662, "47": 676, "48": 691, "49": 701, "50": 717, "51": 735, "52": 756, "53": 776, "54": 792, "55": 804, "56": 819, "57": 832, "58": 845, "59": 860, "60": 871, "61": 887, "62": 900, "63": 927, "64": 938, "65": 947, "66": 961, "67": 973, "68": 990, "69": 1010, "70": 1020, "71": 1036, "72": 1054, "73": 1072, "74": 1094, "75": 1105, "76": 1119, "77": 1132, "78": 1143}
---

**Dave Jones:** Hi. Let's take a look at the ESP8266, a very cool little Wi-Fi module chip that allows you to basically add Wi-Fi into any project you've got for like a couple of bucks.

**Dave Jones:** Fantastic. So, let's take a look at it. Not only can you add it for a couple of bucks, but it also now has Arduino integration, so you can actually program this thing, which is not an Arduino, but you can program it with the Arduino IDE.

**Dave Jones:** And it's really incredibly simple to do. So, let's take a look at it. Cuz there's actually three different things going on here. One is the actual chip, which is under this metal thing here, and that's made by a company called Expressif.

**Dave Jones:** And then there are these modules here, which is the black module with the castellations on there soldered onto a base board, which is the third thing over here. In this case, it's a WeMos D1 Mini.

**Dave Jones:** So, there's three different things going on here. So, for the first part of this is the actual ESP8266 chip itself, and that's made by a company called Expressif. And yes, you can just buy the chip and integrate that into your product.

**Dave Jones:** But, you know, a lot of people don't do that because they're so cheap, as I'll show you in a minute. The module-based things, it's just easier to use the modules.

**Dave Jones:** But if you're saving, you know, penny-pinching, saving every cent, integrating a real high-quality product, you could just use the Wi-Fi chip itself, but then you got to add the external antenna and a couple of external parts.

**Dave Jones:** There it says it there, minimum is seven external components. And basically, it uses a 32-bit Tensilica control micro in it. It's a 16-bit RISC processor. It runs a real-time OS.

**Dave Jones:** It's got a Wi-Fi stack and all that stuff to make it work. It's got low-power management, although Wi-Fi is not hugely low-power, so you can't like run it from a coin cell, uh for example, that's why you do like something like that.

**Dave Jones:** You you use a BLE, the low power Bluetooth. And so, it it's basically the chip in there, and we won't take a look at the data sheet and everything else.

**Dave Jones:** So, if we have a look at the Wikipedia page for the 8266, you'll see that it comes uh generally on these little modules like this. And if we have a look at these, these are actually uh manufactured these modules are manufactured by a third-party company called AI-Thinker.

**Dave Jones:** And there's generally different ones, and these are uh the most prevalent ones available. Everyone seems to be using these. What we're going to uh the one we're going to look at today uses the ESP12F uh or 12S, and it's got 4 mega flash memory in there.

**Dave Jones:** I think it's 64K of RAM, and you can run applications on this processor. You don't need any other external micro or anything. So, it's more than just a Wi-Fi interface.

**Dave Jones:** You can actually run applications and programs on this chip, on this module. It's fantastic. So, the next level out from that is people take these companies take these AI-Thinker modules, and then they add them onto more usable uh boards because uh the the castellation ones are great if you want to uh the castellations are the small little uh cutout circular uh half hole cutouts on the side that allow you to uh

**Dave Jones:** surface mount it onto your own board. Great for a high-volume product, not so good for like one-off stuff and things like that. So, third-party companies make these boards uh that, you know, Adafruit do a Huzzah, and Olimex do one, and there's, you know, a whole bunch of them.

**Dave Jones:** The one we're going to look at today is the WeMos D1 Mini. They They sell a couple of different ones, but it basically takes the ESP12S module uh there, and it puts it on a more usable board with the pins because this chip has the The has uh up to 16 IO pins and it's got UARTs and ADC interfaces and all sorts of stuff.

**Dave Jones:** So, it just basically breaks these out. So, this is a three-level solution that we're playing with here. And this is only like five or six dollars for the WeMos board.

**Dave Jones:** I got it for like on eBay for nine bucks Australian from an Australian supplier delivered. Interestingly, I think my seller actually gave me a dodgy like a fake one because it hasn't got the rounded corners.

**Dave Jones:** It hasn't actually got WeMos written on it, although that's what it was advertised as. So, I think I actually got a fake one. So, oops. Anyway, we're going to use the WeMos D1 Mini in our example today.

**Dave Jones:** But just be aware that the ESP8266 could be up to a three-level solution like this. The chip, the module, and then the board. Choose which one suits your purpose.

**Dave Jones:** And these things are insanely cheap. Look at this. AliExpress for like a module-based one that we've got here. 17 bucks for 10. $1.70 each. Or you can just buy like the um AI Thinker module itself, the ESP12S that we're looking at here or the 12F for $18 for 10.

**Dave Jones:** $1.80 each. Just like you can probably even get them cheaper than that. You know, imagine what they you know, get them cheaper in volume. If you're manufacturing 10,000 items or something, it's just nuts.

**Dave Jones:** And the WeMos module we're looking at here comes in the pro version, the mini, and the light. We just happen to have the mini. They've got little display shields and all sorts of you know, all sorts of variants on this.

**Dave Jones:** So, if we go in and have a look at the WeMos D1 Mini, $4 US from WeMos on AliExpress. Um four bucks. Insane. And you've got to remember, this is four bucks for a module.

**Dave Jones:** That's not just a Wi-Fi module, it's a complete processor with ADCs, IO, and everything. You can run applications on this. It's got 4 mega flash memory, like 64K of RAM, or whatever it is.

**Dave Jones:** And just amazing. This is a complete solution for a Wi-Fi product. You just hook sensors up to it, and a battery, and bam, done. So, how do we program this wonderful little widget?

**Dave Jones:** I'm glad you asked. Uh Espressif have released various uh SDKs over the years, and various There's various tool chains, GCC, and all that sort of stuff. And you can get a basic version, and Z basic, and all sorts of stuff.

**Dave Jones:** But, by far, I think the it probably the easiest way for any beginner to get involved with this is to use the Arduino environment. So, you can actually uh get an Arduino plugin for this that allows you to use the Arduino IDE.

**Dave Jones:** No, it's not an Arduino compatible board. It doesn't use the Atmel processor. What it like nothing to do with it. They're just using the Arduino IDE and everything to make it easy.

**Dave Jones:** And I'll show you how easy it actually is. So, what you want to do is go to the GitHub repository for the ESP8266 Arduino uh environment. And uh so, hats off to uh the people who have written personal people who have written this and are involved in this project, cuz it's absolutely uh fantastic.

**Dave Jones:** It doesn't have names there, does it? But, uh yeah, hats off to everyone involved in this, cuz you'll see it's just great. So, what we'll do is we'll simply download this, and we'll download this as a zip.

**Dave Jones:** So, we'll just download that zip. It's not particularly big, and we've got Arduino master zip. There it is. It's downloading. Done. So, what this is going to let us do is run uh Arduino sketches on this actual module.

**Dave Jones:** So, your regular Arduino environment that you're used to, uh when you go in here and go to boards like this, after we install this, we'll see it pop up as a board.

**Dave Jones:** So, just like any other board that will work with the Arduino environment. Okay, so what we have to do is go into our Arduino environment here. I've got the latest one, 1.8.2.

**Dave Jones:** I'm not sure which version has previously supported it, but I this one is going to work. So, you notice that we don't have anything in here like this. So, what we need to do is go into file preferences here, and you'll notice that there's an additional boards manager URL.

**Dave Jones:** And we just copy and paste this one from over here. There it is, dot JSON Arduino ESP8266, etc. We cut and paste that one in there. And if you've already got multiple boards installed, you just separate them with a comma like that.

**Dave Jones:** So, we should be ready to additional board manager URL. Done. So, now we simply go into tools and we go into a board manager over here. And it's downloading, downloading cuz it now has that new address that we've got.

**Dave Jones:** And bingo, these are all our additional boards, Arduino SAM, Arduino and NRF52, Intel I586 boards by Intel they've added, added Intel Curie board, all this sort of stuff. So, all these weird and wonderful boards that Windows 10 IoT Core and all that sort of stuff, a lot of big name companies like Intel and Microsoft and that have gotten onto um this Arduino thing and produce boards that are

**Dave Jones:** compatible with the Arduino environment. And here it is. It's automatically listed this because we've put in that address where it can get the information from. ESP8266 community, we just want to install that.

**Dave Jones:** So, click on install. It'll download all of the requisite stuff. And you can see that this actually includes support for the Adafruit Huzzah and all sorts of boards, NodeMCU and uh the WeMos uh boards.

**Dave Jones:** So, there might be other boards out there that are not uh particularly supported by this. They may still work in some way. I'm not uh entirely sure. I haven't tried them, but this one definitely supports our WeMos uh board or any of the other ones listed here.

**Dave Jones:** No worries. Now, we've got an extra 153 meg to download. Ah, modern software. Anyway, it works. The amount of capability you get, you damn right I'm going to download 150 uh 3 meg.

**Dave Jones:** No worries. Now, installed, let's go check it out. So, we close that down, and we go into tools, and we go into board, and bingo. There we have it.

**Dave Jones:** ESP8266 modules, all the uh different uh supported ones, including our WeMos D1 and R1 Mini. Awesome. Too easy. But, there's more. One of the great things about this, not only have we installed our board in there, so it has all the support for it, but it's also automatically installed all of the examples.

**Dave Jones:** So, what do we want? Of course, we want a blinky. There you go. Let's give it a go. And there's our example code. Too easy. But, of course, this doesn't mean diddly-squat unless we program our board.

**Dave Jones:** So, let's plug it in. This is plugging in for the uh first time. And of course, it's got all the uh USB to uh serial driver on the back, and everything else.

**Dave Jones:** And it's installing my device driver. Here we go. Searching, searching USB to serial. It'll eventually pop up. Bingo, we're in like Flynn, ready to use on COM 11. And we'll uh choose our COM port.

**Dave Jones:** Here it is. COM 11. So, we'll choose that, and we're ready to go. Are we? Yep, we don't need to open the serial port. We should just be able to uh compile this and run and upload.

**Dave Jones:** So, we've got our board set to the WeMos D1 mini. Uh we'll just leave everything as uh default uh flash size. This has a 4 meg. I'll just leave it all hunky-dory.

**Dave Jones:** Port 11. Let's go. Here we go. Compiling sketch. Could take a little bit cuz it's got lots of stuff to install. It's got all the Wi-Fi stack and the whole kit and caboodle.

**Dave Jones:** So, uh that's to be expected. Archiving built built core sketch uses 22 222 K 21% of the program space for a LED flasher because it's got all of the Wi-Fi stack.

**Dave Jones:** Hey. Blinky. Blinky. It works. Woohoo! That's how easy it is to program an ESP8266 in Arduino. Piece of cake. And if you just go back and look at the examples here, just look at all these different examples.

**Dave Jones:** DNS server stuff, um EEPROM uh stuff, and we've got the regular blink with what we did, RTC, uh and you can make it into an AVR ISP programmer, so you don't need to buy an AVR ISP programmer, HTTP clients, update updates HTTP update server, MD DNS.

**Dave Jones:** I have no idea what half this stuff is, but it's awesome. Uh your own web servers. There's a hello server. All your Wi-Fi uh stuff, client, multi-scanning. Uh ethernet.

**Dave Jones:** Uh advanced chat server, barometric pressure, web server. Like all these example files. This is absolutely brilliant. Um if you want to do some encryption hash stuff, I guess. Um as I said, the SD card stuff.

**Dave Jones:** You want to hook up an SD card to this, piece of cake. Uh Serial, that touchscreen stuff, just brilliant. Um thank you to everyone who's written all these examples and built this entire core.

**Dave Jones:** It just makes it so easy. So, let's demo the Wi-Fi features of this thing, shall we? And by connecting to my YouTube channel to actually get my subscriber and view count from this thing.

**Dave Jones:** So, we can Somebody's written that, of course. You don't have to write it from scratch. So, thank you very much Wit- Witness me now, who's written this Arduino YouTube API.

**Dave Jones:** It's just on the GitHub here, and we should be able to get out our subscriber and view count and stuff like that and connect. It's a good example that it's got to connect to the Wi-Fi, connect through, and so we can just simply download the zip for that, and we can install that one, too.

**Dave Jones:** Fantastic. Let's go. So, what we do is we simply go over to our sketch here, include library, and add a zip raw library. Like I said, you don't have to unzip these things, which is fantastic.

**Dave Jones:** And we select the Arduino YouTube API master. We open that, and that Oh, yep, it's done. Library added. Beauty. So, now if we go back to our examples, we should have right down here examples from custom libraries.

**Dave Jones:** This is great. This is what I love about the Arduino environment now so polished that these things are so trivial to install and get running for, you know, some idiot like me to actually do it.

**Dave Jones:** Channel statistics with Wi-Fi manager. I don't think I need the Wi-Fi manager, but here it is. We've opened it up. Let's shut down the other window there, and that is all the code we need for actually connecting to the connecting to well, connecting to Wi-Fi, the all the stuff we installed before for the ESP8266 all handles all that.

**Dave Jones:** But, this is all we need to connect. So, I need to get my API key, and I need to get my channel ID. I won't show you those and my Wi-Fi SSID and Wi-Fi password, and it should just connect.

**Dave Jones:** Let's try it. All right, so let's give this a whirl. Once First of all, we need to open the serial monitor here. If it ever pops up, there we go.

**Dave Jones:** We've got our serial monitor uh that's COM 11, and it looks like it's 115K board here. So, we need to select that, and we're good to go. Let's actually download this.

**Dave Jones:** I've put in all my credentials up the top with my API key and stuff like that, my YouTube channel ID and Wi-Fi password. So, let's uh Oh. Error compiling.

**Dave Jones:** OH, ARDUINO JSON. OOPS. YEP, SORRY. I forgot about that. Uh so, we go to the uh Arduino JSON GitHub here. Thank you very much, B Blendon. Um so, we'll download that and we'll install that once again just like we did for the uh previous YouTube API.

**Dave Jones:** Easy. So, we'll add the zip library again, JSON master. It is now library added to your libraries, and we should now be able to compile that again. And could take a while once again cuz it's got to compile a huge stack and everything else.

**Dave Jones:** But, uh there's not much code in here. As you can see, like to connect to YouTube and get your stats, it's pretty easy. Someone's done all the hard work for us.

**Dave Jones:** Beauty. We're using 27% of our program space, 40% uh 47% of our memory. Um so, it's still all right. Oops. Mem failed. No, something went wrong. Womp womp womp womp.

**Dave Jones:** So, what I did that. We'll try it again. I just went up there and uh simply re-verify compiled. Done compiling. Okay. Okay. So, yeah, I'm not sure. Maybe I didn't install the uh library give it enough time.

**Dave Jones:** I don't know. Something like that. Anyway, let's see if we can uh download, shall we? So, it compiles okay. So, the problem is actually programming the thing. I'm not sure why.

**Dave Jones:** This is looking good. Ta-da! We're in like Flynn. We've got some garbage come up, BUT THOSE DOTS YAY! Wi-Fi connected. There you go. It could take a while to connect to the YouTube uh API, but uh you can see it obviously connects to the Wi-Fi, which is fantastic.

**Dave Jones:** So, the compile worked, all the stack worked, everything else is connected to the internet, and bingo. It just took a bit. I'm not sure why it took uh so long to pop up, but there it is.

**Dave Jones:** Stats, subscriber account. Yep. Fantastic. That's all there is to program with the ESP8266. Even doing something to me that's really complicated cuz I'm not into the web programming, you know, side of things.

**Dave Jones:** I can program embedded stuff, all right, but all this, you know, internet connected and JSON stuff and everything else I I'm clueless about, but hey, people have done all these examples.

**Dave Jones:** I can work from the examples and compile these. That's how easy it is. So, I hope you found that interesting and useful. If you did, please give it a big thumbs up, and as always, discuss it down below.

**Dave Jones:** Catch you next time. Mhm.
