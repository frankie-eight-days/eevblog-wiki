---
video_id: UKIzhz0XLaQ
title: EEVblog #912 - BM235 Multimeter Reverse Engineering
url: https://www.youtube.com/watch?v=UKIzhz0XLaQ
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 24, "2": 40, "3": 59, "4": 77, "5": 97, "6": 111, "7": 133, "8": 152, "9": 171, "10": 187, "11": 205, "12": 223, "13": 253, "14": 273, "15": 295, "16": 319, "17": 341, "18": 363, "19": 384, "20": 405, "21": 422, "22": 448, "23": 469, "24": 489, "25": 510, "26": 527, "27": 547, "28": 567, "29": 584, "30": 601, "31": 619, "32": 640, "33": 658, "34": 677, "35": 692, "36": 715, "37": 733, "38": 750, "39": 769, "40": 788, "41": 806, "42": 830, "43": 847, "44": 864, "45": 883, "46": 903, "47": 919, "48": 934, "49": 947, "50": 965, "51": 986, "52": 1005, "53": 1021, "54": 1037, "55": 1055, "56": 1074, "57": 1091, "58": 1110, "59": 1126, "60": 1140, "61": 1161, "62": 1186, "63": 1204, "64": 1224, "65": 1251, "66": 1266, "67": 1282, "68": 1297, "69": 1317, "70": 1334, "71": 1351, "72": 1372, "73": 1393, "74": 1412, "75": 1430, "76": 1447, "77": 1461, "78": 1481, "79": 1497, "80": 1516, "81": 1531, "82": 1550, "83": 1569, "84": 1587, "85": 1602, "86": 1616, "87": 1631, "88": 1647, "89": 1663, "90": 1688, "91": 1705, "92": 1729, "93": 1748, "94": 1765, "95": 1783, "96": 1799, "97": 1822, "98": 1833, "99": 1858, "100": 1875, "101": 1900, "102": 1919, "103": 1940, "104": 1962, "105": 1978, "106": 1995, "107": 2017, "108": 2036, "109": 2056, "110": 2074, "111": 2099, "112": 2118, "113": 2137, "114": 2153, "115": 2171, "116": 2187, "117": 2204, "118": 2227, "119": 2249, "120": 2270, "121": 2288, "122": 2305, "123": 2323, "124": 2343, "125": 2365, "126": 2383, "127": 2402, "128": 2424, "129": 2445, "130": 2472}
---

**Dave Jones:** Hi, I've done several videos on my EEVblog BM-235 multimeter. I've done repairs and I've done troubleshooting and teardowns and all sorts of calibration, all sorts of weird and wonderful things, but one thing I haven't done, and I've mentioned it before, is what chipset, what multimeter chipset is used inside the EEVblog slash Brymon BM-235,

**Dave Jones:** because Brymon are the company that designed and manufactured this thing. And I don't know. They won't actually tell me. And I'm not sure why. It's, you know, they just don't want it released to the public, even if it is me, I guess. They just don't want word to get out.

**Dave Jones:** But anyway, it's usually not hard to just look at it and reverse engineer a board. Not completely reverse engineer it, but just do a few basic things to try and figure out what chipset is being used or what chip is being used in any particular design.

**Dave Jones:** It doesn't have to be the EEVblog multimeter here, but I thought that would take a look at it and see if we can actually figure it out. Now, I don't think it's a custom ASIC, because Brymon, they're just not, I don't think they're big enough and bold enough to do their own custom ASIC.

**Dave Jones:** So I'm pretty sure it's going to be an off-the-shelf multimeter chipset. Now, the new BM230 series differs from the venerable BM250 series, the 257, which a lot of people are familiar with. And here's a photo of the underside of the BM257. Oops, sorry, I'll just get rid of me.

**Dave Jones:** And here's a photo of the bottom side, and it uses a substantially different chipset. And you can see it's labeled BTC, or Brymon Technology Corporation. And it's just got some weird custom part number like that. So obviously that's in a much bigger quad flat pack.

**Dave Jones:** It's got the LCD driver built in. You can see the traces going off to the contacts here, which then go through the zebra strips there over to the LCD. So that's all contained in one chipset. So that's one of those very typical complete multimeter chipsets.

**Dave Jones:** It's got the processor in there, it's got the ADC, all the measurements, switching and arranging and all that sort of stuff, plus the LCD driver built in. But the BM235 is significantly different. So let's actually go in and have a closer look here at the board.

**Dave Jones:** And you'll notice that it is branded BTC again, Brymon Technology Corporation. It's got some weird part number there. So they've got this obviously custom silk screen. And this is not hard. You can get this from virtually any chip manufacturer. Just go to them and say, hey, I want, you know, I want to buy 10,000 of these chips.

**Dave Jones:** Can you also custom silk screen brand them for me or laser brand them for me? And they go, no worries, we'll do that. Put your own custom part number on. But it's an off-the-shelf chip. So just because it might have Brymon on it does not mean it's an ASIC.

**Dave Jones:** In fact, in this case, I'm pretty darn sure it's not an ASIC. Because there's only a few companies out there that specialize in multimeter chipsets. And it makes sense just to use one of those off-the-shelf chipsets. So anyway, they've gone for the BM230 series is a lower cost than the 250 series.

**Dave Jones:** Even though it uses two separate chips, they've obviously lowered the cost. And you'll notice that down here, bingo, we've looked at this before, the HYR2613. In fact, if we have a look here, I actually have a video on my second channel, EEVblog2. If you're not subscribed to EEVblog2, you should be.

**Dave Jones:** It's where I put various stuff comparing the BM257 to the 235 here. And I had a look at whether or not you could hack the 235 for serial output. And I won't spoil it, you'll have to go watch it yourself. Anyway, because the main difference between the BM257 and the 235 is that the 257A has a bar graph and B has serial output capability.

**Dave Jones:** You can get like an RS232 infrared serial. So I wanted to see if that was possible, because the cases are identical between them, including the window for the IR module. Anyway, I am actually spoiling that video. So the first thing we're going to do is go check out some typical multimeter chipset manufacturers.

**Dave Jones:** And I know three offhand, I'm sure there's more, but like off the top of my head, I can't think of them anyway. Three of the major ones, one is Fortune Semiconductor, icfortune.com. And if you go in here under measurement, here we go, they've got healthcare, but yep, and all sorts of like custom analog-y type chips.

**Dave Jones:** There's companies that specialize in these things and make an absolute killing from them. Here we go, the FS9700 series, 9800 series, and they're using tons of multimeters, including the low-end Chinese-made flukes and things like that. So they not only do like complete multimeter chipsets like this, but they also do, for example, ADCs.

**Dave Jones:** Now these aren't just ADCs, they're actually specifically designed. Take this one down the bottom, the FS970X, for example, specifically designed for multimeters, but it's just the front-end delta-sigma ADC plus the range-switching and, you know, all that multimeter. It doesn't include the processor and doesn't include the LCD driver.

**Dave Jones:** So they're typically like a serial output type thing, you know, and you can go in and have a look at the data sheets of chips like this. And they are significantly different. But in this case, we're looking for a complete multimeter chipset. This one in, I've had a look at this one before for a design I'm working on for 5,000, 50,000 count analog front-end,

**Dave Jones:** and that's pretty much all it does. Here we go, whoop, it's a, there we go, typical application circuit. You've got the front-end, but then you've got, but then you need the processor and LCD driver over here. So a completely different type of chip to the multimeter chipsets.

**Dave Jones:** Anyway, there's Fortune Semiconductor and then there's Cirrus Tech. They're very popular in a lot of the Chinese meters, and they've got basic 2,000 count ones, 3,000, 4,000, 5,000, 6,000. Now, if we were looking for a chipset for the BM235, it's a 6,000 count multimeter.

**Dave Jones:** So it could certainly be one of those, and there's many, many to choose from. Check it out, once again, these analog, there's the smart DMM ones, which are the complete processor, and then there's just the front-end ICs and things like that. So it could certainly be a Cirrus Tech.

**Dave Jones:** And then the third major one is Hikon. And Hikon manufacture, you can see down the side here, they've got mixed signal stuff, battery management ICs, data converters, mixed signal controllers, and digital multimeter ICs. And they've basically got two chipsets here. The 3131 series I've also looked at for a multimeter type design before,

**Dave Jones:** but that's like a high-end, like 50,000 count design. But if we go over to here, the HY12P series, is we want to have a look at through the different versions here, because if we go over to the, back to the photo here, let's have a look at the pin count.

**Dave Jones:** Bingo, it's a 64-pin quad flat pack. So you can eliminate anything that is not in a 64-pin package. What have we got here? Bingo, LQFP64. So you can actually rule out a bunch of these, but you'd have to go in individually to see what size packages they're available in.

**Dave Jones:** Sure, the manufacturer can put them in different packages for you and things like that. They might even be able to do small custom variants, but yeah, I don't know. It could be a custom variant. It could come down to that. Anyway, the HigonTech ones, certainly, we're looking at, here we go, but they've got built-in LCD drivers.

**Dave Jones:** Now, we'll come back to this, but if we actually have a look at the table here, these two down here are 5,000 count ones, here and here. Now, of course, the BM235 is 6,000 count, but hey, I've seen chipsets being extended beyond their counts before,

**Dave Jones:** so I'm not necessarily going to rule it out because it is the 64-pin quad flat pack. And the other reason that I suspect it actually may be a HigonTech part is because if you have a look down here, bingo, our LCD driver is a HigonTech HY2613C.

**Dave Jones:** So bingo, we've got ourselves a HigonTech LCD driver, and that is the specific one that's actually being used in here. We're not using that package, we're actually using this package here. So the reason I suspect it's HigonTech is because it's very common to use the same brand chip like this

**Dave Jones:** because, hey, you can get better pricing. You say, hey, I'm going to use your LCD chipset as well as use your multimeter chipset. You know, hey, give us a few cents off or something like that, and that can make a huge difference to the bottom cost and then to your final retail price for this thing.

**Dave Jones:** And they were trying to get the price down on the BM230 series compared to the 257, so they've probably got a good deal. So I, you know, that's good circumstantial evidence that it could be a HigonTech part, and so that is where I would look first.

**Dave Jones:** So if we go down here and have a look at these ones, at the 5,000 count parts here, look, the peak hold, now the peak hold functionality, there's one that has peak hold, one that doesn't. Now the 257 had the peak hold, the 230 series, the 235 does not.

**Dave Jones:** So, and it does not have inrush current capability. And it does not have the serial port UART, but let's not get into that. So it's, you know, I'm going to have a look at the HY12P66. That one, yeah, smells like it might be doing the business.

**Dave Jones:** But the thing is, look, it's got an LCD driver built in, as I said, a 4x15 segment. So that is actually just capable of doing the LCD here. It does have a couple more segments, actually up in here they were going to have a variation of this meter with,

**Dave Jones:** for audio, sorry, for automotive stuff as well. So the LCD does actually have a couple of other segments in here. But in theory, I believe that that chipset could actually do it. So why are they using, if it is this one, why are they using separate LCD chip?

**Dave Jones:** I don't know, there could be some other technical reason. Anyway, I don't know it's this one. So if we go down and have a look, oh, beautiful, look, beautiful lookup tables there. The register mapping tables for the individual bits to show you the flow and things like that.

**Dave Jones:** That's just excellent, absolutely brilliant data sheets. The HiCon tech ones, if you want to follow through and see how multimeters actually, multimeter chipsets actually work, highly recommended. Well, looky what we have here. We've got ourselves the pinout. Bingo, we can actually go and compare this with our PCB.

**Dave Jones:** And off the top of my head, I'm telling you, this is looking pretty good. So if we have a squiz here at the chip, look at this. I've got them pin aligned, so pin one down here and pin one down here. Check out all these unused pins all the way along here and up there.

**Dave Jones:** Sure, they could be going to something under there. You can't see underneath. They could be going through some vias down to the other side of the board. But hey, that's pretty good circumstantial evidence that this chipset that they're using, with a lot of unused pins, has a built-in LCD driver.

**Dave Jones:** Otherwise, if you were doing this as a custom ASIC, you wouldn't be wasting all these pins. You'd be going for a smaller package. Sure, you could have like a dual-use scenario in mind or something like that. But anyway, look, map the pins. From pin one through to pin 12 over there are the segments.

**Dave Jones:** So only the last four are something else. So I can actually go in and expand that. There you go, to show you what ones those are. And you can see the last four pins, it matches up. The rest are segments. So because we don't have, we're using a separate LCD driver in this multimeter,

**Dave Jones:** bingo, we don't use the internal segments. So that matches up perfectly. So right there you go, aha. So unless the manufacturers are like ripping off the pinouts between chipsets, which I don't think they do, I think they're pretty substantially different, then hey, this is looking really good.

**Dave Jones:** Anyway, so these segments over here aren't used. So 1, 2, 3, 4, 5 pins unused. 1, 2, 3, 4, 5 pins unused. But aha, look, COM1 and COM0 are actually connected. That's interesting. If it is this chip, COM0 and COM1 are connected. Hmm, interesting.

**Dave Jones:** Anyway, let's go up here. It looks like the pin 49 up here is a power. Ooh, ACM. What's that? We'll have to have a look at that. And analog ground, look, 48 up here. 48 over here is, looks, you know, it's got a nice fat trace going to it,

**Dave Jones:** so that's likely analog ground. There's a couple of unused pins over here. Don't know what they are. Or they could be going under the chip, for example. But anyway, so right off the bat there, that looks like a very good contender. It's almost too much of a coincidence.

**Dave Jones:** So if it's not this one, it could certainly be a Hikon-Tec. It really points towards Hikon-Tec being the manufacturer of this chipset. And do we have any other evidence? Well, operation voltage from 2.4 to 3.6 volts, perfect for operation of a couple of AAA, two AAAs like we've got in here.

**Dave Jones:** 6K Word one-time programmable program memory with 256 bytes of data memory. That's more than enough. I know for a fact that this is an OTP or one-time programmable micro, because they just actually upgraded the firmware on it, fixed a bug, and they can't rewrite them, hence the name one-time programmable.

**Dave Jones:** So once you program them, bingo, if you want to upgrade the firmware, you can't do it. You've got to scrap all those chips or ship them with the old firmware. Only blank ones can you actually program that. And also 6K Word's limited. When they were doing the development of this thing,

**Dave Jones:** when I was talking with them, I didn't really help with the development of this, but they sent me an early, well, they sent me like early spec sheets and things like that while they were working on it. And I said, hey, you know, look, some of these modes are a bit limiting.

**Dave Jones:** Can you add these modes in? And then they came back and said, oh, we're not sure, because the firmware guys are saying that it's, you know, there's not much room left in the firmware, but they did manage to squeeze it in. So, you know.

**Dave Jones:** And the operation mode, 4 MHz, bingo. We've got a 4 MHz crystal on here, but hey, that's pretty stock standard. Although chipset I'm working on at the moment uses 4.17 something or other. It uses an oddball value. So anyway, yeah, I wouldn't go by that.

**Dave Jones:** But it does have the UART module built in, but yeah, it's looking good. True RMS bandwidth, 1.5 kHz. I'm not sure of the specs, because the BM235 has true RMS, but it's only specced up to 440 Hz. It can go beyond that. But I do know for a fact that it does actually die and do weird stuff

**Dave Jones:** beyond 1.5 kHz or thereabouts. I think I measured it once, and it did do that. So it's stacking up pretty well. It's one of these puppies. Obviously the one without the inrush current and the peak hold, that seems to be the only difference between the two.

**Dave Jones:** Is it? Yep. I mean, so obviously they're saving some costs because there's no inrush current capability or peak hold. Hmm. And if you're wondering what sort of processor it's got in this thing, well, there you go. CPU HO8A, and it's got an 8 x 8 hardware multiplier.

**Dave Jones:** Oh, kicking some serious butt there. And if you go over to the page, actually, they've got some decent stuff here. They've got the development kit software. They've got the programmer for frequency calibration. Okay, they've got the software for that. And user manuals and the hardware.

**Dave Jones:** User manual, performance test tool. All sorts of jazzy stuff. I might have to have a play with the hex loader for the programmer. You've got to physically have the programmer, though. And here we go, the HO8A instruction set manual. So that's actually a...

**Dave Jones:** I believe it's like their own variation of some architecture. And they've got the compiler here and the configurations and all sorts of stuff. So here you go. There's the instruction set. So they've got their own processor. Go figure. But it's all there. There you go.

**Dave Jones:** Add C. Is it familiar to anyone? Add L. There you go. Is it a rip-off of the HO8? Hmm. By the way, this configurations document that you can get here, it's brilliant. Check it out. Look, it's got all the different configurations, the switching configurations.

**Dave Jones:** It shows you the signal flow for each particular mode. Look at that. So in 500 millivolt DC volt mode, that's how it flows. This is how it uses the delta sigma ADC. Bingo, which registers you turn on. All sorts of stuff. Incredibly comprehensive.

**Dave Jones:** And this is not proprietary stuff. You can just go to their website and download this. It's fantastic. As I said, if you want to actually see the architecture inside a multimeter chipset, there's no better way to do it than this. It's absolutely fantastic.

**Dave Jones:** Look how comprehensive that is. Jeez, they go into town. Add some waveforms there. Wow. Brilliant. There we go. Is that the capacitance? Yep, that's the capacitance mode. Telling you exactly how it does it. Anyway, check it out. I'll link it in down below.

**Dave Jones:** It's awesome. Great bedtime reading. So although this is looking really good, the sticking point here is these two COM terminals over here. Now, look, there's a... That looks like a ground... Well, no, that's going to the positive side of this tantalum cap here.

**Dave Jones:** So that is supposed to be the COM0 pin. Yeah, that's supposed to... That's pin 58. It's supposed to be COM0. There's no alternate function for that. So whether or not we've, A, got the wrong chip, although I'm reasonably confident at this point it is a Hikon-Tec of some sort,

**Dave Jones:** but whether or not we've got the wrong chip or whether or not they've ordered a custom variant of this chip, I don't know, and they actually removed all the LCD functionality, but they checked and kept all the pin-out and everything the same and maybe just changed a few of the functions there.

**Dave Jones:** I... yeah, I don't know. Anyway, we're close, but still no cigar. Just the smell of a cigar. Hmm. Now once again, if we have a look here, you'll notice that the negative of this tantalum cap, okay, this is our big ground here, or some ground,

**Dave Jones:** goes... that's actually pin 55 there. Okay, that's pin 55. And pin 55 here is RSTVPP. So it's Reset IC or EEPROM Rewrite Voltage Source. So it's not quite making sense. Anyway, pin 54 is VSS, i.e. ground. And sure enough, the one next to it, 54,

**Dave Jones:** that also looks like it goes to the negative side of these caps. So that could be ground, but something else is happening there. In fact, it even says VSS. There it is. Digital VSS 1. So that's the correct pin. So pin 54 is correct.

**Dave Jones:** Not entirely sure what's happening with pin 55 here, but yeah, we're doing reasonably well. Look, and then charge pump capacitor port, pins 52 and 53 here, so we expect to see a capacitor on there. What do we do? Yep, we find a capacitor, C15 there.

**Dave Jones:** Bingo, we've got a charge pump. And then, what is it? Charge pump voltage source 51. Yep, there we go. That comes from the positive side of that tantalum, so that could be the charge pump voltage source. And then the next pin in there,

**Dave Jones:** analog circuit voltage source. Bingo, so pin 50. Okay, so the second pin across, what do we get? We expect that to be VDD analog, the analog circuit voltage source. So you expect to see some sort of star grounding point, because all, you know,

**Dave Jones:** star grounding's gonna matter in something like this. So let's follow the money. Here we go, pin 50 going across. Sorry, I should make my cursor bigger, but hopefully you can see that. And bingo, what do we get? Star grounding point. There's a point here.

**Dave Jones:** The ground runs off here, and it runs off down through a via there, going, buggering off to somewhere else. It runs over to C16 here. So that's exactly what we expect. So it's all matching up. These two comports down here don't match up.

**Dave Jones:** They could be going off doing something else. Maybe the internal micro can program them to do something else, perhaps. Anyway, yeah, those pins are matching up. So I'm really liking this. And if we keep going here, let's go 48 is analog ground. Yep, that looks like a ground.

**Dave Jones:** Going through there to pin 48. Pin 47 is a reference voltage port. Okay, that's going off to a... Yep, there we go. That's going off to a capacitor there. Okay, no worries. I'm happy with that. And then PA0, that's the switch of the analog network.

**Dave Jones:** Okay, so pins 46 through to 40 are... Well, no, actually all going up here are all part of the analog network. And bingo, this is... Look, all these resistors and caps here, that's all part of the analog network. So that's exactly what you expect to see.

**Dave Jones:** So all those pins are matching up very nicely. If we have a look to see where our UART pins are, here we go, transmit and receive 20 and 21 here. So if we go over here, pins 17, 18, 19, 20, and 21. Okay, so they're buggering off down here somewhere,

**Dave Jones:** doing something. But they're also multipurpose pins, so there can be digital input, digital I.O., for example. Obviously, this meter does not have, as we saw in the previous video, does not have the RS232 serial output capability. So obviously, they've programmed the micro in here,

**Dave Jones:** if it is this one, programmed the micro not to have any serial output. It's obviously, it's going to be buggering off to the chipset. But they seem to be going down to some transistors down here, a couple of caps, I don't know. Something's, yeah, something's going on.

**Dave Jones:** But they have to have a serial interface going over to the LCD driver chip. And if we take a look at our LCD driver chip here, the Hikon-Tec part, it's an I2C interface. Bingo. So that's SCL, SDA. So we can find those pins on the,

**Dave Jones:** sorry, on the package here, LQFP48. That's the one where, what's the ABC versions? Oh, they're slightly different in terms of backlight and things like that. Anyway, we're looking at pins 9 and 10. There you go. Pins 9 and 10 there on all the packages.

**Dave Jones:** So we follow the money over to here, and we can have a look. Hopefully they're on the top. Pins 9 and 10. 1, 2, 3, 4, 5, 6, 7, 8, 9 and 10. Ugh, bugger. They're going off under there. Anyway, I could get the physical board and flip it over

**Dave Jones:** and try and see where those vias go. But we expect those, yeah, I'll go do that now, actually. I'll spare you the details. Right, so I've had a look at the physical board and the I2C pins under here, they go off to some vias up here,

**Dave Jones:** which then snake off over to these, which then go through these zero-ohm jumpers here. Yes, you can get zero-ohm resistors, and yes, they do have a tolerance on the datasheet. It's funny. Anyway, they go through here, and bingo, they go up to pins 17 and 18.

**Dave Jones:** What's pin 17 and 18? I hear you ask. Well, let's have a look. Digital input, output, and yeah, they're I0 pins. So, yep, it matches up. They could, although it doesn't say that this thing actually has I2C capability, they could be bit-banging the I2C port.

**Dave Jones:** It doesn't necessarily have to, micros don't have to have an I2C peripheral in them for you to use I2C. I've written my own I2C bit-banging routines before, and it's not that hard. It's pretty easy. You know, it doesn't, it takes, you know, tens of lines of code.

**Dave Jones:** It doesn't take much at all to implement an I2C interface. So it looks like they're the two pins, and there's probably pull-up resistors somewhere. Yeah, there's a via here, via there. It probably goes off to a pull-up resistor somewhere, because an I2C's got to have some pull-ups.

**Dave Jones:** And if we have a look at pins 15 and 16 here, where do they go? They go off to the crystal there. Bingo, and that's exactly their purpose in here. They have a digital I.O., so probably there's an internal oscillator in this thing

**Dave Jones:** if you want to use it, or output for the external oscillator. So it's all matching up pretty well. It's hard to fold it so far. So if we go back to the Hikon Tech page here, like, it's not going to be one of these

**Dave Jones:** mixed-signal microcontrollers, because it needs to have the multimeter functionality built in. There's no separate chip. It's definitely doing all the multimeter functionality in this chip, and the only two that they have here listed on their website, hey, yeah, granted, there could be others

**Dave Jones:** which haven't made it to the website, which we don't know about, subtle variations on parts or whatever, could certainly be one of those, but it's not the 3131 series here, because that one's like a high-end 50,000-count. You're not going to gild the lily

**Dave Jones:** and use that in a 6,000-count meter, price-sensitive 6,000-count meter. So it looks like it is the HY12P65-66 here. It's not going to be the others, 2,000-count, but they're obviously over-counting them here, but the way these dual-slope converters work inside these things, you can actually get a higher count out of them.

**Dave Jones:** So it looks like they are pushing it to 6,000-count, but why are they not using the internal LCD driver of this thing? They're using the external LCD chipset, not entirely sure at this stage. Maybe something will come to me, but anyway, they are definitely doing it.

**Dave Jones:** They could have, I think, could have got away with that chipset, but there's probably some technical reason why they're using the second chipset there, but anyway, that's interesting. That is almost certainly a HY12P66, I'd say. Best guess. I'll tell you what, these two chips over here,

**Dave Jones:** U4 and U5 look interesting. Look, 8-pin SOs, and you'll notice that these four pins over here, these four are all tied together like this. It's almost as if they're like an addressable, they're addressable pins set in address. This one has three pins tied,

**Dave Jones:** the other one's buggering off somewhere else. So that makes me think that these are I2C devices. So actually, one of those has got to be ground, so probably ground and power here like this, because that's going to a bypass cap. So power pin here, ground over here.

**Dave Jones:** So they're going to have three addressable pins here, so that'll give you eight addresses for the I2C. And then you've got your ground over here. These look like your digital address pins, but then you've got to have your I2C pins as well. So they're going to take two pins,

**Dave Jones:** and it makes sense that it's I2C, because look, if this is the power pin here, pin 8, then, because it's going to the bypass cap, then this is going to the top side of a 10k resistor here, 103, 10k, very typical I2C pull-up resistor value.

**Dave Jones:** So that is potentially an I2C pin, but in that case, it doesn't leave much left for your enough pins left. Right, back to the data sheet. This does not have E2P built in. It needs it because this multimeter is actually quite smart. It will remember the last mode that you put it in.

**Dave Jones:** If you leave it in DC volts mode, for example, it'll go back to DC volts mode. If you leave it in capacitance mode instead of diode mode, it'll go back there when you turn the meter off. So it's obviously storing that in E2P,

**Dave Jones:** and this thing, if it is this chip, which we think it is, it does not have any E2P in it. So, which is also why, if you go back to the, oh, go back here, ta-da! 2402. Look at that. External E2P. So that could be the best guess for those,

**Dave Jones:** but why you would need two? Because this thing does not do data logging at all. So it's not like it needs to store, you know, a lot of stuff. So why you would have two E2P chips, I don't know. Strange. Bingo, I found it.

**Dave Jones:** It's a Roam E2P. Sure enough, look, here's the product name marking from the data sheet. It's the BR24L. That's why it's only got LO2 on here, and sure enough, the LO2 is the product marking for the SOP8 package. Bingo! There we go. So it's a 2SK E2P.

**Dave Jones:** Why they've got two of them? I've got no idea. Anyway, yeah, I2C interface. I was right about the I2C interface. If we go down and have a look at the pinout, bingo, there it is. I was right. Power, ground, three address pins, and that is your,

**Dave Jones:** well, that's your write protect, and then your I2C lines there, but yeah, it's got 4K of E2P. Why? I mean, I don't get it. And of course you need an E2P to hold the calibration data in there, but that still doesn't explain two chips.

**Dave Jones:** I mean, 2K is plenty to hold the calibration data, one would suspect, and then hold the mode, the last mode it was in. Geez, you know, if you couldn't do that in a single byte, then I don't think you were trying. So that is just, yeah, strange that they've used two.

**Dave Jones:** I thought this was a real cost-cutting multimeter in terms of like Breiman one. They were trying to get the cost down, but no, they went for the extra BOM item there, so that is rather unusual. You know, I also suspect that they've gone overboard

**Dave Jones:** on the tantalum caps. One, two, three, four, five, six, seven, eight. That big one there, the big yellow one there, that'd be for the battery, and there's another one down there, that'd be for the LCD. Okay, fair enough. Yeah, maybe gone a bit overboard.

**Dave Jones:** These transistors here are obviously to drive the buzzer here, and that's about all she wrote. Hmm. And if you are curious about the other chipsets, the Cirrus Tech, for example, you go in here for the 6,000-count DMM, no, they're 100-pin quad flat packs.

**Dave Jones:** Maybe they might have used those in 128. They do no 64s. So whether or not, you know, they used that in maybe the 257, I don't know. They might have changed to a Hikon Tech. Perhaps. I don't know. But yeah, 6,000-count auto range DMM.

**Dave Jones:** There doesn't seem to be like, you know, 128-pin. No, there's just, no, it's nothing. Just takes you to there. So looks like peak inrush, dual display. We don't have dual display, so it's not going to be that. 50,000-count. Yeah, they could have, with cap, for example,

**Dave Jones:** 128-pin quad flat pack. Definitely not that. And as far as the Fortune semiconductor ones go, well, they, handy package guide here, they do have a 64-pin quad flat pack, but that's only for the 2,000-count one there, which doesn't even do capacitance and everything else.

**Dave Jones:** So it's definitely not that. So there you go. So there you go. Almost certainly, this is the HY12P65-66. Or, I wouldn't rule out some custom variant of it for Breiman. I would not rule that out, but it looks like, yeah, it's an off-the-shelf thing.

**Dave Jones:** They've reprogrammed it. They've decided not to use the built-in LCD drivers. Don't know why. Even though I think it might have enough segments to actually do it. But anyway, I hope you found that an interesting little look inside the Breiman BM230 series, and some unusual choices in there.

**Dave Jones:** Certainly not unusual to use a high-con tech chipset, but separate LCD driver, two e-squared PROMs? I don't know. Anyway, discuss down below. Go for it. Oh, and I'm sure people will ask, you know, can this be hacked to do other things and things like that?

**Dave Jones:** I don't think so, because it's an OTP part. It's a one-time program. It's not like you can get in there, get the tool, and then reprogram it to, you know, repurpose it to do something else. It looks like they've repurposed the UART lines, for example.

**Dave Jones:** So you're not going to be getting serial data out of this puppy anytime soon. It's basically going via I2C to the LCD driver. So if you wanted to actually get data out of this thing wirelessly, I guess you could actually make up your own little module

**Dave Jones:** to hack onto the I2C line, read the data coming out of that, because you will have the data format for the LCD. So what goes into the LCD, even though we don't have the data that's been outputted from the micro itself, it doesn't matter.

**Dave Jones:** It's got to match what the high-con tech I2C data sheet will say and what that chip is expecting. So in theory, you could read that, decode it, and, you know, send that out via Bluetooth or something else wirelessly if you wanted to hack something in that way.

**Dave Jones:** But apart from that, no, sorry, it's an OTP part. Bummer. And if you're wondering what this puppy is down here, this little jumper link J1, my hunch was correct. I did actually check. This goes over to the right protect pin of this E2 problem here.

**Dave Jones:** So this one, this lower one, U5, is almost certainly the calibration E2 problem. Maybe that's why they did it. Maybe that's why they're using two. They're just separating the calibration. In fact, bingo, it just occurred to me. Oh, hang on. Yes, the reason that they're using two is for robustness, okay?

**Dave Jones:** They're doing this for protection, basically. Physical protection so that you cannot erase the, regardless of, you know, some bug in the software, cannot erase the calibration settings of the meter. You've got to actually put that jumper on to enable the right pin, the physical right pin of U5 here, the E2 problem,

**Dave Jones:** that contains the calibration data, whereas the other E2 problem over here will be used for, like, the power on-off settings and things like that. It seems like if you're really penny-pinching every cent, you would have taken that risk that, okay, you're going to just not have this jumper,

**Dave Jones:** not have this calibration jumper here, and just rely on the fact that the software can just store in a different address for the power up and down. So, well, and I guess you don't want to lose your calibration data. These, how many writes on this thing?

**Dave Jones:** How many writes was it? I don't know, but I guess if you power on the meter 10 million times or whatever, surely it's got 40 years, oh, a million, okay. So I think your contacts would wear out on your switch before you powered this meter off and on a million times,

**Dave Jones:** assuming that they got it right in software, and they only, maybe they are actually writing to it every single time you change a range. That would be interesting. So if you're switching, for example, between the capacitance mode and the diode mode, or you're changing between AC and DC,

**Dave Jones:** maybe they're instantly writing that into that chip. So in theory, you could wear out the top E-squared problem here, U4, by, you know, pressing the button a million times or whatever, and you still wouldn't lose your calibration data. You would lose the ability for it to store the last mode you're in,

**Dave Jones:** but that's not a showstopper. Your meter would still work in a separate chip. So they decided just to physically separate that out. So that's a nice engineering design decision, and they didn't. Penny pinch there, that's really interesting. Maybe I could, like, set up a, like a button pusher,

**Dave Jones:** an automated button pusher that actually pressed the button on the, like, pressed, like, the AC, DC button. I should actually do a separate video to prove that. I won't do it now. I think I'll get the scope on there and actually see if it is actually writing to that chip.

**Dave Jones:** Aha. Will this be a second channel video or a part two? Anyway, whether or not it's doing that every time you press that button. Interesting. Anyway, this video's been way too long, so I'll save that for another one. Catch you next time. And a completely shameless plug, because I do flog this thing on my website,

**Dave Jones:** so if you do want an EEVblog BM-235 multimeter, go over to EEVblog.com and check it out. And if you enter as a bonus for watching this whole 40-minute waffle, if you do want one, put in the coupon code Waffle, all uppercase, and you'll get, I think, 20 bucks off.

**Dave Jones:** Bargain! For a limited time only. Hey, check this out. Look, amazing. Symmetrical multimeter stacking, just like the Philadelphia Mass Turbulence of 1984. Unbelievable. No human could stack multimeters like this. Hmm. Well, that's a few multimeters. 40, to be precise. I can't explain it, but there's something very therapeutic about doing this.

**Dave Jones:** Oh, yeah.
