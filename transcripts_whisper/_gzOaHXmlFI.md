---
video_id: _gzOaHXmlFI
title: EEVblog #119 - Renesas Devcon Day 3
url: https://www.youtube.com/watch?v=_gzOaHXmlFI
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 24, "2": 36, "3": 56, "4": 88, "5": 103, "6": 120, "7": 137, "8": 146, "9": 164, "10": 186, "11": 196, "12": 212, "13": 231, "14": 258, "15": 284, "16": 298, "17": 311, "18": 344, "19": 360, "20": 379, "21": 429, "22": 456, "23": 476, "24": 495, "25": 514, "26": 530, "27": 548, "28": 561, "29": 574, "30": 585, "31": 597, "32": 613, "33": 625, "34": 635, "35": 650, "36": 661, "37": 677, "38": 691, "39": 708, "40": 725, "41": 741, "42": 783, "43": 812, "44": 843, "45": 865, "46": 893, "47": 916, "48": 945, "49": 975, "50": 1007, "51": 1033, "52": 1064, "53": 1091, "54": 1106, "55": 1125, "56": 1141, "57": 1157, "58": 1171, "59": 1185, "60": 1201, "61": 1217}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Well, it's Wednesday morning and the conference is actually closed down the exhibition hall, but it's just getting started here. Check it out, 8.30am, there's 12 different things happening.

**Dave Jones:** At 8.30, there's four labs and eight lectures. It's just crazy. And 6.30pm dinner tonight with James Meese, the editor of Popular Mechanics magazine. Everyone's going to be turning up to that, but it just goes all day. It's unbelievable. Well, I'm sure glad these signs are here.

**Dave Jones:** I almost forgot from 12.30pm to 1.15pm today, they've got the general manager of the Global MCU Business Unit, the head honcho himself out here. That's why Renesas are taking this so seriously. They're sending out the man that regular Joe Bloggs can sit and ask questions of the man.

**Dave Jones:** I love it. Good morning, everybody. Those of you who aren't morning people, morning, everybody. This is A19C, super nuts with free software. My name is DJ Glory. I'm a senior engineer at Red Hat. I work in the Global Engineering Services group. We do primarily embedded systems, cross-developers, etc.

**Dave Jones:** So what does free software mean? A lot of people talk about free software, and a lot of people actually know specifically what it means. And they think, well, it's not free because I can't do everything I want to do with it, it's not free because they charge me for it.

**Dave Jones:** It's not entirely about what the user wants. Free software is about what the software wants. The software wants to be free. And by free, I mean there are certain freedoms that the software grants to the users. Free software is about making sure that those freedoms are maintained.

**Dave Jones:** For starters, free software means that you have the freedom to run the program for any purpose. You can't write a piece of software and say we can only use it the way it's going to be, we can only use it in these countries,

**Dave Jones:** we can only use it for these purposes. You can't compete with us with our own software. You have the freedom to run the software for any purpose that you want. You have the freedom to study how the program works and change it to make it do what you want.

**Dave Jones:** So if the software doesn't fit into your needs, you can make it fit into your needs. You have the freedom to redistribute copies to help your neighbor. Now, in the free software world, we talk about neighbors, but who are your neighbors in your business?

**Dave Jones:** They're your customers, your suppliers, your partners. Those are your neighbors. The ability to share your software and the tools you use with them allows you to work together more efficiently. And finally, the freedom to distribute copies of your modified versions to others. So if you get something,

**Dave Jones:** you have not only the option to enhance it to fit with your business practices, but then you can share it with your partners so that they have the same business practices and the same extensions. These lectures are so hectic. I'm glad I got my personal printed itinerary.

**Dave Jones:** And then you don't know where you got to go. It's like one of 16 different lecture or lab rooms. But luckily, on the back of your badge, you've got your little map showing you where to go. It's brilliant. I love it. We're almost ready for the next session.

**Dave Jones:** People are lining up, checking out the board to see what's in there. Aha, just in time. Found it. Open hardware with open tools. I love open hardware. DJ Delore is giving the lab. It's going to be a hands-on lab where we can muck

**Dave Jones:** around with open source hardware tools. Well worth checking out. Let's go. We've got some hardware to play with. We've got CAN, the micro board, LCD. And I think we're going to do example apps using uh all open source tools. And there's DJ. He's getting ready.

**Dave Jones:** He's nervous. Smile for the camera. It's all going to blow up. And that would be good. And this is open source hardware. This is open hardware. Open hardware. Excellent. Slightly different concept. With open source software, it's people sharing one to zero. With open hardware, it's more of a well you can't

**Dave Jones:** share the hardware. What you do is you share the design files that go with it. So people will publish their schematics and their layout and let other people make the same board and program the board. All of the specs for the boards are going to be published so that people who want to play

**Dave Jones:** with it can play with it. And this lab is slightly different from other labs you may have gone to. This is more of a guided tour of the state-of-the-art free software for EDA. Mm-hmm. I'm going to bet money that we're going to put them on zero, one, two, three.

**Dave Jones:** Yeah. All the software on the laptop you're using right now is 100% free software. No such thing. The question of libraries just came up and I'll talk about that when we work. This suite comes with a collection of symbols and the layout editor comes with a selection of

**Dave Jones:** footprints. And we try to cover most of the common things. We like to follow the IEC guidelines for what they're named and which ones get in there. But in our experience, nearly everybody who's putting together a circuit is going to be working with something that's different.

**Dave Jones:** So we assume that as part of your learning experience, you will learn how to create new symbols and footprints. And they're created right within the tool itself. You just draw them and save them. So we don't try to have a 100% complete library because that's a lot of effort and people

**Dave Jones:** are going to have to do their own thing anyway eventually. And now all the sources are here? Wiki and timer? Yep. If you open that, you'll see all the sources. It was my whole development director. I just dumped it in. There's probably some other things in there.

**Dave Jones:** Show ship linky board. Did it work? Oh, there it is. Pretty fancy. Look, it works. All with open source. Winner. All right, I guess I'm sixth then, huh? Oh, goodness. Oh, Starbucks and iTunes. I have two. Oh, well, what if you haven't got iTunes for it?

**Dave Jones:** I gave my lifeline to the Starbucks. Thank you for attending. I hope you enjoyed experiencing the free software alternative for e-games. Who liked this? At least two days. I hope you weren't having to use a touchpad. No, no, no, no. Two days? At least two days?

**Dave Jones:** Actually, I did this at night over the course of about two weeks. I think somebody's going to look this up. Oh, that stuff's available. Those parts and all that stuff is available. And that was designed completely? This was designed 100% with free software, GDED PCB layout,

**Dave Jones:** and I'm doing all the programming using GCC. This is my equivalent of the RX62N development board. Very nice. Is it a four layer? This is a four layer board manufactured in Germany. It uses 6-6 rules, so nothing out of the ordinary. I used strictly prototyping surfaces.

**Dave Jones:** Wasn't that expensive, and I bought all the parts through DigiKey, except for the 6-2N itself, which I got from Rexis. Was there anything you did specifically for this company in Germany to make it work? No. I had the design rules in PCB set for their design rules, so they wouldn't allow me,

**Dave Jones:** and I do do design rule checking, but if I'm doing something in my basement, I have to adjust the edges to compensate for undercutting. And when I do paste, the paste layer that comes out, it was actually post-processed off of this. For each pad, paste layers are the size of the pad, and I shrink them down by certain amounts

**Dave Jones:** based on the geometry of the pad and some other rules that I might throw in in order to move things around. And also, if you look really, really carefully at the bottom, you can see that where the traces hit pins, they flare out.

**Dave Jones:** Those teardrops are added after the fact. It's not something I do in PCB. It's all done in a post-process. So on the Gerbers? No, on the PCB itself, the .PCB, it takes one, generates another one that has all of the extra things in it.

**Dave Jones:** But I don't want to edit it with all that extra stuff, and I want to edit the original. So you can see the teardrops in the Gerber file? You can see them in the Gerber file. You can actually edit the final board after the post-processing,

**Dave Jones:** run design rule check again, and make sure that the post-processing didn't change, you know, violate any of the design rules, then generate your Gerbers and send it out. So that's all done in PCB, you're saying? The post-processing? I wrote a script. A script, okay.

**Dave Jones:** That the PCB uses, it interprets a little language internally. So what I do is I do my own edits and save it, and then I have a script that runs PCB in batch mode with all of these other commands to do the extra steps that I want and saves it under a different name.

**Dave Jones:** Okay. And then the Makefile then goes and invokes it, and uses the command line options to export the Gerbers. Instead of using the GUI like you guys did, it generates all the Gerbers, all the photorealistic stuff, all the EPS, all the webpages. It's all done in the Makefile.

**Dave Jones:** So I save my copy, and I type Make, and boom, everything happens. It takes about five minutes to run through the whole mess. Okay. And then all the files are ready there. The tarballs are sent out, et cetera, et cetera, et cetera, all done.

**Dave Jones:** Very nice. Can you do it? Can you do a plane before, and then have it move to the other? The way you do planes in it is you draw polygons. We don't do the inverse planes like some people do, because some fabs don't like that.

**Dave Jones:** So we do it with polygons. It allows you to do split planes as well. You draw a big rectangle over your board, and then you grab the thermal tool, and you just go click, click, click, click, click, and it changes to one of the eight different types of thermals that we support.

**Dave Jones:** Or you can make solids if you're doing all the switching power supplies in here also. Do you see JIDA being involved with the open source hardware, the new open source hardware stand? We're trying to promote the idea that if you're making open hardware,

**Dave Jones:** it's not really open if the tools you need are not themselves open. Very true. Now, KiCad, JIDA, you know, we kind of don't really mind which one you use as long as you use something. But if you use a proprietary package... Like Eagle.

**Dave Jones:** Like Eagle or OrCAD or Altium to produce a design, is the design really open? Granted, you can use it for whatever you want, but you can't change it unless you can buy the tools. So we're trying to encourage the open hardware specs, the initiatives,

**Dave Jones:** to specify that open hardware is not truly open unless the file formats are open as well. At least if you can interpret the files and do something with the files, as opposed to having a completely closed file system, we'd like them to use open source ETA tools.

**Dave Jones:** But at the very least, you need to be able to work with the ETA files. And how much does JIDA cost? JIDA costs nothing! Completely free! Maybe a penny if you have to pay for your ISP. How do you make your money? Volume!

**Dave Jones:** Last year, I couldn't imagine that the Windows 10 technology would work with NVCA. They are straightaway my enemies. But now... So there are ones for the consolidated computers with no key. In consolidated computers, there are two similar but different types. You can buy Aurex Type-A, B850 Type-A types.

**Dave Jones:** Then you, the customer, have to change the driver for that. And I want to avoid that kind of cost for the customer. Because of that, I'm now ordering my team to unify the Vector as a platform as soon as possible. For 14 hours, I'm confident that we will open it.

**Dave Jones:** And I believe this kind of activity is only possible for consolidated apps. In other words, nowadays, many central network suppliers are unqualified. But, for example, STMicro and TS will not be able to do it. They have to differentiate themselves among the many ARM suppliers.

**Dave Jones:** But former NVCA electronics and former Windows 10 technology can do it. For real world consolidated computers. And only we can, I believe, be able to offer this kind of value-added to you, to my customers. I have an inclination to forget the best thing in the past.

**Dave Jones:** So for me, the most high and big satisfaction is Aurex, release of Aurex. With no kidding, to prepare the platform-based design, I have put so many designs, so that new innovations, internal innovations, so that we will be able to catch up the customer's various requirements.

**Dave Jones:** So Aurex is the most impressive one. This is an official answer. And in my career, as I explained, I have started from 8-bit MCU design. And during my career, I once joined a joint program with Intel. And at that time, Intel had a broad product portfolio,

**Dave Jones:** including the MCUs such as the 1861 or 1896. Maybe the 4000 will remember this name. And for me, the internal design designed by Intel for the 1851 was a big surprise. At that time, their design was very aggressive, using new technologies. And in my career, the 1851 design, of course, that was done by myself,

**Dave Jones:** but that was the most impressive design for me. This is a kind of a non-product memory for next generation. And the mechanism fitted to remember the data is quite different from the conventional flash technologies. It is based on the magneto-electronic effect. And so the Lunasat, and before it was the Lunasat technology,

**Dave Jones:** was the leader of the M1. And also the NEC electronics in R&D level, they brought themselves into the next generation network structure. And now we are preparing the M1 health technology. But to be honest, my personal impression is M1 is very attractive. But many people think that it is just a replacement of flash.

**Dave Jones:** Then, for flash, for example, our proprietary technology, Core.Lunasat, has already confirmed to have a high scalability to 5 processors, to 49 or 28 bitnam. Then, for M1, now I'm looking for a killer application for M1. For example, M1 is a non-product memory, but at the same time, the read-write cycle is very fast.

**Dave Jones:** Meaning that M1 is a non-product memory, and at the same time, a RAM, conventional RAM. So this kind of universal feature will give some new innovative functionality. But so far, the Lunasat technology and also NEC electronics were not successful to find out this kind of technology.

**Dave Jones:** And the Wednesday night dinner event has, once again, they've transformed it into a lovely sit-down dinner table event. What I really want to do tonight is obviously dive into the area called viewer-involvement, embedded design, ubiquitous computing, and look at the trends that are coming.

**Dave Jones:** So many of you are working in different areas of this. See how these things are coming together in a way that will reshape our lives. So the first question is, can we define ubiquitous computing? Some people would say the first ubiquitous computer is our more or less current versions of smartphones.

**Dave Jones:** Other people would go a little farther and look for first-generation PCs. Okay, how many people have one of these? But I think the first networked ubiquitous computer was the ATM. The first one was introduced in 1969 at a chemical bank on Long Island.

**Dave Jones:** I think their ad said something like, on Monday morning, our bank will open and never close again. And that's basically what happened. And Donald Wetzel, who more or less invented the ATM, he knew exactly what he was doing. He knew exactly what this meant.

**Dave Jones:** It wasn't just a better way to do banking. This was the first machine that was going to teach people how to interact with an intelligent device. And it's hard to remember now, but it was a real learning curve to get people comfortable with the machine actually handling their money.

**Dave Jones:** You know, if you think about it, all the technologies they're talking about, they may seem to offer all kinds of benefits, but they have trade-offs, too. Imagine, there was a time, Imagine, there was a time, when if you wanted your money, you'd walk into a bank,

**Dave Jones:** and a person would look you in the eye, often reading your name, and say, how can I help you? The entire transaction was organized around your needs, what you thought, you, the questions that you had. In contrast, going and interacting with an ATM means

**Dave Jones:** you have to accept the menu and the paradigm that the machine imposes on you. We take it for granted now, but it was a challenge for some people as recently as the mid-to-late 80s, I remember in New York, there were still banks advertising,

**Dave Jones:** well, you know, at our bank, you can still talk to a real person. I remember looking at my wife and going, I don't want to talk to a real person. Interesting little-known renaissance fact time. Third biggest semiconductor manufacturer in the world. Intel up here,

**Dave Jones:** fighting it out with Samsung, and then there's renaissance. Number three, who knew? Microsoft Mechanics www.microsoft.com www.microsoft.com
