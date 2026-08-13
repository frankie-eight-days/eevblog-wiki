---
video_id: E3B4OTV8f1o
title: EEVblog #864 - Siglent SDS2000X Series Oscilloscope Teardown
url: https://www.youtube.com/watch?v=E3B4OTV8f1o
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 19, "2": 33, "3": 49, "4": 68, "5": 85, "6": 105, "7": 126, "8": 145, "9": 164, "10": 182, "11": 200, "12": 218, "13": 238, "14": 251, "15": 269, "16": 292, "17": 308, "18": 330, "19": 351, "20": 370, "21": 390, "22": 406, "23": 422, "24": 438, "25": 458, "26": 478, "27": 494, "28": 510, "29": 526, "30": 542, "31": 554, "32": 570, "33": 586, "34": 602, "35": 614, "36": 638, "37": 654, "38": 670, "39": 690, "40": 706, "41": 718, "42": 738, "43": 754, "44": 770, "45": 786, "46": 802, "47": 818, "48": 834, "49": 850, "50": 866, "51": 886, "52": 902, "53": 922, "54": 942, "55": 962, "56": 978, "57": 994, "58": 1010, "59": 1026, "60": 1042, "61": 1058, "62": 1074, "63": 1094, "64": 1106, "65": 1122, "66": 1142, "67": 1166, "68": 1182, "69": 1202, "70": 1222, "71": 1246, "72": 1258, "73": 1282, "74": 1302, "75": 1318, "76": 1334, "77": 1354, "78": 1370, "79": 1390, "80": 1410, "81": 1426, "82": 1438, "83": 1466, "84": 1502, "85": 1526, "86": 1546}
---

**Dave Jones:** Hi, it's another oscilloscope teardown. Very exciting, we love scope teardowns here on the EEVblog. This is the new Siglent SDS2000 X-Series scope. And I have had my hands on this puppy before. Click here to see a video with the Siglent CEO, who actually was kind enough to visit the lab here.

**Dave Jones:** And I had a brief play with it for like 10 minutes and then they took it back from me. Anyway, I've only just recently got one back in care of. Charles at Trio Test and Measure here in Sydney, so thank you very much Charles.

**Dave Jones:** So, I'll try not to break it on you. Anyway, and I will try and refrain from actually turning this on. It'll just be a teardown. Let's go. And I've also previously torn down the new 1000 X-Series, so click here if you haven't seen that one.

**Dave Jones:** So, this one should be a fair bit different. This is 300 megahertz analog bandwidth, 2 gig samples per second. The other one was, 1000 X, was only 1 gig sample per second. So I'd expect to find a different ADC in here perhaps. This is a 4-channel, the other one was only 2-channel.

**Dave Jones:** But just a brief overview, it goes from 70 megahertz up to 300 megahertz. The models, the 70 megahertz model starts at $1285 or thereabouts. US dollars goes up to $2800 for the 300 megahertz version. And I'm pretty sure the hardware is exactly the same.

**Dave Jones:** Even the 70 megahertz model most likely has the 300 megahertz front end, and they're just software limiting that. I don't believe there's a software upgrade option. You have to actually buy the particular model, but I stand to be corrected on that. Mixed signal scope, we've got a 25 megahertz ARB gen as well.

**Dave Jones:** All the bells and whistles. It's got up to 140 meg point of memory. That halves if you use a couple of channels, but 140 meg of memory. Amazing what these scopes have got these days. Pretty darn quick, 140,000 waveform updates per second. And 256 color intensity graded display.

**Dave Jones:** So very nice bit of kit, starting from $1200. Incredible value. And on the back, not a huge amount doing, but we do have building LAN as standard, USB device, pass-fail output, and external trigger as well, which is terrific because you can, with the external trigger,

**Dave Jones:** you don't have to sacrifice one of your analog channels. So it's true, four channels plus external trigger. Brilliant. And just as a size comparison, I'm going to put it next to the tiny little 2-channel Rodin-Schwarz HMO 1200 series here, and it's, oh, look, it's a pretty big scope.

**Dave Jones:** But, of course, it's four channels, of course, and it's pretty thin as well. It doesn't take up much bench space. Nice. And all the knobs are pushable on it, so you can do center and all that sort of jazz. Very nice. I've got to admit, I don't like the look and feel of these knobs.

**Dave Jones:** They're just... I don't know what they were trying to go for. And the color scheme is all a bit bland, and it's just, well, I don't know. Personal taste, but yeah, it's just... leaves a bit to be desired. But, hey, that's nothing. As long as it works and gives good value, that's all you care about.

**Dave Jones:** And they do have the probe detection. You can see the grounded point around there. So they're supplied with switchable probes, so auto-detect. Curiously, it's just one big solid ring. Usually, you know, it's like a half ring or has multiple rings. But, you know, it does not have any external power or anything like that,

**Dave Jones:** so you can't power active probes like you can on some of the higher-end professional scopes. But otherwise, it actually feels, you know, reasonable quality for the price. Not the best feel made unit, but yeah, not bad. And curiously, there's actually screws spread right across the back of this.

**Dave Jones:** There's four here. We're going to have to... it looks like we're going to have to take these off down here. They're all Torx, maybe a couple on the top. That's because it's so large. Usually you only get, like, two down here and two up the top on most scopes these days.

**Dave Jones:** But anyway, let's take it apart and see what's inside. Lots of FPGA goodness, I'm sure, because that's how they're going to be getting the 140,000 waveform updates per second, of course. So there's going to be lots of grunt. There'll be two ADCs in here,

**Dave Jones:** because I believe it halves, well, I believe the sample rate halves when you put on the dual channel. So that indicates that they're sharing an ADC, which is, of course, very common in most scopes. And it should be a different ADC to, as I said, to what we saw in the 1000X,

**Dave Jones:** because it's a higher sample rate. I don't think they would, like, double the number of ADCs and then interleave them. I think they would just use a two gig sample per second converter. But hey, I stand to be corrected. Alright, let's pop the hood on this thing.

**Dave Jones:** And we expect to see some, yep, shielded metal. Power supply separately shielded. Looks like we've got a One Hung Low brand and Adar brand fan on there. Geez, wouldn't trust that any further than I could throw it. And in case you are wondering, yes, the fan is a bit annoyingly loud,

**Dave Jones:** and seems to have like a, like, you can hear the bearings, like they're not good quality bearings. It's just a real cheap-ass fan. Eh, disappointed. But hey, there's a bit of attention to detail. They've cable-tied down the cable for the fan there. And I like the mains here, the mains input up on its own bracket there,

**Dave Jones:** heat-shrunk properly, proper mains earth down here. We've got, that one's, is that crimped or soldered? Anyway, it's heat-shrunk over there. Looks like, doesn't have a shake, it has a shake-proof washer on it, very nice. And this is the cable coming out of the power supply, direct down straight onto the board.

**Dave Jones:** So nicely shielded and nice and neat and tidy. Thumbs up. And there's no sign of the trademark Siglent rust yet. Can't see it, so yep, they're doing well. And the power supply's neat and tidy enough. They've got Celastic holding down the caps, they've got a thermistor,

**Dave Jones:** they've got a MOV, they've got the common mode choke, it all looks, it all looks just fine. They've got the isolation slots, and everything's hunky-dory. They've got the earthing strap on there, and it's alright, except I can hear the groans from here for the Lelon main filter cap.

**Dave Jones:** Hmm. And that's a bit of a shame, because the others are Rubicon. They're a pretty decent brand, so no worries there at all. You've got to wonder if the little heatsink glued on the top of that surface mount package is an afterthought or not.

**Dave Jones:** It's like, oh, we couldn't quite get the heatsink and performance out of our PCB. They've got a few little piddly vias down the side there and there, but yeah, like they just had to stick it on the top. Nothing wrong with that. Hey, whatever works.

**Dave Jones:** These nuts and bolts look a bit how you do and it's like, is that like they've had like, been super glued on or something? Hmm. Anyway, I do like the isolation slots between the pins there. Nice touch. Got the RFI shielding tabs nicely on the ethernet and the USB

**Dave Jones:** connector there. Eh, someone knows what they're doing. You've got to love the pop rivets. Look at this, you can just picture the production workers there with their pop rivet gun, you know, going, you know, k-clunk, k-clunk. I'll tell you what, someone was thinking at the system engineering level, they've made a cut out in the chassis here

**Dave Jones:** to access the RTC battery there. Very nice. And it's small things like that that show you that somebody had a hand in the overall system design of this thing. It's not like they just, somebody did the schematic, threw it over to the PCB

**Dave Jones:** person, they're just laying it out and they put the battery willy-nilly. No, somebody had to, you know, go, right, we want access to this battery without having to take off all this metal work and take off the whole thing. So let's, you know, tell the mechanical

**Dave Jones:** CAD people to, you know, put the, to model that in, the little cut out and tell the PCB person it has to go right there and brilliant. Alright. Let's see if we can get this thing off. We do. I think it's, yep, it all comes off.

**Dave Jones:** Oh, we're in like Flynn. Look at that, that's a nice design. One huge board does everything. Brilliant. Geez, they haven't mucked around with multiple boards. I'll tell you what, right off the bat I'm pretty impressed with this thing. Well laid out and, you know, they haven't

**Dave Jones:** spared too much room inside this thing. So yeah, hats off. Obviously we've got our shielded front ends here. Two channels, two channels. Not sure if we can get that can oh yeah, yeah, I think we might be able to get the can off there.

**Dave Jones:** Excellent. Obviously our analog to digital converters, because they're right next to the cans here. So we'll have our, probably a differential input, so we'll have our differential driver from the analog front end going into our ADC. And that'll be a dual channel 1 gig sample per second converter.

**Dave Jones:** And of course the way they get the 2 gig samples per second is to interleave the two so this is channel 3 and 4. If you've only got channel 4 on, then it can use both channels of the ADC, both to measure channel 4.

**Dave Jones:** So you get your 2 gig samples per second, but if you turn on channel 3 and channel 4 at the same time, you only get halves down to 1 gig sample per second. So of course the trick with these dual channel ones, if you want to use two channels and get the

**Dave Jones:** highest sample rate possible, and why wouldn't you, is to use channels 1 and 3, or 1 and 4, or 2 and 3 and 2 and 4. And these other two monsters here, these are obviously our acquisition FPGAs, so they've got one per two channels there.

**Dave Jones:** This other beast up here, this will be our display processor. And yep, here's our LCD ribbon cable going off, so that'll be just handling the display updating, so it's, you know, this is the reason why they can get the 140,000 waveform updates per second, because they're dumping the data directly from the acquisition

**Dave Jones:** FPGAs here, and dumping it straight to the display, instead of going through the analog device's DSP, which we'll take a closer look at over here. And of course that's a Blackfin DSP, it will be running the OS for this thing, which could be some embedded Linux or whatever it's

**Dave Jones:** you know, a flavor of OS that's actually running, and it's handling all the user interface and the Ethernet and everything else, and the cursors and the front panel, and all that sort of jazz, and the USBs and things like that. But all the acquisition, dumping the data, is done,

**Dave Jones:** goes from ADC to acquisition FPGA straight onto your display processor, and then bam, straight out to your display. Now you can easily tell your logic analyzer stuff, because there's lots of it down here, and we've got individual, they'll be comparators, so it's going to be a decent mixed-signal logic

**Dave Jones:** analyzer, I believe, being able to set the threshold levels and stuff like that. And it's a dead giveaway, that's right down near the mixed-signal connector, right down here. So that's interesting, we'll take a closer look at that. We've got our ARB waveform generator over here, so that's what these relays

**Dave Jones:** are doing, that's near the ARB input. The ARB's probably coming from this lattice CPLD or FPGA up here, so that's probably doing that business, unless there's another processor on the other side of the FPGA or something on the other side of the board.

**Dave Jones:** So if we have a look at the 2000x board, and then we merge the image over to the lesser 1000x model, much much cheaper, you'll notice the lack of a dedicated display FPGA, whereas we've got one here, and bingo, it's there one minute, and it's

**Dave Jones:** on the next. You can see actually a BGA footprint there, which is unpopulated. And from a thermal performance point of view, we've got our vent on the back here, our fan is blowing outwards like this, so this is the outlet fan, and the inlet

**Dave Jones:** are here, and ta-da! Some along the edge here. It's good that they put them at the bottom like this, draws the air over this board, over the heatsinks, and then out like this. If you put them at the top, that would have been, you know, not quite

**Dave Jones:** as efficient as if you put them in at the bottom, the air comes through the bottom there. Nice. And we've got ourselves a little x-ray sticker here, what that's for is that it indicates that they've actually x-rayed this after the board's been assembled, so they're x-raying for the

**Dave Jones:** BGA parts to make sure that they're all hunky-dory, all the balls on there are soldered, so nice, somebody's done the checking. And just in case you weren't convinced that these three are FPGAs and Siglund have levelled up and they're designing their own ASICs now, well

**Dave Jones:** look, dead giveaway, FPGA, there's our JTAG header, and they've only got the one here, so that'd be daisy-chaining all three, which is very common. So what have they got under there? I don't know. Xilinx or Altera? Who knows? I could, eh, I'm not

**Dave Jones:** going to go to the effort to hook up a JTAG boundary scan thing and actually get the IDs out of them. Eh, they're just grunty FPGAs. And coupled onto each one of the acquisition FPGAs is two of these little puppies, Micron, with their bloody

**Dave Jones:** part numbers. Anyway, they do have a little part number decoder on their website and that is, I won't bother reading you the number, I'll just give you the skinny, it's a 2 gig bit DDR3 SD RAM as you'd expect, so that's 256 meg byte, because it's

**Dave Jones:** an 8-bit converter, 250 meg samples, so that seems to be plenty at 256 megabytes per channel. So four of those, you know, one per channel is more than enough. So I wouldn't expect to find secondary ones on the bottom side of the board.

**Dave Jones:** Right next to our display FPGA here is a NetSol S, you might think, NetSol? Who's that? Do they make, is it a networking Ethernet chip? No, this is a SRAM. So this is a 18 meg bit SRAM, so it's 1 meg times 18 bits, and you

**Dave Jones:** can bet your bottom dollar that is going to be used for the intensity graded display on this thing. The 256 levels and all that sort of jazz. Has to be super duper quick and that's why they've got an SRAM in there. And on the other side of that, they've coupled

**Dave Jones:** on a Samsung 1 gig bit DDR3 memory as well. So that's an interesting combination of those two there. And of course you'll note the length matching tracers all in there. Nice little wiggles. I love wiggles. Wiggle wiggle. So right there is a lot of grunt inside this thing with these three

**Dave Jones:** Big Daddy FPGAs and absolute bucket load of memory on this thing. So yeah, they're not mucking around, but you need this. You know, there's probably, there might be $200 worth of parts there. Now as far as the ADC goes, I don't know. Can anyone decode that

**Dave Jones:** pin out? The 1000x Siglent oscilloscope which we tore down previously, it had a Hittite converter in there. Whether or not this is a Hittite one, or one of those National Semi parts or something like that, I don't know. Ooh! PLL clock gen. That's an ADF

**Dave Jones:** 360. Check out the data sheet. I'll link it in down below. It's all about the loop components of course. Oh, it's a PLL by the way. It's an, as you'd expect, a frequency synthesizer. Only up to 1800 MHz. So they're obviously not generating the 2 gig

**Dave Jones:** clock with this thing, because as I said, they don't need it. The ADC over here is a 1 gig sample per second and they're doing interleaving inside the ADC. So that would be generating the 1 gig sample per second clock, not 2 gig samples

**Dave Jones:** per second. But as I said, it's all about this loop stability, the loop components, selecting the right, setting the coefficients inside the registers inside this thing. And that's what Rigol famously screwed up in the 2000 model, was it? They famously got that wrong

**Dave Jones:** and oops! But thankfully they could pretty much fix that in software just by reprogramming the registers in here. And of course everyone wants to see under the hood of the analog front end. And ta-da! There it is. It looks like we have not

**Dave Jones:** 4 identical channels, because look, they're slightly different. Channels, I think this is channel 2 and channel 4 here have this chip here. Slightly different layout, so that'd be a driver. We'll go in there and like a, typically they'll have like a 74HC, you know,

**Dave Jones:** 595 or something like that, just to drive some digital lines and things like that. But otherwise of course the analog sections are absolutely identical. 4 relays which is more than you'd typically find in a front end, I believe. Couple of trim pots because they've got the cut-out holes in the

**Dave Jones:** metalwork to get in there and eh-eh-eh-eh, just tweak the AC performance of this thing. And well, there's not much to it. There's going to be a bit more on the other side of course. Because well, there's not a lot in there, but yeah, probably using

**Dave Jones:** a discrete fit front end and things like that. But this would be a 300, this would be the 300MHz front end. Even, I'm pretty sure, even the 70MHz model would be having, have the 300MHz hardware. And it's just crippled in software, so they've probably got, you know, either they're doing it in software

**Dave Jones:** or like some of the early Rigol units, they're actually doing it as a filter in hardware on the front end. And yes, I will provide high-res photos on EEVblog.com for those playing along at home, but there you go. Not much to it until I take the whole main board out.

**Dave Jones:** Might see a bit more on the underside. Tell you what, some of the soldering's a bit how you're doing around here. It's not going to show up on here, but if I look at it under my mantis in the right light, it really is

**Dave Jones:** there's flux residue around there. It's almost as if, you know, somebody's had a hack at that. Maybe at that little diode there, so hmmm. Varactor diode perhaps? Hmmm. I mean something that comes to mind is that they actually hand-do these to get the different

**Dave Jones:** bandwidths, but I don't know. Anyway, all the usual suspects are here. Analog devices AD8370 variable gain amplifier, 750MHz, not particularly stellar performer, but it does the business for all your different gain ranges and stuff like that. And then you've got your LMH6552, that's a differential amp, 1.5 gig

**Dave Jones:** perfect for an ADC driver, and that's exactly what it's used for. It'll be directly driving the ADC. Doesn't have to go too far. Look. It's only got to go just across the border there. There we go, maybe you can see that flux residue a

**Dave Jones:** bit better, and that cap's just bleh. Not very nice at all. Hmmm. And I was right on the money for the 74HC595, that's the jelly bean you know, serial to parallel latched driver of choice. And another, look, another cap on the second channel there, just bleh.

**Dave Jones:** Too much solder paste? Yeah, it's not a coincidence, this diode here how I reckon, has been hand-done on all four of the channels in the exact location. There it is. See those? And if I go over to this channel here, there it is again.

**Dave Jones:** Look, and the cap next to it. Something's going on there. Are they tweaking those? Is this a hardware tweak for the different bandwidths perhaps? Hmmm. And you can see the difference between the 200MHz 1000X model on the left, and the 300MHz 2000X that we're looking at here on the right.

**Dave Jones:** And you can see that the 300MHz model actually has those two trimmer caps in there. Higher frequency, more parasitics, more issues to deal with, more high frequency stuff that you have to go ee ee ee ee and just trim some stuff. So extra relay in there.

**Dave Jones:** A bit more complicated for the 300MHz version, but similar parts. Similar drivers and variable gain amp. And yep, I was right on the money for the comparators for the digital section there. ADCMP562s, we've seen those before. And they're high-speed PECL comparators, and they've got a whole bunch

**Dave Jones:** of those for all 16 channels. And there's our DAC for our arbitrary waveform generator. It's a Burr Brown, yes. Or TI, whatever you want to call them these days. Anyway, DAC904E that's a 14-bit DAC, and specifically you know, well, one of the typical applications is for ARB generators

**Dave Jones:** like this, so yeah, bang on. If we have a look at the rest of the stuff around the ARB generator, nothing hugely special, just a bunch of relay switching and op amp action. I'm not even going to bother to look those up. But hey

**Dave Jones:** there's the output resistor, there we go. 49.9 ohms. Oh, it's never quite 50. I always find that disturbing. What is your job there, Mr. Little 5-pin pin header? Hmm, we've got ourselves a lattice CPLD down in there. I love how it actually tells you it's a CPLD.

**Dave Jones:** You don't even have to look up the part number for that puppy. So that's, my guess would be that's doing the arbitrary waveform stuff. It's a fair bit away. But I guess, you know, there's the DAC down there, there's all your output amps and everything else, but you know, all your power supply is all

**Dave Jones:** tucked around in here, and there's your ethernet and USB stuff by the way, I won't bother showing you that, or your trigger out circuitry and stuff like that. Nothing fancy-pansy, that'll be going off to the keypad front panel. And Bob's your uncle, couple of line

**Dave Jones:** drivers here, and level converters. But there's our main application processor, the analog devices are Blackfin, which we see in many, many shows. So yeah, common as mud. So they must, you know, they've got a really good little niche market there for these Blackfin DSPs.

**Dave Jones:** I believe, you know, the reason that they choose them, a lot of expertise in China with the Blackfin DSPs, so yeah, that could have a really big hand in it. Anyway, not much doing there at all, won't go into business. Maybe there's like a serial output monitor or something that, you know,

**Dave Jones:** a little interface we can get. Here's a test interface for the production testing and stuff like that, but yeah, apart from that, we've pretty much covered everything I suspect. So that's pretty much it for the main board, I don't think I'm going to

**Dave Jones:** bother to take it out. It seems to be a bit of effort to get, it's not as easy as some of the other scopes I've looked at. So I might just leave that, there might be a couple of, you know, some more passives and

**Dave Jones:** stuff on the bottom of the analogue front end. Not much doing, they'll just be bypassing and stuff on the bottom of the BGAs. Not a huge amount extra I suspect. I think all the goodies are on the top here. Brilliant. ... ... ...

**Dave Jones:** ... ... ... ... I just noticed, someone's had a crack at this before I did. Almost 7 watts standby power, you've got to be kidding me! Unbelievable, you fly to bloody Pluto on 7 watts! And during operation we're looking at about 40 watts there,

**Dave Jones:** power factor of 0.65, and there's our apparent power for those playing along at home. Well, it works, beauty. These, apparently, have LEDs in them. Can't bloody well see them. Ah man, dim as! And that's it for the teardown, no I'm going to resist the temptation and not play with it for this video.

**Dave Jones:** It's just a teardown video. Walk away Dave, walk away from the camera, walk away. Catch you next time. Hi, welcome to a first impressions review of the new Siglent DS1000X series oscilloscope. Quite excited about this one. There's been a lot of anticipation because it's feature set

**Dave Jones:** and value for money. Looks pretty darn impressive. I believe there's only like a couple of people in the world who have got one of these puppies, so you can order it now, but nobody's actually got stock yet. It's coming very, very soon.
