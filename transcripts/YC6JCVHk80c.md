---
video_id: YC6JCVHk80c
title: EEVblog #977 - Keysight 1000X Hacking - Part 1
url: https://www.youtube.com/watch?v=YC6JCVHk80c
source: youtube-asr
---

**Dave Jones:** Hi, let's take a look at the new Keysight 1000 X-Series oscilloscope, take it apart, and see if we can find a debug serial port inside this thing, and see what we can see. Who knows, we might be able to modify this thing, hack this

**Dave Jones:** thing, maybe get some extra functionality or something out of it. Let's give it a go. Now, it's very common for modern bits of test gear, especially ones that run embedded OS's like Windows CE and the like, to have a

**Dave Jones:** debug serial interface or like an RS-232 terminal type interface that displays boot information and stuff like that. So, usually you can access this on the PCB. Now, if you're real lucky, it'll be labeled like serial interface or debug or

**Dave Jones:** something like that, and you're looking for things like TX and RX and like a a header and things like that, but um I don't think that we're going to be lucky here. Let me take the processor board off here. But, if you have a look at the

**Dave Jones:** main board here, these are all like voltage test points, AC trigger in, you know, voltage 1.2 volts, 1 volt. Over here, there's a clock, a data, all that sort of stuff, but that's to do with like the keyboard interface. This

**Dave Jones:** is the USB port here. Don't know why that chip is missing there. They're obviously bypassing that. Basically, I can't see any header. There seems to be nothing on the main board here, and I've had a look at photos on the bottom side of the

**Dave Jones:** board cuz I did a teardown. There's nothing on that main board, nor would you really expect it, I guess, although there could be. But, let's have a look at the processor board. So, what we're looking for is an

**Dave Jones:** RS-232 type serial interface. It doesn't have to be RS-232 signal levels. Can easily be TTL or, you know, 5-V, 3.3-V, just regular digital logic. Once again, we've got JTAG here cuz we've got T-clock, TDO, TDI, TMS. That's all JTAG stuff. We've

**Dave Jones:** got another JTAG in here. So, we've got these test points and they're all labeled labeled very nicely. We have another JTAG down here and we got these DB debug. Now, you might think it's that, but I believe the debug has to do

**Dave Jones:** with the Megazoom for ASIC chip that we've got here. Whereas our Windows CE operating system is working inside this processor. So, that's a Speer 600-2. So, there's clearly nothing on the top side here. There's a couple of pads down in here. But, if we have a

**Dave Jones:** look at the bottom side here, the good news is that all of the BGA pins looks like they're fanned out to an individual via on the bottom of the chip like this. It's a really quite a, you know, 4-500

**Dave Jones:** pin chip or something like that. Good thing about that, as they're not tinned either, which means that they have no solder mask covering them, which means that we can get our multimeter probe on there, really sharp one, and get in

**Dave Jones:** there and we can buzz out and measure the continuity for every single pin on that chip. Beautiful. But, once again, we don't have anything any test pads or anything like that that looks remotely like a serial port or anything to do with a serial port.

**Dave Jones:** So, I think we're out of luck there. What's that? Is that a bug? And here we have it, the Speer 600, which is not recommended for new designs, apparently. So, there you go. It doesn't mean that you I get it

**Dave Jones:** anymore, but um what it says on the website. Basically got a ton of stuff built in. It's got USB host, USB devices, gigabit ethernet, I squared C, synchronous serial ports, two what you are interfaces, which was what we're

**Dave Jones:** interested in here. Um almost certainly uh because I believe we're seeing it on the 2000 3000 X series scopes, so they're going to do the same thing here. And Keysight um for their Windows CE stuff, we have actually seen um you are interfaces like

**Dave Jones:** this before. So, it it's almost certain that it's in here somewhere. UARTs, here we go. But, that doesn't really tell us anything, does it? We need to find the pins. So, what we're going to do is search for

**Dave Jones:** uh UART here, and let's have a look. UART pins, that's the one we want. Page 27. This is a multi-hundred page document, so you got to uh search for stuff. It's pretty tedious to uh find things, but there that's the debug

**Dave Jones:** interface. We don't actually want this, even though I've called it like a debug type interface, and that's what it is. It's but it's serial terminal. So, that's different to the uh actual arm processor uh debug itself. So, what we

**Dave Jones:** want to do is go down here to our UART. Here we go. UART 1 TXD is the pin, so it's got two. We don't know which one it is, but if we copy that, and then we search for that particular pin,

**Dave Jones:** uh here we go. Ta-da! Here's our pin mapping for our, you know, 4 500 pins or however many is on this chip. AA19 here. So, AB19, AA19, they do them uh rows and uh column based with these uh BGA grin

**Dave Jones:** grid packages. Okay, so what we want to do, the pin mapping's usually at the end here. Here it is. Is that the one? Uh PBGA420. Just always make sure it only comes in Yeah, it looks like it only comes in one

**Dave Jones:** chip type. There you go. So, 420 pin. It's a bit of a beast. Um you know, but you can get over 1,000. I've used chips with over 1,000 pins, no worries. Anyway, here is the A1 ball pad corner. So, that's the one that we want

**Dave Jones:** to uh find. And what was it? AA19 or something? So, here is row AA up here and 19. So, it's going to be up in this quadrant, opposite corner to the A1 ball pad corner. You notice how the other one

**Dave Jones:** other ones have little notches taken out of them here? This and there should be like a big identifier on top of the chip. So, let's find that and then we're looking at the opposite pins over this side. There is our pin one dot or our A1

**Dave Jones:** dot over here. You'll notice that the notches are taken out of those corners there, but our tracks are somewhere on these pins under here or should be. And you can see nothing coming out here. This is a 10-layer PCB, by the way. So,

**Dave Jones:** there could be lots of traces buried in the middle that you can't see. Best guess with that it would be coming out on the connector here because they would want to plug this board into a development test jig. And that's what

**Dave Jones:** this debug serial interface is for. Uh terminal interface is for development and you know, checking firmware production checking and all sorts of stuff. So, they're going to want to plug it into here and they can access this via bed of nails. Uh you don't need the

**Dave Jones:** you know, they saved a few cents. Um cents matter on this board. So, you know, they didn't need it for a uh for an actual production board. So, they took it off, but they can still access those via bed of nails. So, if you knew

**Dave Jones:** the exact pin, you could just do all the ones in that quadrant, uh whatever, and then just scrape along there with a continuity tester. Other way to do it is to simply probe all of these and see if you get lucky.

**Dave Jones:** And bingo, that didn't take long at all. I was I'm probing around the bottom uh corner of the spear chip there and bingo but only during the boot period is this debugger serial terminal port actually spewing out boot information and stuff

**Dave Jones:** like that. If you wait until it boots and then probe around, you won't be able to find anything there on the board. So once again, we're searching for a 3.3 volt logic level signal on there and just a little pro tip here because

**Dave Jones:** you're probing multiple pins one after the other and you're looking at the screen at the same time to make sure you know any signals are coming up. Make sure you don't short out the V's by the way. These are very close together even

**Dave Jones:** though I've got a sharp point on our scope there. You know, just want to be careful with that. Anyway, pro tip put on some variable persistence like that's infinite. Put on some variable persistence like a second or something

**Dave Jones:** like that. We power that up, you'll see that you know like you can just you know see information pop up. It just means that the information stays there on the screen a little bit longer. Okay, so a single

**Dave Jones:** shot captured some data there. What we want to do is go in there and just measure the board rate. So this is where your cursors come in handy or you can just do it manually. You just need to be

**Dave Jones:** in the ball park here. So you can actually see that it's you know it's serial UART type information. There we go. 115.2. Now just be careful which point you measure here. You can see that I'm measuring one where obviously the signal

**Dave Jones:** is changing every bit. So we actually don't want to measure a whole cycle here. Just be aware of that. We actually want to measure We actually want to measure the period between the two pulses. So basically the the one bit where it

**Dave Jones:** changes like that and that'll give us our board rate. 115K2. Okay, so what we want to go here is we want a UART RS4232 and the mode of course is UART RS-232. Set up our signals, our threshold at

**Dave Jones:** about a volt or whatever it is is fine. We're not doing that, transmit, we're only doing the uh receive at the moment. Um so our bus configuration, it's almost always eight data bits, uh no parity, uh the one stop bit, our board rate 115 K2,

**Dave Jones:** and our idle mode, we're actually idling high. There you can see that. And uh least significant bit order there. So if we go in, we can now see, tada, does that look sensible? NAND flash. There we go. NAND flash. That looks uh sensible

**Dave Jones:** to me. And you know, carriage return, line feed, um stuff like that. So you know, once you see something intelligent like that, you know, bingo, I've got myself a serial debug interface and Bob's your uncle. Fantastic. Now I could

**Dave Jones:** just hold the probe on the top and uh capture all the information, but hey, let's solder some wires on here. And we also want a receive pin on here as well. So uh we want to transmit from the PC as

**Dave Jones:** well potentially to uh like send it commands or do and to interact with it perhaps. But it's useful just if you got to receive a transmit line out of here, receive into the PC and you can just get

**Dave Jones:** the dup. Anyway, it's that second via there. So if you're probing from the top, it's that one there. You can see it's a bit worn out. Done it a few times. And so we want to solder a wire

**Dave Jones:** onto there and the one next to it, so the fifth pin over there I believe is the receive pin. So that's the transmit of the PC that you're going to hook it up to. So I'll just solder two wires on

**Dave Jones:** there and we'll be in like Flynn. All right, so we'll just feed a bit of solder onto there and just a little bit of fresh stuff onto there as well. That's one. And that's number two. Oh, short. I'll

**Dave Jones:** just tidy that up, wick that off. No worries. So, the next thing you want to do is read that into a PC. And what I've got here is this nice little doohickey because we're dealing with TTL levels here. We can't just hook it up to

**Dave Jones:** a regular serial port. Anyway, I've got it upside down. All the electrons are going to fall out. This is from Marvell 001.de. And I got this in the mailbag. So, thank you very much for sending in. Not only

**Dave Jones:** does it have RS232 signal levels, but it's also got TTL levels here. And you can adjust the voltage between 5 V or 0 and 3.3 V. And yeah, there we go. RS232 or TTL. So, we want TTL. So, that just appears as a

**Dave Jones:** serial port. You can probably like buy a simple one that is TTL 3.3 V compatible interface on eBay for I don't know, 5 or 10 bucks or something like that. But this is just a nice universal one. And we're wired up, ready

**Dave Jones:** to rock. And the ground point, I've just chosen the ground plane under there. Easy. Okay, so what we want now on the PC is to use a terminal port program. You can use Windows Terminal or whatever it is. Or you can use Termite like this.

**Dave Jones:** There's Realterm. And there's many different terminal programs. It's already installed in there as COM3. The baud rate 115, 2 8 data bits, 1 stop bit, no parity. 8N1 as they call it is pretty standard stuff. So, we should be ready to go. Clear the

**Dave Jones:** screen. And you want one that also saves the window to a text file as well. All right, I'm going to go switch it on.

**Dave Jones:** Woohoo! Winner, winner, chicken dinner! Look at this. U-Boot. No, it's not U-boat. It's U-Boot. Success, success. NAND flash. That's that NAND flash serial message that we captured before. And beautiful FPGA type, it's a marsupial. Um, terrific. I just heard the relays

**Dave Jones:** click. So, there we go. It's done. InfinityVision is running. As I said, it typically just does a boot dump like this. This is for a debugging and setup purposes. Totally super valuable, essential for the developers of this, and also for doing,

**Dave Jones:** uh, you know, firmware, um, you know, setup configuration, uh, hacks at the factory, and, uh, stuff like that. But, it can be useful for us. So, there you go. I'm going to, uh, save that, um, screen, and, uh, this will be

**Dave Jones:** our reference before we start doing any modifications with this thing. Now, the interesting thing here is that we don't seem to have a, uh, prompt here. Now, I'm no expert on U-Boot and Windows CE, and like I know bugger all, really. But,

**Dave Jones:** I would have expected a prompt in there. And if we do something like, uh, help, for example, or help games, um, we get no response whatsoever. Hang on.

**Dave Jones:** Ah. So, anyway, let's look at some interesting stuff in here, shall we? There's the, you know, it's got the Speer 600, the DRAM, the flash, everything else. Uh, Windows CE bootloader, all that sort of jazz. File not found. Uh, yeah, because we don't

**Dave Jones:** have a physical, um, ethernet, uh, file in there. So, anyway, preparing to download, real-time clock, loading image, BL image type. By the way, this board is called the BLT board. It's got BLT on the, uh, top, silk screen, copper layer. So,

**Dave Jones:** that's, I think that's their internal name for this, uh, processor board. So, that's just like loading the, uh, image. Okay, the build here is September 28th, 2016. Uh, I have actually also dumped information from a prototype unit which

**Dave Jones:** I actually have and it shows an earlier build for this and has some changes. I've posted that over on the EV blog forum thread, the teardown forum thread there. But anyway, so what we going and looking for here is any

**Dave Jones:** sort of like configuration information. And this is interesting, too. Hang on. Serial two. Okay, it looks like it's initiating that separate serial port. You remember when we saw on the data sheet for the Speer 600 that it actually had two serial ports. Now, I've

**Dave Jones:** had a look around and probed it out and I can't find a second serial port. I can't find any other serial data that's coming out at all. Here Here we go. We got BLT product config 24. This is

**Dave Jones:** interesting. The configuration 24, 24. I don't know what that means, but it's got different configurations, which is what we expect. And this is fantastic. Look at this bandwidth, 200 MHz. Why? This is a 100 MHz scope. Is the analog bandwidth

**Dave Jones:** actually 200 MHz? But why is it got 200 MHz in there? I don't know. Two channels, of course. Board revision F P I, whatever that is. Clock gating board one, don't know. 4 gig samples per second. The ADC sampling at 4 gig, but 2

**Dave Jones:** gig per channel because this scope does two a full 2 gig chip per channel and it doesn't have when you go down. Anyway, it's got another BLT module configuration. So, there's a BLT product and a BLT module. So, I

**Dave Jones:** Once again, they've got different configurations. Revision LP3, whatever that means. And the sample rate, 5 gig samples a second. Which the MegaZoom 4 ASIC is capable of in their high-end um, like the I think the 3,000, 4,000 and

**Dave Jones:** the 6,000 whatever that do they do five at least the high bandwidth ones, the one gig bandwidth ones do five gig samples a second. So, the chip's capable of that. Now, here's some fascinating stuff. BLT product configuration zero

**Dave Jones:** and one ID2 ID4 and look, it's got a voltage in there 1.246 volts, 0.692 volts, right? That's got to be volts. So, that implies that they're using an ADC inside the Speer 600 to actually measure configuration resistors. Um, why

**Dave Jones:** you couldn't just use pins like how many modes are there? Um, anyway, you can do that, do it with ADCs and just set a a resistor divider. So, bingo, hopefully we can modify those resistor values and change the configuration. But, that

**Dave Jones:** doesn't mean this is going to work because I fully expect uh, well, I know for a fact that you can upgrade the bandwidth with the license keys inside this thing. And we might be able to change the configuration and it might

**Dave Jones:** say that it's, you know, maybe if we're lucky it'll boot up and say it's a different model or whatever. Um, that's certainly possible whether or not you can like actually get like the serial decode option because that requires a

**Dave Jones:** license as well and also that bandwidth upgrade requires a license. So, this all all may be for naught doing this hardware um, hacking investigation here, you know, if you don't have the serial keys to enable options. Anyway, that's

**Dave Jones:** really fascinating. So, we need to take another look at the board, look for some configuration set resistors. So, K9, um, I believe that is the main analog motherboard uh, so to speak. So, it's measuring basically zero volts, it's

**Dave Jones:** grounded there ID0, but we don't want to muck around. We're not too concerned with that. Now, this is interesting MSO revision. This scope does not have an MSO option, doesn't have room for it, whatever. have they reserved that for a

**Dave Jones:** future release? I don't know. Anyway, that's got nothing to do with today's experiment. Initializing SPG PGA, it's a marsupial. I love it. In January June 4th build time, June 14th. Wow, so they so they settled on the FPGA

**Dave Jones:** architecture, you know, a fair bit back before this, which is not surprising. You don't want to be around your FPGA architecture at the last minute. If you've screwed that up, then you're in serious trouble. So, factory cal stuff,

**Dave Jones:** there you go. That is some fascinating information in there, and it's amazing what you find when you just get these serial dumps like that, these boot dumps when you got a complex OS like Windows CE. So, let's have a look for some

**Dave Jones:** resistors and see if we can modify this. Hmm. Do you feel lucky, punk? This is the prototype board from my prototype unit, but it's exactly same revision 002 here. It looks identical. If you want to know the difference

**Dave Jones:** between the prototype unit that I've got that I've had for I got it at the electronics trade show last year. There you go. So, whatever date that was, September. Processor board looks exactly the same, but the main motherboard, the

**Dave Jones:** canine board, is revision three instead of revision four, which I got in the production unit. Anyway, so we're looking for configuration set resistors, and they're not going to be these resistor arrays here. So, forget about those. There's a couple of resistors

**Dave Jones:** over here, but I was probing these pads over there just cuz they looked interesting. I got like a 30 MHz sine wave, so it's not that. So, there's no resistors on the top. So, we want to be able to look for some resistors on

**Dave Jones:** the bottom here. There's a potential candidate, but once again, it's not going to be any of these resistor arrays, but hello. Hello. There's a whole strip. Bingo. This is what we want. Look, that looks like a resistor divider. The thicker trace

**Dave Jones:** there is obviously going to be ground or power, and then we've got the thin signal trace going off to a via, which then goes under here to one, you know, to some pin somewhere on the board here. So, these, for all the world, look like

**Dave Jones:** resis- you know, set set resistors right next to the chip. So, if we flip it over, hello, we can access those. It's beautiful, and I love untinted vias. We don't have to get in there and scrape off. We can just

**Dave Jones:** probe. Thank you very much, Keysight. And the PCB layout person who went, "I don't want those bloody tinted vias. Can't hack and probe the thing. Bugger that." So, what we want to do now is just go measuring around there with the

**Dave Jones:** multimeter and see if we can get pretty close to the voltages. So, we're looking for around about 1.25-ish volts, and you know, around about 0.7 volts or something like that. If we can find those voltages, they're pretty specific. So, I think if we can find

**Dave Jones:** those, I think we could be in like Flynn. Hello. 0.6 volts. And we can, you know, check these for activity, and I have, and there's no activity, as in signal activity on the scope. 2.41, no, zero. Bingo. 0.6, let's call it 0.67

**Dave Jones:** volts. That's the fourth one over there, if you can see that. What do we get? 0.68 or something? That's going to I'm going to call that near enough. It's too coincidental to have that sort of voltage, and 1.2

**Dave Jones:** two, as in as opposed to 1.25. I'm going to call that near enough as well. So, that's the last one on the bottom row of that, and the fourth one over. I am going to have a go at modifying

**Dave Jones:** those values and see what happens. Tell you what, this mega zoom 4 ASIC under here gets bloody hot, let me tell you. Anyway, we're looking for the fourth pin across. So, that one there. So, those two resistors there. So, I'll just

**Dave Jones:** take off one of these resistors and that'll pull it to presumably either rail and just see if it changes on boot. See if that value actually changes. If we do, we know we've got it. Bingo. And boot her up.

**Dave Jones:** What are we getting? What are we getting? Is it going to change? We got it. It worked. ID2 ID0. BLT module config, we have changed it. Bingo. It's now 0.064 V. So, this is a 64 mV offset there.

**Dave Jones:** But, yep. We got it. We were able to change the configuration of that. What that means, I don't know. You'd have to experiment with all these configurations. Right. Now comes the hard work. And that little puppy is 120k.

**Dave Jones:** So, we can put like, you know, it'd be okay to put say 100k pot in there. If you're experiment experimenting with this, you wouldn't want to be around soldering desoldering resistor values until the cows come home. Just whack a pot in there. Jeez, you can

**Dave Jones:** hardly Make sure I don't sneeze. So, obviously, if we take out that one, they're our two supplies, ground and supply, and that's our voltage divider tap. We've got another one here which looks to do the same thing with the two resistors

**Dave Jones:** joined, but we've got um four channels that it's measuring the voltage from. So, yeah, we've got Okay. So, these two resistors and these, I'm going to assume these two as well. Still need to verify, but I think, you know, that's a pretty

**Dave Jones:** decent bet. Why? I mean, if you're laying out the board and these were a voltage divider tap, you'd have a trace between those two, not two separate things like that. So, it doesn't make sense. And we've got five vias along

**Dave Jones:** Sorry, six vias along here and only four voltage tap points. So, I don't know. Does this one only go to the supply and that's it? And likewise, this one only go to the supply? The only way to find out is to

**Dave Jones:** suck them off one by one and note the changes. And just a little tip, if you want to get some fine wire down there, my standard 30 gauge mod wire doesn't do it, but just get a stranded bit of tin

**Dave Jones:** copper wire and they're usually small enough to get down almost any via except that, you know, the real micro ones. Now, that's what I'm talking about. Here's a mod for you. Flying wires coming up. Those individual strands there got two pots here. These are just

**Dave Jones:** super glued together and then a little dab of super glue to hold it down on the board. Not too much so you can actually prize it off later. It usually doesn't do any damage. And like you could have maybe attempted to

**Dave Jones:** put one on this side, one on that side and try to bend the leads over, but too hard. Much better to mount them elsewhere and then route fine wires over to there like that. And it might look like they're shorted there, but they're

**Dave Jones:** not. They're crossing over with a fair bit of air. Awesome. And the thing about mounting them separately like that and then rigidly coupling them down to the board is that it decouples the stress from the trimmers here. So, you know,

**Dave Jones:** you got to put your screwdriver in there, you push too hard, and if you've got them right on the solder joints there, it's not good. So, decouple the stress. That's today's tip. So, once we've installed the pots, we boot it up. The

**Dave Jones:** pots are still set to factory mid-level roughly or whatever it is they they are. We're getting ID3 and ID4, which is totally different to what we had before we've done the mod. And the first thing we see in the dump here is that it

**Dave Jones:** actually shows us zero gig samples per second for the board configuration, not the product configuration, the board configuration. But hey, if we go into here to the scope, we can show that it's actually two gig samples per second and

**Dave Jones:** the scope is exactly the same. We haven't changed our model number or anything. But once again, we wouldn't expect it to cuz we're configuration. So what that board configuration is doing, I don't really know cuz it doesn't seem

**Dave Jones:** to make a difference in terms of the actual operation, the sample rate because the educational model has a lower sample rate for example. So I yeah, it's just not doing it. We have to get the product ID. So it seems like the

**Dave Jones:** only thing that those two pots are going to adjust is the processor module sample rate. But what that actually means because that's different to the product sample rate and it doesn't seem to be affected by the sample rate when you're actually using

**Dave Jones:** the thing. So yeah, all those pots for just the sample rate. Bloody Murphy. And I'm feeding in a 1-V peak-to-peak 100 MHz sine wave here and I've verified the 1-V peak-to-peak on my 500 meg 3000 X series scope. So it's showing

**Dave Jones:** it's showing about 880 mV peak there. So you know, it's like a little it's kind of what you expect for 100 MHz bandwidth cuz in theory theory for 100 MHz it's going to be down by 3 dB or .707. So

**Dave Jones:** it's doing reasonably well there actually. What I wanted to show was that it is actually doing the two gig samples second even though we've changed that and it it seems to be working just fine. So the product sample rate is just as it should

**Dave Jones:** be. And there you go. Uh 0.707 at 131 MHz or thereabouts. So, it's got, you know, a fair bit better than its nominal 100 MHz uh quoted bandwidth. So, I've actually had some more play around with this. I've taken off a few of the resistors uh

**Dave Jones:** down the bottom uh there and I cannot um yet find that uh product ID. Um but, it's got to be there somewhere. I just need more time. Or maybe if um before I get around to it, somebody else has already found it

**Dave Jones:** cuz I'm sure um there's Well, there are definitely people uh working on this. So, I have no doubt if we find that product ID, then it starts getting interesting because that board ID doesn't seem to be doing much that I can

**Dave Jones:** see anyway. But, it shows that we are actually getting boot changes and configuration uh type changes by changing some resistor values on there being read from the ADC. So, I hope you found that uh interesting just looking at like a systematic procedure how to

**Dave Jones:** find a serial uh boot UART in um a product uh like this and being able to get some useful info and like start the process of hacking uh this thing. But, as I said, it's probably going to require license keys and everything else

**Dave Jones:** to really get, you know, say the embedded options and the extra bandwidth and uh stuff like that. Anyway, um that's all we got for today. I'm sure there might be uh more parts on this if we can uh get more information. So, if

**Dave Jones:** you like the video, please give it a big thumbs up. Thumbs up. It fits on the screen. There we go. And as always, uh link down to below to the EEVblog forum to discuss where people are discussing hacking this

**Dave Jones:** baby. Catch you next time.
