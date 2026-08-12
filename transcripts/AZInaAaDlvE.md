---
video_id: AZInaAaDlvE
title: EEVblog #635 - FPGA's Vs Microcontrollers
url: https://www.youtube.com/watch?v=AZInaAaDlvE
source: youtube-asr
---

**Dave Jones:** Hi, in this video we're going to take a look at a couple of affordable FPGA starter kits to get you into FPGAs. But before I jump into that, I thought I'd just do a quick little primer here on

**Dave Jones:** exactly how easy is it to hook up and use an FPGA? As I mentioned in my previous videos, which I'll link in, the answer is not very easy at all. Take for example, your classic microcontroller here, your PIC, your AVR, your MSP, whatever it is,

**Dave Jones:** pretty easy for a beginner to use, even if you don't use something simple like like a development board like an Arduino, for example. They're really easy. You get your little PIC or your AVR chip, you stick it on your breadboard, you hook up

**Dave Jones:** 5 volts to it, and you can flash an LED just using a simple low-cost program which plugs into your USB port, couple of wires come over, goes into your chip, and Bob's your uncle. Really easy to do. They've got building oscillators, like

**Dave Jones:** there might be a reset pin on here. You often you don't even need to worry about that cuz it's got an internal pull up. There's no other configuration stuff. Internal oscillators allow the thing to work, run your program, and you can get

**Dave Jones:** a flashing LED blinky circuit up and running very easily and cheaply. But is it the same for FPGAs? Nope. Let's take a look at why. So you can't just do the same thing you can with the micro here. Load on your

**Dave Jones:** breadboard, hook up your 5-volt supply, hook up your USB programmer, JTAG programmer to the thing and get it to blink your LED. It's not that easy like it is with the microcontroller. Yes, you can get simple cheap little JTAG

**Dave Jones:** programmers, which I've done a separate video on that will be linked down below how the JTAG programming system works for FPGAs. And but you can get these cheap programmers and but it doesn't work the same as micros. Why? Because of quite a few things which

**Dave Jones:** we're going to take a look at. First of all, they come in a usually come in pain in the ass BGA packages, not a simple friendly DIP package which you can just plug into your breadboard. Maybe some of

**Dave Jones:** the low-end ones might come in a quad flat pack but it might be you know 100 pins or something like that, real pain in the ass. So right off the bat there, you're going to have to melt this thing

**Dave Jones:** on some sort of adapter board at a bare minimum to get the thing in a usable format that you can connect all your stuff up to. The next thing is that these things are volatile. What that means is that they don't have flash

**Dave Jones:** memory in them like your microcontroller does. So yeah, you can just program it via the JTAG programmer but as soon as you remove the power, poof, your design's gone and you have to download it again. Hopeless. So we'll take a look at that. Next thing

**Dave Jones:** is is that there there's no internal oscillators in these things like there are on your microcontroller. So once again, you've got to add in an external oscillator just to get the damn thing working. And the next thing is that they're

**Dave Jones:** generally not 5-V compatible. So you can't just hook them up to your regular 5-V power supply like you used to. Heck, some of them you can't even hook up to a 3.3-V supply. They often require multiple uh voltages for internal core voltages and

**Dave Jones:** stuff like that for some of your higher-end ones. Some of your lower-end ones, no, you can just get away with single 3.3 but it's something to be aware of. These things aren't easy. We haven't even gotten to all the

**Dave Jones:** configuration pins yet. So here's just some of the crazy stuff you might need to add in red here around your basic circuit which you didn't have to add for your microcontroller here. This is like for a uh Xilinx FPGA, for example. It's

**Dave Jones:** not bang on, it's just a rough example. We'll do a screen capture in the middle of exactly what you need for a basic uh JTAG flash uh boot configuration for a typical FPGA. But, as I said, it's going

**Dave Jones:** to uh change based on the vendor, based on the uh family of FPGA. So, you have to read the documentation, the very extensive documentation, as we'll see, for the individual for the exact FPGA which you're using just to get the damn

**Dave Jones:** thing up and running. So, you've got your USB simple little USB uh JTAG programmer here, but you now need a second chip here, which is your configuration flash memory, which stores all the information for your FPGA. Then, you've got to hook up that correctly.

**Dave Jones:** You have to tie it into the JTAG system that I've done the video on so that it uh forms a loop uh through the JTAG chain there, it's called. And, you have to get that right. If you screw that up,

**Dave Jones:** it's just not going to work. Um then, you've got all the uh configuration lines, the data, init, reset lines, the clocks, uh the done line, all that sort of stuff. You've got to hook that up correctly. If you screw up

**Dave Jones:** one of those lines and you don't get it right, it's just not going to work. And then, you've got various uh VCC voltages for your different banks, which I've done a separate video on before, linked down below. And, you've got weird pins

**Dave Jones:** like HSWAP enable. What does that do? Well, you've got to read the documentation to find out, don't you? Uh you've got mode pins down here, for example, on these Xilinx FPGAs. You've got to put those in a certain

**Dave Jones:** configuration to power the thing up. Or, sometimes you don't now with the more modern families. They've got a separate JTAG interface. Uh but, there's the thing is, there's a lot of stuff you got to do. This uh flash over here has

**Dave Jones:** to have the same JTAG programming voltages, everything else. And, if all that stuff isn't done, then, you know, your FPGA is just not going to work. It's going to be You're going to be sitting there scratching your head and

**Dave Jones:** saying these FPGAs suck. I'm going back to my micro controls. But, basically, why I'm doing all this and telling you about it is because it's not easy to do for a beginner. So, a beginner shouldn't be mucking around with all this stuff.

**Dave Jones:** You should get one of these demo kits that we're going to take a look at that have all this stuff already done for you so and already hooked up so you don't have to worry about any of this stuff. It just,

**Dave Jones:** you know, somebody's done all the hard work to figure out how to get this thing to boot up and make it work. And just to show you that I wasn't kidding, here is the Spartan-6 FPGA configuration user guide. This is just for the configuring

**Dave Jones:** and getting your FPGA up and running and doing what you want. And there's a different one of these for each different Xilinx family, and the other manufacturers will also have similar types of guides. And this guide is, well, 164

**Dave Jones:** pages long, folks. That is just to get the FPGA configuration doing various things. And granted, there are lots of different ways that you can configure FPGAs, but, you know, look at this sort of stuff. It's configuring all sorts of

**Dave Jones:** high-speed priority options, JTAGs, master-slave modes, non-multi boot, safe upgrade, blah blah blah, select map data loading, man, you name it. Look at it. Unbelievable. But, let's go down here. You don't get down CRC configurations, daisy chain, man, it's incredible. But, let's go down

**Dave Jones:** to page 26, shall we? I think it's on. Get down to page 26 here, and bingo, here is our basic configuration that we're going to use for a uh Spartan-6, for example, and that's how to hook it up. There's the FPGA, there's

**Dave Jones:** the uh platform flash memory, as they call it, the external flash memory. They've got the daisy-chaining of the uh JTAG there. You can see like TDI coming in, TDO going out into TDI of the flash, TDO going back out to your um Xilinx

**Dave Jones:** cable header here for your uh programmer. And there's those mode pins there. There's HSWAP enable, the various bank voltages there and there. And look, if you don't get this VCCOUX pin, if you forget to hook that up, then well, your

**Dave Jones:** JTAG's not going to work, and you know, the thing's just going to sit there and do nothing. And you're going to be scratching your head thinking it might be a software problem, or I don't know, something going on. So, there's all

**Dave Jones:** sorts of things you have to hook up just to get your FPGA programmed, working, and boot up, just so you can run that blinky LED program. It's incredible. And there's still a hundred and something pages left. Oh my

**Dave Jones:** goodness. But most of the time, you don't have to look at all this, because you're not going to be using the more obscure modes. But anyway, that's how complicated it is.
