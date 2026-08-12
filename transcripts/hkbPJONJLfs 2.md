---
video_id: hkbPJONJLfs
title: EEVblog #950 - Nixie Tube Display Project - Part 2
url: https://www.youtube.com/watch?v=hkbPJONJLfs
source: youtube-asr
timestamps: {"0": 1, "1": 16, "2": 34, "3": 54, "4": 64, "5": 81, "6": 90, "7": 108, "8": 121, "9": 155, "10": 170, "11": 185, "12": 203, "13": 217, "14": 229, "15": 242, "16": 253, "17": 270, "18": 288, "19": 295, "20": 312, "21": 321, "22": 338, "23": 348, "24": 361, "25": 381, "26": 408, "27": 423, "28": 441, "29": 454, "30": 471, "31": 483, "32": 500, "33": 515, "34": 528, "35": 538, "36": 552, "37": 560, "38": 572, "39": 580, "40": 592, "41": 613, "42": 624, "43": 634, "44": 644, "45": 657, "46": 669, "47": 690, "48": 707, "49": 728, "50": 741, "51": 751, "52": 767, "53": 783, "54": 805, "55": 814, "56": 830, "57": 842, "58": 855, "59": 865, "60": 875, "61": 887, "62": 897, "63": 912, "64": 922, "65": 941, "66": 950, "67": 960, "68": 979, "69": 993, "70": 1005, "71": 1016, "72": 1033, "73": 1042, "74": 1061, "75": 1072, "76": 1082, "77": 1100, "78": 1112, "79": 1127, "80": 1145, "81": 1156, "82": 1169}
---

**Dave Jones:** Hi, welcome to part two of my Nixie tube display driver project. Uh let's have another little look at just driving these Nixie tubes cuz there's a couple of issues outstanding before we actually go into a a final solution that we make into a schematic and a PCB.

**Dave Jones:** Now, the first issue is do you actually need a high voltage driver transistor here, be it within the like the custom microchip serial array that we looked at or individual uh driver transistors or a transistor array like a ULN2003?

**Dave Jones:** Do you actually need the full compliance voltage of 170 V or like say 200 V nominal to drive these things? Well, that's you know a reasonable question to ask and I actually um answered this in a separate video on my second EEVblog channel uh just an hour or two after uploading my previous video.

**Dave Jones:** So, those of my who are subscribed to my second channel and I highly recommend you do cuz occasionally I put updates and other uh miscellaneous videos like that. Um I'll link that in.

**Dave Jones:** But uh rather than just shoot that again, I'll just display that video here for you about the open circuit voltage drop of the Nixie tubes because some people have asked uh there will be a voltage drop on the Nixie tubes on the pins that you aren't actually switching on with your transistors.

**Dave Jones:** So, all the off pins will have so much of a voltage drop on via the Nixie uh tube itself that you can get away with low voltage uh transistors.

**Dave Jones:** Well, hey. We've got some Nixie tubes. Let's measure it. Um I'm powering the Nixie tube from 170 uh volts here through the 22 uh K resistor nominal that I was going to use and people wanted to know what is the open voltage on the other pins, i.e.

**Dave Jones:** when uh they're switched off by the uh driver. And can you actually get away with a lower voltage driver, etc.? Well, let's actually uh take one here and let's go around and measure 49 volts, 24 volts.

**Dave Jones:** Quite some variation. 43 Whoops. 122 Ouch. 118 69 40 47 123 odd. There you go. So, there is quite a significant voltage on there. So, 120 223 volts there on a couple of pins.

**Dave Jones:** Um That means that just for this particular Nixie tube, there's obviously great variation in this. So, I could go measure all eight. But, yeah, and you're probably not going to get this from any data sheet.

**Dave Jones:** So, that's the kind of open circuit voltage you need withstanding voltage, the voltage rating of your driver transistor or your driver, you know, transistor array or your whatever you're going to use to actually drive this thing.

**Dave Jones:** So, yeah, I'm afraid you can't get away with relying on the voltage drop of the Nixie tube itself. So, I hope that cleared that up. And by the way, if you're wondering what the voltage is when you strap all the pins together, tie them all together like this, well, you might have guessed.

**Dave Jones:** Let's have a look. Bingo. 125 odd volts. So, it basically ties it to the highest voltage drop or lowest voltage drop of any one of those particular segment display.

**Dave Jones:** I don't like using the word segment. One of those particular digits in there. So, as you saw there, we could get over 120 volts open circuit float voltage on some of those pins.

**Dave Jones:** Yes, some of them were quite low that you could use low voltage output drivers like a ULN 2003 or any other sort of like jelly bean low voltage driver transistor, but hey, some of them aren't.

**Dave Jones:** So, you know, we can go measure all the Nixie tubes, but hey, we've got a case where the tubes I've got in hand have up to like 120 volts and it could even be higher than that.

**Dave Jones:** So, obviously, we need driver transistors rated to that sort of voltage. But, as a few people pointed out, the classic uh 74141 driver chip, which is now obsolete, although yes, some people have pointed out that some company in Russia still manufactures it or something like that.

**Dave Jones:** I don't necessarily want to use that. I want to use a more modern readily available solution. Anyway, they pointed out that that 74141 is actually a fairly lowish voltage rating on those open collector output driver transistors in there, and fair enough.

**Dave Jones:** It's, you know, 50, 60, 70 volts, something like that. So, how can these things work? Well, if you have a look at the internal diagram for this thing, aha, look at the output pins.

**Dave Jones:** You can see that there's actually Zener diode clamps on the output. So, that's how they're getting away with it. So, what if we actually implemented a Zener diode clamping system on a more modern jelly bean driver that we have available?

**Dave Jones:** Well, the classic ULN 2003, you can do this, and we can actually use these to drive the Nixie tube displays, although there might be a potential issue, which we'll just verify here.

**Dave Jones:** Now, if you're not familiar with the ULN 2003, it's a an array of seven high voltage driver transistors. By high voltage, I mean 50 volts maximum rating. So, obviously, on their own, not good enough for driving our Nixie tubes.

**Dave Jones:** And inside each one is an open collector driver transistor, a high voltage type, but in this case, high voltage means 50 volts. 50 volt maximum rating, not good enough for our Nixie tubes on its own.

**Dave Jones:** But, if you have a look at the internal structure of these things, then they've also got a common diode array on all seven outputs like this tied together and then it goes to the common pin.

**Dave Jones:** So, aha, what we can do is we can then hook this up to our Zener diode clamp like that and bingo, we can clamp all of these pins. So, imagine this output here is driving our Nixie tube, it's going to one of the open pins on our Nixie tube here.

**Dave Jones:** Okay, and it's at 120 volts or whatever. This pin is at 120 volts, then we're going to it's going to be this diode here is going to be forward biased and then that is going to be clamped to a maximum, you know, let's say we used a, you know, a 48 volt Zener on there, you know, anything somewhere lower than our maximum 50 volt rating of our driver

**Dave Jones:** transistor, then obviously this pin here is going to be clamped at 48 volts plus the diode drop here, so 48.6, whatever. Still just call it the clamp voltage and Bob's your uncle, we're protecting that transistor.

**Dave Jones:** But, because they're all tied together common like this, all of the outputs are basically going to be tied to you know, the same maximum clamp voltage there. But, hey, this is a way that we can use the jelly bean ULN2003 cuz these things are as common as mud.

**Dave Jones:** And a few people have asked what I mean by a jelly bean component. Well, a jelly bean component is one that's super cheap, super available, usually, you know, almost by definition available from many different manufacturers.

**Dave Jones:** So, you know, 7400 series logic, 4000 series CMOS logic, Uh, you know, generic uh, you know, 741 op amps and uh, ones like this, the ULN2003. It's actually a series, the ULN uh, 2000 series drivers.

**Dave Jones:** There's different versions. There's a 2004 and whatnot. And they all have different uh, pros and cons. There's even like a low voltage drive uh, version than this that's specifically designed for, you know, 3.3 V logic input.

**Dave Jones:** But but the standard ULN2003 or 2003A available from, you know, countless different manufacturers for, you know, cents each or whatever. They uh, cost really cheap. Um, they can easily accept uh, 3 V input uh, or 3.3 V logic or 5 V logic.

**Dave Jones:** Not so great if you're driving hundreds of milliamps through the If you really want to turn them on hard, turn on this output transistor really hard, then, you know, the input uh, driving voltage can matter.

**Dave Jones:** But we're only talking about like a milliamp or two here. Not a problem. So, we can easily get away with uh, you know, CMOS TTL uh, type compatible 3.3 V and 5 V logic input uh, drive on this transistor.

**Dave Jones:** The basic difference between the different families in here is usually the uh, base resistor cuz they've got a base resistor built in and it's actually not just one transistor, it's actually a Darlington pair.

**Dave Jones:** So, it's actually uh, two transistors to give you extra gain there. But basically, the different families just have different value dropper resistors in there. But I mentioned a potential issue here and let's just have a quick look at it and do a quick measurement.

**Dave Jones:** Now, uh, let's assume that we've got our Nixie uh, driver here. We've got our 22K dropper resistor, got our 120 V supply up here. We've got one of the uh, transistors turned on here.

**Dave Jones:** So, one of the outputs of the ULN2003 is on. So, it's basically uh, because we've chosen 22K there, it's around about 2 milliamps um, that we're going to have flowing.

**Dave Jones:** But all these other ones are turned off. All these transistors are switched off and we've just got basically these forward biased diodes, hopefully depending on the voltage output here.

**Dave Jones:** If it's higher than uh the rated voltage of the Zener, then it's going to be forward voltage. If it's lower, as you saw the measurements before, some of them are, then hey, it's not going to it's going to be reverse biased.

**Dave Jones:** But some of these outputs are going to be up to, as we measured before, like 120 odd volts or something like that. So, we're going to actually get current flowing through the 22k resistor here through let's say this is 120 volts here, open circuit voltage, then that's going to flow through here down and be clamped by this 48 volt Zener diode.

**Dave Jones:** So, how much leakage current do we get total out of all these other pins um if we clamp this here? So, I'm just going to do a simple measurement here.

**Dave Jones:** Don't have a 48 volt Zener to hand, but hey, I'll just use like a 30 volt Zener. We'll just whack it in um and see what we get. So, let's give it a whirl.

**Dave Jones:** Okay, so what I've got here is I've got a digit turned on, digit zero, whatever, it's a random one. 170 volt supply up here. I've got my 22k dropper resistor.

**Dave Jones:** I'm measuring the current at about 1.6 milliamps through that 22k resistor. And what I've done is I've shorted all the other pins, all the other spare ones on the Nixie tube here, shorted those out.

**Dave Jones:** So, I've got that going through a 30 volt Zener here. The reason I'm shorting all of them together is sort of like a worst case thing because these uh diodes, because they're all going to a common terminal, could be doing that anyway.

**Dave Jones:** So, um I'm now going to whoop measure the There we go. 1.6 milliamps flowing through the 22k resistor. I'm going to measure the leakage current um through all the other pins shorted together and through with that 30 volt Zener clamp.

**Dave Jones:** So, here we go. Bingo, that didn't change. We're getting in about 0.33 milliamps, so 330 microamps leakage current shorting all the other pins together into a 30-V Zener. So, that's It's not a problem, and the Nixie tube is still working just fine.

**Dave Jones:** It makes absolutely no difference to the brightness whatsoever. So, looks like that solution will work a treat. Now, the other issue that I didn't really cover in the previous video about I looked at some of the Microchip serial driver chips, and some of them looked fairly ideal except they had totem pole outputs.

**Dave Jones:** And what a totem pole output is is an output that instead of just having an open collector like this one, i.e., the collector pin is just open, it's not connected to anything else inside the chip.

**Dave Jones:** Inside here, these are not open collector outputs. They're what's called a totem pole because they're got ones top and bottom, they look like an old Indian Indian totem pole.

**Dave Jones:** Anyway, something like that. It means that it's got a transistor which actively drives low and a transistor which actively pulls it high as well. So, it's often called a push-pull output driver totem pole, whatever.

**Dave Jones:** Now, there's an potential issue here, and it can be a major one. And so, we'll actually measure this and show why totem pole outputs aren't really suitable. We really need an open collector or open drain output like this.

**Dave Jones:** I've just drawn generic FETs in there, don't worry about that. They can be MOSFETs, they can be BJTs, whatever. Now, let's assume that we've got the 170-V supply, 22-k dropper, we've got our Nixie tube, we've got one of the segments, of course, turned on being driven low, but we've got all the other, you know, nine outputs here actually, you know, just floating, flapping around in the breeze.

**Dave Jones:** Now, if we're driving it with one of these microchip drivers that has a totem pole output, it's got a high HV pin on a high voltage active pin like that.

**Dave Jones:** So, surely you would put you would take that up to your 170 V supply. That's naturally where you'd put it. But, aha, will that cause a problem if this output transistor shorting on shorting all these other pins back up to the 170 V supply?

**Dave Jones:** I think we might come a gutser. So, I won't experiment with my good Nixie tubes. I remember that I had some that I think it was Fran, was it, who sent these into a very early mailbag?

**Dave Jones:** I've actually got three others. They're basically the same, the 12B type. So, I'll use one of these. These are look bendy soldered from boards. Obviously, they've still got the some of the pads left on there.

**Dave Jones:** Have they? Oops. Anyway, we'll try one of these because, you know, we don't want to damage one of our precious Nixie tubes that I'm going to use for my eight display solution.

**Dave Jones:** Okay, so what I've got here is the Nixie tube hooked up, 170 V supply, 22 K dropper resistor. I've got one of the segments turned on. It's segment zero again, not that it matters.

**Dave Jones:** Okay, what I'm going to do now is actually short one of the other outputs here well, Nixie tube pins to the 170 V supply and we're going to measure the current doing that.

**Dave Jones:** So, I've got my second current meter hooked up to the positive supply here. So, that's the on the top of the 22 K resistor there. So, right on the 170 V.

**Dave Jones:** So, let's hook on one of the other pins and I don't think it's going to be pleasant. Whoop. 9 mA. The current for the other one is through the 22 K resistor.

**Dave Jones:** Well, yeah, that's not very pretty. So, let's have a look at the display. What happens to it when we do that? So, we've got 1.5 mA at the moment.

**Dave Jones:** I'll turn on I'll connect one of the other pins. And yeah, the zero still lights up, but we're drawing like 8 9 milliamps, something like that. Oops. So, that's of course undesirable for the health of our Nixie tube and the reason why we can't use one of these totem pole output drivers.

**Dave Jones:** But hey, what if we hook the HV pin to the other side of the 22K resistor like that? So, we're basically only shorting out the pin. Well, we can try that, too.

**Dave Jones:** I'll just change that from here to here. All right, let's try that. Hook it up to a random pin and look at that. It's only 100 micro 80 microamps, something like that.

**Dave Jones:** It's very nice, as you'd expect. Um shorting out the any of the floating Nixie pins to the positive uh anode up there is no problems whatsoever. So, you could potentially hook that HV pin back up to on the other side of your dropper over here.

**Dave Jones:** But the problem with that is uh these, as you saw on the Microchip data sheet, these are high number of output drivers on the one chip. They're like 32 or 64 output drivers and you've got separate dropper resistors for each one of your Nixie tubes like this.

**Dave Jones:** So, you'd have to dedicate one chip to one Nixie tube like that to be able to tie that individual pin back. I wouldn't like to uh tie them across multiple Nixie tubes.

**Dave Jones:** You could probably get away with it, but I like just no. And of course, some of these driver chips also had a built-in uh current source as well down in here.

**Dave Jones:** You could actually a bias uh pin, a bias voltage that you didn't need the dropper resistor up here and that's another thing which maybe you could potentially use to get away with using a totem pole output driver, but you So, it's possible, but yeah, you've got traps like that.

**Dave Jones:** Just be careful how you hook it up, but anyway, I don't think I'm going to be using a totem pole output solution. So, there you go. That's just a couple of extra uh measurements there.

**Dave Jones:** I hope you uh enjoyed that. So, what I'm going to do is I think like I do like the Microchip uh driver solutions. They're really good, but some people have uh I'm not complaining, but they've, you know, um said, "Hey, wouldn't it be nice if you could just use a jelly bean solution that everyone can get in every country, etc., etc."

**Dave Jones:** Okay. Well, yeah. All right. Let's go instead of a discrete transistor solution. I don't like that. I think I'll actually implement the jelly bean ULN uh 2003 with a um suitably uh high voltage uh zener on the common pin.

**Dave Jones:** The only issue with this is that they come in, you know, packs of seven. Um you get seven drivers like this. So, yeah, it doesn't even drive one Nixie tube.

**Dave Jones:** So, you know, you've got to share drivers across multiple Nixies and uh stuff like that, but yeah, that's not really an issue. And also uh strapping uh the unused pins together like this to a uh in this case where, you know, a clamp voltage cuz we're going to we've measured like 125 V on here.

**Dave Jones:** So, we're definitely going to with all the pins uh shorted together, which they do with the diodes. So, um basically, we're applying what's called a pre-bias to all these pins.

**Dave Jones:** And um some designs do this actually deliberately. But one of the uh common reasons is that uh yeah, you can uh use lower voltage output uh driver transistors by applying this uh pre- bias uh clamp for in this case via uh diodes.

**Dave Jones:** And that's how some designs actually do it. They use discrete diodes as well. This uh pre-bias and they actually hook it up to a particular uh supply is to prevent some of the uh segments uh some of the digits from actually uh glowing due to leakage currents and stuff like that, but I, you know, it's not really an issue here.

**Dave Jones:** Sometimes like this will go away depending on if you put like a filter on uh front like a red filter or whatever, um orange filter on uh front of the uh particular display, but we're not too concerned about that.

**Dave Jones:** I mean, we're really getting into the nitty-gritty details of Nixie tubes and and particular variations between tubes and manufacturers and brands and all that sort of jazz, you know, it's Yeah.

**Dave Jones:** Anyway, this is often called a pre-bias as well, and that's kind of sort of what we're doing here.
