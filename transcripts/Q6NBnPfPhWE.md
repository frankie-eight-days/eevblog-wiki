---
video_id: Q6NBnPfPhWE
title: EEVblog #998 - How To Program ESP8266 WiFi With Arduino
url: https://www.youtube.com/watch?v=Q6NBnPfPhWE
source: youtube-asr
---

**Dave Jones:** Hi. Let's take a look at the ESP8266, a very cool little Wi-Fi module chip that allows you to basically add Wi-Fi into any project you've got for like a couple of bucks. Fantastic. So, let's take a look at it.

**Dave Jones:** Not only can you add it for a couple of bucks, but it also now has Arduino integration, so you can actually program this thing, which is not an Arduino, but you can program it with the Arduino IDE. And it's really incredibly simple to do.

**Dave Jones:** So, let's take a look at it. Cuz there's actually three different things going on here. One is the actual chip, which is under this metal thing here, and that's made by a company called Expressif. And then there are these modules here,

**Dave Jones:** which is the black module with the castellations on there soldered onto a base board, which is the third thing over here. In this case, it's a WeMos D1 Mini. So, there's three different things going on here. So, for the first part of

**Dave Jones:** this is the actual ESP8266 chip itself, and that's made by a company called Expressif. And yes, you can just buy the chip and integrate that into your product. But, you know, a lot of people don't do that because they're

**Dave Jones:** so cheap, as I'll show you in a minute. The module-based things, it's just easier to use the modules. But if you're saving, you know, penny-pinching, saving every cent, integrating a real high-quality product, you could just use the Wi-Fi chip itself, but then you got

**Dave Jones:** to add the external antenna and a couple of external parts. There it says it there, minimum is seven external components. And basically, it uses a 32-bit Tensilica control micro in it. It's a 16-bit RISC processor. It runs a real-time OS. It's

**Dave Jones:** got a Wi-Fi stack and all that stuff to make it work. It's got low-power management, although Wi-Fi is not hugely low-power, so you can't like run it from a coin cell, uh for example, that's why you do like something like that. You you use a

**Dave Jones:** BLE, the low power Bluetooth. And so, it it's basically the chip in there, and we won't take a look at the data sheet and everything else. So, if we have a look at the Wikipedia page for the 8266,

**Dave Jones:** you'll see that it comes uh generally on these little modules like this. And if we have a look at these, these are actually uh manufactured these modules are manufactured by a third-party company called AI-Thinker. And there's generally different ones, and these are uh the

**Dave Jones:** most prevalent ones available. Everyone seems to be using these. What we're going to uh the one we're going to look at today uses the ESP12F uh or 12S, and it's got 4 mega flash memory in there. I think it's 64K of

**Dave Jones:** RAM, and you can run applications on this processor. You don't need any other external micro or anything. So, it's more than just a Wi-Fi interface. You can actually run applications and programs on this chip, on this module. It's fantastic. So, the next level out

**Dave Jones:** from that is people take these companies take these AI-Thinker modules, and then they add them onto more usable uh boards because uh the the castellation ones are great if you want to uh the castellations are the small little uh cutout circular uh half hole

**Dave Jones:** cutouts on the side that allow you to uh surface mount it onto your own board. Great for a high-volume product, not so good for like one-off stuff and things like that. So, third-party companies make these boards uh that, you know,

**Dave Jones:** Adafruit do a Huzzah, and Olimex do one, and there's, you know, a whole bunch of them. The one we're going to look at today is the WeMos D1 Mini. They They sell a couple of different ones, but it

**Dave Jones:** basically takes the ESP12S module uh there, and it puts it on a more usable board with the pins because this chip has the The has uh up to 16 IO pins and it's got UARTs and ADC interfaces and all sorts

**Dave Jones:** of stuff. So, it just basically breaks these out. So, this is a three-level solution that we're playing with here. And this is only like five or six dollars for the WeMos board. I got it for like on eBay for nine bucks

**Dave Jones:** Australian from an Australian supplier delivered. Interestingly, I think my seller actually gave me a dodgy like a fake one because it hasn't got the rounded corners. It hasn't actually got WeMos written on it, although that's what it was advertised as. So, I think I

**Dave Jones:** actually got a fake one. So, oops. Anyway, we're going to use the WeMos D1 Mini in our example today. But just be aware that the ESP8266 could be up to a three-level solution like this. The chip, the module, and

**Dave Jones:** then the board. Choose which one suits your purpose. And these things are insanely cheap. Look at this. AliExpress for like a module-based one that we've got here. 17 bucks for 10. $1.70 each. Or you can just buy like the um

**Dave Jones:** AI Thinker module itself, the ESP12S that we're looking at here or the 12F for $18 for 10. $1.80 each. Just like you can probably even get them cheaper than that. You know, imagine what they you know, get them cheaper in volume. If

**Dave Jones:** you're manufacturing 10,000 items or something, it's just nuts. And the WeMos module we're looking at here comes in the pro version, the mini, and the light. We just happen to have the mini. They've got little display shields and all sorts of you know,

**Dave Jones:** all sorts of variants on this. So, if we go in and have a look at the WeMos D1 Mini, $4 US from WeMos on AliExpress. Um four bucks. Insane. And you've got to remember, this is four bucks for a module. That's not

**Dave Jones:** just a Wi-Fi module, it's a complete processor with ADCs, IO, and everything. You can run applications on this. It's got 4 mega flash memory, like 64K of RAM, or whatever it is. And just amazing. This is a complete

**Dave Jones:** solution for a Wi-Fi product. You just hook sensors up to it, and a battery, and bam, done. So, how do we program this wonderful little widget? I'm glad you asked. Uh Espressif have released various uh SDKs over the years, and

**Dave Jones:** various There's various tool chains, GCC, and all that sort of stuff. And you can get a basic version, and Z basic, and all sorts of stuff. But, by far, I think the it probably the easiest way for any beginner to get involved with

**Dave Jones:** this is to use the Arduino environment. So, you can actually uh get an Arduino plugin for this that allows you to use the Arduino IDE. No, it's not an Arduino compatible board. It doesn't use the Atmel processor. What it

**Dave Jones:** like nothing to do with it. They're just using the Arduino IDE and everything to make it easy. And I'll show you how easy it actually is. So, what you want to do is go to the GitHub repository for the

**Dave Jones:** ESP8266 Arduino uh environment. And uh so, hats off to uh the people who have written personal people who have written this and are involved in this project, cuz it's absolutely uh fantastic. It doesn't have names there, does it? But,

**Dave Jones:** uh yeah, hats off to everyone involved in this, cuz you'll see it's just great. So, what we'll do is we'll simply download this, and we'll download this as a zip. So, we'll just download that zip. It's not particularly big, and

**Dave Jones:** we've got Arduino master zip. There it is. It's downloading. Done. So, what this is going to let us do is run uh Arduino sketches on this actual module. So, your regular Arduino environment that you're used to, uh when

**Dave Jones:** you go in here and go to boards like this, after we install this, we'll see it pop up as a board. So, just like any other board that will work with the Arduino environment. Okay, so what we have to do is go into our Arduino

**Dave Jones:** environment here. I've got the latest one, 1.8.2. I'm not sure which version has previously supported it, but I this one is going to work. So, you notice that we don't have anything in here like this. So, what we need to do is go into

**Dave Jones:** file preferences here, and you'll notice that there's an additional boards manager URL. And we just copy and paste this one from over here. There it is, dot JSON Arduino ESP8266, etc. We cut and paste that one in there.

**Dave Jones:** And if you've already got multiple boards installed, you just separate them with a comma like that. So, we should be ready to additional board manager URL. Done. So, now we simply go into tools and we go into a board manager over here. And

**Dave Jones:** it's downloading, downloading cuz it now has that new address that we've got. And bingo, these are all our additional boards, Arduino SAM, Arduino and NRF52, Intel I586 boards by Intel they've added, added Intel Curie board, all this sort of

**Dave Jones:** stuff. So, all these weird and wonderful boards that Windows 10 IoT Core and all that sort of stuff, a lot of big name companies like Intel and Microsoft and that have gotten onto um this Arduino thing and produce boards that are

**Dave Jones:** compatible with the Arduino environment. And here it is. It's automatically listed this because we've put in that address where it can get the information from. ESP8266 community, we just want to install that. So, click on install. It'll download all of the requisite

**Dave Jones:** stuff. And you can see that this actually includes support for the Adafruit Huzzah and all sorts of boards, NodeMCU and uh the WeMos uh boards. So, there might be other boards out there that are not uh particularly supported by this. They

**Dave Jones:** may still work in some way. I'm not uh entirely sure. I haven't tried them, but this one definitely supports our WeMos uh board or any of the other ones listed here. No worries. Now, we've got an extra 153 meg to download. Ah,

**Dave Jones:** modern software. Anyway, it works. The amount of capability you get, you damn right I'm going to download 150 uh 3 meg. No worries. Now, installed, let's go check it out. So, we close that down, and we go into tools, and we go into

**Dave Jones:** board, and bingo. There we have it. ESP8266 modules, all the uh different uh supported ones, including our WeMos D1 and R1 Mini. Awesome. Too easy. But, there's more. One of the great things about this, not only have we installed

**Dave Jones:** our board in there, so it has all the support for it, but it's also automatically installed all of the examples. So, what do we want? Of course, we want a blinky. There you go. Let's give it a go. And there's our

**Dave Jones:** example code. Too easy. But, of course, this doesn't mean diddly-squat unless we program our board. So, let's plug it in. This is plugging in for the uh first time. And of course, it's got all the uh USB to uh

**Dave Jones:** serial driver on the back, and everything else. And it's installing my device driver. Here we go. Searching, searching USB to serial. It'll eventually pop up. Bingo, we're in like Flynn, ready to use on COM 11. And we'll uh choose our COM port. Here it

**Dave Jones:** is. COM 11. So, we'll choose that, and we're ready to go. Are we? Yep, we don't need to open the serial port. We should just be able to uh compile this and run and upload. So, we've got our board set

**Dave Jones:** to the WeMos D1 mini. Uh we'll just leave everything as uh default uh flash size. This has a 4 meg. I'll just leave it all hunky-dory. Port 11. Let's go. Here we go.

**Dave Jones:** Compiling sketch. Could take a little bit cuz it's got lots of stuff to install. It's got all the Wi-Fi stack and the whole kit and caboodle. So, uh that's to be expected. Archiving built built core sketch uses 22 222 K 21% of

**Dave Jones:** the program space for a LED flasher because it's got all of the Wi-Fi stack. Hey.

**Dave Jones:** Blinky. Blinky. It works. Woohoo! That's how easy it is to program an ESP8266 in Arduino. Piece of cake. And if you just go back and look at the examples here, just look at all these different examples. DNS server stuff, um EEPROM

**Dave Jones:** uh stuff, and we've got the regular blink with what we did, RTC, uh and you can make it into an AVR ISP programmer, so you don't need to buy an AVR ISP programmer, HTTP clients, update updates HTTP update server, MD DNS. I

**Dave Jones:** have no idea what half this stuff is, but it's awesome. Uh your own web servers. There's a hello server. All your Wi-Fi uh stuff, client, multi-scanning. Uh ethernet. Uh advanced chat server, barometric pressure, web server. Like all these example files. This is

**Dave Jones:** absolutely brilliant. Um if you want to do some encryption hash stuff, I guess. Um as I said, the SD card stuff. You want to hook up an SD card to this, piece of cake. Uh Serial, that touchscreen stuff, just

**Dave Jones:** brilliant. Um thank you to everyone who's written all these examples and built this entire core. It just makes it so easy. So, let's demo the Wi-Fi features of this thing, shall we? And by connecting to my YouTube channel to

**Dave Jones:** actually get my subscriber and view count from this thing. So, we can Somebody's written that, of course. You don't have to write it from scratch. So, thank you very much Wit- Witness me now, who's written this Arduino YouTube API.

**Dave Jones:** It's just on the GitHub here, and we should be able to get out our subscriber and view count and stuff like that and connect. It's a good example that it's got to connect to the Wi-Fi, connect through, and so we can just simply

**Dave Jones:** download the zip for that, and we can install that one, too. Fantastic. Let's go. So, what we do is we simply go over to our sketch here, include library, and add a zip raw library. Like I said, you

**Dave Jones:** don't have to unzip these things, which is fantastic. And we select the Arduino YouTube API master. We open that, and that Oh, yep, it's done. Library added. Beauty. So, now if we go back to our examples, we should have right down here

**Dave Jones:** examples from custom libraries. This is great. This is what I love about the Arduino environment now so polished that these things are so trivial to install and get running for, you know, some idiot like me to actually do it. Channel

**Dave Jones:** statistics with Wi-Fi manager. I don't think I need the Wi-Fi manager, but here it is. We've opened it up. Let's shut down the other window there, and that is all the code we need for actually connecting to the

**Dave Jones:** connecting to well, connecting to Wi-Fi, the all the stuff we installed before for the ESP8266 all handles all that. But, this is all we need to connect. So, I need to get my API key, and I need to

**Dave Jones:** get my channel ID. I won't show you those and my Wi-Fi SSID and Wi-Fi password, and it should just connect. Let's try it. All right, so let's give this a whirl. Once First of all, we need to open the serial monitor here. If it ever

**Dave Jones:** pops up, there we go. We've got our serial monitor uh that's COM 11, and it looks like it's 115K board here. So, we need to select that, and we're good to go. Let's actually download this. I've put in all my

**Dave Jones:** credentials up the top with my API key and stuff like that, my YouTube channel ID and Wi-Fi password. So, let's uh Oh. Error compiling. OH, ARDUINO JSON. OOPS. YEP, SORRY. I forgot about that. Uh so, we go to the

**Dave Jones:** uh Arduino JSON GitHub here. Thank you very much, B Blendon. Um so, we'll download that and we'll install that once again just like we did for the uh previous YouTube API. Easy. So, we'll add the zip library again,

**Dave Jones:** JSON master. It is now library added to your libraries, and we should now be able to compile that again. And could take a while once again cuz it's got to compile a huge stack and everything else. But, uh there's not

**Dave Jones:** much code in here. As you can see, like to connect to YouTube and get your stats, it's pretty easy. Someone's done all the hard work for us. Beauty. We're using 27% of our program space, 40% uh 47% of our memory. Um so, it's still all

**Dave Jones:** right. Oops. Mem failed. No, something went wrong. Womp womp womp womp. So, what I did that. We'll try it again. I just went up there and uh simply re-verify compiled. Done compiling. Okay. Okay. So, yeah, I'm not sure. Maybe I

**Dave Jones:** didn't install the uh library give it enough time. I don't know. Something like that. Anyway, let's see if we can uh download, shall we? So, it compiles okay. So, the problem is actually programming the thing. I'm not sure why.

**Dave Jones:** This is looking good. Ta-da! We're in like Flynn. We've got some garbage come up, BUT THOSE DOTS YAY! Wi-Fi connected. There you go. It could take a while to connect to the YouTube uh API, but uh you can see it obviously

**Dave Jones:** connects to the Wi-Fi, which is fantastic. So, the compile worked, all the stack worked, everything else is connected to the internet, and bingo. It just took a bit. I'm not sure why it took uh so long to pop up, but

**Dave Jones:** there it is. Stats, subscriber account. Yep. Fantastic. That's all there is to program with the ESP8266. Even doing something to me that's really complicated cuz I'm not into the web programming, you know, side of things. I can program embedded stuff, all right,

**Dave Jones:** but all this, you know, internet connected and JSON stuff and everything else I I'm clueless about, but hey, people have done all these examples. I can work from the examples and compile these. That's how easy it is. So, I hope you found that

**Dave Jones:** interesting and useful. If you did, please give it a big thumbs up, and as always, discuss it down below. Catch you next time.

**Dave Jones:** Mhm.
