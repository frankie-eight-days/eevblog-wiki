---
video_id: 7OCPWCdg2ys
title: EEVblog #436 - Saleae USB Logic Analyser Review & Teardown
url: https://www.youtube.com/watch?v=7OCPWCdg2ys
source: youtube-asr
---

**Dave Jones:** Hi, it's product review time. Well, it was going to be mailbag time actually cuz I've had this one sitting in the mailbag for quite some time as you may have seen. It's from Saleae Logic. It's their eight-channel logic analyzer and

**Dave Jones:** well, I know a lot of people want to see this thing so I thought rather than just slipping into a mailbag, I'll do a full review. So, let's crack the thing open, see what it is. $150 eight-channel logic analyzer, very

**Dave Jones:** affordable and by all accounts, it's got a fairly good reputation. So, let's see if it's any good. And here's the case and isn't it a bit wanky? Look at that. Nice embossing there. They have spent a little bit on the case there.

**Dave Jones:** Well, you don't have to spend much to get that these days from China, do you? But anyway, look at this. Lovely. Nice little Well, don't think it's padded but it's one of those hard shell cases. Really quite neat zipper cases. Let's bump the

**Dave Jones:** camera there. Let's whip this thing open and jeez, where is it? It's down in there. It's tiny. Look at the size of the thing. Unbelievably tiny. We've got a little care package of connectors here, little micro grabbers as you'd

**Dave Jones:** expect. There's a little 0.1 inch header cable and a USB cable and that's it. No CD, no software. Doesn't matter. Download it. Save a disk. And check it out. It really is tiny, about 43 mm square and not very thick at

**Dave Jones:** all. You could fit that in your fob pocket, not a problem whatsoever. Well, you'd have to curl up the probes and you know, they'd be a bit pointy but gee, I don't know. It's a nice little rugged machine aluminum and

**Dave Jones:** black anodized case. Very nice. You could probably run over that thing in your car. I'm trying to give that a bit of a twist on there, but jeez, that's pretty rugged. I don't think surviving is going to be a ruggedness is going to

**Dave Jones:** be an issue for this thing. So, there's a little mini B connector. Why are they using mini B? Why don't they go micro USB? Eh, I don't know. Anyway, um look, they've got that uh machined into there, pin one on the standard 0.1 in

**Dave Jones:** header connector interface and the ground over there. So, you've got your eight channels plus ground. Count the pins, it should be nine. And I see four screws on there. Mhm, you know what we say here on the EV blog, don't turn it

**Dave Jones:** on, take it apart. Now, this has got little T5 Torx screws on there. I'm assuming that it goes into a little uh machined and tapped metal post in there. That's what I'm assuming. And I don't expect a lot of logic in this.

**Dave Jones:** In fact, I'd be surprised if it's more than like uh three chips, probably one for the USB micro for the USB interface, maybe a little logic device for the input buffer. I'm not sure how much buffering this thing

**Dave Jones:** actually does and maybe the and the input buffer chip and maybe that is uh all she wrote. It wouldn't surprise me if it's even less than that. So, let's crack this thing open. Oh, we've been mooned. Now, we go. There's the back

**Dave Jones:** ass of the board and that should just pop out. Ah, look at that. One chip plus a couple of miscellaneous and a reg. And there's the case machined aluminum as I said, anodized and the top is actually plastic. It's you know, there it is. It

**Dave Jones:** bends. It's not metal at all, but that's not a problem. You still could run over this thing in the car and the board would be fully protected. And of course, yes, uh threaded inserts there. Nice. And, of course, this thing is absolutely

**Dave Jones:** bare-bones as far as the logic analyzer it's concerned. We're just got the single uh microcontroller here, which we'll take a look at. The eight inputs, which go straight in through uh 510 ohm series resistors here. We've got some uh

**Dave Jones:** input uh diode clamping. They'd be uh low capacitive um input diode clamps. So, there is uh some input protection there for uh overloads and stuff like that. But, uh basically, there is no input uh buffer chip, uh no input uh

**Dave Jones:** latch chip. So, it goes directly into the microcontroller. And, of course, uh it's got no effectively no uh sample memory in it. It uh samples in real time on the PC. So, it's effectively got an infinite uh sample memory. It uh the

**Dave Jones:** sample rate just depends on the latency of your USB port. Um this is They claim the maximum is uh 24 megasamples per second on this thing. But, you've got to have a uh very low latency USB port to

**Dave Jones:** get that full transfer. And, well, you know, that is adequate for most uses, you know, SPI, I squared C, and other sort of, you know, serial interface stuff. But, you know, this is not a serious uh you know, a professional end

**Dave Jones:** logic analyzer, not by any means. And, by virtue of the lack of an input latch, this thing is effectively uh timing analysis only. It doesn't do state analysis mode unless one of these uh pins here can be used as an external uh

**Dave Jones:** clock input, and it can actually latch the data inside. I doubt it. So, you've got timing analysis only. But, once again, for 150 bucks, general purpose, you know, low-end logic analyzer, uh that's all you need. And, uh I don't see

**Dave Jones:** any uh pull-ups as well. There could be some uh internal to the chip, just those dodgy internal uh pull-ups on the chip. But, they also claim that uh as far as cross talk on the channels goes if you

**Dave Jones:** leave an input channel floating then it may actually pick up cross talk from the other switching driven channels. So that's a bit of a worry but you know in the end it it doesn't matter because if you know you're not using

**Dave Jones:** channels 4 5 and 6 you just switch them off in software. And the input logic thresholds on this thing are of course fixed cuz there's no external circuitry to set your logic threshold. So in this case it's only got one set of

**Dave Jones:** fixed logic thresholds there. 16 channel version by the way has two sets of logic thresholds. This one is fixed with a logic low of 0.8 volts and a logic high of anything over 2 volts. So of course that means it doesn't work on 1.8 volt

**Dave Jones:** systems. It may just by sheer luck but you know you wouldn't count on it for any serious work. So really it's only capable of being used on 2 volt 2 and 1/2 volt 3.3 and 5 volt systems. But of course that pretty much

**Dave Jones:** covers you know every major system that you're going to work on. I mean if you're working on 1.8 volt logic systems you know you're probably working on a pretty serious system and you're probably need a more serious logic

**Dave Jones:** analyzer anyway. And it looks like we have ourselves a low drop out 3.3 volt voltage regulator there. There's those input diode clamps. You can see them in standard 6 pin package there. It's got DO-46 on I'm not going to bother looking up the

**Dave Jones:** type though. It'd be a low capacitive type. You can see the input series protection resistors there. So basically it goes directly from the input pins through series resistors through the diode clamps which are diode clamp to the positive and negative

**Dave Jones:** rails. You can do those with individual diodes but it's just cheaper and easier in most cases to use these little packages. That's what they're designed for. They're cheap and popular and of course it's duplicated over here. On this side, we've got our four resistors,

**Dave Jones:** another diode clamp. We've got our uh 24 MHz uh crystal oscillator. We'll have a look at the uh uh microcontroller data sheet in a minute. It's a Cypress one, but uh that's about all she wrote. We've got ourselves a uh a polyfuse there.

**Dave Jones:** Excellent, but well, that's all you need. And you can see we're up to revision seven on the board. They've gone through quite a few revs on this uh little beast. Uh this thing's been out for a couple of years, by the way. So, I

**Dave Jones:** wouldn't have expected any uh kinks to be ironed out. And uh curiously, it looks like it's a uh four-layer board. You can see that uh dark bit in there, the extra uh layer. So, um yeah, they've gone to the effort to go four-layer um

**Dave Jones:** internal ground and power. And the microcontroller is a Cypress CY7C68013A-56. It's an 8051. Let's go to the data sheet. And here's the internal block diagram. The one we've got, of course, is the is the 56-pin SSOP uh package, as you saw. And

**Dave Jones:** it's an 8051 core operating up to 48 MHz. And well, yeah, they're going to need that because it's four uh clocks per instruction cycles. So, you've got to wonder, how are they getting that maximum sample rate of 24 MHz when the

**Dave Jones:** 8051 core is only capable of 48 MHz with uh four clocks per cycle. Cuz if you're using your GPIO down here, it, you know, you just can't do it. It's not possible. But, aha, look down here, folks. There's

**Dave Jones:** a separate 4-KB FIFO with its own data input down here. So, clearly, they must be using this FIFO. And if we dig further in the data sheet, which I haven't yet, uh we'll almost certainly find that that FIFO is capable of uh uh

**Dave Jones:** first-in, first-out buffer, by the way. So, it does have uh buffering. And um that, of course is um, what they must be using for those higher sample rates. Otherwise, there's, you know, no way in hell that the program core running at

**Dave Jones:** that can read the GPIO and update the memory and do everything else at those sort of clock rates. It it'd probably only be a few megahertz tops or something like that. So, it's got to be using that FIFO. And I think if we

**Dave Jones:** traced the board, we'd uh, probably find that uh, those logic inputs go to the FIFO buffer. And I just checked further down in the data sheet and sure enough uh, the inputs go directly to uh, port B, which is the down on the bottom side of

**Dave Jones:** the pins down here. And uh, they're actually uh, dual purpose pins. They're uh, GPIF, general purpose uh, interface pins, but they're also uh, FIFO data pins uh, zero through seven as well. So, um, it's almost certain that they're

**Dave Jones:** using the FIFO in there. But, I also found out that the general purpose um, interface actually has a selectable interface clock of up to 48 megahertz. Awesome. So, I'd have to read uh, further into the data sheet whether or

**Dave Jones:** not they actually use the GPIF and there's some sort of uh, shortcut uh, down in the FIFO. Although, it doesn't show it in this block diagram. It shows that it has to go through the address common address data bus into the RAM

**Dave Jones:** there. So, whether or not that can actually sample through the GPIF into there at uh, 48 megahertz rate independent of the uh, uh, clock frequency over here. Uh, I don't know. But, it's most likely that they're uh, using the 4K uh, FIFO there

**Dave Jones:** to uh, buffer that data. I know I would. So, one thing I'm curious to know, and I'm not sure if I'm actually going to be able to uh, uh, check this or whether or not it's obvious in the software. But, is there

**Dave Jones:** any uh, thing in the software that tells you that the latency is too high on your USB port and it's not able to get that data out at that clock rate. Is it smart enough to know that oops, I've you know,

**Dave Jones:** I've missed some data, you know, we've got a buffer overrun, and you know, all hell's breaking loose, and well, it's not working at that maximum speed because the last thing you want is data corruption or data dropping out

**Dave Jones:** through one of these USB you know, when effectively a real-time USB interface with just a little buffer in between to buffer the data because if you've got another USB device sort of you know, hogging the port or something like that,

**Dave Jones:** then you know, you don't want your data to drop out and your software not to know because that would be a cardinal sin. You don't want that to happen, which is of course the advantage of a proper logic analyzer like a real logic

**Dave Jones:** analyzer with its own internal sample buffer memory, but of course, that's a higher-end, higher price, and it's got some limitations because well, it's a limited buffer size. You can do buffer data compression and a real-time data compression into memory and stuff

**Dave Jones:** like that on some of the higher-end logic analyzers. Even the lower-end, some of the USB ones do that as well in a similar sort of price range, but this one of course has the advantage of unlimited memory assuming that you stick

**Dave Jones:** within that data throughput rate. Now of course, with the cables here, they have actually color-coded them of course, and you might think well, black goes to ground over here, but no, it doesn't. Black is follows the color code channel

**Dave Jones:** 0 you know, 1 2 3 4 blah blah blah. And they've actually labeled the ground lead there, the gray one. So that's how you're supposed to put it, not the other way around. It would have been nice if they labeled

**Dave Jones:** these ones as well with the channel numbers. And of course, we've got standard fare here on the little mini grabbers like that there, you know, par for the course. You can buy them anywhere, dime a dozen if you lose them.

**Dave Jones:** I'm standard dual sided pin like that, and you can just whack them in either side and go and probe. And by the way, one of the good things about these is that you can plug them directly into 0.1 in headers like that.

**Dave Jones:** So, by all means, if you've got room on your board and you know you're going to want to have to probe the thing, it's a common practice just to build some 0.1 in headers, add them to your board layout

**Dave Jones:** just going to various single signals you need to probe, and then you don't have to dick around with the mini grabbers like this. You know, and they you know, they fall off if you bump them, and you know, fiddly to try and get on to

**Dave Jones:** various pins directly on your chip. Much nicer if you use a 0.1 in header, and you'll find that fairly common in a lot of commercial designs. So, by all means, do it. Make sure you add a ground point

**Dave Jones:** as well. And it can be useful to whack on some power in there for some external circuitry as well, just in case. Just a little tip. I was just pushing the ground uh thing in here, and it just pushed this

**Dave Jones:** apart like this. So, yeah, folks, these aren't the best quality mini grabbers. Bummer, but they do work. But of course, that's not broken, it just slips back on there. Not a problem. I know what you're thinking. You don't get much hardware

**Dave Jones:** for your 150 bucks, do you? Well, of course not, because with a logic analyzer, one of these USB logic analyzers, it's all about the software, folks, and that's what you're paying for, good software. So, let's put this thing back together, hook it up, try it

**Dave Jones:** out. All right, we're on the website, and let's download it. And look, it's got everything. It's got XP, Vista, and Windows 7 32-bit, and Vista and 7 64-bit support. It's got Mac OS S, OS X if you're into that sort of thing,

**Dave Jones:** Leopard, Leopard Plus, Tiger, I don't know. I'm not a Mac person. And it also supports Linux as well for you penguin fans out there, 32-bit and 64-bit. Let's download it. I'm going to use the Windows 7 version. And I won't bore you too much with the

**Dave Jones:** details of the installation, but let's see if it works. And is it quick? I don't know. Status bar, nothing. Come on. And it asks you to install their serial bus controller as well. Looks like they've got their own driver for this

**Dave Jones:** thing. So, yep, not a problem. I'm not going to always trust them. Launch the software. We're done, folks. And bingo. Oh, we're in. Too easy. Look at that. And of course, if we have a look up here, it's disconnected because

**Dave Jones:** we haven't plugged it in yet. So, presumably, let me try that. And installing device driver software. A logic device was found, but there was a problem connecting to it. Another application may be using it. Looks like I've got to shut it down.

**Dave Jones:** Oops. Well, that was absolutely no dramas whatsoever. It just installed, didn't even tell me in the background, and bang, it's we're straight in, and there it is up the top, connected. Looks There's options menu over here, which you can't see them all. Maybe if I

**Dave Jones:** can I can't drag my uh uh capture window, but yeah, we've got preferences, display in ASCII. Oh, there we go. They pop up over here. So, save screenshots, save screen region, display in ASCII, binary, decimal, hexadecimal, user's guide, and give feedback and

**Dave Jones:** report issues. This is the latest version. Let's have a look at the preferences. Uh pre-trigger buffer size. Okay, excellent. That's what you want. You want some pre-trigger data as well. Um 10 meg samples. Only 10 million samples, folks. If you're used to logic

**Dave Jones:** analyzers with building memory, then well, 10 million is an absolute luxury. Enable longer captures up to one terra samples. Geez, that'll depend on data compression, I guess as well because it would I presume it would do some data compression before it

**Dave Jones:** writes it to disk. And check for updates, animate zoning and zooming view state after new capture. What do we got here? Enable single click zoom, aesthetics. Ooh, use arrow glass style. Yes no. There we go. Look at that. That looks a

**Dave Jones:** bit better. Yeah, I didn't like the other one. It was a bit wonky. So, just when you thought this thing didn't have many options and preferences and you know, you're probably asking, "Oh, where do you set up all your serial data SPI?"

**Dave Jones:** Well, you've just noticed this analyzer down here. Look at this. Plus, here it is. CAN bus DMX 512. Brilliant. You don't get that very often. I squared C, I 2 S for you audio freaks out there. PCM stuff, the I 2 S audio. Standard

**Dave Jones:** Manchester one wire bus for all you people working on one wire, you know, Maxim Dallas one wire and other one wire stuff. Async serial, simple parallel, SPI, Uni IO. All your basics are covered there with a few bonus extras. Although,

**Dave Jones:** there is one that's missing there and that's JTAG, of course. But JTAG usually quite high speed. Might have been out of the realm of something like this. But I I guess it would have been nice to have JTAG in there because a lot of logic

**Dave Jones:** analyzers will actually, you know, won't have JTAG. Even high-end ones won't have JTAG option. And as far as measurements go, we got width, period, duty cycle, frequency, show the byte, show timing markers, and show errors as well. Well,

**Dave Jones:** only one thing left to do. Feed some data into this sucker and see what it does. Now, of course, I always like to uh try and use these things without reading the manual at all cuz that's a true test of, you know, is this thing uh

**Dave Jones:** user-friendly or not? Now, if you can from familiar with logic analyzers in general or some other bit of test gear, turn it on. Uh can I use it? Is it intuitive? Well, up here we've got one we've got our number of samples here.

**Dave Jones:** We've got our sample rate and start. And I've hooked up an I²C bus to it and I can just hit start here and occasionally I'll get blank data cuz it is uh packet-based. Um there we go. I get it a few times, blank

**Dave Jones:** data, and then occasionally I will capture the data. That's because um no trigger is uh set up at all. And that's the first thing I noticed, well, where's the trigger capability on this thing? Like, how can I, you know, trigger on a data packet or

**Dave Jones:** something like that? And um you know, we've got some analyzers down here. Let's go I²C analyzer settings. We can set it up. There we go. It's all It looks like it has it automatically detected. No, of course, the uh clock is

**Dave Jones:** uh channel zero up there, so we need to set that and data is channel one, so it hasn't automatically detected that. Address display, 8-bit read write. I'm doing 8-bit read write, so let's save that. And uh it automatically labels

**Dave Jones:** them. Nice. That's another thing I was going to uh check. Rename them. Yep, beautiful. SCL SDA. There it is. Ooh, nice. There we go. And it's put the decoded data in there. Beautiful. It's Look at that. It's got the acknowledge

**Dave Jones:** in there and everything else. Nice. I like it. We're off to a good start, but um I still don't know where the trigger is cuz we're just reading random data there, and we'd find it if we sample in. Hello. Come on. Where's my

**Dave Jones:** data? There we go. It eventually got a packet. And just scrolling around the data here, if I use the uh mouse wheel to scroll in and out, then that is zooms and expands the data. That's exactly what I'd

**Dave Jones:** expect. Excellent. And then uh left button. Oh, I just hold it down and it automatically sort of, you know, drags. It looks like it's got some sort of, you know, some sort of buffering action on that pan stuff, but I just uh grab the

**Dave Jones:** left button and drag that left and right, and that sort of works. So, let's go out like that, and there you go. You can see my uh multiple data packets there. And there it is. We actually need more

**Dave Jones:** samples than that. This is where the huge number of samples comes in as an advantage, folks. Let's go up to 10 meg samples, for example. Takes a while, but look at all those packets we can capture. Brilliant. Now, usually to get

**Dave Jones:** that, you either need a logic analyzer with a 10 meg sample buffer or um and or one with that data compression. That uh actually compresses the data real time so that it doesn't, during all these uh dead periods, I one of those logic

**Dave Jones:** analyzers with data compression won't waste up, you know, millions of samples um storing just all one there. It'll go one during that time period, and it only needs to store a couple of bytes. So, um that's the advantage of those ones with

**Dave Jones:** data compression. This one, eh, because it's real time uh USB, uh it it doesn't need any of that uh data compression. It doesn't store it on the device itself, but uh as you can see, we've captured a whole bunch of

**Dave Jones:** I squared C packets. Nice. And if we have a look down here, we can actually open up uh new tabs as well as um go in to existing ones. It looks like it's got the ninth tab there, and then

**Dave Jones:** we can copy various uh stuff to the capture tab. Uh not sure what that's doing, but it looks pretty flexible. One thing I just noticed in that um it these data labels here haven't copied over to these tabs

**Dave Jones:** over here. Now, I'm not sure if that's a uh um uh you know, and you can change the label on that, too, by the looks of it. I'm not sure if uh that's a feature for some reason or whether or not it's a uh

**Dave Jones:** small bug. Now, it looks like I found the trigger here. There's actually for this By the way, for the channel here, they've actually got You can show and hide the various channels. You can move them up and down as well. Um you can't

**Dave Jones:** actually drag them, which, you know, I would have expected to be able to grab that and just drag it around. Um but, yeah, you can actually move it uh manually. I guess it's not too much of a drama. You only have to do that once,

**Dave Jones:** really, when you're setting up your uh logic analyzer for to, you know, to look and do exactly what you want. But, um in terms of like we can reset trigger here, but look, we've only got um requires uh rising edge uh transition,

**Dave Jones:** and requires a logic one to be present when rising, and that's basically um it. It doesn't look like at the moment, anyway, I haven't found it that you can set up like a data packet trigger or anything like that. Um

**Dave Jones:** Now, one thing I really like are these uh auto cursors. As you can see, when I actually go in there, you can see that uh uh little timing cursor change. You can see the data. Look, there's no data

**Dave Jones:** at the moment cuz I haven't actually uh moved my cursor over something. I don't even have to click on that, and it shows me the uh width, the period, the frequency, and the uh byte as well. Very, very nice. I like that. Now, I

**Dave Jones:** know it's uh grossly unfair to uh compare it to my Agilent uh InfiniiVision mixed signal scope here, but that's what I've got it doing. I've got the uh scope actually generating um one of these uh training signals uh demo

**Dave Jones:** signals down here for the uh I squared C bus. And of course it's got uh you know, real-time decoding and hardware-based uh decoding as well. So, this you know, this is a a pretty uh good logic analyzer in that uh respect. Now, as you

**Dave Jones:** can see, there's actually some uh data changing inside this thing as well as a bit of uh timing jitter as well going back and forth and that's obviously uh deliberate and you can see all the data packets in there and they do change like

**Dave Jones:** that in uh in time period. And we're of course triggering off a reference to uh one packet here. And uh of course, that's what we're not doing at the moment with the uh Saleae uh logic unit, we're just, you know, um

**Dave Jones:** free triggering and just capturing whatever we get. Whereas, you know, we want to actually be able to set a trigger point like that. I mean, any good logic analyzer should be able to set a trigger point for the data. So, in

**Dave Jones:** effect, if we set a uh trigger point and we can't see the data changing like, for example, we're going here, you can see that the data's actually uh counting up, you know, 2 4 6 8 2 4 6 uh or 20 40 60

**Dave Jones:** 80 uh stuff like that. So, if we can't capture that on the uh Saleae logic, then well, it's, you know, not nearly as useful as a uh real logic a real hardware-based uh logic analyzer like this one. And of course, the other thing

**Dave Jones:** I like is the uh decoding of the I squared C uh bus itself. Look, it tells you exactly what's going on there. It's uh setting up a write to address 226 with an acknowledge and then the data byte is uh 16 with acknowledge. So, you

**Dave Jones:** know, it's uh it's doing the business there. I really like that. But to actually um check that this is uh accurate, I'm assuming it is, otherwise people would have reported uh issues and stuff like that and if there were any,

**Dave Jones:** they would have been fixed. But for me to actually check that here, I need to ensure that that packet I'm looking at is exactly the same packet that I'm getting on my Agilent scope. And uh unless I can trigger on exactly the same

**Dave Jones:** uh packet, I'd have to go through and look at every one of them. Well, I did relent and uh read the user's guide. Um it's not uh massive, but it is uh well written. And well, no, folks, um triggering is all you see

**Dave Jones:** there. Um just uh you know, basic positive or negative edge um triggering with data high or low, and that's it. Um there's no ability to uh trigger off a packet in uh real time. And that's rather disappointing. I don't know

**Dave Jones:** whether or not that's a a horsepower issue to do with the PC to be able to process that data in real time. I wouldn't have thought so, especially um you know, add the capability at some lower sample rates. Maybe you can't do

**Dave Jones:** it at 24 MHz or something, but gee, I don't know. PCs are pretty powerful these days. I would have expected um so I'm quite disappointed that is no um trigger on uh data and stuff like that or or trigger on an I squared C

**Dave Jones:** error, for example, so you can sit the you know, have it sitting there um just sampling away, sampling away. So, if you've got a data error on uh the bus you're trying to decode, and well, you know, you want to just um capture it

**Dave Jones:** capture the data and just have it sitting there in the background. And this data only occurs, you know, once every hour. You want it just to sit there and wait for that uh trigger event. You know, look, I got an error on

**Dave Jones:** my I squared um C bus, and boom, it'll, you know, capture the thing. But um it it really is a very bare-bones interface. I do like it. It's nice, and the uh decoding is nice, but in terms of

**Dave Jones:** uh triggering and data uh analysis and um stuff like that, it, you know, it just doesn't really uh compare. So, yeah, I mean, you're paying a a a bargain basement uh price for a logic analyzer and you're getting quite

**Dave Jones:** usable software for the price, but yeah, don't expect uh um you know, professional league uh triggering performance and stuff like that. Look, I can't even Look, there's no way that I can even search. Like, where's the search capability for uh actually

**Dave Jones:** finding this data, right? Confirm, restore. If I go over to I²C, I can export the data, save as text CSV. That's great. Okay, and that but you know, how can I find data? Let's say I want to find something where address,

**Dave Jones:** you know, 222 popped up popped up or something. How do I do that? You can't, by the looks of it. And by the looks of it, I can't even like uh real-time update this display. So, let's say that I wanted to you know,

**Dave Jones:** trigger off the uh you know, rising edge here. And by the way, I can't even trigger off like a uh time period. Like, oh, it's been high. Like, I can't even say, oh, it's been Okay, it's been high

**Dave Jones:** for, you know, X milliseconds or whatever, and then trigger on the first uh point after that. Can't even do that. Um you know, we uh often call that pulse width uh triggering. It just doesn't have that capability. But

**Dave Jones:** anyway, I would like a uh you know, I can I can capture the data, single shot capture, but where's like the free running mode where I can just, you know, do that because then I'd be able to see

**Dave Jones:** if I was able to trigger off, for example, that um pulse width Why does that spring back? That's really rather annoying. How that swings back and it's automatically swings back. Sometimes it does it, sometimes it doesn't. Don't know what's going on

**Dave Jones:** there. It could be a PEBKAC error, I don't know. But uh yeah, like if I was able to trigger off that first edge there after a time period, then I'd be able to just sit there watching this data packet refresh, refresh, refresh,

**Dave Jones:** but there doesn't seem to be a capability to um um that um auto uh sampling and auto triggering. Bummer. One good thing I like is it does seem to have fairly extensive uh data export uh functioning. You can um select which

**Dave Jones:** channels you want to export um between specified uh times. You don't have to export the whole lot. Uh binary, uh CSV, and VCD. I don't know what VCD is off the top of my head, but uh there you go. It um has all these different

**Dave Jones:** formats and then you can uh for the um CSV stuff, you can uh do comma delimited, tab delimited, all that sort of stuff. Really quite flexible. I like it. So, if you want to analyze your data in another package,

**Dave Jones:** looks like it's going to do the business. And another good thing, it looks like you can have multiple uh buses and uh decoding on at the same time. Like I'm trying to set up a uh asynchronous serial one uh say RS-232 one at the

**Dave Jones:** moment. And uh of course, it um it still has the I squared C there and it automatically like if you go in here, set it up, it tells you that uh these two are already in use by the I squared

**Dave Jones:** C. So, looks like you can do multiple ones. Well, as you'd expect because uh really it's only just, you know, decoding this stuff in software after the fact. So, really it should be able to do anything if you can capture, you

**Dave Jones:** know, so really you could uh with eight channels, you could capture uh four separate SPI, uh four separate I squared C buses, or uh asynchronous serial buses at the same time. Beautiful. But, one annoying thing is I was on this

**Dave Jones:** tab here and I changed my uh labels and channels up here, but that only applied to that tab. So, uh when I go back over here to this tab, they're they haven't changed. I don't know. Is this a feature or not?

**Dave Jones:** Well, I'm looking at my uh RS-232 signal here, RX and TX, and it looks exactly like what I'm getting on my uh Agilent scope there. It looks so faithful, but it's telling me there's a framing errors in there. So, I've got this set to auto

**Dave Jones:** baud rate detection. So, maybe I maybe that's not working uh very well and I need to select a fixed baud rate. Let me try that. Aha, it had detected that the auto baud rate was 20,833. It's actually 19.2. So, let's save that

**Dave Jones:** and try again. Here we go. Start. Boom. No, we've still got framing errors. Now, if we have a look at the data down here, we can zoom out on the scope as well. And you can see that's look at this last transmit

**Dave Jones:** packet here. And you can see that the data is completely faithful. No problems at all there, but of course the data is incorrect. We're expecting 23 hex here and 31 hex. And we're just not getting that. So, yeah,

**Dave Jones:** it captures it fine, but decoding not for some reason. I don't know. And I'm just doing a quick SPI bus analysis and capture here. And seems to be working just fine. Matches the Agilent. Not a problem. It's just counting down.

**Dave Jones:** I'm just doing the output line here. I'm just capturing that. There's our clock signal up the top. There's our SPI enable. And there's our data. And this particular example I'm using is just counting down. And sure enough, it does

**Dave Jones:** count down. It's not counting down by one by the way. So, that the data is correct. So, not a problem. Actually, I think this tab-based business, I don't think that's a bug. I think it's specifically set up so that

**Dave Jones:** you can specifically save and capture that particular data that you were working on at that time. So, that's why it doesn't auto change the labels and stuff when you go between them. So, I take back what I said about that. I

**Dave Jones:** think it's fine. So, the verdict on the Saleae Logic8 USB logic analyzer, $150 or thereabouts, well, it's pretty darn basic as you saw. Um I was actually quite disappointed in the software. And if you want to check it out for yourself, you can just

**Dave Jones:** download the software freely from the website, of course, and but it's very bare-bones. Um it's it's nice. I like the way it operated, but jeez, you know, there's no, as you saw, that I could find anyway, I stand to be

**Dave Jones:** corrected, no serial data triggering capability, no free running mode. It just, well, you know, jeez, I expected more. This thing's been out for quite a few years, actually. So, I expected them to keep adding features to the logic analyzer software, but I

**Dave Jones:** don't know what it was like a couple of years back when they first released it, but it's pretty darn basic. And I'm pretty disappointed. I expected more from that. So, really, for 150 bucks, I don't know how it compares with the other USB logic

**Dave Jones:** analyzers out there. I haven't looked at them all, so I don't know. You're going to have to weigh it up yourself, but it's got to get a some thumbs sideways at best, really. I don't mind it. The hardware's nice and rugged. Um

**Dave Jones:** the software seemed to work quite well for what it did, but very, very basic. And by the way, the 16-channel version of this, double the price, the Logic16, you get faster speed on it, 100 MHz for two channels, and then it drops for

**Dave Jones:** extra channels after that. So, there's some extra hardware in there to do that, but the software is the same. So, you pay that extra money, and well, you just get very basic software. It's okay for just, you know, general use, really. If

**Dave Jones:** you just want to muck around and capture your SPI or I squared C buses, stuff like that, low speed stuff, eh, it's okay value for 150 bucks, but just wish they'd add more features. Anyway, if you like the review, please

**Dave Jones:** give it a big thumbs up. If you want to discuss it, jump on over to the EEVblog forum. Catch you next time.
