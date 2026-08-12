---
video_id: YC6JCVHk80c
title: EEVblog #977 - Keysight 1000X Hacking - Part 1
url: https://www.youtube.com/watch?v=YC6JCVHk80c
source: youtube-asr
timestamps: {"0": 0, "1": 11, "2": 44, "3": 65, "4": 78, "5": 88, "6": 101, "7": 112, "8": 130, "9": 143, "10": 158, "11": 180, "12": 199, "13": 215, "14": 226, "15": 243, "16": 259, "17": 276, "18": 288, "19": 298, "20": 314, "21": 331, "22": 345, "23": 356, "24": 369, "25": 380, "26": 393, "27": 403, "28": 415, "29": 430, "30": 438, "31": 450, "32": 473, "33": 494, "34": 506, "35": 523, "36": 532, "37": 541, "38": 558, "39": 571, "40": 585, "41": 601, "42": 614, "43": 628, "44": 641, "45": 655, "46": 665, "47": 678, "48": 691, "49": 702, "50": 714, "51": 727, "52": 742, "53": 753, "54": 764, "55": 773, "56": 788, "57": 801, "58": 816, "59": 826, "60": 840, "61": 849, "62": 860, "63": 879, "64": 890, "65": 908, "66": 920, "67": 934, "68": 946, "69": 957, "70": 966, "71": 979, "72": 991, "73": 1010, "74": 1028, "75": 1044, "76": 1061, "77": 1074, "78": 1084, "79": 1094, "80": 1101, "81": 1112, "82": 1126, "83": 1136, "84": 1151, "85": 1167, "86": 1178, "87": 1197, "88": 1210, "89": 1217, "90": 1230, "91": 1245, "92": 1254, "93": 1267, "94": 1283, "95": 1293, "96": 1308, "97": 1317, "98": 1333, "99": 1345, "100": 1360, "101": 1378, "102": 1391, "103": 1409, "104": 1421, "105": 1437, "106": 1452, "107": 1461, "108": 1474, "109": 1486, "110": 1502, "111": 1518, "112": 1546, "113": 1555, "114": 1564, "115": 1573, "116": 1584, "117": 1601, "118": 1611, "119": 1629, "120": 1638, "121": 1656, "122": 1668, "123": 1678, "124": 1693, "125": 1707, "126": 1721, "127": 1736, "128": 1747, "129": 1761, "130": 1770, "131": 1793, "132": 1802, "133": 1814, "134": 1823}
---

**Dave Jones:** Hi, let's take a look at the new Keysight 1000 X-Series oscilloscope, take it apart, and see if we can find a debug serial port inside this thing, and see what we can see.

**Dave Jones:** Who knows, we might be able to modify this thing, hack this thing, maybe get some extra functionality or something out of it. Let's give it a go. Now, it's very common for modern bits of test gear, especially ones that run embedded OS's like Windows CE and the like, to have a debug serial interface or like an RS-232 terminal type interface that displays boot information and stuff like

**Dave Jones:** that. So, usually you can access this on the PCB. Now, if you're real lucky, it'll be labeled like serial interface or debug or something like that, and you're looking for things like TX and RX and like a a header and things like that, but um I don't think that we're going to be lucky here.

**Dave Jones:** Let me take the processor board off here. But, if you have a look at the main board here, these are all like voltage test points, AC trigger in, you know, voltage 1.2 volts, 1 volt.

**Dave Jones:** Over here, there's a clock, a data, all that sort of stuff, but that's to do with like the keyboard interface. This is the USB port here. Don't know why that chip is missing there.

**Dave Jones:** They're obviously bypassing that. Basically, I can't see any header. There seems to be nothing on the main board here, and I've had a look at photos on the bottom side of the board cuz I did a teardown.

**Dave Jones:** There's nothing on that main board, nor would you really expect it, I guess, although there could be. But, let's have a look at the processor board. So, what we're looking for is an RS-232 type serial interface.

**Dave Jones:** It doesn't have to be RS-232 signal levels. Can easily be TTL or, you know, 5-V, 3.3-V, just regular digital logic. Once again, we've got JTAG here cuz we've got T-clock, TDO, TDI, TMS.

**Dave Jones:** That's all JTAG stuff. We've got another JTAG in here. So, we've got these test points and they're all labeled labeled very nicely. We have another JTAG down here and we got these DB debug.

**Dave Jones:** Now, you might think it's that, but I believe the debug has to do with the Megazoom for ASIC chip that we've got here. Whereas our Windows CE operating system is working inside this processor.

**Dave Jones:** So, that's a Speer 600-2. So, there's clearly nothing on the top side here. There's a couple of pads down in here. But, if we have a look at the bottom side here, the good news is that all of the BGA pins looks like they're fanned out to an individual via on the bottom of the chip like this.

**Dave Jones:** It's a really quite a, you know, 4-500 pin chip or something like that. Good thing about that, as they're not tinned either, which means that they have no solder mask covering them, which means that we can get our multimeter probe on there, really sharp one, and get in there and we can buzz out and measure the continuity for every single pin on that chip.

**Dave Jones:** Beautiful. But, once again, we don't have anything any test pads or anything like that that looks remotely like a serial port or anything to do with a serial port.

**Dave Jones:** So, I think we're out of luck there. What's that? Is that a bug? And here we have it, the Speer 600, which is not recommended for new designs, apparently.

**Dave Jones:** So, there you go. It doesn't mean that you I get it anymore, but um what it says on the website. Basically got a ton of stuff built in. It's got USB host, USB devices, gigabit ethernet, I squared C, synchronous serial ports, two what you are interfaces, which was what we're interested in here.

**Dave Jones:** Um almost certainly uh because I believe we're seeing it on the 2000 3000 X series scopes, so they're going to do the same thing here. And Keysight um for their Windows CE stuff, we have actually seen um you are interfaces like this before.

**Dave Jones:** So, it it's almost certain that it's in here somewhere. UARTs, here we go. But, that doesn't really tell us anything, does it? We need to find the pins. So, what we're going to do is search for uh UART here, and let's have a look.

**Dave Jones:** UART pins, that's the one we want. Page 27. This is a multi-hundred page document, so you got to uh search for stuff. It's pretty tedious to uh find things, but there that's the debug interface.

**Dave Jones:** We don't actually want this, even though I've called it like a debug type interface, and that's what it is. It's but it's serial terminal. So, that's different to the uh actual arm processor uh debug itself.

**Dave Jones:** So, what we want to do is go down here to our UART. Here we go. UART 1 TXD is the pin, so it's got two. We don't know which one it is, but if we copy that, and then we search for that particular pin, uh here we go.

**Dave Jones:** Ta-da! Here's our pin mapping for our, you know, 4 500 pins or however many is on this chip. AA19 here. So, AB19, AA19, they do them uh rows and uh column based with these uh BGA grin grid packages.

**Dave Jones:** Okay, so what we want to do, the pin mapping's usually at the end here. Here it is. Is that the one? Uh PBGA420. Just always make sure it only comes in Yeah, it looks like it only comes in one chip type.

**Dave Jones:** There you go. So, 420 pin. It's a bit of a beast. Um you know, but you can get over 1,000. I've used chips with over 1,000 pins, no worries.

**Dave Jones:** Anyway, here is the A1 ball pad corner. So, that's the one that we want to uh find. And what was it? AA19 or something? So, here is row AA up here and 19.

**Dave Jones:** So, it's going to be up in this quadrant, opposite corner to the A1 ball pad corner. You notice how the other one other ones have little notches taken out of them here?

**Dave Jones:** This and there should be like a big identifier on top of the chip. So, let's find that and then we're looking at the opposite pins over this side. There is our pin one dot or our A1 dot over here.

**Dave Jones:** You'll notice that the notches are taken out of those corners there, but our tracks are somewhere on these pins under here or should be. And you can see nothing coming out here.

**Dave Jones:** This is a 10-layer PCB, by the way. So, there could be lots of traces buried in the middle that you can't see. Best guess with that it would be coming out on the connector here because they would want to plug this board into a development test jig.

**Dave Jones:** And that's what this debug serial interface is for. Uh terminal interface is for development and you know, checking firmware production checking and all sorts of stuff. So, they're going to want to plug it into here and they can access this via bed of nails.

**Dave Jones:** Uh you don't need the you know, they saved a few cents. Um cents matter on this board. So, you know, they didn't need it for a uh for an actual production board.

**Dave Jones:** So, they took it off, but they can still access those via bed of nails. So, if you knew the exact pin, you could just do all the ones in that quadrant, uh whatever, and then just scrape along there with a continuity tester.

**Dave Jones:** Other way to do it is to simply probe all of these and see if you get lucky. And bingo, that didn't take long at all. I was I'm probing around the bottom uh corner of the spear chip there and bingo but only during the boot period is this debugger serial terminal port actually spewing out boot information and stuff like that.

**Dave Jones:** If you wait until it boots and then probe around, you won't be able to find anything there on the board. So once again, we're searching for a 3.3 volt logic level signal on there and just a little pro tip here because you're probing multiple pins one after the other and you're looking at the screen at the same time to make sure you know any signals are coming up.

**Dave Jones:** Make sure you don't short out the V's by the way. These are very close together even though I've got a sharp point on our scope there. You know, just want to be careful with that.

**Dave Jones:** Anyway, pro tip put on some variable persistence like that's infinite. Put on some variable persistence like a second or something like that. We power that up, you'll see that you know like you can just you know see information pop up.

**Dave Jones:** It just means that the information stays there on the screen a little bit longer. Okay, so a single shot captured some data there. What we want to do is go in there and just measure the board rate.

**Dave Jones:** So this is where your cursors come in handy or you can just do it manually. You just need to be in the ball park here. So you can actually see that it's you know it's serial UART type information.

**Dave Jones:** There we go. 115.2. Now just be careful which point you measure here. You can see that I'm measuring one where obviously the signal is changing every bit. So we actually don't want to measure a whole cycle here.

**Dave Jones:** Just be aware of that. We actually want to measure We actually want to measure the period between the two pulses. So basically the the one bit where it changes like that and that'll give us our board rate.

**Dave Jones:** 115K2. Okay, so what we want to go here is we want a UART RS4232 and the mode of course is UART RS-232. Set up our signals, our threshold at about a volt or whatever it is is fine.

**Dave Jones:** We're not doing that, transmit, we're only doing the uh receive at the moment. Um so our bus configuration, it's almost always eight data bits, uh no parity, uh the one stop bit, our board rate 115 K2, and our idle mode, we're actually idling high.

**Dave Jones:** There you can see that. And uh least significant bit order there. So if we go in, we can now see, tada, does that look sensible? NAND flash. There we go.

**Dave Jones:** NAND flash. That looks uh sensible to me. And you know, carriage return, line feed, um stuff like that. So you know, once you see something intelligent like that, you know, bingo, I've got myself a serial debug interface and Bob's your uncle.

**Dave Jones:** Fantastic. Now I could just hold the probe on the top and uh capture all the information, but hey, let's solder some wires on here. And we also want a receive pin on here as well.

**Dave Jones:** So uh we want to transmit from the PC as well potentially to uh like send it commands or do and to interact with it perhaps. But it's useful just if you got to receive a transmit line out of here, receive into the PC and you can just get the dup.

**Dave Jones:** Anyway, it's that second via there. So if you're probing from the top, it's that one there. You can see it's a bit worn out. Done it a few times.

**Dave Jones:** And so we want to solder a wire onto there and the one next to it, so the fifth pin over there I believe is the receive pin. So that's the transmit of the PC that you're going to hook it up to.

**Dave Jones:** So I'll just solder two wires on there and we'll be in like Flynn. All right, so we'll just feed a bit of solder onto there and just a little bit of fresh stuff onto there as well.

**Dave Jones:** That's one. And that's number two. Oh, short. I'll just tidy that up, wick that off. No worries. So, the next thing you want to do is read that into a PC.

**Dave Jones:** And what I've got here is this nice little doohickey because we're dealing with TTL levels here. We can't just hook it up to a regular serial port. Anyway, I've got it upside down.

**Dave Jones:** All the electrons are going to fall out. This is from Marvell 001.de. And I got this in the mailbag. So, thank you very much for sending in. Not only does it have RS232 signal levels, but it's also got TTL levels here.

**Dave Jones:** And you can adjust the voltage between 5 V or 0 and 3.3 V. And yeah, there we go. RS232 or TTL. So, we want TTL. So, that just appears as a serial port.

**Dave Jones:** You can probably like buy a simple one that is TTL 3.3 V compatible interface on eBay for I don't know, 5 or 10 bucks or something like that. But this is just a nice universal one.

**Dave Jones:** And we're wired up, ready to rock. And the ground point, I've just chosen the ground plane under there. Easy. Okay, so what we want now on the PC is to use a terminal port program.

**Dave Jones:** You can use Windows Terminal or whatever it is. Or you can use Termite like this. There's Realterm. And there's many different terminal programs. It's already installed in there as COM3.

**Dave Jones:** The baud rate 115, 2 8 data bits, 1 stop bit, no parity. 8N1 as they call it is pretty standard stuff. So, we should be ready to go. Clear the screen.

**Dave Jones:** And you want one that also saves the window to a text file as well. All right, I'm going to go switch it on. Woohoo! Winner, winner, chicken dinner! Look at this.

**Dave Jones:** U-Boot. No, it's not U-boat. It's U-Boot. Success, success. NAND flash. That's that NAND flash serial message that we captured before. And beautiful FPGA type, it's a marsupial. Um, terrific.

**Dave Jones:** I just heard the relays click. So, there we go. It's done. InfinityVision is running. As I said, it typically just does a boot dump like this. This is for a debugging and setup purposes.

**Dave Jones:** Totally super valuable, essential for the developers of this, and also for doing, uh, you know, firmware, um, you know, setup configuration, uh, hacks at the factory, and, uh, stuff like that.

**Dave Jones:** But, it can be useful for us. So, there you go. I'm going to, uh, save that, um, screen, and, uh, this will be our reference before we start doing any modifications with this thing.

**Dave Jones:** Now, the interesting thing here is that we don't seem to have a, uh, prompt here. Now, I'm no expert on U-Boot and Windows CE, and like I know bugger all, really.

**Dave Jones:** But, I would have expected a prompt in there. And if we do something like, uh, help, for example, or help games, um, we get no response whatsoever. Hang on.

**Dave Jones:** Ah. So, anyway, let's look at some interesting stuff in here, shall we? There's the, you know, it's got the Speer 600, the DRAM, the flash, everything else. Uh, Windows CE bootloader, all that sort of jazz.

**Dave Jones:** File not found. Uh, yeah, because we don't have a physical, um, ethernet, uh, file in there. So, anyway, preparing to download, real-time clock, loading image, BL image type. By the way, this board is called the BLT board.

**Dave Jones:** It's got BLT on the, uh, top, silk screen, copper layer. So, that's, I think that's their internal name for this, uh, processor board. So, that's just like loading the, uh, image.

**Dave Jones:** Okay, the build here is September 28th, 2016. Uh, I have actually also dumped information from a prototype unit which I actually have and it shows an earlier build for this and has some changes.

**Dave Jones:** I've posted that over on the EV blog forum thread, the teardown forum thread there. But anyway, so what we going and looking for here is any sort of like configuration information.

**Dave Jones:** And this is interesting, too. Hang on. Serial two. Okay, it looks like it's initiating that separate serial port. You remember when we saw on the data sheet for the Speer 600 that it actually had two serial ports.

**Dave Jones:** Now, I've had a look around and probed it out and I can't find a second serial port. I can't find any other serial data that's coming out at all.

**Dave Jones:** Here Here we go. We got BLT product config 24. This is interesting. The configuration 24, 24. I don't know what that means, but it's got different configurations, which is what we expect.

**Dave Jones:** And this is fantastic. Look at this bandwidth, 200 MHz. Why? This is a 100 MHz scope. Is the analog bandwidth actually 200 MHz? But why is it got 200 MHz in there?

**Dave Jones:** I don't know. Two channels, of course. Board revision F P I, whatever that is. Clock gating board one, don't know. 4 gig samples per second. The ADC sampling at 4 gig, but 2 gig per channel because this scope does two a full 2 gig chip per channel and it doesn't have when you go down.

**Dave Jones:** Anyway, it's got another BLT module configuration. So, there's a BLT product and a BLT module. So, I Once again, they've got different configurations. Revision LP3, whatever that means. And the sample rate, 5 gig samples a second.

**Dave Jones:** Which the MegaZoom 4 ASIC is capable of in their high-end um, like the I think the 3,000, 4,000 and the 6,000 whatever that do they do five at least the high bandwidth ones, the one gig bandwidth ones do five gig samples a second.

**Dave Jones:** So, the chip's capable of that. Now, here's some fascinating stuff. BLT product configuration zero and one ID2 ID4 and look, it's got a voltage in there 1.246 volts, 0.692 volts, right?

**Dave Jones:** That's got to be volts. So, that implies that they're using an ADC inside the Speer 600 to actually measure configuration resistors. Um, why you couldn't just use pins like how many modes are there?

**Dave Jones:** Um, anyway, you can do that, do it with ADCs and just set a a resistor divider. So, bingo, hopefully we can modify those resistor values and change the configuration.

**Dave Jones:** But, that doesn't mean this is going to work because I fully expect uh, well, I know for a fact that you can upgrade the bandwidth with the license keys inside this thing.

**Dave Jones:** And we might be able to change the configuration and it might say that it's, you know, maybe if we're lucky it'll boot up and say it's a different model or whatever.

**Dave Jones:** Um, that's certainly possible whether or not you can like actually get like the serial decode option because that requires a license as well and also that bandwidth upgrade requires a license.

**Dave Jones:** So, this all all may be for naught doing this hardware um, hacking investigation here, you know, if you don't have the serial keys to enable options. Anyway, that's really fascinating.

**Dave Jones:** So, we need to take another look at the board, look for some configuration set resistors. So, K9, um, I believe that is the main analog motherboard uh, so to speak.

**Dave Jones:** So, it's measuring basically zero volts, it's grounded there ID0, but we don't want to muck around. We're not too concerned with that. Now, this is interesting MSO revision. This scope does not have an MSO option, doesn't have room for it, whatever.

**Dave Jones:** have they reserved that for a future release? I don't know. Anyway, that's got nothing to do with today's experiment. Initializing SPG PGA, it's a marsupial. I love it. In January June 4th build time, June 14th.

**Dave Jones:** Wow, so they so they settled on the FPGA architecture, you know, a fair bit back before this, which is not surprising. You don't want to be around your FPGA architecture at the last minute.

**Dave Jones:** If you've screwed that up, then you're in serious trouble. So, factory cal stuff, there you go. That is some fascinating information in there, and it's amazing what you find when you just get these serial dumps like that, these boot dumps when you got a complex OS like Windows CE.

**Dave Jones:** So, let's have a look for some resistors and see if we can modify this. Hmm. Do you feel lucky, punk? This is the prototype board from my prototype unit, but it's exactly same revision 002 here.

**Dave Jones:** It looks identical. If you want to know the difference between the prototype unit that I've got that I've had for I got it at the electronics trade show last year.

**Dave Jones:** There you go. So, whatever date that was, September. Processor board looks exactly the same, but the main motherboard, the canine board, is revision three instead of revision four, which I got in the production unit.

**Dave Jones:** Anyway, so we're looking for configuration set resistors, and they're not going to be these resistor arrays here. So, forget about those. There's a couple of resistors over here, but I was probing these pads over there just cuz they looked interesting.

**Dave Jones:** I got like a 30 MHz sine wave, so it's not that. So, there's no resistors on the top. So, we want to be able to look for some resistors on the bottom here.

**Dave Jones:** There's a potential candidate, but once again, it's not going to be any of these resistor arrays, but hello. Hello. There's a whole strip. Bingo. This is what we want.

**Dave Jones:** Look, that looks like a resistor divider. The thicker trace there is obviously going to be ground or power, and then we've got the thin signal trace going off to a via, which then goes under here to one, you know, to some pin somewhere on the board here.

**Dave Jones:** So, these, for all the world, look like resis- you know, set set resistors right next to the chip. So, if we flip it over, hello, we can access those.

**Dave Jones:** It's beautiful, and I love untinted vias. We don't have to get in there and scrape off. We can just probe. Thank you very much, Keysight. And the PCB layout person who went, "I don't want those bloody tinted vias.

**Dave Jones:** Can't hack and probe the thing. Bugger that." So, what we want to do now is just go measuring around there with the multimeter and see if we can get pretty close to the voltages.

**Dave Jones:** So, we're looking for around about 1.25-ish volts, and you know, around about 0.7 volts or something like that. If we can find those voltages, they're pretty specific. So, I think if we can find those, I think we could be in like Flynn.

**Dave Jones:** Hello. 0.6 volts. And we can, you know, check these for activity, and I have, and there's no activity, as in signal activity on the scope. 2.41, no, zero. Bingo.

**Dave Jones:** 0.6, let's call it 0.67 volts. That's the fourth one over there, if you can see that. What do we get? 0.68 or something? That's going to I'm going to call that near enough.

**Dave Jones:** It's too coincidental to have that sort of voltage, and 1.2 two, as in as opposed to 1.25. I'm going to call that near enough as well. So, that's the last one on the bottom row of that, and the fourth one over.

**Dave Jones:** I am going to have a go at modifying those values and see what happens. Tell you what, this mega zoom 4 ASIC under here gets bloody hot, let me tell you.

**Dave Jones:** Anyway, we're looking for the fourth pin across. So, that one there. So, those two resistors there. So, I'll just take off one of these resistors and that'll pull it to presumably either rail and just see if it changes on boot.

**Dave Jones:** See if that value actually changes. If we do, we know we've got it. Bingo. And boot her up. What are we getting? What are we getting? Is it going to change?

**Dave Jones:** We got it. It worked. ID2 ID0. BLT module config, we have changed it. Bingo. It's now 0.064 V. So, this is a 64 mV offset there. But, yep. We got it.

**Dave Jones:** We were able to change the configuration of that. What that means, I don't know. You'd have to experiment with all these configurations. Right. Now comes the hard work. And that little puppy is 120k.

**Dave Jones:** So, we can put like, you know, it'd be okay to put say 100k pot in there. If you're experiment experimenting with this, you wouldn't want to be around soldering desoldering resistor values until the cows come home.

**Dave Jones:** Just whack a pot in there. Jeez, you can hardly Make sure I don't sneeze. So, obviously, if we take out that one, they're our two supplies, ground and supply, and that's our voltage divider tap.

**Dave Jones:** We've got another one here which looks to do the same thing with the two resistors joined, but we've got um four channels that it's measuring the voltage from. So, yeah, we've got Okay.

**Dave Jones:** So, these two resistors and these, I'm going to assume these two as well. Still need to verify, but I think, you know, that's a pretty decent bet. Why? I mean, if you're laying out the board and these were a voltage divider tap, you'd have a trace between those two, not two separate things like that.

**Dave Jones:** So, it doesn't make sense. And we've got five vias along Sorry, six vias along here and only four voltage tap points. So, I don't know. Does this one only go to the supply and that's it?

**Dave Jones:** And likewise, this one only go to the supply? The only way to find out is to suck them off one by one and note the changes. And just a little tip, if you want to get some fine wire down there, my standard 30 gauge mod wire doesn't do it, but just get a stranded bit of tin copper wire and they're usually small enough to get down almost any via except

**Dave Jones:** that, you know, the real micro ones. Now, that's what I'm talking about. Here's a mod for you. Flying wires coming up. Those individual strands there got two pots here.

**Dave Jones:** These are just super glued together and then a little dab of super glue to hold it down on the board. Not too much so you can actually prize it off later.

**Dave Jones:** It usually doesn't do any damage. And like you could have maybe attempted to put one on this side, one on that side and try to bend the leads over, but too hard.

**Dave Jones:** Much better to mount them elsewhere and then route fine wires over to there like that. And it might look like they're shorted there, but they're not. They're crossing over with a fair bit of air.

**Dave Jones:** Awesome. And the thing about mounting them separately like that and then rigidly coupling them down to the board is that it decouples the stress from the trimmers here. So, you know, you got to put your screwdriver in there, you push too hard, and if you've got them right on the solder joints there, it's not good.

**Dave Jones:** So, decouple the stress. That's today's tip. So, once we've installed the pots, we boot it up. The pots are still set to factory mid-level roughly or whatever it is they they are.

**Dave Jones:** We're getting ID3 and ID4, which is totally different to what we had before we've done the mod. And the first thing we see in the dump here is that it actually shows us zero gig samples per second for the board configuration, not the product configuration, the board configuration.

**Dave Jones:** But hey, if we go into here to the scope, we can show that it's actually two gig samples per second and the scope is exactly the same. We haven't changed our model number or anything.

**Dave Jones:** But once again, we wouldn't expect it to cuz we're configuration. So what that board configuration is doing, I don't really know cuz it doesn't seem to make a difference in terms of the actual operation, the sample rate because the educational model has a lower sample rate for example.

**Dave Jones:** So I yeah, it's just not doing it. We have to get the product ID. So it seems like the only thing that those two pots are going to adjust is the processor module sample rate.

**Dave Jones:** But what that actually means because that's different to the product sample rate and it doesn't seem to be affected by the sample rate when you're actually using the thing.

**Dave Jones:** So yeah, all those pots for just the sample rate. Bloody Murphy. And I'm feeding in a 1-V peak-to-peak 100 MHz sine wave here and I've verified the 1-V peak-to-peak on my 500 meg 3000 X series scope.

**Dave Jones:** So it's showing it's showing about 880 mV peak there. So you know, it's like a little it's kind of what you expect for 100 MHz bandwidth cuz in theory theory for 100 MHz it's going to be down by 3 dB or .707.

**Dave Jones:** So it's doing reasonably well there actually. What I wanted to show was that it is actually doing the two gig samples second even though we've changed that and it it seems to be working just fine.

**Dave Jones:** So the product sample rate is just as it should be. And there you go. Uh 0.707 at 131 MHz or thereabouts. So, it's got, you know, a fair bit better than its nominal 100 MHz uh quoted bandwidth.

**Dave Jones:** So, I've actually had some more play around with this. I've taken off a few of the resistors uh down the bottom uh there and I cannot um yet find that uh product ID.

**Dave Jones:** Um but, it's got to be there somewhere. I just need more time. Or maybe if um before I get around to it, somebody else has already found it cuz I'm sure um there's Well, there are definitely people uh working on this.

**Dave Jones:** So, I have no doubt if we find that product ID, then it starts getting interesting because that board ID doesn't seem to be doing much that I can see anyway.

**Dave Jones:** But, it shows that we are actually getting boot changes and configuration uh type changes by changing some resistor values on there being read from the ADC. So, I hope you found that uh interesting just looking at like a systematic procedure how to find a serial uh boot UART in um a product uh like this and being able to get some useful info and like start the process of hacking uh this thing.

**Dave Jones:** But, as I said, it's probably going to require license keys and everything else to really get, you know, say the embedded options and the extra bandwidth and uh stuff like that.

**Dave Jones:** Anyway, um that's all we got for today. I'm sure there might be uh more parts on this if we can uh get more information. So, if you like the video, please give it a big thumbs up.

**Dave Jones:** Thumbs up. It fits on the screen. There we go. And as always, uh link down to below to the EEVblog forum to discuss where people are discussing hacking this baby.

**Dave Jones:** Catch you next time.
