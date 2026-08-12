---
video_id: TlWlLeC5BUs
title: EEVblog #499 - What is JTAG and Boundary Scan?
url: https://www.youtube.com/watch?v=TlWlLeC5BUs
source: youtube-asr
timestamps: {"0": 1, "1": 23, "2": 42, "3": 50, "4": 59, "5": 78, "6": 87, "7": 108, "8": 125, "9": 135, "10": 151, "11": 164, "12": 178, "13": 187, "14": 200, "15": 217, "16": 234, "17": 255, "18": 275, "19": 303, "20": 320, "21": 340, "22": 352, "23": 364, "24": 382, "25": 400, "26": 412, "27": 423, "28": 436, "29": 445, "30": 461, "31": 471, "32": 481, "33": 491, "34": 507, "35": 517, "36": 532, "37": 549, "38": 559, "39": 577, "40": 587, "41": 601, "42": 616, "43": 640, "44": 650, "45": 668, "46": 679, "47": 703, "48": 712, "49": 734, "50": 741, "51": 754, "52": 771, "53": 788, "54": 801, "55": 820, "56": 829, "57": 842, "58": 862, "59": 876, "60": 900, "61": 926, "62": 954, "63": 978, "64": 987, "65": 997, "66": 1011, "67": 1032, "68": 1061, "69": 1075, "70": 1092, "71": 1110, "72": 1118, "73": 1140, "74": 1155, "75": 1165, "76": 1185, "77": 1196, "78": 1207, "79": 1216, "80": 1229, "81": 1237, "82": 1250, "83": 1265, "84": 1274, "85": 1285, "86": 1297, "87": 1307, "88": 1320, "89": 1330, "90": 1345, "91": 1356, "92": 1375, "93": 1393, "94": 1406, "95": 1416, "96": 1429, "97": 1448, "98": 1459, "99": 1467, "100": 1480, "101": 1488, "102": 1502, "103": 1522, "104": 1534, "105": 1558, "106": 1585, "107": 1595, "108": 1620, "109": 1635, "110": 1642, "111": 1652, "112": 1670, "113": 1687, "114": 1703, "115": 1713, "116": 1725}
---

**Dave Jones:** Hi, welcome to Fundamentals Friday. Today we're going to take a look at the JTAG interface. JTAG stands for the Joint Test Action Group, and I'm sure you probably heard of JTAG and you may have even used it in terms of programming a microcontroller or an FPGA or you and or using it as a debugging interface or something like that, for example.

**Dave Jones:** Well, that's not the only thing it can do. In fact, it originally wasn't designed for that. Uh JTAG came about in the late '80s when manufacturers started realizing that oh, you know, we're having a real lot of trouble testing assembled PCBs.

**Dave Jones:** Uh packages were getting more dense, so we're moving towards packages like BGA where the balls are on the bottom of the device. You can't use a traditional bed of nails tester to come down.

**Dave Jones:** And if you did, if you got a you know, a 500-pin chip or something, woah, that's a lot of test pins to come down and test your assembled PCB.

**Dave Jones:** It was getting very difficult. So, a bunch of manufacturers got together and said, "Well, what can we do about it? Can we actually embed a come up with a standard that allows us to embed some hardware into the chips so that they can we can use that to test themselves.

**Dave Jones:** So, we can access all of these pins under the PCB without having to use a traditional bed of nails test system. And that's exactly what they came up with.

**Dave Jones:** And it was ratified by the uh IEEE as a standard in around about 1990. And that's where the name comes from, the Joint Test Action Group. Test was originally designed as a way to actually get in there and test individual pins on uh a chip which has JTAG built into it on the assembled PCB.

**Dave Jones:** In cases where you couldn't physically get access like big BGA chips, for example, or there were just too many pins on a huge system that you just, you know, you'd have need thousands of pins to actually test it on your bed of nails or your flying probe tester.

**Dave Jones:** It'd take too long to move all the probes around to test it all. So, that's what it was originally designed for and hence the name boundary scan. JTAG is also known as boundary scan testing.

**Dave Jones:** And as the name implies, we have to have a look at a block diagram here of a typical chip that includes JTAG or this boundary scan testing. Now, this chip could be an FPGA, for example.

**Dave Jones:** It could be a modern microcontroller that has JTAG built in. It could be a special purpose custom chip that implements JTAG as well or practically anything on the market.

**Dave Jones:** A dead giveaway for a chip that has JTAG built in the pin names here. If they've got TDO, TDI, TCK, and TMS, you can bet your bottom dollar it's got JTAG built in.

**Dave Jones:** Now, not all of the chips have all of the same functionality because they don't need it. But, let's take for example a micro a modern microcontroller with a JTAG interface.

**Dave Jones:** Not only will it contain your traditional boundary scan around here, which we'll talk about, but it is also used as the interface where you can program your flash memory built in.

**Dave Jones:** So, it's going to talk to the flash controller built in. And yes, that microcontroller may also have another block in here, which then goes out to your traditional ICSP, your in-circuit serial programming method.

**Dave Jones:** And you may have two different methods actually program your flash microcontroller, for example. But, it's also going to go into debug controllers these days. We've talked about ice systems before, in-circuit emulators, which pretty much have gone the way of the dodo and have been replaced by the JTAG interface.

**Dave Jones:** So, that will also connect into the debug controller and that allows you to monitor and debug your code inside your microcontroller in real time. So, but that originally that wasn't really thought of when the JTAG, the Joint Test Action Group, originally started this.

**Dave Jones:** What they started it for is this boundary scan stuff around here. Now, this is the interesting thing about JTAG, which a lot of people aren't familiar with. They're used to using it to program and debug their microcontroller, for example, but there's much more powerful functionality behind it and most chips which have JTAG built in will also have this boundary scan capability around here.

**Dave Jones:** Now, what is boundary scan? Well, as the name implies, the it has some circuitry attached to each pin. You could call it like a JTAG cell, for example. I've drawn it as one big block here for that sort of, you know, joins all the pins, but in reality it's like an individual JTAG cell, a little bunch of logic in there which connects in between the usual chip IO,

**Dave Jones:** which we have looked at in the last video, for example, with FPGAs. We looked at all the complex IO stuff they had. Well, not only did they have that, I didn't show something last week and that's that bound additional boundary scan circuitry in there, which is tucked away between the chip IO and the pin.

**Dave Jones:** All right, you know, this is a just a a crude graphical representation of of how it works. How they actually implement it in there is up to the individual manufacturer, but it's easy to think of it as being between your regular IO drivers on your microcontroller or your FPGA, for example, and the pin.

**Dave Jones:** And during normal use, you program and debug your microcontroller, you I even know this JTAG, this boundary scan circuitry is actually in there. It just defaults to off when you power on the chip and it does nothing.

**Dave Jones:** It just passes the signal straight through from your regular chip IO circuitry here. So what they do with these little JTAG cells is they actually What I've kind of shown it here.

**Dave Jones:** I've shown an arrow going out like this and going into here, but in reality, as I said, they're like individual cells and they go from one to the other and there's a serial of one one line serial IO which goes in to each cell and then comes out and they're cascaded like that in a serial fashion until the data comes out.

**Dave Jones:** So you feed data into the chip and you can and it just cascades and ripples all the way through like this. Ripples a bad term because it's actually a synchronous clock in here which does everything, so don't confuse that, but and the data flows through in a serial fashion like that and pops out.

**Dave Jones:** And what does that allow you to do? Well, it depends on the functionality built into the boundary scan, but most of them are going to allow you full direct control over that IO pin.

**Dave Jones:** Not only are you able to read the value back directly on the pin of the chip. And this is why I've shown it actually sort of after the chip IO here.

**Dave Jones:** It's in between the chip IO driver and the pin because the idea of boundary scan is you physically read the actual electrical value on that pin, not after any of the chip IO or anything like that.

**Dave Jones:** It actually allows you to read exactly what's on the pin itself. So you can read back all that data and shift it out and do whatever you want with it.

**Dave Jones:** But not only can you read it, you can that they can have a driver in there as well that allows you to set a value on that pin. And being able to set and read values, that gives you an incredibly powerful tool to do in-system debugging.

**Dave Jones:** For example, we if this uh was a a microcontroller, for example, and we hadn't finished doing our firmware yet, we hadn't programmed the chip, it was empty, it does nothing, it doesn't matter.

**Dave Jones:** If we've got a populated PCB, what we can do is hook it up to our uh JTAG programmer, and we can individually talk to and drive and read all of the pins on the board.

**Dave Jones:** So, for example, let's say we had an external memory hooked up to this thing uh onto all these IO pins here. How do you test that memory to make sure it's okay?

**Dave Jones:** Well, we can write individual value values to the address uh and and data buses, and then we can read it all back. And we can actually exercise and test an external memory, for example, through our JTAG interface.

**Dave Jones:** But not only that, the assembled PCB, it allows you to test for your more traditional things like uh shorts and opens and things like that. So, and that's stuck bits.

**Dave Jones:** Let's say this pin in here is shorted to ground, like that. Well, what you try and do is you try and write a one to it and then read it back, and if you can't do that, oops, then you know it's shorted.

**Dave Jones:** If it always reads back a zero, then you know it's always shorted to ground. And also and then, if you had, say, two pins shorted like that on your PC on your assembled PCB, you had a little solder bridge or something like that, well, based on your testing algorithm, you can drive one and read the other, etc.

**Dave Jones:** And you can actually do all that in various combinations, and you can check for shorts between this pin over here and this pin, depending on your layout and your board, and all sorts of stuff.

**Dave Jones:** Incredibly powerful. And that is one of the main uses of JTAG, which a lot of people aren't familiar with. They just think it's programming and debugging, but nope, there's lots of powerful stuff hidden inside your chip you're probably already using.

**Dave Jones:** We've already briefly looked at the four main pins of the JTAG controller and that's all it takes. Four pins is always going to be four pins. There's a TDO, which is the data coming out of the chip.

**Dave Jones:** Don't confuse them in terms of uh your traditional TX and RX when you get them mixed up. TDO on a chip when it's labeled TDO is always the data coming out and TDI is always the data going the serial data going into the chip.

**Dave Jones:** And then you've got your uh T clock line, which is your synchronous clock, which actually controls all the data shifting and everything else in there. And you've got TMS, which is a control line, which does stuff as well uh based on that T clock and everything else.

**Dave Jones:** And those four pins allow you to feed data into the chip and read data back out. And one other powerful feature as well, after you've programmed your microcontroller here and you're running your firmware, you can also at the same time access this boundary scan stuff and read live data changing on your pins here.

**Dave Jones:** Woah! That can be incredibly powerful. But unfortunately, because it's a big serial shifted interface, it's not going to be very fast. It's not real-time, all that sort of stuff.

**Dave Jones:** And as I said, it's not incredibly fast because it is a serial shifted system. And if you've got an FPGA for example, that's got eight a huge one that's got 800 IO pins, poof, you've got to shift through all that data and all the other control data that's hooked into and reading stuff like that.

**Dave Jones:** Can be a massively long serial data stream. But not only that, not only can you talk to one chip, we can hook our programmer, ignoring all this, we haven't talked about that yet, we will in a second.

**Dave Jones:** You have your programmer, your JTAG programmer hooked up directly to the JTAG pins. Okay, you can just talk to this one chip. But the beautiful thing about the serial uh daisy-chaining nature of the JTAG system is that you can have additional chips on your board, essentially an unlimited number, essentially, and then daisy-chain those together.

**Dave Jones:** So, the TDI, so your So, instead of plugging directly into this chip, here's our programmer plugged onto our head header on our board over here. We've got our data coming in, okay?

**Dave Jones:** It goes through this chip, boop boop boop, all the stuff it needs to, and then it shifts the data out, and then the data goes into the TDI pin of chip number two here, and then it goes through its big JTAG daisy-chain in there, comes out the TDIO pin, and then you can daisy-chain that to a third chip, and so on, and so on.

**Dave Jones:** You can have as many chips as you as you like, subject to electrical design rules, and you know, bus like you know, loading and all that sort of stuff.

**Dave Jones:** You can have as many devices in series as you like, and the data finally spits back out. So, you can have 100 chips on your board that all have JTAG interfaces in them.

**Dave Jones:** You can hook them all onto one JTAG header. Lousy four pins, you can test every single pin on every chip on your entire board, both at the assembly stage and when it's actually running, and you can read data back.

**Dave Jones:** Fantastic. So, that's all known as the JTAG chain, and it's very common to have more than one device hooked on here. And I won't go into uh well, I have to go into another video how FPGAs are also like they will have their external flash memory on the JTAG chain as well.

**Dave Jones:** We talked about that, and how that's all tied in, and then how it can actually load data and you program your external flash memory for your FPGA via this huge JTAG chain.

**Dave Jones:** And each individual device will have its own internal ID, and that can be all read out and there's a whole uh well, there's a standard protocol behind all this which then allows you to talk and respond to any one of these chips, but you have to understand that you can't just go oh, I want to talk to this chip only.

**Dave Jones:** You have to get the data if you've physically daisy chain them all like this or you know, if you've got 100 chips on your board, you've daisy chain them all.

**Dave Jones:** Well, you had to get the data just out of this one, you have to wait until you've got the data out of all the others. Well, it depends where it is in the line where it physically is in the daisy chain part of the system.

**Dave Jones:** Now, a lot of boards in in case of development and also production as well, you'll actually build in jumpers on the board here so that you can actually you know, a little two-pin jumper header so that you can actually you know, jump out that and bypass that particular chip from the JTAG interface.

**Dave Jones:** That's useful for speeding up debugging and stuff like that. Let's say you wanted really fast debugging or as fast as possible on the pins of this chip. Well, you could short out all the other chips in your JTAG daisy chain to do just that.

**Dave Jones:** And any JTAG chip that meets the JTAG standard will have an associated file that you can just download from the manufacturer's website and it defines the interface for that particular chip and that's known as a boundary scan description language or BSDL file that you can get from the manufacturer and that's a variant of VHDL.

**Dave Jones:** So, it's like a VHDL sort of language that describes what each individual pin does and the description ID for each chip and all that sort of stuff. So, your JTAG system software that you're using on your PC or your test system will be able to read that BSDL file and know exactly how to talk to and operate and have the all the IO mapping and the pin mapping and all

**Dave Jones:** the internal stuff for interfacing with a particular chip on that JTAG daisy chain. And yes, I know what some people are thinking. If there's a JTAG header, as you've seen in many of my teardowns, inside a product, not only can you hook up to it and read the data back out, potentially read the firmware and everything else, but you can also access the individual pins via the boundary

**Dave Jones:** scan here and you can use that to hack products. Hmm. Now, I did actually leave out one line here because it's actually optional and it's not always used, the TRST pin, which is once again parallel connected to all the devices in the JTAG chain here and that can just reset the entire chip, all of your chips all at once, but you don't have to do that cuz

**Dave Jones:** you can actually reset them through uh commands through the serial lines anyway, or the chip itself may actually have individual like a different sort of reset circuitry built in.

**Dave Jones:** Now, when you got a JTAG daisy chain like this, the maximum system operation of the JTAG chain is going to be determined by the slowest device in the chain.

**Dave Jones:** So, if one device is only capable of working at 10 MHz, for example, then well, that's what you have to run your entire daisy chain at, but um you know, they can work from anywhere from say 10 up to 100 MHz or so.

**Dave Jones:** They can be actually very quick, but still shifting all that data through, it's not going to be able to read pins in real time, that's for sure. And thankfully, we have something in the mailbag from XJTAG, purveyors of fine JTAG pornography, uh that should be able to help us have a look at the hardware side of things and the software.

**Dave Jones:** So, let's crack it open and see what we got. Haha, look at this. Beautiful. With compliments. Aha, we have ourselves a JTAG demo board. Looks very impressive. We have ourselves an XJTAG XJLink 2 JTAG interface and some software.

**Dave Jones:** Now, we'll just take a quick look at a practical example of looking at a a basic hardware JTAG interface using this XJTAG 2 programmer that we got here. Now, this is not a hobbyist level tool.

**Dave Jones:** This is a real professional high-end JTAG development. Not only programmer, but the software and and the whole system behind it. And it comes with this very nice demo board, which should allow us to do which should allow us to like open pins and put various shorts and fault conditions on that as well.

**Dave Jones:** Now, it's got an arm 9 processor on here. That's a TI Stellaris LM 3S300. It's got a Xilinx CPLD on here as well. That's got building flash, so that doesn't have like an external configuration prom or anything like that.

**Dave Jones:** And that CPLD is hooked into some flash memory and some SRAM up here. And then we can like introduce opens on the data bus and do things like that.

**Dave Jones:** So, we're going to have two programmable devices in our JTAG chain for this thing. Now, this programmer is actually capable of doing a lot more. It's capable of reconfiguring all its pins on the output to match, you know, Xilinx or Altera or anyone or any other manufacturer or even your custom own custom interface.

**Dave Jones:** It can supply power through to this board as well. All configurable on each individual pin. It's hooked up to an I2C bus on here as well, which is then hooked into a an I squared C E prom E squared prom.

**Dave Jones:** It's hooked up to an analog to digital converter on the I squared C bus and we've got some analog inputs and stuff like that. Don't have no time to muck around with that, but we definitely want to look at these two devices on the JTAG chain.

**Dave Jones:** That should be easy. Now, what I'm running at the moment is this XJTAG program that comes with it called the pin map chain debugger and this is sort of like a low-level interface where we can just get sort of the raw data and we can configure, as I said, the you can see that the header connector on this thing is completely reconfigurable.

**Dave Jones:** Now, every JTAG programmer and their software is going to be different. This is not going to be a review of the XJTAG stuff. This is just how this one happens to work and here we go.

**Dave Jones:** We can actually reconfigure all of these pins here. We can choose different types. We can choose the XJTAG interface multi ice, the byte altera byte blaster compatible interface, so we can choose that if we want.

**Dave Jones:** Uh we can use the the Xilinx interface or a custom interface, but anyway, what we want is the XJTAG. You can see the pins here. We've got TDI, TMS, TCK, TDO.

**Dave Jones:** You'll notice that there is no T reset. It's not actually used in this configuration and we want to actually power the board from this device, so we can actually choose power on there.

**Dave Jones:** Do I want to continue? Yes, I know what I'm doing. I won't blow up my board and it applies power to pin number one and you can see that these pins change state.

**Dave Jones:** That's actually a live view there. And anyway, what we can do is then we can go down here and we can check Well, let's start ID code. So, let's try that.

**Dave Jones:** There we go. Bang, we're starting to read the ID codes. It's found two different IDs, chip IDs here and you would have to know uh what these IDs uh you would have to know that okay, that chip, but there's definitely two chips on there, so we can stop scanning that.

**Dave Jones:** There we go. So, it's found two devices on that JTAG chain. Now, what we can do is actually a neat function of this is we can get the maximum T-clock.

**Dave Jones:** So, what it's going to do, we can hit that and then it's just going to cycle through the frequencies until it basically gets an error to find the maximum frequency in this signal.

**Dave Jones:** And bingo, there it is, max frequency 26 MHz. So, this XJTAG JTAG two devices capable of 166 MHz. So, if your system was capable of that, this is a neat little tool to find that.

**Dave Jones:** Anyway, just thought I'd show you that. We can clear and now let's check the chain. Here we go, starting chain check and there's two devices found. Bingo, there they are.

**Dave Jones:** It doesn't know the actual codes. It doesn't know how to translate those codes yet through to, you know, to map it to a particular device to tell you if it's an FPGA, but there you go.

**Dave Jones:** It tells you the length of the various chains, but if we go over to device configuration over here, bingo, it has found them. Look, the Xilinx one, there we go.

**Dave Jones:** It's matched it the Xilinx and an arm. There we go and the Xilinx is an XC9536. It's automatically found that and it's automatically found the arm processor as an LM3S300.

**Dave Jones:** Awesome. And what we can do now is we can go up into tools and then view JTAG data and we can check that chain again. And woah. Oh, look at what we got.

**Dave Jones:** All this goodness, there's our raw data from device number one and device number two from both of these devices on the JTAG chain. Brilliant. And of course, you've got to know what each of the individual bits do and things like that, but this just allows you to suck the raw data out of this thing just as a first pass.

**Dave Jones:** Now, I'm running what's called the XJ analyzer program and this allows us to do lots of really funky analysis and I've loaded in the example demo board. It's already pre-configured with our device types and it shows both of the devices down here.

**Dave Jones:** Now, we've actually stopped this but we can actually go in there and run it and here we go. Bingo, we get and now a live map of what our individual pins are doing here.

**Dave Jones:** The yellow ones look that pin on that particular CPOD is oscillating for example. These ones are low, high. Fantastic and we can go in there and modify individual pins.

**Dave Jones:** So we now got it running and look, if we right click here we can set individual pins low low high. We can set them to toggle low or fast the pin properties, the device properties.

**Dave Jones:** Ah, fantastic. There it is. Read value, outputting net all sorts of stuff and you can you know configure all this till the cows come home for your specific of course you'd set it all up for your specific board and your application for what you want to do.

**Dave Jones:** We can go into the device properties there. Max JTAG frequency of this device for example 10 MHz. I'm currently running it at 20 so it looks like we're overclocking it a bit like that.

**Dave Jones:** I mean we can go in there and then we can uh set the chain frequency here and I've got it running at 20 but we can you know drop that back down.

**Dave Jones:** It's adjustable from 10 kHz to 166 in 10 kHz steps. For example, we can drop that down. Not a problem. So there's all the instruction length, the boundary length, how many bytes.

**Dave Jones:** I think that figure was exactly what we saw before in the previous program. 46 pins on here and that's the ID code that we got out of it that matched it.

**Dave Jones:** Fantastic. Now the thing you have to remember here is that we're using the JTAG interface to read all the data of all these pins out live while that microcontroller is doing running its regular firmware.

**Dave Jones:** It's They can two completely independent systems and we can get in there while that microcontroller firmware in this LM3S, for example, is running. We can go in there and individually override pins and disable pins and set them and toggle them and do whatever and the firmware doesn't know that we're actually doing that.

**Dave Jones:** Completely independent. Now, look what happens if I press this button here. Here we go. Look at that. There's a pin on this CPOD. The button's obviously connected to C3 there and if I press that, there we go.

**Dave Jones:** It goes high, low, and if I continue to press it, it tells us that it goes yellow to tell us that it's oscillating. And watch this. We can now go in here to this pin, for example, which is currently set low and we can which is it's telling us because it's it's blue it's got a cross in it that we're actually setting it and we can make that toggle

**Dave Jones:** like that and bingo. Look what we've got over here. Pin 48 up here of our ARM microcontroller is obviously uh connected through to that or they've got some sort of, you know, a linkage somehow either through the firmware is doing that or whatever because if this pin over here was going to an input to this microcontroller and then it was outputting it was just, you know, inverting and then outputting that

**Dave Jones:** signal or something like that, then we can actually see it doing that. So, we can just set that high and look at that. Too easy. So, that one's actually low.

**Dave Jones:** So, they're not actually physically connected. They're inverted. And then extremely briefly, because well, I haven't played with it much, is the full-on developer software with this thing and we can have our boards, for example, I've loaded it in and we can have uh got the schematic of the board, all the parts, we can categorize our devices on it, we can set up all our pins, all our logic files, our test circuits, and

**Dave Jones:** all sorts of stuff designed for test, run, and deploy, and we can configure this thing to basically test any JTAG uh enabled system imaginable. So, you can really see the power of this uh JTAG system.

**Dave Jones:** I mean, imagine if we opened up a product like an oscilloscope or something and it had a JTAG header in there. We could hook up our JTAG programmer to it.

**Dave Jones:** We can see what all the pins are doing, not quite in real time, but you know, it does allow you to uh see things happening. We can set and modify things all independent of the firmware.

**Dave Jones:** It's very powerful. And that doesn't include all the, you know, that's uh nothing to be said for the production testing side of things. The uh testing assembled boards, which is basically what all this uh stuff's about, programming devices, and pretty much it's not just about the programmer hardware.

**Dave Jones:** That's, you know, almost irrelevant uh really, the JTAG uh hardware. It's all about the software. And yes, this is a big uh professional-level software package, but there are many, many ones on the market built into uh many different uh tools and things like that, or they have independent tools like this one.

**Dave Jones:** So, that's JTAG, and it is uh as I have shown, it's an incredibly powerful system that you probably didn't know is lurking behind any chip that has these JTAG uh that has a JTAG interface you may have used for programming or debugging.

**Dave Jones:** So, there you go. I hope I you found that uh video useful and you've learned a bit about JTAG, and I'm sure um I'll be doing more on it in the future.

**Dave Jones:** So, if you like Fundamentals Friday, please give it a big thumbs up. You can't see my thumbs, but I am sticking them up here. And if you want to discuss it, jump on over to the EEVblog forum.

**Dave Jones:** Catch you next time.
