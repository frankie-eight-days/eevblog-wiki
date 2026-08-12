---
video_id: VqDljuHjPrY
title: EEVblog 1684 - Awesome Logging Software:  Test Controller
url: https://www.youtube.com/watch?v=VqDljuHjPrY
source: youtube-asr
timestamps: {"0": 0, "1": 9, "2": 23, "3": 31, "4": 41, "5": 54, "6": 65, "7": 78, "8": 95, "9": 113, "10": 126, "11": 135, "12": 154, "13": 167, "14": 178, "15": 191, "16": 202, "17": 212, "18": 226, "19": 241, "20": 256, "21": 271, "22": 281, "23": 296, "24": 304, "25": 316, "26": 327, "27": 336, "28": 351, "29": 363, "30": 373, "31": 384, "32": 399, "33": 409, "34": 419, "35": 429, "36": 437, "37": 449, "38": 457, "39": 467, "40": 481, "41": 489, "42": 501, "43": 512, "44": 521, "45": 531, "46": 544, "47": 555, "48": 564, "49": 579, "50": 588, "51": 599, "52": 613, "53": 623, "54": 634, "55": 644, "56": 655, "57": 664, "58": 674, "59": 688, "60": 699, "61": 711, "62": 724, "63": 738, "64": 752, "65": 762, "66": 780, "67": 798, "68": 813, "69": 826}
---

**Dave Jones:** Hi, I want to show you a very cool program uh that can log data from a whole bunch of different multimeters and instruments. And uh it's it's really great.

**Dave Jones:** And they just released support for the uh new EEV blog BM2257 available over on evblog.store. There it is. And yes, you can also get the uh PC serial interface for it as well.

**Dave Jones:** I sell that as well. It's an optical uh serial interface here. So, it's just got the uh leads like that. And you know, you can see the two little leads down in there.

**Dave Jones:** Um, and this supports several uh Briman uh meters, including the old 257 as well. You can see there's a little cutout in there, so you can't get it around the wrong way.

**Dave Jones:** Anyway, um serial interface for this thing. And of course, you can actually get download the Brimman software for this, but it's not that great. It's, you know, really old school um kind of um stuff.

**Dave Jones:** But there's this new program called test controller and we're going to take a look at this because it's very cool. So I'm logging main's voltage at the moment. So basic Oh damn, I just screwed it up.

**Dave Jones:** I turned it off. Oops, I've just been logging. But you hold down the whole button and you get the com button there and we can read the uh data from Oh, let's see what happens when the data drops actually.

**Dave Jones:** Anyway, let's go over to the uh program. Um, it's called Test Controller and it's from an EVlogger forum user HKJ who runs the uh I've never been able to pronounce this, leg-info.dk.

**Dave Jones:** It's a fantastic website. Um, got a whole bunch of like multimeter reviews. Let me show you. It's been an awesome resource for a long time that has like like tons of um like it says web page about batteries, chargers, and flashlights, but there's tons of test very detailed test equipment reviews.

**Dave Jones:** So, if you like old school, you know, HTML format web page, multimeter reviews, so DMM information and reviews. Um he's reviewed uh the Brimman's ones, but like tons of different instrument reviews and things like that.

**Dave Jones:** It just goes on and on and on and on. It's fantastic. has reviewed an absolute ton of meters here. Um, it's just it's crazy, right? So, there's the 121GW.

**Dave Jones:** So, if we go into that, uh, for example, you know, he's got really detailed breakdowns of everything, very comprehensive reviews, very cool stuff. So, yeah, tests a ton of, um, you know, stuff and everything and uses the app and does, you know, tear down photos of all of these products.

**Dave Jones:** So, definitely check out the web. Even if you're not interested in this login program, check out uh his website down below. Absolutely fantastic. Um so he's on the EV blog forum and you can get support for this software on the EV blog forum.

**Dave Jones:** So it's up to 161 pages of support. So started this uh in 2020 and um it supports a ton of different uh products like here is the current list.

**Dave Jones:** I I think he I think he's keeping it up to date and here's all the instruments that it supports. very very impressive. So um yeah and he fully supports the program and you can even add your own stuff as well.

**Dave Jones:** I can believe you can do it through like a config file and stuff like that. Um so yeah so you can fairly easily I believe add your own uh stuff just by like having a scripty file um kind of thing.

**Dave Jones:** But anyway, this test controller program here um it took me a little a few minutes to figure out it was actually running um on Java. So it works on Windows.

**Dave Jones:** I'm running Windows 10 here. It works on Linux and uh Mac as well, but you have to have Java installed uh to actually um do it. So yeah, anyway, uh there's heaps of documentation and stuff and heaps of commands and things like that.

**Dave Jones:** So very very impressive. So it's absolutely great. It's got histogram and charting and all sorts of stuff. And uh we're going to try it with the 2257 here. So you can just download it uh down here.

**Dave Jones:** So um yeah, let's go. Now the first thing is when you download it uh you just get uh these files here and this jar file you have to actually um unzip that um it's a compressed file and you have to unzip it into the same subdirectory.

**Dave Jones:** I made this mistake I extracted into a directory above this um but no all these so it extracts out all of these uh subdirectories here. So yeah that that just wasn't clear to me and the program ran but it wouldn't give me various options because it couldn't find the DLS or whatever.

**Dave Jones:** Um, so yeah, um, maybe I didn't RTFM enough, but uh, yeah, just be aware of that you have to unzip um, this uh, uncompress this JAR file into the same uh, subdirectory.

**Dave Jones:** But anyway, you just run testcontroller.bat after you've installed uh, Java. So I just downloaded like the latest um, Java uh, version here for Windows um, 64, but you can get Java for Mac and uh, Linux and other stuff.

**Dave Jones:** So yeah, I don't know what version it needs, but yeah, you just download it and Bob's your uncle. So when you plug in the uh serial interface here, Windows automatically detects that.

**Dave Jones:** It loads up the drivers uh and it appears as a prolific uh PL2303GC serial compport here. And you have to note down that it's actually compport 3. So you have to note down uh that number.

**Dave Jones:** So you just run that batch file and bingo the uh program comes up here like this. Uh when you want to install uh a new product here, here you go.

**Dave Jones:** You just go into load devices here and uh you can just add you can either search sockets down the bottom here or you can just manually select any one of these products and look at these.

**Dave Jones:** Look at all the support. Agyant AMB BK Precision Brimman. So I just manually selected the 2257 there. Um East tester feel ones the flukes um like the fluke 87 for example.

**Dave Jones:** Um I believe like it uses the PO transducer um in there. uh to actually emit high frequency sounds and it sends data via um that. I've never actually tried it myself, but it looks like it supports it.

**Dave Jones:** So, that's kind of cool. Um GW Instant It. So, you can do power supplies. It's not just multimeters, you can do power supplies and a whole bunch of mixers.

**Dave Jones:** Keithley Keysite support red just a ton of support for all the uh power supplies and stuff. It's just Matrix and 01 Roden Schwarz. Look at this. It's just nuts.

**Dave Jones:** Huge Ryol support. Massive Sigant support here. It's just it's crazy, right? I don't know what that spark fund jobby is. TTI, Tektronic support, Tenmar, Unity, right? The whole works.

**Dave Jones:** Absolutely crazy. Anyway, um so what you do is you select your instrument, you go add and uh by default it will not um talk to it. And even if you do scan serial ports up here, that doesn't work in this particular case.

**Dave Jones:** It might work in other cases. This particular case it didn't. So, I had to actually go in there and manually type in COM 3, which we got from uh device manager um you saw before.

**Dave Jones:** And then we can't actually select the board rate. So, I guess it knows what it is based on that um instrument. And we once you enable that uh bingo, physically connect to it over here.

**Dave Jones:** So, there we go. It's connected. You can send um send commands uh to it if you really want to do it manually. But there you go. The current value can just be displayed here.

**Dave Jones:** Small or large text like that. Um, now, uh, table. I couldn't figure out how to get this table working. I thought like it just didn't log up. Didn't um, start logging by default.

**Dave Jones:** There was no log button. Here we go. So, you can change it like the samples and stuff and the slope time and things like that, but I couldn't figure out how to log it.

**Dave Jones:** I realized it's over on the commands page over here. You had to start logging over there. Once you start logging, then you'll get the options for the tables and the charts and the histograms and everything else.

**Dave Jones:** And uh you can see so that's its current value but it's just like adding to the table here. So if we go down here continually so I've got it set to once per second it's going to like this and bingo it gives us our chart.

**Dave Jones:** So there's the main frequency there and you can see how it's dropped out here. This is where I disconnected it uh before and you can actually set that uh value.

**Dave Jones:** You can set that dropout value over here in configuration. So you can do this timeout handle in here. So you can return a zero or you can return an nan depending on what you know you might want to export the data to some other program.

**Dave Jones:** So that's very handy like that and uh timeout delay one sample. So um yeah that's that's very handy. So you can get so there's our chart and of course we can export all of this uh table stuff.

**Dave Jones:** We can export it. I think it just ex exports it to uh CSV I think. So yeah fantastic. So you can import it into other programs if you want to do some more advanced charting.

**Dave Jones:** Um the scales over here the uh you can set scales for the chart. I found that the um auto um scale here didn't do it. Um it just put zero to 240.

**Dave Jones:** It did scale it but then it like it wouldn't like fit it. It wouldn't like fit the scaling. So I just manually So I disabled that and manually selected minimum 235 to 245 volts there like that.

**Dave Jones:** Um so yeah that's it's working. It's working fantastically. I really like it. You can see if there's any data dropouts. It's really obvious. It goes to that known value as I said.

**Dave Jones:** And I really like this histogram function. Look at this right at at one point like we got what one or two couple of samples over here at like 245 volts.

**Dave Jones:** It jumped up, you know, for a split second or whatever a couple of times, but most of the values are um are basically in here. It'd be nice if you could like cursor over those and actually like, you know, pop up with the value on there.

**Dave Jones:** that would be a really nice touch. But, you know, I'm I'm really um quibbling about this. And the scales are exactly the same as what we um had over there.

**Dave Jones:** So, um yeah, I love the histogram function. I love the charting function. It's really good. And then we can get like minimum and maximum stuff and average values. Um slope, I haven't played with any of that.

**Dave Jones:** The math stuff, I haven't even looked at that yet. Add defined. It looks like you can do your own formulas. Look at this. Oh, wow. rolling sum, total sum, slope, standard deviation, min, max, change, delta.

**Dave Jones:** Wow. Dropout filter, digital, you got filters, and all sorts of things. Wow, that looks very advanced. I won't go into that in this uh video. And it can handle multiple devices as well.

**Dave Jones:** So, you can actually remap them um over here. So, you can add so if you got, you know, 10 different BM2257 multimeters, you can add 10 of them, you know, 10 serial ports.

**Dave Jones:** And then you can like assign them um handles and names and stuff like that. Um so that's you know serial numbers. So that's that's really cool. So yes, I'm very impressed with Test Controller.

**Dave Jones:** Well done. Hats off. Big thumbs up to Test Controller. Um try it for your instrument. You've probably got an instrument that is supported by Test Controller. I think it's great.

**Dave Jones:** And um support over on the EV vidlog forum. I'll link in the forum thread down below where you can uh discuss it. if you got bugs, improvements, you want stuff added.

**Dave Jones:** And as I said, um you can actually add your own stuff, too. And it can support massive um like data files, login for long periods of time and stuff like that.

**Dave Jones:** And um yeah, you can set for different uh login intervals and things. And you can do all sorts of a ton of stuff with this program. I probably haven't even uh scratched the surface of, you know, some more like advanced stuff that you can actually uh do for this.

**Dave Jones:** Um, nice comprehensive uh documentation and stuff. There's an installation uh guide like this. Here you go. Installing Java and OS. Um, yeah, dislocations used. So, yeah, I should have read that before.

**Dave Jones:** It took me five minutes of around to figure out uh what I had done wrong there. Oh, and it's got these different pop-ups. There's a calculator popup. There's a timer alarm popup.

**Dave Jones:** What? I knew there was these virtual generators. There's an FFT view popup. It's got everything, right? This is just This is just nuts. This program, hats off. This is insane.

**Dave Jones:** I am not sure if it's open source GitHuby. Um I don't think so, but um yeah, it's free. Just uh download it and it's fully supported. Um he's very active on the EV blog forum.

**Dave Jones:** I want to know how to get the calculator popup now. Aha, popups. Here we go. There you go. Show all mode popups. Wow. Okay. FFT view popup alarm popup.

**Dave Jones:** So you can set alarms and things. Look at that. So you can set so it'll what? It'll beep at you or something if your multimeter, you know, when you're logging your multimeter, it goes over the over a value or something.

**Dave Jones:** That's great. So much thought has gone into like this program. It's just it really is terrific. We can do parametric sweeping as well. Wow. Okay. Skippy command for PMT57 breaker linear log steps.

**Dave Jones:** Wow. It's got a built-in image viewer as well. Maximum PowerPoint tracking. There you go. Time counter. Count events and time between events. Oh, this is too good. It's not a calculator with buttons.

**Dave Jones:** You've got to uh got to type in the formula. But here Oh, so there you go. And they can stay as pop outs. Yeah, that hats off. This is absolutely fantastic um program and it now supports the BM2257 which is fantastic.

**Dave Jones:** You can get it evblog.store along with uh the serial interface for it. Um but yeah, this supports a ton of instruments. So this is great. Um highly recommended. Hats off.

**Dave Jones:** So awesome work to legit liy.info.dk for this awesome program. link it in down below. Check it out. Catch you next time. [Music]
