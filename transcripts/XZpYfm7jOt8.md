---
video_id: XZpYfm7jOt8
title: EEVblog #636 - FPGA Demo Boards - DE0 Nano
url: https://www.youtube.com/watch?v=XZpYfm7jOt8
source: youtube-asr
timestamps: {"0": 1, "1": 12, "2": 31, "3": 47, "4": 62, "5": 77, "6": 90, "7": 102, "8": 117, "9": 132, "10": 144, "11": 156, "12": 166, "13": 184, "14": 194, "15": 204, "16": 214, "17": 225, "18": 242, "19": 256, "20": 264, "21": 278, "22": 292, "23": 313, "24": 325, "25": 337, "26": 350, "27": 364, "28": 375, "29": 384, "30": 396, "31": 412, "32": 422, "33": 432, "34": 443, "35": 457, "36": 473, "37": 488, "38": 500, "39": 510, "40": 520, "41": 532, "42": 550, "43": 573, "44": 585, "45": 597, "46": 610, "47": 628, "48": 636, "49": 646, "50": 656, "51": 665, "52": 672, "53": 684, "54": 693, "55": 702, "56": 714, "57": 725, "58": 739, "59": 756, "60": 768, "61": 778, "62": 789, "63": 800, "64": 814, "65": 834, "66": 842, "67": 855, "68": 877, "69": 888, "70": 903, "71": 923, "72": 932, "73": 946, "74": 962, "75": 972, "76": 982, "77": 994, "78": 1012, "79": 1020, "80": 1029, "81": 1046, "82": 1061, "83": 1071, "84": 1084, "85": 1092, "86": 1103, "87": 1117, "88": 1129, "89": 1144, "90": 1155, "91": 1165, "92": 1177, "93": 1191, "94": 1206, "95": 1220, "96": 1238, "97": 1252, "98": 1265, "99": 1285, "100": 1292, "101": 1302, "102": 1316, "103": 1321, "104": 1333, "105": 1348, "106": 1358, "107": 1371, "108": 1383, "109": 1402, "110": 1418, "111": 1440}
---

**Dave Jones:** Hi, in this video we're going to take a look at a couple of affordable FPGA starter kits to get you into FPGAs. So what I've got here is a couple of basic entry-level FPGA kits.

**Dave Jones:** Three on the top here are sub $100 boards that allow you to get up and running. This is the uh Papilio 1 uh Xilinx based FPGA board. Similar sort of style to an Arduino thing.

**Dave Jones:** You can connect wings on here and stuff like that. You can even get an Arduino compatible softcore processor to program inside this thing. And this thing's under 50 bucks and it's got a you know a decent Xilinx FPGA on there.

**Dave Jones:** Then we've got this Terasic DE0 Nano board. And this one is an Altera based board and it's a nice little compact thing like that. This one is $89 US.

**Dave Jones:** I think it's as little as $49 for US students. So that one's quite reason- quite reasonably priced. Then we've got the Digilent Basis 2. It's an sorry a Xilinx compatible like the Papilio 1.

**Dave Jones:** It's got a Spartan 3E same as what's on the Papilio there. And uh yeah, it's a neat little unit. This one only costs around $79 or $59 student price.

**Dave Jones:** So not bad at all. It has a VGA output as we'll take a look at. And then we have a higher end one which is the MicroZ uh board and it's Xilinx partner with Avnet.

**Dave Jones:** And yes, this is the exclusive Dave Jones edition. Beauty. If you're going to get this, get the Dave Jones edition one. Trust me. And this is basically a Xilinx Uh, it's not one of their Spartan ones one of their low-end Spartans.

**Dave Jones:** It's one of their uh really modern uh high-end zinc ones. And this is an incredibly powerful board, $199 uh for this board, but it can run embedded Linux. And you know, I think it comes actually pre-programmed with embedded Linux.

**Dave Jones:** And it's got Ethernet and the whole works. So, quite a really powerful beast and we'll take a a look at that in more detail as well. So, take a look at the uh Papilio board here.

**Dave Jones:** Just an example of what's required bare-bones to get this thing up and running. Uh once again, this is a fairly fine-pitch uh quad flat pack chip. So, it's not something you can just immediately mount on a breadboard, for example.

**Dave Jones:** We need an external oscillator to make the damn thing work. Then we need our platform flash memory connected to it so that uh it can store our programs when we remove our power.

**Dave Jones:** Uh we've got multiple voltage regulators up here. 1.2 V, 2.5 V, 3.3 V. They're for all the various core voltages required by this particular Xilinx Spartan 3 FPGA. And then we've got the uh USB interface here.

**Dave Jones:** I mean, you don't necessarily need this. You could have just had a JTAG header on there and just plugged it straight in and then used an external uh JTAG programmer for that.

**Dave Jones:** But this one But all of these boards have uh USB built in so you can just connect them straight up to your PC. And that's what you want. And if you do want to program these things yourself, which yeah, it's a great thing to do.

**Dave Jones:** I highly recommend it. Just watch out for all the traps for young players. You can get um the external uh programmers. In this case, JTAG programmer. Xilinx uh do this one, the Platform USB cable.

**Dave Jones:** This one's uh fairly uh cheap on eBay, not as cheap as the Altera ones. This is not a genuine one. This is actually a uh rip-off one. And so is this Altera uh USB uh blaster one.

**Dave Jones:** You can get these for like I think this one is like something crazy like $8 delivered something ridiculous like that. So, Altera does seem to have a lower entry point price as far as the JTAG programmer tool goes.

**Dave Jones:** That it supports that is supported by the official manufacturer software. Now, the two major players in the market, well, in fact, all the FPGA players in the market, but the two main ones are Xilinx and Altera.

**Dave Jones:** They all offer free tools and as you can see on this basis, too, it's advertised that you can use the free CAD tools from Xilinx. In this case, the ISE WebPACK.

**Dave Jones:** It's a massive download, of course, but it is completely free and Xilinx have the and sorry, Altera have their version as well for free. But, the free versions of the tools don't necessarily support the higher-end FPGAs.

**Dave Jones:** So, that's why if you're going to get one of these boards, you have to ensure that it is suitable for use of what whatever FPGA you choose, you have to en- sure that it's compatible with the free tools.

**Dave Jones:** Otherwise, you'll be paying a fortune for the FPGA tools. Now, this Papilio 1 is an open-source hardware type platform, but it is very basic. It's so I don't think it's going to be as sort of, you know, hand-holding as some more of the sort of kits from more of the mainstream providers.

**Dave Jones:** Brief look at the DE0-Nano here. I rather like this really compact little form factor. Nice 0.1 in headers on here and well, that's actually there's some stuff on the bottom, memory and bypass and things like that.

**Dave Jones:** And also another header on the bottom to plug it into stuff. Mounted on standoffs. Neat little self-contained unit. And as I said, it's got a Altera Cyclone IV FPGA.

**Dave Jones:** It's got a USB interface. It's got an E-squared PROM. It's got What have we got? Four DIP switches. It's got an accelerometer built on. Fantastic if you're into accelerometer stuff.

**Dave Jones:** It's got an ADC in there. What else have we got? We've got two push buttons, 40-pin GPIO headers, 32 megabits of SD RAM. Fairly chunky amount of SD RAM in there.

**Dave Jones:** And it's got a serial PROM to program the well, to hold the configuration program and eight LEDs. So, not a bad little board. I don't mind that at all.

**Dave Jones:** The other really good thing about the DE0 Nano, it comes with the software. So, you don't have to download it. And most importantly, the Altera complete design suite, the free package.

**Dave Jones:** Cuz this is absolutely huge. As you can see, it's on a DVD. It can be multi-gigabytes to download the various packages from the manufacturers. This one supplies it for you.

**Dave Jones:** The others don't. And the Basis 2 board, it's much larger than the DE0 Nano. There's a comparison there. 0.1-in female headers along here. So, not as many IO as you get on the DE0 Nano, but you do get more nice big chunky switches and buttons.

**Dave Jones:** We've got a four-way LED display here. You can have it as a clock. What I really like is that it's got a VGA output. And that's really quite nice.

**Dave Jones:** Cuz one of the best examples for an FPGA is being able to interface to a VGA monitor. Cuz you can pick up VGA monitors from the garbage room for nothing, right?

**Dave Jones:** People throw these out. They make great interfaces for FPGA projects. So, this one allows you to experiment off the bat with that. So, that's really quite good at the expense of some IO along here.

**Dave Jones:** But yeah, once again, it's got the platform flash memory, multiple clock sources once again. Xilinx Spartan 3E this time instead of the Altera part. And it's got a PS2 port on it as well.

**Dave Jones:** And you can get modules that actually plug into this. This was I'm not sure of what type or how much they are, but anyway, you can plug those suckers in, but I really like this one because it's got a VGA output you can experiment with and presumably some example programs to drive the VGA.

**Dave Jones:** This much more upmarket MicroZ board is a $199 one. Um, unfortunately, it doesn't really come with any IO, like usable IO. Of course, it's designed to have, you know, embedded Linux.

**Dave Jones:** It uses the high-end Zynq FPGA. Really neat. It's got a built-in ARM 9 processor. Really powerful thing. Runs embedded Linux. I think it's already pre-programmed with it out of the box.

**Dave Jones:** We have to power it up and have a look. Ethernet interface, of course, but all of the IO here is on the bottom. It's got an SD microSD card on the bottom.

**Dave Jones:** All the IO here is designed to plug into a rather expensive IO board, which I don't have. Wasn't provided with this thing, which is being a bit of a bummer.

**Dave Jones:** It's a really big board, which I'll post a photo of right now. That just breaks out all of the IO into handy usable stuff. So, if you're going to get one of these, I'd recommend you spring the extra and get that IO board.

**Dave Jones:** I stand corrected. This sucker contains two, not one, but two 1-gig 1-GHz, folks, ARM Cortex-A9 hard processor cores in there as well, of course, as all the FPGA fabric as well.

**Dave Jones:** It's got two 1-meg sample AD converters as well. So, really powerful board, that one. So, if you're looking to run something inside a traditional as it like inside a traditional processor, you know, these hardcore ones are better than, you know, the soft cores you can program into any almost any FPGA as long as it's got enough enough gates inside, enough room in there.

**Dave Jones:** You can program Um, uh, different types of softcore processors into these things, but you know, something like this dedicated, um, 9 1 GHz processor in there cannot be beat.

**Dave Jones:** Uh, really, it just absolutely kills any softcore processor that you can, uh, program into any other FPGA fabric. And also, you don't want to piss away your FPGA fabric inside these things with the softcore processor.

**Dave Jones:** Like you might put a softcore processor in here, but it might use, I don't know, um, just as a guess, you know, it might use that 10 or 20% of your FPGA space depending on, uh, what type of processor it is.

**Dave Jones:** Don't want to waste it. And they're usually not going to be very quick. Like the FPGA itself, uh, for example, might be very, very quick, but when you, uh, compile in, not the correct term, but we'll use that today, um, an FPGA, uh, core, softcore into this thing, it can't run, you know, at nearly that speed.

**Dave Jones:** You can get them to run at tens of MHz, 50 MHz, maybe. So, this certainly won't be a, uh, complete tutorial in, uh, how to, you know, set up and run these things.

**Dave Jones:** I'll, uh, basically won't uh, show you anything. I'm just going to, uh, install it and get them running. And that's the whole idea. How easy is it to get these things running?

**Dave Jones:** I'll just tell you in the end. I won't show you all the horrible steps to it. So, we'll start out with the DE0 Nano and, uh, that of course has the Altera, um, Cyclone part on it.

**Dave Jones:** So, we're going to install the, uh, thankfully, the, uh, software comes on that, uh, DVD. We didn't have to download it, however big it is, however many gigabytes. We're just going to install that.

**Dave Jones:** So, here we go. Install free package and well, see what pops out the other end. When you install it, uh, you have the option to install that Quartus II.

**Dave Jones:** You have to install that. It's the with free web edition. It is the actual suite of tools for all the FPGA stuff. So, there's no getting around that, but you can also install the ModelSim, uh, as well.

**Dave Jones:** And that's just, uh, simulation stuff. And most beginners probably don't need ModelSim. So, if you want to save the 2.7 gig, you certainly can. And that only took 23 minutes.

**Dave Jones:** That wasn't too bad, I guess. Can be a lot worse than that, trust me. And well, no, I don't wish you to talk back enable sending talk back. No, go away.

**Dave Jones:** Anyway, um it's finished and it installed, as you can see well, it installed all the different families down here, not just the uh Cyclone 4, I think, which we needed.

**Dave Jones:** Installed, you know, Stratix, real high-end stuff, Area, and all those. What the FPGA is this garbage? The software install has now started thrashing the CD drive and locked up.

**Dave Jones:** This was after it said it installed and everything was hunky-dory. And this just goes on and on and on forever. You got to be me. Ah. And on the other CD that comes with it, uh there's no install file or anything like that.

**Dave Jones:** There's just uh some subdirectories with all the stuff. There's uh various uh demonstration programs. Oh, look, my first FPGA. That sounds neat. There's all the uh uh files for the um Altera Quartus uh stuff, the ADC stuff, and yeah, uh there's the uh accelerometer, by the looks of it.

**Dave Jones:** So, that one looks uh quite neat. And then we've got uh the data sheets with the um uh all of the various uh parts. That's pretty handy. And uh we got the schematic.

**Dave Jones:** Fantastic. And we can load that up. And bingo, there it is. And we can have a look at uh how they've implemented this thing. There we go. Not sure what package they've used to uh use that.

**Dave Jones:** It's not Altium. But uh yeah, once again, they've done all the separate pages. This is very common for these FPGA vendors. It It's sometimes it's good, sometimes it's not so great.

**Dave Jones:** That's how they've implemented the uh configuration prom and the JTAG interface, and everything's just spread over a couple of pages here. So, that is a little bit annoying, but uh But there you go.

**Dave Jones:** They give you all the complete schematics, which you will need to um interface this thing. And you notice here's all the uh power supplies, 3.3 V, 2.5 V, 1.2 V for the various cores on the FPGAs cuz these FPGAs can be a real pain in the ass.

**Dave Jones:** Now, according to the quick start guide, we can just run one of the demonstration programs here, a batch file in here after installing our uh Quartus II software, which we've done, and uh and Bob's your uncle, it should download and everything's right because these FPGA tools are actually command line tools.

**Dave Jones:** You don't have to use the GUIs. Um and in fact, you know, that's how a lot of uh third-party tools integrate with these FPGA tools is they're all command line driven.

**Dave Jones:** So, let's go in there and try it. Uh G sensor, here it is, demo.bat. And cuz there's no batch file in there, so we should have to just run test.bat, I guess.

**Dave Jones:** Let's see if it works. Does it work? Demo. No. What? There was some red thing there, I saw it. Oh, fail. And that error message was that it hadn't detected my uh USB Blaster because this board actually has that USB Blaster uh functionality compatibility uh built in to the board as I showed before you could buy for like $8 that external programmer.

**Dave Jones:** It's built in, but look, it um yeah, it just didn't install properly. Oh, it's supposed to do that when you install the Altera Quartus software. You've got to be kidding me.

**Dave Jones:** All right, I manually installed the drivers. They're in the usual uh location in the Quartus software under /drivers/quartus/drivers/usbblaster and did the usual Windows thing. So, one more time for the dummies, here we go, test.bat.

**Dave Jones:** Woohoo! Look. It's doing it. It's doing it. It's doing the business. Well, it's doing something. Uh my LEDs are still uh flashing. By the way, that um uh LED um you know, Knight Rider type thing, wait, um came uh pre-installed with the board, which is really quite nice.

**Dave Jones:** Oh, there we go. Looks like it's done. It worked a treat. Beautiful. I don't even get over that driver issue. Not a problem. Thumbs up. And yeah, check it out.

**Dave Jones:** We are in a command line interface. Man, look I can go CLS and it actually clears the screen. Hello. Command not found. Now, this uh, certainly won't be a tutorial on how to use Altera Quartus II, that's for sure.

**Dave Jones:** I just wanted to show that we can actually load our project into that. And all I did was double click on the project file within that uh, demo subdirectory, that accelerometer sensor we just ran and bingo, here it is loaded into Quartus II and there's our source code.

**Dave Jones:** Fantastic. And if you want to do, of course, we can just modify our demo program, then we can go over here and actually uh, compile the thing. We can analyze, synthesize, fit and then program the device down there.

**Dave Jones:** So, we can just double click on analysis. Do you want to run the task again? Yep, here we go. It's going to go through analysis and synthesis and yeah, it was successful.

**Dave Jones:** There's six warnings, not a problem. So, it all just works. Total logic elements, there we go. Used only only used 189 logic elements. Total uh, dedicated logic registers, total registers 112, not much at all.

**Dave Jones:** And then we can do the same thing for the place and route. Here we go. I'm uh, it's almost complete there and should successful. Four warning error messages. Total logic elements used, look, less than 1% of what that FPGA is capable of.

**Dave Jones:** Total pins, all that sort of jazz. Beautiful. Total memory bits and total PLLs used. It's using one PLL. Uh, there's four uh, phase lock loops within this FPGA. And uh, there you go.

**Dave Jones:** That's a handy little summary. And there's a million different uh, things and resources we can check and things like that. One neat one is the resource utilization by entity here.

**Dave Jones:** You just go into analysis and synthesis and it can give you all this sort of info. But, this basically tells us that how many logic elements in our FPGA are being used by each particular Verilog routine there within our program over here.

**Dave Jones:** So, that's rather neat. Let's try a more media project. I've opened up that Nios embedded core demo program, and I've done the analysis and place and route on that, and it didn't take that long, and look, here it is.

**Dave Jones:** Summary of that after place and route. I've only used 26% of our you know, cheap ass FPGA to run that soft core. It's running external DRAM and everything else.

**Dave Jones:** So, that's not as pretty good, you know, on a low-end cheap ass board like this. I like it. Now, there's a million and one neat different things we can do with all the tools built into this thing, but one I really like is the power analyzer.

**Dave Jones:** Now, after we run the assembler down here, then we can go up into our tools, and sorry, there's a whole bunch of tools. There's million and one tools you can do.

**Dave Jones:** Logic analyzers, signal tapping. Oh. Good stuff. Anyway, let's go to the power play power analyzer tool. And we can run that. I've already run that, and we can go to the report here.

**Dave Jones:** Hello, McFly. Come on. Go into the report. There it is. It simulates the whole thing. Tells us how much power that program is going to be running. Here is total thermal power dissipation 282 mW to run that Nios soft core processor there.

**Dave Jones:** So, you know, that's pretty neat. And here's a summary of the results. 350 mW total thermal power dissipation for that Nios core there, but we can go in and we can get all sorts of things.

**Dave Jones:** Total power dissipation by block types. We can get power dissipation by hierarchy here. Come on. This is slow as a wet week. Man, I'm only running a 2 GHz core i7 here.

**Dave Jones:** I'm not sure what's going on. Maybe it's my screen capture in the background, but all these breakdowns of all the power dissipation. Fantastic stuff. And you can even get an estimate of what current is going to be drawn here from each of the uh individual power rails.

**Dave Jones:** The like the IO, that was based on a I think it was a 12 and 1/2% uh toggle rate or something like that. So, it's just an estimation, but if you see AVCC D, the internal power dissipation, the static current, fantastic.

**Dave Jones:** And of course, one thing you're definitely going to want to well, you're forced into um when you're doing FPGAs, one of the big things is of course assigning pins cuz the pins can do many different functions.

**Dave Jones:** So, uh Altera Quartus II has the pin planner here. And um this one's obviously already loaded up for this particular project and this particular device here, the EP4C blah blah blah.

**Dave Jones:** And you can see the for the BGA part, all of these ridiculous um symbols for the pin outs. But you can go in there and you can form groups, the DRAM, where the DRAM's connected to and the GPIOs and the keys and the LEDs and the switches.

**Dave Jones:** All for And you can create your own new groups and things like that, which then you can assign into your uh into your Verilog VHDL program to uh you know, to access your IO and things like that.

**Dave Jones:** So, here's all our pins, all of our individual pins, and we can set the IO standard here. We can change all that and we can do all sorts of weird and wonderful and wacky stuff with our pin IO, but that's man, there's just IO configuration in FPGAs is a 2-hour tutorial in its own right.

**Dave Jones:** And there's countless other stuff as well in this in both the Altera and the Xilinx tools and the tools from other lesser manufacturers as well. And yeah, I could do a million videos on these and still not cover them.

**Dave Jones:** As you can see, these are very very complex tools, these FPGAs. And you know, pretty much if you're doing it at this sort of level using these vendor tools as they're called, then you know, you have to learn how to do these things.

**Dave Jones:** But, uh by loading in these example projects and getting everything up and running, then it takes, you know, and then working backwards from that, that takes all at least the uh you know, the the Hello World grief out of it cuz FPGAs are incredibly difficult and complex just to get, you know, the blinky LED going, really.

**Dave Jones:** But, I haven't touched on one of the awesome things that comes with this DEO Nano. If you want to create a new project from scratch, how do you do it?

**Dave Jones:** Well, with the uh disk here comes some tools and they've got a control panel that allows you to control stuff, but there's system builder stuff. Let's give this a go.

**Dave Jones:** Here it is. Look at this. Teras- Terasic? Don't know how to pronounce that bloody name. It's a bit hard, but here's the DEO Nano FPGA board and you can EV blog, let's call our project here.

**Dave Jones:** And what do you want to use? I want to use a clock, I want to use a couple of buttons, I want to use SRAM, I want to use everything.

**Dave Jones:** And what Oh, look, 5 megapixel camera. Looks like they've got some modules that you can whack on to the header. That's pretty neat. 4 and a half uh 4.3-in LCD and touch multi-touch LCDs.

**Dave Jones:** Presumably, you can just buy those, plug them in. Anyway, um the whole idea is this will generate a code template for you that you can work from and take all that really annoying pin configuration stuff and things like that out of the equation.

**Dave Jones:** So, here we go. Let's try it. I haven't tried it yet, but let's generate GPIO header. There we go. Well, you know, we've got none. Let's just go GPIO default, shall we?

**Dave Jones:** And let's just go generate. And it will generate uh Here we go. I'll save it and then we'll try and do something. And here it is. Code generated. EV blog and bingo, there's our code.

**Dave Jones:** Let's check it out. We can load that. Just load up the uh Quartus project file here and we're in like Flynn. And here is our project all with our template already set up.

**Dave Jones:** Here's our DRAM configuration, the LEDs, key switches, everything is set up ready to go. Then we can just add our own code on top of that. Beautiful. And then we've got this bit of a wanky control panel software that comes with it, but it just allows you to have a basic play.

**Dave Jones:** It just talks to the board and then just allows you to you know switch the LEDs off and on and you know touch the switches and things like that and you know write stuff to the memory and play with the accelerometer.

**Dave Jones:** There it is. We can muck around and ADC bugger off a vast go away. And then you know and then we can just you know play around with it but really you know that's not a huge value add that's just more of a toy but that system builder stuff that is a real Bobby dazzler let me tell you that is essential for beginners to build to generate those

**Dave Jones:** code templates to get you up and running cuz nothing is worse than your FPGA that just you know that just does nothing. As a beginner you just you know try to get and configure all your pins and just get all the assignments and everything working just so the damn thing compiles and that can be a real hurdle whereas that code generator huge step.
