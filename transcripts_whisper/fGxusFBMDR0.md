---
video_id: fGxusFBMDR0
title: EEVblog #144 - Agilent 2000 X Series Infiniivision Oscilloscope Teardown
url: https://www.youtube.com/watch?v=fGxusFBMDR0
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 23, "2": 52, "3": 69, "4": 90, "5": 115, "6": 135, "7": 148, "8": 274, "9": 314, "10": 331, "11": 342, "12": 364, "13": 379, "14": 399, "15": 416, "16": 433, "17": 464, "18": 483, "19": 504, "20": 515, "21": 539, "22": 561, "23": 583, "24": 634, "25": 654, "26": 664, "27": 691, "28": 772, "29": 791, "30": 843, "31": 854, "32": 874, "33": 892, "34": 1019}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, what was that? You're curious to know what's inside this new Agilent InfiniiVision 2000 series oscilloscope? Well, so am I. And you know what we say here on the EEVblog, don't turn it on,

**Dave Jones:** take it apart. So let's crack this sucker open and see what's inside. Beauty. Okay, we've got the back off and I'm impressed. Look at the shielding on this thing. Look at all the pressed metal work. It's just quite remarkable. And the fan, check out, check out

**Dave Jones:** the fan. It's actually, that's actually a rubber, a rubber surround on that. That's why it's so quiet. See how it, see how it moves there? It's actually compliant. So it's got a little, it's got vibration damping in there and I'm sure they've chosen a quality fan as well.

**Dave Jones:** But it looks excellent, well shielded. It looks like there's a power supply baseboard down the bottom here. There's the real interface power switch down the bottom there. And there's the choke and there's the mains input. It's beautiful. And check out the shielding they've got on the

**Dave Jones:** USB connectors up here. Awesome. One other thing I noticed, the BNCs on the back here, made by AMP. So they're not some 100 low brand, they're quality components as you'd expect from Agilent. I've taken off the shield for the switch mode power supply and check out this switch mode

**Dave Jones:** power supply module here. It looks superbly designed and engineered. I love it. And the really nice high quality cable looms and connectors which go over to the main board in the back there. Completely shielded between the main board and the switch mode. And the

**Dave Jones:** baseboard down here as well is entirely Agilent. It's got the Agilent logo down in there. You may not be able to see it but it's in there, trust me. And there's a fan controller down there. It looks beautifully laid out, beautifully designed so far.

**Dave Jones:** I'm liking it. There's the label for the switch mode supply. It's from Lineage Power. It's a universal 100 to 240 volt input of course. And it looks like a lovely unit. Made in China of course but I think Agilent would have chosen a quality supplier there for their switch mode, no doubt at all.

**Dave Jones:** So and here it is in its naked glory. That was pretty darn easy to take apart. It was designed really well to actually do that. The construction quality of this thing is remarkable. The effort that's gone into actually designing it to be, well I'm not going to say designed to be repairable,

**Dave Jones:** but designed to take it apart is just, it's just remarkable. All of the screws are essentially almost all of the screws are exactly the same. They're identical and it just popped apart real easy. And this is pretty much what I expected. Here's your four input channels.

**Dave Jones:** They're in their cans of course. Unfortunately they're soldered onto there so we're not going to be able to take those off. So let's look at some of the parts in a bit more detail. Let's have a look at what we've got here. We've got the four cans.

**Dave Jones:** These are the four channel converters obviously and they're actually soldered. Those cans are soldered on there so they would actually require quite a lot of butchering to actually get those off. Now these are clearly the two ASICs. I was expecting one big ASIC which handles everything.

**Dave Jones:** That's what I was led to believe especially when you power on the scope and there's a picture of the one big wonderful ASIC which does everything. It's clearly got two. Now as you can see the traces coming from these controlled impedance serial lines here coming

**Dave Jones:** from the four modules. This is obviously the acquisition ASIC. That's the acquisition part of it and then it obviously transfers. This one's probably the memory or something like that. It's got the display memory. Who knows? I wouldn't even hazard a guess as to the architecture used

**Dave Jones:** between these two devices but they're clearly the key to the whole thing. The performance, the phenomenal update rate of this unit and this circuitry up in the top corner here is obviously your power supply section for the ASIC and probably for the modules as well but the

**Dave Jones:** analog modules would almost certainly have their own local power as well. The ultra low noise power supply so that clearly just probably dedicated to the two ASICs. And for those who love to hack there's your JTAG interface right under the ASICs and by far the biggest surprise I got when I opened this is the main processor.

**Dave Jones:** I had money that it would be an Intel Atom processor running Windows CE but it's not. It's an ST Micro ARM 926 Spear system on chip. Now this particular device has a couple of hundred thousand logic gates as well so it's got like FPGA type capability built in and that's clearly coupled

**Dave Jones:** to a Xilinx Spartan 3 FPGA as well so that's a particularly powerful combination but not nearly as powerful as I thought it would be. I was expecting an Intel Atom not sort of a, I'm not going to say bottom of the range ARM 9 but you know not a particularly, it's certainly not one

**Dave Jones:** of the most powerful ARM processors on the market that's for sure. So clearly this processor is not going to be doing the real heavy lifting for the display updating. That's going to be in one of the ASIC custom Agilent ASIC chips because this thing will handle Ethernet and the USB ports

**Dave Jones:** and stuff like that and just you know the generic operating system stuff the file system and all that sort of stuff and it will do the display capability but it's, I don't think, I think it's clearly not responsible for the real-time display updating capability.

**Dave Jones:** I think they may have offloaded that to the custom ASIC. That's my guess anyway and bingo that looks like another JTAG interface for those who want to play around. And it seems I was right with the display processing. If you have a look at the main, one of the main ASICs here, the what I call the second one, it, check out all

**Dave Jones:** the traces heading all the way over here through these, through to the other side and guess what's on the other side? Ta-da! The display connector! So there you go. Obviously this ASIC here is directly responsible for the display in some aspect. So I presume the processor which is over here

**Dave Jones:** actually doesn't talk to the display directly. It probably goes through that particular ASIC which handles everything, or at least it's got part of it anyway, especially the waveform updating and waveform acquisition and display getting those 50,000 waveform updates per second. And you just can't beat old school can you?

**Dave Jones:** A whole bunch of LM324 quad op amps. So and this section down here, because it's right above the logic analyzer input, is clearly the logic analyzer circuitry. And as you'll see there are only two chips soldered in there out of four. So obviously this board is laid out for 16 channel logic analyzer capability, but none

**Dave Jones:** of the 2000 series models, so far at least anyway, have 16 channel capability. So is this the 3000 series board and it's dumbed down to take off the circuitry to get to the 2000? I don't know, because I haven't opened up the 3000 series model yet, but that's rather interesting.

**Dave Jones:** And if you're curious to know what those logic analyzer input chips are, they're max 9201 quad comparators. Now that's one thing with the two Agilent custom ASICs, you'll notice that there's no memory surrounding them. That's because the sample memory is built onto the die.

**Dave Jones:** As you'd expect from an Agilent designed and manufactured oscilloscope, the PCB, not only the component quality, but the assembly quality in their plant in Malaysia is first class. It really is. It looks like the components are quality components. The soldering is superb and the quality of the PCB

**Dave Jones:** material is excellent. I love it. So and there's the front panel of the scope. Once again, it came apart pretty easily. It's superbly designed. Oh, my hat's off to the guys and girls at Agilent who have crafted this thing, because it really is beautiful.

**Dave Jones:** And there's the front panel PCB that handles that, and that's the soft button PCB. There's nothing else there. And you'll notice that it's, once again, Agilent branded. It's got Agilent written all over it. And there's the display on the front and the input

**Dave Jones:** connectors, and that's the flat flex cable which goes to the front panel PCB. Superbly engineered. Absolute precision. I love it. So and here's the bottom of the board. Really not much to speak of at all. There's a memory chip up there, and most of it is just localized power, some filtering, some miscellaneous

**Dave Jones:** support circuitry, stuff like that. So yeah, nothing to write home about on the back at all. And there's the input jacks and the back of the input circuitry as well. And you'll notice how there's these high-speed differential pairs here running into this secondary ASIC now.

**Dave Jones:** So if you remember before how we had the top of the board like this, the input channels on the top here ran into this ASIC. But on the bottom here, they don't. They run into the secondary ASIC here. So that secondary ASIC is connected directly to the input channels as well.

**Dave Jones:** I know that everyone wants to see me take these cans off the input channels, but they're soldered on, and I don't want to butcher it, but you can see under there there's a couple of SMD devices. There's a big relay, and that's about it.

**Dave Jones:** You know, you don't really have to do much for a 200 megahertz front end these days. So I hope you enjoyed that. That's a teardown of the new Agilent InfiniiVision 2000 series oscilloscope, and it's just beautiful. Brings a tear to the eye. Now for the big test.

**Dave Jones:** Will it work? Woohoo! There it is. Just like I bought one. Beauty.
