---
video_id: s8b4h_UybLE
title: EEVblog #238 - Power Supply Design Part 7
url: https://www.youtube.com/watch?v=s8b4h_UybLE
source: youtube-asr
timestamps: {"0": 8, "1": 19, "2": 26, "3": 45, "4": 63, "5": 82, "6": 92, "7": 113, "8": 123, "9": 132, "10": 148, "11": 163, "12": 176, "13": 192, "14": 205, "15": 216, "16": 241, "17": 251, "18": 272, "19": 285, "20": 298, "21": 311, "22": 332, "23": 345, "24": 364, "25": 383, "26": 392, "27": 406, "28": 419, "29": 428, "30": 439, "31": 456, "32": 471, "33": 500, "34": 514, "35": 528, "36": 541, "37": 554, "38": 563, "39": 586, "40": 594, "41": 605, "42": 618, "43": 639, "44": 652, "45": 670, "46": 681, "47": 689, "48": 698, "49": 730, "50": 757, "51": 771, "52": 784, "53": 792, "54": 800, "55": 808, "56": 819, "57": 836, "58": 854, "59": 871, "60": 881, "61": 892, "62": 906, "63": 929, "64": 940, "65": 951, "66": 965, "67": 981, "68": 994, "69": 1006, "70": 1020, "71": 1042, "72": 1062, "73": 1075, "74": 1089, "75": 1098, "76": 1110, "77": 1120, "78": 1132, "79": 1146, "80": 1158, "81": 1169, "82": 1187, "83": 1201, "84": 1216, "85": 1229, "86": 1244, "87": 1261, "88": 1272, "89": 1285, "90": 1297, "91": 1309, "92": 1319, "93": 1334, "94": 1354, "95": 1368, "96": 1377, "97": 1399, "98": 1418, "99": 1434, "100": 1455, "101": 1466, "102": 1485, "103": 1502, "104": 1519, "105": 1524, "106": 1540, "107": 1557, "108": 1571, "109": 1583, "110": 1596, "111": 1618}
---

**Dave Jones:** Hi, it's the next installment in the power supply series. Last time we looked at the revision A schematic and I mentioned you know a few things on there I could possibly change and well I've done just that.

**Dave Jones:** So, let's take a look at rev B and see what the changes are. And here's the old rev A schematic you've seen before and tada here is rev B.

**Dave Jones:** One of the major changes is the formatting of the schematic. Really this is now an A3 format sheet cuz I really was trying to cram a lot of stuff onto this A4 sheet and I was just able to do it and I've added a couple of extra chips.

**Dave Jones:** So, it wasn't really possible to keep that you know single A4 sheet and I didn't want to split it up. So, I've put it onto an A3. I've made it a bit modular and there's a few changes, couple of extra chips and we'll go through them one by one, see what the changes are and why I did them.

**Dave Jones:** This modular aspect to the schematic just makes it a bit nicer because it's ADC separate over here, the micro current part, the USB interface, the the new I squared C IO section, the power supply integrated with the DAC here.

**Dave Jones:** I could have made the DAC as a separate module like I did the ABC but it's all sort of part of the same one and the Arduino compatible AVR microcontroller plus a few miscellaneous things here.

**Dave Jones:** I could tidy it up but now this is the Arduino controller from the previous rev A schematic and as it turns out I was trying to drive the LED on the reset line there and as it turns out that's not a good thing to do on these AVR microcontrollers because you have to burn the fuse which then means you can't do in system serial programming.

**Dave Jones:** So, uh I could use this as a LED output to drive there, I would only have a one-shot deal of program this micro, and that's no good at all.

**Dave Jones:** And you know, you don't know those things unless you read the uh the detailed parts of the data sheet. So, I had to free up that uh reset pin there.

**Dave Jones:** And uh and also I was sharing um part of the ISP interface down here with the uh SPI bus uh for my um ADC and DAC or the uh DAC actually.

**Dave Jones:** So, I decided to uh change that around free up I had to free up that reset pin. And uh that really started a whole cascade of changes cuz as you can see, every single pin was actually used on there.

**Dave Jones:** So, just that the act of freeing up that one pin meant it drove me into various design design decisions that um forced me into using uh external I squared C IO devices over here.

**Dave Jones:** And we'll take a look at those later, but um basically I didn't have enough free pins. But with those external uh chips dedicated to IO, I freed up a few pins, but um as you can see, I'm still using all of the pins.

**Dave Jones:** And as I mentioned previously, I wanted to use an external uh oscillator as well cuz the internal one uh wouldn't have been accurate enough for uh RS-232 uh serial comms, especially over temperature.

**Dave Jones:** So, I'm using an external resonator here. It's going to be 8 MHz. Um it's an ATmega168 still or it could be a 328, whichever uh Arduino compatible one you desire.

**Dave Jones:** But basically, I have uh freed up the uh ISP interface here, which also goes off to a secondary connector, which we'll look at. I've added a um um, cap here to the reset pin, I've totally uh separated that out and I've decided to drive the uh RGB LEDs directly from uh pulse width modulation outputs.

**Dave Jones:** We'll probably take a look at that as well, but uh yeah, there are a few changes and there are a few things I had to keep on the microcontroller as opposed to dedicating them to these IO here.

**Dave Jones:** So, let's discuss that. And you'll notice I've also freed up the AREF pin as well and added some bypassing to ground just if you happen to use the internal referent reference, which we're not actually using it because we have external ADCs and DACs, but this project is designed to be uh expandable, so you can use it beyond its original scope.

**Dave Jones:** So, there's quite a lot of functionality in this circuit now. So, how do you decide what things to drive directly from the micro and what things you put on your external IO chips over here.

**Dave Jones:** And well, in this case, I've dedicated one IO chip to outputs. You can These are actually uh bidirectional. Uh we'll have a look at these uh in more detail later, but these are bidirectional IO I squared C interface.

**Dave Jones:** They're on the same I squared C bus, different programming address down here. I guess we're having a look at it now, aren't we? So, there you go. You can actually um have eight of these chips on the same bus by actually programming them with the three address pins there.

**Dave Jones:** So, I've dedicated one to uh input switches. So, I'm using four of still got four input switches like I used before, but I've got room for four more. So, if you're expanding this project um and you want to add like a a keypad matrix or something like that, you've got eight um key switch inputs or, you know, you can use them as outputs as well if you

**Dave Jones:** really want to. And but I've dedicated one chip to IO up here. And because actually this one down here that is inputs, um it's you know, it's fairly important to be able to interrupt from those.

**Dave Jones:** So, it it actually has an interrupt output pin here. So, I've taken that back to the micro. So, I obviously had to use one of the pins over here for the interrupt input, but because I dedicated this one over here to outputs, then I didn't need to hook up that interrupt output pin back to the micro there.

**Dave Jones:** So, in terms of these output pins here, which ones have I chosen to actually be on the I squared C chip instead of the microcontroller? Well, you have to remember that the I squared C chip, once you once you hook things on here, you lose some capability like pulse width modulation and things like that.

**Dave Jones:** You can still do it, but you got to do it via the I squared C bus. It doesn't have any internal hardware capability to do PWM or other fast stuff like that.

**Dave Jones:** So, really, you only want to put your non-critical output signals on here, and that's exactly what I've done. I've put the ADC chip select over here, the DAC chip select.

**Dave Jones:** I've put the range IO, which actually selects the microcurrent range up here. So, that's you know, that only switches once every blue moon. And lastly, I've got the LCD reset here.

**Dave Jones:** So, that's a non-critical signal as well. So, and I've got four spare. So, if you want to hook on any external circuitry, you can. You've got those four lines available.

**Dave Jones:** So, the ones I've actually put on the micro here, let's have a look at them. Now, of course, the fast stuff like the SPI interface, you want to put directly on your micro.

**Dave Jones:** Even though I'm not using the internal hardware SPI capability, which is actually multiplexed onto these ISP pins, which I wanted to free up. So, I'm not using the hardware SPI interface, I'm using just a regular IO.

**Dave Jones:** So, I'm just going to what's called bit bang the SPI interface, but that's no problems at all. But, you want it but because you want that to be reasonably fast, you're always sampling that ADC and DAC via the you know, you might sample it at 1 kHz or a couple hundred hertz or something.

**Dave Jones:** You're always doing it via that. So, if you put down the I2C interface, there's just overhead there you don't want. So, sure enough, I've got the SPI D in there, which is the data comes from the ADC, the ADC data out and sorry, the data in, which goes to both the DAC and the ADC, and then the data output from the ADC there, and the interrupt input

**Dave Jones:** coming from the I2C device, and there's the SPI clock as well. So, that's the SPI interface. That interrupt reset pin has nothing to do with it. So, it's only those three pins there, data and clock, and the chip select is a little bit slower.

**Dave Jones:** So, I decided to put those over to the I2C because some of the other pins I have to dedicate onto here like there's the I2C bus. I'm using the internal I2C in inside here, see?

**Dave Jones:** SDA and SCL there, SDA and SCL here. That means I'm using the internal hardware I2C interface, and you want to do that. I don't want to have to bit bang that one as well.

**Dave Jones:** I've got the reset pin totally separate, and I've also got the serial, the hardware UART output as well. And once again, you can tell it's a hardware device the pin label is RXD and TXD.

**Dave Jones:** There's a hardware UART inside there, so we're using that, and they go off to a generic IO connector or just a header connector we can use for serial expansion.

**Dave Jones:** And these are rotary encoders. Once again, I've got the four signals A and B phase coming from the two rotary encoders down here, and I could have put those on an I2C input, but I would have had to put it on uh this one here, which actually um had the interrupts um coming back cuz you want to be able to interrupt when you turn the actual knob.

**Dave Jones:** So, it was it just didn't work out just the way I configured these chips. So, it was better uh to put those directly onto the uh microcontroller pins here.

**Dave Jones:** And uh the good thing about the AVR or you know, a lot of good um modern microcontrollers will have this, but they will have um interrupt capability on all the pins.

**Dave Jones:** You can see it there, PC interrupt, you know, 18 and so forth. So, 19, 20, so almost virtually every pin has interrupt capability. So, we've got interrupt capability on those four uh rotary encoder inputs there.

**Dave Jones:** Now, before I had a just one LED for indication, but I decided, "Oh, what the hell? I'll gild the lily again, and I'll use the RGB uh backlight capability in my LCD displays." So, why not drive them with the pulse width modulator, and then you can vary the brightness of those uh three RGB LEDs.

**Dave Jones:** So, once again, you can't put PWM on the output of your I squared C. It's just not going to be pretty. It's not going to work. You're better off using the internal PWM capability of this device.

**Dave Jones:** And here's the three here, uh L, uh B, L, G, and L, R. So, they're the red, green, and blue, and they're connected through to the pins which have OC or an output compare module, OC uh B, and uh OC O A.

**Dave Jones:** So, you have to make sure you get these on the right pins, otherwise you won't be able to use the internal um PWM capability, which uses the output compare module.

**Dave Jones:** You have to go into and look at the AVR data sheet if you want to understand how all that sort of works, but PWM uses the output compare module.

**Dave Jones:** So, there's only a few pins available. I think there's only five or six total on this device. So, you have to connect those LEDs through to those pins with OC capability.

**Dave Jones:** And then the entire AVR ISP capability, including the select pin SS there, goes up to an expansion or I've got a couple of expansion connectors up here. So, that's my generic serial interface connector, which you can hook up to probably, you know, Ethernet, RS232, isolated RS232, USB, wireless, whatever you want to do, some sort of Zigbee module or something, you can hook it up and it's got full

**Dave Jones:** capability interface through to the SPI bus. And why not, while I'm at it, make that compatible with those FTDI Arduino serial programming board. So, not only can you program the Arduino not only program the micro through the regular ISP interface, but you can do it through the TX and RX pins, which use the internal bootloader in the AVR micro.

**Dave Jones:** So, these are the bottom five pins here, um 10 through to six there, are the same pinout as the FTDI, those generic FTDI boards you can buy for five or 10 bucks or something like that.

**Dave Jones:** So, there's a couple of ways that you can program this board. And as you can see, I've thrown on the other SPI pins up there, as well as the RS232 hardware UART, the reset pin for good measure, just in case you need that for some reason.

**Dave Jones:** I needed to fill up an extra pin. Um I was going to put 5 volts on that connector, but on the layout of the board, it wasn't that great.

**Dave Jones:** I got It was like the last pin I wanted to connect and it was just I don't know. It It was just in the middle of nowhere and I couldn't get it through.

**Dave Jones:** Ah, it was a pain in the butt, so I decided, "Nah, bugger it. I'll put the reset pin anyway." And this extra IO one over here is for the key switches.

**Dave Jones:** My four switches are already hooked on to there, but uh you can hook on your own or you can use them for IO or anything you want. And that has um 3.3 volts and ground as well.

**Dave Jones:** So, um and this has 3.3 volts as well. So, you can power external boards straight from those IO connector. And why not? Just for good measure, I've added an I squared C bus expansion, just a four-pin uh SIL header there that uh has SDA and SCL and power and ground.

**Dave Jones:** So, if you want to hook on other I squared C devices, you can do that. And when it comes to choosing one of these I squared C serial expansion IOs, once again, I did the parametric search on Digikey, and pretty much for a DIP device I wanted, and Microchip came up again.

**Dave Jones:** It's the MCP uh 23008, and it's just an SPI interface. It's got programmable address lines and eight uh user-definable input and output you can software configure them to send data through when you set them up first, and then you can use them as IO, just like on a regular microcontroller.

**Dave Jones:** It's great. As I mentioned, it's got an interrupt uh output capability. You can actually uh reset the things if you need to, and power and ground, and that's it.

**Dave Jones:** And they're pretty cheap. They're only like a dollar 20 in one off or less than 80 cents um in volume. So, pretty much a uh no-brainer in terms of uh choosing these devices.

**Dave Jones:** As for the microcurrent circuit here, uh it's the same as before, I have changed the gain. It was 200 before. I've now upped it to uh 500 so that I can get one microamp bit uh resolution for a 12-bit uh converter.

**Dave Jones:** And that was just nicer than 2.5 microamps. I like that nice round number so that your uh ADC can read each bit equals one microamp. And on the output here, I've replaced the reverse uh Schottky diode with an SA12AG uh TVS, which is a um transient voltage suppressor, or a transorb, or whatever you want to call them.

**Dave Jones:** They go under various names. And uh this is a 12-V Zener. So, it will uh actually uh clamp any overvoltage um on the output, as well as offering uh reverse diode protection, as well.

**Dave Jones:** And because I'll get complaints of throwing in the option of the reverse protection diode between input and output on the voltage regulator there. If you want to use it, put it in.

**Dave Jones:** If not, leave it out. One of the key aspects with choosing an op-amp for this particular design is that it must have um capability to have the input pins go down and sense near zero.

**Dave Jones:** So, it's got to have an input common mode range that includes 0 V. So, that most uh single-supply uh op-amps will usually um have this sort of thing. And it also must be able to go down to uh 0 V or near ground on the output.

**Dave Jones:** Now, if it's a regular dual-supply op-amp, like the um NJM uh 14558 that I thought that from my rusty memory that it actually had that capability, it turns out that it doesn't.

**Dave Jones:** Because um the outputs from the uh DAC here, they can go between, you know, 0 and 2.048 V. And that goes directly into the input of the op-amp there.

**Dave Jones:** So, it must be capable the inputs must be capable of going down to ground. And likewise, the outputs, because our output voltage can go down to uh 0 uh V of our power supply, we need output to go down to zero, as well.

**Dave Jones:** So, we need a good single-supply op-amp. And here's the NJM 14558 uh device. And my rusty memory was no good at all. Uh while it had the uh input offset, I didn't uh bother to check um that it was actually a single supply uh capable and it turns out it's it's not.

**Dave Jones:** If we actually go down here and take a look at um this bit here, the input common mode voltage range, VICM, there it is there, then it's only plus minus three or typical plus minus four volts from a plus minus five volt supply up around here, up there.

**Dave Jones:** So, uh really, you're um it's it does not have that capability for the inputs to go down to the negative rail because it's plus minus five, it only goes down to uh say plus minus four typically.

**Dave Jones:** It only does a volt um above and below the rails. And if you're using it as a single supply op amp like we are in this um situation here, as you can see, we've got uh V+ there and we've got ground.

**Dave Jones:** Um it's a single supply op amp, so it's not going to do uh what we want there. It's no good. So, uh we had to choose another op amp.

**Dave Jones:** So, I went through the parametric searches and all that sort of stuff and bingo, um I came up with the uh TLC uh 272, which uh should uh do the job for us.

**Dave Jones:** Let's take a look at this one. Now, if you look at the top level specs up here, it says 500 uh microvolts maximum there uh offset voltage at uh VDD five volts.

**Dave Jones:** Great. Uh it looks uh pretty stable. It's power supply capability very important uh three volts to 16 volts, so that's our maximum input. That covers our maximum and minimum input range, no problems at all.

**Dave Jones:** And bingo, single supply operation. When it says that, then you know um that you're in with a shot of this thing having um you know, the output is going to sense ground and it's going to uh go um to ground on the output as well.

**Dave Jones:** And it says, look at this, common mode input voltage range extends below the negative rail. So, your inputs can not only go to zero, they can go a little bit negative as well.

**Dave Jones:** And some op-amps have that capability. We don't really need it here, but if you need that kind of sort of capability, then this thing can do it. And this chip actually has uh four different grades available.

**Dave Jones:** And the different grades uh determine what the maximum output offset voltage is. So, it says here uh four output offset grades are available um from the C and I suffixes ranging from the low-cost uh TLC272 with no letters afterwards, which is 10 mV.

**Dave Jones:** Not suitable for us. We want better than 10 mV to the high-precision TLC277 which does 500 µV. Well, let's take a look at um the various other uh the various devices and see which one we need to choose.

**Dave Jones:** And by the way, here's that uh bell-shaped uh characteristic uh curve of the input offset voltage plus minus 400 µV there for the uh high-precision TLC277. So, that's what you can typically expect.

**Dave Jones:** Most are going to appear, in fact, in their batch testing there. Most appeared um in the center here, which is slightly offset from zero. It's offset by about 150 µV or 200 µV or thereabouts on the positive side.

**Dave Jones:** But that's the sort of spread that you can expect uh if if you're really going for some sort of really high-precision application, um that's where they can fall. Your chances of getting one right out here, right at the spec windows, is quite small.

**Dave Jones:** But odds are the bulk are going to sort of fall within that margin in there. And here you go. This is the table which uh shows the uh different offset voltages for the different part numbers from the very high-precision TLCs TLC277CP.

**Dave Jones:** So, it's not the 272, it's the 277. Um Um, and that's a µV up there. So, uh let's uh take a look and it's available in plastic dip as well.

**Dave Jones:** So, really, you know, ideally we'd want that 500 microvolts one, but the 277 is quite expensive compared to the 272. So, let's see if the uh 272 in the uh B grade there, you see how it's got the B after the letter.

**Dave Jones:** There's A, C, and B. They're kind of out of order. It's weird. You'd think that the A would be 10 millivolts, the B would be five, and the C might be two millivolts or the other way around, but no, they've sort of got them all muddled up.

**Dave Jones:** Uh who knows what they were thinking there when they actually did that. Um maybe it was an afterthought. They uh did A and B and then they decided, "Ah, we'll do a real cheap crappy C version as well."

**Dave Jones:** And just muddied the waters. Anyway, that's from a temperature range of zero to 70. We're not going to need that full range. So, let's go check out the uh temperature specs of this thing cuz this is going to be a maximum, see?

**Dave Jones:** VIO max. So, let's check out what a uh typical value is. And here's the internal circuitry. And you'll notice that, yes, it's actually CMOS. It uses uh MOSFETs instead of uh traditional bipolar uh transistors.

**Dave Jones:** And uh this is using the uh Lin CMOS process, which is a um silicon gate uh proprietary Texas Instruments one. But this is a CMOS device. And the advantage of uh using a CMOS device instead of a more traditional uh BJT uh type device is that um generally they're going to be uh much lower power.

**Dave Jones:** They're going to be single supply, you know, input rail-to-rail input to output, things like that. So, uh sort of CMOS devices are in general going to be a better choice for an application that we're doing here.

**Dave Jones:** There's something else interesting in the data sheet. You can see the uh layout of the die. You can see the uh output uh they'd be the output transistors there.

**Dave Jones:** I'm assuming they've even marked it on the uh silicon die. I'm assuming that's an accurate uh implementation of the die that they've actually using in this device. And with regards to the common mode input voltage here, you can see let's say at VDD 5 volts, it can actually go negative to down to minus 0.2 volts and it'll go as high as 3.5 volts.

**Dave Jones:** So not quite rail-to-rail input. And here's our guaranteed and typical and maximum input offset voltages for the different grade devices A, B, and C grade devices. So let's take a look at say the B grade here, which is the best one out of the in the 272.

**Dave Jones:** You've got to go to a 277 to get better. And the typical is around about Look, it's very similar to the C to the 277 model. So the 272B is around 230 microvolts typical.

**Dave Jones:** So that's going to be typical at 25° C over the full range, you know, it's guaranteed to be less than 3,000 microvolts, 3 millivolts. So you know, it's Sometimes it's not good design practice to In general, you could say it's not good design practice to design around a typical figure.

**Dave Jones:** But in our case, because that is much lower than what we need, it's going to be good enough. Don't want to you know, spend the extra money for the TLC277.

**Dave Jones:** It's like two or three times the price or something. It's not like 10 or 20% extra. It's a significant price jump between that device and that device. So really, you know, and there's a big jump between the B version and the next best, which is the A version here, 230 microvolts typical offset at 25 to 0.9.

**Dave Jones:** So that's a big jump there. So you know, you probably could get away with the A version, but the B version is probably the go, I think. And as for power consumption of the device uh two amplifiers, a total of uh you know, at 25° 1.4 milliamps maximum for both amplifiers.

**Dave Jones:** It's not the lowest power device uh on the market, but it's good enough for our purposes. And if you look at uh VOL here, the low-level output voltage, um if if you drive the input at minus 100 millivolts, um the output will actually uh go down to zero typically.

**Dave Jones:** That's a typical figure or a maximum of 50 millivolts. Well, I think we're going to get, you know, it's going to be a lot better than 50, I think.

**Dave Jones:** But technically, if you're designing around maximum uh variation specs and it's critical, then you'd have to take that 50 millivolts into account. And in theory, it won't get down to uh 0 volts output, but you know, we don't care if our uh power supply can only get down to 50 millivolts output.

**Dave Jones:** Whoop-di-do. So, there you have it. That's uh rev B of the schematic and uh some thoughts into uh why I went into uh changing things and how you saw how just changing that one little uh reset, freeing up that one reset pin, you know, it changed drove all my extra design decisions.

**Dave Jones:** I went to external um forced me to use external I squared C devices. I could gild the lily with RGBs and add a few other things and add some more uh serial output capability and you know, and uh this is all part of uh system engineering.

**Dave Jones:** When you're doing this sort of thing, which I'll have to do some more uh system engineering stuff where in a future video in this power supply series when we start talking about the case and the PCB design and things like that.

**Dave Jones:** So, all that's uh coming up. Hopefully, I've got some PCB uh layout videos on how I laid out the board and I'll talk about system engineering with the case and how that drove some of the design factors and things like that.

**Dave Jones:** So, there's more to come. Um if you want the uh PDF of this uh schematic, just go to uh the blog website and it'll be there for download. So, I'll catch you next time.

**Dave Jones:** Hey.
