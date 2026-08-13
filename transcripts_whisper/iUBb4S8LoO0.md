---
video_id: iUBb4S8LoO0
title: EEVblog #384 - Agilent 4000X Oscilloscope Teardown
url: https://www.youtube.com/watch?v=iUBb4S8LoO0
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 19, "2": 40, "3": 57, "4": 73, "5": 105, "6": 128, "7": 151, "8": 168, "9": 188, "10": 209, "11": 224, "12": 243, "13": 266, "14": 294, "15": 311, "16": 333, "17": 356, "18": 371, "19": 395, "20": 414, "21": 434, "22": 451, "23": 483, "24": 505, "25": 522, "26": 546, "27": 567, "28": 604, "29": 625, "30": 640, "31": 658, "32": 680, "33": 701, "34": 719, "35": 737, "36": 759, "37": 785, "38": 805, "39": 820, "40": 848, "41": 875, "42": 896, "43": 914, "44": 929, "45": 951, "46": 965, "47": 989, "48": 1004, "49": 1020, "50": 1036, "51": 1051, "52": 1068, "53": 1089, "54": 1104, "55": 1119, "56": 1135, "57": 1154, "58": 1168, "59": 1185, "60": 1207, "61": 1222, "62": 1245, "63": 1268, "64": 1286, "65": 1303, "66": 1324, "67": 1346, "68": 1366, "69": 1386, "70": 1450, "71": 1468, "72": 1482}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Yes, nothing's too expensive here on the EEVblog to take apart. So, we have the Agilent 4000 series, brand new, released today. Bit of a world exclusive. You know what we say here on the EEVblog, don't turn it on, take it apart.

**Dave Jones:** Now, if you've seen my review of this thing, you'll know that it's essentially a 3000X series, but with a touchscreen as well. So, really, I'd expect there to be a different layout board, of course, because it's physically a much larger unit to the 3000X, but its architecture should essentially be pretty identical.

**Dave Jones:** I'd be surprised if they've changed much to this thing at all. So, it looks like, to get into here, we've got two carry strap torque screws on here, because that would go right through to the metal shielding. It'll be all metal shielded on the back here.

**Dave Jones:** We've got three main screws here, and the feet on the side as well. So, let's take those off, and the plastic back panel should just pop out, because the... I don't have to take off these nuts, sorry. I shouldn't have to take those off yet.

**Dave Jones:** So it should just pop out and get bare metal. Let's go. And there you have it. We have the obligatory shielding on this thing, and yes, it is a beautiful piece of work. No problem at all. Look at the beautiful little mount there for the side stand on this thing.

**Dave Jones:** So this thing really is built like the proverbial brick dunny. I like it. Now it does appear like this power supply cover slides up like that, but I can't get the thing to... can't get it to budge, so I'm not quite sure. Hmm.

**Dave Jones:** We are in. There's a couple of little niggly connectors under here, but in like Flynn. And of course the first thing you'll notice is that the power supply is completely shielded inside here. Here's the front panel power switch, which goes straight through to the front panel and down onto the board down there.

**Dave Jones:** Yes, it is a soft power switch, I believe, just like the 3000X, but look, it's very well shielded. Incredibly well shielded. We've got a fan cable and main power, and that, I'm not sure what that is. Some sort of standby thing. So there you go.

**Dave Jones:** Very well shielded power supply. We'll take a look at that later. But what we're interested in is this lovely main board. Mmm. And as expected, it is very similar to the 3000X. The architecture, pretty much exactly the same. We've got our four analog input cans here.

**Dave Jones:** We've got our two mega zoom for A61 per sharing two channels. We've got the one ADC BGA package sharing two channels here. And that's why the memory and sample rate halves when you switch on two channels, or one and two, or three and four.

**Dave Jones:** I mean if you switch on one and three or two and four or something, you get the full memory and full sample rates. Because they're shared between the one mega zoom for ASIC. And we've got the huge ADC there. It looks like that they have a higher spec oscillator in there.

**Dave Jones:** It looks like higher spec. I haven't actually checked out the specs, it just doesn't look like a standard package, that's all. So possibly with the 10 megahertz output here, and input, they're expecting a better oscillator. Perhaps. I don't know, we'll have to check it out.

**Dave Jones:** We've got our backup battery, we've got our Spear 600 processor from ST, it's exactly the same. We've got our Xilinx support FPGA here. And digital inputs, some circuitry will be on the bottom side there, the VGA is built in. And looks like we've got display going off here, and another possible, that could be keyboard.

**Dave Jones:** So apart from that, it's all pretty much the same. There seems to be a little bit more there, but the architecture is practically identical. And if we check out between the two ADCs here, you'll notice there's a couple of unpopulated footprints. A rather large-ish VGA there, and another couple of small leadless chip ones just like this one here.

**Dave Jones:** So we'll have to take a look at that, but I don't remember there being any unpopulated ones like that on the 3000X. So they've tried to add something extra there, but decided that they didn't want it. Maybe it's in the higher-end model, I'm not sure, but I can't see why it would be,

**Dave Jones:** because everything's handled in the MegaZoom 4 ASIC. And clearly they've got more circuitry around here, this is for the dual arbitrary waveform capability, so there's basically two identical channels there, whereas there was only one in the 3000X. And it looks like we've got exactly the same Spear 600 processor as before,

**Dave Jones:** but as you can see, the Xilinx Spartan is an XC3S1600E, whereas we had only the 1200E in the 3000X. So they've decided to add some increased logic density there to that FPGA. And this 4000X does have, of course, the touch zone triggering capability, which the 3000X didn't,

**Dave Jones:** but whether or not that is related to that higher density Spartan there, I've got no idea. I'm not sure if this will show up on camera, but you can probably see a little bit of residue left on that board where it hasn't been cleaned properly.

**Dave Jones:** Not a huge deal, I suspect. Now I don't particularly like that ball solder joint on that BNC connector there, but that's fairly typical of this new lead-free rubbish and high thermal mass items like that big BNC connector. And I love how you can actually see the wires wound on these SMD chip output inductors there.

**Dave Jones:** Look at that. Beautiful. Have a quick look at the power supply stuff. They've got all coil craft inductors there, very nice. There's the backlight supply up there, it's all labeled nicely, plus 13 volts, plus 3.3, plus 1 volts. And if we go down a bit we have even more rails, plus 1.8.

**Dave Jones:** Look at all the via stitching there going through to the inner power plane where it would be distributed over to the FPGAs and other stuff that ASICs that actually require that. We've got 1 volt, we've got 1.2 volts here, we've got 14 volts here, 1.8 volts, 2.5 volts.

**Dave Jones:** Oh man, another 12 volt supply. Voltage is all over the shop. 1.4 volts down here. Man, more voltage rails than you can poke a stick at. But very typical in these system designs. Oh, and we have a traditional 5 volt one. There we go, look at that.

**Dave Jones:** Beautiful. 5.2 over here, check that out. And there's the main 10 megahertz oscillator, and it's a Raycon brand TX0220. Now, I had a quick look at the Raycon website, and of course basically being TX, that means temperature compensated crystal oscillator. So I could only find the 2200, which was a 0.5 ppm to 2.5 ppm temperature compensated oscillator.

**Dave Jones:** So I'm not sure exactly if it's the same one or not. I don't think so, but I think it's better than your usual, you know, 5 by 8 millimeter package. It's certainly a different package to normal anyway, so it might have a better 10 megahertz reference oscillator in this thing compared to the 3000X.

**Dave Jones:** Now I just wanted to show you this because I can with my x10 macro lens here, you can see the balls on that, you can see the solder balls on the pads of that unpopulated BGA, which I showed you before that was between the two ADCs.

**Dave Jones:** Check it out. And there's a better angle on that I think. Beautiful. And as we saw in the 3000X, you can't escape having a good old LM324 in there. And look at that, 74HCT04 as well. Ah, TL072, it's all happening. That is around the circuitry for the demo output signal.

**Dave Jones:** So we've got some AD822 op amps there and some DG4444 muxes, and all that fun stuff which goes with having those analog output signals. There's the two outputs down there. And what do you know, someone's gone to the trouble to measure that battery

**Dave Jones:** and mark the value on there, 3.197. Got to have three decimal places. All right, let's lift this board out of here, and ta-da! We're out! Look at that. Beautiful. And here's the backside of the board, which is actually the front side facing you when you're operating the scope.

**Dave Jones:** So we've got our four analog inputs down here, we've got our two demo signal outputs here, USB, and our two arbitrary waveform gens plus external trigger input. So, you know, clearly the circuitry is all functional, it's right where it should be. And this is the four-channel version of course, but it is available in the two-channel version,

**Dave Jones:** and presumably that's why they've got a separate bracket for each lot of two channels. They just wouldn't populate all those components there on the dual-channel version, I would presume. Because you wouldn't waste the money I guess, or maybe it is populated and they don't put the BNCs on?

**Dave Jones:** I don't know. Anyway, there's a fair bit of circuitry on the bottom for the demo output signals of course, there's our USB controller chip for our two USB hosts there, plus there'll be a third one, so that'll be like a three-channel or four-channel one as well.

**Dave Jones:** And that's our external trigger circuitry around there. Then we've got just some support and bypass stuff for our dual arbitrary waveform gen there, most of the circuitry for that is on the other side of the board as we saw before. More of the power supply stuff, ton of it, all around there on the back side of the board as well.

**Dave Jones:** You can see all the bypassing on the back of the big BGA devices, that's our processor, that's our FPGA, these are our two MegaZoom for ASICs, and these are our two ADCs. And up the top here we've got a couple of custom Agilent chips for the logic analyzer,

**Dave Jones:** a couple of interface devices there, and well, just regular support stuff, and lots of bypassing and things on the back, maybe some localised, more localised power and things like that. Now one interesting difference from the 3000 I believe is that the logic analyzer here

**Dave Jones:** is now using some custom Agilent chips there. Well they're actually, you know, they might be off the shelf, but they're certainly branded Agilent devices there, and they didn't have that on the 3000. So you can see the logic analyzer header connector up the top here,

**Dave Jones:** and these two custom devices, so maybe that goes a little bit of the way towards explaining the extra cost for the logic analyzer on this thing, but like, it's more than like doubles, like two and a half times the cost of the logic analyzer add-on for the 3000, which is crazy, but it certainly is different.

**Dave Jones:** Now here's the analogue front end here, we've got an additional relay on the top, there is another identical looking relay on the top side underneath the metal shielded can, and it looks like there's, like the main amplifier I'd say is around there, the main driver, sorry, which then drives the differential output up into the ADC further up,

**Dave Jones:** so that's all the bypass stuff around there, so most of the active stuff on that thing is on the top side of the board. And then we've got the demo signal outputs there, there's a DG419, which is a precision analogue switch there, I'm not sure what the device is above it, but once again, most of the stuff is on the top side of the board

**Dave Jones:** for those demo signals. And I'm not sure what that particular USB host controller is there, but clearly it is a USB host controller, and it's got its own local oscillator as well, as you'd expect. And it looks like we've got some of the support circuitry for the external trigger input,

**Dave Jones:** there's an ADG633, that's an analogue switch, we've got an AD8510, I believe that's a precision op-amp there, and we've got a good old 74ACT series, oh wait, go figure. And the front side of the board trigger circuitry, we've got a TI594 there, I assume that's like a 74594,

**Dave Jones:** and I'm not sure what this particular national semiconductor device over here is, and we've got a MAX9202 here, which is a fast quad comparator. And on the front side of the board here, one of those devices, well the one that's populated anyway, I assume the other unpopulated ones are the same, that's a Micron SY89855, it's an LV Pekel MUX.

**Dave Jones:** And next to each one of the MegaZoom 4 ASICs is a Samsung DDR2 memory, it's 512 megabits. And surrounding our processor here, we've got our JTAG connector of course, which is joined all together, we've got a 32 kilohertz crystal for the real-time clock, we've got some program memory surrounding that,

**Dave Jones:** and the Xilinx Spartan FPGA with its configuration PROMs down here. And you can see the different bypass capacitor configurations here, this is for the Xilinx FPGA, and this one here is the ARM processor. Next to it you can see that the balls are only around the outside there,

**Dave Jones:** they're not populated in the middle, so it's not a huge pin count, well it's not as large a pin count device as the FPGA over here. So it keeps the balls all the way around the outside there, which leaves room inside for your bypass capacitors,

**Dave Jones:** and a nice big ground fill in the middle there. But the FPGA over here, it's chock full of pins, and you've got to get like eight layers just to route all these pins out on the different layers, and really it's only got room, a little thin sliver that way and that way, to mount your bypass capacitors in the middle.

**Dave Jones:** And then they surround it all around the outside like that, whereas you see they didn't have to do that one with the processor. And we've got an SMSC Ethernet network controller. And near our 10 megahertz reference crystal on the back, here's our frequency synthesizer.

**Dave Jones:** It's an ADF4360, and it's a integer divide by n type, and it generates the high frequency clocks required from the 10 megahertz reference oscillator. It's a volt, and it contains a voltage controlled oscillator as well. And up in the top corner of the board here, we've got ourselves an additional 150 meg crystal oscillator.

**Dave Jones:** And on the back of the case here, we have yet more beautiful shielding, these nice welded integrated standoffs. I love them, but it looks like we have a big shielding plate over a board which has this ribbon cable, and this is probably the touchscreen controller up here would be my guess.

**Dave Jones:** So let's pop the hood on those and see what we've got. Check this out. There's no board under there, it's just an extra shield for the ribbon cable. Look at that! Beautiful. It goes all the way over to this front panel keypad board.

**Dave Jones:** So this is the keypad cable with all the rotary encoders. That'll have its own processor on it. We've seen that in the 3000. So, you know, nothing really exciting going on there. I don't think I'll even bother to take out this whole plate because it's messy.

**Dave Jones:** You've got to take the knobs off and it really becomes quite ugly. So yeah, nothing too exciting on there, but I do want to have a look at that puppy. And yep, this looks like the touchscreen controller board. We've just got data and power coming in here.

**Dave Jones:** And we've got one controller, we've got two controller chips here which go off through these flat flex ribbons through to the front panel down in there. They actually go right up over the top, so they would be the sensor interfaces for the various rows and columns there.

**Dave Jones:** And we've got a main serial interface controller. Let's take a look in more detail. And there's the main touchscreen controller IC. It's from a company called EETI. They're a Taiwanese company that specialise in these sort of touchscreen controllers. And it's the EX5404. I can't get any details, data sheet on that.

**Dave Jones:** You know, it's one of those proprietary, you've got to contact them to get it. Pain in the ass, but there you go. We've got two of those controlling this 12-inch touchscreen. And the main controller there is an EXC7200. And that's all she wrote, really.

**Dave Jones:** I mean, it's, yeah, the architecture is the same as the 3000X. There's a few little optional extras which weren't on the 3000. And of course, unfortunately I can't take off the metal can, they are soldered down to the board. So this is a demo unit.

**Dave Jones:** It's got to go back. It's not like I can risk damaging this thing by taking those off. But there's not much circuitry in the analogue front ends. These are the 200 MHz channels. Don't know why they've got red and green dots on them, part of the testing process.

**Dave Jones:** I hope that one didn't fail. Hmm. So yeah, these analogue front ends will be different depending on the model you buy, right up to 1.5 gig, which the 3000X only went to 1 gig. So these, this is the same for the 200 and the 350 MHz model,

**Dave Jones:** and then the 500 MHz model is different, then the 1 gig model is different again, and the 1.5 gig model is different again. So all those analogue front ends are completely different. They would have to swap the whole board in the unit when you send it back to the factory,

**Dave Jones:** because I'm sure they're not going to solder off these cans and, you know, change circuitry under there. It's just not going to happen. I mean, this one is designed for the 350 MHz front end. Aha! I did get this sucker to slide forward and lift up.

**Dave Jones:** Oh, look at that! Look, folks, we have a big fan guard! Oh, beautiful! Sucks all the air in on this side, right over the power supply, and then right into the fan there. Oh! Fantastic! No pun intended. So that's actually quite a neat bit of work there.

**Dave Jones:** There's the power supply in there, so it sucks all the air in through one end here, and funnels it all the way under there, out this grill here, and of course this is covered on the back here, so then it's got nowhere to go but out through the fan.

**Dave Jones:** Oh! Let's have a look to see what we've got in here, shall we? Here's our PCB mount IEC power input connector, we've got a common mode choke there, there's no other suppression or power factor correction or anything on there. We've got a big power resistor there, and what looks like a little, maybe a little bridge rectifier

**Dave Jones:** or an optocoupler up there. We've got our logic, our soft logic power switch. No, that does not switch in the mains, as you can see, those traces go over to here, which then go into the low voltage side of the power supply. So it really is, yep, it's not a mains power switch, it's a soft standby switch.

**Dave Jones:** And it looks like we have a totally different supply to what was used in the 2000 and 3000X. Now if we have a look at the mains input side here, here's the 240 volts in, and these two brown devices there are PCB mount fuses, and this is actually a PCB mount fuse as well.

**Dave Jones:** So they're not as easy to replace as a regular glass fuse. And tucked away under there we have some filtering, some more common mode chokes, some more filtering there, so yeah, they've done the basics. So what we had before in the 2000 and 3000X was a Lineage brand power supply,

**Dave Jones:** but they've changed it, they've got Artisan brand power supply here, and it looks, you know, it looks first class quality. All the elastic and all the, you know, the quality of the components, it really looks well laid out and well designed, as you'd expect in an Agilent bit of test gear.

**Dave Jones:** Check this out, someone's done an oopsie here. This pot, I believe, yeah, it's a sealed pot by the looks of it, is fouling this connector, and I can't push that down any further. It's lifted up on an angle there. Oops. And it's hard to see the brand of the cap in there, but I see Chemicon there,

**Dave Jones:** so that would be a Nippon Chemicon. So that's quite a well designed little power supply, I don't mind that at all, and because it is totally different to the 2000 and 3000X, possibly we have a lower standby power consumption than that horrible 6 watts we were getting last time.

**Dave Jones:** Worth a check. So there's only one thing left to do, and that's put this sucker back together! And no, sorry, the LCD under there, there's going to be nothing interesting on that, so, and the main keypad controller board. Pretty boring. Boring as the proverbial bat poos.

**Dave Jones:** Thanks for watching. And in case you wanted to know the power consumption, 81.3 watts while operational. Not doing much of course. And standby mode, it was in the order of 6 watts on the 3000, it was an absolute shocker. So it should be, if they've done everything right, it should be lower.

**Dave Jones:** This thing averages, it takes some time, there we go, bingo, 2.1 watts standby, beautiful. One third of the 3000X. Still a bit high, but jeez, you know, you can still fly to the moon on 2 watts. So there you have it. I hope you liked that teardown.

**Dave Jones:** If you want to see a bit more information, there is the 3000X teardown as well, which I will link in. So if you like it, please give it a big thumbs up, that helps a lot. And if you want to discuss it, jump on over to the EEVblog forum, because that's where

**Dave Jones:** all the cool nerds hang out. Catch you next time.
