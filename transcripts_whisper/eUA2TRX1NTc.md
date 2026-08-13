---
video_id: eUA2TRX1NTc
title: STM32 ARM Development - DMA & ADC Discussion
url: https://www.youtube.com/watch?v=eUA2TRX1NTc
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 27, "2": 45, "3": 69, "4": 90, "5": 105, "6": 131, "7": 154, "8": 171, "9": 191, "10": 209, "11": 230, "12": 247, "13": 268, "14": 295, "15": 316, "16": 316, "17": 346, "18": 371, "19": 402, "20": 427, "21": 460, "22": 460, "23": 480, "24": 507, "25": 562, "26": 580, "27": 620, "28": 634, "29": 661, "30": 688, "31": 702, "32": 735, "33": 750, "34": 772, "35": 801, "36": 829, "37": 856, "38": 875, "39": 903, "40": 934, "41": 962, "42": 978, "43": 992, "44": 1009, "45": 1025, "46": 1046, "47": 1069, "48": 1094, "49": 1118, "50": 1147, "51": 1170, "52": 1189, "53": 1213, "54": 1234, "55": 1252, "56": 1275, "57": 1301, "58": 1318, "59": 1339}
---

**Dave Jones:** Hey! So, I'm going to be talking about the STM32F072. It's ADC and DMA module and this is not a tutorial, this is more like a high-level descriptive video, which for people who are using this microcontroller and the ADC or DMA module, you know, it might give them some ideas and some pointers as to how to

**Dave Jones:** resolve issues, especially the ones that you have with the ADC. So, take that as it is, this video is not a tutorial, it's just a high-level overview. There's a lot of details in these modules that I'm not going into whatsoever. So, anyway, let's get started.

**Dave Jones:** With the ADC and interrupts enabled, it simply won't work if you're doing a sequence of samples and the reason is because it takes a while for the interrupt service routine to actually get called and there's a lot of overhead with interrupts. There's a

**Dave Jones:** context switch and then you have to do things like checking what interrupt flag was set. It's actually quite slow, interrupts, and basically by the time the interrupt is serviced, you know, the flag is cleared and all that, the second sample in the sequence is completely ignored because by the time the second

**Dave Jones:** sample is complete, the interrupt flags have not been cleared so it cannot call the interrupt for the second item in the sequence. So, what happens is you completely lose all the data after the first sample in the sequence and there is a solution to this and it's quite convenient.

**Dave Jones:** In the CFGR1 register, you simply set wait to true. What this does is to ensure that the ADC does not continue with its sample sequence, you know, from channel 0, 1, 2, 3, 4, until the data is read from the ADC data register and this means that the CPU can be as

**Dave Jones:** slow as it wants and the interrupts can be called as slow as anything and it won't attempt to set the interrupt flags until the data is read so you won't miss samples of the ADC and this flag simply just fixes the problem. If you're having this issue, give it a go because it's easy to miss in the user

**Dave Jones:** guide and it isn't at all clear that this will fix the problem anyway so give that a go, it might fix it. What I would really recommend doing with these ADCs is ignoring the ADCs interrupts entirely. They're not, they're no good. What you should be using is the DMA and the DMA is quite easy.

**Dave Jones:** You can set it up in one shot mode which means it just goes do it once and then you can trigger the start of that with a function which is what I'm going to do and then eventually I'm going to have it triggered by a timer or you can have it

**Dave Jones:** running circularly which means it just keeps going. It kind of means that, not really. But either way, however you want to set it up, the DMA handles all these the sample latency issues for you. You don't have to wait. As soon as an ADC

**Dave Jones:** sample is done, it puts it into memory and it doesn't occupy the CPU time at all. So this was really useful when I have to sample six channels which I do have to sample, four or something, maybe it was six. And I want to

**Dave Jones:** minimize the latency between the samples so I don't want to be waiting between them and I also want to minimize the overhead on the CPU because it's not a fast CPU and whenever you can minimize latency you should minimize latency especially if it's not very much effort and in the case of these M0s the

**Dave Jones:** DMA is actually really not such a difficult peripheral to use and I will show you how that's used and this is what I think people should use exclusively for the ADC on these microcontrollers. Polling is fine but there's no reason to poll if

**Dave Jones:** you can use the DMA. It's extremely simple. So DMA on the STM32F072 has two options. It's got the module and channel. In the case of this microcontroller it's actually only got one DMA module. Some of them have two. I think the 92 series have two of them.

**Dave Jones:** So for this library I said I'll support both because maybe you guys, the community, can mod this to support more of the series but it's pretty much there now. So the DMA is really quite a simple peripheral on the STM32s. It's much simpler than most other microcontrollers I've used.

**Dave Jones:** It has the same pitfalls as every other peripheral on an ARM processor so don't assume it doesn't. You still have to power up the clock. If you go into my power class for the DMA, so this is the power kernel, you still have to power up the clock.

**Dave Jones:** You still have to enable the interrupt and set the interrupt's priority. I mean, that's just what you have to do with ARM processors. It's just the nature of the beast. But other than that, it's really quite neat. So first thing you do, first I'll explain what a DMA is.

**Dave Jones:** A DMA is a, I think it means direct memory access, but I'm going to Google it. Oh, it does stand for direct memory access. It's a peripheral provided in a lot of microcontrollers, not just these STM32s, that allows automated transfer of data from A to B.

**Dave Jones:** And in the case of this project here, I'm doing automated data transfer from the ADC data register into the DMA. ADC, let's call it the result buffer into memory. So that's from the peripheral into memory. And basically, it's that simple. That's what a DMA does.

**Dave Jones:** You start it, and it does a transaction of the number of items that you specify from memory location that you specify to memory location you specify. And this could be a peripheral, like a register, like the ADC sample register, or it could even be from memory to memory, you could be transferring from one data structure to another.

**Dave Jones:** And there's lots of reasons you would do this. And depending on the microcontroller, you might really need to do this. Like, I would want to do this with bootloaders. For example, if I was doing a bootloader, I would, I would DMA it from, because DMAs actually have very little source code, and you want bootloaders to be as small as possible.

**Dave Jones:** So to do that, you just have the, you don't even have to run the interrupts, you just start a DMA transaction that goes from flash memory or external memory and shoves it directly into your program memory or wherever you like. And it will finish it, it will just do it.

**Dave Jones:** And it will do it as fast as the microcontroller can possibly do. And they're, they're very reliable, and they take up no CPU time. So you can still have the CPU actually doing like things like rendering the user interface, which, you know, if the user interface froze every time you do ADC sequence of samples, especially slow ADCs, you know, that would be pretty grueling and agonizing.

**Dave Jones:** So let's go through what we've done to set up this DMA on the STM32. So, and this is my favorite peripheral on the STM32, by the way. So we've got the peripheral address, that's what PA stands for, it's in the CPAR register. The PA register, peripheral address, and I literally get the address of the peripheral.

**Dave Jones:** So this in this case is the ADC data register, the DR. So it's, it's literally a data registers address, that's a 16 bit, a 16 bit ADC value stored inside a 32 bit address. And in this case, I convert it to a uint32 just to avoid the compiler saying, give me a warning about converting a pointer to an integer implicitly.

**Dave Jones:** Because in this case, it's not an error, I'm doing that on purpose. So I do the cast. And it's really quite simple. So the peripheral address is the ADC module. The memory address is the place I want to put the data. The count is how many blocks of data I want to do, or in the case of the ADC, how many samples are in each sequence, which should match the amount of memory you've allocated to it.

**Dave Jones:** So if you have, if you have two samples in a sequence for the ADC, then you'll need at least two lots of 16 bits. So you'll need 32 bits, or, you know, eight bytes of buffer space. So yeah, that's just literally the count, the number of the number of samples.

**Dave Jones:** I'm not doing a memory to memory transfer. Although, that's something that this library, for some reason, just never supports. Maybe I should make it support it. Maybe. Anyway, and then, so up to this point, it doesn't actually, the DMA doesn't know how big each block of data is.

**Dave Jones:** So it doesn't know, it doesn't know how to pad the data. So the ADC modules register, the data register, actually 32 bits, but we only care about 16 bits of that. So why would we transfer 32 bits when we can transfer 16 bits?

**Dave Jones:** And this, this, this can kind of optimize memory in an application, I can stop using 32 bit buffers for each item. And I can have the DMA literally just grab only the 30, the lowest least significant 32 bits of the data register in the ADC, and put it straight into a uint32.

**Dave Jones:** In the, in the buffer. And all I have to do to make that happen is say, you're reading from something that's 16 bits, and it just does it. It's great. So the next thing, so what about, okay, so we've got, we've got the size of the items for the peripheral.

**Dave Jones:** What about, what about the destination, where it's going, the memory? Well, ideally, you'd want those two to match, but they don't have to. The, the memory block can be larger. So I can put a 16 bit from from the peripheral into 32 bits of buffer, if I wanted, it would pad it, it usually pads the most significant bits, but it's not at all a guarantee.

**Dave Jones:** In fact, there's a table of how it pads it. So if you get, if you're going to have dissimilar sizes, you'd have to look that up. But in my case, they do equal each other. So both of these, both of these are 16 bits.

**Dave Jones:** So it just tells the STM32, I'm you're transferring 16 bits from the peripheral to 16 bits in the buffer. But hang on, you can't just transfer to the buffer in the same spot over and over, right? It needs to auto increment. So that's what this is.

**Dave Jones:** Memory increment is what it stands for. And it basically means after one transfer occurs from the peripheral to the memory, the address of the destination increments automatically. So in the case of this, it would increment by 16 bits or two bytes. And it's ready to put the next sample in the sequence into the next block of memory.

**Dave Jones:** Quite useful, because this is something you would have to manually do, you'd have to manually manage a stack, you know, a thing that builds like that. And that can be a pain in the ass, but why not let the hardware do it? The hardware doesn't take up any program memory, the hardware is faster, the hardware is, well, it's thoroughly debugged by ST, I assume, and all of its users.

**Dave Jones:** So it doesn't really have many bugs. Yeah, it's great. So, okay, so I do a transaction, but how do I know when it's done? In an ADC, I want to do something with the data. Well, you generate an interrupt. So, in this case, I'm generating an interrupt on error, on complete, and it also gives you half complete interrupt.

**Dave Jones:** This is mainly for schedulers and stuff like that, you want to fill a scheduler when it's half done so it's never starving. So when it's complete, it will run one of these interrupts. If there's an error, it runs the error interrupt. That's pretty self-explanatory.

**Dave Jones:** When count number of transactions have occurred, it runs the interrupt on complete. And that's this interrupt down here. That's this function here. And it literally will just check the flags. This is not optimal code, by the way. If you want to complain, and you're wondering why I haven't used the global interrupts to check which one, it's because there's a better way to do it, and the comments tell me the way I'm going to add later when I can be bothered.

**Dave Jones:** Yeah. Anyway, so, after we set the interrupt flags, whether we want those interrupts or not, we then set it if it's circular or not. And that only means, when the transaction's done, should I reset all the settings? Well, with the ADC, I definitely want it to reset the settings because, one, I want to write to the buffer again.

**Dave Jones:** You know, I write to the buffer. So, you have to reset the settings. If I didn't, the DMA would stop working unless I completely reconfigured it every time I start a transaction, which is crazy. Why would I do that? Instead, you can just set the circular flag, and when it's done, it resets the count.

**Dave Jones:** That's this one here. And it's ready to go. Yeah, it's really cool. So, it's ready to start writing from the start of your buffer again. But it won't do it just straight away, especially in the case of the ADC. It doesn't just go nuts.

**Dave Jones:** You can make it do that. You can make it just go nuts, but it won't do that natively. Okay, so there's a few other things the DMA has. The direction of the DMA, you know, am I going from A to B or B to A?

**Dave Jones:** In this case, it's am I going from the memory to the peripheral or the peripheral to the memory? If you were going from the memory to the peripheral, which is the other way around, that could be for something like external memory writing or something like for a DAC.

**Dave Jones:** If you were generating a triangle wave on one of these microcontrollers, it's actually quite difficult to get a good sample rate with a DAC, even if you're doing a busy loop. The best way to do it is with the DMA. You create this lookup table,

**Dave Jones:** which represents whatever waveform you want, and then you have the DMA traverse it. And every time it's done outputting one value to the DAC, it's ready to move to the next one. Or you can even have it automatically triggered by timers if you want some specific sample interval,

**Dave Jones:** which you probably do for a waveform generator. And that would be 100%, or depending on if you're doing anything extra, almost 100% in the background, which means that your CPU is entirely free to do other things. And at the same time, it's able to output at its absolute maximum data rate.

**Dave Jones:** So DMA modules are one of the most important modules to learn of any microcontroller architecture. I'm passionate about that. There's another thing, basically all microcontrollers I've seen have this, and it's priority for DMA. I'm just thinking, nah, screw it, can't be bothered to give caveats.

**Dave Jones:** It's priority for the DMA. So DMAs operate kind of on this central node thing, it's like a matrix. There's usually these diagrams which show the buses which the DMA can grab from, and it's got these link huge points, which kind of says where it can get data from.

**Dave Jones:** But if you read it carefully, it also indicates that you can't have two DMAs on the same channel operate simultaneously. Just can't do it, because the lane in which data goes through the bus is occupied. So to deal with important transactions on a particular peripheral,

**Dave Jones:** for example, the DAC for a waveform generator, you would probably have a very high priority given to the DAC. So you might be updating a few things. You might be outputting information to an LCD screen. That's a memory to peripheral, where the peripheral is the spy bus, maybe.

**Dave Jones:** And you don't actually care that that data is perfectly synchronous. The increment between frames is perfect. You don't care, you just need it to be approximately the right frame rate, approximately consistent. In fact, you probably don't even care about the frame rate. You just want fast, like go, screen, be good.

**Dave Jones:** But you do care about the waveform. So you give the screen updating DMA transfer really low priority, zero. Maybe it's five. I can't remember. Whichever one means low priority. I think it's actually called low priority in this. Yeah, you give the screen low priority for the transaction and the DAC high priority.

**Dave Jones:** And that means that whenever the DAC needs the DMA module, the bus, it just gets it. And the other transaction has to wait. So it might cause the LCD output just to pause for a moment. But that's fine. Because it doesn't need to keep going.

**Dave Jones:** It doesn't need to be perfect, the screen output. But the DAC would need to be. That's why you have priority. And in the case of this, I default the priority to the lowest possible. I think that's the best way to do it. And then when you're done with all that, you just enable the module and you're ready to go.

**Dave Jones:** Now, interrupts in DMA, just before we finish the video. Interrupts are not necessary for DMA modules. In fact, you want to not use them if you can. Like with a screen updating routine. Who cares if the screen, if your goal is simply to copy memory from A to B.

**Dave Jones:** And you don't care when it completes. Why are you monitoring when it's complete? Or if your goal is to output a waveform, even that example, actually. Why do you care that each sample is complete? What you really care about is that it's doing its job.

**Dave Jones:** If you were to have a timer triggering an interrupt every time a sample is complete for the DMA, you would totally saturate CPU load. So you actually want it to be entirely in the background as much as possible. So you want to leave whatever interrupts you can off.

**Dave Jones:** So you probably want to leave interrupt on error on at all times. But interrupt on complete, not necessary. Not at all. In fact, these should be a different order. I should have error first, because that's more important than complete. You'll notice I have absolutely no interrupts for my ADC module.

**Dave Jones:** The way my program structure is set up is, if there was an interrupt, it would be right here. And it would be called static void interrupt. Anyway, there is no interrupt. Which means low CPU load. Yay! Okay, bye.
