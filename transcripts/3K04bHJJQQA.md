---
video_id: 3K04bHJJQQA
title: EEVblog #187 - Tektronix TDS2024C Oscilloscope Teardown
url: https://www.youtube.com/watch?v=3K04bHJJQQA
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 27, "3": 37, "4": 57, "5": 72, "6": 81, "7": 108, "8": 120, "9": 133, "10": 141, "11": 153, "12": 170, "13": 182, "14": 197, "15": 212, "16": 229, "17": 240, "18": 250, "19": 267, "20": 280, "21": 295, "22": 304, "23": 339, "24": 350, "25": 366, "26": 380, "27": 391, "28": 410, "29": 424, "30": 437, "31": 451, "32": 467, "33": 482, "34": 496, "35": 516, "36": 536, "37": 549, "38": 570, "39": 583, "40": 596, "41": 607, "42": 625, "43": 638, "44": 650, "45": 667, "46": 679, "47": 736, "48": 754, "49": 811, "50": 818, "51": 837, "52": 847, "53": 863, "54": 881, "55": 892, "56": 904, "57": 922, "58": 943, "59": 959, "60": 974, "61": 988, "62": 996, "63": 1017, "64": 1032, "65": 1047, "66": 1060, "67": 1070, "68": 1090, "69": 1109, "70": 1120, "71": 1134, "72": 1147, "73": 1161, "74": 1175, "75": 1183, "76": 1280, "77": 1314}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it's product teardown time and it's another oscilloscope.

**Dave Jones:** Just so happened to have this Tektronix TDS 2024C. It's not a new scope, it's a it's a reasonably old model and no, I'm not going to review it cuz I don't think it's worthy.

**Dave Jones:** Not going to bother. I'm only going to do a teardown. Now, the reason for that is because it just reminds me of the old TDS 2000 oscilloscope. Not that there was anything wrong with that.

**Dave Jones:** Great oscilloscope in its day. Pioneering, it practically started the entire digital storage oscilloscope business. All these bench portable ones anyway, the ones that had real-time sampling. They started it all but quite frankly, I had one of those back in I think it was 1997.

**Dave Jones:** I'm not kidding. Not 2007, 1997. And it just reminds me of that. Sure, it's got a few more features but the thing is, it's only got and here's the spec, 2.5 kilobytes of sample memory.

**Dave Jones:** That's not megabytes, that's kilobytes. It's barely enough to do a couple of screens worth. It's hopeless. Now, where is the advancement of the art in the sample memory depth?

**Dave Jones:** Exactly the same 2.5K sample memory. I can't believe it. This is you know, Tektronix's current model and it's just not competitive. It's crazy in terms of sample memory. It's not a bad scope, you know, I can picture it being useful for say the tech fanboys or something like that and they only want a basic scope that just displays a waveform on the screen and that's it.

**Dave Jones:** Well, okay, maybe but jeez, I don't know. It's not very competitive. So, don't expect a review of this thing. I don't think IT'S REALLY WORTHY BUT WE'RE GOING TO TEAR it down cuz I'm quite curious to see what's inside.

**Dave Jones:** Let's go. Just one thing, don't confuse this TDS series with the DPO 2000 series or the MSO 2000 series. They're a different higher-end technology scope. They cost a lot more.

**Dave Jones:** They've got them sample memory. They've got everything else, but this is the TDS series. All right, I know some people are going to want a little quick summary of it.

**Dave Jones:** Really, it's quite small and uh lightweight. So, you know, as you'd expect, it's a reasonably good quality being uh Tektronix, one of the big names in the business, and it is fanless, too.

**Dave Jones:** It doesn't make a sound. Doesn't generate a sound. It is much lighter weight than, say, the uh reference Rigol. Here, it's about the same uh width. It is uh not as deep as the Rigol unit, but it certainly does weigh a fair bit less, but it takes forever to boot up.

**Dave Jones:** It takes like 30 or 35 seconds. Crazy. On the back here, we've got a single USB uh port to connect to the PC for control, and on the front, we've got a USB memory stick.

**Dave Jones:** Uh it's got a fair few more controls in the original uh TDS uh 200 series or the uh or the even the new uh Tektronix TDS 1000 series, which actually replaced the uh 200 series.

**Dave Jones:** This is actually another reason why I'm disappointed by the 2.5 K of sample memory cuz it's not like this is the TDS 1000 series. This is the supposedly the next step up, TDS 2000 series, and ugh, 2.5 K memory, it's crazy.

**Dave Jones:** Anyway, it's pretty bland-looking, actually. Um the just the color and the styles of the control layout, it's like a It's almost like it's a prototype or something. It's like they, you know, they the industrial design people just didn't really finish it off.

**Dave Jones:** And um you know, the knobs aren't bad. The uh the button presses are all reasonably uh qual- reasonably good quality, as you'd expect, but none of the buttons are pushable.

**Dave Jones:** They've got no secondary uh push function on them, which is quite disappointing, but there's extensive uh menu systems. It works uh identically to the original um to the standard Tektronix kind of interface.

**Dave Jones:** And, well, that's about it. Bit underwhelmed, really. One thing I don't like with the interface on this thing is this knob over here. Look, you would think that that was a fifth uh analog input channel, but it's not.

**Dave Jones:** There's the ex- That's the external trigger, and this, believe it or not, is the horizontal control. It's crazy. Why are all these knobs exactly the same? These four, make them the same, fine, but the horizontal, you got to make it bigger.

**Dave Jones:** And, don't put it in the same line like that. It's just crazy uh interface layout design. I don't like it. You would think that this one up here might be your uh horizontal or something like that, but no, that's your typical soft um soft control uh knob.

**Dave Jones:** But, and it's exactly the same style, shape, and color as all the rest. The layout is just I don't know. Who did this? The work experience student? Eh, enough of looking at the scope.

**Dave Jones:** Let's take it apart. Much more interesting. Now, I've got to say that is by far the easiest scope I think I've ever taken apart. A couple of uh T10 Torx screws there, just take the button off with a pair of uh pliers.

**Dave Jones:** You've got to use the rag there, as you saw, just so that you don't mark the uh knob. But, apart from that, it was uh it came apart beautifully and here's the inside of the scope.

**Dave Jones:** I'm actually surprised to see two boards here. We've got a board on the back which clearly drives the display. We'll take a look at that and the main base board down the bottom here and a very nice looking power supply from Emerson Networks.

**Dave Jones:** I like it. Let's take a look at the Emerson power supply here. Each board is individually serial numbered. Looks like uses high quality components, high quality build. I really like it.

**Dave Jones:** You get a sense of a real real big sense of quality with this thing. They've got the celastic around all the major components in there. They've dobbed the celastic in just so things don't move.

**Dave Jones:** I really like it. It uses, yes, it does actually use a real clunking mechanical mains power switch there and we'll actually check that. It actually draws nothing when you switch when you actually switch the thing off.

**Dave Jones:** We got caught with that with the Agilent scopes. They were a bit dodgy in that respect drawing 6 watts. Crazy. Anyway, this one draws zero and it's just quite a nice supply.

**Dave Jones:** It's well laid out. You can see the high voltage isolation slots down in there. Really quite a nice build. Single sided of course. They still do these boards single sided cuz they're actually cheaper to manufacture.

**Dave Jones:** You can save a few cents by doing that. There's a couple of links in there but they've laid it out quite well to avoid the links. So it looks like a really good quality power supply with what looks like decent quality components.

**Dave Jones:** And they've used 105° C Rubicon brand caps and as you can imagine they would be genuine. They wouldn't be rip off ones. Tektronix would make sure they source their components from quality from the original manufacturers.

**Dave Jones:** We've got refer mains class mains class capacitors there. But really the only thing I don't really like is the is the soldered in M205 fuse in there. Why couldn't they have just put a socket in there?

**Dave Jones:** So if it does blow, well, you can just replace it. It I don't know. I didn't like And if you notice these three TO220 packages on the same heatsink here, they don't actually use any mounting hardware, no screws or anything like that.

**Dave Jones:** They're actually stuck on with just an an adhesive thermal tape. And that's that's reasonably common as opposed to say this traditional TO220 device down here, which is which is actually strapped onto its heatsink with one of those metal bracket straps in there.

**Dave Jones:** And it's got decent mob protection on the mains input as well for surges. And here's a good design aspect to show that they were really thinking. The the mains IEC input connector here, sure it's a PCB mount one, which actually saves you on the wiring, which is quite nice, but a lot of people make the mistake of not a physically reinforcing that properly.

**Dave Jones:** They just rely on the PCB mount itself. But this one is actually you can see the two screws there actually screw into their own standoffs fixed welded in standoffs on the metal chassis.

**Dave Jones:** So they take all the stress when the user actually plugs plugs in and disconnects the IEC mains connector on the top here. Because if you didn't have those standoffs, then when when the user plugs in the mains plug into the top like that, all of the stress will be transferred onto the PCB and ultimately to the solder joints and flexible and all that sort of stuff.

**Dave Jones:** But when you add those fixed anchors like that, you take away all that So, they were definitely thinking. Now, curiously, we have this two-board construction. I find that rather unusual.

**Dave Jones:** Uh I expected a single-board construction for a scope like this, just to um just to reduce the complexity. Because, as you can see, you've got to have this uh wiring loom going across here, which is an extra strip step extra cost.

**Dave Jones:** You've got to buy decent quality connectors. You've got to put these ferrite uh beads in here as they've done. You've got to uh add manual steps to actually cable tie the things down.

**Dave Jones:** It just adds a fair bit of complexity there. And they've got another one over here, which is again cable tied. There's no ferrite um beads on that. So, obviously, this, because it's got the ferrite uh beads on here, that means that that's actually transferring all of the uh high-frequency uh the high-frequency data for for the display um itself.

**Dave Jones:** So, it's going from the main processor on the main board down here up to this uh FPGA and uh and display memory up on this board. So, let's take a closer look at that.

**Dave Jones:** So, here's the display board. And uh not terribly surprising at all, apart from that they have actually mounted it on a separate um board in itself. It's got a Xilinx uh Spartan 3 FPGA.

**Dave Jones:** No surprises there, with its own display memory from IDT. Uh no surprises there at all. Uh this is obviously a DC-to-DC converter that goes up there, and that goes off to presumably drive the uh display backlight the high-voltage uh backlight.

**Dave Jones:** And uh there's probably a DC-to-DC converter there, which uh powers um some of the core in the FPGA. I'm sure they most likely don't get the uh core voltage directly from the main board.

**Dave Jones:** And really, that's about uh all you'd expect. That's probably the um the boot-up um the flash for the uh Xilinx Spartan. And not much else, really. And there you go.

**Dave Jones:** We've taken off the front panel assembly. I had to remove all the knobs there and a couple of screws on the back, but it all came apart fairly easily and there's the membrane rubberized keypad on the front that that can just pop out if you want it to.

**Dave Jones:** They've got two contacts per per switch for reliability I am presuming and that's just all one big molded piece and then we have the main board here which has all the rotary encoder knobs on it and that looks quite nice.

**Dave Jones:** And here's our main board. Let's take a look at it. The first thing I notice is that the analog input circuitry doesn't have a complete metal shield on it.

**Dave Jones:** It's only got these these little shielding walls here like that around part of that. Now most this is a 200 MHz analog scope. So most scopes in that category will have even lower end categories will have a metal can there.

**Dave Jones:** So I'm not sure why they've actually done that. I guess they deem it not they don't actually require it. Anyway, let's take a look at some more aspects of it.

**Dave Jones:** There's two main ASICs up here clearly because it's a four I presume they're ASIC. I don't actually recognize the number of them at all. It's a VO42ADG522. I don't really know that.

**Dave Jones:** It doesn't ring a bell. But they've got some they've obviously got some that looks like DRAM there. They've got some high speed IDT memory there and there. And the analog input parts are national semiconductor parts.

**Dave Jones:** Now curiously here's the battery for the real time clock. And look they've got a really an old fashioned SO package real time Dallas semiconductor real time clock over here.

**Dave Jones:** It's quite nice compared to most of the stuff. Although you've got some standard SO packages over here. But some of the stuff is uh you know reasonably old school packaging.

**Dave Jones:** And now let's take a look at the analog input circuitry here. Now we've got two national semiconductor parts. I don't know those offhand. I'd have to look those up whether or not they're custom or they're off the shelf off the shelf devices.

**Dave Jones:** Now, um this one is a 200 MHz bandwidth, but there are lower models, so I'm not sure. I presume it's only a software difference like in the Rigols and many other scopes on the market to actually get the different bandwidths or possibly the 200 MHz one might be different to the 100 MHz model or something like that perhaps.

**Dave Jones:** And obviously and obviously the other channel is exactly identical. We've got some trigger Well, there's not much in the way of a trigger circuitry over here for the external trigger device and there's a close-up of the main one of the main ASIC devices there.

**Dave Jones:** And they've got this expansion header up here and I'm not sure what that's doing and whether or not that's for some I don't know logic and mixed signal version.

**Dave Jones:** I'm not sure. They don't have a mixed signal version in the 2000 series. So, go figure. I'm not sure what's going on here. This looks like a processor for the USB and perhaps for the whole unit itself.

**Dave Jones:** Itself to see that I'd have to actually take the sticker off. There's the power input with a couple of free standing voltage regulators. I'm not a big fan of the free standing TO220 package.

**Dave Jones:** They put it Probably should have put some silicon on that like they did for the power supply. They've got a Cypress semiconductor part here. I believe that's for the USB um host down here for the USB key.

**Dave Jones:** That's the That's the scope probe compensation pin there and really there's not much else. Pretty typical of what you'd expect to find in one of these low-end scopes. Most of the magic is done inside these ASICs here.

**Dave Jones:** There's actually presume they're identical chips, so there's there's presumably one per uh two channels like that. So, if you bought the two-channel one, I'm sure they would just uh depopulate all of the uh analog parts, that extra memory, and that uh ASIC over there.

**Dave Jones:** So, the two-channel would be nearly identical to this, just some uh cost saving now. And if we flip it over and take a look at the bottom side of the board here, let's take a look at what we've got.

**Dave Jones:** Unsurprisingly, there's the uh firmware. It's a dead giveaway. That's the flash chip because it's got the firmware sticker on it. Um and this device here is a uh Freescale.

**Dave Jones:** There we go. Is that a 68 thousand? That looks like an MC68000 device to me, which um I think, if memory serves me correctly, the original TDS series scopes might have used a 68000 processor.

**Dave Jones:** So, they may have carried that over. I will have to double-check that, but there you go. And somehow it's connected into um well, it's connected into all of the uh stuff behind there, those two big um ASIC devices up there, as you can see.

**Dave Jones:** They're directly on the top there cuz you can see all the uh vias connecting the bottom of of those BGA devices there. And smack in the middle of it is that Freescale processor.

**Dave Jones:** Now, uh over here, there's a TI part. I don't recognize that one offhand. Um there's some serpentine uh traces going down there, differential pairs, obviously something to do with the Let's have a look.

**Dave Jones:** I don't know, something to do with the USB, perhaps up there. I'm not sure. And there's some uh shielding um sections like this on the base of both of the analog channels.

**Dave Jones:** But apart from that, not much else on the bottom. Not much doing there. And if we pull this chip's pants down, let's take a look at our TERA MAX 2 PCPLD.

**Dave Jones:** There you go. Some nice attention to detail here for the backup battery there. They've actually covered the bottom pins with a silastic so that you can't short it out to the chassis, I presume, when you're installing it or when you're servicing it.

**Dave Jones:** Very nice. And the top switchboard up here with all the rotary encoders, it looks like it has a couple of its own processors on there. I'm not going to bother to take that board out.

**Dave Jones:** It's not terribly exciting at all. But it looks like Tektronix have put firmware stickers on all their programmable devices, so that's a dead giveaway of the devices that actually have firmware or something else built into them.

**Dave Jones:** And does it work? Unfortunately, we can't tell because the damn thing takes about 30 seconds to boot up. Crazy. Eh, at least the screen's going. There you go. Still going.

**Dave Jones:** Come on. Hey, we're up. There we go. She works. Beauty. See you next time. Don't forget to subscribe, like, and do all that sort of stuff.
