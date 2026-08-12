---
video_id: s8b4h_UybLE
title: EEVblog #238 - Power Supply Design Part 7
url: https://www.youtube.com/watch?v=s8b4h_UybLE
source: youtube-asr
---

**Dave Jones:** Hi, it's the next installment in the power supply series. Last time we looked at the revision A schematic and I mentioned you know a few things on there I could possibly change and well I've done just that. So, let's take a look at

**Dave Jones:** rev B and see what the changes are. And here's the old rev A schematic you've seen before and tada here is rev B. One of the major changes is the formatting of the schematic. Really this is now an

**Dave Jones:** A3 format sheet cuz I really was trying to cram a lot of stuff onto this A4 sheet and I was just able to do it and I've added a couple of extra chips. So, it wasn't really possible to keep that

**Dave Jones:** you know single A4 sheet and I didn't want to split it up. So, I've put it onto an A3. I've made it a bit modular and there's a few changes, couple of extra chips and we'll go through them

**Dave Jones:** one by one, see what the changes are and why I did them. This modular aspect to the schematic just makes it a bit nicer because it's ADC separate over here, the micro current part, the USB interface, the the new I squared C

**Dave Jones:** IO section, the power supply integrated with the DAC here. I could have made the DAC as a separate module like I did the ABC but it's all sort of part of the same one and the Arduino compatible AVR

**Dave Jones:** microcontroller plus a few miscellaneous things here. I could tidy it up but now this is the Arduino controller from the previous rev A schematic and as it turns out I was trying to drive the LED on the reset line there and as it turns out

**Dave Jones:** that's not a good thing to do on these AVR microcontrollers because you have to burn the fuse which then means you can't do in system serial programming. So, uh I could use this as a LED output to drive there, I would only have a

**Dave Jones:** one-shot deal of program this micro, and that's no good at all. And you know, you don't know those things unless you read the uh the detailed parts of the data sheet. So, I had to free up that uh

**Dave Jones:** reset pin there. And uh and also I was sharing um part of the ISP interface down here with the uh SPI bus uh for my um ADC and DAC or the uh DAC actually. So, I decided to uh change that around

**Dave Jones:** free up I had to free up that reset pin. And uh that really started a whole cascade of changes cuz as you can see, every single pin was actually used on there. So, just that the act of freeing

**Dave Jones:** up that one pin meant it drove me into various design design decisions that um forced me into using uh external I squared C IO devices over here. And we'll take a look at those later, but um basically I didn't have enough free

**Dave Jones:** pins. But with those external uh chips dedicated to IO, I freed up a few pins, but um as you can see, I'm still using all of the pins. And as I mentioned previously, I wanted to use an external

**Dave Jones:** uh oscillator as well cuz the internal one uh wouldn't have been accurate enough for uh RS-232 uh serial comms, especially over temperature. So, I'm using an external resonator here. It's going to be 8 MHz. Um it's an ATmega168

**Dave Jones:** still or it could be a 328, whichever uh Arduino compatible one you desire. But basically, I have uh freed up the uh ISP interface here, which also goes off to a secondary connector, which we'll look at. I've added a um um, cap here to

**Dave Jones:** the reset pin, I've totally uh separated that out and I've decided to drive the uh RGB LEDs directly from uh pulse width modulation outputs. We'll probably take a look at that as well, but uh yeah, there are a few changes and there are a

**Dave Jones:** few things I had to keep on the microcontroller as opposed to dedicating them to these IO here. So, let's discuss that. And you'll notice I've also freed up the AREF pin as well and added some bypassing to ground just if you happen

**Dave Jones:** to use the internal referent reference, which we're not actually using it because we have external ADCs and DACs, but this project is designed to be uh expandable, so you can use it beyond its original scope. So, there's quite a lot

**Dave Jones:** of functionality in this circuit now. So, how do you decide what things to drive directly from the micro and what things you put on your external IO chips over here. And well, in this case, I've dedicated one IO chip to outputs. You

**Dave Jones:** can These are actually uh bidirectional. Uh we'll have a look at these uh in more detail later, but these are bidirectional IO I squared C interface. They're on the same I squared C bus, different programming address down here.

**Dave Jones:** I guess we're having a look at it now, aren't we? So, there you go. You can actually um have eight of these chips on the same bus by actually programming them with the three address pins there. So, I've dedicated one to uh input

**Dave Jones:** switches. So, I'm using four of still got four input switches like I used before, but I've got room for four more. So, if you're expanding this project um and you want to add like a a keypad matrix or something like that, you've

**Dave Jones:** got eight um key switch inputs or, you know, you can use them as outputs as well if you really want to. And but I've dedicated one chip to IO up here. And because actually this one down here that is

**Dave Jones:** inputs, um it's you know, it's fairly important to be able to interrupt from those. So, it it actually has an interrupt output pin here. So, I've taken that back to the micro. So, I obviously had to use one of the pins

**Dave Jones:** over here for the interrupt input, but because I dedicated this one over here to outputs, then I didn't need to hook up that interrupt output pin back to the micro there. So, in terms of these output pins here, which ones have I

**Dave Jones:** chosen to actually be on the I squared C chip instead of the microcontroller? Well, you have to remember that the I squared C chip, once you once you hook things on here, you lose some capability like pulse width modulation

**Dave Jones:** and things like that. You can still do it, but you got to do it via the I squared C bus. It doesn't have any internal hardware capability to do PWM or other fast stuff like that. So, really, you only want to put your non-critical

**Dave Jones:** output signals on here, and that's exactly what I've done. I've put the ADC chip select over here, the DAC chip select. I've put the range IO, which actually selects the microcurrent range up here. So, that's you know, that only switches once every

**Dave Jones:** blue moon. And lastly, I've got the LCD reset here. So, that's a non-critical signal as well. So, and I've got four spare. So, if you want to hook on any external circuitry, you can. You've got those four lines available. So, the ones

**Dave Jones:** I've actually put on the micro here, let's have a look at them. Now, of course, the fast stuff like the SPI interface, you want to put directly on your micro. Even though I'm not using the internal hardware SPI capability,

**Dave Jones:** which is actually multiplexed onto these ISP pins, which I wanted to free up. So, I'm not using the hardware SPI interface, I'm using just a regular IO. So, I'm just going to what's called bit bang the SPI interface, but that's

**Dave Jones:** no problems at all. But, you want it but because you want that to be reasonably fast, you're always sampling that ADC and DAC via the you know, you might sample it at 1 kHz or a couple hundred hertz or something. You're always doing

**Dave Jones:** it via that. So, if you put down the I2C interface, there's just overhead there you don't want. So, sure enough, I've got the SPI D in there, which is the data comes from the ADC, the ADC data out and sorry, the data in, which goes

**Dave Jones:** to both the DAC and the ADC, and then the data output from the ADC there, and the interrupt input coming from the I2C device, and there's the SPI clock as well. So, that's the SPI interface. That interrupt reset pin

**Dave Jones:** has nothing to do with it. So, it's only those three pins there, data and clock, and the chip select is a little bit slower. So, I decided to put those over to the I2C because some of the other pins I have to

**Dave Jones:** dedicate onto here like there's the I2C bus. I'm using the internal I2C in inside here, see? SDA and SCL there, SDA and SCL here. That means I'm using the internal hardware I2C interface, and you want to do that.

**Dave Jones:** I don't want to have to bit bang that one as well. I've got the reset pin totally separate, and I've also got the serial, the hardware UART output as well. And once again, you can tell it's a hardware

**Dave Jones:** device the pin label is RXD and TXD. There's a hardware UART inside there, so we're using that, and they go off to a generic IO connector or just a header connector we can use for serial expansion. And these are rotary

**Dave Jones:** encoders. Once again, I've got the four signals A and B phase coming from the two rotary encoders down here, and I could have put those on an I2C input, but I would have had to put it on uh

**Dave Jones:** this one here, which actually um had the interrupts um coming back cuz you want to be able to interrupt when you turn the actual knob. So, it was it just didn't work out just the way I configured these chips. So, it was

**Dave Jones:** better uh to put those directly onto the uh microcontroller pins here. And uh the good thing about the AVR or you know, a lot of good um modern microcontrollers will have this, but they will have um interrupt capability on all the pins.

**Dave Jones:** You can see it there, PC interrupt, you know, 18 and so forth. So, 19, 20, so almost virtually every pin has interrupt capability. So, we've got interrupt capability on those four uh rotary encoder inputs there. Now, before I had

**Dave Jones:** a just one LED for indication, but I decided, "Oh, what the hell? I'll gild the lily again, and I'll use the RGB uh backlight capability in my LCD displays." So, why not drive them with the pulse width modulator, and then you

**Dave Jones:** can vary the brightness of those uh three RGB LEDs. So, once again, you can't put PWM on the output of your I squared C. It's just not going to be pretty. It's not going to work. You're better off using the internal PWM

**Dave Jones:** capability of this device. And here's the three here, uh L, uh B, L, G, and L, R. So, they're the red, green, and blue, and they're connected through to the pins which have OC or an output compare module, OC uh B,

**Dave Jones:** and uh OC O A. So, you have to make sure you get these on the right pins, otherwise you won't be able to use the internal um PWM capability, which uses the output compare module. You have to go into and look at the AVR data sheet

**Dave Jones:** if you want to understand how all that sort of works, but PWM uses the output compare module. So, there's only a few pins available. I think there's only five or six total on this device. So, you have to connect those LEDs through

**Dave Jones:** to those pins with OC capability. And then the entire AVR ISP capability, including the select pin SS there, goes up to an expansion or I've got a couple of expansion connectors up here. So, that's my generic serial interface connector,

**Dave Jones:** which you can hook up to probably, you know, Ethernet, RS232, isolated RS232, USB, wireless, whatever you want to do, some sort of Zigbee module or something, you can hook it up and it's got full capability interface through to the SPI

**Dave Jones:** bus. And why not, while I'm at it, make that compatible with those FTDI Arduino serial programming board. So, not only can you program the Arduino not only program the micro through the regular ISP interface, but you can do it

**Dave Jones:** through the TX and RX pins, which use the internal bootloader in the AVR micro. So, these are the bottom five pins here, um 10 through to six there, are the same pinout as the FTDI, those generic FTDI boards you can

**Dave Jones:** buy for five or 10 bucks or something like that. So, there's a couple of ways that you can program this board. And as you can see, I've thrown on the other SPI pins up there, as well as the RS232

**Dave Jones:** hardware UART, the reset pin for good measure, just in case you need that for some reason. I needed to fill up an extra pin. Um I was going to put 5 volts on that connector, but on the layout of

**Dave Jones:** the board, it wasn't that great. I got It was like the last pin I wanted to connect and it was just I don't know. It It was just in the middle of nowhere and I couldn't get it through. Ah, it was a

**Dave Jones:** pain in the butt, so I decided, "Nah, bugger it. I'll put the reset pin anyway." And this extra IO one over here is for the key switches. My four switches are already hooked on to there, but uh you can hook on your own or you

**Dave Jones:** can use them for IO or anything you want. And that has um 3.3 volts and ground as well. So, um and this has 3.3 volts as well. So, you can power external boards straight from those IO connector. And why not? Just

**Dave Jones:** for good measure, I've added an I squared C bus expansion, just a four-pin uh SIL header there that uh has SDA and SCL and power and ground. So, if you want to hook on other I squared C devices, you can do that.

**Dave Jones:** And when it comes to choosing one of these I squared C serial expansion IOs, once again, I did the parametric search on Digikey, and pretty much for a DIP device I wanted, and Microchip came up again. It's the MCP uh 23008,

**Dave Jones:** and it's just an SPI interface. It's got programmable address lines and eight uh user-definable input and output you can software configure them to send data through when you set them up first, and then you can use them as IO, just like

**Dave Jones:** on a regular microcontroller. It's great. As I mentioned, it's got an interrupt uh output capability. You can actually uh reset the things if you need to, and power and ground, and that's it. And they're pretty cheap. They're only

**Dave Jones:** like a dollar 20 in one off or less than 80 cents um in volume. So, pretty much a uh no-brainer in terms of uh choosing these devices. As for the microcurrent circuit here, uh it's the same as before, I have changed the gain. It was

**Dave Jones:** 200 before. I've now upped it to uh 500 so that I can get one microamp bit uh resolution for a 12-bit uh converter. And that was just nicer than 2.5 microamps. I like that nice round number so that your uh ADC can read each bit

**Dave Jones:** equals one microamp. And on the output here, I've replaced the reverse uh Schottky diode with an SA12AG uh TVS, which is a um transient voltage suppressor, or a transorb, or whatever you want to call them. They go under various names. And

**Dave Jones:** uh this is a 12-V Zener. So, it will uh actually uh clamp any overvoltage um on the output, as well as offering uh reverse diode protection, as well. And because I'll get complaints of throwing in the option of the reverse protection

**Dave Jones:** diode between input and output on the voltage regulator there. If you want to use it, put it in. If not, leave it out. One of the key aspects with choosing an op-amp for this particular design is that it must have um capability to have

**Dave Jones:** the input pins go down and sense near zero. So, it's got to have an input common mode range that includes 0 V. So, that most uh single-supply uh op-amps will usually um have this sort of thing. And it also must be able to go down to

**Dave Jones:** uh 0 V or near ground on the output. Now, if it's a regular dual-supply op-amp, like the um NJM uh 14558 that I thought that from my rusty memory that it actually had that capability, it turns out that it doesn't. Because

**Dave Jones:** um the outputs from the uh DAC here, they can go between, you know, 0 and 2.048 V. And that goes directly into the input of the op-amp there. So, it must be capable the inputs must be capable of

**Dave Jones:** going down to ground. And likewise, the outputs, because our output voltage can go down to uh 0 uh V of our power supply, we need output to go down to zero, as well. So, we need a good single-supply op-amp. And here's the NJM

**Dave Jones:** 14558 uh device. And my rusty memory was no good at all. Uh while it had the uh input offset, I didn't uh bother to check um that it was actually a single supply uh capable and it turns out it's

**Dave Jones:** it's not. If we actually go down here and take a look at um this bit here, the input common mode voltage range, VICM, there it is there, then it's only plus minus three or typical plus minus four volts from a

**Dave Jones:** plus minus five volt supply up around here, up there. So, uh really, you're um it's it does not have that capability for the inputs to go down to the negative rail because it's plus minus five, it only goes down to uh say plus

**Dave Jones:** minus four typically. It only does a volt um above and below the rails. And if you're using it as a single supply op amp like we are in this um situation here, as you can see, we've got uh V+

**Dave Jones:** there and we've got ground. Um it's a single supply op amp, so it's not going to do uh what we want there. It's no good. So, uh we had to choose another op amp. So, I went through the parametric

**Dave Jones:** searches and all that sort of stuff and bingo, um I came up with the uh TLC uh 272, which uh should uh do the job for us. Let's take a look at this one. Now, if you look at the top level specs up

**Dave Jones:** here, it says 500 uh microvolts maximum there uh offset voltage at uh VDD five volts. Great. Uh it looks uh pretty stable. It's power supply capability very important uh three volts to 16 volts, so that's our maximum input. That

**Dave Jones:** covers our maximum and minimum input range, no problems at all. And bingo, single supply operation. When it says that, then you know um that you're in with a shot of this thing having um you know, the output is going to sense

**Dave Jones:** ground and it's going to uh go um to ground on the output as well. And it says, look at this, common mode input voltage range extends below the negative rail. So, your inputs can not only go to zero, they can go a little bit negative

**Dave Jones:** as well. And some op-amps have that capability. We don't really need it here, but if you need that kind of sort of capability, then this thing can do it. And this chip actually has uh four different grades available. And the

**Dave Jones:** different grades uh determine what the maximum output offset voltage is. So, it says here uh four output offset grades are available um from the C and I suffixes ranging from the low-cost uh TLC272 with no letters afterwards, which is 10 mV. Not suitable for us. We

**Dave Jones:** want better than 10 mV to the high-precision TLC277 which does 500 µV. Well, let's take a look at um the various other uh the various devices and see which one we need to choose. And by the way, here's that uh bell-shaped uh

**Dave Jones:** characteristic uh curve of the input offset voltage plus minus 400 µV there for the uh high-precision TLC277. So, that's what you can typically expect. Most are going to appear, in fact, in their batch testing there. Most appeared um in the center here, which is

**Dave Jones:** slightly offset from zero. It's offset by about 150 µV or 200 µV or thereabouts on the positive side. But that's the sort of spread that you can expect uh if if you're really going for some sort of really high-precision application, um

**Dave Jones:** that's where they can fall. Your chances of getting one right out here, right at the spec windows, is quite small. But odds are the bulk are going to sort of fall within that margin in there. And here you go. This is the table which uh

**Dave Jones:** shows the uh different offset voltages for the different part numbers from the very high-precision TLCs TLC277CP. So, it's not the 272, it's the 277. Um Um, and that's a µV up there. So, uh let's uh take a look

**Dave Jones:** and it's available in plastic dip as well. So, really, you know, ideally we'd want that 500 microvolts one, but the 277 is quite expensive compared to the 272. So, let's see if the uh 272 in the uh B grade there, you see how it's got

**Dave Jones:** the B after the letter. There's A, C, and B. They're kind of out of order. It's weird. You'd think that the A would be 10 millivolts, the B would be five, and the C might be two millivolts or the

**Dave Jones:** other way around, but no, they've sort of got them all muddled up. Uh who knows what they were thinking there when they actually did that. Um maybe it was an afterthought. They uh did A and B and then they decided, "Ah, we'll do a

**Dave Jones:** real cheap crappy C version as well." And just muddied the waters. Anyway, that's from a temperature range of zero to 70. We're not going to need that full range. So, let's go check out the uh temperature specs of this thing cuz this

**Dave Jones:** is going to be a maximum, see? VIO max. So, let's check out what a uh typical value is. And here's the internal circuitry. And you'll notice that, yes, it's actually CMOS. It uses uh MOSFETs instead of uh traditional bipolar uh

**Dave Jones:** transistors. And uh this is using the uh Lin CMOS process, which is a um silicon gate uh proprietary Texas Instruments one. But this is a CMOS device. And the advantage of uh using a CMOS device instead of a more traditional uh BJT uh

**Dave Jones:** type device is that um generally they're going to be uh much lower power. They're going to be single supply, you know, input rail-to-rail input to output, things like that. So, uh sort of CMOS devices are in general going to be a

**Dave Jones:** better choice for an application that we're doing here. There's something else interesting in the data sheet. You can see the uh layout of the die. You can see the uh output uh they'd be the output transistors there. I'm assuming

**Dave Jones:** they've even marked it on the uh silicon die. I'm assuming that's an accurate uh implementation of the die that they've actually using in this device. And with regards to the common mode input voltage here, you can see let's say at VDD 5

**Dave Jones:** volts, it can actually go negative to down to minus 0.2 volts and it'll go as high as 3.5 volts. So not quite rail-to-rail input. And here's our guaranteed and typical and maximum input offset voltages for the different grade

**Dave Jones:** devices A, B, and C grade devices. So let's take a look at say the B grade here, which is the best one out of the in the 272. You've got to go to a 277 to get better. And

**Dave Jones:** the typical is around about Look, it's very similar to the C to the 277 model. So the 272B is around 230 microvolts typical. So that's going to be typical at 25° C over the full range, you know, it's guaranteed to be less

**Dave Jones:** than 3,000 microvolts, 3 millivolts. So you know, it's Sometimes it's not good design practice to In general, you could say it's not good design practice to design around a typical figure. But in our case, because that is much lower

**Dave Jones:** than what we need, it's going to be good enough. Don't want to you know, spend the extra money for the TLC277. It's like two or three times the price or something. It's not like 10 or 20% extra. It's a significant price jump

**Dave Jones:** between that device and that device. So really, you know, and there's a big jump between the B version and the next best, which is the A version here, 230 microvolts typical offset at 25 to 0.9. So that's a big jump there. So you know,

**Dave Jones:** you probably could get away with the A version, but the B version is probably the go, I think. And as for power consumption of the device uh two amplifiers, a total of uh you know, at 25° 1.4 milliamps maximum for both

**Dave Jones:** amplifiers. It's not the lowest power device uh on the market, but it's good enough for our purposes. And if you look at uh VOL here, the low-level output voltage, um if if you drive the input at minus 100 millivolts, um the output will

**Dave Jones:** actually uh go down to zero typically. That's a typical figure or a maximum of 50 millivolts. Well, I think we're going to get, you know, it's going to be a lot better than 50, I think. But technically, if you're designing around

**Dave Jones:** maximum uh variation specs and it's critical, then you'd have to take that 50 millivolts into account. And in theory, it won't get down to uh 0 volts output, but you know, we don't care if our uh power supply can only get down to

**Dave Jones:** 50 millivolts output. Whoop-di-do. So, there you have it. That's uh rev B of the schematic and uh some thoughts into uh why I went into uh changing things and how you saw how just changing that one little uh reset, freeing up that one

**Dave Jones:** reset pin, you know, it changed drove all my extra design decisions. I went to external um forced me to use external I squared C devices. I could gild the lily with RGBs and add a few other things and

**Dave Jones:** add some more uh serial output capability and you know, and uh this is all part of uh system engineering. When you're doing this sort of thing, which I'll have to do some more uh system engineering stuff where in a future

**Dave Jones:** video in this power supply series when we start talking about the case and the PCB design and things like that. So, all that's uh coming up. Hopefully, I've got some PCB uh layout videos on how I laid out the board and I'll talk about system

**Dave Jones:** engineering with the case and how that drove some of the design factors and things like that. So, there's more to come. Um if you want the uh PDF of this uh schematic, just go to uh the blog website and it'll be there for download.

**Dave Jones:** So, I'll catch you next time. Hey.
