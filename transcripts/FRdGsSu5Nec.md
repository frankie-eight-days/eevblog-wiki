---
video_id: FRdGsSu5Nec
title: EEVblog #236 - FE-5680A Rubidium Standard Teardown
url: https://www.youtube.com/watch?v=FRdGsSu5Nec
source: youtube-asr
timestamps: {"0": 16, "1": 27, "2": 49, "3": 60, "4": 77, "5": 89, "6": 107, "7": 122, "8": 135, "9": 145, "10": 166, "11": 180, "12": 200, "13": 217, "14": 228, "15": 245, "16": 271, "17": 285, "18": 295, "19": 310, "20": 321, "21": 332, "22": 349, "23": 363, "24": 378, "25": 389, "26": 402, "27": 421, "28": 437, "29": 457, "30": 474, "31": 493, "32": 520, "33": 531, "34": 544}
---

**Dave Jones:** Here's a first look inside. I took the bottom plate off. That was relatively easy and they've got a custom cut mylar sheet here presumably to stop any shorts or anything like that.

**Dave Jones:** And tada! And there's your magic physics package and it's got a lot of other control circuitry as well. There's quite a bit in this thing. And down in there to connect to the physics package, there's a flat flex cable which and a little flat flex board there which takes all the uh all the signals back up to this part of the board somewhere here.

**Dave Jones:** So, that's rather nice. There's a fair bit of engineering which has gone into this thing. And I can tell you I can still feel the heat. The uh that looks like the discharge lamp and that's the uh hottest part of it.

**Dave Jones:** There's your resonance uh cell down there and your photo detector will be uh somewhere in there as long as and uh your uh microwave uh generator as well. So, that is the physics package inside a rubidium frequency standard.

**Dave Jones:** I like it. All right, let's take a look at the processing and control circuitry around here. This one here is an 80C uh 323. It's an 80C 32 but it's a Dallas Semiconductor part.

**Dave Jones:** So, it's a DS 80C 323. Um classic 8-bit microcontroller. This one here is a PSD 813F and that is a companion device for 80 51 type devices. It's got 1 mega flash uh built in.

**Dave Jones:** It's got 256K of EPROM, 16K of SRAM. It's got uh you know, 30 odd IO ports, things like that. We've got a Xilinx CPLD here. That's a um XC9572XL.

**Dave Jones:** And that is the processing core or the processing guts of this thing. And I've got some analog stuff around here as well as what looks like a little surface mount coax connector there.

**Dave Jones:** That might possibly go out to the front panel. Although the front panel's all the way at the top part of it there. So maybe some sort of test connector.

**Dave Jones:** And looking here, what do you know? I instantly recognize the AD9832 programmable DDS signal generator. So it looks like uh this thing actually has uh the capability to do that serial programmable frequency I was talking about.

**Dave Jones:** And if it's even got a MAX232 there to do it. So presumably unless they just disconnect the pins and leave the circuitry there. Um something like that. Then this thing should have that serial input capability.

**Dave Jones:** I'll have to probe around the pins and try that one out. Awesome. And that looks like some sort of unpopulated switch mode converter or something like that. So I'm not quite sure but it's got the big shield around there possibly to put external shield on top of it if they actually have the circuitry there.

**Dave Jones:** There's a couple of bent over 90° TO5 pin TO220 packages stuffed in there. And it looks like they're using that or the entire that which big huge brass metal center piece as the heat sink which connects to the upper and lower cases.

**Dave Jones:** So they're presumably um some sort of drivers for the physics package here. And there's a third device here which they've done that to and a whole bunch of unpopulated stuff around here.

**Dave Jones:** I'm not sure why that's unpopulated. I'm not sure what additional capability that would actually give you, but there you go. That's the I guess you call this the top side even though it's probably the underside of the board technically, and it's it's quite neat.

**Dave Jones:** And that additional capability there with the programmable digitally programmable function generator. Wow, I'm going to have to check that out cuz this one was not advertised as having that capability, whereas some of them on eBay do actually advertise that they are serial output capable devices, but I think this one probably is too.

**Dave Jones:** And there's the assembly once I've lifted it out. They've got some foam padding here. They've got more circuitry underneath there, and not sure why they've added the foam packaging, just impact protection or something like that.

**Dave Jones:** And jeez, it's almost chock-a-block on the bottom of the board or the top side of the board as well. And it looks like we've got some 2941 linear regulators in there.

**Dave Jones:** Once again, bolted onto there as the heat sink. A lot of unpopulated circuitry. There's another device in there and a coax running off to presumably the physics package in there.

**Dave Jones:** That could possibly be the photo cell output or something like that. Who knows? And this is absolutely fascinating. Take a look at it. There's the the main oscillator in it.

**Dave Jones:** There's the quartz oscillator in a standard can, sort of 90° mounted like that, but it's got something on top of it. And I'm not sure what that actually is.

**Dave Jones:** There's got two little leads coming down from it, soldered onto there. It's like some sort of sensor pad. Is it a thermocouple type device which is measuring the temperature of the actual of the can of the oscillator.

**Dave Jones:** I'm I'm going to presume that's what it is. And these two devices in here are max 411 7 high-speed current feedback op-amps. And on the end of the board is this connector which I'm presuming would be a test connector.

**Dave Jones:** There's a max 392 there which is a multi-channel analog max. So I'm assuming that's sort of some sort of test interface that they hook up when they test and uh calibrate and program this thing during production.

**Dave Jones:** Now, basically, the thing I notice about this board is that it's pretty much, you know, spared no expense because these sort of things cost thousands of dollars. So they just they don't try and cost optimize the design at all.

**Dave Jones:** They just build in whatever works, whatever they need to get the job done, whatever precision analog devices they need. Not a problem. Now, I think I'm going to stand corrected on that.

**Dave Jones:** I think this is the RF generator section to generate the high-frequency output to drive. Hence the the really fatness of that RF cable there. I think that is designed to drive the physics package.

**Dave Jones:** That's not the photocell output. That's the RF output designed to drive that. And over here, I think is, you know, the photocell. I think signal probably comes back via this ribbon cable here into these bunch of op-amps down here.

**Dave Jones:** And they've got a couple of 10-turn trim pots down there. I don't know what that's for, tweaking or calibrating the thing or something like that. And here we've got a couple of IFU 220 N-channel power MOSFETs actually soldered directly onto the back of the physics package like that.

**Dave Jones:** Neat. Do I sense a slight budge there with that uh capacitor that surface mount capacitor vertically raised up like that with the wire hanging off it? Uh I don't know whether or not not that's intentional or uh what they've done there.

**Dave Jones:** Yet another linear regulator there hooked on to the main heat sink and that pretty much covers the entire device. Really, there's some unusual uh construction techniques in there. It's got the interesting foam, some hand stuff, but I really like it.

**Dave Jones:** It's really quite nice and novel. They've really gone to town. There's quite a lot of uh system engineering which goes into not only just uh doing the circuit, but doing the physical layout of this thing as well and getting it right and getting it to dissipate the power in that uh package and, you know, making it reliable cuz these things that have to be super reliable or there'd be I

**Dave Jones:** presume really stringent uh testing and performance checks on these things. So, there you have it. That's inside the FE-5680A rubidium frequency standard. I'd recommend you pick one up on eBay.

**Dave Jones:** Uh I've run out of time to uh build it into a case so and uh get it working. So, I'm going to have to uh leave that for uh future uh episode and uh possibly that serial interface as well.

**Dave Jones:** That's intriguing. But, I hope you like that. I'll catch you next time.
