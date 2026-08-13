---
video_id: 6-OLazTJhP0
title: EEVblog #125 - Soup to Nuts with Free Software
url: https://www.youtube.com/watch?v=6-OLazTJhP0
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 26, "2": 49, "3": 79, "4": 103, "5": 119, "6": 143, "7": 170, "8": 194, "9": 215, "10": 235, "11": 251, "12": 271, "13": 288, "14": 307, "15": 323, "16": 343, "17": 364, "18": 382, "19": 399, "20": 414, "21": 433, "22": 452, "23": 467, "24": 478, "25": 493, "26": 516, "27": 547, "28": 562, "29": 584, "30": 604, "31": 621, "32": 640, "33": 656, "34": 686, "35": 705, "36": 732, "37": 760, "38": 781, "39": 800, "40": 814, "41": 832, "42": 854, "43": 877, "44": 898, "45": 913, "46": 931, "47": 948, "48": 963, "49": 983, "50": 998, "51": 1013, "52": 1045, "53": 1056, "54": 1078, "55": 1101, "56": 1116, "57": 1131, "58": 1153, "59": 1169, "60": 1189, "61": 1208, "62": 1223, "63": 1238, "64": 1255, "65": 1268, "66": 1286, "67": 1305, "68": 1324, "69": 1348, "70": 1364, "71": 1378, "72": 1392, "73": 1407, "74": 1422, "75": 1441, "76": 1462, "77": 1484, "78": 1501, "79": 1522, "80": 1538, "81": 1561, "82": 1580, "83": 1592, "84": 1608, "85": 1626, "86": 1642, "87": 1660, "88": 1686, "89": 1710, "90": 1726, "91": 1740, "92": 1758, "93": 1772, "94": 1794, "95": 1808, "96": 1830, "97": 1850, "98": 1870, "99": 1886, "100": 1904, "101": 1927, "102": 1948, "103": 1964, "104": 1982, "105": 1998, "106": 2020, "107": 2036, "108": 2050, "109": 2066, "110": 2082, "111": 2100, "112": 2116, "113": 2134, "114": 2156, "115": 2170, "116": 2186, "117": 2204, "118": 2220, "119": 2258, "120": 2280, "121": 2304, "122": 2322, "123": 2340, "124": 2356, "125": 2378, "126": 2394, "127": 2412, "128": 2432, "129": 2458, "130": 2478, "131": 2498, "132": 2520, "133": 2536, "134": 2556, "135": 2572, "136": 2588, "137": 2606, "138": 2626, "139": 2644, "140": 2658, "141": 2670, "142": 2694, "143": 2708, "144": 2724, "145": 2744, "146": 2762, "147": 2776, "148": 2796, "149": 2822, "150": 2842, "151": 2868, "152": 2886, "153": 2904, "154": 2922, "155": 2940, "156": 2958, "157": 2978, "158": 3000, "159": 3020, "160": 3040, "161": 3062, "162": 3080, "163": 3098, "164": 3116, "165": 3136, "166": 3148, "167": 3172, "168": 3192, "169": 3206, "170": 3218, "171": 3234, "172": 3248, "173": 3270, "174": 3288, "175": 3304, "176": 3320, "177": 3338, "178": 3360, "179": 3382, "180": 3396, "181": 3414, "182": 3434, "183": 3452, "184": 3470, "185": 3484, "186": 3508, "187": 3530, "188": 3550, "189": 3568}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Good morning everybody. Those of you who are morning people, morning everybody. This is AE-19C, supercharged with free software. My name is DJ Deloria, I'm a senior engineer at Red Hat,

**Dave Jones:** work in the Global Engineering Services group. We do primarily embedded systems, cross-developers, etc. I've been working with the GNU tools since 1998. I've also worked with the GNU tools on DJDP since 1989, and my first experience with a Renesas XU was in 1992 with the AJ300.

**Dave Jones:** I'm also one of the co-maintainers of some of the free layout software that I'll be talking about later, and author of the RHC, M16C, M32C, and RHC flash programming guide. So, by now you've seen this chart talking about all the wide range of products Renesas offers.

**Dave Jones:** The things that we're talking about today cover pretty much most of these, since we're talking more about the environment in which we use these products, not the products themselves, but we're going to focus more on the microcontrollers and microprocessors area. This is the lineup of the Renesas microprocessors, and although I have

**Dave Jones:** my favorites, and you might as well do too, we're going to cover pretty much all of them. With the techniques that we will cover today, we'll cover pretty much all of the processors you see here. I think we don't support the 720 and the 780K, but that's about it.

**Dave Jones:** Now, wrong presentation. So, what's the innovation here? And I had some really pretty pictures to bring up. So, we're going to talk about some of the people who have used Free Software, or the concepts behind Free Software, to innovate with their products. And then we'll talk about how you can use those

**Dave Jones:** same concepts to innovate with your products. Companies like Red Hat, IBM, InSoftware with their Quake, Android operating system, Linux kernel itself, and even companies like Utopia, one of the first Linux-based smartphones. Even Apple uses Free Software to produce with their products, despite the fact that when you perceive them as a closed company, they do take advantage

**Dave Jones:** of the Free Software philosophy to innovate with their products. So, what does this mean? It means to me, new business models mean new opportunities for you to interact with your customers and your suppliers. And my position is that Free Software enables mass uptake of your products and freedom

**Dave Jones:** to innovate. Using Free Software in your business gives you control and flexibility. And using Free Software in your products gives your customers control and flexibility. That allows them to do more. It allows them to do things the way they want. And not everybody agrees with this position.

**Dave Jones:** So, the agenda today, we have a few things to cover. We're going to cover the business end of using Free Software. And what I mean is, how to use Free Software for your daily business needs. Email, web browsing, data peer, business backend databases, and all that stuff.

**Dave Jones:** I'm going to talk a bit about using Free Software to design electronics. Hopefully by now you've all seen a nice pretty pink sheet of paper with a little circuit board in your hoodie pack. This board was designed entirely with Free Software. And the embedded development tools for Free Software will be the next topic.

**Dave Jones:** And again, all the software I write for these boards is all Free Software. And then finally, we'll spend some time at the end to talk about the philosophy behind Free Software. How you can apply it, what it means, how you can integrate it into your business.

**Dave Jones:** And throughout, we'll be stopping at the end of each section for questions and answers. So, let's cover some examples of innovation which came about because of the Free Software philosophy. The original IBM PC, most people don't think of it as being Free Software.

**Dave Jones:** It was kind of before that. One of the key things they did was they included with every PC file systems, specifications for the hardware, so that you can add to their platform. You can put your own things in. You can do things with it that they didn't anticipate.

**Dave Jones:** And because of that, people had some arguments on whether the technical point of view was the best platform. It certainly became the most popular platform. You can see where that led. The LAMP stack, some of you might have heard about, Linux Apache and MySQL Python.

**Dave Jones:** It's becoming very popular in the business world as a back-end for businesses. And it's basically entirely out of Free Software to the businesses who use it and apply it the way they want. Quake 3. Most people don't think of video games when they think of

**Dave Jones:** Free Software. But when Quake 3 came out, InSoftware specifically licensed their games to allow, in fact, encourage people to add levels, to use what they had produced, to extend it, to do more things with it. And because of that, their product was relevant and fresh and usable

**Dave Jones:** for much longer than you would have expected. The new tool chain, we've all heard about it in these last few days, talked about who you are at. The concept here is that with many contributors and many users, a product can become ubiquitous. Everybody does it with the new tool

**Dave Jones:** chain because everybody uses the new tool chain. Everybody supports it. They got that through the Free Software philosophy. And finally, you've probably seen many of the smartphones today are starting to use the Free Software offerings in order to get their product to market faster

**Dave Jones:** and concentrate on the pieces that are specific to them and let other people worry about the parts that are common. So what does Free Software mean? A lot of people talk about Free Software, and a lot of people actually know specifically what it means.

**Dave Jones:** And they think, well, it's not free because I can't do everything I want to do with it. Or it's not free because they charge me for it. It's not entirely about what the user wants. Free Software is about what the software wants. The software wants to be free.

**Dave Jones:** And by free, I mean there are certain freedoms that the software grants to the users. And Free Software is about making sure that those freedoms are maintained. For starters, Free Software means that you have the freedom to run the program for any purpose.

**Dave Jones:** You can't write Free Software and say, we can only use it the way we want to. You can only use it in these countries. You can only use it for these purposes. You can't compete with us with our own software. You have the freedom to run the software for any purpose you want.

**Dave Jones:** You have the freedom to study how the program works and change it to make it do what you want. So if the software doesn't fit into your needs, you can make it fit into your needs. You have the freedom to redistribute copies to help your neighbor.

**Dave Jones:** Now, in the Free Software world, they talk about neighbors, but who are your neighbors in your business? They're your customers, your suppliers, your partners. Those are your neighbors. The ability to share your software and the tools you use with them allows you to work together more efficiently.

**Dave Jones:** And finally, the freedom to distribute copies of your modified versions to others. So if you get something, so if you get something, you have not only the option to enhance it to fit with your business practices, but then you can share it with your partners so that they have the same business

**Dave Jones:** practices, the same extension. So let's talk about how you would use Free Software for your business. I mean your daily business needs. Desktop. There are a couple of different standard desktop platforms available. The most popular ones being Economic PDU desktops, which you find in most of today's Linux-based distributions.

**Dave Jones:** They include such things as the Firefox web browser, mail readers, news readers, PDF readers, all the usual things that you need as part of your daily business, like I want to check my email, I need to go online, I need to download some specs so I can read about something.

**Dave Jones:** These are all standard in Linux-based distributions and desktops. There's also a full Office suite included. OpenOffice is basically all the things you need for your standard Office. You need to work across some spreadsheet, database, presentations. In fact, this presentation was developed using OpenOffice, not PowerPoint.

**Dave Jones:** Oh, I did double check it before I sent it to you. And you get some extras in here that you normally wouldn't get in an Office package. For example, OpenOffice can export to webpages and PDFs by default. It always has. It's never been an extra thing you had to buy separately.

**Dave Jones:** And servers. Many businesses use servers for databases, for their mail, for their web, DNS, DHCP, NFX, Samba, routers, firewall, FTP, IRC. Most of the internet runs on free software. So any time you go out and visit a website, there's a really good chance

**Dave Jones:** you're using free software too. And there are other packages as well that other companies have used as part of their moving things together. So any questions so far on this stuff? This actually goes kind of quick. People ask a lot of questions. What's the link between OpenOffice and Java?

**Dave Jones:** Because I think when I do my Java install these days, it asks me about my install of OpenOffice. Is there some link there between... The link between Java and OpenOffice is they're both produced by the same company, which would be Sun Microsystems, now part of Oracle.

**Dave Jones:** So that's kind of a product tie-in thing, that there's no technical reason why, but it's part of the whole package deal for Sun Microsystems. Does anybody use any of these software yet? Oh, excellent. We should do the choir. How many people use a Linux-based distribution by default?

**Dave Jones:** Well, that's the rest of you. We'll be honest. EEM tools. These aren't quite as well known as the Office automation tools, because there are fewer engineers in the world than there are, well, everybody else. There's a couple of different EDH suites that are free software.

**Dave Jones:** I use the Jida PCD suite because as one of the developers, it does what I want. The Jida suite includes the usual things, schematic capture, board layout, simulation, and a few not-quite-so-ordinary things. Scripting, the ability to integrate with your makefiles and your backend processes, databases,

**Dave Jones:** and to extend to other unusual fields. Build materials, burger exportation, documentation generation, and these are available on all the top platforms. Linux, Unix, Macintosh, Windows, Macintosh is based on a Unix free software environment as well. And all of the file formats that they use are all also free to document.

**Dave Jones:** They're open formats. They're easy to use. They're text files. You can run them through any program you want to, modify them in case the tools don't do what you want. You can write your own tools. And the other common suite that Google uses is the PyCats suite, which basically does the same

**Dave Jones:** thing. It has schematic capture. They've got the layout programs. They've got all of the usual things. And they, again, support all of the usual platforms. And in the power of Google's RTV, it really shows up. When you're designing flow, it needs to do something different,

**Dave Jones:** something unique. If you buy a personal package that has everything glued together, you're basically stuck doing things the way they want to do, because everything that is designed to work their way. But with the open source tools, if you want to do something different,

**Dave Jones:** if you have some unusual way of managing your EA flow, then you can do that. The beginner might only use common programs in the expected way. But when you start getting into larger projects and more mature projects, where large databases of products, and they have their own flows,

**Dave Jones:** their own internal partners, and everything like that, these tools can be integrated into that process, rather than trying to integrate your process into the tools. So it's a lot easier to streamline where you meet the requirements of using free software. Back in the day, I don't know why, but I used this huge system of makefiles and scripts,

**Dave Jones:** back-end databases, in order to take all these archives of old semantics and migrate them into new products. So you can reuse old pieces of old projects without having to go and re-edit all of the semantics. It's all done with a giant process that feeds every kind of grid.

**Dave Jones:** And for some examples of these custom flows, when I do my own circuit boards, after I'm done generating the circuit board, I have a series of scripts that I run that modify all of my layouts in order to compensate for the process that I use to

**Dave Jones:** generate the circuit boards. It might adjust the size of the data pads on different layers, depending upon what's connected to it, and whether or not I'm going to use my four-layer process or my two-layer process in order to cope with the process issues that I've had.

**Dave Jones:** It also takes that same circuit board and extracts some of the pieces out of it in order to generate new circuit boards that I use for doing things like case layout, and rendering, and assembly products. And some of the experiments that people are doing with the software,

**Dave Jones:** which you don't normally see with proprietary software, are also interesting. There are some versions of R2s that you can modify to use 3D rendering of your circuit board, so you can rotate around and see the stack-ups and represent the layers, how the layers interact

**Dave Jones:** with each other in 3D view. Or they use the GPUs in R2s to render all of the layers translucently, so you can see through what you're doing. These are all experiments that people are doing outside of the core development. You normally wouldn't be able to do that with proprietary

**Dave Jones:** software. And of course, all of the tools use standard formats for their outputs and for interactions with other vendors. I often get people asking me, well, your free software, what PCBFabs support your output? Well, they all support my output, because I use standards.

**Dave Jones:** We do not use proprietary formats. We use open formats. I can send my output to anybody. And we have, of course, the usual tools for reviewing the output files and checking all of your work and making sure that everything is the way you expect it before you send it out.

**Dave Jones:** And we include a number of simulators as well that are all open source. We have digital simulators that support analog. We have the analog spice-based simulators. And we're working on a next-generation simulator that's in mixed mode that would support both digital and analog

**Dave Jones:** simulators together in the same package, including all of the previews and the charting. Well, let's see what these look like. These are some examples of schematic capture and circuit layout. And hopefully, by now, you've all played with your little circuit board. These schematics in the layout that you see on the board are that board.

**Dave Jones:** The applications resemble most of the applications you're probably familiar with. They use the same look and feel as most of the other applications. They're fairly intuitive to learn. But if you want to do more, and if you need a more powerful interface, they have those as well.

**Dave Jones:** And you can modify the interface yourself to use scripting. You can go scripting up your menu items. You can type in other bits of your process that wasn't originally included. And here's some screenshots of the HiCAD suite. As you can see, it's basically the same,

**Dave Jones:** almost the same interface. Slightly different functionality, a little more integrated, depending upon whether you prefer an on-prem solution or a more expandable building block type solution. And here's some examples of the post-processing tools here. Yes? I'm going to announce that anybody who tried HiCAD last year and then this morning that didn't

**Dave Jones:** have Undo, now has Undo. So if you want to go back and look at it. And with all these packages, the development continues. And we have people who say, I have your latest release, and they've got these buttons. And it's like, well, you have our latest release.

**Dave Jones:** If you don't have our latest release, we're still working on it. If you want to get it right out of our source control system, we've fixed that bug and many other bugs and have this for the future. I've heard rumors that you've been working

**Dave Jones:** on the experience of these tools on Linux versus Windows. Is the experience better? The question is, what's the experience between Windows and Linux for these tools? And indeed, the developers use Linux, so the tools tend to run better under Linux. But they work pretty

**Dave Jones:** much the same under Windows. There's a few issues with some of the more esoteric features. For example, the layout editor in the preject can generate footprints on the fly using a scripting language or the import from a dynamically generated definition of your element.

**Dave Jones:** Well, in Windows, the scripting tools aren't there. So unless you're going to install the extra packages and get them to work, those extra features are going to be hard-pressed to function. But from a point-and-click point of view, they're pretty much identical. And the typefos try very hard to make sure that their stuff works exactly the same on everything.

**Dave Jones:** Now, if you want to compare Linux to Macintosh, different answer. The Macintosh stuff works flawlessly because they are built on a free software basis as well, and they have all of the essential features. And it's, again, another case where you want to try the absolute latest stuff because we're continuously working

**Dave Jones:** on improving the Windows experience. Do you pull the scripting tools from Sigma? Do you pull the scripting tools from Windows or from Sigma? Do we pull the scripting tools from Sigma? There is a Sigma build of these tools. It's called the portable Gita.

**Dave Jones:** It's designed for people who want to try out Windows. You can go download it. It doesn't infest your system with little pointers and things. It's all self-contained. And that's built on Sigma. But the distribution that we use for our official Windows builds is

**Dave Jones:** based on MinGW tools. So you can get a native version of all of those tools. I believe MinGW has many of them, but the one that we use is kind of the old-school one. But you could use other scripting engines, but the one that's built in, which is the one that

**Dave Jones:** we expect to work with, is VM4 preprocessing. And everybody goes, what? I believe that uses WX widgets. Yes, they use WX widgets, so they have a consistent-looking feel across all but at the same time, it may not look exactly like the native ones.

**Dave Jones:** The Gita suite uses GTK for most applications, but for the layout tools, we actually have the ability to switch to a native tool set on each one, although we haven't quite gotten there yet. But we do actually have two different GUIs for Linux-based tools.

**Dave Jones:** One that's based on GTK and is more user-friendly, and another one based on Rotee widgets, which is for power users and allocates a far greater percentage of the screen to your layout. Because we all know that we need as much screen real estate as possible, and in fact, one of the

**Dave Jones:** projects I'm working on is having dual-screen support, where you can actually use your keyboard to your Windows, so you can use one hand to pan around. So, and we're constantly working on formats, the speed of it, etc., etc., etc. But in general, yeah, Windows, Linux, Mac.

**Dave Jones:** So, any other questions? Is there a limitation on layers? Limitation on layers? It depends on how much memory you have. I found once you get to about 56, the user interface becomes a little difficult to work with. And as far as the port size goes, at the moment, we're limited to about a quarter of a mile.

**Dave Jones:** Quarter of a mile at 0.01 mil resolution. My house is really, really small, so I'm afraid that, sorry for that, too. The free software philosophy is that you never put limitations in your code. You try to code in such a way that they can do whatever they want, limited only by their own hardware.

**Dave Jones:** The default build starts you off with eight layers, and allows you to add up to 16, or a total of 16 layers. If you need more than that, there's one spot in the source where you change a 16 to however many you need.

**Dave Jones:** I know people use it for 24-layer voice regularity. So if you can picture a 24-layer port, it's a quarter of a mile. Do you have more patience to get into support blind, or will be early on? We do not currently support blind and buried computers.

**Dave Jones:** It's next on our list of things to do. Most of the people who use our software so far have not needed the computers. They can't afford it. Because you're a big user, I don't think it's easy to support blind and buried computers. Yes, and it's a very popular request.

**Dave Jones:** And we do have some people who have added patches to it to support blind and buried computers. We just haven't integrated it yet. So you can go and get their patches, add them to our source, and get that functionality in an experimental way, at least.

**Dave Jones:** Something that you sort of can't do with other packages, but they already support blind and buried computers. But yes, that's definitely on our to-do list for you. Please ask me if you need help. Please just listen. You mentioned earlier that there are freeware operating systems.

**Dave Jones:** Freeware operating systems. Basically freeware. Are there any cell phones that were developed, for example, with commercial products? I realize you're familiar with this. You mean cell phones? The question is, are there any cell phones that were developed with FreeSoftware? Do you mean developed with or developed using FreeSoftware?

**Dave Jones:** Actually, both. Do you have an iPhone? I do not. Do you have an Android phone? I do not. Do you have a Nokia smartphone? No, I do not. Then for you, the answer is no. But the iPhone was developed based on the BSD kernel, which is open source software,

**Dave Jones:** at least. And they use the GNU tool chain for all of their development. The Android platform actually runs a Linux kernel. And all of their tools were built using the GNU tool chain. Nokia smartphones, many of those are based on a Linux operating system.

**Dave Jones:** And the Kutopia phone also was based on a Linux operating system. Can you answer the personality of both of them? I don't know of any of the phones, as far as circuit boards have been made, using FreeSoftware tools. I do know that there are some very impressive things out there,

**Dave Jones:** but I can't tell you what they are, that were made with FreeSoftware. Because the electronics companies tend to be very secretive about how they produce their boards. I do know one company, who's really top. They have the testing framework for hard drives. All hard drives are manufactured in this area.

**Dave Jones:** They have a very high-speed reliability test platform that's based on a number of boards, about BAB, with very high-speed FPGAs on them, running custom hardware and custom firmware, in order to do super high-speed testing of hard drives. And that was done entirely with FreeSoftware tools.

**Dave Jones:** But the most exciting project that I know about, that uses FreeSoftware tools, is a couple of million miles away, on its way out to the solar system. There are a number of research projects for deep space telemetry and near space that are built using FreeSoftware tools.

**Dave Jones:** Are the companies ashamed of having used them before? It's not that they're ashamed of them, but even if they use commercial tools, most companies do not want to tell you which tools they have chosen, because they feel that that might give some insight

**Dave Jones:** on the design processes. I think that's usually a closely guarded secret in most electronics companies. I don't know. I like telling people what I do, but whenever I ask people, that's usually the response I get, is that they consider that to be a trade secret,

**Dave Jones:** if their choice may be. And certainly, I see a lot of boards that are designed with FreeSoftware tools, and I can't tell anybody about them, because the boards themselves are trade secrets. But we help them expose in our software and learn how to use the tools.

**Dave Jones:** They give us copies of their files to help us help them. Well, I don't know, PJ. Are there studies that have been done to show any kind of metrics that would show the adoption rates of some of these tools within the engineering community?

**Dave Jones:** I haven't seen any studies yet. I know that we're becoming more and more... We're getting there slowly. Granted, we're more targeting the lower size or the entry level, I think. We consider our competitors to be more equal and less alternative designers, because they're huge

**Dave Jones:** and they do everything. But we have started seeing some independent design firms using the tools to do their designs, because it lowers the cost of entry, and it allows them to do some things that might be easier to do. Anything else? Screenshots. We're getting screenshots.

**Dave Jones:** We have some screenshots here of the Nerd Reviewer. We can export to PDF just fine. We have a photorealistic exporter for our layout package, which has thrown a number of people, Oh, you have the boards already? No. In fact, the presentation had a big pop-up

**Dave Jones:** of the board that I designed, and it looked real, except for one thing, because I used that picture and pasted on pictures of all the parts in order to make something that looked like a board. That started off as an experiment by somebody who had exported the different layers

**Dave Jones:** into a paint program and blended them together to make something that looked like a real circuit board. We thought that was really useful if we integrated that into the product. Here's some examples of our simulator output. We have both, obviously, analog and digital.

**Dave Jones:** This particular trace is here in the digital one. I had done a project with an FPGA. I used our simulator to simulate my basic design. I did all of the layout with the designless tools. I took their post-layout design and simulated it again

**Dave Jones:** with our simulator, not theirs, because theirs didn't do what I wanted. So you see all of the timing issues. I took the code, put it in the FPGA, put a logic analyzer in the FPGA, got the actual data back out, and used the same charting software

**Dave Jones:** to get the live data. So the one tool did pre-layout, post-layout, and actual data. So let's talk about the development end of things. Hopefully by now you've all heard of the new tools in GCC. We've been talking about it a lot with RX.

**Dave Jones:** This is a whole different category of tools from the board layout tools. These types of tools are the same tools that we use for our native desktop environments. The same enterprise-class software that's used by companies like the New York Stock Exchange for their Linux

**Dave Jones:** base servers, we use for our embedded development. The same GCC for iPhone apps can be used for your SH tools and your RX tools. And these can be supported by anybody. If you choose to offer support for these as it is, you go in and learn about the tools

**Dave Jones:** and provide support, either global support or from your niche. Red Hat certainly makes most of their money selling support for software to KBA companies. This is very well known with Renesas for supporting Renesas products, Renesas supports many others who maintain the support and

**Dave Jones:** add to these tools. And performance-wise, Renesas just released the core numbers for the Rx last week, and hopefully you were all impressed by those numbers. I know I certainly was. We're very comfortable in not surpassing the proprietary offerings, depending upon the various chips

**Dave Jones:** and what not. Obviously you have to do your own benchmarks to find out exactly what performance you can get using a free software, which we've found in many cases to be a surpass. Why? Because we've had decades of experience with engineers from many companies working to

**Dave Jones:** make this one platform use optimal code. An optimization that was done for the Intel architecture might apply to the Rx. An optimization done for a Toshiba-rated processor might work with an R8C processor. Having a group that does just tools for one processor can't compete with the entire planet

**Dave Jones:** putting together a toolchain for all the processors. And of course we have debugging, either embedded stubs with one in a part, or third-party drivers, despite the fact that these are free software tools, they can't be integrated with proprietary offerings or hardware-specific debugging, JPEG debugging,

**Dave Jones:** Rx debugging, etc. And of course writing software is no use if you can't get it in the chip. And while this isn't free software, this is a hardware thing, I think one of the strong points that Renaissance has with their offerings is that the protocol that they use

**Dave Jones:** to program their chips is documented. It's an open format, and anybody who wants to add their own value to the programming process can do so. I prefer to use my own solutions for these, but I have some cases where I have one microprocessor programming

**Dave Jones:** microprocessor next to it. And these are things that you can do when the specifications are available, when they're not hidden behind some MPA. And of course source control is an issue in any development project. You need to be able to save all of your

**Dave Jones:** work, and there are a large number of free software operands for source control, which are used worldwide. Most of the free software projects, of course, use their own free software base of source control. And depending on your needs, there are different offerings. For example, the Git source control

**Dave Jones:** tool is used by the Linux team because they are so diverse and dispersed. And they have built this package which is designed for their needs, which is to manipulate patches and changes and bring them up through a hierarchy of review and acceptance into the final product.

**Dave Jones:** So let's focus on the video tool chain for a moment. In free software, there are a number of different ways that you interact with the tool chain. In the center of all of this is the free software foundation. They are the owners of the code.

**Dave Jones:** The code is all copyright by them. They don't usually do maintenance of the code or work on the code, but they are the guardians of the code. They ensure that the work that is done on the code is done to the appropriate quality, and that

**Dave Jones:** from a human standpoint, people who are using the code and distributing the code abide by all the rules. And so the people who actually work on the code, there's a number of different ways that they interact with the source itself. For example, new reports can

**Dave Jones:** be added by any third party to the core set of tools. Red Sox, when they come up with a new check, will contract out with a third party supplier, often it's us at Red Hat. And they will ask to have a report added to the tool chain

**Dave Jones:** for the process. And we will work with them and the free software foundation to put together a report that is acceptable to both parties and add it to the core core. You can also add new features to the tools. For example, you may want to add

**Dave Jones:** psycho-accuracy to an existing simulator. You might want to add compatibility with another compiler. You may want to add hardware support to the debugger. These extra features, again, get added into the pool. They work with the software that others have been writing for years.

**Dave Jones:** And they extend the functionality so that everybody benefits from everybody's work. And then the third major way of adding is optimizations. I mentioned performance before. There are a lot of companies that do nothing but optimize these tools. Mostly for code generation, but also for

**Dave Jones:** the user experience. And they all work together to provide one tool chain that they all share so each group does part of the work that they're best at. Now, on the other side of this, we have distributions and support packages. By distributions I mean more than just a Linux distribution.

**Dave Jones:** I mean if you get a core for Renaissance it will come with a CD with all of the tools on it. Or you might buy a support package from Red Hat that includes tools. These are the distributions that I talked about. And support packages,

**Dave Jones:** you might buy an annual support package from Red Hat or cable companies. You might go to a third party consult to have them support you in a particular way. You might find somebody who's willing to be on-site with you as you bring a new tool up to speed or bring more

**Dave Jones:** engineering engineers or new product out if you've got an end point. These are the kinds of support packages where people can draw from the FSF's pool of software in order to provide these services and offerings. You notice that the users of the software interact with all of these

**Dave Jones:** different parts of it. The users can request new ports. They can fund new features and optimizations. They can go directly to the FSF and look for new bug fixes that they might need at 3 o'clock in the morning on a Sunday because they have to ship

**Dave Jones:** on Monday and their support contract doesn't cover that kind of thing. And they use, of course, distributions as support packages. So everybody works together. And then lastly, this chain of development embedded development is the standard free software IDE. The Eclipse IDE is the standard for

**Dave Jones:** free software development because it supports everything. It's highly customizable. You can do everything from Java to embedded to native to all sorts of weird things. You can integrate in third-party applications. In this example, it's doing a RAC in my lab using a piece of custom software that I wrote

**Dave Jones:** to download the code into the chip. I've integrated that in myself so that I can do it in my lab. And lastly, on the embedded development. Question? We hear a lot about companies these days releasing an IDE for their product. And yeah, questions about it.

**Dave Jones:** And they say, well, it's based on Eclipse. But it's their proprietary product. They release it and they say, here, this is from us. This is our IDE. Oh, by the way, it's based on Eclipse. Great. How are they able to do that? From a legal standpoint or a technical standpoint?

**Dave Jones:** I don't know. I guess maybe both. But are they just doing all the hard living to get CDT to integrate it in? The question is, how do these third-party vendors provide their proprietary offerings based on their free software IDE? And the answer to that is that

**Dave Jones:** in the free software world, from a legal and technical standpoint, they define well-known APIs between the core product and the extensions. And these APIs are, of course, published. And normally they would use these APIs for their own free software extensions to the packages.

**Dave Jones:** But because the APIs are well-known and their intention is that you can attach other works to it using these APIs as communications channels, then that allows third-parties to have proprietary offerings which use the same APIs, the same communications channels, to extend these free software offerings

**Dave Jones:** in a proprietary way. So it makes it easy for you to say, we need an IDE for our product. We take Eclipse, you add your product, ship it up. Granted, you have to follow the rules. You can't change Eclipse to include a proprietary code and then ship it.

**Dave Jones:** That's against the rules. But you can add a plug-in or have it call a proprietary function, in which case the configuration parts, the CDTs and scripts and setups, those are part of Eclipse. Those become free software. But the things that they're calling, the

**Dave Jones:** external programs and applications, they remain licensed under the terms of Eclipse. And we'll talk about licensing later because that's something that always changes a lot of times. This approach, I used this approach with Visual Studio. They have a tool there and we were

**Dave Jones:** configuring there, which was calling Hitachi compilers, linkers, and all that. And HEW does exactly the same thing. You integrate your tools into theirs using a well-known API. For those of you taking my lab later, you'll get a chance to try this and see if you like

**Dave Jones:** this idea or not. Anyway, so I mentioned the serial programming before. I think this is one of the strong points of Redisoft that they document the protocol that the chips use. Not the protocol further out on the other side of their properties, but the

**Dave Jones:** protocol. So if you wanted to add your own way of talking to these chips, you have the ability to do so. While it's not free software, it's the free software philosophy that they're following. Any more questions on that before we get on to

**Dave Jones:** the next section? Excellent. I'm mostly out of time. So, the philosophy behind free software. Now, philosophy is kind of a touchy subject. A lot of people talk about free software, and not all of them understand what it is. It is not a religion.

**Dave Jones:** You do not have to go to the courthouse because you have to give everything away. It's a set of core beliefs that can be leveraged to add value anywhere in your business plan. From internal operations to customer experience. Some of them are practical,

**Dave Jones:** some of them are less tangible, like dealing with community, marketing, talent, all of that. And I'm going to break down into these five key points that I'll cover about the free software philosophy. Sharing. When I was a kid, my mom told me to share my toys.

**Dave Jones:** Didn't want to. She thought it was a good idea. Sharing is how you grow a community. Each one who knows helps the ones who don't. We want to grow our communities. Certainly, from a business standpoint, you want to grow your customer community, your partners, your suppliers.

**Dave Jones:** Because the more people using your product, the more opportunity you have for profit. We all want profit. And in software, it used to be that way long ago. You buy a piece of hardware, they would give you the software. That was the only way to use the hardware.

**Dave Jones:** Until some companies realized that they could create an artificial scarcity in software. Start charging money for the software itself. And that worked for a while. But these days, it's changing. With the advent of the internet and the web, it's become trivial to share and copy software.

**Dave Jones:** The individual ones and zeros no longer have any true value. People who work together to add to the project, to provide feedback, to be part of the testing cycle. So that instead of releasing your final release and then finding out if everything's broken because you didn't test it

**Dave Jones:** the same way you're using it, your users can get involved earlier and you avoid the diminishing returns of testing. On the other hand, each participant must share responsibility and control for the project. This is where a lot of people have problems with free software.

**Dave Jones:** Because they want to own the software. They want to be in charge. They want to be the top dog. With free software, the mindset is that you work with other people to add to the software project. You don't own it. You work together.

**Dave Jones:** On the other hand, the people who use the software aren't expected to help with it. They want you to give back a little bit. If you go and download a piece of software and you've got a way to do a little bit better, you're expected

**Dave Jones:** to provide that feedback to the original project so that you can help grow this package that you've got for free. Community. The community aspect is another intangible to this thing. It's hard to justify this. There's no direct revenue stream involved in community. But a lot of companies are growing their community.

**Dave Jones:** The Renaissance service is putting a lot of effort into growing their community with Renaissance University, Renaissance schools, and all of their other community programs. We're facing this in the worldwide way, but we're certainly making this easy. And it's become expected of companies to have an online

**Dave Jones:** presence where they interact with their community and they share ideas with their community members or with each other. You can make a business case for this. Your customers become more loyal to you. They're more likely to choose your product because they can talk to other people

**Dave Jones:** who are using it. On the other hand, your growing pains are public. If you make a mistake, you have to be willing to say, I'm sorry, and move on. The more you involve your community early on, the more they're going to see the problems early on.

**Dave Jones:** They can help you. You need to let them help you with your products. You have to involve them. The free software model is release early and release often. We might have four or five alphas and then a whole series of betas before you finally get the one

**Dave Jones:** release that's the final release. The most public companies would be the only release. And then we follow it on with bug fix releases, many of them. Why? Because we want to get the right stuff out to their customers as soon as possible so that they can help us provide feedback.

**Dave Jones:** We want really fast turnaround time. And the free software philosophy encourages fast turnaround time. Now, support is where the revenue usually becomes more tangible. Red Hat certainly focuses primarily on support and makes most of their money from support packages. We do not sell software.

**Dave Jones:** We give the software out as part of a support package. The support aspects of free software, this is where you profit. How do you profit from free software? Follow me. I first joined Red Hat as part of Singles, one of the Red Hat acquisitions,

**Dave Jones:** and our motto was, we sell free software. Where do we make our money? Follow me. But seriously, we make money with support packages. How do you do that? Well, if you know more about your product, then people will pay you to teach them about your product.

**Dave Jones:** But support means more than that. There's other groups working with you to provide training and to provide packaging. In the comments, for example, there's a lot of effort into packaging new tools such that they get a user experience with it. Also, there doesn't need to be a central

**Dave Jones:** author for any given package. There certainly isn't a central authority in the new tools. That responsibility is shared. People who contribute a specific feature are the people you can go to and ask questions about it. In public forums, in business to business opportunities,

**Dave Jones:** it's becoming the standard way of dealing with these support issues. Going online and saying, hey, you wrote this, but there's got a bug. How do you fix it? Hey, you wrote this, there's a bug. I will fix it. The thing you need to understand

**Dave Jones:** is that the value in your product becomes a support. The ones and zeros do not have intrinsic value anymore. They're just data. I won't say worthless, but it's so trivial to copy them that there's no hard value in it like there would be

**Dave Jones:** in a hardware product. If you focus on your core competencies, the intellectual property that you have now is your intellect. The people that work for you, your history, your relationships with other customers. It's that type of information that you have that is valuable

**Dave Jones:** to your people's skills. Your customers and other people will pay you to be there for them when they need you. Provide training materials to go on-site to teach them, fix bugs, to answer the phone at 3 o'clock in the morning because they have a release the next morning.

**Dave Jones:** I've been there. This part of the preparation for DevCon I pulled many all-nighters waiting up in case Red Sox had problems with their pilot tools. We would respond within hours because that's what they needed and we knew how to do it. They needed that level of support and we provided it.

**Dave Jones:** And then the other key part is to understand that all these other parties who are providing support for your product are not competitors. They are complementing your offerings. People look at Red Hat versus who they're coming to and say, aren't you people competitors?

**Dave Jones:** No, we're not competitors. We're all working together to provide some different levels of support to customers for the same course offer. Now, licensing are two different things. Licensing refers to the software. Licensing refers to your business practices. I'm assuming you want to ask questions

**Dave Jones:** about what I've already covered so far. Now the software license gives freedoms to others. But it also prevents users from denying those freedoms. So, it prevents users from denying those freedoms to others. So, if you give your customers a piece of software and they can do what they want

**Dave Jones:** and they pass it along to the next person that's what they want. The software then becomes less free. I like to call this freedom for the software not freedom for the users. Users can't do anything they want because they can't restrict others. The software

**Dave Jones:** is the part that gives the freedom. And of course, there's no worries about unauthorized copying. How do you pirate something that you're legally entitled to give to other people? It's like, I'm going to be a legal copy of this. No. If you have a copy,

**Dave Jones:** it's a legal copy. Granted, there may be issues with the legal distribution of free software. If you distribute a binary and don't offer the sources then legally you have lost your ability to distribute the software. But the people who have your software still have all the rights that they started with.

**Dave Jones:** Of course, they have to file a report to get the sources. But the whole issue with piracy just doesn't exist. Community-driven extensions and enhancements are allowed. It's not encouraged by the license. They want you to do more with the product. To extend it.

**Dave Jones:** To add your value to it. To do innovative new things with this package that the original authors may not have intended or expected or even thought possible. Security by Obscurity is no longer an option. The license up requires that your user be able to look at their algorithms

**Dave Jones:** and see if they're secure enough for their purposes. If you decide to get away with shipping that little piece of security software that almost works but not quite, you have to get it out anyway and hopefully no one will see it. And again, you now have to be secure

**Dave Jones:** by really good design. And this is the hard part for people to wrap their heads around it. There's no such thing as software intellectual property. Granted, there is software IP from a legal standpoint. From a free software point of view, the intellectual property is not

**Dave Jones:** the ones and zeros. There's no intrinsic value to something that can be copied for no cost. The intrinsic value is in the things that can't be copied. The people, the experience, the history, the relationships. And the license game, the flip side of this,

**Dave Jones:** since the license is different, the licensing practices are different. And from a business standpoint, it simplifies your business model. There are no activation keys. There's no perceived keys. You don't have to worry about how many people are going to be using the software

**Dave Jones:** when you go to a company. The real issue is how many questions are you going to ask? Do you need to be able to ask these questions outside of the whole business model? Are you going to have a lot of trouble? Do you need somebody on site?

**Dave Jones:** And the interactions are where you worry about headcounts and things like that. But you don't have to worry about them making another copy in another PC. That whole policing thing goes away. There's no licensing dongles you have to worry about. There's no no-block

**Dave Jones:** PCs. You'll have some customer who had their Ethernet card broke and they had to renew it and it suddenly didn't have software that's working for them the day before release. That's happened to me before. How many people have had their software suddenly stop working

**Dave Jones:** because of licensing issues? Yeah, I see a lot of hands going up. Free software? Doesn't happen. On the other hand, licensing is no longer a revenue stream. You can't charge for the software because it's the right company. You have to put the value

**Dave Jones:** in the people behind the software. The value is in the support packages, the packaging, the community that goes with it, and all of those other things. On the other hand, because you can offer different levels of support, you can attract smaller customers. A customer producing a $40 device

**Dave Jones:** is not going to be able to pay $10,000 for an EDA package or for a full support package. Maybe they just need the free software and they need at least worth the three questions, and they buy the small support package. And finally, it allows for an unlimited try

**Dave Jones:** before you buy. How many people have written something using an evaluation copy of the software, only to find out 30 days later, just before the release, that it doesn't work anymore? Yeah, a lot of hands go up. With free software, you can give them the full version up

**Dave Jones:** front. If they like it, they just keep using it. If they have problems with it, they buy support packages. And there are many online resources for you which are part of the presentation. And certainly, the web will find you many resources to further extend your experience

**Dave Jones:** with free software. Any questions on the free software philosophy? This is usually very good for licensing questions. Can you clarify enough the GPL versus LGPL? The LGPL, also known as the Lesser General Public License, is designed for libraries and packages that have other alternatives

**Dave Jones:** that aren't free. And it allows you to replace a proprietary package with an equivalent free package without having to open up your whole application. If you use an LGPL library, the part of your project that has to be at least a source is just that library,

**Dave Jones:** not the whole rest of it. You still have to provide a means for your customers to link a modified version of the library in with the rest of your offering. But you don't have to provide the sources to your rest of your offering.

**Dave Jones:** You're providing a large object to your institution. They use that as a means to get free software to places where a proprietary offering already exists and they're simply trying to replace it and there's no real value in the new software. The GPL is used in cases

**Dave Jones:** where the software is not replacing it, but it's better than some libraries. For example, GCC is GPL because it has so much more and the extra pieces of software are sufficient to warrant GPL. And the Google platform uses the Linux bootstrap, Google G,

**Dave Jones:** which is GPL, not GPL, but Google got around with it using the DBus. Can you comment on that? When you have a well-known API that talks to Google Models, and I mentioned this when I talked about Eclipse, it provides a way of separating

**Dave Jones:** from a legal standpoint one work from another work. From one domain to another. Right. So the legal scope is the scope of a work. If you have two pieces getting combined together to produce one work, they're inseparable. They won't work without each other.

**Dave Jones:** Legally, they are one final product. If you have two pieces that could work together but don't have to, they're talking like if you use a web browser to talk to a website, your web browser and web server are not one piece of software.

**Dave Jones:** They're two things. They're talking. So by using DBus, you have taken a well-known API to have two independent works communicating with each other. So they have independent licenses. Anything else? Wow. I wish we had hours worth of questions. Are there any mechanical design packages?

**Dave Jones:** Yes. There are some. Mechanical CAD is one of those interesting fields where there's so many special things you have to do that it's very difficult to be proprietary. But there are some. There's probably many of them. I have a comment and a question,

**Dave Jones:** but I think one of my favorite free software packages is the web suite. I'm going to need to mention it, but it's just... Our business is Bugzilla. Yes. From Bugzilla. I manage so many of the releases in Bugzilla. It's probably the best. It's arguably the best

**Dave Jones:** by the way for free software. And it's very, very customizable. My favorite free software moment is they eventually released it up in a free software place and it was, well, yeah. It's not part of our business. Alright. That's all the time we have.

**Dave Jones:** I'll be available after this for further questions. Thank you for attending.
