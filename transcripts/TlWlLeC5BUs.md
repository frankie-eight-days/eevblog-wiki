---
video_id: TlWlLeC5BUs
title: EEVblog #499 - What is JTAG and Boundary Scan?
url: https://www.youtube.com/watch?v=TlWlLeC5BUs
source: youtube-asr
timestamps: {"0": 1, "1": 14, "2": 32, "3": 48, "4": 59, "5": 75, "6": 90, "7": 108, "8": 123, "9": 135, "10": 154, "11": 171, "12": 187, "13": 202, "14": 225, "15": 239, "16": 256, "17": 270, "18": 287, "19": 303, "20": 315, "21": 330, "22": 348, "23": 362, "24": 375, "25": 389, "26": 403, "27": 418, "28": 434, "29": 447, "30": 457, "31": 474, "32": 486, "33": 499, "34": 514, "35": 530, "36": 543, "37": 555, "38": 569, "39": 585, "40": 597, "41": 611, "42": 625, "43": 643, "44": 657, "45": 671, "46": 683, "47": 700, "48": 715, "49": 726, "50": 739, "51": 751, "52": 769, "53": 782, "54": 798, "55": 814, "56": 825, "57": 835, "58": 849, "59": 865, "60": 879, "61": 897, "62": 914, "63": 926, "64": 944, "65": 962, "66": 977, "67": 989, "68": 1004, "69": 1015, "70": 1032, "71": 1057, "72": 1078, "73": 1092, "74": 1108, "75": 1124, "76": 1140, "77": 1155, "78": 1165, "79": 1178, "80": 1191, "81": 1202, "82": 1216, "83": 1231, "84": 1245, "85": 1258, "86": 1273, "87": 1285, "88": 1301, "89": 1318, "90": 1330, "91": 1347, "92": 1364, "93": 1377, "94": 1393, "95": 1408, "96": 1424, "97": 1441, "98": 1455, "99": 1467, "100": 1481, "101": 1496, "102": 1513, "103": 1528, "104": 1541, "105": 1554, "106": 1573, "107": 1587, "108": 1604, "109": 1617, "110": 1635, "111": 1646, "112": 1659, "113": 1674, "114": 1689, "115": 1703, "116": 1716}
---

**Dave Jones:** Hi, welcome to Fundamentals Friday. Today we're going to take a look at the JTAG interface. JTAG stands for the Joint Test Action Group, and I'm sure you probably heard of JTAG and you may have even used it in terms of

**Dave Jones:** programming a microcontroller or an FPGA or you and or using it as a debugging interface or something like that, for example. Well, that's not the only thing it can do. In fact, it originally wasn't designed for that. Uh JTAG came about in

**Dave Jones:** the late '80s when manufacturers started realizing that oh, you know, we're having a real lot of trouble testing assembled PCBs. Uh packages were getting more dense, so we're moving towards packages like BGA where the balls are on the bottom of the

**Dave Jones:** device. You can't use a traditional bed of nails tester to come down. And if you did, if you got a you know, a 500-pin chip or something, woah, that's a lot of test pins to come down and test your

**Dave Jones:** assembled PCB. It was getting very difficult. So, a bunch of manufacturers got together and said, "Well, what can we do about it? Can we actually embed a come up with a standard that allows us to embed some hardware into the chips so

**Dave Jones:** that they can we can use that to test themselves. So, we can access all of these pins under the PCB without having to use a traditional bed of nails test system. And that's exactly what they came up with. And it was ratified by the

**Dave Jones:** uh IEEE as a standard in around about 1990. And that's where the name comes from, the Joint Test Action Group. Test was originally designed as a way to actually get in there and test individual pins on uh a chip which has JTAG built into it

**Dave Jones:** on the assembled PCB. In cases where you couldn't physically get access like big BGA chips, for example, or there were just too many pins on a huge system that you just, you know, you'd have need thousands of pins to actually test it on

**Dave Jones:** your bed of nails or your flying probe tester. It'd take too long to move all the probes around to test it all. So, that's what it was originally designed for and hence the name boundary scan. JTAG is also known

**Dave Jones:** as boundary scan testing. And as the name implies, we have to have a look at a block diagram here of a typical chip that includes JTAG or this boundary scan testing. Now, this chip could be an FPGA, for example. It could be a

**Dave Jones:** modern microcontroller that has JTAG built in. It could be a special purpose custom chip that implements JTAG as well or practically anything on the market. A dead giveaway for a chip that has JTAG built in the pin names here. If they've

**Dave Jones:** got TDO, TDI, TCK, and TMS, you can bet your bottom dollar it's got JTAG built in. Now, not all of the chips have all of the same functionality because they don't need it. But, let's take for example a micro a modern microcontroller

**Dave Jones:** with a JTAG interface. Not only will it contain your traditional boundary scan around here, which we'll talk about, but it is also used as the interface where you can program your flash memory built in. So, it's going to talk to the flash

**Dave Jones:** controller built in. And yes, that microcontroller may also have another block in here, which then goes out to your traditional ICSP, your in-circuit serial programming method. And you may have two different methods actually program your flash microcontroller, for example.

**Dave Jones:** But, it's also going to go into debug controllers these days. We've talked about ice systems before, in-circuit emulators, which pretty much have gone the way of the dodo and have been replaced by the JTAG interface. So, that will also connect into the debug

**Dave Jones:** controller and that allows you to monitor and debug your code inside your microcontroller in real time. So, but that originally that wasn't really thought of when the JTAG, the Joint Test Action Group, originally started this. What they started it for is this

**Dave Jones:** boundary scan stuff around here. Now, this is the interesting thing about JTAG, which a lot of people aren't familiar with. They're used to using it to program and debug their microcontroller, for example, but there's much more powerful functionality

**Dave Jones:** behind it and most chips which have JTAG built in will also have this boundary scan capability around here. Now, what is boundary scan? Well, as the name implies, the it has some circuitry attached to each pin. You could call it like a JTAG

**Dave Jones:** cell, for example. I've drawn it as one big block here for that sort of, you know, joins all the pins, but in reality it's like an individual JTAG cell, a little bunch of logic in there which connects in between the usual chip IO,

**Dave Jones:** which we have looked at in the last video, for example, with FPGAs. We looked at all the complex IO stuff they had. Well, not only did they have that, I didn't show something last week and that's that bound additional boundary

**Dave Jones:** scan circuitry in there, which is tucked away between the chip IO and the pin. All right, you know, this is a just a a crude graphical representation of of how it works. How they actually implement it in there is up to the individual

**Dave Jones:** manufacturer, but it's easy to think of it as being between your regular IO drivers on your microcontroller or your FPGA, for example, and the pin. And during normal use, you program and debug your microcontroller, you I even know this JTAG, this boundary scan

**Dave Jones:** circuitry is actually in there. It just defaults to off when you power on the chip and it does nothing. It just passes the signal straight through from your regular chip IO circuitry here. So what they do with these little JTAG

**Dave Jones:** cells is they actually What I've kind of shown it here. I've shown an arrow going out like this and going into here, but in reality, as I said, they're like individual cells and they go from one to the other and there's a serial of one

**Dave Jones:** one line serial IO which goes in to each cell and then comes out and they're cascaded like that in a serial fashion until the data comes out. So you feed data into the chip and you can and it just cascades and ripples all the

**Dave Jones:** way through like this. Ripples a bad term because it's actually a synchronous clock in here which does everything, so don't confuse that, but and the data flows through in a serial fashion like that and pops out. And what

**Dave Jones:** does that allow you to do? Well, it depends on the functionality built into the boundary scan, but most of them are going to allow you full direct control over that IO pin. Not only are you able to read the value back directly on the

**Dave Jones:** pin of the chip. And this is why I've shown it actually sort of after the chip IO here. It's in between the chip IO driver and the pin because the idea of boundary scan is you physically read the actual electrical

**Dave Jones:** value on that pin, not after any of the chip IO or anything like that. It actually allows you to read exactly what's on the pin itself. So you can read back all that data and shift it out and do whatever you want with it. But

**Dave Jones:** not only can you read it, you can that they can have a driver in there as well that allows you to set a value on that pin. And being able to set and read values, that gives you an incredibly

**Dave Jones:** powerful tool to do in-system debugging. For example, we if this uh was a a microcontroller, for example, and we hadn't finished doing our firmware yet, we hadn't programmed the chip, it was empty, it does nothing, it doesn't matter. If we've got a populated PCB,

**Dave Jones:** what we can do is hook it up to our uh JTAG programmer, and we can individually talk to and drive and read all of the pins on the board. So, for example, let's say we had an external memory

**Dave Jones:** hooked up to this thing uh onto all these IO pins here. How do you test that memory to make sure it's okay? Well, we can write individual value values to the address uh and and data buses, and then

**Dave Jones:** we can read it all back. And we can actually exercise and test an external memory, for example, through our JTAG interface. But not only that, the assembled PCB, it allows you to test for your more traditional things like uh

**Dave Jones:** shorts and opens and things like that. So, and that's stuck bits. Let's say this pin in here is shorted to ground, like that. Well, what you try and do is you try and write a one to it and then read it back, and if you can't

**Dave Jones:** do that, oops, then you know it's shorted. If it always reads back a zero, then you know it's always shorted to ground. And also and then, if you had, say, two pins shorted like that on your PC on your assembled PCB, you had a

**Dave Jones:** little solder bridge or something like that, well, based on your testing algorithm, you can drive one and read the other, etc. And you can actually do all that in various combinations, and you can check for shorts between this

**Dave Jones:** pin over here and this pin, depending on your layout and your board, and all sorts of stuff. Incredibly powerful. And that is one of the main uses of JTAG, which a lot of people aren't familiar with. They just think it's programming

**Dave Jones:** and debugging, but nope, there's lots of powerful stuff hidden inside your chip you're probably already using. We've already briefly looked at the four main pins of the JTAG controller and that's all it takes. Four pins is always going to be four pins. There's a TDO,

**Dave Jones:** which is the data coming out of the chip. Don't confuse them in terms of uh your traditional TX and RX when you get them mixed up. TDO on a chip when it's labeled TDO is always the data coming

**Dave Jones:** out and TDI is always the data going the serial data going into the chip. And then you've got your uh T clock line, which is your synchronous clock, which actually controls all the data shifting and everything else in there. And you've

**Dave Jones:** got TMS, which is a control line, which does stuff as well uh based on that T clock and everything else. And those four pins allow you to feed data into the chip and read data back out. And one other powerful feature

**Dave Jones:** as well, after you've programmed your microcontroller here and you're running your firmware, you can also at the same time access this boundary scan stuff and read live data changing on your pins here. Woah! That can be incredibly powerful.

**Dave Jones:** But unfortunately, because it's a big serial shifted interface, it's not going to be very fast. It's not real-time, all that sort of stuff. And as I said, it's not incredibly fast because it is a serial shifted system. And if you've got

**Dave Jones:** an FPGA for example, that's got eight a huge one that's got 800 IO pins, poof, you've got to shift through all that data and all the other control data that's hooked into and reading stuff like that. Can be a massively long

**Dave Jones:** serial data stream. But not only that, not only can you talk to one chip, we can hook our programmer, ignoring all this, we haven't talked about that yet, we will in a second. You have your programmer, your JTAG programmer hooked

**Dave Jones:** up directly to the JTAG pins. Okay, you can just talk to this one chip. But the beautiful thing about the serial uh daisy-chaining nature of the JTAG system is that you can have additional chips on your board, essentially an unlimited

**Dave Jones:** number, essentially, and then daisy-chain those together. So, the TDI, so your So, instead of plugging directly into this chip, here's our programmer plugged onto our head header on our board over here. We've got our data coming in, okay? It

**Dave Jones:** goes through this chip, boop boop boop, all the stuff it needs to, and then it shifts the data out, and then the data goes into the TDI pin of chip number two here, and then it goes through its big

**Dave Jones:** JTAG daisy-chain in there, comes out the TDIO pin, and then you can daisy-chain that to a third chip, and so on, and so on. You can have as many chips as you as you like, subject to electrical design

**Dave Jones:** rules, and you know, bus like you know, loading and all that sort of stuff. You can have as many devices in series as you like, and the data finally spits back out. So, you can have 100 chips on

**Dave Jones:** your board that all have JTAG interfaces in them. You can hook them all onto one JTAG header. Lousy four pins, you can test every single pin on every chip on your entire board, both at the assembly stage and when it's actually running,

**Dave Jones:** and you can read data back. Fantastic. So, that's all known as the JTAG chain, and it's very common to have more than one device hooked on here. And I won't go into uh well, I have to go into

**Dave Jones:** another video how FPGAs are also like they will have their external flash memory on the JTAG chain as well. We talked about that, and how that's all tied in, and then how it can actually load data and you program your external

**Dave Jones:** flash memory for your FPGA via this huge JTAG chain. And each individual device will have its own internal ID, and that can be all read out and there's a whole uh well, there's a standard protocol behind all this which then allows you to

**Dave Jones:** talk and respond to any one of these chips, but you have to understand that you can't just go oh, I want to talk to this chip only. You have to get the data if you've physically daisy chain them

**Dave Jones:** all like this or you know, if you've got 100 chips on your board, you've daisy chain them all. Well, you had to get the data just out of this one, you have to wait until you've got the data out of

**Dave Jones:** all the others. Well, it depends where it is in the line where it physically is in the daisy chain part of the system. Now, a lot of boards in in case of development and also production as well, you'll actually

**Dave Jones:** build in jumpers on the board here so that you can actually you know, a little two-pin jumper header so that you can actually you know, jump out that and bypass that particular chip from the JTAG interface. That's useful for

**Dave Jones:** speeding up debugging and stuff like that. Let's say you wanted really fast debugging or as fast as possible on the pins of this chip. Well, you could short out all the other chips in your JTAG daisy chain to do just that. And any

**Dave Jones:** JTAG chip that meets the JTAG standard will have an associated file that you can just download from the manufacturer's website and it defines the interface for that particular chip and that's known as a boundary scan description language or BSDL file that

**Dave Jones:** you can get from the manufacturer and that's a variant of VHDL. So, it's like a VHDL sort of language that describes what each individual pin does and the description ID for each chip and all that sort of stuff. So, your JTAG system

**Dave Jones:** software that you're using on your PC or your test system will be able to read that BSDL file and know exactly how to talk to and operate and have the all the IO mapping and the pin mapping and all

**Dave Jones:** the internal stuff for interfacing with a particular chip on that JTAG daisy chain. And yes, I know what some people are thinking. If there's a JTAG header, as you've seen in many of my teardowns, inside a product, not only can you hook

**Dave Jones:** up to it and read the data back out, potentially read the firmware and everything else, but you can also access the individual pins via the boundary scan here and you can use that to hack products. Hmm. Now, I did actually leave out one line

**Dave Jones:** here because it's actually optional and it's not always used, the TRST pin, which is once again parallel connected to all the devices in the JTAG chain here and that can just reset the entire chip, all of your chips all at

**Dave Jones:** once, but you don't have to do that cuz you can actually reset them through uh commands through the serial lines anyway, or the chip itself may actually have individual like a different sort of reset circuitry built in. Now, when you

**Dave Jones:** got a JTAG daisy chain like this, the maximum system operation of the JTAG chain is going to be determined by the slowest device in the chain. So, if one device is only capable of working at 10 MHz, for example, then well, that's what

**Dave Jones:** you have to run your entire daisy chain at, but um you know, they can work from anywhere from say 10 up to 100 MHz or so. They can be actually very quick, but still shifting all that data through,

**Dave Jones:** it's not going to be able to read pins in real time, that's for sure. And thankfully, we have something in the mailbag from XJTAG, purveyors of fine JTAG pornography, uh that should be able to help us have a look at the hardware

**Dave Jones:** side of things and the software. So, let's crack it open and see what we got. Haha, look at this. Beautiful. With compliments. Aha, we have ourselves a JTAG demo board. Looks very impressive. We have ourselves an XJTAG XJLink 2 JTAG interface and some

**Dave Jones:** software. Now, we'll just take a quick look at a practical example of looking at a a basic hardware JTAG interface using this XJTAG 2 programmer that we got here. Now, this is not a hobbyist level tool. This is a real professional high-end

**Dave Jones:** JTAG development. Not only programmer, but the software and and the whole system behind it. And it comes with this very nice demo board, which should allow us to do which should allow us to like open pins and put various shorts and

**Dave Jones:** fault conditions on that as well. Now, it's got an arm 9 processor on here. That's a TI Stellaris LM 3S300. It's got a Xilinx CPLD on here as well. That's got building flash, so that doesn't have like an external

**Dave Jones:** configuration prom or anything like that. And that CPLD is hooked into some flash memory and some SRAM up here. And then we can like introduce opens on the data bus and do things like that. So, we're going to have two programmable

**Dave Jones:** devices in our JTAG chain for this thing. Now, this programmer is actually capable of doing a lot more. It's capable of reconfiguring all its pins on the output to match, you know, Xilinx or Altera or anyone or any other manufacturer or even your

**Dave Jones:** custom own custom interface. It can supply power through to this board as well. All configurable on each individual pin. It's hooked up to an I2C bus on here as well, which is then hooked into a an I squared C E prom

**Dave Jones:** E squared prom. It's hooked up to an analog to digital converter on the I squared C bus and we've got some analog inputs and stuff like that. Don't have no time to muck around with that, but we definitely want to look at these two

**Dave Jones:** devices on the JTAG chain. That should be easy. Now, what I'm running at the moment is this XJTAG program that comes with it called the pin map chain debugger and this is sort of like a low-level interface where we can just

**Dave Jones:** get sort of the raw data and we can configure, as I said, the you can see that the header connector on this thing is completely reconfigurable. Now, every JTAG programmer and their software is going to be different. This is not going

**Dave Jones:** to be a review of the XJTAG stuff. This is just how this one happens to work and here we go. We can actually reconfigure all of these pins here. We can choose different types. We can choose the XJTAG

**Dave Jones:** interface multi ice, the byte altera byte blaster compatible interface, so we can choose that if we want. Uh we can use the the Xilinx interface or a custom interface, but anyway, what we want is the XJTAG. You can see the pins here.

**Dave Jones:** We've got TDI, TMS, TCK, TDO. You'll notice that there is no T reset. It's not actually used in this configuration and we want to actually power the board from this device, so we can actually choose power on there. Do I want to

**Dave Jones:** continue? Yes, I know what I'm doing. I won't blow up my board and it applies power to pin number one and you can see that these pins change state. That's actually a live view there. And anyway, what we can do is then we can

**Dave Jones:** go down here and we can check Well, let's start ID code. So, let's try that. There we go. Bang, we're starting to read the ID codes. It's found two different IDs, chip IDs here and you would have to know

**Dave Jones:** uh what these IDs uh you would have to know that okay, that chip, but there's definitely two chips on there, so we can stop scanning that. There we go. So, it's found two devices on that JTAG chain. Now, what we can do is actually a

**Dave Jones:** neat function of this is we can get the maximum T-clock. So, what it's going to do, we can hit that and then it's just going to cycle through the frequencies until it basically gets an error to find the maximum frequency in this signal.

**Dave Jones:** And bingo, there it is, max frequency 26 MHz. So, this XJTAG JTAG two devices capable of 166 MHz. So, if your system was capable of that, this is a neat little tool to find that. Anyway, just thought I'd show you that. We can clear

**Dave Jones:** and now let's check the chain. Here we go, starting chain check and there's two devices found. Bingo, there they are. It doesn't know the actual codes. It doesn't know how to translate those codes yet through to, you know, to map

**Dave Jones:** it to a particular device to tell you if it's an FPGA, but there you go. It tells you the length of the various chains, but if we go over to device configuration over here, bingo, it has found them. Look, the

**Dave Jones:** Xilinx one, there we go. It's matched it the Xilinx and an arm. There we go and the Xilinx is an XC9536. It's automatically found that and it's automatically found the arm processor as an LM3S300. Awesome. And what we can do now is we

**Dave Jones:** can go up into tools and then view JTAG data and we can check that chain again. And woah. Oh, look at what we got. All this goodness, there's our raw data from device number one and device number two from both of these

**Dave Jones:** devices on the JTAG chain. Brilliant. And of course, you've got to know what each of the individual bits do and things like that, but this just allows you to suck the raw data out of this thing just as a first pass. Now, I'm

**Dave Jones:** running what's called the XJ analyzer program and this allows us to do lots of really funky analysis and I've loaded in the example demo board. It's already pre-configured with our device types and it shows both of the devices down here.

**Dave Jones:** Now, we've actually stopped this but we can actually go in there and run it and here we go. Bingo, we get and now a live map of what our individual pins are doing here. The yellow ones look that

**Dave Jones:** pin on that particular CPOD is oscillating for example. These ones are low, high. Fantastic and we can go in there and modify individual pins. So we now got it running and look, if we right click here we can set individual pins

**Dave Jones:** low low high. We can set them to toggle low or fast the pin properties, the device properties. Ah, fantastic. There it is. Read value, outputting net all sorts of stuff and you can you know configure all this till the cows come

**Dave Jones:** home for your specific of course you'd set it all up for your specific board and your application for what you want to do. We can go into the device properties there. Max JTAG frequency of this device for example 10 MHz. I'm

**Dave Jones:** currently running it at 20 so it looks like we're overclocking it a bit like that. I mean we can go in there and then we can uh set the chain frequency here and I've got it running at 20 but we can you know

**Dave Jones:** drop that back down. It's adjustable from 10 kHz to 166 in 10 kHz steps. For example, we can drop that down. Not a problem. So there's all the instruction length, the boundary length, how many bytes. I think that figure was exactly

**Dave Jones:** what we saw before in the previous program. 46 pins on here and that's the ID code that we got out of it that matched it. Fantastic. Now the thing you have to remember here is that we're using the JTAG interface to read all the

**Dave Jones:** data of all these pins out live while that microcontroller is doing running its regular firmware. It's They can two completely independent systems and we can get in there while that microcontroller firmware in this LM3S, for example, is running. We can go

**Dave Jones:** in there and individually override pins and disable pins and set them and toggle them and do whatever and the firmware doesn't know that we're actually doing that. Completely independent. Now, look what happens if I press this button here. Here we go. Look at that. There's

**Dave Jones:** a pin on this CPOD. The button's obviously connected to C3 there and if I press that, there we go. It goes high, low, and if I continue to press it, it tells us that it goes yellow to tell us

**Dave Jones:** that it's oscillating. And watch this. We can now go in here to this pin, for example, which is currently set low and we can which is it's telling us because it's it's blue it's got a cross in it

**Dave Jones:** that we're actually setting it and we can make that toggle like that and bingo. Look what we've got over here. Pin 48 up here of our ARM microcontroller is obviously uh connected through to that or they've got some sort of, you know, a linkage

**Dave Jones:** somehow either through the firmware is doing that or whatever because if this pin over here was going to an input to this microcontroller and then it was outputting it was just, you know, inverting and then outputting that signal or something like that, then we

**Dave Jones:** can actually see it doing that. So, we can just set that high and look at that. Too easy. So, that one's actually low. So, they're not actually physically connected. They're inverted. And then extremely briefly, because well, I haven't played with it much, is the

**Dave Jones:** full-on developer software with this thing and we can have our boards, for example, I've loaded it in and we can have uh got the schematic of the board, all the parts, we can categorize our devices on it, we can set up all our pins, all

**Dave Jones:** our logic files, our test circuits, and all sorts of stuff designed for test, run, and deploy, and we can configure this thing to basically test any JTAG uh enabled system imaginable. So, you can really see the power of this uh JTAG

**Dave Jones:** system. I mean, imagine if we opened up a product like an oscilloscope or something and it had a JTAG header in there. We could hook up our JTAG programmer to it. We can see what all the pins are doing, not quite in real

**Dave Jones:** time, but you know, it does allow you to uh see things happening. We can set and modify things all independent of the firmware. It's very powerful. And that doesn't include all the, you know, that's uh nothing to be said for the

**Dave Jones:** production testing side of things. The uh testing assembled boards, which is basically what all this uh stuff's about, programming devices, and pretty much it's not just about the programmer hardware. That's, you know, almost irrelevant uh really, the JTAG uh

**Dave Jones:** hardware. It's all about the software. And yes, this is a big uh professional-level software package, but there are many, many ones on the market built into uh many different uh tools and things like that, or they have independent tools like this one. So,

**Dave Jones:** that's JTAG, and it is uh as I have shown, it's an incredibly powerful system that you probably didn't know is lurking behind any chip that has these JTAG uh that has a JTAG interface you may have used for

**Dave Jones:** programming or debugging. So, there you go. I hope I you found that uh video useful and you've learned a bit about JTAG, and I'm sure um I'll be doing more on it in the future. So, if you like

**Dave Jones:** Fundamentals Friday, please give it a big thumbs up. You can't see my thumbs, but I am sticking them up here. And if you want to discuss it, jump on over to the EEVblog forum. Catch you next time.
