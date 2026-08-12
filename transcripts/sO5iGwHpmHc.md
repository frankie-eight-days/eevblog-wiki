---
video_id: sO5iGwHpmHc
title: EEVblog #37 - Rigol DS1052E Oscilloscope Teardown
url: https://www.youtube.com/watch?v=sO5iGwHpmHc
source: youtube-asr
timestamps: {"0": 11, "1": 26, "2": 41, "3": 56, "4": 71, "5": 92, "6": 112, "7": 127, "8": 144, "9": 158, "10": 174, "11": 186, "12": 206, "13": 225, "14": 237, "15": 252, "16": 267, "17": 280, "18": 297, "19": 311, "20": 329, "21": 342, "22": 357, "23": 368, "24": 384, "25": 396, "26": 413, "27": 425, "28": 440, "29": 456, "30": 470, "31": 491, "32": 507, "33": 522, "34": 536, "35": 551, "36": 568, "37": 583}
---

**Dave Jones:** Hi, welcome to the blog. I'm your host Dave Jones. And this time around we've got an old friend we're going to revisit, the Rigol DS1052E oscilloscope. I've reviewed this before. People can't get enough of it. We've looked at it a couple of times in

**Dave Jones:** various aspects, but this time we're going to take it apart. And once you've taken off those screws and gotten rid of that bracket, the cover just lifts off like that. And as you can see, it's uh fully shielded. The whole thing is

**Dave Jones:** encased in a complete uh metal shield, which is really quite high quality. It's really It's really actually quite impressive. As you take off the two uh jack screws here for the D D connector, then this just uh pops off

**Dave Jones:** like this. And bingo, here it is. All the innards are exposed. There's the power supply as we'll take a look at, but there's what everyone's interested in, which is the main board. There's the um switch mode uh power supply, and this actually

**Dave Jones:** looks really good quality. Because not only is it um FR4 PCB um instead of the usual phenolic base stuff, you can see it's actually got really um quite high quality construction. It's got a really nice quality fuse holder here. It's uh the

**Dave Jones:** earth connection's done really well. The um it's got all the protection type stuff. This just really looks like a very well-designed and top-quality switch mode power supply, much better than what you would you'd expect for a typical uh Chinese product like this. And I know

**Dave Jones:** what everyone's thinking, what everyone wants to see. The ADC chips. Here are three ADC chips. 1 2 3. Yes, they've had the numbers rubbed off, but on the second chip here, I've actually looked at this in detail, and I'll show you a

**Dave Jones:** high-res photo of it. Here you go. Yes, it is actually the dash 40 part. It's the 80 92 88 ADC, and it's actually the 40 MHz part, just like the that other guy's unit. So, that wasn't unique. My

**Dave Jones:** one's got it as well. And yes, I've actually checked the clock going to the chip. I won't do it now because it's a bit touchy to do live, but here's a screenshot of the actual frequency, the actual clock frequency

**Dave Jones:** going into the chip. And sure enough, it's 100 MHz. So, I hope that dispelled any of the rumors that this thing wasn't actually overclocked. It was just done using software or something like that. No, they do actually overclock this chip.

**Dave Jones:** So, Rigol have been caught with their pants down yet again. The interesting thing about this board is that the more I look at it, the more I actually look at the components on it and look at the quality of the

**Dave Jones:** construction and the layout and the design, this is actually really a top-quality actual unit. Top-quality design, top-quality layout, and they've used surprisingly prime spec parts for all of this. Look, the there's a got a little buzzer in here. It's a TDK brand. All of the chips

**Dave Jones:** are, and it goes for all the all the chips in here. I recognize almost every brand. They haven't substituted any cheap Asian no-name generic brand parts at all. These are all prime spec parts, which is really amazing for the price

**Dave Jones:** bracket which they market this thing in. It's under It's now under 500 US dollars. Okay, now let's look at the different parts. Under the can here, we've got the dual input channels. I'll show you inside those in a minute.

**Dave Jones:** Um over there is the trigger input circuitry. You probably can't see right in there, but it's nothing to write home about. I can probably show you some photos of that. And uh then we've got some um generic uh

**Dave Jones:** analog circuitry here, which um lifts which uh DC offsets the input and shifts it and does uh various other multi plexing type um functions. And these input relays here, I think I mentioned it in a previous blog, these actually

**Dave Jones:** switch between um uh whether you feed the signal into five ADCs. There's actually two ADCs per chip. So, there's uh six there and there's another two ADCs on the bottom of the board as well. So, a total of 10

**Dave Jones:** ADCs. So, these relays switch the signal between either going to five ADCs or 10 ADCs. And the reason for that is because if in uh dual channel mode, you actually get half the sample rate. So, you're actually um

**Dave Jones:** only use half the number of ADCs cuz they stagger them as I've mentioned in a previous blog. The signals from the ADCs here, they're actually captured by this Cyclone III Altera FPGA here. Um now, curiously, they've actually got a

**Dave Jones:** Lattice CPLD here as well. Now, what would you put in this CPLD that you wouldn't be able to fit inside this big FPGA here? Well, the only thing I can really think of is because the timing inside PLDs is much more

**Dave Jones:** uh much more deterministic than what you get inside an FPGA. It's very hard to determine the routing, the exact routing time inside these things. It's quite It's much more complex than a PLD. They probably use this to generate the

**Dave Jones:** stagger clocks for the 10 um analog-to-digital converter chips as I've explained in a previous blog. Now, this is the main uh 2 MB 1 MB of memory, sample memory, which is hooked onto the FPGA here. There's a couple of headers.

**Dave Jones:** I don't know what this That looks like a 40-pin header there. I'm not sure what that's for. It's not like an IDE interface or something like that. It's It's definitely something else. So, there's a few headers here, and they're

**Dave Jones:** rather interesting. They're probably like a JTAG header or something like that. I forgot to mention one thing over here. Look at this voltage regulator. It's a 7905, and it's just sitting up there in free space like that. It's not actually

**Dave Jones:** bolted down. And I've mentioned this in a previous blog. That's actually bad for vibration. That can actually vibrate off. So, that's That's really the only bad aspect of this design I can find. Now, here's the main part of the

**Dave Jones:** product. This is an Analog Devices Blackfin DSP processor, and this is what actually drives the entire firmware and drives the LCD and the controls and and everything. And the reason they need a DSP processor, a digital signal processor,

**Dave Jones:** is because of all the FFT and other functions that this scope is capable of. So, you can't really do that with an Well, you can do it with a normal processor, but this is much A DSP is going to be much, much quicker at

**Dave Jones:** processing FFTs, which it does on the analog input channels as well as the frequency spectrum display as well. So, it really needs a grunty DSP, and it's certainly got one. And there's the SDRAM for it, and also the flash chip as well

**Dave Jones:** that holds the firmware. That's all pretty standard stuff. And right here is an NXP controller chip for the front and rear panel universal serial bus interface. That's all pretty standard. Once again, another Prime Spec chip. They haven't spec'd in. You can get

**Dave Jones:** cheap Chinese versions of, you know, a good lot of these chips on here, and they haven't used them. One of my main reasons for taking this apart was to see if I could actually modify the analog front end down here, cuz this is the 50

**Dave Jones:** MHz model, the DS1052E, but there's also a 100 MHz model, the DS1102E. And the only difference, the only difference at all, is the analog bandwidth, at the input analog bandwidth. And that's it, 50 or 100 MHz. Now, I've seen photos inside someone

**Dave Jones:** else's 100 MHz uh front end, and it's identical to this one. So, um at the moment, I haven't been able to figure it out. But, um it looks like maybe it's only a component uh value difference or something like that. I'm

**Dave Jones:** not really sure, but if anyone um has any ideas or things like that, let me know, cuz it'd be great. It's like a $300, almost double the price for the 100 MHz version of this oscilloscope. I'm sure it's it's capable of being

**Dave Jones:** done. It's just a matter of really finding the uh the right component and what the difference is. Um it's it's either in the analog front end down in the metal can there, or it's in this um uh support circuitry down here, which

**Dave Jones:** I've mentioned before. And I'm not sure which one, but I've actually measured I've done a basic measurement. I fed in a 100 MHz signal, and it does actually get attenuated before it gets to the ADC. So, it it is an analog um input

**Dave Jones:** bandwidth limitation. After opening this thing, this Rigol oscilloscope, I'm even more impressed with it. I just simply cannot believe that they use all prime spec components. And the And the quality in the design of this thing, the actual

**Dave Jones:** layout of the board, and the actual uh design of it, and the and the quality of the build construction, and the the power supply in it is is really top quality. A lot of effort's gone into this. Somebody really knows their stuff.

**Dave Jones:** The team that designed this really knows how to design quality products. And I don't know how they get the incredibly low prices because they're not using rip-off parts. Well, they're all prime spec. It's incredible. Rygo, fantastic value for money.
