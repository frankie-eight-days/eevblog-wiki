---
video_id: fm13tIe5wSc
title: EEVacademy #4 -  I²C (I2C) Bit Banging
url: https://www.youtube.com/watch?v=fm13tIe5wSc
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 31, "3": 43, "4": 56, "5": 68, "6": 83, "7": 99, "8": 119, "9": 134, "10": 146, "11": 158, "12": 171, "13": 180, "14": 190, "15": 207, "16": 216, "17": 225, "18": 243, "19": 251, "20": 265, "21": 281, "22": 293, "23": 305, "24": 315, "25": 327, "26": 339, "27": 353, "28": 365, "29": 376, "30": 392, "31": 410, "32": 422, "33": 433, "34": 448, "35": 456, "36": 466, "37": 476, "38": 490, "39": 500, "40": 512, "41": 524, "42": 533, "43": 549, "44": 558, "45": 566, "46": 580, "47": 602, "48": 614, "49": 627}
---

**Dave Jones:** I2C and the very similar SMBus are in almost everything. You'll even find it as a major part of computer motherboards. The interface allows communication with up to 127 devices with only two wires.

**Dave Jones:** For many sensors, I2C is the standard way to get data. So, here we have two wires and you've got the S-clock and the S-data. That's SCL and SDA. The reason that the bus can communicate with 127 devices on only two wires is because those wires are open drain.

**Dave Jones:** Open drain means that the driving side only drives low. Each of the wires have to have a pull-up, which means that when the line isn't being driven low, it gets pulled high.

**Dave Jones:** Now, if you see a schematic one day and you see two resistors pulling up to the power rail, you'll know why that is. The value of these resistors can vary quite a lot and that depends on the speed grade of the interface.

**Dave Jones:** The smaller the resistance, the faster the response. I2C is a really slow interface and a comparable one would be dial-up internet. Dial-up internet was like 56 kilobits per second.

**Dave Jones:** I2C's lowest standard speed is 100 kilobits per second, so its standard speed is double the speed of dial-up internet. Now, a gigabit internet connection, for example, is over 10,000 times that speed.

**Dave Jones:** I2C until recently only had four speed grades, but in 2012 a fifth one was introduced. These speed grades might not be good enough for things like internet or displays, but they are ample for most sensors and data acquisition applications.

**Dave Jones:** The sample rate of common sensors, especially mechanical ones, is mostly quite slow. Strain gauges, which are on bridges, only require a few hertz for the sample rate. Even accelerometers rarely go above uh tens of kilohertz and the I2C bus in the megabit range easily accommodates the data requirements for those sensors.

**Dave Jones:** Now, if we have an accelerometer that samples at 32 kHz, which is unrealistic, we only need 256 kilobits per second for an 8-bit accelerometer. Every sample of an 8-bit accelerometer requires 8 bits of data to communicate.

**Dave Jones:** So, multiplying the speed the sample rate of the accelerometer with the bits, you get 256 kilobits per second. Let's assume that half our frame is our data and the other half is the address.

**Dave Jones:** And so, for this case, it would be 512 kilobits per second, which is far below the 1 megabit per second mode. Now, even with our unrealistic accelerometer, we're still okay with 1 megabit per second.

**Dave Jones:** So, every transaction begins with a start condition. The start condition is when the data line gets pulled low and then the clock line gets pulled low. After the start condition, data is sent.

**Dave Jones:** The data that is sent is usually in 8-bit blocks. Each of the 8 bits is sent with a rising and falling edge of the clock. This is called clocking out data.

**Dave Jones:** In the case that it's a read transaction, you would be clocking in data. The master still drives the clock, but it doesn't drive the data line. After the block is complete, there are two different things that can happen.

**Dave Jones:** If the slave device is okay with the data that was sent, then it will acknowledge the transaction and it will pull the line low. If it's not okay, it will allow the line to float high, which indicates that there's a problem with the transaction.

**Dave Jones:** The first block of data that is transmitted is the address of the slave. The address is between 0 and 127, and this is a 7-bit address. There are another type of address.

**Dave Jones:** This is 10-bit addresses, but we're not going to talk about them here. If a device exists on the I2C bus with the address that was sent, then an acknowledgment will be received.

**Dave Jones:** That's when the line is pulled low. If there isn't a device with the address that was sent, then the acknowledge line will stay high. Now, there are some devices that claim to have eight-bit addresses, but this is usually a device that says it has two different addresses, where the read address is this and the write address is that.

**Dave Jones:** Notice that the least significant bit is the only thing that changes in these addresses. This effectively means that even though they say it's an eight-bit address, it's actually a seven-bit address.

**Dave Jones:** You can take version of the eight-bit address and say it is the a seven-bit address. After the address is sent, depending on what the read and write bit was, data is either received or it is sent from the microcontroller.

**Dave Jones:** If the read-write bit was one, then the master is receiving data. If it was zero, then the master is sending data. When the master is receiving data, it just leaves the data line alone and allows the slave device to set the data bits.

**Dave Jones:** If the data block is not acknowledged by the slave, then it's probably the slave saying, "Stop reading. There's no more data." If the master is writing data and the slave didn't acknowledge, then there's a problem.

**Dave Jones:** If all went well, the master will probably then follow through with a stop condition. The stop condition is when the clock line is released or allowed to go high, and then the data line does the same.

**Dave Jones:** It is allowed to go high. Between blocks of data, for example, between the address and the data blocks, the clock line is held low, but the data line is allowed to go high.

**Dave Jones:** If you're a bit banging this, for example, this makes things quite simple because your function that writes data only needs to clock out eight bits of data, and before and after the transaction, have a start and stop condition.

**Dave Jones:** At the end of data sending, it's always required that the data line is released for acknowledgment, so the state between data blocks is always going to be okay. I've always found it very useful to learn how to bit bang an algorithm so that you fully understand it.

**Dave Jones:** So, we're going to do that right now. We're going to bit bang the algorithm. So, here we go. Okay, so we're just going to put it in C++. The code I'm working on here is based on the example for bit banging SPI.

**Dave Jones:** I use some structures which help in developing these bit banging libraries. I'm just going to work on the bit banging library now. This is a simple implementation and a lot of it is based on the previous SPI bit banging tutorial.

**Dave Jones:** So, the first thing I'm going to do is write this send function. The send function is a basic for loop which sends eight bits and this is going to be the fundamental thing that sends the address and the data and all that kind of thing.

**Dave Jones:** So, the send function is basically just a loop and it does a few different things and it accesses, you know, GPIO through um functions instead of actual pin set and clear calls.

**Dave Jones:** The reason that we're doing um functions instead of direct pin set and clears is because the functions kind of isolate the platform agnostic chism. Um so, that if I were to change platform from this Visual Studio environment to, for example, MSP430, I would only have to change the code inside those functions.

**Dave Jones:** So, I can have those functions in their own file and that file just includes everything that is platform dependent. So, I'm just modifying the SPI code just to um, you know, make the names and logging system make any sense.

**Dave Jones:** Um the way I actually do this is by having before and after any change of a pin, I basically just record the state of all the pins. And that's all I'm doing here.

**Dave Jones:** Um that allows me to plot the data and see kind of like the relative change between each of the pins assuming that there's no noticeable overhead from program execution.

**Dave Jones:** Okay, in the send function, we're just going to store a temporary. We're going to We're going to mask out that top bit and we're going to um store the temporary and probably like clock it out.

**Dave Jones:** Um clocking out is the rising and falling edge. So, let's write that. Okay, so, you know, a rising edge is setting it high, then a falling edge is setting it low again.

**Dave Jones:** Okay, so, we need a start and a stop function, and those just assert the start and the stop conditions we talked about before. Those are going to be used in the I2C write, and the first thing we're going to do in that function is assert the start condition.

**Dave Jones:** Then, we're going to send the address, of course, and you know, then the data, and then then we're going to assert the stop condition. In between each of the the blocks of data we send, we're going to look for an acknowledgement.

**Dave Jones:** So, we need a function that converts a 7-bit address to the 8-bit data address, and that function's going to take whether it's a read or a write address, and that read and write is the lowest bit of a byte.

**Dave Jones:** So, all we're going to do is mask the address to make sure it really is 7-bits, then we're going to shift it across so we have room for that read or write bit, and then we're going to or in that bit.

**Dave Jones:** We also need a function to get an acknowledgement, and an acknowledgement is basically um allowing the data line to go high, and then clocking and reading the data from the slave, and that's what we have here.

**Dave Jones:** Now, if we don't receive an acknowledgement, we do want to abort the write routine. So, let's check if we received an acknowledgement, and then um figure out what we're going to do with that.

**Dave Jones:** I think I'll probably just return true if it's successful and false if it's not. Okay, so, I got to make sure that I'm actually setting the output. That's the SDA, so let's call a function that gets that bit out temporary and sets the pin.

**Dave Jones:** Okay, so, we're going to write to device 0x10, and we're going to write the data 81 in hex. So, we should see that in the spreadsheet we're going to generate.

**Dave Jones:** I need to make sure that the default states of all the pins are correct. Um so, they've got to be all default high because by default, the bus is open.

**Dave Jones:** It's open drain. Just going to update the write routine so that it does indeed stop if it receives the acknowledgement, it sends the stop condition. and it should probably do that anyway, but it doesn't matter.

**Dave Jones:** Okay, so okay, now it's now it's fixed. So, what I'm doing here is just setting the default state of the pins in the variable so that it's also defaulted to zero on the actual variables.

**Dave Jones:** Um and then what I'm doing here is just copying the values from the terminal that it output to. The print the I2C print command did that. Okay, so I've got a scatter plot in LibreOffice Calc here, and let's just check it.

**Dave Jones:** Here's the start condition. And here we have the address. There are seven bits there. Um and here's the acknowledgement here, which we haven't received cuz we're not actually talking to a device.

**Dave Jones:** Um And the condition before the data byte is correct, so it seems like our formation of the frame is correct. Hope you learned a little bit about I2C. See you next time.
