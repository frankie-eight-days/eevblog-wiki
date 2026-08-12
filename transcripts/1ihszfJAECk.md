---
video_id: 1ihszfJAECk
title: EEVblog #269 - Energy Micro Tiny Gecko
url: https://www.youtube.com/watch?v=1ihszfJAECk
source: youtube-asr
---

**Dave Jones:** Hi, there was some people who wanted me to take a closer look at the Energy Micro Tiny Gecko board. Power it up, hook it up, do some measurements. Sounds like a good idea. Let's go. Now, there were a few people who

**Dave Jones:** commented on the mark on the LCD here. It's not a mark at all. It's just the Tada! The uh plastic film protecting the display. Now, let's actually power the thing up and see what happens. Woohoo! Get latest software from

**Dave Jones:** energymicro.com. Not too keen on the uh segmented display here. Oh, it's got a nice little um fancy uh target display there, custom display. And it's jump straight into what looks like the uh cap sense slider thing. So, let's play around with that.

**Dave Jones:** Whoa, yeah, it does work. Let's touch it over here. And you'll notice that that dash disappears and then it's giving you a count, which is presumably the count position on the slider. And if I slide my finger along there, not only does that

**Dave Jones:** bar graph rotational bar graph go up, but uh cap sense touch also goes along and scrolls the text. Cap sense demo. It's a little bit touchy, pardon the pun, but uh you can see that works a treat. And if you push the

**Dave Jones:** button here, you end up in a slider thing which actually Well, it slides the segments along the display like that instead of scrolling the text. And uh if you do it again, it's got uh looks like a pad zero, I

**Dave Jones:** assume refers to that pad. And you can see the value change. And if I touch these pads over here, it doesn't really change at all. And I can swap between pad one. If I touch pad one there, the

**Dave Jones:** value changes. If I touch pad zero, doesn't really change that much. So, there you go. It looks like it comes up pre-loaded with uh uh only a cap sense demo. Could have something else, but I can't find it. There's one thing I

**Dave Jones:** didn't see in the original look at this was this LC sensor here. It's a little inductor and it can detect nearby magnetic fields. And but don't get too excited. You're not going to be able to take this thing out and find Lassiter's

**Dave Jones:** reef or anything like that. It's only got a detection range of a couple of millimeters, I believe. And I did complain that there wasn't a gecko on the board and sure enough previous versions of the board have had a gecko,

**Dave Jones:** but the one I've got they've taken it off. But on the chip there, you can see cute little gecko laser etched onto the chip. I love it. And this switch down here turns it off and on from the

**Dave Jones:** battery power, but let's hook it up to the USB and see what we get. Tada! Ping! And it powers it alternatively from the USB and we've got our uh Seger J-Link debugger LEDs going there. So, let's give the software a

**Dave Jones:** try. And the only documentation you get in the box is this quick start guide which says go to energymicro.com/simplicity. Well, let's give it a try. And bingo! You type in energymicro.com/simplicity and you get this page a step-by-step procedure to run the software. Looks

**Dave Jones:** pretty easy. Let's give it a try. And here it is Simplicity Studio free download and it it appears that they've got different demo boards. This is the tiny gecko, but they have other ones with large RGB type displays on them. And looks

**Dave Jones:** like the software would support all of those. So, let's download it and there's a whole bunch of demo programs. Beautiful. Let's give it a try. And I won't bore you with the entire download process. It was a 7 meg

**Dave Jones:** download, very reasonable size and it popped up with this, "The following recommended packages are not installed. Do you wish to install them?" Ah. Eh, better. On second thought, screw that. It's taking too long, so I'm going to cancel that, and I'll see what

**Dave Jones:** happens when I plug in the board. And it looks like you have to install everything, so don't just do what I did and cancel it. Make sure you install all the options. And here we go, we get the

**Dave Jones:** energy aware stuff because this Tiny Gecko board actually has any energy measurement built in. It's effectively got like a little microcurrent built into it. It can It has two different ranges that can actually record the CPU measure and transmit back

**Dave Jones:** and graph the CPU current for various ranges and power cycle. So, we'll give that a try, and we've got app notes, we've got examples, kit documentation, demos, videos, all sorts of things. Looks pretty good. Here's all the uh

**Dave Jones:** documentation. So, let's take a look at And there's not much on the data sheet, but it does tell you here it has 0.1 microamps or 100 nanoamps to 50 amps measurement range of the measures the voltage and the current of the VMCU

**Dave Jones:** rail, so that measuring voltage and current allows you to calculate how much power because the thing with measuring and characterizing and comparing the power consumption of different microcontrollers is just that you have to do power. You can't necessarily go on

**Dave Jones:** just the current figures because it's dependent upon the supply voltage. Let's take a look at the user manual here. It's 41 pages, seems fairly comprehensive. And if we take a look at the block diagram, there's the segmented display. Look at the tiny little gecko.

**Dave Jones:** They've got a gecko symbol on the display. Haven't figured out how to get that one up yet, but that's nice. It's got a little battery bar graph end uh the various circular things plus the segmented display as well and like a

**Dave Jones:** timer display up here too and there's milliamps, microamps. So maybe if we run some of the power demo apps it'll actually tell us how much power is being consumed. That'd be really nice and there's the rest of the block diagram

**Dave Jones:** the touch slider, a couple of push buttons, the ambient light sensor, the LC sensor as I mentioned uh and some debug stuff and the optional op-amp and that's about it. But what I'm really interested with this thing is the power

**Dave Jones:** management capabilities. And if we click on the demos button here, what do we get? We get a whole bunch of demos and there's a here we go a demo of different energy modes. Let's have a look at that.

**Dave Jones:** So here it is they got the instructions here. It basically you just cut and paste this example code here a tiny amount. You just put it in your main uh thing call up this function once by the looks of it at the start and it looks

**Dave Jones:** like it gives you the the energy profile of the different functions. Look at that main is taking 98% of the power I'm assuming. Yep, energy in microjoules. There it is and that's brilliant. And presumably if you got a big complex app,

**Dave Jones:** you can see which functions are taking the most amount of power. I'm really liking this because doing this sort of stuff with a regular microcontroller which doesn't have the building support for doing something like this would is usually very difficult and ad hoc.

**Dave Jones:** You've got to know how much instruction time is spent in each subroutine and function and then try and measure your battery consumption. But here you can actually do it directly on the demo board. It looks pretty trivial. Wow, this is powerful. And what I did is

**Dave Jones:** I clicked on the main function and this looks like the demo program it's running e-mode.c and you can see the code in here and it's drawing down the bottom here 5.92 milliamps at 3.3 volts but I don't uh

**Dave Jones:** off hand here I don't know what frequency that's running at or what it's actually doing at the moment but you can actually looks like you can go in and you can debug your code directly in this energy aware profiler window. And if you

**Dave Jones:** go into the energy aware battery thing here it gives you a tool which allows you to estimate the battery life of your program. I'm running a demo here and it's a see you can choose your cell alkaline double A triple A or your

**Dave Jones:** CR2032s for example lithium cells number in parallel number in series and uh it can apparently give you a profile boom of there's the battery curve like that and it can show you the minimum where you set your minimum operating

**Dave Jones:** voltage at presumably you can change that figure average current might be 2.8 microamps here estimated system operating time 8 years there you go the rated capacity is on that's a CR2032 cell 8 years at 2.8 microamps that's rather neat you'd have to like you can

**Dave Jones:** actually load in presumably load in your actual program and it will actually estimate it based on your real application. I'm just running one of the simulation demos here but this looks really neat. They've really put a lot of

**Dave Jones:** effort into energy management on these Gecko microcontrollers it seems to what they're actually um them apart so I like this. Man, this is neat. I think I might this is kind of swaying me towards using an energy micro

**Dave Jones:** device in my MicroWatch Mark II, I think. Just because the tools are neat. And if we go into the Energy Aware Designer program here, this allows you to generate C code the initialization C code for various packages and various

**Dave Jones:** peripherals and things like that. So, you go up here, you choose your device from all those and all the different types of packages, and then we can enable things like enable our real-time clock. Bang. You want to do that? We want some

**Dave Jones:** ADCs. Yep, we've got looks like four to choose from in this particular package. Let's enable, you know, four channels of those. And oh, yeah, I squared C. I want one of those. And looks like you can get three different

**Dave Jones:** pin locations for the Yeah, there we go. You can select which pins you want. Oh, neat. I like that. And oh, actually it tells you it conflicts. I'm assuming the red means that they've conflicted with something else. Mhm.

**Dave Jones:** Ah, excellent. All right. I like that. Otherwise, it's put them up here. And we enable that and you can do that with any of the internal peripherals. We've got the timer, the interrupts, and stuff like that. And you

**Dave Jones:** can generate PDF reports for this sort of thing. We can do the We can show pin matrix views. There we go. That's a matrix kind of view. Once again, we can save the PDF for that. It's got a button down here,

**Dave Jones:** but let's get out of that and let's generate our C code. Bingo. There it is. We've got our C code for initializing this particular device. Looks like it's set up as 14 MHz high frequency clock, GPIO, there's a

**Dave Jones:** um, the PIOs open drain with pull up and filter and all that's and there's the ADC, the I squared C. All your initialized code is there for you. I've got to say that is one of the better uh,

**Dave Jones:** configuration tools I've seen from uh, any vendor. That's very nice cuz a lot a lot of the pain involved with uh, microcontrollers is just getting the damn things up and running and uh, getting the modules enabled cuz you first write your program

**Dave Jones:** and then, you know, it doesn't work first go and you're scratching your head wondering why cuz you haven't enabled some pin or uh, some register or something like that. This just allows you to do it in a nice graphical user

**Dave Jones:** interface and make sure you've got it right. Neat. And let's try out the energy aware commander option which apparently allows you to download uh, firmware and do stuff like that. So, let's connect. It's we're connected to our tiny gecko uh,

**Dave Jones:** starter kit. Uh, we're in we can go to uh, various uh, debug modes, USB address, the chip type we've got on the board there, the chip revision. So, it's read the uh, silicon ID code out of that. We can flash in uh,

**Dave Jones:** there we go. We can flash in uh, various stuff. So, that's like a little uh, programmer. Is it? That's almost like a stand alone programmer option, I think. So, let's go look in the demos. There we go. We can download

**Dave Jones:** the demos. Blink the LED. Woohoo! Try different energy energy mode demo using the LCD. Let's try that. Start.

**Dave Jones:** And it resets and that's pretty quick and yep, we've got something on our LCD. When you press the reset button here, you can see that it's uh, in 32 MHz mode and you can actually cycle through different modes, 32 kHz

**Dave Jones:** crystal, and when you do that, that will plus the RTC, the real-time clock. So, you've got all these different modes that you can measure, and in the background, you'll be able to see the graph changing. So, let's give that a try. So, let's take a

**Dave Jones:** look at that. You can see it's drawing 5.92 milliamps now because it's in the 32 MHz mode. So, that's what it's drawing at 32 MHz. 5. Almost 6 milliamps at 3.3 volts, but if we change that mode, we can see it. Let's go to 32 kHz and

**Dave Jones:** see what happens there. And bang, it's dropped. And you can see all the different functions down here where it's taking the power consumption for this application. All right, this is really cool. Check this out. I'll switch it to

**Dave Jones:** 32 kHz mode. There it is. And you should find the current consumption bang, drops all the way down to 1 microamp because we've got that logarithmic scale there. And if I choose the RTC plus LCD option here, there it is, it'll leave the LCD

**Dave Jones:** on, and there we go. It takes about oh, I don't know, 6 7 microamps or something like that to drive that segmented LCD plus the plus to have the 32 kHz real-time crystal uh working at the same time. The touch

**Dave Jones:** slider doesn't seem to be active there at all, but uh there you go. That's how much energy's required. Oh, you can see if I press the button, da da da, there we go. You can see just the slight increase in

**Dave Jones:** energy consumption, and you need to to that into account in your designs. If you've got a low value pull-up resistor on your switch and the user's pressing that, it's taking a little gulp of current every time you actually do that.

**Dave Jones:** So, um you really have to optimize the value of your pull-up resistors on those user switches. And if we go and take a look at the application notes here, they're fairly comprehensive. Like there's uh fat on an SD card, Ethernet, all the good stuff,

**Dave Jones:** AES cipher modes, and uh all sorts of things. There's low energy UARTs. I like it, but let's go in and actually see. And here's a list of the five different energy modes we saw in the example uh demo that we were just

**Dave Jones:** running. So, mode zero is where the CPU is running flat chat and it's just uh you know, everything's chewing as much power as possible. And then there's sleep mode, energy mode one, where basically the CPU is disabled, but uh

**Dave Jones:** and any of the any of the peripherals using the Here we go. Wait for the peripheral reflex system, PRS, woohoo, and the DMA. Um it can actually do autonomous operations without powering up the CPU. For example, the timer may

**Dave Jones:** repeatedly trigger an ADC conversion at a given instance. When the conversion is complete, the results move to DMA to RAM. And when a given number of conversions have been performed, the DMA then wakes up the CPU using an

**Dave Jones:** interrupt. So, you can basically uh data log, by the sounds of it, data log uh things from the ADC without using and powering up the CPU at all. Brilliant. Um and then there's deep sleep. And energy mode two means that there's no

**Dave Jones:** high frequency clocks running at all, only like uh the low power 32 kHz clock for doing I squared C stuff, LCD uh operations, UART operations, analog comparators, real-time clocks, and some basic GPIO uh checking. And mode three is the stop mode, and uh that uh differs

**Dave Jones:** from sleep mode in that uh no oscillator, apart from the watchdog, is actually running at all, even the low-frequency uh one. So, in even in this mode, you can still do an I²C uh address check, watchdog of course, um

**Dave Jones:** you can do uh pin interrupts, analog comparators, and GPIO interrupts without uh any internal clock running. And energy mode number four is complete shutoff mode, where it can draw, so they claim as little as 20 nanoamps. And the

**Dave Jones:** only way to uh exit that mode and get back to operation is to uh reset the is to trigger the reset line or uh cycle the power. But, this claim of 20 nanoamps, I think we might be able to

**Dave Jones:** check that. Hmm. Now, as a bit of a uh industry comparison here, I've got it uh running in the LCD plus um RTC mode. So, um trust me, the LCD is actually uh displaying something here, and it's running the real-time clock as well. And

**Dave Jones:** as you can see, it's drawing around about 5 microamps or something like that, cuz remember this is a logarithmic um uh Y axis here. But, if we compare that 5 microamps running with, say, a uh Microchip uh PIC32MX

**Dave Jones:** um series micro, so I'm comparing an 1 32-bit micro to another, not quite um apples-to-apples, but, you know, reasonably close. In the uh low-power RC mode at 32 kHz, it's going to be drawing roughly um 100 microamps typical at 3.3

**Dave Jones:** V. So, this thing's uh driving an LCD as well as running the uh real-time clock, but I guess the process is not continuously running at 32 kHz here, but you get the idea of uh of what you can

**Dave Jones:** actually uh do with just, you know, 10 microamps or something like that. There's hardly anything uh being used there at all. Sniff of an oily rag. And of course, if you put the uh demo in energy mode uh two, which uh claims on

**Dave Jones:** the LCD that it's uh 32 kHz, so I presume uh the processor's running at 32 kHz. It may not be running continuously, but as you can see, it draws um under 1 microamp. Amazing. And if we use uh

**Dave Jones:** energy mode two with the real-time clock turned on, you can see it's now just a smidgen on or smidgen over 1 microamp. And again, if we choose the PIC32 uh MX series micro as an industry comparison for an equivalent uh 32-bit micro with

**Dave Jones:** the um real-time clock plus the uh timer one with the 32 kHz crystal, there we go. 23 microamps typical, 50 microamps max. So, the energy micro um using its uh um ARM Cortex uh M3 plus all its uh

**Dave Jones:** energy management uh capability, low-power stuff, it draws a 1/23 of that, only 1 microamp. And I've put the board into energy mode four, which is complete shutdown mode. And as you can see, we're down in the noise, under 100

**Dave Jones:** nanoamps there. It's not really accurate down here. It might be say 10 nanoamps average, but really it's not accurate at all. So, let's see if we can get some more accurate measurements of that. And if you read the user manual here, it

**Dave Jones:** actually tells you what it's capable of measuring. Here it is, from 0.1 microamps to 50 milliamps. And does that in uh two different uh ranges. And uh it can go down to 100 nanoamps resolution, but resolution's different to accuracy.

**Dave Jones:** But the built-in uh power measurement uh capability, you know, it's probably good enough for uh most applications, but I think we'll just uh double-check that and uh see if we can measure it ourselves. And if we take a look at the

**Dave Jones:** the here and see how it's doing the MCU power uh current sense. This is the circuit it's using a linear technologies LTC6102 zero drift precision current sense IC. In fact, it's got two of them for one for range one and one for range two as

**Dave Jones:** well. And it's it's not a bad device at all and it's a current sense amplifier. And if we take a look up here, we've got an LP3982. That's a low drop out voltage regulator for the for the supply for the CPU and 5 volts

**Dave Jones:** in 3.3 volts out. And there's our current shunt resistor the 4R7 there. And of course, it taps off those two values down into the current sense amplifier down here for both ranges. And then the output is switched in here. There's our coin cell battery

**Dave Jones:** and our output there goes to our VMCU in there. So that goes to the to a specific pin which goes on to the microcontroller which is just for the MCU core. So we can measure the power consumption of that. And by looking at

**Dave Jones:** this, this is some sort of connector or some sort of test pad. If we look at R704 here zero ohm resistor, we should be able to get in there and use that. If we take desolder that resistor, we

**Dave Jones:** should be able to break into that with my micro current adapter and actually measure the current taken by the MCU pin. Let's give it a go. And if we take a look at our board here, we can see our 4.7 ohm current shunt

**Dave Jones:** resistor there with the two resistors going off into the two current shunt amplifier chips. And here's our ST700 connector down here. And that's our 704. So if we desolder that sucker, we should be able to get in there and measure the current

**Dave Jones:** consumption really nicely using this header connector. I love it. And bingo, we now have a current shunt in there. We can just take that out and we can measure our microcontroller power consumption. They were thinking when they designed this because it's energy

**Dave Jones:** micron, they want you to be able to um measure the energy that this micro is using. Go figure. And what I've got here now is my micro current on the uh milliamp range at the moment hooked in. Jump it into that um

**Dave Jones:** uh current shunt and shunt uh header uh connector up there and I've got the output connected to the fluke on millivolt range. So, 1 uh millivolt equals 1 milliamp. So, it's drawing 4.8 milliamps at the moment and that's in

**Dave Jones:** its default uh 32 MHz uh mode. So, if we let that go down, it's 2.8, switches off, bang, it goes into the mode. So, we can measure the different modes now by just cycling through and selecting the mode we want. Let's go to that 32K

**Dave Jones:** range mode. Go down there and uh let's measure the consumption of that. We're only talking There it is, that 1 microamp. But, of course, we can get much better resolution on that this by switching to our nanoamp range down here and then

**Dave Jones:** taking it up and bingo, there we go, 990 odd milliamps. It's jumping around. We could smooth that out if we wanted to, but it's drawing around that 1 microamp figure. Now, of course, the big question is what happens in that um

**Dave Jones:** uh power mode four where it's completely shut down? Well, we'll find out in a second.

**Dave Jones:** Bingo, it's dropped down to nothing. Let's switch this down to our nanoamp range and uh 1 millivolt, it's drawing not That's a bit disappointing. It's drawing 100 Oh, no, it's going down. There we go. So, obviously something has charged

**Dave Jones:** up there and uh it's got to go down. So, I might wait a bit and see what that gets down to. And there you go. When we power it from the USB input like this, it actually enables the

**Dave Jones:** some of the energy management stuff and some of the analog switches and things. So, you really need to power it from the USB to get that capability. And there we go. It's about 165 or 160 odd nanoamps power consumption. Energy Microchip

**Dave Jones:** around 20 nanoamps in energy mode for that complete shutdown mode. So, I decided to have a look at the schematic again and see what is on that VMCU pin. And it turns out there it is. There's another device on there. It's a

**Dave Jones:** TS3A4751. And that's a Texas Instruments single supply quad analog switch. And if you go down here and take a look at its current consumption, there it is at 25° C, which is it's near enough to that here in the lab. It's around about Well,

**Dave Jones:** no, actually, it's saying that's a maximum figure there. A maximum figure of 75 nanoamps. So, you know, but that could vary quite significantly, I'm sure. But at least a good part of that current is coming from this device.

**Dave Jones:** So, then what that's doing is powering this analog switch here, which has the JTAG signals going through it. So, I'm not sure why they're powering that device. Well, I guess you've got to measure allows you to measure the MCU power

**Dave Jones:** consumption during JTAG debug operations, I suppose. But there you go. There's the VMCU target and the VMCU debug there are the things that go down and power the microcontroller. So, it looks like that's a bit of I don't know if it's an it's not really

**Dave Jones:** an oversight, I guess, but it's just a design thing that doesn't allow you to accurately measure the just the raw core power consumption of this thing. And bingo, I hate these moldy sheet schematics. They're rather confusing, but and VMCU not only powers

**Dave Jones:** this analog switch here, but there's another analog switch. Here it is, VMCU also powers U695B there. So, there's another device. So, there's two of those devices there at 75 micro 75 nanoamps maximum, which brings us to 150, and

**Dave Jones:** we're measuring 160. So, really, it, you know, it it comes out in the end. It works. It's the micro is around about 20 nanoamp 10 or 20 nanoamps or so according to the data sheets, but this isn't going to

**Dave Jones:** be very precise because you've got you're measuring the power consumption of these devices as well, these analog switches, which is going to vary with temperature, and the micro is going to vary with temperature as well. So, unfortunately, that

**Dave Jones:** jumper on there does allow us to measure the current, but there's that residual in there. It allows you to measure the current of your micro under test except for that very deep sleep mode where you can't really characterize the 20 nanoamps.

**Dave Jones:** What a bummer, but I'm not sure it will actually meet its spec. I'm sure they've done their homework, and they've done their isolated measurements there, but that's still handy for developing your applications just using that jumper shunt there, and you can measure the

**Dave Jones:** in-circuit current, or you can do it using the on-board energy management thing. So, there you go. I rather like that. That's a bit of playing around with the energy micro EFM32 Tiny Gecko starter kit. Now, I really I think I like these devices. They live

**Dave Jones:** up to their name, energy micro. They're all about measuring the energy consumption and different energy modes of these microcontrollers. So, next time you're in the market for one of these for a low power micro, check them out. That's energy micro. So,

**Dave Jones:** if you like the video, please give it a thumbs up and you can discuss it all on the forum. Catch you next time.

**Dave Jones:** And this is rather neat. I've got it in LCD mode here and I disconnect the power, break it, and it fades away a bit because it's still storing energy in the bypass caps and that's what's still powering the

**Dave Jones:** circuit. It still keeps it alive for quite a few seconds and even when you think it's dead, it can come back. Beautiful.
