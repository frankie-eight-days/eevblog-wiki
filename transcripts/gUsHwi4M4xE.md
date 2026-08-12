---
video_id: gUsHwi4M4xE
title: EEVblog #496 - What Is An FPGA?
url: https://www.youtube.com/watch?v=gUsHwi4M4xE
source: youtube-asr
timestamps: {"0": 0, "1": 24, "2": 43, "3": 60, "4": 69, "5": 77, "6": 95, "7": 105, "8": 118, "9": 136, "10": 156, "11": 172, "12": 184, "13": 202, "14": 222, "15": 240, "16": 269, "17": 280, "18": 292, "19": 307, "20": 337, "21": 351, "22": 362, "23": 377, "24": 385, "25": 396, "26": 408, "27": 429, "28": 442, "29": 455, "30": 474, "31": 488, "32": 501, "33": 517, "34": 525, "35": 544, "36": 573, "37": 588, "38": 602, "39": 616, "40": 629, "41": 641, "42": 653, "43": 664, "44": 676, "45": 691, "46": 705, "47": 722, "48": 746, "49": 759, "50": 775, "51": 788, "52": 808, "53": 828, "54": 838, "55": 852, "56": 868, "57": 879, "58": 890, "59": 913, "60": 921, "61": 933, "62": 949, "63": 966, "64": 990, "65": 1005, "66": 1018, "67": 1029, "68": 1048, "69": 1057, "70": 1069, "71": 1084, "72": 1095, "73": 1110, "74": 1123, "75": 1142, "76": 1167, "77": 1183, "78": 1203, "79": 1231, "80": 1239, "81": 1247, "82": 1261, "83": 1273, "84": 1286, "85": 1297, "86": 1313, "87": 1324, "88": 1336, "89": 1353, "90": 1378, "91": 1391, "92": 1402, "93": 1416, "94": 1441, "95": 1448, "96": 1461, "97": 1481, "98": 1505, "99": 1521, "100": 1543, "101": 1555, "102": 1568, "103": 1588, "104": 1604, "105": 1630, "106": 1649, "107": 1661, "108": 1675, "109": 1687, "110": 1714, "111": 1728, "112": 1743, "113": 1773, "114": 1799, "115": 1811, "116": 1822, "117": 1832, "118": 1860, "119": 1873, "120": 1888, "121": 1900, "122": 1914, "123": 1935, "124": 1960, "125": 1969, "126": 1983, "127": 1997, "128": 2016, "129": 2040, "130": 2063, "131": 2075, "132": 2090, "133": 2109, "134": 2123, "135": 2140, "136": 2160, "137": 2173, "138": 2191, "139": 2204, "140": 2220, "141": 2237}
---

**Dave Jones:** Hi. Welcome to Fundamentals Friday. Today we're going to take a look at the FPGA or Field Programmable Gate Array. That's what it stands for. What is an FPGA? Well, an FPGA is a programmable device, a programmable chip, which is pretty much the closest thing you can get to actually designing your own chip completely from scratch.

**Dave Jones:** Just like an ASIC you may have heard of or something like that. That's what an FPGA allows you to do. It allows you to design and implement any virtually any digital function you can possibly imagine all within the one universal chip.

**Dave Jones:** They're pretty darn flexible. Now, the big difference between an FPGA and virtually every other chip you can buy on the market is that the FPGA doesn't do anything. It has no intended function when you actually buy it.

**Dave Jones:** Unlike say a microcontroller, it's actually a computer built in. It's all the logic is all hardwired in there and it can actually do something useful. All it needs is a program.

**Dave Jones:** Well, an FPGA can't even do that. You apply power to this thing and it's just going to sit there. It's not going to do anything at all. They are completely stupid.

**Dave Jones:** But, they make up for that with their extreme flexibility allowing you to design anything you can imagine in the digital domain. They can't do analog. Digital only, but in the digital domain you can program it into one of these FPGA chips.

**Dave Jones:** If you want to turn an FPGA into an an AVR microcontroller or a PIC microcontroller, you can do that. If you want to turn it into a digital signal processor, you can do that.

**Dave Jones:** If you want to turn it into a a thousand LED custom driver, you can do that. They're incredibly flexible, limited only by your imagination. So, how do they do this?

**Dave Jones:** Well, they do it by containing thousands, tens of thousands, hundreds of thousands, or even more of individual logic elements. Let's call them CLBs, or configurable logic blocks. They go under various names depending on the vendor, and we won't go into that.

**Dave Jones:** We'll call them CLBs, configurable logic blocks, that can implement pretty much any basic function you can imagine. And because there's so many of them, thousands, tens of thousands, hundreds of thousands, you can configure them in any way you like to perform any complex, or even simple, digital function.

**Dave Jones:** And those configurable logic blocks sit inside these red lines here, this matrix of interconnecting lines. They're basically exactly that, they're just metal interconnects inside the chip that you can join up in any configuration possible.

**Dave Jones:** So, you might want to join this logic block over to this one, over to this one, and then to these IO pins all over the place to implement whatever function you program into this thing.

**Dave Jones:** So, they're often called like a sea of gates, for example, because they're just all these configurable gates sitting on a sea of interconnecting logic. And well, that's a bit of an old term because these are these CLBs, configurable logic blocks, the logic elements, are more than just individual gates.

**Dave Jones:** They're pretty smart in their own right. Now, in theory, the most powerful and flexible FPGA, or configurable logic chip you can imagine, would contain millions of NAND gates, and, you know, an infinite network of all these interconnect lines to join them all together.

**Dave Jones:** Because if you remember your basic digital logic theory, a NAND gate, you can if you have enough NAND gates, you can create anything. You can create a microcontroller, you can create 100 microcontrollers, or any a DSP, or any function you like to do anything just from NAND gates.

**Dave Jones:** Unfortunately, um uh well, those chips do actually uh exist. They're called uh gate arrays, and well, they're not that um much used anymore. Similar sort of concept, these FPGAs, or field programmable gate arrays, with their more complex configurable logic blocks have taken over from that because in theory, um yeah, you could have all these configurable NAND gates in there, but you just simply run out of room.

**Dave Jones:** It's too complex. You can't have an infinite network of all these uh traces crossing everywhere, plus an infinite number of gates in there, and have them all configurably in every orientation.

**Dave Jones:** You would quickly run into a routing, just like routing a PCB, you'd run into a routing nightmare within the FPGA, and in the end it'd just choke on itself, and you wouldn't be able to do anything.

**Dave Jones:** So, an if a modern FPGA is basically an optimization of more complex configurable logic blocks that do contain individual gates and elements, but they also contain flip-flops and look-up tables and things like that.

**Dave Jones:** Um a more you know, more complex block in there, um then surrounded by a limited number of interconnecting traces like this. And then, it's a balance, it's a trade-off between uh what you can what logic function you can perform in one configurable logic block to all your routing resources to be able to get all your signals out to your IO pins around here from your internal logic elements.

**Dave Jones:** And we'll take an extremely brief look at what's inside one of these uh configurable logic blocks here. This is very generic. Um in practice, they are much more complicated than this, but generally, what you're going to get inside an FPGA is a lookup table.

**Dave Jones:** A basic uh lookup table might be, say, four inputs like this. You can get larger ones depending on the uh FPGA types. And then we've got all the configuration fuses in there as well.

**Dave Jones:** Of course, you can actually program that to perform a particular function. So, they've basically got gates in there, and I won't go into lookup table uh details, but then you'll typically have one or more uh flip-flops in here as well.

**Dave Jones:** And you can use those uh flip-flops in various ways, and they'll be uh connected to dedicated uh clock lines, or you can or it can come from the fabric.

**Dave Jones:** And there's more switching stuff in here, and the reset line for the flip-flop, and the Q and not Q outputs. They can you can select which output you actually want to go out from the uh configurable logic block.

**Dave Jones:** So, you've basically got a bunch of flexible inputs, a bunch of uh logic gates, and some um you know, flip-flop latching stuff you can do uh latched logic with, and that clocked logic uh as well.

**Dave Jones:** And then you've basically got some outputs as well. And if you've got thousands or tens of thousands of these things, can become incredibly powerful and flexible. Now, the other thing I've drawn inside here are these IO blocks around the outside of the chip that actually connect to the individual pins on the chip.

**Dave Jones:** And these are um fairly complicated little uh blocks in the of logic in their own right. They're not just a buffer that goes out to the pin, but they can perform they can be programmed to perform all sorts of functions.

**Dave Jones:** Uh tristate input They can be inputs just like a microcontroller. You can program them to be inputs or outputs. You can tristate them. You can have uh You can turn them into differential pair drivers, so not just single-ended differential pairs.

**Dave Jones:** You can have different uh log voltage um logic standards as well on the various pins. They can contain, uh, flip-flops and latches in them for driving DDR memory and all sorts of complicated things like that contained within these IO blocks.

**Dave Jones:** So, they can also be connected to the internal matrix as well. So, you've got lots of these powerful little logic elements in here that you can combine to do any function you want combined with pretty powerful IO as well.

**Dave Jones:** And that all adds up to a very powerful and flexible chip that can do, as I said, anything you can imagine. Now, when I said before that when you power up an FPGA, it's completely stupid.

**Dave Jones:** It doesn't know what to do. I wasn't kidding because an FPGA are typically volatile devices. What that means is that they have no ability to store their internal configuration or how you've programmed the device, what you've programmed it to do.

**Dave Jones:** They've got no ability to store that. So, as soon as you remove the power, it forgets. That FPGA just goes back to being factory fresh. It doesn't know what to do.

**Dave Jones:** It's just a huge sea of these gates sitting there unprogrammed. But, the FPGA has built into it a little, uh, actually quite a complex, uh, configuration logic here which then hooks, which then you have to hook up to an external configuration flash memory.

**Dave Jones:** So, for any FPGA to be useful, you can't just have the FPGA. You've got it's mandatory to have an external configuration flash memory which is basically just a regular, um, you know, a four or eight megabit flash, uh, serial flash memory device that can be parallel as well, um, except that it contains all of the information for all of these little fuses inside here, which logic block

**Dave Jones:** connects to which and how and the fuses inside these configurable logic blocks here, the fuses inside these IO blocks to tell what these IO blocks down here, and you know, hundreds of other fuses for various functions which we'll talk about.

**Dave Jones:** And that's why you need a quite a large, even for a sort of, you know, a cheap medium, you know, a smallish FPGA, you really need a quite a large flash memory cuz there's a lot of fuses inside here which have to be programmed.

**Dave Jones:** And when I say fuses, they're not fuses like flash fuses. They don't permanently store it. They're actually just, you know, transistors or latches that just switch on and store the function for that particular bit.

**Dave Jones:** But you can think of them as fuses except when you turn off the power, boom, they're gone. The FPGA forgets absolutely everything. So, when you turn on an FPGA, it doesn't know what to do.

**Dave Jones:** But this configuration logic up here when you first switch it on, automatically knows, well, okay, power's just switched on. I need to load the data from the external flash memory here and program in all the fuses.

**Dave Jones:** And that can take, you know, seconds sometimes to do. So, FPGAs are not instant-on. They do take some time to boot up and to configure all of their logic.

**Dave Jones:** So, what are some of the advantages of FPGAs? Why would you want to use them? Well, let's take a look at a few. You can, as I said, you can do anything in the digital domain you could possibly imagine.

**Dave Jones:** You can turn it into a microcontroller. You can turn it into a, say, Cray supercomputer. You can drive a custom controller to drive a thousand LED matrix cube or anything like that.

**Dave Jones:** You can do anything. Really, anything. It's amazing. They're also super fast. And some of the, even the basic FPGAs have IO blocks and serial functionality which we'll get into.

**Dave Jones:** They can go into the giga, you know, the gigabits per second region. They have our transceivers built in that can actually do, you know, gigabits per second serial decode and stuff like that incredibly, incredibly quick.

**Dave Jones:** Now, if you compare that to say a microcontroller, for example, even a really fast modern processor like you like the arm used on the Raspberry Pi, you might be able to toggle the IO pin at, you know, 100 MHz or something like that, but really, you know, you're you're bottlenecked by the process.

**Dave Jones:** You can't do any serious processing, you know, on a 100 MHz input signal, for example. Well, as with FPGAs, that's not a problem at all because you can dedicate the logic in here to just do that and we'll that'll come down into this massively parallel thing advantage at the moment to do a specific function on just an IO signal that you want.

**Dave Jones:** So, if you got an input signal coming in and you want to do some really fast processing of it in effectively real time and shoot it out another pin, well, you can dedicate a part of the FPGA to do that.

**Dave Jones:** Incredibly flexible from a speed point of view. Now, they're as their name suggests, they're field programmable. They're FPGAs. How does that differ from a microcontroller which you can reprogram, you can reflash in the field?

**Dave Jones:** Well, this is different in that it's not just a fixed processor. In fact, it doesn't contain a processor at all unless you program one in there, but so you can change anything in your design at all.

**Dave Jones:** So, let's say that you design your custom product and you used a microcontroller, for example, and then you put it out in the field and you went, "Oh, no, I've got to change something and I can't I don't have enough power or processing capability left in my processor to do it or it's not flexible enough to do this or that.

**Dave Jones:** Well, with an FPGA, if you ran your processor inside the FPGA and you had enough resources left over, when your product's gone out in the field, you can go, "Oh, look, I needed, you know, a you know, a FIR filter or something like that to be implemented between this pin and this pin." Well, you can just reconfigure it anything you want.

**Dave Jones:** If you've got enough space left in there, no worries. You put a FIR filter in there or a PID. You can tweak PID controls or do whatever you can possibly imagine.

**Dave Jones:** So, they're more powerful in that respect than a field programmable uh microcontroller because they're not just a processor, they're not just a microcontroller. They can do anything, as we said, anything at all.

**Dave Jones:** And we talked about the massively parallel thing, and this is one of the huge advantages of FPGAs and the main one of the main reasons why you would choose them over a microcontroller for certain projects because if you take your basic microcontroller, it's effectively a bottleneck.

**Dave Jones:** Everything has to run through that processor core in sequence. You know, you've got your individual line of code, you execute each instruction code one by one, and you have to rely on doing that fast enough.

**Dave Jones:** Even if you've got a real-time operating system, it's not really real-time. You can't process these 10 pins at the exact instant that you're processing these 10 pins up here and toggling these outputs here.

**Dave Jones:** It doesn't happen. But with FPGAs, you can because this all these logic block all these logic blocks in here are completely configurable, completely separate. So, you can be processing these pins down here and outputting something over here at the exact instant that you're processing these pins up here and outputting something else over here.

**Dave Jones:** And you can do that, if you've got enough IO pins and enough logic blocks, you can do that hundreds and hundreds of times. So, you can be processing hundreds of things in parallel.

**Dave Jones:** Take for example an analog-to-digital converter. If you had 50 channels of an of ADC data coming in, you know, you had an external ADC chip, of course, cuz these are only digital.

**Dave Jones:** They can't do anything in the analog domain. Well, if you got all this data coming from 50 analog-to-digital converters, 50 channels, and you wanted to process that all at once, well, you can yeah, have a 50-channel uh sample and hold, and then you process it to do it all.

**Dave Jones:** You know, there's a real bottleneck, speed bottleneck there. But in an FPGA, you can have each one a particular bunch of logic blocks dedicated to that one channel. And then you can just duplicate that 50 times, or 100 times, or 500 times within inside your FPGA.

**Dave Jones:** Cuz remember, we've got hundreds, sometimes hundreds of thousands of these logic blocks to play with. Fantastic. So, that is the massively parallel advantage of FPGAs. If you want to do a whole bunch of processing all at once in parallel, then FPGAs are what you want to use over a microcontroller.

**Dave Jones:** And that brings us to one of the final advantages, the high IO count. Um FPGAs specialize in high IO count applications. In fact, the development of FPGAs has really just pushed towards that high pin count capability.

**Dave Jones:** And it's actually quite difficult to get a decent FPGA. And by decent, when you talk about a decent FPGA, you're talking about how many logic blocks effectively it's got.

**Dave Jones:** It's hard to get a decent FPGA with a small number of IO pins. You know, it's not like you can get an SO-16 package, or a even a you know, a 44-pin quad flat pack.

**Dave Jones:** They're actually quite hard to get. That's why most FPGAs are designed for high IO applications. So, they contain hundreds of pins up to, you know, 1,000 plus pins. And because they've got so many pins, they often come in real pain in the ass to use packages like BGA.

**Dave Jones:** So, if you want to drive, for example, some huge LED matrix, you know, you had a you know, a 100 LEDs by a 100 LED matrix or something like that.

**Dave Jones:** Yeah, you can do it with a microcontroller and a whole bunch of external 74HC595 latches or something to latch the individual rows and columns and all that sort of thing.

**Dave Jones:** That's sort of the traditional way to do it. But then, as I said, you come into that real speed bottleneck. The processor has to drive all that incredible incredibly quickly just to get, you know, 25 times per second updating on your LED matrix display.

**Dave Jones:** Well, FPGAs can do all of that in parallel because they've got hundreds of IO pins. So, you can choose one with hundreds of IO pins. You can do it all at once.

**Dave Jones:** Bam! Straight in there. So, that's the huge advantage over microcontrollers. So, these FPGAs sound fantastic, right? Why doesn't everyone use them? They're so fantastic. You can program them to do absolutely anything.

**Dave Jones:** Why are they not in every single product and every hobbyist toolkit? Well, there's lots of disadvantages, and I probably haven't even listed them all. Let's go through them. These FPGAs are expensive.

**Dave Jones:** Why are they expensive? Well, they're expensive relative to another chip which does that could do, potentially, a similar function. I mean, you can get FPGAs as little, you know, as a dollar or two, but they don't contain many configurable logic blocks.

**Dave Jones:** So, they're quite limited in what you can actually do with the things. And so, they're expensive in a relative sense. For example, if you wanted to duplicate an AVR microcontroller in an FPGA, there is no way that you can get one big enough to put an AVR microcontroller in there that's going to be cheaper than just buying the AVR microcontroller on its own.

**Dave Jones:** So, if you're just looking to duplicate the functionality of a pre-existing dedicated hardwired chip, you're wasting your time. So, that's why they are quite expensive. And FPGAs, the really high-end ones, you can pay many, many thousands of dollars for just the one chip.

**Dave Jones:** FPGAs are some of the most incredibly complex and bleeding-edge process technology chips on the market. Why? Because they have to contain mill- sometimes millions of these logic elements and routing paths and and and configuration fuses and everything else just to give you that flexibility.

**Dave Jones:** So, they are very So, they are relatively expensive. And because they also contain all of this flexibility, it means that they're not optimized for power consumption. So, if you're after an ultra-low power design to do something, there's no way an FPGA or an equivalent FPGA is going to be the same as or lower power or nearly as lower power as a dedicated chip to do the function.

**Dave Jones:** It's just not possible due to the process technology and all the complexity. So, they're quite high-power devices and they can chew a lot of power when they start up.

**Dave Jones:** A surge current when they start up and program all these fuses, for example. So, just got to be very careful. You wouldn't use them in a low-power design. They're volatile.

**Dave Jones:** As I said, they completely forget everything. These FPGAs are brain dead. You have to have an external configuration flash memory in order to reprogram the FPGA every time you apply power.

**Dave Jones:** And that can lead to boot time issues. I mean, some uh you want just to work instantly. You can't just uh do that with FPGAs. Although there are some that do have configuration flash.

**Dave Jones:** We'll talk about that maybe. And as I said, they are high pin count. If you're looking for a hobbyist-friendly or a really production-friendly device, an FPGA is not the best way to go about it.

**Dave Jones:** As I said, you can get low low pin count devices. There are a few out there, but they're generally not in easy-to-use packages. Most of them these days come in BGA packages, which are not easy to use.

**Dave Jones:** So, often you have to take that into account. And the other thing is because they're optimized for high pin count, generally if you want a lot of configurable logic blocks in here, a lot of logic density, then you generally have to go for a higher pin count device.

**Dave Jones:** They sort of go hand in hand. High logic density, high pin count. Why? It's annoying. The manufacturers just do it because that's where they think the market is or the market's being driven by those sort of application.

**Dave Jones:** So, it's not like you can get a million logic element device in a nice friendly, you know, TQFP, you know, a 44-pin package or something. It's just not going to happen.

**Dave Jones:** So, they are And the other thing is they are complicated. They are incredibly complicated. Go down Go to the manufacturer's data sheet, Xilinx or Altera or one of the others, and download a data sheet for an FPGA, and you can spend the rest of your life reading that thing.

**Dave Jones:** It's not just one data sheet. Then they have all these different data sheets and applications for how these configurable logic blocks work, how the IO works, how the clock systems work, how the serial interfaces work, and how the DSP cores work in the things, and and how to program them with the best way uh best and quickest way and safest secure way to program them when they boot up, and

**Dave Jones:** ah, they've got, you know, uh dozens and dozens of data sheets and application notes for just the one device. They are Believe me when I say it, the most incredibly complex chips on the market.

**Dave Jones:** Take my word for it, or don't. Go read it for yourself. Um and because they are so complicated, they contain many traps for young players. There's lots of things that can go wrong in this thing.

**Dave Jones:** Because you are effectively designing the chip yourself, you have to take all the timing into account, all the routing into account, and the complexity of the device and how do you configure the IO blocks.

**Dave Jones:** And I haven't even scratched the surface of the complexity of this thing. This is incredibly simplistic what we've looked at here so far. So they are many traps in terms of not only just configuring the things, choosing the right clock pins, for example, because some in addition to these IO blocks here, they'll have dedicated clock pins which have faster routing paths through here.

**Dave Jones:** And depending on if you want a really fast design, you have to know how to use configure your um uh logic in the correct correct uh part of the FPGA.

**Dave Jones:** It can make a difference where you physically place all your stuff in the FPGA. And the tools can sort of take care of some of that or a lot of that for you, but you really have to be aware.

**Dave Jones:** And there are a lot of traps just in configuring and choosing an FPGA. And uh that's the thing. The tools are incredibly complex. Um go and download the tools for these FPGAs, and it's like many gigabytes of downloads, and it There are so many tools which come with these FPGAs.

**Dave Jones:** They are incredibly complex. Yes, you can get uh nice development kits which, you know, have example programs, and you just install all the tools. And even though they got tens of millions of lines of code in there, it all just Yeah, you can get these simple development kits to just work and you can get a simple application running in your FPGA and they look easy, but from that aspect

**Dave Jones:** when you first use them, but when you want to do your own professional design from scratch, boy, you can spend a year just choosing and selecting and programming and configuring and optimizing a you know, a moderately complex FPGA design.

**Dave Jones:** The tools are necessarily complex because these devices themselves are incredibly complex. And as I said, they're hard to choose and compare. Go to just two of the manufacturers, the two top ones who own like 80% of the market, Xilinx and Altera, and try and figure out and compare two different devices.

**Dave Jones:** They'll call these logic blocks different things, configurable configurable logic blocks, they'll call them logic one manufacturer call them logic elements, someone will call them something else. They can contain different number of lookup tables in them.

**Dave Jones:** They might use terms like system gates and all sorts of stuff which confuse the issue and they don't have the industry does not have common terminology for the architecture inside these FPGAs.

**Dave Jones:** The manufacturers all have their own architecture terminology. The architecture is entirely different, the terminology is entirely different between manufacturers. And just being able to choose between, you know, you take for a you take advantage of the fact that it's simple to compare micro controls for example between PIC and Atmel.

**Dave Jones:** Right, yeah, one contains, you know, X number of ADCs of 10 bits, it contains two UARTs, it contains X timers, and you know, they're all fairly generically similar, but FPGAs totally different.

**Dave Jones:** So, good luck trying to choose and compare not only between manufacturers, but choosing the correct size device for your project because when you start your project you might have an idea of what you want to do and you go, "Okay, I need an FPGA because of some of the advantages we talked about." But then you find that well, like how many logic elements do I need because the a device with, you know,

**Dave Jones:** 128K logic elements might cost, you know, twice as much as one with 50,000 logic elements or something like that. How many do you need? You don't know until you actually design your code and then run and and then compile it or synthesize it and try and get an estimate of how many logic elements you're going to use.

**Dave Jones:** So sometimes you have to actually do your design first and then choose your design and then choose your chip last when you know what, you know, how many logic elements you're going to need and things like that.

**Dave Jones:** Maybe you use the power estimating program in the tools. They contain you don't know how much this power this FPGA is going to draw. Don't bother going into the data sheet and going, "Oh, how much current does this FPGA draw?"

**Dave Jones:** It draws nothing when you got nothing in there or, you know, sort of, you know, just a quiescent current but when you're running depends on how much logic you're running, how many IO blocks, how fast, how they're configured, all sorts of stuff.

**Dave Jones:** It's completely dynamic so the tools contain power estimating programs. And so it's just amazingly complex these devices. So you don't generally want to use FPGAs unless you're A really experienced in or B you absolutely need them for some of the advantages we talked about the massively paralleled nature of a project for example or the really fast IO processing or something like that.

**Dave Jones:** Now, here's something that we haven't talked about yet and it requires separate videos. In fact, everything I've talked about here and a whole lot more I could do a one or two hour video on each and every aspect of these FPGAs.

**Dave Jones:** And these HDLs or hardware definition languages are no different. So, these are generally how most people program FPGAs these days. They don't use the schematic capture anymore, even though you can do that if you really want to.

**Dave Jones:** These hardware definition languages, the two major ones are VHDL and Verilog, you may have heard of around the traps. Now, I may get hauled over the coals for this one, but I generally they are not easy and they're not intuitive like your more sequential programming languages like C and basic that you're familiar with on your PC or your microcontroller where you get the processor which executes each instruction line by line by line by

**Dave Jones:** line. FPGAs don't contain a processor unless you put one in there. They are just a sea of logic gates. So, using code to define things like multiplexers and counters and and gates and flip-flops and all that sort of thing is not really that intuitive to most people who've learned electronics and digital electronics the traditional way with gates and flip-flops and muxes.

**Dave Jones:** It's It's a real different world where you have to think that everything's executing in parallel and you have to think about clock domains and all sorts of complicated stuff.

**Dave Jones:** So, HDL it Yeah, you might be able to load your example program when you get your $100 FPGA demo board, but then trying to really understand it and that comes back to the traps as well.

**Dave Jones:** There's not only traps in configuring the FPGAs, but there's also many traps in how well you write or how well you can write your hardware definition language in VHDL or Verilog.

**Dave Jones:** There's lots of traps there that can cause all sorts of problems inside your FPGA, race conditions and all sorts of stuff that we won't go into, but there's and I've probably left off some other disadvantages, but there's a lot of disadvantages to FPGAs and that's why they're not hugely popular except for the more niche applications where the advantages are really so compelling that you'll want to use an FPGA.

**Dave Jones:** Now, I've been going on for like 30 minutes on just what an FPGA is and quite frankly, I haven't even scratched the surface because the simplistic architecture I've sort of explained here is not how modern FPGAs are.

**Dave Jones:** Well, they are in a basic operational sense, which is good introduction of how they actually work, but you know, in practice when you want to implement an FPGA, they're incredibly more much more complex than this.

**Dave Jones:** They haven't been sort of this simplistic with just like the CLB and just the routing paths and the just the IO block and that's pretty much it. They haven't been that way since the dawn of FPGAs many decades ago.

**Dave Jones:** All of your modern FPGAs contain a whole slew of functionality in these things, no pun intended, because there's things like a slew rate control in the IO blocks. Memory is a big thing in FPGAs these days.

**Dave Jones:** Almost all decent FPGAs will have various forms of memory in them in terms of distributed memory which you can utilize in different ways depending on your architecture, your internal architecture you're trying to design, or they can have dedicated RAM blocks and you can implement dual port memory.

**Dave Jones:** You can do all sorts of stuff because a lot of processing happens inside modern FPGAs. That's what a lot of people use them for. So, they'll even contain these days, the manufacturers realize, well, people were all implementing what's called these soft processor cores, which means you might get like a NIOS core, which is or the manufacturers have their own types of, you know, 8, 16, 32-bit or

**Dave Jones:** more processor cores, you can just drop them in there. And they're a soft core, soft because they they can you can just configure it sort of anywhere within the FPGA you want.

**Dave Jones:** As well as a lot of other functionality, but a lot of manufacturers are going, "Well, a lot of people use these cores and they use other functions within the FPGA." Basic stuff like might be an Ethernet controller, for example.

**Dave Jones:** So, they go, "Okay, well, let's put hard logic inside these FPGAs as well." So, they'll embed like an ARM processor and that's actually not in the FPGA fabric. It's not a soft function, it's a hard function.

**Dave Jones:** So, it's, you know, it might have a little ARM processor over here or a couple of them. And they might have, you know, Ethernet transceivers or big uh serdes, serial controllers, and all sorts of things implemented as all this hard logic around what traditionally was a soft FPGA fabric.

**Dave Jones:** The advantage of having that hard processor and hard logic in there is that uh if you know you want a processor in this thing, well, you're better off going for a hard processor with the FPGA fabric around it because it's going to be more optimized, it's lower power, you don't have to worry about designing that aspect of the processor in, you don't have to recompile the processor each time you

**Dave Jones:** want to uh you know, recompile the design for your FPGA. It's all hard in there, just like a microcontroller or microprocessor, and you know it's guaranteed to work. Because the disadvantage of these FPGAs is nothing's guaranteed to work because you've designed it or you've written all the code, you've dropped in all the blocks, even if you might pull these uh you know, modules off the internet, how

**Dave Jones:** do you know if they work? How do you know how the software has routed it within here? Because that's the other thing with FPGAs, routing is a huge part of this thing, and actually fitting all of your design and optimizing.

**Dave Jones:** That's why these tools are incredibly complex, and it can actually take sometimes, you know, a long to like days to actually really fit and compile a real huge design and optimize it inside one of these FPGAs and get the correct timing and routing paths.

**Dave Jones:** And that's the other thing, clocks. These things will have dedicated clock pins and dedicated clock routing paths. Uh I think I said before dedicated clock quadrants, so you can't just uh utilize this logic over here with a clock that you're using on this pin over this side of the FPGA.

**Dave Jones:** And they'll come with uh DSP blocks. That's another very common thing. You'll see that uh uh this FPGA contains uh multipliers, accumulators, and MACs, and DSP cores all scattered around.

**Dave Jones:** A typical FPGA these days might have, you know, 50 or 100 DSP little cores all scattered around the place. And on top of all that complex uh clock routing structure inside modern FPGAs, they'll contain uh digital clock management uh systems.

**Dave Jones:** They go under various names, uh PLLs, and all sorts of things to multiply the external clocks. That's why you might typically find one of these FPGAs working like the external crystal is only 20 MHz, for example, but the process but all the logic inside might be running at a couple of 100 MHz because they mul- those PLLs and digital clock managers, you can multiply the external clocks.

**Dave Jones:** can do phase shifting, and you can do very complicated timing uh and clocking arrangements within side your FPGA architecture, but that opens up a whole can of worms in terms of uh clock timing for your entire system.

**Dave Jones:** And you can really goof that up if you don't know what you're doing. And I haven't even started on the complexity and the limitations, as well, of designing uh compiling your designs into an FPGA.

**Dave Jones:** But, this is the basic architecture of them. And well, you don't be afraid because you can get simple development kits. Start up using FPGAs are are an important part of the electronics design toolkit.

**Dave Jones:** So, they are definitely worth learning. So, don't be afraid because there are some powerful advantages to FPGAs. So, I recommend you actually go to the manufacturer's websites, Altera, Xilinx for starters, uh for example, and check out all the range of FPGAs they've got available.

**Dave Jones:** There's basically one available for every niche applications. Ones are designed for really fast serial processing, others are designed for massive IO, others are designed for DSP uh type work, and others are designed for a whole combination of those things.

**Dave Jones:** Incredibly complex devices, and well, I haven't even scratched the surface. Really, I could do another 100 videos on FPGA. Will I? I don't know. Jeez. Catch you next time.
