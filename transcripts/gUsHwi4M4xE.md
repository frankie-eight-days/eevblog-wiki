---
video_id: gUsHwi4M4xE
title: EEVblog #496 - What Is An FPGA?
url: https://www.youtube.com/watch?v=gUsHwi4M4xE
source: youtube-asr
---

**Dave Jones:** Hi. Welcome to Fundamentals Friday. Today we're going to take a look at the FPGA or Field Programmable Gate Array. That's what it stands for. What is an FPGA? Well, an FPGA is a programmable device, a programmable chip, which is

**Dave Jones:** pretty much the closest thing you can get to actually designing your own chip completely from scratch. Just like an ASIC you may have heard of or something like that. That's what an FPGA allows you to do. It allows you to design and

**Dave Jones:** implement any virtually any digital function you can possibly imagine all within the one universal chip. They're pretty darn flexible. Now, the big difference between an FPGA and virtually every other chip you can buy on the market is that the FPGA

**Dave Jones:** doesn't do anything. It has no intended function when you actually buy it. Unlike say a microcontroller, it's actually a computer built in. It's all the logic is all hardwired in there and it can actually do something useful. All

**Dave Jones:** it needs is a program. Well, an FPGA can't even do that. You apply power to this thing and it's just going to sit there. It's not going to do anything at all. They are completely stupid. But, they make up for that with their extreme

**Dave Jones:** flexibility allowing you to design anything you can imagine in the digital domain. They can't do analog. Digital only, but in the digital domain you can program it into one of these FPGA chips. If you want to turn an FPGA into an an

**Dave Jones:** AVR microcontroller or a PIC microcontroller, you can do that. If you want to turn it into a digital signal processor, you can do that. If you want to turn it into a a thousand LED custom driver, you can do

**Dave Jones:** that. They're incredibly flexible, limited only by your imagination. So, how do they do this? Well, they do it by containing thousands, tens of thousands, hundreds of thousands, or even more of individual logic elements. Let's call them CLBs, or configurable

**Dave Jones:** logic blocks. They go under various names depending on the vendor, and we won't go into that. We'll call them CLBs, configurable logic blocks, that can implement pretty much any basic function you can imagine. And because there's so many of them, thousands, tens

**Dave Jones:** of thousands, hundreds of thousands, you can configure them in any way you like to perform any complex, or even simple, digital function. And those configurable logic blocks sit inside these red lines here, this matrix of interconnecting lines. They're basically exactly that,

**Dave Jones:** they're just metal interconnects inside the chip that you can join up in any configuration possible. So, you might want to join this logic block over to this one, over to this one, and then to these IO pins all over the place to

**Dave Jones:** implement whatever function you program into this thing. So, they're often called like a sea of gates, for example, because they're just all these configurable gates sitting on a sea of interconnecting logic. And well, that's a bit of an old term because

**Dave Jones:** these are these CLBs, configurable logic blocks, the logic elements, are more than just individual gates. They're pretty smart in their own right. Now, in theory, the most powerful and flexible FPGA, or configurable logic chip you can imagine, would contain millions of NAND

**Dave Jones:** gates, and, you know, an infinite network of all these interconnect lines to join them all together. Because if you remember your basic digital logic theory, a NAND gate, you can if you have enough NAND gates, you can create

**Dave Jones:** anything. You can create a microcontroller, you can create 100 microcontrollers, or any a DSP, or any function you like to do anything just from NAND gates. Unfortunately, um uh well, those chips do actually uh exist. They're called uh gate arrays, and well,

**Dave Jones:** they're not that um much used anymore. Similar sort of concept, these FPGAs, or field programmable gate arrays, with their more complex configurable logic blocks have taken over from that because in theory, um yeah, you could have all these configurable NAND gates in there,

**Dave Jones:** but you just simply run out of room. It's too complex. You can't have an infinite network of all these uh traces crossing everywhere, plus an infinite number of gates in there, and have them all configurably in every orientation.

**Dave Jones:** You would quickly run into a routing, just like routing a PCB, you'd run into a routing nightmare within the FPGA, and in the end it'd just choke on itself, and you wouldn't be able to do anything. So, an if a modern FPGA is basically an

**Dave Jones:** optimization of more complex configurable logic blocks that do contain individual gates and elements, but they also contain flip-flops and look-up tables and things like that. Um a more you know, more complex block in there, um then surrounded by a limited number

**Dave Jones:** of interconnecting traces like this. And then, it's a balance, it's a trade-off between uh what you can what logic function you can perform in one configurable logic block to all your routing resources to be able to get all

**Dave Jones:** your signals out to your IO pins around here from your internal logic elements. And we'll take an extremely brief look at what's inside one of these uh configurable logic blocks here. This is very generic. Um in practice, they are

**Dave Jones:** much more complicated than this, but generally, what you're going to get inside an FPGA is a lookup table. A basic uh lookup table might be, say, four inputs like this. You can get larger ones depending on the uh FPGA

**Dave Jones:** types. And then we've got all the configuration fuses in there as well. Of course, you can actually program that to perform a particular function. So, they've basically got gates in there, and I won't go into lookup table uh

**Dave Jones:** details, but then you'll typically have one or more uh flip-flops in here as well. And you can use those uh flip-flops in various ways, and they'll be uh connected to dedicated uh clock lines, or you can or it can come from

**Dave Jones:** the fabric. And there's more switching stuff in here, and the reset line for the flip-flop, and the Q and not Q outputs. They can you can select which output you actually want to go out from the uh configurable logic block. So,

**Dave Jones:** you've basically got a bunch of flexible inputs, a bunch of uh logic gates, and some um you know, flip-flop latching stuff you can do uh latched logic with, and that clocked logic uh as well. And then you've basically got some outputs

**Dave Jones:** as well. And if you've got thousands or tens of thousands of these things, can become incredibly powerful and flexible. Now, the other thing I've drawn inside here are these IO blocks around the outside of the chip that actually

**Dave Jones:** connect to the individual pins on the chip. And these are um fairly complicated little uh blocks in the of logic in their own right. They're not just a buffer that goes out to the pin, but they can perform they can be

**Dave Jones:** programmed to perform all sorts of functions. Uh tristate input They can be inputs just like a microcontroller. You can program them to be inputs or outputs. You can tristate them. You can have uh You can turn them into

**Dave Jones:** differential pair drivers, so not just single-ended differential pairs. You can have different uh log voltage um logic standards as well on the various pins. They can contain, uh, flip-flops and latches in them for driving DDR memory and all sorts of

**Dave Jones:** complicated things like that contained within these IO blocks. So, they can also be connected to the internal matrix as well. So, you've got lots of these powerful little logic elements in here that you can combine to do any function

**Dave Jones:** you want combined with pretty powerful IO as well. And that all adds up to a very powerful and flexible chip that can do, as I said, anything you can imagine. Now, when I said before that when you power up an FPGA, it's completely

**Dave Jones:** stupid. It doesn't know what to do. I wasn't kidding because an FPGA are typically volatile devices. What that means is that they have no ability to store their internal configuration or how you've programmed the device, what you've programmed it to do. They've got

**Dave Jones:** no ability to store that. So, as soon as you remove the power, it forgets. That FPGA just goes back to being factory fresh. It doesn't know what to do. It's just a huge sea of these gates sitting there unprogrammed. But, the FPGA has

**Dave Jones:** built into it a little, uh, actually quite a complex, uh, configuration logic here which then hooks, which then you have to hook up to an external configuration flash memory. So, for any FPGA to be useful, you can't just have

**Dave Jones:** the FPGA. You've got it's mandatory to have an external configuration flash memory which is basically just a regular, um, you know, a four or eight megabit flash, uh, serial flash memory device that can be parallel as well, um,

**Dave Jones:** except that it contains all of the information for all of these little fuses inside here, which logic block connects to which and how and the fuses inside these configurable logic blocks here, the fuses inside these IO blocks to tell what these IO blocks down here,

**Dave Jones:** and you know, hundreds of other fuses for various functions which we'll talk about. And that's why you need a quite a large, even for a sort of, you know, a cheap medium, you know, a smallish FPGA, you really need a quite a large flash memory

**Dave Jones:** cuz there's a lot of fuses inside here which have to be programmed. And when I say fuses, they're not fuses like flash fuses. They don't permanently store it. They're actually just, you know, transistors or latches that just switch on and store the function

**Dave Jones:** for that particular bit. But you can think of them as fuses except when you turn off the power, boom, they're gone. The FPGA forgets absolutely everything. So, when you turn on an FPGA, it doesn't know what to do. But this configuration

**Dave Jones:** logic up here when you first switch it on, automatically knows, well, okay, power's just switched on. I need to load the data from the external flash memory here and program in all the fuses. And that can take, you know, seconds

**Dave Jones:** sometimes to do. So, FPGAs are not instant-on. They do take some time to boot up and to configure all of their logic. So, what are some of the advantages of FPGAs? Why would you want to use them? Well, let's take a look at

**Dave Jones:** a few. You can, as I said, you can do anything in the digital domain you could possibly imagine. You can turn it into a microcontroller. You can turn it into a, say, Cray supercomputer. You can drive a custom controller to drive a thousand

**Dave Jones:** LED matrix cube or anything like that. You can do anything. Really, anything. It's amazing. They're also super fast. And some of the, even the basic FPGAs have IO blocks and serial functionality which we'll get into. They can go into the

**Dave Jones:** giga, you know, the gigabits per second region. They have our transceivers built in that can actually do, you know, gigabits per second serial decode and stuff like that incredibly, incredibly quick. Now, if you compare that to say a

**Dave Jones:** microcontroller, for example, even a really fast modern processor like you like the arm used on the Raspberry Pi, you might be able to toggle the IO pin at, you know, 100 MHz or something like that, but really, you know, you're

**Dave Jones:** you're bottlenecked by the process. You can't do any serious processing, you know, on a 100 MHz input signal, for example. Well, as with FPGAs, that's not a problem at all because you can dedicate the logic in here to just do

**Dave Jones:** that and we'll that'll come down into this massively parallel thing advantage at the moment to do a specific function on just an IO signal that you want. So, if you got an input signal coming in and you want to do some really fast

**Dave Jones:** processing of it in effectively real time and shoot it out another pin, well, you can dedicate a part of the FPGA to do that. Incredibly flexible from a speed point of view. Now, they're as their name suggests, they're field

**Dave Jones:** programmable. They're FPGAs. How does that differ from a microcontroller which you can reprogram, you can reflash in the field? Well, this is different in that it's not just a fixed processor. In fact, it doesn't contain a processor at all unless you

**Dave Jones:** program one in there, but so you can change anything in your design at all. So, let's say that you design your custom product and you used a microcontroller, for example, and then you put it out in the field and you

**Dave Jones:** went, "Oh, no, I've got to change something and I can't I don't have enough power or processing capability left in my processor to do it or it's not flexible enough to do this or that. Well, with an FPGA, if you ran your

**Dave Jones:** processor inside the FPGA and you had enough resources left over, when your product's gone out in the field, you can go, "Oh, look, I needed, you know, a you know, a FIR filter or something like that to be implemented

**Dave Jones:** between this pin and this pin." Well, you can just reconfigure it anything you want. If you've got enough space left in there, no worries. You put a FIR filter in there or a PID. You can tweak PID controls or do whatever you

**Dave Jones:** can possibly imagine. So, they're more powerful in that respect than a field programmable uh microcontroller because they're not just a processor, they're not just a microcontroller. They can do anything, as we said, anything at all. And we talked about the massively

**Dave Jones:** parallel thing, and this is one of the huge advantages of FPGAs and the main one of the main reasons why you would choose them over a microcontroller for certain projects because if you take your basic microcontroller, it's effectively a bottleneck.

**Dave Jones:** Everything has to run through that processor core in sequence. You know, you've got your individual line of code, you execute each instruction code one by one, and you have to rely on doing that fast enough. Even if you've got a

**Dave Jones:** real-time operating system, it's not really real-time. You can't process these 10 pins at the exact instant that you're processing these 10 pins up here and toggling these outputs here. It doesn't happen. But with FPGAs, you can because this all these logic block all

**Dave Jones:** these logic blocks in here are completely configurable, completely separate. So, you can be processing these pins down here and outputting something over here at the exact instant that you're processing these pins up here and outputting something else over

**Dave Jones:** here. And you can do that, if you've got enough IO pins and enough logic blocks, you can do that hundreds and hundreds of times. So, you can be processing hundreds of things in parallel. Take for example an analog-to-digital converter.

**Dave Jones:** If you had 50 channels of an of ADC data coming in, you know, you had an external ADC chip, of course, cuz these are only digital. They can't do anything in the analog domain. Well, if you got all this

**Dave Jones:** data coming from 50 analog-to-digital converters, 50 channels, and you wanted to process that all at once, well, you can yeah, have a 50-channel uh sample and hold, and then you process it to do it all. You know, there's a real bottleneck, speed

**Dave Jones:** bottleneck there. But in an FPGA, you can have each one a particular bunch of logic blocks dedicated to that one channel. And then you can just duplicate that 50 times, or 100 times, or 500 times within inside your FPGA. Cuz

**Dave Jones:** remember, we've got hundreds, sometimes hundreds of thousands of these logic blocks to play with. Fantastic. So, that is the massively parallel advantage of FPGAs. If you want to do a whole bunch of processing all at once in parallel, then FPGAs are what you want

**Dave Jones:** to use over a microcontroller. And that brings us to one of the final advantages, the high IO count. Um FPGAs specialize in high IO count applications. In fact, the development of FPGAs has really just pushed towards that high pin count capability. And it's

**Dave Jones:** actually quite difficult to get a decent FPGA. And by decent, when you talk about a decent FPGA, you're talking about how many logic blocks effectively it's got. It's hard to get a decent FPGA with a small number of IO pins. You know, it's

**Dave Jones:** not like you can get an SO-16 package, or a even a you know, a 44-pin quad flat pack. They're actually quite hard to get. That's why most FPGAs are designed for high IO applications. So, they contain hundreds of pins up to, you

**Dave Jones:** know, 1,000 plus pins. And because they've got so many pins, they often come in real pain in the ass to use packages like BGA. So, if you want to drive, for example, some huge LED matrix, you know, you had

**Dave Jones:** a you know, a 100 LEDs by a 100 LED matrix or something like that. Yeah, you can do it with a microcontroller and a whole bunch of external 74HC595 latches or something to latch the individual rows and columns and all that

**Dave Jones:** sort of thing. That's sort of the traditional way to do it. But then, as I said, you come into that real speed bottleneck. The processor has to drive all that incredible incredibly quickly just to get, you know, 25 times per

**Dave Jones:** second updating on your LED matrix display. Well, FPGAs can do all of that in parallel because they've got hundreds of IO pins. So, you can choose one with hundreds of IO pins. You can do it all at once. Bam! Straight in there. So,

**Dave Jones:** that's the huge advantage over microcontrollers. So, these FPGAs sound fantastic, right? Why doesn't everyone use them? They're so fantastic. You can program them to do absolutely anything. Why are they not in every single product and every hobbyist toolkit? Well, there's lots of

**Dave Jones:** disadvantages, and I probably haven't even listed them all. Let's go through them. These FPGAs are expensive. Why are they expensive? Well, they're expensive relative to another chip which does that could do, potentially, a similar function. I mean, you can get FPGAs as

**Dave Jones:** little, you know, as a dollar or two, but they don't contain many configurable logic blocks. So, they're quite limited in what you can actually do with the things. And so, they're expensive in a relative sense. For example, if you

**Dave Jones:** wanted to duplicate an AVR microcontroller in an FPGA, there is no way that you can get one big enough to put an AVR microcontroller in there that's going to be cheaper than just buying the AVR microcontroller on its

**Dave Jones:** own. So, if you're just looking to duplicate the functionality of a pre-existing dedicated hardwired chip, you're wasting your time. So, that's why they are quite expensive. And FPGAs, the really high-end ones, you can pay many, many thousands of dollars for just

**Dave Jones:** the one chip. FPGAs are some of the most incredibly complex and bleeding-edge process technology chips on the market. Why? Because they have to contain mill- sometimes millions of these logic elements and routing paths and and and configuration fuses and everything else

**Dave Jones:** just to give you that flexibility. So, they are very So, they are relatively expensive. And because they also contain all of this flexibility, it means that they're not optimized for power consumption. So, if you're after an ultra-low power design

**Dave Jones:** to do something, there's no way an FPGA or an equivalent FPGA is going to be the same as or lower power or nearly as lower power as a dedicated chip to do the function. It's just not possible due

**Dave Jones:** to the process technology and all the complexity. So, they're quite high-power devices and they can chew a lot of power when they start up. A surge current when they start up and program all these fuses, for example. So, just got to be

**Dave Jones:** very careful. You wouldn't use them in a low-power design. They're volatile. As I said, they completely forget everything. These FPGAs are brain dead. You have to have an external configuration flash memory in order to reprogram the FPGA every time you apply

**Dave Jones:** power. And that can lead to boot time issues. I mean, some uh you want just to work instantly. You can't just uh do that with FPGAs. Although there are some that do have configuration flash. We'll talk about that maybe.

**Dave Jones:** And as I said, they are high pin count. If you're looking for a hobbyist-friendly or a really production-friendly device, an FPGA is not the best way to go about it. As I said, you can get low low pin

**Dave Jones:** count devices. There are a few out there, but they're generally not in easy-to-use packages. Most of them these days come in BGA packages, which are not easy to use. So, often you have to take that into account. And the other thing

**Dave Jones:** is because they're optimized for high pin count, generally if you want a lot of configurable logic blocks in here, a lot of logic density, then you generally have to go for a higher pin count device. They sort of go hand in hand.

**Dave Jones:** High logic density, high pin count. Why? It's annoying. The manufacturers just do it because that's where they think the market is or the market's being driven by those sort of application. So, it's not like you can get a million logic

**Dave Jones:** element device in a nice friendly, you know, TQFP, you know, a 44-pin package or something. It's just not going to happen. So, they are And the other thing is they are complicated. They are incredibly complicated. Go down Go to

**Dave Jones:** the manufacturer's data sheet, Xilinx or Altera or one of the others, and download a data sheet for an FPGA, and you can spend the rest of your life reading that thing. It's not just one data sheet. Then they have all these

**Dave Jones:** different data sheets and applications for how these configurable logic blocks work, how the IO works, how the clock systems work, how the serial interfaces work, and how the DSP cores work in the things, and and how to program them with the best way uh best

**Dave Jones:** and quickest way and safest secure way to program them when they boot up, and ah, they've got, you know, uh dozens and dozens of data sheets and application notes for just the one device. They are Believe me when I say it, the most

**Dave Jones:** incredibly complex chips on the market. Take my word for it, or don't. Go read it for yourself. Um and because they are so complicated, they contain many traps for young players. There's lots of things that can go wrong in this thing.

**Dave Jones:** Because you are effectively designing the chip yourself, you have to take all the timing into account, all the routing into account, and the complexity of the device and how do you configure the IO blocks. And I haven't even scratched the

**Dave Jones:** surface of the complexity of this thing. This is incredibly simplistic what we've looked at here so far. So they are many traps in terms of not only just configuring the things, choosing the right clock pins, for example, because

**Dave Jones:** some in addition to these IO blocks here, they'll have dedicated clock pins which have faster routing paths through here. And depending on if you want a really fast design, you have to know how to use configure your um uh logic in the

**Dave Jones:** correct correct uh part of the FPGA. It can make a difference where you physically place all your stuff in the FPGA. And the tools can sort of take care of some of that or a lot of that for you, but you really have to be

**Dave Jones:** aware. And there are a lot of traps just in configuring and choosing an FPGA. And uh that's the thing. The tools are incredibly complex. Um go and download the tools for these FPGAs, and it's like many gigabytes of

**Dave Jones:** downloads, and it There are so many tools which come with these FPGAs. They are incredibly complex. Yes, you can get uh nice development kits which, you know, have example programs, and you just install all the tools. And even

**Dave Jones:** though they got tens of millions of lines of code in there, it all just Yeah, you can get these simple development kits to just work and you can get a simple application running in your FPGA and they look easy, but from that aspect

**Dave Jones:** when you first use them, but when you want to do your own professional design from scratch, boy, you can spend a year just choosing and selecting and programming and configuring and optimizing a you know, a moderately complex FPGA design.

**Dave Jones:** The tools are necessarily complex because these devices themselves are incredibly complex. And as I said, they're hard to choose and compare. Go to just two of the manufacturers, the two top ones who own like 80% of the market,

**Dave Jones:** Xilinx and Altera, and try and figure out and compare two different devices. They'll call these logic blocks different things, configurable configurable logic blocks, they'll call them logic one manufacturer call them logic elements, someone will call them something else.

**Dave Jones:** They can contain different number of lookup tables in them. They might use terms like system gates and all sorts of stuff which confuse the issue and they don't have the industry does not have common terminology for the architecture

**Dave Jones:** inside these FPGAs. The manufacturers all have their own architecture terminology. The architecture is entirely different, the terminology is entirely different between manufacturers. And just being able to choose between, you know, you take for a you take advantage of the fact that it's

**Dave Jones:** simple to compare micro controls for example between PIC and Atmel. Right, yeah, one contains, you know, X number of ADCs of 10 bits, it contains two UARTs, it contains X timers, and you know, they're all fairly generically similar, but FPGAs totally different.

**Dave Jones:** So, good luck trying to choose and compare not only between manufacturers, but choosing the correct size device for your project because when you start your project you might have an idea of what you want to do and you go, "Okay, I need

**Dave Jones:** an FPGA because of some of the advantages we talked about." But then you find that well, like how many logic elements do I need because the a device with, you know, 128K logic elements might cost, you know, twice as much as one with 50,000 logic

**Dave Jones:** elements or something like that. How many do you need? You don't know until you actually design your code and then run and and then compile it or synthesize it and try and get an estimate of how many logic elements

**Dave Jones:** you're going to use. So sometimes you have to actually do your design first and then choose your design and then choose your chip last when you know what, you know, how many logic elements you're going to need and things like

**Dave Jones:** that. Maybe you use the power estimating program in the tools. They contain you don't know how much this power this FPGA is going to draw. Don't bother going into the data sheet and going, "Oh, how much current does this FPGA draw?"

**Dave Jones:** It draws nothing when you got nothing in there or, you know, sort of, you know, just a quiescent current but when you're running depends on how much logic you're running, how many IO blocks, how fast, how they're configured, all sorts of

**Dave Jones:** stuff. It's completely dynamic so the tools contain power estimating programs. And so it's just amazingly complex these devices. So you don't generally want to use FPGAs unless you're A really experienced in or B you absolutely need them for some of the

**Dave Jones:** advantages we talked about the massively paralleled nature of a project for example or the really fast IO processing or something like that. Now, here's something that we haven't talked about yet and it requires separate videos. In fact, everything I've talked about here

**Dave Jones:** and a whole lot more I could do a one or two hour video on each and every aspect of these FPGAs. And these HDLs or hardware definition languages are no different. So, these are generally how most people program FPGAs these days. They don't use

**Dave Jones:** the schematic capture anymore, even though you can do that if you really want to. These hardware definition languages, the two major ones are VHDL and Verilog, you may have heard of around the traps. Now, I may get hauled over the coals for this

**Dave Jones:** one, but I generally they are not easy and they're not intuitive like your more sequential programming languages like C and basic that you're familiar with on your PC or your microcontroller where you get the processor which executes each instruction line by line by line by

**Dave Jones:** line. FPGAs don't contain a processor unless you put one in there. They are just a sea of logic gates. So, using code to define things like multiplexers and counters and and gates and flip-flops and all that sort of thing is not really that

**Dave Jones:** intuitive to most people who've learned electronics and digital electronics the traditional way with gates and flip-flops and muxes. It's It's a real different world where you have to think that everything's executing in parallel and you have to think about clock

**Dave Jones:** domains and all sorts of complicated stuff. So, HDL it Yeah, you might be able to load your example program when you get your $100 FPGA demo board, but then trying to really understand it and that comes back to the traps as well.

**Dave Jones:** There's not only traps in configuring the FPGAs, but there's also many traps in how well you write or how well you can write your hardware definition language in VHDL or Verilog. There's lots of traps there that can cause all

**Dave Jones:** sorts of problems inside your FPGA, race conditions and all sorts of stuff that we won't go into, but there's and I've probably left off some other disadvantages, but there's a lot of disadvantages to FPGAs and that's why they're not hugely popular except for

**Dave Jones:** the more niche applications where the advantages are really so compelling that you'll want to use an FPGA. Now, I've been going on for like 30 minutes on just what an FPGA is and quite frankly, I haven't even scratched

**Dave Jones:** the surface because the simplistic architecture I've sort of explained here is not how modern FPGAs are. Well, they are in a basic operational sense, which is good introduction of how they actually work, but you know, in practice when you want to implement an FPGA,

**Dave Jones:** they're incredibly more much more complex than this. They haven't been sort of this simplistic with just like the CLB and just the routing paths and the just the IO block and that's pretty much it. They haven't been that way

**Dave Jones:** since the dawn of FPGAs many decades ago. All of your modern FPGAs contain a whole slew of functionality in these things, no pun intended, because there's things like a slew rate control in the IO blocks. Memory is a big thing in

**Dave Jones:** FPGAs these days. Almost all decent FPGAs will have various forms of memory in them in terms of distributed memory which you can utilize in different ways depending on your architecture, your internal architecture you're trying to design, or they can have dedicated RAM

**Dave Jones:** blocks and you can implement dual port memory. You can do all sorts of stuff because a lot of processing happens inside modern FPGAs. That's what a lot of people use them for. So, they'll even contain these days, the

**Dave Jones:** manufacturers realize, well, people were all implementing what's called these soft processor cores, which means you might get like a NIOS core, which is or the manufacturers have their own types of, you know, 8, 16, 32-bit or more processor cores, you can just drop

**Dave Jones:** them in there. And they're a soft core, soft because they they can you can just configure it sort of anywhere within the FPGA you want. As well as a lot of other functionality, but a lot of manufacturers are going, "Well, a lot of

**Dave Jones:** people use these cores and they use other functions within the FPGA." Basic stuff like might be an Ethernet controller, for example. So, they go, "Okay, well, let's put hard logic inside these FPGAs as well." So, they'll embed like an ARM processor and that's

**Dave Jones:** actually not in the FPGA fabric. It's not a soft function, it's a hard function. So, it's, you know, it might have a little ARM processor over here or a couple of them. And they might have, you know, Ethernet transceivers or big

**Dave Jones:** uh serdes, serial controllers, and all sorts of things implemented as all this hard logic around what traditionally was a soft FPGA fabric. The advantage of having that hard processor and hard logic in there is that uh if you know you want a

**Dave Jones:** processor in this thing, well, you're better off going for a hard processor with the FPGA fabric around it because it's going to be more optimized, it's lower power, you don't have to worry about designing that aspect of the

**Dave Jones:** processor in, you don't have to recompile the processor each time you want to uh you know, recompile the design for your FPGA. It's all hard in there, just like a microcontroller or microprocessor, and you know it's guaranteed to work. Because the

**Dave Jones:** disadvantage of these FPGAs is nothing's guaranteed to work because you've designed it or you've written all the code, you've dropped in all the blocks, even if you might pull these uh you know, modules off the internet, how do you know if they work? How do you

**Dave Jones:** know how the software has routed it within here? Because that's the other thing with FPGAs, routing is a huge part of this thing, and actually fitting all of your design and optimizing. That's why these tools are incredibly complex, and it can actually take

**Dave Jones:** sometimes, you know, a long to like days to actually really fit and compile a real huge design and optimize it inside one of these FPGAs and get the correct timing and routing paths. And that's the other thing, clocks. These things will

**Dave Jones:** have dedicated clock pins and dedicated clock routing paths. Uh I think I said before dedicated clock quadrants, so you can't just uh utilize this logic over here with a clock that you're using on this pin over this side of the FPGA. And they'll come

**Dave Jones:** with uh DSP blocks. That's another very common thing. You'll see that uh uh this FPGA contains uh multipliers, accumulators, and MACs, and DSP cores all scattered around. A typical FPGA these days might have, you know, 50 or 100 DSP little cores all scattered

**Dave Jones:** around the place. And on top of all that complex uh clock routing structure inside modern FPGAs, they'll contain uh digital clock management uh systems. They go under various names, uh PLLs, and all sorts of things to multiply the

**Dave Jones:** external clocks. That's why you might typically find one of these FPGAs working like the external crystal is only 20 MHz, for example, but the process but all the logic inside might be running at a couple of 100 MHz

**Dave Jones:** because they mul- those PLLs and digital clock managers, you can multiply the external clocks. can do phase shifting, and you can do very complicated timing uh and clocking arrangements within side your FPGA architecture, but that opens up a whole can of worms in terms of uh

**Dave Jones:** clock timing for your entire system. And you can really goof that up if you don't know what you're doing. And I haven't even started on the complexity and the limitations, as well, of designing uh compiling your designs into an FPGA.

**Dave Jones:** But, this is the basic architecture of them. And well, you don't be afraid because you can get simple development kits. Start up using FPGAs are are an important part of the electronics design toolkit. So, they are definitely worth

**Dave Jones:** learning. So, don't be afraid because there are some powerful advantages to FPGAs. So, I recommend you actually go to the manufacturer's websites, Altera, Xilinx for starters, uh for example, and check out all the range of FPGAs they've got

**Dave Jones:** available. There's basically one available for every niche applications. Ones are designed for really fast serial processing, others are designed for massive IO, others are designed for DSP uh type work, and others are designed for a whole combination of those things.

**Dave Jones:** Incredibly complex devices, and well, I haven't even scratched the surface. Really, I could do another 100 videos on FPGA. Will I? I don't know. Jeez. Catch you next time.
