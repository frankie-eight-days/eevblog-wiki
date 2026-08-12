---
video_id: yabl87SD-3M
title: Guest Video: Brian Lough - ESP8266 Libraries
url: https://www.youtube.com/watch?v=yabl87SD-3M
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 18, "2": 35, "3": 50, "4": 70, "5": 86, "6": 98, "7": 115, "8": 134, "9": 159, "10": 176, "11": 198, "12": 217, "13": 233, "14": 250, "15": 264, "16": 281, "17": 296, "18": 312, "19": 322, "20": 338, "21": 356, "22": 374, "23": 394, "24": 413, "25": 434, "26": 444, "27": 462, "28": 486, "29": 504, "30": 515, "31": 531, "32": 555, "33": 583, "34": 594, "35": 616, "36": 632, "37": 649, "38": 663, "39": 684, "40": 698, "41": 716, "42": 733, "43": 750, "44": 768, "45": 785, "46": 805, "47": 822, "48": 841, "49": 860, "50": 870, "51": 885, "52": 903}
---

**Dave Jones:** Hi, my name is Brian Locke and on my channel I do videos on Arduinos. I mainly use the ESP8266 microcontroller, which is the same one that Dave used in his NixieTube YouTube subscriber counter. If you're unfamiliar with the chip, it's a $3 microcontroller that can be programmed

**Dave Jones:** using Arduino. The best thing about it is though, that for $3 you get a chip with built-in Wi-Fi. In Dave's video, he mentioned that there's a lot of different libraries and software available for the ESP8266. For example, he used the YouTube API library, which is actually one I wrote.

**Dave Jones:** I thought it'd be interesting in this video to go through some of the different libraries that are available for the ESP8266. The first library we're going to look at is one called Wi-Fi Manager. Dave briefly mentioned this in his video because there's an example of it in the YouTube API

**Dave Jones:** library. Basically what it is, is it's a way of configuring the Wi-Fi on your ESP8266 without needing to reprogram it. Wi-Fi Manager is really configurable and the documentation on the GitHub page is really good, but the basic use case of it is that your ESP8266 will attempt to connect to

**Dave Jones:** the last known Wi-Fi network. If this fails, the ESP8266 will host its own Wi-Fi network and you connect to that using your phone or your laptop or whatever. When you open a web browser, when you're connected to this network, you'll automatically get redirected to this configuration

**Dave Jones:** page. So you click configure Wi-Fi, you enter into the details of your Wi-Fi network that you want the ESP8266 to connect to, so this would be your home network or whatever, and then when you click go, your ESP8266 will restart and it will connect to that network.

**Dave Jones:** You won't need to do this every time your device starts up. These details that you entered are saved in flash memory, so this is what the ESP8266 tries to use on startup. So the only time you'll see this configuration page again under the basic use case is if those details don't work for it.

**Dave Jones:** So I'll cover some more advanced use cases in a minute though. This is a Kickstarter that recently raised $183,000. It's called Connected Alarm Panel. So it aims to be a replacement panel for your alarm system at home that integrates with different IoT platforms such as SmartThings and Home Assistant.

**Dave Jones:** If we scroll down to see a picture of the inside of it, this is a NodeMCU board which has an ESP8266 on it. So this project will definitely have some form of Wi-Fi manager. If it doesn't actually have the Wi-Fi manager library installed, it will have some way of when you plug it in for the first time

**Dave Jones:** hosting its own network to allow the end user to configure it for their own Wi-Fi. So this Wi-Fi manager is even enabling commercial products as well. Wi-Fi manager is available to install through the Arduino library manager. So if you just go to sketch, include library,

**Dave Jones:** manage libraries, and when that loads up, if you search for Wi-Fi manager, you can install this one here by Zappu and just click install. And then just as Dave did with the YouTube API library, if you go to examples, you will now have new examples for the Wi-Fi manager and you can

**Dave Jones:** play around with the different ones of these. So the most basic one is AutoConnect. Basically all you need to do to add Wi-Fi manager to your sketch is you include these three libraries up here, you initialize Wi-Fi manager in your setup, and then you add this line Wi-Fi manager.AutoConnect.

**Dave Jones:** So this will create a Wi-Fi network called AutoConnect AP if it fails to connect to the Wi-Fi network. You can look through the other examples to get more complex use cases. Also, the GitHub page has pretty good documentation. Another great feature about Wi-Fi manager is it

**Dave Jones:** allows you to enable custom configurations inside this configuration page. So for example, this is looking for an MQTT server, but if we go back to the YouTube subscriber counter, we could enable one for the YouTube API key, and we could also enable one for the channel ID.

**Dave Jones:** So this is great for two reasons. Number one, from an end user perspective, you could ship them a device. They'll be able to configure their Wi-Fi on it. And also they can enter in their own YouTube API key and the channel ID of whatever channel they want to monitor.

**Dave Jones:** And then from a code perspective, it keeps these private keys and information completely out of your sketch. So you do need to handle what you do with them when this configuration happens. So you can store them somewhere persistent like EEPROM, but the ESP8266 has something called

**Dave Jones:** SPIFs, which I'd recommend using instead. It's kind of a flash storage system, works kind of like an SD card, but you don't need any external hardware. So this allows you to upload your exact sketch to GitHub and not be worried about sharing private information with anyone.

**Dave Jones:** This brings a new problem though. Previously, if you were only using it to configure your Wi-Fi details, your Wi-Fi details failing to connect was a pretty good indication that you needed to configure something. But now, what if you want to configure your Google API key or your channel ID,

**Dave Jones:** but you're still connected to the same network as before? We need a new way of entering this config portal. So we can do something like on the press of a button, or if you hold this button down at startup, enter into the configuration mode and that's all fine.

**Dave Jones:** But I find the best way of doing this is using another library. And we'll take a look at that now. Double Reset Detector is a library with a pretty descriptive name. Its purpose is to detect when the reset button is pressed twice. It's pretty simple, but it's very useful.

**Dave Jones:** We can install Double Reset Detector the same way as we did with Wi-Fi Manager through the Library Manager. When we have it installed, it'll add new examples. So if we go to the Double Reset Detector folder and then minimal. As mentioned, this library is really simple.

**Dave Jones:** Basically, we need to pass in a timeout, and that's the amount of time in between two resets where the second reset is considered a double reset and also an address. When this method is called detectDoubleReset, it will check an area in persistent memory for a flag.

**Dave Jones:** If it sees that that flag is there, this detectDoubleReset will return true and it's considered a double reset. If that flag is not there, it will return false and it will also set that flag. Inside our loop, we call drd.loop and basically what this will do

**Dave Jones:** is after the specified timeout, it will set that flag to be false again. So the next time detectDoubleReset is called, it will return false. If we look at the example in a bit more detail, when detectDoubleReset returns true, it turns the built-in LED to be on, which is active low,

**Dave Jones:** and if it returns false, it'll turn the built-in LED off. So I have this example running on my board here. So when I press reset once, the built-in LED stays off. If I press it a second time, since it's within the 10 second time limit, the LED will turn on and if I press it again, the LED will turn

**Dave Jones:** off. So this is useful if there's something you want to configure at the startup of your project. So for example, with Wi-Fi Manager, when it detects double reset to be true, you want it to launch into config mode, else just let it flow through as normal.

**Dave Jones:** If you check out the YouTube API library, I have an example that has DoubleResetDetector and Wi-Fi Manager working together. The next library I'd like to cover is another one of mine, and it's for Telegram Messenger. If you're not familiar with what Telegram is, it's very like WhatsApp.

**Dave Jones:** It's basically a multi-platform messaging client, but it has some additional features such as bots. So this is a library I created that allows your ESP8266 to integrate with the Telegram bot API. So that means you're able to send it messages, you're able to receive notifications from it, so it's pretty useful.

**Dave Jones:** To start using the library, you're obviously going to need to install Telegram, but also you'll need a bot token. To get that, you search for a user in app called BotFather, and then when you message him, you'll get a list of commands and you want to type in new bot and follow the instructions.

**Dave Jones:** One thing that's important to note is that your bot will not be able to message you until you start a conversation with it first. So if you just click the link here and click the start button, your bot will now be able to send you messages.

**Dave Jones:** This library can be installed through the Arduino Library Manager, so if you just search for Telegram and install the one with my name, because I think there's one for Arduino 101 boards. You will also need to install the Arduino JSON library the same way as Dave did for the YouTube API library.

**Dave Jones:** So again, there is examples that come with the library. So if we go to Universal Telegram bot and then the ESP8266 folder, there is a good few different examples. So echo bot is probably the most straightforward. So you would enter in your Wi-Fi details here, enter in your bot token.

**Dave Jones:** This is just standard code for connecting up to the Wi-Fi. Inside the loop, it will check Telegram every one second for updates. So this one second can be configured. And if it has a new message, num new messages will return not zero. So while num new messages is not zero, step through them and send a message back.

**Dave Jones:** So it'll take the chat ID from the received message, and also the text from the received message. So it's going to echo back whatever you send to the bot back to you. And it will keep checking get updates until num new messages is zero.

**Dave Jones:** This is the most basic example, but there's several other ones to go through if you're looking for more details. I've tried to document all the features that the library has on the GitHub page and with the included examples. But if you find something lacking, make sure to give out to me and I'll try to update it the best I can.

**Dave Jones:** To show off what this library can do, here's something that I made earlier. So it's Adafruit Feather Huzzah, which has an ESP8266 on it as well. It's got a NeoPixel ring, and it has a button. So when I press the button, I should receive a notification.

**Dave Jones:** Yep, so it just took a couple of seconds to get through, but there's the notification that the message was sent. But I also have these onboard keyboard options. So if I click the red, it will turn the NeoPixel ring on. It's very bright.

**Dave Jones:** If I change it to green, it'll set it to green. And if I set it to blue, it'll change it to blue. I can request the status. The NeoPixel ring is now blue, and then I can turn it off. This can be useful with any project.

**Dave Jones:** Say for example, instead of having a button to send you a notification, you had an LDR instead. So if the room was too dark or too bright, it might send you a message or the same with a temperature sensor. And then with the commands that could be used for basically anything,

**Dave Jones:** if you want to turn on and off a motor, or if you want to even send text to a screen, that's possible too. So I think it's really useful. In the interest of time, I just want to quickly mention a few more libraries that I think are

**Dave Jones:** really useful for the ESP8266. The first one I'd like to mention is one called Blink. And this one is a little bit different because you don't actually need to write any code for the ESP8266. You install a set sketch, and then you do all the configuration on your phone.

**Dave Jones:** So you just set up an account, you get a token, and when you set up your app, you then install a sketch onto the ESP8266 that you get through the library. And as you can see, the sketch doesn't have any configuration in it.

**Dave Jones:** It just has the auth token, and then it does this blink.run. So if you want to turn on and off an LED from the Blink app, you're configuring all of that, including what pin that LED is on in the app. So it's a pretty useful one.

**Dave Jones:** The next one I'd like to mention is another one of mine. It's an Arduino CoinMarketCap API library. So this is used to get cryptocurrency prices from CoinMarketCap. So they support basically any cryptocurrency. So it's an easy way of getting the live price of any cryptocurrency

**Dave Jones:** on your Arduino projects. Mac Lighting is the next software that I want to look at. This one actually isn't a library, but it's nearly more of a collection of libraries. So it's a piece of software that's used for controlling WS2812s, which are addressable

**Dave Jones:** LEDs, and they're also known as NeoPixels. So not only does it give you a web interface to control these NeoPixels, but it also provides an API around them. So you can control them from different devices such as your app or your phone. So the APIs it provides is a REST API, a WebSocket API,

**Dave Jones:** and also one for MQTT. So it's really useful. This one is another one of mine. It's the Arduino IFTT Maker. So there is a trigger in IFTTT, or if this then that, that was called Maker. I think it's now called WebHooks, but it still works the same.

**Dave Jones:** So this is a way of triggering that. So this would be the if part of an if this then that from your Arduino board. So this is a cool way of, say, you have a moisture sensor attached to a plant. You could get your plant to do anything you want

**Dave Jones:** that IFTTT supports. So maybe post to Twitter to say, hey, water me or whatever you'd like to do. And finally, this is another one of mine. It's around the Google Maps API. So if you want to check the live travel time between two positions and from your Arduino project, you can do that

**Dave Jones:** with this. So you just need to sign up for a Google Maps API. It's the same as signing up for a YouTube API, basically. And then you can do that. It can also be used to compare the travel time between multiple different routes.

**Dave Jones:** I built a project before for a friend of mine that showed the quickest route home from work to where he lived. Hopefully you found this video interesting. To jump out in front of a question, I'm sure I'm going to get asked in the comments,

**Dave Jones:** why wasn't this video on the ESP32? To put it simply, the ESP32 just doesn't have the same library support that the ESP866 has. I think 2018 will be the year that ESP32 passes it out, but it's just not quite there. If there's any other libraries that I've missed out on or any

**Dave Jones:** pieces of software you'd like to share, please put them in the comments below. Thanks a lot.
