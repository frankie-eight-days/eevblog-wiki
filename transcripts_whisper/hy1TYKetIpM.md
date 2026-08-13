---
video_id: hy1TYKetIpM
title: EEVblog #145 - Agilent LAN/VGA Module Teardown
url: https://www.youtube.com/watch?v=hy1TYKetIpM
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 18, "2": 34, "3": 46, "4": 80, "5": 95, "6": 122, "7": 149, "8": 172, "9": 200, "10": 219, "11": 244, "12": 258, "13": 275, "14": 294, "15": 313, "16": 332, "17": 348, "18": 365, "19": 387, "20": 409, "21": 425, "22": 447, "23": 461, "24": 478, "25": 496, "26": 511, "27": 533, "28": 551, "29": 572, "30": 591, "31": 600, "32": 620, "33": 635, "34": 656, "35": 678, "36": 690, "37": 709, "38": 722}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, in the previous blog I reviewed the new Agilent 2000 X-Series oscilloscope and it was a beauty and I did a tear down of it,

**Dave Jones:** which everyone seemed to love, but I forgot one thing. I forgot to tear down the optional LAN VGA module and somebody asked if I could do it. Is there any circuitry inside here? Are Agilent just ripping you off? Is it just the connectors and all the circuitry is still

**Dave Jones:** inside the scope? Well, what do you get for your 400 bucks? Good question. Let's find out. Somehow I don't think I'd need to do this in fast motion. There's only two screws on it by the looks of it, so let's crack it open.

**Dave Jones:** There's one. And there's the other. I can see circuitry in there. Look at that. Whoa. Hello. Look at it. There we go. They're not ripping you off. There is some circuitry in there. Okay, let's take a look at what we've got here. We've got a Spartan 3S100 FPGA on the top here,

**Dave Jones:** which is not a particularly top-of-the-line FPGA. It's a rather cheap one. It's only 100k gates. And on the back here, we've got a 4 megabit Cypress SRAM, which is obviously the frame buffer for the VGA output coupled with the FPGA on the top.

**Dave Jones:** The FPGA does all the timing and everything else, and the actual frame data for the VGA display is stored in the 4 megabit SRAM there. And down here, we've got an Analog Devices ADV7125, and that there is a three-channel DAC. Very typical of what you'd find in a VGA, a typical VGA display.

**Dave Jones:** So this is a classic FPGA-implemented VGA display. These two devices here are obviously local voltage regulation. You can tell by the power tracks actually going to them, and the input and output capacitors. It's a dead giveaway. I don't even have to read the numbers on those to figure it out.

**Dave Jones:** And one thing you'll notice is that there is no circuitry for the LAN at all. All we've got is the two differential pairs coming out here, going straight into the connector. And this is just a classic, what they call a MagJack, or a magnetic jack, because it contains the magnetics

**Dave Jones:** required for isolation for the Ethernet interface. So not only will that MagJack contain the isolation transformers, it'll also contain the termination resistors as well. Because normally, these used to be separate devices. You used to have to have separate isolation transformers. If you've seen like an old PC Ethernet card, then you'll see these little big black

**Dave Jones:** square isolation transformers. Well, they don't have those anymore. Pretty much everyone is using these MagJacks. They really are the way to go. So clearly, the Ethernet interface is being handled by the ARM micro. These differential pairs here, they'll be matched length of course,

**Dave Jones:** they will go straight into the ARM9 micro, which we saw in the teardown of the scope. And there's a JTAG interface over here, of course, for the FPGA. And that's pretty much it. There's nothing, you know, it's just a basic implemented VGA controller with the DAC for the

**Dave Jones:** RGB signals. It generates the timing. One thing you'll notice that's not on here is a crystal. There is no oscillator at all on here. So obviously, the timing is coming from the main board. It's coming from the DSO. So that's where it gets its clock from.

**Dave Jones:** I guess, why not? Because you save a bit of system cost there. Why would you bother putting an oscillator on here, which, you know, might cost 50 cents or something, when you can tap the signal straight from your DSO along here? So they're up to REV6 on the board.

**Dave Jones:** I think that was the same as what was in the DSO from memory. So they've had six goes at this board either. Well, A, either they've had six goes at it, or B, they actually automatically update this board when the other one gets

**Dave Jones:** updated. That's another technique, but I doubt it. It'd be a bit silly to update this particular module. It would be its own project, and well, there's not much in here at all. So it's certainly not 400 bucks worth of parts. It's, you know, even from Digikey one-off, it's probably only

**Dave Jones:** 30 or 40 bucks worth of parts. So it's not much at all. So clearly, what you're paying for is the development, and you're paying for, well, because it's Agilent, where everything's optional extra. Let's take a quick look at the layout, because there's something I immediately noticed here.

**Dave Jones:** The DAC, okay? The entire DAC subsystem here is, well, it's here. And why isn't it up near the VGA connector? Because if I was laying out this board, I would have gone, right, I've got a DAC that has analog output signals, and it should be near its connector.

**Dave Jones:** The last thing you want is for those signals to be running right across the board. And especially, you don't want them running underneath a high-speed SRAM like that, with all those digital signals blaring away. You really, that's the last thing you want. So I reckon that's a very strange layout decision there.

**Dave Jones:** I mean, they've obviously got a six-layer board here. The reason you can tell that is because there's virtually no tracks coming out of this SRAM here. They're just going down into some vias down there, and if you have a look on the top, there's no corresponding tracks on the top which go to the

**Dave Jones:** FPGA. So obviously they're on internal layers, so you would have two internal signal layers, plus you can see that there's ground, and there's likely a power plane in there as well. So that is likely a six-layer board. So, well, it's a minimum of a six-layer board, because you can't

**Dave Jones:** see the inner traces on the bottom. So that's how you can tell that there's a ground and a power. So layers, you know, two and five would be ground and power, and with the two signal layers in the middle, which you can't see.

**Dave Jones:** Now, yeah, I just think that's a crazy decision. And the other thing you'll notice is that it's a two-sided load. There's components on both sides, and that just increases your manufacturing cost and complexity. Now, granted, I don't know how many modules of these, how many of these modules they're actually going to sell, so the point might

**Dave Jones:** be a bit moot, but as a layout designer, I would have tried to get this, as a first pass, I would have tried to lay this out all on one side here. You know, you could have moved the FPGA down to the bottom here.

**Dave Jones:** You could have put the SRAM right next to it, or above it, or something like that. You could have put the DAC and all of its associated circuitry up near the connector here. So you might have had FPGA here, SRAM sort of tucked in there, DAC over in this corner here,

**Dave Jones:** and your power supplies, you know, here, or something like that, because you've got your ground planes there, and they're low inductance. You don't necessarily need your power supplies right next to the FPGA. You've got a bit of leeway there. But granted, you wouldn't, actually,

**Dave Jones:** on second thought, you wouldn't put, say, this regulator over here, because then these are the two input power tracks. You've got to get those over there, which is crazy. So I would have, yeah, I would have just moved that down to there, put it in there, put it, well, on the top side, anyway,

**Dave Jones:** this one would have gone down in this corner over here, and then the FPGA, yep, tucks in, tucks in the middle there, SRAM, boom. I don't know. I just found that layout decision strange. I don't know what the layout designer was thinking. So why have they gone and put the LAN and the VGA on a separate

**Dave Jones:** plug-in module? Why didn't they build it into the scope? Well, your guess is as good as mine, but it obviously has a lot to do with, it all ties into the system engineering aspect of it, the budget constraints for the scope, because when you're designing a base model scope like this one,

**Dave Jones:** you really do have to be cost-conscious. And although these parts on here aren't worth an absolute fortune, they do eat into your budget, your Bill of Materials budget, for your scope. So really, you know, the VGA side of it, I can kind of understand why they sort of separated this out.

**Dave Jones:** Now, you could argue that the ARM9 processor in the DSO, because it's not actually handling the refresh of the screen directly, which is what we found out in the previous blog when we did the teardown, it's handled by the ASIC in there. So maybe it would have had some grunt left over to

**Dave Jones:** do the VGA direct, but then you still would have needed the frame buffer and, you know, everything else. And well, you know, you're going to need this external circuitry, and you're probably going to need the DAC as well, because I don't think that the ARM chip has a built-in VGA output.

**Dave Jones:** I haven't checked, but I'm assuming that it doesn't. So really, from a systems engineering point of view, it kind of makes sense to separate out the VGA. So they could have done this as just a video output board. Now, why they've chosen VGA?

**Dave Jones:** VGA is a legacy interface, really. It really is dying out. It would have been a much more sensible choice to do a HDMI slash DVI interface. You know, for a 400 buck module, they could have easily afforded to do a HDMI output version.

**Dave Jones:** So I don't know why they've done that. Now, when it comes to the LAN interface, the only component they're saving cost on in the DSO is the MagJack, and MagJacks aren't that expensive at all. They're very, very cheap. So why Agilent have not included this in the base model DSO?

**Dave Jones:** It's not a bill of materials issue. It's not a cost issue. It would have been a marketing issue. It would have been, like, marketing sales they wanted. Maybe they thought, oh, if we just had this as a video board, then, well, maybe they

**Dave Jones:** made the decision first, okay, let's separate out this video board. You know, we can't really afford the cost in the base unit. Fair enough. Let's put in a separate board. But, hey, and then somebody said, hey, we can't afford, you know, we can't just have a video output board.

**Dave Jones:** People aren't going to buy just that. So why not put, separate out something that's more useful to make it enticing to buy this module? Why not stick the LAN on there? Everyone's going to want a LAN. They'll think they're getting real value for money.

**Dave Jones:** If we just charge 400 bucks for just the VGA interface, people might get a bit pissed off, maybe. But, you know, so why not separate out the LAN? So maybe that's where the design decision for separating out the LAN come from. I don't know.

**Dave Jones:** Pure, utter speculation on my part, but an educated guess.
