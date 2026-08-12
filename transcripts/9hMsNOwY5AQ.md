---
video_id: 9hMsNOwY5AQ
title: EEVacademy #3 - Bit Banging & SPI Tutorial
url: https://www.youtube.com/watch?v=9hMsNOwY5AQ
source: youtube-asr
timestamps: {"0": 0, "1": 9, "2": 18, "3": 34, "4": 52, "5": 67, "6": 84, "7": 100, "8": 121, "9": 131, "10": 140, "11": 151, "12": 167, "13": 177, "14": 188, "15": 196, "16": 220, "17": 239, "18": 250, "19": 264, "20": 275, "21": 284, "22": 297, "23": 310, "24": 325, "25": 342, "26": 356, "27": 366, "28": 377, "29": 394, "30": 404, "31": 416, "32": 429, "33": 441, "34": 455, "35": 468, "36": 484, "37": 496, "38": 512, "39": 531, "40": 539, "41": 556, "42": 571, "43": 585, "44": 596, "45": 611, "46": 623, "47": 638, "48": 658, "49": 670, "50": 688, "51": 700, "52": 712, "53": 722, "54": 740, "55": 747, "56": 762, "57": 768, "58": 778, "59": 799, "60": 809, "61": 818, "62": 830, "63": 840, "64": 852, "65": 865, "66": 878, "67": 888, "68": 896, "69": 906, "70": 917, "71": 933, "72": 946, "73": 956, "74": 963, "75": 971, "76": 985, "77": 995, "78": 1011, "79": 1033}
---

**Dave Jones:** Okay, today we're going to talk about bit banging. Bit banging is the process of using software to control hardware instead of using already existing hardware to output some kind of serial protocol.

**Dave Jones:** Bit banging is usually done in assembly or C or C++ and it's kind of a tortoise and the hare. It's really quite a slow process and it's not usually all that advisable.

**Dave Jones:** Um you often hear a lot of gray beards, you know, you haven't programmed embedded systems till you bit banged or whatever. Bit banging is actually really simple. All you need to know about bit banging is basically all you're doing is setting and clearing pins.

**Dave Jones:** Um so in this little waveform up here, this this waveform up here, um all we're going to be doing is, you know, we're going to set that point to one, set that point to zero, set that point to one, set that point to zero, set that to, you know, one, then we'll do it again to one, and then we're going to set it to zero, and then to one.

**Dave Jones:** Um this is all bit banging is. You're setting the um the pins. And because this is the earliest time, because you're actually plotting this way, um you would have set it in this order, this way.

**Dave Jones:** So to do this, you know, the lines of code would be really simple. All we would have done is we would have said, let's call the value up here V, and um let's just say the lines of code are V equals zero, cuz it transitions down.

**Dave Jones:** V equals one, cuz it transitions up. V equals one, because it stays up. V equals zero, because it transitions down. And then V equals one, cuz it transitions up.

**Dave Jones:** And then again V equals zero, because it transitions down. V equals one, because it transitions up. And then V equals one, because it stays up here. So usually it's more advisable to use the hardware in a microcontroller or some embedded system than to bit bang.

**Dave Jones:** Hardware handles all of the protocol semantics and you don't really have to worry too much about it being overhead on your processor because it all happens in the background.

**Dave Jones:** Um bit banging is for this reason inadvisable in many applications, but sometimes you just don't have enough serial ports or you don't have the type of serial port you want.

**Dave Jones:** So there is some things about bit banging that you need to know before we really go into how you do it. On a microcontroller, each pin has the ability to drive the output high, low, or be high impedance.

**Dave Jones:** Usually when the pin is an input, it is high impedance and this is a trait that you exploit in bit banging. Um this is a Microchip's uh PIC16F88 microcontroller um pin.

**Dave Jones:** And as you can see here, we've got some nifty stuff going on here. It's kind of cool. So we've got a P-FET here, an N-FET here, got some protection diodes here, and the output pin just here.

**Dave Jones:** Um So what they're doing is they have a push-pull driver that sets the value of the output pin. Um so if you say, you know, be one, this push-pull driver just sets the output to one.

**Dave Jones:** Um it just sets it to one. And that's what we're going to do in bit banging. Um if you set it to zero, it of course, you know, sets it to zero.

**Dave Jones:** But if you, for example, wanted to make it high impedance, you wanted to disconnect this output, this is a bit weird, isn't it? So what Microchip's doing is they're using an XOR gate and an AND gate to exploit a trait of these push-pull drivers that if they're opposite values, if they're not, you know, if they're not connected like this, then the outputs will be one of two things.

**Dave Jones:** They will be shorted, you know, power to ground, or both of them will be open circuit, which is exactly what we want to happen. Because if this wire here is effectively connected to well, nothing if this isn't connected and this isn't connected, um then we basically have it as high impedance.

**Dave Jones:** So, what they're doing here is using an XOR gate to XOR with the TRIS register. When the TRIS register on a PIC is set to one, they want the pin to be an input and when it's set to zero, they want it to be an output.

**Dave Jones:** So, they're using this XOR gate to make sure that when this is one, this value here is the opposite to this. And that means that these pins end up being um open like we wanted.

**Dave Jones:** It makes the tri-state pin here. Um and that way we get that trait. So, they're doing some niftyness here to make sure that the two power supply pins aren't shorted.

**Dave Jones:** They're using the AND gate and the XOR gate to make sure that you never have the condition where both the P-FET and the N-FET are on. So, why would you want to make the pin high impedance?

**Dave Jones:** One of the reasons is the I2C interface requires that the pins be open drain. Um each of the pins is pulled up with a resistor to the power supply and if we were just driving the pins, we wouldn't be meeting the protocol's spec.

**Dave Jones:** Um the only way we can do that is by having a open circuit here and allowing the resistor to pull the pin up to the power supply. So, bit banging in general is usually like a tight loop.

**Dave Jones:** The loop is usually a uh series of bit sets and bit clears where between each bit you have some kind of clock. So, a clock line usually is very periodic, something like this.

**Dave Jones:** And between each bit you set, you also have a clock signal so that the other device can clock in the data. Without the clock signal, um the slave device, that is the device that's not controlling the bus, will not receive any commands at all.

**Dave Jones:** So, most serial protocols have a master-slave relationship where the master controls whether the slave is listening or responding or and it sends all the commands. The slave usually won't engage um in conversation.

**Dave Jones:** It will only respond. Because there are very big differences in the way master and slave devices handle their protocol, it is really important to have separate implementations for their bit banging.

**Dave Jones:** And usually you wouldn't bit bang a slave. The reason is because if a slave device is bit banging, then it must always be polling the bus. Otherwise, it might miss communication.

**Dave Jones:** And if it's always polling the bus, the program can't do anything else. Um there's no other task that the program can do while it is polling the bus. So, when bit banging a slave device, they need to do a thing called polling.

**Dave Jones:** Polling is basically the process of checking the value of a pin over and over and over and over and over. And when it changes, you respond. Um when you're bit banging a slave, this can take a lot of time.

**Dave Jones:** And it usually takes too much CPU time to make it viable. So, why would you use bit banging? Why would you ever bit banging? It sounds like it's slow and just worse than using the existing hardware.

**Dave Jones:** Well, sometimes you simply can't use the existing hardware. Sometimes you just don't have enough serial ports. Sometimes you've got a few I2C devices um which is a serial protocol which have the same address and you need to communicate with them.

**Dave Jones:** You You need to connect multiple uh multiple different I2C lines to separate them. Um it's either that or a multiplexing solution. And sometimes you just don't want to pay for the extra chip.

**Dave Jones:** All right, it's time to learn about the serial peripheral interface or SPI. Um SPI is basically a four-wire interface, occasionally three, that has a clock line a chip select and two data lines.

**Dave Jones:** The data lines are basically data in and data out. SPI has a master-slave relationship. That means that all the communications are coordinated by the single device, the master. The slave doesn't ever initiate communication.

**Dave Jones:** Um the only thing the slave can do is respond synchronously with the clock through the MISO line, the master input slave output. The master sends data to the slave via the master output slave input.

**Dave Jones:** Occasionally, these are named differently, um but I believe this way is the best. The uh RX TX way of labeling is confusing and caused pretty big problems with uh UART and other serial protocols.

**Dave Jones:** So, as I said before, there's four different wires, and um these four different wires are as follows here. And then, these wires only go in the single direction. The chip select, clock, and MOSI uh only driven by the master.

**Dave Jones:** The only line that the slave does drive is the MISO. So, a typical SPI frame has a signal that looks like this. You have a clock line that goes up and down like this, and then you have a uh select line, which is active low, and you have these data lines.

**Dave Jones:** The data lines are synchronized with the clock, and they could be synchronized with the rising edge or a falling edge. So, SPI isn't as basic as the previous picture made it seem.

**Dave Jones:** It actually has a thing called polarity, which complicates this interface, which basically indicates the idle state, that's this line here, that the clock line returns to. That is the the logic level that the clock line is on when it's not communicating with any devices.

**Dave Jones:** So, in this case, polarity is zero, and it is logic low before and after SPI frames. In the case where it's polarity one, the idle state is high, as you can see on this line.

**Dave Jones:** Um they are basically just upside down. You can think of the polarity being one being the clock-line inversion. So, the first edge of polarity zero is actually a rising edge, and the first edge of polarity one is a falling edge.

**Dave Jones:** This means that when you implement a protocol for this in bit-banging, or maybe you just want to look at your oscilloscope and try reverse-engineer what you're receiving, you need to know, you know, am I reading on a rising or a falling edge?

**Dave Jones:** Um in this case, we have the middle of the byte, that's kind of when you want to read, um or clock in data, is right in the middle. So, we're reading on that rising and that falling edge.

**Dave Jones:** Strictly speaking, that isn't the end of the complexity of SPI. So, as well as the polarity, the up-so-downness of the clock line, you also have the phase. And that basically is when are we clocking in and clocking out data.

**Dave Jones:** So, a phase of one is basically shifting the data by half the period of the clock. See, the distance between these red lines is the period of the clock, and notice when phase is one, we've shifted the data across by half.

**Dave Jones:** In this case, the data is clocked out on this first red line, and then it is read on this blue line here. That is when phase is one. When phase is zero, it's initially the data, and then it reads on this first line here, clocks out on the blue line, reads on the red line, and you get the opposite for phase one.

**Dave Jones:** This can be a bit confusing in code, because it does make your code look a little higgledy-piggledy. is much more complicated to implement than the polarity. Usually in bit-banging libraries, you have a very simple implementation.

**Dave Jones:** You don't need to usually implement all the different variations in polarity and phase. That's is because you usually have a very specific application in mind, and it's unlikely, and I've never seen it before, that a chip implements simultaneously, for example, polarity zero and one.

**Dave Jones:** Chips do often have support for two different SPI modes, though, but it's not 0 and 1. It's often pairs um two after each other. So, for example, they have support for everything with polarity zero or with polarity one.

**Dave Jones:** This is why in data sheets like this one you often see this type of list. You see a polarity is zero and zero or polarity is one and one.

**Dave Jones:** A common way you see the SPI bus connected is as this diagram shows here. You have all the different devices connected to the same bus and selected with separate chip select lines.

**Dave Jones:** When the device isn't selected, these pins here go high impedance and it is as if the master is communicating directly to the slave it chooses to. Okay, so to demonstrate bit banging, I've got a small library in C++ that basically emulates um a bit banged SPI port.

**Dave Jones:** And we're going to use this library to test whether we've implemented the bit banging correctly. So, we're just going to run it now and it's spit out some data.

**Dave Jones:** We're transmitting the number 12 on the four different SPI modes. So, let's just copy all of that and put it into a spreadsheet. So, we've pasted the data into a spreadsheet and this can be useful if you're you've only got an oscilloscope, not a logic analyzer.

**Dave Jones:** You can compare what the wave looks like on the oscilloscope to what we have in a plot like this. So, in this case we do in fact have 12.

**Dave Jones:** So, as you can see on this this edge here, the uh the rising edge, we have one and on this edge here we have another one followed by two zeros.

**Dave Jones:** And that is how the number 12 looks in binary. So, this is um what we expect and as you can see the polarity is different like we expect where the default value, the idle value, is high when polarity is one and it is low when polarity is low.

**Dave Jones:** The phase is doing the same thing where the the waveform appears to be shifted by half the period. So, what does a write routine look for a bit banged spy port?

**Dave Jones:** So, we've got to be talking with all the four pins to implement this and we have to transmit and receive eight bits. So, that means we need to have a loop that goes around eight times.

**Dave Jones:** But before and after that loop, we need to select and deselect the line. So, that means to put it to logic low and then after the frame, bring it back to logic high.

**Dave Jones:** These two lines here and here handle all the chip select nonsense. And in the middle, we can focus on the bits. So, the first thing we do is set the data pin the MOSI's value.

**Dave Jones:** If the the most significant bit of the input is one, then we want to set the pin to be one. Following that, we do the first rising clock edge and then we input some data from the buffer.

**Dave Jones:** This is um a standard order to do this. And then we want to lower the clock edge again ready for the next loop around. Before we go around again though, we need to make sure that our next bit that we send isn't the same bit.

**Dave Jones:** We need to move the second most significant bit to the position of the most significant bit. And we do this with this shift operation. So, after then we go round to the top again and then we're sending the second most significant bit.

**Dave Jones:** And then it'll go round and round and round till we're at the the eighth bit in the byte and then it will follow through here, return it to the the idle state and deselect the line.

**Dave Jones:** Okay, so here we are loading up Code Composer and um we're just going to show I'm just going to show that the code is exactly the same between platforms.

**Dave Jones:** This is why the Visual Studio Excel testing thing is kind of okay. So, I'm just going to copy my Git for the Visual Studio code. Literally just copying it.

**Dave Jones:** Here we go. And now we're just going to go to the I2C thing in this library here. I'm just going to paste over the top. Um There we go.

**Dave Jones:** So, now it's identical and we're going notice run it straight away. No changes. And yes, it builds and it's loading onto the platform now. I'll um And uh before I start simulation, this is our setup.

**Dave Jones:** This is the Tiva uh C setup. It's a TM4 microcontroller. It's like from 2014, Texas Instruments device. Um and we've got a Saleae Logic Analyzer um bringing feed back into the computer.

**Dave Jones:** We can read back the SPI frame in um the Saleae Logic um on the PC. So, we can confirm that our protocol is correct. Okay, we're just going to run it now.

**Dave Jones:** And the application is configured to only transmit when I'm pressing the button. So, I'm just going to open up Saleae Logic. Okay, so we've set up the logic analyzer now.

**Dave Jones:** We're just going to start simulation. Okay, we've clearly collected too much data, but here we have the SPI frame. So, we've got a few things um transmitting at once here.

**Dave Jones:** So, let's see if we can figure out what's happening. So, what we have here is um the SPI frame, a single SPI frame with a uh clock line here and the chip select here and the data here.

**Dave Jones:** So, what are we transmitting? What number? So, in this case, we're writing a count. So, the port zero is sending the even numbers and port one will be sending odd numbers.

**Dave Jones:** So, here we have the port zero up the top sending 42 and then we have port one sending 53, 45, 47, all the odd numbers and each of them going up by two and the port zero is doing the same, 42, 44, 46, 48.

**Dave Jones:** So, we can confirm that it is receiving the frames correctly and Saleae Logic um the Saleae Logic Analyzer is correctly interpreting our frames. So, I hope you found that useful and I hope that you learned a little bit more about the SPI protocol, bit banging, and how you can use, you know, simulations on the PC to help out in your debugging.

**Dave Jones:** Bye. Mhm.
