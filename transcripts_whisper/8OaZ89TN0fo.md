---
video_id: 8OaZ89TN0fo
title: Guest Video: OpenTechLab - IcoBoard FPGA Experiments
url: https://www.youtube.com/watch?v=8OaZ89TN0fo
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 18, "2": 39, "3": 53, "4": 61, "5": 108, "6": 128, "7": 145, "8": 168, "9": 185, "10": 198, "11": 214, "12": 231, "13": 255, "14": 274, "15": 295, "16": 322, "17": 348, "18": 364, "19": 377, "20": 394, "21": 411, "22": 424, "23": 447, "24": 465, "25": 483, "26": 496, "27": 508, "28": 522, "29": 538, "30": 552, "31": 566, "32": 579, "33": 594, "34": 614, "35": 634, "36": 648, "37": 661, "38": 674, "39": 693, "40": 708, "41": 719, "42": 736, "43": 749, "44": 770, "45": 787, "46": 805, "47": 823, "48": 842, "49": 856, "50": 871, "51": 886, "52": 907, "53": 922, "54": 940, "55": 961, "56": 979, "57": 1006, "58": 1023, "59": 1047, "60": 1060, "61": 1075, "62": 1089, "63": 1105, "64": 1126, "65": 1144, "66": 1167, "67": 1191, "68": 1211, "69": 1228, "70": 1250, "71": 1268, "72": 1289}
---

**Dave Jones:** Hi, I'm Joel from the Open Tech Lab and if you're seeing my face it's because Dave has gone away and he's let me hijack a spot on his channel. Now, if you're checking out my content for the first time, basically I focus on the lowest cost and most powerful tools that I can talk about to get into engineers' hands.

**Dave Jones:** So, I'm really interested in some of the devices that are produced out of China. Some of them are ugly, some of them are bad, but some of them are quite good and they're usually quite powerful within certain limits. And so, this is something to me that's well worth exploring and they're always available at a really, really affordable cost, which to me is really awesome because it lowers the barrier to entry.

**Dave Jones:** Now, the other focus of this channel is on open source and the reason for that is that, to me, the world of open source is like a massive cavern of technological wonders, a massive workshop of tools waiting for people to pick up and use them.

**Dave Jones:** So, I focus heavily on Linux. Everything in my videos is always done with open source and even the production of the videos themselves is done with open source. Now, if you're interested in finding out more, check out my little channel and if you like it, subscribe.

**Dave Jones:** But without further ado, let's get going with the main video. Hi and welcome to the Open Tech Lab. So, I've got some boards in the mail to share with you today sent to me by Edmund Hummenberger all the way from Austria and he sent me a couple of boards and the main one is this Ico board, which is an FPGA board featuring the Lattice Ice 40 FPGA and it works as a hat for the Raspberry Pi and it's designed to help people get into FPGA development using open source software.

**Dave Jones:** Now, I've spoken about the Ice 40 previously, but just as a recap for the ones that don't know, let me explain exactly what is an FPGA. It's basically a type of programmable hardware inside a chip. So, the structure of the chip is a series of tiles of programmable logic gates connected together with wires and switches.

**Dave Jones:** So, the result of this is that you can program this chip to become any kind of digital circuit just by programming the switches and gates with the hardware design that you want. So, it kind of turns any kind of hardware problem into a software problem, if you will.

**Dave Jones:** Now, the general context of this is that we're living in exciting times when it comes to FPGAs and open source because just a couple of years ago, it was not possible to program any FPGA with open source software. And thanks to the hard work of Clifford Wolfe and several other talented developers, it became possible to program these chips with the Ice Storm toolchain.

**Dave Jones:** And since that time, there have been moves towards getting other open source toolchains working for other FPGAs on the market. So, in this video, we're going to have a little mess around with the EIKA board, see what it can do, and we'll have a little look at the status of the open source FPGA ecosystem.

**Dave Jones:** So, let's have a little look at what we have on this board. So, of course, at the heart of it, we have the Lattice Ice40 HX8K. This is the high-speed variant of the FPGA, and it is the very largest of the whole family.

**Dave Jones:** This has 8,000 lookup tables, hence the name 8K, and these are arranged in a 32 by 32 tile grid, and each tile contains eight logic elements. Now, the FPGA is hooked up to various connectors that you can use if you want to attach things to the board.

**Dave Jones:** We have four of these 51-pin FlatFlex connectors, and you can plug in a FlatFlex ribbon cable and take it off to whatever you want. And also, we have this grid of 0.1-inch holes here that are connected to the same lines as these two connectors on the right, and you can solder things onto the board that way.

**Dave Jones:** And also, we have four of these double-row PMOD connectors, and PMOD is something of a standard for FPGA extension modules, and I'll talk a bit more about those in just a minute. And then on the left, we have two LEDs, one, two, and two little switches as well, which can be useful to give some input and output to your hardware design in the FPGA.

**Dave Jones:** So within this board, there is the option to either load the firmware from the Raspberry Pi or to have it stored within the board itself. So for this case, we have this SPI flash chip, and when the board is configured to load from internal memory, the FPGA will automatically download the firmware out of this flash chip when it powers on.

**Dave Jones:** If we flip the board over to the other side, you can see there's a couple of things here. We have this 8-megabit SRAM. Now, this is an option on the more expensive version of the board, and it can be used to store that 1 megabyte of data, and it can be useful for the FPGA to give it somewhere to store any intermediate data that it happens to be processing through.

**Dave Jones:** And then over here, we have another, a second little FPGA. This is a Lattice Mac X02, and its role is to control the connectivity between the ICE40 underneath here and the Raspberry Pi and the SPI flash. So it basically works as a switch depending on whether you want the ICE40 to load its firmware from the flash trip on the other side or whether you want it to get its firmware from the Raspberry Pi.

**Dave Jones:** Now, the ICO board is compatible with most versions of the Raspberry Pi out there, certainly all of the newer generation boards. The only boards that it's not compatible with is the very early Raspberry Pi original version, model B. And the issue is that this board only has the reduced length pin header here with the fewer pins, whereas the ICO board requires the full length expansion header that you find on this Raspberry Pi model 3B that I have here.

**Dave Jones:** And so we can take this board and just slot this on here, and of course, this would also be possible with the Raspberry Pi 2s and the Raspberry Pi 0s. Now, as an alternative to the Raspberry Pi, I've been sent this board, which is the ICO-US baseboard.

**Dave Jones:** And this is designed for cases where we want to use the ICO board but without involving a Raspberry Pi. So in this case, the ICO board would slot onto the pin header, and then we'd plug this board into the PC through this USB connector.

**Dave Jones:** Now, the idea behind this is that it can be useful when you're developing your firmware. It's quite computationally expensive to compile the hardware designs into the bit stream for the FPGA. It can take the Raspberry Pi quite a lot of time to compile that.

**Dave Jones:** It's perfectly supported and quite a useful thing to be able to do. But you might find that it's a bit quicker to do the firmware development on your PC rather than doing it in the Raspberry Pi. And of course, you could do the development in your PC and then use a network transfer to get the firmware once it's compiled onto the Raspberry Pi,

**Dave Jones:** and then use that to load the firmware into the ICO board. But some of the time, it may be just easier to connect the ICO board directly into your PC and cut the Raspberry Pi out of the setup altogether. So that's one use case for this.

**Dave Jones:** But the second one I find much more interesting, because at the heart of this board, we have the FTDI FT2232H, which is a versatile USB controller chip, slave controller, and it has two ports to it. Now, one of the ports on this thing is going to be plugged up to the FPGA's programming port,

**Dave Jones:** so we can load the firmware using one of the ports of the FTDI chip. But the other port is available for general use in your project. And the FT2232H allows high-speed USB transfers, which means we've got a really, really nice way of transferring data at quite some speed,

**Dave Jones:** hundreds of megabits, between the ICO board and the PC. And I can see that coming in extremely useful. Now, I'm slightly confused about the purpose of these pinholes along here. I'm not really sure what they're meant to do. They seem to be sitting on the bus connection between the FTDI chip and the pin header for the ICO board.

**Dave Jones:** And there are all these zero-ohm links, which means that you can break the connection between the FTDI chip and the pin header. So I suppose the holes might be useful if you want to inject your own signals onto the header here for whatever reason.

**Dave Jones:** Now, I guess this must be a first-generation build of the ICO US baseboard, and you can tell because there's a couple of mod wires on here, and I suppose they'll get that fixed up in the design if they do a second manufacturing run of this board.

**Dave Jones:** But overall, don't be fooled by the mod wires, because actually I am very, very impressed by the build quality of these PCBs. Whoever built these PCBs did a really, really good job. They're beautifully laid out, and the PCB manufacturing quality is really, really good.

**Dave Jones:** The silkscreen is razor-sharp. The tracks are just beautifully sharp on the board. Gold finish on all the pads. And also, there's even a bit of a gold trim along the edge of the PCB just to make it look a little bit more bling.

**Dave Jones:** It looks really nice. This is a great quality board. Now, switching back to the Raspberry Pi, let's see if we can use it to load some firmware onto the ICO board. So here's my setup. I've got the Raspberry Pi running a stock image of Raspbian,

**Dave Jones:** and I've attached a monitor and a keyboard and a mouse so I can control it, and I've got it plugged into the network, and I've got the ICO board plugged in on the top. And as you can see, in the default state, the ICO board already has some test firmware loaded into it.

**Dave Jones:** The firmware is blinking the two LEDs on and off. So now we want to go ahead and build our own hardware design to run on the FPGA, and to do that, we're going to need to get a copy of the Ice Storm toolchain,

**Dave Jones:** which is the series of tools that are required to take our hardware design code and compile it into a bit stream that can be loaded onto the FPGA. Now, to help get started with installing the software onto the Raspberry Pi, there is this helpful getting started guide on the ICO board website,

**Dave Jones:** which lists just four steps that are necessary to go ahead and do that. And the first step in this is a link to a Raspbian Jessie image that you can download, and this image has the Ice Storm toolchain pre-installed into it. So all you have to do is download this image and flash it onto an SD card

**Dave Jones:** and then run it up on the Raspberry Pi. But my critique of this is that it's quite a job for them to keep up to date with the upstream Raspbian project with their images, and already this one is a few months old. And in my opinion, it will be a bit better to start with the stock Raspbian image

**Dave Jones:** and then install the Ice Storm toolchain tools into that. I think that's a little bit better. It's better to start with something up to date, and it's more helpful to know how the software is installed. And it's not a complicated process to install the software.

**Dave Jones:** It just takes a little time for the Raspberry Pi to compile it all. So if you're looking for a quick start, you can just download this image. But to demonstrate how to install the Ice Storm toolchain, I'll just show how to compile the tools.

**Dave Jones:** So our first port of call for installing the tools we need is on the project Ice Storm page on Clifford Wolfe's website. And if we scroll down to about halfway through the page, there is this section here. Where are the tools? How to install?

**Dave Jones:** And the first thing we need to do is install the various prerequisites. And we're going to use the section from Ubuntu here. The prerequisites on Ubuntu are the same as on Debian and on Raspbian. So this is what we need. And then we're going to go ahead and build the Ice Storm tools, then Arachne PNR, then Yosis.

**Dave Jones:** And these three tools together form the Ice Storm toolchain. And I found that building these tools on the Raspberry Pi took about 90 minutes to complete. It's rather a slow processor on the Raspberry Pi compared to a desktop. But 90 minutes is not too bad.

**Dave Jones:** Of course, it would be possible to cross-build the tools on a PC and copy them over to the Raspberry Pi. But that's a lot more complicated to set up. So in this case, it's just quicker to build it on the Raspberry Pi itself.

**Dave Jones:** Next up, we need to get a hold of IcoProg, which is the tool that we're going to use to load the firmware into the Ico board into the FPGA. And the source code for this is contained within this GitHub repository. And I'll link this repository and all the other things in the show notes if you want to follow it up.

**Dave Jones:** And if you scroll down, you can see there's this README file. And this gives us all the information we need on how to install this into the Raspberry Pi. The only thing to be aware of is that it has this section on installing WiringPi,

**Dave Jones:** which is a prerequisite of IcoProg. And if you're using Raspbian, as I am, you can skip this step because WiringPi is already installed by default. And then if we go down to the section on installing IcoProg, the instructions are really straightforward. Just grab the source code from Git and use a makefile to build the source code.

**Dave Jones:** And that's about all there is to it. Now, one thing that's immediately noticeable is just how compact the installation is compared to typical proprietary vendor tools, which usually take up gigabytes of disk space. Whereas, as you can see, the installation I've just done here is taking up a mere 274 megabytes.

**Dave Jones:** And a lot of this is taken up by the databases for the ICE40 FPGAs. But also I found that much of this is being taken up by the size of the Yosis executable. And as you can see, if we do an LS on it, it's taking up 159 megabytes of disk space.

**Dave Jones:** And the reason for this is that by default it's being installed without being stripped, which is to say the debug symbols are bundled into the executable. And they don't need to be there, and they can be stripped out. And it turns out that if we do that, what we are left with is just 6.9 megabytes of executable data,

**Dave Jones:** which is absolutely tiny, and of course it would reduce the overall volume of the installation quite a bit. So the installation is pretty compact now, and it could be even better. So now we're about ready to start building a simple example. And for this test, I just want to build something simple that will flash the three LEDs on and off.

**Dave Jones:** Now, this is a nice standard thing to do with any new chip, flash a few LEDs. And for anyone who's new to FPGA programming, this is going to be a super simple example. But it should give you a bit of an idea of the sorts of things an FPGA can do.

**Dave Jones:** Now, in order to achieve this, we're going to be using the 100 megahertz crystal oscillator input, which is the main oscillator on the ICO board. And we need to divide this frequency down to the point where it will be visible as a square wave of low enough frequency

**Dave Jones:** that we can actually see it properly as a flashing light. And so what we're going to do is we're going to use a binary counter. And a binary counter, of course, counts up in binary, but also it ends up producing a series of square waves

**Dave Jones:** where each bit ends up being half the frequency of the one above it. So the zeroth bit will flash at 50 megahertz, the first one at 25, second at 12.5, and so on and so on and so on down until we get 6 hertz, 3 hertz, and 1.5 hertz, which will be a nice speed to have the LEDs flashing at.

**Dave Jones:** So let's go ahead and start writing some Verilog. So I've created an empty directory, so now we can go ahead and pop up a text editor and start writing our code. So this file is called top.v, and it's called that because it's going to contain our top module,

**Dave Jones:** which will encapsulate the whole FPGA design. And I'm going to define some inputs. It'll take a clock input, and I will define the LED outputs. And I'm going to define these as a three-bit word so that we can treat these three LEDs as a group.

**Dave Jones:** And I'm going to close out the module like this. And now let's define the content. So I'm going to define a 26-bit register going from bit numbers 25 down to zero, and I'm going to call it counter. And then I'm going to assign the top three bits of that register to the LED wires.

**Dave Jones:** So let's do that. And I'm going to assign bits 23 up to 25 to those LED pins. And now we're almost done. We just need to make the counter count up with the clock edge. So I'm going to create an always block here, and I'm going to say always.

**Dave Jones:** When the positive edge of the clock occurs, then we will increment the counter by one count. Now, with these always blocks, if you have more complexity involved, you typically wrap it around with a begin and end. But in this case, because we've only got one line to place inside the always block, we can just do it as a nice one-liner just like that.

**Dave Jones:** Next up, we need to define our pin assignments. So I'm going to create a file called demo.pcf, which will contain the constraints of our design. And I'm going to set up the various IOs. The clock signal comes from pin R9 on the device.

**Dave Jones:** The LEDs come from three different pins, so we have to assign LED 1 to C8. We have to assign LED 2 to F7. And we have to define LED 3 as being attached to pin K9. And all of this information is listed on both the IcoBoard website and on the schematic.

**Dave Jones:** Now, that is all we need for our source code, and our design is complete. Now, to save time, I've gone ahead and pre-created the makefile that we're going to need to build the bitstream from our source code. So let's go ahead and run that.

**Dave Jones:** Now, the build process is not ever so quick on the Raspberry Pi. It has not ever so much computing power. But also, our design is extremely simple, so it just takes a couple of seconds to complete. And we just have to wait a moment, and there we are.

**Dave Jones:** We have the results of the build. We've got a few files. But the most significant among them is the file demo.bin, which is the bitstream that we need to load onto the FPGA. Okay, so now we're going to watch the board as we load in our design.

**Dave Jones:** And as you can see, the default design has these two flashing green LEDs, as I mentioned. And the reason for that is that there is a firmware pre-programmed into this flash chip. And the FPGA, when it starts up, the first thing it does is read this flash chip to load the design into itself.

**Dave Jones:** So when we reconfigure the design with this design that we've just synthesized, we're not going to reprogram the contents of the flash chip. We're just going to update the contents that's running live in the FPGA. And to do that, we're going to run the icoprog tool with the "-p'' option, and we're going to type in our synthesized binary data.

**Dave Jones:** And let's run it. And there we have it. The three LEDs are flashing just as we designed them to. So all the code we wrote has now come to life. Now, to help make the design that we've implemented a bit clearer to understand, there is this extremely useful Ice40 layout viewer tool written by Christian Nielsen.

**Dave Jones:** And this is a web-based layout viewer that allows us to load any ASC file. We can upload this file, which is a product of the synthesis process, and it will visualize that file on this canvas. Now, what we're seeing here is a representation of the structure of the FPGA, where every single one of these squares represents one of the tiles in the FPGA.

**Dave Jones:** And the purple tiles are the normal logic and flip-flop tiles. The yellow tiles are RAM tiles. And the turquoise tiles around the outside are I-O tiles. Each of these contains a physical connection to two physical pads on the device. Now, if we were to want to see every single wire inside the device, we could check this draw all spans box.

**Dave Jones:** But this would slow my browser to a crawl because it takes an extremely large amount of drawing effort to try and draw every single wire because there are thousands of them. So, for the most part, we're going to leave that unchecked and just visualize the parts of the design that are actually in use right now.

**Dave Jones:** And if we have a look here, you can see that there are four I-O tiles in use. Each of these has half of the pads that are connected to these, one pad each actually in use. And if we hover over this one, we can see this is the clock 100 megahertz net.

**Dave Jones:** And this is drawn a bit strangely because this pad is connected directly through to the global clock routing net, which is a big net that connects off to every tile inside the FPGA. And then these other three wires, one, two and three, are the three wires that go out to the LEDs to their respective pads.

**Dave Jones:** And each of these connects into this structure that's been implemented in the middle here. And if we zoom in on this part of the design, we can see the 26-bit counter has been implemented using these six logic blocks. And you can see in the middle, we have something quite conventional looking.

**Dave Jones:** It looks rather like we'd expect a counter to look like. The lower two bits are a bit weirdly implemented, and I will leave it as an exercise to the viewer to figure out why it's been implemented this way or how it works. But for the most part, what we've actually got here is pretty straightforward and exactly represents our design.

**Dave Jones:** Well, that concludes the first part of this video, and as you can see, we're only just getting started. So check out the second part of this video, and I've got some really cool demos to show the sorts of things that's possible with this board.
