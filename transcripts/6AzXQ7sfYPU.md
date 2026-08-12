---
video_id: 6AzXQ7sfYPU
title: EEVblog #1124 - Rigol 7000 Oscilloscope Teardown
url: https://www.youtube.com/watch?v=6AzXQ7sfYPU
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 28, "3": 38, "4": 53, "5": 68, "6": 82, "7": 97, "8": 106, "9": 115, "10": 130, "11": 139, "12": 160, "13": 180, "14": 190, "15": 205, "16": 212, "17": 225, "18": 244, "19": 263, "20": 272, "21": 284, "22": 299, "23": 312, "24": 325, "25": 339, "26": 350, "27": 377, "28": 391, "29": 402, "30": 421, "31": 448, "32": 459, "33": 473, "34": 485, "35": 499, "36": 508, "37": 519, "38": 529, "39": 543, "40": 553, "41": 569, "42": 582, "43": 598, "44": 612, "45": 630, "46": 647, "47": 663, "48": 672, "49": 683, "50": 693, "51": 707, "52": 722, "53": 733, "54": 747, "55": 765, "56": 785, "57": 802, "58": 818, "59": 831, "60": 846, "61": 857, "62": 874, "63": 891, "64": 905, "65": 920, "66": 930, "67": 948, "68": 959, "69": 970, "70": 986, "71": 1003, "72": 1017, "73": 1029, "74": 1040, "75": 1053, "76": 1067, "77": 1080, "78": 1094, "79": 1104, "80": 1125, "81": 1133, "82": 1149, "83": 1159, "84": 1170, "85": 1180}
---

**Dave Jones:** Hi, it's teardown time. We've got the brand spanking new Rigol MSO7054. It's a 500 MHz, 10 gig samples per second, four channel scope. It uses a brand new custom ASIC, the Phoenix chipset.

**Dave Jones:** So, it makes Rigol one of the major players now that they have their own custom ASIC for oscilloscope front ends. Not only do they have it for the processing, but they also have one for the analog front end, I believe.

**Dave Jones:** So, super impressive stuff from Rigol. It's taken them a long time to get there. So, any schmuck company can design an oscilloscope. Hi, you can see the glarey screen.

**Dave Jones:** That's terrible. Muriel is glarey screen. Look at it. Awful. Hi. Um, any schmuck can design a scope. Well, you know. Anyway, anyone can design a scope with a big ass FPGA and off-the-shelf ADCs.

**Dave Jones:** But, to roll your own custom ASICs, that's some serious coin and serious commitment. So, let's check it out. Just a few screws on here. It's pretty big scope, $2,700 retail minimum for the four channel 100 MHz.

**Dave Jones:** And as with all the big players, everything is optional extra. So, anyway, let's rip the damn thing open. So, we do have the 500 MHz model here. And that is the serial number for those playing along at home.

**Dave Jones:** But, I believe the hardware is absolutely identical for all the models. Everything's software upgradeable. So, you pay your 2,700 bucks and you get your 500 bandwidth, but you've either got to hack it or pony up the money for the options, just like the big boys.

**Dave Jones:** By the way, not a fan of the feet on this. I think they just like I like them. The feet at the back are fine. Is that rubber? Yeah, I think it is.

**Dave Jones:** Anyway, it's not as rubbery as other rubbery feet, but it just doesn't seem to stick in place. There's like just not much force required to flip it back. I don't like it.

**Dave Jones:** You bet your ass we're going to avoid the warranty. Yeah. I think every scope manufacturer is colluding to have exactly the same way to get their scopes open these days.

**Dave Jones:** Two screw two screws on the bottom of the case and two in here. They're probably meddling in the damn elections, too. And of course, there'll be nothing under here except the metal can.

**Dave Jones:** Oh, hang on. What's going on there? Hello, McFly. There's nothing There's no holes under there. What did they put the mesh there for? Okay, so what's obviously going on here is that somebody designed the case and they went, "Well, we're probably going to need a lot of air flow on this puppy.

**Dave Jones:** Maybe, you know, air flow in here and air flow out here, for example, where the fan blows out." Big-ass fan, by the way. It's absolutely massive. Shame it's like bigger could potentially be quieter because you can move a greater volume of air for a lower RPM.

**Dave Jones:** But anyway, so like they designed the molding the case and decided, "Nah, we'll probably just suck in the air from the side here." And you can see that on the side of the case there.

**Dave Jones:** Has it got it on the other side? Yep. From the sides, nothing on the bottom. And they decided, "No, we're not going to do that, but we don't want to redo the molding of the case, so we can't just have the metal sticking out visible through the back holes.

**Dave Jones:** So, we'll just put this mesh on it that makes it look, I don't know, meshy." Power supply going to be on the back here? I don't Oh, yeah, it is.

**Dave Jones:** It's going to be mounted there. You can see the mounting holes. And we're going to see the big-ass fan, and we're in like Flynn. Nice. There's our four analog front ends, all nicely Oh, jeez, that's They're like nickel screening cans.

**Dave Jones:** I really like the look of those. We've got two two custom A6 up here. They're our ADCs and sampling engines and that well, the new Phoenixy chipset. Oh, got some real old school relays and a battery and one little piss ant um FPGA or processor under there.

**Dave Jones:** Can see a little another Spartan 6 FPGA up there. There's our sample memory. And Bob's your uncle. Geez, it's pretty sweet, isn't it? Look at all the uh nicely laid out um DC-to-DC converters here for all the uh rails I need it for you know you probably got 1.1, 1.5 volts, 1.8 volts.

**Dave Jones:** Goodness. When I was a boy Well, I think I was on the money with the rails here. Let's go in and have a look at them, shall we? They're thoughtfully labeled.

**Dave Jones:** 1.2 volts, 1.0 volts, 0.9 volts, 1 volt, 2.0 volts, 1.8 volts, 1.5 volts, 1 volt, 3.3 volts, 3.3 volts again. I guess they've got to have two separate ones.

**Dave Jones:** Keep them one's digitally, one's analog, maybe. Uh cuz it wouldn't make sense if they're both digital. Um and 5. oddball 5.5 volts and 5.5 volts. Thank you very much.

**Dave Jones:** Uh sorry. Almost forgot 20 volts for all you 20 volt rail fan boys. Oh, and little sneaky bastard 5 volts in there. And also plus minus 15 volts. Obviously for large scale uh analog stuff.

**Dave Jones:** And we've got more over here. Just some uh local linear regulation 1.8 volts, 3. 3 volts uh probably for that uh Spartan there or whatever processor jobby that is there.

**Dave Jones:** Tons of rails. That's the problem with like these newfangled modern uh FPGAs and um chips. They just need so many different rails. It's insane. JUST UH 0.75 VOLTS. WELL, hello McFly.

**Dave Jones:** Can we make it uh any more obvious that they're doing some hardware version configuration with this Spartan 6 FPGA? Geez, I even got the JTAG there just ready to go.

**Dave Jones:** Um like what sort of hardware configuration like hm because I thought everything was software upgradeable in this thing. Interesting. I get the distinct feeling that this label in here might make sense if we actually get the serial boot output for this thing, the debug output.

**Dave Jones:** Hm. Obviously, this is our applications processor here. This is our operating memory. You can see all the serpentine trace length trace length matched traces in there. That's a mouthful.

**Dave Jones:** Um and yeah, it's probably I don't know similar to what we've seen before. We might even be able to get that if we can get Haven't looked for the serial thing for this actually, the serial boot loader interface.

**Dave Jones:** Hm. Could it be up here perhaps? One of these? It's not labeled. Rigol innovation or nothing. Fantastic. Gold plated, too. And apparently, this is this one um I believe I think I have a vague recollection that was the code name for this new scope.

**Dave Jones:** Thing is, it's incredibly Spartan, isn't it? I mean, you know, applications processor, memory, we've got like a bridging FPGA up here, which is kind of between the two. So, whether or not all this flows into the Spartan I mean, I believe I'll get to this um ADC and then applications the new Phoenix chipset, a bridging FPGA applications processor, and the rest is just miscellaneous housekeeping.

**Dave Jones:** Obviously, on the video side of things, they've got a HDMI driver up here for the excellent HDMI out on this thing. Fantastic, although I don't believe it scales. It'd be awesome if you could get like full HD out or even more.

**Dave Jones:** That would have been fantastic if you had get the real estate to do that. You wouldn't need need more than full HD, but but unfortunately, it's only limited to like uh 1280 by um 768 or something like that.

**Dave Jones:** Yeah, there's just remarkably little inside here. Um ADC Phoenix chipset sampling memory got some miscellaneous uh stuff down here, which I don't know cuz this is not the external input.

**Dave Jones:** They've got the external input all the way over here and you can see there's not much uh circuitry around the uh external input there. So, uh but it's good that you get a four-channel scope with an external input.

**Dave Jones:** So, you don't waste one of your channels if you need that external uh trigger. So, that's really uh quite nice, but it obviously can't give you like a a fifth waveform or anything like that, I believe.

**Dave Jones:** But apart from that, you know, rest of it's just uh housekeeping. Um of course, we've got our uh logic analyzer down here. I believe it uses a just an off-the-shelf PCI connector.

**Dave Jones:** That's very nice. They're fantastic connectors. Should be using them for everything. Um I've used them in test jigs and all sorts of stuff. They're great. Um they've got some more rails minus 3.4 volts.

**Dave Jones:** Um What? 4 volts? I mean, you know, what's what? So, that's just uh yeah, uh some local regulation. That'd be for your uh analog supply here. Uh what else have we got?

**Dave Jones:** Um and then just a uh probe compensation output. Um that's all your logic analyzer stuff. We'll take a close look at those. And then we've got our two uh signal generator outputs here.

**Dave Jones:** So, where's all the circuitry for the uh sig gen? It doesn't seem to be there. Is it on the bottom? Beulah? Beulah? Copy that. I have no idea about an Adafruit fan, anyone, but it's not that like this thing is not that uh silent.

**Dave Jones:** You can certainly hear it. It's not overly loud, but anyway, here's our power supply. Looks neat and tidy. I forgot about the mains input down here. Very nicely uh crimped and lock nut terminated down to the chassis there.

**Dave Jones:** Brilliant. And this looks neat and tidy, doesn't it? It's the Jackal. Check it out. The Jackal PCB version 1.00. Geez, don't trust that. All right. Anyway, we've got craps on caps down there.

**Dave Jones:** That's how you're doing on the output. Unbelievable. Someone's gone a bit silly with the snot gun. Oh. I cannot see the brand of the main DC cap here, but I presume it's a craps on as well.

**Dave Jones:** So, yeah. Anyway, that all looks more more snot. Look at that. Wow. So, that's neatly laid out and it'll be perfectly fine if it was like a DSR 1000 series Rigol, but you got to remember this scope with like fully optioned up sells for like 11,000 US dollars.

**Dave Jones:** Yeah, I would want a better quality components in my power supply for 11,000 dollar scope. Well, hot damn. This is serious business. Look at this. 84 degrees. I'm sure it's going to creep up to well over 85 degrees on the ADC ASIC.

**Dave Jones:** No wonder they need the huge ass fan in there. Got almost 74 on the Phoenix chipset up there. The front ends are so hot, I can't keep my hand on there.

**Dave Jones:** They've got to be well over 50. They're going to be talking 53 degrees on the analog front ends. And I'm not doing anything. Like the scope's not working hard.

**Dave Jones:** It's just well, scopes work hard all the time. They're always sampling at 10 gigabits per second. Applications processor, almost 64 degrees. No wonder they need this big ass 120 mm fan in this thing.

**Dave Jones:** If we have a look at the floor here, you can just see the relative temperatures. You can't see the analog front end cuz they're reflective and stuff like that.

**Dave Jones:** You can see little hotspot over there on the And oops, I think it shut down of its own accord. So, might have some over temperature monitoring. You'd probably expect that.

**Dave Jones:** That's probably they would have When they're customizing the ASIC, they're probably measuring the temperature in there. Again, not enough air flow, it gets too hot. So, I was searching around for the serial debug output and I thought, well, one of these headers up here, but it's not they These look like a JTAG headers by the looks of it.

**Dave Jones:** But, this Spartan 6 FPGA here, if you follow the money and a couple of those traces over here leads to a three-way pin header over here and aha, we got one.

**Dave Jones:** There we go. 115K board. So, we'll whack that into our terminal program and let's boot her up. All right, I'm going to go switch it on. Let's go. And we're in like Flynn.

**Dave Jones:** Rigol, dirty. It's dirty. Dirty, filthy buggers at Rigol. Update timer was detected, blah blah and data bitmap bitmap one. Oh, there you go. Let's see, can you change like the boot bitmap screen and stuff like that?

**Dave Jones:** Touch driver. We're in to a root menu. Cannot create socket for UDP 6. Joshua, I haven't even got the send hooked up. Sorry. Dope. So, we're in on die ECC Oh, god.

**Dave Jones:** Keep spewing stuff out. Rigol, you dirty I2C. Oh, this is great. Flamingo Linux kernel, uncompressed, blah blah blah blah blah hash value. I'm sure some people out there can make heads or tails of all this rubbish.

**Dave Jones:** So, just cling on to me. Sorcery code bench light sorcery. I don't know there's some voodoo sorcery going on inside this new Rigol scope, let me tell you. Some dirty voodoo going on.

**Dave Jones:** I'm going to have to look through it carefully to find any reference to that hardware configuration stuff because we have hacked scopes based on that before. All right, I like the look of this.

**Dave Jones:** Hit any key to stop auto boot. Whack a key as in I've plugged in a USB keyboard. Did we get it? No. Nope, it didn't stop. I was pressing the keys, but uh nobody time.

**Dave Jones:** And by the way, it doesn't seem to boot with the uh transmit line connected. So, it's only the receive line uh that seems to work. So, don't know what's going on there.

**Dave Jones:** So, if you follow the money on the boot code, turns out this application processor over here is actually a Xilinx Zynq processor, which is a combined FPGA and ARM processor, very powerful beast that we've seen power entire scopes before uh like the low-end ones.

**Dave Jones:** But, in this case, uh it just looks so tiny tot compared to these beasts. Now, either uh somebody was thinking on the PCB layout here or the uh system like, you know, assembly uh people went, "Oh, look at that.

**Dave Jones:** We've got a ground point there. Um we can just cable tie that. Neat." And it seems like this board just won't lift out on its own. It looks like you've got to take the entire metal cage out first with these clips.

**Dave Jones:** Bummer. That was tricky. Wow. But, we're in. Awesome. And we don't care too much about the LCD, but there's the part number for those playing along at home, and the uh encoder and front panel PCB.

**Dave Jones:** I always find it funny when you find a different brand FPGA in here. We've got an Actel ProASIC3, very nice FPGA, but it's different to the Xilinx parts where we we see on the main board.

**Dave Jones:** So, it's almost as if like you know, like different design team, maybe. Anyway, like it's just interesting the choices. What's a quick response code? And you'll notice the poly switches there on the external probe interfaces.

**Dave Jones:** You don't want the idiot users shorting out the power supply to the external probes. Wow, they're really making sure of the RF shielding connection over to the main board up there.

**Dave Jones:** That's what all the gold pads on there are for. So, there's our soft power button, three USBs, and we're going to take the nuts off here. So, there's our PCI interface for the digital probe.

**Dave Jones:** But, bit more on the bottom, but just all the bypass stuff and other regulation you expected. All right, this is insane. This is a complete 500 MHz analog front end.

**Dave Jones:** You've got to be kidding me. Wow, Rigol's new ASIC they've got here, which does the entire front end, the digital attenuation, and the whole works. Absolutely amazing. Wow. There's a little teensy bit more on the bottom side there, but not much.

**Dave Jones:** It it doesn't include that. That's outside. So, like unbelievable. 500 meg front end. I mean, obviously, you know, it cost millions of dollars to develop this front end ASIC, no doubt.

**Dave Jones:** But, you know, once they've perfected this, they could put 500 meg bandwidth in, you know, a a new version of the Rigol 1054. 500 meg, no worries whatsoever with no price penalty, basically.

**Dave Jones:** But, granted, you do kind of need the sample rate to match the bandwidth. But, you know, a couple of gig would do it. There's no point taking off the other uh cans, of course.

**Dave Jones:** They're all going to be absolutely identical. So, from that ridiculously minimalistic 500 MHz analog uh front end, we've just got our uh differential pair going out and going straight into our DDC DDC ADC.

**Dave Jones:** So, this is a four-channel ADC here. Um I don't know what else it uh contains. You can see all the uh differential pairs um they're all matched length, of course, you know, the serpentine traces, everything else.

**Dave Jones:** Going over to the But, this is a new ADC. This is the new Phoenix ASIC, which handles all the acquisition. Notice that all the memory goes into there. So, and that, of course, is the differentiation we see in like the Keysight and other uh scopes with their uh ASICs.

**Dave Jones:** Because the process technology used in the design of an ADC like this is different to what's used inside a basically all-digital um like processing uh engine and stuff like that.

**Dave Jones:** So, these are all like digital um signals coming out of the ADC. So, there's no analog in this at all, whereas this puppy, the ADC, eh, there's, you know, it's a different ballgame to design one of those.

**Dave Jones:** So, that was a very minimalistic uh design with the new custom ASICs there. It just reduces everything right down. But, it's interesting that they've uh still used the Xilinx Zynq uh FPGA um processor in there instead of probably one of the uh more traditional uh like a TI applications processor or something like that.

**Dave Jones:** So, that's interesting. It's a lot of uh horsepower there for the um user interface. Um whether or not that translates into speed, like user interface speed, we don't know.

**Dave Jones:** Anyway, what's uh fascinating is that front-end chipset and how that Rigol could potentially like decimate the whole lower-end market by by releasing maybe like a $400 new upgraded 1000 series.

**Dave Jones:** They could like 350, 400, 500 MHz even front end for virtually no additional cost on their part. It's just a a strategy whether or not they want to do that.

**Dave Jones:** So, they could potentially release like a scope that's like a hundred a hundred dollars per MHz. That'd be absolutely amazing. So, but no idea if that's going to happen or that but that would really shake things up.

**Dave Jones:** Really interested to see what those little hardware linky things do too if you can hack this thing. So, anyway, as always high res teardown photos are over on EEVblog forum.

**Dave Jones:** That's the best place to discuss it. Subscribe to EEVblog too, notification, all that sort of stuff. You know the deal. Catch you next time.
