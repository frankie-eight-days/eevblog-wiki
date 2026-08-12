---
video_id: 4Zw_W0iaGFM
title: EEVblog #1144 - Padauk Programmer Reverse Engineering
url: https://www.youtube.com/watch?v=4Zw_W0iaGFM
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 14, "2": 32, "3": 57, "4": 70, "5": 91, "6": 108, "7": 131, "8": 146, "9": 166, "10": 182, "11": 203, "12": 220, "13": 239, "14": 265, "15": 285, "16": 308, "17": 328, "18": 349, "19": 366, "20": 380, "21": 406, "22": 425, "23": 449, "24": 463, "25": 479, "26": 501, "27": 514, "28": 528, "29": 546, "30": 568, "31": 590, "32": 606, "33": 628, "34": 642, "35": 660, "36": 676, "37": 690, "38": 710, "39": 728, "40": 744, "41": 762, "42": 780, "43": 798, "44": 816, "45": 828, "46": 848, "47": 862, "48": 878}
---

**Dave Jones:** Hey, so I'm going to be kind of going into the reverse engineering of the PMS-150C programming interface. This might be very difficult, it might be very easy, but I suspect it's going to be quite obscure. So, let's just look at what we've got.

**Dave Jones:** So, first things first, I have this SOIC-8. When I talk about a pin, I'm going to be talking about the numbers. The numbers go round anticlockwise. So, 1, 2, 3, 4, 5, 6, 7, 8. Now, I've made some assumptions with this. So, I'm going to assume that this is ground and this is power.

**Dave Jones:** I'm also going to assume that reset is still reset. So, and I'm also going to assume that reset is active low. So, it's resetting when it's at ground. So, it's running when it's at power rail or something. High, logic high. So, that leaves us with five pins to analyze for.

**Dave Jones:** Data and clocks and things like that, which could potentially be to do with programming. Now, why would you want to do this? Why would you not just use the existing programmer? It is pretty cheap, and I think you probably should use the existing programmer.

**Dave Jones:** But you might have a specific application where you simply want to program it in the field or in the device itself. Or you don't have the ability to cart around this huge blue thing, which may well be the case. And it might be that you just want to get rid of a production step.

**Dave Jones:** Maybe your device has the required power rails, and all it would cost is a MOSFET or something to be able to program it when it's in the device itself. Or even just programming it from test points. Maybe you want to do that. Let's probably just get started.

**Dave Jones:** What I have here is the analog discovery. And I have the programmer. And I'm basically just hooking up the... ...the analog pins of the programmer to the oscilloscope section of the analog discovery. So, I'm going to be looking at the power pin and I'm going to look at the reset pin.

**Dave Jones:** To make sure that things actually make some sense, we're going to need to actually sanity check this. So, the yellow waveform, strangely enough, is the power supply. Now, this might look a bit strange because it's got all these levels, and these I suspect are just programming voltages.

**Dave Jones:** If you look at the far left over here, the section that I am circling, you have these on/off moments. And I'm not really sure what's happening here. It's probably entering some kind of initialization mode, although the power line is being turned off, so I'm not really sure.

**Dave Jones:** And reset is being thrown. But after that point, we have this long section, and I suspect this is where the real initialization happens, where it's getting ready to program... It has to enter some kind of programming mode, this device can't just always be in programming mode.

**Dave Jones:** It uses the pins that would normally be I/O for programming. So, it probably has to enter that mode, or it is also possible that it's always in that mode. It could be in that mode initially, and because it's one-time programmable, the first time you program it, it exits that mode forever.

**Dave Jones:** So, that could well be the case. Because of the shape of this waveform, I'm going to assume it's not. I think there is an initialization section, could be wrong, but I don't know. The next section, we get this high voltage section. Now, this is about 6.5 volts up here.

**Dave Jones:** This is probably the section where the PROM itself is being programmed. And I suspect we have some kind of verification happening over here, programming again, and some more verification. What's going on with the reset line? After each section, it appears that a reset takes place.

**Dave Jones:** So, I'm thinking now, the device must be stateful, meaning that after each stage in the programming, it must retain some state, it must know where it is up to. So, those states aren't lost between these resets, because if they were, you would have to start the programming process all over again, and that would be not very useful.

**Dave Jones:** So, yeah. What kinds of things do we need to look at here? Well, from the start to the start of the programming is about 244 milliseconds. We're going to be looking for the data at 244 milliseconds, approximately. It should be pretty obvious when it is, because there should be a fair bit of data.

**Dave Jones:** And the data to this, what I think is initialization section, is 68 milliseconds. So, let's have a look at what I think the clock pin is. Let's see if the clock pin resides inside, when the reset pin is up or down. Now, this will help us determine whether that really is a reset pin, and whether that power pin is really the power pin.

**Dave Jones:** We don't know. It's not actually guaranteed. Until the device is programmed, that spec sheet, the data sheet, doesn't really come into play. It could burn some fuses and change the pins altogether. Let's have a look. Ooh, that does look like a clock line.

**Dave Jones:** Now, we're getting a lot of aliasing, because the sample rate of the ADC on the analog discovery sucks. But, we can zoom in, and I'm going to. I'm just adding some hold-offs, so it doesn't re-trigger immediately. That's really annoying. Okay, so here we go, we're at 244 milliseconds, thereabouts.

**Dave Jones:** I'm having to reprogram it every time. Now, this is a one-time programmable feature. And, because it takes a while to actually swap the device out, I'm only analyzing the data that's sent when it's already programmed. The device doesn't seem to know the difference.

**Dave Jones:** It can't tell whether it's already programmed. So, I'm only analyzing that data, because otherwise it would take forever. Now, there are probably some differences. We've got the power, and what I believe to be the data. So, we should be able to look at a clock, if we zoom into here.

**Dave Jones:** Now, annoyingly, this device isn't perfect. It isn't perfectly timed. You'll notice that the relative timings change slightly. And, that has made this more difficult. You'll notice, see, right now, totally got a wrong section. Okay, so, it does appear that it clocks when the power line is high, which is exactly expected.

**Dave Jones:** And, if we look at the reset pin, we should see basically the same thing, and we do. So, that's great. So, what now? Well, we've got the clock line. Now, we need to find the data line. Now, I believe it to be the next pin.

**Dave Jones:** It usually, they're usually right next to each other. And, from previous probing around, it looks like the data line. So, let's go ahead and find that. Ooh! So, this is the 244 ms section. And, this looks like data. So, with that assumption, I'm going to move the reset line over to the clock line.

**Dave Jones:** So, channel 1, the yellow one, will now be a clock. There we go. So, if I had some good probes, I probably wouldn't do this at all. Okay, so, let's have a look. Well, if you look at this, let's look at this one data pulse, and compare it to the clock.

**Dave Jones:** The clock goes up and down in that data pulse. Now, it's important. It doesn't always do that. You could just have a rising edge inside a data. Um, so, that will change how we interpret the data. So, I believe this section to represent

**Dave Jones:** 1 0 0 1 1 So, I think that's sort of how the serial protocol is working here. And, I don't know whether it's clocking in or I don't know whether it's clocking in and out on the rising or falling edge. But, because they're both inside every data,

**Dave Jones:** it probably doesn't matter so much. Does that make sense? I don't know. Now, there's something to notice. There is this section here. It's a slower clock rate. Don't know what's happening here. I have tried to figure it out. I have no idea. I can't get it to do anything

**Dave Jones:** in that section, so I don't know why it's clocking. So, over here, it's still pulsing in the high frequency section. So, no different than before. Okay, so I've thought about this since, and I've seen this a little bit before. Um, this could be, um,

**Dave Jones:** the clock pulses required to actually process the command. by the, um, by the PMS150C. So, it could take 12 clock pulses to process a word. Perhaps those pulses are required to shift it out of the, out of one register into another. Who knows?

**Dave Jones:** But, I suspect those slow frequency pulses, they're lower frequency because that's, um, how much time it needs to process things. And, they're also, um, they're also required to actually process it. So, I'm not really sure what that low frequency clock section does. So, if we look at this, we do have these

**Dave Jones:** sections, and, um, they sort of seem to align like this. What could this be? Well, this could be the data direction. Um, the only reason I'd think that is because we have some clocks when it's high, and usually you wouldn't have clocks when it's high and you've got a chip select.

**Dave Jones:** If it is a chip select, you wouldn't have a chip select at all. Um, so, data direction, clock when high makes a lot of sense. But, um, then again, it could just be always clocking, and this whole region could be a big, a big chip select.

**Dave Jones:** Um, why would I think that? Well, it's very periodic. Um, if you look at it again, it's almost perfect. Keep zooming out. So, I think, I think our best bet is some form of chip select in pin 3. ... Okay, so I now have a rough idea

**Dave Jones:** of what the data, clock, power, ground, and recent pins are. But, what about pin 2 and pin 7? It doesn't really seem like they have a purpose, so I'm about to investigate that. Pin 2 is one of our possibilities, and I've looked at this

**Dave Jones:** before, and it is a bit weird. It, now this one doesn't, isn't at all interesting when the device is being programmed. It's actually, it does nothing. Um, but when it's not being programmed, there are these constant pulses. What are they? So I've got, this is the, um, this is

**Dave Jones:** pin 6 now. It appears to have a delay after that initial pin 2 pulse. So pin, this is pin 5. Now. Pin 5 is basically synchronized with pin 6, so it doesn't seem to do anything. Pin 7, what does that do? Well, it seems

**Dave Jones:** to be doing the same thing again. Are pins 7 and 6 and 5 synchronized? Let's see. Maybe there's a timing. Now, I'm going to have to move these channels closer to figure it out. No, they're not. They're not in line. So, let's have a look.

**Dave Jones:** What's going on? Oooh. They're one clock apart, each of them. So what does that mean? The program is checking for, um, open circuit. It's constantly doing that. If I, if I connect, um, the ground of my logic analyzer to it, it beeps and tells me

**Dave Jones:** it won't work. And it also won't program. So, I know it is checking for open circuit, and these checks, these strobing of every single pin, each pin individually, will do that. It will be able to tell if if it has a, um, a shorted pin

**Dave Jones:** because it won't be able to drive it high. So, perhaps it's doing that. But also, perhaps it is doing some kind of ID check. Something is embedded in this signal that allows the programmer to tell what chip it is. Perhaps it's that, perhaps it's the

**Dave Jones:** timing of it. Perhaps it's um, the order of the pins if the micro is the host of this process. I don't know. So, I will just go through a few of the problems that I have with this device in decoding the protocol. Um, and there are

**Dave Jones:** a lot. This is a really weird protocol. Um, the voltage changes for everything. Um, so, this is the chip select and the, um, the clock line. And you'll notice that the voltage envelope is the same. So, but it's not constant. Um, around here it's like

**Dave Jones:** 2 point something volts at max. And up here it goes up to 6.5 we saw much earlier. So, it is still quite mysterious what this protocol is doing. Um, there's so many things that are strange about this. And between programming runs, there is slight variation in the timing.

**Dave Jones:** Um, which makes it very difficult to correlate multiple all the pins, all the data from each of the pins without something like a 5 channel um, a scope with a very deep um, deep memory. Um, because I would need to record the whole programming process

**Dave Jones:** to be able to decode it. Um, so if anyone has any ideas, or this looks familiar to you, um, leave it in the comments. Maybe it is some kind of rip-off of an existing protocol. There were some ideas that it was from the old picprom

**Dave Jones:** programmers, but I'm not so sure. Um, but yeah, um, mystery to me. I couldn't use a logic analyzer because the threshold changes because the voltage changes with the, um, programming stage. So, during the prom programming stage is a higher voltage. Um, and it's also a voltage which is above

**Dave Jones:** the range of the logic analyzer. And if I use a voltage divider, which I did before, I actually lose the data from the previous samples, um, because they're below the threshold. If it is a chip select, it doesn't have an easily distinguishable word length.

**Dave Jones:** Um, it also has four programming voltages. Ground. Two volts. Four volts. Five volts. Seven and a half volts. No! Six and a half volts too! Yeah, it's got tons of levels. Don't know what's going on. Um, ah! I hope this was interesting to someone.

**Dave Jones:** Either way, have a good day. See ya. *sad music*
