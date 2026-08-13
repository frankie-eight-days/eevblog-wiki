---
video_id: dlsPf52MT4c
title: EEVblog #290 - Mailbag
url: https://www.youtube.com/watch?v=dlsPf52MT4c
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 11, "2": 30, "3": 44, "4": 86, "5": 110, "6": 131, "7": 149, "8": 169, "9": 187, "10": 200, "11": 218, "12": 236, "13": 257, "14": 275, "15": 293, "16": 310, "17": 326, "18": 344, "19": 358, "20": 370, "21": 386, "22": 403, "23": 418, "24": 435, "25": 456, "26": 476, "27": 498, "28": 511, "29": 528, "30": 547, "31": 571, "32": 595, "33": 613, "34": 630, "35": 646, "36": 661, "37": 674, "38": 689, "39": 712, "40": 729, "41": 747, "42": 765, "43": 778, "44": 796, "45": 826, "46": 845, "47": 865, "48": 881, "49": 899, "50": 915, "51": 932, "52": 951, "53": 966, "54": 982, "55": 999, "56": 1013, "57": 1033, "58": 1051, "59": 1069, "60": 1083, "61": 1097, "62": 1111, "63": 1129, "64": 1149, "65": 1165, "66": 1183, "67": 1197, "68": 1215, "69": 1233, "70": 1251, "71": 1265, "72": 1283, "73": 1299, "74": 1321, "75": 1337, "76": 1353, "77": 1369, "78": 1385, "79": 1401, "80": 1421, "81": 1437, "82": 1457, "83": 1473, "84": 1487, "85": 1503, "86": 1523, "87": 1537, "88": 1553, "89": 1565, "90": 1583, "91": 1601, "92": 1619, "93": 1635, "94": 1655, "95": 1667}
---

**Dave Jones:** Hi, and welcome to the ever-popular mailbag segment, where I open my email that people have sent me. I've only got two items today, so we won't overdo it. Let's check them out. The first one comes from L. Groth, and I recognize the name.

**Dave Jones:** That'd be Logan Groth. So thanks, Logan. He's a fellow Aussie up in Queensland. I recognize the, uh, that's what the Q stands for, Queensland. One of those funny Queenslanders. Ah, shouldn't say too much. That's where my mum's from. Anyway, let's open this sucker up and, uh, see what we have here.

**Dave Jones:** Oh, by the way, he sent it to that crazy Aussie bloke. P.O. Box 7949, Balcombe Hills, NSW 2153. That's where you should send your stuff. So, thanks, Logan. Let's, uh, open it up. I have no idea. He hasn't, uh, clued me up that he'd be sending this, so let's go.

**Dave Jones:** What have we got? No, nothing else. We've just got bubble wrap. Let's see something in a box. Here's my trusty Victorinox Mini Champ here. There we go, that's better. What have we got? What have we got? Ta-da! Hi Dave, thought you might be interested in a Renesas promo board.

**Dave Jones:** They sent me one, however a second unit turned up a week after, so hey, enjoy! Thank you very much, Logan. What have we got? We've got a Renesas RL78G13 promo board. Advanced features such as ADC operation without CPU wake-up. Ooh, similar to the, uh, Gecko that, um, we had a look at, uh, several weeks back.

**Dave Jones:** High performance core running at, uh, 1.27 DMIPS per megahertz, and, uh, system cost reduction with on-chip data flashing, configurable high-speed oscillator system, safety functions to support IEC6730. What's IEC6730? I don't, uh, recognize that one off the top of my head. I have to check it out.

**Dave Jones:** And thankfully it's not one of those hideous, uh, heat-sealed packages. You just open it like that, and it opens just like a damn well should. Those heat-sealed ones, they suck. Big time, let me tell you. What do we get in here? We get, uh, yeah, it's a promo board, yeah, whatever.

**Dave Jones:** Bit of cardboard. We get a CD. Ooh! We get a screwdriver. Flathead. Eh. Um, and we get a USB cable. A USB cable! Jeez, how many bloody USB cables have I got? Ugh. And check out this ridiculous part number. YRPBRL78G13? You've got to be kidding me.

**Dave Jones:** Who thought up that rubbish? Anyway, it turns out that this is a, um, a, uh, development slash demo board, really for, uh, the RL78 series micros. And it's pretty obvious why they gave you the screwdriver and the kit, because they've got a 10-turn pot on there,

**Dave Jones:** there's a couple of leads and jumpers, and, uh, that's about it in some sort of, uh, dip, um, arrangement here, presumably so you can put some headers on and plug it into a breadboard. But they don't give you the header strips in the kit.

**Dave Jones:** Um, bummer. And apparently it is, um, ooh, ooh, look. Made in Europe. Beauty. Not made in China. Awesome. I love it. ROS compliant. Yeah, yeah, yeah. And, um, apparently it comes, uh, pre-programmed with, um, uh, firmware to be used with the demo software on the disk

**Dave Jones:** to test out the low-power capabilities of these micros. Well, let's check it out. And the first thing I did is Google IEC6730, and I came up with this, uh, Renesas, uh, web page about it, and, uh, it looks like it's a standard for, um, appliance, uh,

**Dave Jones:** for reliability, um, in, uh, appliance product design. It's got three different classes. Class A, uh, control functions not intended to be relied upon for the safety. Class B is control functions which are intended to prevent unsafe, um, operation of controlled devices. And Class C is control functions which are intended to prevent,

**Dave Jones:** uh, special hazards. So appliances such as washing machines, dishwashers, dryers, uh, you know, microwave ovens and things like that, they would be classified as Class B. And it seems that, uh, all the microcontroller manufacturers have something on this. Here's, uh, Freescale, and they talk about the safety standard

**Dave Jones:** for household appliances, the three different classes. They've got a neat little, uh, pop-up thing here, and they talk about invariable memory, they talk about addressing and external comms, and, uh, all sorts of things. It's interrupt handling. Um, it's rather neat. Confirm that the CPU clock frequency is correct,

**Dave Jones:** not too slow, not too fast, no clock. So all of this stuff goes into, um, selecting a microcontroller to be used in one of these, uh, white goods or, uh, products to meet the IEC 60730 standard. And here's a white paper from Texas Instruments

**Dave Jones:** which, uh, showed up at, uh, near the top of the, uh, Google listing for this, and it goes into the various, uh, classes as well. And it goes into the requirements of the compliance and how their, um, system-level, uh, software actually supports that, like CPU registers stuck at fault

**Dave Jones:** and things like that. And, uh, uh, it goes into talking about, um, because the firmware plays a critical role in the self-test, uh, the IEC standard does not specify how the tests are made, only that they be executed successfully. There you go. And I'm sure anyone who has, uh, been involved with designing,

**Dave Jones:** uh, commercial white goods or commercial products like that goes, yeah, I know all about IEC 60730. But there you go. I kind of sort of knew there were standards for these things, but I didn't know the, uh, number, and I haven't really been involved in that.

**Dave Jones:** So there you go. You learn something new every day. All right, I just installed the software, and I chose the quick start, uh, option instead of, uh, doing all of the tools. So here you go, and it popped up with the quick start guide here.

**Dave Jones:** Here's our little board. Um, it looks like that's done in, uh, Altium Designer because that, uh, 3D model there is, uh, very Altium Designer-like. So I think that's what they've used to do this. Here we go, and, uh, there's some demo software with, uh, graphs that, uh, it looks like

**Dave Jones:** measures, uh, voltage and temperature, perhaps. Anyway, let's, uh, run the software and see what we get. And it looks like, um, oh, here we go. Low power tab. Low power modes can be entered by directly clicking halt, stop, or snooze. Uh, blah, blah, blah.

**Dave Jones:** And it looks low current consumption can be measured when the low power modes are selected. Jumper J3 is used for current measurement. There you go, you can remove the, uh, jumper and you can measure the consumption directly of the micro, just like we did on that gecko board.

**Dave Jones:** Excellent. And I won't actually bother measuring the current, of course, uh, but anyway, here's the table just, uh, in run mode. 5.1 milliamps, and that looks like it's running at 32, uh, megahertz. And, uh, halt mode, 1 milliamp. I'm not sure the 32 megahertz oscillator is on.

**Dave Jones:** The 32 kilohertz oscillator is on, doing various stuff, so what's the difference here? I don't, ah, right, oh, the CPU itself is actually, uh, switched off. So, uh, the main CPU's not actually executing. Stop mode, 620, oh, sorry, 620 nanoamps. Yes, um, and what are we doing in 620 nanoamps?

**Dave Jones:** We're running our 32 kilohertz, uh, oscillator, and we're running our real-time clock, and that's, and we're doing some RAM stuff. So that's about it. Um, and snooze mode, 1 microamp, and what are we doing there? 32k, and ADC is on periodically, so you're doing some sort of data logging

**Dave Jones:** or something like that, uh, presumably directly via DMA into the RAM. Once again, very similar to the, um, uh, Gecko devices. Wah, wah, wah, wah. Device driver software not successfully installed. I plugged the device in, and, uh, I get nothing. It says unidentified device.

**Dave Jones:** I can't even read the device code out of the thing. What the hell's going on? I got my blue LED, uh, happening on the board. I've tried a different USB port, and, uh, I did the quick start, um, software installation, which went fine.

**Dave Jones:** What a fail. Well, that sucks ass, really. I'm not gonna bother dicking around. Ah, look, it's just, the program just shut down. You gotta be kidding me. I don't think I'm gonna bother. Gonna open the next package. Bugger this. It's from, uh, Craig, uh, Rodine,

**Dave Jones:** from, uh, Cronau. Thank you very much, Craig. Um, he's from, uh, Monument. There you go, Monument in, uh, CO, which is Colorado, I believe. Monument, Colorado. Sounds like a nice place. Hello to all my, uh, viewers in Colorado. Now let's, uh, open this sucker up,

**Dave Jones:** and, uh, see what's inside. Well, I know what's inside. It, uh, it's written down here. USB logic analyzer. Whoo-hoo! Claims it's $190 worth. So let's have a look. USB logic analyzer, brilliant. Absolutely, ah, this is just, yuck. I hate these stupid, uh, where does it open?

**Dave Jones:** How does this thing open? Here we go. Let's try this. Oh, there we go, tape along this, yeah. Alright, fail. There we go. Now we've got it open. Bloody tape. Alright, here we go, ta-da! Ooh, Cronoview. Let's have a look. Hello, Mr. Jones, please find and close

**Dave Jones:** our 8-bit USB logic analyzer kit. Is it a kit? Build-it-yourself kit? Or is it fully built? Interface software, uh, for Mac, Win, and Linux, cross-platform, um, is included, and also available for direct downloading from cronoview.com. I will resist the temptation to pitch the product to you,

**Dave Jones:** and instead hope you have time to evaluate and review this tool. Well, we'll certainly do that here on the mailbag. So thank you very much, Craig. And by the way, I had a couple of people bitch, uh, last time, um, about the mailbag segment,

**Dave Jones:** that it was just one big, uh, you know, advert, one just long advertisement. It's just an advertisement for products. Well, like, duh! Of course it is. People send me shit, and I open it up, and I look at it. And if it's good, I, you know,

**Dave Jones:** I'm gonna say it's good. If it's bad, I'm gonna say it's bad, and we're gonna have a look at it. And, uh, you know, it's unbelievable. Of course this is effectively, um, an advertisement. You send me stuff, and well, you can, you know, live or die right here,

**Dave Jones:** live opening on the mailbag. And you wanna know what the funny thing is? I only get people saying that sort of thing if it's a product they didn't like. For whatever reason. They just didn't like it, so they bitch. Ooh, it's just an advertisement for the company.

**Dave Jones:** Bloody hell. I don't get any complaints about that when it's a good product. Give me a break. Anyway, sorry about that rant. Let's have a look at the, uh, ChronoView. ChronoView LA8. 8-bit, so it's a pretty, um, looks like it's a low-end price,

**Dave Jones:** low-end logic analyzer. Ooh! And it's in the sub-$200 category. Ooh, that's nice. And, uh, let's look at that. What else have we got? We've got some, ah! Color-coded, um, easy hooks. Excellent. We've got our software, uh, software cable. There we go. And we've got our USB cable.

**Dave Jones:** Again, ooh! It's a, um, A-type. It's not a mini-B. It's a rather nice-looking pouch. I like it. It's got a little thing in there where you can put your easy hooks and, uh, your test cable. And Velcro opens. It's quite nice for the, uh, price, actually.

**Dave Jones:** I wouldn't have expected, uh. Ooh! Ooh! Alloy case. I like it. Extruded aluminum case. Ooh, that feels good. What else have we got in there? Oh, we've got a, yeah. We've got a shoulder strap. You want to carry your logic analyzer around on your shoulder strap.

**Dave Jones:** Bit of, uh, street, uh, you know, nerd cred on the street there. Oh, yeah. What's in your bag? Oh, my 8-bit logic analyzer, mate. Well, now, I'm certainly quite impressed with this. It's built like a brick dunny. It really is. It's, uh, quite nice, solid construction.

**Dave Jones:** The chrono view. Um, don't know about the font on the end there. That's a bit... I haven't really seen a font like that in a product in a long time. I have no idea what these, um, LEDs mean. I-A-T-D. Well, there's enough room on there

**Dave Jones:** to print the full, um, uh, word. So, well, it's pretty non-eventful. But that's, you know, a logic analyzer. I think we're going to have to crack this thing open. And what's inside? Well, it's probably just a, uh, FPGA with a, uh, USB interface and an, uh, input buffer.

**Dave Jones:** And that's, uh, probably about it. Anyway, in this sort of, uh, price range, that's, uh, typically what you get. But anyway, let's crack it open. Hmm. And here it is. It should just slide out. And it does! Whoa, Xilinx FPGA time. And there's no real, uh, surprises on the board,

**Dave Jones:** except I was, uh, wrong in that, uh, this is not an FPGA. It's a Xilinx, uh, CPLD. Specifically, a cool runner to an XC2C256. A 256 macro cell CPLD. Because, well, this, you know, it doesn't need to do, um, something incredibly, uh, complex.

**Dave Jones:** So you can get away with a cheaper, um, CPLD for something like this. We've got an FT, uh, 245, um, USB to parallel, uh, interface. That's got a built-in, uh, FIFO buffer, so it buffers the data so you don't actually, uh, lose anything when you're continuously transmitting.

**Dave Jones:** We've got a 64 megabit, uh, DRAM down here, which means, uh, 8 meg samples per channel. It's also got, uh, pre-triggering. I think it's up to a couple hundred K pre-triggering, uh, data memory as well. And, uh, I'm not sure what that device there is.

**Dave Jones:** It's a PT7015102. It looks like, uh, just a voltage regulator or something like that. So, um, pretty much. We've got the main oscillator, of course, and that's pretty much all there is to it. There's the internal, uh, JTAG interface, so if you wanted to, uh, hack this thing,

**Dave Jones:** I'm sure you could. We've got our LEDs and our input side here. We've got an octal, uh, buffer, of course, because this is 8-channel. It's just a, uh, 74 TTL, um, series, uh, octal, uh, 244 octal buffer. It's a 74, uh, LVTH series,

**Dave Jones:** which, uh, is compatible with, uh, different logic families. So you can use it on 5 volts and 3.3 volts, or, uh, possibly even lower, uh, input compatible. But one thing to note, there's no, um, input pull-down resistors, uh, at all. It's just, uh, or input protection or anything like that.

**Dave Jones:** It's just connected directly to the input of the 244. That's not the best. And, of course, there's nothing fancy in this thing like adjustable, uh, level, uh, trigger threshold or anything like that. It's just, you know, direct, uh, CMOS, uh, TTL, uh, input buffered.

**Dave Jones:** That's it. Doesn't even have an external clock input. So it's timing analysis only. It can't do state analysis. But with 100, uh, meg samples per second and, um, 8 meg samples of memory, um, it's, you know, it's a handy little, uh, logic analyzer.

**Dave Jones:** A little 8-channel logic analyzer. And it's priced accordingly, of course. It's in the, uh, low-end price bracket for these sort of things. But really, um, in logic analyzer, what it's all about, really, is the software is the main thing. And this board is, uh,

**Dave Jones:** Rev A2 and copyright 2010. So it's, uh, been around for a couple of years. And indeed, the silkscreen, uh, date code of, uh, 1510 backs that up, um, as does the, uh, QC sticker down here of, uh, 1910. So presumably, uh, this thing was

**Dave Jones:** manufactured in, uh, and tested in, uh, 2010. So it could have been an old stock they sent me, I'm not sure what's going on there. And if we have a quick look at the, uh, ChronoView website, uh, here's the specs. As I said,

**Dave Jones:** up to 100 mega, 100 meg samples per second, 8.4, uh, meg samples per channel, uh, 256k, uh, pre-trigger channel capability, um, signal loading they claim is roughly 5, uh, picofarads, um, plus 100 microamps state holding current, um, the input voltage ranges from 0.5 volts

**Dave Jones:** to, um, 6 volts. And a logic 1 threshold does go to, uh, from 2 volts to 5.5. So you could, uh, use, uh, any, uh, logic standard within that range. So certainly easily able to do, uh, 2.5, 3.3, uh, or 5, or, uh, 5 volts,

**Dave Jones:** uh, TTL interface. And it's a USB, uh, 2 full speed interface, and they claim it has, um, I2C, SPI, and UART, uh, bus support as well. Whether or not that's actually in the, uh, hardware, or whether or not that's, um, just software analysis later, I assume

**Dave Jones:** it's, uh, it's software based. So there you go, uh, let's have a look at, um, they've got a what's in the box. And probably, ha, it just tells us what's on the board, and we just looked at that, so there you go. We already know everything

**Dave Jones:** we need to know about that. Alright, so I've got the, uh, software running here, it, uh, was, uh, painless installation, the driver's no problem, and the, uh, program pops up here, not a problem. Now I've actually got it, uh, physically connected to an SPI

**Dave Jones:** bus here, and I haven't labelled my, uh, channels, but obviously this is the, uh, clock up the top here, this is the data, and this is the, um, this is the select pin. And, uh, here it is. You, uh, we've got various, uh, zoom up here, it's pretty basic,

**Dave Jones:** and, uh, let's see if the tooltips pop up. No, they did before. I swear they popped up, there we go, acquire data, an acquisition setup, uh, you can refresh it. I wonder how quickly it refreshes, because the acquire data takes quite some time, because it's got a, presumably

**Dave Jones:** it's reading the whole, uh, 8 megbytes, or 64 megbits over the USB there, and, uh, presumably we could, uh, can we refresh that quickly? I'm not sure, uh, what the deal with the, uh, refresh is, whether or not it, uh, resamples the data or not.

**Dave Jones:** Um, guess I'd have to read the actual manual, but, uh, the bus, um, setup, um, we can enable various, uh, things here, we can change, can we change the channel? Yes, we can change the channel color, we can change, uh, label the signal name, so

**Dave Jones:** if you know that's, uh, S-clock, of course, you can change that and it instantly becomes, um, S-clock. Okay, I was just about to, uh, complain that the bus setup here is actually quite, uh, you know, quite convoluted, quite manual to actually, uh, set this

**Dave Jones:** thing up, and then I figured out that they've got what's called the canned bus setup, which is basically a template, and you choose your bus type and it makes it easy for you, so there you go, SPI, number of bits, it's, you know,

**Dave Jones:** so it all sets up relatively easily. And there we go, I just, uh, captured my, uh, SPI bus there using the automated, um, setup capability and setup, S-clock and, uh, MOSI and, uh, MISO and, you know, it's all set up there and it gives you the decoded

**Dave Jones:** data, which is, uh, F6 in this particular case, uh, based on that clock, and, you know, it's okay, it does the job. Um, this, but this, uh, logic analyzer software isn't exactly, uh, blowing my socks off, but it's, it's basic and it does the job, and for the price,

**Dave Jones:** I guess you can't complain at all. So what happens if we go in here and we set, say, our state to, uh, uh, our MISO input here, which is always high, because I haven't actually got it hooked up, it's always high there, and, uh, let's try

**Dave Jones:** and trigger off that and see what happens, and really the triggering is not advanced, um, at all, it's just, you know, there's no sequence, uh, triggering by the looks of it, I, if it is in there I can't find any, uh, sequence based triggering, it's just a basic,

**Dave Jones:** uh, single state across all eight, uh, channels, either you know, high, low, or, uh, zero that, or, uh, any, um, state. So, you know, it really is basic, uh, triggering stuff. So let's trigger on that, and it should not actually, uh, trigger there, so if we acquire data,

**Dave Jones:** aha, there you go, that's what I wanted to test, it's not actually initializing and downloading the data, although I think there is a, um, it's waiting, because it's waiting for that trigger, and that trigger is, uh, clearly not happening. So how do I

**Dave Jones:** stop that? I thought I saw a setting for a timeout, or something like that in there, how do I press escape? Maybe? Oops. No, how do you stop, uh, uh, and data acquisition initiated hardware activity? No? Well, it's non-responsive, how do I stop this, uh,

**Dave Jones:** how do I stop the thing if I didn't want to trigger? Don't tell me it's gonna lock up, that's really quite terrible, it's just sitting there waiting for the trigger, it's not finding it, but it's not, surely, you'd be able to press escape?

**Dave Jones:** Argh! Better stop the recording and, uh, try and figure this out, hang on. Well, there you go, I just, uh, shorted that pin to low and made it trigger, and, well, for the life of me I couldn't figure out how to, uh, without, uh,

**Dave Jones:** you know, getting Windows to shut down the actual program. Um, that's really annoying, if it can't do that. Maybe there is, um, I'm not gonna investigate it, um, but that could potentially be, uh, quite annoying, and it looks like, um, I don't think you can actually, uh,

**Dave Jones:** set the data, uh, depth, because, um, like, sometimes you don't need that much memory if you just want to sample quickly and, uh, you know, you just want to, um, update this thing, then, um, you know, you don't want to wait to download the

**Dave Jones:** full 64 meg samples like that, so, or meg, uh, bits, um, 8 meg samples like that because it does quite take an annoying, rather annoying little, um, amount of time there. You saw that message that said evaluating bus there, it was obviously, uh, decoding that, and it

**Dave Jones:** hasn't, um, centered my stuff on the screen because it's all the way over here, um, because my trigger condition, that's the pre, I assume that's all the pre-trigger data in there, so it's automatically captured that, and there's my, uh, SPI bus. So you can see the advantage of the

**Dave Jones:** cheap memory though, but, um, I, you know, we can zoom across here like this, hang on, what's going on here, the decoding has to catch up there, so I'm not sure what happened, uh, I think there's a glitch in my SPI bus, I'm using a

**Dave Jones:** demo, uh, board to generate uh, SPI, so like, whoop, there we go, we can put, uh, a marker there, can we zoom in? Yeah, we can use our, um, scroll, our mouse, uh, scrolly center wheel to, no, it looks like it just moves it from side to side, we have to use

**Dave Jones:** the plus minus buttons, it's not, the user interface is not massive, see, I would have expected it to center around that line there where I had it, but it didn't, like expand around that line, but it, it doesn't. Um, yeah, I think the, the GUI

**Dave Jones:** needs some work, you can actually analyze your data, um, but it's not, it's not the greatest, look at all that, I don't know what's going on there, so I don't know if that's, I assume it's not the analyzer, that could certainly be a

**Dave Jones:** glitch in my, uh, demo board because it's designed to, uh, do that sort of stuff I believe, but um, yeah, so it works, and it's got search capabilities, you can actually go in there and, uh, you can search for, um, a particular um, state, or something

**Dave Jones:** like that, so, uh, whether or not they occur simultaneously, locate occurrences separately, so, you know, it's got a rudimentary search capability bit. There you go, that's the user interface, um, I'm not, uh, bowled over by it, um, at all, but it seems to do the job, and uh,

**Dave Jones:** for that sort of price category uh, USB logic analyzer, I guess it's not too bad. I'm not going to um, compare it with other logic analyzers on the market, don't ask me, I haven't looked at other low-cost, um, logic analyzers, this is not a

**Dave Jones:** review, this is just a mailbag, uh, quick look, really. So there's quite a few things that this logic analyzer seems to lack, you know, data compression, sample compression, for example, if you exhaust your, uh, you know, if you have, um, very widely spaced packets,

**Dave Jones:** and you're trying to, you know, capture a very small packet which is, you know, tens of seconds apart, or something like that, then you're going to run out of memory pretty darn quickly, because if you go into the acquisition setup, you'll see that at

**Dave Jones:** 50 nanoseconds there, where we can change our sample time to 50 nanoseconds, we're only going to acquire half a second of data. So, you know, if you're trying to capture events larger than that, you need a USB logic analyzer with sample compression. This one doesn't have it, it's very

**Dave Jones:** basic, it takes a bit of advanced um, firmware in there to actually do sample compression, not advanced, but it takes additional hardware capability in the device, firmware capability to actually do that, usually implemented inside an FPGA. I'm not sure if it would be possible to do that in a

**Dave Jones:** CPLD actually, it might be, but FPGA would certainly be the solution for that. And it's just pretty rudimentary triggering, there's no state triggering as I said, and well, you know, it's a real bare bones logic analyzer, but it seems to do the job.

**Dave Jones:** Might be possibly a bit on the expensive side for what it does, I don't know, I'm not going to compare it directly with the other ones, but it does come in a very solid, nice case. I like the case. And if we have a quick look at the price

**Dave Jones:** here, the basic kit is $129, I presume that's US and wouldn't include shipping, and the deluxe kit is $149. So it's cheaper than what they had marked on the package there, so certainly a reasonably priced logic analyzer, but if it's a value for money, I don't know,

**Dave Jones:** you'd have to compare it with the others on the market. So that's the mailbag segment. I hope you liked it, and remember, if you do like it, give it a big thumbs up on YouTube, and if you want to discuss any of this stuff, hop on over to the

**Dave Jones:** EEVblog forum. Catch you next time. EEVlog
