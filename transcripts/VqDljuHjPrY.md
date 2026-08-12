---
video_id: VqDljuHjPrY
title: EEVblog 1684 - Awesome Logging Software:  Test Controller
url: https://www.youtube.com/watch?v=VqDljuHjPrY
source: youtube-asr
---

**Dave Jones:** Hi, I want to show you a very cool program uh that can log data from a whole bunch of different multimeters and instruments. And uh it's it's really great. And they just released support for the uh new EEV blog

**Dave Jones:** BM2257 available over on evblog.store. There it is. And yes, you can also get the uh PC serial interface for it as well. I sell that as well. It's an optical uh serial interface here. So, it's just got the uh leads

**Dave Jones:** like that. And you know, you can see the two little leads down in there. Um, and this supports several uh Briman uh meters, including the old 257 as well. You can see there's a little cutout in there, so you can't get it around the

**Dave Jones:** wrong way. Anyway, um serial interface for this thing. And of course, you can actually get download the Brimman software for this, but it's not that great. It's, you know, really old school um kind of um stuff. But there's this

**Dave Jones:** new program called test controller and we're going to take a look at this because it's very cool. So I'm logging main's voltage at the moment. So basic Oh damn, I just screwed it up. I turned it off. Oops, I've just been logging.

**Dave Jones:** But you hold down the whole button and you get the com button there and we can read the uh data from Oh, let's see what happens when the data drops actually. Anyway, let's go over to the uh program.

**Dave Jones:** Um, it's called Test Controller and it's from an EVlogger forum user HKJ who runs the uh I've never been able to pronounce this, leg-info.dk. It's a fantastic website. Um, got a whole bunch of like multimeter reviews. Let me show you. It's been an

**Dave Jones:** awesome resource for a long time that has like like tons of um like it says web page about batteries, chargers, and flashlights, but there's tons of test very detailed test equipment reviews. So, if you like old school, you know,

**Dave Jones:** HTML format web page, multimeter reviews, so DMM information and reviews. Um he's reviewed uh the Brimman's ones, but like tons of different instrument reviews and things like that. It just goes on and on and on and on. It's

**Dave Jones:** fantastic. has reviewed an absolute ton of meters here. Um, it's just it's crazy, right? So, there's the 121GW. So, if we go into that, uh, for example, you know, he's got really detailed breakdowns of everything, very comprehensive reviews, very cool stuff.

**Dave Jones:** So, yeah, tests a ton of, um, you know, stuff and everything and uses the app and does, you know, tear down photos of all of these products. So, definitely check out the web. Even if you're not interested in this login program, check

**Dave Jones:** out uh his website down below. Absolutely fantastic. Um so he's on the EV blog forum and you can get support for this software on the EV blog forum. So it's up to 161 pages of support. So started this uh in 2020 and um it

**Dave Jones:** supports a ton of different uh products like here is the current list. I I think he I think he's keeping it up to date and here's all the instruments that it supports. very very impressive. So um yeah and he fully supports the program

**Dave Jones:** and you can even add your own stuff as well. I can believe you can do it through like a config file and stuff like that. Um so yeah so you can fairly easily I believe add your own uh stuff

**Dave Jones:** just by like having a scripty file um kind of thing. But anyway, this test controller program here um it took me a little a few minutes to figure out it was actually running um on Java. So it works on Windows. I'm running Windows 10

**Dave Jones:** here. It works on Linux and uh Mac as well, but you have to have Java installed uh to actually um do it. So yeah, anyway, uh there's heaps of documentation and stuff and heaps of commands and things like that. So very

**Dave Jones:** very impressive. So it's absolutely great. It's got histogram and charting and all sorts of stuff. And uh we're going to try it with the 2257 here. So you can just download it uh down here. So um yeah, let's go. Now the first

**Dave Jones:** thing is when you download it uh you just get uh these files here and this jar file you have to actually um unzip that um it's a compressed file and you have to unzip it into the same subdirectory. I made this mistake I

**Dave Jones:** extracted into a directory above this um but no all these so it extracts out all of these uh subdirectories here. So yeah that that just wasn't clear to me and the program ran but it wouldn't give me various options because it couldn't find

**Dave Jones:** the DLS or whatever. Um, so yeah, um, maybe I didn't RTFM enough, but uh, yeah, just be aware of that you have to unzip um, this uh, uncompress this JAR file into the same uh, subdirectory. But anyway, you just run testcontroller.bat

**Dave Jones:** after you've installed uh, Java. So I just downloaded like the latest um, Java uh, version here for Windows um, 64, but you can get Java for Mac and uh, Linux and other stuff. So yeah, I don't know what version it needs, but yeah, you

**Dave Jones:** just download it and Bob's your uncle. So when you plug in the uh serial interface here, Windows automatically detects that. It loads up the drivers uh and it appears as a prolific uh PL2303GC serial compport here. And you

**Dave Jones:** have to note down that it's actually compport 3. So you have to note down uh that number. So you just run that batch file and bingo the uh program comes up here like this. Uh when you want to

**Dave Jones:** install uh a new product here, here you go. You just go into load devices here and uh you can just add you can either search sockets down the bottom here or you can just manually select any one of

**Dave Jones:** these products and look at these. Look at all the support. Agyant AMB BK Precision Brimman. So I just manually selected the 2257 there. Um East tester feel ones the flukes um like the fluke 87 for example. Um I believe like it

**Dave Jones:** uses the PO transducer um in there. uh to actually emit high frequency sounds and it sends data via um that. I've never actually tried it myself, but it looks like it supports it. So, that's kind of cool. Um GW

**Dave Jones:** Instant It. So, you can do power supplies. It's not just multimeters, you can do power supplies and a whole bunch of mixers. Keithley Keysite support red just a ton of support for all the uh power supplies and stuff. It's just

**Dave Jones:** Matrix and 01 Roden Schwarz. Look at this. It's just nuts. Huge Ryol support. Massive Sigant support here. It's just it's crazy, right? I don't know what that spark fund jobby is. TTI, Tektronic support, Tenmar, Unity, right? The whole

**Dave Jones:** works. Absolutely crazy. Anyway, um so what you do is you select your instrument, you go add and uh by default it will not um talk to it. And even if you do scan serial ports up here, that doesn't work in this particular case. It

**Dave Jones:** might work in other cases. This particular case it didn't. So, I had to actually go in there and manually type in COM 3, which we got from uh device manager um you saw before. And then we can't actually select the board rate.

**Dave Jones:** So, I guess it knows what it is based on that um instrument. And we once you enable that uh bingo, physically connect to it over here. So, there we go. It's connected. You can send um send commands uh to it if you really want to do it

**Dave Jones:** manually. But there you go. The current value can just be displayed here. Small or large text like that. Um, now, uh, table. I couldn't figure out how to get this table working. I thought like it just didn't log up. Didn't um, start

**Dave Jones:** logging by default. There was no log button. Here we go. So, you can change it like the samples and stuff and the slope time and things like that, but I couldn't figure out how to log it. I realized it's over on the commands page

**Dave Jones:** over here. You had to start logging over there. Once you start logging, then you'll get the options for the tables and the charts and the histograms and everything else. And uh you can see so that's its current value but it's just

**Dave Jones:** like adding to the table here. So if we go down here continually so I've got it set to once per second it's going to like this and bingo it gives us our chart. So there's the main frequency there and you can see how it's dropped

**Dave Jones:** out here. This is where I disconnected it uh before and you can actually set that uh value. You can set that dropout value over here in configuration. So you can do this timeout handle in here. So you can return a zero or you can return

**Dave Jones:** an nan depending on what you know you might want to export the data to some other program. So that's very handy like that and uh timeout delay one sample. So um yeah that's that's very handy. So you can get so there's our chart and of

**Dave Jones:** course we can export all of this uh table stuff. We can export it. I think it just ex exports it to uh CSV I think. So yeah fantastic. So you can import it into other programs if you want to do

**Dave Jones:** some more advanced charting. Um the scales over here the uh you can set scales for the chart. I found that the um auto um scale here didn't do it. Um it just put zero to 240. It did scale it

**Dave Jones:** but then it like it wouldn't like fit it. It wouldn't like fit the scaling. So I just manually So I disabled that and manually selected minimum 235 to 245 volts there like that. Um so yeah that's it's working. It's working

**Dave Jones:** fantastically. I really like it. You can see if there's any data dropouts. It's really obvious. It goes to that known value as I said. And I really like this histogram function. Look at this right at at one point like we got what one or

**Dave Jones:** two couple of samples over here at like 245 volts. It jumped up, you know, for a split second or whatever a couple of times, but most of the values are um are basically in here. It'd be nice if you

**Dave Jones:** could like cursor over those and actually like, you know, pop up with the value on there. that would be a really nice touch. But, you know, I'm I'm really um quibbling about this. And the scales are exactly the same as what we

**Dave Jones:** um had over there. So, um yeah, I love the histogram function. I love the charting function. It's really good. And then we can get like minimum and maximum stuff and average values. Um slope, I haven't played with any of that. The

**Dave Jones:** math stuff, I haven't even looked at that yet. Add defined. It looks like you can do your own formulas. Look at this. Oh, wow. rolling sum, total sum, slope, standard deviation, min, max, change, delta. Wow. Dropout filter, digital, you

**Dave Jones:** got filters, and all sorts of things. Wow, that looks very advanced. I won't go into that in this uh video. And it can handle multiple devices as well. So, you can actually remap them um over here. So, you can add so if you got, you

**Dave Jones:** know, 10 different BM2257 multimeters, you can add 10 of them, you know, 10 serial ports. And then you can like assign them um handles and names and stuff like that. Um so that's you know serial numbers. So that's that's really

**Dave Jones:** cool. So yes, I'm very impressed with Test Controller. Well done. Hats off. Big thumbs up to Test Controller. Um try it for your instrument. You've probably got an instrument that is supported by Test Controller. I think it's great. And

**Dave Jones:** um support over on the EV vidlog forum. I'll link in the forum thread down below where you can uh discuss it. if you got bugs, improvements, you want stuff added. And as I said, um you can actually add your own stuff, too. And it

**Dave Jones:** can support massive um like data files, login for long periods of time and stuff like that. And um yeah, you can set for different uh login intervals and things. And you can do all sorts of a ton of

**Dave Jones:** stuff with this program. I probably haven't even uh scratched the surface of, you know, some more like advanced stuff that you can actually uh do for this. Um, nice comprehensive uh documentation and stuff. There's an installation uh guide like this. Here

**Dave Jones:** you go. Installing Java and OS. Um, yeah, dislocations used. So, yeah, I should have read that before. It took me five minutes of around to figure out uh what I had done wrong there. Oh, and it's got these different pop-ups.

**Dave Jones:** There's a calculator popup. There's a timer alarm popup. What? I knew there was these virtual generators. There's an FFT view popup. It's got everything, right? This is just This is just nuts. This program, hats off. This is insane. I am not sure if

**Dave Jones:** it's open source GitHuby. Um I don't think so, but um yeah, it's free. Just uh download it and it's fully supported. Um he's very active on the EV blog forum. I want to know how to get the calculator popup now. Aha, popups. Here

**Dave Jones:** we go. There you go. Show all mode popups. Wow. Okay. FFT view popup alarm popup. So you can set alarms and things. Look at that. So you can set so it'll what? It'll beep at you or something if your

**Dave Jones:** multimeter, you know, when you're logging your multimeter, it goes over the over a value or something. That's great. So much thought has gone into like this program. It's just it really is terrific. We can do parametric sweeping as well. Wow. Okay. Skippy

**Dave Jones:** command for PMT57 breaker linear log steps. Wow. It's got a built-in image viewer as well. Maximum PowerPoint tracking. There you go. Time counter. Count events and time between events. Oh, this is too good. It's not a calculator with buttons. You've got to

**Dave Jones:** uh got to type in the formula. But here Oh, so there you go. And they can stay as pop outs. Yeah, that hats off. This is absolutely fantastic um program and it now supports the BM2257 which is fantastic. You can get

**Dave Jones:** it evblog.store along with uh the serial interface for it. Um but yeah, this supports a ton of instruments. So this is great. Um highly recommended. Hats off. So awesome work to legit liy.info.dk for this awesome program. link it in down below. Check it out.

**Dave Jones:** Catch you next time. [Music]
