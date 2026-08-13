---
video_id: S_HIs1Rv5KQ
title: EEVblog1062 - The Things Network - Progress Edit
url: https://www.youtube.com/watch?v=S_HIs1Rv5KQ
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 20, "2": 45, "3": 65, "4": 85, "5": 95, "6": 115, "7": 130, "8": 145, "9": 160, "10": 180, "11": 195, "12": 215, "13": 230, "14": 245, "15": 260, "16": 280, "17": 300, "18": 320, "19": 335, "20": 350, "21": 370, "22": 395, "23": 415, "24": 440, "25": 460, "26": 480, "27": 500, "28": 515, "29": 530, "30": 545, "31": 560, "32": 575, "33": 595, "34": 620, "35": 640, "36": 660, "37": 680, "38": 695, "39": 725, "40": 745, "41": 760, "42": 780, "43": 795, "44": 815, "45": 830, "46": 845, "47": 865, "48": 885, "49": 900, "50": 915, "51": 940, "52": 950, "53": 970, "54": 990, "55": 1000, "56": 1025, "57": 1040, "58": 1060, "59": 1075, "60": 1100, "61": 1115, "62": 1130, "63": 1150, "64": 1165, "65": 1180, "66": 1195, "67": 1210, "68": 1230, "69": 1245, "70": 1260, "71": 1280, "72": 1295, "73": 1310, "74": 1330, "75": 1350, "76": 1365, "77": 1385, "78": 1415, "79": 1435, "80": 1460, "81": 1495, "82": 1520, "83": 1535, "84": 1555, "85": 1575, "86": 1610, "87": 1650, "88": 1670, "89": 1705, "90": 1730, "91": 1750, "92": 1765, "93": 1795, "94": 1820, "95": 1850, "96": 1870, "97": 1885, "98": 1910, "99": 1930, "100": 1950, "101": 1970, "102": 1995, "103": 2025, "104": 2040, "105": 2065, "106": 2095, "107": 2115, "108": 2145, "109": 2170, "110": 2205, "111": 2225, "112": 2245, "113": 2265, "114": 2295, "115": 2320, "116": 2335}
---

**Dave Jones:** Hi, today we're going to take a look at the Internet of Things, or more specifically, the Things Network, or even more specifically than that, LoRaWAN. And I've got one of these new LoRaWAN Things Network gateways, which we'll check out and see how easy it is

**Dave Jones:** to set up. Now, what is LoRaWAN, I hear you ask? Well, LoRaWAN is developed by the LoRa Alliance, and LoRaWAN stands for Long Range, L-O-R-A, Long Range Wireless Area Network, Long Range WAN. And there's basically three major ways to get Things things onto the Internet.

**Dave Jones:** You can either directly connect them to Ethernet, you can wirelessly connect them via Wi-Fi, of course, where you've got to have your local Wi-Fi hub, and you know, you can get a reasonable Wi-Fi type range within proximity. Or if you want to put something, or want to

**Dave Jones:** connect something to the Internet from anywhere, you would use a cellular network GSM type gateway, and there's lots of solutions for that these days. But unfortunately, they're sort of, you know, two extremes. Wi-Fi draws a lot of power, cellular networks can draw a lot of power, cellular network

**Dave Jones:** connections, you've got to have like a SIM card, you know, it's a paid type thing, you've got to actually pay for network connections and things like that. And Wi-Fi, not only is it high power, but it's sort of like small range, doesn't have a large range.

**Dave Jones:** So LoRaWAN actually sits somewhere between these two, not only does it have long range like up to, you know, tens of kilometers, but it also is very low power, so it can run for, say, years from a set of batteries, and it's of course

**Dave Jones:** low data rate. Great for, you know, connecting, which we've got here, like a temperature sensor to the Internet, for example. It's an Internet of Things node. There it is. And if you want to hook this up, well, you know, yeah, you can do Wi-Fi

**Dave Jones:** but it takes power, you can do cellular, yeah, you might have to pay for something and it might use high power, but these things, apparently, we can get the Internet of Things running. And yes, I know I like to make jokes about the Internet of Things and how it's just

**Dave Jones:** groan-worthy that we have Internet of Things connected, light bulbs and toilet seats and all that sort of crap, but there's of course a lot of legitimate uses for the Internet of Things. So I thought we'd have a play around with this new gateway, which I've got here, which is apparently

**Dave Jones:** so I'm told, led to believe, this is the easiest way to get a LoRaWAN network up and running. So this is a gateway that I've got here, and a gateway is what you need, think of it like a Wi-Fi router for example. It's how you can connect your devices, your things, up to

**Dave Jones:** the Internet. You use one of these gateways, but the range can be quite long range. As I said, tens of kilometers, and they can talk to each other, and everything can connect together, and for those playing along at home, this won't be a tutorial on LoRaWAN, because I don't know a huge

**Dave Jones:** amount about it yet, but this is designed to be just experimenting with it, and try and set something up, and have a public Internet of Things node, and see if I can connect little nodes, in this case a little temperature sensor. But there's a whole bunch of other stuff, so let's actually take

**Dave Jones:** a look at this, the Things network. So you can see how basically it works here, you have your devices, you have your gateways, which we've got here, and the gateways actually connect to your traditional Internet, because this can't just connect, you can't just apply power to this,

**Dave Jones:** and it hooks up to the Internet, of course, it's got to connect to an Ethernet or Wi-Fi traditional network connection, and then you can run applications, and get data, and all that sort of stuff. And the Things network actually has this rather nice map, and you can see

**Dave Jones:** all the public gateways, and things like that available. So if we go down to Sydney here, and that's the good thing about this, is that if enough people install these public gateways, then you can just be driving around, for example, and have an Internet of Things

**Dave Jones:** on your bike, or in your car, or walking around, or whatever, and you can just seamlessly move from one gateway to the next, and your Internet of Things sensor or device will have continuous Internet connection, and it can share the data. So let's have a look at a few here in Sydney,

**Dave Jones:** and I'm out here, I'm out near Bella Vista out here, I'm in the Norwest Business Park here, and you can see that there's not a node within KUI of that, but there are quite a few other ones around, and you can see that they're probably all different, like

**Dave Jones:** Curlink, Brand, Curlink, Indoor, all sorts of stuff. There's all sorts of different gateways, so the plan today for this video is to get one of these gateways, which is the official Internet of Things network gateway, and here it is. It's the one that they

**Dave Jones:** actually sell. In this case I got, it's not cheap by the way, but this is apparently the duck's guts in its longest range, and it's the easiest plug-and-play type thing. At the moment you can only, I think you can only get it from MUARC, that's where I got it

**Dave Jones:** from in the US, and it's like $325. It is not cheap. But I wanted to experiment with this because I thought it would be cool. There are much cheaper solutions of course. So I've got the gateway, I've got the Things node, which I believe is just like a little temperature

**Dave Jones:** sensor, and I've got an Arduino, the Things UNO, which is an Arduino UNO with the LoRaWAN transmitter on there. And you can get a whole bunch of devices that doesn't, you don't have to buy them from the Things network. Anything that's compatible with the LoRaWAN

**Dave Jones:** system should work on the Things network. So that's the idea. So, you know, like Artifruit for example, sell a whole bunch of these feathers, which is their little form factor thing. A whole bunch of these things, you know, like RFM32U4 1, there's a Cortex-M0 for example, and

**Dave Jones:** you know, a bunch of different ones like this. You can go to AliExpress for example, you can buy really cheap if you're into ESP32 for example, you can get really cheap LoRaWAN compatible units and stuff like that. It's amazing, you know, $15. Look at that, free shipping, $14, you can get

**Dave Jones:** one with a little screen and everything. LoRaKit, you know, absolutely amazing. But you have to get the right frequency for Australia, I've been told. You need the 915 MHz, which is the license-free band for the US as well as Australia. So there you go, we're going to give it a go and see if we can add our device

**Dave Jones:** to this Things map. Where is it? Yes! So my goal for today's video is to hook up this and just see how easy it is. And they claim, oh look at this, activate your go-to-the-website, connect to Wi-Fi in the Things network, it's that easy, so they reckon.

**Dave Jones:** Let's give it a go. So inside the box we have the gateway, this is the backer edition, there you go, I wasn't a backer, I just bought it on Newark, and it's pretty easy-peasy, we've just got the antenna there, we've got Ethernet and power requires a 2 amp, there's a little SD card in there presumably for

**Dave Jones:** updating, and 27 dBm transmit frequency on the 902 to 928 MHz band. There you go, and it's got Bluetooth and wireless LAN as well. So all we have to do is go there and activate it! Let's see if it's that easy, it'd want to be for the

**Dave Jones:** price. And I got a plug pack with one of these stupid Yankee plugs on it. And we got a little antenna as well, of course if you wanted the maximum range, you'd mount this inside your house, run a coax up to a proper, you know,

**Dave Jones:** maybe a higher gain antenna on your roof or something like that, if you wanted, you know, if you're setting up a public gateway for the absolute maximum. So this one here actually provides up to 10 km, 6 mile radius of network coverage. I think I've read

**Dave Jones:** some people have gotten much more than that if you have, as I said, a high gain antenna way up, you know, you're on top of a hill or whatever, you've got good coverage, and you can get fastened Bluetooth 4.2 modem for indoor, indoor, and other things, connections, so

**Dave Jones:** if you didn't, you know, if you had local nodes for example, you know, if they're around the house and you've got a gateway as well, you don't actually have to connect through the LoRaWAN 915 MHz, you can just connect via Bluetooth, of course,

**Dave Jones:** if you're close enough. So there you go, I hope it like seamlessly transitions, for example if it goes out of Bluetooth range, you'd like to think it transitions open, but runs on open hardware and open software. Is it all here? I don't know, where are the links

**Dave Jones:** to all the hardware? Hmm, maybe it's here somewhere, try and find a link. Support, maybe, maybe it's under Learn. Community support, 25,000 Internet of Things developers, do it yourself, for free. Open source code, there you go, see open source code, go to the Things industry.

**Dave Jones:** It's beautiful, so if we go over to the GitHub, the Things network, Network Stack, Arduino, Docs, Gateway, Gateway Connector Bridge, Gateway Conf, Python stuff, I don't know, I assume that the hardware's there as well. I might just crack this open. Yeah, check it out, that just clips open, ZigBee Connector there, look at that, so it's really

**Dave Jones:** hackable, that looks like, well you don't even have to take the case apart, and you can get in there and hack around on this thing. Very nice. And it's got a PIC32 processor, which I am told makes it less, well, it's always going to be hackable,

**Dave Jones:** for example, like in terms of somebody hacking your device turned into a zombie Internet of Things zombie device or whatever, but because it's based on a PIC32 it's a more obscure hardware platform so that you've got to put more work into deliberately attacking a device like this.

**Dave Jones:** So, you know, that kind of helps. So PIC32 processor and open hardware and a microchip. Well, it's got a microchip on it, so anyway, let's try and plug it in. Let's build this thing together. Now that you have your hands on the Things Gateway node and or UNO, it is time for you to join the movement and help build a global

**Dave Jones:** Internet of Things network. Yeah, as I said, you don't need a huge gateway like this, you can just get one of those little tiny boards and it can become, you know, it can join and become a gateway or whatever. There's just tons of different devices out there,

**Dave Jones:** but this is the approved one from the Things Network. So, activate it. Ooh, docks. Look. Where to start? Gateway registration, packet forwards, troubleshooting. Wow, okay. Six mile range. Set it up in as little as five minutes. Can serve thousands of nodes. It can set up a public gateway and you can have thousands of little

**Dave Jones:** devices driving by and using your thoughtfully provided LoRaWAN gateway. Go to the activation page. All right, here we go. Activate it. Register. Oh, I've got to register first. It's fair enough. All right, so it's asking permission. The client will be able to get

**Dave Jones:** basic information about your account. The client will be able to manage your gateways. Yeah, no worries. Let's get started. Okay, unique identifier. I thought this would be a unique thing on the back, but it's not. So, we'll call it EVBlogOffice, for example, because that's where I'm going to have this one.

**Dave Jones:** And frequency plan, Australia. Bloody ripper. Auto update gateway. It cannot start with or end with a dash or an underscore. Ah, a lowercase. Jeez, that's a bit restrictive. Or should I just call it EVBlog1? I'll just call it EVBlog1. Oh, but I can't

**Dave Jones:** change it! Too much pressure. Connect your gateway. You're successfully registered to EVBlog1. Are you ready to get into this? You need to connect your gateway over WiFi. Make sure the gateway is plugged in, blah blah blah, to access this and the password of things.

**Dave Jones:** Looking for your gateway. Better power it up. Got some lights on there. Got one blue LED. One flashing. Looking, looking, looking. Make sure your gateway is in access point modus mode by checking the LEDs. They should look like this. Oh yes! Right! Yes, the one solid and the

**Dave Jones:** one flashing. Yes, it certainly matches that. One solid and one flashing. I'm going to use up my five minutes allotted time to set up this just by waiting for it to connect. One thing I noticed, with the supplied antenna, it can tilt like that, but the plastic's in the way.

**Dave Jones:** So if you're sitting it flat on a desk, you can't, without taking off the plastic top, you can't actually make the antenna flip up. You can make it go out like that, but it's designed, it's got suction cups obviously, designed to go on a window.

**Dave Jones:** But it, like if you want to sit it flat on your desk, you're out of luck. Fail. Oh, silly me, I've got to connect to the gateway's wifi access point using the password thethings. Heh, that's secure. I'm sure we can change it later.

**Dave Jones:** Yeah, how do I do that on a PC hooked up to my router? I don't know, I'm not that good with technology. Right, so I don't think I'm actually going to be able to do this easily because my computer, the Windows 10 computer I've got, is connected via Ethernet to my

**Dave Jones:** wifi internet modem-y router thing, and you can't it's not like having, if I had my Microsoft Surface here that had the wifi built in, I'd be able to see other wifi devices and connect directly. But it's too hard to do it via the router.

**Dave Jones:** I know everyone thinks it's probably easy, but I'm just going to have to go get, I could do it with my phone, I guess I could do it with my phone, I'll try that. And of course I can't do that because it already

**Dave Jones:** exists. Right, I've connected to it and it's still looking for the gateway, so it's actually connected via the wifi, but it just can't see it. There it is, I'm connected but nah, nothing. So I actually took the thing home and used my Microsoft Surface tablet-y computer thing, which of course

**Dave Jones:** has the wifi built in. So this time, just like my phone, I was able to connect to it, but this time it actually just worked, so no worries. You've got to have a computer with a wifi card in it to be able to actually connect.

**Dave Jones:** And then it said, I had to call it EEVBlog4, and all the lights went on, I got four solid lights, but it never ever, and I left it for a long time, never ever actually connected it in this configuration. But when I actually went over

**Dave Jones:** into the Internet of Things, my account, it says it's actually connected. There it is, EEVBlog4 is connected. So it works, but that setup process never actually went through the motions. Hmm. Kind of a fail, but ultimately seems to work. Alright, so I'm back in the

**Dave Jones:** office here, so I connected and set it up at home and it worked a treat. I brought it back here, it seemed to have a bit of a problem connecting to the router here, it took a few minutes, it cycled through a few times, had to re-turn the power off and on again, but it's connected.

**Dave Jones:** I've got four solid LEDs on the unit, it's just down there, and if we actually go into the console here, we can see, well, got no applications yet, but let's have a look at the gateways. Ta-da! There it is, EEVBlog4. Presumably I can go in and delete the others now, and we are, it is

**Dave Jones:** connected. So there you go. Last seen, 24 seconds ago, and that seems to reset every time you try and access it or something. So there you go. Oh, no, just did it automatically, and it's got the gateway key there, it's a, you know, it's a huge

**Dave Jones:** key, looks pretty secure. Random thing, receive messages, nothing, so we're not receiving anything, we're not transmitting anything, we don't have any apps, nobody's driving by trying to access my thing's gateway. And sure enough, I've set it up here, haven't set up the exact location, but I've just put it on a little island here in the middle of the

**Dave Jones:** Norwest Business Park, no worries. And presumably people can just drive by and use my gateway. Cool! Right, so we've got to get the node thing running now. Awesome. It's getting there. And sure enough, if we go to the map, there it is! Ta-da!

**Dave Jones:** We're in Lake Flynn, we are now part of the network. But curiously, this one doesn't show the range, but if you actually go into the communities thing, and like I'm now part of the Sydney network, there's the core team of the Sydney network, fantastic, there's 95 contributors, 23 gateways in Sydney, which I'm now part

**Dave Jones:** of, it shows my, well, estimated radius. I don't know how you can actually get in there and modify that, maybe it takes into account whether or not you specified indoor or outdoor antenna or whatever, but you can see the range that it should actually cover.

**Dave Jones:** So in theory, this thing should be able to get between my office and my home, because I don't live that far away. So that's the plan, but hey, it is the hills district here, and they don't call it the hills for nothing, so that could be a problem.

**Dave Jones:** But hey, this one node, in theory, should service a couple of business parks around this area. Awesome. Now, let's try and set up this thing's node here. I've installed a very nice case, I like that it's got the lanyard thing, and it's got the waterproof seal around

**Dave Jones:** here, I'm not sure what the IP rating is, it's got a button on the top with a RGB LED apparently, it's got a temperature sensor and a movement sensor and stuff like that, it's just, you know, like you can press a button and activate stuff, or you can display stuff

**Dave Jones:** as the LED. So it's kind of like a multi-purpose demonstration node, but you can use it for real things, because that is quite a rugged case. 3 AAA batteries, which last for at least a year apparently, which isn't too bad. I would have liked to see a bit longer than that for 3 AAAs, but

**Dave Jones:** you know, hey, considering that this thing, the range that we can get with this thing, and I believe this has 27 dBm transmit power as well, I won't take it apart because you can't see much, like, didn't see that it pulled out or whatever, but there's the board.

**Dave Jones:** And apparently if we go to map it here, it says it comes with a pre-installed Arduino sketch that pings home and sends the sensor data on setup as well as every minute. Yes, it is an Arduino in here, basically an Arduino Uno, same as the other Uno

**Dave Jones:** I've got, but it's got the nice case and batteries and everything else in it. And the sensors. So, power your device, there it is. Identify your device. So but yeah, it looks like, and this is what the quick installation guide, we have to go in and set up the, and we've got to use the

**Dave Jones:** Arduino IDE and everything and set up the sketch and get the device ID, download a sketch to get the device ID or something, and then, like, it's really quite convoluted. I expected this out of the box, just to, like, work. I expected to put the batteries

**Dave Jones:** in and like, see this on my, like, and actually be able to click on here. I know this is probably not how it's done, but this is kind of what I expected to be able to look, you know, set this up as by default as like a public

**Dave Jones:** node that I could just see when I connect to that gateway. That's probably not how it works, but that's kind of how I intuitively expected it to work, I guess. So yes, actually I think the sketch is pre-installed but the problem is we have to download another sketch, a deviceinfo.ino

**Dave Jones:** file to get, and then we have to replace it, the 915MHz one, which will then spit out via the serial monitor the device ID and it would have just been far easier if they did that for you, especially for the price, I guess.

**Dave Jones:** It gave you the device ID on the card that came with it. Then you could just, like, go. You can't just assume everyone knows how to use Arduino and has Arduino. Yeah, I do. But, you know, people connecting the internet of things go, what's this Arduino stuff?

**Dave Jones:** What's this sketch? What's this serial monitor? I don't understand. Like, you know, it needs a level of knowledge that, even though it's easy, you know, you think, oh, everyone knows how to use Arduino. Like, no. I don't think that's right. It should come with the device ID, which

**Dave Jones:** is hard-coded into the LoRa module itself, which is great. Everyone's unique special snowflake. Actually, it's not an UNO inside this thing, it's actually a SparkFun board which identifies as a Arduino Leonardo, or something like that. So we have to actually go in, and they point you to this, which is fine, but we have to go in

**Dave Jones:** and install the board. We have to, specifically, I've done this in previous videos, but they link you to the SparkFun instruction page where you've got to install the board, then it installs all the drivers and software automatically. It's very nice in an Arduino environment to do this, but

**Dave Jones:** the fact that I have to do this is just, I think it's wrong. So if we paste in our JSON file there, we should have that board. If we go into Boards Manager here, we should be the Arduino SparkFun, supposed to be an Arduino Pro

**Dave Jones:** Micro, ah, SparkFun AVR Boards Pro Micro, I think that's the one. Install. Yes, should be. And it will now install support for our board. Awesome! Don't worry about this code, it's just old crap. Aha! There we go, SparkFun Pro Micro. So now we should be able to get the examples,

**Dave Jones:** Arduino AVR Boards, alright, the Pro Micro. Okay, so we should be able to now get our device info sketch and download it. Okay, if we go into Manage Libraries here, now we should be able to search for the Things Network. There you go, the Things Network Library.

**Dave Jones:** Ta-da! Install. Beauty. So this should now give us the examples we need. Close. And if we go into Examples, The Things Network! Yes, device info sketch. There we go. Alright, now we're cooking with gas. Let's download this and try it. Upload. Whatever you call it.

**Dave Jones:** Compiling sketch. Ah, replace me. Frequency plan. I think it's 915. Does that make sense? Let's try it. Come on, you can do it. Yes, that looks promising. Come on. There we go. Hang on. Now it's uploading. I selected the right port. Done! Yay!

**Dave Jones:** Our sketch is now... ooh! And our LED's on, I can't show you. Yay! We won! Look, there's our EUI, and it shows the battery volt. There we go. Beautiful. So we just copy that. See? All the effort I have to go through just to do this.

**Dave Jones:** Now I've killed the sketch on there that does anything useful. Now I've got to reinstall the example sketch, the demo sketch, to get us back on the network. It's just a step that didn't need to be done. It's crazy. Actually, I got that wrong.

**Dave Jones:** The plan there should be that. So I just want to do that again, just in case. It shouldn't give a different unique ID, but apparently that's what you had to do. But just putting 915 did work, so meh. Whatever. There we go. We're good to go.

**Dave Jones:** Now, after doing all that, we've already created an account on the Things Network. Now we have to add an application, and then we have to register our device. So here we go. So we add an application. Get started. Add application. The unique identifier of your application on the network.

**Dave Jones:** Okay, so that's not our code. That's EEVBlogNode1. For example, human readable EEVBlogNode thingy. Application UEI issued by the Things Network. Okay, that will be, you can add your own in the application page. EUI. Right. Well that's the thing that we copied from. That's the EUI, yes.

**Dave Jones:** That's the thing we copied over. So, okay. Add application. Handle and registration. Whoa, I missed that. Two seconds ago. Node thingy. Yep. Zero registered devices. Access key. Collaborators. Access keys. Application EUIS. Better read the instructions. Better RTFM again. Does not have any devices yet.

**Dave Jones:** Register your device. Here we go. You are now ready to register your device. On the application page, scroll down to devices. Select devices from the top right hand menu. Alright, let's do that. Devices. Register device. Device ID. Aha! The device, ah, okay. Oh no, that was the application.

**Dave Jones:** So the device ID is eevblog. It's all probably all lower case again, right? Because it, yeah. Node one. So it matches. Is that okay? App key. This field will be generated. Add app. Register. Successfully registered device. All right. Simulate uplink. I don't know, send something.

**Dave Jones:** Uplink message simulated. Does that mean that we're going to see that in our console over here? In our gateway console? If we actually went in here and looked at our traffic, our received messages, it doesn't simulate our message. I don't know if that's the correct thing.

**Dave Jones:** Okay, but now we presumably have to go back and install our sketch, right? The node example. So, oh, and then we've got to copy the app now we've got to copy the app EUI and the app key as well into our node thing.

**Dave Jones:** It's not necessarily hard, but jeez, there's a lot of steps and it's convoluted, and if you don't follow them exactly, you're going to come a gutter. Okay, so examples. The things network. Class dedicated. It wraps the commands to work with the various sensors in a simple API.

**Dave Jones:** Okay, fair enough. I don't see the things network one here. Is it quickstart? Maybe it's the quickstart one. Oh, there we go. Yep. Okay. I assume it's the quickstart. So we've got to add our EUI thing and our app key. Wow. Okay. Where am I?

**Dave Jones:** Okay, we've got our app key. Status join. Lead bulletin, lead off, lead on. Okay. Wax on, wax off. No worries. That's what we want. So let's upload that. We don't need our silly replace me was not declared. Oh yeah. Always forget that. There we go.

**Dave Jones:** It even tells you right there. Isn't that nice? Nice commenting. Well done. There you go. Compiling our sketch. So this should now contain this little node thingy-ma-bob. Should contain our lead on. Should contain our app. Our quickstart app. Yeah, like I know the whole idea of this

**Dave Jones:** is that, you know, you design your own nodes and things like that, but when I buy a thing's node screws. They're not captive. When you buy a thing's like, you know, when I paid like 50, 60 bucks or whatever for my thing's node

**Dave Jones:** I kind of expect it to just do its node thing, you know? Not have to dick around with all this sort of stuff. Just takes the shine off it. Check your coverage. Keys and backend status. Sending Mac join OTAA. What if I press the button?

**Dave Jones:** Does it do anything? No. I have no idea what I'm doing. Check your coverage. So I assume it's like, it's just not connecting. Now I'm actually wondering if I could have just mapped it out of the box. But I followed the quickstart guide, which was all the Arduino

**Dave Jones:** stuff. So can we get your identify your device? Yeah, no, it still says you need your unique EUI. Can't tell, yeah. But maybe it would have just shown up, but it didn't last night. I actually put the batteries in and I had my node connected and everything

**Dave Jones:** and it just, like, so I'm not sure what the deal is there. Anyway, but we're supposed to be getting all this, which is different. So, no, maybe I got the wrong sketch. Aha! I think I might need the thing's node library. So let's

**Dave Jones:** go and try that again. Okay. We can do it. Aha! There you go. The thing's node. We just didn't have that. So yeah, I had the wrong thing installed. Sorry. So we go in here. Boom. That's installed. So we should now have in our examples, the thing's node.

**Dave Jones:** Thank you. Basic, battery monitor, device info, pass through, test. Test? The thing's node, I guess. Ta-da! There we go. That's the one that we should install, and that is get temperature, button, and all that is moving. Right. That's what we want. So actually that, well

**Dave Jones:** where's the thing to set up the thing's node? Where's the thing to set up the EUI and all that sort of jazz? The thing's node.h? No, okay. No, that's just a header, is it? Yeah, no, that's not right. Thing's node. Hmm. Basic. There we go.

**Dave Jones:** Port interval set up. Okay. There you go. That's better. That wasn't obvious. I really like the fact that it actually gives you the things down here. You don't have to copy them from up there. That's just nice, the example code. That's nice. Nice touch.

**Dave Jones:** Someone was thinking. Okay, I think we're set up there. Let's download this sketch and see if we can actually get something going. Oh goodness. This is not the best out-of-the-box experience, let me tell you. Trying to use the internet of things. Mac, join, OTAA.

**Dave Jones:** Join not accepted, denied. Check your coverage keys and backend status. Great, thanks. LED's green now, though. We've got a green LED. It's better than the red we had before, I guess. Denied! Yeah, maybe I'm just not reading the instructions clearly enough. Create an account, add application.

**Dave Jones:** We've registered our device. Our device is hunky-dory, we've done that. The things node example. Yeah, basic. We've got the basic one installed. That's it. Replace me with the frequency plan. Done that. Upload. Surely I'll see the current temperature and values and other sensors.

**Dave Jones:** Things network class loop. You should have code inside loop. Yeah, that's great. You know, when we want to do our custom app. That's terrific. But I just want to get my poor node. It's joining! I've got my mappity doodah thing. Got my gateway mapped.

**Dave Jones:** Okay, data. Hey! No, port one counter. Time. No, or is that that test one? That might have been the test one. I don't know. Activation. No. OTAA. Yeah, that's the activation method. EV blog node one. It's orange. Doesn't look good. Simulate. I don't know.

**Dave Jones:** Payload. Hello. This is text data. Send. I'm at a loss as to what I'm doing wrong here. I don't know why it's not connected. I assume that that is not normal. Join not accepted. Why is it denied? I don't know. I think I'm going to have to seek help from the forum, maybe.

**Dave Jones:** The Things Network forum. So I might just upload this video to the second channel. Just as a temporary, well, I'll probably stay there forever. Just as a temporary thing to show my progress on this. And how my gateway seems to work. But my poor little node

**Dave Jones:** just doesn't, I just don't get it. And that's the end of the quick start guide. You know, we're down, we're supposed to download the basic things in the example, the basic node, replace the app EUI, boom, upload, and serial monitor. Surely I see the current temperature.

**Dave Jones:** Let's run through to understand, and then it just tells you to understand what the app does. And then it tells you nothing about, that's it. That's the end of the example. The setup, the quick start thing. And so, API reference troubleshooting. There's a troubleshooting.

**Dave Jones:** Parts, serial port bricked. No, we're not bricked, we're running just fine. They're talking about AVR, that's to unbrick it and stuff like that. No, we, no. The troubleshooting problem is that it's not actually connecting. So, anyway, help! Maybe I'm just dumb. Maybe I just haven't followed this thing

**Dave Jones:** precisely enough. But that's not a good it's not a good first impression of the Things Network when you buy the like, I maybe expected all this if I, you know, bought something on AliExpress you know, an ESP8266 node for 10 bucks or whatever, but I bought the proper official Things node, and

**Dave Jones:** the proper gateway and everything else, and everyone assured me that this was the easiest way to get on the Things network, and the gateway was ultimately pretty easy after figuring out the Wi-Fi thing. Whether or not you can do that via Ethernet, I don't know, but

**Dave Jones:** I don't know. I can't get the node to do its thing, so, I don't know. I think I might just phone a friend. Catch you next time.
