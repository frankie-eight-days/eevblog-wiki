---
video_id: AZInaAaDlvE
title: EEVblog #635 - FPGA's Vs Microcontrollers
url: https://www.youtube.com/watch?v=AZInaAaDlvE
source: youtube-asr
timestamps: {"0": 1, "1": 18, "2": 40, "3": 56, "4": 67, "5": 79, "6": 98, "7": 111, "8": 123, "9": 134, "10": 142, "11": 153, "12": 171, "13": 189, "14": 201, "15": 215, "16": 229, "17": 246, "18": 266, "19": 277, "20": 288, "21": 300, "22": 315, "23": 324, "24": 333, "25": 342, "26": 353, "27": 367, "28": 377, "29": 392, "30": 406, "31": 426, "32": 441, "33": 464, "34": 484, "35": 501, "36": 518, "37": 528}
---

**Dave Jones:** Hi, in this video we're going to take a look at a couple of affordable FPGA starter kits to get you into FPGAs. But before I jump into that, I thought I'd just do a quick little primer here on exactly how easy is it to hook up and use an FPGA?

**Dave Jones:** As I mentioned in my previous videos, which I'll link in, the answer is not very easy at all. Take for example, your classic microcontroller here, your PIC, your AVR, your MSP, whatever it is, pretty easy for a beginner to use, even if you don't use something simple like like a development board like an Arduino, for example.

**Dave Jones:** They're really easy. You get your little PIC or your AVR chip, you stick it on your breadboard, you hook up 5 volts to it, and you can flash an LED just using a simple low-cost program which plugs into your USB port, couple of wires come over, goes into your chip, and Bob's your uncle.

**Dave Jones:** Really easy to do. They've got building oscillators, like there might be a reset pin on here. You often you don't even need to worry about that cuz it's got an internal pull up.

**Dave Jones:** There's no other configuration stuff. Internal oscillators allow the thing to work, run your program, and you can get a flashing LED blinky circuit up and running very easily and cheaply.

**Dave Jones:** But is it the same for FPGAs? Nope. Let's take a look at why. So you can't just do the same thing you can with the micro here. Load on your breadboard, hook up your 5-volt supply, hook up your USB programmer, JTAG programmer to the thing and get it to blink your LED.

**Dave Jones:** It's not that easy like it is with the microcontroller. Yes, you can get simple cheap little JTAG programmers, which I've done a separate video on that will be linked down below how the JTAG programming system works for FPGAs.

**Dave Jones:** And but you can get these cheap programmers and but it doesn't work the same as micros. Why? Because of quite a few things which we're going to take a look at.

**Dave Jones:** First of all, they come in a usually come in pain in the ass BGA packages, not a simple friendly DIP package which you can just plug into your breadboard.

**Dave Jones:** Maybe some of the low-end ones might come in a quad flat pack but it might be you know 100 pins or something like that, real pain in the ass.

**Dave Jones:** So right off the bat there, you're going to have to melt this thing on some sort of adapter board at a bare minimum to get the thing in a usable format that you can connect all your stuff up to.

**Dave Jones:** The next thing is that these things are volatile. What that means is that they don't have flash memory in them like your microcontroller does. So yeah, you can just program it via the JTAG programmer but as soon as you remove the power, poof, your design's gone and you have to download it again.

**Dave Jones:** Hopeless. So we'll take a look at that. Next thing is is that there there's no internal oscillators in these things like there are on your microcontroller. So once again, you've got to add in an external oscillator just to get the damn thing working.

**Dave Jones:** And the next thing is that they're generally not 5-V compatible. So you can't just hook them up to your regular 5-V power supply like you used to. Heck, some of them you can't even hook up to a 3.3-V supply.

**Dave Jones:** They often require multiple uh voltages for internal core voltages and stuff like that for some of your higher-end ones. Some of your lower-end ones, no, you can just get away with single 3.3 but it's something to be aware of.

**Dave Jones:** These things aren't easy. We haven't even gotten to all the configuration pins yet. So here's just some of the crazy stuff you might need to add in red here around your basic circuit which you didn't have to add for your microcontroller here.

**Dave Jones:** This is like for a uh Xilinx FPGA, for example. It's not bang on, it's just a rough example. We'll do a screen capture in the middle of exactly what you need for a basic uh JTAG flash uh boot configuration for a typical FPGA.

**Dave Jones:** But, as I said, it's going to uh change based on the vendor, based on the uh family of FPGA. So, you have to read the documentation, the very extensive documentation, as we'll see, for the individual for the exact FPGA which you're using just to get the damn thing up and running.

**Dave Jones:** So, you've got your USB simple little USB uh JTAG programmer here, but you now need a second chip here, which is your configuration flash memory, which stores all the information for your FPGA.

**Dave Jones:** Then, you've got to hook up that correctly. You have to tie it into the JTAG system that I've done the video on so that it uh forms a loop uh through the JTAG chain there, it's called.

**Dave Jones:** And, you have to get that right. If you screw that up, it's just not going to work. Um then, you've got all the uh configuration lines, the data, init, reset lines, the clocks, uh the done line, all that sort of stuff.

**Dave Jones:** You've got to hook that up correctly. If you screw up one of those lines and you don't get it right, it's just not going to work. And then, you've got various uh VCC voltages for your different banks, which I've done a separate video on before, linked down below.

**Dave Jones:** And, you've got weird pins like HSWAP enable. What does that do? Well, you've got to read the documentation to find out, don't you? Uh you've got mode pins down here, for example, on these Xilinx FPGAs.

**Dave Jones:** You've got to put those in a certain configuration to power the thing up. Or, sometimes you don't now with the more modern families. They've got a separate JTAG interface.

**Dave Jones:** Uh but, there's the thing is, there's a lot of stuff you got to do. This uh flash over here has to have the same JTAG programming voltages, everything else.

**Dave Jones:** And, if all that stuff isn't done, then, you know, your FPGA is just not going to work. It's going to be You're going to be sitting there scratching your head and saying these FPGAs suck.

**Dave Jones:** I'm going back to my micro controls. But, basically, why I'm doing all this and telling you about it is because it's not easy to do for a beginner. So, a beginner shouldn't be mucking around with all this stuff.

**Dave Jones:** You should get one of these demo kits that we're going to take a look at that have all this stuff already done for you so and already hooked up so you don't have to worry about any of this stuff.

**Dave Jones:** It just, you know, somebody's done all the hard work to figure out how to get this thing to boot up and make it work. And just to show you that I wasn't kidding, here is the Spartan-6 FPGA configuration user guide.

**Dave Jones:** This is just for the configuring and getting your FPGA up and running and doing what you want. And there's a different one of these for each different Xilinx family, and the other manufacturers will also have similar types of guides.

**Dave Jones:** And this guide is, well, 164 pages long, folks. That is just to get the FPGA configuration doing various things. And granted, there are lots of different ways that you can configure FPGAs, but, you know, look at this sort of stuff.

**Dave Jones:** It's configuring all sorts of high-speed priority options, JTAGs, master-slave modes, non-multi boot, safe upgrade, blah blah blah, select map data loading, man, you name it. Look at it. Unbelievable.

**Dave Jones:** But, let's go down here. You don't get down CRC configurations, daisy chain, man, it's incredible. But, let's go down to page 26, shall we? I think it's on. Get down to page 26 here, and bingo, here is our basic configuration that we're going to use for a uh Spartan-6, for example, and that's how to hook it up.

**Dave Jones:** There's the FPGA, there's the uh platform flash memory, as they call it, the external flash memory. They've got the daisy-chaining of the uh JTAG there. You can see like TDI coming in, TDO going out into TDI of the flash, TDO going back out to your um Xilinx cable header here for your uh programmer.

**Dave Jones:** And there's those mode pins there. There's HSWAP enable, the various bank voltages there and there. And look, if you don't get this VCCOUX pin, if you forget to hook that up, then well, your JTAG's not going to work, and you know, the thing's just going to sit there and do nothing.

**Dave Jones:** And you're going to be scratching your head thinking it might be a software problem, or I don't know, something going on. So, there's all sorts of things you have to hook up just to get your FPGA programmed, working, and boot up, just so you can run that blinky LED program.

**Dave Jones:** It's incredible. And there's still a hundred and something pages left. Oh my goodness. But most of the time, you don't have to look at all this, because you're not going to be using the more obscure modes.

**Dave Jones:** But anyway, that's how complicated it is.
