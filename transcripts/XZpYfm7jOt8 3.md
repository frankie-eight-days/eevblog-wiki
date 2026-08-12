---
video_id: XZpYfm7jOt8
title: EEVblog #636 - FPGA Demo Boards - DE0 Nano
url: https://www.youtube.com/watch?v=XZpYfm7jOt8
source: youtube-asr
timestamps: {"0": 1, "1": 15, "2": 35, "3": 56, "4": 74, "5": 92, "6": 109, "7": 126, "8": 139, "9": 153, "10": 166, "11": 184, "12": 196, "13": 206, "14": 219, "15": 232, "16": 252, "17": 264, "18": 278, "19": 292, "20": 309, "21": 325, "22": 341, "23": 356, "24": 373, "25": 386, "26": 401, "27": 417, "28": 430, "29": 443, "30": 460, "31": 470, "32": 488, "33": 502, "34": 515, "35": 526, "36": 544, "37": 560, "38": 576, "39": 593, "40": 604, "41": 616, "42": 630, "43": 642, "44": 653, "45": 665, "46": 676, "47": 688, "48": 699, "49": 714, "50": 729, "51": 742, "52": 758, "53": 772, "54": 784, "55": 799, "56": 814, "57": 828, "58": 840, "59": 855, "60": 869, "61": 884, "62": 902, "63": 923, "64": 934, "65": 948, "66": 962, "67": 974, "68": 986, "69": 1000, "70": 1018, "71": 1029, "72": 1043, "73": 1058, "74": 1073, "75": 1085, "76": 1098, "77": 1112, "78": 1127, "79": 1144, "80": 1154, "81": 1163, "82": 1176, "83": 1194, "84": 1208, "85": 1222, "86": 1235, "87": 1252, "88": 1265, "89": 1277, "90": 1290, "91": 1305, "92": 1317, "93": 1328, "94": 1343, "95": 1356, "96": 1371, "97": 1386, "98": 1402, "99": 1416, "100": 1431, "101": 1445, "102": 1459}
---

**Dave Jones:** Hi, in this video we're going to take a look at a couple of affordable FPGA starter kits to get you into FPGAs. So what I've got here is a couple of basic entry-level FPGA kits. Three on the top

**Dave Jones:** here are sub $100 boards that allow you to get up and running. This is the uh Papilio 1 uh Xilinx based FPGA board. Similar sort of style to an Arduino thing. You can connect wings on here and stuff like that. You can even get an

**Dave Jones:** Arduino compatible softcore processor to program inside this thing. And this thing's under 50 bucks and it's got a you know a decent Xilinx FPGA on there. Then we've got this Terasic DE0 Nano board. And this one is an Altera based board

**Dave Jones:** and it's a nice little compact thing like that. This one is $89 US. I think it's as little as $49 for US students. So that one's quite reason- quite reasonably priced. Then we've got the Digilent Basis 2. It's an

**Dave Jones:** sorry a Xilinx compatible like the Papilio 1. It's got a Spartan 3E same as what's on the Papilio there. And uh yeah, it's a neat little unit. This one only costs around $79 or $59 student price. So not bad at all. It has a VGA

**Dave Jones:** output as we'll take a look at. And then we have a higher end one which is the MicroZ uh board and it's Xilinx partner with Avnet. And yes, this is the exclusive Dave Jones edition. Beauty. If you're going to get this, get the Dave Jones

**Dave Jones:** edition one. Trust me. And this is basically a Xilinx Uh, it's not one of their Spartan ones one of their low-end Spartans. It's one of their uh really modern uh high-end zinc ones. And this is an incredibly powerful board, $199

**Dave Jones:** uh for this board, but it can run embedded Linux. And you know, I think it comes actually pre-programmed with embedded Linux. And it's got Ethernet and the whole works. So, quite a really powerful beast and we'll take a a look

**Dave Jones:** at that in more detail as well. So, take a look at the uh Papilio board here. Just an example of what's required bare-bones to get this thing up and running. Uh once again, this is a fairly fine-pitch uh quad flat pack chip. So,

**Dave Jones:** it's not something you can just immediately mount on a breadboard, for example. We need an external oscillator to make the damn thing work. Then we need our platform flash memory connected to it so that uh it can store our

**Dave Jones:** programs when we remove our power. Uh we've got multiple voltage regulators up here. 1.2 V, 2.5 V, 3.3 V. They're for all the various core voltages required by this particular Xilinx Spartan 3 FPGA. And then we've got the uh USB

**Dave Jones:** interface here. I mean, you don't necessarily need this. You could have just had a JTAG header on there and just plugged it straight in and then used an external uh JTAG programmer for that. But this one But all of these boards

**Dave Jones:** have uh USB built in so you can just connect them straight up to your PC. And that's what you want. And if you do want to program these things yourself, which yeah, it's a great thing to do. I highly

**Dave Jones:** recommend it. Just watch out for all the traps for young players. You can get um the external uh programmers. In this case, JTAG programmer. Xilinx uh do this one, the Platform USB cable. This one's uh fairly uh cheap on eBay, not as cheap

**Dave Jones:** as the Altera ones. This is not a genuine one. This is actually a uh rip-off one. And so is this Altera uh USB uh blaster one. You can get these for like I think this one is like something crazy like $8 delivered

**Dave Jones:** something ridiculous like that. So, Altera does seem to have a lower entry point price as far as the JTAG programmer tool goes. That it supports that is supported by the official manufacturer software. Now, the two major players in the market, well, in

**Dave Jones:** fact, all the FPGA players in the market, but the two main ones are Xilinx and Altera. They all offer free tools and as you can see on this basis, too, it's advertised that you can use the free CAD tools from Xilinx. In this

**Dave Jones:** case, the ISE WebPACK. It's a massive download, of course, but it is completely free and Xilinx have the and sorry, Altera have their version as well for free. But, the free versions of the tools don't necessarily support the

**Dave Jones:** higher-end FPGAs. So, that's why if you're going to get one of these boards, you have to ensure that it is suitable for use of what whatever FPGA you choose, you have to en- sure that it's compatible with the free tools.

**Dave Jones:** Otherwise, you'll be paying a fortune for the FPGA tools. Now, this Papilio 1 is an open-source hardware type platform, but it is very basic. It's so I don't think it's going to be as sort of, you know, hand-holding as some more

**Dave Jones:** of the sort of kits from more of the mainstream providers. Brief look at the DE0-Nano here. I rather like this really compact little form factor. Nice 0.1 in headers on here and well, that's actually there's some stuff on the bottom, memory

**Dave Jones:** and bypass and things like that. And also another header on the bottom to plug it into stuff. Mounted on standoffs. Neat little self-contained unit. And as I said, it's got a Altera Cyclone IV FPGA. It's got a USB

**Dave Jones:** interface. It's got an E-squared PROM. It's got What have we got? Four DIP switches. It's got an accelerometer built on. Fantastic if you're into accelerometer stuff. It's got an ADC in there. What else have we got? We've got two

**Dave Jones:** push buttons, 40-pin GPIO headers, 32 megabits of SD RAM. Fairly chunky amount of SD RAM in there. And it's got a serial PROM to program the well, to hold the configuration program and eight LEDs. So, not a bad

**Dave Jones:** little board. I don't mind that at all. The other really good thing about the DE0 Nano, it comes with the software. So, you don't have to download it. And most importantly, the Altera complete design suite, the free package. Cuz this

**Dave Jones:** is absolutely huge. As you can see, it's on a DVD. It can be multi-gigabytes to download the various packages from the manufacturers. This one supplies it for you. The others don't. And the Basis 2 board, it's much larger than the DE0

**Dave Jones:** Nano. There's a comparison there. 0.1-in female headers along here. So, not as many IO as you get on the DE0 Nano, but you do get more nice big chunky switches and buttons. We've got a four-way LED display here. You can have

**Dave Jones:** it as a clock. What I really like is that it's got a VGA output. And that's really quite nice. Cuz one of the best examples for an FPGA is being able to interface to a VGA monitor. Cuz you can

**Dave Jones:** pick up VGA monitors from the garbage room for nothing, right? People throw these out. They make great interfaces for FPGA projects. So, this one allows you to experiment off the bat with that. So, that's really quite good at the

**Dave Jones:** expense of some IO along here. But yeah, once again, it's got the platform flash memory, multiple clock sources once again. Xilinx Spartan 3E this time instead of the Altera part. And it's got a PS2 port on it as well. And you can get modules

**Dave Jones:** that actually plug into this. This was I'm not sure of what type or how much they are, but anyway, you can plug those suckers in, but I really like this one because it's got a VGA output you can

**Dave Jones:** experiment with and presumably some example programs to drive the VGA. This much more upmarket MicroZ board is a $199 one. Um, unfortunately, it doesn't really come with any IO, like usable IO. Of course, it's designed to have, you

**Dave Jones:** know, embedded Linux. It uses the high-end Zynq FPGA. Really neat. It's got a built-in ARM 9 processor. Really powerful thing. Runs embedded Linux. I think it's already pre-programmed with it out of the box. We have to power it

**Dave Jones:** up and have a look. Ethernet interface, of course, but all of the IO here is on the bottom. It's got an SD microSD card on the bottom. All the IO here is designed to plug into a rather expensive

**Dave Jones:** IO board, which I don't have. Wasn't provided with this thing, which is being a bit of a bummer. It's a really big board, which I'll post a photo of right now. That just breaks out all of the IO

**Dave Jones:** into handy usable stuff. So, if you're going to get one of these, I'd recommend you spring the extra and get that IO board. I stand corrected. This sucker contains two, not one, but two 1-gig 1-GHz, folks, ARM Cortex-A9

**Dave Jones:** hard processor cores in there as well, of course, as all the FPGA fabric as well. It's got two 1-meg sample AD converters as well. So, really powerful board, that one. So, if you're looking to run something inside a traditional as

**Dave Jones:** it like inside a traditional processor, you know, these hardcore ones are better than, you know, the soft cores you can program into any almost any FPGA as long as it's got enough enough gates inside, enough room in there. You can program

**Dave Jones:** Um, uh, different types of softcore processors into these things, but you know, something like this dedicated, um, 9 1 GHz processor in there cannot be beat. Uh, really, it just absolutely kills any softcore processor that you can, uh, program into any other FPGA

**Dave Jones:** fabric. And also, you don't want to piss away your FPGA fabric inside these things with the softcore processor. Like you might put a softcore processor in here, but it might use, I don't know, um, just as a guess, you know, it might

**Dave Jones:** use that 10 or 20% of your FPGA space depending on, uh, what type of processor it is. Don't want to waste it. And they're usually not going to be very quick. Like the FPGA itself, uh, for example, might

**Dave Jones:** be very, very quick, but when you, uh, compile in, not the correct term, but we'll use that today, um, an FPGA, uh, core, softcore into this thing, it can't run, you know, at nearly that speed. You can get them to run at tens

**Dave Jones:** of MHz, 50 MHz, maybe. So, this certainly won't be a, uh, complete tutorial in, uh, how to, you know, set up and run these things. I'll, uh, basically won't uh, show you anything. I'm just going to, uh, install

**Dave Jones:** it and get them running. And that's the whole idea. How easy is it to get these things running? I'll just tell you in the end. I won't show you all the horrible steps to it. So, we'll start out with the DE0 Nano and, uh, that of

**Dave Jones:** course has the Altera, um, Cyclone part on it. So, we're going to install the, uh, thankfully, the, uh, software comes on that, uh, DVD. We didn't have to download it, however big it is, however many gigabytes. We're just going to

**Dave Jones:** install that. So, here we go. Install free package and well, see what pops out the other end. When you install it, uh, you have the option to install that Quartus II. You have to install that. It's the with free

**Dave Jones:** web edition. It is the actual suite of tools for all the FPGA stuff. So, there's no getting around that, but you can also install the ModelSim, uh, as well. And that's just, uh, simulation stuff. And most beginners probably don't

**Dave Jones:** need ModelSim. So, if you want to save the 2.7 gig, you certainly can. And that only took 23 minutes. That wasn't too bad, I guess. Can be a lot worse than that, trust me. And well, no, I don't

**Dave Jones:** wish you to talk back enable sending talk back. No, go away. Anyway, um it's finished and it installed, as you can see well, it installed all the different families down here, not just the uh Cyclone 4, I think, which we needed.

**Dave Jones:** Installed, you know, Stratix, real high-end stuff, Area, and all those. What the FPGA is this garbage? The software install has now started thrashing the CD drive and locked up. This was after it said it installed and everything was hunky-dory. And this just

**Dave Jones:** goes on and on and on forever. You got to be me. Ah. And on the other CD that comes with it, uh there's no install file or anything like that. There's just uh some subdirectories with all the stuff.

**Dave Jones:** There's uh various uh demonstration programs. Oh, look, my first FPGA. That sounds neat. There's all the uh uh files for the um Altera Quartus uh stuff, the ADC stuff, and yeah, uh there's the uh accelerometer, by the looks of it. So,

**Dave Jones:** that one looks uh quite neat. And then we've got uh the data sheets with the um uh all of the various uh parts. That's pretty handy. And uh we got the schematic. Fantastic. And we can load that up. And bingo, there it is. And we

**Dave Jones:** can have a look at uh how they've implemented this thing. There we go. Not sure what package they've used to uh use that. It's not Altium. But uh yeah, once again, they've done all the separate pages. This is

**Dave Jones:** very common for these FPGA vendors. It It's sometimes it's good, sometimes it's not so great. That's how they've implemented the uh configuration prom and the JTAG interface, and everything's just spread over a couple of pages here. So, that is a little bit annoying, but

**Dave Jones:** uh But there you go. They give you all the complete schematics, which you will need to um interface this thing. And you notice here's all the uh power supplies, 3.3 V, 2.5 V, 1.2 V for the various cores on the FPGAs cuz these FPGAs can

**Dave Jones:** be a real pain in the ass. Now, according to the quick start guide, we can just run one of the demonstration programs here, a batch file in here after installing our uh Quartus II software, which we've done, and uh

**Dave Jones:** and Bob's your uncle, it should download and everything's right because these FPGA tools are actually command line tools. You don't have to use the GUIs. Um and in fact, you know, that's how a lot of uh third-party tools integrate

**Dave Jones:** with these FPGA tools is they're all command line driven. So, let's go in there and try it. Uh G sensor, here it is, demo.bat. And cuz there's no batch file in there, so we should have to just run test.bat, I guess.

**Dave Jones:** Let's see if it works. Does it work? Demo. No. What? There was some red thing there, I saw it. Oh, fail. And that error message was that it hadn't detected my uh USB Blaster because this board actually has that USB

**Dave Jones:** Blaster uh functionality compatibility uh built in to the board as I showed before you could buy for like $8 that external programmer. It's built in, but look, it um yeah, it just didn't install properly. Oh, it's supposed to do that when you

**Dave Jones:** install the Altera Quartus software. You've got to be kidding me. All right, I manually installed the drivers. They're in the usual uh location in the Quartus software under /drivers/quartus/drivers/usbblaster and did the usual Windows thing. So, one more time for the dummies, here we go,

**Dave Jones:** test.bat. Woohoo! Look. It's doing it. It's doing it. It's doing the business. Well, it's doing something. Uh my LEDs are still uh flashing. By the way, that um uh LED um you know, Knight Rider type thing, wait, um came uh pre-installed with the board,

**Dave Jones:** which is really quite nice. Oh, there we go. Looks like it's done. It worked a treat. Beautiful. I don't even get over that driver issue. Not a problem. Thumbs up. And yeah, check it out. We are in a

**Dave Jones:** command line interface. Man, look I can go CLS and it actually clears the screen. Hello. Command not found. Now, this uh, certainly won't be a tutorial on how to use Altera Quartus II, that's for sure. I just wanted to show that we

**Dave Jones:** can actually load our project into that. And all I did was double click on the project file within that uh, demo subdirectory, that accelerometer sensor we just ran and bingo, here it is loaded into Quartus II and there's our source

**Dave Jones:** code. Fantastic. And if you want to do, of course, we can just modify our demo program, then we can go over here and actually uh, compile the thing. We can analyze, synthesize, fit and then program the device down there. So, we

**Dave Jones:** can just double click on analysis. Do you want to run the task again? Yep, here we go. It's going to go through analysis and synthesis and yeah, it was successful. There's six warnings, not a problem. So, it all just works. Total

**Dave Jones:** logic elements, there we go. Used only only used 189 logic elements. Total uh, dedicated logic registers, total registers 112, not much at all. And then we can do the same thing for the place and route. Here we go. I'm uh, it's

**Dave Jones:** almost complete there and should successful. Four warning error messages. Total logic elements used, look, less than 1% of what that FPGA is capable of. Total pins, all that sort of jazz. Beautiful. Total memory bits and total PLLs used. It's using one PLL. Uh,

**Dave Jones:** there's four uh, phase lock loops within this FPGA. And uh, there you go. That's a handy little summary. And there's a million different uh, things and resources we can check and things like that. One neat one is the resource

**Dave Jones:** utilization by entity here. You just go into analysis and synthesis and it can give you all this sort of info. But, this basically tells us that how many logic elements in our FPGA are being used by each particular

**Dave Jones:** Verilog routine there within our program over here. So, that's rather neat. Let's try a more media project. I've opened up that Nios embedded core demo program, and I've done the analysis and place and route on that, and it

**Dave Jones:** didn't take that long, and look, here it is. Summary of that after place and route. I've only used 26% of our you know, cheap ass FPGA to run that soft core. It's running external DRAM and everything else. So, that's not as

**Dave Jones:** pretty good, you know, on a low-end cheap ass board like this. I like it. Now, there's a million and one neat different things we can do with all the tools built into this thing, but one I really like is the power analyzer. Now,

**Dave Jones:** after we run the assembler down here, then we can go up into our tools, and sorry, there's a whole bunch of tools. There's million and one tools you can do. Logic analyzers, signal tapping. Oh. Good stuff. Anyway, let's go to the power play power

**Dave Jones:** analyzer tool. And we can run that. I've already run that, and we can go to the report here. Hello, McFly. Come on. Go into the report. There it is. It simulates the whole thing. Tells us how much power that program is going

**Dave Jones:** to be running. Here is total thermal power dissipation 282 mW to run that Nios soft core processor there. So, you know, that's pretty neat. And here's a summary of the results. 350 mW total thermal power dissipation for that Nios

**Dave Jones:** core there, but we can go in and we can get all sorts of things. Total power dissipation by block types. We can get power dissipation by hierarchy here. Come on. This is slow as a wet week. Man, I'm only running a 2 GHz core i7

**Dave Jones:** here. I'm not sure what's going on. Maybe it's my screen capture in the background, but all these breakdowns of all the power dissipation. Fantastic stuff. And you can even get an estimate of what current is going to be drawn here from

**Dave Jones:** each of the uh individual power rails. The like the IO, that was based on a I think it was a 12 and 1/2% uh toggle rate or something like that. So, it's just an estimation, but if you see AVCC

**Dave Jones:** D, the internal power dissipation, the static current, fantastic. And of course, one thing you're definitely going to want to well, you're forced into um when you're doing FPGAs, one of the big things is of course assigning pins cuz

**Dave Jones:** the pins can do many different functions. So, uh Altera Quartus II has the pin planner here. And um this one's obviously already loaded up for this particular project and this particular device here, the EP4C blah blah blah. And you can see the for the BGA part,

**Dave Jones:** all of these ridiculous um symbols for the pin outs. But you can go in there and you can form groups, the DRAM, where the DRAM's connected to and the GPIOs and the keys and the LEDs and the switches. All for And you can create

**Dave Jones:** your own new groups and things like that, which then you can assign into your uh into your Verilog VHDL program to uh you know, to access your IO and things like that. So, here's all our pins, all of our

**Dave Jones:** individual pins, and we can set the IO standard here. We can change all that and we can do all sorts of weird and wonderful and wacky stuff with our pin IO, but that's man, there's just IO configuration in

**Dave Jones:** FPGAs is a 2-hour tutorial in its own right. And there's countless other stuff as well in this in both the Altera and the Xilinx tools and the tools from other lesser manufacturers as well. And yeah, I could do a million videos on

**Dave Jones:** these and still not cover them. As you can see, these are very very complex tools, these FPGAs. And you know, pretty much if you're doing it at this sort of level using these vendor tools as they're called, then you know, you have

**Dave Jones:** to learn how to do these things. But, uh by loading in these example projects and getting everything up and running, then it takes, you know, and then working backwards from that, that takes all at least the uh you know, the the Hello

**Dave Jones:** World grief out of it cuz FPGAs are incredibly difficult and complex just to get, you know, the blinky LED going, really. But, I haven't touched on one of the awesome things that comes with this DEO Nano. If you want to create a new

**Dave Jones:** project from scratch, how do you do it? Well, with the uh disk here comes some tools and they've got a control panel that allows you to control stuff, but there's system builder stuff. Let's give this a go. Here it is. Look at this. Teras-

**Dave Jones:** Terasic? Don't know how to pronounce that bloody name. It's a bit hard, but here's the DEO Nano FPGA board and you can EV blog, let's call our project here. And what do you want to use? I want to

**Dave Jones:** use a clock, I want to use a couple of buttons, I want to use SRAM, I want to use everything. And what Oh, look, 5 megapixel camera. Looks like they've got some modules that you can whack on to

**Dave Jones:** the header. That's pretty neat. 4 and a half uh 4.3-in LCD and touch multi-touch LCDs. Presumably, you can just buy those, plug them in. Anyway, um the whole idea is this will generate a code template for you that you can work from

**Dave Jones:** and take all that really annoying pin configuration stuff and things like that out of the equation. So, here we go. Let's try it. I haven't tried it yet, but let's generate GPIO header. There we go. Well, you know, we've got

**Dave Jones:** none. Let's just go GPIO default, shall we? And let's just go generate. And it will generate uh Here we go. I'll save it and then we'll try and do something. And here it is. Code generated. EV blog and bingo, there's

**Dave Jones:** our code. Let's check it out. We can load that. Just load up the uh Quartus project file here and we're in like Flynn. And here is our project all with our template already set up. Here's our DRAM configuration,

**Dave Jones:** the LEDs, key switches, everything is set up ready to go. Then we can just add our own code on top of that. Beautiful. And then we've got this bit of a wanky control panel software that comes with it, but it just allows you to have a

**Dave Jones:** basic play. It just talks to the board and then just allows you to you know switch the LEDs off and on and you know touch the switches and things like that and you know write stuff to the memory and play with

**Dave Jones:** the accelerometer. There it is. We can muck around and ADC bugger off a vast go away. And then you know and then we can just you know play around with it but really you know that's not a huge value add that's just

**Dave Jones:** more of a toy but that system builder stuff that is a real Bobby dazzler let me tell you that is essential for beginners to build to generate those code templates to get you up and running cuz nothing is worse than your FPGA that

**Dave Jones:** just you know that just does nothing. As a beginner you just you know try to get and configure all your pins and just get all the assignments and everything working just so the damn thing compiles and that can be a real hurdle whereas

**Dave Jones:** that code generator huge step.
