---
video_id: ywewix7DlpI
title: EEVblog #1038 - Uni-T UPO2104CS Oscilloscope Teardown
url: https://www.youtube.com/watch?v=ywewix7DlpI
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 23, "2": 44, "3": 60, "4": 83, "5": 98, "6": 111, "7": 128, "8": 146, "9": 160, "10": 177, "11": 195, "12": 213, "13": 232, "14": 250, "15": 266, "16": 281, "17": 299, "18": 317, "19": 332, "20": 349, "21": 365, "22": 390, "23": 407, "24": 425, "25": 443, "26": 460, "27": 482, "28": 503, "29": 525, "30": 540, "31": 559, "32": 574, "33": 594, "34": 615, "35": 632, "36": 651, "37": 673, "38": 692, "39": 711, "40": 731, "41": 754, "42": 773, "43": 793, "44": 811, "45": 825, "46": 844, "47": 859, "48": 878, "49": 899, "50": 915, "51": 929, "52": 949, "53": 966, "54": 985, "55": 1004, "56": 1020, "57": 1038, "58": 1058, "59": 1081, "60": 1098, "61": 1123, "62": 1140, "63": 1159, "64": 1176, "65": 1196, "66": 1216, "67": 1236, "68": 1252, "69": 1272, "70": 1292, "71": 1316, "72": 1332, "73": 1356, "74": 1372, "75": 1392, "76": 1408, "77": 1432, "78": 1464, "79": 1488, "80": 1500, "81": 1524, "82": 1540, "83": 1564, "84": 1584, "85": 1604, "86": 1628, "87": 1644, "88": 1668, "89": 1692, "90": 1712, "91": 1736, "92": 1756, "93": 1768, "94": 1784, "95": 1804, "96": 1820, "97": 1836, "98": 1856, "99": 1872, "100": 1888, "101": 1904, "102": 1924, "103": 1958}
---

**Dave Jones:** Hi, we haven't done an oscilloscope teardown in a while, and I've had actually this one for a while, but I haven't gotten around to it. It's the Unity UPO2104CS Ultra Phosphor Oscilloscope. Four channels, and that's the key factor here. Up until fairly recently, the venerable Rigol DS1054Z

**Dave Jones:** has practically had the four-channel low-cost oscilloscope market to itself. There basically was no competition, but now more companies are coming out with four-channel oscilloscopes, including Siglent, which I just got this morning. A brand new Siglent, which is going to compete against the Rigol DS1054Z, and you can expect to see that one

**Dave Jones:** very shortly. It's just under embargo at the moment. But there is information on the EEVblog forum for those who want to seek it out, but I have not heard much about this Unity one. Indeed, if you actually go try and buy it, it's really not available

**Dave Jones:** in that many places. But it is a 5, I believe the retail price is $599 US dollars, which is substantially more, $200 more than the $399 Rigol DS1054Z. Street price, but street price on this is about $540 from banggood.com, which is one of the few places

**Dave Jones:** you can get it apart from eBay. So it's not very well-known, I don't know if there's much information out there about it. It has been on the market for a while apparently. But anyway, it is an entry-level 4-channel 1 gig sample per second scope that's obviously going to be shared across

**Dave Jones:** the channels. How many, I don't know. 100 MHz is standard entry-level bandwidth, but it does go up to 200 MHz, so presumably it's got the full 200 MHz bandwidth built into the 100 MHz model. I don't know about any hacks or anything like that.

**Dave Jones:** As always, the things are shared. I might do some stuff at the end or a separate video, but they are pushable. So anyway, let's have a quick 10 out of this puppy, because we haven't torn down a Unity oscilloscope before. And I've been critical of Unity

**Dave Jones:** stuff before, because their production quality is very hit and miss. They make some good stuff and they make some really bad stuff. Hats off to them. They have come good on multimeters and things like that. Recently they're now getting them independently UL certified and tested

**Dave Jones:** and all that sort of stuff, so they seem to be coming along. So it'll be interesting to see what's inside a Unity oscilloscope. Let's get to it. And because I know people will want to see it, here's a quick comparison with the Vendorville 1054Z here.

**Dave Jones:** It's a little bit bigger, weighs about the same, it's fairly hefty, so expect to see a lot of metal and stuff inside. And the user interface is much less cluttered than we get on the Rigol. The Rigol is rightly criticized for its user interface,

**Dave Jones:** and it's just been a bit difficult to use. So as I said, it's fairly hefty, it's got the requisite tilting bail on the top, it's a bit yawn-worthy, doesn't have feet on the front to actually tilt it like that. But if we have a look on the back here, which is rather interesting,

**Dave Jones:** it's got these feet here which just don't, they just flip like that. So I'm not sure what the deal is. It does really make it, and not, you know, this thing is not going to fall over at all. This is like absolutely incredible in terms of stability, really feels good.

**Dave Jones:** Now these feet do actually lock into place, you can actually put them down like that, and it sits very straight, but like almost to the point where it feels like it's tipped forward. Maybe if you had it up on a bench or something like that you'd use it in that configuration,

**Dave Jones:** but otherwise, nah, feet out. Anyway, Ethernet standard on the thing, you've got your mains with a little switch on the back, and external trigger and pass-fail output as well. 30,000 waveform updates per second are claimed on this thing, so, you know, it's pretty well-specced.

**Dave Jones:** 32 meg of sample memory as standard, so that's awesome. That beats most low-end scopes on the market, probably maybe all of them. I'm not sure, 100 VA max. Jeez, we're going to have to measure the power consumption on this thing. Looks like a big-ass fan on the back.

**Dave Jones:** You can see all the metal work, we've got a Kensington lock there. And that's about all she wrote. Anyway, you know what we say here on the EEVblog, don't turn it on, take it apart. Oh, I didn't even see the poor warranty void sticker on there.

**Dave Jones:** Ah, screw that. We are not in like Flynn yet. As I said, all metal work, fairly hefty little beast. Very typical construction of all low-cost scopes. I'm not sure if they naturally evolved this way, to have like the big main board and then the metal shield on the back with the screws around the side,

**Dave Jones:** and then the metal shield lifts off and the power supply is usually bolted onto the back here. You can see the standoffs, the integrated standoffs in there. And then it flips up there, it's pretty much par for the course. I'm not sure if they're copying each other or that's just a natural engineering evolution of these types of scopes.

**Dave Jones:** Anyway, as for airflow on this thing, air comes out the back here, sucked in from only the one side over here. So it's going to flow presumably all over the power supply processor and out this side. So that's not bad. But, let's lift it up.

**Dave Jones:** I think I've got, yep. Yep, she's going to come off. There we go. We are in. Oh, hang on. I hate it when you've got to unclip to get in like Flynn. There you have it. We are in like Flynn. As expected, just a single board construction.

**Dave Jones:** But geez, there's not much on there. Pissant little heat sink here for the FPGA that close. Look, anyway, it looks like we can get the shields off the front end. That's a pretty decent layout. I don't mind that at all. But the capacitor down here, bent over.

**Dave Jones:** That's a bit how you do it. And it's so close to this 32 kilohertz watch crystal here that they've had to put the little insulating sleeves on there. That's hilarious. Like, what the hell? Somebody's put the footprint, laid out the board. And the footprint for the crystal is inside the vertical footprint of, well, I guess it's not.

**Dave Jones:** It looks like the silkscreen's going off here. So they had the intention, and I guess those lines indicate that maybe it, oh no, that could indicate the negative side there. But, like, so they had the intention to lay it flat. But just laying that across there, I just think that's hilarious.

**Dave Jones:** Anyway. Anyway, they have gunked that down, haven't left it flapping around in the breeze. Nice. Let's have a look inside here. It looks like they might have rolled their own power supply, which is not that common. Mostly you farm out these things. But anyway, well, they could have still farmed it out.

**Dave Jones:** I don't know, is that KC2? I don't know. Are there any, maybe that's the manufacturer. Maybe that's the designer and manufacturer. Maybe they have farmed it out. But anyway, it looks neat and tidy. I don't mind that at all. Of course, I took the shield off to get at this.

**Dave Jones:** Can't say I'm a big fan of the earth just going over into the connection over here and going down via that. Probably would have preferred a direct crimp connection and a direct, you know, stud on there and screw. But, you know, it's fine.

**Dave Jones:** Ooh, got some heat shrink over there. Obviously we've got a fuse in there. Yeah, 5x20, fuse, vertical. Jeez, got plenty of room in there to put a fuse holder on the board. Like tight asses. Unbelievable. Anyway, heat shrink around a thermistor there, just to contain it if it explodes.

**Dave Jones:** It's got all the requisite stuff, your common mode filters, everything else. I don't know, the transformer. Who does that? I don't know. Same company makes both at least. And our requisite SAMWAR caps, you know, they're par for the course. Are these ones SAMWAR?

**Dave Jones:** Down there, no. What are they? Minix. Oy, okay. But the other ones, they look like SAMWAR as well. So at least they've matched them, 105 degrees C. Ah, she'll be right I guess. Don't see anything offensive on the back here. They've got the high voltage isolation slots across the diode bridge there.

**Dave Jones:** There's the earth going over to the stud there. They've got the cutout in there. They've got the cutout under the tranny here. And well, that's all she wrote. It's all isolated nicely. And nice attention to detail. They've got the elephant hide on the bottom there.

**Dave Jones:** Not elephant hide. That's pretty cruel. Elephant hide. Insulating sheet, for those who don't know. And there's absolutely nothing doing on the Ethernet and USB and IO board down here. They've just got the 2-pin header goes over to the pass fail and whatnot output.

**Dave Jones:** So there's only 2 wires on there. So where's the return path, I hear you ask? Where's WALL-E? The chassis. Earth. Thank you very much. Few fan aficionados, I'll let you guess that one. I couldn't be bothered unscrewing it to find out, quite frankly.

**Dave Jones:** Alright, let's have a look at the main board under the Togano microscope here. It's version 1.07. Things have had several sucks at the SAV. Which is not uncommon, of course. And all the caps around here, these are wet electrolyte tights. Because you can see the cross, the vent cross mark on the top.

**Dave Jones:** So you know they're not solid aluminium electrolyte capacitors. Got a couple of low dropout voltage regs there. Nothing special. That looks like it's the LCD, does it? Coming from, ta-da, the main applications processor. For all you TI fanboys, there it is right there.

**Dave Jones:** And that's a bit of a beast. That's the Sitara line ARM Cortex-A8 processor, up to 1 gig. I will have to look at, well, 100 there could be the 1 gig model. Anyway, we've got all the termination resistors over here for the driver.

**Dave Jones:** By the looks of it. And you can see we've got coupled into some micron memory there. We'll have to put that into our micron part decoder. But you can see all the little squiggly tracers in there trying to length match all that DDR RAM into the main processor there.

**Dave Jones:** But yeah, that's not your sample memory. So don't get too excited about that. And you can see all the tracers buggering off over here. There's some JTAG pins, do we have? Anyway, they're going over to this puppy over here. And that's a National Semi 83848, that's an Ethernet thigh.

**Dave Jones:** So that's buggering off via this ribbon cable here. Back to the rear panel, which has the Ethernet and whatnot on it. And, well, it got itself a little fuse-y in there. Wonder what that's doing. A couple of inductors. Anyway, here is our memory.

**Dave Jones:** So that's our sample memory, 6YJ17. That's very different to the one that we had over here on the applications processor. So this will contain our 32 meg samples. Let's decode that. So as it turns out, that's an MT41K64. Anyway, blah, blah, blah, blah, blah.

**Dave Jones:** Sure enough, that is 32 meg per channel, because there's 8 bits per channel. Awesome. So there's obviously no second one on the bottom there. All the sample memory's inside that. Unless there's another one for, like, the phosphor display and other stuff, like segmented memory and things like that.

**Dave Jones:** Hmm. And above that is our mystery FPGA, which we'll take a look at. And then, oh, don't you just love all the matched lines? Beautiful. Thing of beauty is a joy forever. Ah. Behold the WonkaMobile. Thing of beauty is a joy forever. Anyway, the Cypress CY7C1360.

**Dave Jones:** That is a 9 meg bit, 256K by 32, 36 pipelined SRAM. So that'll be doing all your fast sampling, and then it'll be dumping it into the sample memory or whatnot. So, yeah, we've got a bunch of fast SRAM attached, as they always do in these scopes.

**Dave Jones:** And, of course, there's no surprise for guessing what's coupled into the other side of the FPGA there is the HAD1511 or HMCAD1511. Let's take a look. That's the HMCAD1511. Analog devices, we've seen this, like, time and time again on practically every scope on the market.

**Dave Jones:** In fact, they're the typical applications. Digital oscilloscopes, that's pretty much what they're targeted for. And yes, single channel, one meg sample per second, they're doing nothing fancy. It's all done in here. It's just basically, you know, off-the-shelf app note type stuff, apart from the front end, which you've got to roll your own, everything else,

**Dave Jones:** and the stuff you've got to do in the FPGA, the phosphor technology, sampling technology, things like that. But apart from, you know, the ADCs, they're just all off-the-shelf stuff. And yes, if we turn on all four channels, I don't even have to power it up to find out.

**Dave Jones:** It's going to limit it to 250 meg samples per second, which is going to completely suck if you've got the 200 megahertz bandwidth. It's barely acceptable. In fact, it just is technically acceptable for the 100 megahertz bandwidth one. 2.5 times the sample rate there with sine x on x interpolation, that's good enough.

**Dave Jones:** But for the four channels, but no good for the 200 megahertz bandwidth. But we've seen this in other scopes, so it's just par for the course. That's what you get in the low-cost scopes. Because these chips are expensive. They're not going to have two of them dedicated in there to the two separate channels.

**Dave Jones:** It just costs more. You can't get the price point. And then if we move up, up, up, up, up, up, up here. Oh, what's that? I'll give you one guess when you've got a single differential pair going out like this, and looks like you've got single line coming in,

**Dave Jones:** and all these resistors and caps and a couple of inductors all around the outside like that, that is our PLL, our phase lock loop that generates our one gig sample per second. So as famously, Rigol actually screwed up some parts in this, and it wasn't very good.

**Dave Jones:** They managed to fix it in software in the internal registers, but anyway, for those who, I know there are people who love to decode these sorts of things and check the values and things like that to see if they've got it right, but yeah, you don't know unless you've got all the, like, you can goof it up.

**Dave Jones:** You can check, but yeah, anyway, let's get a part number on that. It's really hard to get the light right. There you go. I've got to put my hand, it's a glare from my lights overhead. The ADF 4360, for those playing along at home.

**Dave Jones:** Dash 7. And there it is, the integrated synthesizer and VCO. I think it's the same one we've seen in other ones, 350 meg, 218 meg output frequency range, so yeah, it's all par for the course, and then, like I said, you can go in and have a look at all the registers, things like that.

**Dave Jones:** It's all, you know, here's all your reference input section, blah blah blah, how to lock it and all that sort of jazz, but here are your registers, which if you don't set up these correctly, you can come a gutzer. Or you can potentially fix hardware goofs, like happened in the Rigol unit.

**Dave Jones:** I'm sure they probably fixed it in production, like newer units, but years ago when they goofed that up, yep, they were able to just pull a few little tweaks in the registers, I believe, to pull that sucker back into lock. So that's obviously differential output, diff pair running down there,

**Dave Jones:** standard FR4, none of this controlled impedance dielectric rubbish, and that just goes into our ADC down there. So that's about all she wrote. Let's move up here, shall we? This is the... oh, hello, hello, Mr. Bodge. Anyway, this is all above the front end here.

**Dave Jones:** I'll show you, everyone wants to see inside the front end, but this is all the stuff up the top here, so this will be trigger stuff. This does not, this one does not have any option for mixed signal or for like a function gen output or anything like that.

**Dave Jones:** Oh, we've got more up there. There you go. Look at that. Wow. It's all over the shop. What's that? And that is a Analog Devices 5628. Let's go to the data sheet, because I'm shooting this on one monitor here. I haven't booked up a second monitor.

**Dave Jones:** I've got to go, whoops, over there. Anyway, that is a dense DAC. Ooh, 5 ppm per degree C with the on-chip reference. Very nice. So that's doing all your offset stuff and things like that. So that's not a bad little DAC. Wow, I like that.

**Dave Jones:** Anyway, that's a real interesting block there. So I wonder what's going on there. Anyone want to reverse engineer that? There's a bunch of discrete trainees and things in there. We've got ourselves a suspicious looking diode over here, but that's interesting. Huh, they've got some sort of amp.

**Dave Jones:** Some sort of discrete amp or something like that perhaps. Anyway, let's go down here. We've got another one of those. Yep, we've got another one of those DAC jobbies. And I've got to have a 4053. Everyone still sells those by the bajillions. And they're in everything.

**Dave Jones:** They're in absolutely everything. So then we've got 4053s again. Nothing special, nothing special. Jeez, it's a bit different. 4094s, yes, thank you very much. Beautiful. And we've got DACs coming out our rear end. Look at that. DACs all over the shop. Anyway, that's all the support stuff.

**Dave Jones:** Nothing particularly high frequency, but look at that bodge job. Wow. Look at that. They've whacked in a cap across there. And looks like they've done a triple. Is that a triple stacker? We have a triple stacker. Oh no, I think it's only a double stacker.

**Dave Jones:** And of course here's what a lot of your aficionados want to see. The analog front end in glorious HD. Bit of flux residue left there, but we'll excuse them for that. Looks pretty par for the course, doesn't it? Yes, all the channels are identical.

**Dave Jones:** Play spot the difference. High res photo. Oh no, no, no, not quite. Not quite, because you'll notice that there's no big chip in the corner. That's probably a mux for the digital lines. We've seen this before. So there's slight differences, but the actual, like in terms of just driving,

**Dave Jones:** they've shared a couple of these I.O. digital I.O. expanders probably across, I think you'll find that part number in there is probably a, no, no, it's a mux. It's a mux. Anyway, they've shared those across, but the actual, is that a bodge? We've got one!

**Dave Jones:** We've got a bodge. Look at that. There we go. Down here as well, no? What's going on? That one there, no? It's all good. So what on earth is going, what is that? What have they done? It's like a cap in there instead of a resistor.

**Dave Jones:** What? And of course the main jobby we want to see here is the LMH 6552. And I do believe we've seen this before. It's a 65 gig fully differential amp, and that drives the ADC and that provides the gain for the various ranges.

**Dave Jones:** And there you go. Differential ADC driver. You know, differential line driver. Because that's basically what it is doing there. So it's taking the 50 ohm single-ended source here and basically giving you differential pair over here into your ADC. In this case they're showing a 14-bit job.

**Dave Jones:** But yeah, that's I do believe we've seen that exact part or very similar in most of your low-cost scopes on the market. Not only in addition to that, you can see several other sucks of the salve here. Look at that. What's doing there?

**Dave Jones:** Someone's had a go at that. Thank you very much. And yep, down in this channel again. Look at that. Are they the same? Yeah, they've added the 365. So they've modded those after the fact. Somebody's hand soldered those and they decided, no, we want to change that

**Dave Jones:** resistor after they've done their reflow production and changed everything. Anyway, genuine Omron relays. And there's our little trimmer caps. We've got our solid-state relay down there. OPA for the course. I think if you reverse engineer this you'll probably find that it's very similar to most

**Dave Jones:** low-cost digital scopes on the market. And at the end of this video I'll link in a very interesting reverse engineering of the Rigol DS1054 front end. That's been a very popular video. A lot of people liked that one. I won't bother reverse engineering this one though.

**Dave Jones:** Leave that up to someone else. You thought I'd forgotten, didn't ya? Let's get in there and wipe it away. Surprise, surprise! Spartan 6 FPGA XC6S LX45 for those playing along at home. I believe the exact part we've seen in other low-end scopes. Jeez, Xilinx got the

**Dave Jones:** design win all over the shop. In fact, is there a single scope out there that uses an Altera part? I'm not sure if there is. Hmm. So there you have it. That's not too bad at all. It's exactly what you expect in a $400-$500 class scope.

**Dave Jones:** We've got the same ADCs, the same FPGAs, the same application processors, the same front end drivers and everything else. That, you know, same memory, everything else that you'd find in practically all of these low-end scopes. There's not much difference. The build quality is

**Dave Jones:** fine. No worries whatsoever. It's all going to come down to you know, software, implementation, things like that I suspect. And I'm not actually going to take the board out any further. I'm not that fast. There's going to be, you know, bypass caps. I don't think there's any more memory

**Dave Jones:** because we saw that the memory could handle all the channels 32 meg per channel I think. So I don't expect to find much if anything interesting on the bottom. So yeah, I just want to get around to powering this thing up. ... ...

**Dave Jones:** ... ... Takes almost 50 seconds to boot! It's infuriating! Anyway, what does it draw? 44 VA and 26 watts. Jeez, that's not a terrific power factor is it? But anyway, 26 watts. So it says like 100 VA on the back, didn't it? Jeez, not even drawing half that.

**Dave Jones:** And 2.13 watts in standby. That's at least a trip to the moon. Seriously. Mars, maybe. And for those wondering fan noise on the thing, not as bad as the Rigol 1054Z. It's not too bad, like in a quiet lab you would hear it, but you know, look, if you want to put a silent

**Dave Jones:** fan in any of these scopes, by all means just take it apart screw the warranty void sticker and change your fan. Or you can cheat with the warranty void sticker. I've done a video on that. I'll link it in at the end. Stay tuned.

**Dave Jones:** What the hell is this? This is to select... show which channel is selected. They put this like weird gradient thing right through the center of the stuff you want to see. You want to read. Unbelievable! What idiot thought that one up? I find the display quite bright and

**Dave Jones:** easy to read. Don't mind it at all. This is interesting. Look, on the channel information here, we can actually, if we go into next we can actually set a bias voltage. Look at that. That is fascinating. We can set a bias voltage on the front end.

**Dave Jones:** I don't think I've ever seen a scope do that. And of course that is different to our position. Like that we can set a DC bias. Wow! Hmm. Maybe to use to shift? You know, if you're measuring, if you want to keep DC coupled

**Dave Jones:** you don't want to use AC coupled, you want to keep DC coupled and then shift it into the range of the ADC perhaps. Interesting. And I'm trying my standard waveform intensity thing with a 1 MHz carrier with modulated 1 kHz 100%, just to check the 256

**Dave Jones:** level ultra-phosphor intensity display. Look at this. Look at these black artifacts. This is not the camera. I'm actually seeing this. This grid is disappearing in the background where 2.8 Meg depth on here and look, on this side here, it's like chopped off and I don't really like the way it overlays there just with the black.

**Dave Jones:** It just looks like less chopping off the graticule there. You can get rid of that. And the waveform, look, overlaps the grid on the end here. I don't like that at all. And if I do the intensity modulation, I mean, it's got... I'll show you compared to the

**Dave Jones:** Rigol in a minute. You know, it's okay. It's got the nice bright spots in the center where they're supposed to be. It's not the best I've seen, but it's certainly quite adequate. Anyway, it does have a couple of interesting things like that DC bias that we saw

**Dave Jones:** there. I'm not sure of another oscilloscope that actually matches that. I stand to be corrected on that, but anyway yeah, this won't be a review. No. I can't go into it. Anyway, what it does have, another interesting thing, independent time base. Turns all four channels on, and we can modify those

**Dave Jones:** presumably. We've got four different time bases. Modify those independently. You cannot switch off the channels. Function is disabled in independent mode. You've got to have all four channels on, but you can get different time bases. There we go. That is neat. Channel 1, change, yeah.

**Dave Jones:** Channel 3, all the way with LBJ maybe. There we go. Anyway, it's got a few interesting features, but yeah, memory depth, your sample modes, your serial decodes. I don't believe your serial function is disabled. Yeah, they sent me a Reviewscope, doesn't even have serial

**Dave Jones:** decodes. So presumably I've got to go in there and figure out what the hell is going on. SIMOMETER. Brilliant. And trigger select IP config, blah blah blah. Real time date and clock. DDS. Function is disabled. Where is the DDS? There's the hardware and software version for

**Dave Jones:** those playing along at home. Anyway, I hope you enjoyed that look. Let's give it a auto, shall we? See what happens. But anyway, I hope you enjoyed that teardown. If you did, please give it a big thumbs up. As always, high res teardown photos available on EEVblog.com, which links to my

**Dave Jones:** Flickr account. And a lot of people use those photos to like do reverse engineering and hacks and things like that. I have no doubt the full bandwidth in this is that front end has the full 200MHz bandwidth. Can it be hacked? My initial impression, I don't know.

**Dave Jones:** I have to play with it some more. The hardware's okay. The look and feel of it, not, you know, it's a little bit toy-like, but it's got all the requisite stuff. But the price point, I hate to say it, but you know, $599 retail

**Dave Jones:** or $540 US street price for a 4-channel. I can't believe I'm saying this, but it is almost 2018 now, and a 4-channel, 100MHz scope with, you know, well it doesn't include the serial decodes, everything else is $499. Whereas the Rigol, granted, it's the lower bandwidth

**Dave Jones:** one, so you're not quite comparing apples and oranges there. It's 50MHz as opposed to the minimum 100 here. But of course the Rigol has the famous hack, whichever one, which gives it the full memory depth, the full bandwidth, the full decoding capabilities and things

**Dave Jones:** like that. I believe that's still a thing, which is what's made it wildly popular. But for my mind, the thing that differentiates a scope on the market is the number one thing is the number of channels. And it's interesting that more players have came in to try and compete with the Rigol here, and

**Dave Jones:** as I said, Siglent have a new one, and I think GW Instec have one, and a couple of players. So, almost shoot-out time, is it, for entry-level 4-channel scopes. But this one is quite pricey, so yeah, it'd want to have everything for free, and it doesn't even have the serial decodes.

**Dave Jones:** Whereas the new Siglent, which is going to be cheaper than this, 4-channels, 100MHz beats this on price, and it comes with the free serial decoding. So, yeah, I don't know where this leaves the Unity in the market, and doesn't really have anything hugely special about it.

**Dave Jones:** So, yeah, it's going to have a hard time in any shoot-out, I suspect. But, anyway, look out for the Siglent one coming soon, and I'll probably have to do a video playing around with this thing, and I might, I don't know if I'll leave it for the shoot-out or do a separate

**Dave Jones:** mini-review or something like that. Because people keep asking, why don't I fully review scopes? They take a lot of time and effort. It could take like a week's work to properly review a scope and things like that. And with stuff going on at the moment, I don't necessarily

**Dave Jones:** have the time to do that. But, anyway, I'll see what I can maybe a mini-review playing around. Anyway, hope you liked it. Catch you next time. Time's base. I just noticed that. Time's base. Chinglish at its finest. I love it. But it doesn't seem to have an XY mode.

**Dave Jones:** Like, yeah, we've got the independent mode, which is independent time bases for all the channels, which is cool. But, like, I can't find the XY mode. What's doing? What's doing? I don't get it. What? People still use XY mode? Give me a break.

**Dave Jones:** Give me a break.
