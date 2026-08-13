---
video_id: G1xbJ9NOgD0
title: EEVblog #371 - Universal Programmer Teardown
url: https://www.youtube.com/watch?v=G1xbJ9NOgD0
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 27, "2": 47, "3": 70, "4": 95, "5": 111, "6": 131, "7": 156, "8": 175, "9": 191, "10": 212, "11": 228, "12": 255, "13": 269, "14": 289, "15": 316, "16": 339, "17": 354, "18": 374, "19": 392, "20": 410, "21": 429, "22": 454, "23": 478, "24": 492, "25": 511, "26": 555, "27": 576, "28": 599, "29": 616, "30": 644, "31": 658, "32": 675, "33": 695, "34": 719, "35": 747, "36": 781, "37": 807, "38": 824, "39": 852, "40": 870, "41": 889, "42": 912, "43": 929, "44": 951, "45": 971, "46": 988, "47": 1011, "48": 1027, "49": 1053, "50": 1071, "51": 1097, "52": 1125, "53": 1149, "54": 1175, "55": 1200, "56": 1222, "57": 1247, "58": 1263, "59": 1287, "60": 1310, "61": 1337, "62": 1354, "63": 1376, "64": 1398, "65": 1412, "66": 1429, "67": 1443, "68": 1461, "69": 1477, "70": 1494, "71": 1509, "72": 1524, "73": 1546, "74": 1563, "75": 1582, "76": 1604}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Yes, I've got my lapel mic back for those who've been following along with that. We've got a universal programmer today. It's the Wellen VP298 universal programmer. Wellen, they're a Chinese company, but they're a fairly reputable manufacturer, as far as Chinese companies go, of universal programmers.

**Dave Jones:** And if you're not familiar with these universal programmers, you might actually know them as, you know, EEPROM programmers or something like that. But they do a hell of a lot more than just EEPROMs, hence the name universal. They'll pretty much program anything that's programmable up to the maximum number of pins.

**Dave Jones:** Now this is a 48-pin one, it's got a 48-pin ZIF socket, zero insertion force socket on there. And this thing can not only program EEPROMs from a zillion different manufacturers, it can program PROMs, microcontrollers, a ton of different manufacturers, GALs, PALs, all sorts of pretty much anything that is programmable.

**Dave Jones:** This one supports approximately 17,000 different devices from, I don't know, hundreds of manufacturers or something like that. So let's take a look at what's inside, because these things are rather interesting. Now just before we tear this thing down and take a look at what makes it tick, I thought we'd just have a look at one of the uses for these universal programmers.

**Dave Jones:** Not only can they program devices, but they can read things as well. Now take this Samsung Electronics Commander, Telecom Commander series phone system you've seen me do an impromptu teardown of when I first moved into the lab here. And what's it got in it?

**Dave Jones:** It's got an EEPROM. There it is. And they're usually socketed like that, so we can just whip that sucker out of there, whack it into our universal programmer, and read the code out of that thing. And the code can tell us a lot about how the thing works.

**Dave Jones:** You can, you know, disassemble the whole thing if you're, you know, that keen. But it can give you, there can be like a text command, serial commands, things like that embedded in there that allow you to, you know, might be allowing you to control a particular product via a serial port, get into a debug or a service menu or something like that.

**Dave Jones:** So all that info could be hidden in there, so I thought we'd just take this out, read it in, and see what we can find. So let's whack our EEPROM in there and give it a go. This one is actually an Intel 27256, but it should be able to auto detect that.

**Dave Jones:** These things can usually auto detect regular EEPROMs like this because they do have a manufacturer code in them. So we'll whack it in there, make sure you get the orientation of course, and the pin out correct. This one has to be right down towards the bottom.

**Dave Jones:** Not all universal programmers are the same, some might go to the top, or some might be in the middle, something like that, depending on how the internal circuitry is configured to switch all the pins. But universal ones should be just that, universal. They can switch any voltage to any pin, but the software, you know, needs to know,

**Dave Jones:** the library for a particular device needs to know where it is in there, so it needs to default down to the bottom part of the socket down in here, so it knows and can map those pins in there. So let's give the software a try.

**Dave Jones:** And here's the software for the Wellan universal programmer, or a subset of their particular models. Because not all universal programmers from the same manufacturer use the same software. Some universal programmers may be less flexible and support less devices, in terms of programming voltages and pin outs and things like that, and they may have different software.

**Dave Jones:** So just be aware of that when you're actually buying these things. You may buy a cheap one on eBay for, you know, $30 or $50 or something, but then find that it doesn't, it's not really, really universal and doesn't support the device you need.

**Dave Jones:** So just be aware of that anyway. Anyway, here it is, programmer initiate success. So it's actually connected via USB, no problems at all. And let's go and have a look first at what, we'll try and select a device. So we'll pop this up, and here are all the, there you go, there are 90 different, sorry, no, look,

**Dave Jones:** over here we've got, on the right hand side here, we can select EEPROMs, so there's 90 different manufacturers, 3200 devices total, just of E-squared PROMs and EEPROMs. And that's a hell of a lot of chips just on the EEPROM side of things. And we can select MPUs, MCUs, and it actually, it's nice, it gives you the manufacturer's logo and stuff like that.

**Dave Jones:** And these things are updated daily, weekly, stuff like that. For companies that specialize in these universal programmers, they're really completely up to date usually. So it's always worthwhile downloading the latest device file. But it's got 1900 MPUs from ones you've never heard of, ABOV, ALI, you know, ASP.

**Dave Jones:** But there's Atmel there, there you go, there's all the Atmel devices that this one supports, all the ATmegas and tinys, probably not the full range, but you know, there's some Dallas ones, there's Intel, and microchip, let's have a look at the microchip parts.

**Dave Jones:** Supports quite a few microchip parts, no, it's definitely not all of them, looks like only the 12 and the 16 series, doesn't support the 18, 24, or 32 bit series there. But anyway, you know, it's not designed, you wouldn't buy this as a microchip programmer for example,

**Dave Jones:** or an Atmel programmer, but it can certainly do some of them, especially the older ones in the DIP packages and things like that. So let's, you know, and then you can go into device info, so let's choose a PIC 12C508, and go into device info, it's really neat, it tells you that it's a DIP8 package,

**Dave Jones:** then it tells you the part number description, and I really like this. It gives you the full part number so that you can decode the exact part number which is printed on your part. Well, sometimes, often it's not, but it might be printed on the reel or the packaging,

**Dave Jones:** or something like that, you get a chip in. So quite handy to have something like that. So if we choose all of them, here we go, it supports 17,051 devices. Awesome! So, no doubt it'll support our EEPROM, because these all support, you know, these generic EEPROMs.

**Dave Jones:** So what we can probably do here, is do the auto ID. And here we go, warn in Will Robinson, auto select, EEPROM is only enabled for, only enable, jinglish, for a chip of 24 to 40 pins. Other ACTRANS chips is maybe destroyed. Careful, warning, but anyway, I'm pretty darn confident that I've put this thing in correct,

**Dave Jones:** and it is a standard 28 pin EEPROM, I don't think it'll have any drama automatically detecting that. Bingo! There it is. It's an Intel, it's a 27256. So, not a problem. It definitely, guess that, not an issue at all. It gives you the checksum down here, and we're ready to go.

**Dave Jones:** So let's just read that in, it automatically sets everything up for you once it's detected that chip, or you've selected the chip. So we don't want to program it, we want to read it. So let's read it, boom, it'll only take a second, yep, there it tells you, it's quite proud of it,

**Dave Jones:** only took 1.24 seconds to read that. So then you can go into edit here, and of course you can extract this stuff out, and let's have a look here. This is a bit of a bummer, we've got some FFFFF, it's blank! It's blank!

**Dave Jones:** What? What? Ah, fail? If we go into blank check here, it's telling us this EPROM is blank. Ah, bullshit. And let's crack this sucker open and see what's inside. Now what I expect inside here is a fairly heavy duty micro, probably, maybe an FPGA or a PLD or something like that,

**Dave Jones:** and a whole bunch of analog circuitry to switch every single pin on this device. So there'll be 48 channels of MOSFETs to switch each pin high and low and to various voltages. So I expect to see lots of discrete circuitry inside this thing.

**Dave Jones:** I mean, there could, I think there are actually custom chips you can actually get for this purpose, but I'm fairly confident this one will use all discrete circuitry. And it's probably, it could all be on the one board, although the ZIF socket could be mounted on a riser board or something like that,

**Dave Jones:** perhaps, because it's quite a small unit, so maybe there is a dual board system in there, because all that discrete circuitry does take a lot of space to actually do, so it wouldn't surprise me if this is a two board system. Hey, there we go.

**Dave Jones:** Ta-da! Yeah, I think it's going to be a two boarder, as we've got our sockets down here. So let's, how does that pop out? I think it just, oh, yep, yep, there we go, look at that. Ta-da! There it is. So there's a regulator here, two other probably regulators for the programmable programming voltages,

**Dave Jones:** stuff like that, some analog stuff to take care of that, and to switch it and do various things. And we have our daughter board here, and yep, there we go, we have a huge device under there with lots of discrete stuff going down there,

**Dave Jones:** and another big device under there, and some circuitry on the bottom of the daughter slash riser board here, so let's whip that off and look at the goodness. And that's pretty much as I thought it would be. We've got an FPGA here, some other device up here,

**Dave Jones:** look at this, the bastards! They've ripped off the number! Grrr! Hate that crap! And anyway, a whole bunch of discrete circuitry and what looks like little SOT 23 MOSFETs, probably a bunch of N-channel and P-channels there to drive all of the pins. Not as much as I thought, though.

**Dave Jones:** I don't think this is an actual, true, real high-end universal programmer because it doesn't seem to have enough MOSFETs to drive each of the 48 pins to all of the various states. I think they've taken some compromises in the design of this thing, but let's take a look at the main board.

**Dave Jones:** For the main board here, let's start, have a look around this section around here. Now, as I said before, this is likely the high-voltage, well, almost certainly, the high-voltage programming regulators here, and a whole bunch of stuff to handle that and select the various programming voltages required for a whole bunch of different devices.

**Dave Jones:** This dodgy sort of heat sink here, it's not actually stuck down there at all. It's not, they forgot the nut on the back of that, so oops. No real surprises here, we have an LM317, which is probably maybe switched to multiple voltages. We have a low dropout 1117 regulator here, basically the same as the LM317, but it is a low dropout type.

**Dave Jones:** And this one's not a regulator, it's a BD139 power transistor. Pretty bog-standard stuff, and then we have LM339 quad comparator. What else do we have here? LM3... LM3T4 quad op amp, of course. And there we have a TLV5620, which is an 8-bit quad DAC.

**Dave Jones:** No surprises there, this thing has to have some sort of DAC in it in order to set the various programming voltages for all the thousands of devices that actually require, you know, 12 volts or even 25 volts programming voltages for some of the older stuff.

**Dave Jones:** So that's absolute classic MC34063 switch mode controller. I've done a video on that, really old-school stuff. They certainly haven't gilded the lily there, that's for sure. And there we... looks like we have a TI, but that's an LM385 voltage-adjustable voltage reference, I believe.

**Dave Jones:** And of course those voltages aren't massively critical, really, you know. So you can get away with an 8-bit, it's not like you need a 12 or a 16-bit DAC in there, that's for sure. And the main FPGA is a Xilinx Spartan III, fairly old-school stuff, but pretty industry-standard stuff.

**Dave Jones:** An XC3S100E series, so that's a fairly low-end, it's only got a couple of thousand logic elements, it's got a bunch of RAM in there as well. Now, curiously, there's one thing I don't see around that FPGA there, and that is the E-squared PROM

**Dave Jones:** to hold the program code. So it must be kept inside this micro, and this micro, I presume it's some sort of micro, programs the Xilinx Spartan III there, because, you know, these really always need, these FPGAs, they're empty when you turn on the power and boot them up.

**Dave Jones:** So they've got to have a programming PROM near them, or around them, but I don't see it there. We've got one crystal oscillator here, which is obviously sharing the same clock for both of them, I would presume. But the code must be in this bastard here.

**Dave Jones:** So what can we see here? We can see an E there, is that like an S or something? I don't know, there's something still under there. Time for a bit of magic spit. Get some on my finger there, and wet that a bit.

**Dave Jones:** See if that comes up. Ah, they didn't do a spectacular job there, so we might be able to, might be able to see that. I don't know, it's a bit hard. It's certainly hard on the screen here, but I've got some sort of number there.

**Dave Jones:** Let me see if I can decode this. Well, I think they've done a really piss-poor job at this, that's for sure. It's scrubbing off these numbers, that's an ST, so it's definitely an XST micro. And I'll see if I can get some better contrast on this number here, it was upside down before,

**Dave Jones:** so I've turned it around the right way. And oh, ARM, there you go, A-R-M, ARM. It's an ST ARM processor, I just need to look at the main number there. And I'll try my X-Tech digital microscope here, I can sort of, gives me a bit better contrast on that thing.

**Dave Jones:** Let's see if we can turn up the, and wait, there we go, I think we might be, might be getting there. Ah, let me decode this off camera. And well folks, that certainly was a piss-poor effort on their part of trying to scrub the number off this thing,

**Dave Jones:** because I had that in next to no time. It's an ST brand, it's an STR710FZ2T6. And that's an ARM7 core processor, a fairly old one, 256k of program memory, 64k of SRAM, and a whole bunch of other stuff built in which they're not using, apart from the USB stuff.

**Dave Jones:** So there you go. Why even bother if you're not going to do it properly? And even if they did scrub that out, it wouldn't be hard to reverse engineer the pin out on that thing, go onto DigiKey, get the number of pins that are on it, and just decode that.

**Dave Jones:** It was, why? Why bother? Idiots. One thing I've noticed on this board is a very high degree of flux residue between the pins on these devices. This board really hasn't been cleaned nicely at all. It's pretty awful, actually. In some parts, it's just horrendous.

**Dave Jones:** I mean, take a look at that resistor network there, it's just... And that stuff around the MC34063 there, pretty horrid. Really crusty. Now, as for the individual transistor pairs here, they're clearly in pairs based on the circuit topology here. And they're both the same type, so it's not like one is an N-channel MOSFET and the other's a P-channel MOSFET.

**Dave Jones:** They're both like a P-channel MOSFET, presumably to switch through a voltage onto, you know, any of the programming voltages or something onto the pins. And on second thought, these probably aren't power-switching ones, they're probably signal-switching ones based on they're coming from the FPGA here, and there's no power stuff around there.

**Dave Jones:** And as we'll look at, there's more power stuff on the more power-looking MOSFETs on the top board. So really, these are probably signal-switching MOSFET, but they are in pairs. And there's 12 pairs of them, so there's only 24 total there. Not nearly enough to have a truly universal programmer and be able to switch every one of the signals

**Dave Jones:** through to any one of the 48 pins on the ZIF socket. And on the top here, you can see there's a whole bunch of thick traces going through there. So these are obviously designed, these are MOSFETs designed to switch the power here. You see there's a common one going through there, two gate drives, and so they're...

**Dave Jones:** And obviously there's a whole bunch of diodes which are designed for protection, of course. They would be reverse protection. We've got a whole bunch of other signal stuff over here, and there's a whole bunch of 74HC595s. Absolute classic 74 series device. These have been used in Universal and other EEPROM programmers

**Dave Jones:** for donkey's years, decades, many many decades. So classic sort of topology with the 595 serial latches there. But really, yeah, I think I counted like 57 or something transistors on this thing. And once again, there's nearly not enough for it to be a true universal programmer.

**Dave Jones:** So obviously they've made some hard decisions there about what devices they're going to support and just what signals they're going to switch through to which pins. So let me give you a little bit of a dave-cad on exactly what I'm talking about here.

**Dave Jones:** Each of these 48 pins, I would expect to have at least a couple of MOSFETs that can A, switch it to ground, of course, like a standard logic drive, okay? Can switch it between ground and normal VCC, whatever VCC happens to be. That might even use another MOSFET over here, programmable, or a pull-up resistor, or something like that.

**Dave Jones:** And then you would have another couple of MOSFETs here that would be driven by various DACs. So this would be DAC 1, this would be DAC 2. You might even have more than that number of DACs and an associated transistor. And these are the drive signals which all come from a complex, well, you know, a vast network

**Dave Jones:** of those 595 serial latch registers, for example. Or a massive pin-count microcontroller or FPGA or GAU device with enough pins to drive 48, the 48-pin socket that we see on here, with, you know, each various drives. But really, I wasn't expecting, like, a DAC per pin, I don't think, on this programmer,

**Dave Jones:** which is, you know, 200 bucks or something like that, or less. You wouldn't get a DAC per pin, you only get those on the real high-end, you know, multi-thousand dollar, big brand name programmers. And if you've got some weird device that requires, say, 12 volts and 25 volts or something else,

**Dave Jones:** requires multiple voltages on multiple pins, a DAC per pin programmer can handle it. But it needs a vast amount more circuitry than what we see on here. It's clearly not the same amount of circuitry. So, obviously, they've done some sort of trade-off in the amount of circuitry

**Dave Jones:** and the type of devices and the pin-outs that they can actually support. But, hey, they can still support 17,000 devices with the setup they've got here. Still very flexible. So I assume that these two MOSFETs, because they're the same type, they're just conveniently located together, so they're not actually a pair,

**Dave Jones:** they've got individual functionality. You can see that they're tapped off the same voltage rail on the bottom, and if I flip that board over, you can see that trace running down there, and they're all common between those MOSFETs, and they run back over to the,

**Dave Jones:** you know, some part of the voltage control circuitry in the DAC circuitry we saw here before. So they're switching something through there, and they're just conveniently laid in pairs just for layout purposes. So they're not actually pairs, it's not like one is switching it through to ground

**Dave Jones:** and the other's switching it through to a voltage or something like that. So they're all switching through to a specific voltage, driven from the FPGA of course. No idea what the FPGA's doing there, whether or not it's just some big glorified shift register

**Dave Jones:** or something like that, or whether or not it does some more intelligent stuff, I don't know. Your guess is as good as mine. And of course these just go through some, it looks like we've got some 102, so we've got a 1k resistor there, it looks like they're all pull-ups,

**Dave Jones:** or something like that perhaps, going through to the header pins. And of course the type I've shown here isn't a true DAC per pin, because that would actually have one DAC, and it wouldn't need the other MOSFET there, it would just have one DAC and feed that.

**Dave Jones:** And then you would have 48 DACs on this thing, one per pin of course. And there's really not much else on here, there's a JTAG header up here for the ARM processor of course, to program that. There's a jumper up here which allows you to recover the firmware,

**Dave Jones:** which I'm actually trying to do because this thing has died in the arse and doesn't seem to connect at all. So I'm trying to recover the firmware on this and get it working again. So if you've got any good ideas on that, please let me know.

**Dave Jones:** And that's pretty much all there is to one of these universal programmers. It's a bit more complicated than the regular EEPROM program, which pretty much just supports EEPROMs. You can get those very cheaply for like $20, $30 on eBay or something like that these days, I think.

**Dave Jones:** But yeah, this one is about, I don't know, $150, $200 or something. I got this one second-hand. And it's, you know, when you get one of these universal programmers, you can actually program many tens of thousands of different parts. But Murphy, as always, will say the part you want cannot be read or programmed

**Dave Jones:** from one of these puppies. Oh, you can't win. Anyway, I hope you enjoyed that. That's a tear down, there's not a huge amount in there. It'd be nice to actually go in and reverse-engineer the schematic in here and stuff, but that's pretty complex business.

**Dave Jones:** But if you do have a schematic to one of these Wellan universal programmers, we would love to see it. They do sell higher-end devices as well. Much more expensive, full-on production programs. This isn't really a production-quality program. It's just like a prototype program.

**Dave Jones:** It's sort of doing a one-off kind of thing. So the big production ones with the 10 ZIF sockets on them, they're much more complex devices. They're probably a DAC per pin as well or something complex like that. But if you do have a schematic, please drop it in the comments or on the EEVblog forum.

**Dave Jones:** And if you like Tear Down Tuesday, please give it a big thumbs up. Catch you next time.
