---
video_id: WC1YT66c9KM
title: EEVblog #1232 - Add Web Access To Old Instruments!
url: https://www.youtube.com/watch?v=WC1YT66c9KM
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 27, "3": 57, "4": 68, "5": 82, "6": 98, "7": 112, "8": 126, "9": 140, "10": 160, "11": 173, "12": 190, "13": 202, "14": 212, "15": 224, "16": 237, "17": 246, "18": 262, "19": 280, "20": 294, "21": 312, "22": 323, "23": 332, "24": 345, "25": 354, "26": 369, "27": 381, "28": 398, "29": 410, "30": 420, "31": 431, "32": 449, "33": 459, "34": 468, "35": 481, "36": 499, "37": 507, "38": 521, "39": 529, "40": 544, "41": 565, "42": 580, "43": 589, "44": 598, "45": 608, "46": 623, "47": 641, "48": 655, "49": 670, "50": 680, "51": 696, "52": 711, "53": 729, "54": 743, "55": 756, "56": 769, "57": 782, "58": 794, "59": 805, "60": 817, "61": 833, "62": 853, "63": 865, "64": 874, "65": 886, "66": 911, "67": 919, "68": 930, "69": 940, "70": 952, "71": 974, "72": 990, "73": 999, "74": 1012, "75": 1021, "76": 1033, "77": 1050, "78": 1059, "79": 1072, "80": 1087, "81": 1097, "82": 1107, "83": 1116, "84": 1138, "85": 1148, "86": 1157, "87": 1166}
---

**Dave Jones:** Hi, this is my HP 35668 dynamic signal analyzer. You've seen this in previous videos and it's one of countless old school bits of kit you can score on eBay or auction houses or anywhere else that still are fantastic performing instruments and very very useful.

**Dave Jones:** You can get them dirt cheap. But often the problem comes if you want to actually talk to it with a PC cuz all this old school stuff ethernet wasn't invented, USB wasn't invented.

**Dave Jones:** If you're lucky, it might have an old school serial port which with a string commands which makes it easier to talk to, but most instruments, especially HP gear like this back in the day, had the HPIB or the Hewlett-Packard interface bus or also known as the GPIB, the general purpose interface bus, also known as the IEEE 488 standard which they're kind of there are differences between them, but basically they're

**Dave Jones:** lumped into the same particular standard. And that's really the only way to talk to these instruments and of course it's been the de facto industry standard for jeez, I don't know.

**Dave Jones:** When was GPIB invented or HPIB invented? It's been around for a long time. Anyway, you'll find racks and racks of gear even today all networked with GPIB as I'll call it.

**Dave Jones:** Anyway, even modern gear like this Keysight 7 1/2 digit meter, it is backward compatible. They sell these to companies who often have these old racks and things and they need to actually interface those over and there it is, the GPIB interface.

**Dave Jones:** If you see that connector on an instrument, even if it doesn't have it written there, it's almost certainly GPIB. Of course this one has LAN and USB and and things like this old Philips system multimeter, for example.

**Dave Jones:** Let's have a look at that. There you go, GPIB system 21. I don't know what that is. That's probably some custom interface or something. And this is just some of the other gear I've got that's a GPIB controllable in my lab.

**Dave Jones:** This is my old Keithley electrometer that is ancient GPIB interface. Brilliant. I've got my uh one of my voltage and current standards here. I've got my Keithley battery simulator, Keithley source measure unit up here.

**Dave Jones:** Once again, this one actually does have RS 232 and this is a classic. It's the industry standard it was the industry standard source measure unit. But unfortunately, the problem is if you want to control these GPIB instruments, you usually need either a USB to GPIB converter which if you buy the genuine ones can be quite expensive.

**Dave Jones:** There's a flourishing second-hand market for those. You can also get of course plug-in ISA old school and PCI cards from National Instruments are one of the big companies that do those cards.

**Dave Jones:** And yeah, they're fiddly and also you've got the big bulky expensive GPIB cables as well. If you've ever tried to use one of those, ugh. And then you've got to install the correct drivers for them and they might might have an old card, an old adapter or whatever.

**Dave Jones:** The drivers might not work with the latest Windows 10 or Linux or whatever. And then you've got to have the software to actually talk to the driver and send the GPIB commands over and actually get something back from it.

**Dave Jones:** It's really convoluted and pain in the butt process. Well, what if you had something where you could just use your phone or your web browser to talk to your GPI instrument directly?

**Dave Jones:** That'd be cool. Well, today here it is. This is the KISS 488 from HAKSET HX Engineering LLC hxengineering.com. I checked and their website was down so I'm not sure what the deal is there.

**Dave Jones:** Nice diecast casing GPIB connector on there and it's just got one of these ethernet things. There'll be a little micro in there. I'm not going to take it apart and do whatever.

**Dave Jones:** It's got a couple of LEDs on there that can actually help you configure it and know the status of it. Powered from 5-V USB here, and it just plugs directly in to your instrument.

**Dave Jones:** No cable, no mucking around, and you can talk to it just with a web browser. Brilliant. So, I'm going to plug it into the back of my dynamic signal analyzer here, and um see if we can get it on our phone or a network web browser.

**Dave Jones:** This is connected via Wi-Fi to my local router here. So, one of my viewers actually alerted me to this product. It's been around a while, 2017. So, I picked up one, 150 Yankee bucks on eBay directly from the designer of this thing, and it comes with a quick start guide.

**Dave Jones:** Nothing on the back, and a very comprehensive user guide. And KISS stands for keep it simple, stupid. But anyway, it's very comprehensive, especially in the various ways that you can actually connect to it.

**Dave Jones:** NetBIOS name lookup, pings, address DHCP, DHCP server announce protocol, auto IP, network analyzer, or a bigger hammer option, which is just to actually read out the flashing LED on the thing, which will give you the IP address.

**Dave Jones:** Absolutely brilliant. Thought of everything. And we're supposed to get a web interface. Let's give it a whirl. So, let's try the simplest solution, which is the NetBIOS name lookup, HTTP.

**Dave Jones:** No none of that S rubbish. Theory, don't have to look up the IP address of the thing. Neat. All right, please excuse the crudity of this phone capture. I didn't have time to build it to scale or to paint it.

**Dave Jones:** So, let's put in that and see if we can get access. Site cannot be reached. What? So, while that was a fail on my phone, I can confirm that does work on my desktop web browser.

**Dave Jones:** Yeah, it could be a phone or an Android thingy. So, from the web browser, I do actually know the IP address now, so this should work. There we go.

**Dave Jones:** So, yeah, that button that bias domain name will will There it is. There we go. There's our control. That's actually web served from the little web server inside the Keith 488 itself version 1.64.

**Dave Jones:** You can apparently contact the author to get like new firmware versions and stuff. We can go in there and now configure a direct You can set the address here.

**Dave Jones:** You can set whether or not what file capture you want HPGL cuz another great thing about this is that it basically emulates a plotter or a printer. And so, apparently, you can get traces out of this thing.

**Dave Jones:** So, absolutely brilliant. So, anyway, I'm just command to trigger it a screen capture. I'm just going to leave that as standard. And you can set Keith address. I'm just going to leave all that as default.

**Dave Jones:** We go over to control over here. And this is our control page. There you go. And we can have up to 246 different commands actually programmed into the thing.

**Dave Jones:** Or we can send them and you can save them into the embedded into the firmware of the thing itself. And then they'll give you the reply from the instrument down here.

**Dave Jones:** So, we do have to make sure our instrument is set up in this case addressable only analyzer address down here. I've got it set to 22 over here. And then the peripheral addresses, we can actually set our plotter address and our printer address as well on the GPIB bus.

**Dave Jones:** Cuz the GPI Every instrument on the GPIB bus has to give an a unique identifier number. Otherwise, they conflict and All right, so let's give this a try now.

**Dave Jones:** I'll keep it up there so you'll be able to see it like remote and talk on here. So you should be able to see those annunciators uh change if this is able to talk to it down here.

**Dave Jones:** So let's send the asterisks IDN IDN command. Every GPIB instrument should understand that, but please be aware that there are massive differences between the command sets on GPIB instruments.

**Dave Jones:** So like IDN is probably the only major universal one. So I'm going to send that command. And bingo, remote. There you go. Did it return the command? There it is down there.

**Dave Jones:** Winner winner, chicken dinner. As you can see, it gives us the name of the product, the model number, looks like the serial number, and the version number. That's quite common.

**Dave Jones:** This so it works hunky-dory. So we should now, in theory, be able to get the programming manual for this DSA and actually send any sort of command. But I've shown that it works.

**Dave Jones:** So you know, it's just fine. Let's try another instrument. Let's try a more modern instrument here. Let's get this Keysight 7 1/2 digit meter and GPIB settings. There you go, 22.

**Dave Jones:** Let's just keep it the same. I haven't actually reset anything. I haven't reset the power to the Keysight module. I've just simply transferred the cable over to here and I haven't reset any of the firmware.

**Dave Jones:** So I'm just going to give this a whirl. Let's go send again. And looks like it worked. Bingo, Keysight. It talks. No wuckers, it just works. It's brilliant. And once again, we got the name, the model number, the serial number, and it looks like firmware versions as well.

**Dave Jones:** So let's just try sending something, EVM. Let's just I don't know, send that. It just happens to be default in there. Let's see if it sends anything back. Reply from instrument, absolutely nothing Because we're not sending the correct commands.

**Dave Jones:** So, yeah, I just thought I'd send that. Why not? Let's actually do measurement measure test value to see if it actually just gives us some sort of default value back or something like that.

**Dave Jones:** No, it said it take too long. Nope, it didn't like that. And you can see up there, error. So, that's actually a GPIB command error. It didn't like that command.

**Dave Jones:** Of course, we could go get the programming manual for this thing and type in the correct commands. But, let's try an older school real simple instrument like this system multimeter.

**Dave Jones:** Again, that's address 22. So, I won't touch anything. Haven't repowered anything. Just send ID command. That was pretty quick. And bingo. Whoa, actually, that didn't work. It gave us the voltage.

**Dave Jones:** So, it this looks like this Philips 2534 system multimeter doesn't accept the IDN command. But, it did return our voltage. Wow. Okay, well, let's send this EVM command. And bingo, it's returning.

**Dave Jones:** Let's just send anything. Measure value. Send that. And yep, it's just returning voltage every single time. So, that's just a real old school GPIB interface by looks of it.

**Dave Jones:** Okay, I've hooked up a 10K resistor to that. Command, see what we get out of that. RTW 9.9961 plus 10 to the E plus 3. So, yep, that's 9.999K.

**Dave Jones:** So, you can send single commands like that, which is useful, but you can also do capture, which actually has a data logger built in. And I don't believe you need it actually connected to the PC.

**Dave Jones:** It saves it internally and then you can actually update it later. So, unfortunately, it only has like a 3 seconds is the minimum log time and then you can put in a custom command there to actually do it.

**Dave Jones:** So, let's actually select that. And one point logged, 3 seconds later, it should two points logged. There we go. So, it's actually logging those values and I'll just put my fingers on here, just give a bit of a whirl there.

**Dave Jones:** Unfortunately, yeah, once every 3 seconds. I'm not sure what the limitation is there. GPIB is much faster than that. It is capable of going faster. So, and what I'm going to do now is actually disconnect the ethernet cable and see if it just keeps on logging.

**Dave Jones:** Okay, it's stopped updating, of course, cuz it can't actually connect to it. So, I'll do some more wiggle, wiggle, wiggle, yeah, on the connector to just a vary the values a bit and then I'll reconnect it and then we'll download the data.

**Dave Jones:** I haven't tried this yet. I'm assuming it can data log internally. So, the Kiss module is still connected into the instrument, but the ethernet cable's disconnected. And I'll plug it back in.

**Dave Jones:** So, let's see if it can just live connect like that. Let's see if it updates. There it is, 42 points logged. Yep, I think it kept going. All right, beauty.

**Dave Jones:** Let's just go directly over to graphs. Aha, there it is. That's what I had there and then you can select your different logs and there it is. This is where I pulled it out, somewhere in here and I left it for a bit and then I started to fiddle around with it some more.

**Dave Jones:** So, there you go. We've done that and then we can save that to a CSV file for further play. So, that's kind of neat. It's got a like a building autonomous data logger.

**Dave Jones:** Unfortunately, it's a bit limited in terms of you know, data capture. I don't know why 1 second would be really handy. Oh, it's saved it as a HTM. I thought it was a uh CSV.

**Dave Jones:** See what we get. There we go. Raw raw data. HTM. No problem. You can copy and paste that over to uh straight into Excel or your favorite spreadsheet. So, that's very cool.

**Dave Jones:** You can just uh convert any old GPIB instrument into a web-connected interface. Now, of course, this web interface is very cool, but ultimately, you can only send these single uh commands like just a one-off uh type command.

**Dave Jones:** You can't sequence anything. Doesn't have any scripting or anything like that. But, uh-huh, it has a Telnet interface down here, which allows you to uh write your own programs, write your own scripts in any language you want that supports a Telnet interface, which is like a virtual uh serial port interface to the thing.

**Dave Jones:** And the designer, Steve Hendricks, actually uh told me about some a program that I uh one of his customers has already written. And here it is. It's the GPIB Telnet data logger.

**Dave Jones:** Uh I'll provide a link in uh down below for it. And here it is connected to the instrument. I've had it running for a a while here, and I'm just measuring like uh noise.

**Dave Jones:** So, this is my new Keysight 7 1/2 digit DMM, and this is like the drift on uh warm-up. And you can see that. So, it's actually logging, and there's no uh this particular logging application, I think, like limits it to 1 second.

**Dave Jones:** But, in theory, you can write your own applications that sample it as fast as the GPI bus will allow. So, you can use any programming language you want. So, it's just like having that uh PCI or USB GPIB interface with the drivers and then uh you know, from the likes of National Instruments and other manufacturers that then talk to, you know, LabVIEW, LabWindows, CVI, and and Visual Basic,

**Dave Jones:** and all any program you like that has a driver available that actually supports that. And this Telnet interface, and it just works. I didn't have to set anything up.

**Dave Jones:** Fantastic. So, there you go. You can write your own scripts and everything. I'm sure all the script kiddies out there can, you know, whip up a a program in no time to talk through a Telnet interface.

**Dave Jones:** Winner. And of course, you should be able to connect using any simple terminal program as well, as long as it supports uh Telnet. So, I'm using Tera Term here in this particular case.

**Dave Jones:** So, let's go in here. Telnet unspecified IPv4 and bingo, we're in like Flynn. And then we can just send commands up here. Here we go. Send to this process.

**Dave Jones:** Boom. We're in. Joshua. Damn. Now, unfortunately, I couldn't get the screen the HP-GL screen capture thing working with my HP dynamic signal analyzer. I've tried all sorts of things and I just cannot get it to capture it.

**Dave Jones:** So, I don't know if it's something is particular with my DSA. I I haven't got the time at the moment to try and get that, but suffice it to say that you can actually if your product supports HP-GL output or a bitmap printer type output, you can actually capture that.

**Dave Jones:** So, that's really cool for old-school instruments like this DSA. If you can actually get a screen capture, since got like a 3 and 1/2 inch floppy on it and things like that.

**Dave Jones:** And so, old-school storage like that which still, you know, is not great these days to try and get working. And if you can capture get screen captures to put in documentation and things like that, absolutely fantastic.

**Dave Jones:** But unfortunately, I can't get it working, but I'm sure it does work. Uh Steve's got it on his website and you like screen captures and things like that. I'm just probably doing something dumb.

**Dave Jones:** If I do get it working, I might update you on the uh second EVBlog 2 channel. And you can potentially configure like a screen capture command in here a GPIB uh command in there.

**Dave Jones:** And then when you're in the capture part, you can just go screen capture, it'll execute that, and it will extract the file out, and then you go over to graphs here, and you should be able to actually select your bitmap or HPGL uh file over here, but as you can see, it didn't work.

**Dave Jones:** It's just blank. And here's an example of the extra resolution I was telling you about. I've got my ancient but awesome, still almost unmatched these days, done an awesome teardown video of this.

**Dave Jones:** Um it's really fascinating. Anyway, Keithley 617 programmable electrometer, only four decimal places here, but have a look over there. We've got some extra digits on there. Let's see if we get There we go.

**Dave Jones:** 102. There you go. So, there's some decent extra resolution to be had from your instrument here. So, there you go. That's really worthwhile. Just that alone to get extra resolution out of instruments like this.

**Dave Jones:** So, anyway, I think that's very cool and well worth the money. Uh if you're into old instruments like this, I've done an example of um I don't have it anymore.

**Dave Jones:** Sold it on eBay, but an old uh HP multimeter that you can actually extract an extra digit of resolution from it if you actually got the reading over the GPIB.

**Dave Jones:** So, you know, like valuable stuff like that. So, you turn like a a 7 and 1/2 digit meter into an 8 and 1/2 digit meter. Not all meters are like this, of course.

**Dave Jones:** If you extracted it over the GPIB instead of just on the uh display. So, anyway, I think that's pretty cool concept. It simply just works. I've been playing around with it, and there there's been a few times where it's um like it doesn't respond and things like that if I actually uh change like um modes on the like GPIB modes and addresses and stuff like that, and it

**Dave Jones:** kind of gets mixed up, and not so much locked up if you like treat it wrong and stuff like that. But once if you got the right address and everything works, um then it's it's just it works great.

**Dave Jones:** So, I'm I'm quite impressed by this thing. I think it's really quite a neat thing and it's a well worth having if you got um some old instruments like this.

**Dave Jones:** So, anyway, I'll put in a link uh down below and uh you can buy it on eBay or maybe directly from the website if the website gets back up and running, but hope you liked that.

**Dave Jones:** If you did, please give it a big thumbs up and as always can discuss down below. Catch you next time.
