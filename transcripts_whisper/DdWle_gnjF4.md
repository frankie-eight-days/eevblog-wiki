---
video_id: DdWle_gnjF4
title: EEVblog #174 - Renesas RX Design Contest Winners
url: https://www.youtube.com/watch?v=DdWle_gnjF4
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 20, "2": 44, "3": 63, "4": 80, "5": 105, "6": 126, "7": 139, "8": 156, "9": 175, "10": 195, "11": 217, "12": 240, "13": 256, "14": 275, "15": 293, "16": 310, "17": 331, "18": 351, "19": 364, "20": 383, "21": 402, "22": 421, "23": 438, "24": 464, "25": 480, "26": 500, "27": 517, "28": 531, "29": 555, "30": 575, "31": 605, "32": 628, "33": 650, "34": 670, "35": 688, "36": 724, "37": 748, "38": 766, "39": 790, "40": 808, "41": 832, "42": 856, "43": 868, "44": 892, "45": 904, "46": 928, "47": 952, "48": 970, "49": 988, "50": 1012, "51": 1036, "52": 1054, "53": 1078, "54": 1096, "55": 1120, "56": 1144, "57": 1168, "58": 1192, "59": 1204, "60": 1228, "61": 1258, "62": 1276, "63": 1294, "64": 1324, "65": 1348, "66": 1366, "67": 1384, "68": 1402, "69": 1426, "70": 1450, "71": 1474, "72": 1492, "73": 1516}
---

**Dave Jones:** Hi, as you may know, I was a judge in the recent Renesas RX Micro Design Contest, and it was one of the biggest design contests in industry history. Over $100,000 in prize money from Renesas and various partners, a whole bunch of partners were involved.

**Dave Jones:** Almost everyone who entered, I think, won a prize. It was absolutely incredible. And Renesas gave away hundreds of these RX62N micro development boards to enter the contest with, and a whole bunch of people did just that. And there were dozens of brilliant, absolutely brilliant

**Dave Jones:** entries. And there were, I wasn't the only judge, there was Maury Wright, who's a fellow blogger, Kent Loman, who actually designed this board, and a bunch of other judges. They tallied all the scores together, and they announced the winners at the ESC, the Embedded

**Dave Jones:** Systems Conference, a couple of weeks ago. And I thought I'd do a very quick video of just highlighting the top three places, because I think they were really good examples of how you can actually enter and win these design contests. So if you plan on entering future

**Dave Jones:** design contests, stick around. I might have a few hints for you about how to do very well and possibly win one of these industry design contests. So let's go through them. The top three winners for the RX micro design contest. See ya! Okay, let's start out by taking a look at the third place winner, Matt Pratt, with the

**Dave Jones:** BrewBot. Now this one is an absolute beauty. It's basically brewing your own beer at home. And he uses the Renesas RX board to control the whole thing, basically in terms of motor control and web interface to control it, and operating system, and the whole thing like

**Dave Jones:** that, which we'll go into. Now, he ticks all the boxes which you need to win these design contests. He's got an excellent video. It's nice and clear, it's concise, it's got audio as well, it shows the operation of the thing, the construction, all sorts of stuff.

**Dave Jones:** So you've got to have a good video to be really in the running for these contests, and he's got that. And he's got the, even though the schematic isn't much at all, but he's got the build materials, he's got the zip file with the source code, so it's all there.

**Dave Jones:** He's met all the conditions of the contest, and he's got excellent documentation. Now, here it is. It's a PDF file, and this is the basic, it starts out with a photo of the device. There it is, there's the Renesas RX board down there, controlling it.

**Dave Jones:** It's got a whole bunch of stainless steel contraptions and chutes for the, all sorts of stuff, and it's all automated motor control and all that sort of stuff from the Renesas RX series board. Now, the thing with these, you always, in the design contest, you always get a big build like this.

**Dave Jones:** Somebody builds something big and impressive looking, and you immediately see it and you go, wow, look at this, you know, how can this guy not win? And, well, it's true, you're going to, if you build something impressive like this, you're really going to be right up there straight

**Dave Jones:** away. But, it's not all about just a fabulous construction. If this, if the Renesas RX series board down here controlling this thing only flashed a few LEDs and turned a few motors and was basically used as a PLD, sorry, a programmable logic controller, a PLC, then

**Dave Jones:** it wouldn't have been very impressive at all, because this is an electronics design contest. So a really big impressive build like this with lots of wood and lots of metal and motors and things that turn and do stuff, that's fantastic. But if you don't do much on the

**Dave Jones:** electronics and or software side, then really you can be left out. You can not win, you may not even place. And he just scraped into third place with this thing. It was a pretty solid third place actually, he didn't just scrape in, but it was an excellent effort

**Dave Jones:** because he had pretty much consistent across the board, the video and the documentation. Now let's take a look at it. He's got a table of contents about this document, it's 23 odd pages long, fantastic, it's detailed, he's got the background of why he's doing it, he's

**Dave Jones:** got the objectives of his thing, it's well written, it's well written in English which is a big deal. Some people just have terrible documentation skills and it comes across very poorly, but not in this case, it's excellent. Safety he's mentioned, he goes into the design

**Dave Jones:** of it, the servos and the solenoids used. Further on down here he details the construction, the materials used, all sorts of stuff like that. And then he's got a descriptive photo of the all sorts of, I don't even know, what's a grist bag, a mash stirrer, I have no idea.

**Dave Jones:** These are all terms used for a mash motor, used for brewing beer. But he's gone to the effort to label all this stuff and that really comes across quite well. And there's more detailed photos, photos are easy to do. When you're documenting your project, make sure

**Dave Jones:** you photograph it and photos are easy to add, they're simple. You just take a photo, a golden rule of any documentation, be it at work or when you're entering contests like this, just snap a photo. A picture tells a thousand words, it really does.

**Dave Jones:** And there's more detailed photos of his complete build. It's very impressive. There's the hopper system that I assume you put the required elements for the beer in there and it tips them out at the required time. Fantastic. But it's not rocket science really.

**Dave Jones:** A controller that just controls a beer bot like this is not overly complicated at all. As I said it's just a PLC, there's this Vero board build down the bottom with just the extra driver circuitry on it. The Renesas RX board does most of the thing.

**Dave Jones:** But I like how he went to a lot of trouble to build it. It's got a Perspex panel on the front, the wood construction is very nice and all that sort of stuff. So as I said it's not all about the just the

**Dave Jones:** act of actually brewing beer. You can do that with any PLC. But what he's done in this case is that he's actually used the free RTOS. He's used a real-time operating system and developed an entire web server for this thing. So he can control it via the web.

**Dave Jones:** And it also integrates with some existing open source software. And he's actually re-releasing that back to the community so people can develop on this thing. So that is a really excellent way to gain valuable points in a contest like this. Use all the features of the development

**Dave Jones:** board you've been given. In this case it was a classic. It's got Ethernet and comes with web server. It was begging, any application for this contest was just begging to have the web server enabled. So that's what he's done. And he's used a real-time operating

**Dave Jones:** system and the GNU toolchain. It's fantastic. And this is the brew target. I think it's the existing software which he is interfaced to and can control his brew mechanism from. So it's fantastic. And he gives that back. And here's another big bonus point.

**Dave Jones:** Graphs. Personally, when I'm judging a contest like this, if I see that you've measured the performance of this thing, graphs are brilliant. You earn huge points for doing that. It shows you you're dedicated to the project. You're not just slapping it together to put it in there.

**Dave Jones:** It shows that you really care about the design. You've taken the time to measure its performance and optimized it and all that sort of stuff. And as you can see, it's really quite nice. You can actually see how it overshoots there at the start.

**Dave Jones:** He didn't use a PID algorithm in this case, but there's the oscillation around the target temperature and there's the ramp up as it brews the beer, I guess. Fantastic. And then he talks about design improvements as well. So there you go. It's got pretty much everything, including a conclusion

**Dave Jones:** and acknowledgments. And that is pretty much perfect textbook documentation for winning a contest like this. And that's why he got a solid third place. Well done. Let's take a look at second place now. Xingzi Zhang, if I pronounce that correctly, with the RX ECG Silverlight

**Dave Jones:** web server for ECG. It's a bit of a mouthful, but it's an excellent project for several reasons. And let's check it out. Basically what it involves is it involves using the Renesas RX development board to interface to an ECG, an electrocardiogram monitoring system that basically there's just a bunch of amplifiers on the input

**Dave Jones:** fed into ADCs. And that's pretty much it. So it's a pretty simplistic front end, but he's using the Sega RTOS and the Sega network stack as well to web enable this thing. And of course Sega is one of the Renesas RX partners. And you get bonus points for using

**Dave Jones:** the partner tools which come with the board. So he scored points there straight away. And the other thing is it scored big points for originality, because how many people would do a web-based ECG monitoring system, let alone one using the Microsoft Silverlight web server?

**Dave Jones:** And really it's also a good demonstration of the Silverlight web server, which nobody else even thought of doing. It's one of the more obscure applications. So it scored big points there. And on the technical merit side, it also scored pretty big points, not so much for the

**Dave Jones:** electronics side of it, but for the software side requiring to interface with a real-time operating system, the web server, and then going into the Silverlight aspect of it as well. And it's a pretty useful device. So they were three of the categories it scored high in, originality,

**Dave Jones:** technical merit, usefulness. But unfortunately it didn't score as high as the third place Brewbot, for me anyway, in terms of the documentation. While he's got two videos here, they're actually quite poor videos. And let's take a look at them. And here he talks about the board, but it's a very uninteresting, monotonous

**Dave Jones:** kind of audio voiceover. Whereas compare that with the Brewbot, where he was actually in the video himself actually talking about the project. So that gained big points. So the videos weren't very impressive and they weren't very informative, unfortunately. And same with the other one down here.

**Dave Jones:** It's just basically just documenting how to use the program, which isn't really that exciting at all, I've got to say. So I wasn't thrilled by the videos, but he made up for it in the written documentation, which is duplicated on the main page here.

**Dave Jones:** But we can actually go to the schematic. He's also produced the schematic, so he met all the terms and conditions to provide the schematic, the bill of materials and all that sort of stuff once again. So it's all there. But if you go to his documentation, which is also a similar length to the other one,

**Dave Jones:** 22 pages, there you go. So that goes to show that length of documentation and the in-depth part of it matters as well. Abstract introductions, system descriptions, all sorts of stuff, performance and test, it's all there. So let's take a quick look through. It talks about Silverlight, what is it, it's a Microsoft development platform, etc.

**Dave Jones:** I didn't know much about it. I learned something from actually reading this documentation. I went on and had a look at Silverlight and exactly what it was and what it did, and that's great. He's using something that nobody else used. He's got some nice pretty system block diagrams here of how it uses and how it

**Dave Jones:** accesses through the ports and how it can be used for doctors using a web browser in a remote location or something like that. So it's really terrific. And he's got the system description down here, cross-domain, boundary, policy server, talks all about that. Fantastic detailed stuff and all the ports he used, it's all there.

**Dave Jones:** It looks like he's, I don't know whether or not he did that or he's taken that from somewhere else, he probably did that himself, about how all the system requests and things like that work based on the client and the task and all that sort of stuff.

**Dave Jones:** So that's really detailed and quite nice. How the data service works, the analog front end, that's clearly taken from the analog, that little schematic there is cut and pasted from the data sheet. That's another big tip. Take data sheets for your parts that you're using, a full

**Dave Jones:** absolutely chock full of beautiful diagrams and internal descriptions. Make use of them like he has here and he's just added basically just here's the board and these are the lines I'm using that interfaces to this chip. It's great. It's exactly what you need.

**Dave Jones:** It's easy to document stuff like that. Once again he's taken the screen capture from the data sheet in terms of how it all works. So there's some really easy documentation there on offer that you can just steal from the data sheets and it looks impressive.

**Dave Jones:** There's nothing wrong with doing that. More system diagrams of how the buffering works. So detailed. So this written documentation I would rate above the third place getter or the brewbot. The video let it down, otherwise he would have scored perfect marks on the documentation

**Dave Jones:** and the video combined, which is all in one. Now this I really love. He really shows the hardware construction and the dead bug construction technique. Take a look at that. He's flipped the chip upside down. This little tiny 0.5mm thing and wide individual stuff.

**Dave Jones:** I just went that is brilliant. First thing I saw that I thought he's getting bonus points for doing that. Neat little hardware implementation. Nice little hack. I love it. And there's a more detailed up close photo. Isn't it brilliant? So that scored huge bonus points.

**Dave Jones:** He's got the schematic. There it is. Performance and test. Again he's talking about, he's got some screenshots, a whole bunch of stuff, how it all works. Pretty much everything you need to judge this thing. He's left nothing out whatsoever. And that's why it just snuck into

**Dave Jones:** second place. In fact there's not much at all between third, second and first. In fact there's only about 0.4 points. They basically all scored pretty much identically and there was not much separating them whatsoever. And that's how you win a design contest. Or in this case, come a nice solid second.

**Dave Jones:** And that brings us to our first place winner. And it's Thomas Aldred with the NimbleSIG 3 Congratulations Thomas. Now this is a classic example of a project that is so highly technically refined that it's almost, I hate to say it, it's almost impossible to beat in these sort of contests.

**Dave Jones:** Really the only time you're going to stand a chance is if you have such an incredibly novel entry that it might score very highly on one of the obscure judging categories like say cost-effectiveness or something like that. Which most of the projects in this

**Dave Jones:** contest actually really didn't score anywhere on the cost-effectiveness because they all used the same development board, the RX development board. So really that was a bit of a nothing category in terms of this contest I thought anyway. Other contests where you might have to just use a single chip or something like that

**Dave Jones:** then really that's when cost-effectiveness can really, a category like that can really come into it. But the first time I heard the name NimbleSIG I thought, aha! I've heard of this before. And sure enough, I remembered that he had entered this project before in a Circuit Seller design contest

**Dave Jones:** back in 2006. Actually it was the Luminary Micro Design Stellaris 2006 contest, and here it is. That was the NimbleSIG original NimbleSIG, and then he's had the NimbleSIG 2, I believe, somewhere and now the NimbleSIG 3. He's been refining this since at least 2006.

**Dave Jones:** So like 5 or 6 years this project's been refined, and this is why it is so done good. Now the original design, he's actually, the NimbleSIG 3 here that was in Circuit Seller, that one actually used an NXP semiconductor micro. So what he's done is he's

**Dave Jones:** retooled this project to use the technically superior Renesas RX series micro to enter this contest. And bingo! That's exactly what he's done. He still called it the NimbleSIG 3, but there's nothing stopping you from entering a highly refined project you've been working on for years.

**Dave Jones:** And if you've been working on it for years, you're really going to stand a very good chance of winning these things and beating the other people who just see the contest and go, oh well, I'm going to enter this I've got 2 months to enter, and they've only got 2 months to work on their project or something.

**Dave Jones:** You've been working on it for 5 years, who's going to win? It's easy. But it's not because he's been working on it for so long, it's a awesome, awesome project. It's a complete RF analyzer from 200 kHz to 200 MHz, and there's lots of really

**Dave Jones:** magic analogue stuff in here. So let's take a quick look at it, shall we? Welcome to the NimbleSIG 3 RF analyzer demonstration video. We have put this video together to try and demonstrate some of the features of the NimbleSIG 3 RF analyzer. This RF analyzer consists of a dual output RF signal generator that can be

**Dave Jones:** operated over the frequency range of 200 kHz to 200 MHz. Either generator can be operated... So there you go, he goes into detail with a very good voiceover of how it all works, and then he's got separate videos down here for how the user interface works.

**Dave Jones:** Check out the complete graphical user interface he's refined for this thing. It really is quite remarkable, and you actually boot it up, and it says, welcome to the NimbleSIG 3, and there's the user interface. Fantastic stuff, really. And he's got the required documentation.

**Dave Jones:** So let's take a look at the PDF document, shall we? Let's close down that one, and load up this NimbleSIG 3, and here it is. He's got excellent photos. Check out the build of it. It's just a nice build as well. It looks like he's put a ton of effort into this, and he has, because he's been spending years

**Dave Jones:** building and refining this thing. And once again, look at the documentation. Woohoo! Right? It's got absolutely everything you could possibly need. Let's look at the build inside. He's got his own custom, there's the LCD board he's using, off-the-shelf touch screen LCD controller type micro board, and there's the

**Dave Jones:** Renesas RX series development board in the bottom of the box, and he's re-jigged it. He's used a prototyping board on top there, which plugs into the two user headers. He's the only one that actually used that board. I believe it was, I think it was offered as part of the contest,

**Dave Jones:** but he's the only one who used that that I actually saw. And it's a pretty simple interface, but he's redone all of the software and the whole thing. He shows how he uses the RDK as the controller, and to talk to all his individual boards, he's got

**Dave Jones:** the active mixers and the RF gain and the phase detectors, and the DDS signal generators. And he just goes into detail after detail, and there's some of the RF wiring in there, some of the coax wiring. Brilliant. Let's take a look at some of the further build.

**Dave Jones:** And there's the front panel, he's gone to a lot of effort to build that, the user interface of course we're talking about, and it's just, there is no shortage of, how can you not be impressed by this project? I mean, it actually plots, look at this, it actually plots the

**Dave Jones:** performance. It's just an awesome project. He's developed a complete, a serious bit of test gear here, that seriously, you could buy this thing. You know, you would, some people would spend many thousands of dollars buying something of this magnitude, this product. And it's all there, and there's his custom board,

**Dave Jones:** 3, and it's in a custom alloy, a custom machined alloy case, check out that for the shielding. Absolutely brilliant. And then he goes into the complete schematics, and there's the DDS, I think that's, no, that's his phase magnitude detector board. So all these modules

**Dave Jones:** are all custom made, and really, there's no way that you can beat that in a given contest time frame. You can't. The only way you're going to get it is if you've been developing this for years. And he already had those modules and he retooled it to use the Renesas RX board, and that's just fantastic.

**Dave Jones:** So really, that's a, there's that header, there's that extension board which went on top of the RX series board, which is quite nice, it's got various footprints. And he's just using that as just an interface controller, as just an interface board, really. So pretty simplistic use, but a classic example of using

**Dave Jones:** and leveraging an existing project to win a design contest. So if you want to know how to win, remember, rejig your existing project, and you're going to be hard to beat. Thanks. See ya.
