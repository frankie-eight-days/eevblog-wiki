---
video_id: VK8MEcOYTOE
title: EEVBlog #497 - Siglent SDG5000 Function Generator Teardown
url: https://www.youtube.com/watch?v=VK8MEcOYTOE
source: youtube-asr
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Today we've got a brand we haven't torn down before. This is a Siglent SDG 5082 or 5000 series function function {slash} arbitrary waveform generator. It's a quite a decent bit of kit. Goes for over

**Dave Jones:** four digits. So, let's not muck around. Let's take a look inside. No, I haven't even peeled the tape off the front. Haven't even powered it up after taking it out of the box. You know what we say here on the EEVblog? Don't turn it on.

**Dave Jones:** Take it apart. Actually, I will stand corrected on that four digit comment or over a thousand dollars. Yes, it is over a thousand dollars for the 160 megahertz version, but this is the 80 megahertz version. I believe the only difference is the you

**Dave Jones:** know maximum output frequency. The sample rate 500 meg samples per second is the same between units. And so, this one 5082, you can get this for under 600 bucks street price. I think it goes for just slightly over 800 from the official

**Dave Jones:** rep here in Australia. That's in Australian dollars with the bit of a weak Aussie dollar at the moment, but yeah, quite an affordable function gen actually. And of course, it competes directly with the Rigol DG 4000 series which we've seen in quite a few videos

**Dave Jones:** now, but this one they claim they one up the Rigol with its with this easy pulse technology in this thing apparently. So, which allows for lower phase noise, lower {slash} jitter, and greater resolution on in terms of being able to set the duty cycle, the

**Dave Jones:** pulse width, stuff like that. So, you can get really fast edges apparently at low output frequencies. So, anyway, um it does have USB. This isn't going to be your review, of course, but we haven't seen this before, so we probably

**Dave Jones:** shouldn't probably should just give a minute here to give a brief overview. I have not powered up, as I said, haven't used it, so I don't know how it operates. Clearly, these buttons all light up, all the soft buttons. Very small little

**Dave Jones:** keypad here, so it doesn't take up a huge amount of room. Nice indenting on the big knob there. I rather like that. And yes, it's pushable. It's got a secondary uh select function. Really nice. Uh channel one, channel two. I

**Dave Jones:** believe the second output has uh much greater memory. I think six Don't quote me. 16K on channel one and like 512 on channel two or something. For some reason, lots of uh soft buttons along the bottom. Big graphical color

**Dave Jones:** LCD display on the thing and a couple of uh mode buttons. And well, that's a bit Obviously got a fan on the side, so it does uh heat up a bit. And on the back, we've got a USB uh device, external uh

**Dave Jones:** trigger, gate, FSK, burst, multifunction. Uh we've got modulation in. We've got sync out. We've got 10 MHz external 10 MHz reference in. Excellent, so you can hook it up to your rubidium standard or something like that. Fantastic. And the uh reference output,

**Dave Jones:** if you need to synchronize the internal reference with something else. But apart from that, it's pretty spartan. Universal AC input voltage. There is one thing though that irks me a bit. Just these little tacky gold QC pass, QA pass

**Dave Jones:** by, you know, tester number 01 and QA operator 01. It's just It's you know, they're the sort of type of exactly the look and feel of the stickers you get on just the real cheap, crappy stuff that comes out of China. It It, you know, I

**Dave Jones:** know it's only minor, but it just gives me that impression. But anyway, the unit does feel very good. So, uh we've got no problems whatsoever. The shielding bay actually, yeah, it's not too shabby. So, anyway, let's see if we can crack this

**Dave Jones:** open. It's got uh these rubber surrounds. There we go. They just pop off, so they don't Looks like they don't hide any screws or anything. Um they could actually come off. I probably prefer um like the full rubber boot

**Dave Jones:** like you get on uh the Agilent gear and stuff like that, but it looks like we have two screws here, and it looks like that back will pop off, and then the whole chassis there will just slide off.

**Dave Jones:** Warranty void if broken. We can deal with that, no problem whatsoever. Yeah, there are methods to actually uh get those off, but big whoop. So, let's crack this open. We've got a standard uh Phillips here. Now, we haven't By all

**Dave Jones:** accounts, they're not uh not too bad at all. So, expect a reasonable um standard of quality in terms of the design and the uh build quality of the manufacturing of the PCB. They must have captive screws in there, I think. No, doesn't. It just

**Dave Jones:** popped out. And all right, better pick that up before I lose it. And it looks like Is that going to slide out, or have we got another one holding it in? No, maybe we have to take the handle off. No,

**Dave Jones:** turns out that we didn't. Um There we go. Got some nice They've got They've removed the paint there just so that they can get some extra shielding on the case. That's rather nice, and I can see some nice

**Dave Jones:** RFI gaskets here. I got them upside down. Oops, all the electrons will fall out. Got to be careful. Oh, that looks really nice inside. But there we go. Got some very nice um gaskets there. Nice attention to detail

**Dave Jones:** for the EMI shielding on that thing. And this, folks, looks really, really good. Now, at uh first glance, I was going to say I don't mind the build, the design and layout and build quality of this thing. And well,

**Dave Jones:** yeah, I don't mind the, you know, modular board construction and and stuff like that. It looks fairly neat. They've, you know, they've got metal shielding in the middle here. They've got clearly the the mains power supply on this side here going across all

**Dave Jones:** separated. Nice big mechanical clunking switch, which I don't know if that's the real Yeah, it looks like the real deal cuz we've got mains wiring running over here and going like that. Anyway, I was going to say I don't mind that and I

**Dave Jones:** don't, but the first thing I noted was the cheapness of the metal in this. And then I looked closer and even from a distance, I'll get my macro lens out, but it looks like the chassis is all rusted along here and here.

**Dave Jones:** And there you go. Look at that. That is just truly awful. It really is. To get a factory fresh unit straight out of the box and then have, you know, rust on top of the damn thing. I have to get a screwdriver and try and

**Dave Jones:** get that a scrape, but that is just truly horrible. And it's not just in one spot, either. Let's go to the other side. And there's the other side. I mean, look at that. It is just horrible. It really is. Oh,

**Dave Jones:** man, that's just thumbs down. And then the rear panel, they've just clearly just welded that on instead of, you know, screwing that in place. So, it just It just looks and feels really cheap quality. I don't like it at all. Now, I know diddly squat

**Dave Jones:** about welding, so I clearly can't comment on that. So, maybe someone with the Well, well, any welding experience might be able to comment on that, but it's just so cheap and nasty. And combine that with the rusted chassis, you've got

**Dave Jones:** to be kidding me. And they've done the same on the front panel here. You can see the rust on the left-hand side of the connector there on the side. And then they've just uh spot welded those uh tabs there. I mean, it's all

**Dave Jones:** actually folded up from the bottom of the chassis, but they're up It's all one sheet from the bottom and folded, but then at the top of the chassis up there, they're just spot welded together. And then if you have a look in there at

**Dave Jones:** the cable uh penetrator that goes through the front chassis for that ribbon cable there, it's just uh I just punched out and folded and it's There's some rust on that, too. Looks horrible. So, you can see what they've done. This

**Dave Jones:** is all one sheet and they've obviously cut out all of this bottom for the PCB here. Uh not entirely sure why you would need the bottom on there exposed, actually. Um but anyway, they've decided to do that and it's folded over here.

**Dave Jones:** They've obviously just put the uh decal sticker on the back there. So, they've folded that down, folded it over there, and then they've spot welded the sides and also at the front here as well. And I can't really get the camera

**Dave Jones:** angle in there. It's very difficult, but right up under there, you can see my uh huge big scrape or file marks or something, plus more rust. Well, let's forget about the shocking rusted chassis for a minute and have a look at the

**Dave Jones:** electronics as in-depth as possible because it actually does at first glance, it looks really good. The soldering and the construction and the design quality, as I said, they've clearly got like all the major all the major processing and you know display

**Dave Jones:** stuff and logic stuff most of majority of it's happening on this board over here which is opto isolated. There we go. We've got some analog devices isolators. We'll take a serial isolators. We'll take a look at there. So they're jumping that. That's why they

**Dave Jones:** split the boards in there. You can see that the output BNCs of course they're actually uh to the input or the output the output side here. So they're actually reference to there. So the ground reference on the these inputs and outputs on the rear

**Dave Jones:** terminal of course will be ground referenced to the main function gen outputs there. But the USB of course will be is isolated because that's all part of the main processing circuitry in here and then isolated by our analog

**Dave Jones:** devices isolators there. Of course it's got its own separate power coming across here from the main board and then the main output board here of course has it's all has looks like multiple supplies of course coming from our power

**Dave Jones:** supply over here and our power supply over there which we'll take a look at looks really good. But it's really difficult to get down in here and take macro shots of the chips and everything without taking the boards out. So

**Dave Jones:** I'm going to have to do that. I'm going to have to basically strip this thing completely down basically the screws down in here. So I'll have to do that. We've got some nice little right angle board mount coaxials coming off here

**Dave Jones:** really good to the output terminals. So that looks really quite nice and well laid out. So I'm quite impressed. Now I don't mind what they've done with the earthing here at all. You know they've taken it through here. They've got it up

**Dave Jones:** to here. It's nicely crimped and with a you know a slight crimp connector going on to there. It's all rather nice and I like the layout of course of the board in there which will go into but of course this is a PCB mount IEC So,

**Dave Jones:** the first thing I think of as well, there's a through hole pins going to the bottom side. How much clearance to the case? Now, if we have a look on the bottom side here, you can see there is

**Dave Jones:** bugger all clearance there. And at first I thought, "Oh my goodness, that is just, you know, awful. It's going to short out and everything." But, the but because this is a separate physical board in here, it looks like it does

**Dave Jones:** look like they do have larger standoffs in there. So, that's sort of the top of the board lines up with there. So, it's going to be 1.6 mm below that and then you're going to have the pins extending

**Dave Jones:** out. Then you got the thickness of the sheet metal, which is really thin and crap and rusted, of course. So, I don't know. It might have enough clearance in there, but I hope they've put like an insulating sheet or something over that.

**Dave Jones:** Actually, just going back to the rusted chassis here for a second, you can see like down the side wall, it's almost as if like they've Uh you know, I don't know all my sheet metal mechanical processes and stuff

**Dave Jones:** like that, but to me it almost appears as though they've tried to like, you know, deburr this thing or something. You can see all the scratch marks along the side of it and that is just you know, caused it to all rust. And as I

**Dave Jones:** said, I can see a similar thing up under the front panel, but even worse than this. Well, I've got the board out and this really is quite a nice piece piece of work. I'm relatively uh impressed by this. As I said, the big

**Dave Jones:** clunking main switch over here. They've even got nice cutouts in there. High voltage isolation slot routed out of the board in there. Very nice indeed. So, we'll whip that off and uh that just only gets in the way. And of

**Dave Jones:** course, here's the here's the secondary side and we've got some really nice silastic. Somebody's gone to town with the hot snot gun there and they've silastic all that down. We've got some inductors in there. Our output caps will take a look at the

**Dave Jones:** brands. There's our output diodes there and they've, you know, it's designed very well. We've got our isolation slot under our optocoupler there. There's our reference circuitry down in there and really nothing else on the secondary side there at all. There's our

**Dave Jones:** suppression from the primary side to the secondary side and you know, I was going to say all the isolation was quite nice in here, but you'll notice why they've sort of, you know, look at that. There's not much clearance in there. It's

**Dave Jones:** probably going to be good enough, but look, they've gone to, you know, town to, you know, remove all the copper fill out of here and do the nice isolation slots in there. Yet, they ruin that by bringing this trace. I mean, they could

**Dave Jones:** have, you know, snuck it sort of down this side and around to the suppression cap there, but they haven't. They've just look. That's pretty darn close and they've filled that in. They've put a big square in there. Don't know why

**Dave Jones:** they've done that. They've blown it, but it's, you know, it's good enough, but yeah, they just missed that little attention to detail. Then we have nice little touch. We've got our isolation slots between the individual pins of the

**Dave Jones:** driving transistors on the primary side of the transformer here. So, that's a nice touch. They knew what they were doing there certainly and also they've done uh isolation slots in here for the main diode bridge as well. And on the

**Dave Jones:** primary side here, they haven't skimped at all. Of course, slow blow fuse protection. Once again, selastic down. They've got a full cover over that. They just haven't left its ass flapping in the breeze there. We've got a thermistor. We've got MOV

**Dave Jones:** protection down there. We've got the filtering common mode choke. It's all happening. Very nice. No problems whatsoever. The main cap is a Rubycon 105° C rated 400 V 220 MXC series. You know, it's not a one hung low cheapy.

**Dave Jones:** They've chosen a reasonable brand there for the price. And for those playing along at home, the main controller is a T NXP TEA1610T. And that's actually a zero volt switching resonant converter controller and that's exactly what they implemented

**Dave Jones:** here. And it's hard to see, but these are the output caps are 105° C rated Rubycons as well. So, they haven't skimped. And if we get our depth gauge on the post in there, we're looking at just over five five millimeters

**Dave Jones:** clearance. And if we have a look at the depth of that pin on the board, just almost it's about two millimeters. So, that three millimeters clearance is going to be adequate there to the chassis for normal use. I can't remember

**Dave Jones:** the regs the exact values from the regulations off the top of my head, but yeah, it's probably going to be good enough. I really would have liked to have seen some an insulation sheet under this board between all of this mains input

**Dave Jones:** circuitry and the chassis though. And they've gone to the trouble to actually hold this ribbon cable down onto the flat flex connector down there with some tape. Look at that, they've actually taped it all the way down there which

**Dave Jones:** goes onto the connector. So, to get that out, I can't just lift the tabs as usual. I've got to actually peel off all that tape. How annoying. And we've got the main processor board out. Does look quite good as I said and let's take a

**Dave Jones:** look at some individual devices and the soldering quality. And no surprises on the main processor front here, Analog Devices Blackfin DSP which we see time and time again in all of these embedded scopes, the Rigol ones and all sorts of

**Dave Jones:** brands we you You know and love. They've got Blackfin DSP devices in them. Analog Devices must be laughing all the way to the bank. And right down the bottom, a populated JTAG header connector, just raring to go. Hack away. And at first

**Dave Jones:** check, I can't really ID that Texas Instruments part there. Obviously, it's the main clock driver PLL. So, you know, 25 MHz main crystal generating the higher frequencies required for the system operation. And the only other major device on here is this Lattice

**Dave Jones:** Semiconductor Mach XO PLD. It's not even a CPLD. It's just a a sort of a low-end PLD. Although these PLDs are actually quite fast. This one will do 388 MHz. It's only got 640 lookup tables. It's got 320 macrocells. It's got 6K of

**Dave Jones:** high-speed SRAM in there. But, you know, that's about it. And here's a classic example of where you would use a CPLD or PLD over an FPGA. For example, you just need some sort of, you know, glue interface logic between the main

**Dave Jones:** Blackfin processor here. We've got our main memory in here. You can see the traces going down here. So, obviously, it's doing some sort of memory control in there. It's obviously got data linked into the processor down here. But, then

**Dave Jones:** it goes off to this main connector, which is all the serial lines which go over that optical interface we saw back at the start that controls all of the output. So, that is all the serial interface for that sort

**Dave Jones:** of stuff. And it also controls, look, all these traces all tied into the front panel stuff. So, it handles all that. So, it really is a big part of the system glue logic here. And then coupled into all that, we've got our Hynix DRAM

**Dave Jones:** here, fairly high-density one. I think it's 4 meg by 16 bits. And our Spansion flash memory, which of course, contains all of our processor code. And it looks like we've just got a couple of low-end switching regulators down there

**Dave Jones:** from the main DC input here. And then we've got an ISP1763A USB on the go. That's pretty much it there for the main processor board. I forgot a programming header up here for the Lattice PLD as well. But apart from

**Dave Jones:** that, well, that's all she wrote. So, that's quite well designed and laid out. No issues there whatsoever. Let's go have a look at the main output board. And the main board here, as I said, looks to be very well designed and laid

**Dave Jones:** out. They seem to know what they're doing here. We've got our regulation circuitry up the top here. These are all obviously low dropout regulators for all the various rails, which is why they can get away with no regulation on the output of the

**Dave Jones:** converter up there because the main uh uh the main power supply board because then they're just locally regulating them down here. And of course, they're going to use multiple taps there because they want the lowest possible power dissipation in these devices.

**Dave Jones:** They're only using the PCB as the heat sink in there. So, that's why they've just got the multiple voltage rails. And there, of course, because you've got rails for your analog stuff. It might be, say, you know, plus minus 12 V or

**Dave Jones:** something like that. Plus, you need your 3.3 and other 5 V and other rails as well. And heat sink on the main device here, I can't seem to get that off. So, sorry, I am not going to try. I do want this thing to actually

**Dave Jones:** work when I put it back together. So, unfortunately, it is probably stuck on with some of that heat sink glue. So, that's not coming off real easy. Um we've got a TX DAC here which we'll take a look at. A number chip with its number

**Dave Jones:** rubbed off. You've got to be kidding me. The as we said, the uh serial opto-isolated interface coming in here. They've got ground plane around It looks like we've got some more uh switching power supply stuff up here. Relays

**Dave Jones:** everywhere. Um in quality NEC uh brand. So, they haven't actually uh skimped on those at all. Some miscellaneous analog stuff happening around here. And it looks like two identical channels for both uh channel 1 and channel 2 here.

**Dave Jones:** And then it looks like we have a cap and a a uh transient suppressor going down to mains earth on both uh channel 1 and channel 2 outputs. Now, of course, I could hazard a pretty good guess of

**Dave Jones:** what's under this heatsink. It's going to be a Xilinx or an Altera or maybe some other brand uh FPGA. Um you know, it's almost for sure that they're going to have an FPGA in there implementing their uh true pulse uh technology or

**Dave Jones:** easy pulse technology. Uh sorry. And that's coupled into our uh SRAM on either side here. We've got a TX stack with which we'll take a look at mystery device here that's been sort of uh lay you know, rubbed off. I don't think it's

**Dave Jones:** been laser etched. It's not uh It's not uh quite um you know, straight and perfect enough for that. So, they've probably got that on the grinder there and just grinded away. Why? Why? Jesus, not going to stop anyone. If you really

**Dave Jones:** want to find out that chip is, you know, uh jeez, you know, a day's work tops. Unbelievable. Give me a break. Now, this thing actually boasts some pretty good uh phase noise uh jitter specs. And here's why. It BTO507A.

**Dave Jones:** It looks like a uh Chinese manufacturer I've never heard of, but it seems to be a uh TCXO uh temperature controlled crystal oscillator. You can see the multiple footprints they've actually put in there so that they can uh choose a

**Dave Jones:** suitable device for production uh later. Maybe a higher spec uh version or something like that. And right next to our external uh uh input connectors here, we've got an Analog Devices AD CMP 562. That's a dual uh PECL ECL uh

**Dave Jones:** comparator. Extremely quick. We're talking uh 500 picoseconds uh output rise and fall times. Very nice. And there's that dremeled off chip. You've got to be kidding me. It's tied into the uh presumably FPGA down here. I couldn't readily identify those devices

**Dave Jones:** there at uh first glance. So, they're you know, presumably just uh op-amps. They've got two there um presumably uh driving some outputs or some inputs there, and then they've got another one over here as well. And as we've mentioned a couple of times,

**Dave Jones:** here's these Analog Devices uh ADM series 1410 digital isolators. And they've decided to use these instead of uh your regular opto uh couplers that you traditionally find in these applications. These are just nice uh high-aspect, high-performance. You don't have to worry about uh various

**Dave Jones:** issues and stuff like that. They just work. Digital in, digital out, magic kind of devices. They do cost more, though, unfortunately. And it looks like we have some sort of uh current shunt thing happening here with some sort of

**Dave Jones:** uh maybe instrumentation amp tacked on there. And there's the SRAM we've mentioned uh before. It's a uh Cirrus Logic part, and it's a 512K by 18-bit uh SRAM. Of course, you need uh you know, more than your regular 8-bits because

**Dave Jones:** this is a uh 14-bit resolution output uh converter on each channel. So, they've got two of these uh devices. Once again, 500 They're both uh 512K uh devices, identical. So, I'm not sure why the spec for one of the channels is less

**Dave Jones:** than 512K. And of course, our main DAC, which is one of the hearts of any function generator. Of course, uh they of course haven't skimped. It's an Analog Devices uh TX DAC um um AD9781. And as per the data sheet specs for this

**Dave Jones:** thing, this is a dual channel 14-bit uh DAC. Does 500 megasamples per second and per second, exactly as it claims on the front panel and as they claim in the data sheet for the resolution. Not a problem. And you can see it's an LVDS

**Dave Jones:** interface. You can see the controlled impedance pairs going through and they're length matching. That's why I have done uh quite talked about this uh quite often. That's why they got those squiggly lines on there, just length matching all of those just to make sure

**Dave Jones:** that the signals arrive at the exact time for the DAC. And we've got some more fast comparator action around here, same device we saw on the back panel. And then we've got a few uh Intersil 28210 low noise JFET op amps surrounding

**Dave Jones:** a good old 74HC uh 4051. Classic. Got to have some uh 74/4000 series logic in here somewhere. And of course, driving all this magic is an ADF4360. And that is a VCO um you know, many gigahertz operating range. So, that's

**Dave Jones:** what's uh generating the clock. And of course, matched to that, you got to have a low noise low dropout regulator just dedicated to powering that sucker. So, they've got a Micrel What is it? If I can see it.

**Dave Jones:** 5209. And that's going to give us a main uh clock output frequency of somewhere between 2.4 and 2.7 gigahertz. But of course, it's got uh multiple it's got uh divided down uh selectable divided down outputs as well. But you know, clearly,

**Dave Jones:** there we go. That's going up there. Little bit of length matching in there to drive our DAC. So, a lot of the analog performance of this thing is is to be determined by uh you know this uh VCO here which

**Dave Jones:** generates the high frequency clock for the main DAC, of course, and how you uh you know power that. You can't just power that willy-nilly from the supply rail and expect to get good specs. So, really they've um you know they've done

**Dave Jones:** reasonably well there. They haven't skimped at all, of course, but that's what you expect. I mean this thing is you know it's specs are very very good for a um well for any sort of oscillator, let alone one in this sort

**Dave Jones:** of price range. And we haven't showed you the relays yet. There they are, NEC UD2-4, something like that. Anyway, they are NEC branded, really crappy looking um inkjet printing uh labeling identifier on the top of those things. Ooh.

**Dave Jones:** Now if we have a look at the uh bottom of the board here, here's the four relays for one particular channel. And you can see they've got all the matching pads and they've physically removed the uh ground fill underneath directly

**Dave Jones:** underneath those pads. Normally you might do something like that to just uh decrease the capacitance of the individual pin to the ground plane. You know, you might be able to save you know half a puff or uh something that reduce

**Dave Jones:** your capacitance to ground by half a puff or something, but because this is a four-layer board, there's going to be an internal ground plane anyway, unless they've actually left off uh the ground fill inside the inner ground plane as well. But you can see they've

**Dave Jones:** also done similar stuff around here as well. So, maybe they do actually know what they're doing in that respect, and over on the more closer to the output side here, they've also done it here as well. So, I think they probably know

**Dave Jones:** what they're doing there, just trying to reduce that uh capacitance by half a bee's dick. And the output circuitry here, we've uh got some exposed copper on the bottom here, lots of vias that tells us that the uh chips on top have a

**Dave Jones:** thermal pad and uh clearly they're trying to heatsink those. So, let's find out what those chips are. Aha, no real surprises. Texas Instruments THS3095.

**Dave Jones:** High-speed, low-noise, high-voltage, high-current uh current mode op-amps. So, these things are maximum bandwidth 210 MHz. Sort of pretty much perfect for the application required here.

**Dave Jones:** Now, I'm not entirely sure why they've sort of surrounded all this with sort of like a big dip uh footprint. It's almost as if like another like a design to have possibly another module in there or something like that perhaps. Whether or

**Dave Jones:** not they were going to abandon this circuitry and put it on a secondary module whether or not there's a second module that plugs in there. Not entirely sure. Now, because this is only the 80 MHz model, does that mean that the 160

**Dave Jones:** MHz model has something additional in here? I don't know. If anyone with a 160 MHz model of this thing can open it up and confirm, that'd be really nice. So, yes, they're the pads of every alternate resistor there that they've removed that ground

**Dave Jones:** fill on plus the traces going to them. So, clearly they're just reducing the capacitance to ground on those individual high-speed nodes. Hmm, very tricky. And clearly they meant for a shielding can to go in here cuz take a

**Dave Jones:** look at the classic uh mounting points there for that shielding can which would go over that whole thing and also there'd be an internal shield in there just uh separating the relay modules from the output drivers as well. And the

**Dave Jones:** main output uh coax connector here, they've got that running internally underneath, so you can't actually see the traces on there. It's running between the internal ground planes. And you can see the isolation split in the ground planes here, of course, uh

**Dave Jones:** separating all of our output ground reference to our mains ground reference stuff that we had. And of course, there there are That's our data optical isolation barrier in there all the data coming over. But you can see that it also goes up to here to one of

**Dave Jones:** the output connectors as well. So, one of the output connectors is mains ground reference while all the others aren't. And if you have a look at the back panel here, tada! There we go. We've actually got uh two of them that are mains earth

**Dave Jones:** reference because there we go, they don't have the white insulating thing, and three other isolated ones. So, you can actually tell where they come from on that connector because these ones are the isolated ones here on this connector

**Dave Jones:** plus uh one, so there'd be two connections on that one plus one on the other one. And obviously, the other two are connected to this side of the ground instead of the output side. And as for the soldering quality on both boards,

**Dave Jones:** well, pretty much first class, no complaints there whatsoever. And even the high thermal capacity coaxial connectors, not a problem. As you've seen, these two boards are designed and manufactured pretty much first class and certainly more than adequate for the

**Dave Jones:** price range, that's for sure. We're only talking a $600 unit here for the low-end one I've got and just over a thousand for the 160 high-meg unit. But um whoever uh designed this thing certainly knew what they were doing from a function

**Dave Jones:** generator point of view. They've used uh you know, certainly top class components. I don't think they're overclocking anything at all. Everything seems to be within spec. Don't know what's going on with the rubbed off number chip here. Uh

**Dave Jones:** bastards. But anyway, it seems like they really know what they're doing in this thing. Probably I would be fairly certain that it would certainly meet its specs for its you know fairly demanding specs it's got for its performance. So, not a problem

**Dave Jones:** whatsoever. Thumbs up on the electronic side of things. But the chassis? Oh, come on. You got to be kidding me. Rust straight out of the box. That could be their new slogan. Unbelievable. It's just flimsy crap folded metal and spot

**Dave Jones:** welded and rust as far as the eye can see. Unbelievable. Thumbs down. What an absolute shame because the electronics is you know pretty darn impressive. Not a problem whatsoever. Just let down by stupid chassis. Got to be kidding me.

**Dave Jones:** Oh, facepalm. And once again, just like we saw with one unit on the top of the board, we've got some current shunt shenanigans going on here and here as well. So, we've got a total of three of those. Oh, by the way, these output

**Dave Jones:** connector boards, nothing much doing on there at all. But they do have a couple of surface mount transformers on there. Quite neat. And just for completeness, here is the front panel. There were a couple of screws on here. Nice looking

**Dave Jones:** output connectors. They look really huge and massively solid integrated in there. Really like those. They should last quite some time. We've got some EMI tabs up here to connect through to the main chassis there. There's our Once again, they've got tape. Nice attention

**Dave Jones:** to detail there. Tape holding down the flat flex cable connectors there and there. So, that's very nice. Nothing much doing of course. This is going off to the front panel full color TFT display. There's our USB connector over

**Dave Jones:** there on its own little separate board. But, apart from that, eh. Once again, you can see the RF EMI shielding along the base of this thing. They've got that along actually all four sides in there. Excellent. They've done

**Dave Jones:** pretty well in the EMI side of things here, that's for sure. Once again, you can see the horrible rust on the front panel there where they've clearly like, you know, scraped away deburred this thing. It probably doesn't show up

**Dave Jones:** on camera as well as I can see it with my eye, but you can just see the see the scrape marks there. Ah, absolutely horrid. Maybe if I There we go. Look, you can see them clearly. And it's just rusted all the

**Dave Jones:** way along the front there under that under that front panel bezel. Unbelievable. By the way, I don't particularly care for the self-tappers they're using to secure this front panel on, but I guess, you know, it's not something that you'd take off all the

**Dave Jones:** time, so eh. Well, here we go. It's almost back together except for the top case, and hopefully I've plugged everything in, and uh Yeah, well, let's switch this sucker on for the first time, and uh see if it works.

**Dave Jones:** Hello, Siglent. Woohoo! There we go. We're up and running. Not a problem. And bingo, we're in. That's pretty fast boot. I like it. Works a treat. There you have it. That's a teardown of the Siglent SDG 5000, or in particular

**Dave Jones:** the 5082. 80 MHz, 500 megasamples per second function arbitrary waveform generator. And well, I was extremely disappointed at the quality of the chassis in this absolute thumbs down for the mechanical chassis quality and construction. Just awful. It's what I expect to see in one

**Dave Jones:** of those $50 cheap ass no name, you know, power supplies you get on eBay or something, you know, 30 amps at five, you know, 30 volts at five amps for 50 bucks, you know? You expect to get a rusted old

**Dave Jones:** metal chassis with the bloody thing, but not in a, you know, Siglent, who are, you know, a quality brand these days, or at least they're trying to be. And they're they're the performance of some of their gear is, you know, really quite

**Dave Jones:** good. And this thing, you know, is has really good specs for the price. Great bang for buck, but jeez, the quality of that chassis just very disappointing, very flimsy metal. And um And then it's, you know, it's just rusted everywhere as

**Dave Jones:** far as the eye can see. Unbelievable. But of course, the electronics in this absolute thumbs up, first class, not an issue. Couldn't fault it in any way, shape, or form, really. So, overall, what's it going to get? Well,

**Dave Jones:** it's certainly not going to get a thumbs up because it was let down by the stupid rusted crap metal work in this thing. But, you know, it's offset by the decent high quality, well designed electronics in this thing. So, well, it's up to you how

**Dave Jones:** you want to call the overall, Uh, you know, rating this thing, whether or not a rusted little flimsy metal shatty chassis matters to you and whether or not that's actually typical of these units or not or whether or not I've got some dud or

**Dave Jones:** something. But yeah, it's definitely not going to get a thumbs up from me overall. Apart from even with the high quality electronics in there, I just left a bad taste in my mouth the rust. Give me a break.

**Dave Jones:** There we go. Yeah, it tastes like rust. Yeah. Unbelievable. Give me a break. So, yeah, that's it's man, it's almost a thumbs down overall. You know, barely a thumb sideways. Unbelievable. But if it didn't have the rust, even with the flimsiness of the

**Dave Jones:** metal work and stuff like that and the you know, the cheap spot welding, I you know, I still would have been very impressed by this thing I think. So, yeah, just let down down by something as silly as just a mechanical

**Dave Jones:** thing like that. Unbelievable. If you want to discuss it, you know where to do it. The EEVblog forum is the best place for all test equipment and Siglent are actually on the EEVblog forum as well. So, it'll be very

**Dave Jones:** interesting to see what they say about the crap rusted metal chassis in this thing whether or not it's typical of this unit or typical of the construction of these things or whether or not I've just, you know, somehow got

**Dave Jones:** one that's just left on the dock somewhere and it was just uh rusted away to the hilt. I don't know, but anyway, EEVblog forum is the best place on the internet to discuss test gear. Definitely jump on over there. And I

**Dave Jones:** don't mention it much, but if you want to follow what's going on with me and the blog and various other rants on a daily basis, Twitter is the best place to do that. I tweet a lot. EEVblog is my

**Dave Jones:** Twitter name. And so, follow that. And yeah, Facebook, yeah, whatever. I've got some Facebooky account thing. I don't know. The videos get auto uploaded there, but don't send me any messages on Facebook. I don't read them, but Twitter, I definitely do.

**Dave Jones:** Anyway, I hope you enjoyed that little test equipment teardown. I know a lot of people get a bit sick of seeing test equipment teardowns, but I personally like test gear and I like tearing them down. So, that's what you're going to

**Dave Jones:** get a lot of here on the EEVblog. Catch you next time.
